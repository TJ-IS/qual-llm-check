---
otero_id: 21393
otero_key: "G2NCTNJT"
title: "A flexible information manufacturing system for the generation of tailored information products"
authors: "Peter Kaomea; Ward Page"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00067-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A flexible information manufacturing system for the generation of tailored information products

Peter Kaomea $^{*}$ , Ward Page

NCCOSC RDT & E Division 44207, 53140 Gatchell Road, Rm 421A, San Diego CA 92152-7420, USA

## Abstract

Poor data quality can severely hamper the effectiveness of organizations. During Desert Storm combat operations, it became evident that tactical decisions concerning strike and amphibious warfare rely upon timely and accurate information describing the location and condition of enemy targets. Even when there was an abundance of appropriate image data, it was shown to have limited value to the tactical user. There was no way to match available imagery and necessary processing routines to a given user's specific mission requirements. In this paper, we present a system designed to dynamically tailor information products to user needs. Using the flexible manufacturing system paradigm, we use data quality measures to optimally select available image data and dynamically configure process chains to produce an information product tailored to the user's constraints and preferences. © 1997 Elsevier Science B.V.

Keywords: Data quality; Dominant quality curve; Manufacturing possibilities; Process chain

## 1. Introduction

## 1.1. The problem

Poor data quality can severely hamper organizations' effectiveness [1-8]. Many information systems cannot optimize the quality of data provided to users, especially in diverse user communities which have dynamic needs. Such was the case with imagery used during Desert Storm combat operations [14]. Many imagery users had very different needs. Commanders typically needed current imagery of the entire battlefield to assess enemy assets and the status of friendly forces. Image analysts needed high-resolution target imagery to assess the damage done by allied bombing raids and to provide targeting information for future strike missions. Pilots needed imagery to determine threats during bombing missions and to locate mobile targets, particularly the elusive SCUD missiles.

Although the US military and national sensors collected a wealth of imagery, the usefulness of the image data for the tactical user was limited. The tactical users had no knowledge of what imagery was collected in coverage or in type. Consequently, users were unable to select the data that most closely matched their needs. Moreover, most users did not use the received image data effectively. Most users were not proficient at the complex image processing and machine vision routines necessary for them to customize available image data to their particular needs. Tactical users could be provided with higher quality information if they could dynamically select the most appropriate data (image files) and sequences of processing routines based on user context and needs.

## 1.2. The solution

This paper presents a general system structure and techniques to reconfigure a dynamic system that optimizes data for the user. As an illustration of such a dynamic system, we present the Quality-based Tactical Image Exploitation (QTIX) System, which is being developed as part of the US Navy's primary afloat command and control system. We show how the system can optimally produce target classification information, given the user's context and quality needs. Specifically, we show how user context can be represented as a multidimensional data quality curve. Users can 'tune' the curve to meet their needs for solving a specific problem. They can also use the curve to guide the selection of data units and processing routines to optimize the data product.

This application allows users to obtain highly specific imagery and target classification data without knowing about image processing, machine vision, or the location of image data in the vast databases of the Department of Defense. Although this research is presented in the context of the QTIX system, its utility is not limited to this system. It may also be used in other applications in which systems must be customized for a variety of contexts, especially when data quality needs must be traded against one another.

## 1.3. Background

The literature dealing with tradeoffs among multiple decision objectives is large [9]. However, little research has been conducted to address issues directly related to tradeoffs among data quality dimensions such as accuracy and timeliness. There are a few exceptions. Jang et al. [10] proposed a first-order data quality calculus to select dominant quality attributes when multiple quality attributes are involved. Ballou and Pazer [11] analyzed how information systems can be designed to optimize the accuracy–timeliness tradeoff through a utilization function and operations research method. Building upon the concept of dominant preference [9,10], data quality tradeoff function [9,12], and flexible manufacturing systems [13], we developed and formalized the concept of a dominant quality curve for data combined with processes, which we then applied to allow the user to dynamically interact with the QTIX system to determine the optimal information output.

## 1.4. Organization

This paper is organized in four sections: Section 2 is an overview of the QTIX system. This section provides a detailed description of the specific solution used to satisfy the tactical imagery needs of the Navy. Although specific to a particular application, the basic framework presented here may have utility for other applications. Section 3 is a mathematical treatment of the generation of production possibilities, the specification of user preferences, and the optimization of data production given user preferences. Section 4 presents conclusions.

