---
otero_id: 10596
otero_key: "28EWPQA6"
title: "Barcodes, Rfids, Lemonade and Conversation"
authors: "Janis L Gogan; Ashok Rao"
year: "2010"
journal: "Journal of Information Technology"
doi: "10.1057/jit.2010.20"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Teaching case

# Barcodes, RFIDS, lemonade and conversation

Janis L Gogan<sup>1</sup>, Ashok Rao<sup>2</sup>

<sup>1</sup>Information and Process Management, Bentley University, Waltham, MA, USA;

<sup>2</sup>E. Philip Saunders College of Business, Rochester Institute of Technology, Rochester, NY, USA

Correspondence:

JL Gogan, Information and Process Management, Bentley University, 175 Forest Street, Waltham, MA 02452-4705, USA. Tel: þ 1 781 891 2098;

E-mail: jgogan@bentley.edu

## Abstract

Atul Mahajan nicknamed ‘AM,’ a wealthy Indian, sits on the board of Kisan Group, his family’s chemical company (family and company names disguised). Charged with managing the Mahajan family wealth, he has formed a private equity group that helps build mid-market companies. He has also launched a few technology-enabled ventures of his own, including a company that failed in its attempts to sell a service that used encrypted and masked barcodes for document authentication and a successful company that provided administrative and data management support for pharmaceutical clinical trials. Now, apparently with sufficient resources to contemplate another entrepreneurial venture, AM wonders whether to revive the document authentication business, with a turnkey solution or one or more services that would use encrypted RFID tags instead of the older barcode technology. This teaching case was developed based on interviews with Mr. ‘Mahajan’ and two other employees. The case provides an opportunity for students to investigate technical, strategic and operational uncertainties and challenges associated with building a business around a new technology. For business schools that are attempting to ‘globalize’ their curriculum, the case offers the benefit of presenting the point of view of a well-connected Indian entrepreneur.

Journal of Information Technology (2010) 25, 450–456. doi:10.1057/jit.2010.20

Published online 24 August 2010

Keywords: RFID; innovation; new product development; entrepreneurship

## Introduction

n January 2008 Atul Mahajan (known to friends as ‘AM’) stood quietly with several guests in the large living room of his newly renovated home in Pune, a city in the state of Maharashtra, India. The marble floor was cool underfoot, and a light breeze drifted in from an open window at one end of the room. Moments before, a young owl had flown in through this window, and the bird was surveying the scene from a high perch atop a contemporary sculpture in the corner of the room. AM was a follower of the Jain faith, which specifies that man is to live in harmony with other creatures and must not harm even a mosquito, much less a bird. ‘I’ll just cut the light,’ AM said in a soft voice, as he slowly raised his hand to flip the switch. Before Mahajan and his guests had a chance to adjust their eyes to the darkness, the owl spread its wings and flew back out the window, through the large garden, and into the night beyond. ‘Now, where were we, before that wise young fellow visited us?’ said AM, flipping the light back on and turning back to his visitors. ‘Oh, yes: paperwork problems and an RFID opportunity.’

## Background: Kisan Group and the Mahajan family

With about 3000 employees, the Kisan Group of companies (founded by AM’s grandfather) had several manufacturing facilities in India, which produced chemicals for uses in agriculture and other industries. Two of AM’s brothers oversaw operations. AM, who had earned an undergraduate degree in India and a Master’s degree in chemical engineering from Michigan State University, was active in India’s Family Business Forum, the Indian chapter of the Young President’s Association, and other business groups. He had worked for Kisan Group for more than 15 years and now sat on its board, but enjoyed business development more than managing day-to-day operations. When representing Kisan Group, he first concentrated on joint ventures with chemical companies and firms in related industries, and later he branched out into other areas. Now, most of his time was devoted to running a private equity firm, formed so as to diversify the Mahajan family’s holdings and participate in some rapidly growing sectors of the booming Indian economy.

‘I manage the family’s wealth,’ AM explained to a visitor, adding that other wealthy individuals also invested in his pool of funds. He clarified:

We are not too interested in start-ups; we prefer ventures at a mid-market stage, especially Indian companies that need growth capital to get to a higher level. Many Indian companies are eager to take over the manufacturing for American or European firms – after all, our operating costs are quite a bit lower here – but they need a little help to scale up for that work. We make an equity investment in the Indian firm, which uses the money to re-tool or increase its manufacturing capacity.

