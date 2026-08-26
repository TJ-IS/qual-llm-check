---
otero_id: 18780
otero_key: "77K5WGVJ"
title: "Data processing aspects of the integrated circuit and magnetic stripe cards"
authors: "M.S. Madan; M.A. Reid"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90005-z"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Data processing aspects of the integrated circuit and magnetic stripe cards

M.S. Madan and M.A. Reid

Department of Computer Science, Monash University, Clayton, Vic. 3168, Australia

The IC card promises to extend the areas of application of the magnetic stripe card and also to improve the security of operation. There is great interest in its development, but the magnetic stripe card presently leads the field. Progress towards a change-over to an IC card will take time and there are various reasons for this view. In this paper some of these are examined in detail.

Keywords: IC card, IC, Data security, Magnetic stripe card, ATM, EFT, EFTPOS.

![](/api/attachments/77K5WGVJ/fulltext/images/60a0d52a627c11a7d3c85b015e99de51390982b9274b59cbb338d858b3bc9e0b.jpg)

M.A. Reid gained his B.Sc. degree in physics from the University of Glasgow, UK, and his Ph.D. in electrical engineering from the University of Edinburgh, UK He became involved in computing and programming through his work in geophysics, subsequently moving towards electronic engineering specifically the device and fabrication of microelectronics. He is currently with the Department of Electrical Engineering at the Chisholm Institute of Technology, Australia, and is doing postgraduate research work at Monash University, Australia. His interests are in the areas of data communications and microelectronics.

![](/api/attachments/77K5WGVJ/fulltext/images/09205348146d54e9dd2511a3edf510ee972ea938d45d031fc27bea738684f338.jpg)

M.S. Madan gained his M.A. from the Punjab University, India, and a Post Graduate Diploma from the University of London, UK. He joined the field of computing as a mathematician with GEC UK, working on scientific programming from there he moved to Bath University, UK, subsequently moving to work with BOAC/British Airways on their worldwide real time passenger services systems. He is currently with the Department of Computer Science, Monash University,

Australia. His interests are in the areas of data communications, local area networks and on-line business systems.

## 1. Introduction

The idea of a card that is small and easy to carry and that is able to store and process data has been discussed for many years. There are clearly many applications for such a card, ranging from simple token-style use, such as in the payment of transport fares or telephone calls, to the implementation of sophisticated financial and banking transactions. It is not surprising then, given the volume of business, that the latter area has been the one to experience the main impact of progress in the design of cards. In recent years, for example, this has brought about a quickening in the development of automated payment systems within commercial organisations. The most conspicuous occurrence here has been the development and use, mainly by banks, of the Automated Teller Machine (ATM), which allows the card to operate on an account in a direct debit mode. The essential element in these systems is the memory of the magnetic stripe card and the successful adoption of the ATM as a means of effecting such cash transactions. Although, in some quarters, the stripe card technology would be termed primitive, nevertheless it has brought credibility to the use of the card for general financial and cash transactions. The security is mainly achieved through the use of a Personal Identification Number (PIN) which functions as a password to the system. Of course, the level of security required is dictated by the nature of the application but in all cases the supplier and the user of the application want to be secure and there is a need to ensure that the communication channels are free from intrusion or surveillance, or both. An online mode of operation and the use of data encryption techniques are normally employed to ensure that this is the case.

New technological approaches towards achieving increase in application and operational security have brought about the development of the Integrated Circuit (IC) card. This is a plastic card that is of similar dimensions but containing a silicon integrated circuit chip that includes both a processor and memory within the body of the card. This permits the on-card processing of data including the use of data encryption techniques. Its development has the effect of creating a distributed processing network, rather than the conventional centralised system, that supplants the normally desirable feature of on-line operation as a means of ensuring good security. The outcome of this is the creation of a card that is intelligent in addition to being secure. Clearly, these extra on-card processing facilities open up new areas of application for card systems.

As we stand amidst these developments, a close examination of the capabilities of the magnetic stripe card, and its future, together with the oncoming IC card is appropriate.

## 2. Financial transaction cards

## 2.1. History of plastic cards

