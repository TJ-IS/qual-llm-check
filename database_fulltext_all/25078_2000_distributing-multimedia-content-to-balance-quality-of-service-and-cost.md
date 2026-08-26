---
otero_id: 25078
otero_key: "V3ZBN4AW"
title: "Distributing Multimedia Content to Balance Quality of Service and Cost"
authors: ""
year: "2000"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2000.11045636"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [UQ Library] On: 26 July 2015, At: 23:16 Publisher: Routledge Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: 5 Howick Place, London, SW1P 1WG

![](/api/attachments/V3ZBN4AW/fulltext/images/dad94140246b9d99c25d8d31a3f19fd73d8c4a4402dde03124907e4e86f71f17.jpg)

## Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# Distributing Multimedia Content to Balance Quality of Service and Cost

Sandeep Purao, Tae-Dong Han Published online: 09 Jan 2015.

To cite this article: Sandeep Purao, Tae-Dong Han (2000) Distributing Multimedia Content to Balance Quality of Service and Cost, Journal of Management Information Systems, 17:1, 141-165

To link to this article: http://dx.doi.org/10.1080/07421222.2000.11045636

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of

access and use can be found at http://www.tandfonline.com/page/ terms-and-conditions

# Distributing Multimedia Content to Balance Quality of Service and Cost

SANDEEP PURAO AND TAE-DONG HAN

SANDEEP PURAO is an Assistant Professor of Computer Information Systems at the J. Mack Robinson College of Business at Georgia State University in Atlanta. He holds a Ph.D. in MIS from the University of Wisconsin–Milwaukee. His research focuses on various aspects of information systems design, with particular emphasis on ob ject-oriented systems. Dr. Purao’s work has appeared in several journals, such as Communications of the ACM, Decision Support Systems, DataBase, Information and Management, and Journal of Education for MIS. His current research interests in clude reuse-based design with analysis patterns, knowledge management for IS de sign, and studies of complex design tasks. He is a member of AIS, ACM, and IEEE.

TAE-DONG HAN is a doctoral candidate in Computer Information Systems at Georgia State University. He received his master’s degree in MIS from the University of Arizona in 1995 and his bachelor’s degree in business administration from Yonsei Uni versity, Seoul, Korea, in 1983. His research interests include software reuse, multimedia object distribution, database management, and object-oriented systems development. He has published in several major IS conferences and is a member of AIS, ACM, and IEEE.

ABSTRACT: An increasing number of computer applications today use multimedia content such as images, sound, and video over distributed networks of computers. Often, a dispersed set of users, with varying demands, requires ongoing access to this content. Effective placement of the multimedia content at different locations/processors thus becomes essential to ensure acceptable quality of service at a reasonable cost. Achieving this requires the consideration of a set of issues quite different from that required for traditional data distribution. These include (a) scale, both in terms of individual objects and in aggregate, (b) importance of form or appearance, making resolution levels an important, controllable variable, and (c) the temporal dimension, placing stringent demands on response time. These concerns make distribution of multimedia content more than a straightforward extension of traditional distribution approaches. We develop a model and a supporting approach to facilitate effective distribution of multimedia content, focusing on multimedia applications in corporate intranets. The model consists of multiple criteria to reflect different aspects of quality of service and cost which we formulate by leveraging variance in resolution levels to capture trade-offs among these criteria. Since the multiple-criteria allocation model is NP-complete, we propose a decision support approach that generates locally efficient solutions using designer-specified targets and evaluates them using fuzzy-set-based heuristics. The complete model and the approach have been implemented in a prototype to ensure feasibility. We demonstrate use of the prototype for a medical imaging application that illustrates applicability and usefulness of our proposals

KEY WORDS AND PHRASES: fuzzy heuristics, multimedia content, multiple-criteria decision making, object distribution.

AN INCREASING NUMBER OF COMPUTER APPLICATIONS today use rich data such as images, sounds, and video over distributed networks of computers. Examples include video-on-demand, digital libraries [1], telemedicine [24] and distance education [7], which are emerging at a fast pace. Delivery of rich data content is also a large part of electronic commerce. As distributed implementations of multimedia computing systems proliferate in organizations, a number of new concerns are emerging. One such concern is the effective distribution of multimedia content. Distribution involves ap propriate placement of distributable units to maximize quality or minimize cost [13, 22]. This stream of research has progressed from an early file allocation focus to data distribution and, most recently, toward object distribution [22].

Distribution of multimedia content presents unique problems not dealt with so far in this stream. Multimedia content can be of different types, including graphics, im ages, animation, audio, video and holograms. For such data, the content is the definition. For instance, storing the objects A, A , A, or Amay have traditionally conveyed the same information from a universe of discourse (letter “A”). For multimedia data, however, it becomes necessary to preserve the form or appearance of the object. An image stored at different resolutions, a sound stored at different sampling rates, or a video stored at different compression schemes may not convey the same information to the user. Multimedia data also have a temporal dimension. Media such as audio and video need to be continuously retrieved and displayed without interruption and in predefined order. Sometimes, synchronization is required across multiple media types—for example, when voice needs to be synchronized with corresponding video. Further, scale is an important issue for multimedia content. Raw multimedia data can take up huge amounts of storage space and incur a significant communication pen alty, making these costs important elements. Finally, multimedia content, once created, is rarely updated in the traditional sense, making the read-one-write-all (ROWA) strategies used as a basis for traditional data distribution inapplicable. These charac teristics make effective distribution of multimedia content more than a straightforward extension of traditional techniques [12]. The distribution design of a multimedia system, and how this distribution addresses the issues noted above, can have a significant impact on the performance and perceived functionality of distributed multimedia applications.

The driving application we use to motivate the development of our distribution scheme comes from the field of telemedicine: a medical imaging and patient consul tation system. An application in this domain needs to create, store, and manipulate multimedia content of various types, such as X-rays, magnetic resonance images, patient history, ultrasound motion images, consultations, etc. These are often used at different work locations for numerous purposes, such as consulting, analysis and research, education, and billing. Distributing this multimedia content in a manner that provides acceptable quality of service at a reasonable cost is a difficult and relevant problem.

The objective of this paper is to present a model and a supporting approach for effective distribution of such multimedia content in corporate intranets. The mode consists of mathematical formulations of criteria, which include multiple dimensions of quality of service and different cost elements. The approach combines simulation and fuzzy-set-based evaluation to tackle the resulting NP-complete decision situation. The remainder of the paper is organized into six sections. The next section reviews previous work on data distribution, with particular emphasis on applicability to multimedia content distribution. Section 3 lays out the foundations for distribution models and presents key notations. Section 4 develops detailed formulae of distribution criteria and discusses technological constraints. Section 5 outlines the distribution approach for finding efficient solutions from the large solution space. In section 6, we describe implementation of the prototype and results for an illustrative example. Section 7 concludes with a brief commentary about applicability, known limi tations, and directions for future research.

## Previous Work

PRIOR WORK IN DATA [13] AND OBJECT [22] DISTRIBUTION has established two broad phases in the distribution process. The first, fragmentation, involves identification of appropriate distributable units. Two fragmentation schemes have been identified: vertical and horizontal. Vertical fragmentation groups attributes based on attribute affin ity [14], whereas horizontal fragmentation groups multiple objects to create object (sub)sets, using conditions on attribute values [4]. For multimedia content, vertical fragmentation is difficult to imagine, except perhaps for data organization in secondary storage (such as mirrored disks). For instance, in a video object, a frame or a scene (a series of frames with similar structure and/or subject) may be considered a distribution unit. A more suitable approach is horizontal fragmentation, where collections of video objects or groups of images may be considered as distributable units. For many application domains, such larger-grain distributable units will be clearly more appropriate. For example, in a medical imaging application, there may be a large number of X-ray objects. These may be grouped into units by examination date, examination type, disease type, patient type, etc., instead of considering each indi vidual image separately as a candidate for distribution.

The second phase, allocation, involves placing the units, and possibly replicating them, at the platforms of interest, such as processors at dispersed locations [13]. Most research on data distribution has also addressed allocation. Some studies have presented tightly coupled procedures for fragmentation and allocation [21], whereas others, with semantic fragmentation approaches, have opted to decouple the two [11, 18, 25]. Some efforts have also focused clearly on allocation assuming avail ability of reasonable fragments [4]. To date, we are aware of only one research effort that has attempted to address multimedia object distribution [26]. It, however, does not consider the unique aspects of multimedia objects we have outlined above.

