---
otero_id: 27896
otero_key: "3NWKM9VN"
title: "Framing of Seeker-Generated Information and New Solver Participation in Open Innovation Contests: An Empirical Analysis of the Temporal Effects"
authors: "Jiahui Mo; Nila Zhang"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0320"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Framing of Seeker-Generated Information and New Solver Participation in Open Innovation Contests: An Empirical Analysis of the Temporal Effects

Jiahui Mo,<sup>a,</sup>\* Nila Zhang<sup>b,</sup>\*

<sup>a</sup> Wilbur O. and Ann Powers College of Business, Clemson University, Clemson, South Carolina 29634; <sup>b</sup> School of Management, Fudan University, Shanghai 200433, China

Contact: jiahuim@clemson.edu, https://orcid.org/0000-0002-8635-8075 (JM); nilazhang@fudan.edu.cn, https://orcid.org/0000-0001-6488-3269 (NZ)

Received: September 15, 2017 Revised: December 2, 2019; July 21, 2021; March 22, 2023; May 19, 2024 Accepted: August 15, 2024 Published Online in Articles in Advance: April 4, 2025

https://doi.org/10.1287/isre.2017.0320

Copyright: © 2025 INFORMS

Abstract. Open innovation contests are dynamic, allowing new solvers to enter at any point before the deadline, and their participation can be influenced by seeker-generated information (SGI), which is publicly accessible to all solvers. Whereas prior literature has primarily examined solver participation among existing participants in a contest, we shift our focus to potential solvers who have not yet joined. Building on evaluation latitude theory, we identify two dimensions of SGI framing when seekers specify their expectations: the extent of prefer ence disclosure and the latitude of rejection (i.e., defining boundaries for design element deemed unacceptable). Drawing on construal level theory (CLT), this study investigates how these two dimensions of SGI framing influence new solver entry and how these effects vary with the number of remaining days in the contest. Using a comprehensive data set from an open innovation contest platform, this research employs various text-mining techniques to construct measures and conducts contest-day-level analyses with multiple estimation strategies. Our findings indicate that extensive preference disclosure increases the daily influx of new solvers, and this effect becomes stronger as the number of remaining days decreases. Additionally, a wide latitude of rejection initially deters but later encourages solver participation as the deadline nears. These results offer actionable insights into how seekers can strategi cally frame SGI at different contest stages to enhance solver participation in open innovation contests.

History: Xiaoquan (Michael) Zhang, Senior Editor; De Liu, Associate Editor.

Funding: N. Zhang acknowledges support from the National Natural Science Foundation of China [Grants 72302053 and 72271058]

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0320.

Keywords: ideation contest • reviews in open innovation • seeker clarifications • solver participation • textual information

## 1. Introduction

In today’s fiercely competitive global market, firms recognize innovation as paramount to their success. According to a recent survey conducted by the Boston Consulting Group (2021), 79% of companies rank innovation among their top three priorities. In pursuit of innovation, firms are increasingly turning to external sources to access diverse knowledge beyond their internal research and development (R&D) capabilities (Lakhani et al. 2013). Among these approaches, open innovation contests have gained prominence, wherein firms (seekers) post challenges on platforms and external contributors (solvers) offer solutions to compete for predetermined rewards (Erat and Krishnan 2012). Firms have used this model extensively for various projects, ranging from simple tasks such as logo design and programming to more complex scientific development projects. This study focuses on ideation contests (i.e., logo design), one of the most popular categories of open innovation contests.

The success of open innovation contests depends largely on attracting a substantial number of solvers, as higher participation levels increase the diversity of solutions and enhance the overall quality of outcomes (Boudreau et al. 2011, Wooten and Ulrich 2017, Chen et al. 2021). According to Chen et al. (2021), the number of solvers participating in a contest can serve as a proxy for the contest’s quality, provided that the prize remains constant.

Given the voluntary nature of participation in open innovation contests (Schenk and Guittard 2011), solvers have the autonomy to decide not only whether to join a contest but also when to do so throughout its duration. Although seekers face uncertainty regarding the number of solvers who will participate, they can influence participation by generating various forms of information, such as contest descriptions, clarifications to solvers’ queries, and solution reviews. We refer to information generated by seekers in contests as seekergenerated information (SGI).

Existing research on open innovation examines primarily how SGI influences solvers who have already entered contests (Jiang et al. 2022). However, the impact of SGI on attracting potential solvers remains underexplored. On most open innovation contest platforms, SGI is accessible not only to existing participants but also to potential solvers who have not yet joined. This gap warrants further investigation because ineffective management of SGI may inadvertently deter prospective solvers, thereby affecting overall participation in contests. This study seeks to address this gap by examining how SGI influences the entry of potential solvers.

Moreover, SGI, typically presented in a textual form, encompasses a wide array of content that has yet to be fully examined. Recent studies have explored various aspects of textual SGI and its impacts on solver participation and solution diversity (Jiang et al. 2021, Sanyal and Ye 2024). However, beyond the content itself, the framing of SGI also influence recipients’ decisions. Framing with different emphases and tones can shape how audiences perceive its importance and incorporate it into their decision-making process (Entman 1993). Textual SGI, characterized by open-ended dialogue from seekers, allows seekers to determine how they communicate with solvers. Understanding the impact of framing can help seekers strategically structure SGI to attract greater participation.

To address this gap, we build on theories of evaluation latitude to identify two dimensions of SGI framing. When specifying SGI, seekers can explicitly state their preferences and convey what is unacceptable using varying tones. More specifically, they determine the extent of preference disclosure by indicating their preferences for various design attributes such as color, font, and style. Additionally, they can establish the latitude of rejection, which denotes the range of design elements explicitly deemed unacceptable. A broad latitude of rejection within SGI indicates that seekers impose stricter constraints to ensure compliance with their specified requirements.

These two dimensions are particularly relevant in open innovation contests, where solvers must interpret textual SGI to gauge the feasibility of their participation. Such framing can reduce uncertainty by providing clear design expectations, potentially lowering solvers’ costs of refining their submissions. However, excessive constraints may limit their creative exploration. As a result, their framing dimensions could influence potential solvers’ entry decisions. Despite their significance, these two dimensions, which inherently manifest in textual

SGI, have not been thoroughly investigated in the context of open innovation. To bridge this research gap, we propose the following research question: How does SGI framing (i.e., the extent of preference disclosure and the latitude of rejection) influence the incremental number of new solvers on a daily basis?

Moreover, contests typically unfold over a predetermined period, during which solvers can join at any point until the closing date. This variable timeframe means that solvers encounter different remaining durations when they choose to participate. Construal level theory (CLT) suggests that solvers’ responses to SGI may vary based on temporal distance (i.e., the number of days remaining until contest closure) (Trope and Liberman 2010). Because the deadline is farther away, solvers may have greater flexibility to consider abstract aspects and explore broader possibilities. However, when the contest approaches its end, solvers may focus more on the concrete and actional guidance in the SGI. This cognitive shift according to the number of remain ing days underscores the critical need to understand the temporal effects of information on solver participation. Accordingly, we propose our second research question: Do the effects of SGI framing on the daily influx of new solvers vary according to the number of remaining days in the contest?

To address these research questions, we obtained comprehensive data (e.g., contests, solvers, and solutions) from Freelancer, a leading platform for open innovation contests. Utilizing various text mining techniques, we analyze the content in SGI (i.e., keywords related to pre ferences, certainty, and rejection) to construct measures of SGI framing, specifically the extent of preference disclosure and the latitude of rejection. Our analysis indi cates that disclosing extensive preferences enhances solver participation, and this effect strengthens as the contest deadline approaches. A broad latitude of rejection initially deters participation when contests commence, because solvers primarily engage in exploration, and restrictive constraints may hinder their creative processes early on. However, as deadlines approach, solvers shift their focus toward seeking actionable and detailed guid ance. Consequently, a broad latitude of rejection becomes more appealing and tends to attract more solvers toward the end of the contest.

This study makes several theoretical contributions to the literature on open innovation contests. Unlike prior research, which primarily examines submission behaviors after solvers have joined a contest, we shift our focus to the potential new solvers. To the best of our knowledge, this study provides one of the first empirical explorations of SGI framing and its temporal effects on the participation of potential new solvers.

We also comprehensively assess the role of information in open innovation context. Specifically, we examine multiple forms of textual SGI (i.e., descriptions, clarifications, and reviews), introduce a new dimension of information-SGI framing, and analyze its temporal effects across the contest duration.

Furthermore, this study makes theoretical contributions by integrating the latitude of rejection and construal level theory (CLT). We provide empirical evidence on how information framing impacts decision-making at different temporal stages. Our findings enhance the theoretical understanding of evaluation latitude within open innovation contexts.

Our findings provide actionable insights for various stakeholders in open innovation contests. By understanding the effects of information on solver entry at different temporal stages, seekers can more strategically tailor both the timing and the framing of their information. Such strategic adjustments could enhance solver participation and, ultimately, improve contest quality.

The remainder of this paper is organized as follows. Section 2 reviews relevant literature. We present the theoretical foundation and develop the hypotheses in Section 3. Section 4 describes the data and measures. Subsequently, we discuss our econometric models and the findings in Sections 5 and 6, followed by robustness checks in Section 7. Finally, Section 8 concludes by discussing the contributions and implications.

## 2. Literature Review

In this section, we review existing studies of SGI on open innovation contest platforms and the theory on latitude of rejection.

## 2.1. SGI in Open Innovation Contests

There are various forms of information in open innovation contests, such as exemplars, numeric ratings, and reviews. A detailed discussion of information in open innovation contests is provided in Online Appendix A. Whereas previous studies have typically focused on a single type of information (Wooten and Ulrich 2017, Koh 2019), our study encompasses a broad spectrum of SGI by examining all textual forms, specifically contest descriptions, seeker clarifications, and textual reviews. Textual information serves as a key channel for seekers to communicate with solvers through concise dialogue formats, often conveying richer and more detailed information.

Previous research on SGI primarily examines its impact on the performance and participation of existing solvers. For example, Wooten and Ulrich (2017) investigated how reviews, such as ratings, influence the quantity and quality of revisions made by participants. However, because SGI is publicly available, it can also affect the participation of individuals who have not yet joined a contest. Despite this potential influence, the relationship between SGI and the entry of potential solvers remains largely unexplored. This research addresses this gap, which is critical, because attracting a larger pool of solvers can enhance contest quality by increasing the diversity of solutions (Boudreau et al. 2011, Camacho et al. 2019).