The first reference to the term ‘credit card’ occurred in the 1880's [14]. Earlier credit transactions were in the form of a ‘Letter of Credit’ issued by banks and ‘Revolving Credit Account’ by stores. The first credit cards were issued by a number of US state banks in the late 1940's, but the development of the industry was restricted to some extent owing to banking regulations of the time not allowing the use of the cards outside the State in which the issuing bank was licensed to operate. Subsequently, in 1950, the Diners Club charge card was introduced and this was the most significant step in the formation of today's massive plastic card business. Initially the card was of an embossed type and contained information, such as the issuer's and the customer's account number, in a raised set of characters so that the data could be translated by mechanical means to proprietary paper forms. By the end of the 1960's the magnetic stripe memory began to appear on cards along with the set of embossed characters. This dual feature is still provided and gives the card an additional flexibility in its use. The Diners Club card was designed with the intention of providing the holder with proof of credit worthiness when it was produced at any of the establishments that participated in the scheme, in this particular case at hotels and restaurants. This somewhat limited operation was greatly extended when the Bank of America introduced its Bank Americard throughout the United States and subsequently promoted it on a worldwide basis. This operation was eventually to lead to the formation of the present day VISA organisation. At the same time competing services were established and one of these, initially named Interbank, operates today under the name of Mastercard.

At first, these cards were targeted at the more mobile groups of people within the travel, business, and entertainment industries to whom the card was marketed, conferring an element of status on the holder. The card did have a practical value in that it filled a void for this group of people by providing a much needed credit facility. The mass use of cards by the public at large had to wait until the 1970's for both improvements and reductions in cost of electronic communications, accomplished by advances in microelectronic technology. This produced significant developments in computers, computer networks, and telecommunications on a country and worldwide basis. As a consequence, the use of cards has progressed from these early beginnings to the extent that the credit card bill in the US alone was about \$132.5 billion in 1989 [2] and an estimated 1 billion magnetic stripe cards were in circulation worldwide.

## 2.2. Cash versus cards

Much has been said about the emergence of a 'cashless society' in recent times. With it came the implication that the need and availability of cash would be decreasing. The seemingly large numbers of cards in circulation might tend to give the impression that this trend is occurring. However, the evidence available today does not completely support this view, and contrary to a noticeable decline in the usage of cash taking place, the opposite appears to be the case. The number of coins and banknotes available for each member of the population is on the increase in most countries. In fact, 80–90% of all transactions make use of coins and banknotes [4]. The majority of these is for small amounts of cash, and accounts for only about 3% of all transactions in terms of value. Most countries have embraced the idea of a cashless society and the development of card systems for financial transactions, and it is probably true that none has a greater commitment to this than France. Yet, the French anticipate that cards will account for only 5% of all financial transactions by 1991 indicating that a general move towards a displacement of cash by cards is likely to be slow. In fact, plastic cards themselves have conspired against a decline in the use of cash by making it readily available at any time of the day with the worldwide introduction of the automated teller machine (ATM). The main function of the ATMs today appears to be simply to dispense cash, since almost 80% of all ATM transactions are cash withdrawals.

Thus, the future is likely to see the further development of coin and banknote handling equipment in addition to an increasing use of plastic cards. These will generally find application in transactions of higher value, but as the appropriate technology evolves and the cost of that technology decreases more use will be made of cards for low value transactions. Nevertheless the commercial need for a transaction card has clearly been established by the ever increasing mobility of world's population, and its success has been achieved by the advances in microelectronic technology, which have led to a linking of computer and communication technologies.

## 3. The magnetic stripe card

## 3.1. Format of the magnetic stripe card

Magnetic memory stripes were added to the back of the conventional embossed card in the late 1960's. The main purpose was to provide for speedy and accurate entry by automatic means of identification data, which the card holder would otherwise have to key into a terminal, such as, for example, an ATM. Actually the magnetic stripe contains three separate tracks on which data may be recorded; Tracks 1 and 2 are read only tracks, whereas Track 3 provides for read or write or both [8]. Each of the three tracks has been assigned to a specific type of application. The technological concept of the magnetic stripes, viz., using a magnetic material in thin film form as a storage medium is familiar today to almost everyone through its application in the sound and vision entertainment industry. The basic structure of the magnetic stripe card is shown in Figure 1(a).