Another consideration for the allocation problem is the recognition of multiple cri teria. Allocation models have been proposed for file allocation [20] and data distribu tion [15, 16] that formulate multiple objectives. No such approach, however, has been proposed for multimedia content. The lone research effort for multimedia content distribution [26] considers cost, but ignores the important dimension of quality of service (QoS). A reasonable solution approach would be one that considers these multiple criteria. The resulting problem then, is not only NP-complete [6], but becomes even more complex, as it requires judgment from the designer to decide what represents an acceptable solution [20, 32]. Another level of complexity can be introduced if we also consider dynamic reallocation of objects in response to changing demand patterns. Design of a dynamic strategy, however, requires consideration of issues such as network congestion [2, p. 22]. Currently, these are beyond the scope of this project. This paper addresses the first step in the distribution process—that is, an initial static distribution of multimedia content that properly takes into account the multiple criteria of cost and quality of service.

## A Multimedia Object Distribution Model

DEVELOPING THE MULTIMEDIA OBJECT DISTRIBUTION MODEL requires (a) modeling of the underlying hardware infrastructure, such as networks and processors, (b) consideration of a number of unique properties of multimedia data, and (c) recognition of the operational characteristics of the application using the multimedia content.

## Modeling the Networked Infrastructure

Our distribution model focuses on the allocation of multimedia content in corporate intranets, which are typically tightly coupled, and characterized by (clusters of) pro cessors connected by high-speed, high-bandwidth communication links. The access points on the intranet, which may at different points play the role of a server or a client, are represented in our model as workgroups. These workgroups represent the platforms, that is, allocation choices, specified as $\nu , w \in W .$

The underlying configuration is modeled in terms of the key dimensions of network link bandwidth and storage capacity at each workgroup. Having a link of sufficient bandwidth is necessary to ensure that a specific distribution will be feasible. Fo example, one stream of video, even when compressed, can result in several megabit per second (Mbps). The storage requirements can be equally demanding. The workgroups must also possess adequate storage capacity for large object sizes. These are specified as communication bandwidth between workgroups v and w, that is, $\mathbf { b a n d w i d t h } _ { \nu w }$ , and storage capacity at workgroup w, or s $\mathbf { 0 r a g } \mathbf { e } _ { w }$

To account for the stringent availability requirements of multimedia systems, it is also necessary to capture the reliability and failure rate of the hardware components. We use historic data about uptime of links between workgroups and uptime of each workgroup for this purpose. The uptime of a workgroup is defined as the inverse of the occurrence rate of failures. To satisfy a request-response interaction, both workgroups must be available and the link between the two must also be functioning properly. For instance, data loss due to signal corruption from electrical noise may be blamed on the link, but data loss due to buffer overflow at the workgroups may be blamed on the either/both workgroup(s). Statistical measures for these notions of uptime of workgroup and link can be deduced from the probability of failure over a given time interval [17, 29]. These are specified as uptime of the link between workgroups w and v, that is, relia $\mathbf { \Delta } \mathbf { b i l i t y } _ { v w }$ , and uptime of a workgroup, say, w, or uptim $\mathbf { e } _ { w }$

We also attribute the availability of different special processing requirements to the workgroups. For example, the availability of a specialized server may be necessary to store videos, and it may be available only at certain workgroups. As another example, the ability to catalog and store a number of X-ray images may be available only a certain locations in a medical facility. If a data type requires this capability, it is nec essary to ensure that it is allocated only to workgroups where this capability is avail able. These are specified as specialized hardware capabilities, $c \in C$ , and availabilit of capability c at workgroup w {0,1} is denoted as capabil $\mathbf { t y } _ { c w }$

## Characteristics of Multimedia Content

A number of characteristics of multimedia content affect the formulation of our model. First, we distinguish between different types of multimedia content, since different types can require different presentation policies. An important property that can be ascribed to different data types is the presence or absence of temporal nature. We can identify six generic data types: text, graphics, images, audio, video, and holograms. Of these, the first three are static, whereas the last three represent temporal data. For the purpose of the model, though, we allow the designer to define application-spe cific object types, which may include magnetic resonance images (MRIs), X-ray im ages, patient consultation sessions, various charts for monitoring patient responses, etc. These are specified as multimedia data types, $\pmb { t } \in \pmb { T }$ , and temporal nature of mul timedia content {0,1}, is indicated as temporal .

Since the volume of multimedia data is generally very large, data compression schemes are common in many multimedia applications. They can sometimes require some sacrifice in resolution. Resolution refers to the accuracy with which the original content can be reproduced, that is, it determines how much detail can be resolved. For example, some medical applications require at least $2 \mathrm { K } \times 2 \mathrm { K } \times 1 6$ bits resolution fo diagnostic purposes [30]. On the other hand, some training and consultation activities may require lower resolution, and an even lower resolution may suffice for certain administrative functions. It is possible, therefore, to allocate the same object at differ ent workgroups, at different resolutions, increasing availability and reliability. We specify these as resolution levels, k, r Î K.

Another significant parameter is the minimum amount of data that must be trans ferred for an object of a given type to begin its display or playback. This parameter has a direct bearing on response time, which can be measured in a variety of ways. For example, we may measure the time elapsed between the object request time and the arrival time of (a) the first data packet, (b) the last data packet, or (c) a certain minimum amount of data needed to start displaying the content. Unlike text only data, it can take a considerable amount of time to transfer complete multimedia content for large objects. Further, for temporal multimedia data, the last packet may not be necessary to begin playback of the content. The first two options, therefore, are not appropriate for multimedia content. The final option correctly accounts for the fact that for most multimedia data, the buffering time required to begin display is nontrivial and cannot be ignored. We capture this as a predetermined buffer—based on the data type—that must be transferred to the requesting workgroup for objects to start their display or playback. The predetermined amount is specified as a raw number (not a percentage of size) for each data type. We also allow it to be specific for different resolution levels of a data type, and specify it as minTransfer<sub>tk</sub>.

Multimedia content also has special networking requirements because the volumes of images and video messages can be quite large. Text transfer is the least demanding of the various transfer types. The manner of transfer, whether all at once or in chunks, is usually not very crucial, and the volumes are relatively much smaller. A simpler, and potentially lower-cost, network service can provide adequate perfor mance for text transfers. Data transfer for images is considerably more demanding due to the high volume of data. A page of text may be only 2.5 Kbytes (KB). A black and white image of a page may, however, range from 60 KB to 220 KB even after compres sion, and a grayscale or color image can be much larger, of the order of 1 Mbyte (MB) or more [24]. The requirements for audio and video clips are more intensive than for imaging because of the temporal dimension. Unlike an image display, a momentary pause in an audio or video clip is very disturbing. Obviously, a 10-Megabits-persecond (Mbps) network has to be adapted very carefully to stream data at the rate it is being viewed so that it can keep up with the display. While this is feasible with prerecorded and heavily indexed information, dynamic information may not be set up for easy streaming. A higher class of service may be necessary to provide accept able performance [2, p. 23]. Therefore, if the object of interest is to be accessed from a remote workgroup, it is necessary to ensure that sufficient bandwidth is available between the two workgroups. As indicated above, this can be widely different for different data types. If the minimum bandwidth is not available, the response time can be unacceptable or even impossible, particularly for audio or video data. We capture the minimum bandwidth for each data type as reqdBandwidth .

Finally, certain data types may require specialized servers, such as a video server and the hardware or software necessary for the display and manipulation of the data. This is specified in our model as requirement of capability c for data type t {0,1}, that is, reqdCapability<sub>ct</sub>.

## Operational Characteristics of the Multimedia Application

