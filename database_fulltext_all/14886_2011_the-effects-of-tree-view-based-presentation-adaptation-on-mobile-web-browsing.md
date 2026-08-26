---
otero_id: 14886
otero_key: "D3WBMPWJ"
title: "The Effects of Tree-View Based Presentation Adaptation on Mobile Web Browsing"
authors: "Boonlit Adipat; Dongsong Zhang; Lina Zhou"
year: "2011"
journal: "MIS Quarterly"
doi: "10.2307/23043491"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
The Effects of Tree-View Based Presentation Adaptation on Mobile Web Browsing Author(s): Boonlit Adipat, Dongsong Zhang and Lina Zhou

Source: MIS Quarterly, March 2011, Vol. 35, No. 1 (March 2011), pp. 99-121

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: https://www.jstor.org/stable/23043491

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at https://about.jstor.org/terms

# THE EFFECTS OF TREE-VIEW BASED PRESENTATION ADAPTATION ON MOBILE WEB BROWSING $^{1}$

Boonlit Adipat

Graduate School of Management and Innovation, King Mongkut's University of Technology Thonburi, 126 Pracha-Util Road, Bangmod, Thung-Khru, Bangkok, THAILAND 10140 {boonlitadipat@gmail.com}

Dongsong Zhang, Lina Zhou

Department of Information Systems, University of Maryland, Baltimore County, 1000 Hilltop Circle, Baltimore, MD 21250 U.S.A. {zhangd@umbc.edu}, {zhoul@umbc.edu}

Accessing the Web from mobile handheld devices has become increasingly common. However, accomplishing that task remains challenging mainly due to the physical constraints of handheld devices and the static presentation of Web pages. Adapting the presentation of Web pages is, therefore, critical to enabling effective mobile Web browsing and information searching. Based on cognitive fit theory and information foraging theory, we propose a novel hybrid approach to adapting Web page presentation that integrates three types of adaptation techniques, namely tree-view, hierarchical text summarization, and colored keyword highlighting. By following the design science research framework, we implemented the proposed approach on handheld devices and empirically evaluated the effects of presentation adaptation on mobile Web browsing. The results show that presentation adaptation significantly improves user performance and perception of mobile Web browsing. We also discover that the positive impact of presentation adaptation is moderated by the complexity of an information search task. The findings have significant theoretical and practical implications for the design and implementation of mobile Web applications.

Keywords: Presentation adaptation, mobile handheld device, Web browsing and searching, interface design, usability testing

## Introduction

The use of mobile handheld devices such as cell phones, PDAs, and palm pilots has become pervasive in our life. Accessing the Web through a handheld device, called mobile Web (W3C 2008), is no longer a novelty. For many, it has become a common daily routine. According to the 2010 poll from the Pew Internet and American Life Project, nearly 60 percent of adult Americans have either accessed the Internet with a wireless connection or used an application by way of cell phone or PDA. The ability to communicate at virtually any place with the convergence of the Web and wireless technologies offers an unprecedented level of flexibility, accessibility, and convenience to users of mobile handheld devices, particularly for ubiquitous information access.

The convenience of mobile Web, however, has been compromised by some challenges posed by the unique constraints of handheld devices (e.g., small screen size and limited memory), wireless networks, and the mobility of users (Zhang

2007). Most existing Web sites are designed and optimized for desktop and broadband clients only. They are poorly suited for mobile handheld devices, making the Web content look aesthetically unpleasant and difficult to navigate. More importantly, because the text font size cannot be reduced below a threshold of legibility, only a small amount of information can be shown on the screen of a handheld device at a time. For example, there are normally fewer than 15 lines vertically and fewer than 12 characters per line that can be shown on the screen of a typical cell phone (Chae and Kim 2004). As a result, users have to perform left/right and up/down scrolling frequently during Web browsing, which is very annoying. Even if some handheld devices can adjust the Web page display with vertical scrolling only, it requires clipping and wrapping the text, which results in increased Web page length. Users also have to memorize different parts of a Web page that they have viewed and then relate one part to another in order to make sense of the context. These processes place a heavy cognitive load on users (Albers and Kim 2000). As cognitive load increases, users tend to generate more errors (Davison and Wickens 1999), and Web browsing and searching become tedious and inefficient. Therefore, presenting Web content on mobile handheld devices in a way that better adapts to the characteristics of devices and user needs can help users locate information of interest more effectively.

According to W3C (World Wide Web Consortium), adaptation is defined as a process of selection, generation, or modification that produces one or more perceivable units in response to a requested uniform resource. $^{2}$ Presentation adaptation involves a process of reauthoring or rearranging the content layout of a Web page in order to achieve more effective content navigation and improve user experience with mobile Web (Zhang 2007).

Presentation adaptation has been studied in the desktop environment and been proven beneficial in improving the user experience in Web browsing by alleviating the problems of information overload (Tsandilas and Schraefel 2003), frequent scrolling/clicking (Tsandilas and Schraefel 2004), and navigation loss (Furnas and Zacks 1994; Robertson et al. 1991). However, research on adaptation of Web content presentation for mobile handheld devices is still rare. Due to the unique characteristics of such devices, previous theories and findings about presentation adaptation in desktop settings may no longer be applicable. Most previous related studies focused on developing individual adaptation techniques.

$^{2}$ http://www.w3.org/TR/di-gloss/.

They either did not include any user evaluation (e.g., Baudisch et al. 2004; Chen et al. 2005), or used emulators on a desktop rather than real handheld devices while evaluating a specific approach (e.g., Kaasinen et al. 2000; Lam and Baudisch 2005). In particular, there are few empirical studies that systematically examine the impact of presentation adaptation on mobile Web browsing on handheld devices.

This research aims to fill the knowledge gap by answering three important research questions for the task of information search via mobile Web browsing:

(1) Can presentation adaptation techniques improve user performance and perception?

(2) Will more presentation adaptation features result in better user performance and perception?

(3) How does the impact of presentation adaptation vary with task complexity?

This research follows the design science research framework (Hevner et al. 2004), which provides systematic and practical guidelines for building innovative information systems artifacts to solve a problem in an organized and effective manner. There are three types of artifacts created in this research. First, we construct a research model that relates presentation adaptation to user performance and perception. This relationship is moderated by task complexity. Second, we identify and integrate several approaches to presentation adaptation based on cognitive fit theory (Vessey 1991) and information foraging theory (Pirolli 2007). Third, we implement prototype systems on physical handheld devices, and use those systems in an empirical evaluation of the proposed adaptation approaches. To the best of our knowledge, this is the first empirical study that examines the effect of presentation adaptation on user performance and perception of mobile Web browsing using physical devices. This research provides several new theoretical and practical insights on how to adapt Web content for effective browsing on mobile handheld devices and how to improve user interface design for those devices.

## Related Work and the Research Model

Effective information presentation is critical for improving user experience with mobile Web (Qiu et al. 2006). Some presentation adaptation techniques have been developed to alleviate the problems of intensive scrolling and restricted navigation during Web browsing. We categorize existing approaches to presentation adaptation into four categories: page splitting, content outlining, text summary based approach, and visualization based approach. The strengths and weaknesses of each approach are summarized in Table 1.

Table 1. Common Approaches to Presentation Adaptation for Mobile Handheld Devices

<table><tr><td>Approach</td><td>Description</td><td>Strengths</td><td>Weaknesses</td></tr><tr><td>Page splitting</td><td>It divides an original Web page into several smaller sub-pages that fit the screen size of a specific mobile device (Hong et al. 2003).</td><td>Users can perform page-by-page navigation by clicking the next or previous button or indexed page numbers.</td><td>As the size of a Web page increases, the number of split pages will increase accordingly. By nature, this approach just replaces scrolling with button clicking. It still suffers from navigation loss.</td></tr><tr><td>Content outlining</td><td>It constructs a structured representation of a Web page to display content blocks. Content blocks refer to distinct content parts of a Web page.</td><td>Based on the content structure, adaptation process will identify the content blocks of a Web page and how those blocks are related to each other. If a user is interested in a certain content block, he/she can drill down in that block to see further details.</td><td>Existing approaches are heuristics based (e.g., Bickmore and Schilit 1997), which can only generate proper structure presentation for a limited set of Web sites and are hard to generalize. In addition, when a user expands a content block, a separate new page will be opened, causing additional steps to traverse.</td></tr><tr><td>Text summary based approach</td><td>It presents only a portion or a text summary of a Web page (Lam and Baudisch 2005; Otterbacher et al. 2006).</td><td>It enables users to read those snippets or summaries before deciding if they want to see complete details.</td><td>It is difficult to generate an effective summary for a Web page that can accurately capture the main idea and information important to users. There is no empirical evidence about its impact on user perception of mobile Web yet.</td></tr><tr><td>Visualization based approach</td><td>It uses visualization techniques, such as focus and context approach (Björk et al. 1999) and zooming technique (Baudisch et al. 2004) to view a Web page.</td><td>It provides a progressive process for expanding detailed information upon a user&#x27;s request.</td><td>In the focus and context approach, users need frequent switching between the focus and the context, and the context is normally too small to be legible. Multiple zooming levels may cause users to lose the context easily.</td></tr></table>

One of the common limitations of those approaches is the lack of theories that provide the underlying rationale, which can help explain why the approaches can influence user performance and perception of mobile Web browsing. In addition, the majority of the limited number of empirical studies on presentation adaptation often used emulators of mobile devices on desktop computers. Because those studies bypassed some technical challenges that users would encounter while using physical handheld devices (e.g., using a regular mouse to interact with an emulator on a desktop computer is much easier than clicking small buttons on a physical handheld device or using a stylus to interact with the device), their findings may not truly reflect participants' actual performance and perception while using physical devices (Zhang and Adipat 2005).

Based on extant presentation adaptation approaches and information processing theories, we propose a hybrid presentation adaptation approach that integrates tree-view (content outlining), hierarchical text summarization (text summary based approach), and colored keyword highlighting (visualization based approach). Our approach is unique in several aspects. First, the tree-view adaptation approach, a type of content outlining, automatically generates a hierarchical and expandable overview of a Web page based on document object model (DOM) (W3C 2005), which is more flexible and generic than the heuristic based approach employed in earlier studies (e.g., Bickmore and Schilit 1997). Users can navigate through the hierarchical tree view of a Web page and expand or collapse individual sections as they wish. Because the content is displayed in the same tree-view page rather than in a new page, our approach reduces the problem of losing the context due to multiple zooming levels. Second, we add hierarchical text summarization and colored keyword highlighting on top of the tree view to provide users with additional cues and adaptation. Users can view summaries of Web content at multiple levels in the tree view, not just a brief summary of the entire Web site. Third, our colored keyword highlighting approach not only highlights the keywords of interest appearing on a Web page with different colors, but also shows the count of keyword appearances in each section in the tree view.

![](/api/attachments/D3WBMPWJ/fulltext/images/cb83fc994f114a60fb849dae3a18419cd3bf165ee8d47ab7b24b384d40be563a.jpg)  
Figure 1. The Research Model

In this research, we aim to examine the impact of different presentation adaptation approaches on user performance and perception of mobile Web browsing on small handheld devices. The overall research model is shown in Figure 1. User performance has been commonly assessed by search accuracy and search time in the human-computer interaction (HCI) and information seeking literature (e.g., Hicks et al. 2003; Kuo et al. 2004; Speier 2005; Speier and Morris 2003). Because this study focuses on the interaction between the user and handheld devices during the task of information search via Web content browsing, search time and accuracy are appropriate measures of user performance. User perception is measured by perceived ease of use and perceived usefulness, which are commonly used for evaluating information technologies and users' intention to adopt them (Davis 1989; Doll et al. 1998; Karahanna and Straub 1999). In addition, because the complexity of information search via Web browsing varies with the length and structure of individual Web sites, we also explore the potential moderating effect of task complexity on the impact of presentation adaptation.

