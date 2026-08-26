---
otero_id: 24856
otero_key: "EQMFFNXY"
title: "A Hypermedia-Based Design Image Database System Using a Perceptional Link Method"
authors: "Yoshitaka Shibata; Manabu Fukuda; Michiaki Katsumoto"
year: "1996"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1996.11518132"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Hypermedia-Based Design Image Database System Using a Perceptional Link Method

Yoshitaka Shibata, Manabu Fukuda & Michiaki Katsumoto

To cite this article: Yoshitaka Shibata, Manabu Fukuda & Michiaki Katsumoto (1996) A Hypermedia-Based Design Image Database System Using a Perceptional Link Method, Journal of Management Information Systems, 13:3, 25-44, DOI: 10.1080/07421222.1996.11518132

To link to this article: http://dx.doi.org/10.1080/07421222.1996.11518132

![](/api/attachments/EQMFFNXY/fulltext/images/691a27beead787409d65c3c9e3bcc65a86aa1545e22ca710ee00e214329fefd3.jpg)

Published online: 08 Dec 2015.

![](/api/attachments/EQMFFNXY/fulltext/images/3aa7b04a2d7568a83dadf3b5e17899d1ff0b0b75b7ca136e04d0ece10982eb22.jpg)

Submit your article to this journal ↗

![](/api/attachments/EQMFFNXY/fulltext/images/5f0d2f17c2870a85ac9e245dfc5d29e5b669520101b2ad6e48438e4bea80d31e.jpg)

View related articles ↗

![](/api/attachments/EQMFFNXY/fulltext/images/3fe6f91a05c2e75560778ce74ad80eb4249a42bf6760507317ecc7501e84223a.jpg)

Citing articles: 4 View citing articles ↗

# A Hypermedia-Based Design Image Database System Using a Perceptional Link Method

YOSHITAKA SHIBATA, MANABU FUKUDA, AND MICHIAKI KATSUMOTO

YOSHITAKA SHIBATA received his Ph.D. in computer science from the University of California, Los Angeles, in 1985. From 1981 to 1985 he was a doctoral research associate in the Computer Science Department where he engaged in software development for high-speed simulation for an array processor. From 1985 to 1989 he was a research member in Bell Communication Research, where he worked in higher-layer protocol design and end-to-end performance analysis of multimedia information services. Since 1989 he has been an Associate Professor of Information and Computer Science at Toyo University, where he directs an intelligent multimedia network laboratory. His research interests include multimedia databases, intelligent human interfaces, hypermedia systems, and high-speed networks and protocols. He is a member of IEEE, ACM, the Information Processing Society of Japan (IPSJ), and the Institute of Electronic and Communication Engineering in Japan (IEICE).

MANABU FUKUDA received a B.S. in 1994 from Toyo University where he is currently a graduate student in the Department of Electrical Engineering. His research interests include multimedia databases, perceptual information processing, hypermedia systems, and the Internet. He is a member of IPSJ.

MICHIAKI KATSUMOTO received his B.S., M.S., and Ph.D. degrees from Toyo University, the latter in 1996. He is now with the Communication Research Laboratory of the Japanese Ministry of Posts and Telecommunication. His research interests include hypermedia systems and multimedia databases. He is a member of IPSJ, IEICE, the IEEE Computer Society, and the ACM.

ABSTRACT: We introduce a hypermedia-based distributed design image database system that can provide simple and flexible user access capabilities based on the "kansei" link method. As proof of this concept, we have developed a prototype distributed multimedia information network incorporating the DHS model. Dubbed the Textile Design Image Database System (TDIDS), this database aids designers using apparel computer-aided design (CAD) systems in different locations, collaborating or working separately, in the design of clothes, including kimonos. Our purpose has been to create a database that will allow each designer to make the best use of his

Acknowledgments: We would like to thank our user test group among the textile design students in Sugino Women's College in Japan for their patient and enthusiastic service; their many suggestions have consistently born fruit. We would also like to give special thanks to our esteemed colleague and editor, Professor Steven Paiano of Toyo University's English Department. This research was supported by the Kurata Foundation.