Since the number of instances of each multimedia type can be very large, we treat groups of these items as distributable units. Examples of these include a set of images from the previous month for a medical exam, a group of video objects for consultation sessions with patients in a certain location, etc. The distributable units do not represent units of access or manipulation. Typically, the units of access to manipulation are individual objects, that is, part of a distributable unit. A distributable unit can contain objects of only one type. Defining the distributable unit as a collection of objects (instead of a single object) keeps the problem tractable and allows for more pragmatic units such as “MRI films during the first week of June 1999.” Further, the restriction of only one type of objects in a distributable unit ensures appropriate specification of constraints. It is possible to extend traditional research in relational data fragmentation [4] or class fragmentation [22] to derive such horizontal fragments. The object relational data models and databases [27] provide structuring mechanisms for large quantities of such data. They represent the distributable units in our model, specified as $i , j \in J .$ . The distributable unit is mapped to data types {0,1} and specified as of $\operatorname { T y p e } _ { i t } .$

The primary determinant of the allocation decision is access frequencies. Unlike traditional data, multimedia data is rarely updated. Instead, the major operations performed on multimedia data include creation of new objects and access of existing objects. The access frequency is, thus, the key factor that decides the appropriate distribution. It is also possible that an object may be created at one workgroup, but may be stored at another. The notations below capture this. The first, size, indicates the size of a distributable unit i with resolution k, si $\mathbf { \Delta } \mathbf { \Psi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi } \mathbf { \Xi \Xi } \mathbf { \Xi } \mathbf { \Xi \Xi } \mathbf { \Xi } \mathbf \mathbf { \Xi \Xi } \mathbf { \Xi \Xi } \mathbf \mathbf { \Xi \Xi } \mathbf { \Xi \Xi } \mathbf \mathbf { \Xi \Xi } \mathbf \mathbf { \Xi \Xi } \mathbf \mathbf { \Xi \Xi } \mathbf \mathbf \Xi \Xi \mathbf { \Xi \Xi } \mathbf \mathbf \Xi \Xi \mathbf \Xi \Xi \mathbf \Xi \Xi \mathbf \Xi \mathbf \Xi \mathbf \Xi \Xi \mathbf \Xi \Xi \mathbf \Xi \mathbf \Xi \Xi \mathbf \Xi \Xi \mathbf \Xi \Xi \mathbf \Xi \mathbf \Xi \mathbf \Xi \Xi \mathbf \Xi \mathbf \Xi \mathbf \Xi \mathbf \Xi \mathbf \Xi \Xi \mathbf \Xi \mathbf \Xi \mathbf \Xi \mathbf \Xi \mathbf \Xi \mathbf \Xi \mathbf \Xi \mathbf \mathbf \Xi \mathbf \Xi \mathbf \Xi \mathbf \mathbf \Xi \mathbf \Xi \mathbf \mathbf \mathbf \Xi \mathbf \Xi \mathbf \Xi \mathbf \mathbf \Xi \mathbf \mathbf \mathbf \Xi \mathbf \Xi \mathbf \mathbf \mathbf \Xi \mathbf \Xi \mathbf \mathbf \mathbf \mathbf \Xi \mathbf \mathbf \mathbf \Xi \mathbf \mathbf \mathbf \mathbf \mathbf \Xi \mathbf \mathbf \mathbf \mathbf \mathbf \Xi \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf \mathbf $ . The second is a binary variable that indicates that an object is created at a workgroup w, which will be added to the distributable unit i, $\mathbf { c r e a t e } _ { i w }$ . Finally, the third indicates the frequency with which objects from distributable unit i (at resolution k) are required at workgroup w, $\mathbf { f r e q } _ { i k w } .$

Finally, the decision variable is the placement of units at platforms, defined as the allocation {0, 1} of a distributable unit i, at a certain level of resolution $k ,$ to a workgroup w—that is, $\mathbf { X } _ { i k w }$ . Figure 1 shows the formulation decisions and outlines many key variables discussed above.

## Distribution Criteria

BASED ON THE PARAMETERS AND NOTATIONS DEVELOPED SO FAR, we formulate a multimedia distribution model. The model consists of multiple criteria for costs and for different aspects of quality of service. Since the distributable units $i , j \in J$ repre sent groups of multimedia objects, whereas typically an access is performed on a single multimedia object, we need to account for a complex access protocol. To consider the possibility that the required object may be found in a distributable unit with varying probability, we explicitly model this chance. In the absence of semantic information, we exploit the number of objects in each unit, relative to the total, as an estimate of this probability. Consider, for example, 1000 objects of multimedia type t (ignoring resolution levels), for which four distributable units (i1 through i4) have been identified. The first unit, i1, contains 500 objects, the second, i2, contains 300, the third, i3, also contains 300, and the fourth, i4, contains 200 objects. The level of replication, thus, is 1.3, since a total of 1,300 objects are stored. The object being searched for may be object O1. Then the probability of finding O1 in each distributable unit (in the absence of semantic information), is: i1 (50%), i2 (30%), i3 (30%), and i4 (20%). We capture this as the chance that the required specific object is avail able in distributable unit i at workgroup w with any resolution k greater than or equal to the required resolution r. This is specified as the probability that a required specific object is part of a distributable unit i stored at workgroup w with resolution k greater than or equal to the needed resolution r—that is, chance<sub>ikwr</sub>.

![](/api/attachments/V3ZBN4AW/fulltext/images/68c3c7b23309f683b355b4c215f735776474989ae959bd275c38f3c560f07f32.jpg)  
Figure 1. Key Formulations

The required object, thus, may not be available at a given distributable unit. It is then necessary to search for the object at other workgroups before accessing it. Fur ther, the required object may be found in multiple distributable units, at different workgroups, at the required resolution k or higher $( \mathrm { c h a n c e } _ { i k w r } )$ . Then a decision must be made to access the object from one of the workgroups. A successful access is performed only if the workgroup from which the access is to be made is up $( \mathrm { u p t i m e } _ { w } )$ and the link between the requesting workgroup and the serving workgroup is also up $( \mathrm { r e l i a b i l i t y } _ { \nu w } )$ . The materialization of the access is captured in the notation accessed $\romannumeral 1$

Figure 2 shows variables that contribute to this materialization of the access operation. The variable thus captures the routing decision to access a required object from a remote workgroup if it is not locally available. Operationally, based on the simulated values of uptime, reliability, and chance, the value of the accessed variable is determined for difference access instances. Using the above, we formulate expres

![](/api/attachments/V3ZBN4AW/fulltext/images/cb1ff869a379cdb8738c355525e29a00b81e7a63a2eb06c7b4f98ea2b161d762.jpg)  
Figure 2. Access Materialization  
sions for the two optimization dimensions of quality of service (QoS) and cost. A number of specific criteria can be formulated for both dimensions. For this model, we consider two key criteria for QoS—availability and response time—and two elements of cost—storage and communication.

## Measuring Quality of Service (QoS)

Several aspects of quality of service can be considered for a distribution model. Here, we consider two that are considered to be key: availability and response time [29].

## Availability

Availability, a measure of service delivery, is estimated by the probability that the required object is available, as needed, during a given time interval. It is the fraction of times that the system works as intended by the user [8]. For multimedia objects, it translates to availability on demand [17]. We measure it by the uptime of workgroups involved in the request-response operation, and the uptime of links between these workgroups—weighted by the probability that a specific object is available at a certain workgroup. When the workgroup requesting an object and the workgroup storing the object are same $( \mathbf { X } _ { i k w } = 1 )$ , reliability depends solely on the uptime of the workgroup. On the other hand, when the requested object is stored at a workgroup different from the workgroup requesting the object $( { \bf { X } } _ { i k w } = 0$ and $\mathbf { X } _ { i k \nu } = \ o { 1 } { 2 }$ ), reliability depends on the uptime of the workgroups and links involved, and the probability of the requested object being stored at those different workgroups.

![](/api/attachments/V3ZBN4AW/fulltext/images/9eae0e9f556c2ac10b205a6823f9719e181b917be89377024811ff5429cec4b4.jpg)

The formulation computes a stochastic, simulated probability of Availability since the variables uptime, reliability, and chance all represent probabilities of occurrences of different events.

## Response Time

Response time measures the time required for delivery of the minimum amount of data that must be transferred (buffered) to start presentation of multimedia content. This is inversely proportional to the size of bandwidth between related workgroups.