## Theoretical Foundation and Hypotheses Development ■

## Tree-View Presentation Adaptation

Tasks of information search on the Web can be categorized into search by browsing (i.e., viewing Web pages one at a time and navigating from one Web page to another through hyperlinks) and search by queries (i.e., entering a search query into a search engine) (Olston and Chi 2003). Although they complement each other, this research mainly focuses on search by browsing because the content presentation is much more important and relevant to that type of task than to search by queries.

Searching for specific information via Web content browsing is a challenging task that requires support from a system (Marchinonini 1995). Information presentation is vital to this task. When reading a document, readers often perform skimming or scanning (Huckin 1983; Sticht 1997). Skimming refers to very fast reading through the structure of a document (e.g., headings, subheadings) to gain a general idea of its content. Scanning is similar to skimming except that users already know what they want. They scan through content to find information of interest. The small screen size of mobile handheld devices makes it difficult for users to obtain a clear idea about the organization of a Web page (Albers and Kim 2000). Users have to scroll up/down and left/right continuously within a Web page, resulting in inefficient skimming and scanning. This increases the difficulty in finding target information (Jones et al. 1999). In addition, because users need to remember the content and context of a Web page that they have already viewed, the cognitive load increases, leading to the increase of errors (Davison and Wickens 1999).

Cognitive fit theory (Vessey 1991) suggests that the correspondence between task and information presentation format leads to superior task performance. While solving a problem, a person creates a mental representation of the problem based on the information presented to him. This mental representation reflects how he views the problem in his limited working memory (Gentner and Stevens 1983). If a mismatch between task and information presentation occurs, users must make extra cognitive effort to transform information into a format that is suitable for accomplishing the task. This extra effort can result in inferior task performance (Vessey 1994). Therefore, the information should be presented in a format that helps users effectively utilize the working memory while performing a task.

The organization of a document influences the way readers acquire, remember, and use information (Duin 1989). In general, when users browse a Web page, they are likely to rely on its hierarchical structure for navigation so that they can glance down the table of contents or across the tabs of a document and immediately understand both the overall content and its structure (DeStefano and LeFevre 2007; Redish 1993). Hypertexts that are hierarchically structured to capitalize on the inherent organization of the content often result in better comprehension, recall, and navigation (Lin 2003). Past studies using desktop computers suggest that providing information about the structure of Web sites is of utmost importance in Web browsing (Nation et al. 1997; Zhang and Salvendy 2001).

One of the well-recognized techniques for effective information search via Web browsing on desktop computers is the tree-view hierarchical display approach (Johnson and Shneiderman 1991; Nation et al. 1997; Robertson et al. 1991). This approach presents the content of a Web page in a tree-type, multilevel hierarchy. Instead of showing the original Web content entirely, it first displays major section titles in a Web page at the highest level of the tree. Users can click a section title of interest, and the tree will either expand to show the next-level branches or display the detailed content of the selected section (if no subsections are available). However, previous studies and findings were based on desktop computers. It remains unclear whether providing the tree-view adaptation can improve Web browsing on handheld devices.

Based on cognitive fit theory, we argue that the tree-view hierarchical presentation of Web pages would be a good fit for the information search via browsing task on mobile handheld devices and should be an essential component of presentation adaptation for mobile Web. Tree-view adaptation effectively utilizes limited display space to present the structure and content of a Web page; it provides users with both global and local views of Web content and allows quick content scanning and skimming (Johnson and Shneiderman 1991; Nation et al. 1997). In addition, tree view is very intuitive and familiar to users (like browsing a book through its table of contents), alleviating the need for users to create a mental model of a Web page's structure when browsing for target information. More effective information presentation can enhance users' perceptual processes and lead to more effective information exploration (Tegarden 1999). Therefore, we predict that the tree-view presentation adaptation will improve user performance (i.e., search time and accuracy) and user perception (i.e., perceived ease of use and usefulness) in the task of mobile Web browsing. Therefore, the first hypothesis is proposed as follows:

H1: For information search via mobile Web browsing, the tree-view presentation adaptation will lead to

(a) reduction in search time,

(b) increase in search accuracy,

(c) increase in perceived ease of use, and

(d) increase in perceived usefulness.

## Presentation Adaptation with Hierarchical Text Summarization

Users often find it difficult to locate information of interest quickly while browsing a Web site. The reason for this difficulty lies in the lack of enough information to provide appropriate “scent” to the user (Olston and Chi 2003). Information foraging theory (Pirolli 2007), which is related to adaptive interaction with information, seeks to explain how human beings search for information. It is widely used as a theoretical foundation by researchers who study user interaction with Web sites and examine how to adapt information systems to improve users’ information search experience. The theory posits that the information search behavior of humans is analogous to the food foraging mechanisms of animals. An animal relies on scent from prey to make a decision on whether or not it should stay on a site or change location to find additional food. In a similar manner, when searching for information, people rely on information scent (Pirolli 2007), which can be defined as various information cues that help people determine the potential information value. Based on those information cues, people make a decision about whether they should stay on the current Web page (or section) or traverse to another one via a hyperlink. Information scent is vital to information search via browsing because it indicates the utility and relevance of navigation paths that may lead to target information.

Based on the information foraging theory, we argue that it is important for a mobile Web system to provide users with strong information scents to enable effective content skimming and scanning. In addition to presenting the structure of a Web page through a tree view, an adapted presentation should also provide some cues (i.e., information scent) about the content of each section or branch in the tree view so that users can assess the information utility of a particular path before following it. Those cues can be either textual or visual representation (e.g., text labels, colors, font, and size of text) of the content (Furnas 1997; Pirolli et al. 2001).

Text summarization, a process of abstracting the main gist from an information source to produce a condensed representation of content (Hahn and Mani 2000), has been widely used as an information scent in information retrieval to help users quickly identify documents of interest (Chi et al. 2005; Harper and Patel 2005). Good summaries of Web content can provide the user with some level of indication about the relevancy of the content to the user's need before perusing the full content. There are a few preliminary studies on developing summarization techniques for mobile handheld devices (e.g., Buyukkokten et al. 2001; Yang and Wang 2003). However, they mainly focus on technical approaches to summarization. For example, Yang and Wang (2003) have proposed a fractal summarization approach. Their evaluation primarily focuses on the quality of generated summaries rather than the impact of summaries on mobile Web browsing and user perception. Extant research in desktop environments reports that text summarization is a useful tool that helps users find information faster and improves user satisfaction (Harper and Patel 2005; McDonald and Chen 2006; McKeown et al. 2005). Therefore, we predict that adapting presentation by providing hierarchical text summaries of Web content in tree view will have a positive impact on information search via Web browsing on handheld devices. Our second hypothesis is proposed as follows:

H2: For information search via mobile Web browsing, adding hierarchical text summarization to the tree-view presentation adaptation will lead to

(a) reduction in search time,

(b) increase in search accuracy,

(c) increase in perceived ease of use, and

(d) increase in perceived usefulness.

## Presentation Adaptation with Colored Keyword Highlighting

Another adaptation method that can provide information scent for Web browsing uses colors to make the target information easily noticeable (Pirolli et al. 2003). When browsing a Web page, users often look for certain keywords or sentences of interest rather than reading the entire page (Nielsen 2000). Research also suggests that the use of information visualization would enhance users' perceptual processes and lead to more effective information exploration (Olston and Chi 2003; Tegarden 1999). In particular, highlighting keywords in a document with noticeable colors has been found to be the most effective way to draw readers' attention and help them locate target words or sentences (Hoadley et al. 1996).

Some studies conducted in desktop environments (e.g., Fisher et al. 1989; Wu and Yuan 2002) have investigated the effect of keyword highlighting in information search tasks. Most of them found that keyword highlighting improved users' search performance. In this study, in addition to highlighting various keywords in different colors, the proposed colored keyword highlighting adaptation also automatically counts and displays the number of keyword occurrences within every branch at each level of the tree view. Such cues (i.e., information scent) in both the tree view and Web content itself can help users identify which tree branch should be explored and quickly scan through the content and locate the target information. We predict that such a positive impact of colored keyword highlighting should be extended to the mobile Web environment. The third hypothesis is proposed as follows:

H3. For information search via mobile Web browsing, adding colored keyword highlighting to the tree-view presentation adaptation will lead to

(a) reduction in search time,

(b) increase in search accuracy,

(c) increase in perceived ease of use, and

(d) increase in perceived usefulness.

Given the above-mentioned different types of presentation adaptation techniques, one might ask: Will more presentation adaptation features result in better user performance and perception? The presentation adaptation is aimed to better organize and present the Web content in the limited screen space in order to facilitate users' content scanning and skimming, as well as help them identify the relevant portion(s) of a Web page that may contain what they are looking for. Based on cognitive fit theory and information foraging theory, a larger number of useful information cues provided by presentation adaptation should generally help users find the target information more easily and quickly, thus improving their perceived ease of use and usefulness of the adaptive mobile Web system. Specifically, hierarchical text summarization and colored keyword highlighting adaptations provide two independent yet complementary information scents. We predict that the presence of additional effective adaptation features should offer more useful information cues, which can in turn lead to better user performance and perception. Our fourth hypothesis is as follows:

H4: For information search via mobile Web browsing, adding both hierarchical text summarization and colored keyword highlighting to tree-view adaptation will lead to (a) a greater reduction in search time, (b) a greater increase in search accuracy, (c) a greater increase in perceived ease of use, and (d) a greater increase in perceived usefulness than adding only hierarchical text summarization or colored keyword highlighting to tree-view adaptation.

## Task Complexity

The complexity of an information search task is “a central feature in determining the task performance and consequent information needs. It has been associated with the predeterminability of, or uncertainty about, the task” (Vakkari 1999, p. 825). According to Campbell’s (1988) framework of task complexity, there are four primary task characteristics that can increase task complexity:

(1) Multiple paths: Task complexity increases when there are multiple ways (i.e., paths) to perform a task, but only one of them leads to the desirable outcome.

(2) Multiple outcomes: When there are a number of desirable outcomes, task complexity increases because there is more information processing involved in the task.

(3) Conflicting interdependence: If achieving one desirable outcome conflicts with achieving another one, task complexity increases.

(4) Uncertain or probabilistic linkages: The uncertainty of selecting links from a large pool of potential paths to reach a desirable outcome increases task complexity.

Complex tasks of information search via Web browsing, which can be manifested by the large volume of content and/or the large number of hyperlinks within Web pages, may change the effect of presentation adaptation. Web browsing is considered a nonlinear reading behavior in which users have control over the order and inclusion/exclusion of information that they want to read (Charney 1987). When task complexity is low, information that needs to be processed and the number of decisions to be made are limited (Payne 1982). People normally rely on analytical processing when they have sufficient working memory for information processing (Speier and Morris 2003). Complex tasks contain much more information than simple tasks (Wood 1986), thus involving a higher cognitive load that requires significant attention and mental effort (Speier and Morris 2003). As a result, the working memory may not be sufficient to hold all of the information. People have to find other ways to reduce their cognitive load by relying more on perceptual process—visually perceiving information and understanding its meaning (Simon and Lea 1974)—because a perceptual process requires less cognitive effort than an analytical process (Payne et al. 1988; Speier and Morris 2003). Accordingly, the cognitive processing shifts from analytical to perceptual processes in complex tasks.

With tree view, users can perform nonlinear reading behavior on handheld devices due to restructuring of Web content that allows users to select topics of interest and skip the rest, which reduces the amount of required scrolling. Because tree view addresses the fundamental challenge in Web content presentation by reducing users' cognitive load, its benefit in improving mobile Web browsing/searching should be demonstrable in both simple and complex tasks.

