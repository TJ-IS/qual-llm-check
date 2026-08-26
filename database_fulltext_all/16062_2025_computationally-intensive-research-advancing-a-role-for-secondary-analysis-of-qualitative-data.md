---
otero_id: 16062
otero_key: "E5BN4VCK"
title: "Computationally Intensive Research: Advancing a Role for Secondary Analysis of Qualitative Data"
authors: "Kaveh Mohajeri; Amir Karami"
year: "2025"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00923"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
2025

# Computationally Intensive Research: Advancing a Role for Secondary Analysis of Qualitative Data

Kaveh Mohajeri , k.mohajeri@ieseg.fr

Amir Karami

, karami@uab.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Computationally Intensive Research: Advancing a Role for Secondary Analysis of Qualitative Data

Kaveh Mohajeri,<sup>1</sup> Amir Karami<sup>2</sup>

<sup>1</sup>IESEG School of Management, France, k.mohajeri@ieseg.fr <sup>2</sup>Collat School of Business, University of Alabama at Birmingham, USA, karami@uab.edu

## Abstract

This paper draws attention to the potential of computational methods in reworking data generated in past qualitative studies. While qualitative inquiries often produce rich data through rigorous and resource-intensive processes, much of this data often remains unused. In this paper, we first make a general case for secondary analysis of qualitative data by discussing its benefits, distinctions, and epistemological aspects. We then argue for opportunities with computationally intensive secondary analysis, highlighting the possibility of drawing on data assemblages spanning multiple contexts and time frames to address cross-contextual and longitudinal research phenomena and questions. We propose a scheme to perform computationally intensive secondary analysis and advance ideas on how this approach can help facilitate the development of innovative research designs. Finally, we enumerate some key challenges and ongoing concerns associated with qualitative data sharing and reuse.

Keywords: Secondary Analysis of Qualitative Data, Computationally Intensive Research, Computational Methods, Digital Trace Data

Dirk S. Hovorka was the accepting senior editor. This research perspecives article was submitted on January 3, 2023, and underwent two revisions.

## 1 Introduction

In their MIS Quarterly editorial on computationally intensive research, Miranda et al. (2022) aptly observed that “method choices are only loosely coupled to the [type of] data” (p. viii). Numerous studies within the IS field and beyond demonstrate that computational methods can effectively analyze various types and formats of data, including quantitative and qualitative trace data drawn from digital environments, census data, textual documents, images, and videos (e.g., Bahmanyar et al., 2018; Goldberg, 2011; Lindberg et al., 2016). Still, computationally intensive research dealing with qualitative data often focuses on “found” data, such as digital trace data (Berente et al., 2019; Howison et al., 2011; Sarkar, 2021), academic publications (e.g., Larsen et al., 2008; Mortenson & Vidgen, 2016), and organizational documents or reports (e.g., Harrison et al., 2019; Huang et al., 2018). While studies have long hinted at the potential for computational analysis of data generated through qualitative studies (e.g., Indulska et al., 2012), few, if any, have pursued this approach, at least as far as the IS scholarship is concerned. Furthermore, the epistemological and methodological issues of applying computational methods in this context remain underexplored.

Data generated through qualitative studies (e.g., interview transcripts, open-ended survey responses, field notes, and research diaries) are precious materials, typically produced through rigorous, resource-intensive processes and usually accompanied by documented inquiry methods. However, qualitative researchers frequently note that much of their laboriously generated data may remain unused and that, often, only a portion is the subject of final analysis and publication (Davidson et al., 2019; Fielding & Fielding, 2000). Likewise, in the

IS field, we have long been aware that, for instance, the abundance of case studies represents a largely untapped pool of empirical evidence (Myers & Avison, 1997). Despite this, researchers may find it undesirable to utilize computational methods to help streamline their engagements with data generated through qualitative research. Due to specific epistemological justifications and traditions, committed qualitative researchers may still favor conventional, “manual” analysis when it comes to “deep data” research involving primary data (Davidson et al., 2019; Bruns, 2013). Concerns also exist about the applicability of computational methods. Most notably, logistical constraints in qualitative inquiries may cause primary data corpora to end up lacking the scale required for computational methods to yield reliable results, especially with more complex algorithms (Izonin & Tkachenko, 2022; Schmiedel et al., 2019; van Loon, 2022).

This Research Perspectives paper aims to draw attention to and contribute to a scholarly conversation about the potential of leveraging computational methods in analyzing data generated through qualitative studies and seeks to highlight how it can be a valuable addition to the practice of computationally intensive research. While computational methods can legitimately be worked out in certain conditions involving primary qualitative data (e.g., Durcikova et al., 2024), our focus in this paper is on opportunities with secondary analysis of qualitative data (hereafter, SAQD)—the computational reworking of data generated in previous qualitative studies, independent of and transcending the theoretical interests or even the scope of those studies. We begin by making a general case for SAQD in IS research. Next, we argue for computationally intensive SAQD (hereafter, CI-SAQD), contending that even more benefits can be gained from SAQD when it is augmented by computational techniques. This is particularly true when moving beyond an individual data set to analyze an assemblage of data sets spanning multiple contexts and time frames to theorize for cross-contextual or longitudinal issues that are beyond the foci of each constituent data set individually (Davidson et al., 2019). We provide an overview of some relevant computational methods and propose a specific scheme to conduct CI-SAQD. In addition, we explore how CI-SAQD can facilitate the development of innovative research designs. Finally, we briefly discuss some key ongoing challenges and limitations of research that relies on SAQD.

## 2 Making a Case for SAQD in IS Research

For much of the twentieth century, data reuse in social science research was primarily associated with quantitative data sets (Fielding, 2000; Goodwin, 2012; Heaton, 2004). Ideas and practices around qualitative data reuse were rare, with notable exceptions, such as Barney Glaser’s articles in the 1960s (Glaser, 1962,

1963). By the late 1990s, however, the landscape began to shift considerably, particularly in North America and the United Kingdom, where researchers increasingly recognized the significance of the “secondary analysis” of qualitative data previously generated through rigorous research designs and structuring (Heaton, 1998, 2004).

## 2.1 SAQD: Benefits and Distinctions

Although data generated in qualitative studies represents a vastly underutilized resource, many IS researchers may still question or be unaware of the benefits of using such data for new, secondary studies (see Skinner et al., 2022). Yet it must be noted that the significance of qualitative data sharing and its corollary, SAQD, has already been widely addressed based on several different grounds (e.g., Fielding & Fielding, 2000; Goodwin, 2012; Hammersley, 1997; Heaton, 2004; Hinds et al., 1997; Hughes et al., 2020; Mannheimer et al., 2019; Moore, 2007). In the following paragraphs, we discuss three primary arguments advocating the use of SAQD. Also, we differentiate SAQD from other well-known approaches, which involve analyzing secondary qualitative data or reviewing previous qualitative research.

The first primary argument for SAQD highlights cases where collecting primary data is overly cumbersome, if not infeasible or unjustifiable, yet reliance on data from qualitative fieldwork remains indispensable. Research on sensitive topics, hard-to-reach populations, or past events often makes primary data collection unreasonably difficult. There are also situations where researchers aim to avoid overburdening informants (Fielding, 2000; Heaton, 2004; Long-Sutehall et al., 2011; Mannheimer et al., 2019; Sandelowski, 1997). For instance, Bishop and Kuula-Luumi (2017) pointed to the health area as an incredibly fertile domain in terms of the range of sensitive topics with general appeal that have been approached through various genres of SAQD by using data from repositories such as the one provided and curated by healthtalk.org. One specific example in IS research that resonates well with this type of argument for SAQD relates to the research stream on algorithmically managed work. The literature shows that recruiting interviewees in specific algorithmically managed settings may involve notable challenges. For instance, Tarafdar et al. (2022) explained the difficulties involved in interviewing drivers working for ridesharing platforms (e.g., Uber, Lyft), as they often lack time due to demanding schedules and may be wary of being interviewed because of the frequent negative press coverage of ridesharing companies. In such cases, we believe data collected in earlier studies would constitute a valuable source of evidence worth systematically retaining and sharing for future secondary analyses.

The second argument for pursuing SAQD centers on the economy and sustainability of qualitative research. Collecting primary data can be “very resourceintensive and beyond the means of most social scientists who do not have access to significant sources of research funding” (Goodwin, 2012, p. xxii). There are also broader recognitions, maintaining that data sharing and reuse is particularly beneficial to encourage new research partnerships, promote research transparency, provide resources for student research, and “maximize the payoff of public investments in research and education” while imposing less of a burden on research subjects (Mannheimer et al., 2019, p. 644; Heaton, 2004; Bishop & Kuula-Luumi, 2017).

