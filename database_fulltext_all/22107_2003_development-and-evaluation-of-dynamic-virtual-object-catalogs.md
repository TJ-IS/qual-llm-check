---
otero_id: 22107
otero_key: "AHGZT3PD"
title: "Development and evaluation of dynamic virtual object catalogs"
authors: "Benjamin P.-C. Yen; Kenny Y.M. Ng"
year: "2003"
journal: "Information & Management"
doi: "10.1016/s0378-7206(02)00016-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Development and evaluation of dynamic virtual object catalogs

Benjamin P.-C. Yen $^{*}$ , Kenny Y.M. Ng

School of Business, The University of Hong Kong, Pokfulam Road, Hong Kong, PR China

Received 1 October 2000; accepted 10 November 2001

## Abstract

One of the most interesting commercial opportunities for Internet business is the ability to deploy catalogs on the Web. Existing electronic catalogs are able to provide comprehensive information, efficient data update, and economical development; however, the huge data volume due to high variety and fast turnover of customized products often causes their construction and maintenance to be unrealistic. This paper presents a Web-based dynamic virtual object catalog of customized products for Internet commerce and focuses on the comparison of system performance for various catalogs in different perspectives. The results show that the proposed catalog has tremendous advantages in development time, required cost, and storage space over existing catalogs under most conditions.

© 2002 Elsevier Science B.V. All rights reserved.

Keywords: Electronic catalog; Web-based information visualization; Performance evaluation; Customization; Virtual reality

## 1. Introduction

More and more products are “made by users” nowadays, as customers are gradually involved in defining the size, shape, color, need, and other design parameters of products $[26]$ . On the other hand, customers have increasing demand for high quality customized products at decreasing price levels $[44]$ . In order to satisfy customer needs, mass customization could provide each individual customer with a tailor-made product based on his/her requirements $[14]$ , but may not be always a premier way to deliver variety to the products $[50]$ . Mass customization resembles the traditional way of production in terms of manufacturing standard products, holding the finished goods in inventory, and filling orders in a leisurely manner [30]. This aims at providing products and services at an affordable cost with near mass production efficiency and effectiveness, based on needs of customers [38].

Much research has been carried out in the field of mass customization, ranging from product design $[17]$ to system implementation $[1]$ ; however, there is a lack of studies on information management on the Internet. The framework for value networks suggested by Haglind and Helander $[24]$ provided the management of product information and services personalized for an individual customer, but it is restricted to networked organizations with interconnection. The management of customized product information between clients (e.g. electronic catalogs) and a server on the Internet, which is very important in the information era, has been overlooked by many researchers.

Internet technology for information processing of production has been used in communication infrastructure for sourcing [47], CAD/CAM [29,42], production planning and scheduling [46], simulation [18], product promotion [10,41], and product design [27]. Daflucas [11] drew attention to the importance of the Internet as a successful road to mass customization. Helander et al. further pointed out that the supportive functions provided by Web technology facilitated interactive communication between customers or designers and manufacturers. Such interaction could help the customers personalize their product information via Web pages. Consequently, digitization of product information is essential to effective and efficient management of information on an electronic catalog.

To retain the potency of mass customization and avoid wasting resources, a creative approach to a Web-based dynamic virtual object catalog has been proposed $[48]$ . The framework includes both a front-end interface for the user to view the customized product instantaneously in ‘Virtual Reality Modeling Language’ (VRML) models and a back-end server that generates dynamic Web pages and VRML models according to his/her preferences. Based on prior research, this paper aims at the system evaluation of a Web-based dynamic virtual object catalog for customized products in Internet commerce.

## 2. Current customizable catalogs

Electronic commerce helps the convergence of text, data, hologram, images, graphics, audio, full-motion video, and animation in an easy way $[28]$ . With these features, many developers start to build and publish electronic catalogs to adapt to the shift of consumer behavior. However, a main misconception about electronic publishing is that its value lies in the ability to disseminate digital information over computer networks in a manner analogous to physical distribution of hard copy $[5]$ . Gosalvez $[23]$ , therefore, suggested several main performance features from both seller and buyer perspectives, that should be offered by current electronic catalogs. Unfortunately, the ability of electronic catalogs to customize Web content and product information has been overlooked. This ability to personalize, argued by Luedi $[33]$ , is the only way to create customer loyalty and generate repeated visits to Web sites.

Electronic catalogs provide the main entry point for electronic commerce and will fundamentally transform supply-chain relationship [4]. To cope with the market changes and needs, SAQQARA [40] has developed a component-based online catalog for customers to select and configure products effortlessly. Ginsburg et al. [21] also suggested ways to manage the information of multi-vendor electronic catalogs in supporting procurement. Yet such catalogs act as a search engine rather than a customization mechanism for product images. Mattel [3], a doll manufacturer, has successfully implanted functions to personalize the Barbie's appearance for electronic commerce. Customers can set their preferences for attributes (such as face color, eyes, and hairstyle) and view the product on the screen. The image-based customizable catalog with a generic method to organize the information of customized products is shown in Fig. 1 (top). This approach would not be applicable to products with a greater number of attributes; nevertheless, it is seldom realistic due to the needs of longer development time, higher initial cost, and larger storage space for servers.