$$
\begin{array}{r l} \text {Response Time} = & \\ \sum_ {\mathrm{i} \notin \mathrm{k} \in \mathrm{K}} \sum_ {\mathrm{t} \in \mathrm{T}} \left\{\left(\text {accessed} _ {\mathrm{ikvw}}\right) * \left(\min \text {Transfer} _ {\mathrm{kt}}\right) * \left(\text {ofType} _ {\mathrm{it}}\right) \right\} / \text {bandwidth} _ {\mathrm{vw}} \\ & \forall \quad \mathrm{v}, \mathrm{w} \in \mathrm{W} \end{array}
$$

A third criterion—real-time delivery and synchronization—may also be formulated, since multiple media streams sometimes need to be synchronized. Such synchronization requires consideration of a number of dynamic parameters—such as traffic fluctuations— that cannot be statically modeled. Instead, we partially incorporate this objective into our model by formulating it as a constraint for minimum bandwidth. For the two criteria of quality of service we model, replication can have considerable impact. Since most multimedia data is accessed and rarely updated, increasing the replication can have desirable consequences, as shown in Figure 3. However, increasing replication can also lead to increased hardware and administration costs. We consider these next.

## Measuring Costs

Cost is an important criterion, since multimedia data can occupy large storage space and may entail considerable communication cost. Though per-unit storage costs continue to fall rapidly, the storage cost for a multimedia system can be significant, with reported volumes as high as 5 gigabytes per day (GB/day) for some applications [30]. At this scale, redundancy across workgroups can be an expensive proposition. Similarly, though per-unit communication cost continues to fall rapidly, the large amounts of data transfer required to effect multimedia delivery can be considerably expensive. In both cases, though the incremental hardware costs are rapidly falling, the infrastructure and administration costs continue to contribute significantly to the total cost. The costs considered here are the sum of one-period storage costs and data communication costs. This paper limits itself to a one-period static model for reasons of simplicity (similar to [16]). Using appropriate assumptions (similar to [22]), it is possible to include multiperiod costs without requiring any changes to our model.

Unlike the Quality of Service criteria, increasing replication has different consequences for storage and communication costs. Figure 4 shows these consequences.

![](/api/attachments/V3ZBN4AW/fulltext/images/3e993e3b31a649166a9998d139b8426aaea5d47657b24609bfcea999e2ddb3d6.jpg)  
Figure 3. Quality of Service

![](/api/attachments/V3ZBN4AW/fulltext/images/1ab9ead8d211a50a48c9e81e30254148ae5436d02356b7cbe9e14eac64ea1a2b.jpg)

Figure 4. Costs

Storage Cost

The Storage Cost is the sum of costs incurred by the storage and maintenance of data at each workgroup. It is proportional to object size, given storage cost per unit size.

$$
\text { Storage   Cost } = \sum_ {w \in W} \sum_ {i \in J k \in K} \text { size } _ {i k} * X _ {i k w} * (\text { storage   cos   t   per   unit })
$$

## Communication Cost

The Communication Cost contains two elements: (1) access cost, and (2) creation cost. The access cost accrues when the object at the required resolution is not available at the current workgroup and must be accessed from a remote workgroup. It may also accrue when an object is required at the current workgroup at a resolution higher than the one available at that workgroup. The access cost is affected by one additional factor—access frequencies of each object at each workgroup. The creation cost rep resents the possibility that the object created at one workgroup is stored at another workgroup. Both costs are also proportional to object size, given communication cost per unit size. Since the former is likely to be more frequent, the total communication cost largely depends on the access cost.

## =Communication Cost

$$
\sum_ {i \in J} \sum_ {k \in K} \sum_ {w \in W} \left\{f r e q _ {i k w} * s i z e _ {i k} * (c o m m u n i c a t i o n \text { cost   per   unit }) * a c c e s s e d _ {i k v w} + \right.
$$

$$
\left. \text {size} _ {\mathrm{ik}} * (\text {communication cost per unit}) * \left(X _ {\mathrm{ikw}} * \text {create} _ {\mathrm{iv}}\right) \right\} \forall \quad \mathrm{v} \in \mathrm{W}
$$

## Technological Constraints

A number of technological constraints are necessary to complete the formulation. First, we ensure that at least one copy of each distributable unit—at its highest re quired resolution—is allocated. Second, we ensure that a distributable unit can be stored at only one resolution at a workgroup. Third, the storage capacity of each workgroup must be adequate to handle the distributable units allocated to it. Fourth, the required object must be accessed at a resolution that is equal to or higher than the required resolution. Fifth, the bandwidth between workgroups engaged in a requestresponse operation must be sufficient. Finally, the required hardware and software must be available at the workgroup.

Constraint 1: At least one copy of each distributable unit at the highest resolution must be allocated. In other words, every distributable unit must be stored at least once at the highest resolution.

$$
\sum_ {w \in W} X _ {i k w} \geq 1 \quad \forall \quad i \in J, k \geq r, \forall \quad r \in K
$$

Constraint 2: A distributable unit can be stored at only one resolution at a workgroup. This is a pragmatic constraint that indicates that a workgroup does not need to store a distributable unit at more than one resolution. For example, if a workgroup stores a distributable unit at high resolution, it does not need to store the same unit at a lower resolution.

$$
\sum_ {k \in K} X _ {i k w} \leq 1 \quad \forall \quad i \in J, w \in W
$$

Constraint 3: The capacity of the workgroup should be sufficient to allow storage of distributable units allocated. This constraint ensures feasible allocations.

$$
\sum_ {k \in K} \sum_ {i \in J} X _ {i k w} * \text { size } _ {i k} \leq \text { storage } _ {w} \quad \forall \quad w \in W
$$

Constraint 4: The required object can only be accessed from a workgroup where the object is available either with the required resolution (r) or at a higher resolution (k).

$$
r \leq k \quad \forall \quad w \in W \mid (\text { accessed } _ {i k v w} = 1) \land (\text { freq } _ {i r v} > 0)
$$

Constraint 5: The bandwidth utilized to access the object will be at least equal to the bandwidth required for this type of object.

$$
\text { bandwidth } _ {v w} \geq \text { reqdBandwidth } _ {t}
$$

$$
\forall w \in W \left| (\text { accessed } _ {i k v w} = 1) \land (\text { ofType } _ {i t} = 1) \land (\text { freq } _ {i r v} > 0) \right.
$$

Constraint 6: Any special hardware or software requirements must be respected when allocating any of the distributable units.

$$
\sum_ {r \in K} X _ {i r w} * \text { ofType } _ {i t} * \text { reqdCapability } _ {c t} \leq \text { capability } _ {c w}
$$

$$
\forall i \in J, w \in W, c \in C, t \in T
$$

## The Distribution Approach

THE DISTRIBUTION PROBLEM FORMULATED ABOVE presents a situation that is NPcomplete [6], is subject to multiple criteria [20], involves probabilistic formulations for some of the criteria, and involves unarticulated designer preferences. For such problems, analytical approaches to finding optimal solutions clearly fall short. Any reasonable solution approach that addresses such problems must, itself, balance two competing demands: mathematical convergence and behavioral convergence. The first refers to the need to arrive at acceptable solutions that are nearest to the ideal. The ideal solutions may not be attainable, since they are constructed by optimizing each function separately. Mathematical convergence thus represents the proximity of the obtained solution to the ideal solution for each of the criteria. The second is a result of the NP-complete nature of the problem. It refers to the need to evaluate the final solution in terms of the overall solution space. Since it is not possible to explore the complete solution space (due to the NP-complete nature of the problem), it is neces sary to provide the designer some assurance that significantly better solutions are not being overlooked. Since this cannot be asserted with certainty, behavioral convergence refers to the ability to provide a probabilistic assessment of overlooking other solutions [23]. The approach we have elected to instantiate represents a combination of fuzzy-set-based heuristics and generation of locally efficient solutions, drawing on the general method presented in Purao et al. [23].