The third argument goes beyond logistical or practical concerns to underscore the substantive benefits of SAQD. Advocates argue that reusing qualitative data can foster new research questions/designs and enable innovative research to produce novel and impactful findings. As early as the 1960s, Glaser (1963) noted that secondary analysis by independent researchers “can lend new strength to the body of fundamental social knowledge” (p. 11). Subsequent scholars have also similarly emphasized SAQD’s potential (Fielding & Fielding, 2000; Hammersley, 1997; Heaton, 2004). Heaton (2004), for instance, suggested that SAQD “epitomizes the flexible character of qualitative research, enabling researchers to find innovative ways of using pre-existing data” (p. 71). She also explained that SAQD can be beneficial in salvaging data from primary work to address new/additional research questions or for research verification or refinement purposes. In the sociology domain, Fielding and Fielding (2000) showcased the potential of such a practice. They revisited a seminal study on prison life conducted by Cohen and Taylor (1972), demonstrating “support for an alternative, if complementary, conceptualisation, using archived data from the original study” (Fielding & Fielding, 2000, p. 671). Likewise, Weick et al. (2005) demonstrated SAQD in the organizational studies domain, leveraging interview data from a published clinical nursing study to illustrate key elements of their influential sensemaking framework. Data from multiple previous studies dealing with the same (or similar) population(s) can also be systematically leveraged to evaluate the generalizability of primary research findings. This can thus facilitate addressing what may be frequently perceived as a weakness of qualitative research (Hammersley, 1997). In addition, Hammersley (1997) drew attention to how, in general, qualitative data sharing and SAQD can open possibilities of wideranging comparative analysis.

These substantive benefits of SAQD continue to be echoed in more recent scholarship across disciplines such as political science (e.g., Elman et al., 2010; Kern & Mustasilta, 2023), health (e.g., Chatfield, 2020; Tate & Happ, 2018), and the social sciences (e.g., Courage, 2019). However, most notably, SAQD is increasingly valued for its potential to support longitudinal and crosscontextual theorizing. Scholars have emphasized the possibility of “scaling up”<sup>1</sup> across qualitative data sets from multiple studies that extend over different time frames and contexts (Davidson et al., 2019; Edwards et al., 2021; Mason, 2002). For instance, the Timescapes initiative (2007-2012), funded by the UK’s Economic and Social Research Council, demonstrated how longitudinal qualitative data archives can enable groundbreaking temporal research to explore “the lived experience of change and continuity in the social world” (Neale et al., 2012, p. 5).

In IS research, leveraging the richness of multiple qualitative studies to drive innovative theorizing and uncover novel perspectives is already an established practice, though through approaches other than SAQD (e.g., Rivard & Lapointe, 2012; Stafford & Farshadkhah, 2020; Tana et al., 2023). To clarify SAQD’s distinctiveness, it will thus be helpful to briefly compare it to other prominent approaches, specifically qualitative meta-synthesis (Hoon, 2013; Zimmer, 2006) and the case survey method (Larsson, 1993; Lucas, 1974).

SAQD is distinct in that it mainly relies directly on preexisting data rather than on research findings. This largely sets SAQD apart from approaches in the “review research” tradition, such as meta-analysis and metasynthesis (Kunisch et al., 2023), where the researcher often “analyzes the analyses” or “codes the codes” (Stafford & Farshadkhah, 2020) and seldom engages directly with the data itself (Heaton, 1998, 2004; Zimmer, 2006). Furthermore, qualitative meta-synthesis (and most other types of “review research”) typically requires substantial topic homogeneity between the studies being synthesized and the meta-synthesis itself (Zimmer, 2006). By contrast, SAQD can be independent of and completely transcend the theoretical interests or scopes of the primary studies, as exemplified in the supra-analysis type of SAQD (Heaton, 2004). Finally, SAQD studies primarily entail qualitative data analysis, distinguishing them from case survey studies. With the case survey method, researchers typically aim to study “many issues in many cases” (Larsson, 1993, p. 1515) through an essentially quantitative review of qualitative data (Jurisch et al., 2013), where the researcher follows a coding procedure of assigning numbers to different properties/features of the constituent case studies.

## 2.2 Epistemological Considerations

SAQD has sparked intense debates regarding the epistemology of qualitative research for over two decades (Vila-Henninger et al., 2022; Hammersley, 1997, 2010; Savage, 2005). The unease and debates around SAQD often reflect broader tensions between different qualitative research traditions or, more generally, between qualitative and quantitative approaches to social science research (Heaton, 2004; Bishop, 2007). For instance, the primary-versussecondary debate surrounding SAQD has been described as “a proxy for other debates: positivism/interactionism, realism/post-modernism, subjectivity/authorial authority, and even academic freedom/neo-managerialism” (Bishop, 2007, p. 53; also, see Moore, 2005).

Following Heaton (2004), we believe these epistemological debates may be best addressed by first examining different views on the relationship between qualitative and quantitative research. Bryman (1988) and Hammersley (1996) provided useful frameworks in this regard. Bryman (1988) distinguished between “epistemological” and “technical” perspectives, which align closely with Hammersley’s (1996) “paradigm loyalty” versus “methodological eclecticism” positions. The “epistemological” or “paradigm loyalty” view sees quantitative and qualitative research as fundamentally incompatible due to their incommensurable ontological and epistemological beliefs. In contrast, the “technical” or “methodological eclecticism” view emphasizes the practical rather than philosophical aspects of social inquiry. It considers the two quantitative and qualitative approaches complementary, having different strengths and weaknesses, and thus suitable for investigating different kinds of research questions. We observe that the latter view has become increasingly prevalent among IS scholars, who often embrace qualitative research as a broad church encompassing various paradigms (e.g., positivist, interpretive, critical, postmodern, etc.) and genres (Cecez-Kecmanovic & Kennan, 2013; Sarker et al., 2018).

The distinction between the two views outlined above is instrumental in understanding the two main sides of the debates over SAQD. Proponents often align with the “technical” or “methodological eclecticism” view, which Sarker et al. (2018) associated with a data-centric approach. Skeptics, however, tend to lean toward the “epistemological” or “paradigm loyalty” view, aligning more with an interpretation-centric approach (Sarker et al., 2018). Still, a closer examination needs to address the two sides’ positions regarding two fundamental issues: data “fit” and the issue of “not being there” (Heaton, 2004; Hughes et al., 2020; Vila-Henninger et al., 2022). Data “fit” concerns whether data from previous qualitative studies can be legitimately reused for new research purposes. The “not being there” issue raises questions about how the secondary researcher’s distance from the inquiry context might affect data interpretation.

On the issue of data “fit,” critics of SAQD often question the practice of treating qualitative data as a “reified neutral product” that can legitimately be divorced from the situated dynamics of its generation context and repurposed for secondary research (Hughes et al., 2020, p. 567; also, see Moore, 2007). Proponents, however, take a pragmatic stance, in line with the view of data as “representative facts or shared reality” (Sarker et al., 2018), thus supporting qualitative data reuse. The SAQD literature also suggests that data “fit” is not fixed but depends on factors such as the extent of missing data in the corpus, the alignment between primary and secondary research questions, and the suitability of the data’s nature, structure, and format for the intended secondary analysis methods (Hinds et al., 1997; Thorne, 1994).

Regarding the second issue, critics argue that meaningful qualitative analysis relies heavily on researchers’ prolonged, immersive contact with the field, a result of “being there” during data collection (Hughes et al., 2020, p. 566; also, see Mauthner & Parry, 2009, 2013). Proponents, however, tend to “challenge the notion that ‘remove’ from the original spatial, temporal and epistemic context of the production of ‘primary’ data is exclusively a form of deficit” (Hughes et al., 2020, p. 567, emphasis original; also, see Irwin & Winterton, 2011). In other words, the logic here is that opportunities for insight are not inextricably tied to the presence in the immediate data generation contexts; instead, certain observations become possible “precisely when we are not there ‘at the moment’” (Hughes et al., 2020, p. 567).

## 2.3 The Significance of SAQD for the IS Scholarship

Against the backdrop laid out above, we contend that SAQD should first and foremost be embraced in the IS field for its great potential to problematize long-held assumptions about qualitative inquiry, data, and the relationship between researchers and data. SAQD allows IS qualitative researchers to move beyond the traditional view that only what researchers produce as data through direct sensory engagement in specific social contexts is valuable. Instead, it highlights the further significance of what such data “when treated as particular kinds of evidence through specific forms of research engagement and apprehension can be used to say about the social world” (Hughes et al., 2020, p. 567). By reworking preexisting qualitative data, IS scholars can expand the contributions of past studies from merely their findings to what can be additionally unlocked through the reuse of their rich data sets (cf. Glaser, 1962). SAQD can also motivate IS researchers to adopt a bricoleur mindset (Heaton, 2004; cf. Denzin & Lincoln, 2011), leveraging diverse theoretical and analytical approaches while mining a wide array of qualitative data sets to explore novel or supplementary research questions. This completely aligns with the recurrent calls for more flexible, eclectic, and innovative research styles within IS and beyond.