Research on the relationship between task complexity and Web page structure has primarily applied the findings of earlier studies on menu structures (e.g., Jacko and Salvendy 1996; Norman and Chin 1998) to Web page structure (Galletta et al. 2006; Larson and Czerwinski 1998; Parush and Yuviler-Gavish 2004). Many studies have focused on the impact of the depth and breadth of Web page structure on navigation. Breadth refers to the number of options (e.g., hyperlinks or choices) per level, and depth refers to the number of levels in a hierarchy (Lazar 2005). On the one hand, people have a short-term memory that holds limited information within a limited time frame (Miller 1956). Directly presenting a complex Web page on a handheld device enforces users to do more scrolling (Jones et al. 1999), placing higher demands on users' short-term memory (Albers and Kim 2000). By offering several advantages in comparison to direct display of Web pages, such as reducing screen clutter and conveying content navigation structure, the hierarchical tree-view adaptation reduces the demands on users' short-term memory, as well as the cognitive load in keeping track of where they are located. From this perspective, the tree view would offer more benefit to users when browsing more complex Web pages (i.e., performing a more complex task). On the other hand, when a tree has greater breadth and depth, resulting from a complex Web page, the rigidity of the hierarchical tree view may cause difficulties in information search via browsing tasks. Users must make repeated choices at each level of the tree to determine which branch of the tree they should expand or backtrack through the hierarchy (i.e., branch selection). The evaluation of different alternatives increases the user's cognitive processing workload (Johnson and Payne 1985), which in turn would lead to longer task completion time and increased perception of disorientation and complexity (Galletta et al. 2006; Jacko and Salvendy 1996; Larson and Czerwinski 1998).

Similarly, the user perceived ease of use and usefulness of tree-view adaptation may not change as the complexity of information search via browsing tasks increases either, because a good fit between the task and the technology can mitigate the reduction of users' perceived ease of use and perceived usefulness as task complexity increases (Kamis et al. 2008). In view of such a trade-off, we predict that the effect of tree-view adaptation on user performance and perception will not vary with the task complexity. Our hypothesis about no moderating effect of task complexity on the impact of tree-view adaptation is as follows:

H5: Search task complexity will not moderate the effect of tree-view adaptation on

(a) search time,

(b) search accuracy,

(c) perceived ease of use, or

(d) perceived usefulness.

The hierarchical tree-view structure requires a user either to recall or to discover a pathway from the present location to the target location. As the depth and breadth of a hierarchical tree increase with the complexity of a Web page, the user must examine and compare each alternative tree branch so as to determine the most promising path to accomplish the task (Campbell 1988; Newell and Simon 1972). When cognitive processing demands are high, people tend to narrow their attention on relevant cues and conspicuous information (Berlyne 1997; Speier et al. 2003). Researchers have suggested that visual presentation and link labels would help users alleviate their cognitive load in complex information search tasks and make users perceive complex tasks to be less complex (Campbell and Maglio 1999; Kosslyn 1989; Nadkarni and Gupta 2007; Speier and Morris 2003). Those link labels “may act as cues to enable interpretation and lead to more informed navigational choices” (Baron et al. 1996, p. 899).

Larson and Czerwinski (1998) suggest that hierarchical structures with a strong scent for the target information at the top levels of the hierarchy would perform better than those without. Both hierarchical text summarization and colored keyword highlighting adaptations are aimed at enhancing information scent in the tree-view hierarchy to alleviate users' cognitive load and efforts, especially when browsing complex Web pages. Buyukkokten et al. (2001) argue that summarization adds more value to larger documents. The proposed hierarchical text summarization adaptation generates a summary for every single branch of interest at all levels of the tree view. Those summaries are expected to provide useful cues to users when they select a path in the hierarchy to reach the target information, thus improving the tree view by reducing users' cognitive load and improving their performance and perception. The positive influence of summaries is expected to be greater when browsing complex Web sites than simple ones because those information cues are more important to users for path selection in a more complex tree hierarchy. Therefore, our hypothesis about the moderating effect of task complexity on the impact of hierarchical text summarization is as follows:

H6: The greater the search task complexity, the greater the positive effect of adding hierarchical text summarization to tree-view adaptation on

(a) search time,

(b) search accuracy,

(c) perceived ease of use, and

(d) perceived usefulness.

Another common approach to reducing cognitive processing is through the use of visualization techniques that reduce the amount of information examined (Smelcer and Carmel 1997). One important perceptual property of human beings is preattentiveness (Triesman 1985), which refers to visual properties that a person can perceive in fewer than 250 milliseconds without having to scan the visual field serially (Ware 2004). Preattentiveness explains why a small amount of color highlighting is so effective at drawing the attention. Especially, this perceptual property becomes more important to information search in complex Web sites.

In addition to highlighting all the keywords appearing in a specific content section, the proposed colored keyword highlighting adaptation also presents the total count of each keyword appearance within each subsection in tree view. Those scents available in both the tree view and the content itself would not only reduce users' effort in choosing an appropriate path in the tree-view hierarchy, but also help them quickly identify information of interest through those keywords highlighted in different colors. The more complex the Web pages are, the more positive impact and help those scents would provide. Therefore, our hypothesis about the moderating effect of task complexity on the effect of colored keyword highlighting is as follows:

H7. The greater the search task complexity, the greater the positive effect of adding colored keyword highlighting to tree-view adaptation on

(a) search time,

(b) search accuracy,

(c) perceived ease of use, and

(d) perceived usefulness

Finally, as the complexity of information search via browsing task increases (e.g., larger amount of Web content with more hyperlinks), the need for information scents to help locate desirable information will be stronger. As discussed earlier, we predict that task complexity positively moderates the individual effect of hierarchical text summarization and colored keyword highlighting on users' information search performance and perception. Therefore, we expect that as task complexity increases, the effect of adding integrated adaptation of hierarchical text summarization and colored keyword highlighting to tree view will be stronger than that of adding hierarchical text summarization and colored keyword highlighting separately. Our final hypothesis is proposed as follows:

H8: The greater the search task complexity, the greater the positive effect of adding both hierarchical text summarization and colored keyword highlighting, as compared to adding only one of them, to tree-view adaptation on (a) search time,

(b) search accuracy,

(c) perceived ease of use, and

(d) perceived usefulness.

## Research Methodology

The hypotheses were tested through a controlled laboratory experiment with a $5 \times 2$ factorial design with presentation adaptation (five conditions of presentation adaptation) being a within-subjects factor and task complexity (high complexity versus low complexity) being a between-subjects factor. Participants were asked to perform two information search tasks via Web browsing independently using five different mobile Web systems. A different Web site was randomly selected for each presentation adaptation condition from five pre-identified Web sites. Each participant was randomly assigned to one of the two groups (i.e., low- and high-complexity task groups), and was asked to answer two different questions about each designated Web site. The laboratory testing allows participants to concentrate on the given tasks and minimizes potential confounding effects of other factors, such as lighting, user mobility, and other distractions, on the use of mobile devices that often exist in field studies.

## Mobile Web Prototype Systems

We developed mobile Web prototype systems using Java Servlet, Java Micro Edition (Java ME), and Sun's Java ME Wireless toolkit. The IBM J9 runtime environment was used as the Java Virtual Machine to run on the HP iPAQ h4355 Pocket PC, the PDA we used in the experiment. PDAs have been widely used for reading eBooks and browsing Web content. They are considered to be a more representative mobile device than cell phones for this type of task (Barnard et al. 2005). The HP iPAQ h4355 Pocket PC provides integrated Bluetooth and WLAN 802.11b for wireless communication and Internet access. It has 32MB Flash ROM, 64MB SDRAM, $240 \times 320$ display resolution, and a 3.5 inch transflective screen.

To test the hypotheses, we implemented five different prototype systems. The first system (O) directly displayed an original Web page in the IE browser without any adaptation (see Figure A1 in Appendix A). The second prototype system (T) was equipped with tree-view adaptation by adopting DOM, a standard that creates a logical structure of HTML and XML documents in the form of tree-like representation (W3C 2005). Each node in a DOM tree represents an object embedded in a Web document. Examples of objects are HTML/XML tags, images, and text. These objects are related to each other as parent or child nodes in the tree-view, and the child nodes of the same parent node are at the same level in the tree hierarchy (see Figure A2 in Appendix A). We developed an algorithm that generates the DOM tree of a Web page at run time. When a user opens a Web page using this version of the mobile Web system, an overview of the page structure is presented in a tree hierarchy. The user can then expand any section (i.e., a tree branch) to view its detailed content or subsection list by clicking on the bullet preceding the section title (see Figure A3 in Appendix A).

The third system (T+S) enhanced tree view with hierarchical text summarization. There are two major approaches to automatic text summarization: knowledge-poor (extraction) and knowledge-rich (abstraction) methods. The former generates a summary by selecting salient units from a document and concatenating them without changing any words or structure in the units (Hahn and Reimer 1999). In contrast, the knowledge-rich approach applies natural language processing techniques, including grammar and lexicons for syntactic and possible semantic parsing, to generate a summary. Our focus in this study is not to explore different summarization approaches, but to examine the potential impact of hierarchical text summarization on information search. Thus, we adopt a commonly used heuristic approach to text summarization by extraction, which generates a summary by aggregating the first sentence of each paragraph in a Web page (Harper and Patel 2005). Users could view the summary of any content section by clicking on its section title in the tree view. Then, the system would present the summary in a popup window. If a user is interested in reading the full content after viewing its summary, he could click the “full content” button at the bottom of the interface (see Figure A4 in Appendix A).

The fourth mobile Web system (T+H) incorporated colored keyword highlighting into the tree-view adaptation. All of the words or phrases in a Web page that match the keywords or phrases specified in the user profile were automatically highlighted in different colors. In addition, colored keyword highlighting also provides the total counts of keyword appearances within each subsection in the tree view (see Figure A5 in Appendix A). The fifth version of the system (the ALL version) was implemented by integrating all three types of adaptations described above.

According to keywords and search engine statistics, $^{3}$ more than 84 percent of information search queries consist of three or fewer keywords. In our experiment, before using the T+H and ALL versions of the system, each participant selected three keywords from a list of ten system suggestions for each question to create or update his/her user profile in advance. Researchers have pointed out that the selection of search keywords is a common way to introduce experimenter bias to usability testing. People may have different ways to express the same concept (Käki and Aula 2008), thus resulting in significant differences in outcome that have little to do with the system interface or content presentation that is being evaluated. To control for this variability, participants are often asked to use specific keywords predetermined by researchers instead of choosing keywords by themselves in the experiment (Buyukkokten et al. 2001; Chi et al. 2007; Hearst 2009; Woodruff et al. 2001). Similarly, we did not allow participants to specify keywords completely on their own in this study. The candidate keywords were generated in a consistent manner based on the questions and domain-related terms, which simulates the generation of keywords in reality. Specifically, for any question and its associated Web page/site, half of the candidate keywords were nouns and noun phrases extracted from the question directly, and the other half came from the Web site. For example, for the question “What is the top speed of a new generation of the high-speed rail train FASTECH in Japan?,” the list of potential keywords for participants to choose from consists of nouns or noun phrases extracted from the question, including top speed, new generation, high-speed rail train, FASTECH, and Japan, as well as several other domain-related terms such as bullet train, speed record, and Shinkansen technology that appear in the Web site associated with the question.

In order to assess the effect of presentation adaptation, we tried to minimize the potential influence of other system functionalities. For example, participants were not allowed to use the “find” function of the Internet browser in all five systems. Enabling that function could complicate the interpretation of the results.

## Independent and Dependent Variables

## Independent Variables

Presentation adaptation was operationalized by five system conditions: direct presentation of an original Web site without any adaptation (O), tree-view adaptation (T), tree-view enhanced by hierarchical text summarization adaptation (T+S), tree-view enhanced by colored keyword highlighting adaptation (T+H), and integrated presentation adaptation (ALL—T+H+S). As discussed earlier, the tree view of the Web page structure is believed to be essential to the presentation adaptation for handheld devices. Therefore, the tree view adaptation was included in all adaptive system conditions.

