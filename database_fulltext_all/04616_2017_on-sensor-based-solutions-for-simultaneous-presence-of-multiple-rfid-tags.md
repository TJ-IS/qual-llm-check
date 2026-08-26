---
otero_id: 4616
otero_key: "TT9TJVUJ"
title: "On sensor-based solutions for simultaneous presence of multiple RFID tags"
authors: "Selwyn Piramuthu; Robin Doss"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.01.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On sensor-based solutions for simultaneous presence of multiple RFID tags

Selwyn Piramuthu<sup>a,</sup>\*, Robin Doss<sup>b</sup>

<sup>a</sup>Information Systems and Operations Management, University of Florida, Gainesville, Florida, USA <sup>b</sup>School of Information Technology, Deakin University, Victoria, Australia

## A R T I C L E I N F O

Article history: Received 10 July 2016 Received in revised form 10 January 2017 Accepted 12 January 2017 Available online xxxx

Keywords: RFID Yoking proof Security Privacy

## A B S T R A C T

A majority of RFID authentication scenarios involve a single tag that is identified independent of other tag in the field of the reader. However, there are situations that necessitate simultaneous authentication of multiple tags as well as the verification of their simultaneous physical proximity to the reader. Juels (2004) introduced yoking proof for simultaneous authentication of multiple RFID tags. Several researchers have since then developed variants of yoking proof using both symmetric and asymmetric cryptography. Given that the ambient conditions are bound to be very similar for all objects that are in close physical proximity to one another, we critically evaluate the use of various relevant ambient conditions for this purpose. Based on our evaluation, we choose to use tag temperature and develop a variant of yoking proof protocol for simultaneous authentication of multiple tags.

© 2017 Elsevier B.V. All rights reserved

## 1. Introduction

A majority of RFID (Radio-Frequency IDentification) authentication scenarios involve a single tag that is identified independent of other tags in the field of the reader (e.g., [27]). Simultaneous authentication of multiple RFID tags (e.g., [28]) is sometimes useful or even necessary when (a) the items are required to be simultaneously physically present in the field of the reader (e.g., [20,35]) or when (b) the confirmed presence of one can be used to confirm the presence of other related tags (e.g., [31]). Examples of the former include the simultaneous presence of specific components for an assembly operation to proceed and medication with associated leaflet [19]. An example of the latter is the known existence of an item on a pallet, whereby the confirmed presence of this item can be used to infer the presence of a related item on the same pallet [30].

Juels [19] was the first to develop an authentication protocol (yoking proof) to determine the simultaneous presence of multiple RFID tags in close physical proximity of one another. Since then, several researchers have identified vulnerabilities in the original yoking proof as well as existing variants of yoking proof and proposed authentication protocols that purportedly are devoid of commonly identified vulnerabilities. The common thread among these authentication protocols is the use of strong connectedness among the messages that are passed among different RFID tags and the use of time stamps to check for unexpected delays in the response from tags to the reader. Connectedness, used to avoid issues related to independent proof by tags that participate in the yoking proof, is ensured through the use of output from a tag as the input to the next tag in the sequence. The reader generally is assumed to use a clock to ensure that the tags respond within a reasonable amount of time to rule out possibilities of relay attacks [32].

A relay attack occurs when at least one adversary simply relays messages between a (honest) reader and a tag, which could either be honest or one that colludes with the adversary to accomplish the attack, with the purpose of impersonating the tag to the reader. In a successful relay attack, the reader is convinced that it is communicating with an authentic/honest tag. The purpose of these attacks include (a) a tag that’s physically far away from the reader to successfully pretend that it’s in close physical proximity to the reader, (b) entry (e.g., to a building, a car) without the explicit knowledge of the (honest) tag holder (here, someone with a smart card that allows entry into that building, someone with that car’s key), among others. Relay attacks are notoriously dificult to address since these attacks do not involve modification to the (possibly encrypted) messages that are passed between reader and tag. Almost all existing automated means to address relay attacks depend on distancebounding protocols that measure the time taken for messages to travel between tag and reader. The challenge in such distance measurement lies with the accuracy of the clocks used for such a purpose since it is dificult to distinguish something that is an inch away from one that is a mile away due to the speed of light.

To our knowledge, while there have been several cryptographic approaches to developing variants of yoking proofs, none of these existing authentication protocols use external information (e.g., physical proximity, ambient conditions) to aid in the process. For example, ideas based on physical proximity have been discussed from a distance-bounding perspective in the form of close-coupling. The idea behind close-coupling is that the existence and physical proximity of prover (here, RFID tag) pegged to a stationary item near the verifier (here, RFID reader) can be verified based on authentication and distance measurements for prover/coupling-device and prover/verifier pairs. However, this involves authentication and proximity verification of the prover simultaneously by two verifiers (e.g., [30]). In addition to requiring a multi-reader/single-tag authentication protocol (e.g., [20]), the distances between the entities in each of these pairs also need to be simultaneously verified. Nevertheless, the distance-bounding part of the protocol used is subject to the same constraints and issues as discussed above.

Measured ambient conditions are yet another possibility. Several ambient conditions have been mentioned in the literature as possible candidates for addressing relay attacks including light, sound and temperature. Posture/orientation, as measured with accelerometer(s), has also been mentioned as a candidate. Since each of these ambient conditions have associated strengths and weaknesses, it may be necessary to consider the simultaneous use of multiple ambient conditions for improved accuracy. However, real-estate is a premium in devices such as RFID (e.g., [5,6]) and, more often than not, there is a need to choose among alternatives.

We critically evaluate several ambient condition dimensions for physical proximity determination. Based on the result of this evaluation, we choose temperature as a viable ambient condition for use in a yoking-variant authentication protocol. Our rationale is that the use of cryptography in addition to information on ambient condition would result in a method that is stronger in terms of ensuring the simultaneous existence of multiple RFID tags in the field of the reader. The contribution of this paper is, therefore, twofold: (a) critical evaluation of components that comprise ambient condition and (b) the use of ambient condition information for a variant of yoking proof authentication protocol.

The remainder of the paper is organized as follows: We briefly discuss yoking proof and a few of its variants in Section 2. We then present a critical evaluation of several ambient condition components in Section 3. In Section $^ { 4 , }$ we present our proposed authentication protocol, a variant of yoking proof, that incorporates ambient condition information. We conclude in Section 5 with a brief discussion on ambient conditions and the proposed authentication protocol.

