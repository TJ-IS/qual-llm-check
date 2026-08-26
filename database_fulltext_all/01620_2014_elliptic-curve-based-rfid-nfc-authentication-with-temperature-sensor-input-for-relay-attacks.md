---
otero_id: 1620
otero_key: "CEM6NBY8"
title: "Elliptic curve-based RFID/NFC authentication with temperature sensor input for relay attacks"
authors: "Pascal Urien; Selwyn Piramuthu"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.10.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Elliptic curve-based RFID/NFC authentication with temperature sensor input for relay attacks

Pascal Urien <sup>a</sup>, Selwyn Piramuthu <sup>b,c,</sup>⁎

<sup>a</sup> INFRES, TELECOM ParisTech, 75013 Paris, France

<sup>b</sup> Information Systems and Operations Management, University of Florida, USA

<sup>c</sup> RFID European Lab, Paris, France

## a r t i c l e i n f o

Article history: Received 21 June 2013 Received in revised form 28 August 2013 Accepted 16 October 2013 Available online 24 October 2013

Keywords: RFID Mutual authentication Distance bounding protoco Relay attack

## a b s t r a c t

Unless speci<sup>fi</sup>cally designed for its prevention, none of the existing RFID authentication protocols are immune to relay attacks. Relay attacks generally involve the presence of one or more adversaries who transfer unmodi<sup>fi</sup>ed messages between a prover and a veri<sup>fi</sup>er. Given that the message content is not modi<sup>fi</sup>ed, it is rather dif<sup>fi</sup>cult to address relay attacks through cryptographic means. Extant attempts to prevent relay attacks involve measuring signal strength, round-trip distance, and ambient conditions in the vicinity of prover and veri<sup>fi</sup>er. While a majority of related authentication protocols are based on measuring the round-trip distance between prover and veri<sup>fi</sup>er using several single-bit challenge–response pairs, recent discussions include physical proximity veri<sup>fi</sup>cation using ambient conditions to address relay attacks. We provide an overview of existing literature on addressing relay attacks through ambient condition measurements. We then propose an elliptic curve-based mutual authentication protocol that addresses relay attacks based on (a) the surface temperature of the prover as measured by prover and veri<sup>fi</sup>er and (b) measured single-bit round-trip times between prover and veri<sup>fi</sup>er. We also evaluate the security properties of the proposed authentication protocol.

© 2013 Elsevier B.V. All rights reserved

## 1. Introduction

There is a continual trend for systems to gravitate toward automation in order to improve process ef<sup>fi</sup>ciency as well as to reduce errors and vulnerabilities (e.g., [47,48]). Examples of such systems include mobile payment through Near Field Communications (NFC)-enabled smartphones and object identi<sup>fi</sup>cation with RFID tags. While the general ef<sup>fi</sup>ciency and effectiveness in these systems are improved with automation, other challenges arise as a direct consequence. Among these, some of the pressing challenges include those related to privacy and security of the user in these systems as well as attacks from resourceful adversaries.

Several vulnerabilities have been identi<sup>fi</sup>ed in existing systems in a wide variety of applications such as automobiles, mobile payments. For example, in keyless start system, the driver does not need to insert a physical key to start the car. It was shown (e.g., [5]) that it is relatively easy to clone such a car key. In general, the inclusion of human in the loop (e.g., to open the car door) was assumed to reduce such vulnerabilities since starting a car without gaining entry to it is not of much use to the adversary. However, [19] show how both a keyless entry and start system in an automobile can be compromised. Several researchers have studied mobile payment systems with smartphones, and have shown that these transactions are vulnerable due to untrusted readers as well as the presence of adversaries who intermediate the transactions between smartphones and readers (e.g., [20,16,32]). While outright clon ing accounts for some of these vulnerabilities, relay attacks play a significant role as well.

Relay attacks occur when an adversary simply relays signals between (honest) reader and tag without any modi<sup>fi</sup>cation. Since the signal content is not modi<sup>fi</sup>ed by the adversary, almost none of the extant cryptographic RFID authentication protocols are immune to such attacks. Relay attacks work equally well on mutual as well as one-way authentication protocols. Unless it explicitly participates in such an attack (e.g., ma<sup>fi</sup>a fraud attack, discussed below), a prover is generally unaware of a relay attack when it occurs. For example, an adversary can use relay attack to remotely start a car (e.g., [5]) or complete a mobile payment transaction (e.g., [20]).

Relay attacks and their variants have been discussed in the literature since at least a few decades ago (e.g., [10]: p.75; [14]), and there have been several attempts by researchers over the years to reduce the occurrence probability of such attacks. Among the most common are those that measure the round-trip time taken to transfer a single bit between the veri<sup>fi</sup>er and the prover with the assumption that gross deviation from a pre-calculated (based on the speed of light and the expected distance between prover and veri<sup>fi</sup>er) range is a cause for concern. This is also implemented in recently introduced MIFARE cards (e.g., MIFARE Plus X), which is an improvement over their earlier cards (e.g., [21]). However, the measurement of round-trip distance as a proxy for physical proximity determination is fraught with issues including the fact that it is dif<sup>fi</sup>cult to identify relay attacks that are mounted from relatively short distances (e.g., a few kilometers) due to the inherent latency (e.g., default of 5 ms in ISO 14443 proximity cards) that is present in these transactions.

Almost all existing authentication protocols that use a variant of this idea also involve some, even if minimal, computation (e.g., to pop a stack or compare values to choose among several stacks). Any authentication protocol that measures the signal round-trip time is very sensitive to the relative time taken for computation vs. communication [36]. In other words, if computation at the receiver end is multiple orders of magnitude when compared with the round-trip signal travel time, it is dif<sup>fi</sup>cult to measure the latency that is due only to round-trip travel times. Moreover, the computation time also depends on the ambient conditions of the RFID/smartcard processor and a large variation has the potential to wash away differences in signal round-trip times for prover and veri<sup>fi</sup>er that are anywhere from inches to miles apart from each other.

Signal strength has also been suggested as a means to verify physical proximity of prover and veri<sup>fi</sup>er. However, it is easy to modify signal strength. It is also easy to use a stronger signal to read from outside the expected read-range (e.g., BlueSniper ‘ri<sup>fl</sup>e’ [25]). Moreover, such skimmers are relatively inexpensive (≈\$100) and can be assembled using off-the-shelf electronics hobbyist supplies and tools (e.g., [26,30]).

Since round-trip distance measurement and signal strength have their issues, researchers have resorted to identifying other means to address relay attacks. These include the use of environmental sensors and close coupling with another device (e.g., [7]) since these, unlike a request to the user to push a button for example, do not require any action on the user's part and therefore do not interfere with the automated authentication process between prover and veri<sup>fi</sup>er.

The premise that supports the use of ambient conditions to con<sup>fi</sup>rm the relative (physical distance) separation between prover and veri<sup>fi</sup>er is that their ambient conditions must be the same or close enough when these devices are in close physical proximity to each other. Ambient conditions are measured at the prover and veri<sup>fi</sup>er and the measurements are then compared against each other. Ambient conditions in this context include sound, light, temperature, among others. It is known that light and sound measurements are in<sup>fl</sup>uenced signi<sup>fi</sup>cantly by the orientation of the measuring device with respect to the (light or sound) source (e.g., re<sup>fl</sup>ected, incident) and any existing interferences (e.g., standing waves). This necessitates the sensor-generated values to be appropriately compensated and normalized, which is extremely dif<sup>fi</sup>cult due to the sensitivity of the readings to the relative reader and source orientations and the challenges in measuring the relative real-time orientations. We decided not to consider light or sound sensors due to these issues.

We consider the use of environmental sensors, speci<sup>fi</sup>cally temperature sensors, to reduce the occurrence probability of relay attacks. We develop a mutual authentication protocol based on elliptic-curve cryptography that seamlessly integrates both authentication and a means to address relay attacks. We chose elliptic-curve cryptography because it's relatively lightweight when compared against most other public-key cryptography methods. Since the ambient condition near the veri<sup>fi</sup>er can be readily determined by a resourceful adversary, we use the prover's surface temperature instead. This is measured by an on-board temperature sensor on the prover and an appropriate sensor on the veri<sup>fi</sup>er. To reinforce the result based on temperature measurement, we also include a fast bit challenge–response part where round trip times are measured and validated. We believe that the simultaneous use of both temperature and round-trip travel time in our authentication protocol provides a relatively high degree of security. The proposed protocol is for mutual authentication — both the identity of the prover and veri<sup>fi</sup>er as well as the physical separation claimed by these parties are validated.