A task is more complex when there are a large number of alternatives or attributes from which to choose from (Kamis et al. 2008; Payne et al. 1988). In this research, the task complexity was operationalized as within-document browsing and across-document browsing (Marchinonini 1995). Based on the information seeking behavior theory (Marchinonini 1995), within-document browsing refers to navigating a single Web page, while across-document browsing refers to navigating across multiple Web pages in order to find target information. Based on Campbell's (1988) framework of task complexity, there are distinct differences between within-document and across-document browsing tasks. First, compared to within-document browsing, across-document browsing involves many more potential paths (hyperlinks) for users to assess and explore, resulting in an increase of task complexity. Second, there is little uncertainty in within-document browsing because all information is contained inside the current Web page. In contrast, in across-document browsing, uncertainty will inevitably occur when users attempt to choose a hyperlink from a number of alternatives (Germonprez and Zigurs 2005). Adding the much increased content of Web sites, an information search task via across-document browsing is much more complex than via within-document browsing.

## Dependent Variables

Accuracy was measured by the percentage of correctly identified answers to the given questions. Participants were required to find answers from five Web sites using different versions of mobile Web systems (one Web site per system). There were two questions about each Web site. All questions were fact-based (see sample questions in Appendix C). The maximum score a participant could receive was 10 points, with 1 point for each correct answer. There were no partial credits. Participants had to write answers on paper. They could only see one question at a time and could not move to the next question until they either provided an answer or were asked to stop when the task time ran out. In the latter case, the participant's answer was considered incorrect. The cut-off time thresholds (3 minutes for simple tasks and 5 minutes for complex tasks) were determined based on a pilot study. They were much shorter than the time needed to read the entire content without skimming and scanning.

Search time was measured by the time that a participant took to find an answer to a given question (excluding the Web site downloading time). In the experiment, participants had to click a “start” button on the user interface when they were ready to open and browse a Web site. As soon as they found an answer to the current question, they pressed a “stop” button to stop the clock. The starting and ending time was automatically recorded by the system. The participants were not allowed to browse the Web site again once they had pressed the “stop” button. Both accuracy and search time for each mobile Web system were averaged over the two questions.

The instruments for measuring perceived ease of use and usefulness of presentation adaptation were adapted from those proposed in the technology acceptance model (Davis 1989). Perceived ease of use refers to the degree to which a user believes that adapted presentation can be used effortlessly, and perceived usefulness refers to the degree to which a user believes that presentation adaptation can improve his/her task performance. All of the survey questions were measured on a seven-point Likert scale, with 1 indicating “strongly disagree” and 7 indicating “strongly agree.”

## Tasks and Experimental Procedure

In order to minimize the learning effect, five different Web sites were selected for both low- and high-complexity tasks. Although those Web sites varied in their content—which were about geography, history, sports, nature, and science, respectively—they were carefully modified to have similar size and the same content structure so that the potential effect of length and structural difference can be ignored.

The simple tasks required participants to search for information by browsing a single Web page that did not contain any hyperlinks. The generated tree view of such pages had only one level that included nine items (i.e., nine sections). Participants had to get into one of those sections to look for an answer. The complex tasks involved a different set of five Web pages. The generated tree view of each complex Web site consisted of three levels, each containing 25 hyperlinks. Participants had to traverse across Web pages through those hyperlinks to find target Web pages that contained answers to the given questions. The total number of words in each Web site used for complex tasks was about 10 times of that for simple tasks (30,000 ± 200 words per Web site for complex tasks versus 3,000 ± 100 words for simple tasks). Answers to two questions related to a complex Web site were located in two separate Web pages. The order of questions was randomized.

To minimize the potential learning effects resulting from the within-subjects design (Boslaugh and Watters 2008), we randomized the sequence of five system conditions and the selection of Web sites for each system for each participant based on the Latin square design of size five (Maxwell and Delaney 2000). We conducted a pilot study with 10 undergraduate students, who were recruited from a public university located on the east coast of the United States. Each student owned a handheld device and had prior experience with mobile Web browsing. The results of the pilot study indicated that task requirements were clear and appropriate, and prototype systems were stable and reliable. No problems regarding systems and experimental procedures were reported.

Before starting the formal experiment, participants took a knowledge test that assessed their existing knowledge on the subject matters of selected Web sites and questions that would be used in the formal study. The test results revealed that none of the participants had any prior knowledge about those questions. The participants then went through a training session, in which they saw demonstrations of five versions of the mobile Web system and practiced a few information search exercises using the systems. The formal experiment started once the participants felt comfortable with using the systems.

During the formal experiment, the participants first performed information search tasks using one of the five mobile Web systems, and then completed a questionnaire related to their perceptions of the system they just used. This process was repeated for each of the other four mobile Web systems. Participants were instructed to find correct answers as quickly as possible. After participants completed all of the tasks, they were asked to rank the five systems in terms of their preference. In order to minimize the potential impact of confounding factors such as environment and mobility on user performance during the experiment, participants were asked not to pick up the PDA from a cradle placed on the table and were required to sit in their chair while browsing.

## Participants

A total of 60 university students participated in this study. Among them, 60 percent were male; 23 percent were graduate students, and 77 percent were undergraduates. Through a pre-study questionnaire, we ensured that all participants had prior experience with mobile Web browsing. Because university students are a major group of users of handheld devices, they are appropriate for this research. Participants were randomly assigned to one of the two task groups (25 participants in the simple task group and 35 in the complex task group). No significant difference was found in gender, age, and prior experience with the usage of handheld devices between participants in the two groups.

Each participant received \$10 in cash or extra course credits as compensation for their participation in this study. To further motivate participants to try their best in the tasks, we offered extra bonuses (extra \$30, \$20, \$10, and \$10) to the top four participants in each group who found all answers correctly with the shortest time.

## Data Analysis and Results

We used repeated measures ANOVA to analyze the effect of presentation adaptation and task complexity. We also used the Bonferroni multiple comparison because it is a robust method and is recommended to be used for multiple comparisons in the within-subjects design (Maxwell and Delaney 2000).

## Search Time

The descriptive statistics of search time is reported in Table 2. ANOVA on search time shows a significant main effect of presentation adaptation $(F(2,105)=83.1,p<0.05)$ and task complexity $(F(1,58)=53.47,p<0.05)$ , as well as the interaction effect $(F(2,105)=7.74,p<0.05)$ between presentation adaptation and task complexity. The significant interaction suggests that the effect of presentation adaptation could be moderated by task complexity; therefore, following Jiang and Benbasat's (2007) approach, we analyzed the search time in more detail by conducting multiple comparisons of presentation adaptations at each level of task complexity separately.

First, the search time used by participants when they used any of the four mobile Web systems with presentation adaptation was significantly less than the search time used by participants while using the mobile Web system without any adaptation (i.e., the O condition) $p < 0.01$ .

As shown in Tables 3 and 4, in both simple and complex tasks, tree-view adaptation (T) appears to lead to significantly less search time than no presentation adaptation (O) ( $p < 0.01$ ). Therefore, H1(a) is supported and H5(a) is supported. The difference in search time between the T and T+S conditions is close to significance in the complex task ( $p = 0.07$ ), but is far from significance in the simple task ( $p = 1.00$ ), so H2(a) is not supported, and H6(a) is supported. Further, the difference in search time between the T and T+H conditions is significant only in the complex task ( $p < 0.01$ ), but not in the simple task ( $p = 0.62$ ). Thus, H3(a) is partially supported and H7(a) is supported. There is no difference in search time between the T+H and ALL conditions ( $p > 0.05$ ), and the difference between the T+S and ALL conditions only exists in the complex task ( $p < 0.01$ ). Therefore, H4(a) and H8(a) are partially supported.

## Search Accuracy

The descriptive statistics of search accuracy is reported in Table 5. Repeated measure ANOVA on accuracy reveals a significant main effect of presentation adaptation ( $F(2,102)=13.05$ , p<0.01), but no significant main effect of task complexity ( $F(1,58)=2.88$ , p>0.05) and the interaction between task complexity and presentation adaptation ( $F(2,102)=13.05$ , p>0.05). Therefore, we combined data collected from both simple and complex tasks for analysis.

As the results of contrast analysis in Table 6 show, participants achieved higher accuracy when they used mobile Web systems with presentation adaptation (i.e., T, T+S, T+H, and ALL) than without any adaptation (O) (p < 0.01). Because tree-view adaptation (T) led to higher search accuracy than direct display without presentation adaptation (O), hypothesis H1(b) is supported. However, no difference in the search accuracy was detected among the four adaptive system conditions $p > 0.05$ . Therefore, hypotheses H2(b), H3(b), and H4(b) are not supported. Further, the lack of interaction effect between presentation adaptation and task complexity suggests that the impact of presentation adaptation on search accuracy is not moderated by task complexity. Therefore, hypothesis H5(b) is supported, but H6(b), H7(b), and H8(b) are not supported.

Table 2. Descriptive Statistics of Search Time

<table><tr><td rowspan="2">Presentation Adaptation</td><td rowspan="2">Task Complexity</td><td colspan="2">Search Time (Seconds)</td><td rowspan="2">Sample Size</td></tr><tr><td>Mean</td><td>Std. Dev.</td></tr><tr><td rowspan="2">O</td><td>High</td><td>173.06</td><td>13.43</td><td>35</td></tr><tr><td>Low</td><td>90.52</td><td>10.19</td><td>25</td></tr><tr><td rowspan="2">T</td><td>High</td><td>91.12</td><td>8.52</td><td>35</td></tr><tr><td>Low</td><td>29.56</td><td>3.64</td><td>25</td></tr><tr><td rowspan="2">T+S</td><td>High</td><td>71.71</td><td>5.97</td><td>35</td></tr><tr><td>Low</td><td>25.53</td><td>3.60</td><td>25</td></tr><tr><td rowspan="2">T+H</td><td>High</td><td>47.02</td><td>2.91</td><td>35</td></tr><tr><td>Low</td><td>21.92</td><td>1.80</td><td>25</td></tr><tr><td rowspan="2">ALL</td><td>High</td><td>51.01</td><td>3.62</td><td>35</td></tr><tr><td>Low</td><td>24.80</td><td>2.61</td><td>25</td></tr></table>

Table 3. The Results of Multiple Comparisons on Search Time in Simple Tasks

<table><tr><td>(I) Group</td><td>(J) Group</td><td>Mean Difference (I-J)</td><td>Std. Error</td><td>Sig.</td></tr><tr><td rowspan="4">O</td><td>T</td><td>60.96</td><td>9.83</td><td>0.00**</td></tr><tr><td>T+S</td><td>64.99</td><td>10.21</td><td>0.00**</td></tr><tr><td>T+H</td><td>68.61</td><td>9.69</td><td>0.00**</td></tr><tr><td>ALL</td><td>65.72</td><td>10.58</td><td>0.00**</td></tr><tr><td rowspan="3">T</td><td>T+S</td><td>4.03</td><td>5.47</td><td>1.00</td></tr><tr><td>T+H</td><td>7.65</td><td>3.90</td><td>0.62</td></tr><tr><td>ALL</td><td>4.75</td><td>3.67</td><td>1.00</td></tr><tr><td rowspan="2">T+S</td><td>T+H</td><td>3.62</td><td>4.01</td><td>1.00</td></tr><tr><td>ALL</td><td>0.73</td><td>4.64</td><td>1.00</td></tr><tr><td>T+H</td><td>ALL</td><td>-2.89</td><td>3.09</td><td>1.00</td></tr></table>

\*\*p<0.01

Table 4. The Results of Multiple Comparisons on Search Time in Complex Tasks

