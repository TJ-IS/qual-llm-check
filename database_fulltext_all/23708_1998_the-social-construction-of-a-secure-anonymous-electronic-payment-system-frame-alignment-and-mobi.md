---
otero_id: 23708
otero_key: "F592XHW4"
title: "The social construction of a secure, anonymous electronic payment system: frame alignment and mobilization around Ecash"
authors: "David J Phillips"
year: "1998"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1998.6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The social construction of a secure, anonymous electronic payment system: frame alignment and mobilization around Ecash

DAVID J. PHILLIPS

Annenberg School for Communication, University of Pennsylvania, 3620 Walnut Street, Philadelphia, PA 19104-6220, USA

This paper examines public discourse in order to illuminate the processes by which issues of anonymity, surveillance, security, and privacy are integrated into public understandings of, and interactions with, consumer payment systems. Using theories of the social construction of technology, and Gamson's model of issue construction, it analyses the issue package deployed by the developer of the Ecash electronic payment system. An issue package is a set of framing devices which focus and constrain discussion of a particular issue. The paper then analyses three different discursive sites (print media, US Congressional deliberation, and an electronic mailing list) to gauge the success of that package, according to its presence and its resonance within each site. Using theories of frame alignment and social mobilization, the package is identified as a globalizing framing strategy. Its failure is explained by the difficulties a frame of such structure will have in meshing with the discursive practice of each site, in resonating with cultural themes of each site, and in provoking social action.

## Introduction

Technological artefacts are interpretively flexible (Pinch and Bijker, 1989). Understanding of their purpose, and the social contexts and ramifications of their use, is not fixed. Yet these understandings shape and guide the actions which incorporate the artefacts into social practice. Actors interested in structuring that practice may attempt to influence the social interpretation of the artefacts.

For example, consumer payment systems, like credit or debit cards, do not merely facilitate the purchase of goods. They are also instrumental in generating vast databases of transaction generated information. These databases are extremely valuable to business concerns and police agencies (Larson, 1992; Lyon, 1992; Gandy, 1993). Whether consumers understand the surveillance capacities of a payment system, and how they understand the role of surveillance in society, influences how they will create, modify, and interact with the sociotechnical structures which constitute that system.

Bijker uses the term ‘technological frame’ to refer to those ‘elements that influence the interaction within relevant social groups and lead to the attribution of meanings to technical artefacts’ (1995, p. 123). For example, elements of a technological frame may include goals, key problems, tacit knowledge, users’ practice, and exemplary artefacts. Entman describes framing as ‘select[ing] some aspects of a perceived reality and mak[ing] them more salient in a communicating text, in such a way as to promote a particular problem definition, causal interpretation, moral evaluation, and/or treatment recommendation. 'Frames' are manifested by the presence or absence of certain keywords, stock phrases, stereotyped images, sources of information, and sentences that provide thematically reinforcing clusters of facts or judgments' (Entman, 1993, p. 52). In Gamson's model, activist sponsors promote 'packages' for conducting discourse of a particular issue in particular sites. These packages consist of devices (such as metaphors, exemplars, consequences, and appeals to principle) which suggest a frame for viewing the issue, and hence offer a set of reasonable alternatives for action (Gamson, 1988).

This framing activity may occur in a variety of discursive sites, including popular mass media, specialized mass media, and elite deliberation. The success of these packages depends both on their structural fit with the institutional practices of the discursive site and their ‘cultural conduciveness’ and ‘resonance’ within that site (Gamson, 1988).

This paper examines public discourse in order to illuminate the processes by which issues of surveillance, identification, and privacy are integrated into public understandings of consumer payment systems. It first analyses the issue package deployed by the developer of such a system, then it analyses three different discursive sites to gauge the success of the package within each site. These sites include print media, US Congressional deliberation, and the cypherpunks electronic mailing list. The success of the package in each site is analysed according to whether or not the package elements occurred in the discourse, whether the themes of the package resonated within the discourse, and whether the package as a whole was opposed or accepted within the discourse. Finally, the paper uses frame alignment and social mobilization theory to explain the types of success or failure noticed in each site.

## The officially sponsored package

Ecash is an online consumer payment system invented by David Chaum and developed by his company, DigiCash, BV. The official package concerning this system was analysed to reveal framing devices used to represent the system in several sites. The texts deploying this package were all made publicly available by either David Chaum, the inventor of Ecash, or by his company, DigiCash. These texts include testimony before the US House of Representatives, a Scientific American article that was entered into the record at that House hearing, and pages from DigiCash's world wide web site. The pages selected from this site included introductory pages, a description of the Ecash technical protocols, and press releases announcing that Mark Twain Bank in the US and Merita Bank of Finland had begun issuing Ecash backed by national currencies. Citations for all of these sources are included as an appendix.

The analysis reconstructs the DigiCash issue package by a focused reading and interpretation of these texts. The first focus was on how the texts represented the mechanisms of the Ecash system – how it worked and what it was able to do. The second focus was on the representation of the social context of the development and use of Ecash. This included the social conditions which spurred, necessitated, or hampered its development, as well as potential uses of the system, and the ramifications and implications of those uses.

## How it works

Ecash implements electronic bank notes – unique digital messages which can be ‘withdrawn’ from a bank by a consumer, transferred by that consumer to a merchant, then redeemed by the merchant at the issuing bank. This is accomplished in such a way that the consumer need not be identified to the merchant or to the bank at the time of the transaction.

## Public key cryptography and blind signatures

