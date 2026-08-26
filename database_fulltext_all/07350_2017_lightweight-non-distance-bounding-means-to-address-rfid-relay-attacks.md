---
otero_id: 7350
otero_key: "E85EHXWN"
title: "Lightweight non-distance-bounding means to address RFID relay attacks"
authors: "Yuju Tu; Selwyn Piramuthu"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.06.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Accepted Manuscript

Lightweight Non-Distance-Bounding Means to Address RFID Relay Attacks

## Yuju Tu, Selwyn Piramuthu

PII: S0167-9236(17)30121-5

DOI: doi: 10.1016/j.dss.2017.06.008

![](/api/attachments/E85EHXWN/fulltext/images/8661e0502ffcb45ae3d4c554272fce339f6b04864249934213f2901d15893180.jpg)

Reference: DECSUP 12859

To appear in: Decision Support Systems

Received date: 31 January 2017

Revised date: 28 May 2017

Accepted date: 29 June 2017

Please cite this article as: Yuju Tu, Selwyn Piramuthu, Lightweight Non-Distance-Bounding Means to Address RFID Relay Attacks, Decision Support Systems (2017), doi:10.1016/j.dss.2017.06.008

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Lightweight Non-Distance-Bounding Means to Address RFID Relay Attacks

Yuju Tu $^{1}$ , Selwyn Piramuthu $^{2,*}$

$^{1}$ Management Information Systems, National Chengchi University, Taipei, Taiwan $^{2}$ Information Systems and Operations Management, University of Florida, USA  
\*corresponding author: selwyn@ufl.edu

## Abstract

A relay attack is accomplished by simply relaying messages between a prover (e.g., an RFID tag) and a verifier (e.g., an RFID reader) with the goal of convincing the verifier of its close physical proximity to the prover. In almost all relay attack scenarios, the verifier essentially communicates with a prover that is outside the verifier's read-range. Relay attacks are notorious since they occur without the knowledge of the reader and/or tag, and has the potential to cause damage to honest parties (here, RFID reader and/or tag). Almost all means to address relay attacks in RFID systems to date are based on the proximity check idea that involves the measurement of message round trip times between tag and reader. With the speed of light at play, such measurements need not necessarily be accurate and could result in the false assumption of relay attack absence. Our review of published literature on approaches that use non-distance-based means to address relay attacks revealed ambient conditions' potential. We critically evaluate ambient conditions and develop a lightweight mutual authentication protocol that is based on magnetometer readings to address relay attacks.

Keywords: RFID, relay attacks, non-distance-bounding, authentication

## 1 Introduction

As RFID (Radio-Frequency IDentification) tags $[6]$ $[7]$ gain widespread adoption and use in several application areas, it is essential to ensure that the security and privacy requirements of the tagged items are satisfied. For example, with RFID-based Passive Keyless Entry and Start (PKES), the key is no longer required to be physically inserted to unlock or start the vehicle. The only requirement is that the physical key is present in or near the vehicle, and there is no need to manually retrieve the key from one's pocket or bag since automated wireless verification seamlessly takes place through an RFID-based mutual authentication mechanism. While this is convenient, wireless authentication opens up the possibility for security threats in the form of relay attacks. As recently reported, it is possible to break into a PKES-enabled vehicle without any need for identity theft or decryption even while the vehicle's key is physically far away from the vehicle $[5]$ $[17]$ . Similarly, when an RFID-enabled credit card is used to pay through wireless means, someone nearby can relay this information to make payments elsewhere $[15]$ $[18]$ $[19]$ $[29]$ . Also, although biometric passports are protected through the use of encryption, the identities in those passports can possibly be wirelessly relayed to facilitate entry through automated border control systems. RFID-enabled voting mechanism leaves the possibility of a similar vulnerability [2] [26] [27] [36] [43].

A good example of relay attack in another domain is the chess grandmaster problem in which a novice simultaneously plays chess with two grandmasters by playing each move of one grandmaster with that of the other grandmaster $[10]$ . The setup is such that each of the grandmasters is led to believe that they are playing against the (same) novice and not against each other $[4]$ . A recent example occurred during the 2010 chess olympiad where Sébastien Feller was found to have obtained outside help during the games $[16]$ .

These (relay) attacks should not be mistaken for classical identity theft. In an RFID system, identity theft necessarily results in an RFID tag successfully impersonating another RFID tag's identity to the reader. A common means to counter identity theft involves prevention of cloning or the copying of identity token or password by unintended parties, whereas such measures do not have any effect on the types of (relay) attacks encountered in these scenarios. For example, banks in some countries commonly use one-time passwords as tokens to verify the identity associated with each transaction. These passwords are designed such that their validity lasts only for a short time duration (e.g., 3 minutes), which is enough to thwart most identity theft attempts. In the case of relay attack, an adversary can prompt for the generation of a new one-time password and relay the conversation without the knowledge of the owner of the compromised account. Relay attack is entirely different from identity theft, and requires far less resource to accomplish.

Relay attacks do not depend on message decryption or the physical separation between reader and tag. These attacks operate by relaying messages between (honest or dishonest) tag and a honest reader where the reader and tag always believe that they are communicating with a honest tag and reader respectively. Relay attacks are among the most severe attacks that are faced by contactless smart cards (e.g., in mobile payment applications), and are relatively easy to accomplish since there is no need to understand or decrypt any of the messages. Given this, it is not trivial to address relay attacks through cryptographic means.

However, one of the common means to address issues that are associated with relay attacks is through the use of cryptography, specifically with the encryption of messages that are passed between tags and readers. Since wireless medium is used to pass messages between tags and readers in almost all of these applications, it is difficult to safeguard these messages from being intercepted, read, and/or modified by unintended parties. Therefore, an important role of encryption in these communications is to ensure that secrets are not unintentionally revealed through these messages. It is also important to prevent adversaries from successfully impersonating tags to readers and vice versa based on passed messages between tag and reader.

RFID cryptography is a very active area of research. Dozens of protocols for various configurations (e.g., single-tag/single-reader, multi-tag/single-reader) have been proposed that address security/privacy vulnerabilities $[28]$ $[39]$ . Almost all of these protocols rely on message encryption to ensure that even a resourceful adversary would be unable to determine secrets through capture and analysis of any/all messages that are passed between any given reader/tag combination. Typical passive RFID tag communication range is within 10 cm for high-frequency tags and up to about 10 meters for ultra high-frequency tags. A majority of RFID authentication protocols implicitly assume that the reader and tag are in close physical proximity of each other since they can communicate with each other only when the tag is in the field of the reader. However, unless the authentication protocols are specifically developed for protection against relay attacks, they are almost certainly vulnerable to such attacks.

Relay attacks come in a few different flavors that include mafia fraud and terrorist fraud. Mafia fraud is where an adversary successfully relays messages between a honest reader and a honest tag $[14]$ . An example of mafia fraud is the use of relayed messages to open a building door using a smart card that is not in close physical proximity to the reader at the door. Terrorist fraud occurs when the tag is dishonest and colludes with the adversary to misrepresent its physical location $[13]$ .