## 2. Proofs for simultaneous presence

We use the following notations throughout the rest of the paper:

$r _ { 1 } , r _ { 2 } .$ k-bit nonce generated by $T _ { 1 } , T _ { 2 }$

$x _ { 1 } , x _ { 2 } ;$ secret keys of RFID tags $T _ { 1 } , T _ { 2 }$

MAC: Message Authentication Code

MAC<sub>x</sub>[m]: MAC using secret key x on message m

• $P _ { 1 2 } \colon$ proof tags $T _ { 1 }$ and $T _ { 2 }$ scanned simultaneously

• $r _ { R } \colon$ k-bit nonce generated by the reader

$r _ { T _ { 1 } } .$ k-bit nonce generated by $\mathbf { t a g - } 1$

$r _ { T _ { 2 } } .$ k-bit nonce generated by $\mathbf { t a g - } 2$

$T _ { T _ { 1 } }$ : tag-1 temperature as measured by $\mathbf { t a g - } 1$

• $T _ { T _ { 2 } } \mathrm { . }$ : tag-2 temperature as measured by $\mathbf { t a g - } 2$

$P _ { R } , P _ { T _ { 1 } } , P _ { T _ { 2 } }$ : Public key of the reader and tags $( T _ { 1 }$ and $T _ { 2 } )$ respectively

$s _ { R } , s _ { T _ { 1 } } , s _ { T _ { 2 } }$ : Private key of the reader and tags $( T _ { 1 }$ and $T _ { 2 } )$ respectively

Q: the generator of a cyclic subgroup of points on the elliptic curve for the reader and tag

4: allowed tolerance for temperature difference between tag measurements

$\Delta t _ { \mathrm { { m a x } } } .$ maximum allowed round-trip + computational time

Juels [19] proposed the yoking proof (Fig. 1) as evidence for two tags $T _ { 1 }$ and $T _ { 2 }$ to be simultaneously scanned. When two tags pass the yoking proof, it signifies the simultaneous presence of both these tags in the field of the reader at that point in time. The proof is accomplished with the interaction among a reader, the two RFID tags $( T _ { 1 }$ and $T _ { 2 } )$ , and a back-end trusted server/verifier (V). The reader facilitates interaction between the two tags, which correspond with each other through the reader.

While the yoking proof was developed to simultaneously authenticate two RFID tags, it is readily extended to the simultaneous authentication of several (> 2) tags. As can be seen in Fig. 1, the reader initiates the authentication process by sending a “left proof” to one of the tags indicating its role as the ‘left tag’ in the protocol. In response, this tag freshly generates a nonce $\left( r _ { 1 } \right)$ and transmits it to the reader. To maintain connectedness between the tags, the reader forwards this nonce along with the “right proof” role designation to the other (‘right’) tag. Connectedness between the two tags is ensured by incorporating a part of the message from the other tag in the generated message from this tag. This (‘right’) tag therefore uses $x _ { 2 }$ on r to generate the MAC $( m _ { 2 } )$ . The secret keys of the tags $T _ { 1 }$ and $T _ { 2 }$ are respectively $x _ { 1 }$ and $x _ { 2 } .$ . These secret keys are shared with and are known to the server. Upon incorporation of information (here, $r _ { 1 } )$ from the first tag in the MAC (m ), which is transmitted along with a freshly generated nonce (r ) by the second tag to the reader. The reader holds on to the MAC and sends only the nonce it receives from the ‘right’ tag to the ‘left’ tag. Upon reception of this nonce, the ‘left’ tag $\left( T _ { 1 } \right)$ reinforces its connectedness with the ‘right tag $\left( T _ { 2 } \right)$ with the generation of its MAC $( m _ { 1 } )$ on $r _ { 2 }$ through use of $x _ { 1 } .$ . This $\mathsf { M A C } \left( m _ { 1 } \right)$ is then transmitted to the reader. Now, both the tags have generated MACs with the incorporation of information generated by the other tag to ensure connectedness. The reader then puts together necessary components for proof generation $\left( P _ { 1 2 } \right)$ , which is transmitted to the back-end server. The back-end server uses all the information it receives from the reader to verify that the tags $T _ { 1 }$ and $T _ { 2 }$ were indeed scanned together as proof that they were simultaneously in close physical proximity of each other in the reader’s field.

While the yoking proof was instrumental in bringing attention to the need to develop authentication protocols for multiple tags, it was not without vulnerabilities. The first published research that identified vulnerabilities in the yoking proof is that of Saito and Sakurai [25] who identified the existence of a replay attack vulnerability. They showed how the messages that are passed between the reader and ‘left tag’ $\left( T _ { 1 } \right)$ can be captured by a passive adversary, who then replays these messages to the ‘right tag’ $( T _ { 2 } ) .$ . In addition to the identification of this replay attack vulnerability in the yoking proof, they develop and present another protocol (the ‘grouping proof’) with the use of time stamps with the claim that it is not vulnerable to replay attack. This claim was disproved when Piramuthu [24] identified a similar replay attack vulnerability that arises when several responses from the ‘left tag’ are generated with various future time stamps as input. These responses can then be sent to the ‘right tag’ during future authentication rounds when tag $T _ { 1 }$ is not necessarily present in close physical proximity of tag $T _ { 2 }$ (the ‘right tag’).

Several other researchers have since then developed variants of the yoking proof protocol. For example, Bolotnyy and Robins [4] use counters on each tag to sequence the authentication rounds. With a keyed-hash function and a MAC, the counter value is then encoded, which results in increasing the computational complexity of their protocol. Other researchers have proposed variants that are tree-based [9], PUF(Physical Unclonable Function)-based [22], ECC(Elliptic Curve Cryptography)-based ([3]), among others for a wide variety of application areas. For example, several variants of yoking proof have been proposed for medical applications (e.g., [8,18]). It should be noted that a majority of existing variants of yoking proof protocols have been shown to have vulnerabilities (e.g., [17,34]).

![](/api/attachments/TT9TJVUJ/fulltext/images/fb6a38aa60b79ad2ac9813121bcd45cdb7c549f9224d2cfd3fa7d4d673e9317a.jpg)  
Fig. 1. Yoking proof for RFID tags (Juels [19])

## 3. Critical evaluation of ambient conditions