Moreover, recent studies have begun to examine the content of SGI. For instance, Jiang et al. (2021) found that execution guidelines and conceptual objectives in contest descriptions have impacts on solver participation. Sanyal and Ye (2024) classified feedback into two categories—outcome feedback and process feedback— based on feedback contents and examined their impact on solution diversity. Their findings highlight that the content of SGI plays an important role in influencing solver participation. However, beyond the content itself, the manner in which information is framed could also significantly affect participation and outcomes.

## 2.2. Information Framing and the Theory of Latitude of Rejection

Contents in SGI could be conveyed through specific framing, which refers to the strategic structuring and emphasis of information. Framing highlights certain aspects while downplaying others, thereby shaping how audiences interpret its relevance and prioritize it in their decision-making processes (Entman 1993). By aligning the framing with the audience’s values and concerns, communicators can enhance the perceived salience of the information and increase motivation to act. This mecha nism has been studied in marketing and healthcare, where it is used to promote desired behaviors (Riet et al. 2008, Kyung et al. 2024). For example, health messages framed in terms of potential losses (e.g., “If you do not quit smoking, you risk developing lung cancer”) are often more effective at driving behavioral change than gain-framed messages (e.g., “If you quit smoking, your lung function will improve”). Loss-framed messages tend to elicit stronger emotional responses and a heightened sense of urgency, prompting individuals to act in order to avoid negative consequences (Krishnamurthy et al. 2001, Rothman et al. 2006). Thus, framing serves as a critical mechanism in shaping information perception and influencing motivation to act.

By strategically framing the SGI, seekers can effectively direct solvers’ attention and shape their interpretation of information, thus enhancing their designs. SGI serves as a channel through which seekers communicate their expectations to solvers. When expressing these expectations, seekers can frame them in different ways, such as explicitly stating their preferences or specifying what is unacceptable. To examine SGI framing, we build on theories of evaluation latitude. In open innovation, SGI (e.g., textual reviews) naturally functions as an evaluation resource, and existing theories on evaluation latitude provide a theoretical foundation for understanding information framing.

Rooted in social judgment theory, evaluation latitude refers to the range of opinions, attitudes, or responses an individual deems acceptable or intolerable when evaluating something (Sherif and Hovland 1961). This concept can be reflected in three ways. The latitude of rejection encompasses ideas or opinions that are considered unacceptable or objectionable. The latitude of acceptance includes ideas or opinions perceived as reasonable or acceptable. The latitude of noncommitment consists of ideas or opinions to which an individual is indifferent or views as neither acceptable nor unacceptable.

Among these ranges, the latitude of rejection is particularly crucial. This range serves as an internal reference scale for identifying elements that are unequivocally unacceptable (Vargo and Lusch 2017, Cheng et al. 2021). A wide latitude of rejection indicates that an individual clearly defines their attitudinal boundaries (Schleicher et al. 2015) and has a lower tolerance for viewpoints that deviate from their internal reference scale (Petty and Krosnick 2014). For solvers, ensuring that their submissions are not excluded from consideration is a primary concern. Understanding and adhering to these parameters is essential to avoid immediate disqualification. Therefore, the latitude of rejection plays a critical role in the decision-making process (Fazio and Zanna 1978, Schleicher et al. 2015).

The concept of latitude of rejection has been applied in various judgement-related contexts, such as persuasion, marketing, and negotiation (e.g., Granberg 1982, Petty and Cacioppo 1986). In logo design contests, the evaluation process inherently involves the latitude of rejection. For example, one seeker may exhibit a narrow latitude of rejection, considering only specific aspects of a logo— such as its color—unacceptable. In contrast, another seeker may display a wide latitude of rejection, deeming a broad array of design attributes, ranging from color to font and style, unacceptable. Thus, latitude of rejection in SGI may serve as an indicator of how seekers frame their evaluations.

Evaluation theories suggest that evaluation could be reflected through both rejection and acceptance (Vargo and Lusch 2017). Beyond communicating what is unacceptable, it is equally important to make solvers aware of what is acceptable. Acceptance is typically conveyed by expressing preferences. For example, seekers can explicitly state their preferences in contest descriptions rather than framing in terms of what is acceptable. Therefore, we explicitly measure the extent of preference disclosure in SGI because it represents a distinct dimension of how seekers define the boundaries of their expectations.

Based on the above literature review, Table 1 summarizes the differences in research focus between our study and prior studies on information in open innovation contests. Unlike previous research, which primarily examines the content of information, we investigate two dimensions of information framing: the extent of preference disclosure and the latitude of rejection. This study addresses a theoretical gap by exploring how SGI framing influences new solver participation and how these effects evolve as the contest deadline approaches. Furthermore, rather than focusing on a single form of information (i.e., solution reviews), we consider all the textual information comprehensively, recognizing that solvers— particularly new solvers—evaluate multiple information sources when making participation decisions. Therefore, our study also incorporates seekers’ clarifications on existing solvers’ questions.

3. Theories and Hypotheses Development 3.1. Theoretical Foundation and Research Model Our research is grounded in the integration of the rational decision-making framework and construal level theory (CLT).

3.1.1. Rational Decision-Making Framework. Rational decision-makers typically make choices that optimize their outcomes by balancing costs against benefits (Simon 1955, Basten et al. 2010). This rational choice framework has been applied to understand solver behavior in open innovation contests, where solvers carefully evaluate the trade-offs between the participation costs and the probability of winning. For example, Ye and Kankanhalli (2017) found that solvers’ participation decisions are significantly influenced by their perceptions of these costs and benefits. Similarly, Koh (2019) examined how solvers strategically navigate potential benefits and costs to maximize their chances of success while minimizing effort.

However, accurately assessing costs and the probability of winning is often hindered by various uncertainties, such as seeker preferences and the latitude of rejection. In ideation contests, seekers select the most satisfactory solutions as the winning entries; thus, their preferences for specific design attributes—such as color, font, and background—significantly influence their overall satisfaction with a solution and determine whether a solver’s submission will be selected. However, these preferences are typically private information and may not be fully specified upfront (Bockstedt et al. 2016, Jian et al. 2019). A seeker’s latitude of rejection, which reflects the seeker’s tolerance for designs that deviate from his or her internal scale, can significantly impact solvers’ trial costs and their chances of winning, yet it remains unknown to solvers. Understanding seekers’ preferences and their latitude of rejection reduces the risk of producing undesirable submissions and help solvers avoid futile cost expenditures on unwinnable contests, thereby decreasing the number of trials needed to align with seeker expectations.

Table 1. Different Research Focus on Information in Open Innovation Contests

<table><tr><td>Existing studies</td><td>Information forms</td><td>Research focus</td></tr><tr><td>Jiang et al. (2021)</td><td>Descriptions</td><td>Contents: Execution guidelines and conceptual objectives</td></tr><tr><td>Sanyal and Ye (2024)</td><td>Reviews</td><td>Contents: Outcome feedback and process feedback</td></tr><tr><td>This study</td><td>Descriptions Clarifications Reviews</td><td>Framing: Extent of preference disclosure and latitude of rejection</td></tr></table>

Although seekers provide preference information and constraints, solvers must still explore within these boundaries to create a logo that stands out among all contest submissions (Han 2022). Thus, solvers need to carefully balance their exploration within the given constraints.

3.1.2. Construal Level Theory and Remaining Days. Open innovation contests are characterized by a fixed duration, meaning that solvers who enter at different times face varying numbers of remaining days to complete their solutions. Solvers must consider the number of remaining days when making entry decisions in this dynamic contest environment (Jiang et al. 2022).

Construal level theory (CLT) provides insights into how the temporal distance of an event (i.e., the number of remaining days) influences solvers’ information processing and behavior (Trope and Liberman 2010). According to CLT, the number of remaining days reflects how immediate or distant the contest completion appears to solvers. When time is plentiful, individuals engage in more extensive explorations, considering a broader range of options and evaluating them more thoroughly (high-level construals). However, as the deadline approaches, individuals shift toward more concrete and detail-oriented considerations (low-level construals) (Waller et al. 2002).

Following this theory, the transition between different levels of thinking affects how solvers process information and make decisions. When the deadline is distant, the urgency for immediate execution (i.e., submitting final solutions) is less pressing, allowing solvers greater flexibility to explore within the defined preference boundary. As the deadline approaches, the focus intensifies on specific, actionable details essential for developing acceptable solutions. Therefore, clear boundaries regarding design elements deemed unacceptable become increasingly critical because they provide explicit guidance that can be directly applied to submissions.

3.1.3. Research Model. Integrating the rational decision-making framework and construal level theory, we propose a research model (illustrated in Figure 1) that captures the relationships between the framing of SGI and the influx of new solvers into contests. This model also examines the moderating effect of the num ber of remaining days.

Figure 1. Research Mode  
![](/api/attachments/3NWKM9VN/fulltext/images/4e7a297c736a40de51133fc1b20894ef7cc4f8277d5d47f84572f47df6e9c4b7.jpg)

## 3.2. The Relationship Between the Extent of Preference Disclosure and the Incremental Number of New Solvers

Seekers select winning solutions based on their preferences, and solvers must consider these preferences when developing their solutions (Terwiesch and Xu 2008). The extent of preference disclosure via SGI can significantly influence solvers’ assessment of their winning chances and associated costs, thereby impacting their participation.

Extensive preference disclosures provides clear guid ance for solvers, facilitating their understanding of seekers’ expectations across various design elements (Afuah and Tucci 2012). By specifying preferences in detail, seekers can reduce the ambiguity that solvers might face regarding desired design attributes, such as color, font, and style. This clarity enables solvers to tailor their submissions more precisely to seekers’ expectations, thereby increasing the likelihood of producing a design that aligns closely with the seeker’s vision (Woo ten and Ulrich 2017, Boe¨nne et al. 2023).

When solvers have a clear understanding of specific preferences and requirements, they can more effectively allocate their efforts, minimizing the trial-and-error process typically involved in design iterations (Terwiesch and Xu 2008). Consequently, solvers may perceive their investment in such contests as more efficient and worthwhile, thereby increasing their willingness to participate (Archak et al. 2011).

Therefore, providing extensive preference information can increase the expected winning chances and reduce expected trial costs. As a result, it can attract more solvers to participate in the contest. Based on this rationale, we propose the following.

H1. The more extensive the provision of preference informa tion in SGI, the greater the incremental number of new solvers.