<table><tr><td>(I) Group</td><td>(J) Group</td><td>Mean Difference (I-J)</td><td>Std. Error</td><td>Sig.</td></tr><tr><td rowspan="4">O</td><td>T</td><td>81.94</td><td>13.02</td><td>0.00**</td></tr><tr><td>T+S</td><td>100.34</td><td>12.73</td><td>0.00**</td></tr><tr><td>T+H</td><td>126.03</td><td>12.18</td><td>0.00**</td></tr><tr><td>ALL</td><td>122.05</td><td>12.66</td><td>0.00**</td></tr><tr><td rowspan="3">T</td><td>T+S</td><td>18.40</td><td>6.46</td><td>0.07</td></tr><tr><td>T+H</td><td>44.09</td><td>6.69</td><td>0.00**</td></tr><tr><td>ALL</td><td>40.11</td><td>7.06</td><td>0.00**</td></tr><tr><td rowspan="2">T+S</td><td>T+H</td><td>25.69</td><td>4.74</td><td>0.00**</td></tr><tr><td>ALL</td><td>21.71</td><td>5.02</td><td>0.00**</td></tr><tr><td>T+H</td><td>ALL</td><td>-3.98</td><td>2.83</td><td>1.00</td></tr></table>

$^{*}p <   0.05;^{**}p <   0.01$

<table><tr><td colspan="4">Table 5. Descriptive Statistics of Accuracy (%)</td></tr><tr><td rowspan="2">Presentation Adaptation</td><td rowspan="2">Task Complexity</td><td colspan="2">Accuracy (Percentage of Correct Answers)</td></tr><tr><td>Mean</td><td>Std. Dev.</td></tr><tr><td rowspan="3">O</td><td>High</td><td>77.1</td><td>30.54</td></tr><tr><td>Low</td><td>86.0</td><td>27.08</td></tr><tr><td>Total</td><td>80.8</td><td>29.24</td></tr><tr><td rowspan="3">T</td><td>High</td><td>95.7</td><td>14.20</td></tr><tr><td>Low</td><td>98.0</td><td>10.00</td></tr><tr><td>Total</td><td>96.7</td><td>12.58</td></tr><tr><td rowspan="3">T+S</td><td>High</td><td>94.3</td><td>16.14</td></tr><tr><td>Low</td><td>100.0</td><td>0.00</td></tr><tr><td>Total</td><td>96.7</td><td>12.58</td></tr><tr><td rowspan="3">T+H</td><td>High</td><td>98.6</td><td>8.45</td></tr><tr><td>Low</td><td>98.0</td><td>10.00</td></tr><tr><td>Total</td><td>98.3</td><td>9.05</td></tr><tr><td rowspan="3">ALL</td><td>High</td><td>98.6</td><td>8.45</td></tr><tr><td>Low</td><td>100.0</td><td>0.00</td></tr><tr><td>Total</td><td>99.2</td><td>6.45</td></tr></table>

<table><tr><td colspan="5">Table 6. The Results of Multiple Comparisons on Accuracy (%)</td></tr><tr><td>(I) Group</td><td>(J) Group</td><td>Mean Difference (I-J)</td><td>Std. Error</td><td>Sig.</td></tr><tr><td rowspan="4">O</td><td>T</td><td>-15.8</td><td>4</td><td>0.004**</td></tr><tr><td>T+S</td><td>-15.8</td><td>4</td><td>0.004**</td></tr><tr><td>T+H</td><td>-17.5</td><td>4</td><td>0.002**</td></tr><tr><td>ALL</td><td>-18.3</td><td>4</td><td>0.00**</td></tr><tr><td rowspan="3">T</td><td>T+S</td><td>0</td><td>2</td><td>1.00</td></tr><tr><td>T+H</td><td>-1.7</td><td>2</td><td>1.00</td></tr><tr><td>ALL</td><td>-2.5</td><td>2</td><td>0.99</td></tr><tr><td rowspan="2">T+S</td><td>T+H</td><td>-1.7</td><td>2</td><td>1.00</td></tr><tr><td>ALL</td><td>-2.5</td><td>1</td><td>1.00</td></tr><tr><td>T+H</td><td>ALL</td><td>-0.8</td><td>2</td><td>1.00</td></tr></table>

\*\*p<0.01

## Perceived Ease of Use

The descriptive statistics of perceived ease of use (PEOU) and perceived usefulness (PU) are presented in Table 7. Cronbach's alpha of PEOU and that of PU of Mobile Web systems are 0.78 and 0.95, respectively, showing high reliability. ANOVA reveals a significant main effect of presentation adaptation $(F(3,163)=144.65, p<0.01)$ , task complexity $(F(1,58)=8.36, p<0.01)$ , and the interaction between presentation adaptation and task complexity $(F(3,163)=4.56, p<0.01)$ on PEOU. The significant interaction effect suggests that the effect of presentation adaptation on PEOU could be moderated by task complexity; therefore, we analyze it in more detail by conducting multiple comparisons of presentation adaptation on PEOU at two levels of task complexity separately. The results are shown in Table 8 and Table 9, respectively.

<table><tr><td colspan="6">Table 7. Descriptive Statistics of Perceived Ease of Use and Perceived Usefulness</td></tr><tr><td rowspan="2">Presentation Adaptation</td><td rowspan="2">Task Complexity</td><td colspan="2">Perceived Ease of Use</td><td colspan="2">Perceived Usefulness</td></tr><tr><td>Mean</td><td>Std. Dev.</td><td>Mean</td><td>Std. Dev.</td></tr><tr><td rowspan="2">O</td><td>High</td><td>3.94</td><td>1.15</td><td>2.63</td><td>1.30</td></tr><tr><td>Low</td><td>3.93</td><td>0.80</td><td>2.41</td><td>1.06</td></tr><tr><td rowspan="2">T</td><td>High</td><td>5.73</td><td>0.71</td><td>5.31</td><td>0.86</td></tr><tr><td>Low</td><td>6.37</td><td>0.56</td><td>5.96</td><td>0.90</td></tr><tr><td rowspan="2">T+S</td><td>High</td><td>5.51</td><td>1.06</td><td>5.42</td><td>1.07</td></tr><tr><td>Low</td><td>6.41</td><td>0.62</td><td>6.04</td><td>0.63</td></tr><tr><td rowspan="2">T+H</td><td>High</td><td>6.19</td><td>0.72</td><td>6.36</td><td>0.68</td></tr><tr><td>Low</td><td>6.41</td><td>0.52</td><td>6.55</td><td>0.42</td></tr><tr><td rowspan="2">ALL</td><td>High</td><td>6.12</td><td>0.78</td><td>6.33</td><td>0.77</td></tr><tr><td>Low</td><td>6.5</td><td>0.57</td><td>6.56</td><td>0.51</td></tr></table>

Table 8. Multiple Comparisons on Perceived Ease of Use in Simple Tasks

<table><tr><td>(I) Group</td><td>(J) Group</td><td>Mean Difference (I-J)</td><td>Std. Error</td><td>Sig.</td></tr><tr><td rowspan="4">O</td><td>T</td><td>-2.44</td><td>0.17</td><td>0.00**</td></tr><tr><td>T+S</td><td>-2.48</td><td>0.21</td><td>0.00**</td></tr><tr><td>T+H</td><td>-2.48</td><td>0.19</td><td>0.00**</td></tr><tr><td>ALL</td><td>-2.57</td><td>0.21</td><td>0.00**</td></tr><tr><td rowspan="3">T</td><td>T+S</td><td>-0.04</td><td>0.099</td><td>1.00</td></tr><tr><td>T+H</td><td>-0.04</td><td>0.10</td><td>1.00</td></tr><tr><td>ALL</td><td>-0.13</td><td>0.099</td><td>1.00</td></tr><tr><td rowspan="2">T+S</td><td>T+H</td><td>0.00</td><td>0.10</td><td>1.00</td></tr><tr><td>ALL</td><td>-0.09</td><td>0.08</td><td>1.00</td></tr><tr><td>T+H</td><td>ALL</td><td>-0.09</td><td>0.08</td><td>1.00</td></tr></table>

\*\*p<0.01

Tables 8 and 9 show that the tree-view adaptation improves PEOU considerably in both simple and complex tasks (p < 0.01), so H1(c) is supported and H5(c) is supported. However, no difference was detected in PEOU between the T and T+S conditions for both simple and complex tasks (p > 0.05), suggesting that providing hierarchical text summaries did not further improve PEOU of the mobile Web system. Therefore, H2(c) and H6(c) are not supported. Despite there being no significant difference in PEOU between the T and T+H conditions for simple tasks, providing colored keyword highlighting for tree view was found to further improve the PEOU in complex tasks (p < 0.05). So H3(c) is partially supported and H7(c) is supported. Finally, the effect of adding both hierarchical text summarization and colored keyword highlighting to tree view (ALL), in comparison to the effect of adding only hierarchical text summarization to tree view, is significant in complex tasks (p < 0.01) but insignificant in simple tasks (p > 0.05); however, the effect, in comparison to adding only colored keyword highlighting to tree view, did not vary with the task complexity. Therefore, H4(c) and H8(c) are partially supported.

<table><tr><td colspan="5">Table 9. Multiple Comparisons on Perceived Ease of Use in Complex Tasks</td></tr><tr><td>(I) Group</td><td>(J) Group</td><td>Mean Difference (I-J)</td><td>Std. Error</td><td>Sig.</td></tr><tr><td rowspan="4">O</td><td>T</td><td>-1.79</td><td>0.20</td><td>0.00**</td></tr><tr><td>T+S</td><td>-1.56</td><td>0.22</td><td>0.00**</td></tr><tr><td>T+H</td><td>-2.25</td><td>0.19</td><td>0.00**</td></tr><tr><td>ALL</td><td>-2.18</td><td>0.18</td><td>0.00**</td></tr><tr><td rowspan="3">T</td><td>T+S</td><td>0.23</td><td>0.17</td><td>1.00</td></tr><tr><td>T+H</td><td>-0.46</td><td>0.14</td><td>0.02*</td></tr><tr><td>ALL</td><td>-0.39</td><td>0.12</td><td>0.03*</td></tr><tr><td rowspan="2">T+S</td><td>T+H</td><td>-0.69</td><td>0.20</td><td>0.01*</td></tr><tr><td>ALL</td><td>-0.61</td><td>0.13</td><td>0.00**</td></tr><tr><td>T+H</td><td>ALL</td><td>0.07</td><td>0.14</td><td>1.00</td></tr></table>

$^{*}p <   0.05;^{**}p <   0.01$

## Perceived Usefulness

Repeated measures ANOVA of users' PU of the mobile Web systems yielded significant effects of presentation adaptation $F(3,166)=235.82, p<0.01$ , task complexity $F(1,58)=4.95, p<0.05$ , and their interaction $F(3,166)=235.82, p<0.01$ , indicating that the effect of presentation adaptation on PU could be moderated by task complexity. Therefore, we investigated the effect of presentation adaptation on PU at the two levels of task complexity separately.

Tables 10 and 11 show that in both simple and complex tasks, tree-view presentation adaptation resulted in higher levels of perceived usefulness (PU) than the system without any presentation adaptation ( $p < 0.01$ ). Therefore, H1(d) and H5(d) are supported. There was no significant difference in PU between the T and T+S conditions ( $p = 1.00$ ) for both simple and complex tasks, suggesting that adding hierarchical text summarization did not further improve PU. Therefore, H2(d) and H6(d) are not supported. The difference in PU between the T and T+H conditions was only significant for complex tasks ( $p < 0.01$ ), so H3(d) is partially supported and H7(d) is supported. Although the ALL condition results in higher levels of PU than the T+S condition for both simple and complex tasks, the effect is greater for the complex tasks ( $p < 0.01$ ) than for the simple tasks ( $p < 0.05$ ). However, there was no significant difference between the ALL and T+H conditions ( $p = 1.00$ ) for both simple and complex tasks. Therefore, H4(d) and H8(d) are partially supported.