Several researchers have proposed the use of ambient conditions for RFID tag authentication with the observation that both prover and verifier share the same environment during authentication. Ambient condition is a composite that comprises several components including temperature, pressure, light, sound, among others. RFID or NFC (Near Field Communication) devices with appropriate sensors (e.g., [2,7]) can measure their ambient conditions. The literature on the use of ambient conditions for RFID authentication is rather sparse. Extant literature on relay attacks consider a few ambient condition components.

## 3.1. Location-based information using GPS

Location-based systems use technologies such as GPS (Global Positioning System), cellular networks, and WiFi. Among these, GPS has been considered so far as a viable candidate. In cellular networks and WiFi, the location of a device is determined based on the location of other devices such as the use of unique MAC address from a reachable indexed network device. However, the use of GPS ([12]) for determining the exact location of a device is independent of other devices nearby. Location accuracy using GPS is about 3 to 5 m after appropriate corrections, when conditions are ideal (e.g., no signal blockage, access to enough number of satellite signals).

To our knowledge, [21] is the only published research that considers GPS-sensor-based RFID to generate location information and to use this information to address relay attacks. With Intel’s WISP (Wireless Identification and Sensing Platform) [23] and information on location they propose a means to defend against unauthorized reading and relay attacks. Based on location information provided by on-board GPS device, they selectively unlock RFID tag whenever the current location is one among a set of pre-defined locations. They store information on the locations at which that RFID tag is allowed to communicate with a reader. This list is then compared against the current location.

They assume that these valid locations are known in the beginning. Even if the location is known, GPS readings at that location may not be the same in repeated experiments due to noise or minor location displacements. To alleviate issues related to errors in GPS-based location determination, they averaged 10 readings of 10 s durations at each valid location. Their results show that such a setup can be used error-free for several distance separations and speed. However, in a majority of applications that involve purely mobile transactions, the prover and verifier are in close physical proximity of each other and verification of the distance separation between prover and verifier is all that may be necessary to identify relay attacks. Since they do not develop a protocol to complement their experimental study, their study provides only partial evidence for the feasibility of the use of GPS-generated location information for addressing relay attacks. Any authentication protocol that incorporates GPS-generated location information must ensure that the location information is encrypted since an adversary can easily generate GPS information associated with a valid verifier location.

There are several challenges to GPS-sensor-enabled RFID devices. For example, selective unlocking based on a match between current GPS-generated location and valid locations in the stored list may not be easy to implement since (a) the number of valid locations for any realistic application (e.g., supply chains, mobile payments) could be huge while (b) storage and search for a match in such a long list would be resource-intensive, (c) valid locations change continually, and (d) obtaining the entire set of such locations may not be a trivial task. Other challenges to GPS for location identification include its power consumption and latency in location fix (when the last known location cannot be used) during a cold start when it doesn’t have current ephemeris data and waits for error-free full set data from the satellites above. Even when there is no satellite signal blockage, location fix latency can easily exceed 20 s, which is unacceptable for most RFID applications. A few other issues that are associated with the use of GPS-generated data for authentication purposes include the ease with which false GPS signals can be generated as well as GPS signal characteristics such as their severe attenuation when they attempt to pass through dense objects due to their signal weakness.

## 3.2. Posture recognition

While posture is not, strictly speaking, a component of ambient conditions, sensor-enabled tags are used to identify changes in posture. A posture change could be used to instantiate an appropriate response. For example, a sitting posture after a getting in posture could be used to automatically start the car without the user explicitly pressing a button or inserting the key. On the flip side, the car cannot be started when the sequence of necessary posture changes in the person holding the key is not recognized by the car.

Halevi et al. [15] use (accelerometer and magnetometer) sensorenabled RFID to selectively turn on communication with verifier. Others have also used accelerometer in RFID applications (e.g., [11,26]). As in [15,23], they use Intel’s WISP for sensor-based measurements. Halevi et al. use posture changes such as sit to stand and stand to sit to operationalize their study. Since posture changes are generic, in not being location-dependent, an adversary can readily generate data for any given posture change sequence.

Table 1  
Pros and cons of different components of ambient sensor data.

<table><tr><td>Ambient sensor</td><td>Pro</td><td>Con</td></tr><tr><td>GPS</td><td>Location accuracy ~ 3–5 m.</td><td>High power consumption, location fix latency easy to block, corrupt multipath/reflected signals low indoor coverage, easy to generate fake signals</td></tr><tr><td>Light</td><td>Difficult to replicate high tolerance</td><td>directional, relative sensor-orientation-dependent</td></tr><tr><td>Pressure</td><td></td><td>easy to replicate, minor variation across short distances</td></tr><tr><td>Sound</td><td>Difficult to replicate high tolerance</td><td>directional, relative sensor-orientation-dependent</td></tr><tr><td>Temperature</td><td>Not directional high tolerance</td><td></td></tr></table>

## 3.3. Light and sound

Ambient conditions in terms of its light and sound components are unique to each location since it depends on both the (light/sound) source(s) in addition to the environmental characteristics (e.g., surfaces that absorb/reflect light/sound, relative orientation of different surfaces). Since it is dificult to replicate the exact ambient light and/or sound, these components can be used to address relay attacks. The idea here is to measure the (light and/or sound) ambient conditions at the prover as well as the verifier and then compare them to see if they are similar. The underlying premise is that since the prover and verifier are required to be in close physical proximity in RFID applications, the ambient light and sound conditions near prover and verifier must be the same.

Halevi et al. [16] evaluate the use of on-board light and sound sensors to determine the physical proximity of an NFC smartphone to a reader and conclude that because of its directionality, ambient sound has a slight edge over ambient light conditions. Although the light and sound components of ambient conditions may be the same when measured from sensors that face each other, the directionality properties of sound and light, the characteristics of the surface of the prover and verifier facing each other, as well as the characteristics of the ambient environment affect measurement outcomes. Therefore, while the use of ambient light and sound measurements for physical proximity measurement may sound good at first blush, it results in high rates of false readings due to distortions.

## 3.4. Atmospheric pressure

It is unusual for ambient atmospheric pressure to vary significantly between locations that are not that far apart from each other. Therefore, the use of atmospheric pressure is not useful for this purpose in a majority of circumstances.

## 3.5. Temperature

Unlike the effect due to relative orientation of reader and directionality of light and sound on their measured values, ambient temperature is not directional and is therefore less affected. This property of ambient temperature translates to fewer false positive or negative interpretations. To our knowledge, the only study that considers the use of temperature for authentication purposes is [32] where a protocol is developed to address relay attacks. It is possible that the verifier is at an indoor air-conditioned location whereas the (dishonest) prover is farther away in an outdoor location where the ambient temperature is much different (either very cold or very hot).

