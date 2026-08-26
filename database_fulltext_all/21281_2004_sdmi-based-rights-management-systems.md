---
otero_id: 21281
otero_key: "PUE97VUP"
title: "SDMI-based rights management systems"
authors: "S.H. Kwok; C.C. Yang; K.Y. Tam; Jason S.W. Wong"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00075-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# SDMI-based rights management systems

S.H. Kwok<sup>a,</sup>\*, C.C. Yang<sup>b</sup>, K.Y. Tam<sup>a</sup>, Jason S.W. Wong

<sup>a</sup> Department of Information and Systems Management, The Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong, China

<sup>b</sup> Department of Systems Engineering and Engineering Management, The Chinese University of Hong Kong, Shatin, New Territories, Hong Kong, China

Received 1 July 2000; accepted 1 March 2003 Available online 19 June 2003

## Abstract

Building digital rights management (DRM) systems for electronic commerce is still a complex task because such systems are usually required to manage a large set of different media contents, rights information, and enabling technologies. The Secure Digital Music Initiative (SDMI) was proposed to provide a secure environment in which rights management is performed for music distribution through the Internet. Rights management in SDMI is implemented by digital watermarking, but it is not the responsibility of SDMI to provide guidelines for the design of digital watermarks and to explore other potential benefits of using digital watermarks for the music distribution business. This paper fills this gap by proposing an SDMI-based rights management system. The proposed rights management system can support basic SDMI functions and non-SDMI features such as video. A prototype of the SDMI-based rights management system has been developed and the interfaces of the major components are presented.

Keywords: Rights management; Digital watermarking; Copyright protection; Intellectual property protection; Electronic commerce

## 1. Introduction

In the past decade, we witnessed an explosion in the distribution of digital media such as compact discs (CD-ROMs), digital video discs (DVDs), and digital television. Digital and peer-to-peer (P2P) technologies, for example Napster [5] and Gnutella [9], have also made duplicating and distributing illegal copies of copyright-protected material fast, easy, and cheap. Copyright protection and piracy have become the major problems in the music business. In order to combat the potentially disastrous losses to revenues in the music business, the major owners and distributors of copyrighted media contents, such as image libraries, the music and film industries, and online publishers, have sought ways to detect and prevent copyright infringement. Rights management has therefore become a very important concern to content providers to enable rights verification, ownership identification, copyright protection, and control of access rights. Rights management, in general, refers to the problems associated with intellectual property rights, including copyright protection and, in particular, to the problem of assuring that, in a commercial setting, payment is made for a particular use of content and that the actual use does not exceed the authorized use [18].

Cryptographic-based and watermark-based copyright protection schemes are two commonly used technologies for rights protection [13]. In this paper, we focus on watermark-based approach. Digital watermarking is regarded as a tool for rights management. Page [17] stated that digital watermarking as a form of rights management in the protection and authentication of digital images, audio, and video. Digital watermarking basically adds information that is normally invisible or barely visible to human eyes or inaudible or barely audible to human ears, but which can be detectable and extractable for identifying the authenticity or copyright owner of the media.

Until now, there has been no international standard to govern rights management or intellectual property protection in electronic commerce in specifically using digital watermarking. The literature suggests that electronic commerce applications and services have their own countermeasures, including rules, regulations, and approaches against copyright infringement, which means that their digital rights management (DRM) solutions could always be application- and business-dependent.

Digital Property Rights Infrastructure (DPRI) is a research project that specifically addresses copyright issues in music distribution. The project was conducted by a research team at the Hong Kong University of Science and Technology. It was funded by the Hong Kong SAR Government under the Industrial Support Fund (ISF) Scheme. The findings show that digital watermarking could benefit not only copyright management systems but also the broader rights management of electronic commerce systems, in particular, online media distribution [15,16] and electronic commerce [14]. The proposed rights management system in this paper is part of this project and we present some of the project findings in this paper.

Currently, there are some relevant commercial rights management solutions. They are reviewed here.

 Digimarck [7] is a digital watermarking technology that can be used on many digital visual contents, including image and video media. It provides visual content owners a range of solutions including copyright communication, image licensing and management, and enhanced Internet commerce.

These solutions are enabled by a set of digital watermarking tools that embed, read, and respond to the watermarks as they enable new communications capabilities within digital visual content.