AM particularly favored companies in high growth businesses with strong customer demand. While he focused on the extended family’s investments and his private equity group, he occasionally invested his own personal funds in start-up ventures. For example, after solving a problem that Kisan Group faced in the late 1990s he privately funded a venture (described below), which subsequently led to the ‘RFID opportunity.’ Many business deals came together over sumptuous dinners in AM and Karishma Mahajan’s elegant home.

## Lemons or lemonade?

In August 1996 the Indian government passed the National Depository Act to modernize securities trading. Among other things, the Act eliminated the need for paper stock certificates and established a National Securities Depository (NSD) and (later) a second Central Securities Depository (CSD). Many observers proclaimed the start of a new era; rapid, accurate stock trades were expected to lead to a more vibrant capital market in India. Depositories would settle trades of ‘dematerialized’ (paperless or ‘de-matted’) securities. To sell some stock, a shareholder would need to open a ‘de-mat’ account at a bank authorized by NSD or CDS and submit the paper stock certificate to be de-matted (Figure 1 depicts a stock certificate for another Indian company, Orkay Silk Mills, Ltd).

By January 1998 dematerialization was compulsory for institutional investors; individual shareholders could hold their paper certificates, and sellers of up to 500 shares could use physical certificates, but since they would be charged an extra fee, it was expected that many people would ‘de-mat’ their shares.

At publicly traded companies, passage of the Act was greeted with some trepidation because despite many benefits it brought some short-term challenges. For example, Kisan Group’s chief financial officer reported that before shares could be de-matted, it would be necessary to confirm the authenticity and legitimacy of each paper certificate; that is, verify that a stock certificate had not been stolen or counterfeited. It was not uncommon for a shareholder to present stock certificates for sale, only to learn that a counterfeiter had already successfully traded a bogus copy containing the same certificate number. With passage of the Act, this problem would be magnified since many people would now bring in their certificates for dematerialization.

Thus, in the late 1990s Kisan Group had sought an orderly way to verify the authenticity and legitimacy of paper Kisan stock certificates. This was not a trivial task; there were about 50,000,000 outstanding shares of Kisan stock (held by about 200,000 shareholders). A task force charged with solving this problem contacted the Securities and Exchange Board of India (SEBI) for guidance. When SEBI did not respond, several Kisan Group managers visited the SEBI offices in person. ‘I felt it would make sense for SEBI to choose one solution (for all publicly held companies), rather than have every company invent its own,’ AM said. He and his colleagues were given a warm reception, but they got little satisfaction from the conversation. He recalled:

SEBI explained that while they look after shareholder interests, they did not have the authority to tell us what to do about it. They said, ‘We agree there is a problem here, but it’s your job to fix it. And, you’d better fix it.’ Now we had to take action.

After discussing many ideas the task force came up with a plan: Kisan Group would send each shareholder a registered letter, with instructions to affix a special medallion (on a sticky label) on all Kisan stock certificates in their possession. Thereafter, a certificate would be considered invalid unless this medallion was attached to it. The task force considered various ways to prevent the production of fake medallions: design a special rubber stamp, print labels with special ink, or embed microchips in them. While some solutions were adjudged too expensive and others too easy to circumvent, one proposal looked promising: add a barcode (like those used in supermarkets) to each medallion. Kisan factories already used barcodes for inventory control, but as criminals became more familiar with the technology this type of barcode might not provide sufficient protection for valuable stock certificates. A suggestion was made to print a masked barcode, using ink that can only be read with a special infrared scanner. Without this scanner, the human eye (or camera or copy machine) sees just a rectangular, black bar. By itself that was also judged to be not sufficiently secure, since thieves might obtain infrared scanners or figure out how to reproduce masked bar codes. So Kisan Group proposed to encrypt each bar code. An online article published by Microsoft<sup>1</sup> explains:

A secret key, which can be a number, a word, or just a string of random letters, is applied to the text of a message to change the content in a particular way. This might be as simple as shifting each letter by a number of places in the alphabet. As long as both sender and recipient know the secret key, they can encrypt and decrypt all messages that use that key.

![](/api/attachments/28EWPQA6/fulltext/images/b868f2f2ad602bfe47a4c86394c31381c06b64f0b6001edffb0514c924d95b23.jpg)  
Figure 1 Stock certificate, Orkay Silk Mills Ltd.