Throughout the paper, we interchangeably use NFC, RFID, and smartcard to represent the prover. We do this (a) to reinforce the fact that these devices are comparable from a relay-attack perspective and (b) since there's a strong overlap among the technologies and authentication protocols that are associated with these devices.

Based on the proposed mutual authentication protocol, the contributions of this paper are three-fold: (1) use of prover surface temperature for verifying claimed distance separation of prover and veri<sup>fi</sup>er in a mutual authentication protocol, (2) elliptic-curve based public key cryptography for mutual authentication to avoid the key distribution problem, and (3) multi-dimensional (based on both temperature and separation distance as measured by signal round-trip time) to reinforce results from each dimension to address relay attacks.

The remainder of this paper is organized as follows: We provide a brief discussion on relay attacks and their variants known as ma<sup>fi</sup>a attack and terrorist attack as well as their extensions in the next section. In Section 3, we provide an overview of published literature on the use of ambient conditions to address relay attacks. We present the proposed protocol in Section 4 and discuss its security properties in Section 5. We conclude the paper with a brief discussion in Section 6.

## 2. Relay attacks

Relay attacks operate by relaying signals between prover and veri<sup>fi</sup>er without any modi<sup>fi</sup>cation to these messages. By its very nature, these attacks necessarily involve a physical distance component. During the (one-way or mutual) authentication process between an actual prover and veri<sup>fi</sup>er, these entities (prover and veri<sup>fi</sup>er) are in close physical proximity to each other. On the other hand, when the rightful owner or bearer of the prover is unaware of its communication with a veri<sup>fi</sup>er, it's unlikely for this prover and veri<sup>fi</sup>er to be near each other. Researchers have used this observation to develop distance-bounding authentication protocols in which the physical separation of prover and veri<sup>fi</sup>er is determined through single-bit round-trip travel times between prover and veri<sup>fi</sup>er. The basis for distance-bounding protocols that address relay attacks is that no signal travels through space-time faster than light (e.g., [24]). Under this constraint, an adversary cannot increase the signal travel speed to claim a shorter physical separation from the veri<sup>fi</sup>er.

Relay attack comes in several <sup>fl</sup>avors including the distance fraud, ma<sup>fi</sup>a (man-in-the-middle) fraud, and terrorist fraud attacks [13]. The ma<sup>fi</sup>a fraud attack needs two cooperating adversaries — a rogue prover T  and rogue veri<sup>fi</sup>er R . In this setup, the interactions between any pair of honest prover, honest veri<sup>fi</sup>er, rogue prover and rogue veri<sup>fi</sup>er occur as: R–T–R–T. Among the earliest of the distance bounding protocols, Brands and Chaum's [8] protocol includes a series of bit challenge– response exchanges. The round-trip times of these exchanges are then used to corroborate the claimed physical separation between prover and veri<sup>fi</sup>er. While the ma<sup>fi</sup>a fraud attack assumes honest prover and veri<sup>fi</sup>er, the terrorist fraud attack involves a dishonest prover and an honest veri<sup>fi</sup>er. The intention here is for the dishonest prover to convince the honest veri<sup>fi</sup>er that it is indeed present at a claimed location when it really is not. The dishonest prover accomplishes this by collaborating with an adversary. It should be stressed that this collaboration does not involve the prover sharing its secret (e.g., key) information with the adversary.

Over the years, researchers have developed protocols that are claimed to be immune to various forms of relay attacks. For example, Hancke and Kuhn [24] proposed a protocol that is secure against ma<sup>fi</sup>a fraud attack. This protocol has two phases (timed and un-timed). However, no attempt is made to ensure that the parties taking part in these phases are indeed the same. This exposes the protocol to terrorist fraud, where the dishonest prover can easily share necessary information to an adversary without revealing any secret. To address this vulnerability, Reid et al. [39] proposed a modi<sup>fi</sup>ed protocol with a strong link between the timed and un-timed phases. To discourage terrorist fraud attacks on this protocol, knowledge of necessary information for the timed (second) part of the protocol necessitates revelation of secrets.

Since the earlier protocols by Hancke and Kuhn [24] and Reid et al. [39], researchers have proposed several protocols that have attempted to improve on existing protocols in terms of their level of immunity against relay attacks. A majority of the protocols that were proposed follow the general idea of beginning with an un-timed phase where necessary elements to generate the bit-exchange stacks are securely transferred between the prover and veri<sup>fi</sup>er. This phase is then followed by a timed phase where single bits are exchanged between the prover and veri<sup>fi</sup>er and the round-trip times are recorded. These recorded times are then compared against an allowable range, based on the estimated physical distance between prover and veri<sup>fi</sup>er, and relay attack is presumed to be nonexistent when the recorded round-trip times are within reasonable limits [44].

To reduce the likelihood of an attack, as in [24,39], due to the 0 s and 1 s being randomly chosen by the veri<sup>fi</sup>er, Kim and Avoine [27] develop mixed challenges whereby null challenges are sent at random by the prover and the response from the veri<sup>fi</sup>er to these is not evaluated. To minimize guessing and to prevent recovery of secret key in a key-learning attack, Kim et al. [29] added another un-timed phase after the timed phase.

Avoine and Tchamkerten [3] propose a tree-based protocol with an attempt to avoid the interdependencies among the timed-challenges. The secret keys are stored in a binary tree, with the challenges thus generated are based inasmuch as following a branch of the tree. However, in addition to its excessive storage-space requirement, the protocol has been found to be vulnerable to both terrorist and distance fraud attacks [18].

Unlike the protocols with an un-timed and timed phases with several bit-wise challenge–response rounds, Rasmussen and Čapkun proposed a protocol that does not necessitate a large number of timed bit-exchanges between prover and veri<sup>fi</sup>er [38]. They used just one round-trip time to determine whether the prover and veri<sup>fi</sup>er are within expected physical proximity to each other. However, their protocol was later found to be vulnerable with a high probability to ma<sup>fi</sup>a fraud attack [34].

Most of the distance-bounding protocols are one-way in the sense that the veri<sup>fi</sup>er veri<sup>fi</sup>es the identity of and its physical distance from the prover. A few of them, however, consider mutual authentication [37] of prover by veri<sup>fi</sup>er and veri<sup>fi</sup>er by prover. For example, Yum et al. [46], Kim and Avoine [28], and Avoine and Kim[2] propose similar protocols for mutual authentication with minor differences, with [2] assuming the existence of clocks on both prover and veri<sup>fi</sup>er with the implicit assumption that these are not basic passive tags. Moreover, the protocols proposed in [2,28,46] assume that both the prover and veri<sup>fi</sup>er know when they are both ready for the fast bit phase. However, since the prover generally is highly (computational) resource-constrained, it may take (much) longer to encrypt a message and this may necessitate the prover to not be ready when the veri<sup>fi</sup>er begins the fast bit exchange phase. This is a concern since there is no way for the veri<sup>fi</sup>er to check for the prover's readiness to participate in the next (i.e., fast bit exchange) phase. Another concern in these protocols is that they assume that the veri<sup>fi</sup>er knows the identity (and, therefore, the shared secret key) of the prover upon receipt of the <sup>fi</sup>rst message (a freshly generated nonce). Any realistic application is bound to have several tags in the <sup>fi</sup>eld of the reader, and this necessitates some means for the veri<sup>fi</sup>er to uniquely identify each individual prover in its <sup>fi</sup>eld. Although these are only implementation issues, how they are operationalized is not clear from the protocols presented in [2,28,46]. A serious concern is that all [2,28,46] are vulnerable to terrorist attack since the information used in the fast bit exchange phase in these protocols can readily be shared with an adversary [39] without necessarily revealing any of the (dishonest prover) tag's secrets.