The InterTrust Commerce Architecture [3], principally based on DigiBoxk secure containers, InterTrust Commerce Nodes, and a secure operating system layer extension, enables the creation of a globally distributed Intertrustworthyk environment. This environment provides the basis for the broad range of real-world rights and obligations, including intellectual property rights and real-world rules related to those rights and obligations, to be securely expressed and enforced. The strength of the technology is that the right to use the contents of an object can be managed separately from the contents themselves. The rights to the underlying works (the original creation) can be managed separately from the rights relating to particular expressions of those works, just as they are in the real world.

 MusicMatch [4], the developer of the MusicMatch Jukebox, the world’s first personal jukebox software, is participating in Magex’s unique Internet digital music pilot. The music pilot enables record labels and artists to distribute music over the Internet, protect their copyrights, and collect royalty payments. The MusicMatch Jukebox software intends to integrate the Magex service into its digital audio player, allowing users to download rights-protected music tracks from the Internet into the MusicMatch Jukebox. Tracks can then be organized into a digital Music Library, added to custom playlists and played back at CD-quality via the user’s PC. MusicMatch intends to be a Secure Digital Music Initiative (SDMI) compliant product.

Windows Media Rights Manager [2] is a licenseand key-based rights management system in which the rights-protected content cannot be played without a valid license that contains a key to ‘‘unlock’’ the file. The Windows Media Rights Manager is currently adopted by Microsoft Windows Media player and it supports both Microsoft audio and video media files only. The basic Windows Media Rights Manager processes include packaging, distribution, establishing a license server, license acquisition, and playing the media file. When file transfer to a portable device takes place, it is considered to be SDMI-compliant.

The above commercial rights management systems provide certain features beneficial to both consumer and service/contents provider. These features construct the blueprint of future rights management systems and the proposed DRM system is an example of this kind. As these commercial DRM systems are basically targeted for different types of users and different trading environments, their features vary in systems. We summarize these features as follows.

## 1.1. Digimarc

 Supports a wide range of visual contents, including both image and video media

 Provides a range of solutions including copyright communication, image licensing and management, and enhanced Internet commerce.

## 1.2. Intertrust commerce architecture

 A comprehensive architecture is needed for the creation of a globally distributed Intertrustworhty TM environment

 The environment provides the basis for real-world rights and obligations, including intellectual property rights to be securely expressed and enforced.

## 1.3. MusicMatch

 Enables record labels and artists to distribute music over the Internet, protects their copyright, and collects their royalty payments

 Integrates the DRM into its audio player

 Allows users to download rights-protected music tracks from the Internet into the MusicMatch Jukebox

 Organizes tracks into a digital music library, adds to custom playlists, and plays back with CDquality via the user’s PC

 Is SDMI-compliant.

## 1.4. Windows Media Rights Manager

 Uses a license management scheme

 A packaged media file contains a version of a media file has been encrypted and locked with a ‘‘key’’. This packaged file is also bundled with additional information from the content provider  Supports both video and audio

 Supports copy-protection.

To perform rights management on different systems, a generalized operating platform and standard for DRM is needed. In the music industry, major music recordings industry and technology companies have tended to adopt SDMI in the online music distribution business. SDMI offers many desirable DRM features such as copy protection and secure music distribution. The DRM part is powered by digital watermarking technology. However, the SDMI specification does not provide guidelines for the design of digital watermarks and the selection of rights information for different business models. Moreover, SDMI does not take advantage of watermarking for other potential business services including marketing. A limitation of SDMI is that SDMI is only applicable to digital music although it can potentially be extended to other types of media content. This paper proposes an SDMI-based rights management system for both digital audio and video and studies its potential for other value-added features with digital watermarking.

The rest of the paper is organized as follows: Section 2 introduces the principles of digital watermarking and illustrates three basic watermarking processes. Section 3 summarizes the SDMI specifications and covers its major components. Issues regarding rights management and digital watermarking in SDMI are also discussed. Section 4 delineates the concepts of rights management and presents the basic features that a rights management system needs. Section 5 explains the design of the overall SDMIbased rights management system and its major functional components. Digital watermarking for rights management is also addressed in this section. Moreover, we demonstrate how a rights management system can be used for marketing. In Section 6, we present interfaces of the SDMI-based rights management system. Finally, Section 7 summarizes the contributions of our study.

## 2. Digital watermarking

Digital watermarking is a promising technology that assists digital information publishers and distributors in fighting the battle against piracy in the information age. Although the development of digital watermarking is still at its infancy, digital watermarking has already attracted many first-rate researchers. Many watermarking techniques and commercial watermarking systems have therefore been developed and have emerged to focus on rights management, especially copyright protection on digital media content. Moreover, other applications of digital watermarking are revealed, such as marketing and advertising.

