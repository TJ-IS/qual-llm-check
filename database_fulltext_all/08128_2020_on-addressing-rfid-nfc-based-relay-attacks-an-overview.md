---
otero_id: 8128
otero_key: "P55RSAMU"
title: "On addressing RFID/NFC-based relay attacks: An overview"
authors: "Yu-Ju Tu; Selwyn Piramuthu"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113194"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

On Addressing RFID/NFC-based Relay Attacks: An Overview

Yu-Ju Tu, Selwyn Piramuthu

![](/api/attachments/P55RSAMU/fulltext/images/54f7e0c8b3672821ec6c1d5e244154c56364032daf88dd068b0b895de6050107.jpg)

PII: S0167-9236(19)30223-4

DOI: https://doi.org/10.1016/j.dss.2019.113194

Reference: DECSUP 113194

To appear in: Decision Support Systems

Received date: 16 August 2019

Revised date: 3 November 2019

Accepted date: 8 November 2019

Please cite this article as: Y.-J. Tu and S. Piramuthu, On Addressing RFID/NFC-based Relay Attacks: An Overview, Decision Support Systems (2019), https://doi.org/10.1016/ j.dss.2019.113194

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# On Addressing RFID/NFC-based Relay Attacks: An Overview

Yu-Ju Tu<sup>1</sup>, Selwyn Piramuthu<sup>2,∗</sup>

<sup>1</sup>Management Information Systems, National Chengchi University, Taipei, Taiwan <sup>2</sup>Information Systems and Operations Management, University of Florida, USA corresponding author: selwyn@ufl.edu

## Abstract

Relay attacks generally occur between two entities that communicate with each other through wireless means. When a relay attack between a honest prover and a honest verifier occurs, an adversary tricks the prover and verifier into believing that they are indeed communicating with each other. Such attacks are rather difficult to identify and prevent since a passive adversary does not modify any of the communicated messages between prover and verifier. RFID/NFC-based applications are particularly vulnerable to such attacks. We provide an overview of RFID-based relay attacks and evaluate various streams of research that have attempted to address these attacks. Specifically, we consider distance-bounding techniques and the use of artificial or natural ambient conditions, with specific emphasis on the latter.

Keywords: RFID, relay attack, cryptography, ambient conditions

## 1 Introduction and Background

The last decade has witnessed an explosion in interest related to systems that incorporate RFID (Radio-Frequency Identification) and its sub-type NFC (Near Field Communication). The significance of this interest stems from the desire for automation through wireless means (e.g., NFC-based secure mobile payments) and various applications of fine-granular information such as that generated through itemlevel RFID tags (e.g., Bose and Yan 2011, Bose and Pal 2005, Bose et al. 2011). As Moore’s law predicted, the size and cost of an electronic chip have drastically decreased, which has facilitated the development of novel applications that incorporate RFID. A large number of pervasive computing and ubiquitous automation systems rely on RFID technology as the core. RFID-based information systems also play a crucial role in IoT (Internet of Things) and FinTech (Financial Technologies) domains. For example, introduced in 2014, Apple Pay is a popular NFC-based mobile payment service. The number of Apply Pay users exceed 380 millions (Clement 2019). The number of IoT devices worldwide is predicted to increase to 75 billion by 2025; the battery-free or solar-powered RFID stickers are expected to be largely used for indoor and outdoor sensing and tracking, saving energy and developing smart infrastructure or environment (Matheson 2019). Other potential mass use cases of RFID include food supply chain, intelligent transportation, and healthcare (Thibaud et al. 2018).

While RFID-based systems have several advantages over competing technologies such as barcode, these systems are vulnerable to attacks from adversaries (e.g., Mitrokotsa et al. 2010). A majority of these attacks stem from the fact that (1) RFID tags are extremely resource-constrained devices and (2) communication between RFID and reader occur through wireless means. Although researchers have developed cryptographic protocols that are resistant to various types of attacks that are mounted against RFID systems, relay attacks have remained elusive to such attempts.

A relay attack occurs when an adversary relays authentication-related communication between a prover (here, RFID) and a verifier (here, reader). During a relay attack, an adversary does not modify any of the messages that are communicated between prover and verifier. Due to this, the verifier and prover may not even be aware of such an attack when it happens. Relay attacks are generally used as a means to falsify the distance between prover and verifier. For example, an access card-controlled door may be opened by an adversary who relays communication between the door reader and an access card that is nowhere near the door.

The core idea of an RFID relay attack is analogous to the classical deceptive trick of a novice chess player (Conway 1976). Tony, a novice chess player, invites a chess master Alice to play a chess game with him. Simultaneously, Tony invites another chess master Bob to play another chess game with him. Tony then passes on Alice’s chess moves to Bob and Bob’s chess moves to Alice. So, both Alice and Bob will regard Tony as a chess master, even though he is simply a novice at the game of chess. This chess game trick can be easily solved. As long as Alice and Bob can see each other face-to-face while playing the chess game, there is no place for Tony to hide and play as the malicious middle man. The same cannot be said of RFID and reader. Unfortunately, RFID and reader in most applications cannot ‘see’ each other; not to mention the fact that the communication occurs in open air and is easily relayed by anyone.

There is a growing set of publications that attempt to address relay attacks in RFID-based systems. To determine the level of interest among researchers for RFID-based relay attacks, we searched Google Scholar with the keywords ‘RFID’ and ‘relay attacks’. We plot the resulting output in Figure 1. As can be seen in this figure, there is a general increasing trend in the number of research publications per year that address relay attacks.

![](/api/attachments/P55RSAMU/fulltext/images/318a4f2d9add75adc5fceeff262d7c05f4a68cd3ea6345bffb84738addb93b7c.jpg)  
Figure 1: Number of research publications per year on RFID-based relay attack

200RFID relay attacks are generally regarded as atypical security threats as compared to most conven-<sup>150</sup>tional security threats. The few dozen representative solutions that have appeared in published literature have their respective limitations. Furthermore, the variety of application contexts and the mode of relay attacks have dynamically evolved. For example, a new breed of crime that is based on RFID relay attack (i.e., car relay theft) has the potential to inflict serious damage (BBC 2018). While there have been sev-eral attempts at addressing RFID relay attacks over the years, a valid and universal solution against such attacks has evaded such attempts so far. It is therefore critical to find realistic solutions that work sooner than later since new applications that include RFID-based systems are being introduced at a much faster rate as years go by. For example, the value of global mobile wallet market with NFC as the key enabler 8was reportedly worth nearly 900 million in 2018, and is predicted to be worth more than 3000 billion in only five years (Industry-reports 2019).

2Since relay attacks involve encrypted messages that are relayed between prover and verifier by an adversary, it is only natural to attempt to thwart such attacks through cryptographic means. To this end, a majority of published studies propose cryptographic authentication protocols with the goal to identify <sup>Fig.</sup> <sup>3.</sup> <sup>The</sup> <sup>number</sup> <sup>of</sup> <sup>RFID-based</sup> <sup>ambient</sup> <sup>condition</sup> <sup>studies</sup>a relay attack when it happens. The common goal of a relay attack happens to involve distance. Here, an adversary relays messages between a prover and a verifier that are farther removed than the expected normal physical separation between prover and verifier, which is in the order of a few millimeters to a few meters. With distance as the objective, the time taken for a message to travel between prover and verifier is used to measure the distance between them. More recently, researchers have resorted to the use of ambient conditions or context to detect relay attacks.

We present an overview of existing approaches against RFID-based relay attacks. Such a review is necessary to take stock of the state of the art and to identify possible avenues to move forward to address relay attacks. We therefore attempt to answer the following research questions.

RQ1: What are the current research trends and findings in RFID-based relay attacks?

RQ2: How are the research trends likely to evolve in the near future?

In the following sections, we first provide a review of different types of RFID-based relay attacks. Next, we present a concise summary of defense mechanisms and their comparisons based on a selective review of representative prior studies. Finally, we conclude with recommendations for future studies in this general area.