Ecash is implemented using blind signature cryptography, which is in turn based on digital signatures. Digital signatures use a key pair, rather than a single key, to encrypt and decrypt messages. A private key is used to sign messages by encrypting them and another public key is used to decrypt and verify the message. A message signed with the private key can be verified only by means of the associated public key. The signer's private key is kept on her presumably secure computer system. The signer's public key is widely disseminated. So, if Alice wants to send a signed message to Bob, she transforms it using her private key. Upon receipt, Bob applies her public key to verify that it was she who sent it. Digital signatures can be used to create digital bank notes. Each denomination would be a message signed by the bank with a particular private key. 'All messages bearing one key might be worth a dollar, all those bearing a different key five dollars, and so on . . . These electronic bank -notes could be authenticated using the corresponding public key, which the bank has made a matter of record' (Chaum, 1992, p. 96).

To withdraw a dollar from the bank, Alice generates a random 100-digit number to serve as the note. She signs this number with her private key. The bank verifies her signature, then signs the note with the private key corresponding to the bank's one dollar denomination, and returns the signed note to Alice. They also debit her account by one dollar. To make a purchase with her digital note, Alice transfers it to Bob, who forwards the note to the bank. The bank verifies its signature, credits Bob's account, and sends him a digitally signed 'deposit slip'. Bob then sends the purchased goods to Alice.

This system provides security, in that no party can cheat any of the others. However, it provides no privacy. The bank can link buyer and seller by keeping track of who withdrew and deposited each note. Blind signatures restore privacy. Blind signatures may be analogized with embossed envelopes. Alice creates a bank note and hides it in a ‘digital envelope’. The bank embosses the envelope (and the note within it) with their ‘worth-one-dollar’ stamp, debits Alice’s account, and returns the embossed envelope to her. Alice removes the note from the envelope and spends it. The bank has never seen the note it has embossed, and so cannot link the use of that note to Alice.

In mathematical terms, Ecash implements blind signatures through a reversible cryptographic protocol. As in the unblinded process, Alice's computer generates a random number to serve as the note, but before she sends it to the bank, she multiplies it by a random blinding factor. When she receives the signed, blinded note back from the bank, she divides out the blinding factor. She is left with the original random number, on which the bank's signature remains. When Bob presents the note to the bank, it recognizes its signature, but not the note itself. It cannot identify the note that they issued to Alice as the note that they received from Bob.

Secure, anonymous electronic payment system

## Double spending prevention

Like all digital data, digital notes are easily copied. Therefore Ecash incorporates protection to ensure that each note is spent only once. In the current implementation, this protection is provided by on-line authorization of each payment. The bank maintains a database of every redeemed note. It checks the note it received from Bob against this database, and if it finds that it has already been redeemed, it informs Bob that the note is worthless, and Bob aborts the transaction with Alice. If the note has not been previously redeemed, it is added to the database. The bank informs Bob that the note is valid, and, according to Bob's preference, either returns new notes to him, or credits his account.

## Context and use of the system

## Ecash as a technological solution to a social problem

In this package, Ecash is explicitly presented as a 'privacy technology' which solves the problem of oppressive dossier creation (US Congress, 1995a, p. 8). These dossiers are useful to organizations as they try to prevent fraud and minimize risk, but in a trade-off for this organizational security, the individual becomes vulnerable to institutional scrutiny. The social risks of identification-based transaction systems are exacerbated by two social trends. First, more and more people are engaging in commercial transactions in cyberspace. Second, information transaction costs are dropping, making possible ever more finely grained surveillance practice.

Ecash permits organizations to prevent fraud and while also permitting individuals to protect their personal information. It enables ‘secure parity between individuals and organizations’ (Chaum, 1992, p. 101). Whereas identification-based payment systems would lead to ‘a centralized system with disenfranchized participants (like the electronically tagged animals in feedlots)’, Ecash (and other privacy technologies) would maintain the equivalent of, or improve upon, ‘our world today’, where ‘each participant is able to protect its own interests (like buyers and sellers on a town market square)’ (US Congress, 1995a, p. 8). At stake in this choice are ‘the core values we as a nation have fought for, and continue to stand for’ (US Congress, 1995a, p. 7).

## One-way anonymity prevents crime

The anonymity offered by Ecash is ‘one-way’ – the payee is identified to the bank during the transaction clearing process. Ecash banks are able to list the amounts of all payments received for all accounts. Moreover, the payer can, if she wishes, reveal the original note and the blinding factor to the bank, and so permit the bank to link the note they signed for her to the note they redeemed for the seller, producing an irrefutable receipt. In this way, acceptors of illicit payments (for example, extortionists, black marketeers, or acceptors of bribes) would be vulnerable to 'sting' operations.

## Consumer driven market demand

The texts mention that increasing public awareness of and demand for privacy technologies are working to stimulate Ecash's success. According to Digicash package, people are becoming more concerned with the privacy of computerized data, and because of DigiCash's presence in the media, they are also realizing that 'electronic payments need not mean an obliteration of privacy' (US Congress, 1995a, p. 9). As consumers become aware of alternatives, the global Internet provides unprecedented mobility to choose among them. Government, then, has two tasks to perform. First, they should encourage, rather than stifle, new developments in privacy technology. Second, they should establish confidence in these technologies by protecting against systemic risk since this role should not be left to 'the micro-economic interests of commercial organizations' (US Congress, 1995a, p. 7). If governments fail in their tasks of promoting and protecting privacy technologies, they will be left behind in global competition. If they succeed, they will see economic growth and market leadership.

## Summary