Open innovation contests typically have predetermined durations. According to construal level theory (CLT), the temporal distance to a deadline can significantly shift solvers’ cognitive focus, subsequently influencing their decision-making processes (Trope and Liberman 2010). When the deadline is far away, solvers are not under immediate pressure to finalize their submissions. This temporal distance gives them the flexibility to explore a broader range of ideas and experiment with various styles or concepts. During this period, solvers may engage in high-level, abstract thinking, enabling them to generate innovative and original solutions that distinguish their submissions (Liberman and Trope 1998). Extensive research indicates that this exploratory phase is crucial for fostering creativity and innovation because it enables individuals to delve deeply into the problem space and consider a wider array of potential solutions (Amabile 1988).

As the contest deadline approaches, however, solvers face increased pressure to submit entries that comply with the seeker’s requirements within a shorter timeframe. This shift induces a transition from high-level abstract thinking to low-level concrete thinking, where solvers focus on immediate, practical concerns (Trope and Liberman 2003). With limited opportunities to iterate their solutions through multiple revisions, solvers prioritize meeting the specific, actionable guidance provided by extensive preference information. This shift aligns with the findings of Karau and Kelly (1992), who demonstrated that as deadlines near, individuals tend to engage in more focused and directed activities to meet the impending requirements. Therefore, the positive effect of extensive preference information is likely to become more pronounced as the contest approaches its end. Based on this reasoning, we propose the following hypothesis.

H2. The positive effect of extensive preference disclosure in SGI increases as the number of remaining days decreases.

## 3.3. The Relationship Between the Latitude of Rejection and the Incremental Number of New Solvers

The satisfaction of seekers with solutions depends significantly on their latitude of rejection (Hart et al. 2003). A wider latitude of rejection indicates a more narrowly defined and inflexible attitude (Sherif and Hovland 1961), wherein seekers consistently dismiss solutions that fail to meet their stringent criteria. This characteristic ensures a well-defined evaluation process for submissions and establishes clear boundaries of unacceptability (Martinsuo and Poskela 2011). The latitude of rejection influences solvers’ assessments of costs and their predicted probabilities of winning in a contest, thereby affecting their participation.

When seekers have a wide latitude of rejection, they typically provide explicit guidance on what will not be accepted. Solvers must adhere precisely to these guide lines, minimizing trial-and-error costs associated with deviating from the seekers’ preferences (Cheng et al. 2021). A wider latitude of rejection offers solvers a clear framework for tailoring their designs effectively to meet the seekers’ expectations (Hameiri et al. 2020). Consequently, with clear guidance, solvers are less likely to be rejected or lose a contest compared with those participating in contests without well-defined boundaries.

Furthermore, well-defined boundaries allow solvers to avoid investing time in designs that are unlikely to meet the seekers’ requirements. This efficiency enhances the exploration process, enabling solvers to concentrate their efforts on viable solutions that fit within the given parameters while still achieving high levels of innovation and originality. Thus, solvers may prefer contests where seekers establish a wider latitude of rejection. Based on these arguments, we propose the following hypothesis.

## H3. The wider the latitude of rejection in SGI, the greater the incremental number of new solvers.

According to construal level theory (CLT), when sol vers have ample time, they tend to focus on broad, exploratory activities rather than specific requirements. Clear rejection criteria can effectively guide solvers exploration within known boundaries, helping them avoid futile directions and concentrate their efforts on more promising elements (Erat and Krishnan 2012). However, overly restrictive rejection criteria may limit the scope of exploration, potentially constraining creativity and innovation. This restriction can deter solvers from participating because the perceived opportunity to produce a novel and successful design diminishes.

As the number of remaining days in the contest decreases, solvers face increased pressure to complete their designs according to the seekers’ requirements. At this stage, solvers are likely to prioritize information that provides actionable guidance on how to design their submissions. Rejection information becomes particularly valuable because it specifies explicitly which design elements should be avoided, thereby reducing ambiguity and uncertainty (Locke and Latham 2002). Consequently, solvers may place greater importance on the latitude of rejection when contests are nearing their end. Based on this reasoning, we propose the following hypothesis.

H4. The positive effect of latitude of rejection in SGI increases as the number of remaining days decreases.

## 4. Data and Measures 4.1. Survey

In Section 3, we developed a theoretical framework to examine how SGI framing influences the number of new solvers participating in contests. To gather modelfree evidence for our hypotheses concerning solvers decision-making in real-world scenarios, we conducted a survey via Amazon Mechanical Turk (MTurk) in August 2018, collecting 200 responses, comprising 122 men and 78 women. Notably, 73% of respondents had prior experience with open innovation. To ensure comprehension, we provided detailed information about our research platform, including screenshots of contest details, before initiating the survey.

Survey findings revealed that approximately 86% of solvers read seekers’ clarifications in the public clarification area, and 88% review feedback on existing solutions before entering a contest. Additionally, 52% of solvers assess seekers’ preferences from available information, 69% consider seekers’ sentiments toward submissions, and 67% attempt to gauge seekers’ degree of certitude. These insights further underscore the significance of SGI framing in solvers’ contest evaluations and entry decisions.

## 4.2. Research Context and Platform

Our study utilized Freelancer as the research platform. Contests, along with their rewards, durations, and descriptions, are listed in reverse chronological order on the platform’s contest pages, where solvers select contests to enter. Upon accessing a contest page, solvers can view detailed descriptions, clarifications, existing solutions, reviews, and ratings. Entry into contests is open throughout their duration, during which seekers may update descriptions<sup>1</sup> or clarify contest requirements in a designated public area in response to solvers’ inquiries.<sup>2</sup> Seekers also provide textual reviews and ratings of submitted solutions. Table 2 presents examples of the three forms of textual SGI. All information is publicly accessible to both active and prospective solvers and may contain different types of content. For example, descriptions and clarifications typically outline seekers requirements and frequently include keywords that indicate their preferences. Seekers generate reviews as comments on solvers’ solutions. Thus, reviews not only contain preference-related keywords but also convey varying tones, such as rejecting solutions with either certain or uncertain phrasing. After the contest deadline, seekers select the best solution and award the designated prize. However, they reserve the right to forgo selecting a winner if the submitted solutions are deemed unsatisfactory.

We developed a Java-based crawler to collect data on all logo-design contests posted on Freelancer between February and March 2016. This data set encompasses predefined contest attributes, such as prize amount and duration, alongside detailed information about each solution, including its creator, timing, ratings (from 1 to 5), and reviews. Our data collection extends to solvers profile information and historical performance, capturing the number of contests each solver entered, their tota solution submissions, and their winning records. In total, the data set comprises 2,367 logo-design contests. On average, 40 new contests were launched daily, with approximately 271 contests open each day. These contests typically lasted between four and 10 days, offering an average prize of \$58.68. Each contest attracted an average of 24 solvers and generated 10 reviews. Our data set includes 8,552 unique solvers who participated in at least one contest, contributing to a total of 55,231 proposed solutions. The average solver participated in 6.46 contests, with a standard deviation of 16.69.

Because we focus specifically on textual SGI on open innovation platforms, we employ various text-mining techniques to analyze SGI framing and will discuss the corresponding measures in subsequent subsections.

## 4.3. Measure for Extent of Preference Disclosure 4.3. Measure for Extent of Preference Disclosure

Seekers typically express their preferences through various information forms, including descriptions, clarifications, and reviews. Such information serves as a repository of preference cues, capturing essential design elements such as color, font, and style. For instance, the specific mention of “yellow” may indicate a preference for this color. The prevalence of preference-specific keywords within the textual information provides a quantitative measure of the extent of preference disclosure.

Table 2. Examples of Textual Seeker-Generated Information (SGI)

<table><tr><td>Information forms</td><td>Examples</td><td>Information</td><td>SGI framing</td></tr><tr><td>Descriptions</td><td>I need a logo-to-go a product sleeve for a new product. It should be an American style, typical USA Style.I just need it jazzed up a bit. Unique colors. Unique fonts.I need new t-shirt designs for men&#x27;s and women&#x27;s Crossfit shirts.</td><td>Keywords for preferences</td><td>Extent of preference disclosure</td></tr><tr><td>Clarifications</td><td>We need a compact size logo. Logo stamp should be on the left. $2,000 \times 1,000$ .No specific color; however, 2 or 3 colors maxI would like the source file, a JPEG, PNG, and Vector File.</td><td>Keywords for preferences</td><td>Extent of preference disclosure</td></tr><tr><td>Reviews</td><td>Please try out different fonts for the words, too.Add black stars at either end of the nation, and remove green stars.Instead of the basketball player, if you could try some other images.Black and white colors for the design.</td><td>Keywords for preferencesRejection attitude when doing valuationCertain attitude when doing evaluation</td><td>Extent of preference disclosureLatitude of rejection</td></tr></table>

We employed content analysis, utilizing natural language processing tools from the R package (Indurkhya and Damerau 2010) to preprocess text and extract keywords indicative of preferences. We acknowledge that not all words in the text are informative regarding preferences. Specifically, function words—such as conjunctions, pronouns, and auxiliary verbs—carry little lexical meaning and serve primarily to maintain grammatical structure. Therefore, our analysis focused on adjectives and nouns, which typically convey specific details relevant to seekers’ preferences (Archak et al. 2011).

In the analysis process, certain words were rarely used, characterized by their infrequent occurrences within the data set. Including such rare keywords in the analysis would significantly increase computational complexity. To address this, we excluded words that appeared in less than 0.1% of the data set to optimize computational efficiency without compromising the integrity of the data analysis. Following this refinement, we identified 1,941 candidate keywords.

We enlisted the support of three students to identify keywords indicative of seekers’ preferences among the remaining candidates. The intercoder reliability was evaluated using Krippendorff’s alpha (1980), yielding a consistency score of 0.91—surpassing the commonly accepted threshold of 0.7. This high score indicated strong agreement among the coders regarding the classification of keywords. Following this, the authors conducted a thorough review to resolve any remaining ambiguities, culminating in the identification of 557 keywords. Subsequently, we meticulously tracked the occurrence of each keyword across various information forms—descriptions, clarifications, and reviews. Table 3 presents the 10 most frequently appearing keywords. We computed the cumulative frequency of identified preference keywords across all information forms for each contest as the measure for the extent of preference disclosure.

## 4.4. Measure for Latitude of Rejection