For a successful attack in this scenario, the adversary has to somehow ensure that the relayed temperature of the prover (RFID tag) is the same or close to that of the ambient temperature of the verifier. This is not trivial and an educated guess may not be satisfactory since the ambient temperature at the prover is most likely significantly different from that at the verifier.

Temperature readings, when used in consort with other forms (e.g., cryptography) of security measures, could help secure the prover/verifier against attacks. When used appropriately and in close physical proximity to the verifier, the prover’s temperature as measured by its own sensor and the reader’s sensor would be the same with a very high probability. This could be used to identify attacks when they occur.

## 3.6. Discussion

We considered prover and verifier ambient conditions to improve tag/reader authentication. Given that research on the use of ambient conditions to verify distance proximity is relatively new, to our knowledge, there is only one [32] published cryptographic authentication protocol that incorporates environmental-sensorbased input. We discussed existing studies in this general area. We also elaborated on the possibility of using ambient temperature measurements as input to identify attacks.

To address attacks with one or more components of ambient condition, each of these components must (a) have a high variance in values across different locations/environment that are commonly encountered by the mobile device of interest, (b) be accurately measurable with inexpensive sensors that have a small physical footprint and (c) not be directional. Based on our evaluation, a summary overview of several components of ambient condition in light of their possible use in authentication protocols is provided in Table 1.

As can be seen in Table 1, among the ambient condition components considered, GPS is the least desirable with several negative characteristics from the point of view of implementation in a highly constrained device such as RFID. The most desirable among these are temperature sensors due to their non-directionality characteristic and relatively high tolerance with respect to measurement error. The latter is a direct consequence of higher temperature difference between prover and verifier. On the other hand temperature’s nondirectionality property allows for more accurate measurement of ambient temperature regardless of the sensor’s orientation. Physical proximity-based attacks are best addressed through multiple approaches such as an authentication protocol that incorporates input from ambient sensor(s) as well as through cryptography.

To verify the claims made in Table 1, we experimentally considered these ambient sensors except for the GPS sensor since we couldn’t get usable readings from GPS sensors inside a building. To operationalize this, we considered two tags that are in close physical proximity of each other and measured their ambient condition values. We generated 30 readings for each of the entries in the second and third columns in Table 2. As can be seen in the last column of this table, measured light and sound values were significantly different for the two tags due to the directionality property of light and sound. The pressure measurement at the two tags were not significantly different. However, because pressure is primarily dependent on elevation, it is not useful for our purpose since locations farther away from the tags also have similar pressure values in a non-hilly area. Due to its non-directional property, the difference in measured temperature values at the two tags was not statistically significant.

## 4. The proposed protocol

We first discuss the essential requirements of the proposed protocol, then present the protocol, followed by analysis of its security and privacy properties.

Table 2  
Ambient condition readings from two tags $T _ { 1 }$ and $T _ { 2 }$ in close physical proximity.

<table><tr><td>Ambient sensor</td><td> $T_1$  Mean(StDev.)</td><td> $T_2$  Mean(StDev.)</td><td>p-value (paired two-tailed t-test)</td></tr><tr><td>Light ( $cd/m^2$ )</td><td>8636.33(1514.12)</td><td>11879.67(671.88)</td><td> $\ll 0.0001$ </td></tr><tr><td>Pressure (mmHG)</td><td>30.459(0.0019)</td><td>30.458(0.0017)</td><td>0.317</td></tr><tr><td>Sound (dB)</td><td>93.33(3.23)</td><td>101.267(3.237)</td><td> $\ll 0.0001$ </td></tr><tr><td>Temperature (F)</td><td>81.7067(0.3383)</td><td>81.6567(0.352)</td><td>0.5581</td></tr></table>

## 4.1. System model

Since RFID tags are extremely resource-constrained devices, the proposed protocol must be as lightweight as possible.The number of messages per tag per authentication round must be minimal to accomplish authentication of the RFID tag before it has the opportunity to move outside the field of the reader while authentication is in progress. Low cost RFID tags generally don’t keep state information, and this necessitates avoidance of race conditions (e.g., when multiple readers simultaneously attempt communication with a tag) from the tag’s perspective. Clearly, secure data must always be encrypted and never be sent in plaintext form when communicated over wireless medium. Since attacks can be expected to come from both passive and active adversaries, the developed authentication protocol must be secure against both (active and passive) types of attacks.

## 4.1.1. Adversary model

Since we are interested in the simultaneous authentication of multiple tags that are in close physical proximity of one another, any compromise of one or few tags by an adversary allows for the possibility of location manipulation whereby a tag’s presence at a given location and time are falsely verified to be true. This seriously violates the core of multiple RFID tag authentication. Replay attacks can be used by resourceful adversaries to impersonate a tag to the reader or vice versa with the result that a tag that is not in close physical proximity to other tag(s) is indeed classified as one with the misrepresentation of reality.

## 4.1.2. Assumptions

The adversary ( ) is assumed to follow the Dolev-Yao intruder model [14] in which has the ability to freely eavesdrop, block, modify, and inject messages that are passed between an RFID tag and a reader.

## 4.1.3. Security properties

We expect the proposed protocol to fulfill the following security properties:

Correctness: A tag cannot incorrectly claim to be present in the field of the reader during the time period of interest when it really is not.

Identification information loss prevention: Since the tag(s) may contain sensitive item-level information, the proposed authentication protocol must ensure that the item’s identification information cannot be revealed to an unauthorized party.

Accountability: The ability to recognize if/when an item is not present at its intended/expected claimed location at any point in time.

## 4.2. The protocol

The system comprises Reader, Back-end Server, and the Tags. The tags are assumed to be temperature-sensor-enabled whereby they can readily measure their surface temperature as necessary. An example of such an RFID tag is Intel’s WISP [23]. We illustrate the proposed protocol for two tags $( T _ { 1 } , T _ { 2 } )$ . However, this authentication protocol can be extended to any number (n) of tags where the Reader sends the response from a tag to its immediate successor in the sequence and the final proof $P _ { 1 . . n }$ is submitted by the Reader to the Back-end Server. We assume the existence of a secure channel between the Reader and Back-end Server and that an adversary cannot impersonate an honest Reader to the Back-end Server. We also assume that the communication channel between Reader and tags is not secure. The proposed protocol only ensures that the Reader authenticates the tags and not vice versa.