The DigiCash issue package constructs Ecash as a technology which empowers the individual with respect to organizations in the face of ever more fine-grained surveillance techniques, and leaves intact the existing police and regulatory controls over the monetary system which protect society's interests.

Essential to the cogency of this construction are two facets of anonymity and traceability. The first is payer anonymity. The payer anonymity afforded by Ecash will, according to Chaum, preserve the level of privacy that people enjoy now with cash. This level of privacy is not only traditional, expected, and desired, but it is essential for the maintenance of the core values of democratic participation and free markets. At the same time, the payee identification permitted by the system, in conjunction with nontransferability, will maintain or improve the current level of protection of 'society's interests'. Payee identifiability permits irrefutable incrimination of acceptors of extortion, bribes, or ransom, while nontransferability ensures that value can neither be accrued nor circulated without passing through financial institutions.

Because it empowers individuals vis-à-vis organizations, the adoption of Ecash will be driven by public demand and a robust market for electronic financial services.

This package is complex and cogent. The interests of individuals, central banks, and police agencies are each addressed and subsumed in a single technological solution.

Although the texts focus on different aspects of this construction, as a whole it is remarkably consistent across all of the texts. For example, the Congressional testimony stressed the social problems necessitating action as well as the solutions offered by Ecash, while the press release mentioned the solutions only, yet the solutions mentioned were the same in both cases. Not only were all of the texts consistent with each other, but, with few exceptions, all of the texts were equally available, and often referred to each other. There seems to be little attempt to play to different audiences, to offer different packages in different sites. There were only two exceptions to this. Chaum's comments during the question and answer period of the Subcommittee hearing were not available on the DigiCash web site, though his prepared statements were. The Ecash protocols, though they were posted on the DigiCash site, had no internal links on that site. To find them, one had to know their address, which was posted to the cypherpunks mailing list.

## Success of the officially sponsored package

This section examines the framing of Ecash in other discursive sites to judge how successful the official package was. The success of the package was judged by two criteria. Firstly, were the package elements evident in the discourse? Secondly, in what context did they appear? Were they embraced, opposed, or ignored? The selection of those sites, and of material within those sites, was guided in part by interviews with 17 actors involved in various ways in the development of electronic payment systems. They include the principal developers of three systems, adopters of those systems, coordinators and participants in electronic fora and physical conferences, lawyers, academics, reporters, and government officials. Their names and affiliations are included in the Appendix. Their answers to questions regarding the importance of various media for the discussion and deployment of new payment systems guided the choice of textual material for analysis.

Three sites were chosen for analysis – certain popular and industry publications, US Congressional hearings, and the cypherpunks electronic mailing list. Because each site had a unique discursive structure, the analytic method differed for each. However, each analysis was guided by the same goal – to discover and interpret the success of the DigiCash issue package. This package might be noted in shorthand as ‘privacy and security through one-way anonymity’.

## Press

A corpus of articles was generated by searching the CURNEWS file of NEWS library of NEXIS with the criteria 'HLEAD (DIGICASH) AND DATE > 2/28/95 AND DATE < 4/1/96'. Of these 71 articles, only those from certain publishers were retained for analysis. Those publishers were the American Bankers Association, The American Banker, Lafferty, Faulkner and Grey, and the Financial Times. These publications were chosen because interviewees mentioned that their coverage was important, good, or influential. National or international popular press reports were also retained, including articles in Popular Science, The Mail, PC-Computing, Newsweek, Business Week, The Times, and The New York Times. The final corpus consisted of 23 articles. Citations for these articles can be found in the Appendix.

The first analysis examined each article to determine whether or not it included the theme ‘privacy and security through one-way anonymity’. Each article was coded on how it described Ecash’s anonymity features. Description of anonymity features were classified either as no mention of anonymity, unmodified mention of anonymity, mention of payer anonymity, or mention of one-way anonymity (that is, payer anonymity with payee identification). Articles were then analysed to see how these anonymity features were conceptually linked to problems of privacy and security.

The analysis showed that only one of the 23 articles, an interview with David Chaum, echoes the complete official package – that privacy is a problem of organizational surveillance versus individual autonomy which Ecash solves by offering payer anonymity while providing organizational security and protection against criminality through payee identification. The other articles offer only fractured and partial representations of the package. Seven articles suggest that individual privacy is a social problem which Ecash solves, though they do not address security or criminality issues. Another seven articles mention Ecash's anonymity without placing it in any social context which includes a concern for consumer privacy. Eight articles mention neither anonymity, privacy, nor security. They represent Ecash as a resource or obstacle in various business strategies.

This analysis suggests that though fragments of DigiCash's official package appear with some frequency, rarely do those elements coalesce to form the powerful argument which is essential to the package.

The first analysis aimed only to get an idea of whether or not the official package appeared in the press. The second analysis was performed to gain a more nuanced understanding of the context in which those framing elements appeared. This was a detailed analysis of the overall representation of Ecash in three

Secure, anonymous electronic payment system

publications – The American Banker, Newsweek, and Business Week. The American Banker was chosen because interviewees often cited it for its excellent coverage. Newsweek and Business Week were chosen because theirs was the only national, mass market coverage.

The four American Banker articles all focused on the business environment of payment systems and the tactics of their developers. The only social issue that the systems addressed was the need for a secure network payment mechanism.