![](/api/attachments/77K5WGVJ/fulltext/images/942f907e6e0a24dc6487b30496343a1102ddd9c07d3b47f87e3af522bbbc2ed6.jpg)

(a)  
![](/api/attachments/77K5WGVJ/fulltext/images/92f0906c7ebed4b0cc7fb2a3261a015927bdf10a8da9ce26018fedbb53b4e2a3.jpg)  
(b)

## Track 1

This track was originally developed by the International Airlines Transport Association (IATA) purely for airline use, and a standard format was defined to facilitate the sale of tickets from vending machines. In more recent times, other bodies have become interested in using this track, as it is the only one to allow the encoding of the card holder's name. This would be a convenience when the name of the person has to be printed on a paper form or receipt and would avoid the necessity of retrieving it from some central computer. There are 26 different formats, each designated by a letter of the alphabet, for this track; it has a capacity of 79 characters.

## Track 2

The development of Track 2 was instigated by the American Bankers Association (ABA). It was driven by the need of the credit card companies for a standardised plastic card that could be used at point-of-sale (POS) terminals with a need for credit authorisation before completing the transaction. These terminals function in an on-line mode and, as a result, Track 2 has become the most extensively used encoding procedure for plastic cards; it is the only track used by Visa and Mastercard in their debit and credit applications. The capacity of the track is limited to 40 characters, which is considered by some to be a disadvantage, since it means that all relevant, data for a transaction has to be retrieved from a central computer.

## Track 3

This was developed for use in applications involving off-line Electronic Funds Transfer (EFT); the format of the track offers compatibility to both magnetic stripe and embossed cards. This track has a somewhat greater storage capacity, 107 characters, than the other two tracks, and because of this the various financial institutions have considered using it for on-line applications. Its contents are re-written each time it is used and it contains an encoded version of the PIN which is unique to each card holder.

All the three tracks are based on international standard ISO-7811. The general layout of the formats for the three tracks is shown in Figure 1(b).

## 3.2. Security aspects of the magnetic striped card

It was not until the early 1970s that thought was given to considering the application of electronic techniques to the process of transferring funds in the banking and commercial world. Until then it had been accomplished solely by the use of off-line paper systems; the outcome today is almost total consumer acceptance of credit and debit card systems.

It appears that the institutes employing these systems had enough financial benefits flowing to them to justify, continue, and advance their use. Initially, before a practical system could be set in place, the most pressing problem facing the designers was to provide a card based system that would be inherently secure. It had to instil the confidence in the users and operators. Clearly, the development of an EFT system could not progress otherwise. From this point of view there is a need for customer authentication and for ensuring the authenticity and integrity of a transaction. Much of the original research in the security area was undertaken by the Mastercard Company of the US. It was they who realized that the use of a secret Personal Identification Number (PIN) was a suitable technique for authentication of customers and that cryptographic methods using secret keys were necessary for transaction security. It is this combination of security features that is the foundation of the magnetic stripe card's success.

## 4. Data networks in the banking system

## 4.1. Electronic funds transfer

Retail banking customers in a society that is becoming increasingly mobile are now demanding service at any time of the day or night. In addition, the expectations of technology are such that the banks are under pressure to provide a response to a service request, or transaction, that is almost instantaneous, and also to arrange for the service to be provided throughout the community at multiple banking points with the minimum of inconvenience. This is achieved by means of a distributed network of service points. The implementation of such services by the banks can only be accomplished by what has come to be known as Electronic Funds Transfer (EFT). In reality this is merely the use of computers, usually connected by means of telecommunication lines to terminals or processors that control the outcome of a financial transaction. The EFT services presently available may generally be divided into three categories:

1. Automated teller machines (ATMs), which constitute by far the most dominant EFT service and which can be operated in a shared network between banks, essentially as cash dispensers;