The latitude of rejection denotes the spectrum of ideas, opinions, or messages that individuals deem unacceptable. Individuals with a broad latitude of rejection are characterized by strict criteria that lead to the rejection of submissions failing to align closely with their predefined expectations (Schleicher et al. 2015). Such individuals tend to use decisive and absolute language in their feedback, clearly delineating unacceptable elements (Eagly and Kulesa 1997, Cheng et al. 2021). Their evaluations are marked by certainty and an emphasis on specific instances of noncompliance, typically accompanied by detailed negative feedback on particular design elements. In open innovation contests, seekers with a broad latitude of rejection exhibit similar linguistic patterns, incorporating rejection-related keywords, expressions of certainty, and references to specific design elements. To accurately assess seekers latitude of rejection, it is crucial to identify the range of elements they consider unacceptable. This process can be facilitated through the application of text-mining techniques, involving the following steps.

A single review usually consists of multiple sentences, not all of which evaluate specific design attributes. The initial step involves filtering out sentences that do not pertain to the evaluation of specific design attributes. By leveraging the keywords identified in Section 4.3, directly related to specific design dimensions such as logo attributes, we retain sentences that incorporate these keywords because they pertain to specific design elements.

For instance, consider the review: “I certainly like it! I love purples. My biggest thing would be to not have a box around the text of the image.” Whereas the first sentence is nonspecific, the latter two directly address design elements (color and structural features); thus, only these are retained for further analysis.

Table 3. The 10 Most Frequently Appearing Keywords

<table><tr><td colspan="2">Appearance frequency in clarifications</td><td colspan="2">Appearance frequency in reviews</td><td colspan="2">Appearance frequency in descriptions</td></tr><tr><td>Noun</td><td>Count</td><td>Noun</td><td>Count</td><td>Noun</td><td>Count</td></tr><tr><td>Color</td><td>2,394</td><td>Color</td><td>26,345</td><td>Company</td><td>3,863</td></tr><tr><td>Idea</td><td>1,514</td><td>Font</td><td>22,421</td><td>Color</td><td>2,435</td></tr><tr><td>Company</td><td>1,199</td><td>Background</td><td>7,726</td><td>Website</td><td>1,766</td></tr><tr><td>Font</td><td>1,136</td><td>White</td><td>7,290</td><td>Brand</td><td>1,094</td></tr><tr><td>Image</td><td>1,066</td><td>Blue</td><td>7,091</td><td>Image</td><td>914</td></tr><tr><td>Attach</td><td>762</td><td>Black</td><td>7,056</td><td>Product</td><td>868</td></tr><tr><td>Text</td><td>722</td><td>Text</td><td>6,919</td><td>File</td><td>698</td></tr><tr><td>Website</td><td>691</td><td>Letter</td><td>6,572</td><td>Black</td><td>662</td></tr><tr><td>Letter</td><td>556</td><td>Image</td><td>6,127</td><td>White</td><td>616</td></tr><tr><td>White</td><td>556</td><td>Icon</td><td>5,312</td><td>Font</td><td>589</td></tr></table>

Additionally, seekers with a wide latitude of rejection tend to explicitly reject elements deemed unacceptable. To identify the rejection sentences, we apply a deeplearning Java package for sentiment analysis (Socher et al. 2013) to each retained sentence in the subset, classifying them as positive, neutral, or negative (Hu and Liu 2004, Das and Chen 2007). This process aids in detecting sentences that explicitly express rejection (negative sentiment). To validate the sentiment classification, three graduate students performed manual labeling, achieving a classification accuracy of 85.4%. This high accuracy underscores the reliability of the sentiment analysis approach employed. Following this analysis, the candidate sentences were further refined by retaining only those that expressed rejection, each reflecting the seekers’ rejection on specific design elements.

As discussed earlier, individuals with a wide latitude of rejection not only reject specific attributes but also use definitive language when rejecting, clearly defining the boundary of noncompliance. To extract such “certainty” from the subset of sentences, we utilize the Linguistic Inquiry and Word Count (LIWC-22) tool (Boyd et al. 2022). LIWC specifically analyzes the presence of definitive words such as “always,” “certainly,” “definitely,” and “never,” which serve as linguistic cues for certainty. By counting the frequency of these certainty words in each sentence within the subset, LIWC assigns a certitude score to each sentence. Sentences with a score above 0 are classified as those rejecting specific design attributes with certainty. Finally, we calculate the total number of sentences containing definitive rejections of specific attributes as the measure for the latitude of rejection. Table 4 provides examples of sentences with rejection and certainty.

## 4.5. Control Variables

In our analysis, we account for a range of fundamental contest characteristics that may influence outcomes, such as prize amount and contest duration. Additionally, we control for the guarantee status of payments because contests with nonrefundable, guaranteed prizes reduce the financial risk to solvers, potentially serving as a proxy for the seekers’ accountability.

Table 4. Examples of Sentences Conveying Rejection and Certainty

<table><tr><td>Rejection</td><td>The fonts look old and outdatedNot liking this oneSorry, getting worseCould use better fontI feel it doesn&#x27;t pop out as much from the background</td></tr><tr><td>Certainty</td><td>Logo has to be flatNot really our styleToo busyColor perfectNever purples</td></tr></table>

Furthermore, we control for the seeker’s experience, operationalized as the number of contests they have successfully completed prior to the current contest. This measure acts as an indicator of the seeker’s reputation, which may alleviate solvers’ concerns regarding the seeker’s accountability and trustworthiness.

We also control for many time-variant variables that could affect the entry of new solvers, including the number of existing solvers who have participated in the contest, the average capabilities of these solvers, the volume of clarifications provided by solvers, the total number of reviews offered by seekers, and the number of competing contests during the same period (Mo et al. 2021). The politeness in SGI could also influence solvers’ participation (Hong et al. 2021, Wu et al. 2023). To measure the politeness in SGI, we use LIWC 22 to calculate the politeness score of sentences and use the average politeness score as a control variable, which reflects the degree of politeness. To account for competition quality, we cal culate the average score of all submitted solutions, thereby quantifying overall contest quality.

Construal level theory (CLT) suggests that temporal distance (i.e., the number of days remaining until the contest deadline) influences solvers’ decisions. Therefore, we control for the moderator variable (the number of remaining days) by calculating the interval between the entry day and the contest closure. We use the date of solution submission as a proxy for entry. Statistics for all primary and control variables are presented in Table 5, and correlations among these variables are detailed in Table C.1 in Online Appendix C.

## 5. Empirical Models, Econometric Issues, and Estimation Strategies 5.1. Model Specification

We focus on the relationship between information framing and the daily influx of new solvers. By employing a contest-day-level analysis, we investigate how the information available one day prior to the focal day influences the incremental number of new solvers on the focal day. We specify Model 1 as follows:

$$
\log \left(E (N D V _ {i t} | S G I)\right)
$$

$= \beta _ { 0 } + \beta _ { 1 } L o g$ of extent of preference disclosu $r e _ { i t - 1 }$

$+ \beta _ { 2 } L o g$ of latitude of rejection $\dot { \mathbf { \zeta } } _ { i t - 1 } + \beta _ { 3 } D a y \_ l e f t _ { i t - 1 }$

\- $- \beta _ { 4 } L o g$ of extent of preference disclosure<sub>it�1</sub>

$\times D a y \_ l e f t _ { i t - 1 } + \beta _ { 5 } L o g$ of latitude of rejectio $\boldsymbol { \imath } _ { i t - 1 }$

$$
\times D a y \_ l e f t _ {i t - 1} + \beta_ {6 - 9} C o n t e s t C o n t r o l s _ {i}
$$

$$
+ \beta_ {1 0 - 1 5} P a r t i c i p a t i o n C o n t r o l s _ {i t - 1}
$$

$$
+ \beta_ {1 6} \text { Number   of   competing   contests } _ {i t - 1} + \mu_ {t} + \varepsilon_ {i t},\tag{1}
$$

Table 5. Variables and Statistics

<table><tr><td>Types of variables</td><td>Variables</td><td>Description</td><td>Obs</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td rowspan="2">Dependent variables</td><td>No. of new solvers</td><td>Number of new solvers that participated in the contest on the focal day</td><td>16,322</td><td>3.412</td><td>6.698</td><td>0</td><td>363</td></tr><tr><td>No. of new solutions</td><td>Number of new solutions submitted in the contest on the focal day</td><td>16,322</td><td>10.055</td><td>19.091</td><td>0</td><td>981</td></tr><tr><td rowspan="2">Main independent variables</td><td>Log of extent of preference disclosure</td><td>The log number of preference keywords in the descriptions, clarifications, and reviews by 1 day before the focal day</td><td>16,322</td><td>2.683</td><td>0.943</td><td>0</td><td>6.404</td></tr><tr><td>Log of latitude of rejection</td><td>The log number of definitive rejection sentences in reviews by 1 day before the focal day</td><td>16,322</td><td>0.030</td><td>0.167</td><td>0</td><td>3.091</td></tr><tr><td>Moderator</td><td>Day_left</td><td>The number of remaining days</td><td>16,322</td><td>3.070</td><td>2.17</td><td>0</td><td>9</td></tr><tr><td rowspan="11">Control variables</td><td>Average ratings</td><td>Average ratings of existing solutions by 1 day before the focal day</td><td>16,322</td><td>1.831</td><td>1.45</td><td>0</td><td>5</td></tr><tr><td>Guaranteed</td><td>Whether a contest is guaranteed to make the payment or not</td><td>16,322</td><td>0.885</td><td>0.32</td><td>0</td><td>1</td></tr><tr><td>Log of seeker reviews</td><td>The log number of reviews provided by 1 day before the focal day</td><td>16,322</td><td>0.896</td><td>1.168</td><td>0</td><td>6.057</td></tr><tr><td>Log of solver clarification questions</td><td>The log number of clarification questions that solvers provided by 1 day before the focal day</td><td>16,322</td><td>1.013</td><td>1.048</td><td>0</td><td>3.912</td></tr><tr><td>Log of existing solvers</td><td>The log number of existing solvers participating in a contest by 1 day before the focal day</td><td>16,322</td><td>2.067</td><td>1.31</td><td>0</td><td>6.016</td></tr><tr><td>Log of seeker experience</td><td>The log number of seekers&#x27; completed contests before posting the focal contest</td><td>16,322</td><td>0.641</td><td>0.977</td><td>0</td><td>5.416</td></tr><tr><td>Prize</td><td>The award amount of the contest</td><td>16,322</td><td>59.56</td><td>59.75</td><td>7.64</td><td>1,400</td></tr><tr><td>Contest duration</td><td>Number of open days of the contest</td><td>16,322</td><td>7.139</td><td>1.30</td><td>4</td><td>10</td></tr><tr><td>Log of average solver capability</td><td>Average solvers&#x27; ratio of winning contents to total number of participating contests before entering the focal contest</td><td>16,322</td><td>0.005</td><td>0.045</td><td>0</td><td>0.693</td></tr><tr><td>Number of competing contests</td><td>Number of competing contests that are available on the focal day</td><td>16,322</td><td>270.97</td><td>17.46</td><td>232</td><td>311</td></tr><tr><td>Log of average review politeness</td><td>Log of average politeness score of review sentences by 1 day before the focal day</td><td>16,322</td><td>0.267</td><td>0.759</td><td>0</td><td>4.615</td></tr></table>