In the general press, Business Week and Newsweek both set the system in a wider social context, but the context is one of historically stable and foundational social institutions – banks and governments – collapsing in the face of networked anarchy. For example, Newsweek's title asks 'The End of Money?' while the subtitle answers 'Probably not'. Business Week is less ambivalent in this regard, talking repeatedly of social transformations on the scale of the Industrial Revolution. Each article mentions privacy rights as a social issue, and each presents Ecash as a solution to the issue, but in each, fear of currency collapse, counterfeiting, and institutional mayhem overshadow privacy issues.

In summary, these analyses show that although portions of the official package can be found in the press coverage, the package is usually fractured and its rhetorical power diminished. Ecash is likely to be addressed in the context of business strategies rather than social problems, and when a social context is presented, the possibility of catastrophic social reorganization is foregrounded.

## Congress

This section analyses transcripts of four sessions of the 'Future of Money' hearings before the Subcommittee on Domestic and International Monetary Policy of the Committee on Banking and Financial Services of the US House of Representatives. These hearings occurred between July 1995 and June 1996. Witnesses included representatives of 13 payment system developers, 8 government agencies, 5 banks or banking industry groups, 3 institutional adopters other than banks, and 2 policy experts. David Chaum testified before the Subcommittee on 25 July 1995.

The questions asked in this analysis are the same as in the analysis of press coverage. Was the official package evident? If so, in what thematic context did it appear, and was it embraced, opposed, or ignored?

First, the official package was fully available in this discourse. Chaum presented that package clearly and completely through his prepared statements, through supporting material entered into the record, and through his answers to Congresspersons' questions.

However, further analysis suggests that that package was not resonant; the themes of the package did not get much play in the discourse. Although privacy was recognized as a legitimate concern, Chaum's theme of the proper relation of privacy to security was not echoed, nor was Ecash ever recognized as a solution to privacy concerns.

Privacy was a prevalent concern for the witnesses, especially those from banking and credit card companies, who asserted that the success of Internet commerce depended on consumers' trust that their privacy would be protected. But their formulation equated privacy with security: each was defined as the prevention of unauthorized interception or modification of data. When data is protected against unauthorized interception, privacy is protected, too. The clearest example of this is found in the testimony of David Van Lear, the president of a transaction processing service owned by five bank holding companies, when he describes the privacy and security issues involved in various transaction mechanisms – 'As to privacy, [when] all [transaction] information is within a single bank [and therefore protected from interception], ... there is no major issue' (US Congress, 1995a, p. 65).

The most salient threat to this kind of privacy is from anonymous, unauthorized hackers, who 'hijack' proprietary information. This theme runs counter to the DigiCash theme that privacy is essentially a matter of power between individuals and organizations.

The DigiCash privacy theme was echoed more closely by Congresspersons, who recognized it not only as a consumer issue, but as a live political concern among human rights activists. By the final hearing, Representative Flake, the ranking Democrat on the committee, had incorporated privacy into his platform. Democrats, he said, 'will . . . have concerns about privacy issues . . . The new technology being developed has the capacity to track, among other things, consumer spending habits. The result is that the anonymity that some consumers enjoy with cash could disappear' (US Congress, 1996b, p. 54). However, privacy was still held in tension with security, especially with the perceived needs of law enforcement. This was especially apparent in Representative Castle's question: 'I guess it is relatively easy to do security [by identification and record-keeping], but in doing so you are asking individuals to give up their privacy . . . How do you deal with that . . . almost irreconcilable conflict?' . . . (US Congress, 1995b, p. 35). Also, Flake characterized the subcommittee's purpose as asking 'what sort of legislative or regulatory regime will govern privacy as we move to new payment products' (US Congress, 1996b, p. 54). No Congress person ever recognized Ecash, or any cryptographic protocol, as a solution which satisfied and alleviated that tension.

The cypherpunks electronic mailing list was a venue for discussion of cryptographic techniques, their applications, and their social implications. A large part of the discussion addressed financial cryptography and electronic commerce. A large part of that discussion addressed the Ecash system.

For this analysis, all articles that dealt with electronic commerce were saved over a period of ten months (June 1995 through March 1996). This resulted in a collection of 891 articles. These articles were then filtered for occurrences of the keywords 'Chaum', 'DigiCash', or 'Ecash'. This collection of 419 articles was analysed to reveal and reconstruct the meanings of Ecash among the participants of the mailing list.

Unlike articles in the press, where standards of objectivity and balance disguise persuasive technique and often result in a seemingly authorless discourse of declaratives, mailing list articles are grounded in the authors' subjectivities. The discourse is wide-ranging, conversational and multilogic – questions are raised and answered, debated, and raised again. Since readings are actively contested, it is easier to impute intended readings and readership activity. Although these contests also stand against a ground of unspoken and understood agreement, the discourse was not monolithic; many constructions were formed and argued. I represent here only the most predominant of them. Because the dynamics of this discourse is so much more complex and subtle than either the press or Congressional discourses, the analysis will also be more nuanced.

Cypherpunks is a public site in that anyone with access to e-mail can subscribe, read, or contribute. However, it often has the 'feel' of a private conversation. In balancing concerns for the privacy of cypherpunks participants with concerns for public accessibility of the source material for this research, I have followed the practice of Gurak (1997) by anonymizing the author, but citing accurately subject line, date, and time of the posting.

The DigiCash package was very much alive in this discourse. Participants displayed an eager grasp both of the underlying algorithms and of DigiCash's proclaimed reasons for adopting those algorithms. However, while the algorithms themselves were embraced, DigiCash's framing was rejected.