Based on the proximity check idea $[4]$ , Brands and Chaum $[8]$ proposed a protocol to address mafia fraud. The essence of this protocol is the measurement by the verifier of round trip times taken by 1-bit messages between prover and verifier. Hancke $[23]$ illustrated mafia attack with an RFID tag and reader from a distance of 50 meters, and Hancke and Kuhn $[24]$ then developed a distance-bounding protocol based on proximity check for RFID applications. Distance-bounding protocols have since then been implemented in commercially available RFID tags (e.g., MIFARE Plus from NXP).

A core of distance-bounding protocols is their reliance on the relationship between distance and signal travel time. Since signal takes more time to travel farther, an unusual delay could signal the possibility of a relay attack. However, with the speed of light, accuracy is measured in terms of nanoseconds when the distance is in meters. The distance-bounding protocols therefore depend on the accuracy of the clock on the reader-side. To ensure that a tag is just meters away from the reader, the clock needs to have accuracy at nanosecond scale. While this may not necessarily be an issue (e.g., commonly used GPS clocks have accuracies in nanoseconds), the turn-around time at the tag-side might be an issue. In other words, if the turn-around time is in terms of microseconds for whatever reason, it might be difficult to distinguish reader-tag separations that are kilometers apart from those that are just a few meters apart. This necessitates the exploration of other (i.e., non-distance-bounding-based) options to address relay attacks. From our survey of existing literature on RFID relay attacks, it was clear that almost all existing protocols use some distance-bounding variant. To address this void, we consider other possible (e.g., ambient conditions) avenues to approach and address relay attacks.

To this end, we critically examine several possible facets of ambient conditions from the perspective of relay attacks and choose magnetometer readings to determine the tagged item's location and develop a mutual authentication protocol that is secure against relay attacks. Our approach has several merits. First, we avoid the limitations with respect to round-trip distance measurement as in existing distance-bounding protocols. Second, our approach is generalizable across various RFID applications since it is neither sensitive to the tagged item's movement nor restricted to the orientation of the tagged item with respect to reader. Third, it is economically feasible since it relies on already available battery-less passive tag technology that is in accordance with EPC Gen-2 standard.

The contribution of this paper is two-fold: (1) we consider non-distance-bounding alternatives to address relay attacks through detailed evaluation of possible alternatives, and (2) we develop a lightweight authentication protocol with the incorporation of magnetometer readings that is secure against relay attacks. Although we use magnetometer readings in the proposed mutual authentication protocol, the protocol itself is not specific to magnetometer sensors in that any sensor reading can be used as long as the ambient condition measured satisfies basic requirements (e.g., non-directional) for such applications.

The remainder of this paper is organized as follows: We briefly review distance-bounding approaches against relay attacks in the next section. In Section 3, we consider several possible non-distance-bounding options that include both the use of ambient conditions and others where it is possible to use battery-less RFID tags. We then present the proposed protocol and its security analysis in Section 4. We conclude the paper in Section 5 with a discussion on non-distance bounding approach to address relay attack with a specific focus on the proposed protocol.

## 2 Distance-bounding Approaches Against Relay Attacks

Relay attack becomes an issue when close physical proximity of RFID tag and reader cannot be confirmed with certainty. It is not difficult to envision adversaries positioned between tag and reader to relay messages between them when they are physically farther apart and are oblivious to relay attack as it happens.

Distance-bounding approaches to address relay attacks operate with the premise that the distance between two entities (here, RFID tag and reader) can be precisely measured through the round-trip time taken by single bit messages to pass between these entities. While this may be valid under ideal conditions where there is no unintended delay anywhere, it may not necessarily be true in reality. A small delay in (microseconds, for example) turn-around time at the tag side can easily wash out differences in distances of miles vs. meters. The tag needs to receive the bit, decide what to do with it, and then return the bit to the reader. This involves computation time that can easily overshadow the communication time between tag and reader.

We use the following notations throughout the remainder of this paper:

• T: Tag

\- $R$ : Reader

\- ||: Concatenation operator

\- $\oplus$ : Exclusive-OR (XOR) operator

\- $wt_{H}(A)$ : Hamming weight of vector A

\- $\text{rot}(A, \rho)$ : Function to rotate entries in vector A by $\rho$ places

\- $u, v, w, TM, RM$ : $k$ -bit temporary vectors

\- $r_R$ : random $k$ -bit nonce generated by the reader

\- $r_T$ : random $k$ -bit nonce generated by the tag

\- $h$ : keyed hash function

\- $x, y, z$ : tag's $k$ -bit shared secret with the reader

\- $T_{R}$ : tag temperature as measured by the reader

\- $T_{T}$ : tag temperature as measured by the tag

\- $T_{mag}$ : The $k$ -bit measured magnetic field by tag

\- $R_{mag}$ : The $k$ -bit measured magnetic field by reader

\- $\Delta_{mag}$ : Allowed tolerance level for difference in detected magnetic fields

\- $T_{mag*}^{i \in 1..m}$ : A set of $m$ optional $T_{mag}$ generated by reader on the basis of $R_{mag} \pm \Delta_{mag}$

\- $N_{t}$ : $k$ -bit noise generated by tag with a random mix of $\frac{k}{2}$ bits = 1 and $\frac{k}{2}$ bits = 0

\- $N_r$ : $k$ -bit noise generated by reader with a random mix of $\frac{k}{2}$ bits = 1 and $\frac{k}{2}$ bits = 0

\- $A \approx B$ : signifies $wt_H(A \oplus B) = 0.5k$ , where $k = length(A) = length(B)$

\- $P_{R}, P_{T}$ : Public key of the reader and tag respectively

\- $s_{R}, s_{T}$ : Private key of the reader and tag respectively

\- $Q$ : the generator of a cyclic subgroup of points on the elliptic curve for the reader and tag

\- $\epsilon$ : allowed tolerance for temperature difference between reader and tag measurements

\- $f_{a}(b)$ : encrypted value of $b$ with key $a$ and pseudorandom function $f$ ; $f: \{0,1\}^{*} \to \{0,1\}^{2k}$

\- $L, R$ : the left and right parts, $k$ bits each, respectively of the encrypted value

\- $t_i^s, t_i^f$ : start and finish times, respectively, of fast bit iteration $i$

\- $\Delta t_{max}$ : maximum allowed round-trip time

To understand the essentials of distance-bounding protocols, we now discuss the core of the earliest RFID-based distance-bounding protocol that was proposed by Hancke and Kuhn (2005) as illustrated in Figure 1. This protocol comprises two phases, with an un-timed first phase and a timed second phase [24]. The reader has the clock. The first phase is used to generate $R^0 ||R^1$ . During each iteration of the timed phase, either $R^0$ or $R^1$ is chosen at random and a bit from its $(i - 1)^{th}$ position is sent to the tag during the $i^{th}$ iteration. At the end, (a) each of the $n$ round trip times are checked to ensure that it is at most a pre-defined value $(\Delta t_{max})$ and (b) the $R(R^0 \text{ or } R^1)$ values are valid. When either of these tests fails, it signifies the presence of a relay attack, and the protocol is aborted.