We envision a cooperation of efforts between the human application designer and a computer-based decision aid that formalizes our approach. Figure 5 shows an overview of our approach. It consists of two phases. In the first phase, the designer sets targets to be sought by the decision aid. Using the goals and iterating through simula tions and goal adjustments, the decision aid generates locally efficient (nondominated) solutions that meet the targets {1}. In order to identify these solutions, it also gener ates a large solution sample (regardless of dominance) that allows interpretation of the solutions in the form of several measures of risk using fuzzy-set-based heuristics {2}. Using these measures, the designer iterates as often as necessary. When the designer decides that the risks associated with stopping are acceptable, the final shortlist of locally efficient solutions—along with their fuzzy evaluations—is presented to the designer, who makes the final choice {3}. During the process, the designer may iter ate through the simulation process if the number of locally efficient solutions is not sufficient (A) or by further analyzing the generated nondominated solutions by ad justing the target values (B). If the simulated sample is not considered representative or sufficient, the designer may also iterate through the entire cycle—regenerating the sample—by adjusting the simulation parameters (C). A number of statistical techniques and fuzzy-set-based results form the basis of operationalizing the approach shown in Figure 5. Purao et al. [23] specify the theoretical bases that contribute to this approach to approximately solving NP-complete multiple-criteria problems. The approach we propose represents an extension and instantiation of the framework pre sented in Purao et al. [23]. We elaborate below on the choices we have made to operationalize the approach.

![](/api/attachments/V3ZBN4AW/fulltext/images/0cd1a871c4dd83cd73266d374fbc6868af6f8671fa581dd1a701572bbb123f0d.jpg)  
Figure 5. The Decision Support Approach

## Generating Locally Efficient Solutions

To generate locally efficient solutions, we use systematic random sampling. Since a by-product of this search is also a compilation of a large pool of solutions (both dominated and nondominated), the procedure needs careful consideration of a number of important subtasks, such as sampling strategy and feasibility checking.

## Sampling Strategy

The populations of interest during the sampling are the criteria values, since they allow evaluation of the locally efficient solutions. The criteria values, however, repre sent transformations of the search space (solution vectors). We therefore sample the underlying vector space. A prerequisite for effective random sampling is the ability to select an element with uniform probability from the space under consideration [9]. No such “general” methodology exists for random sampling from standard multivariate distributions [5, p. 155], though numerous techniques are available for random sampling from univariate distributions [19]. Since each alternative is a binary vector (made up of a series of values representing $\boldsymbol { \mathrm { X } } _ { i k w } , \boldsymbol { w } \in W )$ , we treat each element in the vector as the outcome of a Bernoulli trial. Vectors comprised of Bernoulli elements can be treated as analogous to elements generated from a binomial distribution [10]. Since we are interested in generating a representative sample (i.e., covering as much of the population space as possible), we define “success” as the generation of an extreme value for a criterion. The number of successful solutions generated, then, represents a Poisson distribution. Using standard notation, a high probability of generating at least one successful solution (i.e., in the upper p percent) is given by: 1– $( ( n p ) ^ { x } e ^ { - n p } ) / { \cal O } _ { \cdot } ^ { \prime } )$ . By selecting a confidence factor, the sample size, n, can be com puted. For instance, a sample size of 300 (1,200) provides values in the top and bottom $9 0 ^ { \mathrm { t h } } \ ( 9 5 ^ { \mathrm { t h } } )$ percentile with 95% level of confidence. Selecting the sample size, then, requires choice of confidence levels and extreme value percentiles desired.

## Ensuring Feasibility

It is important to check each sampled alternative for feasibility. This is relatively easily verified—by checking each generated vector to ensure that specified problemspecific constraints are met. An important assumption here is the existence of a large number of “feasible” solutions to sample from. Studies [3] have shown that for effec tive sampling it is necessary that feasible solutions constitute at least a modest frac tion, say 1%, of the total random solutions generated—a condition quite easily met.

## Checking for Nondominance

The generated solutions are checked for nondominance to create a list of locally efficient solutions. Nondominance implies that the choice between two solutions requires designer input. For instance, consider the two solutions (say, x and y) with three criteria, say, C1 to C3. Solution x may have values 74, 92, and 83, whereas solution y may have the values 76, 90, and 80. Neither solution dominates the other fully, since each is better and worse than the other with regard to at least one crite rion. During sampling, a small number of solutions are typically found to be nondominated. As the sample size grows, the number of nondominated solutions creeps up quite slowly. This ensures that a small set of clearly viable (nondominated) solutions can be made available to the designer for consideration without wasting designer efforts on clearly inferior (dominated) solutions. Making these solutions available to the designer, however, is not sufficient. Additional help can be provided to the designer by evaluating these solutions to determine their attractiveness.

## Evaluating Solutions Using Fuzzy-Set-Based Heuristics

To interpret the solutions, we employ fuzzy-set-based measures, expanding on the suggested set of measures from Purao et al. [23].

## Interpreting the Locally Efficient Solutions

Each locally efficient solution can be interpreted using the large sample of solu tions available for comparison. This sample provides a benchmark against which each solution can be judged. Recall the problem with three criteria (C1 to C3)—say, flexibility, dependability, and performance—for which a locally efficient solution x may be available with the values 74, 92, and 83. Against the generated sample, the probability of achieving a value > 74 for the first criterion may be computed as 19% $( \mathsf { P } _ { 1 } )$ (estimated using the proportion of solutions with values greater than 74 in the generated sample). Similar probabilities for the second (>92) and third (>83) criteria may be $7 \% ( \mathrm { P } _ { 2 } )$ and $23 \% ( \mathrm { P } _ { 3 } )$ , respectively. This information can be restated in several additional ways by treating the criteria evaluation functions as generators of elements in fuzzy sets [31]. For example, the lower bound for finding a solution that dominates this solution can be computed—based on an assumption of independence— as just 0.31% – P(Dominating):Lower $\mathrm { B o u n d = \Pi \Pi _ { i } ^ { \phantom { + } } ) }$ , where $\mathrm { { P _ { i } } }$ represents the prob ability that the value for the $\mathrm { i } ^ { \mathrm { t h } }$ criterion will be exceeded. The upper bound can be estimated as $7 \% \mathrm { ~ - ~ } \mathrm { P ( D o m i n a t i n g ) { : } ~ } \mathrm { U }$ Upper $\mathrm { \mathbf { B o u n d } = \mathbf { M i n } [ P _ { i } ] }$ , based on the inverse assumption of a complete overlap. Similar $| { \mathrm { y } } ,$ the upper bound on the probability of finding another efficient solution with respect to the current solution can be simply stated as 23% – P(Nondominated):Upper $\mathbf { B o u n d = M a x [ P _ { i } ] }$ . The lower bound can be estimated using a combination of probabilities based on different scenarios—that is, with each combination of criteria exceeding their value and the others not exceeding, in turn. The summary of these membership functions is shown in Table 1.

These probabilities are used to assess the risks associated with stopping the search. For example, since P(Dominating) indicates the probability of finding a solution that is better on all criteria than the current solution, a low value indicates that not many unexplored solutions would dominate the current solution and the current solution is a good candidate. It can also be interpreted to mean that further simulation is not needed and that the designer may stop the process. A low value for P(Nondominating) indicates that the chances of finding another nondominated solution in the unexplored solutions are low. The designer can use this information to filter the solutions to arrive at a manageable number of solutions quickly. Since the criteria may be nonindependent, specific information regarding joint or conditional probability distributions is diffi cult to construct at different value ranges. The estimations above can therefore provide useful bounds for assessing the relative worth of each solution. In the absence of well-behaved criteria that lend themselves to algebraic manipulation of the n-dimen sional search space, these fuzzy-set-based functions are especially useful. Due to their simplicity, they can also entail negligible computational burden—that is, extremely quick response time.

## Iteration

Using the interpretations as above, the designer may iterate through either of the cycles indicated in Figure 5. For example, based on the evaluations, the designer may adjust the tolerances to locate solutions that meet a slightly different set of goal (cycle B), or may choose to simulate an entirely fresh set of simulated results (cycle C or A).

Table 1. Solution Evaluation Functions Using Fuzzy Sets

<table><tr><td colspan="2">P (Finding a solution that dominates the current solution)</td><td colspan="2">P (Finding a solution that is nondominated with respect to the current solution)</td></tr><tr><td>Lower Bound</td><td>Upper Bound</td><td>Lower Bound</td><td>Upper Bound</td></tr><tr><td> $\Pi_{i\text{el}} P_i$ </td><td> $\min_{i\text{el}} P_i$ </td><td>Let  $\alpha = 1$  $\forall i \in I$ If  $P_i > 0.5 : \alpha^* = P_i$ Else:  $\alpha^* = (1 - P_i)$ </td><td> $\max_{i\text{el}} P_i$ </td></tr></table>