## 2 RFID-based Relay Attack Variants

By its very nature, an RFID-based relay attack signifies that communication messages are unexpectedly passed between two parties that include an RFID tag (T) and a reader (R). It is unexpected since the two parties are not in close physical proximity of each other as is required for such communication to take place.

Relay attacks come in a few different flavors that differ based on the honesty status of the prover while the verifier is always assumed to be honest. The first type of RFID-based relay attack occurs when both (i.e., prover and verifier) parties are not aware of the attack. This scenario is referred to as RFID-based Mafia attack. Under normal circumstances, communication occurs only between a honest tag and a honest reader. However, an adversary can easily use a malicious reader to impersonate the honest reader to the honest tag and then relay the message from the honest reader to the honest tag. Similarly, the adversary can use a malicious tag to impersonate the honest tag and then relay the honest tag’s message to the honest reader. Thus, there are two pairs of readers and tags (i.e., RTRT) in this scenario (Figure 2). The inner reader and tag pair (i.e., T and R) are malicious. The outer reader and tag pair (i.e., R and T) are honest. There are several possible instances in this type of relay attack. For example, PKES (Passive Keyless Entry System) is used to unlock and start a vehicle automatically. With PKES, people no longer waste their time to locate the keys from their pockets or bags and then insert them into the key slots of their vehicles. Rather, they just need to possess their PKES tags, usually in the form of key fob, on their person as they approach their vehicles. RFID-based PKES readers inside their vehicles validate their identities as they approach their vehicles. The RFID reader constantly scans its surroundings by sending out data, such as a ‘Hello’ message. An adversary can easily capture this ‘Hello’ message. Next, the adversary relays the captured ‘Hello’ to the vehicle owner’s PKES tag. In principle, for relay attack to occur, the distance between the owner with the PKES tag and the associated<sub>controlled</sub> vehicle does not matter. Upon receiving the ‘Hello’ message, the tag by default sends out an appropriateR T response to initiate communication with the reader. By relaying messages back and forth between the vehicle and the PKES key, an adversary is able to successfully unlock the vehicle without the vehicle owner’s permission (BBC 2018, Francillon et al. 2011, Ranganathan et al. 2017).

![](/api/attachments/P55RSAMU/fulltext/images/c72448a0766bf94160d8937481859c0faa672064806f29b62b36cbc7a993a61f.jpg)  
Figure 2: Mafia Relay Attack

<sup>controlled</sup> The second type of relay attack occurs when the (dishonest) RFID tag is aware of the unexpectedly R Trelayed data, but the (honest) RFID reader is not (Figure 3). This means that unlike the first type, the second type benefits from a mole that is played by the tag. Because mobile payment communication occurs through NFC, it is essentially an application of RFID.

![](/api/attachments/P55RSAMU/fulltext/images/524888de65e40aa7d06e117df3a26c4c788c0a4441b7e63da92e17ada9af5974.jpg)  
Figure 3: Terrorist Fraud Relay Attack

When a customer makes a mobile payment, the process is under the threat of RFID-based relay attacks (Kfir and Wool 2005, Francis et al. 2013, Marforio et al. 2012). Furthermore, with a dishonest customer’s permission, an adversary can easily relay this customer’s payment information to make a purchase at a location where this customer is obviously absent. In the end, because the customer has an alibi, the customer can easily falsify the payment and the credit card issuing bank is forced to absorb the collateral damage. In other words, under this scenario, a dishonest mobile payment user can use the colluded or compromised payment means to mount a relay attack. This type of RFID-based relay attack is referred to as a Terrorist Fraud attack.

There are many examples that typify the first and second type of RFID-based relay attacks (e.g., Owen and Wool 2009, Hlavac et al. 2007, Azizi et al. 2012). For example, an electronic passport is vulnerable to the first type of attack. The personal identity data in a traditional paper-based passport is the physical printed data that is used in OCR (optical character recognition)-based systems. However, an embedded RFID tag holds the data in electronic passports. This signifies that an adversary can impersonate someone else by simply relaying the other person’s electronic personal identity to successfully pass through the check-point. An electronic ballot system also has the possibility of threat from RFID-based relay attack. As compared with the conventional paper-based ballot system, an electronic ballot system has many merits that include better accuracy and efficiency. However, an adversary can relay someone else’s electronic ballot data to somewhere without that person being aware of such an attack. Similarly, an advanced gun control mechanism is vulnerable to an RFID-based relay attack. By design, an intelligent or smart gun cannot be fired if the shooter is unable to identify himself or herself via the RFID-based safety mechanism. This is because whenever the handle or trigger of the gun is held by someone, the gun uses RFID-based authentication to determine whether the gun user has correctly proved his or her identity. When authentication fails, the gun remains locked for safety reasons. However, it has been shown that the gun’s RFID-based data can be relayed to thwart its safety mechanism (Greenberg 2017).

![](/api/attachments/P55RSAMU/fulltext/images/2a3250c087fa24416da32cfc3b603958501df82ad7d840a5ae6f2ac61909cdb7.jpg)  
Figure 4: Relay attack type 3

Theoretically, there should be a third type of RFID-based relay attack. In this scenario, the (dishonest) RFID reader is aware of the attack but the (honest) RFID tag is not (Figure 4). The reader can then collude with an adversary to facilitate a relay attack. This scenario is the complement of the second type of RFID-based relay attack. After a comprehensive review of prior studies, we have not found any instance or example of this type of RFID-based relay attack. However, this does not signify that the third type of attack will never happen in the future. For example, a hacked reader can be made to act in dishonest ways. Here, such a dishonest reader is able to communicate with honest tags during a relay attack. We summarize RFID-based relay attack examples from the literature in Table 1.

Table 1. RFID-based relay attack examples.

<table><tr><td>Threatened areas</td><td>Example cases</td><td>References</td></tr><tr><td>Intelligent transportation</td><td>PKES (passive keyless entry system) or Smart car key</td><td>BBC (2018)Francillon et al. (2011)Ranganathan and Capkun (2017)</td></tr><tr><td>Contactless payment</td><td>NFC (near field communication)Mobile payment</td><td>Kfir and Wool (2005)Francis et al. (2013)Marforio et al. (2012)</td></tr><tr><td>Electronic government</td><td>Electronic passportElectronic ballot</td><td>Wool and Kfir (2009)Hlavac and Rosa (2007)Azizi et al. (2012)</td></tr><tr><td>Intelligent weapon safety</td><td>Smart gun control</td><td>Greenberg (2018)</td></tr></table>

In the next section, we review and compare defense mechanisms that have been proposed in the literature against RFID-based relay attacks.

## 3 A Selective Review of RFID-based Relay Attack Defense Mechanisms

Distance-bounding and co-presence of ambient conditions are two major streams of the solutions that have been proposed in extant publications (Avoine et al. 2018, Conti and Lal 2019). As both of these are suitable for autonomous applications, they generally do not need any human intervention, manual effort, and so forth to operate. We now provide an overview of methods that make use of distance bounding means. We then consider methods that use ambient conditions to address relay attacks. We conclude this section with a brief discussion of these methods.

## 3.1 Distance Bounding-based Methods