In a more advanced form of cryptography, text is translated into unintelligible gibberish (ciphertext) by using a mathematical algorithm which in turn is controlled by a ‘key’ consisting of a long stream of numbers. The longer the number, the stronger the encryption; thus 128- bit encryption is stronger than 64-bit encryption. In symmetric (secret key) encryption, the two parties share the same key. In asymmetric encryption two keys are generated: a confidential private key and a corresponding public key, which is freely available. Information is encrypted using the public key but can only be decrypted with its corresponding private key, which is created by the same algorithm.

Thus, if a criminal were to obtain an infrared scanner to read the bar code on an encrypted Kisan Group stock certificate medallion, unintelligible gibberish would appear; the stream of numbers were meaningless until the corresponding private key was applied to decrypt it. The private keys were held in a secure database (Figure 2).

![](/api/attachments/28EWPQA6/fulltext/images/161bb4dbf511d647495ac008d418c16ab712bc683a28d8af4e7f9b7de716b92d.jpg)  
Figure 2 Public-key encryption.

The integration of five elements – (1) software, (2) hardware (the barcode scanner), (3) the barcode symbology, (4) a database, and (5) the masked and encrypted barcode – provided strong protection at just 25 paise (about half a US cent) per medallion, according to its designer. Probably this solution would be patentable, but AM had recognized that the stock certificate application must be developed quickly, so he hadn’t worried too much about this aspect. To build it, various individuals with the necessary expertise, including a barcode expert, an encryption expert, and several programmers, were hired for reasonable wages,<sup>2</sup> thanks to an ample supply of programmers in Pune. Most of AM’s technical employees worked ‘in a box,’ with little visibility into the tasks being performed by others on the team. Mahajan believed this approach helped to strengthen the security of the final product. He also hired a security consultant to conduct several system audits. At first, the auditor found ways to compromise the system, but eventually he expressed the opinion that all elements worked correctly and that it was highly unlikely that the encryption could be deciphered without the private key. Now the Kisan Group Board of Directors approved this solution.

Once he had implemented the medallion solution for Kisan, AM had figured that he could sell it to other publicly held Indian companies, who faced the same problem of verifying that share certificates were authentic. Mahajan wasn’t certain about his pricing model, but two approaches had seemed feasible:

We could provide this as a service, charging a trivial amount per transaction: every time a share is handled a client would pay us less than a cent. That would add up to a lot of money if we serve many client companies, each with many certificates. Or, we could charge a large fixed fee for the service.

AM told colleagues that the stock certificate problem was not the only domain where this authentication solution could be applied: other valuable documents – such as passports, bills of lading, and deeds – could be secured with an encrypted and masked barcode.

Mahajan decided to invest his own funds to start a new business, AuthentiDox (India) Ltd, with Kisan Group as its first customer. He also planned to forge a partnership with a US company (one of whose founders AM had recently met) that performed similar services for the US securities industry.

Mahajan understood that he would not be able to sell a document-protection service without insurance coverage. So, he approached insurance companies to learn how to go about getting coverage. He was advised to make a presentation to representatives from Lloyd’s of London; if Lloyd’s agreed that the system was highly secure, it would be possible to get insurance. The presentation was successful, and once one insurance company signed on, several more followed. AM then was able to get an insurance policy from an Indian company (the Indian company took 5% of the risk and the rest was covered by various Lloyd’s of London members).

Now Mahajan urged his AuthentiDox (India) Ltd. sales team to sign up other publicly traded companies to buy the medallion service. He himself made many presentations to managers at other companies in an effort to drum up business. Unfortunately, however, the selling effort was a ‘dismal failure,’ in his own words. While many potential customers expressed mild interest in the service, not one customer signed up. AM had spent 60 lakhs (\$135,000) of his own funds on this project. Although he only recouped a portion of this investment by signing up Kisan Group as a customer, AM told close friends that he ‘did not lose much sleep’ over this one failure. Asked why he was not able to sell the solution to clients other than Kisan Group, he offered several ideas:

We ‘belled the cat’ by talking with SEBI, but some companies thought they didn’t need to take any special action. Perhaps they felt it would be less costly to deal individually with holders of disputed stock certificates. Or, maybe our timing was off; had we come forward with this solution a year earlier, perhaps we’d have gotten a better reception. I don’t know; maybe I underestimated the resources needed to effectively market this.

For the next several years AM focused on other investment opportunities. He founded a successful company that handled project-management and data-management aspects of pharmaceutical clinical trials, and his private equity group evaluated other investment opportunities for the Mahajan family’s money. AM took pride in thinking creatively about business opportunities. He described his philosophy, which blended his outgoing nature with a pragmatic consideration for how to pull deals together:

Money is important, but not as important as having a good idea and putting a deal together. Think of it like this: Do you want milk from the cow? Perhaps you need to give fertilizer to the farmer, so he can grow nice sweet grass for the cow to eat; then you’ll get your milk. Sometimes that’s what I do, to get a deal done. It’s fun, you know?

## Could RFID revive AuthentiDox (India)?

In January 2008 Mahajan was intrigued with a technology that had gotten a lot of press: RFID (Radio Frequency Identification). RFID had been around for several decades, but now was the ‘talk of the town’ thanks to dramatic performance improvements combined with declining production costs. An RFID system includes a small tag which stores a limited amount of data (usually on a 64- to 128-bit microchip) and a wireless reader. The tag can send simple messages (via a radio frequency transponder) to the reader. The least expensive ‘passive’ RFID tags store the least amount of data and are read-only (data on a tag is written once and can be read often). These passive tags do not require batteries; a reader’s electromagnetic signal transfers a sufficient amount of power to the RFID antenna (which converts the signal to alternating current) to permit the tag’s contents to be read. For this type of tag, the reader needs to be located less than two feet away. If produced in very high quantities, AM believed that passive tags would eventually cost as little as 5 cents apiece. Another type of reader can be located up to 30 feet away. Active RFID tags, which contain on-board batteries and more memory (as much as 1 MB) can be read at even longer ranges (up to 100 feet) and were much more expensive, at \$10 to \$50 apiece. In the United States many toll collection systems used this type of RFID system. Many active RFID tags have read/write capabilities (data can be replaced, or new data added to a tag). Some RFID tags can be read through liquids or under other difficult environmental conditions, and they can be scanned at rates as fast as 1000 per second.

In order to put RFID to work a company needs to invest in tags, readers, and middleware that receives data from tags (usually just an identification number), matches it with data contained in one or more files, and provides directions to one or more application software modules designed to use the data. For example, a hospital patient’s wristband might contain an RFID tag which stores the patient’s identification number. The reader receives that number, and the middleware matches it to data contained in a patient master file (such as patient name and address) and to other files containing clinical data such as medications prescribed for this patient and lab results. Before giving a patient a dose of medicine, a caregiver might be required to use the RFID system to verify the patient’s identity or check that this medicine was prescribed for this patient. The AuthentiDox (India) solution would require middleware to match the data on the RFID tag with data stored in a file of authorized medallion numbers.

The most common use of RFID technology was for inventory management in supply chains. Active tags were typically applied to crates, pallets or truckloads of inventory to facilitate shipping and other logistics operations. The US Department of Defense and Wal-Mart had made big RFID investments to reduce labor costs, theft and waste, and to improve product replenishment processes. It was expected that eventually RFID would replace barcodes in Kisan Group’s factories and logistics operations.

While use of RFID to track crates of products through the supply chain was widely accepted, privacy advocates expressed concern that some RFID applications involved unacceptable levels of surveillance. For example, RFIDequipped cars or trucks made it possible for managers to monitor the movements of mobile workers throughout the day; some workers objected to this. Concerns were also voiced about customer privacy. Some companies pilot tested the use of inexpensive passive RFID tags in individual items (apparel, Gillette razor blades, etc.). A shopper wearing an article of RFID-tagged clothing might thus unwittingly advertise the clothing’s brand and model to a retailer, who could react with a targeted sales pitch to that customer should she pass by a tag reader. Some critics viewed this as unacceptably intrusive. Apart from a wish to avoid negative publicity from being targeted by privacy advocates, other companies’ reluctance to use RFID was more straight-forward: they were already using inexpensive barcodes and did not yet see a strong rationale for investing in the more expensive RFID technology.

Atul Mahajan was interested in the idea of embedding passive encrypted RFID tags in paper. A rise in counterfeiting had led to proposals to embed RFID tags in the new Euro currency (Juels and Pappu, 2003). US officials tested RFID-embedded passports. In Japan, the Expo 2005 World’s Fair featured entrance tickets containing an RFID chip that was 0.06 mm thick. AM figured these applications were ‘the tip of a very large iceberg’ of opportunities to use RFID to authenticate valuable documents. He searched for news about recent RFID developments, with an eye to identifying if conditions were ripe for an RFID-based document protection service. Hitachi announced that it had created a prototype RFID chip that was just 0.005 mm thick – small enough to be embedded in letter paper. AM also found several reports that discussed the use of encrypted data on RFID tags. For example, one solution (Ateniese et al., 2005) proposed to encrypt tags in item-level applications so as to protect the privacy of consumers. A paper by researchers at the University of Adelaide and MIT (Ranasinghe et al., 2005) observed that existing encryption schemes did not as yet work well with the inexpensive tags currently used for item-level applications; however, their article ended on an upbeat note:

Cost effective and efficient hardware implementations y may involve finding ways to optimize and improve on existing cryptographic systems y taking into consideration the specialized nature of low cost RFID labels.

Another paper (Israsena, 2006) reported that ‘TEA’ (Tiny Encryption Algorithm) could be used, although a consensus had not yet been reached as to whether TEA would offer sufficiently strong protection for valuable documents. Computerworld quoted an expert who reported that RFID had not yet taken off at the levels that had been predicted a few years earlier (Gittlen, 2006). Thus, it was clear that while pallet- and case-level RFID applications were fairly well accepted, item level RFID (whether for articles of apparel, documents, or other items) was not quite ‘ready for prime time.’ Still, Mahajan believed that dropping tag prices and advances in encryption science might lead to a compelling business opportunity in the near future. One paper, by a team of Swiss researchers, really caught his eye; it called for the use of public key encryption on RFID tags as an anti-counterfeiting measure. The article stated (Staake et al., 2005: 1607):

Counterfeiting imposes a menace to industry worldwide. The International Chamber of Commerce estimates that seven percent of the world trade is in counterfeit goods, with the counterfeit market being worth \$350 billion in 2001 y RFID is a promising technology to fight counterfeiting.

Mahajan was scheduled to travel through Zurich in the coming year, and he made a mental note to arrange a meeting with the Swiss RFID researchers to learn more.

## Dinner at the Mahajans

At the dinner party which included the surprise visit from the owl, a servant passed around cups of lemonade (Jains do not drink alcohol). Friends chatted about the booming Indian economy<sup>3</sup> and awaited the arrival of one more guest, an Indian who had lived for many years in the US. He had phoned earlier to let AM know that he was making his way through traffic from a bank on the other side of Pune. A death in the family had brought this guest back to Pune, and his wife, who came ahead to the party, described the hurdles her husband faced as executor for his father’s estate. ‘What a hassle!

To close out bank accounts, he had to visit so many offices, and provide so many stamped copies of the death certificate and other documents. Various forms need to be filled out, and when a particular form is not available at a particular bank branch, he has to travel across town just to get the right form! To prove his identity, he even had to bring along witnesses who would vouch for him. Each transaction has entailed so many steps, and he is just getting started. I can only imagine the paperwork hassles he’ll face when we sell the car and the house.

‘Isn’t it just as bad in the US?’ said one guest. ‘There don’t seem to be as many manual steps involved, but actually, it is pretty bad there, as well,’ replied the woman. She added:

I was the executor for a friend’s estate, and that also involved a lot of paper shuffling. First the probate court needed to verify that I was holding the true, final version of my friend’s will; it took a few weeks to accomplish that. Then, before I could disburse any funds as directed in the will, the banks, pension funds and so on needed to see the original stamped probate court order, and in most cases I had to present these in person at each bank. Some banks also required that I provide them with a notarized copy for their files. I’m so accustomed to getting money out of ATM machines and paying bills over the Internet; all this running around seems hopelessly old fashioned!

## Mahajan took a sip of his lemonade before replying:

You know, about a decade ago I tried to turn a ‘lemon’ of a problem into ‘lemonade’ by selling a barcode document authentication solution. We got no takers at that time, so we dropped the idea. I see your tale of woe from the perspective of the banks, pension funds, and government offices that rely on the authenticity of many documents. It seems the problem is still very much with us.

A guest chimed in: ‘Certainly the bad guys don’t like authentication schemes; there’s a lot of money in fraud! For a few minutes the group swapped stories about highprofile criminals. A mobster named Abdul Karim Telgi had been convicted and sentenced to a 10-year prison term for his role in a highly publicized stamp-fraud case. Other recent news stories reported that individuals had impersonated a developer to obtain huge home loans by submitting fake real estate documents. One guest, who was trained as an engineer, found this discussion quite interesting. Observing that RFID costs were dropping quickly, he stated: ‘Perhaps the time has come to use RFID to authenticate documents. What do you think, AM: Is there a business opportunity here?’