![](/api/attachments/PUE97VUP/fulltext/images/3a48727a902dd913cf253081192a1d1230d53951c34bd4d5ffbaaf7cfa99cf5b.jpg)  
Fig. 1. Watermark insertion.

Three basic watermarking processes are required in digital watermarking. They are watermark insertion, watermark detection, and watermark extraction. In general, watermark insertion requires (i) original data, (ii) a watermark, and (iii) and a private key (also known as ‘‘seed’’). The output is the watermarked data. A watermark consists of a number of binary bits that represent information about the ownership of the media, the user’s identity, the description of the original data, and so on.

The watermark insertion process as shown in Fig. 1 embeds a watermark into the original data. Depending on the applications, the watermark can be perceptible or imperceptible in the watermarked data. For applications that require that the original data not be perceptually distorted, an imperceptible watermark is desired. For other applications that require that the embedded data, for example a company logo or trademark, to be shown, a perceptible watermark is preferred.

![](/api/attachments/PUE97VUP/fulltext/images/ace2138442d292ceeb68b398de73cfc614aa758c6c9313d47b60f3195cfa97a2.jpg)  
Fig. 2. Watermark extraction.

![](/api/attachments/PUE97VUP/fulltext/images/be591c99c6b9af8ea5540f866603df841c3627e08ce9e43c7ba3a37a79e5d1f2.jpg)  
Fig. 3. Watermark detection.

Watermark extraction and watermark detection as depicted in Figs. 2 and 3 are respectively used to retrieve and verify the embedded watermark from the watermarked data. In watermark extraction, a public key is used together with the watermarked data to retrieve the embedded watermark. In watermark detection, a public key and a specified ID watermark are used together with the watermarked data to determine whether or not the watermarked data contains the expected watermark.

## 2.1. Digital watermarks

Digital audio watermarks are basically a series of binary numbers of digital audio content, while digital images and video watermarks can be a pattern or a logo for visual digital content, such as an image and or a video clip. They all have something in common. That is, the watermark for these applications carries meaningful information for later processing and interpretation. In the context of rights management, this information may serve for owner verification, usage control, access control, and input for other applications.

## 3. Secure Digital Music Initiative

The objectives of the SDMI [6] are to provide consumers with convenient access to quality recordings, ensure copyright protection for artists’ work, and enable technology and music companies to build successful businesses. SDMI is a forum for the music industry to develop a voluntary and open architecture for playing, storing and distributing digital music that will enable a new market to emerge. SDMI is focused on two tracks. The first track has already produced a standard or specification for portable devices. The longer-term effort is to work toward the completion of an overall architecture for delivery of digital music in all forms.

SDMI is composed of a number of functional components, including a portable device (PD), a licensed compliant module (LCM), and portable media (PM). These components provide a secure environment for music distribution, rendering, and storage. The functional reference model of SDMI is depicted in Fig. 4. Different components are operated at different layers in the reference model.

## 3.1. Application layer

The application layer hosts all SDMI-compliant electronic music distribution (EMD) applications, software players, home library software applications, CD extractors, and other applications. Rights management and screening occur at the application layer of the reference model.

## 3.2. LCM layer

LCM is the module that supports contents in various formats to be transferred from SDMI-compliant applications to PDs and PMs. The LCM may serve as a trusted translator in the case where there is a PD format that the application cannot interpret, such that SDMI applications are not required to communicate directly with all PD formats. As depicted in Fig. 4, it is expected that an application may communicate with multiple LCMs, while a single LCM may also communicate with multiple applications. An important function of a LCM is to provide an abstracted device interface to SDMI applications for PDs and PMs.

## 3.3. PD layer

Only SDMI-protected content is allowed in communications. The PD layer receives SDMI-protected content from the LCM-PD interface. The PD layer constitutes the playback component of the PD reference model, which allows for multiple PD formats as depicted in Fig. 5.

## 3.4. Digital watermarking in SDMI

The SDMI portable device specification [6] states that digital watermarking is required for both local and distributed SDMI-protected content and EMD can also be watermarked. Digital watermarking is used to identify property ownership. SDMI addresses the importance of digital watermarking and includes it in the specification. However, SDMI does not address the design of digital watermarks, the selection of rights information for digital watermarks, and the way to apply digital watermarking efficiently in rights management. Moreover, other potential benefits and advantages of using digital watermarking, such as marketing and control functions, are also not covered in the SDMI specification.