Overall, there exist very few formal models and proofs of security of distance-bounding protocols that address relay attacks, and even those have been deemed to be <sup>fl</sup>awed. For example, Dürholz et al.'s [17] attempt at provably secure distance-bounding protocols has been shown to be <sup>fl</sup>awed due to the replacement of pseudorandom function by a random function in a game-reduction proof [6].

## 3. Related literature

The use of ambient conditions for physical proximity check is relatively recent in the literature on relay attacks in RFID/smartcard/NFC systems. The idea here is that since the prover and veri<sup>fi</sup>er are supposed to be in close physical proximity to each other during authentication, the ambient conditions for both the prover and veri<sup>fi</sup>er should be the same or at least very similar to each other. Since the concept of ambient condition is multi-dimensional, researchers have resorted to selecting a single dimension (e.g., light, sound) or a select few for simultaneous consideration. One of the reasons for such initiatives is to automate the authentication process with minimal input from humans since human input is error-prone and it usually lowers the process throughput.

Sensor-enabled RFID has been available since more than a decade (e.g., [9,4]) ago and recent advances in technology as well as the increasing demand for such tags in ambient-condition-critical applications have provided the thrust for lower unit cost as well as the development of sensor-enabled tags with smaller footprint. We now consider a few ambient condition dimensions and discuss published literature in this area.

## 3.1. GPS

The idea that it is possible to verify location through the use of GPS coordinates to ensure that a transaction takes place where it is claimed is not new (e.g., [12]). Recent advances in technology have resulted in the possibility of incorporating low-cost location sensing capabilities in RFID tags.

Ma et al. [31] use a setup with such a sensor-based RFID tag to generate location-based information. They use Intel's WISP (Wireless Identi<sup>fi</sup>cation and Sensing Platform) [35], which is a passively-powered RFID tag that partially implement Class 1 Generation 2 EPC standard, and location-based information to defend against unauthorized reading and relay attacks. Their framework calls for selective unlocking of the RFID tag for communication based on location-awareness as well as the use of location information against relay attacks. Although they do not develop or present any authentication protocols to complement their experimental study, they perform location and speed tests using their setup.

Their general idea is to use the onboard non-volatile EEPROM of about 8 kb to store a list of valid locations at which any given RFID tag can be switched on for communication with a reader. The list is then continually compared against the current location whenever a reader prompts the RFID tag for communication. They take the average of 10 readings over 10 s at each valid location to reduce errors in GPS due to minor deviations in the exact location. Their results show that such a setup can be used error-free for speeds of 15, 25, and 35 mph (these are the speeds they used in their experiments) and location error tolerance of ±2m, ±3m, and ±5m (these are the values they used in their experiments). They also simultaneously varied speed and location and found that at a speed of 25 mph, the read accuracy is 100% for location tolerance of ±20 m at speed tolerances of ±2, 3, and 5 mph as well as at a speed of 35 mph, the read accuracy is 100% only for location tolerance of ±10 m at speed tolerance of ±5 mph, and was only about 96.67% for speed tolerances of ±2 and 3mph. Their test on the accuracy of proximity detection with an error tolerance of about 6.2 showed that only a 1 m distance resulted in 100% accuracy. This study alludes to the seamless integration and automation of GPS-enabled RFID systems for location-aware applications such as the processing of mobile transactions.

It should be noted that the experiment was conducted outside in an environment with clear uninterrupted access to GPS signals. However, GPS signal is relatively easy to block since it is one of the weakest broadcast radio signals. GPS signals cannot penetrate most solid or dense objects such as buildings and mountains, and wet trees with heavy branches and leaves can mask or attenuate GPS signals. To make things worse, it is relatively easy to generate fake GPS signals to fool sensitive timing equipment or to mislead location-based services. Moreover, multipath or re<sup>fl</sup>ected signals can corrupt GPS data. The use of GPS inside buildings, where a majority of transactions occur, is extremely challenging due to these issues.

## 3.2. Posture recognition

The idea here is to recognize and respond in real-time based on the instantaneous posture of the person. Halevi et al. [22] use sensorenabled RFID (with accelerometer and magnetometer) to accomplish this by selectively turning on communication of the RFID tag. Other researchers have also considered the use of accelerometer in RFID applications (e.g., [11,41] and the references therein). As [35,22] use Intel's WISP to operationalize their study. Both [35,22] are of similar structure in the sense that they both use Intel's WISP to illustrate the use of sensor-enabled RFID for measuring ambient conditions and they are both experimental studies to show the gist of the method and do not include an authentication protocol to complement the experiments. As for posture recognition, Halevi et al. use several posture changes (e.g., sit to stand, stand to sit), with and without orientation estimation and device tilt, to estimate the accuracy at which such posture changes can be recognized using accelerometer- and magnetometer-enabled RFID tags. Although the recognition rates were not 100%, they were close enough for certain combinations of posture changes.

## 3.3. Sound and light

As with the use of GPS and posture recognition, light and sound can also be used for physical proximity determination based on the premise that two entities that are in close physical proximity will have similar ambient conditions with respect to sound and light. In the case of user authentication, sensor-based ambient condition measurements can be used to complement those done through cryptographic means.

Halevi et al. [23] evaluate the use of on-board light and sound sensors for validating the presence of an NFC smartphone in close physical proximity to a reader. They use two mobile phones (Nokia N97) to simulate a valid NFC device and RFID reader and use the phone's built-in microphone to record 1 s of continuous audio data. They chose <sup>fi</sup>ve different locations (concert hall, McDonalds, cafe and two libraries) to simultaneously record ambient sound with the two mobile phones. They then compared the time-frequency square distance between each recorded signal from one phone and that from the other phone. Using a classi<sup>fi</sup>er they developed to determine the detection rate for each pair of sample locations, they <sup>fi</sup>nd that audio signal-based correlation technique yields 100% detection rate.

They also use ambient light sensors in two Google Nexus S phones to conduct the next part of their study at the same <sup>fi</sup>ve locations. Their results indicate that both light and sound can be effectively used to detect physical proximity of NFC devices, with ambient sound having a slight edge over ambient light conditions due to their sensitiveness to phone orientation.

Sound and light measurements are signi<sup>fi</sup>cantly affected due to the relative orientation of all present light/sound sources and reader. Interpretation and/or use of results based on ambient light or sound measurements could be grossly misleading due to the challenges associated with directionality of light and sound as well as the characteristics of any existing interferences in their path.

## 3.4. Pressure

We are not aware of any published research on the use of atmospheric pressure to address relay attacks. However, atmospheric pressure does not vary signi<sup>fi</sup>cantly in most nearby locations.

## 3.5. Humidity

We are not aware of any published research on the use of humidity to address relay attacks. Although relative humidity might be a good metric since it varies appreciably across locations, it is dif<sup>fi</sup>cult to measure with a high degree of accuracy in a sensor-based setup.

## 4. The proposed method

As can be seen from the discussion in Section 3, to our knowledge, there is no published (mutual or one-way) authentication protocol against relay attacks that use sensor-based (ambient condition) information at both reader and tag. We attempt to address this de<sup>fi</sup>cit in published literature.

In their paper, Halevi et al. [23] (Section 6.4) mention in the passing that, “Temperature sensors are likely not going to be useful because indoor temperatures at different locations do not vary signi<sup>fi</sup>cantly.” However, in a majority of relay attack scenarios, what matters is not the indoor temperature but rather the RFID/smartcard/NFC smartphone temperature as measured by the reader and that on the RFID tag, smartcard or NFC smartphone as measured by these devices themselves. We conducted an experiment using an infrared temperature scanner to verify this and the results (°C) averaged from thirty observations each are given in Table 1. The <sup>fi</sup>rst and second columns are temperature measurements on a smartcard after it was removed from a wallet – on the chip area and the plastic area respectively. The third column is the temperature measurement of a smartcard that is in a wallet inside a pant pocket. The values in the third column are a mix from the plastic and chip areas, and this is re<sup>fl</sup>ected in the larger variance. The differences between all possible (i.e., columns 1–2, 1–3, 2–3) pairs of these values are statistically signi<sup>fi</sup>cant (p b 0.01) using pair-wise t-test for samples with unequal variances.