2. Point-of-sale (POS) terminals, which are networked to link directly to a customer's bank account so that a customer's state of credit worthiness can be ascertained and the account debited accordingly;

3. Automated clearing houses (ACHs), which constitute the services and networks that are provided to other banks. By this means, large transaction volumes can be settled automatically, and accounts reconciled between financial institutions without the transfer of paper between offices. These are inter bank services and are regarded as being part of 'wholesale' banking.

Other services exist or are being developed, such as home banking and telephone bill paying, but as yet these have not yet reached a mature stage of operation. To some extent this may be attributed to the lack of communications facilities and equipment within the average home.

## 4.2. Automated teller machine networks

There are now approximately 200,000 ATMs installed throughout the world, and the services offered to customers include making withdrawals and deposits, with some limitations, retrieving information about an account and, in some cases, arranging for the payment of bills. A typical configuration for an ATM network is shown in Figure 3. Leased lines are generally used and remote ATMs are almost all multidropped on these lines [9,13].

![](/api/attachments/77K5WGVJ/fulltext/images/1ef61b6d0cbe2bfcd13479734bcb1a5d6a0ce4e6c8c288f8d228fc3b88514d1c.jpg)  
Fig. 2. Typical ATM configuration.

While the capital outlay required to establish an ATM network is quite large, the cost of handling a transaction manually far exceeds that of implementing it on an ATM, owing to the increasing costs of employing people. The overall expense of the ATM network can be reduced by institutions arranging to share the ATM installations and this has come to be regarded as an ideal arrangement, because maximum use is made of otherwise underutilized terminals and also because banks pay for only a portion of the total operating costs. The format of a typical shared ATM network is shown in Figure 2. In this configuration, leased lines are used to carry the transaction data in an on-line mode of operation and enable any transaction entered at any ATM in the network to be routed to the appropriate bank. The network contains a sophisticated switch that routes each transaction to the destination bank's data centre. In addition, the switch can handle transactions if any bank's data centre goes off-line by invoking software routines that are contained within the switch. Usually this occurs after some predetermined 'timeout' has elapsed without a response from the destination bank. These routines also impose restrictions on the number of times a customer can use the network in a day and on the amount of cash that may be withdrawn in some specified time. Clearly, a record of all transactions that occur in the off-line mode must be maintained and this also is the responsibility of the switch. The switch records copies of every transaction that occurs to provide a backup for auditing purposes. This front-end style of processing is typical of shared ATM networks and is sometimes termed as a 'negative' file mechanism.

## 4.3. Operation and security of ATMs

The ATMs rely entirely on the magnetic stripe plastic card for their operation; in particular Track 2 is used to store information required to initiate a transaction. The contents of the track are shown in Figure 4.

![](/api/attachments/77K5WGVJ/fulltext/images/fca73745b43082ec862d6a6480585d93ee24b29f3d1b9aa7fc9f113697c8c90f.jpg)  
Fig. 3. Shared ATM network.

<table><tr><td>Field Name</td><td>Length (characters)</td></tr><tr><td>Start sentinel</td><td>1</td></tr><tr><td>Primary Account Number</td><td>Up to 19</td></tr><tr><td>Separator (SEP)</td><td>1</td></tr><tr><td>Country Code</td><td>3</td></tr><tr><td>Expiration date or SEP</td><td>4 or 1</td></tr><tr><td>Discretionary Data</td><td>(the balance up to maximum record length)</td></tr><tr><td>End Sentinel</td><td>1</td></tr><tr><td>Longitudinal redundancy check (LRC)</td><td>1</td></tr><tr><td>MAXIMUM TOTAL</td><td>40</td></tr></table>

Fig. 4. Data held on Track 2.

The primary account number, sometimes referred to as PAN, consists of the following 19 digits:

<table><tr><td>Industry code for the issuer</td><td>1 digit</td></tr><tr><td>Issuer identification</td><td>5 digits</td></tr><tr><td>Customer identification number</td><td>12 digits</td></tr><tr><td>Check digit for customer account number</td><td>1 digit</td></tr></table>