![](/api/attachments/PUE97VUP/fulltext/images/3c3bf7b33a4751f3ad2bd4349cea9dfd424256d71e7c76456bf76e808bd96508.jpg)  
Fig. 4. Reference model functional layers of SDMI (Version 1.0).

![](/api/attachments/PUE97VUP/fulltext/images/a67a03fb18c75c66362b4565f162f40034ecab90ef00668b7ac4bc9f2c454921.jpg)  
Fig. 5. The functional reference model of portable device (version 1.0).

## 3.5. Rights management in SDMI

In SDMI, rights management refers to usage rules that are specified by content providers to govern the content’s use in the SDMI domain. For example, usage rules include rules governing copying (including number of copies/generations of copies permitted), moves, check-in/check-out (including number of usable copies), export from the SDMI domain, and combinations thereof. Usage rules are embedded, attached and/or associated with the content in a protected manner.

## 4. Rights management

Rights management [18] in general refers to the problems associated with intellectual property rights, including copy protection and in particular to the problem of assuring that, in a commerce setting, payment is made for a particular use of content and that the actual use does not exceed the authorized use. In electronic business, consumers make transactions through the web. Ordering, payment, and delivery all take place at the commerce website. It is anticipated that rights management should also be an online service at the commerce website.

Based on the review of commercial DRM systems in Section 1 and the characteristics of digital watermarking in Section 2, we identify the basic features that a rights management system should possess. They:

 Enable intellectual property rights, including copy protection

 Support online ownership verification

 Integrate and persistently protect the artistic integrity of media

 Support various electronic media and formats  Enable pass-along distribution between consumers, know who they are, and get paid by new listeners

 Create merchandising, promotion, direct response marketing, and affinity groups

 Receive timely financial payments and usage information for the media

 Enable the user’s multimedia player for rights management

 Protect all distributed media content though the SDMI framework

 Track the usage of the distributed media contents

 Locate where the media content is and who owns the media content

 Support and respect media label policies.

To accomplish these features, we propose to adopt SDMI as the core architecture for the framework of the rights management system. Digital watermarking is used for the implementation of rights management as well as for providing other value-added features to the system.

## 5. An SDMI-based rights management system

The SDMI architecture provides the basis for a wide range of real-world rights and obligations, including intellectual property rights and real-world rules related to those rights and obligations, to be securely enforced. SDMI was initially designed for digital music. However, the architecture is extendable to other digital media content because the major functional components in the SDMI architecture are addressed but not defined. It is feasible to integrate more desirable features in these components to support other media contents.

We propose an SDMI-based rights management system using digital watermarking for online media distribution businesses that support various digital media content. The system supports both audio and video services. The proposed rights management system is a three-tier client/server system as depicted in Fig. 6. The system consists of three major functional components and they are a rights management system (RMS) server, a rights management database (RMDB), and a multimedia player (MP). Fig. 6 shows that the RMS server is accessible by one of its MPs although the RMS server can support multiclient access. Digital watermarks are used to carry information within these components. Communications between two or more SDMI-compliant components are protected and authenticated by a secure authenticated channel (SAC) according to SDMI. SDMI-protected media content is used throughout the system.

## 5.1. RMS server, RMDB, and MP

In order to manage digital rights of the distributed media content effectively, it is necessary to allow clients to communicate with the centralized server (the RMS server). The RMS server is mainly responsible for ‘‘global’’ rights management. This means that the RMS server is in control of the execution of rights to the distributed media content. The RMS server can basically activate, maintain, and terminate the usage rights of distributed media content.

Rights-protected and watermarked media content is obtained from any source. This is different from the SDMI specification. The SDMI has the restriction that the distributed media contents must be from a SDMI-compliant device or source. The usage rights will be activated when the MP requests to render digital media content. The MP first extracts the rights information from the embedded watermark using an internal watermark extraction process. The extracted rights information is formulated as a request. The MP’s request, which contains the product ID, the User ID, and other relevant information, is sent through the Internet using SAC. When the RMS server receives the request, it will verify the MP and the targeted media content by looking up their information in the RMDB. A permission to grant access to and usage of the distributed media content will be issued and returned to the MP. The MP keeps the access and usage rights within the unit and can play the content as granted. In order to update the rights status of the distributed media content, the MP is required to communicate with the RMS server whenever it is online.

As long as the permission is valid, the MP is entitled to open and play the distributed media content even when the MP is disconnected from the Internet. In the offline mode, a ‘‘local’’ rights management module within the MP will be invoked and will manage the rights of the media locally under certain constraints. The constraints are as follows.