As can be seen from Table 1, the temperature measurements need not be the same and could vary signi<sup>fi</sup>cantly depending on whether the tag is inside a purse, in a wallet on the person, or outside by itself and the (chip or plastic) location on the tag where its temperature is measured. Clearly, a realistic relay attack scenario would most likely involve a tag (smartcard or a smartphone) that is on the person (perhaps in a pocket or a wallet in a pocket) and with a temperature closer to human body temperature depending on whether the card is closer to the body or facing the outside. Regardless, when used appropriately and in close physical proximity to the reader, the tag temperature as measured by its own sensor and the reader's sensor would be similar with a very high probability. We use this observation to design our mutual authentication protocol.

## 4.1. System model

We use the example of a smartphone to illustrate the system model.

## 4.1.1. Principals

Our system comprises the following three principals: customer, smartphone and smartphone reader with temperature reader. The smartphone includes an RF-device that incorporates a temperature sensor and the ability to communicate with a reader. The temperature sensor measures the surface temperature of the smartphone. The authentication protocol is instantiated when the smartphone is tapped on the reader. The surface temperature of the smartphone is measured both by the RF-device temperature sensor in the phone and the temperature sensor in the reader.

## 4.1.2. Adversary model

Based on the transaction processing environment, possible threats to the authenticity of the RF-device in the smartphone can originate from manipulated distance between the smartphone and the reader, whereby the adversary reduces the perceived physical separation between smartphone and reader. Other forms of threats include any

## Table 1

Average (standard deviation) tag temperature measurements.

<table><tr><td>Tag (chip area)</td><td>Tag (plastic area)</td><td>Tag (wallet in pocket)</td></tr><tr><td>27.84 (0.24)</td><td>30.83 (0.08)</td><td>35.23 (0.34)</td></tr></table>

form of attack (e.g., replay attack) that would enable a dishonest smartphone to impersonate an honest smartphone.

## 4.1.3. Assumptions

We assume the adversary (A) to follow the Dolev–Yao intruder model [15]. The adversary A has complete control over the communication between the RF-device in the smartphone and the reader whereby A can eavesdrop, block, modify, and inject messages anytime from/to any entity.

We are interested in ensuring that transaction processing between smartphone and reader occurs only when the smartphone and reader are in close physical proximity to each other. We are also interested in ensuring that an adversary is prevented from initiating communication between smartphone and reader without the knowledge of the smartphone owner or owner's representative.

## 4.2. Security properties

The proposed protocols should have the following security properties:

Correctness Only the correct amount as per the transaction initiated by the smartphone owner or the owner's representative is charged.

Unlinkability An adversary cannot link a given smartphone location information to its identity.

Accountability It should be possible to recognize if/when communication between the smartphone and a reader occurs without the explicit knowledge of its owner or owner's representative.

## 4.3. The proposed authentication protocol

We use the following notations throughout the remainder of this paper:

• $r _ { R } \mathrm { : }$ random k-bit nonce generated by the reader

• r<sub>T</sub>: random k-bit nonce generated by the tag

• T : tag temperature as measured by the reader

• $T _ { T } \mathrm { : }$ tag temperature as measured by the tag

$P _ { R } , P _ { T } .$ public key of the reader and tag respectively

• s , s : private key of the reader and tag respectively

• Q: the generator of a cyclic subgroup of points on the elliptic curve for the reader and tag

• : allowed tolerance for temperature difference between reader and tag measurements

• f (b): encrypted value of b with key a and pseudorandom function $f ;$ f $\because \{ 0 , 1 \} ^ { * } \to \{ 0 , 1 \} ^ { 2 k }$

• L, R: the left and right parts, k bits each, respectively of the encrypted value

• t<sup>s</sup>, t<sup>f</sup>: start and <sup>fi</sup>nish times, respectively, of fast bit iteration i

$\Delta t _ { m a x } .$ maximum allowed round-trip time

Given the resource constraints of RFID tags, we use elliptic curvebased public key cryptography to avoid the key distribution problem and to ensure security with minimal computational resources. The security of elliptic curve cryptography depends on the dif<sup>fi</sup>culty of the elliptic curve discrete logarithm problem. For a scalar s, given two points on the elliptic curve P and $Q ( \in E ( \mathbb { F } )$ , where E is an elliptic curve over a <sup>fi</sup>nite <sup>fi</sup>eld ) such that $P = s Q ,$ <sup>ð Þ</sup>it is computationally dif<sup>fi</sup>cult to determine s when s is suf<sup>fi</sup>ciently large. Here, s is the discrete logarithm of P to the base Q. The main operation in elliptic curve cryptography is point multiplication, where s is multiplied with a point Q on the elliptic curve to obtain another point P on the same curve. In our case, knowledge of s Q and Q (similarly, s Q and Q) does not translate to knowledge of $s _ { R }$ (respectively, s ). Q is the generator of a cyclic subgroup of points of the elliptic curve of order k where the elliptic curve discrete logarithm problem is infeasible. The private keys are the secrets (∈[2, k − 1]). We use a variant of [40] as used in [33,45].

It is unclear in some existing distance-bounding protocols (e.g., [24]) as to how a given tag is uniquely identi<sup>fi</sup>ed, and its shared secret is used, with just a random number of input from the reader (since this reader could possibly simultaneously store the shared secrets of several other tags). These protocols do not attempt to authenticate either party by the other, while others explicitly identify the parties in the sent messages (e.g., [39], where the identi<sup>fi</sup>ers are sent in the <sup>fi</sup>rst message from both the parties). In our proposed protocol, the identi<sup>fi</sup>cation information is not shared since we do not use symmetric key cryptography (e.g., [1,42]) and the parties do not share any secret.

The proposed mutual authentication protocol comprises two components for measuring the physical proximity of reader and tag to each other: tag temperature and physical distance as measured by signal round-trip time. The main idea in our protocol (Fig. 1) is to use a temperature sensor-enabled RFID tag (or smartcard or NFC smartphone) that can measure its surface temperature and a temperature-sensor enabled reader that can measure the tag temperature. The measured temperatures are then exchanged between tag and reader and the difference in their temperatures is then checked for validity. When both the tag and reader are in close physical proximity to each other, the temperature difference should be minimal and could be due to variations in the measurement instruments. We use  to capture and account for this variation through appropriate calibration of reader and tag temperature sensors. We also use fast bit exchange between reader and tag, in the second part of the protocol, to generate evidence for the physical separation between prover and veri<sup>fi</sup>er.

The protocol begins when the reader detects the presence of the tag (or a smartcard or smartphone, which can easily be used to replace an RFID tag in the proposed protocol). It generates a fresh random nonce $\left( r _ { R } \right)$ and then sends $P _ { R }$ to the tag. Both the reader and the tag measure the temperature on the surface of the tag (respectively, $T _ { R }$ and T ). The tag then generates a fresh nonce $\left( r _ { T } \right)$ and computes $a _ { T } .$ The tag shares $a _ { T }$ with the reader. The reader then sends $r _ { R }$ to the tag. The tag computes $a _ { T } ^ { \prime } ,$ which it sends along with $r _ { T } P _ { T }$ to the reader, which then veri<sup>fi</sup>es its temperature measurement with that of the tag. The rationale for sending $a _ { T }$ before sending $r _ { T } P _ { T }$ is to avoid man-in-the-middle attack whereby an adversary blocks the tag's messages and modi<sup>fi</sup>es them with the appropriate temperature value before sending them to the reader. With both a and a′, the reader is able to identify any irregularities in the expected values. We do not do the same with $a _ { R }$ since the tag would abort if $T _ { R }$ is not as expected. It should be noted that knowledge of the public key (P<sub>T</sub>) and the generator (Q) does not translate to knowledge of the tag's secret (i.e., s ).