It is improvident and unrealistic to store and manage image-based catalogs when there are a wide variety of design parameters (such as color and texture) of products. For instance, if there are three parameters in total and three possible choices for each parameter, it requires $3 \times 3 \times 3 = 27$ product images, but if a new parameter with three attributes is added to the group, the developers need to generate 81 images. Nonetheless, if the media images and objects can be generated dynamically by superimposition of images to models, then only $3 + 3 + 3 = 9$ components are needed. Such difference in overhead increases exponentially when the number of parameters and the number of possible choices increases. The main issue of the problem lies in its management information system. The traditional catalog is a dynamic-static catalog (dynamic generation and static management) while the proposed catalog is a dynamic-dynamic catalog (dynamic generation and dynamic management).

## 3. An overview of dynamic virtual object catalogs

A well-defined business process of electronic commerce involves three phases: pre-purchase interaction, purchase consummation, and post-purchase

![](/api/attachments/AHGZT3PD/fulltext/images/8e32680caa8eb8fedcc89635efd0b9474eacbff4672824bf3afffbfa806f3c7b.jpg)

At the beginning, the product selection interface allows customers to configure their products. After choosing the design parameters by the customers, corresponding pre-made image file of the object is retrieved from the storage and posted on a product presentation interface, which the image is in static form. From its physical properties, the catalog is defined as dynamic-static catalog.

Our proposed method is to retrieve the corresponding individual image files of the selected attributes from the file server, and then combined them together to form an object. The difference between the current and previous catalog is that the object is dynamically generated out from a process instead of retrieving a static image of the object from the storage. This catalog is defined as dynamic-dynamic catalog.

Fig. 1. A comparison between the traditional method (top) and the neotetric approach (bottom) to generate electronic catalogs.

interaction. The design and implementation of electronic catalogs mainly focuses on the issues conforming to the phase of pre-purchase interaction. The catalog in the prototype system includes user interfaces for selecting design attributes and browsing through an interactive 3D environment. A catalog of electronic/virtual pets is chosen as an example.

## 3.1. System design

The Internet provides a user with publishing media, an environment to access and manage the product information. A typical functional process includes a selection stage and a presentation stage. The product selection stage concerns user input of design attributes, while the product presentation stage involves the display of an object contour. The design requirements may be categorized into following five aspects:

\- Functionality and modularity: The proposed electronic catalogs should support dynamic classification and 3D virtual object generation functions and provide an environment for users to select design parameters and view a 3D virtual appearance.

\- Extendibility and maintainability: Dynamic catalogs should be flexible enough for the company to maintain and upgrade Web templates and databases. The company modifies the related databases on Web pages without changing the templates. On the other hand, if the company wants to update the Web pages, data is brought up to date in the renewal processes.

\- Usability and operability: Electronic catalogs with 3D display utility should be user friendly and operable. Potential users do not need to possess prior computer and programming knowledge to surf the Web or try out catalogs [15,34,36].

\- Availability and accessibility: Due to global competition, electronic catalogs need to be accessible and available anytime and anywhere on the Internet. Mirror sites as backup servers enhance their availability.

\- Inter-operability and compatibility: Industrial standard formats for 3D modeling, such as ‘Initial Graphics Exchange Specification’ (IGES) [49] and ‘Data Exchange File’ (DXF) [16] are adopted in 3D virtual objects information exchange among CAD/CAM software; this guarantees compatibility and performance.

## 3.2. System architecture

The overall client/server architecture of a Web-based dynamic virtual object catalog is based on a three-tier architecture consisting of: user interface layer, business logic layer (functional layer), and data access layer (see Fig. 2). The catalog system consists of two major parts: server and clients. The server includes a file, database, and Web server. In addition, it is equipped with a dynamic Web page generator and a 3D virtual object generator. The file server contains pre-made HTML templates for Web pages formation and 3D object files (e.g. VRML files) for 3D modeling. Information about the Web pages and design parameters of products is stored in the database server.

![](/api/attachments/AHGZT3PD/fulltext/images/92de70de1c7ac2e401dd67a93a8b0b7730d85b9b5e9b4c87bb479bbfb182dc01.jpg)  
Fig. 2. Web-based client/server architecture for customized product.

## 3.3. System components

A dynamic virtual object catalog is a compound of four strongly affiliated components that may be grouped and identified in three layers, as shown in Fig. 2.

\- Web and VRML browsers support the interaction channel between clients and Web server to provide users with quick, smooth, and friendly communication interfaces. Web browsers (such as Netscape Navigator or Internet Explorer) mainly interpret HTML descriptions, while VRML browsers, such as Silicon Graphic Cosmo Player [12], convert VRML description into 3D VRML models.

\- Common Gateway Interface (CGI) programs, embedded in host languages (such as Visual Basic and C/C++), function as interfaces between Web servers and applications. The process is sequenced as a flow in which CGI programs connect applications to databases for the queries from clients, return the result from applications to Web servers, and in turn forward it to clients [19].

\- Database systems are normally located in physical servers to store, retrieve, update, and track the data in the information flow between servers and clients.