The distance-bounding solution is grounded on checking RTT (round trip time), RSS (received signal strength), or AOA (angle of arrival) as defense against RFID-based relay attack. Brands and Chaum (1993) first used the term ‘distance-bounding’ to formulate a security problem to determine the exact distance between two parties in communication. Their solution is based on sending out rounds of data (the challenges) and receiving back the corresponding rounds of data (the responses) between the two parties in order to compute their time of flight to infer the distance between them. The focus of their solution is on defending Mafia relay attack, rather than Terrorist Fraud relay attack. From an RFIDbased perspective, Bahl and Padmanabhan (2000) determine the distance between RFID tag and reader by triangulating radio signal arrival angles and strengths. Similarly, Fishkin and Roy (2003) determine the distance by analyzing the amount of radio energy received. However, because radio signal strength and arrival angles can respectively be amplified and altered easily, Hancke and Kuhn (2005) improve the distance-based solution against RFID-based relay attack. Their lightweight approach is applicable in a resource-constrained RFID environment such as that of a passive RFID tag. Next, Reid et al. (2007) improved the distance-based solution and developed a means to defend against both Mafia relay attack and Terrorist fraud relay attack. Tu and Piramuthu (2007) redesigned the encryption and computation algorithm of Hancke and Kuhn (2005) to achieve greater success at preventing both Mafia relay attack and Terrorist fraud relay attack. Kim et al.(2009) developed a more robust solution, as compared with the one by Tu and Piramuthu (2007). In addition to Mafia relay attack and Terrorist fraud relay attack, their solution was designed to handle other RFID-based security threats such as active attacks. Yum et al. (2010) use distance-bounding technique for mutual authentication.

Almost all of the above distance-bounding-based solutions may violate location-based privacy because of information leakage between the communicating parties. Rasmussen and Capkun (2008) pro-<sup>ˇ</sup> vide several suggestions to enhance general location privacy in a distance-bounding based solution. The suggestions include the use of random delays between messages and multiple challenges that are separated by a constant time duration. They thus propose a location private distance-bounding based solution that does not leak any range and distance information to an adversary. Later, Cremers et al.(2012), Boureanu et al.(2013), Vaudenay et al.(2013), and Boureanu et al.(2015) showed that the previously proposed distant-bounding based solutions ignore the situations when the RFID tag (i.e., prover) intends to lie about its location. This is theoretically different from a Terrorist fraud relay attack since the tag does not collude with an adversary. However, such situations are very likely to influence distance-based solution’s proximity-checking capability against relay attacks. For example, a dishonest tag for some reason may send the responses in advance prior to receiving the challenges during the fast challenge-response phase in the distance-bounding protocol by Hancke and Kuhn (2005). This may result in a distance-based fraud. Also, the dishonest tag can consider capturing and replaying the responses of other nearby honest tags (i.e., distance hijacking). Their proposed distance-bounding solution is aimed at handling such situations. Similarly, Trujillo-Rasua et al. (2014) propose a lightweight distance-bounding based solution that only involves limited computational resources to deal with distance fraud. There are a few other variants in addition to the aforementioned distance-bounding based solutions(Avoine et al. 2018).

Recently, Pagnin et al. (2018) redesigned the encryption algorithm in the distance-bounding based solution. They specifically use LPN (learning parity with noise) to enhance RFID data randomness during communication. Their proposed solution can thus offer a high success rate at defending against Mafia relay attack and Terrorist fraud relay attack. Abidin et al. (2016) and Abidin (2019) propose the appli cation of quantum theory to deal with RFID-based relay attacks. For example, they present a conceptual model of using quantum bits to improve the fast challenge-response phase in the distance-bounding protocol by Hancke and Kuhn (2005). Yang et al. (2017) consider defending against RFID-based relay attacks under a situation in which both RFID reader and tag are beyond their normal communication range. For example, although one hop is the normal radio communication distance between an RFID tag and reader pair, it is not impossible for a tag and reader to communicate with each other at a distance of two hops. This suggests that there is an entity (or device) located between the tag and reader that enables the communication to occur. To prevent RFID-based relay attacks in this type of situation, Yang et al. 2018 propose a distance-bounding based solution that involves the role of the untrusted in-between entity. We present the main findings of these representative distance-bounding based studies in Table 2.

## 3.2 Ambient Conditions-based Methods

While the number of distance bounding-based solutions constitute a greater proportion of those against relay attacks in the literature (Figure 5), the number of studies that use ambient conditions against relay attacks have gradually increased over the past several years (Figure 6). We interchangeably use ‘ambient conditions’ and ‘context awareness’ in this paper.

In a strict sense, ambient conditions based solution and distance-bounding based solution share a similar assumption for defense against RFID-based relay attacks. The attacker tends to misrepresent the fact that the RFID tag and reader are in close physical proximity when they are indeed physically much farther apart. Simply put, both the solutions use the idea of autonomous proximity-checking to detect relay attacks. Unlike distance-bounding solutions, the ambient conditions based solutions do not rely on measuring RTT, RSS or AOA to achieve proximity-checking. Instead, the solution directly compares the ambient characteristics of RFID reader and tag, i.e., the co-presence of the ambient conditions at the

Table 2. A summary of the selective distance-bounding based solutions against RFID-based relay attacks

<table><tr><td>The solutions (studies)</td><td>Key findings</td></tr><tr><td>Brands and Chaum (1993)</td><td>They use the term “distance-bounding” to formulate a security problem of determining the distance between two parties in communication. Their solution is based on measuring the time difference between sending out rounds of challenge bit and receiving back the corresponding rounds of bit data, i.e., RTT (round trip time). Their solution is focused on defending Mafia relay attack, rather than Terrorist relay attack.</td></tr><tr><td>Bahl and Padmanabhan (2000)</td><td>Their solution is based on triangulating and comparing radio signal arrival angles, i.e., AOA (angle of arrival)</td></tr><tr><td>Fishkin and Roy (2003)</td><td>They analyze received signal strength for inferring the distance between RFID tag and reader. Their reason is that the distance is proportional to the power of radio energy received, i.e., RSS (received signal strength)</td></tr><tr><td>Hancke and Kuhn (2005)</td><td>Their solution improves the solution by Brands and Chaum (1993) with a focus on lightweight computation.</td></tr><tr><td>Reid et al. (2007)</td><td>Their solution improves the distance-bounding based solution by Hancke and Kuhn (2005) with the use of the symmetric key cryptography method. Moreover, their solution can resist Terrorist relay attack with better probability</td></tr><tr><td>Tu and Piramuthu (2007)</td><td>Their solution improves distance-bounding based solution by Hancke and Kuhn (2005) with more efficient encryption loops. Thus, the solution can increase the success rate of preventing Terrorist relay attack.</td></tr><tr><td>Kim et al. 2008 (2008)</td><td>Their solution (i.e., Swiss Knife) improves the distance-bounding based solution by Hancke and Kuhn (2005). The solution not only can deal with Mafia relay attack and Terrorist relay attack, but also can further handle other RFID security threats, such as an active attack.</td></tr><tr><td>Rasmussen and Capkun (2008)</td><td>Their solution improves the distance-bounding based solution by Hancke and Kuhn (2005) with enhanced location privacy in terms of leaking no range and distance information to an attacker.</td></tr><tr><td>Yum et al. (2010)</td><td>Their solution improves the distance-bounding based solution by Hancke and Kuhn (2005) with mutual authentication</td></tr><tr><td>Cremers et al. (2012), Boureanu et al. (2013), Vaudenay et al. (2013), Boureanu et al. (2015)</td><td>Their solution is focused on patching such loopholes as distance fraud or hijacking for a series of distance-based solutions that are variants of the one proposed in Hancke and Kuhn (2005).</td></tr><tr><td>Trujillo-Rasua et al. (2014)</td><td>Their proposed distance-based solution is focused on dealing with distance fraud with minimal computational resources</td></tr><tr><td>Yang et al. 2017</td><td>Their solution extends the distance-bounding based solution by Hancke and Kuhn (2005) to consider the situation where both RFID reader and tag are out of their normal communication distance. Thus, their proposed solution involves the role of the untrusted entity or device between RFID reader and tag.</td></tr><tr><td>Pagnin et al. (2018)</td><td>Their solution is to integrate the distance-bounding based solution by Hancke and Kuhn (2005) and LPN (learning parity with noise). Their solution offers a high success rate at defending against Mafia and Terrorist relay attacks</td></tr><tr><td>Abidin et al. (2016) Abidin (2019)</td><td>They use quantum bits to improve the fast challenge-response phase in the conventional distance-bounding based solution, such as the one by Hancke and Kuhn (2005)</td></tr></table>