Figure 4 shows clearly that the additional information relates mainly to the customer's name and the expiry date of the card. Obviously this information is readily available to anyone that handles the card. It remains unchanged throughout the life of the card and in this sense the card plays a passive role in the execution of a transaction.

A standard dialogue is set up between the ATM and the host computer during the execution of a transaction with the following steps:

1. An authorization request is made by the ATM to the host computer.

2. An authorization reply is made by the host computer to the ATM.

3. A transaction completion message is sent to the ATM to indicate that the data base has been updated.

When an authorization request is made to the host computer, the ATM will normally begin to count the timeout interval, which is typically of the order of 10 seconds. In the case where there is no reply from the host within the specified time, the ATM automatically sets in motion the procedures used for off-line operation. The outcome will be either to terminate the transaction or to authorize the completion of the transaction while arranging for a backup record to be made.

## 4.4. Security considerations for ATMs

Security has always been an area of general concern in the banking world, and as the processing of transactions has been placed in the public view with the introduction of ATM networks, the need for secure operation has become more acute. There are, as a result, some standard security measures that are applied to ATMs. One essential element is the magnetic stripe card and, although it can readily be forged, it has helped to create a workable ATM system that has been found to be remarkably secure. Actually the inherent security of the system relies entirely on the use of the PIN, the other essential element in the operation of an ATM system, which is similar to implementing a system of passwords. This satisfactory level of security has occurred despite the fact that the ATM has not generally operated in an on-line mode at all times. Some measure of the security of the system has come from an assessment of credit card fraud. As an example, it is maintained that the losses of Visa and Master Card have averaged about 1% of their total sales. Of this amount about 15% was card related fraud in 1982 which involved counterfeiting and alteration of the embossed lettering. These figures have gone some way to creating the confidence that presently exists in the system.

Security measures can generally be grouped into two specific areas: those concerned with protection of the network and those concerned with protection of the data within the network. The protection of PINs is central to the security of an ATM network and to this end it is essential that no PIN ever appears in an unencrypted state in the network. For example, a transaction that requires the PIN to be sent from an ATM, or some external network, to a central computer or to a switch must be encrypted. This is usually accomplished by passing the PIN to a separate hardware module for encryption prior to transmission to any external network. Clearly, it is also essential that no encryption algorithms or software that is involved in the PIN encryption process appear or are accessible in any readable form. Generally, in ATM systems the message data on the lines are not protected by encryption methods in spite of the generally accepted need for operational security. The reasons for this are the deterioration in transaction processing response time and the fact that the PIN is not protected while the message is within the computer centre, since the message is in the clear once it is past the line encryption device. From an operational point of view, the security module provides an adequate level of system protection and in addition it is not as expensive to implement as line encryption.

## 5. The integrated circuit card

## 5.1. The structure of the IC card

The PIN acts as the cardholder's signature and serves the same purpose in the EFT transaction as a written signature does in a conventional financial transaction. In more recent times, the advances in integrated circuit technology have made it possible to include circuits within the body of the card. The first promotion of the card was in France where Roland Moreno and his company, Innovation, patented designs in the 1970s [15]. The circuits consist essentially of a microprocessor and various types of integrated circuit memory. In this way, it is possible to provide facilities that allow identification and authentication of the user of the card to be performed directly instead of entirely on an entry point terminal connected to a central computer. The processor acts as a gateway to the memory of the IC card: in some cards the memory and the processor are integrated to form a single chip system that makes forgery very difficult and that provides for the highest level of operational security [3,7]; in others, the processor and memory are contained in separate but interconnected chip circuits [5].

The general form and layout of the processor is shown in Figure 5. On the card, the integrated circuit component may be inserted in the central left or upper left side. This configuration satisfies the needs of all card designers – European, Japanese, and American. The electrical contacts to the integrated circuit, which provide an interface to the external communication equipment, are arranged in two columns and may be located at the front, as shown in Figure 6, or on the reverse of the card according to the user's choice. Space is reserved on the front of the card for a logo, and also for stamped embossed characters. A region on the reverse of the card is provided for the application of the magnetic stripes, such as ISO 1, ISO 2 and ISO 3 that have been described earlier in the section on magnetic stripe cards.

