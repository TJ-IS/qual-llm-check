---
otero_id: 10906
otero_key: "5DAX6PXW"
title: "Knowing What a User Likes:  A Design Science Approach to Interfaces that Automatically Adapt to Culture"
authors: "Katharina Reinecke; Abraham Bernstein"
year: "2009"
journal: "MIS Quarterly"
doi: "10.25300/misq/2013/37.2.06"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# KNOWING WHAT A USER LIKES: A DESIGN SCIENCEAPPROACH TO INTERFACES THAT AUTOMATICALLYADAPT TO CULTURE<sup>1</sup>

Katharina Reinecke Harvard School of Engineering and Applied Sciences, 33 Oxford Street, Cambridge, MA 02138 U.S.A. {reinecke@seas.harvard.edu}

Abraham Bernstein Department of Informatics, University of Zurich, Binzmuehlestrasse 14, 8050 Zurich, SWITZERLAND {bernstein@ifi.uzh.ch}

Adapting user interfaces to a user’s cultural background can increase satisfaction, revenue, and market share. Conventional approaches to catering for culture are restricted to adaptations for specific countries and modify only a limited number of interface components, such as the language or date and time formats. We argue that a more comprehensive personalization of interfaces to cultural background is needed to appeal to users in expanding markets. This paper introduces a low-cost, yet efficient method to achieve this goal: cultural adaptivity. Culturally adaptive interfaces are able to adapt their look and feel to suit visual preferences. In a design science approach, we have developed a number of artifacts that support cultural adaptivity, including a prototype web application. We evaluate the efficacy of the prototype’s automatically generated interfaces by comparing them with the preferred interfaces of 105 Rwandan, Swiss, Thai, and multicultural users. The findings demonstrate the feasibility of providing users with interfaces that correspond to their cultural preferences in a novel yet effective manner.

Keywords: Culture, design science, adaptive systems, personalization

## Introduction

The growing number of Internet users worldwide has led international companies to try to conquer newly emerging markets. Yet many of these efforts have resulted in surprising failures with highly popular websites in a domestic market being rejected by Internet users from other countries in favor of local alternatives. Google is a prominent example of a company that has struggled to gain share in foreign markets. The classic minimalism of its main search engine site is one of the reasons that the company achieved a leading position within most Western markets. Yet this simplicity has failed to appeal to users in South Korea, where Google’s market share has long been a very distant second to the local competitor Naver.com (The Economist 2009; Sang-Hun 2007). One of the reasons might be that Naver.com presents its users with search results from various categories including web pages, images, and books, making its interface much more complex and colorful (Sang-Hun 2007)—a design that is common among South Korean websites.

How much preferences differ between countries becomes clear from research comparing websites designed by East Asian companies with those designed by their Western counterparts (Burgmann et al. 2006; Callahan 2005; Schmid-Isler 2000). Findings in this research area repeatedly emphasize that national culture influences our perception of good design.

Realizing the connection between culture and preferences, many companies now offer localized versions of their website. Localization usually involves the alteration of the user interface (UI) to provide for different languages and date/time formats, or, less often, a more sophisticated adaptation of colors and images (Russo and Boor 1993; Taylor 1992). Researchers have found that users react with a more positive attitude to localized interfaces (Nantel and Glaser 2008), see them as more usable (Ford and Gelderblom 2003; Sheppard and Scholtz 1999), and more appealing (Corbitt et al. 2002).

As users can easily switch to the competition with only one click (Chau et al. 2002), localization can provide a significant competitive advantage. However, there are three major problems hindering the wide-spread use of localization.

The design of sophisticated localized versions is extremely costly (Höök 2000). Carrying out wellexecuted software localization usually requires an ethnographic analysis of each country for which a localized version is needed (Yeo 1996). As a consequence, extending a market results in more time required for (1) comprehensive ethnographic studies and (2) a complex implementation of localized versions accompanied by rising costs, costs that companies are often reluctant to bear without a guarantee of benefit.

Localization does not cater to the cultural ambiguity of many users. Companies typically design one website version per target country (or region) and anyone who resides in this country receives the same interface. In most cases, the user is required to select a specific country at first entry or the website retrieves the user’s current whereabouts through the IP address. This method disregards users with multicultural backgrounds, who have been influenced by several national cultures. For example, an Indian who has lived in Belgium for several years would have to decide between a Belgian or an Indian version of a company’s website, but might be better off with a mixture of both.

Localization is usually limited to adapting the language, date, or time formats (Kersten 2002). Less visible interface aspects, such as images, the content arrangement, or even workflows, usually remain the same for all countries. The importance of allowing for more comprehensive modifications, however, has been demonstrated in several experiments. For example, researchers have shown that culture determines preferences for a linear or nonlinear navigation style (Kralisch 2005), or for a more or less complex interface (Schmid-Isler 2000). Moreover, studies have demonstrated that a person’s reading direction influences the focus point (Chan and Bergen 2005), and thus where users place their center of attention (Röse 2005). Such results indicate that the status quo of localization does not sufficiently cater to the extensive variations in perception between users of different cultural backgrounds.

We propose to address these problems with culturally adaptive user interfaces that adapt themselves to the user’s cultural preferences rather than having the user adapt to a more or less standardized interface. Using a design science approach (Peffers 2007), we introduce a method to implement cultural adaptivity and demonstrate this method with a culturally adaptive system called MOCCA.

To the best of our knowledge, MOCCA is the first system that is able to adapt its interface to the preferences of users of any national culture, and any combination of different national cultures (called extended national culture in the following). Our research question explores how well a culturally adaptive system such as MOCCA can predict user interface preferences by knowing only a person’s (extended) national culture. To answer this question, this paper evaluates MOCCA’s adaptation rules, which link national cultures to certain user interface preferences. MOCCA was tested with 75 participants from Rwanda, Switzerland, and Thailand, plus 30 multicultural participants who have lived in at least two different countries.

Our findings show that MOCCA’s initial adaptation rules accurately match 51 percent of our participants’ preferences on average. With a simple learning procedure, MOCCA was able to improve and achieve an average prediction accuracy of 61 percent. By comparison, users’ preferences were matched only 33 percent of the time with randomly created interfaces.

Consequently, our contributions are as follows: First, we present a theoretically founded novel approach for automatically adapting interfaces to cultural preferences. We introduce a cultural user modeling ontology, an algorithm to approximate a person’s cultural background, a set of literature-derived user interface adaptation rules, as well as a user interface adaptation ontology. We show how these elements combine into a prototype web application. Second, we empirically evaluate this approach using the prototype, and demonstrate that our approach is able to approximate cultural preferences.

In the following section, we introduce prior work on which we based our method for designing for cultural adaptivity. Its subsections detail findings in cultural anthropology, the influence of culture on UI preferences, and how the literature has tackled the problem of acquiring information about a user. Important findings from previous work on adaptive systems and their implications for our approach are also discussed. We then describe our methodology and our approach to cultural adaptivity. We developed five different artifacts that demonstrate the approach and detail its implementation in a prototype application. Next, we describe an evaluation of the prototype. The final sections discuss limitations, future work, and conclusions.

## Related Work

Our contribution is novel in that we present the first approach that enables user interfaces to adapt to the preferences of people of any national culture, and any combination of different national cultures, by automatically changing various user interface aspects. A major obstacle to the development of comparable approaches in the past might have been the lack of knowledge about culture, what aspects it includes, and how it influences design preferences and perception. This information is indispensable for developing adaptation rules that trigger modifications of the UI. For an approach to cultural adaptivity we need to (1) know what culture is (i.e., what aspects of one’s life it is influenced by), (2) understand how singular aspects of culture affect UI perception, (3) acquire user-specific information about these aspects, (4) translate the aspects into adaptation rules, and (5) develop systems that are flexible enough to cater to the rules. We review the relevant work on these open questions and, based on the literature, establish the requirements for cultural adaptivity.

## The Intangible Nature of Culture

Information systems research has long acknowledged that cultural differences can inhibit the successful use of information technology (Leidner and Kayworth 2006), and its user acceptance (Kappos and Rivard 2008). The differences have mostly been analyzed on a national or an organizational level of culture, both of which are often closely intertwined (Leidner and Kayworth 2006).

Anthropology discusses a more complex view of the term: There, culture is often (loosely) described as a common “programming of the mind” (Hofstede 1997, p. 1007), which leads certain cultural groups to collectively share values and preferences (Callahan 2005). A major impediment to a more finite definition of culture is that the term cannot be equated with a specific country, nor can its effects be confined by artificial country borders. While a person’s nationality does influence the cultural identity to some extent (Hofstede 1997), people can belong to several cultures (and nations) and mental affiliations to another culture can shape a person’s values, as in the case of migration (Gupta and Ferguson 1997). Hence, former residences and a differing nationality of parents could change a person’s predominant values. In addition, there are several influences on the formation and development of one’s own culture. For example, the general behavior and mode of interaction in a country influences people’s cultural values (Karahanna et al. 2005). Political orientation and social structure affect whether people think in a more self-centered mode or define themselves more as a member of a group (i.e., a family) (Hofstede 2001). Independent from countries and their cultural values, a person moves within cultures and subcultures on a more individual level. This is the case, for example, if a person is influenced by an organizational culture. Additionally, people’s education level can determine their openness to adopt foreign cultural values (Hayward and Siaya 2001), their mother tongue (and possible foreign languages) impacts their thinking and perception (Nisbett and Masuda 2003), and the intensity of their belief determines how religion influences their daily habits and principles. Hence, the magnitude of how the various aspects of culture affect a person’s values has to be assessed on an individual level. Culture does not produce groups of people with uniform codes of behavior, but it creates groups that share similar thinking to some extent.

Given the amorphous nature of cultural background, the nation as a territorial concept is a frequently used proxy indicator. In fact, the majority of research in Information Systems addressing cultural differences focuses on a person’s or a group’s affiliation to a country (Leidner and Kayworth 2006). To facilitate comparisons between national cultures, cultural anthropologists have tried to define culture with a definite set of constructs. Examples are the cultural classifications developed by Hall and Hall (1990), Hofstede (2001), and Trompenaars and Hampden-Turner (1997) (for an overview, see Zahed et al. 2001). Of all these classifications, Hofstede’s work has received the most attention (Ford et al. 2003), presumably because it facilitates the comparison of more than 74 countries<sup>2</sup> by providing tangible scores (Hofstede ND). After a large-scale quantitative analysis in these countries, he distinguished between the five dimensions of power distance (PDI), individualism (IDV), masculinity (MAS), uncertainty avoidance (UAI), and long term orientation (LTO) (Hofstede 2001). Every country received five scores (one for each dimension), by which countries can be compared to one another. Power distance, for example, describes the extent that hierarchies take place and are accepted within a society. In countries that have been assigned a high power distance score (e.g., Russia or China), inequalities are believed to be much more acceptable in society than in low power distance countries such as Austria or Denmark. The people in highly individualist countries (e.g., the United States) are usually seen as more independent from a group, such as from a family. In contrast, people in collectivist countries (e.g., many Latin American and Asian countries) often see themselves as part of a group. Hofstede’s third dimension, masculinity, refers to more competitive societies versus more feminine countries, in which consensus and caring for the weak is seen as more desirable. Societies that tolerate uncertainty, ambiguity, and unstructured situations fairly well were further classified as having a low uncertainty avoidance. Hofstede later added a fifth dimension, long term orientation, which describes societies’ feel of time. Countries with a short-term orientation (e.g., Ghana, Philippines) are believed to focus on the nearer future, for example, on fast accomplishments. In contrast, long-term oriented countries, such as Taiwan or China, are seen as more traditional, relationships are more important; they tend to save for the future, and are more willing to work toward long-term goals.

Hofstede’s work has often been criticized because his classification reduces culture to nationality (hence, the name national culture) and ignores ongoing changes in a person’s or a group’s shared cultural values (McSweeney 2002; Myers and Tan 2002). Hofstede derived his dimensions by comparing data from IBM employees, and critics point out that they might not be applicable to contexts outside of this specific organizational culture (McSweeney 2002). Whether they are good predictors for UI preferences has been heavily debated, with some researchers doubting the validity of the dimensions (Khashman and Large 2010; Oshlyansky 2007). Others, however, have demonstrated that certain dimensions can be linked to users’ design choices with some success (Burgmann et al. 2006; Callahan 2005; Dormann and Chisalita 2002). We build on his work because Hofstede’s dimensions are the only national cultural classification that has been used to link tangible country scores to UI preferences.

## The Influence of Hofstede’s Dimensions on UI Preferences

In the field of human–computer interaction, researchers have put much effort into investigating culture on a national level and into finding differences in the preferences of people between countries (Ford and Gelderblom 2003; Sheppard and Scholtz 1999). Many of these researchers based their work on the fact that, to some extent, design preferences of different cultural groups are generalizable for the people within one group (Ford and Gelderblom 2003; Sheppard and Scholtz 1999). Other research has demonstrated that people within the same cultural group even show similar navigation and search behavior (Kralisch and Berendt 2004; Kralisch et al. 2005). Hofstede’s advocates have further established a substantial base of work describing which UI aspects are influenced by certain dimensions and their different score ranges. We have summarized these findings in Table 1, which lists the influences with regard to high or low dimensional scores compared to the world average. It is important to note that these studies have been conducted in different contexts. The connections in Table 1 are not necessarily replicable using other websites or investigation procedures, but they provide tangible hints on what a user might like. With the information about a person’s national culture, for example, it is feasible to phrase adaptation rules, such as “if a user has a low score in the dimension power distance, then provide a complex interface.”

## Cultural Influences on UI Perception and Preferences

Beyond national cultures and Hofstede, there are many other cultural aspects that shape a person’s preferences (see Table 2 for a summary). Different languages have been found to affect whether or not a person mostly concentrates on a central object, as found for people speaking Western languages (Nisbett 2003). Asian languages, in contrast, seem to train people’s brain to equally perceive the context surrounding a focal point (Nisbett 2003). Research also found that a language’s writing and reading direction determines the spatial routines literate humans employ (Chan and Bergen 2005): Initially, people direct their eyes to the start location of their writing system orientation. This finding has been also shown to impact the center of attention on a screen, suggesting that error messages and important interface elements should be placed according to the start location of a person’s writing system orientation (Röse 2005). Another cultural influence is religion, which is often named as a mediator of preferences for certain symbols and colors, and implicitly the feeling of trust (Siala et al. 2004). Furthermore, varying education levels contribute to the creation of cultural groups, so-called “subcultures” (Karahanna et al. 2005). As a very rough rule, people with a higher education level use the computer more frequently than people with a low education level (Microsoft 2004). A high computer literacy, in turn, could indicate that the user needs less support. However, a more concrete predictor of the need for support might be the form of education to which an individual is accustomed. A predominance of teacher-centered instruction at school can have the effect that students are used to detailed instructions, and that this habit transfers to the use of computers. In fact, cultures with a prevalence for teacher-centered instruction often adopt the learning style of observers, and these are thought to prefer a linear navigation (Liegle and Janicki 2006).