Furthermore, it is encouraging that many epistemological and methodological concerns around qualitative data reuse have already been addressed through various research practices and strategies. For instance, to ensure data “fit,” secondary researchers are advised to draw on their prior familiarity with certain data sets. Another practice is moving away from treating qualitative data as “given” and adapting it to match the goals of the secondary analysis. Finally, a third practice is augmenting preexisting data sets with additional primary data (see Heaton, 2004). Likewise, to address the issue of “not being there,” one strategy is to deposit all relevant study documentation (e.g., field notes, research diaries, and other correspondence related to research execution) by primary researchers when archiving qualitative data (Corti & Thompson, 1998; Fink, 2000; Mannheimer et al., 2019). Another strategy is to consult with primary researchers, where possible, to gain deeper insights into the original work and become sensitized to the context of the primary study (Hinds et al., 1997).

## 3 Toward Computationally Intensive SAQD

Computational analysis of qualitative data has substantially impacted management and IS scholarship, enabling fresh approaches to theorizing and reexamining previously intricate problems and questions, especially with large-scale <sup>2</sup> data sets (Hannigan et al., 2019; Miranda et al., 2022). However, as stated earlier, computational methods are predominantly utilized for analyzing “found” qualitative data. This tendency can even be observed in the methodological thinking and texts that aim to justify computational methods (e.g., Schmiedel et al., 2019; Berente et al., 2019), where these methods are often positioned in contrast to or separate from “conventional” or “traditional” qualitative research that relies on, for instance, interview data. We posit that this division is unnecessarily restrictive, if not damaging. Data generated through qualitative studies, as with digital trace data and other types of “found” data, can yield valuable insights and help ambitious and innovative theorizing when analyzed computationally. This is where we introduce CI-SAQD: the integration of computational methods with secondary analysis of qualitative data.

While computational methods can be applied to primary qualitative data, integrating them with SAQD has unique advantages. SAQD enables the assembly of data sets from multiple studies, addressing the need for larger data corpora, which are often required for reliable computational analysis (Izonin & Tkachenko, 2022; van Loon, 2022). In addition, CI-SAQD can be even more effective than conventional SAQD for facilitating longitudinal and cross-contextual theorizing by computationally engaging with assemblages of multiple data sets spanning different time frames and contexts. This, in turn, can significantly enhance research richness and can yield substantive insights into social processes (Davidson et al., 2019). CI-SAQD can also facilitate certain research designs, incorporating multiple and various modes of theorizing with different data sets within a single study.

The following subsections provide an overview of computational methods relevant to CI-SAQD, propose a specific CI-SAQD scheme, and expound on how CI-SAQD can enable innovative research designs.

## 3.1 Overview of Relevant Computational Methods

Computational methods generally deal with two types of data: structured (organized and stored in tabular formats with rows and columns representing instances and features) and unstructured (lacking a standard shape or organization). Most qualitative data, such as interview transcripts, are unstructured, and researchers often rely on unsupervised<sup>3</sup> computational techniques to derive structured understandings and descriptions. In particular, topic modeling has been widely applied across various domains (e.g., Bybee et al., 2023; Greve et al., 2022; Karami et al., 2020b; Grisham et al., 2023). Topic models often rely on a particular computational foundation, such as linear algebra, probability, neural networks, or fuzzy clustering (Karami et al., 2020a; Abdelrazek et al., 2023). Four specific topic models are briefly reviewed below.

Latent semantic analysis (LSA) is a topic model that draws on linear algebra using singular value decomposition (SVD) to reduce the dimensionality of term-document matrices, uncovering hidden semantic structures in textual data (Deerwester et al., 1990). It has been applied in several domains, such as political science (e.g., Valdez et al., 2018), business (e.g., Lau et al., 2014), and health (e.g., Han & Choi, 2010). However, it is believed that LSA struggles with estimating the number of topics (or dimensions) and assigning topics to new, unseen documents, limiting its applicability (Blei et al., 2003; Abdelrazek et al., 2023; Zengul et al., 2023).

Latent Dirichlet allocation (LDA) is a probabilistic topic model, where each piece of unstructured data, such as a transcript, is assumed to contain multiple topics, each representing a collection of semantically related words. For instance, LDA might categorize terms like “data,” “number,” and “computer” under a topic, which can be labeled as “data analysis” (Blei, 2012; Blei et al., 2003; Boyd-Graber et al., 2017). LDA is widely applied to data sets of various scales across domains such as management, health, and politics (e.g., Boyd-Graber et al., 2017; Hannigan et al., 2019). It substantially facilitates assigning topics to new documents, enabling more straightforward interpretation and offering better performance than earlier models like LSA. However, LDA requires careful parameter tuning and can involve substantial human effort for interpretation (Rijcken et al., 2021).

Fuzzy latent semantic analysis (FLSA), based on fuzzy clustering, allows each data item to be assigned to multiple clusters (Karami et al., 2018). FLSA functions according to degrees of truth rather than traditional binary values, where each keyword is associated with each document to a certain fuzzy membership degree. FLSA has primarily been used in health research (Abdelrazek et al., 2023). One main advantage of this topic model is that it can address redundancy issues, typically offering higher topic coherence than LDA (Rijcken et al., 2021). However, FLSA has yet to be widely tested with large-scale data sets.

Top2Vec uses the Word2Vec neural network to detect word similarity within documents (Angelov, 2020). It is effective for large-scale data sets and has been applied in areas such as analyzing customer reviews (Yazıcı & Ozansoy Çadırcı, 2024) and identifying patient needs (Karas et al., 2022). Despite its strengths, Top2Vec has limitations, including challenges with parameter interpretation (Abdelrazek et al., 2023), excessive topic generation, and suboptimal performance with smaller data sets (Zengul et al., 2023). Additionally, while documents can theoretically be linked to multiple topics, Top2Vec typically assigns only one dominant topic per document (Egger & Yu, 2022).

To sum up, when selecting a topic modeling technique, researchers should consider three critical factors: data set scale (Egger & Yu, 2022; Zengul et al., 2023; Abdelrazek et al., 2023), ease of parameter tuning and topic interpretation (Zengul et al., 2023; Abdelrazek et al., 2023), and topic quality and coherence (Karami, 2015; Rijcken et al., 2021).

## 3.2 Computationally Intensive SAQD: A Proposed Scheme

In this subsection, we propose a scheme to conduct CI SAQD, using LDA as the underlying computational technique. Several reasons underpin this choice. First, LDA allows topic numbers to be determined through both quantitative (e.g., coherence analysis) and qualitative (e.g., human coding) methods. While models like Top2Vec can automate this process, they risk overfitting by generating an excessive number of topics (Zengul et al., 2023). Second, probabilistic topic models like LDA were designed to address certain limitations of linear algebra-based methods, such as the laten categorization method (Larsen et al., 2008), particularly in terms of the inference of document-topic distribution (Blei et al., 2003). Compared to such methods, LDA consistently produces more coherent topics (Egger & Yu, 2022; Zengul et al., 2023). Another advantage of LDA is its widespread accessibility and popularity (Egger & Yu, 2022). It is available in various programming languages (e.g., C, Java, Python, and R), making it usable by researchers with diverse technical backgrounds. LDA’s methodological alignment with the grounded theory approach further enhances its appeal (Baumer et al., 2017). Furthermore, LDA’s performance has been tested across varying data set scales, demonstrating superior results with larger data corpora (Schmiedel et al., 2019; Tang et al., 2014). When applied to large data sets, LDA can afford applications such as tracking topic evolution over time and space, assessing topic associations with external factors like financial indices, conducting topic comparisons across multiple data sets, and uncovering novel semantic patterns that can redefine research questions (Hannigan et al., 2019; Kiley et al., 2023; Schmiedel et al., 2019). Finally, LDA is wellestablished in the IS field, where it has been recognized for its potential to be integrated with conventional qualitative methods for theory building and to address a variety of research problems across different context (Gjerstad et al., 2021; Jung & Suh, 2019; Lappas et al., 2016; Rai, 2016; Yang & Subramanyam, 2023).

Figure 1 illustrates our proposed scheme, one possible approach (out of many) to integrating SAQD with computational elements and steps. The scheme focuses solely on the empirical phase of CI-SAQD research, which, like other types of research, is guided in the first place by the researcher’s phenomena of interest, theoretical considerations, and research questions.

![](/api/attachments/E5BN4VCK/fulltext/images/fa3182cbd08bb55cb4ea26a6b2da4cf60d1acd8d27623059c42db803b4dbb178.jpg)  
Figure 1. A Scheme for Conducting Computationally Intensive SAQD