reader and tag locations.

There has been an increase in the number of studies that focus on the use of ambient conditions to defend against RFID-based relay attacks (Conti and Lal. 2019). For example, Francis et al. (2010) propose that sensitive mobile applications, such as NFC-based payment or electronic ticket, be protected through location or proximity information. They thus illustrate a framework that uses context awareness authentication and access control to defend against relay attacks. Ma and Saxena (2011) suggest that a new and promising way to protect RFID-based systems against relay attacks is to enable RFID tags with the capability to sense ambient conditions. Specifically, they suggest leveraging the use of the RFID tag’s on-board sensor (e.g., Piramuthu and Doss 2017) to acquire appropriate information on the tag’s environment or that of the tag itself in order to achieve proximity-checking. In a similar vein, although Schurmann and Sigg (2013) do not directly develop a solution against RFID-based relay attacks, they propose a fuzzy cryptographic communication channel between devices by comparing their background audio patterns such as that in clap, music, snap, speak, and whistle. Conceptually, their proposed solution should be able to defend against RFID-based relay attacks by detecting the co-presence of ambient audio conditions.

![](/api/attachments/P55RSAMU/fulltext/images/24188a7944593c1aafff3a9c98ee1c0b99d92ea952ff43f15080eda0f8392125.jpg)

Figure 5: The number of RFID-based distance-bounding studies  
![](/api/attachments/P55RSAMU/fulltext/images/f680e8eb27e1e054198a65e43886ea4815ae3a082db039da6b893a94669951d8.jpg)  
<sub>Fig.</sub> <sub>3.</sub> <sub>The</sub> <sub>number of</sub> <sub>RFID-based</sub> <sub>ambient</sub> <sub>condition studies</sub>  Figure 6: The number of RFID-based ambient conditions studies

Ma et al.(2012, 2013) use location sensing technology such as GPS to enhance RFID-based security and privacy. Dakhore and Lohiya (2015) use GPS coordinates to address RFID-based relay attacks. However, the use of GPS has many limitations such as cost, outdoor use only, and long distance use only. Halevi et al. (2013) propose that any object’s presence in the environment must be correlated with the object’s contextual information. They illustrate several possibilities to use sensing technologies to detect motion conditions, audio conditions and light conditions to reduce the threat of RFID-based relay attacks. In particular, they demonstrate how their proposed mechanisms can improve the success rate at preventing RFID-based relay attacks without negatively affecting the underlying RFID-based application.

Truong et al. (2014) investigate the integrated performance of combining WiFi, Bluetooth, audio and GPS input to achieve proximity-checking against RFID-based relay attacks. They show that the simultaneous consideration of multiple ambient conditions rather than any single one can significantly improve the performance of the ambient conditions based solution. Similarly, Gao (2014) proposed an RFID-based relay attack defense solution that relies on detecting the co-presence of WiFi, Bluetooth, GPS, and audio conditions. Shrestha et al. (2014) consider the combination of temperature, humidity, altitude, and gas conditions in an integrated proximity-checking mechanism to detect RFID-based relay attacks.

Urien and Piramuthu (2013, 2014) rely on detecting the co-presence of temperature conditions to achieve proximity-checking. They specifically investigate the integration of ambient conditions and elliptic-curve cryptography to defend against RFID-based relay attacks. Tu and Piramuthu (2017) propose a solution that uses geomagnetic field conditions to achieve proximity-checking. Their RFID-based relay attack solution uniquely incorporates a lightweight cryptography method to enhance their solution’s applicability. Choi et al.(2018) use ambient sound against RFID-based relay attack. Their proposed solution is focused on improving PKES security and has the capability of dealing with sound-playback situations. In general, as compared with use of ambient sound or light conditions, the use of ambient temperature and geomagnetic field conditions against RFID-based relay attack has fewer concerns regarding orientations of RFID tag and reader antenna. Wang (2019) suggests improving PKES security against relay attacks through an integrated examination of the co-presence of Bluetooth energy conditions, RSSI (Receiving Signal Strength Indicator) conditions, WiFi conditions and GPS coordinates for proximity-checking.

Mehrnezhad et al. (2014) focus their attention on detecting the co-presence of physical vibrations to defend against RFID-based relay attacks. For example, they suggest that an NFC payment user can tap the reader twice for initiating the payment process. Because the tapping motion generates vibration signals, such signals can be sensed and examined by an accelerometer to achieve proximity-checking. Analogously, Li et al. (2015) compare the vibrations of motions to perform near field authentication against relay attacks. For example, they let the same user simultaneously move his or her two fingers on the screens of two mobile phones. Because the sliding motions by the same person’s two fingers naturally tend to generate highly correlated vibrations, proximity-checking can be done.

Gurulian et al. (2016) investigate the use of ambient condition sensors to achieve proximity-checking against RFID-based relay attacks, with a specific focus on NFC-based solutions. Similar to Gurulian et al. (2016), Akram et al. (2016) observe that a majority of the existing natural ambient condition sensors may not be sufficient enough to offer quality performance for proximity-checking in a certain number of realistic cases. Their cases specifically pertain to NFC-based applications such as mobile payment or contactless banking transaction. Shepherd et al. (2017) conduct an empirical investigation in which 1,000 sensor-involved records from 252 students were analyzed during a field trial. Their conclusion is similar to that of Akram et al. (2016). Later, Gurulian et al. (2017a, 2017b) proposed a relay attack solution with the use of infrared light conditions, such as a random-bit sequence of pulses and pauses, to achieve proximity-checking. They also propose other similar solutions based on the use of vibration as ambient condition as defense against relay attacks (Gurulian et al. 2018). Their solutions are noticeably associated with artificial ambient conditions, rather than natural ambient conditions.

Piramuthu (2018) proposes to address RFID-based relay attacks with the co-presence of ambient conditions in a situation where the component tag relationship (i.e., tag inclusion or exclusion) is considered. Dabosville et al. (2019) propose a way against relay attacks for NFC-based applications by comparing side-channel leakage conditions. For example, signal-to-noise is a common leakage condition. A unique characteristic of this solution is that side-channel leakage is generally considered a vulnerability in security systems. They demonstrate the possibility of using such leakage conditions to address RFID-based relay attacks. We summarize the main findings of these representative ambient conditions based studies in Table 3.

## 3.3 Discussion

Both the distance-bounding and ambient conditions based solutions have their respective concerns when dealing with RFID-based relay attacks (Avoine et al. 2011, Boureanu and Vaudenay 2015, Urien and Piramuthu 2014, Tu and Piramuthu 2017). For the distance-bounding based solution, it is conventionally assumed that because of radio signal’s inherent physical limits, the ratio of the signal arrival time to the signal travel distance, the ratio of the signal strength to the signal travel distance, and the ratio of signal arrival angle to the signal travel distance are constant and predictable. In other words, if there is any delay or the signal strength is weaker or irregular arrival angle is detected, there is a higher possibility of a relay attack. However, radio signal can be easily amplified. Similarly, radio signal arrival angle is likely to be altered. More importantly, radio signal travels extremely fast. Thus, if the distance between RFID reader and tag are only in the range of dozens of meters, it is difficult to distinguish between normal and abnormal signal arrival time, strength, and angle. Consequently, these measures are not useful for detecting RFID-based relay attacks. This also means that the measurement of radio signal flight time for distance-bounding solution has to be at a fine granular scale (e.g., nanoseconds) because of the high signal transmission speed.

Table 3. A summary of selective ambient condition based solutions against RFID relay attacks