## 2. System description

This system is analogous to a flexible manufacturing plant. The user can be compared to the consumer of the product produced by the plant and the user interface is intended to translate user needs into design specifications. In the QTIX system, the products are data units customized to meet the consumers' needs. The raw materials of the system are images collected and stored in a data warehouse. Similarly, there is a set of production tools and machinery—a database of image processing and machine vision processes. These tools transform the raw materials (images) into the information products (data units) desired by the consumers, i.e. target identifications and locations. The manufacturing possibilities generator takes into consideration all available raw materials and production tools to generate the set of all producible data units. Then, the manufacturing system selector determines exactly which data units should be produced to optimize user needs given production capabilities and limitations (see Fig. 1).

This model has proven useful because the user can see what products are available from the system at any time. The user can also view tradeoffs between qualities. Given this information, the user can efficiently specify the utility of data unit products and receive an optimal data unit product in return.

![](/api/attachments/G2NCTNJT/fulltext/images/18f7f92e5518b4cf57bf87d791c4bd686328db71c8799a1747ed74aad453c2b3.jpg)  
Fig. 1. System architecture.

Furthermore, the manufacturing process is hidden from the users, who no longer need to know or understand how the complex processing routines work, or even when to use them. In this respect, they are now more like consumers than factory operators.

## 2.1. Product marketing and design: user interface

The QTIX user interface (shown in Fig. 2) provides graphic displays, pull-down menus, pan-and-zoom functions, and slide bars. The display provides available data context, content and quality, and elicits interaction from the user to specify the relative value of data units with all possible combinations of quality values.

![](/api/attachments/G2NCTNJT/fulltext/images/2b173f137493ce7bf0703d8366fe3684bd097cc0eade46144ae341b9d0b511e9.jpg)  
Fig. 2. User interface.

![](/api/attachments/G2NCTNJT/fulltext/images/069fee40f5fbc493395a8157ec1d4cb59ced653d4f7f119221dcbefa14a3e95a.jpg)  
Fig. 3. Relation of data context, content, and quality.

Quality, context, and content are the three primary aspects of data in the QTIX system (see Fig. 3). User context is established first and this information is then used to determine a default set of data qualities. The user may then 'tune' the data qualities and content needs for a specific situation. Finally, data to fit these needs are supplied to the extent possible, given available data units and processes.

## 2.1.1. Data content

Data content requirements are explicit data needs specified by the user in a language and format familiar to them. In this application, the content section is used to specify the target type (e.g. SCUD missile) and the area of interest (e.g. southern Iraq). Currently, the user specifies the bounding region of interest by outlining the area on a map. In future versions of the system, we will use tactical order-of-battle databases and trafficability analysis tools to incorporate more contextual information about 'where' a target might be located. This would further bound the region of interest.

## 2.1.2. Data quality

Data qualities are aspects of the data implied by the interpretation or application of the data. In most cases, an analyst is required to extract these qualities and to translate them to quantifiable metrics based on discussions with users. In the case of image analysis, users require target classifications and locations, but they do not typically specify the image resolution or currency used to produce these classifications. Although users typically desire target classifications with specific timeliness and accuracy, current systems do not offer a choice of tradeoffs between these qualities. In the QTIX system, the quality requirements of currency, resolution, accuracy, and timeliness are specified through slide bars. The user may specify minimum currency for the imagery from which target information is produced. For example, if a user wishes to locate a mobile SCUD missile launcher, then a currency of less than 2 h for the images may be necessary, whereas if the user needs imagery of a fixed target, such as a building, then images that are 1 day or even 1 year old may suffice. Similarly, a user may use the resolution slide bar to specify the minimum resolution requirement. If a user is trying to locate small targets, higher resolution images may be needed to distinguish the target of interest from other objects that are similar in size and shape.

## 2.1.3. Data context

Data context provides the backdrop against which data supplied by the system will be interpreted and applied. As shown in Fig. 2, the context section allows for the specification of the user type (e.g. image analyst, strike planner, pilot, or all-source analyst) and purpose of the query (e.g. battle damage assessment, strike planning, or image analysis). Each combination of user type and query purpose implies a different importance of targets, processing time and accuracy requirements, and needed image resolutions and currencies.