The empirical phase begins with constructing a corpus of qualitative data. Data sources may include published qualitative studies, archives containing data from previous qualitative studies, or even primary data from the researcher’s past projects, according to Heaton (2004, 2008). The “data search and selection” step requires considering what is practically accessible as data, which is also contingent on the researcher’s skills and resources. Research questions, epistemological stance, theorizing modes (i.e., inductive, deductive, abductive), units of analysis, and specific contextual preferences such as geography, time, or language would also fundamentally drive the broad and in-depth search processes for data.

During the broad search for data, researchers often make preliminary decisions about inclusion or exclusion in relation to the data corpus they assemble. Metadata, typically attached to archived data items, can help structure files in the assembled corpus (Davidson et al., 2019). The subsequent in-depth evaluation of “fit” between the research study criteria and provisionally selected data sets is a more challenging task. Based on the SAQD literature (e.g., Fielding, 2000; Hammersley, 1997, 2010; Heaton, 2004; Hinds et al., 1997), the notion of fit can be characterized by two dimensions: suitability and sufficiency.

Suitability refers to the data set’s alignment with the researcher’s phenomena of interest and ability to support the researcher’s desired theorizing mode. Researchers can also draw from classic strategies for sampling and case selection (see Flyvbjerg, 2006). However, suitability often hinges on practical circumstances that may diverge from initial research expectations. Sufficiency, on the other hand, pertains to the richness and quality of the data set. Preexisting data must offer enough depth and detail to support the researcher’s envisioned theorizing tasks. Richness can usually be gauged by examining the presence of “thick” descriptions or narratives that provide a chain of evidence, explaining sequences of unfolding events (Beaudry & Pinsonneault, 2005; Paré & Elam, 1997; Yin, 2014). Data quality can also be assessed by investigating the rigor of the primary studies. According to Hinds et al. (1997), such an investigation may involve examining the primary researchers credentials, methodological expertise, and other factors, such as the amount of time spent at the site for data collection.

The “pre-processing” step aims to clean data and extract features from the data corpus constructed in the previous step. Pre-processing involves removing irrelevant content (e.g., stop words), normalizing related terms (e.g., lowercase conversion), and enhancing semantic information capture (e.g., handling negation) (Hickman et al., 2022). Feature extraction methods, such as the bag-of-words (BoW) model (Aggarwal, 2015), are also applied at this stage.

In the “semantic exploration” step, text data is analyzed using LDA. This requires setting three specific parameters. The first one is the number of topics. There are some methods to estimate the number of topics, such as coherence analysis, which measures semantic similarity among top words in a topic (Röder et al., 2015). The other two parameters are alpha and beta, representing document-topic and topic-word densities. Assuming each document represents a few topics, a small value often must be set for alpha. Also, beta is adjusted to a lower value when the identified topics have sparse word usage. Parameter tuning can thus significantly help avoid very general and shallow topics (Tang et al., 2014). Regarding semantic identification and analysis, one must consider what LDA produces as two key outputs: (1) the probability of each word per topic or P(W|T), essential for identifying topics, and (2) the probability of each topic per document or P(T|D), used to assess topic significance and enable further analyses (e.g., ttest or ANOVA on topic weights). Screening the identified topics may reveal opportunities for further refinements, such as adding more stop words to filter out common but semantically insignificant words. This suggests that one must often iterate between “semantic exploration” and “pre-processing” to improve topic quality.

The “interpretation and visualization” step involves interpreting and labeling the topics identified and analyzed in the previous step. Researchers perform tasks such as reviewing top words within topics (e.g., top 10 ranked by P(W|T)) and identifying relevant documents by sorting P(T|D). Researchers in a team may also employ methods such as consensus coding (Lim et al., 2015) to achieve agreement on topic meanings and labeling and group topics into higherorder categories. In addition, external auditors can validate these interpretation and labeling processes, adding an extra layer of rigor. Visualizations, such as word clouds, bar charts, line charts, and maps, can be used to illustrate findings, highlight topic dynamics, and explore patterns over time or space (Bai et al., 2021; Bennett et al., 2021; Lin et al., 2020). Finally, iterations between the “semantic exploration” and “interpretation and visualization” steps are often necessary to address problems such as unclear or overly general topics. Relying on relevant domain knowledge, researchers can fine-tune the number of topics, alpha, and beta, to control topic diversity and word selection within topics (Tang et al., 2014; Wallach et al., 2009).

Epistemological discussions about what has been framed in various ways, including “the digitalization of qualitative research” (Lee & Sarker, 2023), also intersect with the “interpretation and visualization” process. Critics argue that “big data” and computational techniques can separate methods from methodology and discipline (Smith, 2014). However, scholars like Davidson et al. (2019) have emphasized how computational approaches make “the shift between breadth and depth more transparent, enabling us to move across disciplinary and epistemological perspectives and introduce cross-contextual generalisations” (p. 373). Günther et al. (2023) described this as a “reflexive dance” between researchers and algorithms, where the interplay—if researchers maintain an active and reflexive stance— can ensure enhancing transparency and meaning rather than introducing bias and opacity. We thus concur with the perspective that computational methods like topic modeling do not “spit out” answers. They support rather than replace researchers, whose interpretive capabilities and decisions remain central to connecting results with the broader theoretical framing and questions of research studies (Kiley et al., 2023).

Table 1 summarizes the key issues and considerations related to our proposed CI-SAQD scheme.

Table 1. A Summary of the Proposed CI-SAQD Scheme

<table><tr><td>Steps</td><td>Key issues and considerations</td><td>Examples of corresponding literature</td></tr><tr><td>Data search &amp; selection</td><td>·Accessibility of preexisting data·Use of qualitative data archives·“Fit” between the research study criteria and provisionally selected data sets·Suitability and sufficiency of preexisting data</td><td>Bishop &amp; Kuula-Luumi (2017)Davidson et al. (2019)Hammersley (1997, 2010)Heaton (2004)Hinds et al. (1997)</td></tr><tr><td>Pre-processing</td><td>·Removing irrelevant content·Normalizing related terms·Enhancing semantic information capture·Feature extraction methods</td><td>Aggarwal (2015)Hickman et al. (2022)</td></tr><tr><td>Semantic exploration</td><td>·Setting the number of topics·Setting alpha and beta·P(W|T) and P(T|D) for semantic identification and analysis·Iteration between the semantic exploration and pre-processing steps</td><td>Tang et al. (2014)Röder et al. (2015)Schmiedel et al. (2019)</td></tr><tr><td>Interpretation &amp; visualization</td><td>·Topic interpretation and labeling·Use of consensus coding·Involving external auditors·Use of visualizations·Iteration between the interpretation &amp; visualization and semantic exploration steps</td><td>Bai et al. (2021)Bennett et al. (2021)Tang et al. (2014)Lim et al. (2015)Wallach et al. (2009)</td></tr></table>

## 3.3 Computationally Intensive SAQD: Innovative Research Designs

Theorizing can be seen as a systematic process involving a dialectic between data and generalizations aimed at accounting for empirical observations (Timmermans & Tavory, 2012). Qualitative research within IS and beyond is famous for often approaching such dialectics inductively, producing “either a substantive or a formal theory through a heuristic process of abstraction” (Timmermans & Tavory, 2012, p. 169). While inductive theory-building approaches still dominate, deductive qualitative research focused on theory testing has also gained traction over the past several decades. This mainly stems from the recognition that relying solely on quantitative methods for theory testing can be inadequate, if not damaging, particularly when assessing theories involving causal claims, emergent longitudinal relationships, dynamic processes, or human intentions in situ (Løkke & Sørensen, 2014; Miller & Tsang, 2011).

While theory testing is especially crucial in fields like management and IS, theories often remain unchallenged post-development (Suddaby et al., 2011; Fisher & Aguinis, 2017), and concerns persist about “the overabundance of weak and untested theory” (Cronin et al., 2021, p. 667, emphasis added). A contributing factor in qualitative research is the historical convention that theory building and testing require separate data sets (Hyde, 2000), which has created a “practical” barrier to pursuing deductive theorizing within IS and beyond (Bitektine, 2008; Dubé & Paré, 2003; Løkke & Sørensen, 2014).

The abovementioned situation inspires the potential for new research designs integrating CI-SAQD, allowing for multiple rounds of theorizing, each based on a distinct data corpus. In this context, we expect that computational methods can enhance efficiency, if nothing else, when engaging with these potentially large-scale data sets across theorizing rounds. In addition, we know that computational techniques like topic modeling are well-suited for various theorizing modes, enabling researchers to navigate inductive, deductive, and abductive approaches effectively (Fligstein et al., 2017; Haans, 2019; Hannigan et al., 2019; Kaplan & Vakili, 2015).