where $N D V _ { i t }$ represents the incremental number of new solvers who entered contest i on day t. To examine the effects of SGI, we included Log-transformed measures of the extent of preference disclosure and latitude of $r e j e c t i o n _ { i t - 1 }$ from the previous day. We use the date of the first submission as a proxy for the entry day of solvers, calculating the number of remaining days $( D a y \_ l e f t _ { i t - 1 } )$ . For instance, if a contest lasts five days and solver i enters on the third day, then the remaining days for solver i would be two. To investigate whether the effects of SGI framing on the incremental number of new solvers vary with the number of remaining days, we include interaction terms between Day ${ \mathit { l e f t } } _ { i t - 1 }$ and the two main independent variables. The coefficients $\beta _ { 4 }$ and $\beta _ { 5 }$ capture these interaction effects.

We control for the observable contest-level characteris tics (ContestControls ) that remain constant for all solvers, including whether the payment is guaranteed, prize amount, contest duration, and seeker experience. These controls help mitigate the potential effects of intrinsic contest characteristics and seeker attributes that could influence the daily increase in the number of new solvers. Additionally, we account for other participationrelated factors $( P a r t i c i p a t i o n C o n t r o l s _ { i t - 1 } )$ such as average $r a t i n g s _ { i t - 1 } ,$ log of seeker reviews <sub>�</sub> , log of existing solvers<sub>it�1</sub>, log of solver clarification questions<sub>it�1</sub>, and log of average solver capability <sub>�</sub> . Besides, we also control for the politeness of SGI by the variable log of average review politeness<sub>it�1</sub>. To account for the competitive effect from concurrent contests, we include the number of competing contests as a control variable. We also consider potential temporal heterogeneity in solvers’ decisionmaking by incorporating a day dummy variable (µ ).

Variance inflation factors (VIF) were examined to ensure that multicollinearity does not confound the results. The highest VIF value was 2.04, with an average VIF of 1.73, indicating that multicollinearity is not a concern in our models. In the following subsections, we outline various estimation strategies to address econometric issues. The findings are then discussed in Section 6.

## 5.2. Poisson Regression Model

Because the dependent variable in Model 1 is a count variable, we first employ a Poisson regression model for estimation. We begin by including only the control variables, followed by the addition of the two main independent variables. Finally, we introduce the interaction terms. The results are presented in Table 6.

## 5.3. Selection Bias and Matching

Seekers have discretion in providing feedback, which may introduce self-selection bias. The observed increase in solver participation may not be solely attributable to SGI framing. Instead, more experienced seekers—who naturally attract more solvers because of their established reputation—may be more inclined to provide feedback. Likewise, higher solver participation could stem from inherent contest characteristics, such as longer durations, which are also associated with a greater number of reviews. If contests or seekers that provide feedback differ systematically differ from those that do not, then these underlying differences could confound the effects of SGI framing. To ensure that solver participation is driven by SGI framing rather than contests or seeker characteristics, we aim to make contests and see kers as comparable as possible across all aspects, except for the presence of feedback.

To mitigate this issue, we adopt the propensity score matching (PSM) approach (Schultz and Zaman 2001, Tucker 2010, DeFond et al. 2017). We match contests with and without reviews on a daily basis based on contest attributes (i.e., payment, duration, guaranteed status) and seekers’ characteristics (i.e., seeker’s experience). Additionally, we incorporate existing contest dynamics (i.e., the number of clarification questions and average solver capabilities) in the matching process to ensure that contests in the treatment and control groups have comparable clarification questions and participants at the same stage. This approach helps alleviate concerns that reviews may be influenced by observed dynamics (e.g., the number of questions and solvers in the contests). We employ one-toone matching with a caliper size of 0.01 to identify similar contests with and without feedback information. This process results in 4,325 contests, with reviews being matched to 4,325 contests without reviews.

Table 6. Coefficients for the Poisson Regression Estimation

<table><tr><td>Types of variables</td><td>Models</td><td colspan="2">(1)</td><td colspan="2">(2)</td><td colspan="2">(3)</td></tr><tr><td rowspan="2">Main IVs</td><td>Log of extent of preference disclosure</td><td></td><td></td><td>0.055***</td><td>(0.0061)</td><td>0.149***</td><td>(0.0127)</td></tr><tr><td>Log of latitude of rejection</td><td></td><td></td><td>0.008</td><td>(0.0297)</td><td>0.231***</td><td>(0.0593)</td></tr><tr><td rowspan="2">Interactions</td><td>Log of extent of preference disclosure × Day_left</td><td></td><td></td><td></td><td></td><td>-0.022***</td><td>(0.0026)</td></tr><tr><td>Log of latitude of rejection × Day_left</td><td></td><td></td><td></td><td></td><td>-0.069***</td><td>(0.0169)</td></tr><tr><td rowspan="17">Controls</td><td>Day_left</td><td>0.253***</td><td>(0.0043)</td><td>0.253***</td><td>(0.0043)</td><td>0.309***</td><td>(0.0077)</td></tr><tr><td>Prize</td><td>0.003***</td><td>(0.0000)</td><td>0.003***</td><td>(0.0000)</td><td>0.003***</td><td>(0.0000)</td></tr><tr><td>Contest duration</td><td>-0.298***</td><td>(0.0050)</td><td>-0.299***</td><td>(0.0000)</td><td>-0.298***</td><td>(0.0050)</td></tr><tr><td>Guaranteed</td><td>0.728***</td><td>(0.0179)</td><td>0.713***</td><td>(0.0179)</td><td>0.710***</td><td>(0.0179)</td></tr><tr><td>Log of seeker experience</td><td>0.119***</td><td>(0.0045)</td><td>0.121***</td><td>(0.0045)</td><td>0.122***</td><td>(0.0045)</td></tr><tr><td>Average ratings</td><td>-0.171***</td><td>(0.0046)</td><td>-0.171***</td><td>(0.0046)</td><td>-0.169***</td><td>(0.0046)</td></tr><tr><td>Log of seeker reviews</td><td>-0.020***</td><td>(0.0059)</td><td>-0.049***</td><td>(0.0069)</td><td>-0.069***</td><td>(0.0074)</td></tr><tr><td>Log of existing solvers</td><td>0.200***</td><td>(0.0053)</td><td>0.197***</td><td>(0.0053)</td><td>0.203***</td><td>(0.0054)</td></tr><tr><td>Log of solver clarification questions</td><td>-0.322***</td><td>(0.0075)</td><td>-0.322***</td><td>(0.0075)</td><td>-0.331***</td><td>(0.0076)</td></tr><tr><td>Log of average solver capability</td><td>-2.253***</td><td>(0.1611)</td><td>-2.239***</td><td>(0.1615)</td><td>-2.249***</td><td>(0.1608)</td></tr><tr><td>Log of average review politeness</td><td>0.016*</td><td>(0.0071)</td><td>0.016*</td><td>(0.0071)</td><td>0.018*</td><td>(0.0072)</td></tr><tr><td>Number of competing contests</td><td>-0.001***</td><td>(0.0003)</td><td>-0.001***</td><td>(0.0003)</td><td>-0.002***</td><td>(0.0003)</td></tr><tr><td>Time Effect</td><td>Yes</td><td></td><td>Yes</td><td></td><td>Yes</td><td></td></tr><tr><td>Pseudo-R2</td><td>0.235</td><td></td><td>0.235</td><td></td><td>0.236</td><td></td></tr><tr><td>Aic</td><td>106,755.1</td><td></td><td>106,676.39</td><td></td><td>106,568.48</td><td></td></tr><tr><td>Bic</td><td>106,901.41</td><td></td><td>106,838.09</td><td></td><td>106,745.59</td><td></td></tr><tr><td>Number of observations</td><td>16,322</td><td></td><td>16,322</td><td></td><td>16,322</td><td></td></tr></table>

Note. Standard errors are in parentheses.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

The matching performance and the results of the probit estimation are presented in Online Appendix D. We then combine these two groups of contests and re-estimate Model 1 using the matched data set. The findings, presented in column (1) of Table 7, are consistent with our main results, reinforcing the robustness of our results.

## 5.4. Endogeneity and Control Function Approach

Our two main variables—the extent of preference disclosure and the latitude of rejection—are potentially endogenous, because seekers decide how to frame SGI, and unobserved intrinsic characteristics of seekers may contribute to variations in SGI framing (Gross 2017, Jiang et al. 2021). For instance, some seekers, particularly those with a wide latitude of rejection, may prefer detailed requirements, whereas others may favor more conceptual feedback. Such unobserved factors necessitate addressing potential endogeneity concerns.

To address this issue, we identified instrumental variables (IVs) that are predictive of our main variables but uncorrelated with the error terms in the model. We leveraged seekers’ historical information-generation behaviors as IVs under the assumption that seekers exhibit consistent framing styles across contests. For example, seekers who favor detailed requirements with rejection tones will consistently write reviews in this manner. Thus, examining how seekers generate information in previous contests provides insights into their behavior in subsequent contests.

Specifically, for the first endogenous variable, the extent of preference disclosure, we used the average extent of preference disclosure from all contests hosted by the same seeker in the year preceding contest i as the IV. Similarly, for the second problematic variable, the latitude of rejection, we employed the average latitude of rejection in seeker i’s previous contests within the past year as the IV. Because these IVs are derived from SGI in historical contests, they should not directly influ ence the focal contest’s performance, but they should significantly affect the focal contest’s SGI framing because of the seeker’s consistent information generation behaviors and language habits. These IVs thus satisfy the exclusion restriction.

Additionally, the framing of SGI can be influenced by intrinsic contest characteristics (Wu et al. 2024). For example, contests with greater complexity may prompt seekers to provide more requirement-related feedback to clarify their specifications in greater detail. To alleviate endogeneity concerns arising from the potential influence of unobserved contest characteristics, we include an additional set of IVs based on similar contests. Contests with similar attributes are likely to share intrinsic characteristics and thus require similar information. We calculate contest similarity based on attributes such as required skill tags, guaranteed payment status, prize amount, duration, seeker experience, and entry day using cosine distance. For each contest, we selected the 30 most similar historical contests as peers and calculated the average extent of preference disclosure and latitude of rejection among these peers, using these averages as IVs for the focal contest. Because these IVs are derived from previously completed similar contests, they should not directly influence the focal contest’s performance, thereby satisfying the exclusion restriction.