Since the first phase is not timed, an adversary can capture and hold $r_{R}$ thereby prolonging the un-timed phase, and repeatedly send a fixed (say, 0) value to the tag during its timed phase and gather all its responses. Then when the reader is ready, upon reception of $r_{T}$ from the adversary, the adversary can impersonate the tag and respond with the R values it captured from the tag. This would only ensure that the adversary is correct in at least half its responses to the reader during the timed phase. For the other half of the time, the adversary can correctly guess 50% of the time on average. This results in an accuracy probability of $\left(\frac{3}{4}\right)^{n}$ in a mafia fraud scenario. However, this protocol is vulnerable to a terrorist fraud attack where a dishonest tag colludes by sharing $R^{0}||R^{1}$ with the adversary and successfully fakes its distance from the reader. Reid et al. (2007) developed a modified protocol in which the (dishonest) tag is forced to not share anything with the adversary since that would involve revelation of its secret information to the adversary [42]. This modified protocol too has its issues, as discussed in [38]. A majority of RFID-based distance-bounding protocols that claim to be resistant to relay attacks include timed one-bit exchanges between tag and reader as their main component to ensure that the distance traveled by the messages reflect the claimed distance between tag and reader. The timed messages are intentionally kept at one bit length to (a) stay in compliance with the goal to keep the computational overhead at the tag side to a minimum and (b) to facilitate measurement of round-trip times as the primary focus with the elimination or reduction of other activities that involve time.

<table><tr><td>Reader(secret x)</td><td></td><td>Tag(secret x)</td></tr><tr><td> $r_{R} \leftarrow \{0,1\}^{m}$ </td><td rowspan="6"> $\xrightarrow{r_{R}}$  $\xleftarrow{r_{T}}$ for  $i = 1..n$ </td><td rowspan="7"> $r_{T} \leftarrow \{0,1\}^{m}$  $R^{0}||R^{1} \leftarrow h(x,r_{T} || r_{R})$  $R_{i} \leftarrow \begin{cases} R^{0}_{i} & \text{if } C_{i} = 0 \\ R^{1}_{i} & \text{if } C_{i} = 1 \end{cases}$ </td></tr><tr><td> $R^{0}||R^{1} \leftarrow h(x,r_{T} || r_{R})$  $C \leftarrow \{0,1\}^{n}$ </td></tr><tr><td>start clock ( $t_{i}^{s}$ )</td></tr><tr><td>stop clock ( $t_{i}^{f}$ )</td></tr><tr><td>check  $R_{i}, \Delta t_{i} = t_{i}^{f} - t_{i}^{s} \leq \Delta t_{max}$ </td></tr><tr><td>Abort process if  $R_{i}, \Delta t_{i}$  invalid</td></tr><tr><td></td><td>End for</td></tr></table>

Figure 1: The distance-bounding protocol of Hancke and Kuhn (2005)

Several minor variations of the distance-bounding protocol with both timed and un-timed phases have been proposed over the years. These protocols include modifications to the outer loop $[48]$ , the use of mixed challenges $[30]$ , response pre-computation $[33]$ , among others. There have also been attempts at measuring round-trip times without the use of single-bit exchanges such as the one in Rasmussen and Čapkun (2008), which was later shown to be vulnerable to mafia fraud attack $[34]$ $[41]$ .

## 3 Non-distance-bounding Approaches Against Relay Attacks

With the dominance of distance-bounding approaches for RFID relay attacks, it is no surprise that there is a paucity of published research that consider means other than distance-bounding ones. We now consider a few approaches that do not include a distance-bounding component to address relay attacks. Other than distance-bounding approaches, published literature on RFID-based relay attacks include those that are based on system noise, ambient conditions, posture recognition, and location awareness.

## 3.1 System Noise

Hamida et al. (2013) use two calibration coil antennas at the reader and card side to develop a means to detect noise due to statistic variations when a relaying communication occurs in an amplifier and forwards relay attacks. Their means is featured with the use of physical layer characteristics. They show through experiments that when relay attacks occur in the far-field channel, the presence of an adversary may impact the noise level in that channel. In other words, they argue that the occurrence of relay attacks must be positively associated with the increase of noise change in communication. However, their method relies on setting up a judgmental threshold in order to determine whether there is a significant increase in noise change variance $[22]$ $[44]$ $[45]$ .

## 3.2 Ambient Conditions

Ambient conditions comprise several different facets that include temperature, humidity, pressure, light intensity, sound, among others. To our knowledge, there are about a handful of published research that either directly or tangentially discuss the use of ambient conditions to address RFID relay attacks. We therefore do not limit our discussion to just these papers and instead critically consider several ambient conditions from the perspective of relay attacks in order to evaluate all feasible options with specific emphasis on available RFID-based sensors.

The core idea with the use of ambient conditions to thwart relay attacks is fundamentally different from that of distance-bounds, although they all share the common goal of identification of relay attacks when they occur. Whereas the physical proximity of RFID tag and reader is verified through one-bit signal transmission time in the distance-bounding protocols, the premise in the approaches that use ambient conditions is that the RFID tag and reader are bound to experience the same ambient conditions when they are in close physical proximity to each other $[11]$ $[21]$ $[37]$ $[46]$ .

Technology advances during the past several years have resulted in improvements in wireless sensors, specifically with respect to their footprint and data transmission capabilities. With their widespread adoption and use, unit sensor cost has come down as well. Their applications span a wide range that include livestock habit monitoring to manufacturing process fault detection. It was also the case that since passive RFID tags do not have access to a power source, the use of associated sensors was beyond question. Recent years have witnessed breakthroughs in this regard as well. For example, we now have WISP (Wireless Identification and Sensing Platform) RFID tags that are essentially battery-free RFID tags with sensing capability at very reasonable cost $[37]$ . Several researchers have considered the use of WISP tags to address relay attacks.

Halevi et al. (2012) illustrate the possibilities of using on-board sound and light sensors for countering relay attack with the use of two (Nokia N97) mobile phones with NFC capability $[21]$ . They experimentally verify sound and light readings without their incorporation in an associated authentication protocol. The reasoning here is that when the two phones are next to each other, they both most likely experience the same light and sound conditions. While this premise is generally true, the fact is that both light and sound waves are directional and the relative orientation of the detection mechanism can affect what is measured. Unless the RFID tag and reader are in close physical proximity with the same orientation and experience no reflection or other effects, it is difficult to ensure that the (sound or light) readings from reader and tag would be the same or even similar.

Another ambient condition that has been considered in published research on relay attacks is temperature. Urien and Piramuthu (2014) consider the use of temperature sensor-enabled WISP RFID tags $[49]$ . As with the use of other ambient conditions, measured temperature by the on-board sensor of an RFID tag would be very similar to that of its reader, if the tag and reader are in close enough physical proximity to each other. Moreover, the observed tag temperature is very difficult to be modified to that of the reader if the tag is far away from the reader. With this consideration, they propose a mutual authentication protocol (Figure 2) that uses both the surface temperature of the tag as measured by itself as well as the reader and a distance-bounding measure with the use of one-bit messages. In that sense, this authentication protocol is not based purely on ambient condition measurements since it also uses the distance-bounding measure.