Finally, the shortlist retained is presented to the designer, along with the risks associated with each solution. At this stage the designer can select the solution he or she most prefers among nondominated solutions. The efficient solution “most preferred” by the designer is the best compromise solution. Implicit in the definition is the fact that it is the solution that maximizes the designer’s unarticulated preference function

## Implementation and Results

THE MULTIMEDIA OBJECT DISTRIBUTION MODEL and the simulation-based decisionsupport approach described above were developed in Java using Symantec Café™ and implemented on a Pentium class personal computer. The user interface consisted of a series of web pages designed to facilitate easy interaction. The prototype, however, was focused more on implementing the underlying distribution criteria, the simulation process, and demonstration of different steps in the distribution procedure. The prototype went through several tests with different examples, constructed in a manner similar to that used by Lee and Sheng [20]. We demonstrate below an illustrative example and a sample session with the results.

## An Illustrative Example

We demonstrate our model and distribution approach with a test application consisting of six workgroups in a medical facility, connected with six links. Figure 6 shows the infrastructure. The circles represent workgroups, such as radiology, outpatient, billing, etc.; the lines represent links; and the numbers next to each workgroup and link indicate the workgroup uptime, link reliability, and link bandwidth. Additional characteristics not shown include storage capacity, special characteristics, etc., as for mulated earlier.

We consider five data (object) types, including MRIs, Patient Consultation Ses sions, X-ray Images, Patient Medication Records, and Patient Charts. Each object type has different object size and minimum data amount needed for real-time play

![](/api/attachments/V3ZBN4AW/fulltext/images/8055a96b1ef729ca05a13ffc3d3a301af3b14e445049946f6f4983e0c7be4410.jpg)  
Figure 6. A Test Application  
back. The possible resolutions of each object are high, medium, and low. Table 2 shows the minimum transfer times for each data type at three resolution levels. Fol lowing Lee and Sheng [20] and Jain [15], we have devised a table of frequencies that acts as the basis for exercising our model. The probability that a required object at a certain resolution is available at a certain workgroup is computed as the proportion of the number of objects in the distributable units to the total.

## A Sample Session

Our sample session begins with the designer entering target values for the four criteria: storage costs, communication costs, response time, and availability. They are interpreted as: at most \$50,000 for storage and communication costs, respectively, at most 1.0 second response time and at least 98% availability. Figure 7 shows the user interface the designer uses to enter the target values and to invoke the simulation process [Submit], which generates 17,500 solutions by systematically varying the replication levels. The sample ensures that at least one extreme solution >99.9% is obtained, with >99% confidence. For our session, it also results in generation of 168 locally efficient solutions.

Since the number of locally efficient solutions (168) is still quite large to be considered individually, the designer adjusts the target values for storage and communication costs to \$30,000 each and the value for response time to 0.4 seconds. The target for availability is not changed, since it is considered to be sufficiently strict. This filters the solutions to 95 nondominated solutions, which indicates that further refin ing of target values is possible. The next tightening is done with \$20,000 for communication costs and results in 32 nondominated solutions. Finally, another adjustment is the target value for response time to 0.18 seconds, resulting in the 21 locally effi cient solutions shown in Table 3.

To assist the designer in evaluating the solutions in terms of the relative attractiveness, each solution is interpreted using the probability computations discussed ear lier. These are expressed in Table 3 as Pr(Dominating) and Pr(Non-Dom). The first represents the probability of finding a solution that dominates that solution, whereas the second represents the probability of finding a solution that is a nondominated solution with respect to that solution. For both, the lower and upper columns repre sent the lower and upper bounds, respectively.

Table 2. Minimum Transfer Times for Each Object Type

<table><tr><td>Object Type</td><td colspan="3">Type 1</td><td colspan="3">Type 2</td><td colspan="3">Type 3</td><td colspan="3">Type 4</td><td colspan="3">Type 5</td></tr><tr><td>Resolution</td><td>Low</td><td>Mid</td><td>High</td><td>Low</td><td>Mid</td><td>High</td><td>Low</td><td>Mid</td><td>High</td><td>Low</td><td>Mid</td><td>High</td><td>Low</td><td>Mid</td><td>High</td></tr><tr><td> $minTransfer_{tk} (KB)$ </td><td>1</td><td>1</td><td>1</td><td>5</td><td>5</td><td>10</td><td>5</td><td>5</td><td>10</td><td>5</td><td>5</td><td>10</td><td>5</td><td>10</td><td>15</td></tr></table>

![](/api/attachments/V3ZBN4AW/fulltext/images/c6a78d7461788b2457d47311d3dab9e80ade0f27dc6a41ad7afb35d2ca4c8cb6.jpg)  
Figure 7. Entering Targets