<table><tr><td>The solutions (studies)</td><td>Key findings</td></tr><tr><td>Ma et al. (2012), Ma et al. (2013), Dakhore and Lohiya (2015)</td><td>They directly use location information, such as GPS coordinates, to achieve proximity-checking against RFID-based relay attacks.</td></tr><tr><td>Halevi et al. (2013)</td><td>They propose that any object&#x27;s presence in the environment must be correlated with the object&#x27;s contextual information, such as various ambient conditions. They thus demonstrate several possibilities of using sensing technologies to achieve proximity-checking such as posture recognition, audio and light detection for reducing the threat of RFID-based relay attacks.</td></tr><tr><td>Schurmann and Sigg (2013)</td><td>Although their investigation is not focused on RFID, they develop a secured fuzzy cryptographic communication against relay attacks by ensuring the co-presence of ambient audio patterns such as clap, music, snap, speak, and whistle.</td></tr><tr><td>Truong et al. (2014), Gao (2014)</td><td>They focus on using the co-presence of WiFi, Bluetooth, GPS, and audio conditions to achieve proximity-checking</td></tr><tr><td>Shrestha et al. (2014)</td><td>They focus on using the co-presence of temperature, humidity, altitude, and gas conditions to achieve proximity-checking</td></tr><tr><td>Urien and Piramuthu (2013), Urien and Piramuthu (2014)</td><td>They use the co-presence of temperature conditions to achieve proximity-checking. In addition, the solution is focused on integrating both ambient conditions and cryptography against RFID-based relay attacks</td></tr><tr><td>Mehrnezhad et al. 2014</td><td>They use the co-presence of tapping vibrations to achieve proximity-checking and rely on accelerometer to sense such vibration signals.</td></tr><tr><td>Li et al. (2015)</td><td>They detect the co-presence of the vibrations of finger sliding motions to achieve proximity-checking. For example, when the same person moves his or her two fingers on two screens simultaneously, the fingers&#x27; sliding patterns tend to be closely correlated.</td></tr><tr><td>Tu and Piramuthu (2017)</td><td>They use the co-presence of geomagnetic field conditions to achieve proximity-checking. This is an alternative solution to the one by Urien and Piramuthu (2013). This solution also includes a new lightweight protocol against RFID-based relay attack.</td></tr><tr><td>Choi et al. (2018)</td><td>They detect the co-presence of ambient sounds to defend PKES from relay attacks. Also, their solution can deal with the sound-playback situations.</td></tr><tr><td>Gurulian et al. (2017a), Gurulian et al. (2017b)</td><td>They use the co-presence of artificial ambient conditions, rather than natural ambient conditions. Specifically, they use infrared light conditions, such as a random-bit sequence of pulses and pauses to achieve proximity-checking.</td></tr><tr><td>Gurulian et al. (2018)</td><td>This solution is similar to the one by Gurulian et al. (2017a, 2017b). They use the co-presence of vibration conditions to achieve proximity-checking.</td></tr><tr><td>Piramuthu (2018)</td><td>The solution is focused on using the co-presence of ambient conditions to address RFID relay attacks and considering relationship among RFID tags, such as inclusion and exclusion.</td></tr><tr><td>Dabosville et al. (2019)</td><td>Their solution is unique and different from the surveyed solutions above. They use side-channel leakage conditions (e.g., signal-to-noise) to achieve proximity-checking, although the leakage is conventionally considered as a non-negligible threat to any security system.</td></tr><tr><td>Wang (2019)</td><td>The proposed solution against PKES relay attacks is mainly based on using the co-presence of Bluetooth energy conditions, RSSI (Receiving Signal Strength Indicator) conditions, GPS conditions, and WiFi to achieve proximity-checking</td></tr></table>

For ambient conditions based solutions, whether the conditions are reliable for identifying RFIDbased relay attack is a key concern. For example, some ambient conditions are not permanent and are only intermittent. Some are directional or hard to measure immediately and constantly. Therefore, not all of the ambient conditions can be used flexibly to achieve proximity-checking in order to detect relay attacks. Compared to the well-established distance-bounding based solutions, the ambient conditions based solutions are still at the early evolution stage. A majority of the extant ambient conditions based solutions are not reliable enough to be used as defense against RFID-based relay attacks when these ambient conditions are likely to be manipulated. Shrestha et al. (2019) point out the possibility of manipulating the readings of several ambient condition sensors. For example, they show that temperature conditions, gas conditions, audio conditions or air pressure conditions could be modified or controlled with the use of off-the-shelf equipment such as an air compressor.

Other than the distance-bounding and ambient conditions based solutions, physical intervention is another possible means to address RFID-based relay attacks. For example, Stajano et al. (2010) propose using multiple communication channels including the out-of-band channel to prevent relay attacks. Choudary and Stajano (2011) present a model for adding noise to RFID communication channel as the attack’s defense solution. Saxena et al. (2011) demonstrate a model that uses mobile phone as the token to establish a second communication channel to protect an RFID-based system from relay attacks. Alshehri and Schneider (2015) use user engagement to defend against NFC mobile relay attacks. Use of a Faraday cage, such as enclosing the RFID tag in a metallic mask, provides resistance to RFIDbased relay attacks (Kfir and Wool 2005, Khattab et al. 2017). Singh et al. (2019) propose reordering pulses in ultra-wide band (UWB) radio communication channel to defend against Mafia relay attacks. We summarize these concerns in prior literature for dealing with RFID-based relay attacks in Table 4.

## 4 Summary of Findings and Future Research

As reflected in the previous sections, existing studies have made great progress in addressing RFID-based relay attacks. However, considerable issues are also left to be further clarified and explored. Thus, we specifically recommend several sets of questions for future RFID-based relay attack research to consider and investigate. In terms of systems analysis and design, all existing distance-bounding and ambient conditions based solutions against RFID relay attacks are imperfect. For distance-bounding, there are still concerns that include alteration of RFID signal arrival angle, amplification of RFID signal strength, and the erroneous process of computing the RFID signal time of flight. For example, the main idea that is shared among distance-bounding based solutions is the use of signal travel time to determine the distance between RFID prover and verifier. However, since radio signal travels at the speed of light, it takes only a few nanoseconds for signal to travel distances of a few meters. Extreme precision is required with the measurement of time delay due to relay attack, processing time, and that due to possible system clock measurement bias.

Table 4. A summary of the major solutions against RFID-based relay attacks

<table><tr><td>Types</td><td colspan="2">Proximity-checking</td><td>Physical intervention</td></tr><tr><td>Core ideas</td><td>Distance-bounding</td><td>Co-presence of ambient conditions</td><td>Out of regular radio band</td></tr><tr><td>Main categories</td><td>Received signal strength (RSS)Angle of arrival (AOA)Round trip time (RTT)</td><td>Natural ambient conditions. e.g., sound, light, temperature, and magnetic fieldArtificial ambient conditions. e.g., infrared light and vibration</td><td>Multiple channelsUWB channelFaraday cage</td></tr><tr><td>Possible concerns</td><td>Radio signal is likely to be amplifiedRadio signal arrival angle is likely to be alteredUnit for measuring radio signal flight time has to be calibrated in a fine granular scale (e.g., nanoseconds) due to the very fast radio signal transmission speed (i.e., light speed)Any tiny time measurement error (e.g., one microsecond) is likely to result in a distance deviation of kilometers or more.Considerable number of rounds of bits of challenge-response are generally required and thus time-consuming</td><td>Not all of ambient condition sensors are available or suitable for RFID useSome ambient conditions are not permanent or directional, thus limiting their ubiquitous applicationsAs compared with the well-established distance-bounding based solutions, the ambient condition based solutions are still in the early evolution stages.</td><td>Not applied to considerable number of RFID applicationsHard to be self-maintainedHard to be generalizedAdditional cost and manual effort for customization are required.</td></tr></table>