\- Styling templates are pre-defined HTML meta documents. The object files are VRML descriptions generated by 3D modeling software, such as 3D Studio Max 2, with some of the tags/scripts in the documents/files left empty. These templates/files are further modified to Web pages/3D virtual objects by filling in the empty tags/scripts with an executable program such as CGI.

## 3.4. System functions and process flows

The intercommunication through the CGI programs between a client and a server of the Virtual Market on the Net $[45]$ is illustrated in Fig. 3. It also shows the functional process flow of dynamic virtual object catalogs from product selection to product presentation. Fig. 4 demonstrates a real-time generation of a customized 3D electronic pet model on the Cosmo Player platform. Buyers use the system to choose attributes of an electronic pet for customizing products and to view them in an interactive 3D display. The design parameters of a virtual pet are presented as a hierarchy: case shape, case material, texture/color of the upper case, nature of pets, button shape, button color, and texture/color of the lower case (see Fig. 5).

![](/api/attachments/AHGZT3PD/fulltext/images/01b4913f9286fb62bc18c09e6a9ed73c160ad76ca08b381e12ba2749ad39c705.jpg)  
Fig. 3. Information flow from product selection to product presentation stage.

## 4. Performance evaluation and comparison

Instead of measuring the subjective user satisfaction through survey $[2,9]$ , this paper focuses on the feasibility of applying objective measurable indices to performance evaluation. The assessment is based on the properties of dynamic, online, and 3D presentation modes and is carried out from two viewpoints: the company and the user.

## 4.1. Definition

From the perspective of the company, the cost involves the development and investment of the dynamic virtual object catalog. This is intended to save a company (such as AMP) more than one-fifth of the traditional printing cost annually $[31]$ , and/or to increase the sales by 437% $[22]$ . In addition, storage space should be considered when the company is using a Web hosting package with limited storage space. According to the Web hosting company, NetSource One [35], the maximum disk storage package offered by the company is, at most, 300MB. From the perspective of the user, page-loading time is one of the most important factors [20,37].

\- Development time is the time needed to create a catalog throughout the stages of design, creation, and installation.

\- Required cost is the total cost. The costs are measured in accordance with the ‘Web Price Index’ (WPI) of Business Marketing Online [7] in money per hour.

\- Storage space is the required disk space needed for a well-designed electronic catalog to function. The storage of a dynamic virtual object catalog, to be specific, is defined as the sum of file sizes of all the mentioned system components (expect Web/VRML browser) required for its virtual model formulation.

![](/api/attachments/AHGZT3PD/fulltext/images/e3279209cc2e7c9062c1e9689b17c9c762f8aaa29ff35d835cfbfaae00642fa2.jpg)  
Fig. 4. Virtual bird—a customized electronic pet.

![](/api/attachments/AHGZT3PD/fulltext/images/787dd3443f2dbecf96a38c8d97a973ecd6b5f100e196aaa5f75ddfb9684ce94b.jpg)  
- 5 textures: Color wave, blue shock, maple, sunflower, tulip  
- 5 colors: Red, blue, pink, yellow, silver

Fig. 5. Hierarchical order of design attributes.

\- Page-loading time is the time between click of the hyperlink and full display on the screen. Physically, it includes the time for file transfer from a server to a client, posting material on the interface and loading a plug-in program (if necessary) to the Web browser.

## 4.2. Methodology

## 4.2.1. System configurations

Experiments were conducted on a Pentium II 400 MHz server with 128MB RAM, and a Pentium 200 MHz with 32MB RAM client connected with a normal 10Mbit LAN and a standard 33.6 kbps modem. Netscape Navigator 4.6 and Silicon Graphic Cosmo Player 2.1 were used for browsing HTML documents and VRML files, respectively.

## 4.2.2. Experimental materials

Electronic pets in 2D images and 3D VRML models, as illustrated in Table 1, were used in the evaluation of system performance. JPEG and GIF were the image formats put to use in the evaluation [6]. JPEG images are stored in a high quality resolution of standard baseline format, while GIF images are stored in an adaptive palette with 256 colors. VRML 2.0 was used as the standard for modeling 3D virtual objects. The object files with common components (such as textures, database, and the 3D object generator) were used to generate 3D virtual objects, and it should be noticed that the individual object is composed of a VRML model and texture-mapped image(s), excluding the database and object generator. The total storage requirement of our prototype system is 757KB, including three basic virtual pet models (ranging 65 to 416KB), five texture images of 10KB each, three pet textures of 1KB each, an object generator of 29KB, and a database of 104KB.

## 4.2.3. Analytic comparison

The development time, required cost and storage space are compared in pairs of properties (dynamic versus static, online versus offline, and 3D versus 2D display) to form a set based on the circular case virtual pet. For example, a set in the dynamic virtual object catalog includes an object file (circular case), a generator, a database, and eight texture-mapped images (three pet and five case textures). Referring to the hierarchical structure of the virtual pet shown in Fig. 5, a set of 2D images or static virtual object catalog that is in the circular case has 6000 combinations.

## 4.2.4. Measuring procedure

The page-loading time is one of the major performance indices, and it may be compared individually, i.e. an image versus a 3D model. The administrator is required to measure ten runs of the page-loading time and then take the average as the quantitative performance index. In measuring the page-loading time, the plug-in program should be pre-loaded on the browser at the beginning. In addition, to avoid recalling frequently accessed documents in the local drive, a memory cache of the browser is set to zero to ensure the page-loading time strictly depended on the network computer rather than a local computer.