We use elliptic curve-based public key cryptography to ensure security with minimal computational resources. By definition, in elliptic curve cryptography, knowledge of $s _ { T _ { 1 } } Q$ and Q (similarly, $s _ { T _ { 2 } } Q$ and Q) does not translate to knowledge of $s _ { T _ { 1 } }$ (respectively, $s _ { T _ { 2 } } )$

The protocol (Fig. 2) is instantiated when there’s a need to determine the simultaneous physical proximity of two tags (say, $T _ { 1 }$ and $T _ { 2 } ) .$ . The Back-end Server sends the secret keys of the two tags (i.e., $s _ { T _ { 1 } } , s _ { T _ { 2 } } )$ to the Reader, which then freshly generates a nonce $\left( r _ { R } \right)$ and sends it along with its public key $\left( P _ { R } \right)$ to the tag (T ) designated as the left tag. In response, $T _ { 1 }$ measures its surface temperature $\left( T _ { T _ { 1 } } \right)$ and then generates its own fresh nonce $( r _ { T _ { 1 } } )$ and computes $\overset { \cdot } { a _ { T _ { 1 } } } ( = P _ { R } s _ { T _ { 1 } } T _ { T _ { 1 } } + r _ { R } r _ { T _ { 1 } } Q ) . T$ then sends $r _ { T _ { 1 } } P _ { T _ { 1 } } , a _ { T _ { 1 } }$ to the Reader. To identify any blocked transmission between Reader and $T _ { 1 } ,$ the Reader waits for a pre-determined amount of time $( \varDelta t _ { m a x } )$ for response from $T _ { 1 } .$ . If response from $T _ { 1 }$ fails to arrive during this time, the Reader generates a fresh $r _ { R }$ and repeats the (“left proof”) process.

Once the Reader receives the response from $T _ { 1 } ,$ , it retrieves the surface temperature of $T _ { 1 }$ from this message. It then sends the “right proof” request to the other tag $\left( T _ { 2 } \right)$ with $r _ { R } , a _ { T _ { 1 } } . ~ T _ { 2 }$ then measures its surface temperature $\left( T _ { T _ { 2 } } \right)$ ) and generates a fresh nonce $( r _ { T _ { 2 } } ) .$ It then generates $a _ { T _ { 2 } } ,$ , which it sends to the Reader along with $r _ { T _ { 2 } } P _ { T _ { 2 } \cdot } \mathrm { I f }$ response from $T _ { 2 }$ does not arrive before $\Delta t _ { m a x } ,$ it resends its message to $T _ { 2 } .$ . Once it receives a response from $T _ { 2 } ,$ the Reader retrieves $T _ { T _ { 2 } }$ from this message and ensures that the difference in temperature measurements by $T _ { 1 }$ and $T _ { 2 }$ is less than a pre-determined reasonable value $( \mathrm { i } . \mathbf { e } . , \lvert T _ { T _ { 1 } } - T _ { T _ { 2 } } \lvert \ \leq \ \epsilon ) .$ When the difference exceeds $\epsilon ,$ it takes further action that could include invalidation of the proof that $T _ { 1 }$ and $T _ { 2 }$ are simultaneously in close physical proximity to the Reader. If the temperature difference is reasonable, the Reader submits the proof $P _ { 1 2 } ( = r _ { R } , S _ { T _ { 1 } } , S _ { T _ { 2 } } , a _ { T _ { 1 } } , a _ { T _ { 2 } } )$ to the Back-end Server.

Next, we consider security analysis and then analysis of privacy properties of the proposed protocol.

## 4.3. Security analysis

## 4.3.1. Forward security

Knowledge of the tag’s secret cannot be used by the adversary to decipher previously sent messages with the use of elliptic curve cryptography since this secret is always incorporated with the generator function value and this requires knowledge of Q.

## 4.3.2. Secrecy/data integrity and authenticity

This is accomplished by the elliptic curve-based cryptographic method used and also by ensuring that no private information such as the tag’s secret are sent in cleartext to reasonably guarantee the integrity of the messages sent between the reader and tags.

S. Piramuthu, R. Doss / Decision Support Systems xxx (2017) xxx–xxx

## 4.3.3. DoS/synchronization problem

The proposed protocol relies on acknowledgments for each of the messages that are sent by the reader to the tags. When a valid response is not received by the reader within a pre-specified $( \varDelta t _ { m a x } )$ time, the reader resends the previously sent message to that tag and waits for a response. An adversary can therefore not repeatedly block these messages since the reader would then tag and abort that authentication process. Since the keys are not updated after each authentication round, an adversary does not have any opportunity for desynchronization attacks, for example, due to the tag being unreachable because its key is different than what is expected.

## 4.3.4. Passive replay

The proposed protocol has four messages that are transmitted in the open to the receiver. The first message includes $P _ { R }$ (the reader’s public key), which is not secret, and a freshly generated nonce $\left( r _ { R } \right)$ with no significance. Passive replay of these to $T _ { 1 }$ will not result in the same response twice since the tag generates a fresh nonce and incorporates that in the transmitted message to the reader. The second message (from $T _ { 1 }$ to the reader) cannot be replayed to the reader since it incorporates the nonce from the reader and the same nonce is unlikely to be repeated by the reader. The third and fourth messages are similar to the first and second messages in terms of their dynamics. Passive replay of these therefore will not translate to anything usable for an adversary.

## 4.4. Analysis of privacy properties

Privacy is an important component of authentication. We consider the privacy properties of the proposed authentication protocol using Avoine’s [1] adversarial model and use the notations as defined in [1] to maintain consistency. We use Avoine’s adversarial model since several of the relatively recent models have associated drawbacks. For example, Coisel and Martin [10] identify issues in models that were proposed by Vaudenay [33] and Hermans [17].

RFID authentication protocols can be checked for their traceability through Avoine’s formal analysis framework. A protocol that is proved to not be traceable is ensured of its satisfaction of associated privacy properties. The attack by an adversary on tag $\tau$ and reader for a given instance p<sup>i</sup> of the authentication protocol $\mathcal { P }$ is operationalized through the following set of oracles [1]:

$Q u e r y ( \pi _ { T } ^ { i } , m _ { 1 } , m _ { 3 } ) ;$ : The Query (Q) oracle models the adversary that transmits a message $m _ { 1 }$ to the tag by means of the forward channel, and upon receipt of response from tag it then sends the message m .