For example, let us suppose that an enemy runway is attacked, and strike planners need to assess whether sufficient damage has been done, to determine if another bombing run is necessary. In this circumstance, images must not be older than the amount of time elapsed since the bombing run—thus, currency must be high. Furthermore, high-resolution imagery is necessary so that small, localized effects can be detected and the operational status of the target can be determined. To meet these quality constraints, QTIX automatically sets currency and resolution slide bars with appropriate values whenever Battle Damage Assessment is the context.

## 2.1.4. The dominant quality curve

Based on the context, currency, resolution, target type, available image analysis routines, and available images, a dominant quality curve (shown bold in Fig. 4) is dynamically constructed by QTIX and presented to the user. The dominant quality curve allows the user to see graphically the tradeoff between accuracy and timeliness. In the QTIX example, the curve represents the optimal processing time for a corresponding accuracy level. It is constructed from dominant segments of the quality curves generated when images are paired with available processes.

## 2.1.5. Example scenario

For exposition purposes, let us suppose that a pilot who is developing a strike plan chooses the target type to be ‘SCUD missile’ and the area of interest to be ‘southern Iraq’. For this mission, only images that have been taken within the last 4 h are pertinent, as the SCUD missile is a mobile target. Using this information, the QTIX system will produce a dominant quality curve that will be used by the pilot to determine the tradeoff between accuracy and the amount of processing time allowed for producing the target information.

There are a number of automated target recognition (ATR) algorithms available for finding SCUD missiles in images. Each SCUD ATR algorithm operates on image data of a specific type (or types) and resolution (or range of resolutions). There may be as many as 50 SCUD ATR algorithms and 500 images available in the area of interest. The challenge is to associate the available algorithms with the available images to find the image-algorithm pair that will produce the best target information.

There are six filters used in the QTIX system to make the number of images and ATR algorithms manageable and to allow for the selection of the best image-algorithm pair from the possible combinations. These are the area of interest filter, currency filter, resolution filter, the timeliness and accuracy filters, and the ATR algorithm filter. The first three filters are used to select only those images that are pertinent to the mission. The last filter is used to select pertinent ATR algorithms, and the processing time and accuracy filters are used to select the optimal image-algorithm pair using the dominant quality curve based on the user's requirements.

The timeliness and accuracy filters provide an interactive way for the user to select an image-algorithm pair based on user time or accuracy requirements. The mechanism used in this tradeoff is the dominant quality curve, which is made up of segments of image-algorithm quality curves. Each image-algorithm quality curve encapsulates the tradeoff between timeliness (processing time) and accuracy level for the algorithm given the image data. When all of the available image-algorithm quality curves are put together, it is not likely that one curve will give the best time-accuracy tradeoff for all timeliness values or classification accuracy. Therefore, the dominant quality curve takes the image-algorithm quality curve segments that dominate for all accuracy and processing times. By selecting a specific timeliness value, the accuracy that can be achieved in that time can be easily found using the dominant quality curve. As the dominant quality curve is made up of image-algorithm quality curves, selection of a timeliness value or accuracy also determines the image-algorithm pair used in processing.

![](/api/attachments/G2NCTNJT/fulltext/images/43f4e741b86536fb00d4f4a5bbd3dca2563e6ae687bf2d3b862e9cb64d1d0fae.jpg)  
Fig. 4. Production possibilities and dominant quality curve.

The dominant quality curve is a very effective technique because it allows the user, by setting different currency or resolution values, to explore different kinds of image analysis routines that can be applied to produce target information—a capability that does not exist in current systems. In addition, it allows the user to revise plans. For example, knowing that the degree of accuracy of the target information will increase from 80% to 98% with only a small increase in processing time, a commander may decide to postpone the flight mission for a short time so that a different production method can be applied to produce target information with 98% accuracy.

## 2.2. Raw materials: image database

Whereas the user interface determines product specification, the image database contains the raw material used in the production of the data unit products. The image database contains raw images such as electro-optical, radar, multi-spectral, and infrared images of areas of interest around the world. Each image is categorized according to geographical region of coverage, resolution based on pixel size, and time of capture.

## 2.3. Production tools: image processing and computer vision processes