In cypherpunks, Ecash was understood as a particular application of blind signature cryptography. It was the cryptography, rather than Ecash per se, that was fundamentally important. Ecash as implemented was merely the current, not the last, best hope for realizing the possibilities of blind signatures. Among the most important of these possibilities was the creation of anonymous digital bearer certificates. These were understood as a tool in an ideological contest which set the power of established governmental structures against the rise of libertarian capitalism.

The effect of an anonymous system of digital bearer certificates was articulated at two levels. At a macro level, highly networked and anonymous systems of value transfer would facilitate a ‘geodesic’ economy: a global, fluctuating, and chaotic economic system resistant to monetary policy. Large scale applications would mediate ‘large, decentralized market[s] that [are] difficult for anyone to regulate’. (A\_\_\_\_, ‘Jump Start Ecash....’) In this scenario, Ecash might be used for payments between Internet service providers relaying voice phone calls. The relationships among these providers would be ephemeral and based not on trust or long term contracts, but on the good-on-its-face-value of the Ecash.

At a micro level, as economic activities become anonymous, consensual transactions become impervious to interference from governmental authorities, and strictures against victimless economic crimes become unenforceable. Electronic remailer systems, which would facilitate mutually anonymous communication, might be paid for with Ecash. Gambling operations might serve as Ecash money laundries, removing the flow of money from legal oversight.

The geodesic economy would have a counterpart in a geodesic state. 'Anonymity, e-cash, [and] black markets [would] usurp power of courts.... Business relations will be removed from the realm of violence and into the realm of mutually consensual, organizationally emergent social structures'. (B\_\_\_\_, 'Re: Mark Twain Bank'...) 'With the rise of alternate dispute resolution systems, the [judicial] system would move toward a system where law issues less from state authorities and more from private ones'. (C\_\_\_\_, 'Re: Anonymity and Intellectual Capital') In short, digital cash would 'drastically reduce and eventually eliminate the whole concept of "government"'. (D\_\_\_\_. 'Re: Still more...')

These were not necessarily implications of Ecash per se. They were implications of a cheap, popular system of digital bearer certificates. Ecash was not this system; it was merely the 'existence proof' of such a system. In particular, Ecash fell short of the ideal because it was neither transferable nor fully anonymous. Attempts to use and develop Ecash in ways which would provide these attributes were a significant focus of attention in cypherpunks.

Payee anonymity was considered essential to an ideal electronic cash system which would support and mediate an economic system impervious to governmental intervention. Much discussion took place regarding ways to use E-cash so that payees could

## Secure, anonymous electronic payment system

remain anonymous. One participant developed a transitive blinding scheme which would interact seamlessly and undetectably with the implemented Ecash system, yet would permit both payer and payee anonymity. In this scheme, the payee would create the coin or token, blind it and send it to the payer, who would blind it and send it to the bank. The bank's imprint would remain as first the payer, then the payee unblinded the coin. The coin redeemed by the payee would be unfamiliar both to the bank and to the payer. Mechanisms for coin transfer and exchange were debated, and some progress was made on implementing third party coin exchanges or chained, anonymous coin remailers. But, it was pointed out, coin exchanges are illegal under money laundering laws. However, if it is possible to transfer coins before redeeming them, they may be legally exchanged for goods. The market then becomes a money laundry. This scenario requires two things: transferable coins and places to spend them. So some participants on the cypherpunks list exhorted others to put shops on the net. One participant, working as a consultant for Mark Twain Bank, successfully urged the bank to temporarily reduce the fees for their merchant accounts. This rate reduction was publicized on the mailing list. The system, then, as presented and deployed by DigiCash, was supported by some cypherpunks participants in an effort to shape it to their own ends.

In summary, the official DigiCash package was very much alive in the cypherpunks site. Understanding of Ecash's algorithmic operation was appreciative, intimate, and nuanced. Likewise, the official DigiCash framing of the relation between Ecash, individuals, the state, and business organizations was fully recognized. However, that framing of social context was actively opposed, even when use of the system itself was supported.

## Summary

The DigiCash package experienced different levels of success in each of the three sites studied. The most meagre measure of success, the mere availability of the complete package within the site, was met in the Congressional hearings and in the cypherpunks mailing list, but not in the press. The package as a whole resonated only in the mailing list, it was echoed by no one in the hearings. Finally, even in the mailing list, it was not embraced, but opposed. The following section suggests that these differing levels of success may be explained by the rhetorical structure of the package itself, and by the institutional relationship of the package's sponsors to the discursive sites.

## Globalizing frames, alignment, and mobilization

## The DigiCash package as a globalizing frame alignment strategy

The DigiCash issue package explicitly mentions a strategy for Ecash adoption. Adoption will be driven not by institutional interests but by consumer demand. It will be driven by mobilized individuals. Therefore, in the analysis of the effectiveness of this package, I approach DigiCash as a social movement organization (SMO) and call on previous research investigating frame alignment, social movements, and mobilization.

Snow et al. define micromobilization as the 'range of interactive processes devised and employed by SMOs and their representative actors to mobilize or influence various target groups with respect to the pursuit of collective or common interests' (1986, p. 465, footnote). In part, this micromobilization occurs through frame alignment, the 'linkage or conjunction of individual and SMO interpretive frameworks' (p. 467). That is, frame alignment is an exercise in coordinating the frames of the SMO and of its target groups.

Snow et al. describes four modes of frame alignment, including frame amplification and frame transformation. Frame amplification is the clarification or invigoration of an existing frame. It may include the identification, idealization, or elevation of one or more values, or the amplification of the importance of presumed structural relationships. For example, amplification tactics may focus on, and attempt to make salient, the seriousness of an issue, the locus of blame for a problem, or the possibility of change and the necessity for action. Frame transformation is an attempt to create and nurture new values, and to redefine already meaningful activities and events. Frame amplification reinforces the frames of the target group, while frame transformation attempts to alter those frames.