Ideally, the tag is outside (vs. in a wallet on the person, for example) and is scanned by the reader. The reader then computes $a _ { R }$ and shares it with the tag. The tag then veri<sup>fi</sup>es if its self-measured temperature is close to the one measured by the reader. We experimentally determine the maximum allowed variation () and use this to accept or reject a reading based on its claimed location. The temperature readings should be almost the same, barring minor sensor measurement errors, when both the reader and the tag are in close physical proximity to each other. Both the tag and the reader abort the protocol when either of them observe a large deviation $\left( \mathrm { i . e . , } > \epsilon \right)$ in the temperature measurements. Knowledge of the temperature values by the other party would result in the knowledge of their freshly generated random nonce. Even with the knowledge of the unknowns from the tag's side, a resourceful adversary will not be able to manipulate the tag's temperature value sent to the reader for successful authentication since it does not know the reader's temperature measurement before-hand. To reduce the possibility of related attacks in the future, both the reader and the tag update their private keys at the end of each successful authentication round. The details of this update are irrelevant since the public key is updated every time there's an update to the private key. In other words, the reader and tag can each generate a fresh nonce and XOR the private key to generate the new private keys.

<table><tr><td>Reader(secret:  $s_R$ )</td><td></td><td>NFC/RFID(secret:  $s_T$ )</td></tr><tr><td> $r_R \leftarrow \{0,1\}^k$  $T_R \leftarrow$  temperatureverify if  $|T_T - T_R| < \epsilon$ if invalid: update  $s_R$  and abort $a_R \leftarrow r_R r_T P_R + P_T s_R T_R$ </td><td> $\overset{P_R}{\rightarrow}$  $\overset{a_T}{\leftarrow}$  $\overset{r_R}{\rightarrow}$  $\overset{a'_T, r_T P_T}{\leftarrow}$  $\overset{a_R}{\rightarrow}$ </td><td> $T_T \leftarrow \text{temperature}; r_T \leftarrow \{0,1\}^k$  $a_T \leftarrow r_T + P_R s_T T_T$  $a'_T \leftarrow r_T r_R P_T + P_R s_T T_T$ verify if  $|T_R - T_T| < \epsilon$ if invalid: update  $s_T$  and abort</td></tr><tr><td> $L||R \leftarrow f_{s_R P_T}(T_T, T_R)$  $\mathcal{X}_R \leftarrow \{0,1\}^k$  $\mathcal{Z}_R \leftarrow (L \oplus R \oplus \mathcal{X}_R)$ start clock ( $t_i^s$ )stop clock ( $t_i^f$ ) $\forall i,$  validate  $\mathcal{Z}_{T_i}$ ;check if  $\Delta t_i = t_i^f - t_i^s \leq \Delta t_{max}$ update  $s_R$ ; abort if invalid</td><td> $\overset{\text{ready}}{\underset{\text{for } i = 1..k}{\longrightarrow}}$  $\overset{\mathcal{Z}_{R_i}}{\longrightarrow}$  $\overset{\mathcal{Z}_{T_i}}{\underset{\text{End for}}{\longleftarrow}}$  $\overset{\mathcal{X}_R}{\underset{\mathcal{X}_T}{\longleftarrow}}$ </td><td> $L||R \leftarrow f_{s_T P_R}(T_T, T_R)$  $\mathcal{X}_T \leftarrow \{0,1\}^k$  $\mathcal{Y}_T \leftarrow s_T$  $\mathcal{Z}_{T_i} \leftarrow \begin{cases} \mathcal{Y}_{T_i} & \text{if } \mathcal{X}_{T_i} == \mathcal{Z}_{R_i} \\ else & \begin{cases} L_i & \text{if } \mathcal{Z}_{R_i} == 1 \\ R_i & \text{otherwise} \end{cases} \end{cases}$  $\forall i,$  validate  $\mathcal{Z}_{R_i}$ update  $s_T$ ; abort if invalid</td></tr></table>

Fig. 1. The proposed authentication protocol.

In the second part of the protocol, we measure the round-trip time taken by fast bit exchanges between reader and tag. We <sup>fi</sup>rst encrypt the temperature of the tag as measured by the reader and tag to generate L and R, which are the left and right parts of the encrypted value, each of length k bits. To reduce the possibility of replay attack, we use random numbers ( and ). We use $y _ { T } {  } s _ { T }$ to reduce the possibility <sup>X X Y</sup>of a terrorist fraud attack. We also measure the round-trip times taken by each fast bit challenge–response pair. Since the tag may be slower in computing the encryption function, we allow for the tag to <sup>fi</sup>rst send a ready signal to the reader when it is ready for the fast bit exchange phase. The tag's response during the fast bit exchange phase is based on the reader's prompt $\left( \mathrm { i . e . , ~ } \mathcal { Z } _ { R _ { i } } \right)$ . Since the tag chooses from <sup>Z</sup>three different vectors depending on the reader's prompt and the tag's random number, an adversary repeatedly querying the tag just before the fast bit exchange phase (i.e., the pre-ask strategy) would at best only provide the adversary with a <sup>1</sup> probability of successfully authenticating itself as a valid tag to the reader. However, pre-ask strategy will not work in this protocol since the tag will not send at the end of the fast bit exchange part when at least one of the $\mathcal { Z } _ { R _ { i } }$ values is found <sup>Z</sup>to be invalid. We could also set a threshold on the correct number of $\mathcal { Z } _ { R _ { i } }$ values sent from the reader to account for noise in the system.

## 5. Security analysis

## 5.1. Prevention of mafia attack

We reduce the probability of a ma<sup>fi</sup>a attack by verifying that both the tag and reader are in close physical proximity to each other through temperature and round-trip time measurements.

## 5.2. Prevention of replay attack

We reduce the probability of a replay attack by generating a fresh nonce during every round of the protocol. Using freshly generated nonce by the reader and tag makes it hard to impersonate either the tag or the reader.

## 5.3. Prevention of terrorist attack

Similar to the protocol of Reid et al. [39], where the colluding tag could share information on the fast bit exchanges with an adversary, we ensure that the timed fast bit exchange phase includes terms that are meant to be secret $\left( T _ { T } , T _ { R } , S _ { T } \right)$

## 5.4. Forward security

This signi<sup>fi</sup>es that when the current key of a tag is known, it can be used to extract previous messages (assuming that all of its past conversations are recorded). This is prevented by updating the tag's key soon after each authentication round as well as by the freshly generated nonce during every round.

To show that no entity learns (its) forbidden facts, the limitations of the entities need to be modeled and these limitations effectively obstruct these entities from inferring these (forbidden) facts. We now prove the correctness of the <sup>fi</sup>rst part of the proposed protocol using strand space by following the logic presented in ([43]). We use $P _ { N F C }$ to represent the proposed protocol and use guarantees from the responder's and initiator's side through propositions to develop the proof.

We use the following notations for proof using strand space:

$\mathcal { P } , \Sigma \colon$ penetration strand space, strand space

$T , T _ { n a m e } .$ set of text representing atomic messages

• : bundle

$s _ { T } ^ { - 1 } \colon$ inverse (RFID key)

• $K _ { P } \mathrm { : }$ keys known to the penetrator

• ≺: precedence relationship

• ⊏: subset

De<sup>fi</sup>nition 1. An in<sup>fi</sup>ltrated strand space $\mathcal { P } , \Sigma$ is a $P _ { N F C }$ space if Σ is the union of three kinds of strands.

1. Penetrator strands $s { \in } { \mathcal { P } }$

<sup>P</sup>2. Initiator strands with trace Init[Reader, RFID, $P _ { T } , Q , P _ { R } ]$ , de<sup>fi</sup>ned to be $\langle - P _ { T } , - Q , + P _ { R } , + Q , r _ { R } r _ { T } P _ { R } + P _ { T } s _ { R } T _ { R } , r _ { T } r _ { R } P _ { T } + P _ { R } s _ { T } T _ { T } \rangle$ , where Reader, R $\mathrm { \bar { \cdot } I D } \in T _ { n a m e }$ but $P _ { R } , Q \not \in { \mathrm { T } } _ { n a m e }$

3. Its complement, the responder strands with trace Resp[Reader, RFID, $P _ { R } , Q , P _ { T } ]$ , de<sup>fi</sup>ned to be $\langle + P _ { T } , + Q , - P _ { R } , - Q , r _ { R } r _ { T } P _ { R } + P _ { T } S _ { R } T _ { R } , r _ { T } r _ { R } P _ { T } +$ $P _ { R } s _ { T } T _ { T } \rangle$ , where Reader, ${ \mathrm { R F I D } } \in \mathrm { T } _ { n a m e }$ but $P _ { T } , Q \notin \mathrm { T } _ { n a m e }$

## 5.4.1. The responder’s guarantee: Agreement

## Proposition 1. Suppose:

1. Σ is a $P _ { N F C }$ space and is a bundle containing a responder's strand s <sup>C</sup>with trace Resp[Reader, RFID, $P _ { T } , Q , P _ { R } ] ;$

2. $s _ { T } ^ { - 1 } \notin K _ { P } ;$ and

3. $P _ { T } \neq Q , P _ { R } \neq Q$ and $P _ { T } , Q$ uniquely originate in Σ then contains an initiator's strand t with trace Init[Reader, RFID, $P _ { T } , Q , P _ { R } ]$

We prove this proposition using the following lemmas.

Lemma 1. $P _ { T } , Q$ originate at the second message (the one from the RFID tag).

We know $P _ { T } , Q \mathsf { \sqsubset R F I D } \left( \mathsf { s a y } \right.$ , node $n _ { o } )$ ) and the sign for the second message (say, $\nu _ { o } )$ is positive since it originates from RFID. We, therefore, <sup>V</sup>need to verify that $P _ { T } , Q$ are not in the preceding node (here, Reader) in the strand, which is the preceding node on this strand. I.e., $P _ { T } , Q \neq P _ { R } , Q $ $P _ { T } , Q \neq s _ { T }$ . These are all true by de<sup>fi</sup>nition.