Urien and Piramuthu (2014) use elliptic-curve cryptography to avoid the key distribution problem. In addition, they use surface temperature measurements of RFID tag by both the tag itself and by the reader $T_{T}$ and $T_{R}$ . They assume that when an RFID reader senses a tag somewhere outside, it is able to scan the surface temperature of the tag. Next, the reader will send the temperature to the tag $T_{R}$ . Similarly, the tag will also scan the temperature on its own and send it to the reader. Thus, they can check with each other on their temperature measurements as a proxy to determine their distance from each other. Ideally, the temperature readings should be very similar, since the RFID tag and reader are physically located close to each other. In other words, if the readings differ within a specific tolerance level ( $\epsilon$ ), the protocol would allow the authentication process to continue. In their experiments, they use infrared temperature scanners. The results show that $27.84(0.24)^{\circ}\mathrm{C}$ and $30.83(0.08)^{\circ}\mathrm{C}$ are the average (standard deviation) tag temperature measurements from a smartcard after it was removed from a wallet on the chip area and the plastic area respectively. $35.23(0.34)^{\circ}\mathrm{C}$ was the temperature measurement of a smartcard that is in a wallet inside a pant pocket. Moreover, such temperature differences are all statistically significant (p < 0.01) according to pair-wise t-test for samples with unequal variances.

Although not related to relay attack, Piramuthu and Doss [40] consider the use of temperature sensors to confirm the close physical proximity and simultaneous presence of two RFID tags in the field of the reader. After considering a few different ambient condition measures such as light, pressure, and sound, they chose temperature as the ambient condition of interest for this application due to its non-directional property.

Among the different ambient conditions that have been discussed in the literature with respect to RFID authentication and related relay attacks, temperature stands out in terms of its non-directionality property. However, temperature may not be suitable for use to thwart relay attacks under all circumstances. For example, it is possible for the tag temperature to be close to that of its reader's ambient temperature during a relay attack even though the tag and reader are miles apart. A worse scenario is where the tag temperature is markedly different from the ambient temperature, with the reader unable to measure the tag's surface temperature even though they are in close physical proximity of each other. For example, an RFID-based authentication in a PKES car key might fail if it's based on temperature since it is possible for a tag that's inside the pocket of the driver to have a tag surface temperature that is close to the person's body temperature which may be significantly different from that of the ambient car temperature.