The results of ranking five systems in terms of participants' preference for accessing the Web via mobile handheld devices reveal that the ALL version was the favorite system, with 40 participants (66.67 percent) rating it as the best system. In descending order of participants' preference, the other systems are T+H, T+S, T, and O. It is also worth noting that most participants preferred the systems with more presentation adaptation features to those with fewer features. The hypotheses testing results are summarized in Table 12.

## Discussion

## Findings

There are several major findings of this study. First, the tree-view based presentation adaptation can significantly reduce the search time and increase the accuracy of information search via Web browsing on a handheld device, as well as increase perceived ease of use and usefulness of mobile Web systems. The results strongly indicate that providing the structure of Web content in a hierarchical format, which enables users to quickly locate information of interest without having to navigate the entire Web page, is effective for Web browsing on a handheld device.

Second, hierarchical text summarization provided on top of tree view did not have the significant impact on user performance in information search and perception of mobile Web systems as we expected. There are a few possible reasons for these surprising findings.

(1) The naïve approach that we used to generate text summaries may not be sufficiently effective for the Web pages selected in this study.

(2) Due to technical difficulty, in the experiment, the summary of a section/subsection was not displayed automatically as a desirable stylus-over event, but was displayed in a new pop-up window upon a user click. The user had to click on another tab to either view the full content of the section/subsection or go back to the tree-view page. Such an extra step could have compromised the potential benefits of summaries.

<table><tr><td colspan="5">Table 10. Multiple Comparisons of Perceived Usefulness in Simple Tasks</td></tr><tr><td>(I) Group</td><td>(J) Group</td><td>Mean Difference (I-J)</td><td>Std. Error</td><td>Sig.</td></tr><tr><td rowspan="4">O</td><td>T</td><td>-3.55</td><td>0.25</td><td>0.00**</td></tr><tr><td>T+S</td><td>-3.63</td><td>0.24</td><td>0.00**</td></tr><tr><td>T+H</td><td>-4.13</td><td>0.25</td><td>0.00**</td></tr><tr><td>ALL</td><td>-4.15</td><td>0.28</td><td>0.00**</td></tr><tr><td rowspan="3">T</td><td>T+S</td><td>-0.08</td><td>0.18</td><td>1.00</td></tr><tr><td>T+H</td><td>-0.59</td><td>0.19</td><td>0.054</td></tr><tr><td>ALL</td><td>-0.60</td><td>0.19</td><td>0.04*</td></tr><tr><td rowspan="2">T+S</td><td>T+H</td><td>-0.51</td><td>0.12</td><td>0.003**</td></tr><tr><td>ALL</td><td>-0.52</td><td>0.14</td><td>0.01*</td></tr><tr><td>T+H</td><td>ALL</td><td>-0.01</td><td>0.09</td><td>1.00</td></tr></table>

$^{*}p <   0.05;^{**}p <   0.01$

Table 11. Multiple Comparisons of Perceived Usefulness in Complex Tasks

<table><tr><td>(I) Group</td><td>(J) Group</td><td>Mean Difference (I-J)</td><td>Std. Error</td><td>Sig.</td></tr><tr><td rowspan="4">O</td><td>T</td><td>-2.68</td><td>0.26</td><td>0.00**</td></tr><tr><td>T+S</td><td>-2.78</td><td>0.26</td><td>0.00**</td></tr><tr><td>T+H</td><td>-3.72</td><td>0.25</td><td>0.00**</td></tr><tr><td>ALL</td><td>-3.70</td><td>0.24</td><td>0.00**</td></tr><tr><td rowspan="3">T</td><td>T+S</td><td>-0.11</td><td>0.21</td><td>1.00</td></tr><tr><td>T+H</td><td>-1.05</td><td>0.16</td><td>0.00**</td></tr><tr><td>ALL</td><td>-1.02</td><td>0.17</td><td>0.00**</td></tr><tr><td rowspan="2">T+S</td><td>T+H</td><td>-0.94</td><td>0.22</td><td>0.00**</td></tr><tr><td>ALL</td><td>-0.91</td><td>0.14</td><td>0.00**</td></tr><tr><td>T+H</td><td>ALL</td><td>0.03</td><td>0.15</td><td>1.00</td></tr></table>

\*\*p < 0.01

<table><tr><td colspan="5">Table 12. A Summary of Hypotheses Testing Results</td></tr><tr><td>Hypotheses</td><td>Search Time</td><td>Accuracy</td><td>Perceived Ease of Use</td><td>Perceived Usefulness</td></tr><tr><td>H1: The effect of tree-view adaptation</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>H2: The effect of adding hierarchical text summarization</td><td>N</td><td>N</td><td>N</td><td>N</td></tr><tr><td>H3: The effect of adding colored keyword highlighting</td><td>P</td><td>N</td><td>P</td><td>P</td></tr><tr><td>H4: The effect of adding hierarchical text summarization and colored keyword highlighting</td><td>P</td><td>N</td><td>P</td><td>P</td></tr><tr><td>H5: No moderating effect of task complexity on tree-view</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>H6: The moderating effect of task complexity on adding hierarchical text summarization</td><td>Y</td><td>N</td><td>N</td><td>N</td></tr><tr><td>H7: The moderating effect of task complexity on adding colored keyword highlighting</td><td>Y</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td>H8: The moderating effect of task complexity on adding both hierarchical text summarization and colored keyword highlighting</td><td>P</td><td>N</td><td>P</td><td>P</td></tr></table>

Y = Supported; N = Not supported; P = Partially supported

(3) For the goal-oriented task of finding specific facts, text summaries may not be able to precisely indicate the location of the specific facts for which the user is looking.

Third, providing colored keyword highlighting in tree view reduced search time by enabling users to perform effective scanning/skimming. The positive impact of colored keyword highlighting on PEOU and PU of mobile Web systems was moderated by task complexity, which was manifested by its stronger effect for complex search tasks than for simple tasks.

Fourth, the results show that the effects of presentation adaptations are generally greater for complex tasks than for simple tasks. This suggests that as task complexity increases, presentation adaptation will provide greater benefits.

Fifth, providing additional presentation adaptation (e.g., colored keyword highlighting) to the tree view could further improve users' information search performance and perception. However, such improvement is not guaranteed (e.g., hierarchical text summarization in this study). Our results imply that the number of additional presentation adaptation features may not be important. It is, instead, the type of feature that matters. If an adaptation feature does not fit the task or is complicated to use, it may not have a positive impact.

Finally, although adaptive mobile Web systems led to higher search accuracy than the system without any adaptation, the differences in search accuracy were not significant among those adaptive systems, mainly because, with the help of any presentation adaptation, almost all participants were able to find accurate answers from Web sites within the task time frame.

## Theoretical Contributions

This research investigates the effect of presentation adaptation on user performance and perception in information search via Web browsing. To the best of our knowledge, this is the first empirical study that evaluates the effect of those presentation adaptation techniques on mobile Web browsing using physical handheld devices. This research provides several major theoretical contributions.

First, our results demonstrate the importance and benefits of presentation adaptation to Web browsing on handheld devices. This research provides theoretical insights on how to improve the effectiveness of mobile Web browsing. It makes contributions to the interface design for mobile devices, specifically for Web page presentation. Fundamentally, the findings of this study suggest that a presentation adaptation method should (1) present information to users in a concise and well-organized manner that supports effective skimming and scanning; (2) enable users to explore information without losing context; and (3) make important information stand out. Specifically, providing information about the structure and themes of a Web page in a hierarchical tree view and adding colored keyword highlighting are proven to be effective.

Second, in addition to examining various presentation adaptation approaches, this research goes one step further by revealing that the task complexity can influence the impact of presentation adaptation. The effect of presentation adaptation on user performance and perception in information search via browsing on handheld devices will be greater as the complexity of Web pages increases. These findings provide a variety of insights for research on mobile HCI and context-aware mobile applications. Because the complexity of Web pages has been continuously increasing, presentation adaptation becomes increasingly important for mobile Web users.

Third, this research utilizes cognitive fit theory and information foraging theory as theoretical foundations when proposing presentation adaptation methods for mobile Web browsing. Extant studies on presentation adaptation methods for mobile devices lack theoretical support. The results of this study indicate that the cognitive fit theory could be well extended to the mobile Web context. Any presentation adaptation approach that reduces users' cognitive load, such as tree view, should help improve their performance in mobile Web browsing tasks. Providing hierarchical text summarization adaptation in tree view was not found useful in this study. This could be attributed to the lack of fit between the task and the implementation of this adaptation feature. McDonald and Chen (2006) suggest that the benefits of a text summary primarily depend on the task. We speculate that for an information search task, users may perform better with query-based summaries (i.e., summaries generated mainly based on user queries) than the traditional generic summaries used in this study. The latter may be more beneficial and suitable when users have no specific goals in mind.

Even though adaptation through hierarchical text summarization involved extra steps in this study, it didn't deteriorate user performance. The addition of colored keyword highlighting to tree-view adaptation improved users' searching performance and perception of mobile Web systems. On the one hand, those findings suggest that the basic principle of information foraging theory is generally applicable to mobile Web browsing. On the other hand, the nonsignificant text summarization adaptation implies that certain information cues that have been proven effective in information search on desktop computers are not effective for handheld devices. As a result, some traditional information cues and methods that provide those cues may need to be modified or customized for handheld devices.

Fourth, one of the major limitations of prior research on mobile computing is the lack of empirical studies using real handheld devices (Zhang et al. 2009). This study sets up an example of conducting empirical research with mobile handheld devices. Although using real devices poses more technical challenges than using emulators, the research findings obtained from actual user–device interaction are more convincing and generally applicable.

## Practical Implications

The findings of this study also provide several practical guidelines for the adaptation of Web page presentation on handheld devices. First, effective scanning and skimming are important to information search via mobile Web browsing. Therefore, adapting the presentation of Web content in a way that allows users to see an outline of content first is essential. This study also indicates that task complexity is a vital factor in the usability of presentation adaptation systems. System engineers need to clearly understand the nature of tasks before designing and implementing adaptation features. For example, users could be provided with more effective presentation adaptation schemes when they are dealing with complex Web sites.

Mobile Web systems should provide users with a colored keyword highlighting feature to support their information search process. In our post-study interviews, all participants agreed that this feature was very helpful for the search tasks. In practice, the keywords indicating users' interest can be acquired by different methods, including explicit user feedback, implicit feedback, or direct user solicitation (Kelly 2004; Spool et al. 1999). Designers of mobile systems should consider including effective input mechanisms that enable users to enter their keywords with ease if the direct solicitation method is used.

Although it could be helpful to provide a variety of presentation adaptation features from which users may choose, caution should be taken in the design and integration of those features. In this study, the majority of participants chose the ALL version of mobile Web system as the favorite because it had the largest number of presentation adaptation features.

On the other hand, the incorporation of additional adaptation features may introduce other usability issues, such as potentially increasing the complexity of the system. Hence, system designers should carefully consider how adaptation features can be seamlessly integrated so as to maximize the benefit of individual adaptation techniques and the system usability simultaneously.

## Limitations and Future Research

The proposed hybrid presentation adaptation approach is by no means complete and optimal. Like all other studies on mobile applications, this research has some limitations due to resource constraints and technical challenges. First, our experiment was conducted in a laboratory setting, which does not completely reflect all possible usage situations of handheld devices. For example, in our study, the mobile device was placed on a table. In reality, users may use mobile devices when they are on the move. Therefore, it would be interesting to conduct a field study in the future.