Experimental materials used in the evaluation  
![](/api/attachments/AHGZT3PD/fulltext/images/dec37b791c6f22a16122ada85036a0043ef2ae75a17aea6448db775e8679fb5b.jpg)  
$^{a}$ Storage space including a VRML model, texture-mapped image(s), a database and an object generator.

## 4.3. Static versus dynamic catalog

A set of 3D virtual pets of circular case was used as an example for the evaluation. The main components of the static virtual object catalog are generated VRML models with texture-mapped images, while the dynamic virtual object catalog consists of unassembled VRML sub-models, texture-mapped images, a database and a virtual object generator.

## 4.3.1. Development time

Since both static and dynamic catalogs share the same processes in the design and installation stage (due to the same type of medium), the development time is enumerated only at the creation stage. It takes about 1 h, on average, for VRML model construction using CAD or 3D modeling software. The created model can be modified to another model in 5 min just by editing some of its values, properties and paths. There are a total of 6000 combinations, and if one model is constructed, there are still 5999 models left for modification. Another component, the texture-mapped images, requires about 5 min effort for each creation. Hence, the total time required to develop a whole set of static models is 502 h. The time needed to create a database and write an object generator is about 16 and 40 h, respectively; thus, the construction of a dynamic model, a database, and an object generator takes only 57.5 h, and this saves about 89% of the total development time.

Although the dynamic catalog is superior to a static catalog in terms of a set of virtual pets with 6000 combinations, what would happen with a catalog having fewer combinations? Would a dynamic catalog still be better? A similar case, but not targeting to intangible digital information, Dewan et al. [13] concerned the balance between the degree of customization and the pricing strategies for tangible customized products. Based on Table 2, the crossover point for the number of combinations is 670—the break-even point of the two catalogs.

Table 2  
Comparison between a static and dynamic virtual object catalog

<table><tr><td></td><td>Static</td><td>Dynamic</td></tr><tr><td>Development time</td><td>502 h</td><td>57.5 h</td></tr><tr><td>First model</td><td>1 × 1 h</td><td>1 × 1 h</td></tr><tr><td>Leftover models</td><td>5999 × 5 min</td><td>NA</td></tr><tr><td>Texture of pet</td><td>3 × 5 min</td><td>3 × 5 min</td></tr><tr><td>Texture of body</td><td>5 × 5 min</td><td>5 × 5 min</td></tr><tr><td>Database</td><td>NA</td><td>1 × 16 h</td></tr><tr><td>Object generator</td><td>NA</td><td>1 × 40 h</td></tr><tr><td>Required cost</td><td>US$ 55,300</td><td>US$ 9500</td></tr><tr><td>First model</td><td>US$ 200 × 1 h</td><td>US$ 200 × 1 h</td></tr><tr><td>Leftover models</td><td>US$ 110 × 500 h</td><td>NA</td></tr><tr><td>Textures</td><td>US$ 140 × 0.67 h</td><td>US$ 140 × 0.67 h</td></tr><tr><td>Database</td><td>NA</td><td>US$ 200 × 16 h</td></tr><tr><td>Object generator</td><td>NA</td><td>US$ 150 × 40 h</td></tr><tr><td>Storage space</td><td>2497MB</td><td>600KB</td></tr><tr><td>Basic virtual model</td><td>6K × 416KB</td><td>416KB</td></tr><tr><td>Texture of pet</td><td>5 × 1KB</td><td>3 × 1KB</td></tr><tr><td>Texture of body</td><td>5 × 10KB</td><td>5 × 10KB</td></tr><tr><td>Database</td><td>NA</td><td>104KB</td></tr><tr><td>Object generator</td><td>NA</td><td>29KB</td></tr><tr><td colspan="3">Page-loading time</td></tr><tr><td>10Mbit LAN</td><td>10.8 s</td><td>10.9 s</td></tr><tr><td>33.6 kbps modem</td><td>36.4 s</td><td>37.4 s</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Break-even point analysis $^{a}$ 

Development time

1.67 h + (y - 1) h/12 = 57.5 h
y = 670.960
y = 670 (possible combination)

Required cost

US 295 + US 110(y - 1)/12 = US 9500
y = 1005.182
y = 1004

Storage space $^{a}$ 

469KB + (y - 1) × 416KB = 600KB
y = 1.315
y = 1
</div>

$^{a}$ Remark: y is a variable, which represents the maximum possible number of combinations.

## 4.3.2. Required cost

Based on WPI, we assumed that the creation and modification of a VRML model cost US\$ 200 and 110 per h, respectively. The rate for image textures production is assumed to be US\$ 140 per h. Then the total cost of a set of static models is US\$ 55,300. A dynamic catalog, with no matter how many combinations of attributes or elements, needs only one VRML model in addition to an object generator and a database. The total cost for this component series is, therefore, US\$ 9500, and this saves almost 83% of the total required cost. The break-even point (see Table 2) has a maximum possible number of combinations of 1004.

## 4.3.3. Storage space