![](/api/attachments/77K5WGVJ/fulltext/images/e48ada10efdfbb2a64706fcaf6272c552c55322d90f9f6cf962de7fce80b5fb3.jpg)  
Fig. 5. Structure of processor.

One of the original cards, the Honeywell Bull CP8 card, which is well documented, was fabricated by Motorola using their 6805 8-bit processor chip as a basis for the design. The final chip design contained some ROM, RAM and EPROM memory as well as the basic processor. The card has 8 contact points that conform with ISO standard 7816-2 for IC cards but the Motorola design makes use of 6 of these contacts as follows:

C1 - Supply voltage for processor.

C6 - PROM programming voltage level.

C5 - Ground.

C3 - Clock signal.

C2 - Card reset signal.

C7 - Asynchronous input-output data line.

C4, C8 - Reserved for future use.

![](/api/attachments/77K5WGVJ/fulltext/images/2856b1218cbd5540ad93cf14c9062a49894394b875110803c12cab79fce3fa8b.jpg)  
Fig. 6. Physical structure of IC card.

When the card is activated the processor executes the code stored in the ROM memory and subsequently locates the desired application program which may already exist within the card memory or may be resident in some external computer system. The input-output contact allows exchange of data between the card and external equipment and communication is accomplished using an asynchronous serial link.

## 5.2. IC card memory

A common feature in the design of all IC cards is the need to partition the memory into sections that are conditionally accessible by a user. The processing capability of the chip includes a limited instruction set and has the ability through the use of a pointer to split the memory into 2 sections; only addresses above the pointer can be read while those below require a security code before permitting access. Memory capacity at this stage of the development of the integrated circuit is of the order of 16k bytes but, clearly, this will be increased in the future. A particular interest, of course, is the prospect of designing an integrated circuit specifically for use in IC cards.

At the software level, the memory of the IC card is usually divided into 3 areas; an operating system area, an application program area and a data storage area. The operational modes of the IC card place demands on the characteristics of the required memory and there is, at present, a need for both volatile and non-volatile types. Programmable memory technology is now receiving much attention from logic system designers and the large semiconductor houses are providing uncommitted logic array packages which can be configured to the desired logic function with the aid of readily available hardware and software tools. These logic array packages contain built-in security features that provide the proprietary design with copy protection and also enable an electronic signature to be included to give device identification [10].

## 5.3. Security aspects in IC card

In essence, the operational security of the IC card relies, firstly, on the impossibility of modifying the operating system resident in the ROM memory and, secondly, on the partitioning of the

PROM memory into a number of zones with varying levels of accessibility. To maintain data security in the PROM memory it is usual to consider the memory as a passive element attached to and controlled by an active processor. This is the situation in both single and multichip systems that are currently in use. It is the standard approach taken in microprocessor system design; in other words, a general purpose component is programmed to implement the required system performance.

Data security and confidentiality are addressed by manufacturers by controlling access to the PROM memory through the processor and using validation of the PIN. The original French CP8 card, for example, with its 'one time programmable' EPROM memory has 7 such zones: one particular zone, the Fabrication Zone, contains data relating to the card, such as a batch and serial number. The accessibility of any zone is a function of the zone contents and cannot be altered after the card is personalised prior to being issued. The card produced by the GEC of the United Kingdom contains re-usable EEPROM memory which is partitioned into 3 sections housing the operating system, the application programs, and the transaction data.

## 5.4. IC card developments

The development of the IC card has been driven by two distinct forces: the continual advancement in the technology of integrated circuit design and the commercial and security needs of the EFT networks. A family of IC cards are now being envisaged and various forms of the cards are on trial $[6,11–12]$ in several parts of the world: these variations arise partly because of different approaches taken in the application of electronic technology, and partly because of the uses envisaged for the card. For example, the card may be used when buying a bus ticket, in pay phones; for videotex and, of course, as a credit or debit card in commercial and business systems. Equally well it may be used in the data area for medical records and as a driver's licence; in the security area as identification of the bearer, protection of authorization and records stored on the card, encryption and decryption of messages and authentication of transactions, to name a few of the many possible applications. In fact the card offers great potential for new applications.

