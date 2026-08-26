---
otero_id: 13076
otero_key: "TVKY5JZ6"
title: "A novel steganographic algorithm using animations as cover"
authors: "Gopalakrishna Reddy Tadiparthi; Toshiyuki Sueyoshi"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.03.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A novel steganographic algorithm using animations as cover

Gopalakrishna Reddy Tadiparthi <sup>a</sup>, Toshiyuki Sueyoshi <sup>b,c,</sup>⁎

<sup>a</sup> Department of Computer Science, New Mexico Institute of Mining and Technology, Socorro, NM 87801, USA

<sup>b</sup> Department of Management, New Mexico Institute of Mining and Technology, Socorro, NM 87801, USA

<sup>c</sup> National Cheng Kung University, Department of Industrial and Information Management, Tainan, Taiwan

## a r t i c l e i n f o

Article history: Received 2 October 2007 Received in revised form 16 March 2008 Accepted 23 March 2008 Available online 8 April 2008

Keywords: Information Hiding Steganographic model Encoding Decoding Animation

## a b s t r a c t

Information security is gaining widespread importance in distributed decision support systems [T.S. Raghu, and H. Chen, Cyberinfrastructure for homeland security: Advances in information sharing, data mining, and collaboration systems. Decision Support Systems 43 (2007) 1321–1323]. Conventional steganographic models available in the literature on information hiding use the knowledge of cover-object and stego-object to extract embedded data. Embedding algorithms have been predominantly used in steganography for hiding data whereas encoding algorithms have been used for data compression. This research study proposes a modi<sup>fi</sup>ed model for steganographic system that incorporates encoding algorithms based upon the information theoretic model documented in Cachin [C. Cachin, An Information-Theoretic Model for Steganography, Information and Computation 192 (1) (2004) 41–56.]. The differences between the conventional model and the proposed model are analyzed in this study. We further implement the proposed model by designing a novel steganographic algorithm that utilizes animations as cover-objects. The proposed approach is then compared with an encoding algorithm for gif animations and a modi<sup>fi</sup>ed embedding algorithm with animations as the cover. Gifshuf<sup>fl</sup>e is a steganographic software that hides data in gif animations. Digital Invisible Ink Toolkit (DIIT) is a software that uses embedding algorithm to conceal data into images. DIIT is remodeled to hide data within animated images in this study. Experiments reveal that the encoding algorithms are suitable for information hiding using animations. The study <sup>fi</sup>nds that the proposed encoding framework with animations provides a practical framework for analysis and has a better security performance than Gifshuffle and DIIT. Although the proposed model achieves more hiding rate, Gifshuf<sup>fl</sup>e is computationally faster than other techniques.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

In recent years, the wide amount of transfer of sensitive data over large computer networks has made information security an indispensable technology. Raghu and Chen [32] assembled a special issue on Cyber-infrastructure for security in Decision Support Systems [Vol. 43(4) pp. 1321–1449] that contains a series of eight articles that describe the importance of cyberinfrastructure for homeland security. Cryptography, a key component in many data security systems, formed the basis in Information Security for a long period. When data is protected using encryption algorithms, this protection is conspicuous i.e., a casual observer can recognize the presence of encrypted data in a channel. This visibility could attract attention from attackers and they try to decrypt the data. The strength of a cryptographic algorithm relies on its algorithmic complexity. With the advent of grid computers and quantum computers, it may be possible that this cryptographic strength is compromised. With the proliferation of computer networks and Internet, there is an increased need for a secure methodology to transmit sensitive data over long distances by concealing its own presence.

Information security plays a signi<sup>fi</sup>cant role in the current advanced decision support systems. Decision Support Systems (DSS) have evolved from being a single-user system to a collaborative system that spans over many levels in an organization [35]. These systems are increasingly used not only in an intranet within an of<sup>fi</sup>ce but also over public Internet that connects many organizations and corporate environments [23]. Thus, intranet based DSS are gaining widespread importance in enterprises [2]. In such systems, the management is concerned with transmission of secure data. Transmission of con<sup>fi</sup>dential data is common in such systems [37]. A manager has to ensure that internal data is not stolen and is securely transmitted. Distributed DSS use a lot of data transfer between them. See [37] for a detailed taxonomy on intranet based DSS. Securing the con<sup>fi</sup>dential data in DSS is a critical and important task for a manager.

Transmitting con<sup>fi</sup>dential information has always been a challenge to researchers in the <sup>fi</sup>eld of communications and information security [3,36]. One such method of transmitting classi<sup>fi</sup>ed data is to hide con<sup>fi</sup>dential information within innocent looking data so that a casual observer cannot detect the presence of a secure communication. Steganography is the study of art and science of undetected communication. One of the goals of steganography is that the presence of a secret message should not be detectable. The security of a steganographic algorithm depends upon whether an attacker can distinguish a cover-object from a stego-object.

Many researchers have proposed algorithms for hiding data in many forms of the digital medium. Hiding has been accomplished in many computer <sup>fi</sup>le formats by identifying unused / redundant data areas or by transforming it from one domain to another. Furthermore, all these models assume that the receiver knows the cover-object before extraction of the hidden data. Conventional practical steganographic models assume that protection can be provided by means of a pass-phrase or key, which is encrypted within the stego-object. These models do not consider a private channel to send the password/secret-key. The steganalysis of the conventional algorithms do not include the knownalgorithm attack, which is an analysis technique used in modern security systems. There is a need for the design of a steganographic model that overcomes all these disadvantages in the conventional models.

Animations are widely used in many websites for advertising, presentations, tutorials, television cartoons and others. Most of the websites use <sup>fl</sup>ash animations to present their data. They also use gif animations to represent certain key frames, especially when bandwidth is limited or when the webpage needs to download quickly. There is no existing framework dedicated to the representation of a steganographic system based on animations. Furthermore, not many software systems exist that can hide data within an animation. Animations are different from image <sup>fi</sup>les in that they have many images and they are linked to each other. These images may be independent of each other. Animations are different from video <sup>fi</sup>les where in video <sup>fi</sup>les the continuous motion is broken into discrete frames. This is why the compression format of animation <sup>fi</sup>les and video <sup>fi</sup>les are different. There is a need for a stand-alone steganographic algorithm for animations that can hide data within an animation and provide a framework for steganalysis.

This study proposes a steganographic model based on coveranimations. The model provides a design framework for a system administrator as well as for an analyst to design the security. The model is extended from the recently proposed theoretical models in the <sup>fi</sup>eld of information security. We also propose a steganographic algorithm for hiding information in animations.

The remaining part of this article is organized as follows: Section 2 reviews the previous works in steganography. Section 3 describes the proposed theoretical model. Section 4 discusses the proposed steganographic algorithm. Section 5 summarizes experiments and results obtained from a simulated study. Section 6 concludes this research along with future extensions of the proposed method.

## 2. Literature survey