Lemma 2. The set $S = \{ \boldsymbol { \mathrm { n } } \in \mathcal { C } \colon P _ { T } , Q \sqsubset t e r m ( \boldsymbol { n } ) \land \nu _ { o } \forall t e r m ( \boldsymbol { n } ) \}$ has a ≼-minimal node $n _ { 2 } .$ <sup>C</sup>. The node $n _ { 2 }$ is regular with a positive sign.

We need to check if $\dot { n } _ { 2 }$ lies on a penetrator strand p.

S. If g h ⊏ term(m), where m is a positive node on a strand $p ^ { \prime }$ of kind S, then $\mathrm { g h } \sqsubset \mathrm { t e r m } ( \langle p ^ { \prime } , 1 \rangle )$ . Minimality of m in T is contradicted by $\langle p ^ { \prime } , 1 \rangle \prec m$

E. (D.) If g $\mathrm { h } \sqsubset \mathrm { t e r m } ( m )$ , where m is a positive node on a strand $p ^ { \prime }$ of kind E (D, respectively), then $\mathrm { ~ g ~ h ~ } \sqsubset \mathrm { t e r m } ( \langle p ^ { \prime } , 2 \rangle )$ ). Minimality of m in T is contradicted by $\langle { p ^ { \prime } , 2 } \rangle \prec m .$

C. If g h term(m), where m is a positive node on a strand $p ^ { \prime }$ of kind C and m is minimal in T, then $\mathrm { ~ g ~ h ~ } = \mathsf { t e r m } ( m )$ and $p ^ { \prime }$ has trace $\langle - g , - h , + g h \rangle$ . This contradicts the minimality of $n _ { 2 }$ in S since $\mathrm { t e r m } ( \langle p ^ { \prime } , 1 \rangle ) = \mathrm { t e r m } ( n _ { 2 } )$ and $\langle p ^ { \prime } , 1 \rangle \prec n _ { 2 }$

Lemma 3. Node $n _ { 2 }$ follows $n _ { 1 }$ on the same regular strand t, and $\mathrm { t e r m } ( n _ { 1 } ) = \{ P _ { T } , Q , r _ { T } r _ { R } P _ { T } + P _ { R } s _ { T } T _ { T } \}$

From Lemma 1 and by de<sup>fi</sup>nition, we know that $P _ { T } , Q$ originate at $n _ { o }$ and its uniqueness in Σ. We also know that $n _ { 2 } \neq n _ { o }$ since $\nu _ { o } \sqsubset t e r m ( n _ { o } )$ and $\nu _ { o } \downarrow t e r m ( n _ { 2 } )$ . Therefore, $P _ { T } , Q$ do not originate at $n _ { 2 }$ and there is a node $n _ { 1 }$ preceding $n _ { 2 }$ on the same strand such that $P _ { T } , Q \sqsubset t e r m ( n _ { 1 } )$ By the minimality property of $n _ { 2 } , P _ { T } , Q , r _ { T } r _ { R } P _ { T } + P _ { R } s _ { T } T _ { T } \sqsubset$ term(n ). Here, $P _ { T } , Q , r _ { T } r _ { R } P _ { T } + P _ { R } s _ { T } T _ { T } = \mathrm { t e r m } ( n _ { 1 } )$ since no regular node contains an encrypted term as a proper sub-term.

Lemma 4. The regular strand t containing $n _ { 1 }$ and $n _ { 2 }$ is contained in and is an initiator strand.

If t were a responder strand, it would contain only a subsequent negative node. Here, $n _ { 2 }$ is a positive node. The last node of t (i.e., $n _ { 2 } ,$ which follows $n _ { 1 } )$ as well as the previous nodes are contained in .

Lemmas 3 and 4 prove Proposition 1.

## 5.4.2. The initiator's guarantee: Secrecy & agreement

## Proposition 2. Suppose:

1. Σ is a $P _ { N F C }$ space and is a bundle containing an initiator's strand s with trace Init[Reader, RFID, $P _ { T } , Q , P _ { R } ] ,$

2. $s _ { T } ^ { - 1 } \notin K _ { P } ;$ and

3. $P _ { R } ,$ Q uniquely originate in Σ then for all nodes $m { \in } { \mathcal { C } }$ such that $P _ { R } ,$ $Q \subset t e r m ( m )$ either $P _ { R } , \ Q , \ r _ { R } r _ { T } P _ { R } \ + \ P _ { T } s _ { R } T _ { R } \ \sqsubset \ t e r m ( m )$ or $P _ { T } , \ Q$ $r _ { T } r _ { R } P _ { T } + P _ { R } s _ { T } T _ { T } \sqsubset t e r m ( m )$

Proposition 3. Suppose:

1. Σ is a P space and is a bundle containing an initiator's strand s <sup>C</sup>with trace Init[Reader, RFID, $P _ { T } , Q , P _ { R } ] ,$

2. $s _ { T } ^ { - 1 } \notin K _ { P } ;$ and

3. $P _ { R } Q$ uniquely originate in Σ then contains the <sup>fi</sup>rst two nodes of a <sup>C</sup>responder's strand t with trace Resp[Reader, RFID, $P _ { T } , Q , P _ { R } ]$

The set $\{ \mathsf { m } { \in } \mathcal { C } : P _ { T } , Q , r _ { T } r _ { R } P _ { T } + P _ { R } s _ { T } T _ { T } \mathbb { \subset } t e r m ( m ) \}$ is non-empty <sup>f gC þ ð Þ</sup>since it contains 〈s,2〉. I.e., it contains a minimal member $( m _ { o } )$ . Now, the regular strand t can be shown to have trace Resp[Reader, RFID, $P _ { T } ,$ $\mathrm { ~ \ i ~ { ~ Q ~ } ~ } { \cal P } _ { R } ] \mathrm { ~ i f ~ } m _ { o }$ lies on t. The regular strand t can also be shown to have at least two nodes in . However, if $m _ { o }$ lies on a penetrator strand t, then t can be shown to be an E-strand with trace $\langle - s _ { T } , - P _ { T } , - Q , + Q ,$ $+ P _ { T } , r _ { T } r _ { R } P _ { T } + P _ { R } s _ { T } T _ { T } \rangle$ . However, this contradicts Proposition $^ { 2 , }$ which implies that $P _ { R } , Q$ do not appear in the form shown in node 〈t,2〉.

As in $[ 2 8 ]$ , we now consider the probabilities of successful ma<sup>fi</sup>a and distance fraud attacks.

## 5.5. Mafia fraud