![](/api/attachments/PUE97VUP/fulltext/images/a0a5fc167339ec26d6b7370820e22632acc1440370ab052c480628802924c89d.jpg)  
Fig. 6. Major components of the proposed rights management system.

 The MP must be registered with the RMS server before it is actually used.

 The user must register with the RMS server.

 An authentication must be enforced on the MP.

 The local rights management must be initiated by the RMS server when the distributed media content is being loaded by the MP for the first time.

 The usage rights for a digital media has a time limitation, so the MP is required to connect to the RMS server for an update when the usage rights have expired.

The RMDB, which is a server-side database management system, is used to store all rights-related information. The RMS server, together with the RMDB establishes rights to the distributed media content. Upon receiving an access request from an

MP, the RMS server may determine the geographical location of the MP by interpreting the MP’s Internet protocol (IP) address and then keep this information in the RMDB for other applications and services.

The RMDB stores all rights-related information as well as the RMS server-generated information. In the RMDB, a data entry may refer to a customer’s, company’s, or product’s rights information. This can be represented by a product ID, user ID, company ID, access rights, a company’s web address, and so on. The RMDB can be a LCM according to SDMI specifications.

The MP is SDMI-compliant and video-enabled. It is a PD that may contain a LCM. In addition to rendering the video and audio media, another major feature of the MP is its support of a local rights management module. The local rights management module resides in the MP and manages access and usage rights of the media contents locally when the MP is disconnected from the Internet.

## 5.2. Digital watermarking for rights management

Content providers and owners demand that a rights management system is able to detect and track duplicate copies. In the context of rights management, digital watermarks carry serial numbers also known as indexing information that uniquely identifies the entry of the rights-protected contents in the RMDB. The serial number is represented by a key that refers not only to rights information, but also to product information, a customer’s personal interests, and distributor details. The rights information usually includes copyright and licensing information, for example, the identities of the copyright holder, the creators of the material, and the authorized usage of the digital media content. Technically, a watermark is derived from the key using a hashing function or a pseudo-random generator.

## 5.2.1. Rights information

In the online media distribution business, authors and publishers who distribute their digital media contents online expect to specify the usage and access rights for the distributed media contents so that consumers may use the media content according to the specified rights. Copyright infringement is the major problem with digital media contents because duplicated copies can be identical to the original copy. Digital watermarking enables the rights holders to insert rights information into digital contents without distorting the quality of the contents or changing the original contents. Different rights information is needed in different business models but rights information usually includes information about the content providers, distributors, and consumers. In addition to rights management, an online media distribution business has other business goals to achieve, such as marketing and promotion. To achieve all these goals, information about the user (ID, credit, rights information, etc.), the user’s affiliations (interests, nationality, gender, etc.), the product (ID, serial no., model number, type, name, etc.), the product affiliation (fan club, related products, accessories, etc.), and the links (URL) through which to gather more related information is usually needed [8]. The collected information is related to other information within the RMDB. Digital watermarks may carry indexing information so that the RMS server can reference to relevant rights information in the RMDB.

## 5.2.2. Rights management

In some cases, digital watermarking can also be used to identify the source of the infringing materials. For those companies that license videos online and enable customers to download licensed videos, the companies may insert distinct watermarks into the videos for downloading and the embedded watermarks uniquely identify the licensees (and customers). If an unauthorized use of a video is discovered, the RMS server can check and determine from which licensee it came. In the case that the video being used is a pirated copy that was copied from a legitimate copy, the proposed RMS system is able to help the rights holders stop unauthorized dissemination. When the pirated copy is being used offline illegally, rights holders can always identify the true owners by extracting the embedded watermarks.

Digital watermarking technology enables rights holders to enforce their intellectual property rights by seeking out and prosecuting copyright pirates. As with much Internet law, there are jurisdictional problems with infringement being rife in countries with the least protection, but the proposed harmonization provisions will at least ensure that rights holders are able to protect their works commercially in a large part of the world market.

## 5.2.3. Marketing

Digital watermarks contain product information such as a product ID, a user ID, and the location of the designated RMS server. This information is useful in many rights-related and non-related applications. A careful selection of the embedded information will enable many business opportunities, for example marketing. Some value-added features of watermarking have been addressed by Acken [1].

Distributed media content carrying a distinct watermark is traceable by a watermark spider when the media contents are being rendered by a third-party media player and the player is accessible to the Internet. For example, the watermark spider, SysCoP Spider [19], acts as a robot to search for watermarked media contents in the Internet and automatically locates their geographical locations.