A typical information security system involves three entities such as sender, receiver, and warden. This is the most common model used in the <sup>fi</sup>eld of information security. Sender is an entity who is transmitting information to a receiver by means of an available transmission channel. Sometimes, the information may contain secret data which is intended only for the receiver. Warden is an entity who may have access to a public channel. The objective of steganography is covert communication between sender and receiver. Warden may intercept the information transmitted between the sender and receiver. The warden may be passive or active. A passive warden observes the passing messages in the public channel to detect the presence of covert communication. An active warden may modify the data sent between the sender and the receiver on the public channel to avoid secret communication. The objective of this study is to design a steganographic system to escape the detection.

The taxonomies for information hiding techniques that are available in the literature are based on the <sup>fi</sup>le type of the cover-object or individual algorithms on a particular type of digital media. A literature survey in the <sup>fi</sup>eld of steganography reveals research studies that have been carried out in different aspects of computer science (information theory, signal processing, and multimedia processing). The different steganographic techniques can be classi<sup>fi</sup>ed into the following three broad categories: theoretical models, type of algorithms to achieve security, and steganalysis algorithms.

Theoretical Models. The theoretical models of information hiding are based upon the concepts of information theory. Theoretically, steganographic models are classi<sup>fi</sup>ed into secret-key, public-key, and pure. In a secret-key steganography, the key, shared only between the sender and the receiver, is assumed to be communicated over a secure transmission channel before a use of the steganographic system. The warden does not have any knowledge of the key. See [4] for a detailed speci<sup>fi</sup>cation of such a model based upon “prisoners problem.” In a public-key steganographic model, the sender knows the public key of the receiver [11,21]. In a pure steganographic system, the sender and the receiver do not share any prior information. See [27] for a detailed analysis of various data hiding techniques developed in recent years. A detailed information theoretic model is documented in [28,34]. The proposed model in this research study belongs to the category of secret-key steganography.

Type of Algorithms. Based upon the algorithms used for concealing data, steganography can be classi<sup>fi</sup>ed as embedding, encoding, and hybrid.

Embedding Algorithms. Those algorithms which replace certain portions of the cover-object with the secret-data are called embedding algorithms. These algorithms are primarily used with multimedia <sup>fi</sup>les. The technique replaces the least signi<sup>fi</sup>cant bits of each pixel in an image by the bits of secret data. Image based hiding algorithms range from embedding in bit planes of the images [7,12] to masking [31] and to transform domain based techniques [10,13]. These image based steganographic algorithms were later extended to video and audio <sup>fi</sup>les. The research [29] uses bit-plane steganography combined with wavelet compression to hide in video <sup>fi</sup>les. In [6], each individual video frame is used for hiding data based on texture masking and lattice structure. Similar algorithms have been developed to hide data in redundant areas of audio <sup>fi</sup>les [20,38]. The study [8] uses difference of values between two consecutive pixels for embedding data. All the embedding algorithms take advantage of the redundancy in the <sup>fi</sup>le description of multimedia data representation. The study [14] presents a matrix embedding algorithm suitable for achieving a large embedding capacity. Embedding algorithms were so common that the terminologies (embedded data, cover, and stego-object) proposed in [30] were the de facto terms in Steganography. The research [17] develops DIIT for embedding data into images based on bmp, jpeg, and png. This toolkit also provides common steganalysis techniques for the user to estimate the algorithmic strength.

Encoding Algorithms. Those algorithms which change the representation of cover-object according to some form of secret-data are called encoding algorithms. In other words, the cover-object is encoded according to the format of secret data. This type of steganography uses the <sup>fi</sup>le-format of the cover-object or the construction process of cover-object during encoding. In most cases, the algorithm is combined with the creation of such a cover/stego object. The research [1] hides data in executable programs by selecting suitable instructions, permuting or rescheduling instructions, and changing the layout of the code. The study [42] proposes a stego-encoding algorithm based on cyclic coding, which leads to less number of cover-bit-alterations. The research [31] proposes an encoding technique for audio and image streams, which hides encrypted or error-coded data inside the images. An encoding algorithm for hiding in gif animations is introduced as gifshuf<sup>fl</sup>e in [22]. The algorithm proposed in this study belongs to the encoding steganography.

Hybrid Algorithms. This category of research cascades steganography with other information security techniques. Such algorithms, whose strength depends on other information security techniques in addition to steganography, are known as hybrid algorithms. The strength of information security in such models is achieved by combining (multiplying) the security of each of the cascade components in the system (multiplicative model). Most commonly used cascaded information security methods are cryptography and/or Error Control Coding (ECC). For example, the research [33] uses a combination of signal processing, cryptography, and steganography to increase the security of information. The study [24] has developed a steganographic model for images by using ECC to achieve robustness. Even though hybrid steganography increases the strength of the algorithm, it generally reduces the net hiding capacity of the cover and increases the computational time to hide/extract the hidden data. ECC is widely used with steganography to recover data lost during transmission. This increases the extracting strength of an algorithm during an attack. ECC can be combined with encoding or embedding steganography. The research [42] uses ECC with stego-encoding. The study [26] combine ECC with embedding to achieve a steganographic scheme based on chaos and Euler theorem. Some studies such as Hansen et al. [16] use a genetic programming and selfcorrecting approach to computer security. The basic rationale for the use of ECC is to induce self-correcting capabilities to the stego-object so that they can be resistant to the noise in the transmission channel.

Steganalysis. Steganalysis is the art of discovering the existence of hidden information. Initially, the requirement of a steganographic system was that the difference between cover and stego should be imperceptible to human senses. To analyze text with semantic meanings, Yang and Li [41] follow a constraint network approach to analyze linguistics semantics using Hop<sup>fi</sup>eld networks. With the advent of many automated software tools for steganalysis, this requirement is modi<sup>fi</sup>ed in the manner that the difference should be undetectable to any available steganalysis tool. For example, the study [40] discusses contemporary tools of steganography and also discusses the commonly used steganalytic techniques. When examined by an active warden, the hidden message should be robust against any possible modi<sup>fi</sup>cation. Automated detection tools are being developed to deal with the enormous amount of data <sup>fl</sup>owing through the computer networks. A lot of works have been done in the field of steganalysis using machine learning algorithms. This study is limited to the design and development of steganography algorithms, except mentioning the possible extensions and steganalysis techniques in the concluding section.

## 2.1. Requirements and goals of a steganographic system

A steganographic system should meet certain pre-requisites. The following requirements are condensed from the views of [9,39]:

Detection: A fundamental requirement of a steganographic system is that the hidden message carried by stego should not be detected or noticed when the stego is observed casually. Information hiding models should be perceptually transparent. Most of the steganographic techniques take advantage of the limitations of human auditory system and human visual system (visual transparency). This may not be applicable directly for current practical purposes as it is practically impossible to employ human resources to go through each and every multimedia <sup>fi</sup>le passing through the network. Most of the current tools to detect steganography use automated software based on statistical and machine learning techniques for detection.

Capacity: Since the stego carries the secret data embedded/encoded within itself, it is important to know the amount of data which the cover/stego can embed/encode. This maximum amount of data bits that the stego can accommodate is called steganographic capacity. The goal of a steganographic algorithm is to maximize the capacity. Steganographic capacity is assuming an important role in the quality metric of a steganographic software.