A virtual pet is composed of seven attributes and there are 6000 possible combinations in total, for a set of 3D virtual pets of circular case. If an object file takes about 416KB of disk space, then the static catalog takes about 2496MB plus 51KB for texture-mapped images. A dynamic catalog, on the other hand, takes only 600KB (including the texture-mapped images for case and pet, database and object generator). This saves almost 99.98% of the total storage space. Moreover, analysis shows that the break-even point of the static and dynamic catalog is no more than two.

## 4.3.4. Page-loading time

The page-loading time of static and dynamic objects on a normal LAN is 10.8 and 10.9 s, respectively. Based on the t-test (p = 0.77), it was found that there is no significant difference between the page-loading time of static objects and dynamic objects on a normal LAN. Similarly, there is no difference between the page-loading times of static and dynamic objects on a modem (p = 0.64).

## 4.4. Offline versus online catalog

A set of virtual pets of circular case was chosen again as an example for a comparison of development time and cost evaluation between a paper-based and dynamic virtual object catalog (see Table 3). Normally, the production process of a paper-based catalog involves the process from the preparation to creation stage. The process begins with digitizing the products to images with a digital camera, organizing the data with a word processor or equivalent software, and printing the high quality paper-based catalogs using a commercial offset printing press, such as a five-color Heidelberg printing machine [25]. On the other hand, a dynamic virtual object catalog evolves from its creation to installation stage.

Comparison between a paper-based and dynamic virtual object catalog

<table><tr><td></td><td>Paper-based</td><td>Virtual object</td></tr><tr><td>Development time</td><td>126 h</td><td>61.5 h</td></tr><tr><td>Basic time</td><td>NA</td><td>57.5 h</td></tr><tr><td>HTML page</td><td>NA</td><td> $1 \times 2$  h</td></tr><tr><td>Server setup</td><td>NA</td><td>2 h</td></tr><tr><td>Digitizing</td><td>6K  $\times$  0.5 min</td><td>NA</td></tr><tr><td>Cataloging</td><td>600  $\times$  3 min</td><td>NA</td></tr><tr><td>Printing</td><td>1.5 Mh/6000</td><td>NA</td></tr><tr><td>Overheads</td><td>250  $\times$  5 min</td><td>NA</td></tr><tr><td>Required cost</td><td>US$ 104,050</td><td>US$ 10,370</td></tr><tr><td>Basic cost</td><td>NA</td><td>US$ 9500</td></tr><tr><td>HTML page</td><td>NA</td><td>US$ 110  $\times$  2 h</td></tr><tr><td>ISP cost per year</td><td>NA</td><td>US$ 50  $\times$  12 + 50</td></tr><tr><td>Digitizing</td><td>US$ 110  $\times$  50 h</td><td>NA</td></tr><tr><td>Cataloging</td><td>US$ 110  $\times$  30 h</td><td>NA</td></tr><tr><td>Printing &amp; others</td><td>US$ 359  $\times$  250</td><td>NA</td></tr><tr><td>Storage space</td><td>Incomparable</td><td></td></tr><tr><td>Page-loading time</td><td>Incomparable</td><td></td></tr><tr><td colspan="3">Printing price (for 250 catalogs) $^{a}$ </td></tr><tr><td>Pages</td><td>Cost (US$)</td><td></td></tr><tr><td>8</td><td>1206.0</td><td></td></tr><tr><td>12</td><td>1804.5</td><td></td></tr><tr><td>16</td><td>2403.0</td><td></td></tr><tr><td>20</td><td>3001.5</td><td></td></tr><tr><td>24</td><td>3608.0</td><td></td></tr><tr><td>28</td><td>4198.5</td><td></td></tr><tr><td>32</td><td>4797.0</td><td></td></tr><tr><td>600</td><td>?</td><td></td></tr></table>

Break-even point analysis $^{b}$  
Required cost  
US\$ 104,050y/250 = 10,379  
$y = 24.936$  
y = 24  
$^{a}$ An incremental increase of four pages increases the printing costs by US 598.5. Therefore, the formula is: printing cost = 1206 + 598.5(y - 8)/4, where y is the number of pages, and $\geq$ 8.  
$^{b}$ Remark: y is a variable, which represents the number of catalogs to be given out or the number of people has accessed the Web site.

## 4.4.1. Development time

The total development time of a dynamic catalog is 61.5 h in which 2 h are spent for server setup, 2 h for one HTML page (the front page), 1 h for the VRML model, and 56.5 h for CGI programming, database, and texture-mapped images. For a paper-based catalog, it is assumed that the process of digitizing a product and downloading an image to local computer takes 0.5 min per item. It is also assumed that the cataloging is done by inserting 10 images with corresponding descriptions in one A4 or 'letter' size paper, taking about 3 min per page. As there are 6000 combinations for each set, 600 pages (or 300 sheets) are needed. Moreover, in order to produce paper catalogs of the same imaging quality as the electronic ones, a commercial offset printing press should be adopted. The average printing speed of the press is usually 6000 sheets (one-side) per h (see Heidelberg Web page). Furthermore, overhead, such as binding the paper catalogs, is assumed to take 5 min per catalog. Thus, the total time of producing 250 copies of a catalog is almost 126 h, and this is about twice the total time of producing a corresponding dynamic catalog.

## 4.4.2. Required cost