<table><tr><td>Reader(secret:  $s_R$ )</td><td></td><td>NFC/RFID(secret:  $s_T$ )</td></tr><tr><td> $r_R \leftarrow \{0,1\}^k$  $T_R \leftarrow$  temperatureverify if  $|T_T - T_R| < \epsilon$ if invalid: update  $s_R$  and abort $a_R \leftarrow r_R r_T P_R + P_T s_R T_R$ </td><td> $\overset{P_R}{\rightarrow}$  $\overset{a_T}{\leftarrow}$  $\overset{r_R}{\rightarrow}$  $\overset{a'_T, r_T P_T}{\leftarrow}$  $\overset{a_R}{\rightarrow}$ </td><td> $T_T \leftarrow \text{temperature}; r_T \leftarrow \{0,1\}^k$  $a_T \leftarrow r_T + P_R s_T T_T$  $a'_T \leftarrow r_T r_R P_T + P_R s_T T_T$ verify if  $|T_R - T_T| < \epsilon$ if invalid: update  $s_T$  and abort</td></tr><tr><td> $L||R \leftarrow f_{s_R P_T}(T_T, T_R)$  $\mathcal{X}_R \leftarrow \{0,1\}^k$  $\mathcal{Z}_R \leftarrow (L \oplus R \oplus \mathcal{X}_R)$ start clock ( $t_i^s$ )stop clock ( $t_i^f$ ) $\forall i,$  validate  $\mathcal{Z}_{T_i}$ ;check if  $\Delta t_i = t_i^f - t_i^s \leq \Delta t_{max}$ update  $s_R$ ; abort if invalid</td><td> $\overset{\text{ready}}{\underset{\text{for } i=1..k}{\longrightarrow}}$  $\overset{\mathcal{Z}_{R_i}}{\underset{\substack{\mathcal{Z}_{T_i} \\ \text{End for}}}{\longrightarrow}}$  $\overset{\mathcal{X}_R}{\underset{\substack{\mathcal{X}_T \\ \text{otherwise}}}{\longrightarrow}}$ </td><td> $L||R \leftarrow f_{s_T P_R}(T_T, T_R)$  $\mathcal{X}_T \leftarrow \{0,1\}^k$  $\mathcal{Y}_T \leftarrow s_T$  $\mathcal{Z}_{T_i} \leftarrow \begin{cases} \mathcal{Y}_{T_i} & \text{if } \mathcal{X}_{T_i} == \mathcal{Z}_{R_i} \\ \text{else} & \begin{cases} L_i & \text{if } \mathcal{Z}_{R_i} == 1 \\ R_i & \text{otherwise} \end{cases} \end{cases}$  $\forall i,$  validate  $\mathcal{Z}_{R_i}$ update  $s_T$ ; abort if invalid</td></tr></table>

Figure 2: Temperature use to address relay attacks [Urien and Piramuthu (2014)]

What has not been discussed in existing literature on RFID authentication is the use of the earth's magnetic field to determine the absolute orientation at any RFID tag's location. A magnetometer can be used to measure the magnetic field at any given location which can then be used to verify the location of the tagged entity. Magnetic field measurement has been shown to be a reliable means for location determination (e.g., [47]). To our knowledge, none of the published literature on RFID relay attacks consider the use of magnetometer for this purpose. RFID tags with magnetometer have been commercially available at least since 2013 when Farsens introduced Magneto, a battery-less magnetometer tag that can be used to measure and transmit magnetic field measurement data to an EPC C1G2 reader.

## 3.3 Posture Recognition

Other than ambient conditions, personal patterns can also be used against relay attack. For example, Halevi et al. [20] present a posture-sensing approach. They use magnetometer and accelerometer readings to determine posture and to unlock the WISP RFID tag only when a pre-determined posture is identified. The premise of their approach is that the tag owner's posture can be used in a valid context where RFID tag is truly near reader. For instance, in a possible use of posture recognition to start a car with a variant of PKES (Passive Keyless Entry and Start system), the driver is assumed to be in a pre-defined posture while sitting on the car seat. Thus, their approach verifies the proximity of RFID tag to RFID reader by profiling the patterns of the tag owner's posture. The patterns used here include the postures at real-time and those that are recorded for that person sitting in that car. Thus, if the patterns are matched, the tag would be switched on for communication with the reader. If the patterns do not match, the tag would remain switched off. In other words, the mechanism needs additional training sessions. During the training sessions, the mechanism profiles the owner's postures, such as that with respect to the owner's accessories (e.g., pocket and wallet) and then elicit their patterns. As a result, if the owner changes the patterns when using the tag, the owner needs to go through a new training session to make necessary updates. The results presented in Halevi et al. show that the mechanism is promising. However, they stop with their provision of evidence through experimental data, and do not take a step further to develop an authentication protocol that incorporates this functionality. The average success rate of their mechanism remained acceptable, even in scenarios where owner's postures varied during their experiments. An issue with posture recognition to authenticate driver is the possibility of a high percentage of false positives due to the limited space between the driver's seat and the steering wheel that allows for a rather limited set of posture variants and related calibration challenges.

## 3.4 Location Awareness

A related idea is the use of location-awareness where the physical location of the tag and reader are compared to determine whether they are in close physical proximity to each other. For example, Ma et al. [32] show that the implementation of GPS function in an RFID tag to counter relay attack is feasible. They use a low cost external GPS sensor that is attached to a WISP tag to operationalize their experiment with fixed reader locations. The reader locations are stored in the RFID tag, which gets unlocked and is ready for communication with readers only when it senses that it's in one of the (stored) reader's locations. They show that this setup works reasonably well when the tag is 2, 3, and 5 meters from the reader as well as when the tag is mobile at 15, 25, and 35 miles per hour. The GPS sensor they use has an update rate of once per second. They do not take the next step to show that this could be incorporated in a protocol that automatically accomplishes what they show in multiple manual steps. Some of the challenges with this setup include (a) WISP RFID tag memory, which is about 8KB to enable storage of a reasonable number of reader locations, (b) its applicability when the reader is mobile, (c) the ease with which the tag's GPS measurements is messed with, including issues related with penetration of GPS signals in buildings or thick foliage cover, and (d) form factor, since the GPS sensor that they use is large and inflexible.

<table><tr><td>Type</td><td>Strength</td><td>Weakness</td><td>Literature</td></tr><tr><td>GPS</td><td>convenient</td><td>outdoor use only; easy to jam, spoof, disable</td><td>[3] [9] [12] [32] [37]</td></tr><tr><td>Posture</td><td>ease of use</td><td>directional; calibration challenges</td><td>[11] [20] [46]</td></tr><tr><td>Pressure</td><td>convenient</td><td>easy to replicate, minor variation across short distances</td><td></td></tr><tr><td>Temperature</td><td>not directional</td><td>measurement when tag not in reader&#x27;s line-of-sight</td><td>[21] [49]</td></tr><tr><td>Light</td><td>hard to replicate</td><td>directional</td><td>[20] [40]</td></tr><tr><td>Sound</td><td>hard to replicate</td><td>directional</td><td>[20] [40]</td></tr><tr><td>Magnetic field</td><td>not directional</td><td>variations due to ferromagnetic interference</td><td>[1] [47]</td></tr></table>

Table 1: Profile of context-awareness sensors

## 3.5 Discussion

In sum, the non-distance-based approaches we discussed largely hinges on the quality of sensor data and the appropriateness of the ambient condition for this purpose. According to existing literature, sensor data readings of high quality often have the potential to provide differentiable readings across various locations and orientations that include indoor locations and non-directional setups.

Conventionally, if a sensor measurement of an ambient condition is directional, the quality of that sensor data would be low. For example, although GPS is widely used, the quality of GPS data is rather poor because of various issues. Based on that perspective, the use of temperature is justified since temperature is non-directional. Thus, the quality of temperature sensor data is often higher for applications that involve proximity determination, because the sensor is capable of providing consistent readings regardless of relative tag and reader orientations. However, there are some issues with temperature since the tag temperature may be different from that of its environment and may not necessarily be accurately measured by a reader. This may not necessarily be an issue if only the self-reported (i.e., tag reporting its own temperature and the use of this in the authentication protocol) values are used. However, this will not work if the tag is not visible to the reader as required by an authentication protocol (e.g., [49]).

When properly calibrated, magnetometer measurements can be reliably used to determine proximity of tag to reader. Table 1 summarizes the profile of the ambient conditions/sensors that are possible candidates for addressing relay attacks. We could not find a reference for the use of pressure for this purpose in existing literature. Since there could be other facets of ambient conditions that are better candidates to address relay attacks, the set of ambient conditions considered here is not meant to be complete. However, we are not aware of any other obvious ambient condition candidates.

<table><tr><td>Ambient Sensor</td><td> $T_1$  Mean(StDev.)</td><td> $T_2$  Mean(StDev.)</td><td>p-value (paired two-tailed t-test)</td></tr><tr><td>Light ( $cd/m^2$ )</td><td>8636.33(1514.12)</td><td>11879.67(671.88)</td><td>&lt;&lt; 0.0001</td></tr><tr><td>Pressure (mmHG)</td><td>30.459(0.0019)</td><td>30.458(0.0017)</td><td>0.317</td></tr><tr><td>Sound (dB)</td><td>93.33(3.23)</td><td>101.267(3.237)</td><td>&lt;&lt; 0.0001</td></tr><tr><td>Temperature (F)</td><td>81.7067(0.3383)</td><td>81.6567(0.352)</td><td>0.5581</td></tr><tr><td>Magnetic declination(milliradians)</td><td>111.72(0.087)</td><td>111.74(0.067)</td><td>0.2431</td></tr></table>

Table 2: Ambient condition readings from two sensor-based tags $T_{1}$ and $T_{2}$ in close physical proximity

We experimentally evaluated the sensors mentioned in Table 1, except for GPS and posture sensors since it was not possible for us to obtain usable readings from GPS sensors inside a building and posture sensor use in the original study[20] was for a specific application (automobile driver seat) only. We used results from [40] (Table 2) for all but the magnetometer reading values since the purpose is to measure those readings from two objects that are in close physical proximity of each other. These measurements were obtained with two physically close tags. Each of the entries in the second and third columns in Table 2 were the result of 30 readings. Statistical significance of the differences in the mean values of these pairs of measurements are given in the last column. Based on the statistical significance values, it is clear that measured light and sound values were significantly different for the two tags due to the directionality property of light and sound. The pressure measurement at the two tags were not significantly different. Nevertheless, pressure measurements are not useful for our purpose since it reflects the elevation at the measured location, and elevation doesn't vary over significant distances in most areas. Given its non-directional property, the difference in measured temperature values at the two tags were not statistically significant. The differences in magnetometer declination readings were also not statistically significant. Based on the characteristics of the different sensors discussed above as well as their appropriateness for incorporation in a mutual authentication protocol that also addresses relay attack issues, we decided on the use of magnetometer readings in our proposed protocol. Please note that the protocol itself is generic in the sense that it is sensor-agnostic.

## 4 Proposed Mutual Authentication Protocol

To circumvent issues associated with distance-bounding through round-trip time measurements, we develop a mutual authentication protocol that does not depend on round-trip distance measurement. The protocol also satisfies the following properties: (a) its functionality must not be sensitive to tag movement within the field of the reader, (b) it should not need human input during authentication, (c) all, if any, sensor measured quantities must be independent of directionality at that location, (d) the sensor should be readily available for any passive (i.e., battery-less) tag in accordance with either EPC Gen-2 or WISP standards, and (e) the protocol must be lightweight. We first present and discuss the protocol and then present its security analysis.

## 4.1 Relay Attack-Resistant Mutual Authentication Protocol

The proposed mutual authentication protocol is given in Figure 3. We use readings from magnetometer-enabled RFID tags and reader to operationalize this protocol. Specifically, the core of the protocol is the fact that the two magnetometer readings (i.e., the ones taken by tag and reader) are bound to be the same or very similar when such measurements are taken in close physical proximity of each other. An adversary cannot successfully relay messages between a reader and a tag that's physically farther away from the reader and still pass the authentication test since the tag-read measurement will be significantly different from that at the reader's end. Moreover, unless the adversary identifies vulnerabilities in the authentication protocol that allows for modification of magnetometer reading values in the protocol, it is not possible to accomplish a successful relay attack.

<table><tr><td>Reader [shared secrets: x,y,z]</td><td></td><td>Tag [shared secrets: x,y,z]</td></tr><tr><td>1.Generate  $r_R$ 1.1 u←x ⊕ y ⊕  $r_R$ Abort if no response within pre-specified time6.Detect magnetic field  $R_{mag}$ 7.Generate  $T_{mag*}^{i\in 1..m}$ 8.Verify if there is any  $T_{mag*}^i \approx TM$ ; otherwise, abort9.Generate  $N_r$ 10. $RM \leftarrow T_{mag*}^i \oplus N_r$ 11.w← $rot(z \oplus x, wt_H(TM))$ </td><td>Hello||u $\xrightarrow{\text{Hello||u}}$  $\xleftarrow{v \oplus TM}$  $\xrightarrow{w \oplus RM}$ </td><td>1.2 Abort, if  $wt_H(u \oplus x \oplus y) = 0$ 2.Detect magenetic field  $T_{mag}$ 3.Generate  $N_t$ 4. $TM \leftarrow T_{mag} \oplus N_t$ 5.v← $rot(y \oplus z, wt_H(r_R))$ 12.Verify if  $RM \approx T_{mag}$ ; otherwise, abort</td></tr></table>

Figure 3: The proposed authentication protocol

To ensure that the authentication protocol is lightweight, we only make use of exclusive-OR (XOR) and rotation functions. The RFID tag and reader share three secrets x, y, and z. Our rationale behind the use of three shared secrets instead of just one shared secret between tag and reader is that knowledge of any one of the secret will not compromise the authentication protocol by rendering it vulnerable to attacks by an adversary. To ensure that an adversary does not block messages between reader and tag and disrupting the process, the reader expects a response from the tag after it sends its initial message. If this message from the tag is not received within a pre-specified amount of time, the reader aborts the protocol. Note that all communication between reader and tag occur through wireless medium.

The reader initiates the authentication process by generating a random k-bit nonce $r_{R}$ and XORs this with the XOR of two of its shared secrets $(x \oplus y)$ resulting in u. The reader then sends a hello message along with u to the tag. Upon reception of this message, the tag ensures that $r_{R}$ is non-zero by computing the Hamming distance of $u \oplus x \oplus y$ and aborts the authentication process when the Hamming distance is zero. To proceed, the tag detects the magnetic field $T_{mag}$ and then generates $N_{t}$ , which is a k-bit noise with a random mix of $\frac{k}{2}$ bits = 1 and remainder of the $\frac{k}{2}$ bits = 0. The even split of 0s and 1s is to ensure that its information content is zero and the adversary does not benefit by guessing its value. The tag generates TM by $T_{mag} \oplus N_{t}$ . It also rotates the XOR of two shared secrets $y \oplus z$ by $wt_{H}(r_{R})$ places to generate v. The tag can now generate $v \oplus TM$ , which sufficiently hides its magnetometer reading from an adversary.

Upon reception of $v \oplus TM$ from the tag, the reader generates its own magnetometer reading $R_{mag}$ , which it uses to compare against that from the tag. Since the readings from the magnetometers at the tag and reader side may not necessarily be exactly the same, we allow for some tolerance. Moreover, the difference between the readings, if any, are bound to be minor due to reader calibration. Therefore, the differences are likely only at the least significant bit level in binary representation. So, we consider all possible variants of the least significant bits ( $T_{mag*}^{i\in1..m}$ ) for a match with the knowledge that half of the bits in the tag's readings are flipped. When a match is not found, the authentication protocol is aborted. Otherwise, the reader generates $N_{r}$ , which is a k-bit noise with a random mix of $\frac{k}{2}$ bits = 1 and $\frac{k}{2}$ bits = 0. The reader takes XOR of $N_{r}$ and $T_{mag*}^{i}$ to generate RM. The reader also rotates the XOR of first and third shared secrets ( $x \oplus z$ ) $wt_{H}(TM)$ bits to form w. Next, the reader sends $w \oplus RM$ to the tag. When it receives $w \oplus RM$ , the tag validates RM, and aborts the protocol if RM is invalid.

## 4.2 Security Analysis

The proposed protocol has several characteristics that ensure its security. Freshly-generated nonce $(r_{R})$ is used during every run of the protocol. Moreover, the noise vectors generated by the tag $(N_{t})$ and reader $(N_{r})$ add to this characteristic. Independent magnetic field measurements by both reader and tag and the encryption of messages passed between tag and reader ensures that it is secure against mafia fraud attacks. The protocol is also secure against terrorist attack since a (dishonest) tag has to share its secrets $(y \oplus z)$ with an adversary to accomplish such an attack.

Knowledge of any one of the shared secrets $(x, y, z)$ does not lead to any advantage to the adversary. Knowledge of at least two of the three shared secrets would compromise the security of the protocol. However, it is difficult to retrieve any of the shared secrets from passively observing the messages passed between tag and reader or even through active capture and modification of messages.

We now consider a few specific attacks on such authentication protocols.

Tag/Reader Anonymity: The tag and reader identification information (e.g., secret keys) are protected from the possibility of information leakage since this information can be used to track and/or trace the tag or (mobile) reader. This is significant since knowledge of such information can allow for the possibility of cloning the tag or reader. We include the possibility of the reader being mobile, as is the case in some RFID applications.

Forward Security: If all shared secrets are somehow known to an adversary, these secrets cannot be used to decrypt all earlier messages since TM and RM do not involve these shared secrets and both these are encrypted messages.

Tag/Reader Location Privacy: Since the messages are seemingly random between any two authentication rounds, it is difficult for an adversary to use any of the messages to track the tag and/or the (mobile) reader.

Secrecy/Data Integrity and Authenticity: The integrity of the messages passed between tag and reader is ensured by not sending anything that could compromise the security of the protocol in cleartext. Even though the protocol is lightweight, it is designed to be secure and to maintain its secrets regardless of active or passive attacks from adversaries.

DoS/Desynchronization: Since the shared secret keys are not updated after every authentication round, desynchronization is not an issue. The possibility for Denial of Service (DoS) attacks in the proposed protocol is only through blocking and/or modification of message(s). Blocking messages will not grant an adversary any advantage: the reader waits for acknowledgement message from the tag within a predetermined amount of time, and aborts if this does not happen; since the tag is not expected to have an onboard clock, it is not affected when an adversary blocks the second message from reader to tag since its signature is not the same as the first message from the tag - i.e., the tag can tell a fresh authentication round from one that is in-process and responds accordingly. Modification of any of the messages by an adversary similarly will not allow for protocol compromise.

Passive Replay: Passive replay of any of the three messages that are passed between tag and reader from a previous authentication round will not result in successful authentication due to the existence of $r_{R}$ , $N_{t}$ , and $N_{r}$ that introduce sufficient randomness in the passed messages during each authentication round.

Reader/Tag Impersonation Attack: For an adversary to impersonate a reader to a tag or a tag to a reader it should have the ability to generate messages that seem appropriate and valid to the recipient. In the proposed authentication protocol, the first message (from reader to tag) passes muster. However, since the second message $v \oplus TM$ from tag to reader) depends on $r_{R}$ , and therefore the first message from reader to tag, an adversary cannot send any random message from reader to tag and hope that it is a step in successful impersonation of reader to tag. In other words, an adversary cannot successfully impersonate a reader to the tag. An adversary also cannot successfully impersonate a tag to a reader since it requires knowledge of the secrets $y \oplus z$ .