Distortion: An ideal steganographic algorithm would minimize distortion between cover and stego. The steganographic technique should be tamper-proof. There should be an indication if the stego-object has been modi<sup>fi</sup>ed.

Robustness: The steganographic technique should withstand a given set of transformations and <sup>fi</sup>ltering techniques to the stego. These stego-objects are subjected to incidenta attacks to measure the robustness. This goal is not only a requirement for a good stego-system but also for many information security tools like a network analysis toolkit [5].

## 3. Proposed model

As mentioned previously, the proposed steganographic model and algorithm in this study can be classi<sup>fi</sup>ed under a secret-key stego-system with encoding/decoding. The model provides the design framework to hide data by encoding an animated set of images. Fig. 1 illustrates the schematic of the proposed steganographic system. This system is based on the information-theoretic model [4].

In the proposed steganographic model of Fig. 1, there are three participating entities: a sender, a receiver, and a warden. The sender transmits data and the receiver receives data. The warden can read all data that passes through the transmission channel to which he is attached. The purpose of transmission channels is for transfer of information, which are assumed to be an asynchronous transmission media where data can be transferred sequentially, one element (bit) at a time. The order in which the data is received is in the same order in which it is sent. There are two kinds of transmission media: private and public channels. The private channel is available only to sender and receiver. It is assumed that no one can eavesdrop in a private channel and hence it is also called as a secure channel. In reality, there is no channel that is completely secure. The public channel is a transmission channel where a warden has access to communications between sender and receiver. Although public channel and private channel can exist in tandem, it is assumed that the private channel exists before a public channel is used in operation. Once transmission, although a public channel starts the private channel, is not available anymore. This is in agreement with the assumptions of the “prisoner’s problem.” It is also assumed that the public channel is free of white noise. The inbuilt protocols of the transmission media handle such noise. Thus, any data sent through one end of the public channel is received at the other end without any noise. A real-life example of a public channel is the Internet. Each layer of the TCP/IP network has error detection and correction capabilities to handle noise [33].

Fig. 1 illustrates the process of hiding and the roles of the different entities. The sender can either transmit coveranimation (C) or stego-animation (S). Cover-animation is an animation that is not processed for hiding information. When the sender transmits cover-animation through the public channel, no encoding takes place, the switch ‘0’ is closed. When the sender transmits stego-animation through the public channel, encoding takes place and the switch ‘1’ is closed. The stego-animation (S) is created by the encoding function (F) which is an algorithm that accepts secret message (E), cover-animation (C) and secret key (K) as input parameters and encodes the cover-animation according to the probability distribution of E (P ).

The receiver receives a stego-animation (Ŝ), which can be one of the following: C, S, or the modi<sup>fi</sup>ed animation sent by the warden. The receiver extracts the data (Ê), using an extraction function (G) which accepts input parameters K and Ŝ. The warden listens to all data sent through the public channel. A passive warden uses certain algorithms to detect the presence of hidden data in S. An active warden modi<sup>fi</sup>es S and resends it to the receiver as Ŝ. These changes are called as attacks on the stego-system.

The proposed model is similar to the conventional model used by existing steganographic software. It should be noted that most of the documented theoretical models [4,28,34] agree with the proposed model and share similar assumptions.

The proposed model is different from the practically used models in the following aspects: First, Conventional practical steganographic models assume that the secret key is embedded in the stego-object. A password or an encrypted password is used as security measure. The receiver should have knowledge about the password before extracting the data. Information security has evolved from using weak authentication measures like username/password to using key-based systems like sitekey, private-key, public-key and others. In the same vein, we include a secret-key, transmitted through a separate secure channel, in the proposed model.

![](/api/attachments/TVKY5JZ6/fulltext/images/eddcadb76b70283a300661585acec92109dd0466513001c143911a6951bca3aa.jpg)  
Fig. 1. Steganographic model for hiding animations [4].

Second, existing practical models assume that the secure channel is nothing but a public channel that is encrypted. The model clearly delineates public and private channels either physically or by means of time. Warden does not have access to private channel.

Third, existing models assume that the attacker (warden) does not have any knowledge about the steganographic algorithm. The principles of modern information security recommend that an information security algorithm should be publicly known. Such a philosophy is called “Kerckhoff’s principle.” Thus, we assume that the steganographic algorithm is publicly available and is even known to the attacker.

![](/api/attachments/TVKY5JZ6/fulltext/images/3a50551e4cd668705bb1d7abd6ba623044ebb2c9d2c48ebb7f88e1901333d4cc.jpg)  
Fig. 2. Flowchart describing the encoding and decoding process.

![](/api/attachments/TVKY5JZ6/fulltext/images/4120b1105d791b3ea36d3bbc42f192e2403966306c20c4ac7cf12527bab7074e.jpg)  
Fig. 3. Frame table creation.

Fourth, some existing models require that the cover and stego be known to the receiver. The proposed model does not impose this restriction. The receiver should be able to extract the hidden data based on stego and secret key.

Fifth, the proposed model provides different parameters in a modular design. This facilitates extending the model by adding more components.

## 4. Proposed steganographic algorithm

This section describes the proposed algorithm for the stego-system de<sup>fi</sup>ned in Fig. 1. Before proceeding to the algorithm, we will de<sup>fi</sup>ne the important terminology to understand the algorithm.

## 4.1. Terminology

Animation and image frames: An animation is a collection of moving diagrams that are made up of a series of images representing a narration. The images are connected by unity of either location or time. Therefore, an animation is composed of a sequence of images. The individual image used in such an animation is an image frame. Animations are available in different digital formats like GIF animations, <sup>fl</sup>ash animations etc., which are common in web applications. As an example, let i , i , i etc., represent the image frames.

Motion: A subset of animation which represents a meaningful semantic is called a motion. A motion composes two or more image frames. As an example, let $\begin{array} { r } { m = i _ { 1 } i _ { 2 } i _ { 3 } } \end{array}$ represent a motion represented by the sequence of images $i _ { 1 } , i _ { 2 } ,$ and $i _ { 3 } .$

Image transition set: A set of two or more image frames that sequentially represents a motion in an animation. The cover-animation transition set consists of a permutation of t image frames. As an example, let $\mathrm { I T S } _ { \mathrm { C } } { = } \{ m _ { 1 } , m _ { 2 } { , } { \ldots } { , } m _ { \mathrm { t c } } \}$ be an image transition set for cover-animation.

Animation probability distribution: $P _ { \mathrm { C t } }$ represents the probability distribution of each image transition in a coveranimation image transition set. $P _ { \mathrm { S t } }$ represents the probability distribution of each image transition in a stego-animation image transition set. As an example, the probability distribution of each image transition in a cover animation can be speci<sup>fi</sup>ed by the following formula:

$$
P _ {C t} = \operatorname * {P r} (X \leq x) = \sum_ {X \leq x} \operatorname * {P r} (x) \forall x \in I T S _ {c}
$$

Secret data: This is the data that has to be sent from the sender to the receiver without the knowledge of warden. Modular arithmetic representation is used for secret data (mod n). Here, n is the number system of the secret data. It could be either text (n=26), binary (n=2), hex (n=16), octal (n=8), or any n-ary number system.