The card design is continually influenced by the rapid progress in many aspects of microelectronic technology, for example, memory design. Nevertheless, the card design assures a basic compatibility with the existing technology of the magnetic stripe card and thus the international standards ISO 7810, 7816-1 and 7816-2 are relevant.

From a functional point of view, the IC card is a computer, comprising a processor, some units of memory, and input-output facilities. The memory areas can allow customer account data to be stored on the card so that automatic recording of transactions can be accomplished. These features result in the creation of a card that is intelligent as well as secure; terms such as 'smart card' and 'IC card' are generally used for the card. At the same time, it can be observed that an IC card is much more complex to manufacture, process, interface and use, than the magnetic stripe card. To this extent, the IC card has to prove its commercial viability.

## 6. Comparative assessment

## 6.1. Cost considerations

The magnetic stripe card has evolved through its wide acceptance and cost-effectiveness as the major financial transaction card, and, therefore, it will not be easily unseated from that position. However, the IC card is receiving attention from the card manufacturing industry as an alternative because of its authentication, identification and other security related features. An important factor in its acceptance will be the trade-off between its higher manufacturing cost and the value of its additional functions to the user. Microprocessor technology is and will remain comparatively expensive. The French are the leading users of the IC card; in production volumes of several millions, the cost per card is estimated to be under \$3 [1], which is between 5 and 10 times that of a magnetic stripe card. The exigencies of application will determine the choice of card.

## 6.2. Issues in terminal design

The magnetic stripe card has the attractive feature of not requiring physical connection to the terminal, since the magnetic medium is sensed externally. The IC card is an active device and it operates by electrical connection to an external system: thus the terminal and the IC card must be regarded as an integrated facility. The complexity and cost of the terminal will impact commercial acceptance of the IC card; a more technically sophisticated card is likely to require a simpler style of terminal, incurring less expense. A move in this direction has already occurred in Japan, leading to the design and production by Toshiba in a joint venture with Visa International of the 'super smart card' that is equipped with a keyboard and a liquid display panel in addition to processor and memory circuits. Furthermore, Nippon Telegraph and Telephone Corporation has developed a card-reading telephone to enable people to use the card for a variety of transactions related to banking and shopping.

Amongst the prospective card manufacturer's, the General Electrical Company of the UK was one of the first companies to attempt to emulate the 'no physical electrical connection' feature of the magnetic stripe card by designing an IC card that relies on inductive coupling with the terminal to perform reading and writing of the memory. It is possible in this way to dispense with electrical connections and produce a more reliable system. In order to gain commercial acceptance of the IC card, an important requirement is the development of an integrated card-terminal system.

## 6.3. Operating characteristics

The IC card, because of its computing capability and power, will require certain interface compatibilities not hitherto used in other card products. If we consider the technology of the present day credit and debit cards, for instance Visa, the only requirement is that information be read by an accepting device. After that, any further information, say the PIN and the amount of the transaction are input from a separate keyboard and do not demand anything else from the card. The simplicity of this operation speaks for itself.

This position, however, changes considerably when an IC card, which has its own computing and data storage capability, is used to perform the same operations. Additional requirements and need for more capabilities emerge. The card stores financial information in the form of actual transactions processed and data now need to be updated; for example, new balances may need to be produced and recorded. Because of this, the card has to interface with a variety of accepting devices thus providing a framework for distributing computing power into the hands of the general public. Taking into account the large number of card accepting devices already in the field, this is a huge requirement.

## 6.4. Commercial aspects

It is abundantly clear that the magnetic stripe card has had remarkable success. It has enabled banks to provide their customers with a purely cash dispensing facility, of good availability. To extend the base of this network, it has been necessary for the banks to move towards retail store outlets and provide point-of-sale cash service through electronic transfer of funds (EFTPOS). Whilst this service is growing it has not advanced at the pace originally anticipated. This requires on-line operation when using a magnetic stripe card, and this mode of operation is relatively expensive.