## 5 Discussion

Relay attacks have the potential to cause serious damage to privacy and security in contactless applications. Existing solutions to relay attack mostly involve some variant of distance-bound, while there is some interest in other approaches such as those related to context awareness. An easy way to avoid relay attacks is by shielding the tag from unintended reads such as a pocket made of RFID-blocking fabric $[35]$ . However, this approach is often not sustainable because it defeats the original intended purpose of automation with minimal human input. Context-awareness has also been used to selectively unlock the devices, but the reliability of such a mechanism depends entirely on related sensors. Some researchers have proposed the use of RFID signal strength measurement to counter relay attack. However, its applicability is limited due to the fact that signal strength is highly prone to errors [25], [29], [31].

Distance-bounding approaches are based on the belief that if the signal travel distance is short, the travel time can not be long. The distance-bounding approaches rely on such a time-distance relationship to check for the physical proximity of RFID tag and reader. The premise of context-awareness approaches is that if RFID tag and reader are near each other, their ambient conditions would be similar. After all, the RFID tag and reader must share similar space if they are near each other. Namely, the context-awareness approaches depend on such a space-wise constraint to verify physical proximity. Both the distance-bounding and context-awareness approaches have been shown in previous studies as reasonably effective defense against relay attacks. However, distance-bounding protocols are vulnerable when the computation/processing time at the tag's side during the fast bit exchange process is in the order of microseconds since this would wash away any accurate round-trip time measurement. This is a serious issue in distance-bounding-based means to address relay attacks.