Data transition set: The secret data is grouped into permutations of $t _ { \mathrm { E } }$ elements. It contains all possible permutations of n numbers in $t _ { \mathrm { E } }$ positions.

Data probability distribution: $P _ { \mathrm { E t } }$ represents the probability distribution of each element in the data transition set.

Secret:-key (K) It is assumed that only the sender and receiver know the values of K, which is transmitted through a secure private channel. K is composed of $( n , t _ { \mathrm { E } } , P _ { \mathrm { E t } } , t _ { \mathrm { C } } )$

```txt
Procedure Encode (K, C, E, S)
INPUT
K: secret key
C: cover-animation
E: secret data
OUTPUT
S: stego-animation
1 CreateProbabilityDistributionTable(C, t_C, N, P_{ct})
2 if (N < t_c) then
3 Choose a different cover-animation
4 Return
5 minimumDistance ← 0
6 for each P ∈ AllPermutations(P_{ct}) do
7 Distance ← KSTEST(P_{ET}, P)
8 if (Distance < minimumDistance) then
9 minimumDistance ← Distance
10 minP ← P
11 P_{ct} ← minP
12 for each t_E patterns in E do
13 S ← S + [image frames represented by P_{ct} that is closest to P_{et} (pattern)]
14 GifAnimate(All image frames in S)
15 Return
```  
Fig. 4. Pseudocode for encoding the secret data into cover-animation.

## 4.2. Description of the proposed algorithm

Fig. 2 shows the <sup>fl</sup>owcharts of encoding and decoding algorithms. The <sup>fl</sup>owchart on the left-hand side explains the steps that a sender would follow to hide secret data into an animation. The other <sup>fl</sup>owchart on the right-hand side explains the steps that a receiver would perform to extract the secret data from the animation. The dotted line represents the boundary line for separating the transmission of public and private information. The sender constructs the secret key, K and sends it through the private channel. The receiver receives K and is ready for operation in the public channel. As described earlier, the secret key is an important component in a stego-system and is shared only between the sender and the receiver.

Encoding: The sender hides the secret-data (E) by an encoding process. The sender accepts an original animation (C). Then, N unique images in each animation are found out by using frame grabber software. Each of these images is labeled for identi<sup>fi</sup>cation purposes. Fig. 3 explains the creation of a frame table. The frame table consists of a frame ID, which identi<sup>fi</sup>es each frame uniquely, and a corresponding picture image. This is a tabular representation of the set F described above. The frame table is represented by an array of (frame ID, pointer to the image <sup>fi</sup>le). The original animation sequence is passed through a frame grabber. The function of the frame grabber is to capture each frame/image in the animation sequence. These frames are inputted to a hamming network to identify the unique set of frames used in this animation. The frame table consists of identi<sup>fi</sup>cation numbers for denoting an image frame.

Fig. 4 shows the pseudocode of the encoding process. The cover-animation probability distribution is created by the code. Fig. 5 shows the functional implementation of <sup>fi</sup>nding out the probability distribution for image transitions. For the purposes hamming network, is used for image recognition. The features are also decided by the hamming network. The features are dimensions of the picture, edges in the picture, color resolution, and color palette. The neural network is trained based on each of these features. See Lines 3–11 in Fig. 5. If the number of unique image frames, N is less than the speci<sup>fi</sup>ed number of transitions in a motion (t ) then we choose a different cover-animation whose $N { > } t _ { C } .$ Then, we generate all permutations of N images taken t at a time. See Line 16 in Fig. 5. For each of these arrangement tuple, we construct a histogram as the number of occurrences of this sequence in the original animation. See Lines 19–22 in Fig. 5. A probability distribution function is constructed for the above histogram See Lines 23–24 in Fig. 5. The pseudocode in Fig. 5 returns this probability distribution function $( \mathrm { P _ { C t } } )$ to the Encode function in Fig. 4.