For the ambient conditions based solution, there is still a need to investigate the more generalizable and manageable ambient conditions against RFID-based relay attacks. For example, although it has already been shown that passive RFID tags can have multiple sensing capability (Fernandez-Salmeron et al. 2015), the choice of available sensors is still limited to a certain number of types. In addition, almost all of the ambient conditions based solutions are dependent on an assumption that these ambient conditions cannot be faked or relayed. It is already known that GPS signal can be intercepted and redirected. Also, Miettinen et al. (2015) show that guessing ambient conditions is possible. Thus, once context-guessing or context-manipulation as mentioned in Miettinen et al. (2015) and Shrestha et al. (2019) are easily attainable, several of the existing ambient condition based propositions against relay attacks would become irrelevant.

Moreover, almost all of the extant RFID-based relay attack definitions and solutions share the premise that the attacker only tends to misrepresent the fact that RFID tag and reader are in close physical proximity of each other. Yet, it is theoretically possible for the complementary scenario in which the attacker intentionally misrepresents that RFID tag and reader are not in close physical proximity of each other. Rather, they are farther apart and are separated by a certain distance. For example, in an unmanned store, communication with an RFID tagged product is likely to be relayed to misrepresent that it is far from, rather than near, the reader at the shop’s payment terminal and thus any shoplifter can easily carry the product to pass through the gate without payment for the product. Once an RFID tag is detached from its originally associated object (e.g., Tu et al. 2018), almost all of the published solutions in prior literature against RFID-based relay attacks become useless. In other words, it is necessary to address the unexpected RFID tag removal situations when designing and developing RFID-based relay attack solutions. Published literature still lacks these investigations.

The integration of AI (artificial intelligence) based, distance-bounding based, and ambient conditions based solutions against RFID relay attack is also a promising future research direction. For example, AI has generally proved its usefulness in a wide variety of areas. But, the conventional AI based solution often requires abundant resources to implement. This suggests that the application of machine learning approaches that are suitable in the very resource-constrained RFID environment to address relay attacks is surely worth further investigation. Furthermore, it should be feasible and worthwhile to combine an AI based solution and existing proximity-checking solutions against RFID-based relay attacks.

Lastly, we recommend conducting value-based empirical and analytical investigations of RFID-based relay attacks. Since GDPR took effect in 2018, many firms are highly motivated to invest in IT/IS projects for improving data security and information privacy. Any organizational investment that helps defend against RFID-based relay attacks has to be evaluated in terms of its performance factors. This will lead to a series of questions that need to be further clarified, examined, and analyzed. For example, what are the benefits of preventing RFID-based relay attacks or the losses and risks of suffering from such attacks?

We present our recommendation in regard to these future research questions in Table 5. The table also includes a number of corresponding research areas and topics for future research investigations.

Table 5. Recommended RFID-based relay attack research questions and contributing research areas

<table><tr><td>Potential research questions</td><td>Potential contributing research areas</td></tr><tr><td>How to address the existing concerns regarding use of the distance-bounding-based solutions against RFID-based relay attacks?</td><td rowspan="7">Systems science discipline:RFID/IoT system analysis and design that can help resist RFID-based relay attacksRFID/IoT, sensors, and technologies that can help resist RFID-based relay attacksRFID/IoT authentication artifacts including models and protocols or prototypes that can help resist RFID-based relay attackscDecision or information science discipline:Machine learning approaches for detecting RFID-based relay attacksintrategraded decision support for predicting or preventing RFID-based relay attacksorganization or management science discipline:Empirical examination with respect to RFID-based relay attacksaAnalytical modeling with respect to RFID-based relay attackSRFID/IoT management practices for defending against RFID-based relay attacks in terms of information privacy, security, and legal considerations</td></tr><tr><td>How to address the identified concerns in prior literature regarding the use of ambient condition based solutions against RFID-based relay attacks?</td></tr><tr><td>Following the question above, how to address the situation when a relay attacker can relay the ambient conditions as well?</td></tr><tr><td>How to address the situation when RFID relay attacker tends to misrepresent that the tag and reader are farther separated, rather than that they are in close physical proximity of each other?</td></tr><tr><td>Following the question above, how to address the unexpected RFID tag removal situations when designing and developing RFID-based relay attack solution?</td></tr><tr><td>How to integrate AI-based, distance-bounding based, and ambient condition based solutions against RFID relay attacks?</td></tr><tr><td>What are the benefits in preventing RFID-based relay attack or the losses and risks of suffering from such attacks?</td></tr></table>

## 5 Concluding Remarks

We attempted to profile the present state of RFID-based relay attack investigations, highlight their findings, and interpret the future evolution trend of relay attack research. As Avoine et al. (2018) and Conti and Lal (2019) observe, the best or universal solution to avoid all such attacks currently does not exist. In other words, every representative solution against RFID or NFC relay attacks in existing literature is worth a review to consider their respective trade-offs. We comprehensively reviewed existing RFIDbased relay attack investigations and solutions. We then selectively presented the representative ones and highlighted their key points. More importantly, we highlighted several critical issues in RFID-based relay attacks research that have not been carefully investigated in prior literature across not only the technical discipline but also the managerial one. Our hope is that this work motivates researchers to consider the identified challenges and to develop better means to protect RFID-based systems against relay attacks.

## Acknowledgement

We thank the two anonymous reviewers for carefully reading the previous version of this paper and for taking their time to provide extensive constructive comments, which helped us improve the content and presentation of this paper. Yu-Ju Tu thankfully acknowledges support from MOST(Taiwan).

## References

[1] Abidin, A. Quantum distance bounding. ACM Proceedings of the 12th Conference on Security and Privacy in Wireless and Mobile Networks, pp. 233-238 (2019).

[2] Abidin, A., Marin, E., Singelee, D., Preneel, B. Towards quantum distance bounding protocols. Radio Frequency Identification and IoT Security, Springer LNCS 10155, pp. 151-162 (2016)

[3] Akram, R.N., Gurulian, I., Shepherd, C., Markantonakis, K., Mayes, K. We were wrong: ambient sensors do not provide proximity evidence for NFC transactions. arXiv:1601.07101v2 [cs.CR] 18 Feb (2016)

[4] Alshehri, A., Schneider, S. Addressing NFC mobile relay attacks: NFC user key confirmation protocols. International Journal of RFID Security and Cryptography, 3(2), pp 137-147 (2015)

[5] Avoine, G., Bingol, M. A., Kardas, S., Lauradoux, C., Martin, B. A framework for analyzing¨ RFID distance bounding protocols. Journal of Computer Security, 19(2), pp. 289-317 (2011)

[6] Avoine, G., Bingol, M.A., Boureanu, I.,¨ Capkun, S., Hancke, G., Kardas, S., Kim, C.H., Lau-<sup>ˇ</sup> radoux, C., Martin, B., Munilla, J., Peinado, A., Rasmussen, K.B., Singelee, D., Tchamkerten,´ A., Trujillo-Rasua, R., Vaudenay, S. Security of distance-bounding: A survey. ACM Computing Surveys, 51(5), pp. 94-132 (2018).

[7] Azizi, M., Bagheri, N., Mirgadri, A. Providing a distance bounding protocol named pasargad in order to defend against relay attacks on RFID-based electronic voting System. International Journal of UbiComp, 2(3). pp. 69-82 (2012).

[8] Bahl, P., Padmanabhan, V.N. RADAR: An In-Building RF-based User Location and Tracking System, Conference on Computer Communications. Nineteenth Annual Joint Conference of the IEEE Computer and Communications Societies (Cat. No.00CH37064) (2000)

[9] BBC. West Midlands PCC Calls Car Security Summit. https://www.bbc.com/news/uk-englandbirmingham-43737877 12 April 2018.

[10] Bose, I., Yan, S. The green potential of RFID projects: A case-based analysis. IEEE IT Professional, 13(1), pp. 41-47, January-February (2011).

[11] Bose, I., Pal, R. Auto-ID: Managing anything, anytime, anywhere in the supply chain. Communications of the ACM, 48(8), pp. 100-106, August (2005).