We therefore considered possible non-distance-bounding approaches to identify relay attacks as they occur. Specifically, we critically evaluated several facets of ambient condition since a reader and tag in close physical proximity should experience the same ambient conditions. For relay attacks to work, an adversary has to either find vulnerabilities in the protocol or somehow ensure that the ambient condition near the tag and reader are identical. Both of these have their own challenges, depending on the strength of the authentication protocol and the ambient condition facet(s) of interest. Our analysis led to our choice of magnetometer reading due to its dominant beneficial characteristics. We then developed a lightweight protocol with the incorporation of magnetometer readings at both the tag and reader levels. Unlike most existing protocols that claim to defend against relay attacks, the proposed authentication protocol uses magnetic field for proximity check. The protocol is flexible in the sense that any sensor readings can be used instead as long as such readings are reliable and valid. Given the limitations that are associated with the use of time to measure distance in such applications, we also do not use the time component for this purpose. We evaluated the protocol against commonly seen vulnerabilities in such authentication protocols and found the proposed protocol to be secure.

A limitation with the proposed protocol is associated with how relay attacks have traditionally been defined. As modeled in existing literature, the adversaries in relay attack scenarios only attempt to show that the actual physical separation between tag and reader is closer than what it is in reality. This is done to show that the tag and reader are indeed in close physical proximity of each other. However, there could be scenarios where an adversary may want to show that the tag and reader are physically farther apart. Our protocol will not work in that scenario since the sensor readings of tag and reader will need to be different. To our knowledge, none of the published authentication protocols that purport to address relay attacks consider this possibility.

The ease with which relay attacks are accomplished and the extensive harm such vulnerability renders, it is necessary to identify relay attacks when they occur and stop the process. While existing authentication protocols that use round-trip time measurements are a good start, they have serious issues. The proposed authentication protocol is a step in the direction of addressing relay attacks with fewer issues.

## References

[1] Akram, R.N., I. Gurulian, C. Shepherd, K. Markantonakis, K. Mayes (2016) “Empirical Evaluation of Ambient Sensors as Proximity Detection Mechanism for Mobile Payments,” arXiv preprint, arXiv:1601.07101., 1-13

[2] Azizi, M., N. Bagheri, A. Mirgadri (2012) “Providing a Distance Bounding Protocol Named Pasargad in order to Defend against Relay Attacks on RFID-Based Electronic Voting System,” International Journal of UbiComp, 2(3) pp. 69-82.

[3] Bacheldor, B. (2009) “Hybrid Tag Includes Active RFID, GPS, Satellite and Sensors,” RFID Journal, February 24.

[4] Beth, T., Y. Desmedt (1990) “Identification tokens - or: Solving the chess grandmaster problem,” CRYPTO LNCS 537, 169-176.

[5] E.Biba (2005) “Does Your Car Key Pose a Security Risk?” http://pcworld.about.net/news/Feb142005id119661.htm.

[6] Bose, I., A.K.H. Lui, E.W.T. Ngai (2011) “The Impact of RFID Adoption on the Market Value of Firms: An Empirical Analysis,” Journal of Organizational Computing and Electronic Commerce, Vol. 21, No. 4, pp. 268-294

[7] Bose I., A.C.M. Leung (2008) “Radio Frequency Identification for Customer Relationship Management,” RFID in Operations and Supply Chain Management: Research and Applications, eds. T. Blecker and G. Huang, Erich Schmidt Verlag Publishing, pp. 273-288.

[8] Brands, S., D. Chaum (1993) “Distance-bounding protocols,” EUROCRYPT, LNCS 765, 344-359.

[9] Buckner, M., R. Crutcher, M.R. Moore, S.F. Smith (2001) “GPS and Sensor-Enabled RFID Tags,” unclassified document, Oak Ridge National Laboratory. http://www.ornl.gov/webworks/cppr/y2001/pres/118169.pdf

[10] J.H. Conway (1976) On Numbers and Games. Academic Press.

[11] Czeskis, A., K. Koscher, J.R. Smith, T. Kohno (2008) “RFIDs and secret handshakes: defending against ghost-and-leech attacks and unauthorized reads with context-aware communications,” Proceedings of the ACM Conference on Computer and Communications Security (CCS), pp. 479-490.

[12] Denning, D.E., P.F. MacDoran (1996) “Location-Based Authentication: Grounding Cyberspace for Better Security,” Computer Fraud & Security, Feb., pp. 12-16.

[13] Desmedt, Y. (1988) “Major security problems with the ‘unforgeable (Feige)-Fiat-Shamir proofs of identity and how to overcome them,” $6^{th}$ Worldwide Congress on Computer and Communications Security and Protection, pp. 147-159.

[14] Desmedt, Y., C. Goutier, S. Bengio (1987) “Special uses and abuses of the fiat-shamir passport protocol,” CRYPTO, LNCS 293, 21-39.

[15] Drimer, S., S.J. Murdoch (2007) “Keep your enemies close: distance bounding against smartcard relay attacks,” Proceedings of the USENIX Security Symposium, pp. 87-102.

[16] FIDE Ethics Commission (2011) Judgement report available at: www.fide.com/images/stories/NEWS\_2012/FIDE/FIDE\_Ethics\_Commission\_Judgement\_in\_the\_case\_French\_Team.pdf.