Research designs, such as those illustrated in Table 2, can broaden IS researchers’ choices to account for complex phenomena by enabling novel forms of longitudinal and/or cross-contextual research. Integrated inductivedeductive theorizing (II-DT) enables researchers to incorporate both inductive and deductive phases into their projects. For instance, in the first phase, the researcher might inductively develop a theory of digital transformation through a primary case study in the manufacturing sector. The second phase would then involve deductive testing of the theory, utilizing computational analysis of an assemblage of data from previous qualitative studies in two other sectors, i.e., computationally intensive amplified analysis.<sup>4</sup> Another approach, sequential deductive theorizing, allows multiple rounds of theory testing within a single research project. During each round, the theory is revised before commencing the next round. For example, the researcher might test and refine a well-established theory about algorithmic control by drawing on data from three major technology companies. Each round would then involve computational analysis of data about a distinct technology company, incorporating prior qualitative studies, digital trace data, and corporate reports, i.e., computationally intensive assorted analysis.<sup>5</sup>

We can also envision more advanced designs that extend beyond the two basic approaches outlined above. For instance, to enhance rigor in theorizing, one could combine the II-DT and sequential designs, where a theory developed in the initial phase of II-DT undergoes sequential testing in later phases. This approach can be referred to as sequential II-DT. Alternatively, a parallel II-DT approach could be employed, involving parallel, independent theory assessments during the second phase of II-DT using, for instance, two or more distinct corpora of preexisting qualitative data.

To conclude this subsection, we acknowledge the growing movement in qualitative research advocating that “abduction, rather than induction, should be the guiding principle of empirically based theory construction” (Timmermans & Tavory, 2012, p. 167). Abduction is also associated with arguments challenging the perceived dichotomy between induction and deduction (Goldberg, 2015). Notably, recent perspectives suggest that an abductive orientation can better leverage SAQD’s defining features in theorizing, especially considering that much of the criticism against SAQD is anchored in an inductive epistemology (Deterding & Waters, 2021; Vila-Henninger et al., 2022). We expect this abductive orientation to also benefit the research designs discussed earlier. For instance, we envisage that a research design like II-DT can be plausibly reworked into an integrative abductive process. This aligns with Charles S. Peirce’s assertion that “abduction is an integral process of the scientific method” (Timmermans & Tavory, 2012, p. 171), encompassing both induction and deduction (Vila-Henninger et al., 2022). We anticipate that this shift will open new avenues for exploration and application with SAQD and CI-SAQD. Consequently, we call for more nuanced methodological treatments of this subject in the future.

Table 2. Examples of Research Designs Augmented by CI-SAQD

<table><tr><td>Type of research design</td><td>Illustration of an example scenario</td><td>Description of an example scenario</td></tr><tr><td>Integrated inductive-deductive theorizing (II-DT)</td><td><img src="/api/attachments/E5BN4VCK/fulltext/images/6d119778f3b892db05acf3e3610dbec58ad5939bc07e0902db17c1b46d433feb.jpg"/></td><td>The INT phase is accomplished through a conventional qualitative study using primary qualitative data. The DET phase entails computationally intensive amplified analysis to test the theory built in the INT phase.</td></tr><tr><td>Sequential deductive theorizing</td><td><img src="/api/attachments/E5BN4VCK/fulltext/images/e0da07200b2fb41291d355b1beb62231676a328e353c82759175fed20e409a1a.jpg"/></td><td>Three consecutive rounds of DET with an already established theory are conducted. Each round of DET entails computationally intensive assorted analysis.</td></tr><tr><td>Sequential II-DT</td><td><img src="/api/attachments/E5BN4VCK/fulltext/images/666c326c1a01a2c1d1bc15261b790b1e5d32698b5ac350c0f8410f7787a28521.jpg"/></td><td>The INT phase is accomplished through a conventional qualitative study that draws on primary qualitative data. Two consecutive DET rounds follow, each involving computationally intensive amplified analysis.</td></tr><tr><td>Parallel II-DT</td><td><img src="/api/attachments/E5BN4VCK/fulltext/images/ef4d6600e1a6e30d0e0b34f9a50ef4512ee8274778d9240982a78e721ffc78a6.jpg"/></td><td>The INT phase is accomplished through a computationally intensive qualitative study drawing on digital trace data. Two parallel DET rounds are conducted in the second phase, each involving computationally intensive amplified analysis.</td></tr><tr><td colspan="3">Note: INT: inductive theorizing, DET: deductive theorizing</td></tr></table>

## 4 SAQD: Challenges and Limitations

Practicing SAQD often involves two broad categories of challenges: practical challenges and deeper epistemological, ethical, and legal challenges. The practical challenges primarily revolve around the availability, suitability, and adequacy of preexisting qualitative data. Still, many of these practical challenges can be mitigated or resolved by adhering to specific guidelines, including those concerning the suitability and sufficiency of preexisting data we previously discussed.

The second category of challenges involves more complex issues and questions that remain the subject of ongoing debates across disciplines (Feldman & Shaw, 2019; Heaton, 2004; Mannheimer et al., 2019; Mauthner & Parry, 2009, 2013). For instance, ethical concerns about confidentiality agreements and ensuring participant anonymity are central to the discussions about preserving and sharing qualitative data (Neale,

2013; Ruggiano & Perry, 2019). Similarly, as stated, epistemological debates continue over whether qualitative data can plausibly be “reused.” At the same time, some argue that challenges like ensuring a proper fit between data and theory or avoiding data misinterpretation are not unique to SAQD and are hurdles faced in both primary and secondary qualitative studies (Fielding, 2000; Hughes et al., 2020; Moore, 2007). In addition, even some critics of SAQD concede that their reservations “need not entirely preclude support for data sharing and re-use or all opportunities for comparative analysis” (Feldman & Shaw, 2019, p. 15).

We believe that many challenges associated with SAQD can be addressed by developing robust protocols and structures to foster collaboration among such entities as researchers, data repositories, university libraries, and funding institutions (see Feldman & Shaw, 2019; Mannheimer et al., 2019). Additionally, we emphasize the unique opportunity—and responsibility—for our community, especially now, in the era of computational methods, to engage more deeply with SAQD, advancing its various epistemological, methodological, and practical aspects. A first promising step forward might involve initiatives to establish and maintain digital archives. Such initiatives would promote a culture of preserving and sharing precious, rich qualitative data on contemporary and historical IS phenomena, serving current research needs and providing a crucial resource for future generations of IS scholars.

## 5 Conclusion

This paper aims to contribute to a scholarly conversation on leveraging computational methods when reusing data generated in previous qualitative studies. A similar theme has also recently gained momentum and been echoed in the social sciences and management research communities (Davidson et al., 2019; Hannigan et al., 2019). Our work also aligns with broader recognitions that the digitalization of research resources and processes continues to have consequential impacts on qualitative research (e.g., see Simeonova & Galliers, 2023). New mindsets and novel approaches have emerged, especially over the past two decades, regarding qualitative data generation, preservation, sharing, and analysis. Digital advancements have spurred the prevalence of qualitative data sharing and reuse, while the “archiving of qualitative research data is increasingly becoming a matter of national policy and practice in the United Kingdom, United States, Canada and Europe” (Mauthner & Parry, 2009, p. 301). In addition, disruptive innovations, particularly with artificial intelligence (AI), signal notable shifts in qualitative research concerning established methods and practices such as coding. However, it still seems inconceivable that AI tools can serve as anything more than aids for generating inputs to the more interpretive aspects of qualitative research, remaining firmly within the realm of human expertise (Morgan, 2023; Perkins & Roe, 2024; Wachinger et al., 2024).

As researchers increasingly gain access to preexisting qualitative data—such as interview transcripts, field notes, and observational records—through digital archives and other mediums, the sheer scale of such data often exceeds the reading and analysis capacity of qualitative research teams. This paper’s ideas and guidelines about computationally intensive secondary analysis not only offer a pathway to harness this data wealth more efficiently but also lay a groundwork for rigorous research drawing on carefully constructed assemblages of such data to innovatively approach today’s intricate phenomena and questions.

## Acknowledgments

We sincerely thank the senior editor, Dirk S. Hovorka, and the reviewers for their invaluable guidance, constructive feedback, and patience. We also gratefully acknowledge the opportunity to present an earlier version of this paper at a research seminar at IESEG School of Management. We appreciate the insightful comments from the participants, particularly Frank de Bakker.

## References

Abdelrazek, A., Eid, Y., Gawish, E., Medhat, W., & Hassan, A. (2023). Topic modeling algorithms and applications: A survey. Information Systems, 112, Article 102131.

Aggarwal, C. (2015). Mining text data. In Data Mining (pp. 429-455). Springer.

Angelov, D. (2020). Top2vec: Distributed representations of topics. arXiv. preprint https://arxiv.org/abs/2008.09470

Bahmanyar, R., Espinoza-Molina, D., & Datcu, M. (2018). Multisensor earth observation image classification based on a multimodal latent Dirichlet allocation model. IEEE Geoscience and Remote Sensing Letters, 15(3), 459-463.