Assume that 250 copies of paper catalogs are required with a life-cycle of 1 year, and that the cost of a Web hosting (such as NetSource One) is about US\$ 650 per year, including the setup fee of US\$ 50. In addition, a Web page costs US\$ 110, a virtual object costs US\$ 200, texture-mapped images and an object generator with a database cost US\$ 9300. Therefore, the total cost of a dynamic catalog is US\$ 10,370. PrintingForLess.com [39] shows that 250 copies of paper catalog on #2 grade 80 lb gloss paper with overheads (collating and stapling) and shipment within the tenth business day would cost US\$ 89,750 (see Table 3 for more details on this calculation). In addition to printing, it is assumed that the digitizing and cataloging process follows the rate of designing a Web page, i.e. US\$ 110 per h. For that reason, the total cost of the paper catalog is US\$ 104,050, which is 90% more expensive than the dynamic catalog. If we assume that there are no fixed costs for producing paper catalogs, we find that the two costs meet at the point of 24 (see Table 3).

## 4.5. 2D versus 3D presentation catalog

This evaluation was carried out on a set of circular case virtual pets of 2D images and 3D models (see Table 4). The production process for an image-based catalog is almost the same as that for a paper catalog. The only difference is that instead of printing the catalog, it is published on the Web site.

Table 4
Comparison between an image-based and dynamic virtual object catalog

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Image-based $^{a}$ Virtual object
Development time 80 h 61.5 h
Basic time NA 57.5 h
HTML page NA 1 × 2 h
Digitizing 6K × 0.5 min NA
Cataloging 600 × 3 min NA
Required cost US 8800 US 9750
Basic cost NA US 9500
HTML page NA US 110 × 2 h
Digitizing US 110 × 50 h NA
Cataloging US 110 × 30 h NA
Storage space 114MB 710KB
Basic space NA 600KB
HTML page 20KB × 600 20KB
Digital image 17KB × 6000 90KB
Page-loading time
10Mbit LAN 1 s 10.9 s
33.6 kbps modem 5 s 37.4 s
Break-even point analysis $^{b}$
Development time
(80 h/6000)y = 61.5 h
y = 4612.5
y = 4612 (possible combination)
Required cost
(US 8000/6000)y = US 9750
y = 6647.727
y = 6646
Storage space
(114,000KB/6000)y = 710KB
y = 37.368
y = 36
</div>

$^{a}$ The digital images are stored in JPEG format of virtual bird.  
$^{b}$ Remark: y is a variable, which represents the maximum possible number of combinations.

## 4.5.1. Development time

The digitizing, downloading and cataloging process takes 30 s per product and 3 min per page, respectively. Assume that a Web page editor is used in the cataloging process with 10 product images and descriptions arranged on a page. Then, 600 pages require 80 h for the image-based catalog and 61.5 h for the dynamic virtual object catalog production. The proposed catalog saves no more than 23% of the total development time of an image-based catalog. Again, under the assumption of no setup time for the development of image-based catalog, the break-even point (or maximum possible number of combinations) of these two catalogs occurs at 4612 combinations.

## 4.5.2. Required cost

According to Carmichael, the hourly rate for designing a Web page is about US\$ 110. Using this for digitizing and cataloging, if the total production time of an image-based catalog is 80 h, then the total cost is about US\$ 8800. Conversely, the dynamic catalog costs about US\$ 9720. The amount of these two costs is more or less the same as for the image-based catalog. Moreover, with the no fixed cost assumption, the break-even point is 6646 combinations.

## 4.5.3. Storage space

As Table 1 shows, different patterns and formats of an image may lead to different file sizes. For example, a virtual bird in GIF and JPEG format takes 6 and 14KB, respectively. The virtual bird and virtual cat with texture have different file sizes. Therefore, we selected JPEG images in the evaluation, since the storage space of this format depends more on the image size (not on the colors pallet). If a HTML page takes 20KB and a JPEG image takes on average 17KB, then the total storage space of an image-based catalog is 114MB. The dynamic catalog takes only 710KB of storage space: 600KB for the basic model (including an object file and generator, a database and set of texture-mapped images), 20KB for the front page, and 90KB for the images. This saves almost 99% of the total storage space. Also, with break-even point analysis, the maximum number of combinations is 36.

## 4.5.4. Page-loading time

Without using any statistical techniques, it can be seen that the page-loading time on a normal 10Mbit LAN is significantly shorter than on a standard modem. Also, the page-loading time for a 3D object is significantly longer than a 2D image. It is, therefore, reasonable that the 3D object has a longer page-loading time.

## 5. Limitations and discussion

This study has a number of limitations. First, all evaluations are based on a set of virtual pets of circular case. Each object file occupies 416KB of the storage space, which is the largest value between square and triangular cases. Therefore, the total storage space and maximum possible number of combinations may vary. For example, if the comparison is on the basis of a set of triangular case virtual pets (65KB), the ratio between the storage space of static and dynamic catalogs will be decreased.

The second limitation is that not all of the page-loading times of 3D virtual pets are the same. Normally, the page-loading time of a 3D virtual object should be directly proportional to the file size. It can be concluded accordingly that the page-loading time will also vary.