The key to the proposed algorithm is to <sup>fi</sup>nd a matching probability distribution of cover-animation that is closest to the probability distribution of the secret data $( \mathrm { P _ { E t } } ) .$ . For this purpose, we use the well-known Kolmogorov–Smirnov test [15] for <sup>fi</sup>nding the distance between two distributions. The

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Procedure CreateProbabilityDistributionTable (A, t, N, P$_{ct}$)
INPUT
A: animation
t: number of transitions in A
OUTPUT
N: Number of unique image frames
P: Probability distribution function of A
OTHERS
ann: an artificial neural network like Hamming Network to identify images
features: properties of each image frame
1 frameID ← 1
2 Unique = null /* empty set */
3 for each imageFrame ∈ A do
4    if ~Unique(imageFrame) break /* duplicate */
5    i ← 1
6    for each feature' ∈ Features(imageFrame) do
7    features(i)←value(feature')
8    i ← i +1
9    Train (ann, feature)
10    Unique ← Unique + (frameID, Pointer to imageFrame)
11    frameID ← frameID + 1
12 N ← No. of Elements in Unique
13 if (N &lt; t) then
14    Choose a different cover-animation
15 Return
16 Motions ← [All possible combinations and permutations of N image frames in of length t$_{c}$]
17 i ← 1
18 histogram ← New empty array for each element in Motions
19 for each imageMotion ∈ Motions do
20    for each Pattern(imageMotion) ∈A do
21    histogram[i] ← histogram[i] + 1
22    i ← i+1
23 for j← 1 to i do
24    P[j] ← histogram[i] / Total
25 Return
</div>

Fig. 5. Pseudocode for creating the probability distribution function.

```txt
Procedure Decode (K, Š, Ê)
INPUT
K: secret key
Š: received stego-animation
OUTPUT
Ê: extracted data
1 CreateProbabilityDistributionTable(S, tC, N, Pct)
2 if (N < tC) then
3    Data cannot be extracted
4    Return
5 minimumDistance ← 0
6 for each P ∈ AllPermutations(Pet) do
7    Distance ← KSTEST(Pct, P)
8    if (Distance < minimumDistance) then
9    minimumDistance ← Distance
10    minP ← P
11 PEt ← minP
12 for each tc patterns in Š do
13    Ê ← Ê + [data pattern represented by represented by PET that is closest to Pct(image pattern)]
14 Return
```  
Fig. 6. Pseudocode for decoding the secret data into cover-animation.

Kolmogorov–Smirnov (KS) is a commonly described normality test available in the literature. The KS is based on maximum difference between the sample cumulative distribution and the hypothesized cumulative distribution. The proposed steganographic method chooses the Kolmogorov–Smirnov algorithm over all other normality testing algorithms because the KS does not depend on the number of intervals, which makes it more powerful than the chi-square test. The function KSTEST in Line 7 calls the prede<sup>fi</sup>ned function as implemented by the pseudocode in [15]. The order of $P _ { \mathrm { C t } }$ is varied to <sup>fi</sup>nd out the combination of $P _ { \mathrm { C t } }$ that is closest to $P _ { \mathrm { E t } } .$ See Lines 5–11 in Fig. 4. Finally, each pattern in the secret-data, E is replaced by the image-frame set represented by corresponding $P _ { \mathrm { C t } }$ . See Lines 12–13 in Fig. 4. The rationale behind using such an algorithm is that the key requirement in a steganographic algorithm is detection. If the probability distribution of S is close to C, then the detection is dif<sup>fi</sup>cult. We construct a mapping between the probability of distribution of C and probability of distribution of E. Thus, the probability of S is the same as C for a warden who does not have the secret key (K). But, the receiver who has knowledge about K can decode using the algorithm in Fig. 6. Finally, all these image frames are concatenated and encoded into a GIF <sup>fi</sup>le for transmission. See Line 14 in Fig. 5.

Decoding: The decoding process or extraction of the secret data from the animation is performed by the receiver. Fig. 6 describes the pseudocode of the decoding algorithm. First, based on the secret key, the probability distribution of the received stego-animation, $\mathrm { P _ { C t } }$ is created. We use the same symbol $\mathrm { P _ { C t } }$ because it is the same as the coveranimation. If the number of unique image frames (N) is less than $\mathrm { t _ { c } , }$ the hidden secret-data cannot be extracted. We <sup>fi</sup>nd the combination of $\mathrm { \Delta P _ { E t } }$ with minimum distance from $\mathrm { P _ { C t } }$

See Lines 5–11 in Fig. 6. It can be observed that the roles of $\mathrm { P _ { E t } }$ and $\mathrm { P _ { C t } }$ is reversed from encoding and decoding function. Based on the image sequence found in the received animation, the algorithm decodes each image transition sequence and its corresponding secret data sequence. See Lines 12–13 in Fig. 6.

Discussion: This encoding/decoding algorithm is based on the premise that there exists at least one combination of the probability distributions of cover-animation and probability distributions of secret data that are closest in distance to each other. By reducing the difference in probability distribution, we can minimize the relative entropy between the coveranimation and the secret-data. The research [4] suggests relative entropy can be approximated by mathematical distance. Hence, we use Kolmogorov–Smirnov test [15] several times on all possible combinations of the probability distribution to <sup>fi</sup>nd the minimum distance and the closest combination of probability distribution. After <sup>fi</sup>nding the closest probability distribution, we match the corresponding patterns from cover-animation to secret-data. Thus, there is a one-toone mapping between patterns of cover-animation and secret-data.

## 5. Experimental results

## 5.1. Software

The purpose of this study is to compare the performance of embedding algorithm (animated-DIIT), encoding algorithm (gifshuf<sup>fl</sup>e) and the proposed algorithm. All these algorithms are performed on an animation as a cover. As of this writing, there were not many software available that could hide data in an animation. The DIIT algorithm is modi<sup>fi</sup>ed in a manner that it can be used to hide animations. This modi<sup>fi</sup>ed DIIT is henceafter referred to as animated-DIIT. Fig. 7 describes the animated-DIIT from the sender’s perspective.

![](/api/attachments/TVKY5JZ6/fulltext/images/c585090dbe9d28ecc244690bfbaf975cd9c5fdcae4d22333d0bfd5a2f48ff2ca.jpg)  
Fig. 7. Animated-DIIT.

Table 2  
Table 1  
Categories of animations (As of April 1, 2006)

<table><tr><td>Category</td><td>Count</td><td>Average No. of Unique frames</td><td>Average file size (in KB)</td><td>Average No. of pixels in each image frame</td></tr><tr><td>Donald</td><td>5</td><td>8</td><td>5.83</td><td>9408</td></tr><tr><td>Titi and Grosminet</td><td>10</td><td>15</td><td>5.12</td><td>8428</td></tr><tr><td>Simpsons</td><td>25</td><td>10</td><td>9.98</td><td>10080</td></tr><tr><td>Snow white and Cinderella</td><td>15</td><td>13</td><td>12.37</td><td>13572</td></tr><tr><td>Biblical figures</td><td>20</td><td>15</td><td>13.10</td><td>20383</td></tr><tr><td>Prehistory</td><td>15</td><td>19</td><td>12.87</td><td>6557</td></tr><tr><td>Fruit</td><td>10</td><td>12</td><td>3.12</td><td>1768</td></tr></table>

Gifshuf<sup>fl</sup>e [22] is a software that can hide data in gif animations. DIIT (Digital Invisible Ink Toolkit) [17] can hide data into digital images. The proposed approach can encode information in animations created from BMP (BitMap) images. DIIT is capable of operating on JPEG (Joint Photographic Experts Group), BMP (BitMap), and PNG (Portable Network Graphics) images. Thus, gif image frames are converted into BMP formats. DIIT and Gifshuf<sup>fl</sup>e are open source. The source code is available to do modi<sup>fi</sup>cations and extend it according to our proposed steganographic model. Gifshuf<sup>fl</sup>e is written in C programming language. DIIT is written in Java programming language. The proposed approach is written in C# programming language.

## 5.2. Data set

For testing the three algorithms, we obtained 100 animations as cover-animations from the following website: http://us.bestgraph.com/. The 100 cover-animations are classi<sup>fi</sup>ed into various categories as shown in Table 1. Figs. 8 and 9 shows sample frames of the animation from Simpsons category.

## 5.3. Performance measures

In Section 2, we have identi<sup>fi</sup>ed the requirements of a steganographic system as capacity, detection, distortion, and robustness. In this section, the capacity and distortion of the three algorithms are measured. Then, detection and robustness are discussed from the perspective of security. Finally, the computation time taken by each algorithm is measured.

![](/api/attachments/TVKY5JZ6/fulltext/images/595a29fa31337118b2adbb4f3466224aca18581cc2034acc610fb6b403d8a9cb.jpg)  
Fig. 8. Simpsons Category — Bart. Source: http://us.bestgraph.com

![](/api/attachments/TVKY5JZ6/fulltext/images/1ff35496666cfeca0697a0c23f3bfd22dc6fd98603389db6131d811b95868ca6.jpg)  
Fig. 9. Simpsons Category — Maggie. Source: http://us.bestgraph.com.

Hiding rate: We measure the steganographic capacity (maximum number of bits that a cover-object can hide) all 100 animations. Since the cover-animation does not change size, the measurement of steganographic capacity is straightforward in the case of embedding steganography. In the case of encoding steganography, the cover-animation can change the size. To generalize the measure, we use the capacity as a ratio, hiding rate. Hiding rate is derived from [19], and is expressed as:

$$
\text{Hiding Rate} = \frac {\text { Hiding Data Size }}{\text { Data Size of Cover }} \times 100 \%
$$

Table 2 describes the minimum, maximum, and average hiding rate of the 100 cover-animations obtained using gifshuf<sup>fl</sup>e, animated-DIIT, and the proposed approach, respectively. Gifshuf<sup>fl</sup>e has the least average hiding rate (0.7283%). The proposed approach has the highest hiding rate (2.0179%).

The three algorithms are not only different but also contradictory. This is observed from the hiding rates of cover-animations, Maggie and Bart. Maggie has a minimum hiding rate of 0.0106% when gifshuf<sup>fl</sup>e is used to embed data into it. While animated-DIIT and the proposed approach achieve a maximum hiding rate on Maggie with rates 4.0301% and 4.0916%, respectively. This signi<sup>fi</sup>cant difference may be due to the fact that Maggie has fewer colors and hence the color-table used in the gif compression is smaller. Hence, the hiding capacity for the gifshuf<sup>fl</sup>e algorithm is limited. Animated DIIT embeds the hidden data into each image, and since Maggie has 21 image frames in its animation and each image frame has 13,572 pixels (116×117), it achieves the highest hiding rate. In the approach, since Maggie has the highest number of transitions among the 100 animations, we achieve higher hiding rate than the rest.

It is generally observed that the hiding rate increases with the <sup>fi</sup>le size for a Gifshuf<sup>fl</sup>e algorithm. For an animated-DIIT algorithm, the hiding rate is directly proportional to number of pixels in image frame and number of image frames. In the case of our proposed approach, the hiding rate is only related to the number of unique image frames in the animation (N).

Computational cost: Calculating the time taken for an algorithm to execute is a very important decision factor in real-time applications. All the experiments were performed on a Windows XP system based on Intel Pentium IV 2.40 GHz CPU. Table 3 shows the average CPU execution time required by each hiding algorithm for the 100 animations.

Results of hiding rate (%)

<table><tr><td></td><td>Gifshuffle</td><td>Animated-DIIT</td><td>Our approach</td></tr><tr><td>Min. Hiding Rate</td><td>0.0106 (Maggie)</td><td>0.1204 (Bart)</td><td>0.2131 (Bart)</td></tr><tr><td>Max. Hiding Rate</td><td>2.1493 (Bart)</td><td>4.0301 (Maggie)</td><td>4.0916 (Maggie)</td></tr><tr><td>Avg. Hiding Rate</td><td>0.7283</td><td>1.2721</td><td>2.0179</td></tr></table>

Table 3  
Results of CPU time (milliseconds)

<table><tr><td></td><td>Gifshuffle</td><td>Animated-DIIT</td><td>Our approach</td></tr><tr><td>Min. CPU time</td><td>0.1346 (Maggie)</td><td>0.5014 (Lisa)</td><td>1.4572 (Bart)</td></tr><tr><td>Max. CPU time</td><td>1.2639 (Cinderella)</td><td>5.1956 (Maggie)</td><td>10.3541 (Maggie)</td></tr><tr><td>Avg. CPU time</td><td>0.2401</td><td>2.0443</td><td>4.0747</td></tr></table>

The execution time of the proposed approach is the highest among the three algorithms. As described in the previous section, the proposed algorithm has multiple combination and permutations. Even hiding in a simple animation like Bart (3 unique images) requires 1.4572 (ms: millisecond); this is higher than the maximum CPU execution time for Gifshuf<sup>fl</sup>e. Gifshuf<sup>fl</sup>e is the fastest because the algorithm reads the color table of the gif animation into an array data structure, embeds data, and then writes it to disk. It is a very straightforward algorithm. In the case of animated DIIT, it reads each image frame into a 2-dimensional array, embeds into the bitmap of each image frame, and <sup>fi</sup>nally writes the data to a disk. Thus, it takes time than the Gifshuf<sup>fl</sup>e. The proposed approach reads all the image frames twice. First, it reads to build the probability distribution table Second, it reads to encode the images according to the hidden data. Then, <sup>fi</sup>nally it writes data to disk. This process takes more time than the other three algorithms. The last row represents the average CPU time taken for each of the three algorithms. The different programming languages used to write the software may also have played a role in the different CPU times achieved in our experiment.

Distortion: The distortion between the cover and stego is measured by weighted mean squared error (MSE). The MSE for each animation is calculated as shown in Fig. 10. Table 4 shows the different weighted MSE values for 100 animations. In the proposed approach, this method for measuring is not applicable as the individual images in the animation are rearranged. As mentioned previously, the proposed encoding algorithm only rearranges the images in the animation according to the distance between the probability distributions of cover-animation and secret-data. In the case of the other two steganography algorithms, the average weighted MSE ranges from 34.7164 to 41.1573. The gifshuf<sup>fl</sup>e has less

Table 4  
Results of weighted mean square error

<table><tr><td></td><td>Gifshuffle</td><td>Animated-DIIT</td><td>Our approach</td></tr><tr><td>Min. MSE</td><td>16.2366 (Bart)</td><td>34.1872 (Mothers Day)</td><td>NA</td></tr><tr><td>Max. MSE</td><td>67.8234 (Birthday)</td><td>79.2814 (Maggie)</td><td>NA</td></tr><tr><td>Avg. MSE</td><td>34.7164</td><td>41.1573</td><td>NA</td></tr></table>

MSE because of its operation on palette based images, and it only modi<sup>fi</sup>es the color table. In the case of animated-DIIT, it operates on each pixel of the bitmap-based images. Hence, animated-DIIT has the maximum average MSE.

Security analysis: The research [18] de<sup>fi</sup>nes robust steganography to be a model between the sender and the warden in which the warden is allowed to do some pre-de<sup>fi</sup>ned limited alterations to the stego-object. Another effort [11] de<sup>fi</sup>nes a robust channel as one whose content cannot be altered without making unreasonably drastic changes to the stegoobject (i.e., requiring a malicious, instead of an active warden). As mentioned previously, based on the types of wardens, the steganographic security can be classi<sup>fi</sup>ed as detection and estimation. A passive warden tries to detect the presence of a hidden data in the stego-animation, whereas an active warden tries to decode/extract the hidden data. Many researchers discuss the security of a steganographic algorithm based on two types of attacks that can be carried out on those systems, stego-only attack and known-cover attack [26].

In a stego-only attack, the warden is assumed to have information only about the stego-animation. From the perspective of a passive warden, all the three algorithms exhibit minimum distortion. They also maintain a high <sup>fi</sup>delity that is close to the original animation. In the proposed algorithm, the number of image frames is different in the cover and stego animations. Still, it preserves the <sup>fi</sup>delity of the original animation by maintaining the same probability distribution in the stego as the cover. Thus, these stegoanimations do not trigger any alert to a passive warden. From the perspective of an active warden, one may subject the stego-animation to incidental attacks such as rotation, scaling, or embedding into the image frames of stegoanimation. Incidental attacks were carried out on the 100 animations and the secret data was not recovered in the case of gifshuf<sup>fl</sup>e and animated-DIIT algorithm. This is because such incidental attack operations change the format of the individual image frames in the animations. The proposed algorithm was able to recover all the secret-data in the 100 animations. See Table 5. For example, if the active warden rotates or scales all the image frames in the stego-animation, it will not affect the decoding process. But, if the active warden uses such operations like slicing or cutting some of the image frames from the animation, it affected our decoding process and the proposed algorithm also failed.

```txt
Function WeightedMSE (I, J, CF, SF)
INPUT
I: No. of rows in each cover-animation frame
J: No. of columns in each cover-animation frame
CF: Pixel values of all the image frames in cover-animation
SF: Pixel values of all the image frames in stego-animation

1 TotalMSE ← 0
2 for each imageFrame ∈ Unique(C) do
    ∑_{i=1}^{I} ∑_{j=1}^{J} \left( CF_{ij} - SF_{ij} \right)^{2}
3    MSE = \frac{I \times J}{I \times J}
4    TotalMSE ← TotalMSE + MSE
5 weightedMSE <- TotalMSE / N in S)
6 Return
```

Table 5  
Summary of steganography algorithms in security perspective

<table><tr><td rowspan="2"></td><td colspan="5">Stego-only attacks</td><td rowspan="2">Known-cover attacks</td><td rowspan="2">Known-algorithm attacks</td></tr><tr><td>Rotation</td><td>Scaling</td><td>Embedding</td><td>Slicing</td><td>Cutting</td></tr><tr><td>Gifshuffle</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td></tr><tr><td>animated-DIIT</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td><td>N</td></tr><tr><td>Our proposed approach</td><td>Y</td><td>Y</td><td>Y</td><td>N</td><td>N</td><td>N</td><td>Y</td></tr></table>

In the known-cover attack, the warden has information about the cover-animation and the stego-animation. In this case, all our algorithms will fail. There is no existing steganographic algorithm which can protect against known-cover attack. This is because the warden can easily detect the difference between the cover and stego by applying all statistical tests on all features of the digital media.

In addition to the above documented attack methods, this study discusses an additional method based on “Kerckhoff’s principle.” This principle is mostly applied to the design of modern cryptographic systems and also provides a worst-case scenario that could happen to a security system. We assume that the warden has information about the encoding/decoding algorithm used. The warden does not have access to the secret key. We call such an attack mode as known-algorithm attack. From the perspective of this attack, Gifshuf<sup>fl</sup>e and animated-DIIT provide a password as a secret key. This password is encrypted in the stego-animation. Since encrypted data is easy to detect, it alerts the warden that there is a hidden message in the animation. Thus, the primary requirement of steganography, escaping detection from a warden, is not satis<sup>fi</sup>ed. The steganalysis techniques provided by the DIIT software do some standard steganalysis techniques, but fails to consider this attack methodology. In the proposed model, the secret key is sent through a private secure channel before the start of the operation of the stego-system. Thus, the warden does not have any access to the secret key. This is an advantage in the design of our stego-system.

Table 5 shows the summary of the above discussion. A ‘Y’ in the cell indicates that the secret data was completely recovered from the 100 animations. A ‘N’ indicates that the secret data was not recovered from the 100 animations.

## 6. Conclusions and future extension

This study proposed a novel information hiding algorithm based on animations, secret-key stego-systems, and encoding. Animations are widely used in advertising, facial recognition, and web-development. An animation can be divided into many meaningful motions; each motion can represent a semantic in itself. The different algorithms in literature were categorized as embedding, encoding, and hybrid. The design of the proposed model was compared with the other available conventional practical models. The performance of the proposed algorithm was evaluated with other encoding and modi<sup>fi</sup>ed-embedding algorithms. The basic rationale for using animations and encoding algorithms was justi<sup>fi</sup>ed in the experimental analysis. Encoding algorithms provide better security with less distortion.

The proposed approach was compared to the encoding animation steganography software, gifshuf<sup>fl</sup>e, and to the modi<sup>fi</sup>ed image embedded transform-based steganography software, DIIT. There were no existing hybrid steganography techniques for animation. The proposed approach performs better than the other approaches in terms of hiding rate and weighted mean square error. Gifshuf<sup>fl</sup>e performs better than the other two approaches in terms of computational cost. A detailed analysis of the security of the algorithms indicates that none of the algorithms are robust to offensive attacks. Only the proposed approach could withstand incidental attacks.

Information security is a very dynamic <sup>fi</sup>eld and it is very important that it is easy for system designers to design a practical model [25]. The proposed extended steganographic model for animations is consistent with the recent theoretical work in the <sup>fi</sup>eld of steganography. The advantage of the proposed model with respect to the theoretical models discussed is that the proposed secret key does not depend on the cover. Thus, the cover-animation can be changed with every transmission without changing the secret key. The proposed model is better than conventional practical models in terms of secret-key management, private channel, and analysis of known-algorithm attack.

In spite of all the advantages discussed above, the proposed model lacks in the fact that the sender cannot change the secret data distribution. This is because the secret key depends on the probability distribution of the secret data. The secret-key is dependent on the probability distribution and number system of the secret-data. Hence, if we change the secret data, we have to initialize the system again to a new secret key. This can be overcome by having 2 private channels and 2 secret-keys with different level of security. The disadvantage of the proposed algorithm is that it takes more time to execute and more space is required if the length of secret data increases. This is a shortcoming of this approach. One way to overcome this would be to use ensemble algorithms by combining embedding and encoding. Future work is needed in this direction to carefully combine embedding into each frame and still keep the high robustness factor that has been achieved. Furthermore, the proposed approach is limited in the fact that it is more suitable to live animation plays, i.e., a live telecast of images would be the most appropriate. An extension of this model to the recorded video/audio formats is an important future research work. Steganalysis of the steganographic models is an important future extension of this study

An important research question that needs to be followed in a future research agenda is why the proposed approach is better. i.e., a theoretical analysis of the proposed model with respect to the other approaches should provide a deep knowledge as to why and how the proposed approach is superior to the other approaches. Such a mathematical analysis is an important future research extension of this study.

The proposed stego-system is novel in that it provides not only the theoretical aspect but also practical implementation of a secret-key encoding stego-system. It provides us with a practical way of matching the probability distributions of cover and secret-data based on Kolmogorov-Smirnov statistical test. This is a very important premise of this algorithm because many theoretical models discuss the security of a steganographic algorithm based on the statistical analysis of the stego.

Finally, it is hoped that this study makes a contribution on the development of steganography. We look forward to seeing further research extensions, as discussed in this article.

## References

[1] B. Anckaert, B. De Sutter, D. Chanet, K. De Bosschere, Steganography for executables and code transformation signatures, Lecture Notes in Computer Science, 2005, pp. 425–439.

[2] S. Ba, K.R. Lang, A.B. Whinston, Enterprise decision support using intranet technology, Decision Support Systems 20 (2) (1997) 99–134.

[3] D.J. Berndt, J.W. Fisher, J.G. Craighead, A.R. Hevner, S. Luther, J. Studnicki, The role of data warehousing in bioterrorism surveillance, Decision Support Systems 43 (2007) 1383–1403.

[4] C. Cachin, An information-theoretic model for steganography, Information and Computation 192 (1) (2004) 41–56.

[5] K.M. Carley, J. Diesner, J. Reminga, M. Tsvetovat, Toward an interoperable dynamic network analysis toolkit, Decision Support Systems 43 (2007) 1324-1347.

[6] I.I. Chae, B.S. Maniunath. Data hiding in video. IEEE International Conference on Image Processing 1 (1999) 311–315.

[7] R. Chandramouli, N. Memon, Analysis of Lsb based image steganography techniques, IEEE International Conference on Image Processing (ICIP), Oct 7–10 2001, Thessaloniki, 2001, pp. 1019–1022.

[8] C.C. Chang, J.C. Chuang, Y.C. Hu, Spatial domain image hiding scheme using pixel-values differencing, Fundamenta Informaticae 70 (3) (2006) 171–184.

[9] B. Chen, G.W. Wornell, Quantization index modulation methods for digital watermarking and information embedding of multimedia, The Journal of VLSI Signal Processing 27 (1–2) (2001) 7–33.

[10] Q. Cheng, T.S. Huang, An additive approach to transform-domain information hiding and optimum detection structure, IEEE Transactions on Multimedia 3 (3) (2001) 273–284.

[11] S. Craver, On public-key steganography in the presence of an active warden, Proceedings of 2nd International Workshop on Information Hiding, Portland, Oregon, USA, 1998, pp. 355–368.

[12] N. Cvejic, T. Seppanen, Increasing robustness of Lsb audio steganography using a novel embedding method, in: International Conference on Information Technology: Coding Computing, ITCC 2004, Apr 5–7 2004, Las Vegas, NV, United States, 2004, pp. 533–537.

[13] M. Fahmy Tolba, M. Al-Said Ghonemy, I.A.H. Taha, A.S. Khalifa, High capacity image steganography using wavelet-based fusion. Proceedings — International Symposium on Computers and Communications, 2004, pp. 430–435.

[14] J. Fridrich, D. Soukal, Matrix embedding for large payloads, IEEE Transactions on Information Security and Forensics 1 (3) (2006) 390–395.

[15] T. Gonzalez, S. Sahni, W.A. Franta, An ef<sup>fi</sup>cient algorithm for the Kolmogorov–Smirnov and Lilliefors Test, ACM Transactions on Mathe matical Software 3 (1977) 60–64.

[16] J.V. Hansen, P.B. Lowry, R.D. Meservy, D.M. McDonald, Genetic programming for prevention of cyberterrorism through dynamic and evolving intrusion detection, Decision Support Systems 43 (2007) 1362–1374.

[17] K. Hempstalk, "Digital Invisible Ink Toolkit,", University of Waikato, 2005.

[18] N.J. Hopper, J. Langford, L.V. Ahn, Provably secure steganography, in: Advances in Cryptology: CRYPTO, 2002.

[19] D. Inoue, T. Matsumoto, A scheme of standard midi <sup>fi</sup>les steganography and its evaluation, in; Security and Watermarking of Multimedia Contents IV, Jan 21–24 2002, San Jose, CA, United States, 2002, pp. 194–205.

[20] D. Inoue, M. Suzuki, T. Matsumoto, Detection-resistant steganography for standard midi <sup>fi</sup>les, IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences E86-A 8 (2003) 2099–2106.

[21] S. Katzenbeisser, F.A.P. Petitcolas, Information Hiding Techniques for Steganography and Digital Watermarking: Artech House, 2000

[22] M. Kwan, "Gifshuf<sup>fl</sup>e," 2003

[23] A.L. Lederer, D.J. Maupin, M.P. Sena, Y. Zhuang, Technology acceptance model and the World Wide Web, Decision Support Systems 29 (3) (2000) 269–282.

[24] Y.K. Lee, L.H. Chen, A Secure Robust Image Steganographic Model, 2000

[25] J. Lee, H.R. Rao, Perceived risks, counter-beliefs, and intentions to use anti-/counter-terrorism websites: an exploratory study of governmentcitizens online interactions in a turbulent environment, Decision Support Systems 43 (2007) 1431–1449.

[26] D.C. Lou, C.H. Sung, A steganographic scheme for secure communications based on the Chaos and Euler Theorem, IEEE Transactions on Multimedia 6 (3) (2004) 501–509.

[27] P. Moulin, R. Koetter, Data-hiding codes, Proceedings of the IEEE 93 (12) (2005) 2083–2125.

[28] P. Moulin, J.A. O'Sullivan, Information-theoretic analysis of information hiding, IEEE Transactions on Information Theory 49 (3) (2003) 563–593.

[29] H. Noda, T. Furuta, M. Niimi, E. Kawaguchi, Video steganography based on bit-plane decomposition of wavelet transformed video, in:Security, Steganography, and Watermaking of Multimedia Contents VI, Jan 19–22 2004, San Jose, CA, United States, 2004, pp. 345–353

[30] B. P<sup>fi</sup>tzmann, Information hiding terminology, Proceedings of First Workshop of Information Hiding, Cambridge, UK, 1996, pp. 347–350.

[31] R. Radhakrishnan, M. Kharrazi, N. Memon, Data masking: a new approach for steganography? Journal of VLSI Signal Processing Systems for Signal, Image, and Video Technology 41 (3 SPEC. ISS.) (2005) 293–303.

[32] T.S. Raghu, H. Chen, Cyberinfrastructure for homeland security: advances in information sharing, data mining, and collaboration systems, Decision Support Systems 43 (2007) 1321–1323.

[33] R. Ratan, C.E. Veni Madhavan, Steganography based information security, IETE Technical Review (Institution of Electronics and Tele communication Engineers, India) 19 (4) (2002) 213–219.

[34] H.T. Sencar, M. Ramkumar, A.N. Akansu, An overview of scalar quantization based data hiding methods, Signal Processing 86 (5) (2006) 893–914.

[35] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002) 111–126.