The production tools used to process the raw image data comprise a set of image processing and analysis routines. There are a large number of processes available that have been developed over the years by researchers in image understanding and computer vision. Each of these processes falls into one of two broad categories: image processing and computer vision. Image processing processes clean up and modify raw image data to remove sensing artifacts. These processes include histogram equalization, noise removal, resampling to normalize pixel size, and photogrammetry methods used to maintain accurate distance measures between image pixels.

Computer vision processes are used to extract useful information about the real world from the image, and can be further categorized as belonging to feature extraction, grouping, and classification. In some cases, processes can belong to more than one category at a time. For example, neural networks typically span all three categories. These categories describe the typical processing sequence in current computer vision systems. Image processing functions are applied to the raw image data to prepare them for feature extraction processes. Significant features are extracted, grouped, and passed to classification processes that determine the real-world object represented in the image. Within each category of computer vision processes there are a number of processes that transform the data in similar ways but differ in approach, processing time, input data type, etc. These differences can be used to tune a high-level algorithm to available data to generate data units that were previously unattainable. An example of such processes is edge detection. Edge detection processes extract edge features from images. Some edge detectors are good at finding edges in low-contrast images whereas others are better at returning the exact location of the edge within the image.

![](/api/attachments/G2NCTNJT/fulltext/images/fd507ff098192958e11db31d5b765ccf5c4357f4b8e5048f41aae0f5d284a48b.jpg)  
Fig. 5. Processing possibilities.

![](/api/attachments/G2NCTNJT/fulltext/images/5e70dfa2d9ec2965608fd139a72bf6468caae9afa73a5074bacb8b54aa07da40.jpg)  
Fig. 6. Construction of virtual ER from data and processes.

## 2.4. Manufacturing possibilities generator

The manufacturing possibilities generator combines data units and processes to generate data production possibilities. The output of this system is a specification of all data units that can be produced with available data units and processes. In a classical decision system, data are provided to the user from data in a database. In the QTIX system, data can also be produced via processes applied to data in the database. The range of processing possibilities is determined at run-time through the construction of all possible processing algorithms given available processes and rules for process construction (see Fig. 5).

The result is that the original entity relationship diagram is replaced by a modified virtual entity relationship diagram because of the introduction of processes (see Fig. 6). The resulting virtual data make the production possibilities available to the user (see Fig. 4).

![](/api/attachments/G2NCTNJT/fulltext/images/a27ae3504bc9b3b068c4ec5aab9f7025d23377823f7b688694507d1db5c8ecf5.jpg)  
Fig. 7. Sample algorithm construction.

## 2.5. Manufacturing possibilities selector

Once the full range of data unit products has been generated, it is necessary to select the product that fits within the constraints that the user has specified and that matches most closely the indicated preferences. The manufacturing possibilities selector performs this function. The selector receives a production possibilities curve from the manufacturing system generator along with a data quality utility curve from the user interface. The selector supplies the data unit and processes that provide the output data unit with the highest utility. Fig. 7 shows an example of the selection and integration of processes and data performed by the manufacturing possibilities selector.

## 3. Theory

The general problem considered here is how to provide precisely specified data products that meet the data consumer's constraints. Data products are provided by applying processes to raw data or to data produced by other processes. The problem is to choose the raw data unit and process chain that are able to meet the data consumer's constraint limitations.

The goal of this work is to develop a mathematical framework that will support the production of highly specific data quality needs. The approach taken in the QTIX system is to first provide a model for representing all of the qualities of data units that may be important to users. Then processes are modeled as transforms of these data units—moving the quality description of each unit from one point in data quality space to another. After this groundwork is set, databases are modeled as a set of data units. The concept of the ‘process base’ is introduced as the set of all available processes. Together, a database and process base can be used to produce a larger set of data than was originally attainable.

![](/api/attachments/G2NCTNJT/fulltext/images/45f8588661e196b00c467136f76eb309d8af6895425dabeb655100329d74fd20.jpg)  
Fig. 8. An example of a data unit mapped in a data quality space in which n = 2.

![](/api/attachments/G2NCTNJT/fulltext/images/ea7b0c39f6b0e24bf4ca5df2f7b83df867a785050f4288d9585ce9e77d64840d.jpg)  
Fig. 9. Illustration of a process $p$ transforming a data unit from $d_{i}$ to $d_{o}$ .