The last limitation is that the study is only good as a reference. The major considerations are the development time, required cost, storage space, and page-loading time, and these variables have no fixed value, so that two identical prototype systems may produce two different results, because different people have different ways to accomplish their tasks, different countries or companies may have different paying rates, different software may have different ways to generate the images and models, and different networks may have different traffic.

## 6. Conclusions

This paper shows the results of implementing and evaluating a Web-based dynamic virtual object catalog of customized products. The prototype system indicates the feasibility of setting up the proposed catalog within the current technologies and infrastructures and demonstrates the advantages of using a real-time dynamic approach to display 3D virtual customized products. In addition, a dynamic virtual object catalog could be updated effectively by editing the corresponding Web content, product information, image(s), and/or model(s) in the database and file server. That is, the dynamic property provides quick and easy maintenance.

However, one should understand that the evaluation is only one of many factors affecting the selection of catalog types. Other factors may include spatial arrangement and various kinds of display features or print styles, such as color, font size, and style of characters. Despite the textual arrangement and display in electronic catalogs, there is also a crucial need to explore and understand the user perception of the powerful means of multimedia in, for example, first impression bias [32], information presentation [43], and impact on online shopping [8].

## Acknowledgements

This research was partially sponsored by Taran Eastman Publishing Ltd. under Grant TEIL 99/00.EG01.

## References

[1] D. Alford, P. Sackett, G. Nelder, Mass customization—an automotive perspective, International Journal of Production Economics 65 (1), 2000, pp. 99–110.

[2] J. Ang, P.H. Soh, User information satisfaction, job satisfaction and computer background: an exploratory study, Information and Management 32 (5), 1997, pp. 255–266.

[3] Barbie, http://www.barbie.com/, 5 January 2000.

[4] P. Baron, M.J. Shaw, A.D. Bailey Jr., Web-based e-catalog systems in B2B procurement, Communications of the ACM 43 (5), 2000, pp. 93–100.

[5] H. Berghel, Value-added publishing, Communications of the ACM 42 (1), 1999, pp. 19–23.

[6] H.E. Burdick, Digital Imaging: Theory and Applications, McGraw-Hill, NY, 1997.

[7] M. Carmichael, The Web Price Index (WPI) rate card, Advertising Age's Business Marketing Online, http://www.netb2b.com/cgibin/netb2b/article.pl?id=1385, 10 January 2000.

[8] P.Y.K. Chau, G. Au, K.Y. Tam, Impact of information presentation modes on online shopping: an empirical evaluation of a broadband interactive shopping service, Journal of Organizational Computing and Electronic Commerce 10 (1), 2000, pp. 1–22.

[9] L.-D. Chen, K.S. Soliman, E. Mao, M.N. Frolick, Measuring user satisfaction with data warehouse: an exploratory study, Information and Management 37 (3), 2000, pp. 103–159.

[10] Citizen, http://www.citizen.com.sg/, 17 June 2000.

[11] M. Daflucas, Road to mass customization, Industrial Computing 17 (3), 1998, pp. 16–19.

[12] J. December, M. Ginsburg, HTML 3.2 and CGI Professional Reference Edition Unleashed, Sams.net Publishing, IN, 1996.

[13] R. Dewan, B. Jing, A. Seidmann, Adoption of Internet-based product customization and pricing strategies, Journal of Management Information Systems 17 (2), 2000, pp. 9–28.

[14] M.A. Eastwood, Implementing mass customization, Computers in Industry 30 (3), 1996, pp. 171–174.

[15] R.E. Eberts, User Interface Design, Prentice-Hall, NJ, 1994.

[16] S. Elloit, F. Miller, J. Adouaf, D. Espinosa-Aguilar, S. Alexander, D. Barnard, P. Kakert, D. Kalwick, K. Kelm, M. Koch, M. Williamson, Inside 3D Studio Max 2, Vol. 1, New Riders Publishing, IN, 1998.

[17] E. Feitzinger, H.L. Lee, Mass customization at Hewlett-Packard: the power of postponement, Harvard Business Review 1/2, 1997, pp. 116–121.

[18] P.A. Fishwick, Web-based simulation: some personal observations, in: Proceedings of the 1996 Winter Simulation Conference, San Diego, CA, 1996, pp. 772–779.

[19] C. Franklin, Visual Basic 6.0 Internet Programming, Wiley, NY, 1998.

[20] D. Gehrke, E. Turban, Determinants of successful Website design: relative importance and recommendations for effectiveness, in: Proceedings of the 32nd Hawaii International Conference on System Sciences, Hawaii, 1999 (Abstract from CD-ROM).

[21] M. Ginsburg, J. Gebauer, A. Segev, Multi-vendor electronic catalogs to support procurement: current practice and future directions, in: Proceedings of the 12th International Bled Electronic Commerce Conference, Bled, Slovenia, 1999.

[22] L. Goff, The sharper image, Catalog Age, August 1999, pp. S15–S16.

[23] M.G. Gosalvez, Electronic product catalogues: what is missing? International Journal of Electronic Markets 7 (3), 1997, pp. 3–5.

[24] M. Haglind, J. Helander, Development of value networks—an empirical study of networking in Swedish manufacturing industries, in: Proceedings of the International Conference on Engineering and Technology Management, NY, 1998, pp. 350–358.