Table 7. Findings From Alternative Estimation Methods

<table><tr><td>Variables</td><td>PSM(1)</td><td>Control-function(2)</td><td>Control-function with nonlinear submission control(3)</td><td>Seeker fixed-effect model(4)</td></tr><tr><td>Log of extent of preference disclosure</td><td>0.126***(0.0196)</td><td>0.332***(0.0143)</td><td>0.289***(0.0142)</td><td>0.061***(0.0235)</td></tr><tr><td>Log of latitude of rejection</td><td>0.300**(0.0850)</td><td>0.113*(0.0645)</td><td>0.132**(0.0649)</td><td>0.344***(0.0651)</td></tr><tr><td>Log of extent of preference disclosure × Day_left</td><td>-0.022***(0.0050)</td><td>-0.045***(0.0028)</td><td>-0.041***(0.0027)</td><td>-0.046***(0.0038)</td></tr><tr><td>Log of latitude of rejection × Day_left</td><td>-0.083***(0.0221)</td><td>-0.081***(0.0179)</td><td>-0.098***(0.0181)</td><td>-0.064***(0.0177)</td></tr><tr><td>Number of new submissions</td><td></td><td></td><td>0.013***(0.002)</td><td></td></tr><tr><td>Square of number of new submissions</td><td></td><td></td><td>-0.000***(0.000)</td><td></td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Pseudo- $R^2$ </td><td>0.310</td><td>0.243</td><td>0.261</td><td></td></tr><tr><td>Aic</td><td>35,862.738</td><td>105,601.88</td><td>103,068.86</td><td>33,289.021</td></tr><tr><td>Bic</td><td>36,011.11</td><td>105,794.38</td><td>103,269.07</td><td>33,444.561</td></tr><tr><td>Number of observations</td><td>8,650</td><td>16,322</td><td>16,322</td><td>12,169</td></tr></table>

Notes. Standard errors are in parentheses. Controls include Day\_left, average ratings, guaranteed, log of seeker reviews, log of existing solvers, log of solver clarification questions, log of seeker experience, prize, contest duration, log of average solver capability, number of competing contests, log of average review politeness.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

To address endogeneity, we adopt a two-stage control function approach, commonly used for endogeneity issues in nonlinear models (Villas-Boas and Winer 1999, Ducarroz et al. 2016, Jian et al. 2019). In the first stage, we use the IVs along other control variables to construct functions for each endogenous variable (Wooldridge 2015), which in our case are the extent of preference disclosure and the latitude of rejection. The coefficients of the IVs are highly significant (as shown in Table E.2 in Online Appendix E), indicating that our IVs have a strong impact on the endogenous variables. We conduct various tests to validate the instrumental variables. The Kleibergen-Paap rk Wald F statistic is 149.479, and the Cragg-Donald Wald F statistic is 634.364, both of which pass the weak instrumental variable test (Stock and Yogo 2005). KS statistics further suggest that the instrumental variables also satisfy the exclusion restriction test (D’Haultfoeuille et al. 2021). In the second stage, we include the residuals from the first stage as additiona regressors in the main model. The results, displayed in column (2) of Table 7, indicate that the findings in the main model remain consistent.

## 5.5. Ruling Out Effects from Solvers’ Submissions

SGI can be influenced by solvers’ submissions and questions because seekers often tailor their information in response to these dynamics. Consequently, SGI framing may vary depending on solvers’ submissions and questions. For instance, a higher number of solver submissions may prompt seekers to provide more feedback.

Our matching in Section 5.3 could help address this issue. As we explained earlier, we match contests on a daily basis, ensuring that contests are not only similar in contest attributes and seeker characteristics but also comparable in participation factors that may influence review provision. For example, when matching a contest with a review on day t, we ensure that it has a similar number of solvers and questions as a contest without a review on the same day. This approach helps mitigate differences in potential participation factors that could affect reviews.

Beyond the matching approach, we employ an alternative method to further address this issue. Solver submission patterns may not be linear throughout the contest, and their effects on SGI may also follow a nonlinear pattern. To account for this, we include both the number of new submissions and its square term in our control function models. Thus, in the first-stage equation, along with the IVs and control variables, we incorporate these submission-related variables.

These variables may also impact new solver participation because the behavior of existing solvers can influence the decisions of potential new solvers. Therefore, we include these variables in our second-stage estimation as well. We estimate the model using the control function approach and present the findings in column (3) of Table 7.

## 5.6. Unobserved Factors

Unobserved seeker characteristics (e.g., a seeker’s reputation or online presence) may systematically influence solver participation, potentially attracting or deterring sol vers. To mitigate the impact of these unobserved seekerlevel factors, we employ a seeker fixed-effects model. This approach explicitly accounts for time-invariant heteroge neity across seekers, ensuring that our estimates are not biased by the above unobserved characteristics. The results of the fixed-effects model, presented in column (4) of Table 7, remain consistent with our main results.

## 6. Findings and Discussion

The findings remain consistent across different estimation methods, including Poisson regression, control function approach, and propensity score matching (Tables 6 and 7). Our results provide key insights into the impact of SGI framing on solver participation over time.

From Table 6, we observe that the coefficient of Log of extent of preference disclosure is 0.055 and is significant at 1% level, supporting H1. Our findings indicate that the overall effect of the extent of preference disclosure is signifi cantly positive. This positive effect underscores that providing more extensive preference disclosure generally attracts more participants. Preference keywords, which offer detailed guidance, likely help solvers better understand and meet the seeker’s expectations, thereby reducing their uncertainty and minimizing trial-and-error costs. This finding aligns with the rational decision-making framework, which suggests that solvers are more likely to join contests with lower costs and higher probabilities of winning.

However, the positive effect is moderated by the number of remaining days. Across all the estimation methods (Tables 6 and 7), the coefficients for the interaction term between the extent of preference disclosure and the number of the remaining days are negative and significant. Our findings support H2, indicating that as contests approach their deadline, the positive impact of preference disclosure becomes more pronounced.

We further find that, although the overall effect of the latitude of rejection is positive, it is not statistically significant, leading to the rejection of H3. However, all models (Tables 6 and 7) indicate that the interaction between the latitude of rejection and the number of remaining days is negative, supporting H4. Specifically, for contests with more than three days remaining, the latitude of rejection has a significantly negative impact on the number of new solvers. However, as contests approach closure (i.e., fewer than three days remaining), the negative effects reverse, becoming positive. Overall, the negative effect of latitude of rejection in the early stage is offset by its positive effect in the later stage, resulting in an insignificant net effect.

Our findings provide evidence that both CLT and the latitude of rejection influence solvers’ decision-making. Clear and precise rejection criteria help solvers understand the boundaries within which they need to operate, allowing them to tailor their efforts and avoid immediate rejections. However, this positive effect is significant only when the deadline is near. When the deadline is far away, the latitude of rejection can overshadow other important factors, such as solvers’ need for exploration, which is their primary focus in the early stage. According to CLT, solvers are more likely to consider broader strategies and engage in exploratory behavior when the deadline is distant. Excessive rejections during this phase can constrain solvers’ exploration, potentially reducing creativity and innovation. As contests progress, solvers shift their focus from abstract exploration to detail-oriented tasks. During this phase, clear rejection criteria provide valuable guidance, helping solvers narrow their focus within acceptable bounds and enhancing participation. This shift in focus, as explained by CLT, accounts for the changing impact of latitude of rejection throughout the contest duration.

Overall, our findings support the construal level theory (CLT) and confirm that solvers’ focus shifts as the temporal distance decreases. When the deadline is distant, solvers are more likely to engage in high-level explorations rather than focusing on specific details. At this stage, extensive preference disclosures or an overly restrictive rejection approach can limit designers’ creative freedom, hindering their ability to explore novel and innovative solutions. As the contest progresses and the deadline approaches, solvers engage in more concrete thinking, focusing on specific requirements and clearly rejecting criteria to refine their submissions.

## 7. Robustness Checks

To assess the robustness of our findings, we conducted analyses incorporating additional controls and alternative measures for key variables.

First, we acknowledge the limitation that we cannot observe the exact day that solvers decide to enter a contest, and we use their first submission date as a proxy. In the main model, we account for a one-day delay between solvers’ entry decisions and their submissions. However, to account for the possibility that solvers may require additional time to develop their solutions, we perform an additional robustness check using information lagged by two days—that is, information posted two days before their submission date. The results, presented in column (1) of Table 8, remain consistent with our main findings.

Besides, the main analysis relies on the assumption that solvers participating on the same day observe the same SGI. However, there is a time lag between early and late submission on the same day, resulting in different SGI exposure for solvers joining at different times of the day. To address this, we use a shorter time lag by considering SGI in every eight-hour interval instead of the original one-day lag in the main analysis. The results are presented in column (2) of Table 8, and the findings are consistent with our main results.

Second, competition is often associated with the intensity of high-rated submissions. Our current measurement (average ratings) may not directly capture the intensity of competition within the top-tier submissions. Therefore, we use the number of submissions with very high ratings (e.g., higher than 4 stars out of 5 stars) as an alternative control of competition intensity. The results are presented in column (3) in Table 8, and the findings remain consistent.

Third, we further account for the potential impact of information length by incorporating additional controls. Specifically, we included the word counts of the three forms of information (i.e., descriptions, clarifications, and reviews) as control variables. The results, displayed in Column (4) of Table 8, remain consistent with our main findings.

Fourth, we use alternative measures for information framing. In the main analysis, we used the total number of preference keyword occurrences, assuming that each occurrence may imply different requirements and serve as a proxy for preference cues. However, the same requirements may be repeated. In such cases, using the total number of occurrences of all preference keywords may capture redundant requirements. To mitigate this issue, we apply an alternative measure, the number of unique preference keywords appearing in descriptions, reviews, and clarifications, and then repeat the analysis. Our findings (column (5) of Table 8) remain consistent across different measures of preference.

Fifth, we considered an alternative measure of the dependent variable. In the main analysis, we used the incremental number of new solvers to measure solver participation. However, a single solver can submit multiple solutions, which increases the variety of solutions. Therefore, we use the incremental number of new solutions from new solvers as an alternative measure. The results using this new dependent variable are presented in column (6) of Table 8, and they are consistent with our main findings.