By promoting the frame of ‘privacy with security through one way anonymity,’ DigiCash employed both amplification and transformation. By identifying problems both of privacy and security, it amplified two formerly isolated and contradictory frames. Through the concept of one way anonymity, it introduced a new, global, transforming frame through which to understand the relation of privacy and security, and the mediating power of Ecash in that relation. It is thus an attempt to induce social movement – to create, in Eyerman and Jamieson’s phrase, a new ‘cognitive praxis’, to open a new ‘cognitive territory, a new conceptual space that is filled by a dynamic interaction between different groups and organizations’ (1991, p. 55).

Any movement that seeks to destabilize existing social alignments is a challenger movement. Globalization, however, attempts both to challenge and to appease, to draw attention to the contradictions of segregated frames, showing that a solution here is a problem there, but then also to provide a master frame which encompasses and resolves those contradictions. This new, global frame will maintain and subsume core elements of many separate frames, and so maintain a certain stability.

## Criteria for success of framing strategies

Gamson suggests that a successful issue package must meet three conditions. Firstly, the rhetorical structure of the package and the manner of its deployment must be consistent with the organizational practices of the discursive site. This requires familiarity with and access to those discursive sites, as well as the ability to structure the package in such a manner that gatekeepers to those sites will accept it, and participants in those sites will listen to it. Secondly, the package themes must have cultural conduciveness and resonance among the social groups inhabiting the discursive site. It must also inoculate against counter themes that will inevitably be raised in opposition. Finally, the new frame must be compelling enough to spur mobilization (Gamson, 1988).

The failure of the DigiCash frame in the three sites studied demonstrates the difficulty a globalizing frame can be expected to have in meeting Gamson's conditions. Consider first the problem of access to discursive sites. Three facets of globalizing frames make it unlikely that the press will provide good vehicles for them. First, because they try to link a variety of hitherto disparate and conflicting ideas, globalizing frames are inherently complex, and so likely to be truncated or simplified in the course of routinized news production. Second, globalizing frames are inherently about harmonizing dissonant frames, whereas routine news production privileges and highlights conflict. Third, globalizing frames are inherently novel, and their supporters purport to stand outside any of the social groups which the new globalizing frame attempts to subsume. If those supporters are actually outside those groups, they may have difficulty getting news organizations to recognize them as legitimate spokespersons. Though novel material is likely to be deemed newsworthy, the outsider position of supporters of novel packages will likely result in the marginalization and trivialization of their presentation (Tuchman, 1978; Gans, 1980; Gitlin, 1980). These institutional practices of news production explain, in part, the truncated and sensationalized presentation of Ecash in the press.

The availability of the complete frame was not as problematic in the other sites. The formally democratic forum of Congressional deliberation ensured that, once invited, Chaum could present the DigiCash package in its entirety. In the cypherpunks list, gate-keeping was far less instrumental, and the reputation of Chaum and Ecash were sufficient to generate eager interest among the participants. Many of those participants were technically proficient. For them, the DigiCash issue package, embodied in the Ecash protocols, appeared in a familiar and comfortable form. A sense of collegiality prevailed in this forum, and so the proficient were willing to translate and elucidate those protocols. Moreover, cypherpunks is a forum for activists. This activism spurred participants to explore the issue package, its rationale, and its entailments in great depth.

A globalizing frame will also generally have difficulty meeting the second criteria. It must simultaneously resonate with and inoculate against diametrically opposed cultural themes. DigiCash attempts to attain this resonance by amplifying framing elements of both privacy and security, and to inoculate against intrusive surveillance and anonymous criminality by offering one-way anonymity. Yet in every discourse, amplification occurs without the simultaneous inoculation. Themes – such as the benefits of cash as an anonymous system, the necessity for tracing some financial transactions, the beneficial role of government as protector of law and order, and the necessity of privacy – are successfully amplified, but in each discourse, the counter-theme is awakened and not allayed. Harmonization, globalization, and transformation never occur, and no cognitive space is opened for social movement.

Evidently the third criteria is not met. The new global frame must be compelling enough within each social group to spur mobilization. Oppositional frames are 'collective action frames', they 'inspire and legitimate social movement activities', they underscore injustice, specify blame or causality, and suggest the means of resolution (Snow and Benford, 1992, pp. 137–8). In a globalizing tactic, the persuader must convince different groups of almost diametric types of injustice. Yet it must also be temperate and accommodating of the histories and concerns of all of those groups. In the case of Ecash, ardent anarcho-capitalists must be convinced of the injustice of tax evasion and bribery, while ardent defenders of the state must be convinced of the injustice of panoptic surveillance. While each may be willing to embrace half the package, neither is willing to embrace the whole. Meanwhile, those who just want to shop must be convinced that information imbalance is a social ill worthy of personal corrective action. This research suggests that privacy issues, especially in the context of consumerism, may be inadequate to instigate such mobilization.

Secure, anonymous electronic payment system

## Discussion and Conclusion

Globalizing transformation requires that an outsider mobilize the sentiments and actions of a variety of social groups in a variety of discursive sites. As such, it is an extraordinarily difficult strategy. The previous analysis suggested three intrinsic problems with the strategy. First, its proponents may have difficulty gaining reputable access to a variety of discursive sites. Second, they may fail to provide resonant themes in each site, or they may be may fail to inoculate against the counterthemes such resonance may awaken. Finally, a sense of accommodation may weaken the package's ability to spur mobilization.