[12] Bose, I., Lui, A.K.H., Ngai, E.W.T. The impact of RFID adoption on the market value of firms: An empirical analysis. Journal of Organizational Computing and Electronic Commerce. 21(4), pp. 268-294 (2011).

[13] Boureanu, I., Mitrokotsa, A., and Vaudenay, S. Secure and lightweight distance-bounding. International Workshop on Lightweight Cryptography for Security and Privacy, Springer, pp. 97-113 (2013).

[14] Boureanu, I., Mitrokotsa, A., Vaudenay, S. Practical and provably secure distance-bounding. Journal of Computer Security, 23(2), pp. 229-257 (2015).

[15] Boureanu, I., Anda, A. Another look at relay and distance-based attacks in contactless payments. IACR Cryptology ePrint Archive, 402 (2018).

[16] Boureanu, I., Vaudenay, S. Challenges in distance bounding. IEEE Security Privacy, 13(1) pp. 41-48 (2015).

[17] Brands, S., Chaum, D. Distance-Bounding Protocols. Advances in Cryptology, EUROCRYPT 93, Springer LNCS 765, pp 344-359 (1993).

[18] Choudary, O., Frank Stajano, F. Make noise and whisper: a solution to relay attacks. B. Christianson et al. (Eds.) Security Protocols 2011, LNCS 7114, pp. 271-283 (2011)

[19] Conway, J.H. On Numbers and Games. Academic Press (1976)

[20] Conti, M., Lal, C. A Survey on Context-based Co-Presence Detection Techniques. arXiv preprint arXiv:1808.03320, adsabs.harvard.edu (2019)

[21] Choi, W., Seo, M., Lee, D.H. Sound-proximity: 2-factor authentication against relay attack on passive keyless entry and start system. Journal of Advanced Transportation, Article ID 1935974, 13 pages, (2018)

[22] Clement, J. Apple Pay Statistics Facts. Oct 1 (2019). https://www.statista.com/topics/4322/apple-pay/

[23] Cremers, C., Rasmussen, K. B., Schmidt, B., Capkun, S. Distance hijacking attacks on distance <sup>ˇ</sup> bounding protocols. IEEE Symposium on Security and Privacy, pp. 113-127 (2012)

[24] Dabosville, G., Maghrebi, H., Lhuillery, A., Bringer, J., Le, T.H. On the bright side of darkness: side-channel based authentication protocol against relay attacks. IACR Cryptology ePrint Archive, pp.4-14 (2019)

[25] Dakhore, S., Lohiya, P. Location aware selective unlocking for enhancing RFID security. International Journal of Innovative Research in Computer and Communication Engineering, 3(4), pp.3663-3668 (2015)

[26] Fernandez-Salmeron, J., Rivadeneyra, A., Martinez-Marti, F., Capitan-Vallvey, L., Palma, A., Carvajal, M. Passive UHF RFID tag with multiple sensing capabilities. Sensors, 15(10), pp. 26769- 26782 (2015)

[27] Fishkin, K.P., Roy, S. Enhancing RFID Privacy via Antenna Energy Analysis. RFID Privacy Workshop (2003)

[28] Francillon, A., Danev, B., Capkun, S. Relay attacks on passive keyless entry and start systems in <sup>ˇ</sup> modern cars. Proceedings of the Network and Distributed System Security Symposium (NDSS) (2011)

[29] Francis, L., Hancke, G., K.Mayes. A practical generic relay attack on contactless transactions by using NFC mobile phones. International Journal of RFID Security and Cryptography, pp. 92-106 (2013).

[30] Francis, L., Mayes, K., Hancke, G., Markantonakis, K. A location based security framework for authenticating mobile phones. Proceedings of the 2nd ACM International Workshop on Middleware for Pervasive Mobile and Embedded Computing, Bangalore, pp.1-8 (2010)

[31] Gao, X. Strengthening zero-Interaction authentication using contextual co-presence detection. MSc Thesis, University of Helsinki, pp.1-76 (2014)

[32] GDPR, https://eugdpr.org/ (2019)

[33] Greenberg, A. Anybody Can Fire this ’Locked’ Smart Gun with \$15 Worth of Magnets. WIRED, 24 July (2017).

[34] Gurulian, L., Shepherd, C., Markantonakis, K., Akram, RN., Mayes, K. When theory and reality collide: demystifying the effectiveness of ambient sensing for NFC-based proximity detection by applying relay attack data. arXiv:1605.00425v1 [cs.CR] 2 May (2016)

[35] Gurulian, I., Akram, R.N., Markantonakis, K., Mayes, K. Preventing relay attacks in mobile transactions using Infrared light. Proceedings of the Symposium on Applied Computing (SAC17), pp. 1724-1731 (2017a).

[36] Gurulian, I., Markantonakis, K., Shepherd, C., Frank, E., Akram, R.N. Proximity assurances based on natural and artificial ambient environments. International Conference for Information Technology and Communications, Springer, Cham. pp. 83-103 (2017b).

[37] Gurulian, I., Markantonakis, K., Frank, E., Akram, R.N. Good vibrations: artificial ambiencebased relay attack detection. 17th IEEE International Conference on Trust, Security and Privacy, pp. 481-489 (2018).

[38] Halevi, T., Li, H., Ma, D., Saxena, N., Voris, J., Xiang, T. Context-aware defenses to RFID unauthorized reading and relay attacks. IEEE Transactions on Emerging Topics in Computing, pp. 307-318 (2013)

[39] Hancke, G.P., Kuhn, M.G. An RFID Distance Bounding Protocol. Proceedings of the IEEE/Create-Net SecureComm, pp.67-73 (2005).

[40] Hlavac, M., Rosa, T. A note on the relay attacks on e-passports. International Association for Cryptologic Research (2007).

[41] Industry-reports. Mobile Payments Market - Growth, Trends, and Forecast (2019 - 2024). https://www.mordorintelligence.com/industry-reports/mobile-payment-market

[42] Kalamandeen, A., Scannell, A., Lara, E., Sheth, A., LaMarca, A. Ensemble: cooperative proximity-based authentication. Proceedings of the 8th international conference on Mobile systems, applications, and services, ACM, pp. 331-344 (2010)

[43] Kfir, Z., Wool, A. Picking virtual pockets using relay attacks on contactless smartcard systems. Proceedings of the 1st International Conference on Security and Privacy for Emerging Areas in Communication Networks (SecureComm) (2005)

[44] Khattab, A., Jeddi, Z., Amini, E., Bayoumi, M. RFID security threats and basic solutions. RFID Security, Springer, Cham, pp. 27-41 (2017).

[45] Kim, C.H., Avoine, G., Koeune, F., Standaert, F., Pereira, O. The swiss-knife RFID distance bounding protocol, Springer LNCS 5461 (2009).

[46] Li, L., Zhao, X., Xue, G. A proximity authentication system for smartphones. IEEE Transactions on Dependable and Secure Computing, 13(6), pp. 605-616 (2015).

[47] Ma, D., Saxena, N. A context aware approach to defend against unauthorized reading and relay attacks in RFID systems. Security and Communication Networks, 7(12), pp. 2684-2695 (2011).

[48] Ma, D., Prasad, A.K., Saxena, N., Xiang, T. Location-aware and safer cards: enhancing RFID security and privacy via location sensing. Proceedings of the ACM Conference on Wireless Network Security, pp. 51-62 (2012).

[49] Ma, D., Saxena, N., Xiang, T., Zhu, Y. Location-aware and safer cards: enhancing RFID security and privacy via location sensing. IEEE Transactions on Dependable and Secure Computing, 10(2), pp.57-69 (2013).

[50] Marforio, C., Ritzdorf, H., Francillon, A., Capkun, S. Analysis of the communication between col-<sup>ˇ</sup> luding applications on modern smartphones. Proceedings of the ACM Annual Computer Security Applications Conference (ACSAC), pp. 51-60 (2012).