Send $\mathbf { \nabla } \pi _ { \mathcal { R } } ^ { j } , m _ { 2 } ) \mathbf { : }$ : The Send (S) oracle models the adversary transmitting the message m to the reader by means of the backward channel and getting a response from the reader.

$E x e c u t e ( \pi _ { T } ^ { i } , \pi _ { \mathcal { R } } ^ { i } ) ;$ The Execute (E) oracle models the adversary $\boldsymbol { A }$ <sup>T R</sup>instantiating the authentication protocol $\mathcal { P }$ between the tag and reader ${ \mathcal { R } } ,$ and receiving the messages through both the forward and the backward channels.

Reveal $\pi _ { \mathcal { T } } ^ { i } ) \colon$ The Reveal (R) oracle models the adversary retrieving the secrets stored in a tag’s memory. On accessing the R-oracle, the adversary is restricted in that it no longer has access to any other oracle.

The adversary’s goals are captured through untraceability, which essentially allows the adversary to identify the tag based on its interactions in the authentication protocol. This is accomplished by noting that it is dificult to prevent physical tracing by an adversary in contact with the tag. Here, existential and universal traceability refer to tag tracing by an adversary either temporarily or definitively respectively.

Theorem 1. The proposed authentication protocol P is Existential-UNT-QSE.

Proof. Consider an adversary with access to the Q-oracle and the satisfaction of $\omega _ { i } ( T _ { 1 } ) \epsilon \left\{ Q u e r y \left( \pi _ { T _ { 1 } } ^ { i } , * \right) \right\}$ and $\omega _ { i } ( T _ { 2 } ) \epsilon \left\{ Q u e r y \left( \pi _ { T _ { 2 } } ^ { i } , * \right) \right\}$ For any given protocol interaction $I _ { i }$ that corresponds to Q-oracle’s response $m _ { 2 } \epsilon \big ( r _ { T _ { 1 } } P _ { T _ { 1 } } , \alpha _ { T _ { 1 } } \big ) , r _ { T _ { 1 } } P _ { T _ { 1 } }$ is guaranteed to be uncorrelated since it is based on random $r _ { T _ { 1 } }$ . Moreover, $\alpha _ { T _ { 1 } }$ is dependent on constants $P _ { R }$ and $s _ { T _ { 1 } }$ , random $r _ { T _ { 1 } }$ , and variable $T _ { T _ { 1 } }$ . Given this, $\alpha _ { T _ { 1 } }$ is guaranteed to be unique for each protocol execution instance. The proposed authentication protocol is Existential-UNT-Q since the adversary does not learn any useful information even with access to the $\scriptstyle { \mathrm { Q } } \ { \mathrm { } }$ -oracle.

We now consider an adversary with access to both the Q and S oracles such that:

$$
\omega_ {i} (T _ {1}) \in \left\{\text { Query } \left(\pi_ {T _ {1}} ^ {i}, *\right), \text { Send } \left(\pi_ {T _ {1}} ^ {i}, m _ {2} ^ {1}\right) \right\} \quad \text { and }
$$

$$
\omega_ {i} (T _ {2}) \epsilon \left\{\text { Query } \left(\pi_ {T _ {2}} ^ {i}, *\right), \text { Send } \left(\pi_ {T _ {2}} ^ {i}, m _ {2} ^ {2}\right) \right\}
$$

where, m<sub>2</sub>4 $\left( r _ { T _ { 1 } } P _ { T _ { 1 } } , \alpha _ { T _ { 1 } } \right)$

The adversary receives $m _ { 3 }$ as response from tag T<sub>2</sub> upon sending $m _ { 2 }$ such that: $m _ { 3 } \epsilon ( r _ { T _ { 2 } } P _ { T _ { 2 } } , \alpha _ { T _ { 2 } } )$

Here, $r _ { T _ { 2 } } P _ { T _ { 2 } }$ and $\alpha _ { T _ { 2 } }$ are both guaranteed to be unique for each authentication protocol run due to random $r _ { T _ { 2 } }$ , thereby not providing any advantage to the adversary. The proposed authentication proto col is therefore Existential-UNT-QS.

We now consider an adversary with access to the $\textstyle { \mathrm { ~ Q ~ } } S$ and E oracles such that:

$$
\omega_ {i} (T _ {1}) \epsilon \left\{Q u e r y \left(\pi_ {T _ {1}} ^ {i}, *\right), S e n d \left(\pi_ {T _ {1}} ^ {i}, m _ {2}\right), E x e c u t e \left(\pi_ {T _ {1}} ^ {i}, \pi_ {R} ^ {j}\right) \right\}
$$

$$
\omega_ {i} (T _ {2}) \epsilon \left\{\text { Query } \left(\pi_ {T _ {2}} ^ {i}, *\right), \text { Send } \left(\pi_ {T _ {2}} ^ {i}, m _ {2}\right), \text { Execute } \left(\pi_ {T _ {2}} ^ {i}, \pi_ {R} ^ {j}\right) \right\}.
$$

Even with eavesdropping on several instances of the authen tication protocol runs, the adversary is guaranteed to not gain any advantage over the QS-oracle with the use of the reader’s public key $P _ { R }$ and elliptic curve cryptography. This renders the proposed authentication protocol Existential-UNT-QSE, which is the strongest security requirement when an attacker cannot tamper with the tag [1]. -

Theorem 2. The proposed authentication protocol P is FORWARD-UNT-OSER

We consider the case where the adversary has access to the R-oracle in addition to the $Q , S$ and E oracles such that:

$$
\begin{array}{l} \omega_ {i} (T _ {1}) \in \left\{\text { Query } \left(\pi_ {T _ {1}} ^ {i}, *\right),   \text { Send } \left(\pi_ {T _ {1}} ^ {i}, m _ {2}\right),   \text { Execute } \left(\pi_ {T _ {1}} ^ {i}, \pi_ {R} ^ {j}\right), \right. \\ \left. \text { Reveal } \left(\pi_ {T _ {1}} ^ {i}\right) \right\} \quad \text { and } \end{array}
$$

$$
\begin{array}{l} \omega_ {i} (T _ {2}) \epsilon \left\{\text {Query} \left(\pi_ {T _ {2}} ^ {i}, *\right), \text {Send} \left(\pi_ {T _ {2}} ^ {i}, m _ {2}\right), \text {Execute} \left(\pi_ {T _ {2}} ^ {i}, \pi_ {R} ^ {j}\right), \right. \\ \text {Reveal} \left(\pi_ {T _ {2}} ^ {i}\right) \Big \}. \end{array}
$$