Bai, X., Zhang, X., Li, K. X., Zhou, Y., & Yuen, K. F. (2021). Research topics and trends in the maritime transport: A structural topic model. Transport Policy, 102, 11-24.

Baumer, E. P., Mimno, D., Guha, S., Quan, E., & Gay, G. K. (2017). Comparing grounded theory and topic modeling: Extreme divergence or unlikely convergence? Journal of the Association for Information Science and Technology, 68(6), 1397-1410.

Beaudry, A., & Pinsonneault, A. (2005). Understanding user responses to information technology: A coping model of user adaptation. MIS Quarterly, 29(3), 493-524.

Bennett, J., Rachunok, B., Flage, R., & Nateghi, R. (2021). Mapping climate discourse to climate opinion: An approach for augmenting surveys with social media to enhance understandings of climate opinion in the United States. PLOS One, 16(1), Article e0245319.

Berente, N., Seidel, S., & Safadi, H. (2019). Research commentary—data-driven computationally intensive theory development. Information Systems Research, 30(1), 50-64.

Bishop, L. (2007). A reflexive account of reusing qualitative data: Beyond primary/secondary dualism. Sociological Research Online, 12(3), 43- 56.

Bishop, L., & Kuula-Luumi, A. (2017). Revisiting qualitative data re-use: A decade on. SAGE Open, 7(1), Article 2158244016685136.

Bitektine, A. (2008). Prospective case study design: Qualitative method for deductive theory testing. Organizational Research Methods. 11(1), 160- 180.

Blei, D. M. (2012). Probabilistic topic models. Communications of the ACM, 55(4), 77-84.

Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet Allocation. Journal of Machine Learning Research, 3(Jan), 993-1022.

Boyd-Graber, J., Hu, Y., & Mimno, D. (2017). Applications of topic models. Foundations and Trends in Information Retrieval, 11(2-3), 143- 296.

Bruns, A. (2013). Faster than the speed of print: Reconciling “big data” social media analysis and academic scholarship. First Monday, 18(10), 1-5.

Bryman, A. (1988). Quantity and quality in social research. Unwin Hyman.

Bybee, L., Kelly, B., & Su, Y. (2023). Narrative asset pricing: Interpretable systematic risk factors from news text. The Review of Financial Studies, 36(12), 4759-4787.

Cecez-Kecmanovic, D., & Kennan, M. A. (2013). The methodological landscape: Information systems and knowledge. In K. Williamson & G. Johanson, (Eds.), Research methods: Information, systems and contexts (pp. 113-137). Tilde

Chatfield, S. L. (2020). Recommendations for secondary analysis of qualitative data. The Qualitative Report, 25(3), 833-842.

Cohen, S., & Taylor, L. (1972). Psychological survival: The effects of long-term imprisonment. Allen Lane.

Corti, L., & Thompson, P. (1998). Are you sitting on your qualitative data? Qualidata’s mission. International Journal of Social Research Methodology, 1, 85-90.

Courage, F. (2019). Using the mass observation project: A case study in the practice of reusing data. Przegląd Socjologii Jakościowej, 15(1), 32-40.

Cronin, M. A., Stouten, J., & van Knippenberg, D. (2021). The theory crisis in management research: Solving the right problem. Academy of Management Review, 46(4), 667-683.

Davidson, E., Edwards, R., Jamieson, L., & Weller, S. (2019). Big data, qualitative style: A breadth-anddepth method for working with large amounts of secondary qualitative data. Quality & Quantity, 53(1), 363-376.

Deerwester, S., Dumais, S. T., Furnas, G. W., Landauer, T. K., & Harshman, R. (1990). Indexing by latent semantic analysis. Journal of the American Society for Information Science, 41(6), 391-407.

Denzin, N. K., & Lincoln, Y. S. (2011). The SAGE handbook of qualitative research. SAGE.

Deterding, N. M., & Waters, M. C. (2021). Flexible coding of in-depth interviews: A twenty-firstcentury approach. Sociological Methods & Research, 50(2), 708-739.

Dubé, L., & Paré, G. (2003). Rigor in information systems positivist case research: Current practices, trends, and recommendations. MIS Quarterly, 27(4), 597-636.

Durcikova, A., Miranda, S. M., Jensen, M. L., & Wright, R. T. (2024). United we stand, divided we fall: An autogenic perspective on empowering cybersecurity in organizations. MIS Quarterly, 48(4), 1503-1536.

Edwards, R., Davidson, E., Jamieson, L., & Weller, S. (2021). Theory and the breadth-and-depth method of analysing large amounts of qualitative data: a research note. Quality & Quantity, 55, 1275-1280.

Egger, R., & Yu, J. (2022). A topic modeling comparison between LDA, NMF, Top2Vec, and BERTopic to demystify Twitter posts. Frontiers in Sociology, 7, Article 886498.

Elman, C., Kapiszewski, D., & Vinuela, L. (2010). Qualitative data archiving: Rewards and challenges. PS: Political Science & Politics, 43(1), 23-27.

Feldman, S., & Shaw, L. (2019). The epistemological and ethical challenges of archiving and sharing qualitative data. American Behavioral Scientist, 63(6), 699-721.

Fielding, N. (2000). The shared fate of two innovations in qualitative methodology: The relationship of qualitative software and secondary analysis of archived qualitative data. Forum Qualitative Sozialforschung / Forum: Qualitative Social Research, 1(3). https://doi.org/10.17169/fqs-1.3. 1039

Fielding, N. G., & Fielding, J. L. (2000). Resistance and adaptation to criminal identity: Using secondary analysis to evaluate classic studies of crime and deviance. Sociology, 34(4), 671-689.

Fink, A. S. (2000). The role of the researcher in the qualitative research process. A potential barrier to archiving qualitative data. Forum Qualitative Sozialforschung / Forum: Qualitative Social Research, 1(3). https://doi.org/10.17169/fqs-1.3. 1021

Fisher, G., & Aguinis, H. (2017). Using theory elaboration to make theoretical advancements. Organizational Research Methods, 20(3), 438- 464.

Fligstein, N., Stuart Brundage, J., & Schultz, M. (2017). Seeing like the Fed: Culture, cognition, and framing in the failure to anticipate the financial

crisis of 2008. American Sociological Review, 82(5), 879-909.

Flyvbjerg, B. (2006). Five misunderstandings about casestudy research. Qualitative Inquiry, 12(2), 219- 245.

Gjerstad, P., Meyn, P. F., Molnár, P., & Næss, T. D. (2021). Do President Trump’s tweets affect financial markets? Decision Support Systems, 147, Article 113577.

Glaser, B. G. (1962). Secondary analysis: A strategy for the use of knowledge from research elsewhere. Social Problems, 10(1), 70-74.

Glaser, B. G. (1963). Retreading research materials: The use of secondary analysis by the independent researcher. American Behavioral Scientist, 6(10), 11-14.

Goldberg, A. (2011). Mapping shared understandings using relational class analysis: The case of the cultural omnivore reexamined. American Journal of Sociology, 116(5), 1397-1436.

Goldberg, A. (2015). In defense of forensic social science. Big Data & Society 2(2). https://doi.org/ 10.1177/2053951715601145

Goodwin, J. (Ed.). (2012). SAGE secondary data analysis. SAGE.

Greve, H. R., Rao, H., Vicinanza, P., & Zhou, E. Y. (2022). Online conspiracy groups: Microbloggers, bots, and coronavirus conspiracy talk on Twitter. American Sociological Review, 87(6), 919-949.

Grisham, E. L., Dashtgard, P., Relihan, D. P., Holman, E. A., & Silver, R. C. (2023). They saw a hearing: Democrats’ and Republicans’ perceptions of and responses to the Ford-Kavanaugh hearings. Personality and Social Psychology Bulletin, 51(5), 730-741.

Günther, A. W., Thompson, M., Mayur, P., & Polykarpou, S. (2023). Algorithms as Coresearchers: Exploring meaning and bias in qualitative research. In B. Simeonova & R. Galliers (Eds.), Cambridge handbook of qualitative digital research (pp. 211-228). Cambridge University Press.

Haans, R. F. J. (2019). What’s the value of being different when everyone is? The effects of distinctiveness on performance in homogeneous versus heterogeneous categories. Strategic Management Journal, 40(1), 3-27.

Hammersley, M. (1996). The relationship between qualitative and quantitative research: Paradigm loyalty versus methodological eclecticism. In J. T. Richardson (Ed.), Handbook of qualitative

research methods for psychology and the social sciences. BPS Books.

Hammersley, M. (1997). Qualitative data archiving: some reflections on its prospects and problems. Sociology, 31(1), 131-142.

Hammersley, M. (2010). Can we re-use qualitative data via secondary analysis? Notes on some terminological and substantive issues. Sociological Research Online, 15(1), 47-53.