An active way to locate distributed media contents is to use our MP. Whenever the MP needs to communicate with the RMS server, the location of the media is automatically presented to the RMS server and uploaded to the RMDB. The RMS server can track the media and this can help content providers to have focused-marketing strategies and plans for related products.

A more aggressive and positive approach could be one that whenever the watermarked media contents are opened or reproduced, our MP will automatically forward the embedded information, including the user ID and the location of the media contents, to the RMS server. This scheme is borrowed from the SDMI architecture. This provides valuable marketing data about the distribution of products. In addition, the approach may also benefit marketing campaigns and provide better management of assets.

## 5.3. Summary

The proposed DRM system has many advantages over existing commercial DRM systems. Our DRM system integrates most of the desirable features identified from the existing DRM systems. It is SDMI-compliant and it supports the online music distribution business. In our system, we do not use a license scheme that is the core technology in Windows Media Rights Manager [2]. The problem of having a license in DRM is that the license is usually presented in a digital file and hackers are capable of manipulating, swapping, and reproducing such digital licenses. Our approach uses digital watermarking. Some researchers at Princeton University have shown that knowledgeable hackers could also crack digital watermark [10,20]. However, our DRM system can ensure that the MP can play only SDMI-protected (or watermarked) media content. When the embedded watermark is removed from the rights-protected content, the media content cannot be used by other multimedia players because our system uses proprietary file formats for the media contents.

Problems with the proposed DRM system include: (1) it could be too dependent on the centralized RMS server. The security of the RMS server becomes a major concern in the system and (2) it will be inconvenient to connect the MP to the RMS server for access and usage rights approval when the media content is first being accessed.

![](/api/attachments/PUE97VUP/fulltext/images/c3bef01b17b0dcae563766a72fc22419c0239013b5669fb446a45e5ca7d863fd.jpg)  
Fig. 7. Administration interface of the RMS server.

![](/api/attachments/PUE97VUP/fulltext/images/80fcb187e69e301f735b0a06018a66b5d1d6e39b23397b444671ef552652f507.jpg)  
Fig. 8. Multimedia player—interface of music player.

## 6. Interfaces of the prototype system

We built a prototype of the SDMI-based rights management system. Some components are complet ed and the interfaces of the RMS server administration and MP are displayed in this section.

## 6.1. RMS server administration

The interface of the RMS server administration is shown in Fig. 7. As can be seen, the interface contains two parts. The top shows the status of all RMS server-side components in the system. And the bottom gives the detailed log information about connected RMS clients and MPs or other compatible applications.

![](/api/attachments/PUE97VUP/fulltext/images/13df787bde515aeaaf5d7664a1e64b7b994d996fdb69b49c91781cf84a92856e.jpg)  
Fig. 9. Music player—file menu.

![](/api/attachments/PUE97VUP/fulltext/images/5c9c414c42fce9c276a16e20c587566fef36ef9d4a6db090d33d5efd2eaf4e27.jpg)  
Fig. 10. Multimedia player—registration page.

## 6.2. Multimedia player

The MP is composed of three functional modules, namely the music player, the video player, and the mini browser.

## 6.3. Music player

The music player is the default player of the MP. The interface of the music player is given in Fig. 8. In the File menu, there is a ‘‘Register’’ function as shown in Fig. 9. The ‘‘Register’’ function invokes an online registration page to register the usage of the media in the rights management system. The registration page is displayed in Fig. 10.

![](/api/attachments/PUE97VUP/fulltext/images/af8cf61565d1d4e5c8ec1f5ad2bcc2b5b5ec2660b4e520d81257f26d857c2e64.jpg)  
Fig. 11. Interface of multimedia player—view—file info.

![](/api/attachments/PUE97VUP/fulltext/images/24a814ee61c88406c545f724aedf3ad5cb0af36813ec3908ec9a51ce98aa6994.jpg)  
Fig. 12. Multimedia player—view—‘‘File Info’’ page.

In the View menu as shown in Fig. 11, there is a ‘‘File Info’’ option. The ‘‘File Info’’ displays detailed information on the current media file, such as the filename, product ID, product content, product version, issued date, expiry date, access right, and so on. The ‘‘File Info’’ page is presented in Fig. 12. As can be seen, the file extension is ‘‘wmm’’ and this is the file format of our watermarked SDMI-compliant media.

![](/api/attachments/PUE97VUP/fulltext/images/a031d5818d3c132403ff42448b9302d0cfe55067c5c57706e25c3498bfe374eb.jpg)  
Fig. 13. Interface of multimedia player—video player.