The adversary can retrieve the tag secrets $s _ { T _ { 1 } }$ and $s _ { T _ { 2 } }$ through the Roracle. To track a tag, the adversary needs to retrieve the constants $s _ { T _ { 1 } }$ $o r s _ { T _ { 2 } } f r o m \alpha _ { T _ { 1 } } o r \alpha _ { T _ { 2 } }$ respectively. For the “left proof”, the adversary can retrieve the tag secret key $s _ { T _ { 1 } }$ from the R-oracle. $U s i n g s _ { T _ { 1 } }$ , the adversary can obtain $r _ { T _ { 1 } }$ from $r _ { T _ { 1 } } P _ { T _ { 1 } }$ . Moreover, using $r _ { R } ,$ , the attacker can extract $P _ { R } s _ { T _ { 1 } } T _ { T _ { 1 } } f r o m \alpha _ { T _ { 1 } }$ . Since the adversary does not know the reader’s secret

Please cite this article as: S. Piramuthu, R. Doss, On sensor-based solutions for simultaneous presence of multiple RFID tags, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.01.003

S. Piramuthu, R. Doss / Decision Support Systems xxx (2017) xxx–xxx  
![](/api/attachments/TT9TJVUJ/fulltext/images/c23ae40e133f82d4236febc69274eb2f3c6ee490075cf9ea7bd492c825a3f8a1.jpg)  
Fig. 2. The proposed protocol with ambient temperature information.

key $s _ { R } ,$ it is not possible for the adversary to determine $s _ { T _ { 1 } }$ . This signifies that the R-oracle does not provide any significant advantage to the adversary and the proposed protocol is . -

Theorem 3. The proposed protocol P is desynchronization resistant.

Desynchronization is accomplished by the adversary who can successfully complete the protocol run or if the tag updates its secrets even when the authentication protocol does not successfully conclude. Theorem 1 states that the proposed authentication protocol achieves the strongest security requirement of . This signifies that an adversary cannot successfully complete a protocol run. Moreover, secrets are not updated in the proposed protocol. Hence, the tags are guaranteed to share the correct secrets with the reader. The proposed authentication protocol is therefore resistant to desynchronization attacks.

Theorem 4. The proposed authentication protocol P guarantees recent aliveness.

The use of elliptic curve cryptography ensures that the proposed authentication protocol satisfies the freshness and algebraic replay resistance (ARR) conditions that are required to guarantee recent aliveness [13]. Knowledge of the private key $s _ { R }$ is required to determine $s _ { T _ { 1 } }$ for a given $\alpha _ { T _ { 1 } }$ . As the probability of an adversary guessing $r _ { T _ { 1 } }$ and $s _ { T _ { 1 } } f r o m \alpha _ { T _ { 1 } } o r r _ { T _ { 1 } } P _ { T _ { 1 } }$ is negligible, freshness is achieved. Moreover, with previous traces of the protocol, the advantage for the adversary to correctly determine either $r _ { T _ { 1 } } o r s _ { T _ { 1 } }$ when challenged by the tag and/or to guess $s _ { T _ { 1 } }$ or $s _ { T _ { 2 } }$ is negligible. Hence, recent aliveness is satisfied, and the proposed authentication protocol is resistant to replay attacks including algebraic replay attacks. -

## 5. Discussion and conclusion

Cryptography, and sometimes time, have been used to ensure security and privacy in published RFID authentication protocols. Although single RFID authentication is the most common scenario that is considered in extant RFID authentication protocols, cases where multiple RFID tags need to be simultaneously authenticated are not uncommon. Juels [19] introduced yoking proof to address these cases. Since then, researchers have developed variants of yoking proof with different approaches for a variety of application contexts.

While it is satisfactory to develop authentication protocols using just cryptography, we claim that the strength of these protocols can be improved through use of additional means. We propose the use of ambient conditions for this purpose with the premise that objects that are in close physical proximity to one another are bound to experience the same ambient conditions. To this end, the contribution of our paper is twofold: (a) we critically evaluate several ambient condition dimensions and related literature and make a case for temperature as a good option among the considered ambient conditions, (b) we then develop an elliptic curve-based variant of yoking proof authentication protocol with the incorporation of ambient condition information.

We believe that the use of cryptography in addition to temperature measurements results in improving the strength of the developed authentication protocol. To our knowledge, this is the first study that uses ambient condition information in an authentication protocol to prove the simultaneous presence of multiple RFID tags in the field of the reader. Given the significance of proper authentication and the deleterious consequences when the process is flawed, there is positive utility in any additional information that can be used to complement existing ones.

## References

[1] G. Avoine, Adversarial Model for Radio Frequency Identification, Cryptology ePrint Archive Report 2005/049, 2005.

[2] B. Bacheldor, Hybrid tag includes active RFID, GPS, satellite and sensors, RFID J. (February 24 2009) 24.

[3] L. Batina, Y.K. Lee, S. Seys, D. Singele, I. Verbauwhede, Extending ECC-based RFID authentication protocols to privacy-preserving multi-party grouping proofs, Pers. Ubiquit. Comput. 16 (3) (2012) 323–335.

[4] L. Bolotnyy, G. Robins, Generalized ‘Yoking Proofs’ for a Group of Radio Frequency Identification Tags, International Conference on Mobile and Ubiquitous Systems (Mobiquitous), San Jose, CA, July 1–4, 2006.

[5] I. Bose, R. Pal, Auto-ID: managing anything, anywhere, anytime in the supply chain, Commun. ACM 48 (8) (2005) 100–106.

[6] I. Bose, C.W. Lam, Facing the challenges of RFID data management, Int. J. Inform.Syst. Supply Chain Manag. 1 (4) (October–December 2008) 1–19.

[7] M. Buckner, R. Crutcher, M.R. Moore, S.F. Smith, GPS and Sensor-Enabled RFID Tags, Oak Ridge National Laboratory. 2001, http://www.ornl.gov/webworks/ cppr/y2001/pres/118169.pdf.

[8] C.L. Chen, C.Y. Wu, Using RFID yoking proof protocol to enhance inpatient medication safety, J. Med. Syst. 36 (5) (2012) 2849–2864.