Han, C., & Choi, J. (2010). Effect of latent semantic indexing for clustering clinical documents. Proceedings of the 9th IEEE/ACIS International Conference on Computer and Information Science (pp. 561-566).

Hannigan, T. R., Haans, R. F., Vakili, K., Tchalian, H., Glaser, V. L., Kaplan, S., & Jennings, P. D. (2019). Topic modeling in management research: Rendering new theory from textual data. Academy of Management Annals, 13(2), 586-632.

Harrison, J. S., Thurgood, G. R., Boivie, S., & Pfarrer, M. D. (2019). Measuring CEO personality: Developing, validating, and testing a linguistic tool. Strategic Management Journal, 40, 1316- 1330

Heaton, J. (1998). Secondary analysis of qualitative data. Social Research Update, 22(4), 88-93.

Heaton, J. (2004). Reworking qualitative data. SAGE.

Heaton, J. (2008). Secondary analysis of qualitative data: An overview. Historical Social Research, 33(3), 33-45.

Hickman, L., Thapa, S., Tay, L., Cao, M., & Srinivasan, P. (2022). Text preprocessing for text mining in organizational research: Review and recommendations. Organizational Research Methods, 25(1), 114-146.

Hinds, P. S., Vogel, R. J., & Clarke-Steffen, L. (1997). The possibilities and pitfalls of doing a secondary analysis of a qualitative data set. Qualitative Health Research, 7(3), 408-424.

Hoon, C. (2013). Meta-synthesis of qualitative case studies: An approach to theory building. Organizational Research Methods, 16(4), 522- 556.

Howison, J., Wiggins, A., & Crowston, K. (2011). Validity issues in the use of social network analysis with digital trace data. Journal of the Association for Information Systems, 12(12), 767- 797.

Huang, A. H., Lehavy, R., Zang, A. Y., & Zheng, R. (2018). Analyst information discovery and interpretation roles: A topic modeling approach. Management Science, 64(6), 2833-2855.

Hughes, K., Hughes, J., & Tarrant, A. (2020). Reapproaching interview data through qualitative secondary analysis: Interviews with internet gamblers. International Journal of Social Research Methodology, 23(5), 565-579.

Hyde, K. F. (2000). Recognising deductive processes in qualitative research. Qualitative Market Research, 3(2), 82-90.

Indulska, M., Hovorka, D. S., & Recker, J. (2012). Quantitative approaches to content analysis: Identifying conceptual drift across publication outlets. European Journal of Information Systems, 21(1), 49-69.

Irwin, S., & Winterton, M. (2011). Debates in qualitative secondary analysis: Critical reflections (Timescapes Working Paper No. 4). https://timescapes-archive.leeds.ac.uk/wpcontent/uploads/sites/47/2020/07/WP4-March-2011.pdf

Izonin, I., & Tkachenko, R. (2022). Universal intraensemble method using nonlinear AI techniques for regression modeling of small medical data sets. In A. K. Bhoi, V. H. C. de Albuquerque, P. N. Srinivasu, & G. Marques (Eds.), Cognitive and soft computing techniques for the analysis of healthcare data (pp. 123-150). Academic Press.

Jung, Y., & Suh, Y. (2019). Mining the voice of employees: A text mining approach to identifying and analyzing job satisfaction factors from online employee reviews. Decision Support Systems, 123, Article 113074.

Jurisch, M., Wolf, P., & Krcmar, H. (2013). Using the case survey method for synthesizing case study evidence in information systems research. Proceedings of the Americas Conference on Information Systems.

Kaplan, S., & Vakili, K. (2015). The double-edged sword of recombination in breakthrough innovation. Strategic Management Journal, 36(10), 1435- 1457.

Karami, A. (2015). Fuzzy topic modeling for medical corpora. (Publication No. 3721828) [Doctoral dissertation, University of Maryland, Baltimore County]. ProQuest Dissertations & Theses Global.

Karami, A., Gangopadhyay, A., Zhou, B., & Kharrazi, H. (2018). Fuzzy approach topic discovery in health and medical corpora. International Journal of Fuzzy Systems, 20, 1334-1345.

Karami, A., Lundy, M., Webb, F., & Dwivedi, Y. K. (2020a). Twitter and research: A systematic literature review through text mining. IEEE Access, 8, 67698-67717.

Karami, A., White, C. N., Ford, K., Swan, S., & Spinel, M. Y. (2020b). Unwanted advances in higher education: Uncovering sexual harassment experiences in academia with text mining. Information Processing & Management, 57(2), Article 102167.

Karas, B., Qu, S., Xu, Y., & Zhu, Q. (2022). Experiments with LDA and Top2Vec for embedded topic discovery on social media data—A case study of cystic fibrosis. Frontiers in Artificial Intelligence, 5, Article 948313.

Kern, F. G., & Mustasilta, K. (2023). Beyond replication: Secondary qualitative data analysis in political science. Comparative Political Studies, 56(8), 1224-1256.

Kiley, J., McKenny, A., Short, J., & Smith, A. (2023). Call for papers for a feature topic—Having a way with words: Innovations and improvements in text analysis methods. Organizational Research Methods, 26(4), 752-755.

Kunisch, S., Denyer, D., Bartunek, J. M., Menz, M., & Cardinal, L. B. (2023). Review Research as scientific inquiry. Organizational Research Methods, 26(1), 3-45.

Lappas, T., Sabnis, G., & Valkanas, G. (2016). The impact of fake reviews on online visibility: A vulnerability assessment of the hotel industry. Information Systems Research, 27(4), 940-961.

Larsen, K. R., Monarchi, D. E., Hovorka, D. S., & Bailey, C. N. (2008). Analyzing unstructured text data: Using latent categorization to identify intellectual communities in information systems. Decision Support Systems, 45(4), 884-896.

Larsson, R. (1993). Case survey methodology: Quantitative analysis of patterns across case studies. Academy of Management Journal, 36(6), 1515-1546.

Lau, R. Y., Li, C., & Liao, S. S. (2014). Social analytics: Learning fuzzy product ontologies for aspectoriented sentiment analysis. Decision Support Systems, 65, 80-94.

Lee, A. S. & Sarker, S. (2023). A philosophical perspective on qualitative research in the age of digitalization. In B. Simeonova & R. Galliers (Eds.), Cambridge handbook of qualitative digital research (pp. 15-27). Cambridge University Press.

Leh, A. (2000). Problems of archiving oral history interviews. The example of the Archive “German Memory.” In Forum Qualitative Sozialforschung / Forum: Qualitative Social Research, 1(3). https://doi.org/10.17169/fqs-1.3.1025

Lim, B. H., Valdez, C. E., & Lilly, M. M. (2015). Making meaning out of interpersonal victimization: The narratives of IPV survivors. Violence Against Women, 21, 1065-1086.

Lin, H. J., Sheu, P. C. Y., Tsai, J. J., Wang, C. C., & Chou, C. Y. (2020). Text mining in a literature review of urothelial cancer using topic model. BMC Cancer, 20(1), 1-7.

Lindberg, A., Berente, N., Gaskin, J., & Lyytinen, K. (2016). Coordinating interdependencies in online communities: A study of an open source software project. Information Systems Research, 27(4), 751-772.

Long-Sutehall, T., Sque, M., & Addington-Hall, J. (2011). Secondary analysis of qualitative data: a valuable method for exploring sensitive issues with an elusive population? Journal of Research in Nursing, 16(4), 335-344.

Løkke, A. K., & Sørensen, P. D. (2014). Theory testing using case studies. Electronic Journal of Business Research Methods, 12(1), 66-74.

Lucas, W. A. (1974). The case survey method: Aggregating case experience (R-1515-RC). Rand Corporation.

Mannheimer, S., Pienta, A., Kirilova, D., Elman, C., & Wutich, A. (2019). Qualitative data sharing: Data repositories and academic libraries as key partners in addressing challenges. American Behavioral Scientist, 63(5), 643-664.

Mauthner, N. S., & Parry, O. (2009). Qualitative data preservation and sharing in the social sciences: On whose philosophical terms? Australian Journal of Social Issues, 44(3), 291-307.

Mauthner, N. S., & Parry, O. (2013). Open access digital data sharing: Principles, policies and practices. Social Epistemology, 27(1), 47-67.

Mason, J. (2002). Qualitative research resources: A discussion paper. For the ESRC Research Resources Board.

Miller, K. D., & Tsang, E. W. (2011). Testing management theories: Critical realist philosophy and research methods. Strategic Management Journal, 32(2), 139-158.

Miranda, S., Berente, N., Seidel, S., Safadi, H., & Burton-Jones, A. (2022). Editor’s comments: Computationally intensive theory construction: A primer for authors and reviewers. MIS Quarterly, 46(2), iii-xviii.