![](/api/attachments/PUE97VUP/fulltext/images/83672d5c35774ebf57cd23dcd96ab1baefcff98ad6bc1302c220bf37fa3911c6.jpg)  
Fig. 14. Interface of multimedia player—mini browser.

## 6.4. Video player

The MP can also support video. Fig. 13 displays the interface of the video player while it is rendering a video file.

## 6.5. Mini browser

The MP can act as a web browser. It enables users to access watermarked SDMI media content efficiently via the Internet and it also allows the RMS server to communicate and update information with the MP. The interface of the mini browser is shown in Fig. 14.

## 7. Conclusions

This paper has presented an SDMI-based rights management system. Digital watermarking is the core technology for this rights management system. Its major functions include inserting rights information, conducting rights verification, and executing other rights-related processes. The underlying framework of the proposed DRM system is based on SDMI because it will likely be adopted by the recordings industry for the online music distribution business and SDMI-complaint products are available in the market. The features of the proposed system are referenced to many commercial DRM systems. The proposed DRM system has been implemented and some interfaces are presented in this paper.

The major contributions of this paper include the following:

(1) Discussing the implementation of digital watermarking in SDMI-based DRM systems;

(2) Studying the use of digital watermarks and rights information for DRM;

(3) Exploring the applicability of value-added features in DRM system, such as marketing, for DRM using digital watermarking technology.

In future developments, our research will focus on another promising rights management specification, MPEG-21, for multimedia applications. MPEG-21 is still being developed and therefore we did not compare it with the proposed DRM system in this paper.

From the application perspective, another possible direction for DRM is mobile commerce in which DRM may operate on mobile devices that are usually constrained by processing power and storage [11,12].

## Acknowledgements

This research is supported in part by the Hong Kong Research Grants Council through a Direct Allocation Grant (DAG99/00.BM38) and the Sino Software Research Institute (SSRI) (SSRI01/02.BM01).

## References

[1] J.M. Acken, How watermarking adds value to digital content, Communications of ACM 41 (7) (1998) 75–77.

[2] Anonymous, Architecture of Windows Media Rights Manag-

er, http://www.microsoft.com/windows/windowsmedia/wm7/ drm/architecture.aspx, accessed on 14 March 2003.

[3] Anonymous, InterTrust Technologies-About DRM, http:// www.intertrust.com/main/overview/drm.html, accessed on 14 March 2003.

[4] Anonymous, MUSICMATCH Jukebox Digital Audio Software, http://www.musicmatch.com, accessed on 14 March 2003.

[5] Anonymous, Napster, http://www.napster.com, accessed on 14 March 2003.

[6] Anonymous, SDMI-Amendment 1 to SDMI Portable Device Specification, Part I, Version 1.0, http://www.sdmi.org/ download/port<sup>\_</sup>device<sup>\_</sup>spec<sup>\_</sup>amend1.pdf, accessed on 14 March 2003.

[7] Anonymous, Digimarc, http://www.digimarc.com, accessed on 11 March 2003.

[8] O. Benedens, Geometry-based watermarking of 3D models, IEEE Computer Graphics and Applications 19 (1) (1999) 46 – 55.

[9] J. Brown, The Gnutella Paradox, 2003, http://archive.salon. com/tech/feature/2000/09/29/gnutella<sup>\_</sup>paradox/, accessed on 14 March 2003.

[10] S. Craver, J.P. Stern, Lessons learned from SDMI, Proceedings of the IEEE Fourth Workshop on Multimedia Signal Processing (2001) 213– 218.

[11] F. Hartung, F. Ramme, Digital rights management and watermarking of multimedia content for m-commerce applications, IEEE Communications Magazine 38 (11) (2000) 78 – 84.

[12] S.H. Kwok, Digital rights management for mobile multimedia, in: E.P. Lim, Z. Shen, K. Siau (Eds.), Mobile Commerce: Current States and Future Trends, 2002, Chap. 5.

[13] S.H. Kwok, Digital watermarking for digital rights management, in: L. Jain, H.C. Huang, J.S. Pan (Eds.), Intelligent Watermarking Techniques, 2003.

[14] S.H. Kwok, S.C. Cheung, K.C. Wong, K.F. Tsang, S.M. Lui, K.Y. Tam, Integration of digital rights management into Internet Open Trading Protocol (IOTP), Decision Support Systems (DSS) 34 (4) (2003) 413– 425.