[51] Mehrnezhad, M., Hao, F., Shahandashti, S.F. Tap-Tap and Pay (TTP): preventing Man-In-The-Middle attacks in NFC payment using Mobile Sensors. Second International Conference on Research in Security, pp 1-15 (2014).

[52] Miettinen, M., Asokan, N., Koushanfar, F., Nguyen, T. D., Rios, J., Sadeghi, A. R., Yellapantula, S. I know where you are: Proofs of presence resilient to malicious provers. Proceedings of the 10th ACM Symposium on Information, Computer and Communications Security pp. 567-577 (2015)

[53] Matheson, R. Photovoltaic-powered Sensors for the ‘internet of Things.’ MIT News Office, 27 September (2019).

[54] Mitrokotsa, A., Rieback, M.R., Tanenbaum, A.S. Classifying RFID attacks and defenses. Information Systems Frontiers, 12(5), pp. 491-505 (2010).

[55] Oren, Y., Wool, A. Attacks on RFID-based electronic voting systems. IACR Cryptology, ePrint Archive, 422, (2009).

[56] Pagnin, E., Yangb, A., Hub, O., Hanckeb, G., Mitrokotsa A. HB+DB: Distance bounding meets human based authentication. Future Generation Computer Systems, 80 pp. 627-639 (2018)

[57] Piramuthu, S. Addressing relay attacks without distance-bounding in RFID tag inclusion/exclusion scenarios. International Symposium on Signal Processing and Intelligent Recognition Systems (SIRS), Springer CCIS 968, pp. 147-156 (2018).

[58] Piramuthu, S., Doss, R. On sensor-based solutions for simultaneous presence of multiple RFID tags. Decision Support Systems, 95, pp. 102-109 (2017).

[59] Ranganathan, A., Capkun, S. Are we really close? Verifying proximity in wireless system. IEEE<sup>ˇ</sup> Security and Privacy, pp 52-58, May/June (2017).

[60] Rasmussen, K., Capkun, S. Location privacy of distance bounding. Proceedings of the Annual<sup>ˇ</sup> Conference on Computer and Communications Security (CCS), pp. 149-160 (2008).

[61] Reid, J., Gonzalez Nieto, J.M., Tang, T., Senadji, B. Detecting relay attacks with timing-based protocols. Proceedings of ASIACCS, pp. 204-213 (March 2007).

[62] Saxena, N., Uddin, M.B., Voris, J., Asokan, N. Vibrate-to-unlock: mobile phone assisted user authentication to multiple personal RFID tags. Proceeding of IEEE International Conference on Pervasive Computing and Communications (PerCom), pp 181-188 (2011).

[63] Shrestha, B., Saxena, N., Truong, H. T. T., Asokan, N. Drone to the rescue: Relay-resilient authentication using ambient multi-sensing. International Conference on Financial Cryptography and Data Security, Springer, pp. 349-364 (2014).

[64] Schurmann, D., Sigg, S. Secure communication based on ambient audio. IEEE Transactions on mobile computing, 12(2), pp. 358-370 (2013).

[65] Shrestha, B., Saxena, N., Truong, H. T. T., Asokan, N. Sensor-based proximity detection in the face of active adversaries. IEEE Transactions on Mobile Computing, 18(2), pp. 444-457 (2019).

[66] Shepherd, C., Gurulian, I., Frank, E., Markantonakis, K., Akram, R.N., Panaousis, R., Mayes, K. The Applicability of Ambient Sensors as Proximity Evidence for NFC Transactions. IEEE Symposium on Security and Privacy Workshops, pp.179-188 (2017).

[67] Singh, M., Leu, P., Capkun, S. UWB with Pulse Reordering: Securing Ranging against Relay<sup>ˇ</sup> and Physical Layer Attacks. Network and Distributed Systems Security (NDSS) Symposium, San Diego, pp 1-15 (2019).

[68] Stajano, F., Wong, F-D., Christianson, B. Multichannel protocols to prevent relay attacks. Proceedings of Financial Cryptography, LNCS 6052, pp. 4-19 (2010).

[69] Truong, H. T. T., Gao, X., Shrestha, B., Saxena, N., Asokan, N., Nurmi, P. Comparing and fusing different sensor modalities for relay attack resistance in zero-interaction authentication. IEEE International Conference on Pervasive Computing and Communications, pp. 163-171 (2014).

[70] Trujillo-Rasua, R., Martin, B., Avoine, G. Distance bounding facing both mafia and distance frauds. IEEE Transactions on Wireless Communications, 13(10), pp. 5690-5698 (2014).

[71] Tu, Y.-J., Piramuthu, S. RFID distance bounding protocols. First International EURASIP Workshop on RFID Technology, pp. 67-68 (2007).

[72] Tu, Y.-J., Zhou, W., Piramuthu, S. A novel means to address RFID tag/item separation in supply chains. Decision Support Systems, 115, pp. 13-23 (2018).

[73] Thibaud, M., Chi, H., Zhou, W., Piramuthu, S. Internet of Things (IoT) in high-risk Environment, Health and Safety (EHS) industries: A comprehensive review. Decision Support Systems, 108, pp. 79-95 (2018).

[74] Tu, Y.-J., Piramuthu, S. Lightweight non-distance-bounding means to address RFID relay attacks. Decision Support Systems 102, pp. 12-21 (2017).

[75] Urien, P., Piramuthu, S. Identity-based authentication to address relay attacks in temperature sensor-enabled smartcards. European Conference on Smart Objects, Systems and Technologies (Smart SysTech), pp. 1-7 (2013).

[76] Urien, P., Piramuthu. S. Elliptic curve-based RFID/NFC authentication with temperature sensor pp. 28-36 (2014).

[77] Vaudenay, S. On modeling terrorist frauds. International Conference on Provable Security, Springer, pp. 1-20 (2013).

[78] Wang, J. A secure keyless entry system based on contextual information. MS Thesis, Queen’s University, pp. 1-84 (2019).

[79] Yang, A., Pagnin, E., Mitrokotsa, A., Hancke, G. P., Wong, D.S. Two-hop distance-bounding protocols: Keep your friends close. IEEE Transactions on Mobile Computing, 17(7), pp. 1723- 1736 (2017).

[80] Yum, D.H., Kim, J.S., Hong, S.J., Lee, P.J. Distance bounding protocol for mutual authentication. IEEE Transactions on Wireless Communications, 10(2), pp.592-601 (2010).

## Highlights

• Relay attacks are difficult to identify when they occur

• We provide an overview of existing means to address relay attacks

• Specifically, we consider distance and ambient conditions based approaches

• We discuss issues with these approaches and possible future research directions

![](/api/attachments/P55RSAMU/fulltext/images/3d7d5fadfd3234bec8e3280a4818e73f2a3d727e7483b36e77e00de4cc882352.jpg)  
Figure 1

![](/api/attachments/P55RSAMU/fulltext/images/39a6cf7cdd13efc89691f3a25e3bc20abf7845336c0463fc8a7a78ede2b9f8be.jpg)  
Figure 2

![](/api/attachments/P55RSAMU/fulltext/images/dd44208d80bdfa88ba2dff8602a9a82ba273da9c1e52ab625ca0cc2fcee419cf.jpg)  
Figure 3

![](/api/attachments/P55RSAMU/fulltext/images/71fb8ddbe6a2fee1de1404b2cbd4b7581b374fe645a3beeef5b2512ced263d46.jpg)  
Figure 4

![](/api/attachments/P55RSAMU/fulltext/images/d54b1724b20c44874e0caf6132318f43917fa25a4a226f8ca750892304f523c9.jpg)  
Figure 5

![](/api/attachments/P55RSAMU/fulltext/images/fbd647f991e577659efe33d3bdd6df097482e80e933677e287405714de8c4ec2.jpg)  
Figure 6