Moore, N. (2007). (Re)using qualitative data? Sociological Research Online, 12(3), 1-13.

Moore, N. (2005, September 28). (Re)using qualitative data? Thoughts from the CRESC Qualitative

Research Laboratory. Presented at the Reusing Qualitative Data Workshop, CRESC, Manchester.

Morgan, D. L. (2023). Exploring the use of artificial intelligence for qualitative data analysis: The case of ChatGPT. International Journal of Qualitative Methods, 22, https://doi.org/10.1177/16094069 231211248

Mortenson, M. J., & Vidgen, R. (2016). A computational literature review of the technology acceptance model. International Journal of Information Management, 36(6), 1248-1259.

Myers, M. D., & Avison, D. (1997). Qualitative research in information systems. MIS Quarterly, 21(2), 241-242.

Neale, B., Henwood, K., & Holland, J. (2012). Researching lives through time: An introduction to the Timescapes approach. Qualitative Research, 12(1), 4-15.

Neale, B. (2013). Adding time into the mix: Stakeholder ethics in qualitative longitudinal research. Methodological Innovations Online, 8(2), 6-20.

Paré, G., & Elam, J. J. (1997). Using case study research to build theories of IT implementation. In A.S. Lee, J. Liebenau, & J. I. DeGross (Eds.), Information systems and qualitative research (pp. 542-568). Chapman and Hall.

Parry, O., & Natasha, S. M. (2005). Back to basics: Who re-uses qualitative data and why? Sociology, 39(2), 337-342.

Perkins, M., & Roe, J. (2024). The use of generative AI in qualitative analysis: Inductive thematic analysis with ChatGPT. Journal of Applied Learning and Teaching, 7(1), 390-395.

Rai, A. (2016). Editor’s comments: Synergies between big data and theory. MIS Quarterly, 40(2), iii-ix.

Rijcken, E., Scheepers, F., Mosteiro, P., Zervanou, K., Spruit, M., & Kaymak, U. (2021). A comparative study of fuzzy topic models and LDA in terms of interpretability. Proceedings of the IEEE Symposium Series on Computational Intelligence.

Rivard, S., & Lapointe, L. (2012). Information technology implementers’ responses to user resistance: Nature and effects. MIS Quarterly, 36(3), 897-920.

Röder, M., Both, A., & Hinneburg, A. (2015, February). Exploring the space of topic coherence measures. Proceedings of the 8th ACM International Conference on Web Search and Data Mining (pp. 399-408).

Ruggiano, N., & Perry, T. E. (2019). Conducting secondary analysis of qualitative data: Should we,

can we, and how? Qualitative Social Work, 18(1), 81-97.

Sandelowski, M. (1997). “To be of use”: Enhancing the utility of qualitative research. Nursing Outlook, 45(3), 125-132.

Sarkar, S. (2021). Using qualitative approaches in the era of big data: a confessional tale of a behavioral researcher. Journal of Information Technology Case and Application Research, 23(2), 139-144.

Sarker, S., Xiao, X., Beaulieu, T., & Lee, A. S. (2018). Learning from first-generation qualitative approaches in the IS discipline: An evolutionary view and some implications for authors and evaluators (PART 1/2). Journal of the Association for Information Systems, 19(8), 752-774.

Savage, M. (2005). Revisiting classic qualitative studies. Historical Social Research, 6(1), 118-39.

Schmiedel, T., Müller, O., & vom Brocke, J. (2019). Topic modeling as a strategy of inquiry in organizational research: A tutorial with an application example on organizational culture. Organizational Research Methods, 22(4), 941- 968.

Setzke, D. S., Böhm, M., & Krcmar, H. (2020). Combining the case survey method and qualitative comparative analysis for information systems research. Proceedings of the Americas Conference on Information Systems.

Shah, C. (2020). A hands-on introduction to data science. Cambridge University Press.

Simeonova, B., & Galliers, R. D. (Eds.). (2023). Cambridge handbook of qualitative digital research. Cambridge University Press.

Skinner, R. J., Nelson, R. R., & Chin, W. (2022). Synthesizing qualitative evidence: a roadmap for information systems research. Journal of the Association for Information Systems, 23(3), 639- 677.

Smith, R. J. (2014). Missed miracles and mystical connections: Qualitative research, digital social science and big data. In Big data? Qualitative approaches to digital research (pp. 181-204). Emerald.

Stafford, T. F., & Farshadkhah, S. (2020). A method for interpretively synthesizing qualitative research findings. Communications of the Association for Information Systems, 46, 117-133.

Suddaby, R., Hardy, C., & Huy, Q. N. (2011). Where are the new theories of organization? Academy of Management Review, 36(2), 236-246.

Tana, S., Breidbach, C. F., & Burton-Jones, A. (2023). Digital transformation as collective social action.

Journal of the Association for Information Systems, 24(6), 1618-1644.

Tang, J., Meng, Z., Nguyen, X., Mei, Q., & Zhang, M. (2014). Understanding the limiting factors of topic modeling via posterior contraction analysis. Proceedings of the International Conference on Machine Learning (pp. 190-198).

Tarafdar, M., Page, X., & Marabelli, M. (2022). Algorithms as co‐workers: Human algorithm role interactions in algorithmic work. Information Systems Journal, 33(2), 232-267.

Tate, J. A., & Happ, M. B. (2018). Qualitative secondary analysis: a case exemplar. Journal of Pediatric Health Care, 32(3), 308-312.

Thorne, S. (1994). Secondary analysis in qualitative research: Issues and implications. In J. M. Morse (Ed.), Critical issues in qualitative research methods (pp. 263-279). SAGE.

Timmermans, S., & Tavory, I. (2012). Theory construction in qualitative research: From grounded theory to abductive analysis. Sociological Theory, 30(3), 167-86.

Valdez, D., Pickett, A. C., & Goodson, P. (2018). Topic modeling: latent semantic analysis for the social sciences. Social Science Quarterly, 99(5), 1665- 1679.

van Loon, A. (2022). Three families of automated text analysis. Social Science Research, 108, Article 102798.

Vila-Henninger, L., Dupuy, C., Van Ingelgom, V., Caprioli, M., Teuber, F., Pennetreau, D., Bussi, M., & Le Gall, C. (2022). Abductive coding: Theory building and qualitative (re)analysis.

Sociological Methods & Research, 53(2), 968- 1001.

Wachinger, J., Bärnighausen, K., Schäfer, L. N., Scott, K., & McMahon, S. A. (2024). Prompts, pearls, imperfections: Comparing ChatGPT and a human researcher in qualitative data analysis. Qualitative Health Research. Advance online publication. https://doi.org/10.1177/10497323241244669

Wallach, H., Mimno, D., & McCallum, A. (2009). Rethinking LDA: Why priors matter. Proceedings of the 23rd International Conference on Neural Information Processing Systems (pp. 1973-1981).

Weick, K. E., Sutcliffe, K. M., & Obstfeld, D. (2005). Organizing and the process of sensemaking. Organization Science, 16(4), 409-421.

Yang, Y., & Subramanyam, R. (2023). Extracting actionable insights from text data: A stable topic model approach. MIS Quarterly, 47(3), 923-954.

Yazıcı, G., & Ozansoy Çadırcı, T. (2024). Creating meaningful insights from customer reviews: a methodological comparison of topic modeling algorithms and their use in marketing research. Journal of Marketing Analytics, 12(4), 865-887.

Yin, R. K. (2014). Case study research: Design and methods. SAGE.

Zengul, F., Bulut, A., Oner, N., Ahmed, A., Yadav, M., Gray, H. G., & Ozaydin, B. (2023). A practical and empirical comparison of three topic modeling methods using a COVID-19 Corpus: LSA, LDA, and Top2Vec.

Zimmer, L. (2006). Qualitative meta‐synthesis: A question of dialoguing with texts. Journal of Advanced Nursing, 53(3), 311-318.

## About the Authors

Kaveh Mohajeri is an associate professor in the Department of Innovation, Entrepreneurship, and Information Systems at IESEG School of Management, France. He received his BSc degree in industrial management and his MSc in IT management from the University of Tehran, Iran. He also has a PhD in information systems from Virginia Commonwealth University. A core part of his research agenda concerns advancing novel methodological thinking and research practices, focusing on the issues of research relevance and impact, deductive theorizing, and computationally intensive qualitative research. His work has been published in MIS Quarterly, Journal of the Association for Information Systems, and Journal of Information Technology, among other outlets.

Amir Karami is an associate professor of business analytics/quantitative methods in the Management, Information Systems, and Quantitative Methods Department at Collat School of Business at the University of Alabama at Birmingham. His research interests include text mining, social media analytics, generative AI, health informatics, mis/disinformation, and computational social science. His work has been published in various journals, such a International Journal of Information Management and Journal of Biomedical Informatics.