## 3.1. Representing user needs

## 3.1.1. Data units as multidimensional entities

Data units in a database can be characterized by a multidimensional set of quality parameters. Let us denote each quality value by q. Then, the quality of data unit, d, can be described by a set of n quality parameters as

![](/api/attachments/G2NCTNJT/fulltext/images/9afad2da28c329e3ee6df38393eb69e0c64653758a3569cde58a55b13f9b2b37.jpg)  
Fig. 10. Illustration of a process p transforming a data set $D_{i}$ into data set $D_{o}$ .

![](/api/attachments/G2NCTNJT/fulltext/images/723e489de0c1e8e7fba06461511f699f04707c28c43897375d907cce824061b3.jpg)  
Fig. 11. Expansion of output data set, $D_{0}$ , by applying multiple processes to a given input data set, $D_{i}$ .

$$
d = \left\{q _ {1}, q _ {2}, q _ {3}, \dots , q _ {n} \right\}
$$

Each data unit may be thought of as occupying a position in data quality space. Fig. 8 shows a sample data unit, d, located in a two-dimensional data quality space. Data units with the same qualities would share the same position.

## 3.1.2. Data production preferences

Given all the data that a given system can produce, a user typically has a preference for some data items over others. These preferences can be expressed by a utility function, $U(d)$ .

## 3.2. Representing production possibilities

## 3.2.1. Processes as data transforms

Processes can be thought of as data transforms that move data through data quality space from one position to another. Let p represent a process transform, $d_{i}$ represent an input data unit, and $d_{o}$ represent the corresponding output data unit. Then, $d_{o} = p(d_{i})$ . Fig. 9 shows how process p transforms $d_{i}$ into $d_{o}$ .

## 3.2.2. Production possibilities with multiple data units

Processes can typically accept a set of data units as inputs. Let this set be denoted by

$$
D _ {\mathrm{i}} = \left\{d _ {1}, d _ {2}, d _ {3}, \dots , d _ {n} \right\}
$$

A given process, p, maps elements of the set, $D_{i}$ , into another set, $D_{0}$ (see Fig. 10). This is denoted as

$$
D _ {\mathrm{o}} = p (D _ {i})
$$

3.2.3. Production possibilities with multiple processes

Let us consider now that there are multiple processes available in an information system. Let P be the set of m processes;

$$
P = \left\{p _ {1}, p _ {2}, p _ {3}, \dots , p _ {m} \right\}
$$

Let $D_{i}$ denote the set of all data available in an information system. Then, assuming each process, $p_{x}$ in P, is applied to whatever subset of $D_{i}$ that intersects its domain, some set, $D_{o}$ , can be produced (Fig. 11) where

$$
D _ {\mathrm{o}} = p 1 \left(D _ {\mathrm{i}}\right) \cup p _ {2} \left(D _ {\mathrm{i}}\right) \dots p _ {m} \left(D _ {\mathrm{i}}\right)
$$

## 3.2.4. Production possibilities with feedback

To fully enumerate the data production possibilities of a database, $D_{i}$ , and a set of processes, P, we must consider that data units produced could be fed back into the input database to be used by subsequent processes (Fig. 12). Under certain conditions, this could result in the production of additional output data units that were previously unattainable. For example, if a process, p, is applied to a data unit, $d_{i}$ , it would produce a data unit, $d_{o}$ . If $d_{o} \notin D_{i}$ , then it may be possible that $d_{o}$ could be used by a process in P to produce a new output, $d_{o} \notin 'D_{o}$ .

![](/api/attachments/G2NCTNJT/fulltext/images/1593339425bda16668dab5287082b53bcf2e2e47090d02ae21d132098ab01e56.jpg)  
Fig. 12. System flow diagram illustrating the production of data set $D_{0}$ and the update of data set $D_{i}$ .

## 3.3. Optimizing needs given possibilities

From a given utility function, $U(d)$ , and a production possibilities function, $D_{i}$ , the data unit(s) which should be produced are those that maximize user needs and that are producible:

$$
u (d) = \max [ u (d) ]; \quad \forall d \in D _ {i}
$$

## 4. Conclusions