Table 8. Findings for Robustness Checks

<table><tr><td>Variables</td><td>Lagged 2 days (1)</td><td>Lagged 8 hours (2)</td><td>Number of very high ratings (3)</td><td>Information length (4)</td><td>Unique preference keywords (5)</td><td>Incremental number of new solutions from new solvers (6)</td><td>Ratio of days left (7)</td><td>Solver-level fixed effect model (8)</td></tr><tr><td>Log of unique preference keywords</td><td></td><td></td><td></td><td></td><td>0.144*** (0.0138)</td><td></td><td></td><td></td></tr><tr><td>Log of preference keywords</td><td>0.275*** (0.0177)</td><td>0.1418*** (0.0183)</td><td>0.175*** (0.0127)</td><td>0.182*** (0.013)</td><td></td><td>0.118*** (0.0089)</td><td>0.2346*** (0.0142)</td><td>0.130*** (0.0159)</td></tr><tr><td>Log of latitude of rejection</td><td>0.243** (0.0988)</td><td>0.1183*** (0.0218)</td><td>0.233*** (0.0598)</td><td>0.240*** (0.059)</td><td>0.235*** (0.0596)</td><td>0.114** (0.0446)</td><td>0.2966*** (0.0649)</td><td>0.105* (0.0635)</td></tr><tr><td>Log of unique preference keywords × Day_left</td><td></td><td></td><td></td><td></td><td>-0.021*** (0.0028)</td><td></td><td></td><td></td></tr><tr><td>Log of preference keywords × Day_left</td><td>-0.040*** (0.0033)</td><td>-0.0244*** (0.0035)</td><td>-0.026*** (0.0026)</td><td>-0.026*** (0.0025)</td><td></td><td>-0.012*** (0.0018)</td><td></td><td>-0.012*** (0.0032)</td></tr><tr><td>Log of latitude of rejection × Day_left</td><td>-0.089** (0.0278)</td><td>-0.0216*** (0.0039)</td><td>-0.069*** (0.0171)</td><td>-0.058*** (0.0168)</td><td>-0.070*** (0.017)</td><td>-0.042*** (0.0122)</td><td></td><td>-0.036** (0.018)</td></tr><tr><td>Log of preference keywords × Ratio of day left</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.2907*** (0.0207)</td><td></td></tr><tr><td>Log of latitude of rejection × Ratio of day left</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.6471*** (0.1385)</td><td></td></tr><tr><td>Average ratings</td><td>-0.209*** (0.0063)</td><td>-0.064*** (0.005)</td><td></td><td>-0.159*** (0.0046)</td><td>-0.170*** (0.0046)</td><td>-0.179*** (0.0031)</td><td>-0.1648*** (0.0046)</td><td>-0.193*** (0.0056)</td></tr><tr><td>Number of very positive rating</td><td></td><td></td><td>-0.002 (0.0058)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Length of descriptions/ clarifications/reviews</td><td></td><td></td><td></td><td>Yes</td><td></td><td></td><td></td><td></td></tr><tr><td>Time effect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Pseudo-R2</td><td>0.3652</td><td>0.2604</td><td>0.226</td><td>0.238</td><td>0.236</td><td>0.276</td><td>0.235</td><td>0.068</td></tr><tr><td>Aic</td><td>72,439.674</td><td>154,846.85</td><td>107,952.28</td><td>106,341.77</td><td>106,602.95</td><td>235,733.04</td><td>106,780.42</td><td>439,006.88</td></tr><tr><td>Bic</td><td>72,613.176</td><td>155,049.22</td><td>108,129.38</td><td>106,534.27</td><td>106,780.05</td><td>235,910.14</td><td>106,957.53</td><td>439,313.06</td></tr><tr><td>Number of observations</td><td>13,955</td><td>48,966</td><td>16,322</td><td>16,322</td><td>16,322</td><td>16,322</td><td>16,322</td><td>8,181,057</td></tr></table>

Notes. Standard errors are in parentheses. Controls include Day\_left, average ratings, guaranteed, log of seeker reviews, log of existing solvers, log of solve clarification questions, log of seeker experience, prize, contest duration, log of average solver capability, number of competing contests, log of average review politeness $^ { * } p < 0 . 1 ; ^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1 .$

Sixth, we validate our model using an alternative measure for the moderator variable. In our main analysis, we used the number of remaining days to capture the time pressure perceived by solvers. However, because contests vary in duration, the same number of remaining days may impose different levels of time pressure, depending on the total contest duration. To address this, we used the ratio of days left as an alternative moderator. The results, presented in column (7) of Table 8, remain consistent with our main findings.

Lastly, to provide additional empirical evidence on whether SGI influences prospective solvers, we explicitly examine how their joining decisions are influenced by SGI. Specifically, we conduct a granular analysis at the solver-contest-day level, investigating how a solver’s decision to join task j on day t is influenced by the SGI available for task j as of day (t � 1). We construct solver i’s consideration set by identifying all contests available on day t and define the solver’s join decision among all these contests as a binary variable. For each contest j in the set of k available contests on day t, if solver i joins contest j on day t, then the variable takes a value of 1; otherwise, it takes a value of 0. We estimate this model using a solver fixed-effects logit regression, incorporating the same set of variables as in Equation (1). The coefficients of SGI capture the extent to which SGI influences solver i’s joining decisions. The results, presented in Column (8) of Table 8, further confirm that solvers’ joining decisions are influenced by SGI, reinforcing the findings obtained from the contest-day level analysis.

## 8. Conclusions

The number of solvers is vital to the open innovation ecosystem. This study considers the dynamic nature of contests and examines the effects of SGI framing on the daily influx of new solvers as well as how these effects vary with the number of remaining days in a contest. Our findings demonstrate that providing extensive preference keywords increases the influx of new solvers. However, the positive effect of preference disclosure varies over the contest duration. As the deadline approaches, more preference specifications become even more effective in boosting participation. Meanwhile, the latitude of rejection initially exerts a negative impact when solvers have ample time to develop solutions, but its effect turns positive as the deadline nears.

This study contributes to the literature on open innovation contests. First, it extends the existing research on solver participation in the open innovation contests. Prior research has examined primarily how reviews affect the participation of existing solvers, particularly their subsequent submissions. However, this study accounts for the dynamic nature of contests by investigating how SGI influences the participation of potential solvers. To the best of our knowledge, this is one of the first studies to examine the impact of intermediate SGI on the entry of new solvers.

Second, this study advances the literature on information in open innovation contests by introducing a new dimension: SGI framing. Existing research on SGI focuses primarily on the sentiment and volume of reviews and ratings. The few studies on textual SGI have explored different types of reviews and the specifications in descriptions. However, seekers provide additional types of information throughout the contest, including clarifications, which remain underexplored. This study conducted a comprehensive examining of SGI by considering multiple forms of SGI (descriptions, reviews, and clarifications), heterogeneous framing (the extent of preference disclosure and the latitude of rejection), and their tempora effects. The findings underscore the dynamic influence of SGI framing on solver decision-making across different contest stages.

Lastly, this study integrates the theory of latitude of rejection and construal level theory (CLT) within the rational decision-making framework. It employs various text-mining techniques to assess how seekers define the boundaries of their rejections. Our findings provide more empirical evidence on the better understanding of evaluation latitude within open innovation contexts.

This study provides important implications for all stakeholders in the open innovation ecosystem. First, the findings provide insights for seekers on how to strategically frame SGI to attract solvers at different stages of a contest. The results highlight the importance of considering the temporal dimension when managing SGI, because information that may deter solvers early in the contest could become more attractive as the contest progresses. In the early stages, excessive detail may constrain solvers’ exploration and discourage participation. Therefore, seekers should focus on fostering an environment that promotes exploration and creative freedom. As the deadline approaches, the focus should shift toward providing clear guidance and boundaries to help solvers align their solutions with specific requirements. At this stage, detailed preferences and welldefined rejection boundaries become more valuable in attracting solvers.

This research also offers valuable insights into the design of information on open innovation platforms. The findings suggest that these platforms should be structured to reduce solver uncertainty by ensuring that relevant information is publicly accessible and presented in effective forms. For example, this study highlights that textual information can convey rich details. Platforms that currently rely solely on ratings should consider incorporating textual feedback options. Additionally, clarifications serve as a crucial form of information. Platforms lacking this feature should enable seekers to provide further classifications for solvers. Furthermore, platforms should enhance the accessibility of SGI by facilitating efficient information extraction. For example, they could generate reference indices for solvers, such as sentiment scores, the number of design elements mentioned in SGI, or certitude scores reflecting the certainty of seekers’ feedback.

This study underscores the importance of reading SGI because it helps solvers assess uncertainties before entering contests. New solvers, in particular, need to develop strategies to mitigate uncertainty and make informed contest selection decisions. The findings provide actionable guidelines for solvers on these platforms. For instance, solvers should actively review seekers’ clarifications and reviews to gain insights into contest expectations and reduce ambiguity. They should also pay particular attention to the framing of information, such as the degree of certainty with which seekers reject specific design elements.

This study had some limitations. First, it does not explicitly capture how solvers process information in a dynamic environment. Future studies could conduct experiments to examine how individual solvers interpret SGI framing and subsequently make contest selection decisions. Furthermore, other potential dimensions of SGI framing may warrant investigation to assess their impact on solver behavior.

## Acknowledgments

The authors thank the senior editor, the associate editor, and three anonymous reviewers for their constructive feedback throughout the review process. Jiahui Mo and Nila Zhang contributed equally and are joint first authors.

## Endnotes

<sup>1</sup> We monitored 106 contests over two weeks, and only six contests updated their descriptions. The update rate of descriptions is esti mated to be approximately 6%.

<sup>2</sup> The public clarification area allows solvers to ask questions and enables seekers to provide clarifications. We consider only clarifications generated by seekers in the public clarification area as SGI.

## References

Afuah A, Tucci CL (2012) Crowdsourcing as a solution to distant search. Acad. Management Rev. 37(3):355–375.

Amabile TM (1988) A model of creativity and innovation in organi zations. Res. Organ. Behav. 10(1):123–167.

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Basten U, Biele G, Heekeren HR, Fiebach CJ (2010) How the brain integrates costs and benefits during decision making. Proc. Natl. Acad. Sci. USA 107(50):21767–21772.

Bockstedt J, Druehl C, Mishra A (2016) Heterogeneous submission behavior and its implications for success in innovation contests with public submissions. Production Oper. Management 25(7): 1157–1176.