[15] S.H. Kwok, C.C. Yang, Watermarking in online media e-business, Proceedings of the International Conference on Information Technology: Coding and Computing (ITCC-2002) (2002) 158 – 163.

[16] S.H. Kwok, C.C. Yang, K.Y. Tam, J.S.W. Wong, An SDMIbased rights management system for electronic media using digital watermarking, Proceedings of the International Conference on Electronic Commerce (ICEC 2000) (2000) 193 – 200.

[17] T. Page, Digital watermarking as a form of copyright protection, Computer Law and Security Report 14 (6) (1998) 390 – 392.

[18] T. Stewart, Designing Systems for Internet Commerce, Addison Wesley, Boston, USA, 1998.

[19] S. Wolthusen, Watermarking, 2003, http://syscop.igd.fhg.de/, accessed on 12 March 2003.

[20] M. Wu, S. Craver, E.W. Felten, B. Liu, Analysis of attacks on SDMI audio watermarks, Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (2001) 1369 – 1372.

![](/api/attachments/PUE97VUP/fulltext/images/a737cc637f1fb8ef6b90af9fe54cb87010b6892cd6a7f003839b8b19b87b419a.jpg)

Dr. Kwok received a BEng (Hons) in Electronic and Communications Engineering from the University of North London. He received his Diploma of Imperial College (DIC) from the Imperial College of Science, Technology and Medicine, and his PhD in Digital Image Processing from the University of London. He is currently assistant professor at the Department of Information and Systems Management, Hong Kong University of Science and

Technology (HKUST). He was visiting scholar and a research assistant in the Department of Electronic and Information Engineering at the Hong Kong Polytechnic University. His research interests include digital rights management, copyright protection management, knowledge management, multimedia database management systems, digital watermarking, web and mobile services, peer-topeer technology, and electronic commerce applications. His research has been published in various journals, including Communications of the ACM (CACM), International Journal of Electronic Commerce (IJEC), Decision Support Systems (DSS), Electronic Markets, IEEE Transactions on Circuits and Systems for Video Technology, IEEE Transactions on Image Processing, Graphical Models and Image Processing, Journal of Parallel and Distributed Computing, Optical Engineering, International Journal of Information Technology and Decision Making (IJITDM), Journal of Applied Systems Studies (JASS), and ACM SIGecom Exchanges.

![](/api/attachments/PUE97VUP/fulltext/images/43e19f4e9d428fd827b9a9a1b8c2581eb6867d8a5b58547669203cb144f9ec0b.jpg)

Christopher C. Yang is currently an associate professor in the Department of Systems Engineering and Engineering Management at the Chinese University of Hong Kong. From 1997 to 1999, he was an assistant professor in the Department of Computer Science and Information Systems and associate director of the Authorized Academic JavaSM CampusSM at the University of Hong Kong. He received his BS, MS, and PhD in Electrical and Com-

puter Engineering from the University of Arizona, Tucson, in 1990, 1992, and 1997, respectively. From 1995 to 1997, he was a research scientist in the Artificial Intelligence Laboratory in the Department of Management Information Systems, where he was an active researcher in the Illinois Digital Library project. From 1992 to 1997, he was also a research associate in the Intelligent Systems Laboratory in the Department of Electrical and Computer Engineer ing. His current research interests are digital library, information visualization, Internet agent, cross-lingual information retrieval, and color image retrieval. He has published over 80 refereed journal and conference papers. He has served as a guest editor for the Journal of the American Society for Information Science and Technology. He was the chairman of the Association for Computing Machinery Hong Kong Chapter and the program co-chair of the First Interna tional Conference of Asia Digital Library.

![](/api/attachments/PUE97VUP/fulltext/images/da9cf9c10c5329ad89aeb92850d5b92eb1297793e5d7b1bad5d8699080298257.jpg)

Dr. Kar Yan Tam is currently professor of Information and Systems Management and Senior Weilun Fellow at the Hong Kong University of Science and Technology. His research interests include adoption of IT innovations, digital copyright protection technology, and electronic commerce. His papers have appeared in major management science and information system journals He is currently on the editorial board of a number of IS journals.

![](/api/attachments/PUE97VUP/fulltext/images/43714b29012a3f05aff07f5304fe7f42267b83421aa7655a3a02b42a8b246554.jpg)

Jason S.W. Wong received his BS in Computer Engineering from the University of Hong Kong in 1999 and MSc in Systems Engineering and Engineering Management from the Chinese University of Hong Kong in 2003. He was a research assistant in the Digital Library Laboratory in the Chinese University of Hong Kong. He is currently with Crystal Decisions (HK).