IC card technology could overcome some of the difficulties that have prevented the widespread use of EFTPOS. These cards contain enough built-in intelligence to enable them to function in the less expensive off-line mode and still maintain a desirable level of operational security. As a result of this there is likely to be a saving in the cost. To execute a transaction using an IC card, the retailer's terminal must first check that the card is valid and not outdated. The PIN can then be verified against the encoded PIN contained in the card's memory thus providing a degree of security. Transactions could be stored in the terminal, and also in the IC card, and sent to the card issuer at appropriate times. In addition, the IC card could attach various restrictions and conditions to the authorization of a specific transaction. This would depend on the application, but the procedures would limit the extent and risk of illegal use of cards. In this respect, the so-called 'super smart card' designed jointly by Visa International and Toshiba approaches the limit in operational security to the extent that all information can be encrypted on the card, thus removing the risk of intercepting transmission of plain text between the terminal and the card.

## 7. Conclusions

The magnetic stripe card has an attractive intrinsic simplicity that has not prevented it from functioning with sufficient security within a limited operational environment. It has the additional attractive feature of not requiring physical electrical connection to the terminal, since the magnetic medium is sensed externally. As a financial transaction card, it has proved cost effective and earned its place.

However, the IC card is gaining recognition in the commercial world. These cards have unique advantages as identification and access passes, bearers of personal records, carriers of electronic authorisation and tickets, encryption devices and 'electronic money'. In banking systems this is seen as offering a 'value added' function to the current magnetic stripe card due to its increased security. As a security product, it offers a scale of levels of security depending on the requirements of the user. The increase in memory capacity and advances in integrated circuits will permit multi-application utilization, each application with its own security keys and access rules.

The IC card is not just a card, but a family of cards, from basic card to most sophisticated. Each is upward compatible with the higher family member supporting the functionality of lower family members wherever business considerations so demand; at the same time, it may be compatible with the magnetic stripe card. The realization of such a card as a business product will evolve when the mechanism for its manufacture and marketing shows economic feasibility. It is then that the business community will be able to make a commercial assessment of the card as a data processing element compared to a magnetic stripe card.

## References

[1] Bright, R. Smart Cards: Principles, Practice, Applications, Horwood, 1988.

[2] Durie, J. “Chase Lifts Share of Credit Cake”, The Australian, 9 January 1990.

[3] Guillou, L.C. A Highly Reliable and Portable Security Device, Advances in Cryptology-Crypto 84, Springer-Verlag, 1985, pp. 464–479.

[4] Harrop, P. "New Electronics for Payment", IEE Review, October 1989, pp. 339–342.

[5] Kruse, K. "Security a la Carte", Siemens Magazine COM, Vol. 5, 1986, pp. 13–19.

[6] Martin, S.L. “Smart Card Development Expands as Standards near Final Approval”, Computer Design, Vol. 27, No. 16, Sept. 1988, pp 30–31.

[7] McDonald, N., and Sylvester, D. “The IC Card, the Smart Card that Will Lead Us into the Future”, GEC Review, Vol. 3, No. 3, 1987, pp. 152–159.

[8] Meyer, C., and Matyas, S. Cryptography: A New Dimension in Information Security, Wiley, New York, 1982, pp. 675–678.

[9] Mier, E. "Bank Data Networks: Moving Millions Electronically", Data Communications, April 1981, pp. 19–31.

[10] National Semiconductor Corporation, "GAL 20V8

Generic Array Logic", Preliminary Application Note, September 1987.

[11] Piper, A. “The Intelligent Managers Guide to Smart Cards”, International Management, February 1986, pp. 26–28.

[12] Shogase, H. “The Very Smart Card: A Plastic Pocket Bank”, IEEE Spectrum, October 1988, pp. 35–39.

[13] Southworth, L.E. "Basic EFT Network Switching", Data Communications, September 1983, pp. 179–183.

[14] Svigals, J. Smart Cards-The Ultimate Personal Computer, Macmillan Publishing Company, New York, 1985.

[15] Weinstein, S.B. “Smart Credit Cards: The Answer to Cashless Shopping”, IEEE Spectrum, February 1984, pp. 43–49.