The proposed protocol does not have a separate set of prede<sup>fi</sup>ned and random challenges as in [28]. Moreover, a pre-ask strategy along with necessary random guesses will result in successfully responding to only half the challenges from the reader on average. This is because the tag chooses its response from three vectors and guaranteed responses can only be obtained when either $L _ { i }$ or $R _ { i }$ is chosen with a probability of 0.25 each. Regardless, for any given challenge from the reader, since the response is binary the probability of a correct response is $_ { 0 . 5 }$ We use the same de<sup>fi</sup>nitions of events as in [28] to motivate this part of the study. The events considered are:

$\overline { { a } } _ { i } \mathrm { : }$ attack not detected by reader at ith round

• b : attack is detected by tag at ith round

• $b _ { i } \colon$ attack not detected by tag at ith round

${ \overline { { A } } } _ { i } \colon$ attack not detected by reader until ith round

$B _ { i } \colon$ <sup>fi</sup>rst time detection of attack by tag at ith round

${ \overline { { B } } } _ { i } \colon$ attack not detected by tag until the ith round

We now determine the probability of not being detected by the reader until the ith round $( P ( i ) )$ as given by:

$$
P (i) = P \Big (\overline {{A}} _ {i} | \overline {{B}} _ {i} \Big) P \big (\overline {{B}} _ {i} \big) + \sum_ {k = 1} ^ {i} P \Big (\overline {{A}} _ {i} | B _ {k} \Big) P (B _ {k})\tag{1}
$$

We <sup>fi</sup>rst calculate the individual terms in $P ( i )$ and then put them together.

$$
P \left(\overline {{A}} _ {i} | \overline {{B}} _ {i}\right) = \prod_ {j = 1} ^ {i} P \left(\overline {{a}} _ {j} | \overline {{b}} _ {j}\right) = \prod_ {j = 1} ^ {i} \left(\frac {1}{2}\right) = \left(\frac {1}{2}\right) ^ {i}\tag{2}
$$

$$
P (\overline {{B}} _ {i}) = \left(\frac {1}{2}\right) ^ {i}.\tag{3}
$$

Similarly,

$$
P (B _ {k}) = \left(1 - \frac {1}{2}\right) ^ {k - 1} \frac {1}{2} = \left(\frac {1}{2}\right) ^ {k},\tag{4}
$$

$$
P \left(\overline {{A}} _ {i} | B _ {k}\right) = \prod_ {j = 1} ^ {k - 1} P \left(\overline {{a}} _ {i} | \overline {{b}} _ {j}\right) \prod_ {j = k} ^ {i} P \left(\overline {{a}} _ {j} | b _ {k}\right) = \prod_ {j = 1} ^ {k - 1} \frac {1}{2} \prod_ {j = k} ^ {i} \frac {1}{2},
$$

and this equals,

$$
P \left(\overline {{A}} _ {i} \mid B _ {k}\right) = \left(\frac {1}{2}\right) ^ {i}.\tag{5}
$$

From Eq. (1)–(5), we get

$$
P (i) = \left(\frac {1}{2}\right) ^ {i} \left(\frac {1}{2}\right) ^ {i} + \sum_ {k = 1} ^ {i} \left(\frac {1}{2}\right) ^ {i} \left(\frac {1}{2}\right) ^ {k} = \left(\frac {1}{2}\right) ^ {i}.\tag{6}
$$

This is the same as the probability of impersonation with no prior knowledge.

## 5.6. Distance fraud

For a dishonest tag wanting to provide the (false) impression of (usually, closer) physical distance to the reader, knowledge of the challenge prior to the beginning of the fast bit challenge phase could help the tag send in its response before it receives the challenges. However $\mathcal { X } _ { R }$ in the challenge is unknown to the tag and it therefore cannot mount a distance fraud attack and succeed, on average, better than random chance.

## 6. Discussion and conclusion

Relay attacks are dif<sup>fi</sup>cult to prevent since these attacks do not depend on cryptography. Moreover, these attacks are passive, and occur without the knowledge of the tag as well as the reader involved. Of the means that have been proposed in the literature thus far, a majority are based on measuring the round-trip travel time for signals between tag and reader. Given recent advances in sensor-enabled RFID tags, it is now economically viable to incorporate these tags in a wider array of applications. We considered the use of temperature sensor-enabled tags for addressing relay attacks. Unlike a majority of distance-bounding protocols that measure only the round-trip times taken by fast bit challenges, we propose the measurement of the surface temperature of the tag as measured by the tag itself and by the reader in addition to distance-based validation. When the tag is in close physical proximity to the reader, as is often the requirement in RFID/smartcard/NFC applications, the temperature measurement of the tag's onboard sensor should be very close to that which is measured by the reader. It is rather dif<sup>fi</sup>cult to modify the temperature of the tag, to what is measured by the reader, when the tag is with its rightful owner who is far away from the reader. Moreover, the proposed authentication protocol renders it dif<sup>fi</sup>cult for the adversary to respond appropriately to the reader with a modi<sup>fi</sup>ed temperature reading.

As NFC applications become prevalent with the use of, for example, mobile payment with smartphones or item-level identi<sup>fi</sup>cation of objects through RFID tags, it is critical to ensure that the security and privacy of users as well as the integrity of transactions are maintained. Given that relay attacks are among the most dif<sup>fi</sup>cult to prevent in RFID/smartcard/NFC applications, there is an urgent need to develop means to address this issue. To our knowledge, this is the <sup>fi</sup>rst paper that uses physical proximity-based information determined through temperature sensors as a part of a mutual authentication protocol to address relay attacks in RFID/smartcard/NFC applications. We hope that this paper encourages other researchers in the area to develop protocols using multiple approaches that synergistically work together to resist attacks from resourceful adversaries.

## Acknowledgments

We thank the two reviewers for carefully reading the paper and for their constructive suggestions. These suggestions have helped us improve the content and presentation of this paper.

## References

[1] G. Avoine, M. Bingol, X. Carpent, S. Yalcin, Privacy-friendly authentication in RFID systems: on sub-linear protocols based on symmetric-key cryptography, IEEE Transactions on Mobile Computing 12 (2013) 2037–2049

[2] G. Avoine, C.H. Kim, Mutual distance bounding protocols, IEEE Transactions on Mobile Computing 12 (2013) 830–839.

[3] G. Avoine, A. Tchamkerten, An ef<sup>fi</sup>cient distance bounding RFID authentication protocol: balancing false-acceptance rate and memory requirement, Proceedings of the Conference on Information Security (ISC). 2009 pp 250–261

[4] B. Bacheldor, Hybrid tag includes active RFID, GPS, satellite and sensors, RFID Journal (February 24 2009).

[5] E. Biba, Does Your Car Key Pose a Security Risk? RFID Chips in Keyless Entry Systems and ExxonMobil's Speedpass Can Easily be Hacked, Study Finds, http://pcworld. about.net/news/Feb142005id119661.htm2005

[6] I. Boureanu, A. Mitrokotsa, S. Vaudenay, On the pseudorandom function assumption in (secure) distance-bounding protocols — PRF-ness alone does not stop the frauds! Proceedings of LATINCRYPT, 2012, pp. 100–120.

[7] C. Boursier, P. Girard, C. Mourtel, Activation des Cartes à Puce sans Contact à l'insu du Porteur. Symposium sur la Sécurité des Technologies de l'information et des Communications (SSTIC). 2008 pp. 1–12

[8] S. Brands, D. Chaum, Distance-bounding protocols. Advances in cryptology — EUROCRYPT '93 Lecture Notes in Computer Science 765 (1994) 344–359