Table 1. Relationships between Hofstede’s Dimensions and UI Design Aspects (Reinecke 2011)

<table><tr><td></td><td>Low Score</td><td>High Score</td><td>Reference</td></tr><tr><td rowspan="6">Power Distance</td><td>Different access and navigation possibilites; nonlinear navigation</td><td>Linear navigation, few links, minimize navigation possibilities</td><td>Burgmann et al. 2006Marcus and Gould 2000Voehringer-Kuhnt 2002</td></tr><tr><td>Data does not have to be structured</td><td>Structured data</td><td>Marcus and Gould 2000</td></tr><tr><td>Most information at interface level, hierarchy of information less deep</td><td>Little information at first level</td><td>Burgmann et al. 2006Marcus and Gould 2000</td></tr><tr><td>Friendly error messages suggesting how to proceed</td><td>Strict error messages</td><td>Marcus and Gould 2000, 2001</td></tr><tr><td>Support is only rarely needed</td><td>Provide strong support with the help of wizards</td><td>Marcus and Gould 2000</td></tr><tr><td>Websites often contain images showing the country's leader or the whole nation</td><td>Images show people in their daily activities</td><td>Gould et al. 2000Marcus and Gould 2000</td></tr><tr><td rowspan="4">Individualism</td><td>Traditional colors and images</td><td>Use color to encode information</td><td>Marcus and Gould 2000</td></tr><tr><td>High image-to-text ratio</td><td>High text-to-image ratio</td><td>Gould et al. 2000</td></tr><tr><td>High multimodality</td><td>Low multimodality</td><td>Hermeking 2005</td></tr><tr><td>Colorful interface</td><td>Monotonously colored interface</td><td>Barber and Badre 1998</td></tr><tr><td rowspan="3">Masculinity</td><td>Little saturation, pastel colors</td><td>Highly contrasting, bright colors</td><td>Dormann and Chisalita 2002Voehringer-Kuhnt 2002</td></tr><tr><td>Allow for exploration and different paths to navigate</td><td>Restrict navigation possibilities</td><td>Ackerman 2002</td></tr><tr><td>Personal presentation of content and friendly communication with the user</td><td>Use encouraging words to communicate</td><td>Callahan 2005Dormann and Chisalita 2002Hofstede 1986</td></tr><tr><td rowspan="3">Uncertainty Avoidance</td><td>Most information at interface level, complex interfaces</td><td>Organize information hierarchically</td><td>Burgmann et al. 2006Cha et al. 2005Choi et al. 2005Hodemacher et al. 2005Marcus 2000Marcus and Gould 2000, 2001Zahed et al. 2001</td></tr><tr><td>Nonlinear navigation</td><td>Linear navigation paths / show the position of the user</td><td>Baumgartner 2003Burgmann et al. 2006Corbitt et al. 2002Kamentz et al. 2003Marcus 2000Marcus and Gould 2000, 2001</td></tr><tr><td>Code colors, typography &amp; sound to maximize information</td><td>Use redundant cues to reduce ambiguity</td><td>Marcus and Gould 2000, 2001</td></tr><tr><td rowspan="2">Long Term Organization</td><td>Reduced information density</td><td>Most information at interface level</td><td>Marcus and Baumgartner 2004Marcus and Gould 2000</td></tr><tr><td>Content highly structured into small units</td><td>Content can be arranged around a focal area</td><td>Marcus and Gould 2000</td></tr><tr><td colspan="4">Table 2. Effects of Cultural Influences on Perception and Preferences</td></tr><tr><td>Cultural Influences</td><td>Suggested UI adaptations</td><td colspan="2">Reference</td></tr><tr><td>Language</td><td>Objects in focus, versus objects embedded in context</td><td colspan="2">Nisbett 2003</td></tr><tr><td rowspan="2">Reading/writing direction</td><td>Left-to-right alignment, right-to-left alignment, or right-to-left/top-to-bottom alignment of all interface elements</td><td colspan="2">Chan and Bergen 2005</td></tr><tr><td>Place elements at the starting point of a person's reading direction if they require full attention</td><td colspan="2">Röse 2005</td></tr><tr><td rowspan="2">Religion</td><td>Different numbers of religious symbols, exchangeable for each religion</td><td colspan="2">Siala et al. 2004</td></tr><tr><td>Different color schemes: colorfulness, brightness, and contrast</td><td colspan="2">Siala et al. 2004</td></tr><tr><td rowspan="3">Political Orientation/social structure</td><td>Objects in focus, versus objects embedded in context</td><td colspan="2">Schmid-Isler 2000</td></tr><tr><td>Different levels of hierarchy in the information presentation</td><td colspan="2">Schmid-Isler 2000</td></tr><tr><td>Variable complexity/information density</td><td colspan="2">Schmid-Isler 2000</td></tr><tr><td rowspan="2">Education level</td><td>Different levels of support</td><td colspan="2">Microsoft 2004</td></tr><tr><td>Variable numbers of navigational cues</td><td colspan="2">Microsoft 2004</td></tr><tr><td rowspan="2">Form of instruction</td><td>Nonlinear navigation versus linear navigation with instructions</td><td colspan="2">Liegle and Janicki 2006</td></tr><tr><td>Different levels of support</td><td colspan="2">Liegle and Janicki 2006</td></tr></table>

## Acquiring and Storing Information About a User’s Cultural Background

The strong effect of culture on people’s design preferences suggests a rapid acquisition of information about users. In fact, in the best of all worlds we would have sufficient knowledge about a user’s culture before he or she first accesses the interface, because, as suggested by previous research, the first impression counts (Lindgaard et al. 2006).

Related work has provided ideas on how to obtain user information in order to subsequently adapt to certain aspects (e.g., by using questionnaires in an initial registration process; de Bra 1999), through performance tests (Gajos et al. 2008), or by observing the user’s interaction (Kralisch et al. 2005) as exemplified in news personalization based on what a user has previously accessed (Aggarwal and Yu 2002; Henze 2005). Unfortunately, the last two methods do not seem to be directly applicable for adapting to users’ cultural preferences, mostly because the effects of cultural background on performance and user interaction have yet to be fully understood. A static knowledge acquisition with the help of a questionnaire could be a more promising solution. However, long questionnaires run the risk that users avoid the effort of filling in answers (e.g., due to privacy concerns) and. thus, restrain from registering. It is, therefore, advisable to keep the initial acquisition process at a minimum but enable users to voluntarily provide more information later to refine adaptations.

To store user information and ensure application-independent access at the same time, researchers have proposed to use distributed user models (Dolog and Nejdl 2003), where user information is shared through ontologies (Zhou et al. 2005). Ontologies are data models that describe a set of concepts within a domain, and consider the relationship between these concepts. With that, they provide the means to specify a common understanding of the user modeling domain across applications. Research on such shared user models has been conducted in the area of e-government with the portal adaptation ontology (Stojanovic and Thomas 2006) and in e-learning applications (Aroyo et al. 2006; Dolog and Nejdl 2003). For our purpose, these studies present a foundation that will need to be extended to capture cultural elements of a user’s preferences.

## Adaptive User Interfaces

Adaptive systems are usually referred to as systems that are able to adapt themselves to the user by acquiring information and triggering suitable modifications to the user interface (Jameson 2008). On the basis of a user’s profile, adaptive systems provide personalized content (Aggarwal and Yu 2002; Henze 2005) or advertisements (e.g., as on the social networking platform Facebook or next to Google’s search results). Most industrial systems do not offer a flexible and automatic rearrangement of UI elements.

Huber (1803) questioned the benefit of adaptive systems over a manual adaptation by the user. Summarizing various studies on decision support systems that automatically adapt themselves to a user’s cognitive style, Huber argued that it is inherently difficult, if not infeasible, to assign operational design guidelines to users’ cognitive style. One reason is that cognitive style might only hint at a small subset of individual design preferences. Further, it has been suggested that adaptive systems do not adhere to usability principles (Höök 2000), and that it is important to maintain “controllability” (Jameson and Schwarzkopf 2002). Indeed, the amount of control necessary for, or preferred by, a user can vary highly (Kay 2001).

In line with discussions on the controllability, research has described different options for introducing adaptations, and for the timing of new adaptations (Dieterich et al. 1993): (1) the user explicitly requests adaptations and then actively chooses or rejects them, (2) he or she explicitly requests adaptations that are then automatically triggered, (3) the system automatically recommends adaptations, but lets the user decide whether to accept or reject them, or (4) the system automatically triggers adaptations. Jameson and Schwarzkopf (2002) suggest that choosing a perfect solution for all users from such different options is not possible, because it depends on the individual experience of users, and on the type of applications and its adaptations.