[17] Francillon, A., B. Danev, S. Capkun (2011) “Relay attacks on passive keyless entry and start systems in modern cars,” Proceedings of the Network and Distributed System Security Symposium (NDSS).

[18] Francis, L., G. Hancke, and K. Mayes (2013) “A practical generic relay attack on contactless transactions by using NFC mobile phones,” International Journal of RFID Security and Cryprography, pp. 92-106.

[19] Francis, L., G. Hancke, K. Mayes, K. Markantonakis (2012) “Practical relay attack on contactless transactions by using NFC mobile phones,” Proceedings of the Workshop on RFID and IoT Security (RFIDsec 2012 Asia), pp. 21-32.

[20] Halevi, T., S. Lin, D. Ma, A.K. Prasad, N. Saxena, J. Voris, T. Xiang (2012) “Sensing-enabled defenses to RFID unauthorized reading and relay attacks without changing the usage model,” Proceedings of the IEEE International Conference on Pervasive Computing and Communications, pp. 227-234.

[21] Halevi, T. D. Ma, N. Saxena, T. Xiang (2012) “Secure Proximity Detection for NFC Devices Based on Ambient Sensor Data,” Proceedings of the European Symposium on Research in Computer Security (ESORICS) pp. 379-396.

[22] Hamida, S.T.B., P.H. Thevenon, J.B. Pierrot, O. Savry, O., C. Castelluccia (2013) “Detecting relay attacks in RFID systems using physical layer characteristics,” Proceedings of the 6th Joint IEEE-IFIP Wireless and Mobile Networking Conference (WMNC), pp. 1-8.

[23] Hancke, G. (2005) “A practical relay attack on ISO 14443 proximity cards,” www.cl.cam.ac.uk/gh275/relay.pdf

[24] Hancke, G., M. Kuhn (2005) “An RFID distance bounding protocol,” SecureComm, 67-73.

[25] Hering, J. (2004) “The BlueSniper ‘rifle,” presented at $12^{th}$ DEFCON, Las Vegas.

[26] Hlavac, M., T.Rosa (2007) “A Note on the Relay Attacks on e-passports,” International Association for Cryptologic Research, http://eprint.iacr.org/2007/244/pdf.

[27] International Civil Aviation Organization (2015) “http://www.icao.int/”.

[28] Kapoor, G., W. Zhou, and S. Piramuthu (2011) “Multi-tag & Multi-owner RFID Ownership Transfer in Supply Chains,” Decision Support Systems, 52(1), pp. 258-270, December.

[29] Kfir, Z., A. Wool (2005) “Picking virtual pockets using relay attacks on contactless smartcard systems,” Proceedings of the 1st International Conference on Security and Privacy for Emerging Areas in Communication Networks (SecureComm), pp. 47-58.

[30] Kim, C.H.. G. Avoine (2009) “RFID distance bounding protocol with mixed challenges to prevent relay attacks,” Proceedings of the International Conference on Cryptology And Network Security pp. 119-133.

[31] Kirschenbaum, I., A. Wool (2006) “How to Build a Low-Cost, Extended-Range RFID Skimmer,” Cryptology ePrint Archive: Report 2006/054.

[32] Ma, D., A.K. Prasad, N. Saxena, T. Xiang (2012) “Location-aware and safer cards: enhancing RFID Security and privacy via location sensing,” Proceedings of the ACM Conference on Wireless Network Security (WiSec), pp. 51-62.

[33] Mauw, S., J. Toro-Pozo, R. Trujillo-Rasua (2016) “A class of precomputation-based distance-bounding protocols,” Proceedings of the IEEE European Symposium on Security and Privacy (EuroS&P), pp. 97-111.

[34] Mitrokotsa, A., C. Onete, S. Vaudenay (2012) “Mafia Fraud Attack against the RC Distance-Bounding Protocol,” Proceedings of the IEEE International Conference on RFID -Technologies and Applications (RFID-TA), pp.74-79.

[35] “RFID-Blocking READY Jeans, Protected by Norton, https://www.betabrand.com/mens-rfid-blocking-pocket-norton-denim-jeans.html.”

[36] Oren, O., A. Wool (2009) “Attacks on RFID-Based Electronic Voting Systems,” IACR Cryptology, ePrint Archive, 422.

[37] Philipose, M., J.R. Smith, B. Jiang, K. Sundara-Rajan, A. Mamishev, S. Roy (2005) “Battery-free wireless identification and sensing,” IEEE Pervasive Computing, 4(1), pp.37-45.

[38] Piramuthu, S. (2007) “Protocols for RFID Tag/Reader Authentication,” Decision Support Systems, 43(3), pp. 897-914, April.

[39] Piramuthu, S. (2011) “RFID Mutual Authentication Protocols,” Decision Support Systems, 50(2), pp. 387-393, January.

[40] Piramuthu, S., R. Doss (2017) “On Sensor-Based Solutions for Simultaneous Presence of Multiple RFID Tags,” Decision Support Systems, 95, March, pp. 102-109.

[41] Rasmussen, K., S. Čapkun (2008) “Location Privacy of Distance Bounding,” Proceedings of the Annual Conference on Computer and Communications Security (CCS). pp. 149-160.

[42] Reid, J., J.M.G. Nieto, T. Tang, B. Senadji (2007) “Detecting Relay Attacks with Timing-Based Protocols, Proceedings of the 2nd ACM Symposium on Information,” Computer, and Communications Security, pp.204-213.

[43] Riha, Z. (2009) “Book Chapter: The Future of Identity in the Information Society,” IFIP Advances in Information and Communication Technology Volume, 298, pp 151-159.

[44] Shen, W., H. Xu, R. Sun, P. Wang (2015) “Research on Defense Technology of Relay Attacks in RFID systems,” International Conference on Computer Science and Intelligent Communication (CSIC 2015), pp. 18-22.

[45] Shoukry, Y., P. Martin, Y. Yona, S. Diggavi, M. Srivastava (2015) “PyCRA: Physical Challenge-Response Authentication For Active Sensors Under Spoofing Attacks,” Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security, pp. 1004-1015.

[46] Shu, Y., Y. Gu, J. Chen (2012) “Sensor-data-enhanced authentication for RFID-based access control systems,” Proceedings of the IEEE Mobile Ad Hoc Sensor Systems (MASS), pp.236-244.

[47] Taghvaeeyan, S., R. Rajamani (2014) “Nature-inspired position determination using inherent magnetic fields,” Technology, 2(2), pp. 161-170.

[48] Tu, Y.-J., S. Piramuthu (2007) “RFID distance bounding protocols,” 1st International EURASIP Workshop on RFID Technology, pp. 67-68.

[49] Urien, P., S. Piramuthu (2014) “Elliptic curve-based RFID/NFC authentication with temperature sensor input for relay attacks,” Decision Support Systems, 59, pp. 28-36.

## Biographical Note

Yu-Ju Tu is Assistant Professor of Information Systems at the National Cheng Chi University in Taiwan. His research interests include RFID systems

Selwyn Piramuthu is Professor of Information Systems at the University of Florida. His research interests include RFID systems

## Highlights

\- A mutual authentication protocol against relay attacks in RFID systems

\- Critically evaluate the use of ambient conditions in RFID authentication protocols

\- Use magnetometer readings in a mutual authentication protocol