[9] H.Y. Chien, S.H. Liu, Tree-Based RFID Yoking Proof, Proceedings of the International Conference on Networks Security, Wireless Communications and Trusted Computing, 2009, pp. 550–553

[10] I. Coisel, T. Martin, Untangling RFID Privacy Models, Cryptology ePrint Archive Report 2011/636, 2011.

[11] A. Czeskis, K. Koscher, J.R. Smith, T. Kohno, RFIDS and Secret Handshakes: Defending Against Ghost-and-Leech Attacks and Unauthorized Reads with Context-Aware Communications., Proceedings of the ACM Conference on Computer and Communications Security (CCS), 2008. pp. 479–490.

[12] D.E. Denning, P.F. MacDoran, Location-Based Authentication: Grounding Cyberspace for Better Security., Computer Fraud & Security, Feb. 1996, 12–16.

[13] T. van Deursen, S. Radomirovic, Algebraic Attacks on RFID Protocols, Information Security Theory and Practices: Smart Devices, Pervasive Systems and Ubiquitous Networks (WISTP 2009) (LNCS 5746), 2009, 38–51.

[14] D. Dolev, A.C.C. Yao, On the security of public key protocols, IEEE Trans. Inf. Theory 29 (2) (1983) 198–207.

[15] T. Halevi, S. Lin, D. Ma, A.K. Prasad, N. Saxena, J. Voris, T. Xiang, Sensing-Enabled Defenses to RFID Unauthorized Reading and Relay Attacks without Changing the Usage Model, Proceedings of the IEEE International Conference on Pervasive Computing and Communications (Percom), 2012. pp. 227–234.

[16] T. Halevi, D. Ma, N. Saxena, T. Xiang, Secure Proximity Detection for NFC Devices Based on Ambient Sensor Data, Proceedings of the European Symposium on Research in Computer Security (ESORICS), 2012. pp. 379–396.

[17] J. Hermans, R. Peeters, Private Yoking Proofs: Attacks, Models and New Provable Constructions, Radio Frequency Identification. Security and Privacy Issues LNCS 7739, 2013, 96–108.

[18] H.H. Huang, C.Y. Ku, A RFID grouping proof protocol for medication safety of inpatient, J. Med. Syst. 33 (6) (2009) 467–474

[19] A. Juels, Yoking Proofs for RFID Tags, Proceedings of the First International Workshop on Pervasive Computing and Communication Security, IEEE Press. 2004,

[20] G. Kapoor, W. Zhou, S. Piramuthu, Multi-tag and multi-owner RFID ownership transfer in supply chains, Decis. Support. Syst. 52 (1) (2011) 258–270.

[21] D. Ma, A.K. Prasad, N. Saxena, T. Xiang, Location-Aware And Safer Cards: Enhancing RFID Security and Privacy via Location Sensing, Proceedings of the ACM Conference on Wireless Network Security (WiSec), 2012. pp. 51–62.

[22] S. Mauw, S. Piramuthu, A PUF-based Authentication Protocol to Address Ticket-Switching of RFID-tagged Items, Security and Trust Management LNCS 7783, 2013, 209–224.

[23] M. Philipose, J.R. Smith, B. Jiang, K. Sundara-Rajan, A. Mamishev, S. Roy, Battery-free wireless identification and sensing, IEEE Pervasive Comput. 4 (1) (January-March 2005) 37–45.

[24] S. Piramuthu, On Existence Proofs for Multiple RFID Tags, Proceedings of the IEEE International Conference on Pervasive Services (ICPS), 2006. pp. 317–320.

[25] J. Saito, K. Sakurai, Grouping Proof for RFID Tags, Proceedings of the 19th International Conference on Advanced Information Networking and Applications (AINA’05), 2005. pp. 621–624.

[26] Y. Shu, Y. Gu, J. Chen, Sensort-Data-Enhanced Authentication for RFID-Based Access Control Systems, Proceedings of the IEEE Mobile Ad Hoc Sensor Systems (MASS), 2012.

[27] S. Sundaresan, R. Doss, S. Piramuthu, W.L. Zhou, Secure tag search in RFID systems using mobile readers, IEEE Trans. Dependable and Secure Comput. 12 (2) (2015) 230–242.

[28] S. Sundaresan, R. Doss, S. Piramuthu, W.L. Zhou, A robust grouping proof protocol for RFID EPC C1G2 tags, IEEE Trans. Inf. Forensics Sec. 9 (6) (2014) 961–975.

[30] Y.J. Tu, S. Piramuthu, A decision-support model for filtering RFID read data in supply chains., IEEE Trans. Syst. Man Cybern. Part C 41 (2) (2011) 268–273.

[31] Y.-J. Tu, W. Zhou, S. Piramuthu, Identifying RFID-embedded objects in pervasive healthcare applications, Decis. Support. Syst. (January 2009)

[32] P. Urien, S. Piramuthu, Elliptic curve-based RFID/NFC authentication with temperature sensor input for relay attacks, Decis. Support. Syst. 59 (2014) 28–36.

[33] S. Vaudenay, On Privacy Models for RFID, Advances in Cryptology - ASIACRYPT 2007, Lecture Notes in Computer Science, vol. 4833. 2008, 68–87.

[34] A.K. Wickboldt, S. Piramuthu, Patient safety through RFID: vulnerabilities in recently proposed grouping protocols, J. Med. Syst. 36 (2) (2012) 431–435.

[35] W. Zhou, E.J. Yoon, S. Piramuthu, Simultaneous multi-level RFID tag ownership & transfer in health care environments, Decis. Support. Syst. 54 (1) (December 2012) 98–108.

Selwyn Piramuthu is a Professor of Information Systems at the University of Florida and a member of the RFID European Lab in Paris. His research interests include RFID systems.

Dr. Robin Doss joined the School of Information Technology, Deakin University, Australia, in 2003 and is currently the Associate Head of School (Development & International). Prior to joining Deakin University, he was part of the technical services group at Ericsson Australia and a research engineer at RMIT University. Robin received a Bachelor of Engineering in Electronics and Communication Engineering from the University of Madras, India in 1999, and a Master of Engineering in Information Technology and a PhD in Computer Systems Engineering from the Royal Melbourne Institute of Technology (RMIT), Australia in 2000 and 2004 respectively. His PhD thesis was on mobility prediction for next generation wireless networks. In 2007, he also completed a Graduate Certificate in Higher Education from Deakin University.