Although these difficulties may seem to doom globalizing transformation as an effective tactic, there are certain factors which may yet lead to its success. First, not all power is discursive, and nondiscursive power may lead to discursive capitulation. For example, DigiCash holds the patents on blind signature technology, and may be able to use that power to coerce groups into coalition. If Ecash significantly reduces its issuer's costs, those issuers might be willing to accept one-way anonymity as an entailment of that cost reduction, and to promote it using their institutional resources.

Alternatively, practice may change so that privacy themes suddenly have salience. That is, Ecash may become the payment system of choice for mediating marginal practices – the purchase of online pornography, for example. Defence of this practice may never be articulated as such, yet it may strengthen the mobilization potential of privacy themes. The passage of the Video Rental Privacy Act, the strongest piece of US privacy legislation, might be understood as a defence of privacy rights in ancillary defence of pornography consumption.

Nevertheless, this research has suggested that effective use of a globalizing frame in an issue package is extremely difficult. It is perhaps effective only for actors whose institutional power extends over a variety of discursive sites, or in times when generally recognized social phenomenon bring into question the presumed opposition of established theme and counter-theme pairs.

## References

Bijker, W.E. (1995) Of Bicycles, Bakelites, and Bulbs: Toward a Theory of Sociotechnical Change (MIT Press, Cambridge, MA).

Chaum, D. (1992) Achieving electronic privacy. Scientific American, (August) 96–101.

Entman, R.M. (1993) Framing: toward clarification of a fractured paradigm. Journal of Communication, 43(4), 51–8.

Eyerman, R. and Jamison, A. (1991) Social Movements: A Cognitive Approach (Penn State University Press, University Park, PA).

Gamson, W.A. (1988) A constructionist approach to mass media and public opinion. \*Symbolic Interaction\*, 11(2), 161–74.

Gandy, O. (1993) Toward a political economy of personal information. Critical Studies in Mass Communication, 10(1), 70–97.

Gans, H.J. (1980) Deciding What's News: A Study of CBS Evening News, NBC Nightly News, Newsweek, and Time. (Vintage, New York).

Gitlin, T. (1980) The Whole World is Watching: Mass Media and the Making and Unmaking of the New Left (University of California Press, Berkeley).

Gurak, L. (1997) Persuasion and Privacy in Cyberspace: The Online Protests over Lotus MarketPlace and the Clipper Chip (Yale University Press, New Haven).

Larson, E. (1992) The Naked Consumer: How Our Private Lives Become Public Commodities (Penguin, New York).

Lyon, D. (1992) The new surveillance: electronic technologies and the maximum security society. Crime, Law, and Social Change, 18(1–2), 159–75.

Pinch, T. and Bijker, W. (1989) The social construction of facts and artifacts: or how the sociology of science and the sociology of technology might benefit each other, in The Social Construction of Technological Systems: New Directions in the Sociology and History of Technology, Bijker, W., Hughes, T. and Pinch, T. (eds) (MIT Press, Cambridge, MA), pp. 7–50.

Snow, D.A. and Benford, R.D. (1992) Master frames and cycles of protest, in Frontiers in Social Movement Theory, Morris, A.D. and Mueller, C.M. (eds) (Yale University Press, New Haven, CT).

Snow, D.A., Rochford, E.B., Worden, S.K. and Benford, R.D. (1986) Frame alignment processes, micromobilization and movement participation. American Sociological Review, 51 (4), 464–81.

Tuchman, G. (1978) Making News: A Study in the Construction of Reality (Free Press, New York).

## Appendix: data sources

## Official DigiCash package

An Introduction to Ecash http://www.digicash.com/publish/ecash\_intro/ecash\_intro.html. 19 March 1996. Also on file with author.

Cash on the Internet Now Has Become a Reality with Ecash http://www.digicash.com/publish/ecash\_intro/about.html. 19 March 1996. Also on file with author.

Ecash Frequently Asked Questions http://www.digicash.com/publish/ecash\_intro/faq.html. 19 March 1996. Also on file with author.

Ecash Protocol Version 1.2 http://www.digicash.com/ecash/protocol.html. 19 March 1996. Also on file with author.

First Bank to Launch Electronic http://www.digicash.com/publish/ec\_pres3.html. 19 March 1996. Also on file with author.

First European Electronic Cash Systems Opens for Business on the Internet http://www.digicash.com/publish/ec\_pres4.html. 19 March 1996. Also on file with author.

Money on the Internet http://www.digicash.com/publish/ecash\_intro/moneynet.html. 19 March 1996. Also on file with author.

Chaum, D. (1992) Achieving electronic privacy. Scientific American, (Aug) 96–101.

US Congress (1995a) House. Committee on Banking and Financial Services. Subcommittee on Domestic and International Monetary Policy. The Future of Money – Part 1. 104 Cong. 1 sess. 25 July. Serial No. 104–27.

## Press coverage

The American Banker (1996) A glimpse into the future of money, as Citi sees it, 23 February.

The American Banker (1996) A midwestern banker preaches gospel of electronic money, 16 February.

Popular Science (1998) Brave new electronic transactions; electronic cash, 248(3) (March).

CardFAX (1995) Different drummer, 17 July.

Retail Banker International (1995) Digicash goes live in US, 1 November.

Network News (1995) DigiCash signs its first E-Cash customer bank, 27 October.