Second, the current scope of the tree-view adaptation approach deals with static HTML pages only. It does not handle the display of multimedia content such as video, dynamic HTML, and other types of decorating graphical presentation. We plan to enhance the tree-view adaptation so that it can handle heterogeneous Web content. Moreover, because this study did not use tree view with four or more levels, we need to validate whether or not the findings will hold true for even more complicated Web sites that have deeper and broader tree structures and thereby increase the difficulty in tree navigation and search (Lazar 2005). From a tree search perspective, a deep tree can cause a well-known problem in tree traversal, namely combinatorial explosion, resulting in many alternative paths to be explored, which could negatively influence the effectiveness of tree-view based presentation. Therefore, it may be necessary to seek a balance between the depth and breadth of the tree-view or trim the generated tree-view of complex Web sites based on knowledge about the user's interest and preferences (e.g., based on previous browsing history or user profiles). As a result, regardless of how complex an original Web page could be, the generated DOM tree should be simple while sufficiently informative for effective browsing.

Third, one of the major objectives of this study is to examine the effect of keyword highlighting adaptation. To avoid the potential confounding effect, we followed a compromised approach by allowing participants to choose keywords from a list of 10 candidates, as described in the section on mobile Web prototype systems. In this way, we reduced the potential experiment bias incurred by self-determination of keywords while emulating the user keyword selection to some extent. That being said, it would be more natural if participants were able to choose keywords on their own. In addition, we excluded the time that participants took to select keywords from the task completion time. Although such a treatment is common in studies on information seeking behavior, keyword selection or entry would increase the overhead of the colored keyword highlighting adaptation in comparison to other adaptation approaches, especially when the keywords have to be changed constantly.

We had demonstrated all five systems in the training session before the participants started the formal experiment. Seeing and practicing those systems in advance would not have influenced participants' search performance due to the randomization of the sequence of five system conditions in the experiment. They might, however, have an effect on participants' perceptions of those systems.

There are other potential future research issues. In mobile environments, other context information such as time, location, environment (e.g., ambient light), and the user's ongoing activities can also be utilized to provide more advanced, intelligent presentation adaptation to make mobile Web live up to its potential. For example, a system can automatically enlarge the font size of a Web page when it detects that the environment is dark, or automatically remove advertisements, large-size images, and irrelevant sections from a Web page when the network traffic is heavy.

Even though adding hierarchical text summarization to tree view did not result in improvement of user performance and user perception in this study, it is premature to claim that summarization is not helpful in mobile Web browsing. It is worthwhile to examine the impact of hierarchical text summarization using a more advanced text summarization approach and stylus-over display in future research. Another potential future research issue is to investigate the effectiveness of presentation adaptation using other information search or browsing tasks such as information browsing without specific goals (Marchinonini 1995).

With the explosive growth of handheld device users, using presentation adaptation to enable more effective and ubiquitous information access via mobile Web will have a far-reaching impact.

## References

Albers, M. J., and Kim, L. 2000. “User Web Browsing Characteristics Using Palm Handhelds for Information Retrieval,” in

Proceedings of IEEE Professional Communication Society International Professional Communication Conference, Cambridge, MA, pp. 125-135.

Barnard, L., Yi, J. S., Jacko, J. A., and Sears, A. 2005. “An Empirical Comparison of Use-in-Motion Evaluation Scenarios for Mobile Computing Devices,” International Journal of Human-Computer Studies (62:4), pp. 487-520.

Baron, L., Taguesutcliffe, J., Kinnucan, M. T., and Carey, T. 1996. "Labeled, Typed Links as Cues When Reading Hypertext Documents," Journal of the American Society for Information Science (47:12), pp. 896-908.

Baudisch, P., Xie, X., Wang, C., and Ma, W.-Y. 2004. “Collapse-to-Zoom: Viewing Web Pages on Small Screen Devices by Interactively Removing Irrelevant Content,” in Proceedings of the 17 $^{th}$ Annual ACM Symposium on User Interface Software and Technology, Santa Fe, NM, October 24-27, pp. 91-94.

Berlyne, D. E. 1997. “Novelty, Complexity, and Hedonic Value,” Perception & Psychophysics (8), pp 279-286.

Bickmore, T. B., and Schilit, B. N. 1997. “Digestor: Device-Independent Access to the World Wide Web,” in Proceedings of the 6 $^{th}$ World Wide Web Conference, Santa Clara, CA, March 22-27, pp. 665-663.

Björk, S., Holmquist, L. E., Redström, J., Bretan, I., Danielsson, R., Karlgren, J., and Franzén, K. 1999. “WEST: A Web Browser for Small Terminals,” in Proceedings of the 12 $^{th}$ Annual ACM Symposium on User Interface Software and Technology, Asheville, NC, November 7-10, pp. 187-196.

Boslaugh, S., and Watters, P. A. 2008. Statistics in a Nutshells: A Desktop Quick Reference, Sebastopol, CA: O'Reilly Media.

Buyukkokten, O., Garcia-Molina, H., and Paepcke, A. 2001. "Accordion Summarization for End-Game Browsing on PDAs and Cellular Phones," in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Seattle, WA, pp. 213-220.

Campbell, C. S., and Maglio, P. P. 1999. “Facilitating Navigation in Information Spaces: Road-Signs on the World Wide Web,” International Journal of Human-Computer Studies (50:4), pp. 309-327.

Campbell, D. J. 1988. “Task Complexity: A Review and Analysis,” Academy of Management Review (13:1), pp. 40-52.

Chae, M., and Kim, J. 2004. “Do Size and Structure Matter to Mobile Users? An Empirical Study of the Effects of Screen Size, Information Structure, and Task Complexity on User Activities with Standard Web phones,” Behavior & Information Technology (23:3), pp. 165-181.

Chen, Y., Xie, X., Ma, W.-Y., and Zhang, H.-J. 2005. “Adapting Web Pages for Small-Screen Devices,” IEEE Internet Computing (9:1), pp. 50-56.

Charney, D. 1987. “Comprehending Non-Linear Text: The Role of Discourse Cues and Reading Strategies,” in Proceedings of the Conference on Hypertext, Chapel Hill, NC, pp. 109-120.

Chi, E. H., Gumbrecht, M., and Hong, L. 2007. “Visual Foraging of Highlighted Text: An Eye-Tracking Study,” in Human-Computer Interaction: HCI Intelligent Multimodal Interaction Environments, J. Jacko (ed.), Berlin: Springer, pp. 589-598.

Chi, E. H., Hong, L., Gumbrecht, M., and Card, S. K. 2005. "Scenthighlights: Highlighting Conceptually-Related Sentences During Reading," in Proceedings of the $10^{th}$ International Conference on Intelligent User Interfaces, San Diego, CA, pp. 272 - 274.

Davis, F. D. 1989. “Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology,” MIS Quarterly (13:3), pp. 319-340.

Davison, H., and Wickens, C. 1999. “Rotorcraft Hazard Cueing: The Effects on Attention and Trust,” Technical Report ARL-99-5/NASA-99-1, University of Illinois, Aviation Research Lab, Savoy, IL.

DeStefano, D., and LeFevre, J. 2007. “Cognitive Load in Hypertext Reading: A Review,” Computers in Human Behavior (23), pp. 1616-1641.

Doll, W. J., Hendrickson, A., and Deng, X. 1998. “Using Davis’s Perceived Usefulness and Ease-of-use Instruments for Decision Making: A Confirmatory and Multigroup Invariance Analysis,” Decision Sciences (29:4), pp. 839-869.

Duin, A. H. 1989. “Factors that Influence How Readers Learn from Text: Guidelines for Structuring Technical Documents,” Technical Communication (36), pp. 97-101.

Fisher, D. L., Coury, D. G., Tengs, T. O., and Duffy, S. A. 1989. "Minimizing the Time to Search Visual Display: The Role of Highlighting," Human Factor (31:2), pp. 167-182.

Furnas, G. 1997. “Effective View Navigation,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, S. Pemberton (ed.), Atlanta, GA, March 22-27, pp. 367-374.

Furnas, G., and Zacks, J. 1994. “Multitrees: Enriching and Reusing Hierarchical Structure,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems: Celebrating Interdependence, B. Adelson, S. Dumais, and J. Olson (eds.), Boston, MA, April 24-28, pp. 330-336.

Galletta, D. F., Henry, R. M., McCoy, S., and Polak, P. 2006. "When the Wait Isn't So Bad: The Interacting Effects of Website Delay, Familiarity, and Breadth," Information Systems Research (17:1), pp. 20-37.

Gentner, D., and Stevens, A. L. 1983. Mental Models, Hillsdale, NJ: Lawrence Erlbaum and Associates.

Germonprez, M., and Zigurs, I. 2005. “Causal Factors for Web Site Complexity,” Sprouts: Working Papers on Information Environments, Systems, and Organizations (3:2).

Hahn, U., and Mani, I. 2000. “The Challenges of Automatic Summarization,” Computer (33:11), pp. 29-36.

Hahn, U., and Reimer, U. 1999. “Knowledge-Based Text Summarization: Salience and Generalization Operators for Knowledge Base Abstraction,” in Advances in Automatic Summarization, I. Mani and M. Maybury (eds.), Cambridge, MA: MIT Press, pp. 215-232.

Harper, S., and Patel, N. 2005. “Gist Summaries for Visually Impaired Surfers,” in Proceedings of the 7 $^{th}$ Iinternational ACM SIGACCESS Conference on Computers and Accessibility, Baltimore, MD, October 9-12, pp. 90-97.

Hearst, M. A. 2009. Search User Interfaces, New York: Cambridge University Press.

Hevner, A., March, S., Park, J., and Ram, S. 2004. “Design Science Research in Information Systems,” MIS Quarterly (28:1), pp. 75-105.

Hicks, M., O'Malley, C., and Nichols, S. 2003. "Comparison of 2D and 3D Representations for Visualising Telecommunication Usage," Behaviour & Information Technology (22:3), pp. 185-201.

Hoadley, E. D., Simmons, L. P., and Gilroy, F. 1996. “Investigation the Effects of Color, Fonts, and Bold in Text Documents,” unpublished paper, School of Business and Management, Loyola College in Maryland, Baltimore, MD.

Hong, Y.-S., Park, I.-S., Ryu, J.-T., and Hur, H.-S. 2003. “Pocket News: News Contents Adaptation for Mobile User,” in Proceedings of the 14 $^{th}$ ACM Conference on Hypertext and Hypermedia Nottingham, UK, August 26-30, pp. 79-80.

Huckin, T. N. 1983. “A Cognitive Approach to Readability,” Chapter 5 in New Essays in Technical and Scientific Communication, P. V. Anderson, R. J. Brockmann, and C. R. Miller (eds.), Farmingdale, NY: Baywood Publishing Co., pp. 90-108.

Jacko, J. A., and Salvendy, G. 1996. “Hierarchical Menu Design: Breadth, Depth, and Task Complexity,” Perceptual Motor Skills (82:3), pp. 1187-1202.

Jiang, Z., and Benbasat, I. 2007. “The Effects of Presentation Formats and Task Complexity on Online Consumers’ Product Understanding,” MIS Quarterly (31:3), pp. 475-500.

Johnson, B., and Shneiderman, B. 1991. “Tree-Maps: A Space-Filling Approach to the Visualization of Hierarchical Information Structures,” in Proceedings of the Second Conference on Visualization '91, G. M. Nielson and L. Rosenblum (eds.), San Diego, CA, October 22-25, pp. 284-291.

Johnson, E. J., and Payne, J. W. 1985. “Effort and Accuracy in Choice,” Management Science (31:4), pp. 395-414.

Jones, M., Marsden, G., Mohd-Nasir, N., Boone, K., and Buchanan, G. 1999. “Improving Web Interaction on Small Displays,” Computer Networks (31:11-16), pp. 1129-1137.

Kaasinen, E., Aaltonen, M., Kolari, J., Melakoski, S., and Laakko, T. 2000. “Two Approaches to Bringing Internet Services to WAP Devices,” Computer Networks (33:1-6), pp. 231-246.

Käki, M., and Aula, A. 2008. “Controlling the Complexity in Comparing Search User Interfaces Via User Studies,” Information Processing and Management (44:1), pp. 82-91.

