---
otero_id: 15840
otero_key: "3GCTDDG5"
title: "Umpires of Social Media: A Systems Science Analysis of Facebook’s Sociotechnical Content Moderation"
authors: "Anna Zaitsev"
year: "2025"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00918"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 26 Issue 2

Article 8

2025

# Umpires of Social Media: A Systems Science Analysis of Facebook’s Sociotechnical Content Moderation

Anna Zaitsev

, azaitsev@ut.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Umpires of Social Media: A Systems Science Analysis of Facebook’s Sociotechnical Content Moderation

Anna Zaitsev<sup>1</sup>

<sup>1</sup>Sykes College of Business, The University of Tampa, USA, azaitsev@ut.edu

## Abstract

Content moderation on social media platforms, such as Facebook, plays a critical role in curating user-generated content by mitigating harmful, misleading, or inappropriate materials. Despite significant investments in both human and algorithmic moderation systems, platforms continue to struggle with effectively managing the vast and complex flow of content, often facing criticism from various user groups for perceived inconsistencies and failures. This paper provides a systems theory analysis of Facebook’s content moderation system, with a particular focus on its sociotechnical nature, where human and non-human actors interact to moderate content. Using the COVID-19 pandemic as a revelatory case study, this research explores the disruptions to Facebook’s moderation processes caused by external shocks and identifies key conflicts within the system. Through the lens of systems science, the study reveals several points of tension, including conflicting goals between stakeholders, breakdowns in communication, and the challenges posed by both human and algorithmic moderators. By understanding these conflicts, this paper offers insights into why content moderation continues to be a significant challenge for social media platforms and proposes recommendations for improving moderation efforts. This study contributes to the broader discourse on content moderation by demonstrating the value of applying systems theory to analyze and address the complexities of these sociotechnical systems.

Keywords: Systems Theory, Facebook, Content Moderation, Sociotechnical Systems

Varun Grover was the accepting senior editor. This research article was submitted on September 5, 2022, and underwent four revisions.

## 1 Introduction

Social media platforms have revolutionized communication, allowing users to share information on an unprecedented scale. However, this ubiquity comes with significant challenges, particularly regarding the moderation of harmful content such as misinformation, copyrighted material, and violent or explicit imagery (Gillespie, 2018; Jiang et al., 2019). Platforms like Facebook have developed complex content moderation systems to manage these issues while balancing user engagement and free speech. Despite these efforts, content moderation remains a persistent challenge, with frequent controversies highlighting its limitations and the trade-offs involved (Gruzd et al., 2023).

The rise of fake news, propaganda, and inappropriate content has led to increasing scrutiny of content moderation practices (Khan et al., 2022; Moravec et al., 2020). Public dissatisfaction often stems from perceived inconsistencies in how moderation policies are applied, with accusations of biased enforcement or insufficient transparency (Register et al., 2024; Shaughnessy et al., 2024). For example, journalistic exposés have revealed internal disagreements within social media companies about moderation decisions, further fueling public distrust (Silverman & Mac, 2020a, 2020b). These challenges have been exacerbated by the sheer scale of platforms like Facebook, which must moderate content for billions of users in diverse sociopolitical contexts.

Content moderation is not merely a technical problem but a sociotechnical one involving the interplay of human and algorithmic decision-making. The complexity of this system means that even welldesigned processes can produce unpredictable or unsatisfactory outcomes, particularly when responding to external shocks such as the COVID-19 pandemic (Douek, 2022; Kreiss & McGregor, 2019). During the pandemic, Facebook’s content moderation system faced significant disruption due to the sudden shift to remote work, exposing vulnerabilities in both human and machine-driven moderation efforts (Isaac, 2020). Understanding why these systems struggle requires a holistic analysis considering both technical components (e.g., algorithms) and social factors (e.g., human moderators and organizational values).