Figure 8 shows the third solution (sample #778) in the pool of 21 solutions and the corresponding probabilities. These probabilities give the designer another opportunity to further filter the solutions. For example, the designer may decide to delete any solutions if there is a high probability of finding other solutions that dominate that solution or other nondominated solutions. It is possible to present this information in a graphical format to further aid the decision process. However, since the purpose of this project was to establish proof of concept, the above user interface was considered sufficient.

The designer reasons that since the upper limit of Pr(Non-Dom) is much higher (42.9% to 95.2%) compared to the upper limit of Pr(Dominating) (0% to 28.6%), the primary concern is Pr(Non-Dom). The designer therefore discards solutions where the upper limit of Pr(Non-Dom) exceeds 70%. This reduces the pool to the seven solutions shown in Table 4. From these solutions and using the probabilities, the designer may then select the final solution. The designer selects solution 12 (Sample 4548) as the final solution. It has a probability of no more than 19.1% (lower limit 0.9%) of finding a solution that may dominate this solution (see Table 3).

However, it is possible that the designer may continue the decision process by explor ing other possibilities. For example, the designer may revert to the set of 168 locally efficient solutions (Table 3) and filter it again by changing target values. If the response time is another important criterion, the designer may set the target values as storage costs \$40,000, communication costs \$20,000, response time 0.1 seconds, and availability 98%, yielding 57 solutions. A further adjustment of target values to storage cost \$35,000, communication costs \$25,000, response time 0.08 seconds, and availabilit

Table 3. Initial Solution Pool

<table><tr><td colspan="10">Filtered from a set of 168 solutions by specifying target values</td></tr><tr><td rowspan="2"></td><td>Storage Cost:</td><td>30,000</td><td>Response Time:</td><td>0.18</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Communication Cost:</td><td>20,000</td><td>Availability:</td><td>0.98</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"></td><td rowspan="2">Sample Number</td><td rowspan="2">Storage Costs</td><td rowspan="2">Comm Costs</td><td rowspan="2">Resp Time</td><td rowspan="2">Availability</td><td colspan="2">Pr(Dominating)</td><td colspan="2">Pr(Non-Dom)</td></tr><tr><td>Lower</td><td>Upper</td><td>Lower</td><td>Upper</td></tr><tr><td>1</td><td>673</td><td>30000</td><td>10200</td><td>0.0875</td><td>0.99989</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>81.0%</td></tr><tr><td>2</td><td>706</td><td>30000</td><td>18700</td><td>0.1583</td><td>0.99994</td><td>0.2</td><td>4.8</td><td>0.0</td><td>90.5</td></tr><tr><td>3</td><td>778</td><td>30000</td><td>15500</td><td>0.1500</td><td>0.99992</td><td>2.0</td><td>9.5</td><td>0.1</td><td>81.0</td></tr><tr><td>4</td><td>796</td><td>30000</td><td>11500</td><td>0.1792</td><td>0.99994</td><td>0.2</td><td>4.8</td><td>0.0</td><td>95.2</td></tr><tr><td>5</td><td>1193</td><td>29784</td><td>12869</td><td>0.0993</td><td>0.99968</td><td>0.1</td><td>4.8</td><td>0.0</td><td>71.4</td></tr><tr><td>6</td><td>4052</td><td>26163</td><td>18648</td><td>0.1610</td><td>0.99812</td><td>0.0</td><td>0.0</td><td>0.0</td><td>90.5</td></tr><tr><td>7</td><td>4359</td><td>28626</td><td>17286</td><td>0.1142</td><td>0.99926</td><td>1.6</td><td>14.3</td><td>1.1</td><td>57.1</td></tr><tr><td>8</td><td>4368</td><td>29800</td><td>12525</td><td>0.1120</td><td>0.99945</td><td>0.2</td><td>9.5</td><td>0.1</td><td>76.2</td></tr><tr><td>9</td><td>4370</td><td>27911</td><td>17980</td><td>0.1393</td><td>0.99897</td><td>6.3</td><td>19.1</td><td>0.5</td><td>76.2</td></tr><tr><td>10</td><td>4403</td><td>28252</td><td>14609</td><td>0.1288</td><td>0.99926</td><td>1.5</td><td>23.8</td><td>1.1</td><td>57.1</td></tr><tr><td>11</td><td>4502</td><td>28252</td><td>17143</td><td>0.1293</td><td>0.99910</td><td>4.0</td><td>28.6</td><td>2.2</td><td>61.9</td></tr><tr><td>12</td><td>4548</td><td>28626</td><td>13010</td><td>0.1262</td><td>0.99936</td><td>0.9</td><td>19.1</td><td>0.9</td><td>42.9</td></tr><tr><td>13</td><td>5459</td><td>29176</td><td>15998</td><td>0.1175</td><td>0.99906</td><td>2.3</td><td>19.1</td><td>1.2</td><td>66.7</td></tr><tr><td>14</td><td>8870</td><td>29501</td><td>16221</td><td>0.1275</td><td>0.99946</td><td>2.3</td><td>28.6</td><td>1.8</td><td>57.1</td></tr><tr><td>15</td><td>10379</td><td>29220</td><td>15243</td><td>0.1336</td><td>0.99941</td><td>2.7</td><td>28.6</td><td>2.5</td><td>52.4</td></tr><tr><td>16</td><td>12710</td><td>29729</td><td>17475</td><td>0.1511</td><td>0.99950</td><td>8.0</td><td>23.8</td><td>0.6</td><td>81.0</td></tr><tr><td>17</td><td>13646</td><td>29729</td><td>17696</td><td>0.1259</td><td>0.99928</td><td>5.0</td><td>23.8</td><td>1.2</td><td>71.4</td></tr><tr><td>18</td><td>14150</td><td>27474</td><td>19698</td><td>0.1472</td><td>0.99806</td><td>2.9</td><td>4.8</td><td>0.0</td><td>95.2</td></tr><tr><td>19</td><td>14904</td><td>27794</td><td>16843</td><td>0.1365</td><td>0.99861</td><td>3.1</td><td>14.3</td><td>0.5</td><td>85.7</td></tr><tr><td>20</td><td>16760</td><td>28199</td><td>17335</td><td>0.1407</td><td>0.99903</td><td>6.5</td><td>23.8</td><td>1.0</td><td>71.4</td></tr><tr><td>21</td><td>16772</td><td>27740</td><td>18460</td><td>0.1475</td><td>0.99885</td><td>4.5</td><td>9.5</td><td>0.1</td><td>81.0</td></tr></table>

![](/api/attachments/V3ZBN4AW/fulltext/images/3ee5b2e25a13cfebdf23c6637569d434db78a704c3ffb42f0c5b8cb379e2839b.jpg)  
Figure 8. Evaluating Solutions

Table 4. Filtered Solution Pool 1

<table><tr><td colspan="6">Filtered from the Initial Solution Pool (Table 3)Upper Limit of Pr(Non-Dom) no more than 70%</td></tr><tr><td>RowNumberfrom Table 3</td><td>SampleNumber</td><td>StorageCosts</td><td>CommCosts</td><td>RespTime</td><td>Availability</td></tr><tr><td>7</td><td>4359</td><td>28626</td><td>17286</td><td>0.1142</td><td>0.99926</td></tr><tr><td>10</td><td>4403</td><td>28252</td><td>14609</td><td>0.1288</td><td>0.99926</td></tr><tr><td>11</td><td>4502</td><td>28252</td><td>17143</td><td>0.1293</td><td>0.99910</td></tr><tr><td>12</td><td>4548</td><td>28626</td><td>13010</td><td>0.1262</td><td>0.99936</td></tr><tr><td>13</td><td>5459</td><td>29176</td><td>15998</td><td>0.1175</td><td>0.99906</td></tr><tr><td>14</td><td>8870</td><td>29501</td><td>16221</td><td>0.1275</td><td>0.99946</td></tr><tr><td>15</td><td>10379</td><td>29220</td><td>15243</td><td>0.1336</td><td>0.99941</td></tr></table>

98% results in just one solution. This solution (sample 12659) represents another possible acceptable solution in addition to sample 4548 found earlier.

Yet another attempt may be made by the designer to filter the solution pool—with stricter target values for storage and communication costs—by making concessions in response time. Setting the target values as storage costs \$20,000, communication costs \$15,000, response time 0.4 seconds, and availability 98% does not result in any solutions. Relaxing the targets to storage costs \$28,000, communication costs \$19,000, response time 0.5 seconds, and availability 98% results in the 14 solutions shown in Table 6.

With the new filtered solution pool, a new cycle can begin, which is not shown here. The examples shown here represent one of the cycles (B) shown in Figure 5. Additional examples—especially of the other two cycles (A and C) from Figure 5—can easily be envisioned. They, however, require multiple simulation sessions and are not shown here. However, even from this limited demonstration of one of the cycles, it is easy to see that with our approach different solutions can be found, depending upon different emphases for different designers.

Table 5. Filtered Solution Pool 2

<table><tr><td>Row Number from Table 3</td><td>Sample Number</td><td>Storage Costs</td><td>Comm Costs</td><td>Resp Time</td><td>Availability</td></tr><tr><td>1</td><td>12659</td><td>33382</td><td>11035</td><td>0.0756</td><td>0.99983</td></tr></table>

## Conclusion

THIS STUDY HAS DEVELOPED A MODEL for multimedia content distribution in organizational intranets. The model has been formulated as a multi-criteria problem involving four criteria: storage costs, communication costs, response time, and availability. Several important characteristics—such as the importance of content and resolution levels—make the formulation of these criteria unique and peculiar to multimedia object distribution. The simulation-based solution provides a possible approach to assist the designer in exploring the efficient solutions. Finally, evaluating them using fuzzy-set-based heuristics allows us to arrive at a reasonably accept able solution.

The model can be used in conjunction with a fragmentation scheme that identifies appropriate groups of objects, such as magnetic resonance images for current pa tients, medical resonance images for patients currently scheduled for surgical procedures, ultrasound images from previous-month exams, etc. These can be determined using a scheme similar to Shin and Irani [25] or Purao et al [22]. The solution ap proach is independent of the two-tier or multi-tier architectures and should apply equally well in both cases. We expect that it would scale rather easily for larger problems. The example we demonstrate in this paper consists of six workgroups and four distributable units made up of 1,000 objects. The computation of simulations in this case was relatively quick on a mid Pentium class PC. Since the sample size does not increase in a linear proportion, the performance should not be affected drastically as the problem size scales.

The model can be improved by removing the restriction that the distributable units must contain objects of one type only. As the research progresses, we expect to consider composite objects, which may contain different data types, as distributable units. Our trials with the fuzzy heuristics we outlined have led to the identification of some intriguing problems about result interpretation which we intend to address next. The distribution approach can be further enhanced using data visualization tools, which can position the available solutions in the search space. These remain on our future research agenda. It is also conceivable that a comprehensive approach can be developed that performs object distribution and network configuration simultaneously. Fo traditional data and file allocation, a few such approaches have been proposed [15, 20]. However, for multimedia object distribution, the implications of real-time delivery, quality of service, and network congestion can make the earlier approaches inap plicable. The network configuration problem, therefore, remains beyond the scope of this study. Our future research plans include the above extensions. Finally, our cur rent and future plans also include developing simulation-based approaches to moni tor and adjust the distribution results incorporating dynamic parameters such as network traffic into the response time and availability criteria.

Table 6. Filtered Solution Pool 3

<table><tr><td colspan="10">Filtered from a set of 168 solutions by specifying new target values</td></tr><tr><td rowspan="2"></td><td>Storage Cost:</td><td>28,000</td><td>Response Time:</td><td>0.50</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Communication Cost:</td><td>19,000</td><td>Availability:</td><td>0.98</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2"></td><td rowspan="2">Sample Number</td><td rowspan="2">Storage Costs</td><td rowspan="2">Comm Costs</td><td rowspan="2">Resp Time</td><td rowspan="2">Availability</td><td colspan="2">Pr(Dominating)</td><td colspan="2">Pr(Non-Dom)</td></tr><tr><td>Lower</td><td>Upper</td><td>Lower</td><td>Upper</td></tr><tr><td>1</td><td>68</td><td>27983</td><td>14411</td><td>0.1148</td><td>0.99973</td><td>0 %</td><td>0 %</td><td>0 %</td><td>85.7 %</td></tr><tr><td>2</td><td>175</td><td>22500</td><td>18600</td><td>0.2083</td><td>0.99931</td><td>1.7</td><td>7.1</td><td>0.2</td><td>85.7</td></tr><tr><td>3</td><td>176</td><td>27983</td><td>16422</td><td>0.1662</td><td>0.99974</td><td>0.4</td><td>7.1</td><td>0.1</td><td>85.7</td></tr><tr><td>4</td><td>177</td><td>22473</td><td>18694</td><td>0.2090</td><td>0.99927</td><td>0.0</td><td>0.0</td><td>0.0</td><td>92.9</td></tr><tr><td>5</td><td>338</td><td>27910</td><td>14563</td><td>0.1157</td><td>0.99972</td><td>0.2</td><td>7.1</td><td>0.1</td><td>64.3</td></tr><tr><td>6</td><td>356</td><td>27910</td><td>16452</td><td>0.1667</td><td>0.99974</td><td>0.9</td><td>14.3</td><td>0.5</td><td>64.3</td></tr><tr><td>7</td><td>401</td><td>27910</td><td>13559</td><td>0.1878</td><td>0.99975</td><td>0.0</td><td>0.0</td><td>0.0</td><td>64.3</td></tr><tr><td>8</td><td>491</td><td>25933</td><td>16579</td><td>0.2320</td><td>0.99904</td><td>3.8</td><td>21.4</td><td>0.5</td><td>85.7</td></tr><tr><td>9</td><td>2769</td><td>26992</td><td>18195</td><td>0.1713</td><td>0.99719</td><td>7.1</td><td>35.7</td><td>0.6</td><td>92.9</td></tr><tr><td>10</td><td>13421</td><td>27040</td><td>18208</td><td>0.1540</td><td>0.99843</td><td>3.8</td><td>21.4</td><td>1.1</td><td>71.4</td></tr><tr><td>11</td><td>13451</td><td>26586</td><td>18243</td><td>0.2221</td><td>0.99853</td><td>9.3</td><td>28.6</td><td>0.8</td><td>78.6</td></tr><tr><td>12</td><td>14727</td><td>27757</td><td>18473</td><td>0.1481</td><td>0.99828</td><td>5.0</td><td>14.3</td><td>0.3</td><td>78.6</td></tr><tr><td>13</td><td>17087</td><td>25144</td><td>18320</td><td>0.2370</td><td>0.99810</td><td>8.1</td><td>14.3</td><td>0.0</td><td>92.9</td></tr><tr><td>14</td><td>17096</td><td>27303</td><td>17978</td><td>0.1784</td><td>0.99942</td><td>3.8</td><td>35.7</td><td>3.8</td><td>50.0</td></tr></table>

Acknowledgments: We thank Ashley Bush for her comments on an earlier draft of this paper. We also thank the anonymous reviewers, whose comments have helped improve the paper considerably.

## REFERENCES

1. ACM. ACM Digital Library. Available at http://info.siglink.acm.org/dl/, 1998.

2. Andleigh, P.K. Multimedia Systems Design. Upper Saddle River, NJ: Prentice-Hall, 1996.

3. Baum, S.; Terry, W.R.; and Parekh, U.N. By Morse, J.N. (ed.), Random Sampling Approach to MCDM, Organizations: Multiple Agents with Multiple Criteria. Berlin: Springer-Verlag, 1980, pp. 10–27.

4. Ceri, S.; Navathe, S.B.; and Wiederhold, G. Distribution design of logical database schemas. IEEE Transactions on Software Engineering, SE-9, 5 (1983), 487–504

5. Dagpunar, J. Principles of Random Variate Generation. New York: Oxford Universit Press, 1988.

6. Eswaran, K.P. Placement of records in a file and file allocation in a computer network. Proceedings of IFIP Congress, Stockholm, Sweden, 5–10 August 1974. New York: North-Holland, 1974, 304–307.

7. GaTech. The Classroom 2000 Project. Available at http://c2000.gatech.edu/brothert/research/presentations/fce1/, 1998.

8. Goel, A.L. Software reliability models: Assumptions, limitations, and applicability. IEEE Transactions on Software Engineering, SE-11, 12 (1985), 1411–1423.

9. Gupta, R.S.; Smolka, A.; and Bhaskar. S. On randomization in sequential and distributed algorithms. ACM Computing Surveys, 26, 1 (March 1994), 7–86.

10. Haas, T. Personal Communication. Milwaukee, WI. 1994.

11. Hale, D. A framework for distributed database fragment allocation utilizing semantic meta-data to compose data fragments. Ph.D. dissertation, University of Wisconsin–Milwaukee. 1986.

12. Han, T. and Purao, S. Modeling for effective multimedia object distribution: Some issues and solutions. Proceedings of 27th Conference of Southeast Decision Science Institute (February 1997), 140–142.

13. Hevner, A., and Rao, A. Distributed data allocation strategies. Advances in Computers, 27 (1988), 121–155.

14. Hoffer, J.A., and Severance, D.G. The use of cluster analysis in physical database design Proceedings of the First International Conference on Very Large Data Bases (1975), 69–86.

15. Jain, H.K. A comprehensive model for the design of distributed computer systems. IEEE Transactions on Software Engineering, SE-13, 10 (October 1987), 1092–1104.

16. Jain, H.K., and Dutta, A. Distributed computer system design: a multicriteria decision making methodology. Decision Sciences, 17, 4 (Fall 1986), 437–453.

17. Kopetz, H., and Verissimo, P. Real time and dependability concepts. In S. Mullender (ed.), Distributed Systems. Reading, MA: Addison-Wesley, 1993, pp. 411–446.

18. Kulkarni, U. An integrated support system for design of distributed databases. Ph.D. dissertation, University of Wisconsin–Milwaukee, 1989.

19. Law, A., and Kelton, W. Simulation Modeling and Analysis, 2d ed. New York: McGraw-Hill, 1991.

20. Lee, H., and Sheng, O. A multiple criteria model for the allocation of data files in a distributed information system. Computers & Operations Research, 19, 1 (1992), 21–32

22. Purao, S.; Jain, H.K.; and Nazareth, D. Effective distribution of object-oriented applica tions. Communications of the ACM, 41, 8 (1998), 100–108.

23. Purao, S.; Jain, H.K.; and Nazareth, D. Supporting decision making in combinatorially explosive multicriteria situations. Decision Support Systems (2000), Forthcoming.

24. Reid, J. A Telemedicine Primer: Understanding the Issues. West Des Moines, IA: Innovative Medical Communications, 1996.

25. Shin, D., and Irani, K.B. Fragmenting relations horizontally using a knowledge-based approach. IEEE Transactions on Software Engineering, 17, 9 (September 1991), 872–883.

26. Song, S., and Jain, H.K. Distribution of multimedia objects. Proceedings of the American Conference on Information Systems (1996), 708–709.

27. Stonebraker, M. Architectural options for object-relational DBMSs. Available at http:/ www.informix.com/informix/whitepapers/wparcopt.pdf, 1997.

28. Törn, A.A. A sampling-search-clustering approach for exploring the feasible/efficient solutions of MCDM problems. Computers & Operations Research, 7, 1–2 (1980), 67–79

29. Umar, A. Distributed Computing and Client-Server Systems. Englewood Cliffs, NJ: Prentice-Hall, 1993.

30. Wright, D. Broadband: Business Services, Technologies, and Strategic Impact. Boston: Artech House, 1993.

31. Zadeh, L.A. Fuzzy probabilities. Information Processing & Management, 20, 3 (1984), 363–372.

32. Zeleny, M. Multiple Criteria Decision Making. New York: McGraw-Hill, 1982.