[9] M. Buckner, R. Crutcher, M.R. Moore, S.F. Smith, GPS and Sensor-Enabled RFID Tags, unclassi<sup>fi</sup>ed document, Oak Ridge National Laboratory, 2001, (http://www.ornl.gov/ webworks/cppr/y2001/pres/118169.pdf).

[10] J.H. Conway, On Numbers and Games, Academic Press, 1976.

[11] A. Czeskis, K. Koscher, J.R. Smith, T. Kohno, RFIDs and secret handshakes: defending against ghost-and-leech attacks and unauthorized reads with context-aware communications, Proceeedings of the ACM Conference on Computer and Communications Security (CCS), 2008, pp. 479–490

[12] D.E. Denning, P.F. MacDoran, Location-based authentication: grounding cyberspace for better security, Computer Fraud & SecurityFeb. 1996. 12–16.

[13] Y. Desmedt, Major security problems with the ‘unforgeable’ (Feige)–Fiat–Shamir proofs of identity and how to overcome them, Proceedings of the Securicom 88, 6<sup>th</sup> Worldwide Congress on Computer and Communications Security and Protection, 1988, pp. 147–159.

[14] Y. Desmedt, C. Goutier, S. Bengio, Special uses and abuses of the Fiat–Shamir passport protocol, Proceedings of the Advances in Cryptology (CRYPTO) Springer LNCS 293, 1987, pp. 21–39.

[15] D. Dolev, A.C.-C. Yao, On the security of public key protocols, IEEE Transactions on Information Theory 29 (2) (1983) 198–207.

[16] S. Drimer, S.J. Murdoch, Keep your enemies close: distance bounding against smartcard relay attacks, Proceedings of the USENIX Security Symposium, 2007, pp. 87–102.

[17] U. Dürholz, M. Fischlin, M. Kasper, C. Onete, A formal approach to distance-bounding RFID protocols, Proceedings of the International Conference on Information Security (ISC), 2011, pp. 47–62.

[18] M. Fischlin, C. Onete, Provably secure distance-bounding: an analysis of prominent protocols, IACR Cryptology ePrint Archive 2012, 1282012.

[19] A. Francillon, B. Danev, S. Čapkun, Relay attacks on passive keyless entry and start systems in modern cars, Proceedings of the Network and Distributed System Security Symposium (NDSS), 2011.

[20] L. Francis, G. Hancke, K. Mayes, K. Markantonakis, Practical relay attack on contactless transactions by using NFC mobile phones, Proceedings of the Workshop on RFID and IoT Security (RFIDsec 2012 Asia), 2012, pp. 21–32.

[21] G.d.K. Gans, J.-H. Hoepman, F.D. Garcia, A practical attack on the MIFARE classic, Proceeding of the 8<sup>th</sup> IFIP WG 8.8/11.2 International Conference on Smart Card Research and Advanced Applications (CARDIS), 2008, pp. 267–282.

[22] T. Halevi, S. Lin, D. Ma, A.K. Prasad, N. Saxena, J. Voris, T. Xiang, Sensing-enabled defenses to RFID unauthorized reading and relay attacks without changing the usage model, Proceedings of the IEEE International Conference on Pervasive Computing and Communications (PerCom), 2012, pp. 227–234.

[23] T. Halevi, D. Ma, N. Saxena, T. Xiang, Secure proximity detection for NFC devices based on ambient sensor data, Proceedings of the European Symposium on Research in Computer Security (ESORICS), 2012, pp. 379–396.

[24] G.P. Hancke, M.G. Kuhn, An RFID distance bounding protocol, Proceedings of the JEEE/Create-Net SecureComm. 2005 pp. 67-73

[25] J. Hering, The BlueSniper ‘ri<sup>fl</sup>e’, presented at 12<sup>th</sup> DEFCON, Las Vegas, 2004.

[26] Z. K<sup>fi</sup>r, A. Wool, Picking virtual pockets using relay attacks on contactless smartcard systems, Proceedings of the 1<sup>st</sup> International Conference on Security and Privacy for Emerging Areas in Communication Networks (SecureComm), 2005, pp. 47–58.

[27] C.H. Kim, G. Avoine, RFID distance bounding protocol with mixed challenges to prevent relay attacks, Proceedings of the International Conference on Cryptology and Network Security (CANS). 2009 pp. 119–133

[28] C.H. Kim, G. Avoine, RFID distance bounding protocols with mixed challenges, IEEE Transactions on Wireless Communications 10 (5) (2011) 1618–1626.

[29] C.H. Kim, G. Avoine, F. Koeune, F.-X. Standaert, O. Pereira, The Swiss-knife RFID distance bounding protocol, Proceedings of the International Conference on Information Security and Cryptology (ICISC), 2008, pp. 98–115.

[30] I. Kirschenbaum, A. Woo, How to build a low-cost, extended-range RFID skimmer Cryptology ePrint Archive: Report 2006/0542006.

[31] D. Ma, A.K. Prasad, N. Saxena, T. Xiang, Location-aware and safer cards: enhancing RFID Security and privacy via location sensing, Proceedings of the ACM Conference on Wireless Network Security (WiSec), 2012, pp. 51–62.

[32] C. Marforio, H. Ritzdorf, A. Francillon, S. Čapkun, Analysis of the communication between colluding applications on modern smartphones, Proceedings of the ACM Annual Computer Security Applications Conference (ACSAC), 2012, pp. 51–60.

[33] S. Martínez, M. Valla, C. Roig, J.M. Miret, F. Giné, A secure elliptic curve-based RFID protocol, Journal of Computer Science and Technology 24 (2) (2009) 309–318.

[34] A. Mitrokotsa, C. Onete, S. Vaudenay, Ma<sup>fi</sup>a fraud attack against the RC distancebounding protocol, Proceedings of the IEEE International Conference on RFID-Technologies and Applications (RFID-TA), 2012, pp. 74–79.

[35] M. Philipose, J.R. Smith, B. Jiang, K. Sundara-Rajan, A. Mamishev, S. Roy, Battery-free wireless identi<sup>fi</sup>cation and sensing, IEEE Pervasive Computing 4 (1) (January-March 2005).37-45.

[36] S. Piramuthu, Protocols for RFID reader/tag authentication, Decision Support Systems 43 (3) (April 2007) 897–914.

[37] S. Piramuthu, RFID mutual authentication protocols, Decision Support Systems 50 (2) (January 2011) 387–393.

[38] K. Rasmussen, S. Čapkun, Location privacy of distance bounding, Proceedings of the Annual Conference on Computer and Communications Security (CCS), 2008, pp. 149–160.

[39] J. Reid, J.M. Gonzalez Nieto, T. Tang, B. Senadji, Detecting Relay Attacks with Timing-Based Protocols, Queensland University of Technology ePrint, 2006. http://eprints.qut.edu.au/view/year/2006.html.

[40] C.-P. Schnorr, Ef<sup>fi</sup>cient identi<sup>fi</sup>cation and signatures for smart cards, Proceedings of the International Conference on Advances in Cryptology (Crypto '89), Springer LNCS 435, 1990, pp. 239–252.

[41] Y. Shu, Y. Gu, J. Chen, Sensor-data-enhanced authentication for RFID-based access control systems, Proceedings of the IEEE Mobile Ad Hoc Sensor Systems (MASS), 2012.

[42] H.-M. Sun, W.-C. Ting, A Gen2-based RFID authentication protocol for security and privacy, IEEE Transactions on Mobile Computing 8 (8) (2009) 1052–1062.

[43] F.W. Thayer Fábrega, J.C. Herzog, J.D. Guttman, Strand spaces: proving security protocols correct, Journal of Computer Security 7 (1999) 191–230.

[44] Y.-J. Tu, S. Piramuthu, RFID distance bounding protocols, Proceedings of the <sup>fi</sup>rst International EURASIP Workshop on RFID Technology (RFID 2007), 2007, pp. 67–68.

[45] P. Urien, S. Piramuthu, Framework and authentication protocols for smartphone, NFC, and RFID in retail transactions, Proceedings of the IEEE International Conference on Intelligent Sensors, Sensor Networks and Information Processing (ISSNIP), 2013, pp. 77–82.

[46] D.H. Yum, J.S. Kim, S.J. Hong, P.J. Lee, Distance bounding protocol for mutual authentication, IEEE Transactions on Wireless Communications 10 (2) (2011) 592–601.

[47] W. Zhou, E.J. Yoon, S. Piramuthu, Simultaneous multi-level RFID tag ownership & transfer in health care environments, Decision Support Systems 54 (1) (December 2012) 98–108.

[48] W. Zhou, S. Piramuthu, Preventing ticket-switching of RFID-tagged items in apparel retail stores, Decision Support Systems 55 (3) (June 2013) 802–810.

Pascal Urien is the father of the Internet Smartcard. He is a full professor at INFRES – TELECOM ParisTech.

Selwyn Piramuthu is a professor of Information Systems at the University of Florida and a member of the RFID European Lab in Paris. His research interests include RFID systems.