Despite the growing body of literature on content moderation and misinformation, there remains a gap in understanding why moderation efforts frequently fall short of expectations, both from platforms’ and users’ perspectives (Morrow et al., 2022; Jiang et al., 2019. This paper seeks to address this gap by applying a systems theory approach to analyze the underlying conflicts and limitations within Facebook’s content moderation system during the COVID-19 pandemic. Specifically, the study aims to answer the following research question: Why do social media platforms struggle with content moderation, and what key attributes inhibit its effectiveness? To address these questions, this paper applies systems science, particularly systems theory, which offers valuable insights into the interconnected and dynamic nature of complex systems (Demetis & Lee, 2016). By examining Facebook’s content moderation as a sociotechnical system, this study highlights the various points of conflict between the system’s internal components and its external environment. Using the COVID-19 pandemic as a case study, the paper illustrates how environmental disruptions can exacerbate existing conflicts within the moderation system, ultimately impacting the effectiveness of content moderation efforts. This study contributes to the growing discourse on content moderation by providing a comprehensive systems theory analysis of Facebook’s moderation process. The findings explain why content moderation remains a persistent challenge and offers potential avenues for improving the system’s resilience and effectiveness in the face of future disruptions.

## 2 Theoretical Background

This section presents the requirements for systems science, which is the theoretical lens guiding this study’s analysis. It then introduces the concept of sociotechnical systems, which provides additional theoretical background to the analysis. The section concludes by detailing how the literature on content moderation was applied as data and reference.

## 2.1 Systems Science Requirements

Systems science is a major interdisciplinary research area that has yet to gain prominence in information systems research (Demetis & Lee, 2016). Originating in the attempt to explain every system under one general systems theory (von Bertalanffy, 1968), systems science investigates systems whose aggregate parts create emergent behavior or synergy. Systems theories are traceable to biology (von Bertalanffy, 1968), mathematics, and philosophy (Wiener, 1965), but its ideas have spread to engineering (Dekkers, 2015) and organizational and management studies (Senge, 1991; Dekkers, 2015), information systems (Checkland, 1989; Alter, 2006; Chatterjee et al., 2021), and even social media moderation (Douek, 2022). The proponents (Checkland, 1989; Checkland & Scholes, 1990) of the approach maintain that systems science and systems thinking (i.e., the process of thinking with the aid of systemic ideas) provide a useful explanatory device in such subject areas as engineering, natural sciences, and social sciences, where one must see the system as “an adaptive whole” rather than focusing on its individual parts.

Demetis and Lee (2016) extended the focus of observations from humans to machines—more specifically, to algorithms. They suggested guidelines for analyzing information systems through a systems thinking lens to expand the application of systems science to information systems (Demetis & Lee, 2016). Building on general systems theory (Skyttner, 2005) and Niklas Luhmann, who applied systems theory to sociology and philosophy (Luhmann, 1995, 2006; Luhmann et al., 2013), Demetis and Lee have proposed a set of general principles for theorizing about pieces of technology as systems (Demetis & Lee, 2017a, 2017b):

The whole is more than the sum of the parts: “The same component, when in different combinations with different components with which it interacts are theorized to manifest different properties [sic]” (Demetis & Lee, 2016, p. 121), and there may be nonunidirectional relationships between components. In other words, the systems “emerge” from their components.

Goal-seeking: “Systemic interaction must result in some goal or final state to be reached or some equilibrium point being approached” (Demetis & Lee, 2016, p. 121).

Transformation process (of inputs into outputs): The system transforms the inputs that enter the system into outputs to achieve the system’s goals.

Communication: The system can understand and employ communication, including non-human communication channels.

System/environment distinction: The environment and the system are structurally coupled. Without the environment, there is no system, and vice versa. The system replicates the distinction between itself and the environment by “reentry”: “the system re-enters into itself or copies itself into itself” (Luhmann et al., 2013, p. 56). Many other system features, such as autopoiesis, reentry, and communication, reinforce the distinction (Luhmann et al., 2013).

Self-reference and autopoiesis: Self-reference means that the system has processes that collect information about the system itself and apply it to change the system; the system can refer to itself and its components. Autopoietic systems (from Greek auto, “self,” and poiesis, “creation” or “production.”) are built on the elements and structure of the system’s previous generations (Dekkers, 2015). The system’s operations are reproduced within the system, reinforcing the difference between the system and the environment, i.e., the system-environment distinction (Luhmann, 1995; Luhmann et al., 2013). In a closed system, the autopoietic process triggers the organization to form an identity, i.e., the composition of the system components or parts and their relationships. Due to the systemenvironment distinction, one can distinguish the system from other systems within the organization (Luhmann et al., 2013).

Systems theory can elucidate the decision-making processes that social media organizations apply in their battle against prohibited content.

Furthermore, by applying systems thinking in the context of social media moderation decision-making, one expects to find system elements that do not fit neatly into the suggested requirements. Demetis and Lee (2016, 2017a) stated that they do not intend the list of requirements to be all-encompassing but, instead, a set of requirements for consideration and analysis (Demetis & Lee, 2016, 2017a). Since the analysis extends to a system comprising human and non-human decision makers and multiple organizations, one must examine whether the initial systems theory starting point should include other requirements to accommodate such systems. One possible requirement is the concept of sociotechnical systems, combining both social and technical (Sarker et al., 2019).

## 2.2 Sociotechnical Systems

The content moderation system, a combination of data, information systems, and humans, is sociotechnical. In sociotechnical systems, the social and technical parts of the system work together as co-producers of the desired outcome (Trist, 1981). Even if general systems theorists do not explicitly address systems as such, they often include sociotechnical systems, such as transnational or man-machine systems, that inevitably include non-human actors (Skyttner, 2005).

Demetis and Lee (2018) also presented non-human actors as part of their case examples, i.e., the impact of algorithms and human/non-human decision-making processes on the Dow Jones “Flash Crash of 2:45” (Demetis & Lee, 2017b, 2018), highlighting their role as independent and often subversive system elements. They argued that technology (i.e., the high-frequency trading algorithm) subverted and subdued human decision-making and the broader sociotechnical trading system (Demetis & Lee, 2018).

Similarly, the content moderation system, consisting of various modes of decision-making, might be subject to unexpected influence from non-human actors, namely the algorithms supporting moderation. Understanding the system requires understanding both the social and the technical aspects to yield outcomes that combine both humanistic and instrumental and generate synergy between the two (Sarker et al., 2019). Social media organizations would benefit from understanding whether non-human decision-making is subversive in the content moderation system, as in the stock crash case. The non-human agency of the algorithms might also generate some unexplored benefits for the system.

This study’s analysis of the content moderation system includes the sociotechnical nature of the system as an additional requirement for the analysis to uncover how non-human decision-making affects it. The paper returns to this concept and further elaborates in Section 4.1, where the study confirms that the system is sociotechnical after presenting the system components.

## 2.3 Literature on Content Moderation

Social media represents a popular research topic, and platform content moderation is subject to increasing academic attention (Gillespie, 2018; Jiang et al., 2019; Douek, 2022). Scholarly literature on content moderation can be divided into three categories: fake news moderation, algorithmic moderation, and regulatory and human moderation issues. Each category has informed this study in one of two ways: Some literature provided data on the activities and actors of the content moderation process, and other literature provided helpful background information or theoretical analysis and informed of the current state of the research.

First, studies of fake news moderation and analysis of the phenomenon’s impact and mitigation strategies are emerging in the literature (e.g., Moravec et al., 2020; Jang & Kim, 2018; Zwass, 2021). Research ranges from definitions (Khan et al., 2022) to emotional impact (Horner et al., 2023) and mitigation efforts (Kim & Dennis, 2019; Moravec et al., 2020; Gimpel et al., 2021; Morrow et al., 2022). This branch of literature highlighted the issues the content moderation system struggles with regarding this specific content branch. For this study, the fake news analysis provided information on the moderation process on behalf of the fact-checkers. Furthermore, the analysis of potential methods for intervention (e.g., Moravec et al., 2020) informed the analysis of system communication efforts.

Second, an expanding body of knowledge on algorithmic moderation covers both its technical aspects (Gorwa et al., 2020; He et al., 2022) and its sociotechnical aspects, including bias in data (Kroll et al., 2016; Binns et al., 2017), attitudes towards moderation in general (Riedl et al., 2022), and attitudes towards AI moderation specifically (Molina & Sundar, 2024). This literature explains social media’s challenges when applying algorithmic moderation to augment or replace human decision-making. For the moderation process model, the literature in this category provided information on the algorithms’ software developers and the issues one must consider when creating and modifying an algorithm, especially regarding the process of training data, which informed the autopoiesis analysis.

Third, content moderation research also addresses regulatory aspects (e.g., Langvardt, 2017), specific contentious issues, such as hate speech (e.g., Kalsnes & Ihlebæk, 2021), human moderators’ often unsavory labor conditions (Gray & Suri, 2019), discrepancies in advertisement moderation (Kreiss & McGregor, 2018; Ali et al., 2019), and alternative moderation strategies (Zeng & Kaye, 2021). The third category brings attention to the complex organizational structures, hierarchies, and exceptions that can hinder moderation efforts. The scholarly works from this category informed the study on the activities of the human moderators, moderation policies, and legislative and moral considerations linked to moderation, offering more insights into the human decision makers of the content moderation process and the formulation of the system guidelines.

The literature shows that despite different methods currently applied to facilitate moderation and improvements suggested by studies, the issue remains complex: Attitudes towards moderation vary, the humans and AI moderators have different weaknesses, and platforms do not engage in uniform approaches in their moderation. Hence, this study has chosen a more holistic approach to finding the root causes of the dysfunction. Table A2 in the Appendix summarizes the academic literature that this study applied as data, the academic works that describe the content moderation process, and the actors interacting with data throughout the process. Other scholarly works, not mentioned explicitly in Table A2 but referenced throughout the paper, have informed this research in different ways, providing background information, theoretical contributions, or research results supporting the analysis and conclusions of this study.

The following section describes the data analysis and research in secondary data sources that provide an understanding of the system. It describes how different actors and processes form the whole content moderation system, presenting the human and nonhuman actors and their relationships to the data that flow through the social media platform.

## 3 Data Analysis and the Content Moderation Process Modeling

This study asks why social media platforms struggle with content moderation and the key attributes that inhibit the effectiveness of extant moderation measures. To approach this question, the study conducted an explanatory case-study analysis of the content moderation actors and processes during the disruption of the content moderation systems due to social media companies’ COVID-19 pandemic mitigation efforts. Explanatory case studies are wellsuited to answering “why” questions (Yin, 2018). Furthermore, the case study format is appropriate for understanding contemporary events when one has no control over the subject (Yin, 2018).

This paper’s longitudinal case study was crafted by analyzing various secondary data sources, ranging from academic literature to documentary films. Due to the differences among the sources, the study applies several content analysis practices—for instance, a media analysis of investigative journalism—to understand the overall picture of the content moderation system (O’Leary, 2017). The application of additional sources, such as news articles or documentaries, news-media analysis (Hodgetts & Chamberlain, 2014), and best practices of film analysis (Knoblauch et al., 2014), created a descriptive process model of the system (Langley, 1999). Furthermore, the research included a scoping literature review to find academic writing that would consist of more details on the moderation process (Arksey & O’Malley, 2005).

Next, the paper details the data sources and the analytical process for both the system process modeling and the content moderation case study.

## 3.1 Data Collection and Analysis for System Process Modeling

Facebook’s actions during the COVID-19 pandemic offer a unique case study due to the significant disruption of office closures and drastically heightened user behavior. This became evident when the first newspapers published the first articles on content moderation breakdowns (i.e., Dwoskin & Tiku, 2020; Isaac, 2020; Koetsier, 2020). Something interesting happened within the social media company, and understanding the events required a better understanding of the system and its components.

Disentangling the system required gathering secondary data describing the content moderation process—namely, academic articles, news, and other documentation describing the system and the COVID-19 disruption (O’Leary, 2017). Although Facebook does not disclose all the details of its internal content moderation processes, Facebook’s transparency reports (e.g., Facebook Transparency, 2024; Facebook Newsroom, 2020), academic research (Kreiss & McGregor, 2018, 2019), and undercover investigative journalism (Paton et al., 2018; Newton, 2019a, 2019b; Silverman & Mac, 2020a) enable one to piece together a picture of the process. Despite lacking primary empirical data, examining and collating data revealing different aspects of the process and system enabled an understanding of the content moderation system to some degree. Via process mapping, the documents that formed the data set enabled the construction of an initial model of Facebook’s content moderation and fact-checking process (Langley, 1999). Table A1, Table A2, and Table A3 in the Appendix detail the main and supplemental data sources

The secondary data analysis led to sketching preliminary process models to capture data flows, stakeholders,<sup>1</sup> and the organizations involved (Langley, 1999). Figure 2 presents the final version of this process model with a brief process description. A more detailed description of the process can be found in the Appendix.

Analyzing the data describing the content moderation system enabled the creation of a model describing the actors and processes of system moderation. The model provided initial scaffolding for the systems theory requirements and supported forming the research question.

## 3.2 Data Collection and Analysis for the Content Moderation Case Study

Concurrently with the data sourcing and modeling of the content moderation system, the author collected and analyzed data on COVID-19 events alongside the requirements for systems science. The first round of secondary data analysis covered the COVID-19 outbreak in the early months of the pandemic in 2020. News sources, Facebook statements, newspaper articles, and scholarly work were the basis for investigating the disruption of the moderation process and Facebook’s actions (Appendix Table A3). First, the focus was on Facebook’s communiqué during the pandemic; then, on writing about content moderation during COVID-19 by the major newspapers with a national focus, wide distribution, <sup>2</sup> and technologyfocused publications.<sup>3</sup> However, in many cases, local news provided more detailed information on the events pertaining to the moderators (Isaac, 2020; Martin, 2022). Articles emerged from searches for the latest news on Facebook and content moderation on the Google News search tab. The research process sought relevant news articles from May 2020 to June 2022. An article database was created to provide information on the effects of the lockdowns on human moderators, fact-checkers, Facebook stakeholders, and moderation with AI, and it was used to piece together a rough timeline of major events. The process excluded duplicate news and included only one source per event. The goal was to find the originating news story for each event; a select list appears in Appendix Table A3.

Finally, an additional search for news articles in May 2023 supported understanding the situation at the end of the pandemic. The latest news was the source for updating the content moderation model and systems theory analysis.

Figure 1 summarizes the process of data analysis and modeling. The dotted lines signify an iterative approach and adjustments to the analysis. The highlevel timeline of the COVID-19 pandemic’s effects on content moderation appears in Figure 3.

![](/api/attachments/3GCTDDG5/fulltext/images/2b79d68111318c7cbb1df22d6b823fb31993440ebcf34ab8cdc8c2e778fdc999.jpg)  
Figure 1. The Research Process

Environment  
![](/api/attachments/3GCTDDG5/fulltext/images/192b0a40f6813f9bdc29f687e8927d09b6e02a03e2a791e2e12d01473473d51d.jpg)  
Figure 2. The Facebook Content Moderation System

![](/api/attachments/3GCTDDG5/fulltext/images/516cd03c66db6d3fe04dd3993fccbaa74d824c415f099a9c64152d1b9e2b123e.jpg)  
Figure 3. Timeline

## 4 Content Moderation Process

Facebook’s fight against content that its terms of service forbid has taken many forms. Facebook content moderation involves several actors. Figure 2 describes the flow of data. The larger light-gray box illustrates the social media platform and its distinction from the environment. The smaller gray box in the middle illustration portrays the content moderation system. The arrows show the direction of information flow, and the labels indicate the type of data the content moderationsystem actors transfer. Different data inputs and outputs appear on either side of the gray box, whereas the actors (humans and algorithms) appear within the gray box. This general process describes the high-level view of the flow of organic and paid content posted on Facebook. A more comprehensive description of the various actors appears in the Appendix.

1. The data input to Facebook is user-generated content in the form of posts on individual users’ personal “walls” or “timelines,” posts in Facebook groups, and the front-page newsfeed—i.e., an algorithmically selected feed of user-created content, user-shared media links (Facebook, 2024a), and advertisements (Facebook, 2024b).

2. Numerous algorithms screen the content uploaded to Facebook, searching for forbidden content (Terdiman, 2018; Facebook, 2024f). The algorithms preprocess data and make the frontline moderation decisions. The data can be sent for a human review (b) or published directly onto the platform as output (e)

3. Software developers have created moderation algorithms to fulfill the platform terms of service. The developers also provide algorithm training data (a) that should teach the algorithms to enforce the terms of service, which reflect guidelines for operations (c).

4. In difficult cases where the algorithm is not enough, the preprocessed data (d) is directed to the human decision makers: moderators, fact-checkers, or teams that handle CIB (Facebook, 2024f). Facebook employees screen advertisements and track and remove malicious human actors or networks propagating fake news, fake groups, and impersonators (Facebook, 2024a; Facebook Newsroom, 2020). Professional fact-checking organizations evaluate news articles and provide additional context for their claims (Stamos, 2018; Taylor & Hoffmann, 2019; Facebook, 2024c). The output of this process is a set of processed data (e).

5. The moderators can seek assistance from Facebook’s quality-assurance experts, escalating decisionmaking on the data (d) to senior moderators who interpret the rules set by Facebook’s stakeholders. The output of this process is also a set of processed data (e).

6. The platform’s terms of service are the basis for its moderation guidelines (c). These guidelines control how Facebook mitigates problematic content, reflecting company management’s perspectives and the organizational culture (Gillespie, 2018). System stakeholders who design the terms of service include any member of the organization who directly impacts the guidelines: legal teams, content moderation managers, CIB moderation, and moderation of organic content. Facebook’s Oversight Board also resides in the “stakeholder” category because its capability of overruling moderation decisions impacts the guidelines. Stakeholders reside, in general, outside of the content moderation system but can be conceptualized as a part of the decisionmaking body that affects the social media platform as a whole.

7. The output of the process (e) is the stream of processed data that will appear on the platform, either in its original form or with additional data appended to the post (e.g., limitations or warnings) (Facebook, 2024c).

## 4.1 Content Moderation System as a Sociotechnical System

When assessing the actors of the content moderation system, it quickly becomes clear that rather than consisting solely of human decision makers, the content moderation system is sociotechnical (Bostrom & Heinen, 1977; Trist, 1981; Sarker et al., 2019). The algorithms perform a variety of tasks, from image recognition to copyright infringement detection (Facebook, 2024e; 2024f), but despite attempts to further automate decisionmaking (Seetharaman et al., 2021; Facebook, 2024f), more complex decisions are left to human decision makers (Facebook, 2024f). The human decision makers range from the moderators and fact-checkers to the Csuite of the social media giant. As long as code, training data, or rule-setting involves humans, content moderation systems will not consist solely of algorithmic decision makers.

The sociotechnical nature of the content moderation system is not explicit to the regular user; they seldom encounter algorithmic decision-making, nor can they identify it as such. To the outsider, the content moderation system looks like a black box; the various decision makers are invisible and interchangeable. However, from within the system, the actors play specific and often complementary roles (Facebook, 2024f). Exploration of these roles and their interplay is essential to understanding the complexity of content moderation and why platforms struggle with moderation. The sociotechnical perspective might illuminate whether the system struggles due to human decision-making or if the non-human agency contributes to moderation dissatisfaction. Furthermore, the perspective is also helpful when studying if the nonhuman agency is subverting human decision-making, resulting in unexpected outcomes (e.g., Demetis & Lee, 2017b, 2018).

## 5 Content Moderation Case Study: Facebook Moderation During the COVID-19 Pandemic

Facebook content moderation is a complex process that consists of human and non-human decision-making elements and multiple organizations and stakeholders. Thus, it is an example of a system that we can analyze through the lens of systems science. This lens is especially useful because it allows us to holistically grasp the system as the sum of its components: organizations, people, and algorithms. This study argues that Facebook content monitoring fulfills Demetis and Lee’s (2016) systems science requirements, expanded by additional recruitment for the system to be a sociotechnical information system (Sarker et al., 2019).

This section explains the COVID-19 pandemic’s early effect on the content moderation system and how its progression changed the situation. Focusing on the content moderation system disruption from January 2020 until May 2023, the paper details the underlying system-environment distinction that drove the case (Yin, 2018; Demetis & Lee, 2016).

Next, the study analyzes the Facebook content moderation system in the context of the pandemic through the lens of systems theory requirements, including sociotechnicality. First, the section examines each requirement against the content moderation system in terms of how the system fulfills the requirement. Second, the section presents a diagnosis of the requirement and how it manifested in the system during the COVID-19 response. Then, the section examines conflicts within the system and makes recommendations for social media platforms.

## 5.1 The COVID-19 Content Moderation Case Background

The outbreak of the COVID-19 coronavirus upended the world and set the context for an interesting case study of Facebook’s content moderation system suddenly facing unexpected challenges. Governments worldwide tried to hinder the virus’s spread by implementing full or partial quarantines that included social-distancing mandates and nonessential-business closures.

Traditionally, human Facebook content moderators worked from centralized offices with strict security measures and no access to the content when off the premises (Newton, 2019a, 2019b; Biddle, 2020). However, in late March 2020,<sup>4</sup> Facebook sent most of its global moderation workforce home (Dwoskin & Tiku, 2020; Roberts, 2020). The company communicated that the only most crucial content (e.g., child safety, terrorism, and harmful COVID-19 content) would receive human attention; the company would rely more on automation for moderation, expecting more errors and longer review times (Jin, 2020).

Not long afterward, in April 2020, users began to notice some moderation mishaps: algorithms overzealously marked links to articles discussing the coronavirus as fake news (Matsakis & Martineau, 2020; Koetsier, 2020) and limited content on charitable efforts to provide homemade masks to healthcare workers (Isaac, 2020; Tiffany, 2020). However, the early errors and bugs were just a warm-up. A few weeks into the outbreak, the pandemic unleashed a viral avalanche of fake news, ranging from dangerously misleading treatment suggestions (Legon & Alsalman, 2020) to statesponsored misinformation (Wong et al., 2020).

Facebook addressed fact-checking issues by creating various initiatives and partnerships (Miles, 2020). In August 2020, Facebook announced that AI algorithms would perform a significant portion of content analysis (King & Gotimer, 2020). Furthermore, Facebook seems to have allowed content moderators to work remotely as early as March 2020, despite earlier user privacy considerations (Shead, 2020; Thomas, 2020).

Some attempts at fact-checking were controversial. For example, when fact-checkers flagged several articles discussing the virus’s origins as fake news (Teoh et al., 2020), media outlets and even medical journals decried censorship by fact-check (New York Post, 2020; Godlee & Abbasi, 2021). In hindsight, Facebook implemented some moderation guidelines in 2020 that might have been hastily decided and incorrect (Rosen, 2020). For example, in January 2021, the Oversight Board overruled the decision to restrict the discussion of drugs for potentially treating the disease (Oversight Board, 2021). Furthermore, in May 2021, Facebook decided to reverse the policy that earlier forbade the discussion of a lab leak as the virus’s potential origin.

In late 2020 and early 2021, Facebook’s attempts to return moderation to the office were met with resistance, leading to changes to remote work policies. Some employees worked remotely well into January 2022 and possibly longer (Emerson, 2022). It has also been revealed that Facebook collaborated with US officials, probably at the beginning of April 2021 and until an undisclosed date, on some of their content moderation decisions, sparking censorship concerns and lawsuits (Blaff, 2023; Soave, 2023; Tracy, 2023).

On May 5, 2023, the WHO declared the pandemic over (WHO, 2023). Some content moderators were called back into the office, but some continued to work remotely (Emerson, 2022; Martin, 2022).

## 5.2 Systems Theory Analysis of the Content Moderation Case

Analyzing the sudden disruption of the system’s normal operations through the systems theory lens can better explain why the pandemic so thoroughly disrupted the system. Facebook’s moderation system provides an excellent example of the utility of Demetis and Lee’s requirements, the additional system feature (i.e., sociotechnicality) that reveals the system’s weak points, and the pandemic-related adaptations that took place. The following analysis briefly discusses the systems science requirements and propositions that one can draw respectively from each requirement. Each proposition describes the system in the ideal state, i.e., how the system would operate with minimal disruptions. Then, diagnosing the pandemic disruption leads to identifying case revelations. The diagnosis informs conceptualizing a set of conflicts that explain why content moderation is not a straightforward endeavor. Each section offers recommendations for social media platforms to manage the conflict that each requirement creates.

## 5.2.1 The System Is Sociotechnical, and “The Whole Is More than the Sum of the Parts”

Systems theory requirement: The system whole requirement states that the system must emerge as the sum of its components and become something more, namely, a whole (Demetis & Lee, 2016). Conversely, the whole defines the nature of the parts that studying only the whole cannot explain (Skyttner, 2005). The study proposes that the sociotechnical system consists of human and non-human actors, and the balanced interplay of the parts elevates the system to more than the sum of the parts. This requirement means that when the system operates as it should, it is difficult for an outsider to observe where one part ends and the other begins. The data is moderated in a seamless fashion, without the user ever knowing which part of the sociotechnical system, human or non-human, performed the moderation. Similarly, the different subsystems within the content moderation system complement and reinforce each other, contributing to the whole rather than tearing the system apart. In other words, content goes in unfiltered and comes out moderated as expected, as defined by the terms of service.

However, the sudden environmental upheaval illuminated the different parts and their roles, as well as the sociotechnical nature of the system. The disruptions confirmed the system’s boundaries and internal structures. The moderation outcomes became unpredictable and flawed when different decision makers scrambled to reestablish flow and control. Assessing the disturbed system enables pinpointing the most crucial elements that elevate the system to more than the sum of its parts.

Diagnosis: Before the pandemic, an observer would not have experienced many interruptions in using the social media platform; the system was functioning in its ideal state, i.e., the whole was more than the sum of the parts. However, the pandemic response interfered with day-today moderation activities, and the system components— the human and machine moderators and organizational stakeholders—became more visible in the observable dysfunction. Cracks appeared in the usually seamless process, with more spam and the content assessment process slowing down (Tiffany, 2020; Scott & Kayali, 2020).

Moreover, suddenly diminishing the human actors’ role and tilting the decision-making balance further toward the machine elements interfered with the prior state of the system as a whole. Initially, reducing human decisionmaking resulted in numerous faulty decisions (Isaac, 2020; Lomas, 2020; Roberts, 2020). However, the changes put more pressure on the subsystem composed of algorithms and their developers, who were responsible for mitigating the lack of human oversight by facilitating extensive algorithmic content moderation (Sumbaly et al., 2020).

Conflict 1—Actor imbalance: Two types of actor imbalances contribute to the system’s dysfunction: an imbalance of the sociotechnical system and a human actor imbalance.

First, the suddenly diminishing role of human decisionmaking created conflict within the sociotechnical subsystems, consisting of human and AI actors presiding over different aspects of moderation. Demetis and Lee (2018) stated that when technological agency exceeds human agency, a role reversal occurs between humans and algorithms, and humans become the artifact. The algorithms no longer live in a human system; humans live in a technological system (Demetis & Lee, 2018).

The extensive application of AI tools in content moderation is an example of such a role reversal already (Rosen, 2020). However, the response to the pandemic deepened the role reversal when new algorithm deployment offset the lack of human moderation (Sumbaly et al., 2020). Thereafter, the algorithms became the primary decision makers, delegating secondary quality assurance roles to human decision makers.

Second, the imbalances between different human actors, i.e., moderators, fact-checkers, and other stakeholders, stemmed from decision-making imbalances and the lack of engagement and transparency between the parties (Silverman & Mac, 2020a; Pasternack, 2020; Horwitz, 2021b). Historically, the content moderation system disadvantaged third-party organizations (Newton, 2019b; Full Fact, 2019) and created disconnections within the system; the moderators and fact-checkers were not part of the decision-making regarding the rules and regulations; Facebook communicated the rules to third parties in a topdown fashion (Newton, 2019b).

The pandemic response exasperated the situation for both imbalanced. Instead of convergence, the system tilted toward an imbalance between humans and technology; rather than augmenting human decisionmaking, the algorithms dominated it (Demetis & Lee, 2018). Furthermore, the increased volume of misinformation put more pressure on the third-party fact-checking organizations that had to investigate a slew of novel claims regarding the pandemic but also maintain the preset rules of the platform (Sumbaly et al., 2020; Perry, 2020).

Prescription: More focus on the extant human decision-making capital can help alleviate the issues arising from the actor imbalance conflict. Leveraging the expertise of moderators and fact-checking organizations would generate better algorithm training data, more comprehensive internal policies, and more transparency between all parties. Fact-checking initiatives such as Facebook’s offer a good opportunity to add transparency (Goldshlager & Watson, 2020).

Conversely, algorithmic dominance may be beneficial if carefully tailored to the strengths of algorithms. Algorithms can cut costs and safeguard the human psyche: anecdotal evidence from content moderators describes deep mental scarring during their work from seeing instances of horrific human depravity (Newton, 2019a, 2019b; Glaser, 2018). However, fake news is particularly challenging for the algorithms to identify (Newton, 2019b); algorithms do not always catch the psyche-damaging child exploitation and violence, let alone gray areas that require human interpretation (Paton et al., 2018). Human oversight might remain a long-time necessity.

Finally, outsourcing parts of the decision-making through the Oversight Board could provide additional transparency and a way to address users’ moderationdecision grievances. Even though the Oversight Board is part of the content moderation system, its members are not employees of Facebook/Meta and thus outsiders to the organization, bringing in fresh perspectives.

## 5.2.2 Goal Seeking, Transformation Process (Inputs into Outputs), and Communication

Systems theory requirement: With or without disruptions, the system is goal-seeking, searching for a point of equilibrium or final state (Demetis & Lee, 2016). Linked to system goals is the transformation process. The transformation of inputs into outputs (Demetis & Lee, 2016) must occur if the system is striving to attain its goals (Demetis & Lee, 2016). In addition, the system engages in communication, the conduit of goals and transformation processes within the system and out to the environment. System communication consists of announcements (or utterances), information, and understanding (Demetis & Lee, 2016, based on Luhmann, 2006). Communication between the system and the environment consists of announcements that attempt to convey information describing the system’s decisionmaking, such as banners, warnings, flags, or (less explicitly) removed content. Understanding the information is a cognitive process of the users these announcements target. As Demetis and Lee envisioned, announcements, information (i.e., the aggregation of all the announcements), and eventual understanding emerge from the system. The accumulated announcements tell the environment what approach the content moderation system is taking toward the content, manifesting the internal system guidelines to the environment for users to interpret.

The study proposes that goal misalignment between subsystems or with the external environment can muddle communication and transformation processes. Conversely, disruption or confusion of the transformation or communication processes will hinder the system from reaching its goal. Understanding these interlinked forces can assist in interpreting the perception that the system is sending mixed messages internally and externally, potentially damaging the system’s reputation with the users.

Diagnosis: In general, the primary goal of the Facebook content moderation system is to monitor, identify, and potentially remove forbidden content, i.e., transform raw data into moderated data. Laws and content guidelines regulate the data transformation in an observable internal decision-making hierarchy. Additionally, subgoals link to different types of content. For example, the platform aims to ensure the fact-checking of fake news and the identification of its disseminators to permanently remove them (Stamos, 2018; Facebook Newsroom, 2020). The ideal goal would be a state in which each content item complies with the rules and guidelines. However, this is not the goal of the broader organization within which the content moderation system exists. The platform’s goal is to gain more advertisement revenue by maximizing the user base and the time spent on the platform. Former insiders have spoken of a strong drive for profit maximization and disregard for harm reduction (Horwitz, 2022b).

The content moderation system’s internal communication consists of announcements, information, and understanding. For example, new content moderation guidelines are communicated to all system participants. However, the sociotechnical nature of the system makes its internal understanding bimodal, consisting of both human understanding (the cognitive understanding of communication) and the algorithms’ “technological understanding” (Demetis & Lee, 2017b). Every human actor either conceives or receives the Facebook guidelines; from that point on, they are subject to a sensemaking process of discussion and deliberation among employees and individual interpretation (Newton, 2019b; Full Fact, 2019).

The disruptions of the system as a whole—the first requirement—did not amend the goal of ensuring content moderation according to the system’s internal rules. However, new supplementary goals and communication needs emerged—namely, detecting and flagging fake news or harmful content regarding the virus. The company launched several initiatives to provide information about the virus, e.g., additional outputs (Jin, 2020; Bond, 2020). For example, Facebook stated that its goals included informing users about the pandemic (Jin, 2020; Brady, 2020) and ensuring that the information did not violate new platform policies regarding information on masks, vaccines, or cures (Rosen, 2020; Facebook, 2024a; Jin, 2020).

Later, the content moderation system had two competing goals: quickly removing all potential misinformation and effectively distributing and communicating accurate information (Hegeman, 2020). The new goals created a shift in communication efforts toward new forms of announcements, information, and (hopefully) understanding. The direction of inputs and outputs was partially reversed: The content moderation system, which primarily operated based on input from the environment, now also provided inputs to the environment in the form of communication, i.e., information the platform generated (Jin, 2020; Hegeman, 2020). Once the platform became an active provider of information and not simply its conduit, this pandemic-related reversal made ensuring that information did not qualify as fake news more critical.

Conflict 2—Divergent goals: Due to legislative requirements for moderation, Facebook could not resolve the two conflicting goals—the platform’s goal to maximize engagement and the content moderation system’s goal to remove content with which users were engaging (Gillespie, 2018). Even if the system seeks a state of equilibrium, the constant pressure for more communication and new stakeholder demands in response to the environmental changes that clash with the system’s primary goals will cause friction.

Furthermore, the goals within the system and those of various human and non-human actors should seek alignment to avoid internal conflict. The moderators, fact-checkers, and algorithms should operate within the same parameters the guidelines set. Still, due to the sensemaking process applied to the guidelines, the outcomes can differ, resulting in false content flags or confusion among the moderators and fact-checkers (Full Fact, 2019; Horwitz & Seetharaman, 2020; Horwitz, 2021a, 2021b).

Conflict 3—Clashing communications: The most explicit changes in the goals of data transformation are the new ways the system produces announcements. Compared to implicit messaging that communicates the platform’s values through content moderation decisions, pandemic communication had a different, straightforward tone. Removing a piece of content implies impropriety, but a “fake news flag” explicitly states the platform’s opinion of the content. The change in system goals complicated decisions concerning which messages the platform considered reliable and which institutions, organizations, and articles it found acceptable to promote (Rosen, 2020).

Facebook’s various attempts at communicating with its users showcase the difficulty that fake news or organic posting of perceived misinformation poses. In contrast to the straightforward system communication applied in decisions on user-flagged content, copyright violations, or advertisement policies (Facebook Help, 2024, Facebook, 2024b, 2024e)—i.e., well-understood restrictions or decisions to remove or allow content— fake news or misleading postings constituted convoluted communication. Over time, announcements and utterances moderating pandemic information took many forms: context links for the items trending on the newsfeed feature (Anker et al., 2017), a banner indicating content disputed by the fact-checkers (Smith et al., 2017), warning banners directing users into “educational pop-ups” (Jin, 2020), and banners with links to sources that Facebook deemed authoritative (see Figure 4). Each announcement reminds the users that their experience on the platform reflects a position in the discourse, not just neutrally processing inputs. Notably, the format of the announcements (e.g., warning banners) is not necessarily effective in deterring users from reading fake news (Kim & Dennis, 2019).

Prescription: Social media companies should invest in research on the efficacy of announcements (Ross et al., 2018; Kim & Dennis, 2019). The platforms need to discern effective forms of communication from ineffective announcements that generate just noise (Ross et al., 2018; Pennycook et al., 2020). A robust, evidence-based balance between explicit and implicit outgoing communication would serve users and stakeholders.

Social media companies must also recognize that users see explicit communication as taking a position in the discourse. The content moderation system must communicate internally and externally the positions the platform is taking to avoid conflicting messaging.

## 5.2.3 System-Environment Distinction

Systems theory requirement: The systems science requirement states the structural coupling between the environment and the system, meaning that both exist in relation to each other (Demetis & Lee, 2016). The environment (everything outside the system) is the source from which data flows into the system, and the same environment is where the data resides after the system processes it. Understanding the distinction between the two and their linkage is important when drawing boundaries around the system to identify it. The distinction is also a useful analytical tool for analysis when the isolated system reacts to environmental changes.

We propose that for the system to maintain alignment and capabilities to absorb environmental changes, the system-environment gap cannot become too distinct. One must identify actors or subsystems especially vulnerable to discrepancies and take action to mitigate system isolation.

![](/api/attachments/3GCTDDG5/fulltext/images/9bb36fa4d1c3f1bd1409866e031a448cbd5ea52f8876a3eb92ca06834fbc0457.jpg)  
Figure 4. The Facebook Fake News Warning Banner

Diagnosis: Part of the difficulty of assessing content that would contradict Facebook’s newly minted and constantly evolving COVID-19 policies, such as fake news or medication and vaccine discussions on the platform (Jin, 2020; Rosen, 2020; Oversight Board, 2021), stems from the system-environment distinction. Fake news distributors can deliver their messages in sophisticated ways, making them difficult to track (Howard et al., 2019), and people can avoid algorithmic moderation by using such devices as creative spelling, reversing images or memes (Pulos, 2020; Sumbaly et al., 2020). The system’s human actors exist within the content moderation system but also in the complex environment and myriad other (social) systems. Human actors enter the system to conduct the operations that define it and distinguish it from the environment (Luhmann, 2006). However, when they finish their daily work, they exit the system and join the user base that fake news attempts to manipulate.

The systems communicating outside the moderation system counteract the content moderation system communication (i.e., the fake news detection guidelines). This cacophony of messaging might inhibit the moderators’ ability to distinguish false information from true. For example, moderators flag fake news partially based on their own biases (Common, 2020). Anecdotal evidence also describes an opposite phenomenon of the system’s effects on moderators. Due to constant exposure within the system, conspiratorial content convinced some moderators, compromising their moderation decisions (Newton, 2019b).

Furthermore, stakeholders are not bias-free either. They applied political reasoning when informing the moderators to ignore the general moderation rules with some controversial content (Horwitz & Seetharaman, 2020; Horwitz, 2021a). Human bias and disregarded guidelines can misalign different moderator parties, which are already scattered across multiple organizations: most of the human decision-making is outsourced to contractors, further complicating communication and alignment (Glaser, 2018; Gray & Suri, 2019; Newton, 2019b).

Evaluating sophisticated misinformation that straddles the line between truth and lies is even more difficult for an algorithm that is only as good as the set of rules built into it (Kroll et al., 2016). When the rules and guidelines the system applies try and fail to emulate the environment’s legislation and social norms, the algorithm will also fail.

Conflict 4—Disharmonious worlds: The distinction between the environment and the system generates a conflict without a resolution. Due to the nature of the distinction and the complexity of the environment (in this case, consisting of billions of people and hundreds of nation-states with their cultures, customs, and laws), perfect alignment of the environment and the system is unlikely, as well as undesirable, as such alignment would erase the system.

Prescription: The environment’s complexity keeps such globally operating social media giants as Facebook without comprehensive options for addressing these conflicts. However, mitigating conflict can occur in several ways, ranging from training human decision makers to developing more accurate algorithmic moderation to stronger participation of moderators and fact-checkers. More accurate machine decision-making might be soon attainable, given the novel content moderation advancements in large language model AIs (He et al., 2022; Hoes et al., 2023).

Increasing viewpoint diversity in human decisionmaking could also result in more balanced moderation. For example, X has created Community Notes <sup>5</sup> —a feature that allows selected users to fact-check posts (Pröllochs, 2022). The feature decentralized the factchecking process, increasing the diversity of moderators and requiring less moderation by the platform itself.

Finally, the system could align itself more closely with an external legislative framework (e.g., US law) in lieu of a complex set of internally generated rules, seemingly arbitrarily enforced. Other social media platforms, including so-called “alt-tech” and X (after Elon Musk purchased it in 2022) (Robertson, 2022), have attempted to embrace this approach.

## 5.2.4 Self-Reference and Autopoiesis

Systems theory requirement: Demetis and Lee (2016) make clear that Luhmann sees a self-referential system as “one that can collect information about its own functioning, which, in turn, can contribute toward a change in its functioning” (Geyer, 2002, p. 1022). System reentry and re-creation foster content moderation system autopoiesis, receiving inputs and producing outputs to perpetuate the process and reproduce itself (Demetis & Lee, 2016).

Self-referential cycles and an identity based on earlier system generations must be identified to fulfill this requirement. The study proposes that self-reference and autopoiesis can trigger self-reinforcing changes in the system, intentionally or unintentionally. Furthermore, the analysis of self-reference and autopoiesis can help explain some flaws in the system that persist and the amplification of misinterpretations over time. Understanding these forces can also help in distributing and solidifying new ideas or practices.

Diagnosis: Observing the content moderation system’s autopoiesis works best in one of its subsystems, namely, algorithmic decision-making. For example, Facebook algorithms attempt to predict images’ subject matter to identify nude images (Gillespie, 2018; Facebook Transparency, 2024). The system is fed new data about how nude photos look, improving the algorithms’ results (Witten et al., 2016). After the initialization, the algorithm will continue “living” and reproducing its activities autopoietically. However, it requires “energy” in the form of data, similar to a biological cell that can recreate itself but requires nutrients (Luhmann et al., 2013).

In the Facebook content moderation system, the stakeholders’ content moderation rules distinguish between the system and the environment. The environment does not care about these internal rules, but the system does (Luhmann, 2006). In reentry, the system reinforces the distinction between itself and the outside environment by recreating the rules. The inclusion of external factcheckers—a later addition to the content moderation system—represents a form of autopoiesis. The system recreates itself by absorbing this new feature and enforces the system-environment distinction by extending moderation rules to encompass fact-checking organizations.

Similarly, the system absorbs the new Oversight Board and the rulings that the board members mete out, recreating the system once more. The new rules added after the initial shock of the pandemic contributed to recreating the system and perpetuating new distinctions between the system and the environment. Certain discussion topics, imagery, or news articles are not forbidden in the environment, but within the system, they have become taboo (Gillespie, 2018; Oversight Board, 2022).

Conflict 5—Guidelines discord: Some of these changes resulted from internal, self-referential observations within the system. An example is the moderation decisions regarding some contentious topics regarded initially as fake news and banned on the platform, such as the virusorigin claims (Tracy, 2023). Initially, the Facebook stakeholders analyzed data flagged or removed and the resulting complaints, issuing moderation rules based on their analysis, environmental changes, and potential environmental pressure (Tracy, 2023). Promulgated through the system, these changes became part of the internal guidelines. Later amendments (Rosen, 2020) meant the system had to absorb its new state. The content moderation system must reflect both existing data flows and external environmental pressures. It can only respond to both by continuously reinventing itself, adding more examples of what content to remove, clarifying the rules around fake news, and generating new data sets to analyze for further improvement. It reenters itself to recreate itself (Luhmann, 1995). In other words, decision-making imbalances can affect self-reference and continuous autopoiesis. The pandemic forced the system to update its internal guidelines and adopt novel rules and regulations. The system recreated itself to account for these new rules and underwent a novel “reentry” that established the new distinction between the system and the environment (Luhmann, 2006). When the disruptive events in the environment recede, the system will retain the novel form it has taken unless the pandemic rules and regulations are intentionally dismantled.

Prescription: The system should recognize “mutations” and develop a strategy for deciding whether to remove them or nurture them as useful additions. Regular audits and revisions of the internal guidelines can help identify and reassess the guidelines. Another concern is that the mutations occur where bias (algorithmic or otherwise) can slip into the system (Kroll et al., 2016). To minimize bias, organizations should acknowledge this system feature and closely monitor the processes contributing to self-reference and autopoiesis.

## 5.2.5 Summary of Prescriptions

The analysis of each requirement reveals a conflict within the content moderation system or between the system and the environment. However, understanding the drivers of conflict is also an opportunity for social media organizations to better understand the content moderation system and attempt to resolve the conflicts. Each analysis of systems science requirements in prior sections suggests social media company mitigation actions; Table 1 summarizes them.

These prescriptions could benefit both the internal stakeholders who decide on the rules of the system and such parties as the Oversight Board that reevaluates existing moderation decisions. These prescriptions are not only Facebook’s; they apply to other similar social media systems. Such platforms as X and YouTube manifest features similar to Facebook’s system and are subject to the same systems theory requirements. Careful analysis, aided by systems thinking, can reveal similar weaknesses in other platforms and similar recommendations to consider.

## 6 Implications

## 6.1 Implication for Theory

The analysis of the content moderation system in the context of the systems theory requirements not only reveals how the content moderation system fulfills the requirements. It also highlights the mechanics of the internal and external forces that hinder the system’s effectiveness. Since systems thinking is a useful tool to create a synthesis of the whole rather than for analyzing individual parts, the conflicts that the requirements analysis reveals can appear as different aspects of the same phenomenon—namely, the system’s attempt to balance its mission, the environmental pressure, and stakeholders’ and users’ whims (Demetis & Lee, 2016). The balancing efforts do not end with Facebook; each social media company that engages in moderation must find an equilibrium between the types of content it allows (Gillespie, 2018).

Table 1. Recommendations for Social Media

<table><tr><td>Systems theory requirement</td><td>The proposal</td><td>Systemic weakness</td><td>Prescriptions</td></tr><tr><td>The system is sociotechnical; the whole is more than the sum of the parts</td><td>The sociotechnical system consists of human and non-human actors; the balanced interplay of the parts elevates the system to more than the sum of the parts.</td><td>1. Actors imbalance:Conflicts between subsystems, i.e., human and AI decision-making</td><td>Strengthen human decision-making capabilities and create avenues for third parties to communicate and provide feedback.Explore opportunities for algorithmic moderation but not yet at human moderation&#x27;s expense.Outsource difficult decisions to system insiders but platform outsiders, i.e., the Oversight Board.</td></tr><tr><td>Goal seeking, transformation process (of inputs into outputs), and communication</td><td>Goal misalignment between subsystems or with the external environment can muddle communication and transformation processes. Disruption or confusion of the transformation or communication processes will hinder the system from reaching its goal.</td><td>2. Divergent goals and 3. Clashing communications:Conflict between platform goals and moderation goals as well as conflict between modes of communication within the platform and to the users</td><td>Understand what explicit communication means, in lieu of prior platform neutrality.Ensure the communication is effective and maintains the user experience that platform users expect.</td></tr><tr><td>System-environment distinction</td><td>The system maintains alignment and capabilities to absorb the changes in the environment; the system-environment gap cannot become too distinct.</td><td>4. Disharmonious worlds:The conflict arising from the erosion of internal rules which have become inconsistent with the environment.</td><td>Carefully consider the cascading effect the change in system goals has on the overall system, i.e., moving from implicit to explicit communication, from showing user-generated to Facebook-generated content. Reactionary responses are likely to cause unintended consequences.</td></tr><tr><td>Self-reference and autopoiesis</td><td>Self-reference and autopoiesis can trigger self-reinforcing changes in the system, intentionally or unintentionally.</td><td>5. Guidelines discord:Conflict between the internal rules of different subsystems</td><td>Acknowledge that erroneous or reactionary policies will likely strengthen during the self-referential reentries and autopoiesis and plan for recurring audits and revisions.Require careful monitoring of the system self-reference for human and non-human moderators.</td></tr></table>

This paper identifies five main conflicts through systems theory analysis: (1) actor imbalance, (2) divergent goals (3) clashing communications, (4) disharmonious worlds, and (5) guidelines discord. These conflicts illuminate why social media platforms struggle with content moderation and why the public often derides their efforts (Gillespie, 2018; Harris, 2020).

The five areas of conflict appear in Figure 5. The direction of each arrow describes which system or subsystem has an influence on another. First, there are two internal conflicts within the content moderation system, a subsystem of the social media platform. There is a conflict between the actors, human and non-human decision makers (actor imbalance), as well as a conflict between internal guidelines, goals, and the actor interpretation (guidelines discord). Furthermore, the content moderation subsystem conflicts with both the social media platform and the environment. Since the content moderation system is only one of many subsystems within the social media platform, it has little influence on the environment, mainly in the form of one-directional communication targeting the users (clashing communications). Conversely, the environment has a large impact on the platform and the content moderation subsystem (disharmonious worlds). The platform goals and stakeholders influence the content moderation system (divergent goals), and the different elements of the content moderation system, i.e., the actors, goals, and guidelines of the content moderation system each influence each other.

![](/api/attachments/3GCTDDG5/fulltext/images/d2205f1c6a70ba0fd15f479ea18a7cdd3c2367fdeb33b62e73b8e950c9eda3fe.jpg)  
Figure 5. Conflicts in Social Media Content Moderation

Conflicts pertaining to actor imbalance, divergent goals, clashing communications, disharmonious worlds, and guidelines discord result in poor content moderation because the content moderation system cannot reflect the environment due to the isolation created by its internally set guidelines. Yet, when eventually updated either by edicts from the stakeholders or by internal entropy, the new guidelines are not communicated effectively to the outside environment, generating further confusion and discontent among the users.

The five conflicts identified through the system theory lens attest to the usefulness of systems theory requirements as a tool for further analysis, encouraging other authors in the field of information systems to consider how the tool can contribute to their work (Chatterjee et al., 2021). Including the sociotechnical nature of the content moderation system extends the understanding of information systems analysis using systems theory and grounds the study in the sociotechnical tradition of information systems research (Sarker et al., 2019).

Furthermore, this study illuminates the complexity of content moderation and highlights the role of algorithms, expanding the literature on content moderation (e.g., Gorwa et al., 2020; Horner et al., 2021) and contributing to the emergent body of knowledge on algorithms’ impact on social media (Binns et al., 2017; Kitchens et al., 2020; Molina & Sundar, 2022).

## 6.2 Implications for Practice

This study suggests that pandemic or no pandemic, these conflicts exist for all social media platforms. The case heightened the conflicts, enabling an examination of an extreme case with more significant disruptions to the system’s daily operations (Yin, 2018). First, the study proposes that goal misalignment will have a detrimental impact on communication and transformation processes and vice versa. The misalignment leads to divergent goals and clashing communications conflicts. Most social media platforms have had issues with consistent and opaque moderation decisions that the upper echelons of social media stakeholders have made and propagated through the system, muddling internal communications (Silverman & Mac, 2020a; Newton, 2020; Taibbi, 2022). Different rules for different types of content, such as advertiser materials or handpicked content creators, can create confusion and frustration among employees, factcheckers, and platform users (Silverman & Mac, 2020a; Newton, 2020; Taibbi, 2022). The users become unhappy with the moderation decision and begin campaigns or boycotts (Gillespie, 2018; Mills, 2021)—or seek alternatives that state moderation goals or their lack more clearly (Mahl et al., 2023).

Second, the system and environment gap should not become too wide. Otherwise, the system becomes an insular bubble that does not reflect the perspectives that persist in the environment, resulting in conflict (disharmonious worlds). Users persistently claim partisan bias in social media content moderation (Jiang et al., 2019), one of the reasons why touting fact-checking as the solution to fake news moderation is insufficient. The factchecks appended to user-generated content are products of the fact-checkers’ actual or perceived political partisanship (Lazer et al., 2018; Walter et al., 2020; Allen et al., 2022) because they operate with the same incomplete information as everyone else. The platforms are also slow to correct fact-checkers’ errors (e.g., Soave, 2021). In short, alternatives to professional fact-checking might be more acceptable. Algorithmic moderation is sometimes seen as a better, less biased alternative to factchecking organizations by people with a positive overall perception of AI (Molina & Sundar, 2024).

Furthermore, preliminary research indicates that the Community Notes model of X might be a more scalable alternative (Chuai et al., 2023). Using crowdsourcing as factchecking reduces the discrepancy between the system and the environment by replacing the actors (i.e., moderators, fact-checkers) who may appear to be living within the system bubble with actors who are part of the environment. Crowdsourcing is one example of how platforms could narrow the system and the environment gap.

Third, a balanced interplay among the different sociotechnical components should elevate the platforms to more than the sum of their parts. However, two forces disrupt the search for equilibrium: actor imbalance, due to the exceedingly technical nature of the sociotechnical system, and guideline discord, which self-reference and autopoiesis create, reinforcing the generation of a bubble effect and internal conflict. As the study proposes, self-reference and autopoiesis can trigger self-reinforcing system changes that become deeply embedded within subsystems, further widening the system-environment distinction.

The current trajectory for content moderation systems is to apply even more automation and resolve issues in their purview. Further automating the monitoring process—if not entirely, at least to the extent that the algorithms perform most of the work—would reduce the need for the augmented-human-decision-makers model (Zuckerberg, 2017; Seetharaman et al., 2021). Artificial distinctions between social and machine systems no longer apply; the role of algorithms as primary decision makers has reversed the sociotechnical system’s dynamic (Demetis & Lee, 2018). This process has been in the works for a long time, only recently taking major steps toward developing large language model AIs (Trautman et al., 2023). The pandemic was unlikely to speed up the development of such tools, but it has accelerated their adoption, according to sources within social media organizations (see Sumbaly et al., 2020; The YouTube Team, 2020). The system will eventually find a new form of equilibrium between the actors; the steps forward that all social media platforms take now happen amid the conflicts of actor imbalance and guidelines discord and require alleviating the current “growing pains.”

## 6.3 Limitations

All research has limitations, and this study is not exempt. This study’s main limitation is the lack of primary data confirming the moderation model derived from secondary sources. This paper generated the moderation model from a patchwork of different data sources and may have unintentionally overlooked aspects of the Facebook content moderation system. Journalists and their newspapers, just like Facebook’s stakeholders, might have been mistaken or biased, misinterpreting events or attributing causal relations to events where no causality existed. There is also the matter of the one-sidedness of the data describing the modification and reversal of moderation decisions. The picture remains incomplete since we do not have access to internal communication and must rely on Facebook’s transparency communication.

Conversely, by triangulating events and presenting multiple sources for many journalistic claims, one can remove at least some of the bias and truthfully map out the events and processes. Furthermore, the basis of systems theory analysis is a high-level view of the system. This approach does not require understanding the system’s minute details. The papers that inspired this study, such as Demetis and Lee’s (2016) analysis of the Flash Crash, included similar analyses.

Furthermore, a multitude of other reasons might have triggered some of the events that this paper attributes to the pandemic. The weeks and months in early 2020 were a tumultuous time across the globe. However, the paper attempts to mitigate this issue by focusing strictly on the content moderation system and the events that are clearly attributable to the system. Content moderation is a globally distributed affair, with contractors and factcheckers located in such various places as Ireland (Hern, 2020), the Philippines (Chen, 2014), and the United States (Newton, 2016b), among other locations. Only the pandemic was truly a global event; many other turbulent events were more local. Moreover, some developments (especially accelerated use of automatic moderation) were not limited to a single organization but were attributed to the pandemic by multiple organizations attempting similar resolution strategies for content moderation disruption.<sup>6</sup> Hence, the study considers the pandemic response the initial driver for the disruptions and the acceleration of non-human decision-making.

## 7 Conclusion

This paper began by asking why social media organizations struggle to moderate content and what attributes inhibit the effectiveness of moderation efforts. Using Facebook and the pandemic disruption of the content moderation system as an example, the analysis revealed that content moderation involves decision-making that is not centralized but forms a complex sociotechnical system in which human and non-human decision makers participate in the hunt for controversial content.

The main culprits are the disconnect between the system’s internal rules and actions that autopoiesis reinforces, the social media platform’s goals, and environmental changes. Resolution to these conflicts—even a temporary one—could help platforms provide a service to their users and mitigate pressure from various stakeholders.

The best way to leverage the sociotechnical nature of any platform’s content moderation system is to create a system where technical solutions augment the system’s human components rather than dominating the system (Demetis & Lee, 2018). At least for now, augmented human actors are capable of more nuanced decision-making but can significantly benefit from algorithmic assistance. However, the pandemic’s impact showed the new tension between the system’s social and technological components, causing a realignment in the moderation system, which resulted in errors but also accelerated AI tool adoption.

Furthermore, the efforts to control the spread of fake news and other questionable content related to the pandemic seem to have affected the organizations’ willingness to remove other content types. Before the pandemic, banning users with high-profile accounts appeared more sporadically. Since the pandemic, social media organizations have taken stronger stances on political, medical, and conspiracy content, attempting to align their response to environmental change and conflict (disharmonious worlds) (Rosen & Bickert, 2021; Soave, 2023). The acceleration of more robust positioning against political content was especially evident when many social media platforms, including Facebook, decided to ban then-President Trump’s accounts (Clegg, 2023). This acceleration speaks to platform mission creep and furthers the divergent goals and guidelines discord conflicts.

Controversies around moderation have also prompted calls for more social media platform regulation in the United States (Pecorin, 2020), the European Union (Turillazzi et al., 2023), and, somewhat surprisingly, from the platform owners themselves (Zuckerberg, 2019). However, it is likely that new technologies (e.g., deepfakes and AI-generated content) and global conflicts will make moderation and legislation more difficult in the future (Ruschemeier, 2023).

Yet the efficacy of legislation and regulation is ambiguous (Jang & Kim, 2018). The platforms’ regulatory measures have faced critiques for lacking transparency (Myers West, 2018) and inconsistent enforcement that is misaligned with local legislation (Common, 2020). These factors create user distrust of both the platforms and the content, stoking overmoderation concerns (Myers West, 2018). Furthermore, policy experts and political pundits assert that social media regulation raises many censorship and free speech concerns (Samples, 2019; Hasson, 2020; Taibbi, 2022). Stronger moderation might risk alienating users (Gillespie, 2018; Mills, 2021) and facilitating the growth of alternative platforms (Mahl et al., 2023). Hasty policy decisions and secretive tweaks of the algorithms attract bad publicity, hinder trust in the platforms, and create an appearance of social media companies’ detrimental effects on people and nations (Auxier, 2020). Nonetheless, nonregulation also raises concerns (Langvardt, 2017).

Some authors see fake news and misinformation as a part of ongoing online communication and are skeptical of any platform’s effort to curtail such content (Andersen & Søe, 2019). Furthermore, some claim that the harms inflicted by fake news might be overemphasized (Bail et al., 2020; Feldman, 2020; Budak et al., 2024). Media literacy training (Vraga & Tully, 2019) and countermessaging (i.e., truthful information that counters fake news) (Buchanan & Benson, 2019) might offer a better solution than excessive moderation. Rather than reactively fighting a losing battle, platforms should investigate more proactive measures or limit their involvement to moderating illegal content only. The suggestions in this study, derived from the systems thinking analysis, can provide additional guidelines when deciding on such measures.

## References

Ali, M., Sapiezynski, P., Bogen, M., Korolova, A., Mislove, A., & Rieke, A. (2019). Discrimination through optimization: How Facebook’s ad delivery can lead to biased outcomes. Proceedings of the ACM on Human-Computer Interaction.

Allen, J., Martel, C., & Rand, D. G. (2022). Birds of a feather don’t fact-check each other: Partisanship and the evaluation of news in Twitter’s Birdwatch crowdsourced fact-checking program. Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems

Alter, S. (2006). Work systems and its artifacts: Does the definition matter? Communications of the Association for Information Systems, 17(1), Article 14.

Andersen, J., & Søe, S. O. (2019). Communicative actions we live by: The problem with fact-checking, tagging or flagging fake news—the case of Facebook. European Journal of Communication, 35(2), 126-139.

Anker, A., Su, S., & Smith, J. (2017). New test to provide context about articles. Facebook Newsroom. https://about.fb.com/news/2017/10/news-feedfyi-new-test-to-provide-context-about-articles/

Arksey, H., & O’Malley, L. (2005). Scoping studies: towards a methodological framework. International Journal of Social Research Methodology, 8(1), 19-32.

Auxier, B. (2020). 64% of Americans say social media have a mostly negative effect on the way things are going in the U.S. today. Pew Research Center. https://www.pewresearch.org/shortreads/2020/10/15/64-of-americans-say-socialmedia-have-a-mostly-negative-effect-on-theway-things-are-going-in-the-u-s-today/

Bail, C. A., Guay, B., Maloney, E., Combs, A., Hillygus, D. S., Merhout, F., Freelon, D., & Volfovsky, A. (2020). Assessing the Russia Internet Research Agency’s impact on the political attitudes and behaviors of American Twitter users in late 2017. PNAS, 117(1), 243-250.

Blaff, A. (2023). Internal Facebook emails reveal White House pressured social-media platform to censor Covid “misinformation.” The National Review. https://www.nationalreview.com/news/internalfacebook-emails-reveal-white-house-pressuredsocial-media-platform-to-censor-covidmisinformation/

Beckett, L. (2019). Facebook to ban White nationalism and separatism content. The Guardian. https://www.theguardian.com/technology/2019/m

ar/27/facebook-white-nationalism-hate-speechban

Biddle, S. (2020). Facebook contractors must work in offices during coronavirus pandemic—while staff stays home. The Intercept., https://theintercept.com/2020/03/12/coronavirusfacebook-contractors/

Bilobrov, S. (2015). Extraction of video fingerprints and identification of multimedia using video fingerprinting (US Patent 8,934,545).

Binns, R., Veale, M., Van Kleek, M., & Shadbolt, N. (2017). Like trainer, like bot? Inheritance of bias in algorithmic content moderation. Proceedings of the International Conference on Social Informatics

Bond, S. (2020). Did you fall for a coronavirus hoax? Facebook will let you know. NPR. https://www.npr.org/2020/04/16/835579533/didyou-fall-for-a-coronavirus-hoax-facebook-willlet-you-know

Bostrom, R. P., & Heinen, J. S. (1977). MIS problems and failures: A socio-technical perspective. Part I: The causes. MIS Quarterly, 1(3). 17-32.

Brady, G. (2020). Press call transcript. Facebook. https://about.fb.com/wp-content/uploads/2020/03/ March-18-2020- Press-Call-Transcript.pdf

Buchanan, T., & Benson, V. (2019). Spreading disinformation on Facebook: Do trust in message source, risk propensity, or personality affect the organic reach of “fake news”? Social Media+ Society, 5(4). https://doi.org/10.1177/205630511 9888654

Budak, C., Nyhan, B., Rothschild, D. M., Thorson, E., & Watts, D. J. (2024). Misunderstanding the harms of online misinformation. Nature, 630(8015), 45- 53.

Chatterjee, S., Sarker, S., Lee, M. J., Xiao, X., & Elbanna, A. (2021). A possible conceptualization of the information systems (IS) artifact: A general systems theory perspective. Information Systems Journal, 31(4), 550-578.

Checkland, P. (1989). Soft systems methodology. Human Systems Management, 8(4), 273-289.

Checkland, P., & Scholes, J. (1990). Soft system methodology in action. John Wiley & Sons.

Chen, A. (2014). The laborers who keep dick pics and beheadings out of your Facebook feed. Wired. https://www.wired.com/2014/10/contentmoderation/

Clegg, N. (2023). Ending suspension of Trump’s accounts with new guardrails to deter repeat offenses. Meta

Newsroom. https://about.fb.com/news/2023/01/ trump-facebook-instagram-account-suspension/

Common, M. F. (2020). Fear the reaper: how content moderation rules are enforced on social media. International Review of Law, Computers & Technology, 34(2), 126-152.

Content Moderators (2020). Open letter from content moderators re: pandemic. Foxglove. https://www. foxglove.org.uk/news/open-letter-from-contentmoderators-re-pandemic

Crawford, K., & Gillespie, T. (2016). What is a flag for? Social media reporting tools and the vocabulary of complaint. New Media & Society, 18(3), 410-428.

Chuai, Y., Tian, H., Pröllochs, N., & Lenzini, G. (2023). The roll-out of community notes did not reduce engagement with misinformation on Twitter. arXiv. https://arxiv.org/abs/2307.07960

Dekkers, R. (2015). Applied systems theory. Springer.

Demetis, D., & Lee, A. (2016). Crafting theory to satisfy the requirements of systems science. Information and Organization, 26(4), 116-126.

Demetis, D., & Lee, A. (2017a). Taking the first step with systems theorizing in information systems: A response. Information and Organization, 27(3), 163-170.

Demetis, D., & Lee, A. (2017b). When humans using the IT artifact becomes IT using the human artifact. Proceedings of the 50th Hawaii International Conference on System Sciences.

Demetis, D., & Lee, A. (2018). When humans using the IT artifact becomes IT using the human artifact. Journal of the Association for Information Systems, 19(10), 929-952.

Douek, E. (2019). Facebook’s oversight board: Move fast with stable infrastructure and humility. North Carolina Journal of Law and Technology, 21(1), 1-78.

Douek, E. (2022). Content moderation as systems thinking. Harvard Law Review, 136(2), 526-606.

Dwoskin, E., & Tiku, N. (2020). Facebook sent home thousands of human moderators due to the coronavirus: Now the algorithms are in charge. Washington Post. https://www.washingtonpost. com/technology/2020/03/23/facebookmoderators-coronavirus/

Edelson, L., Lauinger, T., & McCoy, D. (2020). A security analysis of the Facebook ad library. Proceedings of the IEEE Symposium on Security and Privacy.

Emerson, S. (2022). Facebook moderators have been told they can work from home after employee protests. BuzzFeed News https://www.buzzfeednews.com/

article/sarahemerson/facebook-moderators-whowere-ordered-back-to-the-office-can

Facebook. (2024a). Facebook guidelines for safe, respectful behaviour. https://www.facebook.com/ business/help/2193703447560909?id=20806097 7200861

Facebook. (2024b). Facebook advertisement policies. https://www.facebook.com/policies/ads/

Facebook. (2024c). Fact-checking on Facebook: What publishers should know. https://www.facebook. com/help/publisher/182222309230722?ref=about .fb.com

Facebook. (2024d). Hate speech. https://transparency. facebook.com/community-standardsenforcement#hate-speech

Facebook. (2024e). Intellectual property. https://www. facebook.com/help/399224883474207/?helpref= hc\_fnav

Facebook. (2024f). How does Facebook use artificial intelligence to moderate content? https://www. facebook.com/help/1584908458516247

Facebook Help. (2024). Why am I seeing a warning before I can view a photo or video? https://www. facebook.com/help/814083248683500?helpref=u f\_permalink

Facebook Newsroom. (2020). August 2020 coordinated inauthentic behavior report. https://about.fb.com/ wp-content/uploads/2020/09/August-2020-CIB-Report.pdf

Facebook Transparency. (2024). Community standards enforcement report. https://transparency.facebook. com/community-standards-enforcement

Feldman, B. (2020). Did Russia’s Facebook ads actually swing the election? The New York Magazine. https://nymag.com/intelligencer/2017/10/didrussias-facebook-ads-actually-swing-theelection.html

Full Fact. (2019). Report on the Facebook Third Party Fact Checking Programme. https://fullfact.org/media/ uploads/tpfc-q1q2-2019.pdf

Geyer, F. (2002). The march of self-reference. Kybernetes. 31(7/8), 1021-1042

Gillespie, T. (2018). Custodians of the internet: Platforms, content moderation, and the hidden decisions that shape social media. Yale University Press.

Gimpel, H., Heger, S., Olenberger, C., & Utz, L. (2021). The effectiveness of social norms in fighting fake news on social media. Journal of Management Information Systems, 38(1), 196-221

Glaser, A. (2018). Want a terrible job? Facebook and Google may be hiring. Slate. https://slate.com/

technology/2018/01/facebookand-google-arebuilding-anarmy-of-content-moderatorsfor-2018.html

Gleicher, N. (2019). Taking down coordinated inauthentic behaviour in Indonesia. Facebook Newsroom. https://about.fb.com/news/2019/01/taking-downcoordinated-inauthentic-behavior-inindonesia/,11

Gruzd, A., Soares, F. B., & Mai, P. (2023). Trust and Safety on Social Media: Understanding the Impact of Anti-Social Behavior and Misinformation on Content Moderation and Platform Governance. Social Media + Society, 9(3). https://doi.org/ 10.1177/20563051231196878

Godlee, F., & Abbasi, K. (2021). Rapid response: Open letter from the BMJ to Mark Zuckerberg. The BMJ, 375, Article n2635.

Goldshlager, K., & Watson, O. (2020). Launching a \$1m grant program to support fact-checkers amid COVID-19. Facebook Journalism Project. https://www.facebook.com/journalismproject/cor onavirus-grants-fact-checking/

Gorwa, R., Binns, R., & Katzenbach, C. (2020). Algorithmic content moderation: Technical and political challenges in the automation of platform governance. Big Data & Society, 7(1). https://doi.org/10.1177/2053951719897945

Gray, M. L., & Suri, S. (2019). Ghost work: How to stop Silicon Valley from building a new global underclass. Eamon Dolan Books.

Grossman, S., Porras, M. F., & Ramali, K. (2020). Hello from the other side: An investigation into a musical pro-Muslim brotherhood disinformation operation. Stanford Internet Observatory. https://cyber.fsi.stanford.edu/publication/helloother-side-investigation-musical-pro-muslimbrotherhood-disinformation-operation

Harris, T. (2020). Commentary on The Social Dilemma. The Social Dilemma. https://thesocialdilemma. com/

Hasson, P. J. (2020). The manipulators: Facebook, Google, Twitter, and big tech’s war on conservatives. Regnery Publishing.

He, Q., Hong, Y. K., & Raghu, T. S. (2022). The effects of machine-powered content moderation: An empirical study on Reddit. Proceedings of the 55th Hawaii International Conference on System Sciences.

Hegeman, J. (2020). Providing people with additional context about content they share. Facebook Newsroom. https://about.fb.com/news/2020/06/ more-context-for-news-articles-and-othercontent/

Hern, A. (2020). Facebook moderators forced to work in Dublin office despite high-tier lockdown. The Guardian. https://www.theguardian.com/ technology/2020/oct/23/facebook-moderatorsforced-to-work-in-dublin-office-despite-hightier-lockdown

Hodgetts, D., & Chamberlain, K. (2014). Analysing news media. In U. Flick (Ed.), The SAGE handbook of qualitative data analysis (pp. 380-393). SAGE.

Hoes, E., Altay, S., & Bermeo, J. (2023). Using ChatGPT to fight misinformation: ChatGPT nails 72% of 12,000 verified claims. PsyArXiv. https://psy arxiv.com/qnjkf/download

Horner, C. G., Galletta, D., Crawford, J., & Shirsat, A. (2023). Emotions: The unexplored fuel of fake news on social media. In A. R. Dennis, D. F. Galletta, & J. Webster (Eds.), Fake news on the internet (pp. 147-174). Routledge.

Horwitz, J. (2021a). Facebook says its rules apply to all. Company documents reveal a secret elite that’s exempt. The Wall Street Journal. https://www.wsj. com/articles/facebook-files-xcheck-zuckerbergelite-rules-11631541353?mod=article\_inline

Horwitz, J. (2021b). The Facebook whistleblower, Frances Haugen, says she wants to fix the company, not harm it. The Wall Street Journal. https://www.wsj.com/articles/facebookwhistleblower-frances-haugen-says-she-wants-tofix-the-company-not-harm-it-11633304122

Horwitz, J., & Seetharaman, D. (2020). Facebook executives shut down efforts to make the site less divisive. The Wall Street Journal. https://www. wsj.com/articles/facebook-knows-it-encouragesdivision-top-executives-nixed-solutions-11590507499

Howard, P. N., Ganesh, B., Liotsiou, D., Kelly, J., & Francois, C. (2019). The IRA, social media and political polarization in the United States, 2012- 2018. University of Oxford.

Ingram, M. (2019). Facebook’s fact-checking program falls short. Columbia Journalism Review. https://www.cjr.org/the\_media\_today/facebookfact-checking.php

Isaac, M. (2020). Facebook hampers do-it-yourself mask efforts. Baltimore Sun. https://www.baltimoresun. com/coronavirus/sns-nyt-facebook-mask-effortscoronavirus-20200406-seo5tis7rrhtbnhfxewkbga eny-story.html

Jang, S. M., & Kim, J. K. (2018). Third person effects of fake news: Fake news regulation and media literacy interventions. Computers in Human Behavior 80, 295-302.

Jiang, S., Robertson, R. E., & Wilson, C. (2019). Bias misperceived: The role of partisanship and misinformation in YouTube comment moderation. Proceedings of the International AAAI Conference on Web and Social Media, 13(1), 278-289.

Jin, K.-X. (2020). Keeping people safe and informed about the coronavirus. Facebook. https://about.fb.com/ news/2020/03/coronavirus/#managingunprecedented-usage

Kalsnes, B., & Ihlebæk, K. A. (2021). Hiding hate speech: Political moderation on Facebook. Media, Culture & Society, 43(2), 326-342.

Kelion, L. (2017). Facebook artificial intelligence spots suicidal users. BBC News. https://www.bbc.com/ news/technology-39126027

Khan, A., Brohman, K., & Addas, S. (2022). The anatomy of “fake news”: Studying false messages as digital objects. Journal of Information Technology, 37(2), 122-143.

Kim, A., & Dennis, A. R. (2019). Says who? The effects of presentation format and source rating on fake news in social media. MIS Quarterly, 43(3), 1025- 1040.

King, J., & Gotimer, K. (2020). How we review content. Facebook Newsroom. https://about.fb.com/news/ 2020/08/how-we-review-content/

Kitchens, B., Johnson, S. L., & Gray, P. (2020). Understanding echo chambers and filter bubbles: The impact of social media on diversification and partisan shifts in news consumption. MIS Quarterly, 44(4), 1619-1649.

Knoblauch, H., Tuma, R., & Schnettler, B. (2014). Video analysis and videography. In U. Flick (Ed.), The SAGE handbook of qualitative data analysis (pp. 435-449). SAGE.

Koetsier, J. (2020). Facebook deleting coronavirus posts, leading to charges of censorship. Forbes. https://www.forbes.com/sites/johnkoetsier/2020/0 3/17/facebook-deleting-coronavirus-postsleading-to-charges-of-censorship/?sh=74b6 1d65962b

Kreiss, D., & McGregor, S. C. (2018). Technology firms shape political communication: The work of Microsoft, Facebook, Twitter, and Google with campaigns during the 2016 us presidential cycle. Political Communication, 35(2), 155-177.

Kreiss, D., & McGregor, S. C. (2019). The “arbiters of what our voters see”: Facebook and Google’s struggle with policy, process, and enforcement around political advertising. Political Communication, 36(4), 499-522.

Kroll, J. A., Barocas, S., Felten, E. W., Reidenberg, J. R., Robinson, D. G., & Yu, H. (2016). Accountable algorithms. University of Pennsylvania Law Review, 165, 633-705

Kwon, D. (2017). Can Facebook’s machine-learning algorithms accurately predict suicide? Scientific American. https://www.scientificamerican.com/ article/can-facebooks-machine-learningalgorithms-accurately-predict-suicide

Langley, A. (1999). Strategies for theorizing from process data. Academy of Management Review, 24(4), 691-710.

Langvardt, K. (2017). Regulating online content moderation. Georgetown Law Journal, 106, 1353- 1387.

Lazer, D. M., Baum, M. A., Benkler, Y., Berinsky, A. J., Greenhill, K. M., Menczer, F., Metzger, M. J., Nyhan, B., Pennycook, G., Rothschild, D., Schudson, M,. Sloman, S. A., Sunstein, C. A, Thorson, E. A., Watts, D. J, & Zittrain, J. L. (2018). The science of fake news. Science, 359(6380), 1094-1096.

Legon, A., & Alsalman, A. (2020). How Facebook can flatten the curve of the coronavirus infodemic. Avaaz Misinformation Hub. https://avaazimages. avaaz.org/facebook\_coronavirus\_misinformation. pdf

Li, Y., & Wang, J. (2019). Robust content fingerprinting algorithm based on invariant and hierarchical generative model. Digital Signal Processing, 85, 41-53.

Lomas, N. (2020). Lacking eyeballs Facebook ad review system fails to spot coronavirus harm. TechCrunch. https://techcrunch.com/2020/04/08/ lacking-eyeballs-facebooks-ad-review-systemfails-to-spot-coronavirus-harm/

Luhmann, N. (1995). Social systems. Stanford University Press.

Luhmann, N. (2006). System as difference. Organization, 13(1), 37-57.

Luhmann, N., Baecker, D., & Gilgen, P. (2013). Introduction to systems theory. Polity Cambridge.

Lyons, T. (2018). Hard questions: How is Facebook’s fact-checking program working? Facebook Business. https://about.fb.com/news/2018/06/ hard-questions-fact-checking/

Mahl, D., Zeng, J., & Schäfer, M. S. (2023). Conceptualizing platformed conspiracism: Analytical framework and empirical case study of BitChute and Gab. New Media & Society, 26(12), 6938-6957.

Martel, C., Pennycook, G., & Rand, D. G. (2020). Reliance on emotion promotes belief in fake news. Cognitive Research: Principles and Implications, 5(1), 1-20.

Martin, M. (2022). Meta says it left its Mountain View offices to build a “best-in-class remote work experience.” Current employees beg to differ. Mountain View Voice. https://www.mvvoice.com/news/2022/11/29/meta-says-it-left-itsmountain-view-offices-to-build-a-best-in-classremote-work-experience-current-employees-begto-differ/

Matsakis, L., & Martineau, P. (2020). Coronavirus disrupts social media’s first line of defense. Wired. https://www.wired.com/story/coronavirussocial-media-automated-content-moderation/

Meta. (2024). We are committed to protecting your voice and helping you connect and share safely. https://about.meta.com/actions/promoting-safetyand-expression

Meta Help. (2024). Rating options for fact-checkers. https://www.facebook.com/business/help/341102 040382165

Miles, C. (2020). Crowdtangle launches program to support investigative journalists at INN. Meta Journalism Project. https://www.facebook.com/ journalismproject/inn-crowdtangle-partnership

Mills, S. (2021). #DeleteFacebook: from popular protest to a new model of platform capitalism? New Political Economy, 26(5), 851-868.

Molina, M. D., & Sundar, S. S. (2022). When AI moderates online content: Effects of human collaboration and interactive transparency on user trust. Journal of Computer-Mediated Communication, 27(4), Article zmac010.

Moravec, P. L., Kim, A., & Dennis, A. R. (2020). Appealing to sense and sensibility: System 1 and System 2 interventions for fake news on social media. Information Systems Research, 31(3), 987- 1006.

Morrow, G., Swire‐Thompson, B., Polny, J. M., Kopec, M., & Wihbey, J. P. (2022). The emerging science of content labeling: Contextualizing social media content moderation. Journal of the Association for Information Science and Technology,73(10), 1365-1386.

Mosseri, A. (2016). News feed FYI: Addressing hoaxes and fake news. Facebook newsroom. https://about.fb.com/news/2016/12/news-feedfyi-addressing-hoaxes-and-fake-news/.

Myers West, S. (2018). Censored, suspended, shadowbanned: User interpretations of content

moderation on social media platforms. New Media & Society, 20(11), 4366-4383.

Newton, C. (2019a). Bodies in seats. The Verge. https://www.theverge.com/2019/6/19/18681845/f acebook-moderator-interviews-video-traumaptsd-cognizant-tampa.

Newton, C. (2019b). The trauma floor. The secret lives of Facebook moderators in America. The Verge. https://www.theverge.com/2019/2/25/18229714/c ognizant-facebook-content-moderator-interviewstrauma-working-conditions-arizona.

Newton, C. (2020). Mark in the middle. The Verge. https://www.theverge.com/21444203/facebookleaked-audio-zuckerberg-trump-pandemic-blm.

New York Post. (2020). Facebook’s “fact checkers” are the real fake news after censoring Post story. https://nypost.com/2020/04/17/facebook-factcheckers-foul-again-after-censoring-post-story/

O’Leary, Z. (2017). The essential guide to doing your research project. SAGE.

Oversight Board. (2022). Ensuring respect for free expression, through independent judgement. https://www.oversightboard.com/our-work

Oversight Board. (2021). Oversight Board overturns Facebook decision: Case 2020-006-FB-FBR. https://oversightboard.com/news/3251316354928 91-oversight-board-overturns-facebook-decision case-2020-006-fb-fbr/

Paluri, M., Mahajan, D., Girshickm, R., & Ramanathan, V. (2018). Advancing state-of-the-art image recognition with deep learning on hashtags. Facebook Engineering. https://engineering.fb. com/ml-applications/advancing-state-of-the-artimage-recognition-with-deep-learning-onhashtags/

Pasternack, A. (2020). Facebook is quietly pressuring its independent fact-checkers to change their rulings. Fast Company. https://www.fastcompany.com/ 90538655/facebook-is-quietly-pressuring-itsindependent-fact-checkers-to-change-theirrulings

Paton, T. (Director), Hawkings, C. (Assistant producer) Isfryn, C. (Producer), Kleeman, N. (Executive producer) & Pullen, T. (Development executive producer). (2018). Inside Facebook: Secrets of the social network [Video file].

Pecorin, A. (2020). Republicans attack Twitter, Facebook CEOs on moderating content. ABC News. https://abcnews.go.com/Politics/tech-ceos-facegrilling-moderating-content/story?id= 73876835.

Pennycook, G., Bear, A., Collins, E. T., & Rand, D. G. (2020). The implied truth effect: Attaching

warnings to a subset of fake news headlines increases perceived accuracy of headlines without warnings. Management Science, 66(11), 4944- 4957.

Perry, T. (2020). How Facebook is using AI to fight COVID-19 misinformation. The IEEE Spectrum. https://spectrum.ieee.org/how-facebook-is-usingai-to-fight-covid19-misinformation

Pröllochs, N. (2022). Community-based fact-checking on Twitter’s Birdwatch platform. Proceedings of the International AAAI Conference on Web and Social Media.

Pulos, R. (2020). Covid-19 crisis memes, rhetorical arena theory and multimodality. Journal of Science Communication, 19(7), Article A01.

Register, Y., Grasso, I., Weingarten, L. N., Fury, L., Chinea, C. E., Malloy, T. J., & Spiro, E. S. (2024). Beyond initial removal: Lasting impacts of discriminatory content moderation to marginalized creators on Instagram. Proceedings of the ACM Confererence on Human-Computer Interaction

Riedl, M. J., Whipple, K. N., & Wallace, R. (2021). Antecedents of support for social media content moderation and platform regulation: the role of presumed effects on self and others. Information, Communication & Society, 25(11), 1632-1649.

Roberts, S. T. (2020). The great A.I. beta test. Slate. https://slate.com/technology/2020/04/coronavirus -facebook-content-moderation-automated.html.

Robertson, A. (2020). Facebook fact-checking is becoming a political cudgel. The Verge. https://www.theverge.com/2020/3/3/21163388/fa cebook-fact-checking-trump-coronavirus-hoaxcomment-politico-daily-caller.

Robertson, A. (2022). What Elon Musk’s Twitter “free speech” promises miss. The Verge. https://www.theverge.com/2022/4/15/23025120/e lon-musk-twitter-free-speech-governmentcensorship

Rodriguez, S. (2020). Here are some instances where Facebook has been an arbiter of truth. CNBC. https://www.cnbc.com/2020/05/28/facebook-hasbeen-an-arbiter-of-truth-here-are-examples.html.

Rosen, G. (2020). An update on our work to keep people informed and limit misinformation about COVID-19. Facebook Newsroom. https://about.fb.com/ news/2020/04/covid-19-misinfo-update

Rosen, J., & Bickert, M. (2021). Our preparations ahead of inauguration day. Facebook Newsroom. https://about.fb.com/news/2019/10/update-onelection-integrity-efforts/

Rosen, J., Harbath, K., Gleicher, N., & Leathern, R. (2019). Helping to protect the 2020 us elections. Facebook About. https://about.fb.com/news/2019/ 10/update-on-election-integrity-efforts/

Ross, B., Jung, A., Heisel, J., & Stieglitz, S. (2018). Fake news on social media: The (in) effectiveness of warning messages. Proceedings of the 39th International Conference for Information Systems.

Rubin, V. L., Conroy, N., Chen, Y., & Cornwell, S. (2016). Fake news or truth? using satirical cues to detect potentially misleading news. Proceedings of the Second Workshop on Computational Approaches to Deception Detection.

Ruschemeier, H. (2023). AI as a challenge for legal regulation—the scope of application of the Artificial Intelligence Act proposal. Era Forum, 23(3), 361-376. Springer.

Samples, J. (2019). Why the government should not regulate content moderation of social media. Cato Institute. https://www.cato.org/policy-analysis/ why-government-should-not-regulate-contentmoderation-social-media

Sarker, S., Chatterjee, S., Xiao, X., & Elbanna, A. (2019). The sociotechnical axis of cohesion for the IS discipline: Its historical legacy and its continued relevance. MIS Quarterly, 43(3), 695-720.

Schroepfer, M. (2019). F8 2019, day 2 keynote and session videos. Facebook Engineering. https://engineering.fb.com/ai-research/f8-2019- day-2/

Seetharaman, D., Horwitz, J., & Scheck, J. (2021). Facebook says AI will clean up the platform. Its own engineers have doubts. The Wall Street Journal. https://www.wsj.com/articles/facebookai-enforce-rules-engineers-doubtful-artificialintelligence-11634338184?mod=article\_inline

Senge, P. (1991). The fifth discipline, the art and practice of the learning organization. Performance+ Instruction, 30(5), 37-37.

Scott M., & Kayali L. (2020) What happened when humans stopped managing social media content. Politico. https://www.politico.eu/article/facebookcontent-moderation-automation/

Shaughnessy, B., DuBosar, E., Hutchens, M. J., & Mann, I. (2024). An attack on free speech? Examining content moderation,(de-), and (re-) platforming on American right-wing alternative social media. New Media & Society. Advance online publication. https://doi.org/10.1177/1461444824 1228850

Shead, S. (2020). Facebook moderators say company has risked their lives by forcing them back to the office. CNBC. https://www.cnbc.com/2020/11/18/

facebook-content-moderators-urge-mark-zuckerbergto-let-them-work-remotely.html

Silverman, C., & Mac, R. (2020a). Facebook fired an employee who collected evidence of right-wing pages getting preferential treatment. BuzzFeed News. https://www.buzzfeednews.com/article/ craigsilverman/facebook-zuckerberg-what-iftrump-disputes-election-results

Silverman, C., & Mac, R. (2020b). Facebook’s preferential treatment of US conservatives puts its fact-checking program in danger. BuzzFeed News. https://about.fb.com/news/2019/10/updateon-election-integrity-efforts/

Skyttner, L. (2005). General systems theory: Problems, perspectives, practice. World scientific.

Smith, J., Jackson, G., & Raj, S. (2017). Designing against misinformation. Facebook Medium. https://medium.com/facebook-design/designingagainst-misinformation-e5846b3aa1e2

Smith, R. (2020). The UK election showed just how unreliable Facebook’s security system for elections really is. CNBC. https://www.cnbc. com/2020/11/18/facebook-content-moderatorsurge-mark-zuckerberg-to-let-them-workremotely.html

Soave, R. (2021). Facebook said my article was “false information.” Now the fact-checkers admit they were wrong. Reason. https://reason.com/2021/12/ 29/facebook-masks-false-information-sciencefeedback-wrong-covid/

Soave, R. (2023). Inside the Facebook files: Emails reveal the CDC’s role in silencing COVID-19 dissent. Reason. https://reason.com/2023/01/19/facebookfiles-emails-cdc-covid-vaccines-censorship/ 1/9

Stamos, A. (2018). Authenticity matters: The IRA has no place on Facebook. Facebook Newsroom. https://about.fb.com/news/2018/04/authenticitymatters/

Sumbaly R., Miller, M., Shah, H., Xie, Y., Culatana. S., et al. (2020, May 12) Using AI to detect COVID-19 misinformation and exploitative content. Meta: ML Applications Blog. https://ai.meta.com/blog using-ai-to-detect-covid-19-misinformation-andexploitative-content/

Taibbi, M. (2022). The Twitter files. Substack. https://twitterfiles.substack.com/p/1-thread-thetwitter-files

Taylor, E., & Hoffmann, S. (2019). Industry responses to computational propaganda and social media manipulation. Oxford Information Labs, The Computational Propaganda Project.

Teoh, F., Anderson, D., & Lipsitch, M. (2020). Viral New York Post article perpetuates the unfounded claim that the virus that causes COVID-19 is manmade. Health Feedback. https://healthfeedback.org/ evaluation/viral-new-york-post-articleperpetuates-the-unfounded-claim-that-the-covid-19-virus-is-manmade/

Terdiman, D. (2018). Here’s how Facebook uses AI to detect many kinds of bad content. Fast Company. https://www.fastcompany.com/40566786/hereshow-facebook-uses-ai-to-detect-many-kinds-ofbad-content

Thomas, Z. (2020). Facebook content moderators paid to work from home. BBC News. https://www.bbc. com/news/technology-51954968

Tiffany, K. (2020). No, the internet is not good again. The Atlantic. https://www.theatlantic.com/technology/ archive/2020/04/zoom-facebook-moderation-aicoronavirus-internet/610099/

Tracy, R. (2023). Facebook bowed to White House pressure, removed Covid posts. The Wall Street Journal. https://www.wsj.com/articles/facebookbowed-to-white-house-pressure-removed-covidposts-2df436b7

Trautman, L. J., Voss, W. G., & Shackelford, S J., (2023) How we learned to stop worrying and love AI: Analyzing the rapid evolution of generative pretrained transformer (GPT) and its impacts on law, business, and society. SSRN. http://dx.doi.org/ 10.2139/ssrn.4516154

Trist, E. (1981). The evolution of socio-technical systems. Ontario Ministry of Labour, Ontario Quality of Working Life Centre.

Turillazzi, A., Taddeo, M., Floridi, L., & Casolari, F. (2023). The digital services act: an analysis of its ethical, legal, and social implications. Law, Innovation and Technology, 15(1), 83-106.

von Bertalanffy, L. (1968). General system theory. G. Braziller.

Vosoughi, S., Roy, D., & Aral, S. (2018). The spread of true and false news online. Science, 359(6380), 1146-1151.

Vraga, E. K., & Tully, M. (2019). News literacy, social media behaviors, and skepticism toward information on social media. Information, Communication & Society, 24(2), 150-166.

Walter, N., Cohen, J., Holbert, R. L., & Morag, Y. (2020). Fact-checking: A meta-analysis of what works and for whom. Political Communication, 37(3), 350- 375

WHO. (2023). Statement on the fifteenth meeting of the IHR (2005) Emergency Committee on the

COVID-19 pandemic. https://www.who.int/news/ item/05-05-2023-statement-on-the-fifteenthmeeting-of-the-international-health-regulations-(2005)-emergency-committee-regarding-thecoronavirus-disease-(covid-19)-pandemic

Wiener, N. (1965). Cybernetics or control and communication in the animal and the machine, MIT Press.

Witten, I. H., Frank, E., Hall, M. A., & Pal, C. J. (2016). Data mining: Practical machine learning tools and techniques. Morgan Kaufmann.

Wong, E., Rosenberg, M., & Barnes, J. E. (2020). Chinese agents helped spread messages that sowed virus panic in U.S., officials say. The New York Times. https://www.nytimes.com/2020/04/22/us/politics/ coronavirus-china-disinformation.html

Wu, C.-J., Brooks, D., Chen, K., Chen, D., & Chodhury, S. (2019). Machine learning at Facebook understanding inference at the edge. Proceedings of the IEEE international symposium on high performance computer architecture.

Yin, R. K. (2018). Case study research: Design and methods. SAGE.

The YouTube Team. (2020, March 16). Protecting our extended workforce and the community. YouTube Official Blog. https://blog.youtube/news-andevents/protecting-our-extended-workforce-and/

Zeng, J., & Kaye, D. B. V. (2022). From content moderation to visibility moderation: A case study of platform governance on TikTok. Policy & Internet, 14(1), 79-95.

Zuckerberg, M. (2017). Building global community. Facebook. https://www.facebook.com/notes/ 3707971095882612/

Zuckerberg, M. (2019). The internet needs new rules. Let’s start in these four areas. The Washington Post. https://www.washingtonpost.com/opinions/markzuckerberg-the-internet-needs-new-rules-lets-startin-these-four-areas/2019/03/29/9e6f0504-521a-11e9-a3f7-78b7525a8d5f\_story.html

Zwass, V. (2021). Editorial introduction. Journal of Management Information Systems, 38(4), 889- 892.

## Appendix A: Main and Supplemental Data Sources

Four main sources were applied to form the armature of the content moderation system model. First, Tarleton Gillespie’s (2018) book, Custodians of the Internet: Platforms, Content Moderation, and the Hidden Decisions that Shape Social Media, clarified the overall content moderation landscape but lacked Facebook specificity. Absent a comprehensive academic account of the moderation system process, the study moved away from conducting a traditional academic literature review and toward three other sources besides Gillespie (2018). They provided an initial scaffolding for the process: an article by Casey Newton (2019a), “The Trauma Floor: The Secret Lives of Facebook Moderators in America,” a documentary film titled Inside Facebook: Secrets of Social Networking (2018), and a report by Full Fact (2019), “Report on the Facebook Third Party Fact Checking Programme.” These sources formed the backbone for mapping the content moderation process.

However, the four primary documents alone were insufficient, leaving several gaps in the process description—for example, only Gillespie (2018) addressed the role of algorithms. Several news outlet sources were utilized to fill in the gaps. High-quality articles discussing content moderation, available via the most common search engines, enabled the incorporation of additional information on the process into the study (e.g., Glaser, 2018; Terdiman, 2018).

Moreover, Facebook’s transparency efforts have produced blog posts, policy statements, and other communications that provided additional information on relevant processes, especially the application of algorithms, the moderation of advertisements, and efforts against coordinated inauthentic behavior (CIB) (e.g., Facebook Newsroom, 2020; Facebook Transparency, 2024; Lyons, 2018; Gleicher, 2019; Teoh et al., 2020; Perry, 2020). Highlighting and thematically coding paragraphs that discuss fact-checking, algorithms, or other aspects of the work process led to these documents yielding more details. Then, new findings were compared to data from the first four primary sources to close the gaps in understanding the process.

Furthermore, a better understanding of the process and the potential stakeholders supported a literature review of academic work on the subject that focused on finding process descriptions and studies on stakeholder involvement rather than a traditional review. For example, scholarly papers that discussed advertisement moderation were beneficial (Kreiss & McGregor, 2018; Ali et al., 2019).

Table A1 summarizes the document types and describes what information was gained from them. The top four entries in Table A1 have been applied as the main sources for our investigation of the Facebook content moderation process. The additional documents listed below are the main sources, and additional materials were studied to fill in the gaps in the process.

Table A2 summarizes the academic literature applied in this study to inform the process specifically. These articles listed in this appendix directly discuss the content moderation process; other academic literature cited in the study has informed the research in different ways. Table A3 summarizes the newspaper articles and other sources used to inform the content moderation case during the COVID-19 pandemic.

Table A1. Summary: Data Sources for Content Moderation System Model

<table><tr><td>Document type</td><td>Description</td><td>Sources</td></tr><tr><td>Book: Custodians of the Internet: Platforms, Content Moderation, and the Hidden Decisions That Shape Social Media</td><td>Content moderation process explained• Extensive chronology of the history of content moderation on major social media platformsComparison of content-policy guidelines</td><td>Gillespie (2018)</td></tr><tr><td>Documentary film: Inside Facebook Inside Facebook: Secrets of Social Networking</td><td>Details of the moderation process from the content moderator perspective</td><td>Paton et al. (2018) (see Appendix Table A3)</td></tr><tr><td>Article: “The Trauma Floor: The Secret Lives of Facebook Moderators in America”</td><td>Details on the organizational structures and content moderation process</td><td>Newton (2019b) (see Appendix Table C1)</td></tr><tr><td>Report: “Report on the Facebook Third Party Fact Checking Programme”</td><td>Details on the fact-checking process from the perspective of an independent third-party fact-checking organizationComprehensive and detailed view of the organization's relationship with other fact-checkers and FacebookProvides insights into the decision-making process of the fact-checkers who determine whether news on Facebook is fake, true or something in between</td><td>Full Fact (2019)</td></tr><tr><td>Additional documents</td><td>Description</td><td>Sources</td></tr><tr><td>Documents on human moderation</td><td>Additional details on the organizational structures within content moderation organizations and Facebook</td><td>Biddle (2020); Chen (2014); Content Moderators (2020); Crawford and Gillespie (2016); Gillespie (2018); Glaser (2018); Gray and Suri (2019); Facebook Transparency (2024); Facebook (2024d); Hern (2020); Newton (2019a); Shead (2020); Thomas (2020)</td></tr><tr><td>Documents on algorithmic moderation</td><td>Details on the efforts for algorithmic content moderation</td><td>Bilobrov (2015); Gillespie (2018); Gorwa et al. (2020); Facebook (2024a); Facebook Transparency (2024); Facebook (2024f); Perry (2020); Li and Wang (2019); Kelion (2017); King and Gotimer (2020); Kroll et al. (2016); Kwon (2017); Paluri et al. (2018); Schroepfer (2019); Seetharaman et al. (2021); Sumbaly et al. (2020); Terdiman (2018); Wu et al. (2019); The YouTube Team (2020); Zuckerberg (2017)</td></tr><tr><td>Documents on fact-checking</td><td>Details on the fact-checking operations by the third-party fact-checkers</td><td>Anker et al. (2017); Facebook (2024c); Goldshlager and Watson (2020); Ingram (2019); Lyons (2018); Miles (2020); Mosseri (2016); New York Post (2020); Pasternack (2020); Robertson (2020); Rosen et al. (2019); Smith et al. (2017); Soave (2021); Taylor and Hoffmann (2019); Teoh et al. (2020);</td></tr><tr><td>Documents on CIB moderation</td><td>Facebook press reports on the moderation of coordinated inauthentic behavior</td><td>Facebook Transparency (2024); Gleicher (2019); Howard et al. (2019); Stamos (2018)</td></tr><tr><td>Documents on advertisement moderation</td><td>Documents describing aspects of advertisement moderation.</td><td>Ali et al. (2019); Edelson et al. (2020); Facebook (2024b); Silverman and Mac (2020a); Silverman and Mac (2020b); Smith (2020)</td></tr><tr><td>Documents detailing Facebook stakeholders</td><td>Documents describing the actions of Facebook stakeholders</td><td>Beckett (2019); Blaff (2023); Brady (2020); Clegg (2023); Douek (2019); Hasson (2020); Horwitz (2021a): Horwitz (2021b) Horwitz and Seetharaman(2020); Newton (2020); Rodriguez (2020); Rosen et al. (2019); Silverman and Mac (2020a); Silverman and Mac (2020b); Soave (2023); Tracy (2023); Zuckerberg (2017); Zuckerberg (2019)</td></tr></table>

Table A2. Summary: Selected Academic Literature

<table><tr><td>Selected academic literature</td><td>Description</td><td>Sources</td></tr><tr><td>Fake news impact and mitigation</td><td>What is the impact of fake news and mitigation strategies</td><td>Buchanan and Benson (2019); Gimpel et al. (2021); Horner et al. (2023); Jang and Kim (2018); Khan et al. (2022); Kim and Dennis (2019); Lazer et al. (2018); Martel et al. (2020); Moravec et al. (2020) Vraga and Tully (2019); Vosoughi et al. (2018);</td></tr><tr><td>Fact-checking and moderation</td><td>Fact-checking strategies, issues with fact-checking, moderation</td><td>Ali et al. (2019); Allen et al. (2022); Andersen and Søe (2019); Common (2020); Edelson et al. (2020); Kreiss and McGregor (2018); Kreiss and McGregor (2019); Molina and Sundar (2022); Morrow et al. (2022); Zeng and Kaye (2022)</td></tr><tr><td>Regulation of social media</td><td>Discussion on the regulation of social media</td><td>Bail et al. (2020); Jang and Kim (2018); Kalsnes and Ihlebæk (2021); Langley (1999); Myers West (2018); Riedl et al. (2022); Samples (2019)</td></tr></table>

Table A3. Summary: Data Sources for Facebook’s Content Moderation System COVID-19 Response

<table><tr><td>Document on Facebook&#x27;s COVID-19 response</td><td>Description</td><td>Sources</td></tr><tr><td>Documents from Facebook</td><td>Facebook&#x27;s communication on moderation decisions during the pandemic</td><td>Brady (2020); Jin (2020); Rosen (2020)</td></tr><tr><td>General</td><td>News articles on the interesting events that took place during the pandemic focusing on the effect of breakdown of the sociotechnical system</td><td>Bond(2020); Isaac (2020); Koetsier (2020); Legon and Alsalman (2020); Perry (2020); Roberts (2020); Soave (2021); Soave (2023); Teoh et al. (2020); Tiffany (2020); Wong et al. (2020); WHO (2023)</td></tr><tr><td>News articles on moderator work conditions</td><td>News articles on the working conditions of the moderators</td><td>Biddle (2020); Content Moderators (2020); Dwoskin and Tiku (2020); Emerson (2022); Hern (2020); Lomas (2020); Martin (2022); Matsakis and Martineau (2020); New York Post Editorial Team (2020); Thomas (2020); Shead (2020)</td></tr></table>

## Appendix B: The Facebook Moderation and Fact-Checking Process

Section 4 in the main paper describes a high-level view of Facebook’s content moderation and fact-checking process. The illustrated process can be viewed in Figure 2. This appendix discusses the process and each actor, human and non-human, in more detail. First, the appendix presents the non-human decision-making components, followed by the various human actors within the system.

## Algorithmic Decision-Making in Content Moderation

The content moderation process begins when a user uploads a piece of data to Facebook. Data types vary from text to images and video clips. At this point, the algorithms screen some data types, such as music or video files, for copyright infringements (Facebook, 2024e; Gorwa et al., 2020). Applying video “fingerprinting” (a data summarization procedure) algorithms to screen content requires no human content reviewer (Bilobrov, 2015; Li & Wang, 2019; Seetharaman et al., 2021). The algorithm compares the content the user uploaded to a database of copyrighted content, and the copyright screening software flags the matches. Facebook then notifies the uploader about the screening process’s results, which can be appealed and reviewed by a human moderator.

Algorithms also screen for other types of forbidden content, including nudity, terrorism, graphic violence, spam, fake accounts, hateful speech, and suicidal messages (Terdiman, 2018; Kelion, 2017; Zuckerberg, 2017). Facebook has disclosed that the platform applies various image recognition and natural-language-processing algorithms based on machine-learning methods (Schroepfer, 2019; Gorwa et al., 2020; Paluri et al., 2018). According to Facebook, algorithmic image recognition is becoming very effective; the platform claims its algorithms will automatically recognize human nudity or sexually explicit images with 98% accuracy (Facebook, 2024a).

An algorithm that identifies a problematic piece of content might delete it and notify the user (for example, in the case of suspected copyright infringement—Facebook, 2024a), automatically apply warnings that restrict the visibility of the content (Facebook Help, 2024) or forward the content to a human decision maker for further evaluation. However, if a piece of data does not violate copyright laws or other guidelines, the first step of algorithmic decision-making deems it acceptable. The algorithms allow the data to pass onto the platform (Figure 2, bottom arrow).

Facebook’s developers or external contractors create content copyright algorithms, image and natural language processing tools, and other algorithms (Figure 2, top left corner) (Seetharaman et al., 2021). The developers imbue the algorithms with their understanding of the content rules and provide the algorithms with the training data to reinforce these interpretations of the rules (Kroll et al., 2016). Some rules are straightforward. For example, the algorithms determining copyright violations are designed to comply with each country’s extant copyright legislation where the organization operates (Facebook, 2024f). Similarly, content depicting child exploitation is strictly prohibited by legislation (Gillespie, 2018). Other rules can be vaguer and more difficult to translate for algorithmic decision-making. For example, algorithms might struggle more than humans with identifying satire, live streams, or skillfully crafted fake news (Rubin et al., 2016; Seetharaman et al., 2021). The algorithm’s developers will have to navigate legislation and the company rules and guidelines set by Facebook stakeholders (see Facebook Stakeholders section below) when designing, developing, and improving the content moderation algorithms.

## Human Decision-Making in Content Moderation

What happens to the data after it arrives on the platform depends on how users engage. Platform users can report content they believe is fake news, a violation of copyright laws, or otherwise unacceptable (Crawford & Gillespie, 2016). It is unclear whether the algorithmic check is reapplied when the data reenter the process, as our study lacks this level of process detail. However, flagging a piece of content leads the content analysis tools to present it to moderators or fact-checkers, who make the final judgment (Gillespie, 2018). Vague concepts such as hate speech and fake news are difficult for algorithms to identify and moderate, often requiring human verification (Gillespie, 2018; Facebook, 2024f).

The “first response” human decision makers of the content moderation system include the moderators, fact-checkers, advertisement checkers, and the team addressing coordinated inauthentic behavior.

## Moderation of Organic Content

Human content moderation encompasses the moderation of many types of data the algorithms lack skills for assessing. A human moderator, most likely working for a Facebook contractor, will pick up the data from their moderation queue (Paton et al., 2018). The moderators have three available actions regarding the content they analyze: ignore the flags and leave it as is, delete it, or mark it as “disturbing,” limiting the content’s end-user visibility (Facebook Help, 2024). Furthermore, the moderation decision triggers a feedback process that notifies the person who posted the content and who flagged it about the decision.

In unclear cases, the moderators first discuss decisions with their peers. If this does not resolve the issues, they might escalate the decision-making process to “subject matter experts” or “quality assurance,” who have more decision-making power than the contractor (Paton et al., 2018; Newton, 2019b). In some exceptional cases, content is flagged as “shielded,” and only secondary moderators who are permanent Facebook employees can decide whether it is deleted or stays on the website (Paton et al., 2018).

## Moderation of Coordinated Inauthentic Behavior

Another type of content moderation on Facebook consists of moderation of what the platform describes as coordinated inauthentic behavior (CIB). Facebook defines CIB as “Coordinated efforts to manipulate public debate for a strategic goal where fake accounts are central to the operation” (Facebook Newsroom, 2020). For example, the IRA’s activities qualify as CIB (Rosen et al., 2019), and similar networks are continuously removed worldwide (Grossman et al., 2020). Facebook claims domestic and foreign campaigns are involved in CIB (Facebook Newsroom, 2020). From Facebook’s reporting, we can discern that the moderation of CIB is an internal process conducted by a select set of Facebook employees (Stamos, 2018). Unlike other types of moderation or fact-checking, this process is not outsourced or left to third parties, presumably because it requires more technical skill and access to the platform’s back end. Unlike ‘regular’ moderators, Facebook’s CIB moderation can remove whole accounts, not only individual pieces of content (Gleicher, 2019).

## Fact-Checkers

The moderation of fake news forms a special content moderation category with different decision makers than “ordinary” content moderation. Like the other content moderators, fact-checking organizations receive articles in a task queue (Full Fact, 2019) tailored to each fact-checker’s regional or domain expertise (Full Fact, 2019; Ingram, 2019; Teoh et al., 2020). The organizations may not know why each piece of content appears in their queue, but they receive basic facts such as the number of shares and the original upload date. Fact-check organizations have nine categories for classification, including “false,” “true,” “opinions,” and “satire” (Meta Help, 2024).

The organizations add their verdict on the news, which appears on the platform as an additional message attached to the content. Fact-checkers also provide additional information about why they deem the news fake, attaching this explanation to the content (Full Fact, 2019; Facebook, 2024c)

The main difference between regular moderators and fact-checkers is that Facebook has more control over contractors through escalation channels and quality assurance employees (Paton et al., 2018; Newton, 2019b). In contrast, fact-checkers attend Facebook events and discuss fact-checking with similar organizations, but they are considered neutral third parties, partners rather than contractors (Full Fact, 2019). This could mean that third-party fact-checkers have less oversight from Facebook and more freedom in the approaches they use in their fact-checking. It could also imply that Facebook is outsourcing the decisionmaking to third parties to avoid direct scrutiny if the fact-checks are perceived as faulty or partisan by the content creators who have influence within the company (Pasternack, 2020; Robertson, 2020).

## Moderation of Paid Advertisement

Advertisements are moderated in-house and by outsider fact-checking partners (Silverman & Mac, 2020b; Kreiss & McGregor, 2019). Special advertisement categories, such as political ads, have dedicated Facebook teams that work with candidates to ensure ad compliance (Kreiss & McGregor, 2018, 2019) and (at least in early 2020), according to Facebook, the political advertisement was unmoderated (Smith, 2020). Political advertisers have also dedicated Facebook teams that work with candidates to ensure ad compliance (Kreiss & McGregor, 2018, 2019). Facebook has launched a database called Ad Library to provide transparency in their political advertisement, through which reporters and researchers could monitor political advertisements (Edelson et al., 2020). However, the Ad Library’s security measures and the reliability of the data access have been critiqued (Edelson et al., 2020; Smith, 2020).

## Facebook Stakeholders

Facebook stakeholders author guidelines and rules about content and disseminate them across the content moderation system (Newton, 2019b). These stakeholders include any member of the organization who directly impacts the guidelines. This includes the organization’s legal team, which interprets nation-level rules, and all managers who oversee different areas of moderation, such as advertisement moderation, CIB moderation, and moderation of organic content. Furthermore, the stakeholders include the recently established Facebook Oversight Board (the so-called “Facebook Supreme Court”), which consists of 40 independent experts (Douek, 2019). The stakeholders are tasked with difficult decisions about the limitations of speech on the platform. Even though the Oversight Board is not technically part of the organization, it is a stakeholder of the system due to its direct influence on the system and nothing else than the system.

The human content moderators and fact-checkers apply the stakeholders’ rules according to their best understanding. The rules are also relevant for the algorithms’ developers, who must teach the algorithms the new rules each time the stakeholders change the guidelines.

## Appendix C: Inside Facebook—Timestamped Video Content Analysis

Table presents an example of the timestamped coding of the documentary film Inside Facebook: Secrets of Social Networking (Paton et al., 2018) created for Dispatches/Channel 4. This analysis applied video analysis best practices (Knoblauch et al., 2014). First, the documentary was watched several times with closed captioning. Next, a slow walkthrough of the film was conducted. Every time the moderators and the journalist discussed or showed Facebook content monitoring, the film was paused for screenshots and notes, and the actions taking place in the film were coded. This analysis formed the base for modeling the system stakeholder.

Table C1. Inside Facebook: Timestamped Video Content Analysis

<table><tr><td>Theme</td><td>Code</td><td>Timestamped section in “Inside Facebook”</td><td>Corroborating quotes</td></tr><tr><td>Training</td><td>Training</td><td>02:35-03:00 Training session for content moderators and examples of tags for flagging content03:42-03:59 Training session on moderation guidelines</td><td>03:42-3:54 Trainer: So I’m going to go with you and give you the first glimpse of what you are going to be doing as content moderator. We are going to follow Facebook’s policies and decide whether to ignore or delete what we have.</td></tr><tr><td rowspan="3">Organization</td><td>Moderators</td><td>03:00-03:17 Overview of the office and description of the organization</td><td>3:10-3:20 Narrator: Facebook has outsources a lot of it’s activity. Our reporter is working for a company called CPL Resources.Trainer: There is a piece in the policy that you should not be speaking about work related topics, ok?</td></tr><tr><td>Facebook stakeholders</td><td>41:30-41:57 and 42:36-43:09 Details about the queue for “shielded” content</td><td>42:43-42:53 Moderator: We don’t worry too much about deleting their stuff because those pages are shielded, so if you delete a video or whatever, you haven’t deleted Tommy Robinson’s video, it just goes straight to shielded reviewer queue.</td></tr><tr><td>Internal quality assurance</td><td>20:36-21:34 Discussion of policy changes and new guidelines22:42- 23:14 Discussion of moderation guidelines</td><td>20:41-20:55 Moderator 1: This is under new policy now. What was the policy change? Even if it’s condemning, it’s M.A.D. [marked as disturbing]. Everything but a condemning is a delete, isn’t it? Moderator 2: I think that’s what I gathered from the last meeting anyway.</td></tr><tr><td rowspan="2">Guidelines</td><td>Accuracy targets</td><td>Not addressed in the document</td><td></td></tr><tr><td>StandardsGuideline tools</td><td>00:59-01:20 Discussion on moderation guidelines regarding dead people01:24-01:32 Discussion on secretive nature of moderation guidelines01:42-01:47 Discussion on moderating guidelines of “hate” speech02:08 -02:21 Discussion on moderating guidelines of political groups and censorship03:17-03:39 Discussion on secretive nature of moderation guidelines05:48-06:14 and 06:45-08:11 Discussion on moderation guidelines of violence and dead people18:35-18:49 Details about the process of tickets and queues27:46-29:12 and 29:43-30:00 Discussing reporting videos with self-harm, reporting process34:29-35:39 Discussion on guidelines for underage user accounts35:43-36:03 and 36:21-37:26 Discussion on guidelines for “hate speech” (UK context)39:31-40:40, 41:16-41:30 and 42:21-42:36 Discussing policies regarding political groups, activist accounts and limitations set form moderators and escalation process</td><td>06:12 - 06:28 Trainer: We have our three actions. We have ‘ignore’, is no action taken. ‘Delete’ - we will remove it from Facebook and ‘Mark as disturbing’ - is restrictions are placed on who can see the content and how it is presented.2:44-2:48 Narrator: This year, Facebook published a set of rules of what content is allowed. Trainer (demonstrating rules in training): To build and preserve the worlds engagement and trust in Facebook.</td></tr><tr><td></td><td>Issues</td><td>25:36-27:06 Discussing reporting and the reporting backlog, showing examples of the queue</td><td>25:34-25:51 Moderator1: Recently there has been a huge spike in stuff getting reported, we have constantly a backlog now. There was 15 000 reports that needed to be done. The team would do maybe 3000 a day and it doesn’t look like it’s ever going down.</td></tr><tr><td rowspan="3">Process</td><td>Moderation tools</td><td>04:00-04:32 Discussion on content flagging process and examples of content which is deleted17:53-18:35 Film shows the moderators viewing the video clips and discusses the process of reporting and moderating25:36-27:06 Discussing reporting and the reporting backlog, showing examples of the queue30:42-31:17 and 31:52-32:16 Showing the view of a tickets regarding a videos of self-harm: moderating in process</td><td>18:33-18:47 Narrator: Each of these reports is called a ‘ticket’ and the tickets build up in ‘queues’ that the moderators work through. After three and a half weeks of training, our reporter is working through his own queue of tickets.</td></tr><tr><td>Auditing</td><td>Not addressed in the document</td><td></td></tr><tr><td>Escalation</td><td>06:14-06:45 Discussion on actions that the moderators can take09:55-10:10 and 12:58-13:01 Discussion about the reporting process and the response process13:13-14:49 Discussion on an escalation process and policies discussing live videos 27:46-29:12 and 29:43-30:00 Discussing reporting videos with self-harm, reporting process 32:42-33:07 Showing the view of a tickets regarding a videos of self-harm: moderating in process37:37-38:50 Discussing nuances of guidelines and showing the moderator queue 41:30-41:57 and 42:36-43:09 Details about the queue for “shielded” content</td><td>13:13 - Trainee: What must to be done to escalate? Like, if the video’s up like five minutes ago, the kid is beaten and we just Mark As Disturbing, that’s it? Second trainee: Yes but.. this is the odd thing, yes. Trainer: We do have policies for live video which are different...</td></tr></table>

## Appendix D: The Trauma Floor Analysis

Table D1 presents examples of the coding of the article “The Trauma Floor: The Secret Lives of Facebook Moderators in America.” The thematic analysis was done by following the news-media analysis model (Hodgetts & Chamberlain, 2014). First, topics and then key themes were identified. These were coded and ordered. Next, the article was coded in an iterative process with codes initially derived from the documentary film; when new topics emerged, all the data was recoded. The goal of the modeling process of the content moderation system is descriptive rather than theory-building at this first stage

Table D1. The Trauma Floor Analysis Examples

<table><tr><td>Theme</td><td>Code</td><td>Example quotations from “The Trauma Floor” article</td></tr><tr><td>Training</td><td>Training</td><td>She spent the past three and a half weeks in training, trying to harden herself against the daily onslaught of disturbing posts: the hate speech, the violent attacks, the graphic pornography. Chloe’s job is to tell the room whether this post should be removed. She knows that section 13 of the Facebook community standards prohibits videos that depict the murder of one or more people.</td></tr><tr><td rowspan="3">Organization</td><td>Moderators</td><td>Until recently, most Facebook content moderation has been done outside the United States. But as Facebook’s demand for labor has grown, it has expanded its domestic operations to include sites in California, Arizona, Texas, and Florida.</td></tr><tr><td>Facebook stakeholders</td><td>Ellen Silver, Facebook’s vice president of operations, said in a blog post last year that the use of contract labor allowed Facebook to “scale globally” — to have content moderators working around the clock, evaluating posts in more than 50 languages, at more than 20 sites around the world.</td></tr><tr><td>Internal quality assurance</td><td>When Miguel has a question, he raises his hand, and a “subject matter expert” (SME) — a contractor expected to have more comprehensive knowledge of Facebook’s policies, who makes 1 dollar more per hour than Miguel does — will walk over and assist him.</td></tr><tr><td rowspan="4">Guidelines</td><td>Accuracy targets</td><td>Accuracy, in this case, means that when Facebook audits a subset of contractors’ decisions, its full-time employees agree with the contractors. The company has set an accuracy target of 95 percent, a number that always seems just out of reach. Cognizant has never hit the target for a sustained period of time — it usually floats in the high 80s or low 90s, and was hovering around 92 at press time.</td></tr><tr><td>Standards</td><td>Each post presents Miguel with two separate but related tests. First, he must determine whether a post violates the community standards. Then, he must select the correct reason why it violates the standards. If he accurately recognizes that a post should be removed, but selects the “wrong” reason, this will count against his accuracy score.The fourth source is perhaps the most problematic: Facebook’s own internal tools for distributing information. While official policy changes typically arrive every other Wednesday, incremental guidance about developing issues is distributed on a near-daily basis.Often, this guidance is posted to Workplace, the enterprise version of Facebook that the company introduced in 2016. Like Facebook itself, Workplace has an algorithmic News Feed that displays posts based on engagement.</td></tr><tr><td>Guideline tools</td><td>Often, this guidance is posted to Workplace, the enterprise version of Facebook that the company introduced in 2016. Like Facebook itself, Workplace has an algorithmic News Feed that displays posts based on engagement.</td></tr><tr><td>Issues</td><td>Those challenges include the sheer volume of posts; the need to train a global army of low-paid workers to consistently apply a single set of rules; near-daily changes and clarifications to those rules; a lack of cultural or political context on the part of the moderators; missing context in posts that makes their meaning ambiguous; and frequent disagreements among moderators about whether the rules should apply in individual cases.</td></tr><tr><td rowspan="3">Process</td><td>Moderation tools</td><td>Instead, Miguel finds an open workstation and logs in to a piece of software known as the Single Review Tool, or SRT. When he is ready to work, he clicks a button labeled “resume reviewing,” and dives into the queue of posts.Miguel works the posts in his queue. They arrive in no particular order at all.</td></tr><tr><td>Auditing</td><td>From Miguel’s 1,500 or so weekly decisions, Facebook will randomly select 50 or 60 to audit. These posts will be reviewed by a second Cognizant employee — a quality assurance worker, known internally as a QA.</td></tr><tr><td>Escalation</td><td>Sometimes, questions about confusing subjects are escalated to Facebook. But every moderator I asked about this said that Cognizant managers discourage employees from raising issues to the client, apparently out of fear that too many questions would annoy Facebook. This has resulted in Cognizant inventing policy on the fly.</td></tr></table>

## About the Author

Anna Zaitsev is an assistant professor at the Sykes College of Business at the University of Tampa. Her research interests include systems theory, agile software development, design science and application of design thinking for software development, social media recommendation algorithms, and human interactions with generative AI tools. Her work has been published in competitive international conferences and leading journals, including The European Journal of Information Systems, Information & Organization, and First Monday.

Copyright © 2025 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