Prompted by his friend, AM wondered anew whether it was time to revive AuthentiDox, but using encrypted RFID instead of encrypted barcodes. Besides using it to protect currency, stock certificates, and passports, he wondered: What other valuable documents could be profitably protected using RFID? Lloyd’s of London had specified that the medallion solution was sufficiently secure for the particular application of verifying stock certificates. Mahajan was confident that similar insurance could be obtained to protect other types of documents using encrypted RFID; however, since it was necessary to obtain insurance for each separate application, he would want to carefully consider the options before going forward. And, he was aware that there would be plenty of technical challenges.

AM believed that if respected scientists were predicting that a solution could be found, it would likely come true. So, he wanted to be ready to capitalize on the technology as soon as it was available. To that end, he wondered what could be done in the next year to evaluate market opportunities and match them with appropriate shortand long-term technology solutions for authenticating documents. Was RFID the answer to this problem?

The doorbell rang; the final guest had arrived and it was time to sit down for a delicious dinner and continued conversation. As he and Karishma ushered their guests into the dining room, Atul Mahajan silently resolved to give careful thought to the RFID opportunity the next day, and decide whether to launch a new document authentication service.

## Notes

1 ‘Description of Symmetric and Asymmetric Encryption,’ Revision 1.3, 26 October 2007. http://support.microsftcom/kb/ 246071.

2 At the time, the average salary for an Indian programmer was less than \$10,000. In 2007 the average salary was about \$12,000.

3 See for example Economic Survey of India 2007, Organization for Economic Co-operation and Development (OECD), 9 October 2007. www.oecd.org/eco/surveys/India.

## References

Ateniese, G., Camenisch, J. and de Medeiros, B. (2005). Untraceable RFID Tags via Insubvertible Encryption, in Proceedings of CCS’05 (Alexandria VA, 7-11 November): New York: ACM Press

Gittlen, S. (2006). The Failure of RFID, Computerworld Networking, 15 June. Israsena, P. (2006). Securing Ubiquitous and Low-cost RFID Using Tiny Israsena, P. (2006). Securing Ubiquitous and Low-cost RFID Using Tiny

Encryption Algorithm, in Proceedings of the 1st International Symposium on Wireless Pervasive Computing, Phuket, Thailand, (16–18 January); Piscataway, NJ: IEEE Press.

Juels, A. and Pappu, R. (2003). Squealing Euros: Privacy protection in RFIDenabled banknotes, in R. Wright (ed.) Financial Cryptography ’03, Berlin: Springer-Verlag, LNCS no. 2742, pp. 103–121.

Ranasinghe, D.C., Engles, D.W and Cole, P.H. (2005). Low-cost RFID Systems: Confronting security and privacy, Auto-ID Labs White Paper, SWNET-023, September.

Staake, T., Thiesse, F. and Fleish, E. (2005). Extending the EPC Network: The potential of RFID in anti-counterfeiting, in Proceedings of the ACM Symposium on Applied Computing (March 13–17, 2005, Santa Fe, NM) 1607–1611. New York: ACM Press.

## About the authors

Janis L Gogan holds EdM, MBA, and DBA degrees from Harvard University. A member of the Information and Process Management faculty at Bentley University she teaches IT management courses and conducts field-based research on inter-organizational information sharing under time pressure and IT-enabled innovation in health care. Dr. Gogan’s publications include teaching cases which have been taught in US, European, Australian and Asian schools, and 95 papers in refereed conference proceedings and journals (such as Communications of the Association for Information Systems, Electronic Markets, Government Information Quarterly, International Journal of Electronic Commerce, Journal of Management Information Systems, and The Information Society).

Ashok Rao graduated from the Indian Institute of Technology, Kharagpur (B.Tech, EE) and obtained his M.S. (EE) and Ph.D. (Industrial Engineering) degrees from the University of Iowa. In industry, he worked at Canada Packers and Leeds & Northrup, and was Director of business systems at Northern Telecom. A member of the Babson College faculty for 25 years, he was Professor of technology operations and information management and served as Chair of the division of management. His consulting and research interests include new product development, total quality management, computer integrated enterprises and management training. He is active in the Center for Quality Management and the American Production and Inventory Control Society (APICS). Since 2007, Dr. Rao is Dean of the E. Phillip Saunders College of Business, Rochester Institute of Technology.