Incorporating quality information explicitly in the development of information systems can be surprisingly useful. A general framework for modeling data and processes in information has been formulated for the purpose of deriving methods to produce data units of specific data qualities. In addition, an initial system architecture has been specified for specific data quality production via a chain of processes. In this research, we investigated how imagery production methods can be associated with quality information so that users could select the quality of the target information they need before it is produced. Toward this goal, we developed the concept of a dominant quality curve, which is a set of tradeoffs, computed based on the available production methods (process chains) and image data. The dominant quality curve is shown to be effective for users such as pilots and commanders in making their tactical decisions.

The mathematical treatment of quality transformations and the dominant quality curve helps to establish a foundation for designers to further understand QTIX and improve its performance. We organize the image processing and computer vision processes into different processing stages, much like an assembly line in a manufacturing plant.

The research presented in this paper is a first step toward the design and development of flexible information systems that treat processes as analogous to machine tools, and data as analogous to raw input materials in a manufacturing setting. By associating quality transforms with the data transforms performed by processes, the system is able to produce information products that closely conform to the user's information quality requirements.

## References

[1] K.C. Laudon, Data quality and due process in large interorganizational record systems, Commun. ACM 29 (1) (1986) 4–11.

[2] G.E. Liepens, R.S. Garfinkel, A.S. Kunnathur, Error localization for erroneous data: a survey, TIMS-Stud. Manage. Sci. 19 (1982) 205–219.

[3] G.E. Liepens and F.R.R. Uppuluri (Editors), (1990). Data Quality Control: Theory and Pragmatics. Marcel Dekker, New York.

[4] R.C. Morey, Estimating and improving the quality of information in the MIS, Commun. ACM 25 (5) (1982) 337–342.

[5] R.C. Oman, T.B. Ayers, Improving data quality, J. Syst. Manage. 39 (5) (1988) 31–35.

[6] T.C. Redman, (1992). Data Quality: Management and Technology. Bantam, New York.

[7] D.M. Strong, Decision support for exception handling and quality control in office operations, Decision Support Syst. 8(3) (1992) 217–227.

[8] D.M. Strong, S.M. Miller, Exceptions and exception handling in computerized information processes, ACM Trans. Inf. Syst. 13 (2) (1995) 206–233.

[9] R.L. Keeney and H. Raiffa, (1976). Decisions with Multiple Objectives: Preferences and Value Tradeoffs. Wiley, New York.

[10] Y. Jang, H.B. Kon and R.Y. Wang, (1992). A data consumer-based approach to data quality judgment. In: V. Storey and A. Whinston (Editors), Second Annual Workshop on Information Technologies and Systems (WITS-92), pp. 179–188.

[11] D.P. Ballou, H.L. Pazer, Designing information systems to optimize the accuracy–timeliness tradeoff, Inf. Syst. Res. 6(1) (1995) 51–72.

[12] D.P. Ballou, H.L. Pazer, Modeling data and process quality in multi-input, multi-output information systems, Manage. Sci. 31 (2) (1985) 150–162.

[13] C.S. Draper-Lab, (1984). Flexible Manufacturing Systems Handbook. Noyes, Park Ridge, NJ.

[14] M.J. Mazarr, D.M. Snider and J. Blackwell, (1993). Desert Storm: the Gulf War and what we learned. Published in cooperation with the Center for Strategic and International Studies, Washington, DC.

![](/api/attachments/G2NCTNJT/fulltext/images/f9af999ed9f06968797c66fb593244a867c5c6495896297bba43a51b41680b38.jpg)

Peter Kaomea has designed and implemented command, control, and surveillance systems for the Naval Command, Control, and Ocean Surveillance Center for 9 years. He also serves as a Captain in the US Air Force Reserves. His education includes a B.Sc. in electrical engineering from MIT, an M.Sc. in electrical engineering from the University of Hawaii, and an M.Sc. in management science from MIT Sloan School. He currently works as a technical process de-

signer for a major financial institution.

![](/api/attachments/G2NCTNJT/fulltext/images/1d74dcef3f37f6e18d5caaf70507c2a24c99fb5087d1c644cef167a67ac51341.jpg)

Ward Page is senior project manager and researcher at the Naval Command, Control, and Ocean Surveillance Center. He specializes in tactical information exploitation systems. He holds B.Sc. and M.Sc. degrees in computer science from the University of Illinois.