Boe¨nne M, Leten B, Van Dyck W (2023) Does constructive feedback improve idea quality in idea contests? Exploring the role of hierarchy and feedback overlap. R & D Management 53(3): 345–363.

Boudreau KJ, Lacetera N, Lakhani KR (2011) Incentives and prob lem uncertainty in innovation contests: An empirical analysis. Management Sci. 57(5):843–863.

Boston Consulting Group (2021) The 2021 most innovative companies report. Accessed December 2021, https://www.bcg.com/ en-us/publications/2021/most-innovative-companiesoverview.

Boyd RL, Ashokkumar A, Seraj S, Pennebaker JW (2022) The Development and Psychometric Properties of LIWC-22 (University of Texas at Austin, Austin), 1–47.

Camacho N, Nam H, Kannan PK, Stremersch S (2019) Tournaments to crowdsource innovation: The role of moderator feedback and participation intensity. I. Marketing 83(2):138–157.

Chen P-Y, Pavlou P, Wu S, Yang Y (2021) Attracting high-quality contestants to contest in the context of crowdsourcing contest platform. Production Oper. Management 30(6):1751–1771.

Cheng A, Baumgartner H, Meloy MG (2021) Identifying picky shoppers: Who they are and how to spot them. J. Consum. Psychol. 31(4):706–725.

Das SR, Chen MY (2007) Yahoo! For amazon: Sentiment extraction from small talk on the web. Management Sci. 53(9):1375–1388.

DeFond M, Erkens DH, Zhang J (2017) Do client characteristics really drive the Big N audit quality effect? New evidence from propensity score matching. Management Sci. 63(11):3628–3649.

D’Haultfoeuille X, Hoderlein S, Sasaki Y (2021) Testing and relaxing the exclusion restriction in the control function approach. J. Econometrics 240(2):105075.

Ducarroz C, Yang S, Greenleaf EA (2016) Understanding the impact of in-process promotional messages: An application to online auctions. J. Marketing 80(2):80–100.

Eagly AH, Kulesa P (1997) Attitudes, attitude structure, and resistance to change: Implications for persuasion on environmental issues. Bazerman MH, Messick DM, Tenbrunsel AE, WadeBen zoni KA, eds. Environment, Ethics, and Behavior: The Psychology of Environmental Valuation and Degradation (New Lexington, San Francisco), 122–153.

Entman RM (1993) Framing: Toward clarification of a fractured paradigm. J. Communication 43(4):51–58.

Erat S, Krishnan V (2012) Managing delegated search over design spaces. Management Sci. 58(3):606–623.

Fazio RH, Zanna MP (1978) On the predictive validity of attitudes: The roles of direct experience and confidence. J. Personality 46(2):228–243.

Granberg D (1982) Social judgment theory. Burgoon M, ed. Communication Yearbook, vol. 6 (Sage, Beverly Hills, CA), 304–329.

Gross DP (2017) Performance feedback in competitive product development. RAND J. Econom. 48(2):438–466.

Hameiri B, Idan O, Nabet E, Bar-Tal D, Halperin E (2020) The paradoxical thinking ‘sweet spot’: The role of recipients’ latitude of rejection in the effectiveness of paradoxical thinking messages targeting anti-refugee attitudes in Israel. J. Soc. Polit. Psych. 8(1):266–283.

Han E (2022) What is design thinking and why is it important. Harvard Bus. School (January 18), https://online.hbs.edu/blog/ post/what-is-design-thinking

Hart S, Hultink EJ, Tzokas N, Commandeur HR (2003) Industrial companies’ evaluation criteria in new product development gates. J. Product Innov. Management 20(1):22–36.

Hong Y, Peng J, Burtch G, Huang N (2021) Just DM me (politely): Direct messaging, politeness, and hiring outcomes in online labor markets. Inform. Systems Res. 32(3):786–800.

Hu M, Liu B (2004) Mining and summarizing customer reviews. Proc. Tenth ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 168–177.

Indurkhya N, Damerau FJ (2010) Handbook of Natural Language Processing (Chapman and Hall/CRC, New York).

Jian L, Yang S, Ba S, Lu L, Jiang C (2019) Managing the crowds: The effect of prize guarantees and in-process feedback on participation in crowdsourcing contests. MIS Quart. 43(1):97–112.

Jiang Z, Huang Y, Beil DR (2021) The role of problem specification in crowdsourcing contests for design problems: A theoretical and empirical analysis. Manufacturing Service Oper Management 23(3):637–656.

Jiang Z, Huang Y, Beil DR (2022) The role of feedback in dynamic crowdsourcing contests: A structural empirical analysis. Man agement Sci. 68(7):4858–4877.

Karau SJ, Kelly JR (1992) The effects of time scarcity and time abundance on group performance quality and interaction process. J. Experiment. Soc. Psych. 28(6):542–571.

Koh TK (2019) Adopting seekers’ solution exemplars in crowdsourcing ideation contests: Antecedents and consequences. Inform. Systems Res. 30(2):486–506.

Krippendorff K (1980) Validity in content analysis, chapter 1. Mochmann E, ed. Computerstrategien Fu¨ r Die Kommunikationsanalyse (Campus, Frankfurt/New York), 69–112.

Krishnamurthy P, Carter P, Blair E (2001) Attribute framing and goal framing effects in health decisions. Organ. Behav. Hum. Decis. Process 85(2):382–399.

Kyung N, Chan J, Lim S, Lee B (2024) Contextual targeting in mHealth Apps: Harnessing weather information and message framing to increase physical activity. Inform. Systems Res. 35(3): 1034-1051

Lakhani KR, Lifshitz-Assaf H, Tushman M (2013) Open innovation and organizational boundaries: Task decomposition, knowledge distribution and the locus of innovation, chapter 19. Grandori A, ed. Handbook of Economic Organization: Integrating Economic and Organization Theory (Elgar, Northampton, MA), 355–382.

Liberman N, Trope Y (1998) The role of feasibility and desirability considerations in near and distant future decisions: A test of temporal construal theory. J. Personality Soc. Psychol. 75(1):5–18.

Locke EA, Latham GP (2002) Building a practically useful theory of goal setting and task motivation: A 35-year odyssey. Amer. Psychol. 57(9):705–717.

Martinsuo M, Poskela J (2011) Use of evaluation criteria and innovation performance in the front end of innovation. J. Product Innovation Management 28(6):896–914.

Mo J, Sarkar S, Menon S (2021) Competing tasks and task quality: An empirical study of crowdsourcing contests. MIS Quart. 45(4):1921–1948.

Petty RE, Cacioppo JT (1986) Communication and Persuasion: Central and Peripheral Routes to Attitude Change (SpringerVerlag, New York).

Petty RE, Krosnick JA (2014) Attitude Strength: Antecedents and Consequences (Psychology Press, New York).

Riet JVT, Ruiter RA, Werrij MQ, De Vries H (2008) The influence of self-efficacy on the effects of framed health messages. Eur. J. Soc. Psych. 38(5):800–809.

Rothman AJ, Bartels RD, Wlaschin J, Salovey P (2006) The strategic use of gain-and loss-framed messages to promote healthy behavior: How theory can inform practice. J. Communication 56(Suppl\_1):S202–S220.

Sanyal P, Ye S (2024) An examination of the dynamics of crowd sourcing contests: Role of feedback type. Inform. Systems Res. 35(1):394–413.

Schenk E, Guittard C (2011) Towards a characterization of crowd sourcing practices. J. Innovation Econom. 1(7):93–107.

Schleicher DJ, Smith TA, Casper WJ, Watt JD, Greguras GJ (2015) It’s all in the attitude: The role of job attitude strength in job attitude–Outcome relationships. J. Appl. Psychol. 100(4):1259–1274.

Schultz P, Zaman M (2001) Do the individuals closest to internet firms believe they are overvalued. J. Financial Econom. 59(3): 347–381.

Sherif M, Hovland CI (1961) Social Judgment (Yale University Press, New Haven, CT).

Simon HA (1955) A behavioral model of rational choice. Quart. J. Econom. 69(1):99–118.

Socher R, Perelygin A, Wu JY, Chuang J, Manning CD, Ng AY, Potts C (2013) Recursive deep models for semantic compositionality over a sentiment treebank. Proc. Conf. Empirical Meth ods Natural Language Processing (EMNLP) (Association for Computational Linguistics (ACL), Kerrville, TX), 1631–1642.

Stock J, Yogo M (2005) Asymptotic distributions of instrumental variables statistics with many instruments. Andrews DWK, Stock JH, eds. Identification and Inference for Econometric Models: Essays in Honor of Thomas Rothenberg, vol. 6 (Cambridge Univer sity Press, Cambridge, UK), 109–120.

Terwiesch C, Xu Y (2008) Innovation contests, open innovation, and multiagent problem solving. Management Sci. 54(9):1529–1543.

Trope Y, Liberman N (2003) Temporal construal. Psychol. Rev 110(3):403–421.

Trope Y, Liberman N (2010) Construal-level theory of psychological distance. Psychol. Rev. 117(2):440–463.

Tucker JW (2010) Selection bias and econometric remedies in accounting and finance research. J. Accounting Literature 29(1): 31–57.

Waller MJ, Zellmer-Bruhn ME, Giambatista RC (2002) Watching the clock: Group pacing behavior under dynamic deadlines. Acad. Management J. 45(5):1046–1055.

Wooldridge JM (2015) Control function methods in applied econo metrics. J. Human Resources 50(2):420–445.

Wooten JO, Ulrich KT (2017) Idea generation and the role of feedback: Evidence from field experiments with innovation tourna ments. Production Oper. Management 26(1):80–99.

Wu X, Chen Y, Zhang N (2023) The impact of politeness in bidding descriptions on hiring decisions in online labor markets. Proc. 2023 Pacific Asia Conf. Inform. Systems (Association for Information Systems, Atlanta), 74.

Wu S, Liu Q, Zhao X, Sun B, Liao X (2024) Attracting solvers’ participation in crowdsourcing contests: The role of linguistic signals in task descriptions. Inform. Systems J. 34(1):6–38.

Vargo SL, Lusch RF (2017) Consumers’ evaluative reference scales and social judgment theory: A review and exploratory study. Rev. Marketing Res. 1:245–284.

Villas-Boas JM, Winer RS (1999) Endogeneity in brand choice mod els. Management Sci. 45(10):1324–1338.

Ye HJ, Kankanhalli A (2017) Solvers’ participation in crowdsourcing platforms: Examining the impacts of trust, and benefit and cost factors. J. Strategic Inform. Systems 26(2):101–117.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