[25] Heidelderger, http://www.heidelberg.com/, 6 July 2000.

[26] M.G. Helander, H.M. Khalid, M.M. Tseng, Mapping customer needs in Web-based DIY design of consumer products, in: Proceedings of the 3rd Annual International Conference on Industrial Engineering Theories, Applications and Practice, Hong Kong, 1998 (Abstract from CD-ROM: PN256.pdf).

[27] G.Q. Huang, K.L. Mak, Design for manufacture and assembly on the Internet, Computers in Industry 38 (1), 1999, pp. 17–30.

[28] R. Kalakota, A.B. Whinston, Frontiers of Electronic Commerce, Addison-Wesley, Reading, MA, 1996.

[29] Y.C. Kao, G.C. Lin, CAD/CAM collaboration and remote machining, Computer Integrated Manufacturing Systems 9(3), 1996, pp. 149–160.

[30] W.R. King, IT-enhanced productivity and profitability, Information System Management 15 (3), 1998, pp. 70–72.

[31] D. Kosiur, Understanding Electronic Commerce, Microsoft Press, Redmond, 1997.

[32] K.H. Lim, I. Benbasat, L.M. Ward, The role of multimedia in changing first impression bias, Information Systems Research 11 (2), 2000, pp. 115–136.

[33] A.F. Luedi, Personalize or perish, International Journal of Electronic Markets 7 (3), 1997, pp. 22–25.

[34] A. Marcus, History lesson: the Web discover user interface design, in: Proceedings of the 7th International Conference on Human Computer Interface, San Francisco, 1997.

[35] NetSource One, http://www.nsone.net/hosting/plans.htm, 7 July 2000.

[36] J. Nielsen, Usability Engineering, Academic Press, Boston, 1993.

[37] J. Nielsen, Top 10 mistakes in Web design, Alertbox, http://www.useit.com/alertbox/9605.html, 10 February 2000.

[38] B.J. Pine II, Mass customization: the new frontier in business competition, Harvard Business School Press, Boston, 1993.

[39] PrintingForLess.com, http://www.printingforless.com/, 15 February 2000.

[40] SAQQARA, http://www.saqqara.com/, 17 February 2000.

[41] Seiko, http://www.seiko-corp.co.jp/index\_e.html, 25 June 2000.

[42] C.S. Smith, P.K. Wright, Cybercut: a World Wide Web-based design-to-fabrication tool, Journal of Manufacturing System 15 (6), 1996, pp. 432–442.

[43] N. Tractinsky, J. Meyer, Chartjunk or goldgraph? Effects of presentation objectives and content desirability on information presentation, MIS Quarterly 23 (3), 1999, pp. 397–420.

[44] M. Tseng, J. Jiao, C.J. Su, Virtual prototyping for customized product development, Integrated Manufacturing Systems 9(6), 1998, pp. 334–343.

[45] Virtual Market on the Net, http://iez125.ieem.ust.hk/EC98/VRPET/, 25 June 1998.

[46] B.P.-C. Yen, Interactive scheduling agents on the Internet, in: Proceedings of the 30th Hawaii International Conference on System Sciences, Hawaii, 1997 (Abstract from CD-ROM).

[47] B.P.-C. Yen, C.J. Su, Information technology infrastructure for textile and apparel industry in Hong Kong, International Journal of Electronic Markets 7 (2), 1997, pp. 9–12.

[48] B.P.-C. Yen, K.Y.M. Ng, Web-based virtual reality catalog in electronic commerce, in: Proceedings of the 33rd Hawaii International Conference on System Sciences, Hawaii, 2000 (Abstract from CD-ROM: INMIW03.pdf).

[49] I. Zeid, CAD/CAM Theory and Practice, McGraw-Hill, Singapore, 1991.

[50] P. Zipkin, The limits of mass customization, MIT Sloan Management Review 42 (3), 2001, pp. 81–87.

![](/api/attachments/AHGZT3PD/fulltext/images/ea1fd94fdd3fe2d695bfa9674c2da68c27eaf27917e06a43c76d190810c75fc9.jpg)

Benjamin P.-C. Yen is an associate professor in the School of Business at the University of Hong Kong. He received his PhD degree in Industrial Engineering and Operations Research from Columbia University. His research interests include electronic catalogs in electronic commerce, IT-based supply-chain management, and Web information retrieval. Dr. Yen has collaborated with international companies in the US

and Asia, such as Siemens, Bell Labs, Daran Eastman, etc. He has papers published in major information system and operations research journals including Journal of Organizational Computing and Electronic Commerce, Electronic Commerce Research Journal, International Journal of Electronic Markets, Information Processing Letters, Annals of Operations Research, and European Journal of Operations Research, etc.

![](/api/attachments/AHGZT3PD/fulltext/images/d36d5923c7898dd3c30fc01e35177b5e3cff479f52611ad57525271da4b3d15c.jpg)

Kenny Y.M. Ng is currently working as a research assistant in the School of Business, The University of Hong Kong. He received both his BEng and MPhil degrees in Industrial Engineering and Engineering Management from the Hong Kong University of Science and Technology. His research interests include electronic commerce, electronic catalog, human-computer interaction, geographical information systems, and production management.