or her creativity and originality—his or her “style and sensitivity to beauty,” or, in Japanese, kansei.

In our hypermedia system, “metanodes” are defined as abstract nodes that are dynamically organized by multimedia objects, while “metalinks” are defined as flexible kansei links. Metanodes and metalinks are combined to organize a dynamic hypermedia space from which users can easily retrieve desired design image objects by querying a knowledge agent. The knowledge agent, utilizing the knowledge base, creates links from kansei word objects provided by the user to suitable design image objects among those stored on multimedia databases distributed across the network. The knowledge agent also performs query conversion of individual users’ subjective kansei (idiosyncratic, subjective use of kansei words) into objective kansei words using each user’s own “user model,” These objective kansei words are then converted to equivalent color values. Color value is the means by which all stored design images are characterized. This dynamic linking of kansei word objects to equivalent design images allows individual users’ kansei to influence the retrieval process. The sophisticated and flexible CAD systems of the future will require multimedia database systems with cooperative supporting capabilities similar to our kansei system.

KEY WORDS AND PHRASES: design databases, hypermedia, image datatabases, perceptual retrieval.

THE RAW HORSEPOWER OF COMPUTER HARDWARE IS GROWING STEADILY; network technology is providing radical breakthroughs in connectivity, yet, to the layperson, computers remain almost as daunting as ever. Artists in particular often experience particular frustration when they attempt to use computer technology. The time and temperament necessary to master current computer design applications remain a formidable barrier, despite the high level of functionality of such applications. While a multitude of advances in computer technology may be necessary to address such complaints adequately, a useful step in that direction is our multimedia database system, the Textile Design Image Database System (TDIDS), which responds and adapts to its users' individual tastes.

Our TDIDS project is designed to implement a database that would be difficult to create using standard database technology: There are a number of distinct traditions of textile, clothing, and kimono production sprinkled throughout the cities and small towns of Japan, many of which preserve and perpetuate design traditions that are centuries old. The textures and design patterns of these products remain relevant and valuable in various design fields—not only in traditional kimono design but in more modern design industries, including the general apparel industry, dress making, and interior design. In order to obtain data on traditional Japanese textiles, however, at present one must visit a number of different local textile industrial institutes, art galleries, and/or museums. A database of traditional Japanese textiles has yet to be established, perhaps because of the volume and complexity of the subject matter. To implement such a database, we propose a hypermedia-based textile design image database system whereby database servers who store traditional textile images, distributed across many cities and towns, are connected by a high-speed network and coordinated by a knowledge agent. Our TDIDS is a working prototype of just such a network.

The kansei approach to our TDIDS has evolved over several years in response to our desire to develop more intelligent, human-centric computer interfaces. In previously published research, we introduced a Dynamic Hypermedia System (DHS) [5, 7] in which the links between a reference point and a corresponding object were dynamically determined using a knowledge base, thereby attaining more suitable and flexible linking. Such hypermedia systems provide useful human interfaces for multimedia database systems, allowing users to interactively access databases by retrieving multimedia information with simple icon-driven mouse operations. We utilized a DHS interface in the first implementation of our TDIDS; users were able to access and manipulate the database directly by simple mouse operations.

The system incorporated conventional keyword retrieval methods—such as specifying materials, patterns, or representative colors as keywords—or similarity retrieval methods—such as directly specifying color values on the color map that are similar or representative of the design images [5].

These methods of design image database retrieval, however, were often not sufficient from the point of view of the designers who served as our users. They rarely found the users' queries or retrieved images usable and felt the system was rather "hit-or-miss." Many of the designers expressed a wish for a more direct and subjective retrieval method.