The American Banker (1996) Digicash deal with Europe's top web server brings Ecash to Finnish Bank, 15 March.

CardFAX (1995) DigiCash signs up Mark Twain Bank to offer cash on-line, 30 October.

The American Banker (1995) Digicash to test live internet cash system with Mark Twain, 23 October.

ABA Banking Journal (1996) E-cash becomes reality, via Mark Twain and Digicash, January.

Mail on Sunday (1995) Electronic account that can fill your digital wallet, 12 November.

Electronic Payments International (1995) Leading the US charge for E-cash, August.

CardFAX (1995) MasterCard international expects to unveil an electronic program for transactions going over computer networks, 6 July.

The American Banker (1995) Money creators: a player goes after big bucks in cyberspace, 5 May.

Electronic Payments International (1995) Regulation key to electronic purse, August.

Bank Technology News (1995) Small bank makes big waves in electronic cash world, 1 December.

Electronic Payments International (1995) The banker's friend or foe?, December.

PC-Computing (1995) The check's on the web: Cyberspace and Digicash announce electronic cash services, 8(8) (August).

Newsweek (1995) The end of money?, 30 October.

Business Week (1995) The future of money, 12 June.

Credit Card Management (1995) The money changer, June 8(3).

The New York Times (1995) Today, shoppers on internet get access to electronic cash, 23 October.

Sunday Times (1996) Webwatch, 14 January.

## Congressional hearings

US Congress (1995a) House. Committee on Banking and Financial Services. Subcommittee on Domestic and International Monetary Policy. The Future of Money – Part 1. 104 Cong. 1 sess. 25 July, Serial No. 104–27.

US Congress (1995b) House. Committee on Banking and Financial Services. Subcommittee on Domestic and International Monetary Policy. The Future of Money – Part 2. 104 Cong. 1 sess. 11 October, Serial No. 104–27.

US Congress (1996b) House. Committee on Banking and Financial Services. Subcommittee on Domestic and International Monetary Policy. The Future of Money – Part 3. 104 Cong. 1 sess. 7 March, Serial No. 104–27.

US Congress (1996b) House. Committee on Banking and Financial Services. Subcommittee on Domestic and International Monetary Policy. The Future of Money – Part 4. 104 Cong. 1 sess. 11 June, Serial No. 104–27.

## Cypherpunks mailing list (partial listing only on quotes sources)

A\_\_\_\_. 'Jump Start ecash With iPhone'. Email to cypherpunks@toad.com. 5 Mar 1996 20:35:21.

B\_\_\_\_. 'Re: Mark Twain Bank (was: Anonymity: A Modest Proposal)'. Email to cypherpunks@toad.com. 25 Oct 1995 13:29:40.

C\_\_\_\_. 'Re: Anonymity and Intellectual Capital'. Email to cypherpunks@toad.com. 19 Nov 1995 11:47:01.

D\_\_\_\_. 'Re: Still more on the Digicash protocol'. Email to cypherpunks@toad.com. 07 Dec 1995 13:34:16.

## Interviewees and their affiliations at time of interview

Doug Barnes. Vice President of Sales and Marketing for c2.org, a service which administers Ecash servers.

Secure, anonymous electronic payment system

David Chaum. Chief Executive Officer of DigiCash, BV; inventor of the Ecash system.

Kawika Daguio. Government Relations Specialist for the American Bankers' Association.

Duncan Frissell. Off-shore banking consultant, cypher-punks participant.

Michael Froomkin. Associate Professor of Law, University of Miami School of Law; cypherpunks participant.

Ian Goldberg. Computer scientist, programmer, researcher and graduate student in cryptography at the University of California at Berkeley; cypherpunks participant.

Robert Hettinga. Founder of Digital Commerce Society of Boston, founder of e\$pam and e\$ mailing lists, cypherpunks participant.

Rafael Hirschfeld. Former technical director of the CAFE project, a European consortium of technical, academic, and industrial partners developing electronic purses based on Chaumian protocols.

Eric Hughes. Cofounder of cypherpunks mailing list; digital finance consultant.

Tim Jones. Managing Director of Retail Banking Services, NatWest; co-inventor of Mondex system; former Chief Executive of Mondex.

Bob Kaimen. Director of Cyberpayments Project of the Financial Crimes Enforcement Network (FinCEN) of the US Department of the Treasury.

Jeffrey Kutler. Executive Editor, The American Banker.

John Lopez. Counsel for Subcommittee on Domestic and International Monetary Policy of the Com-

mittee on Banking and Financial Services of the US House of Representatives.

David Nebhut. Economist in the Office of the Comptroller of the Currency, US Department of the Treasury.

Sholom Rosen. Vice President for Emerging Technologies, Citibank; inventor of Electronic Monetary System (EMS).

Frank Trotter. Senior Vice President and Director of International Markets Division, Mark Twain Bank.

Tom Vartanian. Partner in Fried, Frank, Harris, Schriver & Jacobson, a Washington law firm specializing in banking regulation.

## Biographical note

David J. Phillips is a Post Doctoral Fellow at the Annenberg School for Communication at the University of Pennsylvania, where he recently earned his PhD. His most recent publication is Crytography, Secrets and the Structuring of Trust in Technology and Privacy: The New Landscape, edited by Phil Agre and Marc Rotenberg (MIT Press).

Address for correspondence: Dr D.J. Phillips, Annenberg School of Communication, University of Pennsylvania, 3620 Walnut Street, Philadelphia, PA 19104-6220, USA. E-mail: djp@pobox.asc.upenn.edu