Kamis, A., Koufaris, M., and Stern, T. 2008. “Using an Attribute-Based Decision Support System for User-Customized Products Online: An Experimental Investigation,” MIS Quarterly (32:1), pp. 159-177.

Karahanna, E., and Straub, D. W. 1999. “The Psychological Origins of Perceived Usefulness and Ease-of-Use,” Information and Management (35:4), pp. 237-250.

Kelly, D. J. 2004. Understanding Implicit Feedback and Document Preference: A Naturalistic User Study, unpublished Ph.D. dissertation, Communication, Information and Libraries Studies, Rutgers, The State University of New Jersey, New Brunswick, NJ.

Kosslyn, S. M. 1989. “Understanding Charts and Graphs,” Applied Cognitive Psychology (3:2), pp. 185-225.

Kuo, F.-Y., Chu, T.-H., Hsu, M.-H., and Hsieh, H.-S. 2004. “An Investigation of Effort-Accuracy Trade-Off and the Impact of Self-Efficacy on Web Searching Behaviors,” Decision Support Systems (37:3), pp. 331-342.

Lam, H., and Baudisch, P. 2005. “Summary Thumbnails: Readable Overviews for Small Screen Web Browsers,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Portland, OR, April 2-7, pp. 681-690.

Larson, K., and Czerwinski, M. 1998. “Web Page Design: Implications of Memory, Structure and Scent for Information Retrieval,” in Proceedings of SIGCHI Conference on Human Factors in Computing Systems, Los Angeles, CA, April 18-23, pp. 25-32.

Lazar, J. 2005. Web Usability: A User-Centered Design Approach, Reading, MA: Addison Wesley.

Lin, D. M. 2003. “Hypertext for the Aged: Effects of Text Topologies,” Computers in Human Behavior (19:2), pp. 201-209.

Marchinonini, G. 1995. Information Seeking in Electronic Environments, New York: Cambridge University Press.

Maxwell, S. E., and Delaney, H. D. 2000. Designing Experiments and Analyzing Data, Mahwah, NJ: Lawrence Erlbaum Associates.

McDonald, D. M., and Chen, H. 2006. “Summary in Context: Searching Versus Browsing,” ACM Transactions on Information Systems (24:1), pp. 111-141.

McKeown, K., Passonneau, R. J., Elson, D. K., Nenkova, A., and Hirschberg, J. 2005. “Do Summaries Help? A Task-Based Evaluation of Multi-Document Summarization,” in Proceedings of the 28 $^{th}$ Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Salvador, Brazil, August 15-19, pp. 210-217.

Miller, G. A. 1956. “The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information,” Psychological Review (63), pp. 81-97.

Nadkarni, S., and Gupta, R. 2007. “A Task-Based Model of Perceived Website Complexity,” MIS Quarterly (31:3), pp. 501-524.

Nation, D. A., Plaisant, C., Marchionini, G., and Komlodi, A. 1997. "Visualizing Websites Using a Hierarchical Table of Contents," in Proceedings of the Third Conference on Human Factors and the Web, Designing for the Web: Practices and Reflections, Denver, CO, June 12, pp. 1-9.

Newell, A., and Simon, H. A. 1972. Human Problem Solving, Englewood Cliffs, NJ: Prentice-Hall.

Nielsen, J. 2000. Designing Web Usability: The Practice of Simplicity. Indianapolis, IN: New Riders Publishing.

Norman, K., and Chin, J. 1988. “The Effect of Tree Structures on Search in a Hierarchical Menu Selection System,” Behaviour and Information Technology (7), pp. 51-65.

Olston, C., and Chi, E. H. 2003. “Scenttrails: Integrating Browsing and Searching on the Web,” ACM Transactions on Computer-Human Interaction (10:3), pp. 177-197.

Otterbacher, J., Radev, D., and Kareem, O. 2006. “News to Go: Hierarchical Text Summarization for Mobile Devices,” in

Proceedings of the 29 $^{th}$ Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, S. Dumais, E. N. Efthimiadis, D. Hawking, and K. Järvelin (eds.), Seattle, WA, August 6-11, pp. 589 - 596.

Parush, A., and Yuviler-Gavish, N. 2004. “Web Navigation Structures in Cellular Phones: The Depth/Breadth Trade-Off Issue,” International Journal of Human-Computer Studies (60:5-6), pp. 753-770.

Payne, J. 1982. “Contingent Decision Behavior,” Psychological Bulletin (92:2), pp. 382-402.

Payne, J., Bettman, J. R., and Johnson, E. J. 1988. “Adaptive Strategy Selection in Decision Making,” Journal of Experimental Psychology: Learning, Memory, and Cognition (14:3), pp. 534-552.

Pirolli, P. 2007. Information Foraging Theory: Adaptive Interaction with Information. New York: Oxford University Press.

Pirolli, P., Card, S. K., and van der Wege, M. M. 2001. “Visual Information Foraging in a Focus + Context Visualization,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Seattle, WA, pp. 506-513.

Pirolli, P., Card, S. K., and van der Wege, M. M. 2003. “The Effects of Information Scent on Visual Search in the Hyperbolic Tree Browser,” ACM Transactions on Computer-Human Interaction (10:1), pp. 20-53.

Qiu, M., Zhang, K., and Huang, M. 2006. “Usability in Mobile Interface Browsing,” International Journal of Web Intelligence and Agent Systems (4), pp. 43-59.

Redish J. C. 1993. “Understanding Readers,” Chapter 1 in Techniques for Technical Communicators, C. M. Barnum and S. Carliner (eds.), New York: Macmillian, pp. 15-41

Robertson, G. G., Mackinlay, J. D., and Card, S. K. 1991. “Cone Trees: Animated 3D Visualizations of Hierarchical Information,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems: Reaching through Technology, New Orleans, LA, pp. 189-194.

Simon, H. A., and Lea, G. 1974. “Problem Solving and Rule Induction: A Unified View,” in Knowledge and Cognition, L. Gregg (ed.), Hillsdale, NJ: Lawrence Erlbaum, pp. 105-128.

Smelcer, J., and Carmel, E. 1997. “The Effectiveness of Different Representations for Managerial Problem Solving: Comparing Maps and Tables,” Decision Sciences (28:2), pp.391-420.

Speier C. 2005. “The Influence of Information Presentation Formats on Complex Task Decision-Making Performance,” International Journal of Human-Computer Studies (64:11), pp. 1115-1131.

Speier, C., and Morris, M. G. 2003. “The Influence of Query Interface Design on Decision-Making Performance,” MIS Quarterly (27:3), pp. 397-423.

Speier, C., Vessey, I., and Valacich, J. S. 2003. “The Effects of Interruptions, Task Complexity, and Information Presentation on Computer-Supported Decision-Making Performance,” Decision Sciences (34:4), pp. 771-797.

Spool, J. M., Schroeder, T., Schroeder, W., Snyder, C., and DeAngelo, T. 1999. Web Site Usability: A Designer's Guide, San Francisco, CA: Morgan Kaufmann.

Sticht, T. G. 1997. “Comprehending Reading at Work,” in Cognitive Processes in Comprehension, M. A. Just and P. A. Carpenter (eds.), Hillsdale, NJ: Lawrence Erlbaum Associates, pp. 221-246.

Tegarden, D. P. 1999. “Business Information Visualization,” Communications of the AIS (1:4), pp. 1-37.

Triesman, A. 1985. “Preattentive Processing in Vision,” Computer Vision, Graphics, and Image Processing (31:2), pp.156-177.

Tsandilas, T., and Schraefel, M. C. 2003. “Adaptive Presentation Supporting Focus and Context,” in Proceedings of the Workshop on Adaptive Hypermedia and Adaptive Web-Based Systems, Nottingham, UK, pp. 193-205.

Tsandilas, T., and Schraefel, M. C. 2004. “Usable Adaptive Hypermedia Systems,” New Review of Hypermedia and Multimedia (10:1), pp. 5-29.

Vakkari, P. 1999. “Task Complexity, Problem Structure and Information Actions: Integrating Studies on Information Seeking and Retrieval,” Information Processing and Management (35:6), pp. 819-837.

Vessey, I. 1991. “Cognitive Fit: A Theory-Based Analysis of the Graphs Versus Tables Literatures,” Decision Sciences (22), pp. 219-241.

Vessey, I. 1994. “The Effect of Information Presentation on Decision Making: A Cost-Benefit Analysis,” Information and Management (27:2), pp. 103-119.

W3C. 2005. “Document Object Model (DOM),” WC3 Architecture Domain (available online at http://www.w3.org/DOM/; retrieved February 27, 2005).

W3C. 2008. “Mobile Web Best Practices 1.0,” WC3 Recommendation (available online at http://www.w3.org/TR/mobile-bp/; retrieved August 14, 2008).

Ware, C. 2004. Information Visualization: Perception for Design, San Francisco: Morgan Kaufmann.

Wood, R. E. 1986. “Task Complexity: Definition of the Construct,” Organizational Behavior and Human Decision Processes (37), pp. 60-82.

Woodruff, A., Faulring, A., Rosenholtz, R., Morrison, J., and Pirolli, P. 2001. “Using Thumbnails to Search the Web,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Seattle, WA, pp.198-205.

Wu, J.-H., and Yuan, Y. 2003. “Improving Searching and Reading Performance: The Effect of Highlighting and Text Color Coding,” Information & Management (40), pp. 617-637.

Yang, C. C., and Wang, F. L. 2003. “Fractal Summarization for Mobile Devices to Access Large Documents on the Web,” in Proceedings of the 12 $^{th}$ International Conference on World Wide Web, Budapest, Hungary, May 20-24, pp. 215-224.

Zhang, D. 2007. “Web Content Adaptation for Mobile Handheld Devices,” Communications of the ACM (50:2), pp. 75-79.

Zhang, D., and Adipat, B. 2005. “Usability Testing for Mobile Applications,” International Journal of Human-Computer Interaction (18:3), pp. 293-308.

Zhang, D., Adipat, B., and Mowafi, Y. 2009. “User-Centered Context-Aware Mobile Applications—The Next Generation of Personal Mobile Computing,” Communications of the Association for Information Systems (24:3), pp. 27-46.

Zhang, H., and Salvendy, G. 2001. “The Implication of Visualization Ability and Structure Preview Design for Web Information Search Tasks,” International Journal of Human-Computer Interaction (13:1), pp. 75-95.

## About the Authors

Boonlit Adipat received his Ph.D. in Information Systems from the Department of Information Systems at the University of Maryland, Baltimore County. He is currently an adjunct professor in the Graduate School of Management and Innovation, King Mongkut's University of Technology, Thonburi, Thailand. His current research interests are in the areas of mobile applications, human-computer interaction, and system analysis and design. His work has been published in several academic journals and conference proceedings such as International Journal of Human-Computer Interaction and the Workshop on Information Technologies and Systems (WITS).

Dongsong Zhang received his Ph.D. in Management Information Systems from the Eller School of Management at the University of Arizona. He is currently an associate professor in the Department of Information Systems at the University of Maryland, Baltimore County. His current research interests include mobile HCI, computer-mediated collaboration and communication, knowledge management, and e-services. He has published about 100 papers in academic journals, conference proceedings, and book chapters, including journals such as Journal of Management Information Systems, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Software Engineering, IEEE Transactions on Multimedia, IEEE Transactions on Systems, Man, and Cybernetics, IEEE Transactions on Professional Communication, Decision Support Systems, Information & Management, among others.

Lina Zhou is an associate professor of Information Systems at the University of Maryland, Baltimore County. She was a research scientist at the Center for the Management of Information at the University of Arizona prior to joining UMBC. Her research aims to improve knowledge management and human decision making by designing and developing intelligent technologies. She has published over 30 referred papers in academic journals such as Journal of Management Information Systems, Information & Management, IEEE Transactions, Communications of the ACM, and Decision Support Systems. Her current research interests include online deception, intelligent systems, knowledge management, social network analysis, and ontology development.