In more recent times, research has given a different view and underlined the advantages of adaptive systems, which “represent the most promising solution to the contradiction between striving to achieve cost-savings on the one hand and...customer satisfaction on the other” (Maier 2005. Supporting this thesis, research has shown that systems that adapt the presentation of their interface to the user’s abilities can indeed improve performance (Gajos et al. 2008; Hurst et al. 2007; Hurst et al. 2008). Moreover, adaptive interfaces can have immense economic benefits: Hauser et al. (2009) demonstrated that adapting the presentation of advisory information on a website to users’ cognitive style can increase purchase intentions. In their work, the adaptations support users when making purchase decisions by adapting the image-to-text ratio and the level of detail of the information that is being presented (Hauser et al. 2009; Urban et al. 2009). Their success at least partly refutes Huber’s early advice that using cognitive style to adapt decision support systems is not worthwhile.

In previous work on adaptive systems, few researchers have aimed to personalize the entire visual presentation of user interfaces to increase a user’s perception of appeal. This is despite the fact that many researchers acknowledge the importance of a user’s first impression of a website design (Lindgaard et al. 2006) and the decisive role of culture on whether a user gets a good or bad impression, or develops a feeling of trust toward a particular design (Cyr et al. 2005).

Many researchers have also raised concerns that localization does not sufficiently cater to the variety of cultural preferences, but only a few researchers have proposed intelligent approaches to cater to users’ individual cultures. Work in this direction has mainly concentrated on tutoring systems, with researchers arguing that the learning style is highly influenced by culture (Blanchard et al. 2009; Kamentz and Womser-Hacker 2003). That work, however, is concentrated on adaptations of the content (e.g., the instructions provided to learners) and did not envision a modification of interface elements. Adaptations on the interface level were incorporated in Heimgärtner (2005), but were only indicated for specific countries and did not include multicultural influences.

Overall, our goal differs from previous research in that we aim to personalize the information presentation by adapting all user interface aspects that are perceived and preferred differently between cultures. In addition, our goal is to provide users with interfaces that correspond to their own design choices, and to predict these design choices before the user sees the initial interface. Hence, in contrast to previous research, which has mostly attempted to improve objective metrics such as performance (reducing time/error rates) or sales (increasing purchase intentions) our aim is to meet a subjective metric: a users’ overall perception of good design.

## Research Approach

The research presented here follows a design science research approach. Hevner et al. (2004) described design science research as a build-and-evaluate process with the goal of producing a set of artifacts. Our main goal was to define and develop artifacts that support cultural adaptivity of user interfaces. Since cultural adaptivity is a novel approach, its design can be seen as a search process (Hevner et al. 2004) involving an iterative evaluation and refinement of artifacts. The research approach we employed follows Peffers et al. (2007) (see also Figure 1).

![](/api/attachments/5DAX6PXW/fulltext/images/afda52b146e98a3857cd398aa3269db762fd45d8c3a3404a93010813583b4a06.jpg)  
Figure 1. Design Science Research Methodology (Following Peffers et al. 2007)

We first identified the problems of conventional localization: (1) user interfaces are usually designed for only a few target cultures, (2) the process of designing special interfaces for each of these target cultures is time-consuming and costly, and (3) the interfaces usually only differ in language and a few minor visual aspects.

We then defined concrete objectives to inform the requirements of a possible solution to the above-mentioned problems. Our first objective is to find a solution that caters to users of any national culture, as well as to users who have been influenced by several different national cultures. The large variety in users’ cultural backgrounds makes it necessary to find ways for an automatic adaptation of the user interface. A second objective is to reduce the development effort. Modular user interfaces that allow a flexible composition of various interface elements increase the number of variations of this interface element to the power of the number of adaptable interface elements. For example, if we have 3 design variations for the style of a button, and 3 design variations for the text within this button, the button could take on from 9 to 32 different designs. Thus, instead of designing each interface version from scratch, a modular user interface approach allows us to achieve many more versions with less design effort. The modular approach is also beneficial for our third objective, which is to allow comprehensive modifications of the interface. The requirement, therefore, is to create different designs for all those parts of the interface that are subject to cultural preferences.

At the design stage (see number 3 in Figure 1), we were unaware of the nature of cultural background, of how preferences differed between cultures, and hence, which user interface modifications were needed. We inferred the requirements for our artifacts by drawing on theoretical foundations in the related fields of cultural anthropology, cognitive science, and human–computer interaction. We further combined knowledge and techniques from the research fields of user modeling and adaptive systems in order to make design decisions that fundamentally influenced the direction of our approach.

Building on this theory, we developed several artifacts to support cultural adaptivity and, where possible, evaluated alternatives of major design decisions. The prototype web application builds on four artifacts (a cultural user model ontology, an algorithm to approximate a user’s cultural background, adaptation rules, and an adaptation ontology). For demonstration purposes, the prototype was trialed by triggering adaptations for fictitious users. We compared the resulting interfaces for these fictitious users to the specifications in the adaptation rules and eliminated any technical errors. This step served as a technical review of the prototype to ensure that user interfaces were correctly composed at a theoretical level.

Following the theoretical validation of our approach, we evaluated whether the user interfaces corresponded to users preferences. We conducted four studies, one with culturally ambiguous users who have been influenced by various national cultures, and three with participants who have always lived within the same national culture. The results of these four studies were used to inform improvement possibilities, which we evaluated in a further iteration of the design process. These evaluation results are presented in this paper.

## Designing for Cultural Adaptivity

In this section, we will describe how our objectives for cultural adaptivity informed the development of various artifacts that support cultural adaptivity. These artifacts include a cultural user model ontology, an algorithm to approximate a user’s cultural background, adaptation rules, and an adaptation ontology, as well as a prototype to-do list web application called MOCCA, which is an artifact instantiation (Hevner et al. 2004) developed to instantiate our approach.

## Artifact 1: A Cultural User Model Ontology

In collaboration with cultural anthropologists, we have previously established a list of aspects that influence cultural background (Reinecke et al. 2010). We focused on extracting those aspects of culture that impact interface preferences by conducting a thorough literature review on related work from various research fields, such as cultural anthropology, cognitive science, and human–computer interaction.

To create a knowledge base with this information, all of these aspects are defined in a cultural user model ontology developed in the web ontology language OWL (McGuinness and van Harmelen 2004). The ontology has the advantage that it can contain a complex and extendable model of the user’s cultural background, which unifies the knowledge across applications, as suggested by Dolog and Nejdl (2003). In addition, it is application-independent, meaning that the knowledge has to be acquired only once while still being accessible to an infinite number of applications.

As shown in Figure 2, the central concept in our cultural user model ontology is the Person class with its disjoint<sup>3</sup> subclasses Female and Male, which can be used as control variables as suggested by Kamentz and Womser-Hacker (2003). A so-called datatype property (i.e., a connection between an object and a literal) hasYearOfBirth with the value year representing the user’s age, which can be inferred from the sum of all durations the user has lived at current and former residences. The Person class further links to the classes PoliticalOrientation, SocialStructure, Religion, EducationLevel, FamiliarFormOf Education, and ComputerLiteracy. All of these classes are interconnected through datatype properties modeling the impact on the user’s cultural background (see the legend in Figure 2). This impact factor can be customized by the application or the user (e.g., with the help of a user model editor). Additionally, each of these knowledge classes is connected to all relevant individuals. The class Religion, for example, provides instances of different religious beliefs as well as of major philosophies.

To model the cultural influence of different places of residence, the ontology comprises the object properties (linking two classes) hasCurrentResidence and hasFormer Residence, all having the range Location. The property hasCurrentResidence is functional, and therefore cam have at most one individual relating to it. Location is further subdivided into the subclasses Continent and Country, which contain individuals of all continents as well as of all countries listed in ISO 3166 (International Organization for Standardization 1997a).

In addition, datatype properties of the range integer record the months of residence for each instance of current Residence and formerResidence. With the help of the datatype property hasYearOfBirth, which provides us with information about the user’s age, we can calculate the cultural influence of each of these locations on the user. The algorithm for this calculation is described in the next section. The ontology has been complemented with the class Language, which is subdivided into the disjoint subclasses Mothertongue and SecondLanguage. A person’s native language cannot be specified as a second language. As with the other classes within the domain Person, both can be assigned an impact factor, and both inherit an integrated language ontology from Language as listed in ISO 639 (International Organization for Standardization 1997b). All languages have been assigned a reading direction, which later triggers adaptations of the alignment of interface elements.

A specific design decision was made by additionally incorporating Hofstede’s classification into the ontology. Previous work suggests that his cultural dimensions can be linked to user interface preferences. If this is the case, including the dimensions would (1) support the calculation of a user’s cultural background, as we will describe in more detail in the next section, and (2) generalize our knowledge of user preferences, which is otherwise restricted to the most wellresearched countries, such as the United States or China. Instead of directly linking certain adaptations to a specific country, we could link them to dimensions and, thus, also provide adaptations for those countries that research has so far ignored. We assume that these hypotheses are correct, but if not, this component of our approach can be extended or replaced with other cultural models in future work.

![](/api/attachments/5DAX6PXW/fulltext/images/75d8f4221508b5a7b027847d98a752bd1f0c6ccc845be511876692fa49bd5abf.jpg)  
Figure 2. The Set of Cultural Variables and Aspects that Impact UI Preferences, Modeled in a Cultural User Model Ontology

## Artifact 2: An Algorithm to Approximate Cultural Background

The conversion of a user’s country information into a personal cultural background is achieved by an algorithm, which traverses the following steps:

The application enquires about the user’s current and former places of residence as well as about the respective durations. In this first approach to cultural adaptivity, we have limited the initial registration process to only three questions.

This information is passed onto the server, where it is stored in the user-specific instance of the cultural user model ontology.

The application receives the cultural dimensions for each of the user’s places of residence from the cultural user model ontology.

The application calculates the percentage influence of each residence with the help of the single duration and the cumulative time span (which is assumed to be roughly equal to the user’s age in months):

$$
\text { influenceOfCountry } _ {N} = \frac {\text { monthlyDurationOfStayInCountryN }}{\text { ageInMonths }}\tag{1}
$$

For each of Hofstede’s five dimensions, and consequently for each country of residence, the algorithm then calculates a new score:

$$
\text { userDimScore } _ {H} = \sum_ {i = 1} ^ {N} \text { countryScore } _ {H} * \text { influenceOfCountry } _ {i}\tag{2}
$$

with H being one of Hofstede’s five dimensions; N being the number of different countries of residence, and countryScore being the Hofstede score that a country received in the respective dimension.

The new cultural dimensions are compared to the world averages that are stored in the cultural user model ontology. In the adaptation rules, the deviation from the world average now provides information about which rules are triggered.

Accordingly, the weighted averages of the different national cultures a user is influenced by can be translated to specific adaptations of the UI. Here, using Hofstede’s dimensions as a basis for the adaptation rules has two advantages: First, we can build on the numerous studies that have related certain dimensions to UI aspects and listed differences in cultural preferences for low and high scores of each dimension. In combination, these findings can be reformulated to serve as adaptation rules. Second, the national interpretation of culture by Hofstede allows us to associate a person’s current and former countries of residence with interface preferences. The proposed linear combination of influence of former residences (in equations 1 and 2) can only serve as a first approximation as it is unclear whether the different stages in people’s life have equal impact on their culture. Having spent one’s school years in a certain country, for example, may have a stronger influence on one’s cultural outlook than years spent in retirement, but we cannot generalize such assumptions. We, therefore, weight the influence of a certain country on a person’s extended national culture purely according to the time this person spent in a country.

Different forms of the algorithm were evaluated and results were used to iteratively refine the final calculation. Specifically, we conducted a preliminary evaluation (Reinecke and Bernstein 2008), in which we aimed to predict participants’ answers in a set of survey questions based on the information about their extended cultural background. During the analysis, we adjusted several variables in the algorithm, for example, factoring in the parents’ nationality or weighing the influence of countries differently according to when a participant lived there. We settled on the algorithm version where the calculation of the participant’s extended cultural background best correlated with their user interface preferences.

## Artifact 3: Adaptation Rules

Our adaptation rules were informed by literature on cultural influences on preferences and perception, which we introduced earlier (the findings of previous studies were summarized in Table 1 as a list of general adaptation rules). In a preliminary study, we were able to validate the specified mapping of Hofstede’s dimensions to certain UI preferences (Reinecke and Bernstein 2008).

For use in any application, the general adaptation rules have to be tailored to suit the specific domain—in our case to the UI of a to-do list application called MOCCA. To develop such specific adaptation rules we iteratively traversed the stages of analysis, design, and implementation multiple times. The process made use of different sources of inspiration. We compared and analyzed variations in the designs of two international webpages, which were chosen because of their high number of page requests: the different national websites for the 2008 Olympic Games in Beijing<sup>4</sup> and the various national versions of the online encyclopedia Wikipedia.<sup>5</sup> While the national versions of the Olympic Games websites were designed freely, and thus, varied heavily in the representation of content, Wikipedia restricts the localized versions to a certain design, which undoubtedly increases the recognition value. Nevertheless, variations in the design interpretations of the localized versions were recognizable in both websites, suggesting that the designs were developed by local design teams. We, therefore, assumed that the websites represented the preferences of the general audience in the respective country.

As a next step, we aligned the localized web pages with Hofstede’s cultural dimension scores and with previous evaluations on the relation between the dimensions and UI designs. The way the localized web pages implemented culturally specific features especially helped us generate ideas on how our application could incorporate the rules. Table 3 describes the outcome of this endeavor with 10 adaptable interface aspects, and their specific effects when adapted to a low, medium, or high score for certain dimensions of Hofstede in our to-do application MOCCA. The table shows the adaptation rules “extremes” for each of Hofstede’s dimensions and UI aspect; these adaptation rules can be further refined by adding different changes in the UI that mirror this gradation.

The adaptation rules can be incorporated into any application by simply following conditional statements, such as if (UAI = high) then show wizard. However, in order to retain flexibility and be able to learn and refine rules, it makes more sense to detach Hofstede’s dimensions and scores from the adaptable interface aspects. We have addressed this issue with an adaptation ontology, which we will describe in the following section.

## Artifact 4: An Adaptation Ontology

According to the number of possible adaptations, as described in Table 3, a culturally adaptive system needs to be extremely flexible in the composition of the various interface components in order to cater to the different user profiles and the corresponding adaptation rules. For example, each interface element should be available in different versions, the number of elements and functionalities visible at first sight has to be adaptable, and the placement of interface elements should be as versatile as possible. Thus, the application has to take over parts of the usual design process performed by human designers via the calculation of the best possible position of elements for the respective user profile. For this purpose, we have developed an adaptation ontology for the domain of web applications (described in detail in Appendix A), which incorporates those parts of an interface that are dependent on cultural preferences. The adaptation ontology can be reused and extended to suit specific UI designs and could be easily modified (e.g., for use in mobile applications).

Table 3. MOCCA’s Adaptation Possibilities According to a Classification of the User’s Cultural Dimension Score into Low, Medium, or High

<table><tr><td>Interface Aspect:</td><td>Linked to Dimension:</td><td>Low</td><td>Medium</td><td>High</td></tr><tr><td>Information Density</td><td>Long Term Orientation (LTO)</td><td>To-do items provide little information at first sight, requiring a user to click before seeing more information</td><td>To-do list shows all information at first sight</td><td>Complex version that additionally presents encoded information with big icons</td></tr><tr><td>Navigation</td><td>Power Distance (PDI)</td><td>Tree menu and to-dos in list view, allows nested sorting</td><td>Flat navigation and list view, or tree menu and icon-represented to-do list</td><td>Flat navigation and icon-represented to-do list</td></tr><tr><td>Accessibility of functions</td><td>Power Distance (PDI)</td><td>Functionalities are always accessible but grayed out if not needed</td><td>Functionalities appear on mouse-over</td><td>Functionalities are always accessible</td></tr><tr><td>Guidance</td><td>Uncertainty Avoidance (UAI)</td><td>While users enter a dialog, all other information on the UI retains visible and accessible</td><td>Information other than the current dialog is still visible, but inaccessible</td><td>Unnecessary information is hidden in order to force users to concentrate on a currently active dialog</td></tr><tr><td>Structure</td><td>Power Distance (PDI)</td><td>Minimum structure: Different elements of the UI are only structured through alignment</td><td>Elements are separated and each color-coded for better distinction</td><td>Maximum structure: Elements are bordered and affiliations between information is accentuated across elements</td></tr><tr><td>Colorfulness</td><td>Individualism (IDV)</td><td>Many different colors</td><td>A medium number of colors</td><td>The UI is homogeneously colored</td></tr><tr><td>Saturation</td><td>Masculinity (MAS)</td><td>Pastel colors with little saturation</td><td>Medium saturation and contrast</td><td>Highly contrasting, bright colors</td></tr><tr><td>Support</td><td>Uncertainty Avoidance (UAI)</td><td>On-site support with the help of short tool- tips</td><td>The UI offers question mark buttons that expand into help bubbles</td><td>An adaptive wizard that is always visible</td></tr></table>

The core task of the ontology is to store information about an element’s possible placement areas within the UI, and to connect the different versions of each UI element with a specific score for one or more of the cultural dimensions. The element with the score closest to the one stored in the user’s cultural user model instance is later selected by the application and taken for the composition of the personalized interface.

While the adaptation ontology is designed to define possible interface compositions, the application itself has the responsibility of retrieving and interpreting this information. It is, therefore, interwoven with the cultural user model ontology, which stores the information about the user’s cultural background including his or her dimension scores. The retrieval of these scores is a precondition for triggering the corresponding adaptations: At first, the application has to read out the user’s scores and, possibly, other information about the user’s cultural background. Second, it has to look up the corresponding adaptation rules in the adaptation ontology by traversing the interface elements for ones that correlate with the user’s scores. Note that this correlation has to be defined by the application; in our approach, the UI elements are chosen according to what gives the smallest difference between the user’s cultural score in the related dimension and the score assigned to the respective UI element. After this comparison has been completed, the application can compose the UI. Since this is subject to implementation details and the technologies used, we will describe the information extraction process from the ontology, as well as the composition of the UI with our culturally adaptive web application MOCCA in the next section.

## Artifact 5: A Prototype Culturally Adaptive System

As a proof-of-concept and experimental vehicle, we have developed MOCCA, a web application that serves as a to-do list tool, helping users to access and manage their tasks online. The advantage of this application is that it relies on user-generated content (such as to-dos) and, thus, cannot influence participants with content or information that might be culturally biased. Some examples of MOCCA’s interfaces are shown in Figure 3. MOCCA is able to adapt its interface to the user’s cultural background based on the procedure described in Figure 4.

1. During the registration process, MOCCA asks the user about his/her current country of residence, about former countries he/she has lived in, and the length of stay in each country.

2. MOCCA derives the percentage influence of each of these countries according to the duration of the user’s stay at those places. In the case of Figure 4, the user previously lived in Norway and Australia, but spent the majority of her life in China. This user-specific information is stored in the cultural user model ontology.

3. For each of the user’s countries of residence, MOCCA retrieves Hofstede’s scores from the cultural user model ontology.

4. MOCCA calculates a five-dimensional vector based on the weighted averages of the different national cultures. Each dimension in this five-dimensional vector is labeled low, medium, or high depending on its world average: Scores that fall below or exceed the world average score for the corresponding dimension by ±10 points, are classified as medium, and scores below or above this range as low or high respectively. The five-dimensional vectors and their labels are passed on to the adaptation ontology.

5. The labels for each dimension are now mapped to certain adaptations of MOCCA’s interface. For our example user, MOCCA’s adaptations would include increased guidance, shallow menu structures, strong colors, and a complex interface, as shown in Figure 3(a).

According to Table 3, MOCCA considers eight adaptable aspects of the interface, each of which can be individually altered to either a low, medium, or high classification of the dimension with which they are associated. In addition, MOCCA can adapt itself to the user’s reading direction (i.e., left-to-right, right-to-left). The technical implementation that allows these possible combinations of user interface elements is described in Appendix B. With this initial adaptation process, MOCCA relies on estimating the user’s cultural background based on a weighted average of national cultures. Note that MOCCA enables further refinement of a person’s cultural background by entering more information into its user model editor (e.g., about educational background or religion). At any stage of use, changes in the cultural user model ontology can then trigger adaptations of MOCCA’s UI. Beyond this, MOCCA offers the possibility to manually refine the look and feel of the UI with the help of its built-in preference editor.

## Experiments

We report on two summative evaluations of MOCCA’s ability to adequately adapt to the varying UI preferences of users of different cultural backgrounds. The first study focuses on participants with a multicultural background, whom we refer to as culturally ambiguous, because they have been influenced by several countries of residence. We show that the algorithm, which calculates the user’s cultural background based on a weighted average of current and former residencies, is suitable for predicting their UI preferences. Subsequently, we evaluate MOCCA with culturally unambiguous users who have only lived in one country. This second set of evaluations was conducted in Rwanda, Switzerland, and Thailand.

## Method

Participants. To evaluate MOCCA’s performance for culturally ambiguous participants (Study 1), we recruited 30 participants from the local university campus (age: 24–37, mean = 28.7; 7 female). The majority of participants had lived in two or more countries (mean = 2.47, sd = 0.89). For Study 2 on the evaluation of participants who were influenced by only one country of residence, we conducted experiments in Rwanda, Switzerland, and Thailand. The countries were selected because of their physical distance (being located on three different continents), which we expected to reflect cultural diversity. Figure 5 shows an overview of the Hofstede scores for each of the three countries. Note that Hofstede’s studies did not include Rwanda, but the whole region of East Africa. In addition, Switzerland was one of the countries that was not evaluated with regards to their long term orientation. We adopted the German classification of a low long term orientation (score 31), since it is likely that our Swiss German participants would have been allocated a similar score.

![](/api/attachments/5DAX6PXW/fulltext/images/e1055b5cb15fc003d06896636f7911f4dc4a91fbc6dafe8e7ef3da543db2a836.jpg)  
(a) MOCCA with a button navigation, a wizard for increased guidance, and strong colors. Most explanatory items are replaced by symbols, giving the interface a playful look and feel.

![](/api/attachments/5DAX6PXW/fulltext/images/60d0d94f95f32e349670b952e2be69ffeff53b31eaf933831860471923be976a.jpg)  
(b) A monotonously colored version of MOCCA with a tree navigation and a simple interface.

![](/api/attachments/5DAX6PXW/fulltext/images/72459a782661f55e9c16483d0715b966f8b067c5695736a8f767807f67726a42.jpg)  
(c) MOCCA with right-to-left alignment with the flat navigation on the right side.

MOCCA ? about logout  
![](/api/attachments/5DAX6PXW/fulltext/images/b02de03f297dfcd2b4cb643cf0c6daee48304078d7ac74d9184533d10d8d38ea.jpg)  
(d) An interface with a medium complexity and a medium colorfulness.

Figure 3. Different Personalized Versions of MOCCA’s User Interface That Were Generated Taking into Account the Users’ Cultural Backgrounds  
![](/api/attachments/5DAX6PXW/fulltext/images/892368fea5861d4d4a4e1aba6895d613492d71f2b39d746021a8670030b71a8e.jpg)  
Figure 4. MOCCA’s Initial Adaptation Process with a User Who Has Previously Lived in China, Norway, and Australia

![](/api/attachments/5DAX6PXW/fulltext/images/091689a096195960b257c6255633d12d123e69dfa38fe9af8fce87f597d6dfe2.jpg)  
Figure 5. Test Country Dimensions for Thailand, Rwanda, and Switzerland According to Hofstede

We recruited a total of 75 participants for Study 2: 30 participants from Thammasat University in Bangkok, Thailand (mean age = 20.7; 21 female), 21 participants from the National University of Rwanda (mean age = 25.6; 4 female), and 24 participants from the University of Zurich in Switzerland (mean age = 26.5; 8 female). In order to minimize other influences on participants’ national culture, only students at university level (Person#hasEducationLevel 0 universityDegree in terms of our ontology) were invited to take part in our studies, thus ensuring a high education level amongst all participants. We also controlled for a high computer literacy (Person#has ComputerLiteracy 0 high) to avoid a bias that could result from a varying knowledge of common UI components and functionalities.

Apparatus. The evaluations used a modification of the paper prototyping method (Snyder 2003), which is a common usability testing procedure in user-centered design. MOCCA’s interface was replaced by paper-based UI mockups in shades of gray (see Appendix C for some examples), which enabled participants to choose their preferred layout without being influenced by colors. Only the tasks on colorfulness and saturation involved sets of colors from which participants were asked to choose.

Procedure. Prior to explaining the tasks, we asked participants to put themselves in the position of a UI designer, who is developing the software for their own use. Participants were expected to consider their own experiences and preferences with UIs. They were encouraged to take their time to go through the tasks and to ask questions for clarification. We then briefly explained the application’s purpose and its main functionalities (e.g., the possibility to create to-dos, categories, and projects).

Participants were presented with an outline of the MOCCA interface within which they were asked to place their choice of UI elements. For every task, participants were asked to choose between three interface elements, as they are listed in Appendix C. They were able to see all three UI elements for each task at once and arrange them freely. Each participant had to perform a total of eight tasks concerning the following eight interface aspects (see also Table 3): (1) information density, (2) navigation, (3) accessibility of functions, (4) guidance, (5) structure, (6) colorfulness, (7) saturation, and (8) support. The tasks were presented in the same order for each participant as they partly built on one another. The presentation order of the three different choices of UI elements per task was counterbalanced between participants. We preceded each task with a short explanation, where the main differences between the three choices were pointed out. In order to avoid influencing the users’ decisions, we followed a written script that enabled us to keep the explanations both consistent and neutral. Throughout the experiment, participants were encouraged to think aloud and these comments were noted. On completion of each task, we took photos of the arrangement on the UI outline (see Figures 6(a) and 6(c) as an example). The study ended with a small questionnaire soliciting information about the participant’s current and possible former countries of residence with durations in years and months. We also recorded the nationality of the participant’s father and mother as well as the participant’s age and gender. Participants were given monetary compensation for their time.

![](/api/attachments/5DAX6PXW/fulltext/images/c8fbb259286dd07a13d1aea2c5421fc3fca769db8937c6077dad63d3c49bf9d7.jpg)  
(a) The user interface as chosen by Participant 3 in our first experiment (PDI = low, IDV = high, UAI = normal, LTO = low).

![](/api/attachments/5DAX6PXW/fulltext/images/90d277a2acf3e08d7d300c342df6622fef0c8b03748a73583fd27ec7a71106b5.jpg)  
(c) The user interface as chosen by Participant 3 in our first experiment (PDI = high, IDV = low, MAS = high; UAI = low, LTO = high).

![](/api/attachments/5DAX6PXW/fulltext/images/4831ddeb2b5db0c4cdea2cce7c55e052e839b0fcdede4361f2ff4586b5124313.jpg)  
(b) MOCCA’s automatically generated UI for Participant 3.

![](/api/attachments/5DAX6PXW/fulltext/images/3b57e516e7503afdf79a2163d612b1d4d483cb2e4000607476fb14153f9764ed.jpg)  
(d) MOCCQA’s automatically generated UI for Participant 27.  
Figure 6. The Final Self-Built Interface in Comparison to the Interface Generated by MOCCA for Two Different Participants

Test Design and Analysis. Our independent variables were cultural background (five dimensions) and the user interface design (with eight levels of interface aspects, corresponding to eight tasks). We used a within-subjects design so that the eight tasks resulted in a complete user interface for each participant.

Controlled variables were participant’s age, education level, and computer literacy. Our dependent measures were participant’s choices of an interface element (low, medium, or high) for each task. Additionally, we were interested in comparing each participant’s self-designed UI to the one that MOCCA provided for this participant. Such variations between the user’s choice when selecting one of three interface elements per task and the element recommended by MOCCA are recorded with the dependent variable choicedeviation score. Because there are three interface elements per task, this score can take the values 0 (correct prediction), 1, and 2. Every participant receives one choice-deviation score per task.

## The whole procedure for analysis was as follows:

We first entered a participant’s information about current and former countries of residences plus the respective durations into MOCCA’s user modeling component, which automatically classified the user into low, medium, or high for each of the five dimensions. This triggered a personalized UI for each participant, composed of those elements that correspond to this classification.

Participant’s choices in each of the eight tasks were also translated into low, medium, or high following their classification in Table 3.

The comparison between a participant’s choices and the interface elements that MOCCA generated according to its adaptation rules then allowed us to calculate the choice-deviation score. If MOCCA had predicted a low individualism, for example, and the user chose the corresponding element in our test, we noted a deviation of 0. If instead, he or she chose the medium element, the deviation resulted in 1. If MOCCA calculated a participant’s uncertainty avoidance index to be high, but this participant chose the UI element assigned to the category low, we noted a deviation of 2 (the maximum deviation). With these three choices between UI elements, the probability of randomly guessing the right choice was 33 percent, or p = 1/3.

MOCCA’s prediction accuracy was evaluated based on the frequency of the choice-deviation score being 0. The higher the number of times that MOCCA generated the same user interface element for a task as chosen by the user, the higher its prediction accuracy. For analysis, we coded correct predictions with 1, and incorrect ones with 0 per task and participant. Remember that the expected frequency of a choice-deviation score of 0 was 33 percent, as this frequency could have been achieved at random. To test whether MOCCA reached a significantly higher frequency, we used Pearson’s chi-square test for categorical data (with one degree of freedom).

We also used chi-square tests to investigate the distribution of participants’ choices for each interface aspect and country in order to note whether a significant majority (called majority in the following) had chosen the same element. This resulted in a contingency table of three countries by three possible choices with four degrees of freedom. Additionally, the distribution of choices between two countries was compared with a chi-square test and a two countries by three possible choices contingency table (two degrees of freedom). For cell counts with an expected frequency below five, we applied Fisher’s exact test to follow-up results.

Adjustment of Data. In the first experiment, we excluded the task on structure from analysis after the majority of participants made a choice contradictory to their oral statements. Specifically, they found the design of the low-structure version to be slightly confusing, and named this as a reason for choosing one of the other versions. Overall, the version for a maximum structure (high PDI in Table 3) was preferred by

14 participants, which was different from the fairly even distribution of choices we achieved testing other interface aspects. For the second experiment, we redesigned this UI aspect taking into account participants’ comments. The result section on our first experiment with culturally ambiguous participants therefore reports on the data from 7 tasks performed by 30 participants.

Hypotheses. We proposed the following hypotheses:

Hypothesis H.1(a): MOCCA’s accurate predictions are better than chance. The initial adaptation rules based on Hofstede’s dimensions are better in predicting the user’s choices of interface elements (demonstrated by a choice-deviation score of 0) than what can be expected by chance.

Hypothesis H.1(b): MOCCA’s mis-predictions are mostly slight rather than severe. The second highest frequency of choice-deviation scores will be for the medium choicedeviation value (1), indicating that in most cases where there is not an exact match, the user’s choice is close to MOCCA’s recommendation. The fewest number of choices are for maximum choice-deviation value (2).

H.1(a) and H.1(b) address the core assumption of our approach: the ability to predict the user’s preferences based solely on his/her (extended) national culture. If MOCCA does not accurately predict the user’s choice, we assume that, in the majority of cases, the prediction does not completely oppose the user’s choice.

Hypothesis H.2: UI preferences can be clustered by culture. (Tested in the second experiment.) The majority of users within a (national) culture choose the same UI elements.

H.2 tests if people from the same country have similar UI preferences. If positive, it could serve to refine our adaptation rules based on the preferences of people of the same national culture. Moreover, a positive H.2 would confirm the need for culturally adaptive systems even if our particular approach fails.

## Study 1: Accuracy of the Adaptation Rules for Culturally Ambiguous Users

The first study<sup>6</sup> aims to evaluate whether MOCCA’s adaptation rules are suitable for predicting UI preferences of multicultural (or culturally ambiguous) users.

Table 4. Summary of the Prediction Results for N = 30 Culturally Ambiguous Users (in Percent)

<table><tr><td>Interface Choice/Task</td><td>Dimension</td><td>Correct Predictions</td><td>Deviation of 1</td><td>Deviation of 2</td></tr><tr><td>Information Density</td><td>LTO</td><td>90.0</td><td>6.7</td><td>3.3</td></tr><tr><td>Navigation</td><td>PDI</td><td>56.7</td><td>36.7</td><td>6.7</td></tr><tr><td>Accessibility of Functions</td><td>PDI</td><td>60.0</td><td>40.0</td><td>0</td></tr><tr><td>Guidance</td><td>UAI</td><td>66.7</td><td>30.0</td><td>3.3</td></tr><tr><td>Colorfulness</td><td>IDV</td><td>50.0</td><td>36.7</td><td>13.3</td></tr><tr><td>Saturation</td><td>MAS</td><td>53.3</td><td>26.7</td><td>20.0</td></tr><tr><td>Support</td><td>UAI</td><td>50.0</td><td>50.0</td><td>0</td></tr><tr><td>Average</td><td></td><td>61.0</td><td>32.4</td><td>6.7</td></tr></table>

Depending on the task, the adaptation rules correctly predicted the preferences of at least 15 and at most 27 participants (mean = 18, sd = 4.23), with an overall prediction accuracy of 61 percent (see Table 4 for a summary of the percentage occurrence of the choice-deviation scores for all task). Thus, compared to the 33 percent that could be expected by chance, the results show that MOCCA is able to correctly anticipate (choice-deviation score = 0) a majority of participants’ preferences.

However, not all participants’ choices were accurately predicted. An average of 9.1 (sd = 4.07) out of our 30 international participants across all tasks received an interface version that deviated from their own choice by one. Only two participants on average across all tasks (sd = 2.23) received predictions with a choice-deviation score of 2.

Comparing our observed data per task with the result of chance, our results show that the deviation scores are better than a random assignment of interface choices (see Table 5). This shows that our adaptation rules are beneficial for predicting user preferences not just overall, but for every single task.

According to these results, H.1(a) was supported: The calculation of cultural dimensions based on Hofstede’s country scores and the influences of other countries of residence enabled us to correctly predict the majority of user interface preferences. In addition, the majority of mis-predictions happened with a choice-deviation score of 1 for all tasks, which supports H.1(b).

Distribution of Choices. By analyzing our data based on an equal distribution of probabilities with p = 1/3 we assumed that participants’ choices were roughly balanced across our three interface versions per task. If one version had been avoided by most or even all participants, this would suggest that it was not well designed, or was flawed in some other respect. In our experiment, the distribution of choices was balanced: Elements assigned to a low score were chosen 72 times, the elements for a medium score 76 times, and the elements for a high score 62 times. Thus, participants went for the extremes in 134/210 of the cases (approximately 64%).

Impact of Other Cultural Influences. Participants were chosen based on a high computer literacy in order to avoid a bias due to differences in the knowledge of common UI functionalities. Despite this, participants with strongly differing cultural backgrounds showed noticeable differences in the choice of interface elements—an observation that will be strengthened by the results of our next experiment. We therefore assume that a high computer literacy and a regular use of computers does not necessarily supersede cultural preferences; in other words, people do not automatically adopt the same attitudes towards usability and aesthetics when regularly being exposed to foreign user interfaces, as for example on the Internet. This is consistent with previous theories that cultural exchange does not necessarily lead to a substantial adoption of foreign values, but instead, the outside influence sometimes enhances one’s own cultural identity (Sahlins 1993).

Similarly, we anticipated higher education levels to result in a more limited spread of choices, which were instead uniformly distributed according to participants’ dimensions. Thus, participants’ extended national culture seemed to have a greater influence on their preferences than the subcultural influence of a shared education level.

Finally, we looked at the influence of the parents’ nationality. As cultural differences appear to develop early in life (Fernald and Morikawa 1993), we expected the parents’ nationality to have a strong impact on the participant’s preferences toward parents’ cultural background. After adding Hofstede’s dimensions for parents’ nationality with an estimated impact of 25 percent to the participants’ dimensions, the score of 7 participants (out of 30) changed in a way that it would trigger a different adaptation of the UI. The number of correct predictions (choice-deviation scores = 0), however, decreased for six of the seven participants with the new adaptation, resulting in an overall lower rate of correct predictions (mean before = 5.1, mean after = 3.4). Hence, the parents’ nationality did not enhance the prediction accuracy in our case—a result that is in line with our preliminary evaluation, as briefly described earlier in the Artifact 2 section. Intuitively, we are almost certain that a differing nationality of the parents does affect a person’s cultural preferences, such as experienced with migrants. The reason we did not find any such changes in participants’ preferences could be due to our small sample, combined with the fact that all participants had a high computer literacy, and a high education level.

<table><tr><td colspan="3">Table 5. Results Demonstrate That the Deviation Scores Are Better than a Random Assignment of Interface Choices</td></tr><tr><td>Interface Choice/Task</td><td> $\chi^2_{(1)}$ </td><td>Significance</td></tr><tr><td>Information Density</td><td>44.08</td><td>p &lt; .001</td></tr><tr><td>Navigation</td><td>7.6</td><td>p &lt; .01</td></tr><tr><td>Accessibility of Functions</td><td>9.89</td><td>p &lt; .01</td></tr><tr><td>Guidance</td><td>15.38</td><td>p &lt; .001</td></tr><tr><td>Colorfulness</td><td>3.92</td><td>p &lt; .05</td></tr><tr><td>Saturation</td><td>5.61</td><td>p &lt; .05</td></tr><tr><td>Support</td><td>3.92</td><td>p &lt; .05</td></tr></table>

## Study 2: Accuracy of the Adaptation Rules for Users Influenced by Only One Country of Residence

The results of our first study demonstrated that MOCCA, to a large extent, is able to correctly predict preferences of culturally ambiguous users. This follow-up study was designed to evaluate MOCCA’s performance for users who have lived in only a single country, with three experiments in Thailand, Rwanda, and Switzerland. Apart from the validation of the adaptation rules, it also aimed to find out whether preferences for users of the same country are indeed similar, as previous work suggests. If this is the case, a learning mechanism could be used to modify the adaptation rules by gathering knowledge about the design preferences of people with a similar cultural background.

The results of our experiments in Thailand and Switzerland were comparable to our first study with culturally ambiguous users. MOCCA was able to accurately predict 60.8 percent of the Thai participants’ preferences, and 56.8 percent of the preferences of our Swiss participants. Only in Rwanda did our adaptation rules fail to perform better than chance with only 24.4 percent accurate predictions. The prediction results for all three countries are shown in Tables 6, 7, and 8. According to these results, H.1(a) was supported for Thailand and Switzerland, but not for Rwanda. Our hypothesis H.1(b) was that if there were incorrect predictions, the majority of the choice-deviation scores would be 1 rather than 2. The results for Thailand supported H.1(b) for all tasks but colorfulness and saturation. Rwanda showed a similar picture, with the majority of incorrect predictions deviating by only one. However, two tasks on information density and colorfulness did not confirm H.1(b) in Rwanda. The choices of Swiss participants contradicted our predictions with a choicedeviation score of 2 for the three tasks structure, colorfulness, and saturation. The majority of tasks, however, showed support for H.1(b) in Switzerland.

Interestingly, participants of the same country mostly agreed in their choices. In all three countries, a significant majority of participants of the same national culture chose the same element in at least six of eight tasks (p < .05), supporting H.2. The main choices in each country are summarized in Table 9 and marked with an asterisk (\*) if they matched our predictions. Nonsignificant results indicate that there was no agreement in participants’ choices within that country.

Contrasting the relatively homogeneous choices within countries, participants’ preferences significantly differed between countries for seven out of eight tasks (see column “Between All Three Countries” in Table 10). Only the second task, which asked for the preferred navigation, showed similar frequency distributions for all three countries.

We were not able to determine significant majority choices for the navigation task for Thailand, and Rwanda. Likewise, our Swiss participants did not clearly favor one interface version over another in this task (p < .1; see Table 9). The task on structure showed a similar diversity in choices for Thailand and Switzerland, while we did find a clear majority choice for our Rwandan participants for this task. Rwandans, in contrast, did not agree on a specific saturation of colors. Of all these tasks, however, structure is the only one that resulted in controversial choices. Our Swiss participants, for example, equally favored the low and the highly structured version. For all other tasks, we believe that a larger number of participants in the future will help us to determine which interface version is preferred by a majority of people in a specific country. MOCCA’s resulting UIs for the three countries after accounting for the majority choices look clearly different (see the right column in Figure D1, Appendix D), which also supports our argument that user interface preferences are dependent on national culture.

Table 6. Summary of the Prediction Results for N = 30 Thai Users (in Percent)

<table><tr><td>Interface Choice/Task</td><td>Dimension</td><td>Correct Predictions</td><td>Deviation of 1</td><td>Deviation of 2</td></tr><tr><td>Information Density</td><td>LTO</td><td>20.0</td><td>80.0</td><td>0</td></tr><tr><td>Navigation</td><td>PDI</td><td>43.3</td><td>56.7</td><td>0</td></tr><tr><td>Accessibility of Functions</td><td>PDI</td><td>56.7</td><td>43.3</td><td>0</td></tr><tr><td>Guidance</td><td>UAI</td><td>83.3</td><td>16.7</td><td>0</td></tr><tr><td>Structure</td><td>PDI</td><td>46.7</td><td>46.7</td><td>6.7</td></tr><tr><td>Colorfulness</td><td>IDV</td><td>86.7</td><td>3.3</td><td>10.0</td></tr><tr><td>Saturation</td><td>MAS</td><td>93.3</td><td>0</td><td>6.7</td></tr><tr><td>Support</td><td>UAI</td><td>56.7</td><td>43.3</td><td>0</td></tr><tr><td>Average</td><td></td><td>60.8</td><td>36.3</td><td>2.9</td></tr></table>

Table 7. Summary of the Prediction Results for N = 21 Rwandan Users (in Percent)

<table><tr><td>Interface Choice/Task</td><td>Dimension</td><td>Correct Predictions</td><td>Deviation of 1</td><td>Deviation of 2</td></tr><tr><td>Information Density</td><td>LTO</td><td>14.3</td><td>23.8</td><td>61.9</td></tr><tr><td>Navigation</td><td>PDI</td><td>42.9</td><td>57.1</td><td>0</td></tr><tr><td>Accessibility of Functions</td><td>PDI</td><td>28.6</td><td>71.4</td><td>0</td></tr><tr><td>Guidance</td><td>UAI</td><td>19.1</td><td>61.9</td><td>19.1</td></tr><tr><td>Structure</td><td>PDI</td><td>9.5</td><td>90.5</td><td>0</td></tr><tr><td>Colorfulness</td><td>IDV</td><td>9.5</td><td>42.9</td><td>47.6</td></tr><tr><td>Saturation</td><td>MAS</td><td>47.6</td><td>52.4</td><td>0</td></tr><tr><td>Support</td><td>UAI</td><td>23.8</td><td>76.2</td><td>0</td></tr><tr><td>Average</td><td></td><td>24.4</td><td>59.5</td><td>16.1</td></tr></table>

Table 8. Summary of the Prediction Results for N = 24 Swiss Users (in Percent)

<table><tr><td>Interface Choice/Task</td><td>Dimension</td><td>Correct Predictions</td><td>Deviation of 1</td><td>Deviation of 2</td></tr><tr><td>Information Density</td><td>LTO</td><td>54.2</td><td>33.3</td><td>12.5</td></tr><tr><td>Navigation</td><td>PDI</td><td>37.5</td><td>45.8</td><td>16.7</td></tr><tr><td>Accessibility of Functions</td><td>PDI</td><td>41.7</td><td>50.0</td><td>8.3</td></tr><tr><td>Guidance</td><td>UAI</td><td>62.5</td><td>37.5</td><td>0</td></tr><tr><td>Structure</td><td>PDI</td><td>37.5</td><td>25.0</td><td>37.5</td></tr><tr><td>Colorfulness</td><td>IDV</td><td>62.5</td><td>12.5</td><td>25.0</td></tr><tr><td>Saturation</td><td>MAS</td><td>75.0</td><td>0</td><td>25.0</td></tr><tr><td>Support</td><td>UAI</td><td>83.3</td><td>16.7</td><td>0</td></tr><tr><td>Average</td><td></td><td>56.8</td><td>27.6</td><td>15.6</td></tr></table>

Table 9. Majority Choices for All Three Test Countries (\* as predicted, significance of χ<sup>2</sup>-test with df = 2)

<table><tr><td>Interface Choice/Task</td><td>Dimension</td><td>Thailand</td><td>Rwanda</td><td>Switzerland</td></tr><tr><td>Information Density</td><td>LTO</td><td>high, p &lt; .01</td><td>high, p &lt; .05</td><td>low*, p &lt; .05</td></tr><tr><td>Navigation</td><td>PDI</td><td>medium*, n.s.</td><td>medium*, n.s.</td><td>medium, p &lt; .1</td></tr><tr><td>Accessibility of Functions</td><td>PDI</td><td>medium*, p &lt; .001</td><td>high, p &lt; .001</td><td>medium, p &lt; .05</td></tr><tr><td>Guidance</td><td>UAI</td><td>medium*, p &lt; .001</td><td>medium, p &lt; .05</td><td>medium*, p &lt; .001</td></tr><tr><td>Structure</td><td>PDI</td><td>low &amp; med.*, n.s.</td><td>low*, p &lt; .05</td><td>low &amp; high*, n.s.</td></tr><tr><td>Colorfulness</td><td>IDV</td><td>low*, p &lt; .001</td><td>high, p &lt; .001</td><td>high*, p &lt; .01</td></tr><tr><td>Saturation</td><td>MAS</td><td>low*, p &lt; .001</td><td>medium*, n.s.</td><td>high*, p &lt; .001</td></tr><tr><td>Support</td><td>UAI</td><td>medium*, p &lt; .05</td><td>high*, p &lt; .001</td><td>medium, p &lt; .001</td></tr></table>

Table 10. Differences in the Distribution of Choices Between Countries, and Between Rwanda and Thailand, Who Share Mostly Similar Dimensions

<table><tr><td>Interface Choice/Task</td><td>Dimension</td><td>Between All Three Countries</td><td>Between Rwanda and Thailand</td></tr><tr><td>Information Density</td><td>LTO</td><td> $\chi^{2}_{(4)} = 16.92, p < .01$ </td><td>n.s.</td></tr><tr><td>Navigation</td><td>PDI</td><td>n.s.</td><td>n.s.</td></tr><tr><td>Accessibility of Functions</td><td>PDI</td><td> $\chi^{2}_{(4)} = 34.71, p < .001$ </td><td> $\chi^{2}_{(2)} = 3.94, p < .05$ </td></tr><tr><td>Guidance</td><td>UAI</td><td> $\chi^{2}_{(4)} = 11.67, p < .05$ </td><td>n.s.</td></tr><tr><td>Structure</td><td>PDI</td><td> $\chi^{2}_{(4)} = 13.30, p < .01$ </td><td> $\chi^{2}_{(2)} = 10.68, p < .01$ </td></tr><tr><td>Colorfulness</td><td>IDV</td><td> $\chi^{2}_{(4)} = 41.71, p < .001$ </td><td> $\chi^{2}_{(2)} = 30.09, p < .001$ </td></tr><tr><td>Saturation</td><td>MAS</td><td> $\chi^{2}_{(4)} = 60.21, p < .001$ </td><td> $\chi^{2}_{(2)} = 24.70, p < .001$ </td></tr><tr><td>Support</td><td>UAI</td><td> $\chi^{2}_{(4)} = 34.44, p < .001$ </td><td> $\chi^{2}_{(2)} = 18.39, p < .001$ </td></tr></table>

## Summary of All Results and Discussion

Both of our experiments showed promising results that mostly support our design rationale to calculate a user’s extended national culture using Hofstede’s dimensions. Recall that this decision was made in order to be able to infer user interface preferences for any national culture, and any weighted combination of different national cultures. To this end, we evaluated the extent to which MOCCA is able to present participants with an interface that corresponds to their selfbuilt paper-prototype interface. We will now summarize the results of all experiments (see Table 11 for an overview of the hypothesis testing).

H.1(a): Across all participants and tasks, MOCCA’s adaptation rules proved to be significantly better in predicting our participants’ choices than a random assignment of UI elements. Specifically, the calculation of a user’s extended cultural background based on a weighted average of influences of other countries of residence demonstrated a good prediction accuracy $( \chi _ { \tiny { ( 1 , \mathrm { N } = 3 0 ) } } ^ { 2 } , \mathfrak { p } < . 0 1$ across all seven tasks for our culturally ambiguous participants). H.1(a) was further substantiated by the results of our evaluations in Switzerland and Thailand, where MOCCA correctly predicted a majority of participants’ preferences. The hypothesis was not supported for Rwanda, where MOCCA’s prediction accuracy was a mere 24.4 percent.

Table 11. Summary of the Hypothesis Testing Results (Check marks indicate that the hypothesis was supported)

<table><tr><td>Test Group</td><td>H.1(a)</td><td>H.1(b)</td><td>H.2</td></tr><tr><td>Culturally ambiguous participants</td><td>✓</td><td>✓</td><td>N/A</td></tr><tr><td>Thailand</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Rwanda</td><td>✕</td><td>✓</td><td>✓</td></tr><tr><td>Switzerland</td><td>✓</td><td>✓</td><td>✓</td></tr></table>

MOCCA’s failure to predict the choices of our Rwandan participants could have several reasons. First, Hofstede’s dimensions do not include Rwanda, but summarize several East African countries. It is possible that the scores adopted for Rwandans do not adequately represent their national culture. Second, our adaptation rules rely on a mapping of previous studies on Hofstede’s dimensions to user interface preferences. These studies have mostly compared Europeans, Americans, and Asians, while only a very few addressed countries in Africa. If correlations between Hofstede’s dimensions and user interface preferences have been found in those countries, it could be that additional studies in countries in Africa would have refuted specific links between one dimension and certain preferences.

However, the negative result for Rwanda has several implications for our approach. We cannot readily assume that our method generalizes to any country in this world. This means that it is important to provide users with the ability to manually modify the interface if the initial version is not sufficiently adapted to their preferences. MOCCA already offers this possibility with its built-in preference editor. Additionally, we believe that it is possible to refine our adaptation rules over time, which is discussed in Appendix D.

H.1(b): We assumed that prediction errors mostly occur with a choice-deviation score of 1 and, thus, that MOCCA is able to reduce those cases to a minimum where it falsely triggers the completely opposite UI element (choice-deviation score of 2). We were able to substantiate this hypothesis with on average 39.1 percent of the predictions deviating by 1, but only 10.1 percent deviating by 2 from participants’ choices across all experiments.

While these results are encouraging, they also indicate the need for manual overrides: in practice, offering an interface aspect to users with opposing preferences without any alternatives could mean that these users refrain from using the application. Hence, the finding confirms the need for intervention possibilities that allow users to choose alternatives.

H.2: The results of our second experiment are especially interesting seeing that the use of national culture as a concept to assume the same preferences for all users within one country is highly disputed. Our experiments suggest that, when controlling for education level and computer literacy, the majority of participants of the same country do have similar UI preferences. Hypothesis H.2 was, therefore, supported for all three test countries for at least six of eight tasks. Moreover, participants’ choices highly differed between countries, which indicates that preferences are indeed dependent on national culture to some extent. In Appendix D, we show a possibility to improve MOCCA’s prediction accuracy by learning from users’ majority choices. The correct predictions increased to 65.8 percent for Thailand and 60.4 percent for Switzerland. For Rwanda, the number of correct predictions more than doubled with a new prediction accuracy of 54.2 percent.

## Limitations and Future Work

As with most novel approaches, our research on cultural adap tivity has opened up possibilities for new and exciting future research.

The experiments presented in this paper show that the conjunction of artifacts designed can indeed be used to support a cultural adaptive system. Our experiments do not show, however, if the design choices made were optimal. First, the ontologies (Artifacts 1 and 4) are both the result of a knowledge engineering effort. Other modeling techniques may be more suitable for similar studies. Future work needs to compare these designs to others and establish their strengths and limitations. Second, the approximation algorithm (Artifact 2) relied on the assumption that cultural influences could be aggregated with a weighted linear model. This assumption counters the intuition that influences during school years or from the parents’ background outweigh those of later years (note that we did not find the latter effect). We believe that this simplified aggregation algorithm should deserve scrutiny in the future, once research has established a better understanding of how our aesthetic preferences evolve. It would be exciting to see whether other models, or a combination of Hofstede with refining variables, result in more accurate predictions.

Third, the adaption rules (Artifact 3) were the results of an extensive literature review. While we made every effort to be exhaustive, our adaptation rules are based on findings in the literature that are not entirely comparable, and the implications of study results are often a matter of interpretation. This is mainly due to different study designs, and varying demographics of participants, which makes it impossible to generalize findings, or compare the results of different national cultures if they were not directly contrasted in one and the same study. Nevertheless, we were able to show that our adaptation rules can serve as a basis for a library of culture-related UI guidelines.

Last but not least, our prototype system, MOCCA, focused on task management. Arguably, further evaluations should also address the generalizability of our approach for other domains beyond that of a to-do list application. The experiments themselves also entail some threats to validity. In particular we need a broader range of participants, both in terms of having subjects with a higher cultural diversity (i.e., more countries) and in terms of higher demographic diversity (e.g., in terms of age distribution, prior education, etc.). To expand on this issue: In our studies, we controlled for a high education level, and a high level of computer literacy. It would be interesting to see how the prediction accuracy rate behaves, and whether it can be even further improved if taking into account different education levels and computer skills, or other aspects that influence culture.

Also, our experiments showed that some people’s preferences were more predictable by our adaptation rules than others. In future evaluations, larger numbers of participants are needed to analyze which factors lead users to deviate from the crowd. Such a study could also lay the foundation to explore if the 60 to 70 percent threshold that we found in MOCCA’s prediction accuracy can be passed with a better prediction method, background information, other user’s usage information, and/or other personalization techniques. In the future, we also plan to investigate the effects of cultural adaptivity in a long-term study by evaluating the initial user satisfaction, and comparing it to customer retention and the number of successful transactions at different points in time. Future work also concerns the adaptation of content to cultural background, and the integration of this into a holistic approach to cultural adaptivity.

## Conclusion

Today’s user interfaces are usually designed in a “one size fits all” approach, disregarding the fact that design preferences differ between cultures. While more and more websites offer localized versions of their content, the conventional approach to localization is geared toward adaptations of the language and date/time formats, but not toward the entire design. This ignores the variety of user preferences that needs to be considered in order to adapt to cultural background. As a result, many users access web pages or software interfaces that they do not find appealing.

In this paper, we have argued that interfaces that automatically adapt their entire presentation to a user’s national culture—taking into account the current location and former countries of residence—can better fit users’ preferences. Our main contributions are a design approach for culturally adaptive UIs, the introduction of different artifacts that support the implementation, and an evaluation of how well the resulting UIs fit users’ own design choices. The approach to cultural adaptivity assumes that it is possible to approximate culture by calculating a weighted average of Hofstede’s country scores based on a user’s residence history and map this extended national culture to certain interface preferences. To evaluate this, we developed a prototype web application called MOCCA, which is able to compose its UI of various different elements, thereby adapting its look and feel to suit users’ extended national culture. In a comprehensive evaluation of MOCCA and its adaptation rules, we asked 105 participants (30 multicultural, 30 Thai, 21 Rwandan, and 24 Swiss) to choose their preferred elements for different aspects of a UI. For each participant, these choices were then compared to MOCCA’s automatically generated interface. The results demonstrated that our approach to cultural adaptivity is able to anticipate up to 61 percent of user preferences (compared to 33 percent that could have been achieved at random). MOCCA correctly predicted 61 percent of preferences of our multicultural users who had lived in at least two countries. In Thailand and Switzerland, MOCCA was able to produce similar results with 60.8 percent and 56.8 percent correct predictions, respectively. A fourth experiment in Rwanda showed that the adaptation rules did not adequately represent Rwandan preferences with no more than 24.4 percent correct predictions. However, the results in all three countries substantiated our assumption that people of the same national culture share similar preferences, suggesting that we can learn from the majority preferences within one country and override insufficient adaptation rules over time.

We therefore added a design iteration in which we implemented a simple learning mechanism, and evaluated MOCCA’s improvement for the three countries Rwanda,

Switzerland, and Thailand. Results produced an increase in the prediction accuracy for all countries to an average of 60.1 percent correct predictions.

With these results in mind, it can be assumed that in the future, culturally adaptive interfaces are technically feasible and could provide a competitive advantage over localized, or non-adapted, websites or software applications: Users will be less likely to turn to the competition if the software or website corresponds to their (aesthetic) preferences. We believe that our approach to cultural adaptivity, extended with the described learning capability to refine the adaptation rules, provides a major building block for improving the international access to websites and applications—a goal that is not only sensible from a business side, but has the potential to help overcoming the international digital divide.

## Acknowledgments

We would like to especially thank senior editor Shirley Gregor for many insightful comments that have tremendously improved the quality of this article. We also thank the associate editor, Samir Chatterjee, and the anonymous reviewers for their valuable feedback, David Eberle for helping to carry out the experiment in Thailand, Patrick Minder and Andreas Bossard for supporting the development of our prototype, and all of our participants. Katharina Reinecke was supported by the Hasler Foundation under grant no. 2322, and by the Swiss National Science Foundation under fellowship number PBZHP2-135922.

## References

Ackerman, S. 2002. “Mapping User Interface Design to Culture Dimensions,” in Proceedings of the International Workshop on Internationalization of Products and Systems, Austin, TX, pp. 89-100.

Aggarwal, C., and Yu, P. 2002. “An Automated System for Web Portal Personalization,” in Proceedings of the 28<sup>th</sup> International Conference on Very Large Data Bases, Hong Kong, August 20- 23, pp. 1031-1040.

Aroyo, L., Dolog, P., Houben, G.-J., Kravcik, M., Naeve, A., Nilsson, M., and Wild, F. 2006. “Interoperability in Personalized Adaptive Learning,” Educational Technology & Society (9:2), pp. 4-18.

Barber, W., and Badre, A. 1998. “Culturability: The Merging of Culture and Usability,” paper presented at the Conference on Human Factors & the Web, Basking Ridge, NJ.

Baumgartner, V.-J. 2003. “A Practical Set of Cultural Dimensions for Global User-Interface Analysis and Design,” unpublished Master of Science thesis, Fachhochschule Joanneum, Austria.

Blanchard, E. G., Lane, H. C., and Allard, D. (eds.). 2009. Proceedings of the 2<sup>nd</sup> International Workshop on Culturally-Aware Tutoring Systems, Brighton, United Kingdom, July 6-7.

Burgmann, I., Kitchen, P., and Williams, R. 2006. “Does Culture Matter on the Web?,” Marketing Intelligence & Planning (24:1), pp. 62-73.

Callahan, E. 2005. “Cultural Similarities and Differences in the Design of University Websites,” Journal of Computer-Mediated Communication (11:1), Article 12.

Cha, H., Oshlyansky, L., and Cairns, P. 2005. “Mobile Phone Preferences and Values: The U.K. vs. Korea,” in Proceedings of the International Workshop on Internationalization of Products and Systems, Amsterdam, July 7-9, pp. 29-41.

Chan, T., and Bergen, B. 2005. “Writing Direction Influences Spatial Cognition,” in Proceedings of the 27th Annual Conference of the Cognitive Science Society, Hillsdale, NJ: Lawrence Erlbaum Associates.

Chau, P., Cole, M., Massey, A., Montoya-Weiss, M., and O’Keefe, R. 2002. “Cultural Differences in the Online Behavior of Consumers,” Communications of the ACM (45:10), pp. 138-143.

Choi, B., Lee, I., Kim, J., and Jeon, Y. 2005. “A Qualitative Cross-National Study of Cultural Influences on Mobile Data Service Design,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Portland, OR, April 2-7, pp. 661-670.

Corbitt, B., Thanasankit, T., and Haynes, J. 2002. “A Model for Culturally-Informed Web Interfaces,” in Internet Management Issues: A Global Perspective. J. D. Haynes (ed.), Hershey, PA: Idea Group Publishing, pp. 1-26.

Cyr, D., Bonanni, C., Bowes, J., and Ilsever, J. 2005. “Beyond Trust: Website Design Preferences Across Cultures,” Journal of Global Information Management (13:4), pp. 25-54.

De Bra, P. 1999. “Design Issues in Adaptive Web-Site Development,” in Proceedings of the 2<sup>nd</sup> Workshop on Adaptive Systems and User Modeling on the WWW (http://wwwis.win.tue.nl/ asum99/debra/debra.html).

Dieterich, J., Malinowski, U., Kühme, T., and Schneider-Hufschmidt, M. 993. State of the Art in Adaptive User Interfaces,” in Adaptive User Interfaces: Principles and Practise, M. Schneider-Hufschmidt, T. Kühme, and U. Malinowski (eds.), Amsterdam: North Holland Elsevier, pp. 13-48.

Dolog, P., and Nejdl, W. 2003. “Personalisation in Elena: How to Cope with Personalisation in Distributed eLearning Networks,” in Proceedings of the International Conference on Worldwide Coherent Workforce, Satisfied Users: New Services for Scientific Information, Oldenburg, Germany, September 17-19, pp. 17-19.

Dormann, C., and Chisalita, C. 2002. “Cultural Values in Web Site Design,” in Proceedings of the 11<sup>th</sup> European Conference on Cognitive Ergonomics, Cantania, Italy, September 8-11.

Fernald, A., and Morikawa, H. 1993. “Common Themes and Cultural Variations in Japanese and American Mothers’ Speech to Infants,” Child Development (64:3), pp. 637-656.

Ford, D. P., Connelly, C. E., and Meister, D. B. 2003. “Information Systems Research and Hofstede’s Culture’s Consequences: An Uneasy and Incomplete Partnership,” IEEE Transactions on Engineering Management (50:1), pp. 8-25.

Ford, G., and Gelderblom, H. 2003. “The Effects of Culture on Performance Achieved Through the Use of Human–Computer Interaction,” in Proceedings of the Annual Research Conference of the

South African Institute of Computer Scientists and Information Technologists on Enablement Through Technology, pp. 218-230.

Gajos, K. Z., Wobbrock, J., and Weld, D. 2008. “Improving the Performance of Motor-Impaired Users with Automatically-Generated, Ability-Based Interfaces,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Florence, Italy, April 5-10, pp. 1257-1266.

Gould, E., Zakaria, N., and Yusof, S. 2000. “Applying Culture to Website Design: A Comparison of Malaysian and US Websites,” in Proceedings of IEEE Professional Communication Society International Professional Communication Conference and Proceedings of the 18<sup>th</sup> Annual ACM International Conference on Computer Documentation: Technology & Teamwork, pp. 161-171.

Gupta, A., and Ferguson, J. 1997. Anthropological Locations: Boundaries and Grounds of a Field Science, Berkeley, CA: University of California Press.

Hall, E. T., and Hall, M. R. 1990. Understanding Cultural Differences: Germans, French and Americans, London: Nicholas Brealey Publishing.

Hauser, J., Urban, G., Liberali, G., and Braun, M. 2009. “Website Morphing,” Marketing Science (28:2), pp. 202-223.

Hayward, F. M., and Siaya, L. M. 2001. “Public Experience, Attitudes, and Knowledge: A Report on Two National Surveys about International Education,” Technical Report, American Council on Education, Washington, DC.

Heimgärtner, R. 2005. “Towards Cross-Cultural Adaptive Human– Machine-Interaction in Automotive Navigation Systems,” in Proceedings of the International Workshop on Internationalization of Products and Systems, Amsterdam, The Netherlands, July 7-9, pp. 97-111.

Henze, N. 2005. “Personalization Services for e-Learning in the Semantic Web,” in Proceedings of the 2<sup>nd</sup> International Workshop on Adaptive Systems for Web-Based Education: Tools and Reusability, Amsterdam, The Netherlands, July 18, pp. 55-58.

Hermeking, M. 2005. “Culture and Internet Consumption: Contributions from Cross-Cultural Marketing and Advertising Research,” Journal of Computer-Mediated Communication (11:1), pp. 192-216.

Hevner, A. R., March, S. T., Park, J., and Ram, S. 2004. “Design Science in Information Systems Research,” MIS Quarterly (28:1), pp. 74-105.

Hodemacher, D., Jarman, F., and Mandle, T. 2005. “Kultur und Web-Design: Ein Empirischer Vergleich Zwischen Grossbritannien und Deutschland,” in Proceedings of Mensch und Computer: Kunst und Wissenschaft – Grenzü berschreitungen der interaktiven Art, Linz, Austria, September 4-7, pp. 93-101.

Hofstede, G. 1986. “Cultural Differences in Teaching and Learning,” International Journal of Intercultural Relations (10:3), pp. 301-320.

Hofstede, G. 1997. Cultures and Organizations: Software of the Mind, London: McGraw-Hill.

Hofstede, G. 2001. Culture’s Consequences: Comparing Values, Behaviours and Organisations Across Nations (2<sup>nd</sup> ed.), London: Sage Publications.

Hofstede, G. “Geert Hofstede” (http://www.geert-hofstede. com, accessed July 30, 2012).

Höök, K. 2000. “Steps to Take Before Intelligent User Interfaces Become Real,” Interacting With Computers (12:4), pp. 409-426.

Huber, G. P. 1983. “Cognitive Style as a Basis for MIS and DSS Designs: Much Ado About Nothing?,” Management Science (29:5), pp. 567-579.

Hurst, A., Hudson, S., and Mankoff, J. 2007. “Dynamic Detection of Vovice vs. Skilled Use Without a Task Model,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, San Jose, CA, April 28-May 3, pp. 271-280.

Hurst, A., Hudson, S., Mankoff, J., and Trewin, S. 2008. “Automatically Detecting Pointing Performance,” in Proceedings of the13th International Conference on Intelligent User Interfaces, Maspalomas, Gran Canaria, Spain, January 13-16, pp. 11-19.

International Organization for Standardization. 1997a. “Country Codes – ISO 3166” (http://www.iso.org/iso/home/standards/ country\_codes.htm).

International Organization for Standardization. 1997a. “Language Codes – ISO 639” (http://www.iso.org/iso/home/standards/ language\_codes.htm)

Jameson, A. 2008. “Adaptive Interfaces and Agents,” in The Human–Computer Interaction Handbook: Fundamentals, Evolving Technologies and Emerging Applications (2<sup>nd</sup> ed.), A. Sears and J. Jacko (eds.), Boca Raton, FL: CRC Press, pp. 433-458.

Jameson, A., and Schwarzkopf, E. 2002. “Pros and Cons of Controllability: An Empirical Study,” in Proceedings of the 2<sup>nd</sup> International Conference on Adaptive Hypermedia and Adaptive Web-Based Systems, Malaga, Spain, May 29-31, pp. 193-202.

Kamentz, E., and Womser-Hacker, C. 2003. “Defining Culture-Bound User Characteristics as a Starting-Point for the Design of Adaptive Learning Systems,” Journal of Universal Computer Science (9:7), pp. 596-607.

Kamentz, E., Womser-Hacker, C., Szwillus, G., and Ziegler, J. 2003. “Lerntheorie und Kultur: eine Voruntersuchung für die Entwicklung von Lernsystemen für internationale Zielgruppen,” in Proceedings of Mensch und Computer: Interaktion in Bewegung, Stuttgart, Germany, September 7-10, pp. 349-358.

Kappos, A., and Rivard, S. 2008. “A Three-Perspective Model of Culture, Information Systems, and Their Development and Use,” MIS Quarterly (32:3), pp. 601-634.

Karahanna, E., Evaristo, R., and Srite, M. 2005. “Levels of Culture and Individual Behavior: An Integrative Perspective,” Journal of Global Information Management (13:2), pp. 1-20.

Kay, J. 2001. “Learner Control,” User Modeling and User-Adapted Interaction (11:1), pp. 111-127.

Kersten, G. E., Kersten, M. A., and Rakowski, W. M. 2002. “Software and Culture: Beyond the Internationalization of the Interface,” Journal of Global Information Management (10:4), pp. 86-101.

Khashman, N., and Large, A. 2010. “Investigating the Design of Arabic Web Interfaces Using Hofstede’s Cultural Dimensions: A Case Study of Government Web Portals,” in Proceedings of the Annual Conference of the Canadian Association for Information Science, Montreal, Canada, June 2-4.

Kralisch, A. 2005. “The Impact of Culture and Language on the Use of the Internet: Empricial Analyses of Behaviour and Attitudes,” unpublished Ph.D. thesis, Humboldt University Berlin, Germany.

Kralisch, A., and Berendt, B. 2004. “Cultural Determinants of Search Behaviour on Websites,” in Proceedings of the 6<sup>th</sup> International Workshop on Internationalization of Products and Systems, Vancouver, BC, Canada, July 8-10.

Kralisch, A., Eisend, M., and Berendt, B. 2005. “The Impact of Culture on Website Navigation Behaviour,” in Proceeding of the 11<sup>th</sup> International Conference on Human–Computer Interaction, Las Vegas, NV, July 2005, pp. 22-27.

Leidner, D. E., and Kayworth, T. 2006. “Review: A Review of Culture in Information Systems Research: Toward a Theory of Information Technology Culture Conflict,” MIS Quarterly (30:2), pp. 357-399.

Liegle, J. O., and Janicki, T. N. 2006. “The Effect of Learning Atyles on the Navigation Needs of Web-Based Learners,” Computers in Human Behavior (22:5), pp. 885-898.

Lindgaard, G., Fernandes, G., Dudek, C., and Brown J. 2006. “Attention Web Designers: You Have 50 Milliseconds to Make a Good First Impression!,” Behaviour & Information Technology (25:2), pp. 115-126.

Maier, E. 2005. “Activity Theory as a Framework for Accommodating Cultural Factors in HCI Studies,” in Workshop Proceedings of Mensch und Computer, Linz, Austria, pp. 69-79.

Marcus, A. 2000. “International and Intercultural User Interfaces,” User Interfaces for All: Concepts, Methods, and Tools, C. Stephanidis (ed.), Hillsdale, NJ: Lawrence Erlbaum Associates, pp. 47-63.

Marcus, A., and Baumgartner, V.-J. 2004. “A Practical Set of Culture Dimensions for Global User-Interface Development,” in Proceedings of the 6<sup>th</sup> Asia Pacific Conference on Computer Human Interaction, Rotorua, New Zealand, June 29–July 2, pp. 252-261.

Marcus, A., and Gould, E. W. 2000. “Crosscurrents: Cultural Dimensions and Global Web User-Interface Design,” ACM Interactions (7:4), pp. 32-46.

Marcus, A., and Gould, E. W. 2001. “Cultural Dimensions and Global Web Design: What? So What? Now What?,” in Proceedings of the 6<sup>th</sup> Conference on Human Factors and the Web, Austin, TX, June 19.

McGuinness, D. L., and van Harmelen, F. 2004. “OWL Web Ontology Language Overview,” W3C Recommendation, February 10 (http://www.w3.org/TR/owl-features/).

McSweeney, B. 2002. “Hofstede’s Model of National Cultural Differences and Their Consequences,” Human Relations (55:1), pp. 89-118.

Microsoft. 2004. “Factors that Influence the Use of Computers,” (http://www.microsoft.com/enable/research/factors1.aspx, accessed February 10, 2010).

Myers, M., and Tan, F. 2002. “Beyond Models of National Culture in Information Systems Research,” Journal of Global Information Management (10:1), pp. 24-32.

Nantel, J., and Glaser, E. 2008. “The Impact of Language and Culture on Perceived Website Usability,” Journal of Engineering and Technology Management (25:1-2), pp. 112-122.

Nisbett, R. E. 2003. The Geography of Thought, New York: Free Press.

Nisbett, R. E., and Masuda, T. 2003. “Inaugural Articles: Culture and Point of View,” in Proceedings of the National Academy of Sciences (100:19), pp.11163-11170.

Oshlyansky, L. 2007. “Cultural Models in HCI: Hofstede, Affordance and Technology Acceptance,” unpublished Ph.D. thesis, Swansea University, Swansea, Wales.

Peffers, K., Tuunanen, T., Rothenberger, M. A., and Chatterjee, S. 2007. “A Design Science Research Methodology for Information Systems Research,” Journal of Management Information Systems (24:3), pp. 45-77.

Reinecke, K., and Bernstein, A. 2008. “Predicting User Interface Preferences of Culturally Ambiguous Users,” in Extended Abstracts of the Proceedings of the SIGCHI International Conference on Human Factors in Computing Systems, Florence, Italy, April 5-10, pp. 3261-3266.

Reinecke, K., and Bernstein, A. 2009. “Tell Me Where You’ve Lived, and I’ll Tell You What You Like: Adapting Interfaces to Cultural Preferences,” in Proceedings of the 17<sup>th</sup> International Conference on User Modeling, Adaptation, and Personalization, Trento, Italy, June 22-26, pp.185-196.

Reinecke, K., and Bernstein, A. 2011. “Improving Performance, Perceived Usability, and Aesthetics with Culturally Adaptive User Interfaces,” ACM Transactions on Computer-Human Interaction (18:2), Article 8.

Reinecke, K., Schenkel, S., and Bernstein, A. 2010. “Modeling a User’s Culture,” in Handbook of Research on Culturally-Aware Information Technology: Perspectives and Models, E. G. Blanchard and D. Allard (eds.), Hershey, PA: IGI Global, pp. 242-264.

Röse, K. 2005. “Aspekte der interkulturellen Systemgestaltung,” in Proceedings of Mensch und Computer: Kunst und Wissenschaft – Grenzü berschreitungen der interaktiven Art, Linz, Austria, September 4-7, pp. 80-90.

Russo, P., and Boor, S. 1993. “How Fluent Is Your Interface? Designing for International Users,” in Proceedings of the INTERACT ’93 and CHI ’93 Conference on Human Factors in Computing Systems, Amsterdam, The Netherlands, April 24-29, pp. 342-347.

Sahlins, M. 1993. “Goodbye to Tristes Tropes: Enthography in the Context of Modern World History,” The Journal of Modern History (65:1), pp. 1-25.

Sang-Hun, C. 2007. “South Koreans Connect Through Search Engine,” The New York Times, Technology Section, July 5 (http://www.nytimes.com/2007/07/05/technology/05online.html).

Schmid-Isler, S. 2000. “The Language of Digital Genres: A Semiotic Investigation of Style and Iconology on the World Wide Web,” in Proceedings of the 33<sup>rd</sup> Hawaii International Conference on System Sciences, Los Alamitos, CA: IEEE Computer Society Press.

Sheppard, C., and Scholtz, J. 1999. “The Effects of Cultural Markers on Web Site Use,” in Proceedings of the 5<sup>th</sup> Conference on Human Factors and the Web, Gaithersburg, Maryland, June 3.

Siala, H., O’Keefe, R., and Hone, K. 2004. “The Impact of Religious Affiliation on Trust in the Context of Electronic Commerce,” Interacting With Computers (16:1), pp. 7-27.

Snyder, C. 2003. Paper Prototyping: The Fast and Easy Way to Design and Refine User Interfaces, San Francisco: Morgan Kaufmann Publishers.

Stojanovic, L., and Thomas, S. 2006. “Fostering Self-Adaptive E-Government Service Improvement Using Semantic Technologies,” in The Semantic Web Meets eGovernment, 2006 AAAI

Spring Symposium Series, Stanford University, Stanford, CA, March 27-29 (http://imu.ntua.gr/sweg/papers/SS0606Stojanovic N1-fit.pdf).

Taylor, D. 1992. Global Software: Developing Applications for the International Market, New York: Springer.

The Economist. 2009. “Seeking Success,” February 26.

Trompenaars, F., and Hampden-Turner, C. 1997. Riding the Waves of Culture: Understanding Cultural Diversity in Business, London: Nicholas Brealey Publishing Ltd.

Urban, G. L., Hauser, J. R., Liberali, G., Braun, M., and Sultan, F. 2009. “Morph the Web to Build Empathy, Trust and Sales,” MIT Sloan Management Review (50:4), pp. 53-61.

Voehringer-Kuhnt, T. 2002. Kulturelle Einflüsse auf die Gestaltung von Mensch-Maschine Systemen, Munich: GRIN Verlag.

Yeo, A. 1996. “Cultural User Interfaces: A Silver Lining in Cultural Diversity,” SIGCHI Bulletin (28:3), pp. 4-7.

Zahed, F., van Pelt, W., and Song, J. 2001. “Crosscurrents: Cultural Dimensions and Global Web User-Interface Design,” IEEE Professional Communication (44:2), pp. 83-103.

Zhou, B., Hui, S. C., and Fong, A. C. M. 2005. “Web Usage Mining for Semantic Web Personalization” in Proceedings of the Workshop on Personalization on the Semantic Web, Edinburgh, Scotland, July 25-26, pp. 66-72.

## About the Authors

Katharina Reinecke received her Ph.D. in computer science from the University of Zurich, and she is now a postdoctoral fellow in the Intelligent and Interactive Systems group at Harvard School of Engineering and Applied Sciences. In her research, she combines the fields of human–computer interaction, cultural anthropology, and machine learning for an interdisciplinary approach to user interfaces that adapt their visual design and workflows to cultural preferences.

Abraham Bernstein is a full professor of Informatics at the University of Zurich, Switzerland. His research focuses on various aspects of the semantic web, crowd computing and collective intelligence, knowledge discovery and data mining, as well as human–computer interaction and CSCW. His work is based on both social science (organizational psychology/sociology/economics) and technical (computer science, artificial intelligence) foundations. He serves on the editorial board of ACM Transactions on Intelligent Interactive Systems, Journal on Web Semantics, International Journal on Semantic Web and Information Systems, Informatik Spektrum, and Journal of the Association for Information Systems.

# KNOWING WHAT A USER LIKES: A DESIGN SCIENCEAPPROACH TO INTERFACES THAT AUTOMATICALLYADAPT TO CULTURE

Katharina Reinecke Harvard School of Engineering and Applied Sciences of Business, 33 Oxford Street, Cambridge, MA 02138 U.S.A. {reinecke@seas.harvard.edu}

Abraham Bernstein Department of Informatics, University of Zurich, Binzmuehlestrasse 14, 8050 Zurich, SWITZERLAND {bernstein@ifi.uzh.ch}

## Appendix A

## The Adaptation Ontology

The adaptation ontology (shown in Figure A1) defines an element’s possible placement areas within the UI as well as its minimum and maximum size. Its main element is the class UserInterface, which defines general layout characteristics such as the colorfulness, color saturation, and alignment of the interface. It also specifies which UI element is currently used with the datatype property isUsed. The UI is further divided into the disjoint subclasses Header, Content, and Footer. The class Header generally describes the top part of a web page, which usually features a logo, a menu, and sometimes breadcrumbs showing the exact position within the hierarchy of web pages. The class Content can be divided into the disjoint subclasses Navigation, which contains several individuals such as a tree navigation, or a flat, nonhierarchical navigation, and WorkArea. The latter describes the part of the web page where the content is being presented, and this presentation can be adapted with different levels of information density, guidance, and accessibilities of functions. Additionally, the look and feel of the Navigation and WorkArea changes according to various characteristics inherited from the classes Content and UserInterface.

The ontology also determines the adaptation rules: To derive the adaptations (i.e., certain versions of specific interface elements) that are suitable for a person’s cultural background, all user interface elements (represented in the class UserInterface) are connected to the class CumoValue. The latter class stores the score for one or more of the cultural dimensions in five corresponding subproperties. The element with the score closest to the one stored in the user’s cultural user model instance is later selected by the application and taken for the composition of the personalized interface. Hence, the adaptation ontology also shows which element of the UI relates to which cultural dimension (subproperties of the class CumoValue).

![](/api/attachments/5DAX6PXW/fulltext/images/87b12ab57b678953f9f06e64c37dbb342cb79c123c1ff2aa7a78bf9ca0c66dc1.jpg)  
Figure A1. An Upper Layer of the Adaptation Ontology

## Appendix B

## Technical Implementation of MOCCA

In this appendix, we describe the technical implementation of our culturally adaptive prototype. MOCCA is implemented according to a model– view–controller architecture with the help of the open source framework Struts, which supports the interplay between the techniques shown in Figure B1. Struts also supported MOCCA’s internationalization, that is, the adaptation of all software strings to different languages according to a specified locale. So far, MOCCA offers the languages English, German, French, and Thai.

![](/api/attachments/5DAX6PXW/fulltext/images/79fa817a45336c20a532a0126030fa0b18f70ddfed98a422a22bddcc564171cc.jpg)

Figure B1. Overview of the Techniques and Scripting Languages Used in MOCCA

![](/api/attachments/5DAX6PXW/fulltext/images/f0c3357d53ce3860716dde472f3ca75be9259545d351f879366c7a239d84e96a.jpg)

In MOCCA, UI elements are developed as Java Server Pages (JSP), which can be loaded and compiled by an Apache Tomcat server at runtime. The use of AJAX (Asynchronous Javascript and XML) allows communication between the browser and server, without the need for a whole page to be reloaded. Design requirements are specified in cascading style sheet (CSS) files, the order of which is predefined in the adaptation ontology. According to this order, certain adaptation rules can overwrite layout and design settings as required for the specific cultural background. In order to communicate with the adaptation and cultural user model ontology, MOCCA makes use of the open source framework Jena, which allows it to access and query the ontologies with the help of the query language SPARQL and an OWL API. Additionally, MOCCA is connected to a MySQL database, which is used to store to-dos, projects, and categories with the help of Hibernate, a framework for object-relational mapping. The prototype was iteratively tested and refined in order to ensure the suitability of adaptations by creating fictitious users and comparing the resulting interfaces to the specifications in the adaptation rules. Fictitious users were randomly generated and fed into MOCCA’s user database according to their representation by the five-dimensional cultural vectors. At this stage, the prototype confirmed that it is technically possible to develop culturally adaptive systems with a sufficiently flexible interface.

## Appendix C

## Paper-Based Prototypes of MOCCA’s UI Elements

We used paper-based prototypes of different versions of MOCCA’s UI elements to conduct our experiments, some of which are shown in this appendix. Note that a participant’s choices determined the design of the three versions for the next tasks. If a participant chose a high information density in Task 1, for example, she would have been presented the following choices with an interface representing such a high information density as well, as shown here with the interface elements of Task 3. The complete set of paper prototypes can be requested from the authors.

![](/api/attachments/5DAX6PXW/fulltext/images/eadd4e8e02f05fba215f4e546d02872495b520de8144b9bdee266120d9b05db2.jpg)  
NAVIGATIONadd category

CATEGORY

PROJECT

![](/api/attachments/5DAX6PXW/fulltext/images/47c3d67c3c9e70a1ae1694f4b68bc28eced46b459975f5d58fda7f844f108c7a.jpg)  
(a) Tree menu (in combination with the to-dos in list view for a low PDI, or in combination with an iconrepresented to-do for a medium PDI)  
(b) Flat navigation (in combination with the to-dos in list view for a medium PDI, or in combination with an icon-represented to-do list for a high PDI)

## Figure C2. Task 2: Different Navigations Allowing for Different Levels of Flexibility (PDI = Power Distance Index. Note that this task builds on the participant’s choice in the first task.)

![](/api/attachments/5DAX6PXW/fulltext/images/1a4a458fd545037b07b2bceecb4d208cb4ea858a07d44590f71884e91bf0fafe.jpg)

![](/api/attachments/5DAX6PXW/fulltext/images/14ee7c356414cc82e87350eeb36eff2d9d3a0ecbcc45db0a8d41443673f7c6ab.jpg)  
(b) Functionalities accessible on mouse-over (medium PDI)

![](/api/attachments/5DAX6PXW/fulltext/images/129ca02d8166116f89f3a2069e1ab6cff58514d5d88676faec80928427d59f50.jpg)  
(c) Functionalities always accessible in a central place (high PDI)

![](/api/attachments/5DAX6PXW/fulltext/images/b64abad94506a9e7ee55cac5a1eaef95bfa83c8e9c213577d1fcccd9e9c26b05.jpg)

![](/api/attachments/5DAX6PXW/fulltext/images/ecb9679e624f6b8f184146ddfe01ed34c962d1735d49cb2721d089f4235f57c7.jpg)

## (a) Different regions of the website are only structured through alignment (low PDI)

![](/api/attachments/5DAX6PXW/fulltext/images/f3cbef021bcfd94e3d33d91a3bf8be8122f92adc56fc28b15f55402a34ce7808.jpg)

## (b) Different regions of the website are visually separated (medium PDI)

![](/api/attachments/5DAX6PXW/fulltext/images/8c30e96dbcc67d8412dbe2562166e2bf42afbe0beef9476314f91a2d3744d4fc.jpg)  
(c) Maximum structure with bordered elements emphasizing their affiliation to projects and categories (high PDI)

![](/api/attachments/5DAX6PXW/fulltext/images/8680fcae978b43a7972b342db1649b4d074050f503a28fc9ab715a2cbfcb0d5b.jpg)  
high: color-coordinated, tone-in-tone

![](/api/attachments/5DAX6PXW/fulltext/images/1b7469e195d3dfcb41ac7e1bf95106936810b5ef6b0f127d9e302a8de1dc0e6d.jpg)  
(a) On-site support with the help of short tool tips (low UAI)

![](/api/attachments/5DAX6PXW/fulltext/images/5f476cd0aa1f12b8f1e685b288c6ea3280796aa6d2290affb93943a3a8d4145c.jpg)

## (b) Question mark buttons that expand into help bubbles offer comprehensive on-site support medium (UAI)

![](/api/attachments/5DAX6PXW/fulltext/images/abaa332b1125b809b4bd8ff5db88b5f45fff678d298af882fc4f300eed81e058.jpg)  
(c) An adaptive help wizard offers the most comprehensive help (high UAI)

Figure C7. Task 8: Different Levels of Support 9UAI = Uncertainty Avoidance Index)

## Appendix D

## Design Iteration: Improvement of the Adaptation Rules Through Learning

While the evaluations with our culturally ambiguous, Thai, and Swiss participants all showed similar and reliable results with an average correct prediction accuracy of 59.5 percent, MOCCA merely predicted 24.4 percent of the preferences of our Rwandan participants correctly. The Rwandan participants made very similar choices (see Table 9), but these choices systematically differed from our adaptation rules.

This finding informed our decision to explore an improvement possibility of MOCCA’s adaptation rules. As a first exploration in this direction, we used the results from our second experiment to “teach” MOCCA how to learn from the choices of users. As described in the section on Artifact 5, MOCCA already enables users to modify the look and feel of its user interface in a built-in preference editor. We entered our participants’ choices in this preference editor, and let MOCCA calculate the majority preference per task and country. The system now overwrote the old adaptation rules with the majority preference, if this majority choice for a certain task was significant according to a Pearson’s chi-square test for categorical data (see also Table 9). To evaluate this “learning” mechanism, we calculated the choice-deviation scores with our Thai, Swiss, and Rwandan participants’ choices, and MOCCA’s three newly generated interfaces for each of these countries. For an overview of the UIs as they were initially predicted for the three countries, and the resulting adaptations after taking into account the majority preferences of participants from the same country, please refer to Figure D1.

The number of accurately predicted choices increased for all three countries (see Figure D2). In the case of Thailand, MOCCA’s recommendations resulted in 65.8 percent correct predictions (as opposed to 60.8 percent before). The number of accurate predictions per user ranged from three to eight tasks (mean = 5.27, sd = 1.08), thereby increasing from an average of 4.87 tasks that were correctly predicted by MOCCA’s initial adaptation rules (Figure D2). The improvement resulted from only one change in the adaptation rules.

In contrast, the adaptation rules for Rwanda were changed in four cases out of eight, resulting in 54.2 percent of accurately predicted preferences (an increase from 24.4 percent). Accurate predictions ranged between two and six per user (mean = 4.33, sd = 1.11). Thus, for the average user, we were able to predict more than 50 percent of the UI preferences correctly. Additionally, the frequency of a choice-deviation score of 1 decreased from 59.5 percent to 34.5 percent.

For the Swiss participants, MOCCA now achieved a prediction accuracy of 60.4 percent with accurate predictions per user ranging from 3 to 8 tasks per user (mean = 4.83, sd = 1.34). Altogether, MOCCA’s prediction accuracy increased from 47.3 percent to 61 percent across the three countries. The number of times MOCCA predicted with a deviation of 1 dropped from 41.4 percent to 30.5 percent, and for a deviation of 2 from 11.3 percent to 8.6 percent. This improvement demonstrates that it is feasible to anticipate a majority of UI preferences by learning from choices of users with similar origin.

MOCCA  
![](/api/attachments/5DAX6PXW/fulltext/images/125feb6200369f854085c72a32729010df16cd65ce192ad8fb3f9ab180ef38b0.jpg)  
(a) The initial UI for Thailand with a list-view of to-dos, a flat navigation, and many different, but light, colors

![](/api/attachments/5DAX6PXW/fulltext/images/d9fd348de011d8e883696ece6adbed816d7154e2ce44b2a662b47797da5682b0.jpg)  
(b) The UI for Thailand after taking into account the majority choices of participants

![](/api/attachments/5DAX6PXW/fulltext/images/3ac7360c5d7823b7c65a64888949314c502b807663d8484831abe590d5c8f49e.jpg)  
(c) The UI for Rwandans before learning, with a flat navigation, and a list-view of to-dos

![](/api/attachments/5DAX6PXW/fulltext/images/0df6e0da3a20ca5e54c933499f12e680e35c77a4659d5eb3933804b7d028901f.jpg)  
(d) After learning: In comparison to the initial adaptation rules, Rwandans preferred a higher information density, a hierarchical navigation, and a wizard for maximum support

![](/api/attachments/5DAX6PXW/fulltext/images/36c09208a67172f66e5f2e31a16c443453843fc1e12784bc56d91d023816c729.jpg)  
(e) The Swiss interface with a hierarchical navigation, a medium information density, and minimal color

![](/api/attachments/5DAX6PXW/fulltext/images/bd11fa2489eb38c9a54fe4770ecfffeb20ae4bb528ab6ba9ccfe2f9f428df034.jpg)  
(f) The final interface for Swiss users with a low information density and structure, and the preferred flat navigation  
Figure D1. MOCCA’s Uis for Thailand, Rwanda, and Switzerland Before and After Refinement of Adaptation Rules