[36] D.B. Skillicorn, N. Vats, Novel information discovery for intelligence and counterterrorism. Decision Support Systems 43 (2007) 1375–1382.

[37] S. Sridhar, Decision support using the intranet, Decision Support Systems 23 (1) (1998) 19–28.

[38] R. Tachibana, Two-dimensional audio watermark for Mpeg Aac Audio, in: Security, Steganography, and Watermaking of Multimedia Contents VI, Jan 19–22 2004, San Jose, CA, United States, 2004, pp. 139–150.

[39] S. Venkatraman, A. Abraham, M. Paprzycki, Signi<sup>fi</sup>cance of steganography on data security, in: information technology: coding and computing, 2004, Proceedings. ITCC 2004. International Conference on, vol.2, 2004, pp. 347–351.

[40] H. Wang, S. Wang, “Cyber warfare: steganography vs. steganalysis,” Communications of the ACM, vol. 47, 2004, pp. 76–82.

[41] C.C. Yang, K.W. Li, An associate constraint network approach to extract multi-lingual information for crime analysis, Decision Support Systems 43 (2007) 1348–1361.

[42] X. Zhang, S. Wang, Stego-encoding with error correction capability, IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences E88-A (12) (2005) 3663–3667.

Gopalakrishna Reddy Tadiparthi is a Ph.D. candidate with the Department of Computer Science, New Mexico Institute of Mining and Technology, Socorro, NM 87801 USA. (e-mail: gtadiparthi@computer.org).

Toshiyuki Sueyoshi is a full professor at the Department of Management, New Mexico Institute of Mining and Technology Socorro, NM 87801 USA. (phone: 505-835-6452; fax: 505-835-5498; e-mail: toshi@nmt.edu). He also is a visiting full professor at National Cheng Kung University, Department of Industrial and Information Management. Tainan. Taiwan.