In a project conceptually related to our kansei approach, the ART MUSEUM [4, 6], Kato et al. developed a system capable of kansei retrieval, though their method was in our opinion insufficient. The ART MUSEUM incorporates user models constructed in advance for each user and fixed (not dynamically adapting to the users' kansei). And, since the perceptual retrieval indexes are created by a single indexer, they necessarily reflect the indexer's kansei. Therefore, unless the users understand and manipulate the indexes well, they cannot perform true kansei retrieval. Hirabayashi et al. [1] describe a perceptual retrieval method keyed to an impression scale. We do not consider this method a true kansei retrieval method either; it suffers from shortcomings similar to those of the ART MUSEUM project: The impression scale is fixed beforehand and does not adapt to individual users' kansei.

From our own experiences and a review of related research, we realized that, in order to create a useful retrieval system, each image would have to be characterized by kansei words. As the relationship between words and different design images changes depending upon individual kansei, we decided that design images cannot be objectively, statically characterized by kansei words in a truly useful manner.

To overcome this problem we have developed a subjective retrieval method based on a user model structure designed to reflect differences in kansei among different individual users. Our method is based on “intelligent” user models that model individual users’ kansei by observing and adapting to users’ repeated acts of image retrieval. Users retrieve design images by simply selecting “kansei words,” such as “exotic,” “elegant,” or “chic.” These kansei queries are converted into objective kansei words by each user’s user model; they are then interpreted as a color value (Red-

Green-Blue or Munsell color), or a combination of colors according to information stored in the knowledge base.

The design images, on the other hand, are characterized by various components such as color components, design patterns, materials, and textures. Since it is known that color components have a stronger influence on users' kansei than the other components have, we initially incorporated the color values and their corresponding area percentages to characterize the design images. Thus, by specifying color values to the image database, nominated images can be retrieved, sent through the knowledge agent, and browsed on the user's station. Browsed images are then evaluated for user satisfaction. On the basis of this evaluation, the parameter values of the user model are adjusted to minimize the difference between the user's subjective kansei and the browsed images' kansei definitions. The initial parameter values of the user's user model are informed by "color image engineering," the experiences of professional designers involved in our project, and statistical data on the evaluation of typical design images by our user test group of designers. These experimental data are collected into the knowledge agent to serve as the knowledge base and used to initialize the user model and convert kansei words into an equivalent color combination. The user model's learning process is repeated several times for each new user, often enough to allow convergence of parameter values during the initial retrieval stage. By combining this subjective retrieval method based on the user model with a DHS based on the kansei link method, the system performs far more flexible and kansei-like retrievals of design images than are possible using more conventional database search methods.

## Textile Design Supporting Systems

TEXTILE DESIGN, LIKE OTHER FIELDS OF DESIGN, INVOLVES MANY HOURS of tedious trial and error. Such labor-intensive design work is greatly aided by our multimedia database which allows designers to simply and interactively retrieve textile images and patterns by specifying kansei words (along with corresponding scales of intensity), immediately pasting these textile images over three-dimensional apparel design images, and thereby quickly producing finished design images. Examples of kansei words are “exotic,” “elegant,” or “chic.”

Figure 1 shows how such a system works from a user's point of view. In response to the user's queries, images appear (transmitted from multimedia databases distributed throughout the network) in the browsing window (top left). From among these images, the user chooses those of interest to him or her and then pastes these images into the clip window (top middle). Manipulation of color and color intensity is performed in the color convert window (top right). The texture grid window (bottom left) contains images of fashion models wearing user-selected white “neutral materials.” These “neutral materials” include lines for shaping two-dimensional images into three-dimensional images. The user then creates finished images in the texture map window (bottom right) by pasting fashion model images from the texture grid window, then textile images from the window.

![](/api/attachments/EQMFFNXY/fulltext/images/bafc370fd62a699a7008374432d7a131b4c68f18e306d78c74d927d7c773c7c8.jpg)

![](/api/attachments/EQMFFNXY/fulltext/images/af8c930de1439651ba8da19d30edca81e553bfe2f1e7b4578c66a4bda052ff8a.jpg)

![](/api/attachments/EQMFFNXY/fulltext/images/5ede436cdaba6c58dd690ffe95f318cd8c8f25a0402b62f1a6144c2b54ee9c1f.jpg)  
Figure 1. Textile Design Supporting System

To achieve the level of performance described above, a multimedia database system should offer the following functions:

1. "Kansei" retrieval functions, to make best use of users' individual creativity;

2. Interactive access capability provided over a distributed database environment;

3. A simple but robust graphical user interface;

4. A user model that considers the differences among users' kansei.

## Dynamic Hypermedia Systems

WHEN WE REVIEW THE CURRENT STATE OF DESIGN DATABASE SYSTEMS, it is obvious that a more flexible, more effective, and more intelligent user interface is needed. We believe that hypertext systems, in which each unit of information is directly connected to others and users can navigate simply over the linked information space using a graphical user interface (GUI), are essential to such improvements. Other researchers have developed several prototype applications that utilize hypertext or hypermedia systems to access a multimedia database system. For example, World Wide Web (WWW) is the most popular and global hypermedia system. Another hypermedia system, "Miyabi," applies a media-based navigation approach based on similarity retrieval by shapes in the images. Those systems, however, do not provide intelligent link operations that perform dynamic and automatic linkages from the user's current reference point to the most suitable information unit(s) based on the user's information retrieval goals.

In order to solve the problems inherent in current conventional hypermedia systems, we developed a new dynamic hypermedia system consisting of a metanode, a metalink, and a frass. A metanode is defined as the semantically integrated information unit. Each metanode is organized by video, audio, graphics, and/or text media as presented in figure 2, and manipulated as an ordinal node. Individual media data are structured as files and stored on local database servers distributed over the network. Each local database management system, such as the relational database system, maintains the file names of those media data within its own database as a set of tuples. In our TDIDS, video and graphics data are not used. Figure 3 describes a sample metanode that explains a “chic” image in the TDIDS. In this example, the metanode is organized by image data that shows its characteristics and by audio and text data that describe its material, pattern, texture, and representative color components.

Larger units of information space are organized as a “frass” (“frame with class”); a frass is defined as a set of classified metanodes that are semantically related to each other. For example, some of the design images in our TDIDS are characterized as “chic”; others may be characterized as “elegant,” although their degrees of impression may be changed for each image. Thus, those similar images are classified into a cluster of the whole images and defined as a frass. A frass has characteristics of both a class (as used in object-oriented systems) and a frame (as used in knowledge-base systems).

Figure 2. Structure of a Metanode

![](/api/attachments/EQMFFNXY/fulltext/images/97aad81213a4180c122b664580dfd83660b1b48dfffe5a05d9dfdeb98cd7778b.jpg)

![](/api/attachments/EQMFFNXY/fulltext/images/ad4cc9577ec0726573d0e9adeac39436a8b81904dc8d8382a2fb0257455b1ca7.jpg)  
Figure 3. Example of a Metanode

A frass can be easily implemented with an object-oriented language and organized as a knowledge base. Figure 4 shows an example of frasses consisting of a set of images with the same attribute “chic” and “elegant,” but with different attribute percentage values.

A metalink is defined as a virtual link between different metanodes and/or frasses. Unlike conventional links, multiple metalinks from a reference point in the current information unit to subsequent metanodes or frasses may be connected to each other. Using the knowledge base, the link manager in the knowledge agent (explained in the next section) dynamically selects the most suitable metalinked metanodes and frasses depending upon the user's requests. This decision process can be repeated as long as any following node exists.

To enable multiple users to share the knowledge base, we divided the DHS into two parts. One part is the client agent; the other is the object manager. A client agent containing the user's user model and performing I/O interface functions is located on each user's station. The object manager is separated from the users' stations and independently situated as part of the knowledge agent.

Downloaded by [University of Pennsylvania] at 06:11 12 August 2017  
![](/api/attachments/EQMFFNXY/fulltext/images/e5863807fba74ec143114f2e70fb27d26491050c884beb2c584d38b43d8b5e40.jpg)  
Figure 4. Illustration of Frass  
Frass:Textile

## The Knowledge Agent

THE TDIDS, SHOWN IN FIGURE 5, CONSISTS OF A NUMBER OF USER STATIONS, multimedia databases, and a knowledge agent distributed over an interconnected network consisting of multiple LANs and a WAN. The knowledge agent performs various functions to aid intelligent information retrieval, acting as a user's "consultant" and managing the databases distributed over the network. Users issue kansei word queries (they may also issue conventional word queries) to the knowledge agent through their individual client agents. User queries to the knowledge agent are then converted into database queries (having first been converted from subjective to objective kansei words by the user model) and transmitted to all related multimedia databases using the multicast remote procedure call [3]. The link manager in the knowledge agent creates links to the most suitable metalinked metanodes and frasses using information from the knowledge base. The object manager then collects these images, filters out any redundant images, and sends these selected images to the user's stations, organizing a suitable information space for the user. Thus, users can interactively browse and retrieve images without knowing the locations of the databases queried. From the user's point of view, this information space appears as a seamless multimedia database space, as if it existed entirely within the knowledge agent even though the actual information is located within database servers distributed across the network and managed by multimedia database management systems localized within each server.

In future large multimedia information systems based upon our kansei approach, several knowledge agents will be able to coexist. Each knowledge agent will have its own knowledge base and area that it can cover within the database servers. When a knowledge agent is asked for information about a subject for which it does not have a complete knowledge base, it will ask other knowledge agents whether they have information in their knowledge base on the subject in question. Thus, by cooperating with each other, knowledge agents will obtain new knowledge and create links to suitable metanodes stored on database servers pertaining to other areas of information.

## The Knowledge Base

The knowledge base provides information to the knowledge agent that is used to determine links to suitable objects (metalinked metanodes and/or frasses) depending upon users' requests or interests. Each metanode is classified according not only to its attributes but to the degree of those attributes. In the TDIDS, the attributes of metanodes (in this case, textile images) are characterized as various kansei attribute words or a combination of them. These kansei attributes are quantified as independent kansei vector values to express the degree of attribute. At the same time, each image is characterized by color and design pattern. $^{1}$ Thus, the relationship between an image's attributes, colors, and pattern is stored as knowledge base within the knowledge agent. In our TDIDS, fifteen of the kansei words including "pretty," "romantic," "dandy," "casual," "natural," "formal," "dynamic," "elegant," "clear," "gorgeous,"

Figure 5. Distributed Textile Design Image Database System

![](/api/attachments/EQMFFNXY/fulltext/images/6ff74a5b7892d3cf1a698a72ba6f0a7e9854affc6d432958a074a3bdefbc4f69.jpg)

Table 1. Kansei Words and Cluster ID Numbers

<table><tr><td>Cluster ID no.</td><td>Kansei word</td><td>Cluster ID no.</td><td>Kansei word</td><td>Cluster ID no.</td><td>Kansei word</td></tr><tr><td>1</td><td>Pretty</td><td>6</td><td>Romantic</td><td>11</td><td>Dandy</td></tr><tr><td>2</td><td>Casual</td><td>7</td><td>Natural</td><td>12</td><td>Formal</td></tr><tr><td>3</td><td>Dynamic</td><td>8</td><td>Elegant</td><td>13</td><td>Clear</td></tr><tr><td>4</td><td>Gorgeous</td><td>9</td><td>Chic</td><td>14</td><td>Cool casual</td></tr><tr><td>5</td><td>Ethnic</td><td>10</td><td>Classic</td><td>15</td><td>Modern</td></tr></table>

“chic,” “cool,” “ethnic,” “classic,” and “modern,” which are frequently used in kimono design, are related to 130 Munsell color combinations. An example of the knowledge base is summarized in Table 1, which presents the relations between the kansei words “chic” and “elegant,” and the equivalent color components. In this case, the kansei word “chic” is related to sixteen color components, including Yellow Red with Dull tone (YR\_DL), Yellow with Gray tone (Y\_Gr), and so on. On the other hand, the kansei word “elegant” is related to eighteen color components, including Red with very pale tone (R\_Vp).

When executing textile image retrieval, the user can specify a combination of kansei words and their degrees as a query. The knowledge agent then selects the best metanode match(es) from among the subsequently nominated metanodes.

## The Kansei Link Method as Implemented in the TDIDS

IN ORDER TO LINK SELECTED KANSEI WORDS (which the system treats as objects) to suitable design images, the relationships between kansei words and design images are clearly defined. Design images within the TDIDS are generally characterized by representative colors—namely, color values (RUB, HUV, or Munsell color expressions), and their area percentage of the whole image. In addition, most color values are characterized by one or several kansei words. For example, bright red colors are generally characterized by kansei words such as “dynamic” “casual,” or “passionate.” A combination of a brown color and a gray color is classified by kansei words such as “classic” or “dandy.”

Figure 6 shows an example of the TDIDS's automatic indexing. The best five dominated colors and their area percentages of the original image are extracted by calculating their color pixel distribution. Then, the kansei words equivalent to each extracted color are selected. Next, a kansei vector is formed using the area percentages of the best five color components, assuming that the degree of the kansei is proportional to the area percentage of the equivalent color. Thus, by registering these vector values in advance, all design images can be indexed and stored in the databases distributed over the network.

On the other hand, the initial or “default” relationships between color components and kansei words are also stored in the knowledge agent as part of the knowledge base. These default settings determine the relationship between kansei words and color values as informed by color engineering, the opinions of professional designers involved in the project, and statistical data on the evaluation of sample design images by our user test group, even taking into account changes in fashion from one generation to the next. These “default” relationships form the “objective” or “average” kansei stored in the knowledge base. Thus, as shown in figure 7, users select kansei words and send them to the knowledge agent, where they are converted into equivalent color values based on the knowledge base. The knowledge agent then creates dynamic links from the user’s kansei words to suitable design images. We call this the “kansei link method”: All design images are expressed by representative color values and color value area percentages. By registering these values in advance, all design images can be indexed and managed by a conventional database management system.

![](/api/attachments/EQMFFNXY/fulltext/images/5ace4600b2e37d491aee8dd89a408e0006965978d823db7e91110356ed79a23c.jpg)

A  
↑

<table><tr><td></td><td>38%</td><td>elegant</td><td>chic</td><td rowspan="5">formal</td><td></td><td>modern</td></tr><tr><td></td><td>16%</td><td>elegant</td><td>chic</td><td>cool</td><td>modern</td></tr><tr><td></td><td>16%</td><td></td><td>chic</td><td>cool</td><td>modern</td></tr><tr><td></td><td>6%</td><td></td><td>chic</td><td>cool</td><td>modern</td></tr><tr><td></td><td>4%</td><td>elegant</td><td>chic</td><td></td><td></td></tr><tr><td colspan="2">Kansei Vector</td><td>{58</td><td>80</td><td>16</td><td>38</td><td>76}</td></tr></table>

B

<table><tr><td rowspan="2">Object ID</td><td rowspan="2" colspan="5">Best 5 of Colors and Color Area Size</td><td colspan="6">Perceptional Vector</td></tr><tr><td>pretty</td><td>...</td><td>elegant</td><td>chic</td><td>...</td><td>ood modern</td></tr><tr><td>3200002</td><td>38%</td><td>16%</td><td>16%</td><td>6%</td><td>4%</td><td>0</td><td>...</td><td>58</td><td>80</td><td>...</td><td>38 76</td></tr><tr><td>3200003</td><td>37%</td><td>28%</td><td>15%</td><td>6%</td><td>3%</td><td>0</td><td>...</td><td>65</td><td>37</td><td>...</td><td>28 15</td></tr></table>

Figure 6. Indexing of Design Image as Kansei Vector: A: The Original Design Image; B: Best Five-Color Component and Kansei Vector; C: Registration of Kansei Vector in Knowledge Base

## The User Model

THE KANSEI LINK METHOD INCLUDES TWO RETRIEVING METHODS: the objective retrieval method and the subjective retrieval method. In the objective retrieval method, users send queries to the knowledge agent directly (bypassing the user model); the queries are then converted into database queries by the knowledge agent. This method provides general design image retrieving capabilities; however, since it is based upon the “objective” or “average” human kansei stored in the knowledge base, the retrieved images may not suit the user’s taste—they are an informed average, not a “custom fit.”

In the subjective retrieval method, the user's subjective kansei queries are converted into objective kansei queries by the user model located within the user's client agent. The user model compensates for differences between individual users' kansei and the "objective" kansei stored in the knowledge base. To organize the user model, we define a kansei vector space consisting of N kansei vector components (currently, we use fifteen kansei vector components). Since most design images can be characterized by several kansei words, these are expressed by N vector components, as indicated in figure 8 (some of N components may be 0). Therefore, by specifying kansei words as vector values Q, suitable design images R (matching the "objective" kansei) can be retrieved. However, since images R were selected based on the "objective" or "average" kansei, the user will not necessarily be satisfied with these images. Therefore, the user model must compensate for the difference between Q and R according to the following equation:

$$
R = U Q,
$$

where U is the user model, as expressed by the $N \times N$ matrix. Since all the vector components of Q cannot necessarily be specified as a query, U cannot be determined by one attempt; however, by repeated evaluation of retrieved images $R_{i}$ , the modification of the user model $U_{i}$ and the user's characteristic selection of kansei words affect $Q_{i}$ . Thus, the user model can be gradually conversed to a more correct value

![](/api/attachments/EQMFFNXY/fulltext/images/930dc222dc8ffbcab5a4a5d9623732d03057898ab6cf9fe7d04ffe04cd79eeb6.jpg)  
Figure 7. Kansei Retrieval

according to the following equation:

$$
R _ {i} = U _ {i} Q _ {i}.
$$

The optimal $U_{iopt}$ that minimizes the following error function $E_{i}$ at each step i,

$$
E _ {i} = \frac {(U _ {i} Q _ {i} - R _ {i}) ^ {T} (U _ {i} Q _ {i} - R _ {i})}{2}
$$

must satisfy the following condition:

$$
\frac {\partial E _ {i}}{\partial U _ {i}} = 0.
$$

By finding the $U_{iopt}$ and updating $U_{i} \leftarrow U_{iopt}$ , the user model can learn the correct parameter value. This learning process for the user model is usually executed at the beginning of image retrieval but can be repeated at any time after the model has been fixed. As the user models interact with the knowledge agent, the knowledge agent gathers statistics from them; thus, they influence it (and hence each other) on a dynamic basis. Through this process, the “objective” kansei is changed. On our prototype system, to provide these statistics, users periodically perform image satisfaction evaluation. In future systems, the knowledge agent may gather statistics by more subtle and automatic means.

## Prototype System

OUR PROTOTYPE SYSTEM (PREVIOUSLY SHOWN IN FIGURE 6) CONSISTS of several RISC-based workstations and file servers. The system is connected by FDDI, Ethernet, and ISDN networks. Three SONY NWS–3865 workstations (equivalent to Sun Sparc 2)

Figure 8. Illustration of Updating User Model

![](/api/attachments/EQMFFNXY/fulltext/images/2348884ff6e5a63ac14b9e5b7d42de6b033537e6923f3ab21281cd92e6b12f46.jpg)

with color video interfaces serve as user workstations, and one SUN-4/670MP houses the knowledge agent. Several SONY NWS-3870s (equivalent to Sun Sparc 2) are used as multimedia database servers. The application programs were written in C language. The implementations of the Dynamic Hypermedia System and the knowledge agent were developed using a combination of C language and a knowledge base language, IXLA [9]. The knowledge base is implemented in object-oriented IXLA language. Figure 9 shows a sample output from a textile image retrieval prompted by the kansei word “elegant.”

## System Evaluation

IN ORDER TO EVALUATE OUR PROTOTYPE TDIDS, we have employed a questionnaire method by which members of our user test group indicated their degree of satisfaction (0–100 percent) with images provided by our kansei retrieval system. We entered 1,600 images and 15 kansei words. The user carried out the questionnaire five times for each kansei word. In addition, we investigated kansei vector values for two selected kansei words, "chic" and "clear." We chose these because "chic" contains the most entries in the TDIDS while "clear" contains the least, as we geared our prototype TDIDS to appeal to our young user test group; our user test group consisted of 28 users—16 male and 12 female, all in their early twenties. Changes resulted after each user models' kansei values were updated (see figures 10 and 11). The horizontal axis is kansei word ID; the vertical axis is kansei vector value. In figure 10, which represents the kansei word "chic," kansei values gradually converged after each questionnaire. In other words, the user models matched to their users. With the last questionnaire, retrieved image satisfaction reached 80 percent. In figure 11, representing "clear," the kansei values did not converge to a great extent, that is, the user models did not match to their user.

The questionnaire results show that our user models' kansei retrieval and updating method works well. However, when there are few images linked to a kansei word or the images are not suitable, the user model will not match well with the user for that kansei word.

## Conclusions

WE HAVE INTRODUCED A NEW, "INTELLIGENT" HUMAN INTERFACE based on the concept of a Dynamic Hypermedia System using the kansei link method to provide simple and flexible user access to multimedia information networks. Metanodes, metalinks, and frasses organize a dynamic hypermedia space wherein users can easily retrieve desired information objects by performing kansei word queries. The knowledge agent uses information from the knowledge base to create links from kansei word objects to suitable design images chosen from the various multimedia databases distributed over the network. The knowledge agent also performs query conversion from the users' kansei words to objective kansei words using information from each users' individual user model. In order to verify the functionality of our proposed human interface, we have developed a prototype multimedia information network dubbed the Textile Design Image Database System. With this prototype system, we have confirmed the usefulness of our proposed kansei approach interface. We are currently in the preliminary stages of full implementation of an improved TDIDS on a prefectural-wide scale. This new TDIDS will also incorporate image pattern as an additional key for kansei word selection.

![](/api/attachments/EQMFFNXY/fulltext/images/7ae0ff12c162bdcf746d990256be4b7611949e753daae4583ee98a32812d67e1.jpg)  
er Interface for Textile Design Image Database System

![](/api/attachments/EQMFFNXY/fulltext/images/c9e7a5306ee7d046b0917e98e68c0e95b35be078472dc08d29a3655fa721b28d.jpg)  
Figure 10. Kansei Vector Value of User Models of "Chic"

![](/api/attachments/EQMFFNXY/fulltext/images/dd451d8925e85ff3290fd40789afe921528e788f5f1a67723b096dbd999e5076.jpg)  
Figure 11. Kansei Vector Value of User Models of "Clear"

While we have developed the kansei approach as an aid to designers, we feel it has potential for wide application. for example, as the basis for a music database delivered over a high-speed network that would allow users to select music using kansei words, adapting to their tastes over time. It is significant that our kansei approach requires little in the way of processor overhead; it is well suited for application using current technology.

## NOTE

1. Although image pattern is not used as a key kansei word retrieval within our current prototype, image pattern information was included in the knowledge base since it will be incorporated as a key in our next TDIDS implementation.

## REFERENCES

1. Hirabayashi, F.; Matoba, H.; and Kasahara, Y. Information retrieval using impression of documents as a clue. ACM SIGIR (1988), 233–244.

2. Hirata, K.; Hara, Y.; Shibata, N.; and Hirabayashi, F. Media-based navigation for hypermedia systems. Proceedings of ACM Hypertext '93, November 1993, pp. 82–93.

3. Hirose, N.; Katsumoto, M.; and Shibata, Y. Retrieval method and performance analysis of distributed database system. IPSJ Multimedia Communication and Distributed Processing System Workshop, 94, 1 (October 1994), 289–297 [in Japanese].

4. Kato, T.; Kurita, T.; Shimogaki, H.; Mizutoti T.; and Fujimura, K. Cognitive view mechanism for multimedia database system. Proceedings of IEEE IMS '91, 1991, pp. 179–186.

5. Katsumoto, M.; Fukuda, M.; and Shibata, Y. Dynamic hypermedia system based on perceptual link method for distributed design image database. Proceedings of IEEE ICOIN-9, December 1994, pp. 49–54.

6. Kurita, T.; Kato, T.; Fukuda, I.; and Sakakura, A. Sense retrieval on image database of full color paintings. Transactions of IPSJ, 33, 11 (1992), 1373–1383 [in Japanese].

7. Shibata, Y., and Katsumoto, M. Dynamic hypertext and knowledge agent systems for multimedia information networks. Proceedings of ACM Hypertext '93, November 1993, pp. 82–93.

8. Wilbur, S., and Bacarise, B. Building distributed systems with remote procedure call. Software Engineering Journal (1987), 148–159.

9. IXLA Reference Manual. Tokyo: ISR Japan Inc., 1996.
