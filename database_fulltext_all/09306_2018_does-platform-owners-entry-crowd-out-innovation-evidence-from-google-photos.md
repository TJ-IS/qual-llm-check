---
otero_id: 9306
otero_key: "5WZTV62D"
title: "Does Platform Owner’s Entry Crowd Out Innovation? Evidence from Google Photos"
authors: "Jens Foerderer; Thomas Kude; Sunil Mithas; Armin Heinzl"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2018.0787"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/5WZTV62D/fulltext/images/00d3a694060f77a78785819f8c730658ebf86b5089a3c95c8f4377a23521908a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Does Platform Owner’s Entry Crowd Out Innovation? Evidence from Google Photos

Jens Foerderer, Thomas Kude, Sunil Mithas, Armin Heinzl

Jens Foerderer, Thomas Kude, Sunil Mithas, Armin Heinzl (2018) Does Platform Owner’s Entry Crowd Out Innovation? Evidence from Google Photos. Information Systems Research

Published online in Articles in Advance 14 May 2018

https://doi.org/10.1287/isre.2018.0787

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms.

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Does Platform Owner’s Entry Crowd Out Innovation? Evidence from Google Photos

Jens Foerderer,<sup>a</sup> Thomas Kude,<sup>b</sup> Sunil Mithas,<sup>c,d</sup> Armin Heinzl<sup>a</sup>

<sup>a</sup> Business School, University of Mannheim, 68131 Mannheim, Germany; <sup>b</sup> ESSEC Business School, 95021 Cergy-Pontoise, France; <sup>c</sup> Robert H. Smith School of Business, University of Maryland, College Park, Maryland 20742; <sup>d</sup> Muma College of Business, University of South Florida, Tampa, Florida 33620

Contact: foerderer@uni-mannheim.de, http://orcid.org/0000-0002-3090-4559 (JF); kude@essec.edu, http://orcid.org/0000-0002-9891-0517 (TK); smithas@rhsmith.umd.edu, http://orcid.org/0000-0002-2182-6202 (SM); heinzl@uni-mannheim.de, http://orcid.org/0000-0001-9886-9596 (AH)

Received: August 28, 2016 Revised: June 1, 2017; December 2, 2017; January 30, 2018 Accepted: February 12, 2018 Published Online in Articles in Advance: May 14, 2018

https://doi.org/10.1287/isre.2018.078

Copyright: © 2018 INFORMS

Abstract. We study how platform owners’ decision to enter complementary markets afects innovation in the ecosystem surrounding the platform. Despite heated debates on the behavior of platform owners toward complementors, relatively little is known about the mechanisms linking platform owners’ entry and complementary innovation. We exploit Google’s 2015 entry into the market for photography apps on its own Android platform as a quasi-experiment. We conclude based on our analyses of a time-series panel of 6,620 apps that Google’s entry was associated with a substantial increase in complementary innovation. We estimate that the entry caused a 9.6% increase in the likelihood of major updates for apps afected by Google’s entry, compared to similar but not afected apps. Further analyses suggest that Google’s entry triggered complementary innovation because of the increased consumer attention for photography apps, instead of competitive “racing” or “Red Queen” efects. This attention spillover efect was particularly pronounced for larger and more diversified complementors. The study advances our understanding of the efects of platform owner’s entry, explicates the complex mechanisms that shape complementary innovation, and adds empirical evidence to the debate on regulating platforms.

History: Panos Constantinides, Ola Henfridsson, and Geofrey Parker, Special Issue Editors; Youngjin Yoo, Associate Editor. This paper has been accepted for the Information Systems Research Special Issue on Digital Infrastructure and Platforms.

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2018.0787.

Keywords: platform ecosystem • platform governance • platform owner • platform entry • complementors • innovation • Google Photos • racing • Red Queen • attention spillover

## 1. Introduction

Platform owner’s entry into complementary markets is a popular yet not well understood phenomenon. In 2015, Google entered the market for photography apps on its Android platform with an all-purpose photography app, and began to compete with thousands of complementors on its own platform, thus raising questions about the impact of such an entry on innovation in the app ecosystem. Google’s announcement came as a surprise to complementors and is in sharp contrast to the behavior of other platform owners. For example, the enterprise software vendor SAP regularly publishes a two-year road map informing complementors about its activities in markets complementary to its enterprise software platforms (Parker et al. 2017). These remarkably diferent practices sparked considerable interest in the behavior of platform owners toward their complementary markets to understand whether and how entry afects innovation in the platform ecosystem and implications for platform governance (e.g., Adner and Kapoor 2010, Gawer and Henderson 2007, Gilbert and Katz 2001).

Researchers have framed the decision to enter complementary markets as an aspect of platform governance to orchestrate complementors (Boudreau and Hagiu 2009, Tiwana 2015, Wareham et al. 2014). Entry has been studied in three streams of work on platform governance, the economics of multi-sided markets (e.g., Farrell and Katz 2000), platform engineering and design (e.g., Eaton et al. 2015), and strategy (e.g., Gawer and Henderson 2007). These streams suggest that entry may allow platform owners to appropriate rents (Farrell and Katz 2000, Huang et al. 2013), foster integration (Adner and Kapoor 2010, Li and Agarwal 2017), and retain control over platform evolution (Eaton et al. 2015, Gawer and Henderson 2007). However, there is also evidence of entry hurting complementors’ revenues, eventually causing them to hesitate contributing to the platform in the future, thus “crowding out” complementary innovation (Gawer and Henderson 2007). If entry reduces complementors’ incentives to innovate, then it may appear to run counter to the initial motivation to establish a platform, i.e., profiting from complementary innovation (Gawer and Henderson 2007). Thus, analyzing the consequences of entry on complementary innovation can help platform owners and policy makers determine the overall impact of this governance decision.

The consequences of entry on complementary innovation are hotly debated, and ultimately an empirical question. Prior work suggests several theoretical mechanisms for the efect of entry. The economics literature suggests a negative efect on complementary innovation. By entering complementary markets, platform owners can potentially appropriate complementors’ rents and ultimately reduce complementors’ incentives to innovate (Choi and Stefanadis 2001, Farrell and Katz 2000). As a reaction to expropriation by the platform owner, complementors may invest available resources in mechanisms to protect their innovations or eventually afiliate with competing platforms (Ceccagnoli et al. 2012, Huang et al. 2013). Thus, entry may curb complementors’ innovation.

By contrast, the management and marketing literatures suggest a positive influence of entry on complementary innovation via two diferent mechanisms: Racing and attention spillover. First, studies on competitive dynamics suggest that entry may trigger racing efects. According to this mechanism, entry puts complementors under direct competitive pressure, urging them to innovate, not to lag behind (Barnett and Hansen 1996, Barnett and Pontikes 2008). Second, studies on consumer research suggest that entry may trigger attention spillover efects. According to this mechanism, entry stimulates innovation by attracting consumers and providing complementors with new demand and feedback to innovate (Li and Agarwal 2017, Liu et al. 2014).

Despite these theoretical disagreements about the consequences of entry on complementary innovation, there has been scant empirical research on this phenomenon. Most literature on entry is descriptive and focuses on the managerial practices of platform owners (Gawer and Cusumano 2002, Gawer and Henderson 2007). Some studies investigated the consequences for platform owners when complementors have appropriability concerns (Ceccagnoli et al. 2012, Huang et al. 2013). Yet, to our knowledge, these studies do not provide insights into the direct efects of entry on innovation and its underlying mechanisms, something that we do in this study. The conflicting arguments outlined above suggest the need for empirical research that identifies the efect of entry on complementary innovation and untangles the underlying theoretical mechanisms.

This study tests the efects of entry on complementary innovation, thus contributing to the literature on platform governance (e.g., Gawer 2014, Tiwana et al. 2010). We exploit Google’s release of Google Photos, an all-purpose app for organizing, editing, and sharing digital photographs, to users of its smartphone platform Android, as a quasi-experiment. This event is intriguing because many photography-related apps existed before Google’s entry and the release of Photos is an exogenous shock to complementors and their innovation outcomes. In addition, this context allows us to isolate the efects of entry on the innovation outcomes of photography-related apps, and to compare them to a control group of complementors not afected by entry. We use time-series panel data on a representative sample of $6 { , } 6 2 0$ apps from the Google Play Store, the largest store for Android apps worldwide. We observe the apps monthly, beginning three months before and ending three months after the release of Google Photos, and estimate the impact of entry on innovation following a diference-in-diferences (DID) framework. We model complementary innovation as complementors’ decision to release a major update for their app, in terms of adding new features or functionalities. We identify major updates by text-analyzing the release notes published by complementors.

To preview our key results, our DID analyses of apps afected by Google’s entry compared with apps not afected by entry suggest strong and positive efects of entry on complementary innovation. Subsequent tests point toward an attention spillover efect as an explanation for the increase in complementary innovation: Platform owners’ entry increases consumer demand and feedback, which provides complementors with new ideas and opportunities to innovate. Our analyses suggest that the attention spillover efect is more pronounced for larger and more diversified complementors. One plausible explanation is that larger and more diversified complementors perceive entry as an opportunity to innovate rather than as a threat.

## 2. Theoretical Background 2.1. Platform Governance, Entry, and Complementary Innovation

Platform strategies and governance have recently gained significant attention (e.g., Gawer and Cusumano 2002, Parker et al. 2016, Rochet and Tirole 2003). We define a platform as a system that brings system adopters together with firms that provide complements to the system, so-called complementors. Our focus is platforms that support uncoordinated and generative complementary innovation as is the case in mobile operating systems (Thomas et al. 2014, Yoo et al. 2010).<sup>1</sup> Following Brandenburger and Nalebuf (1996), a complement to a product or service is any other product or service that makes the focal product or service more attractive. Mobile platforms, for example, become more attractive with the availability of apps. Given that platforms are subject to multi-sided network efects (Katz and Shapiro 1994), winner-takes-all dynamics (Rochet and Tirole 2003), and antitrust regulations (Gilbert and Katz 2001), platform owners’ activities go beyond designing, developing, and distributing products and services to include decisions for governing complementary innovation by orchestrating the behavior and contributions of complementors (Boudreau and Hagiu 2009).

We draw on three streams of prior work on platform governance to inform our investigation of platform owners’ entry into complementary markets. These three streams are the economics of multi-sided markets (e.g., Farrell and Katz 2000), platform engineering and design (e.g., Eaton et al. 2015), and strategy (e.g., Gawer and Henderson 2007). See Online Appendix A for an overview of selected studies on platform governance. First, we draw on research on the economics of multi-sided markets that relies on analytical models to study governance instruments (Anderson et al. 2014, Farrell and Katz 2000, Rochet and Tirole 2003). These studies view entry as a means to extract rents from complementors and to recoup the initial investments of platform owners in their platforms. Other models studied two instruments closely related to entry, tying and vertical integration. Tying refers to the practice of making the sale of the platform conditional on the purchase of a complement (Choi and Stefanadis 2001), such as Microsoft’s decision to sell its Windows platform together with Internet Explorer. Vertical integration refers to the practice of making a complement a feature of the core platform (Farrell and Katz 2000), such as Apple integrating flashlight and blue light reduction features into its iPhone operating system.

Second, we draw on prior work that studies platform governance from a design and engineering perspective (e.g., Ghazawneh and Henfridsson 2013). This work recognizes that governance outcomes are the result of a complex and dynamic sociotechnical negotiation between platform owners and complementors often mediated through technical artifacts and their characteristics, such as boundary resources (Eaton et al. 2015, Foerderer et al. 2018, Ghazawneh and Henfridsson 2013) or platform modularity (Tiwana et al. 2010). From this perspective, entry relates to the notion of “securing,” a “process by which the control of a platform and its related services is increased” (Ghazawneh and Henfridsson 2013, p. 177). In this sense, entry may serve as an instrument to secure technological control over the platform in that it helps to ensure technological integration and direct platform evolution over time (Tiwana et al. 2010).

Finally, we draw on strategy-related work on platform governance that provides rich descriptions of governance practices (e.g., Gawer and Cusumano 2002,

Huber et al. 2017, Wareham et al. 2014). For example, the descriptions of Intel’s decision-making on complementors by Gawer and Cusumano (2002) and Gawer and Henderson (2007) document a continuous balance between implementing market-based competitive policies and approaches focused on committing to complementors. While these observations derive from platforms for coordinated innovation, more recent findings suggest that governance practices may also matter on platforms for uncoordinated innovation (e.g., Huang et al. 2018, Huber et al. 2017). For example, Huang et al. (2013) observe that firms are more likely to become complementors for a platform if they have mechanisms in place to safeguard against appropriation, such as patents, copyrights, and downstream capabilities.

We extend prior work and contribute to the nascent but rapidly evolving literature on platform governance by providing insights into the consequences of entry, in terms of platform owners’ decisions to release own complements that overlap with functionality covered by complementors’ products. Thereby, we respond to calls for research to understand the impact of governance instruments (Gawer 2014, Tiwana et al. 2010, Yoo et al. 2010).

## 2.2. Mechanisms to Explain the Efect of Entry on Complementors’ Innovation: Racing and Attention Spillover

Although entry has been subject to prior work on platform governance, the question of whether entry curbs or fosters complementary innovation, and in particular, the theoretical mechanisms through which entry might afect complementary innovation, remain understudied. As noted above, the wider economics literature suggests entry to curb complementary innovation (Choi and Stefanadis 2001, Farrell and Katz 2000, Huang et al. 2013), whereas the management and marketing literatures suggest two mechanisms that support the alternative hypothesis that entry may in fact stimulate complementary innovation. We refer to these mechanisms as racing and attention spillover.

The racing mechanism suggests that increased innovation after entry reflects the result of supply-side competitive dynamics (Gawer and Henderson 2007, Tiwana 2015). According to the racing mechanism, entry poses a competitive threat to complementors, to which complementors respond by increasing their innovation output. This rationale stems from work on competitive dynamics or the “Red Queen” efect in the strategic management literature (Barnett and Hansen 1996, Barnett and Pontikes 2008, Derfus et al. 2008). The Red Queen efect means that performance diferences across firms (e.g., innovation) are the result of a continuous, escalating, and evolutionary contest (Derfus et al. 2008). The only way firms can maintain their performance relative to others is by engaging in innovative actions, which leads to situations in which “all the firms end up racing as fast as they can just to stand still relative to competitors” (Derfus et al. 2008, p. 61). Racing mechanisms have been documented in the context of hardware platforms and Internet browsers (Gawer and Henderson 2007, Tiwana 2015). Gawer and Henderson (2007), for example, find that Intel sometimes deliberately entered complementary markets to inject competition among complementors, with the ultimate goal of stimulating complementors’ innovation outputs. Taken together, these arguments and case study evidence for the racing mechanism suggest that entry may foster complementary innovation by stimulating supply-side competition.

In contrast to the racing mechanism, the attention spillover mechanism suggests that increased innovation is the result of increased demand-side attention and feedback following the platform owner’s market entry. Entry enlarges the overall number of consumers attracted to a market category from which complementors stand to benefit, and which may eventually increase their innovation. For example, Li and Agarwal (2017) observe that Facebook’s integration of Instagram increased the demand for apps similar to Instagram. The theoretical rationale for an attention spillover efect derives from the wider literature on consumer research, which has studied spillover efects from a firm’s product market decisions such as advertising (e.g., Liu et al. 2014). Although such activities intuitively increase attention for a focal product and reduce consumer demand for competing products, more recent evidence indicates that a firm’s activities can have positive spillover efects on same-category products by increasing the overall number of consumers in a market category, in terms of “enlarging the pie” for all market participants (Liu et al. 2014, Sahni 2016). Following this argument, entry might stimulate complementary innovation by increasing demand and feedback from consumers. Consumer feedback enables innovation by opening new opportunities from which complementors can draw to innovate (e.g., Brown and Eisenhardt 1995, March 1991). Overall, the attention spillover mechanism suggests that entry increases complementor innovation by increasing demand-side attention.

We empirically assess the explanatory power of the above two mechanisms as to how entry afects complementary innovation.

## 3. Method

## 3.1. Empirical Context: Release of the Google Photos Android App

We study a platform owner’s entry decision in the context of mobile operating systems. We investigate the consequences of Google’s 2015 entry into the category of photography apps on its Android mobile operating system. On May 28, 2015, Google published the app Google Photos (hereafter referred to as Photos) in the Google Play Store.<sup>2</sup> Google described Photos as an all-purpose app for organizing, editing, and sharing digital photographs. Photos addressed many of the needs of the “pic or it didn’t happen” trend among smartphone users: The app was promoted to decrease users’ eforts in organizing photographs. It automatically grouped images by individuals, landmarks, and objects shown in the images using machine learning and artificial intelligence. In addition, the app included the functionality to manipulate photographs. Finally, Photos gave users extensive free online storage for pictures and videos. The event was relatively unanticipated by complementors. Photos received significant media attention immediately after its release. Not only did the technology press cover the release of Photos but also major general press outlets picked up the news, including the Wall Street Journal and the New York Times (e.g., Swanson 2015). Five months after its introduction, Photos was reported to have reached 100 million monthly users.<sup>3</sup>

## 3.2. Research Design

Figure 1 summarizes our research design. We exploit Google’s introduction of Photos as a quasi-experiment. The release of Photos allows us to compare innovation outcomes of complementors afected by entry with the innovation outcomes of complementors not afected by entry, before and after the release of Photos. Our identification strategy uses the release of Photos as an exogenous shock to complementors to assess the consequences of platform owners’ entry for complementary innovation.

Measuring innovation is complex; useful proxies are often context-specific. Our unit of analysis is at the app level, and we model innovation by major app updates, in terms of complementors’ introducing new functionality or features in their apps. Prior work investigated updates from a perspective of maintaining software (Kemerer and Slaughter 1999); we argue that updates are an important means of innovation. Software is technologically flexible, meaning that producers can redefine and shape software products after their market release. We choose updates as a proxy for innovation because updates allow us to isolate the decision to innovate more thoroughly for two reasons. First, with updates as a dependent variable, we can use app-level controls for potential heterogeneity that may influence the innovation decision. Second, unlike other measures of innovation (e.g., new app releases), updates allow us to more directly infer racing and attention spillover efects. Other work that used updates in an innovation context include Boudreau (2012), who used a count of application updates in the context of handheld applications, and Tiwana (2015), who used the frequency of updates to infer the speed of product evolution. New app releases are an alternative proxy for innovation. However, we do not rely on new app releases as a proxy of innovation for our main estimations because there is little variance that we can predict and because new app releases are likely to occur with a substantial delay, which our post-entry period might be unable to fully capture or that might be confounded with other events in case of an extended post-entry period.

Figure 1. Research Design  
![](/api/attachments/5WZTV62D/fulltext/images/ae856c2b2561a98d31b0640757db6301ed4c6e071291ab4f7e99d15ad57134c5.jpg)  
Notes. The figure illustrates the quasi-experimental research design implemented in this study. We exploit the release of the Google Photos app on May 28, 2015 (dashed line) as an exogenous shock in photography apps that were afected by Google’s entry. Starting with March 2015, we track a sample of apps in both groups before the release of Photos (pre-entry period) until three months after the release (post-entry period), on a monthly time-series. We then estimate the DID. Our observation period deliberately excludes events that may confound the estimates, including a general update of the Google Play Services in September, an Android operating system release in October, and a comprehensive update of the Google Photos Android app in December.

## 3.3. Sample

Our analysis is at the app level. We collected data directly from the Google Play Store. One advantage of our sample is that it comprises app-level time-series data on a representative selection of apps in the Google Play Store, which helps to get a full picture of complementary innovation, account for time-invariant heterogeneity, and avoid potential selection bias that can arise by using data on apps listed in top rankings or by using a cross-sectional design. We compiled our data in two steps.

First, we indexed apps in the Google Play Store between July and December 2014. This step resulted in a list of all apps available in the Google Play Store at that time.

Second, in January 2015, we selected a random sample of 100,000 apps from our index. We observed this sample monthly, tracking app-specific information, including an app’s average rating by customers, the number of reviews, updates, and prices. So as not to compare functional apps with content, we removed apps labeled as “books and references,” “comics,”

“education,” “libraries and demos,” “news and magazines,” “wallpaper,” “widgets,” and “games.”

We compared our sample with population-level characteristics published by AppAnnie, a major mobile analytics firm, on the distribution of apps across categories and the distributions of average ratings, reviews, and prices. We did not observe significant diferences, which increases confidence in the reliability of our data.

## 3.4. Treatment and Control Group Construction

To identify apps afected by entry (treatment) and apps not afected by entry (control), we use the Google Play categorization system. Categories are particularly suited for studying the efects of entry for two reasons. First, they share similar functionality and, second, they compete for the same consumer attention. As to the first property, categories group apps of similar functionality. For example, “communications” labels apps that connect people, such as instant messaging and video conferencing, whereas “photography” is a label for apps that assist in capturing, editing, managing, storing or sharing photos. For the second property, categories allow consumers to explore apps that serve a similar purpose, such as photography apps. Empirically, categories reduce heterogeneity among apps: User preferences, development costs, and prices of apps in the same category are likely to be correlated.

Because Google published Photos in the category “photography,” we define apps in the category “photography” as the treatment group. We chose apps in the category “entertainment” as the control group. The selection of an appropriate control group is a matter of theoretical reasoning and empirical observation. From a theoretical perspective, entertainment apps are suitable because they have a comparably narrow functional purpose and are unlikely to overlap with photography apps. For example, entertainment apps include television program overviews or video streaming apps, but not pure entertainment content. Our findings remain robust when we use categories other than “entertainment” as the control group. Empirically, among all categories, entertainment apps showed the highest similarity in terms of the distribution of major updates, ratings, reviews, and prices before entry. By focusing on two categories, we assume that we substantially minimized the unobserved heterogeneity among the hundreds of thousands of apps in the Google Play Store. We address potential concerns about our choice of control group when assessing the robustness of our results. Our regressions follow a DID framework (Angrist and Pischke 2009, Bertrand et al. 2004). To allow enough time for estimating pre-entry diferences, we define a three-month period, March 1, 2015 to May 27, 2015, as the pre-entry period. Correspondingly, we define the period from June 1, 2015 to September 1, 2015 as the post-entry period.<sup>4</sup> Our final sample includes 1,266 treatment apps and 5,354 control apps, each observed over a six-month period, resulting in a total of 39,720 app-month observations.

## 3.5. Variables

We model innovation as the complementors’ decision to release a major update for their app, in terms of introducing new functionality or features. Our dependent variable is MAJOR UPDATE, which we constructed by text-analyzing the release notes that complementors publish along with updates of their apps.

We used text analysis to identify updates that introduce new features, and exclude non-innovative updates, including bug fixes and eficiency improvements. Prior work relies on release numbers (e.g., 2.0, 2.1) to distinguish minor from major updates (e.g., Boudreau 2012, Tiwana 2015). Although it is an informal convention that integer increases in release numbers indicate major updates (Kemerer and Slaughter 1999), this standard is ambiguous and not enforced in many contexts. Therefore, following Kemerer and Slaughter’s (1999) arguments, we used release notes to gain richer insights into complementary innovation. Release notes textually describe key aspects of an update. They provide detailed insights into the extent and novelty of the changes. Release notes are visible to users of the Google Play Store. They are displayed below the product description in a section entitled “What’s new,” making them an important aspect of communication between complementors and consumers. Release notes on the Google Play Store are limited to 500 characters, which requires complementors to be precise in their description of changes, thus making release notes an accurate document for our analyses.

Our approach to text analysis follows prior work that has used word lists (i.e., dictionaries) to objectively draw inferences from the text (Bao and Datta 2014). Dictionaries use keywords or phrases to classify documents into categories or measure the extent to which documents belong to a particular category (Bao and Datta 2014). We constructed dictionaries for minor and major updates by selecting a random subsample of 100 release notes from our sample and coding them into minor and major updates based on working definitions agreed on by the authors. Subsequently, in an iterative procedure, we identified key words used in the release notes of minor and major updates. The final dictionary for major updates includes, among other terms, the words “feature,” “new,” and “major.” We automated the dictionary-scoring using the Natural Language Toolkit in Python 2.7. We implemented an algorithm that first removed filler words, punctuation, and stop words from the release notes. We subsequently lemmatized the release notes, which gave us a list of unique words for each release note. We then scored our dictionaries against the condensed release notes, yielding a measure of “word hits” for each of the dictionaries.<sup>5</sup> We coded a release note as a major update if the dictionary for major updates scored higher on a release note compared to the dictionary for minor updates. In case of draws, we discussed the release note and coded it manually. Finally, we included the dichotomous variable MAJOR UPDATE into our model, which we coded as 1 for apps that were updated with new features in a given month and 0 for apps that received minor or no updates.

The conventional DID framework relies on two indicators, one for indicating treatment assignment and one for indicating the time period after the treatment. The treatment indicator is PHOTOS, which is 1 if the focal app is afected by Google’s release of Photos, i.e., if the app is in the treatment group. The time indicator is AFTER, which is 1 for the periods after the release of Photos. The DID is then given by interacting AFTER with PHOTOS.

We operationalize the racing mechanism by monthly diferences in app ratings (RATINGDIFF). According to the racing mechanism, increases in the innovation output of a complementor result from competitive pressure. The app rating system on Google Play ofers a unique opportunity to capture racing. Well rated apps are perceived to fulfill user expectations, to have an agreeable and engaging interface, and to be well suited to consumer needs. Decreases in app ratings are likely to capture the impact of competitive actions and have implications for complementors (Tiwana 2015,

Yin et al. 2014). RATINGDIFF is the monthly diference in consumers’ rating of an app on a scale from 1 to 5 stars, where 1 star represents a low rating and 5 stars represents a high rating. Thus, if racing efects trigger innovation increases, we should observe that these innovation increases are caused by deteriorating consumer ratings after entry.

We operationalize the attention spillover mechanism by monthly diferences in the number of app reviews (REVIEWSDIFF). According to the attention spillover mechanism, increases in the innovation output of a complementor result from increases in consumer attention. Monthly diferences in the number of app reviews capture changes in demand and feedback for an app. Prior research used the number of reviews as a proxy for consumer demand (Yin et al. 2014). In addition, reviews provide complementors with evaluations of multiple attributes of their app and help complementors understand consumer needs.<sup>6</sup> Thus, if attention spillover efects trigger innovation increases, we should observe that these innovation increases are caused by increasing numbers of consumer reviews after entry. We logged REVIEWSDIFF to reduce skewness.

Variables included in the additional analyses are PRICE, which is the price of an app in US\$, PORT-FOLIO SIZE, which is the count of total apps published by a complementor before the release of Photos, and PORTFOLIO DIVERSIFICATION, which is the number of categories in which a complementor had published apps before the release of Photos. See Online Appendix C for descriptions of the variables used in this study and how we obtained them from Google Play.

Table 1 reports the summary statistics and correlations.

## 3.6. Empirical Model

To estimate our main variable of interest, MAJOR UPDATE, we use the following specification:

$$
\begin{array}{c} M A J O R U P D A T E _ {i, t} = \beta_ {0} + \beta_ {1} A F T E R _ {t} \times P H O T O S _ {i} \\ + V _ {i} + T _ {t} + \epsilon_ {i, t}, \end{array}
$$

where MAJOR $U P D A T E _ { i , t }$ is measured in month t for app i, PHOTOS<sub>i</sub> is an indicator variable for whether app i is in the treatment group, AFTER<sub>t</sub> equals 1 if the current month is after the release of Photos, $V _ { i }$ are app fixed efects, and $T _ { t }$ are time fixed efects. App and time fixed efects are collinear with the main efects of AFTER and PHOTOS and are therefore omitted. The coeficient of interest is $\beta _ { 1 } ,$ which can be interpreted as the relative change of the treatment group, compared to the control group, caused by the treatment. We cluster heteroskedasticity-robust standard errors at the app level to adjust for the panel structure of the data. We also estimate continuous variables to assess the impacts of entry on price, reviews, and ratings. In these cases, the model specification is similar and follows the same notation as above.

Table 1. Summary Statistics and Correlations

<table><tr><td>Variable</td><td>Mean</td><td>S.D.</td><td>Min.</td><td>Max.</td><td>1</td><td>2</td><td>3</td></tr><tr><td>1. MAJOR UPDATE</td><td>0.01</td><td>0.07</td><td>0</td><td>1</td><td></td><td></td><td></td></tr><tr><td>2. log (REVIEWS(in thousands))</td><td>0.66</td><td>0.45</td><td>0.26</td><td>7.16</td><td>0.02</td><td></td><td></td></tr><tr><td>3. RATING</td><td>3.61</td><td>0.41</td><td>1.20</td><td>4.40</td><td>0.04*</td><td>0.16*</td><td></td></tr><tr><td>4. PRICE (in US$)</td><td>0.12</td><td>0.79</td><td>0</td><td>42.60</td><td>-0.01</td><td>-0.05*</td><td>-0.08*</td></tr></table>

Notes. The table provides descriptive statistics for the variables used in this paper. MAJOR UPDATE is an indicator variable (1 <sup></sup> apps that received a “major update”) that we derived from classifying the change logs published by complementors. RATING is the mean rating given by consumers to an app, which can range from 1 to 5 stars. REVIEWS is the count of reviews submitted for an app. PRICE holds the purchase price of an app in US\$. N <sup></sup> 39,720 app-months.  
<sup>∗</sup>Significance at the 5% level.

## 4. Results

## 4.1. Efects of Entry on Innovation

To investigate whether entry crowds out complementary innovation, we examine the change in the likelihood of a major update between treatment and control apps after the release of Photos. Table 2 shows our estimations, specified as a linear probability model (LPM) in Model 1 and as logit in Model 2. In Model 1, we observe a statistically significant positive coeficient of AFTER <sup>×</sup> PHOTOS, which indicates that the probability of MAJOR UPDATE increases by 9.6% after entry for treatment apps compared to that for the control apps. The increase in the likelihood suggests that Google’s entry positively influenced complementary innovation.

As Model 2 in Table 2 shows, the finding is robust to a logit formulation. The predicted probabilities are between 0 and 1. Thus, the potential bias of the LPM that is evident if predicted values lie outside the range of 0 and 1 is not an issue for our estimation. We focus on LPM specifications hereafter because it enables us to estimate a model using extensive app-level fixed efects, whereas estimating logit models using a large number of fixed efects may lead to inconsistent standard errors (Long and Freese 2006).

Figure 2 plots the marginal probability of MAJOR UPDATE with the vertical line marking Google’s release of Photos. We observe that treatment and control apps are on nearly identical trends before entry, which provides evidence for the assumption of parallel pre-period trends. We also observe that the likelihood of MAJOR UPDATE shows a significant peak after entry, whereas the time trend continues for control apps. Taken together, we find a significant shift in complementary innovation after entry: It is more likely that complementors release major updates for their apps following entry.

Table 2. Efect of Entry on MAJOR UPDATE

<table><tr><td></td><td>(1)Major update</td><td>(2)Major update</td></tr><tr><td>Specification</td><td>LPM</td><td>Logit</td></tr><tr><td>Photos</td><td></td><td>0.259(0.181)</td></tr><tr><td>After × Photos</td><td>0.096***(0.009)</td><td>1.472***(0.193)</td></tr><tr><td>Intercept</td><td>0.005***(0.001)</td><td>-5.382***(0.187)</td></tr><tr><td>App fixed effects</td><td>Yes</td><td>No</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Adj./Pseudo R-squared</td><td>0.039</td><td>0.121</td></tr><tr><td>F/Wald test</td><td>63.180***</td><td>658.51***</td></tr></table>

Notes. The table shows the regression results of the change in the likelihood of a MAJOR UPDATE following the release of Google Photos, compared with control apps. Model 1 reports the results of an LPM; Model 2 shows the logit estimates in regular coeficient notation. In both models, the estimate of interest After <sup>×</sup> Photos indicates a strongly positive increase in the probability of MAJOR UPDATE following entry, compared to control apps. Robust standard errors are clustered on app and given in parentheses. N <sup></sup> 39,720 app-months. <sup>∗∗∗</sup>Significance at the 0.1% level.

Figure 2. Marginal Probability of MAJOR UPDATE Over Time  
![](/api/attachments/5WZTV62D/fulltext/images/12c3d85b2b55a296239109072f6104d2baaa1df212a8ed7dfacb4a44791031bf.jpg)  
Notes. The figure plots the marginal probability of MAJOR UPDATE over time as estimated by a logit specification. The solid line gives the marginal probability for apps afected by the release of Photos (treatment) and the dashed line gives the marginal probability for apps not afected (control). The figure illustrates the nearly identical pre-entry trends and the significantly increased probability of MAJOR UPDATE following entry. Note that this plot does not adjust for app fixed efects.

## 4.2. Analyses of Mechanisms

If entry does not crowd out innovation, what theoretical mechanisms underlie this efect? We motivated racing and attention spillover mechanisms as two potential explanations. To assess the validity of these explanations, we follow Baron and Kenny’s (1986) three-step procedure for mediation analysis.

Because the first step of the analysis is given by regressing MAJOR UPDATE on AFTER<sup>×</sup>PHOTOS, we proceed with the second step, i.e., estimating the efects of entry on the mediators. Table 3 shows the results. In Model 1, we observe that entry does not have a significant efect on RATINGDIFF. The coeficient of AFTER <sup>×</sup> PHOTOS is near 0 and insignificant. Thus, Model 1 does not support the second step of the mediation analysis for the racing mechanism. In Model 2, we estimate the second step of the mediation analyses for the attention spillover mechanism. We observe that entry has a significant positive efect on REVIEWS-DIFF. The significant coeficient of AFTER <sup>×</sup> PHOTOS shows that apps afected by entry receive more consumer reviews than those not afected by entry. This finding indicates that entry increases consumer attention to apps in the same category as the entering app. Thus, Model 2 supports the second step of mediation analysis in assessing the attention spillover efect.

Table 3. Efect of Entry on RATINGDIFF and REVIEWSDIFF

<table><tr><td rowspan="2">Specification</td><td>(1)RATINGDIFF</td><td>(2)REVIEWSDIFF</td></tr><tr><td>Linear</td><td>Linear</td></tr><tr><td>After × Photos</td><td>-0.002(0.003)</td><td>0.086***(0.014)</td></tr><tr><td>Intercept</td><td>-0.000(0.000)</td><td>0.002(0.002)</td></tr><tr><td>App fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Adj. R-squared</td><td>0.008</td><td>0.215</td></tr><tr><td>F-test</td><td>30.556***</td><td>1,355.367***</td></tr></table>

Notes. The table shows the regression results for RATINGDIFF (Model 1) and REVIEWSDIFF (Model 2). Model 1 does not support a significant change in RATINGDIFF. Model 2 supports a significant positive change in REVIEWSDIFF. Robust standard errors are clustered on app and given in parentheses. N <sup></sup> 39,720 app-months.  
<sup>∗∗∗</sup>Significance at the 0.1% level.

Finally, we assess the third step of the mediation analysis. Table 4 shows the results. Model 1 provides the baseline. In Model 2, the coeficient of RAT-INGDIFF is insignificant, thus providing no support for a mediation efect of RATINGDIFF. Taken together with the findings from step 2, we conclude that racing efects are unlikely to explain the observed positive efect of entry on MAJOR UPDATE. In Model 3 in Table 4 we observe a significant positive coeficient of REVIEWSDIFF and we observe that the coeficient of AFTER<sup>×</sup>PHOTOS decreases in magnitude and statistical significance. Taken together with the findings from step 2, these observations suggest a partial mediation of the efect of AFTER <sup>×</sup> PHOTOS on MAJOR UPDATE via REVIEWSDIFF, which is supported by Sobel (p < 0.001), Aroian $( p < 0 . 0 0 1 )$ , and Goodman (p < 0.001) tests. In Model 4, we simultaneously test the racing and attention spillover mechanisms, and find that the efect of REVIEWSDIFF on MAJOR UPDATE remains significant while the efect of RATINGDIFF remains nonsignificant. Thus, the release of Photos seems to lead to an increase in consumer attention to photography apps in general, from which complementors stand to benefit, thereby explaining why we observe a higher likelihood of major updates in the afected category.<sup>7</sup>

Table 4. Efect of RATING and NUMBER OF REVIEWS on MAJOR UPDATE

<table><tr><td rowspan="2">Specification</td><td>(1) Major update</td><td>(2) Major update</td><td>(3) Major update</td><td>(4) Major update</td></tr><tr><td>LPM</td><td>LPM</td><td>LPM</td><td>LPM</td></tr><tr><td>After × Photos</td><td>0.096***(0.009)</td><td>0.094***(0.009)</td><td>0.037***(0.005)</td><td>0.036***(0.005)</td></tr><tr><td>Ratingdiff</td><td></td><td>0.004(0.008)</td><td></td><td>0.010(0.008)</td></tr><tr><td>Reviewsdiff</td><td></td><td></td><td>0.482***(0.032)</td><td>0.474***(0.032)</td></tr><tr><td>Intercept</td><td>0.005***(0.001)</td><td>0.004**(0.001)</td><td>0.005***(0.001)</td><td>0.004***(0.001)</td></tr><tr><td>App fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Adj. R-squared</td><td>0.039</td><td>0.033</td><td>0.177</td><td>0.156</td></tr><tr><td>F</td><td>63.180***</td><td>58.952***</td><td>92.750***</td><td>86.689***</td></tr></table>

Notes. The table shows the regression results of the final step of the mediation analysis. Model 1 reports the baseline; Model 2 adds RATINGDIFF; Model 3 adds REVIEWSDIFF to the baseline; Model 4 adds RATINGDIFF and REVIEWSDIFF. Robust standard errors are clustered on app and given in parentheses. N <sup></sup> 39,720 app-months. Significance at the 0.1% level.

## 4.3. Further Analyses: Do the Efects of Entry Difer Depending on Complementors’ Resources or Diversification?

So far, our analyses suggest (1) that entry stimulates complementary innovation and (2) that this efect can be explained by an attention spillover mechanism. Next, we explore additional context factors for these two findings. One set of context factors in which we are interested concerns characteristics of complementors app portfolios in terms of diferent sizes of complementors’ app portfolios (PORTFOLIO SIZE) as well as complementors’ degree of diversification in the app market over categories (PORTFOLIO DIVERSIFICATION).

First, we explore whether PORTFOLIO SIZE and PORTFOLIO DIVERSIFICATION influence the likelihood of a MAJOR UPDATE after entry. To examine the influence of PORTFOLIO SIZE, we split the sample into three quantile groups based on the portfolio size of complementors (low, medium, high). Table 5 shows the results when estimating our main model for each quantile group. In all three models, the DID coefficient is positive and strongly significant, supporting the main conclusions we derived earlier. Interestingly, we see diferences in the magnitude of the reactions of complementors depending on the size of their portfolio: In Model 1, we observe that small portfolio complementors are less likely to update their photography apps compared to large portfolio complementors with a larger stock of apps, as shown in Model 3. Overall, the likelihood of complementors with large portfolios issuing updates is approximately twice that of complementors with smaller stocks of apps.

Table 5. Analyses by PORTFOLIO SIZE

<table><tr><td rowspan="2"></td><td>(1)Majorupdate</td><td>(2)Majorupdate</td><td>(3)Majorupdate</td></tr><tr><td>Low quantilegroup ofPORTFOLIOSIZE</td><td>Medium quantilegroup ofPORTFOLIOSIZE</td><td>High quantilegroup ofPORTFOLIOSIZE</td></tr><tr><td>Specification</td><td>LPM</td><td>LPM</td><td>LPM</td></tr><tr><td>After × Photos</td><td>0.068***(0.010)</td><td>0.113***(0.018)</td><td>0.138***(0.021)</td></tr><tr><td>Intercept</td><td>0.005**(0.002)</td><td>0.006*(0.003)</td><td>0.004(0.003)</td></tr><tr><td>App fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Adj. R-squared</td><td>0.024</td><td>0.051</td><td>0.064</td></tr><tr><td>F</td><td>23.973***</td><td>16.866***</td><td>24.057***</td></tr><tr><td>N</td><td>21,936</td><td>9,774</td><td>8,010</td></tr></table>

Notes. The table shows the regression results of additional analyses based on the portfolio size of complementors. Robust standard errors are clustered on app and given in parentheses. N is given in appmonths.  
<sup>∗∗∗</sup>Significance at the 0.1% level.

We also investigate the efect of entry on MAJOR UPDATE difers depending on complementors’ diversification (see Table 6). We again split the sample into three quantile groups based on PORTFOLIO DIVER-SIFICATION (low, medium, high). Table 6 shows the results when estimating our main model for each quantile group. In all three models, the DID coeficient is positive and strongly significant, supporting our earlier findings. Similar to our findings for PORTFO-LIO SIZE, more diversified afected complementors are more likely to release a major update following the release of Photos, compared to complementors with more focused portfolios.

Second, we examine the role of PORTFOLIO SIZE and PORTFOLIO DIVERSIFICATION for the salience of the racing and attention spillover mechanisms. Although our focus is on understanding how Google’s entry influenced complementary innovation, the complementors’ decision to innovate is not entirely a function of the platform owner’s decisions because the innovation trajectory of a platform is often an outcome of complex and dynamic sociotechnical negotiations between the platform owner and complementors (Eaton et al. 2015).

Table 6. Analyses by PORTFOLIO DIVERSIFICATION

<table><tr><td></td><td>(1)Major update</td><td>(2)Major update</td><td>(3)Major update</td></tr><tr><td>Subsample</td><td>Low-quantile group of PORTFOLIO DIVERSIFICATION</td><td>Medium-quantile group of PORTFOLIO DIVERSIFICATION</td><td>High-quantile group of PORTFOLIO DIVERSIFICATION</td></tr><tr><td>Specification</td><td>LPM</td><td>LPM</td><td>LPM</td></tr><tr><td>After × Photos</td><td>0.089***(0.013)</td><td>0.098***(0.012)</td><td>0.114***(0.025)</td></tr><tr><td>Constant</td><td>0.005*(0.002)</td><td>0.003*(0.002)</td><td>0.010*(0.004)</td></tr><tr><td>App fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Adj. R-squared</td><td>0.035</td><td>0.040</td><td>0.047</td></tr><tr><td>F</td><td>24.283***</td><td>27.732***</td><td>13.771***</td></tr><tr><td>N</td><td>15,774</td><td>18,930</td><td>5,016</td></tr></table>

Notes. The table shows the regression results of additional analyses based on the portfolio diversification of complementors. Robust standard errors are clustered on app and given in parentheses. N is given in app-months.  
<sup>∗</sup>Significance at the 5% level; <sup>∗∗∗</sup>significance at the 0.1% level.

Arguably, racing and spillover efects may be viewed as creating diferent types of incentives to innovate for complementors. Whereas racing efects may be viewed as a threat or as a negative incentive to defend against a potentially powerful entrant or platform owner, attention spillover efects can be viewed from an opportunity perspective, in terms of representing a positive incentive by enlarging overall consumer interest in the market niche. Therefore, whether entry is considered a threat or an opportunity depends not only on the specific innovations or actions of a platform owner but also on complementor characteristics. If complementors cannot take advantage of a “growing pie,” they are likely to see entry as a threat. In this case, the motivation for complementors to increase their innovative eforts may be to counteract this threat. On the other hand, if complementors are well endowed with resources, then they may view a platform owner’s entry as an opportunity and the motivation for increasing innovation eforts may be to participate in the growing pie. This discussion suggests that for complementors that are more resourceful and diverse (diversity may create some synergy with their other products), the attention spillover efect may apply, whereas for those that are less resourceful and diverse, the racing efect may be more salient.

To test these assertions, we examined whether the racing and attention spillover mechanisms are more or less salient depending on complementors’ PORT-FOLIO SIZE and PORTFOLIO DIVERSIFICATION. Models 1a and 1b of Table 7 show the low and high quantile groups and provide the baseline for our analysis of the role of complementors’ portfolio size. Models

2a and 2b show that the attention spillover efect is of greater valence for developers with more apps (0.592 versus 0.404). By contrast, we do not find support for a racing efect: The coeficient of RATINGDIFF is close to 0 and has no significant efect on a developer’s likelihood to release an update, independent of their portfolio size.

Models 3a and 3b in Table 7 show the low and high quantile groups and provide the baseline for our analysis of the role of complementors’ diversification. Models 4a and 4b show that the attention spillover efect is slightly stronger for more diversified complementors (0.494 versus 0.462). We find no substantial support for a racing mechanism. In Model 4a, the coeficient of RATINGDIFF is insignificant. In Model 4b, the coeficient is weakly significant, close to 0, and in the opposite direction (i.e., positive; recall that the racing mechanism suggests that complementors increase innovation activities in response to deteriorating ratings).

Taken together, we find a stronger efect of entry for larger and more diversified complementors. One plausible explanation might be that larger and more diversified complementors perceive entry as an opportunity to innovate rather than a threat. As entry increases demand for a category, a category becomes more attractive to complementors, thus attracting investments from complementors with more resources.

## 4.4. Robustness Checks

Whereas our main results are stable across diferent specifications, consistently pointing to the finding that entry did not crowd out innovation, there are several alternative explanations. Next, we discuss five approaches to ensure the robustness of our findings.

Table 7. Mediation Analyses Split by PORTFOLIO SIZE and PORTFOLIO DIVERSIFICATION

<table><tr><td>(1a)Majorupdate</td><td>(1b)Majorupdate</td><td>(2a)Majorupdate</td><td>(2b)Majorupdate</td><td>(3a)Majorupdate</td><td>(3b)Majorupdate</td><td>(4a)Majorupdate</td><td>(4b)Majorupdate</td></tr></table>

<table><tr><td>Subsample</td><td>Low-quantile group of PORTFOLIO SIZE</td><td>High-quantile group of PORTFOLIO SIZE</td><td>Low-quantile group of PORTFOLIO SIZE</td><td>High-quantile group of PORTFOLIO SIZE</td><td>Low-quantile group of PORTFOLIO DIVERSIFICATION</td><td>High-quantile group of PORTFOLIO DIVERSIFICATION</td><td>Low-quantile group of PORTFOLIO DIVERSIFICATION</td><td>High-quantile group of PORTFOLIO DIVERSIFICATION</td></tr><tr><td>Specification</td><td>LPM</td><td>LPM</td><td>LPM</td><td>LPM</td><td>LPM</td><td>LPM</td><td>LPM</td><td>LPM</td></tr><tr><td>After × Photos</td><td>0.068***(0.010)</td><td>0.138***(0.021)</td><td>0.030***(0.007)</td><td>0.034**(0.011)</td><td>0.089***(0.013)</td><td>0.114***(0.025)</td><td>0.035***(0.009)</td><td>0.034***(0.010)</td></tr><tr><td>Ratingdiff</td><td></td><td></td><td>0.007(0.010)</td><td>-0.009(0.022)</td><td></td><td></td><td>0.014(0.012)</td><td>0.037*(0.017)</td></tr><tr><td>Reviewsdiff</td><td></td><td></td><td>0.404***(0.043)</td><td>0.592***(0.049)</td><td></td><td></td><td>0.462***(0.063)</td><td>0.494***(0.057)</td></tr><tr><td>Intercept</td><td>0.005**(0.002)</td><td>0.004(0.003)</td><td>0.004**(0.001)</td><td>0.004(0.003)</td><td>0.005*(0.002)</td><td>0.010*(0.004)</td><td>0.005*(0.002)</td><td>0.004(0.003)</td></tr><tr><td>App fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Adj. R-squared</td><td>0.024</td><td>0.064</td><td>0.12</td><td>0.20</td><td>0.035</td><td>0.047</td><td>0.14</td><td>0.16</td></tr><tr><td>F</td><td>24.0***</td><td>24.1***</td><td>30.5***</td><td>41.3***</td><td>24.3***</td><td>13.771***</td><td>29.7***</td><td>25.5***</td></tr><tr><td>N</td><td>21,936</td><td>8,010</td><td>21,936</td><td>8,010</td><td>15,774</td><td>5,016</td><td>15,774</td><td>5,016</td></tr></table>

<sup>∗</sup>Significance at the 5% level; <sup>∗∗</sup>significance at the 1% level; <sup>∗∗∗</sup>significance at the 0.1% level.  
Notes. The table shows the regression results of additional analyses based on the portfolio size and diversification of complementors. Robust standard errors are clustered on app and given in parentheses. N is given in app-months.

First, there may be concerns about our measure of innovation, which relies on app updates. We used new app releases as an alternative proxy to check the robustness of our measure of innovation. For each category, Google maintains a ranked list of the top 500 paid and free apps that were newly released or updated within the last 30 days. Although Google does not specify further conditions for membership in the ranking, analyzing fluctuations in the lists allows us to draw inferences on the number of new apps released to the photography category compared to other categories. We collected monthly snapshots of the Top 500 rankings for each category in the Google Play Store over 2015. For each category-month, we then counted the apps that entered the rankings for the first time in 2015. We then averaged the entrant count over the pre- and post-treatment periods.

Figure 3 compares the average monthly new entrants for the photography category with the average monthly new entrants per category in the Google Play Store before and after entry. We observe a substantial increase in entrants in the photography category compared to all other categories. When estimating the results using ordinary least squares (OLS) regressions and category fixed efects, the diference is significant at conventional levels $( p < 0 . 0 5 )$ . The results support the validity of our main finding that Google’s entry increased complementary innovation.

Figure 3. Average Monthly Entrants into the Top 500 New Apps Rankings for the Photography Category and Others, Before and After the Release of Photos  
![](/api/attachments/5WZTV62D/fulltext/images/2f9ce79d7142476b46e7a4d31696299fb6e7abcede31adf6fd419ca378e83c3e.jpg)  
Notes. The figure plots the average monthly entrants per category into the top 500 new apps rankings for the “photography” category as compared to all other categories in the Google Play Store, before and after the release of Photos. The whiskers give the standard errors.

Second, we tested for heterogeneity between treatment and control groups. We investigated the assumption underlying the DID approach that sorting into treatment and control groups is random. We tested whether apps in the treatment and control groups are statistically indistinguishable in terms of pre-entry observational characteristics. We observe in Table 8 that prior to entry, treatment and control apps show similar characteristics: They have the same likelihood of major update, the same average rating, receive a similar number of reviews, and have the same average price. Despite observational equivalence, however, there may still be an unobserved heterogeneity in the time trends between treated and untreated apps that our previous analyses did not reveal. Although we have safeguarded our estimations by including time fixed efects, there is the possibility that treatment and control apps were on diferent pre-treatment time trends. To assess diferences in such trends, we follow the procedure proposed by Bertrand et al. (2004) and estimate models where we interact a continuous time indicator (TIME TREND) with the treatment indicator PHOTOS for the pre-entry periods. Table 9 shows estimations of pre-entry time trends for major update, rating, reviews, and price. The estimates suggest that there is a time trend in some of the outcomes used, but that this trend is identical for apps afected by treatment and for control apps. The estimated coeficient of PHOTOS <sup>×</sup> TIME TREND is not statistically diferent from 0, further supporting our choice of the control group. The results reinforce the claim that our fixed efects strategy has efectively controlled for ex ante heterogeneity in the groups.

Table 8. Robustness Check for Pre-Entry Heterogeneity of Treatment and Control Groups

<table><tr><td></td><td>(1) Major update</td><td>(2) Ratingdiff</td><td>(3) Reviewsdiff</td><td>(4) Price</td></tr><tr><td>Specification</td><td>LPM</td><td>Linear</td><td>Linear</td><td>Linear</td></tr><tr><td>Photos</td><td>0.007(0.007)</td><td>0.006(0.019)</td><td>0.017(0.018)</td><td>0.033(0.034)</td></tr></table>

Notes. The table shows the regression results of assessing pre-entry diferences of apps afected by entry and apps not afected. The intercept is omitted for the sake of brevity. The estimates indicate no significant diferences. Robust standard errors are clustered on app and given in parentheses. N <sup></sup> 19,860 in app-months.  
<sup>∗</sup>Significance at the 5% level; <sup>∗∗</sup>significance at the 1% level; <sup>∗∗∗</sup>significance at the 0.1% level.

Third, we conducted falsification tests to ensure that our research design appropriately isolates the efect of entry. Our research design is based on the assumption that the release of Photos only afected photography apps. We observed that entry did not afect our control group of entertainment apps, which gives confidence that the reaction to the treatment was as expected, in terms of afecting photography apps. If we observe, in addition, that entry did not alter complementors’ decision to update their apps in any category of the Android ecosystem other than photography, then this should provide substantial evidence for the identifying assumption of our research design. To investigate this possibility, we reestimated our core regression predicting the likelihood of a MAJOR UPDATE for each app category in our sample. Online Appendix E summarizes these reestimations using the apps within each category as a subsample. The results support our identifying assumption, i.e., that the release of Photos was associated with significant changes in MAJOR UPDATE only in the category for photography apps.

Table 9. Robustness Check for Pre-Entry Parallel Trends of Treatment and Control Groups

<table><tr><td rowspan="2">Specification</td><td>(1) Major update</td><td>(2) Ratingdiff</td><td>(3) Reviewsdiff</td><td>(4) Price</td></tr><tr><td>LPM</td><td>Linear</td><td>Linear</td><td>Linear</td></tr><tr><td colspan="5">Predictors</td></tr><tr><td>Time trend</td><td>0.006***(0.001)</td><td>-0.013***(0.002)</td><td>0.000(0.001)</td><td>-0.000(0.000)</td></tr><tr><td>Photos × Time trend</td><td>0.002(0.001)</td><td>0.001(0.001)</td><td>0.003(0.002)</td><td>0.000(0.002)</td></tr></table>

Notes. The table shows the regression results of assessing pre-entry diferences in time trends of apps afected by entry and apps not afected. The intercept is omitted for the sake of brevity. The estimates indicate no significant diferences. Robust standard errors are clustered on app and given in parentheses. N <sup></sup> 19,860 app-months.  
<sup>∗∗∗</sup>Significance at the 0.1% level.

Fourth, we used an alternative identification strategy based on a more granular measure of similarity between apps based on Hoberg and Phillips (2010). Even within the photography category, some apps may be more similar to Photos than others, thus apps within the photography category may difer as to how they are afected by entry. Therefore, we constructed an additional measure of app similarity by computing the cosine similarity of the descriptions of apps to the description of Photos (Hoberg and Phillips 2010). This measure has the advantage of being a continuous indicator of treatment. Mathematically, the cosine similarity is a measure of similarity between two vectors of an inner product space in terms of the cosine of the angle between these two vectors. This procedure yielded a measure of PHOTOS OVERLAP defined between 0 and 1, where higher values indicate a higher similarity of an app with Photos. We then reestimated our models using PHOTOS OVERLAP as the treatment indicator for apps afected by entry. Online Appendix F summarizes the procedure and the estimates obtained. The analyses confirm our main finding. We observe positive and significant efects of entry on MAJOR UPDATE and a mediating efect of REVIEWSDIFF on MAJOR UPDATE. The coeficients show similar signs and significance as in our main estimation. In sum, when using PHOTOS OVERLAP as a treatment indicator, we find support for our main results.

Although we believe that the “photography” category is a reasonable choice for assessing the treatment efects and despite reasons that apps in the “social” category may not be a good fit as a treatment group, we also assessed the reactions of complementors in the social category.<sup>8</sup> In particular, we ran analyses in which we extended the treatment group to include both apps in the categories “photography” and “social.” See Online Appendix G for the resulting estimates. When extending the treatment group to “social” apps, we find our main estimates confirmed. However, extending the treatment group leads to weaker efect magnitudes and lower explained variance. Thus, “social” apps appear to be less afected by the release of Photos, strengthening the use of “photography” apps to isolate the efects. We also computed the cosine similarity (Hoberg and Phillips 2010) between the description texts of apps in the “social” category and Photos to obtain a broad indicator of the similarity between apps in the “social” category and Photos. The mean cosine similarity we obtained is 0.162 (0.094), which is significantly lower than the mean cosine similarity between “photography” apps and Photos, which is 0.284 (0.136). Therefore, we conclude that using the “photography” category as the treatment group is appropriate.

## 5. Discussion

## 5.1. Main Findings

Our goal in this study was to understand the consequences of a platform owner’s decision to enter the market complementary to its platform for complementary innovation as well as implications for platform governance. We assessed the consequences of entry by exploiting a quasi-experiment in the context of Google Photos, an Android app that Google released in May 2015.

Our results yield three major findings. First, the release of Google Photos triggered an increase in complementary innovation. We estimate a 9.6% increase in the likelihood of a major update for apps afected by Google’s entry, compared to apps not afected by entry. This efect is robust to alternative specifications of innovation and various choices of the control group, and accounts for any time-invariant app-level heterogeneity.

Second, we found that the increase in complementary innovation is likely to result from an attention spillover efect, and not from a racing efect. For photo management apps, there was a strong increase in consumer attention as inferred from diferences in the number of reviews they received following Google’s market entry, thereby creating a new and strong incentive for complementors to innovate.

Finally, we found that the attention spillover efect is particularly pronounced for resourceful complementors. One plausible explanation is that complementors with a larger or more diversified portfolio of apps perceive a platform owner’s entry and the consequent increase in consumer attention for a category as an opportunity as opposed to a threat, and therefore may direct their eforts toward that particular category.

## 5.2. Contributions

Our study makes three main contributions. First, we provide evidence on the influence of platform owners’ entry on complementary innovation. Entry represents a key decision in platform governance as it may allow platform owners to appropriate rents, foster integration, and retain control over platform evolution (Farrell and Katz 2000, Gawer and Henderson 2007). Because prior work on the economics of multi-sided markets viewed entry as a means to recoup investments and argued that entry will erode complementors’ innovative eforts (e.g., Farrell and Katz 2000, Hagiu and Spulber 2013), our findings suggesting that entry fosters complementary innovation contribute novel insights to this discussion. Our findings also relate to prior work from a strategy perspective that stressed the importance of platform leadership and commitment to not squeezing complementors by infusing too much competition (e.g., Cusumano and Gawer 2002, Wareham et al. 2014). We extend this work because our findings suggest that entry may be one way to show platform leadership as it gives complementors opportunities to successfully innovate.

The second contribution of this paper is to untangle supply-side and demand-side explanations, i.e., whether entry triggers a complementor-side racing mechanism (Barnett and Hansen 1996, Barnett and Pontikes 2008) or a consumer-side attention spillover mechanism (Liu et al. 2014, Sahni 2016). While racing and attention spillover mechanisms have been described before, this study documents their relative salience in influencing complementary innovation. The finding that the positive efects of entry on complementary innovation are driven by demand-side attention spillover efects while there was no evidence for supply-side racing efects can be interpreted in light of same-side and cross-side network efects (Eisenmann et al. 2006, Parker and Van Alstyne 2005).

Our finding that the observed innovation efects are not related to racing efects means that Google’s entry did not substantially stimulate complementorside direct network efects (see Online Appendix H). Instead, Google’s entry seemed to stimulate cross-side network efects, in terms of an indirect efect triggered via the consumer side. Thus, entry could be interpreted as reinforcing the cross-side positive network efects that helped the platform ignite and grow.<sup>9</sup>

Extending the work on platform engineering and design (e.g., Eaton et al. 2015, Ghazawneh and Henfridsson 2013), our work suggests that entry into complementary markets may not only help platform owners control the quality of add-on functionality in terms of securing such functionality but that it may also provide a resourcing instrument as entry provides complementors with “digital real estate [. . .] available for their own innovations” (Parker et al. 2016, p. 175). In addition, we contribute to the work on consumer attention by outlining potential consequences of attention spillovers on complementary innovation as an important outcome for many firms (e.g., Li and Agarwal 2017, Liu et al. 2014).

Our final contribution is an improved understanding of the conditions that afect the salience of attention spillover efects. We extend prior work by suggesting that attention spillover efects may create stronger incentives to innovate for some complementors than for others and by identifying specific characteristics of complementors that afect the salience of attention spillover efects (Boudreau 2017). Considered in the light of work on platform governance, we contribute to a stream of research that recognizes diferences in the characteristics and behaviors of complementors (Boudreau 2017, Boudreau and Jeppesen 2015).

## 5.3. Research Implications

Our study suggests at least three implications for research. First, our research has implications for understanding the efects of entry on complementary innovation. Although focusing on whether platform owner’s entry into complementary markets promotes or hurts innovation is important, there is a need to understand conditions that explain when the efects will be beneficial or detrimental. These conditions may be related to the heterogeneity across platforms in that not all platforms are “born equal” (see Thomas et al. 2014). Such heterogeneity can arise from the design, context, and evolution of a platform.

From a design perspective, the diferences between product platforms and digital platforms may explain the difering efects of entry. Whereas product platforms are based on single design hierarchies that coordinate distributed product development, such as in supply chains or alliances (Gawer 2014), digital platforms are based on layered design hierarchies developed for uncoordinated innovation (Yoo et al. 2010), such as in our study context. Complementor behavior on product platforms may deviate from the behavior observed on digital platforms as more recent studies indicate (Boudreau 2017, Boudreau et al. 2017, de Reuver et al. 2017).

From a context perspective, the diference between consumer and enterprise platforms may explain the difering efects of entry. For example, attention spillover may be less salient in enterprise contexts because such contexts are often characterized by fewer platform adopters, higher switching costs or more sophisticated decision processes in client’s purchasing departments.

Finally, from an evolution perspective, platform owner’s market entry should be interpreted in light of a platform’s history. Whereas our study considers Google’s entry into the market for photography apps, additional insights may be obtained when considering a platform’s evolution. For example, Apple and Google have taken diferent approaches to governing their mobile platforms and balancing discipline and autonomy of complementors (Mithas and Kude 2017). Apple has been careful in opening its iPhone platform, allowing few key complements in the beginning, but gradually increasing access to the platform over time. By contrast, Google’s Android platform has traditionally shown a largely uncontrolled mode of governance. Over time, Google implemented a series of actions to regain control over its platform, especially with the goal of increasing complement quality and reducing device and software fragmentation. We call for future research on a platform’s evolution when studying market entries of platform owners. In the case of Google, this means that the release of Photos as well as complementary innovation should be studied considering Google’s control moves over time.

Second, our research has implications for understanding attention spillover and racing mechanisms in complementary markets. For attention spillover mechanisms, our research raises important questions related to their temporality and transferability. We call for future research exploring whether attention spillover is enduring. For complementors, if the efect is sustained, they might benefit from Google’s entry. For platform owners, if the efect is sustained, they have incentives to enter complementary markets not only to capture value but also to create new value. In addition, there is a need to understand whether attention spillover spreads to other platforms. For example, the release of the Google Photos app may also afect complementors on Apple’s iPhone platform, creating cross-platform innovation dynamics that require future research. Closely related is the question whether attention spillover mechanisms are triggered if a large firm other than the platform owner enters the complementary market. For example, in 2016, Nintendo announced the release of its classical game Super Mario for Apple’s platform. Large firms such as Nintendo have stronger market power than many of the small complementors, which poses questions as to whether such an entry may create similar attention spillover efects than the platform owner’s entry and how such an entry compares to the efects observed in this study. For the racing mechanism, future research should consider two factors describing ecosystem contexts: Power imbalance and ex ante information. Arguably, racing mechanisms may be muted when complementors deliberately avoid competition with the platform owner if market power is concentrated with the platform owner, whereas racing mechanisms might be more pronounced when power is more equally distributed between platform owners and complementors. Racing mechanisms might be afected by a platform owner’s upfront provision of information about a planned market entry. The availability of such ex ante information might influence a complementor’s eforts to match a platform owner’s entry.

Third, our research has implications for understanding how the outcomes of a platform owner’s governance decisions are influenced by heterogeneity among complementors (Boudreau 2017, Boudreau and Jeppesen 2015, Tiwana 2015). Our results suggest that the attention spillover mechanism is more pronounced among complementors that are well endowed with resources, in that they ofer apps in diferent categories, based on the argument that these complementors recognize the opportunities associated with increased customer attention. Future research may build on these insights and study the role of other complementor characteristics for the salience of attention spillover efects. For example, prior work has studied downstream capabilities and intellectual property rights as factors influencing complementors’ sales and the likelihood of an initial public ofering (Ceccagnoli et al. 2012). Future research may examine whether these and similar factors also have an efect on the salience of the attention spillover mechanism.

## 5.4. Policy and Managerial Implications

Our contributions have important policy and managerial implications. First, from a policy perspective, we provide some new insights for regulatory and antitrust investigations into whether a platform owner’s behavior afects consumer surplus and innovation. Our findings imply that Google’s entry attracted consumers to the focal market niche, which triggered more innovation from complementors at least in the short term. However, we do not discount the possibility that entry may have unintended consequences in the long run by deterring complementors from making investments in innovation that improves consumer choice and welfare. An implication of our research is that the standard economic models often used in antitrust analysis should consider the two independent sides in the context of platforms, i.e., consumers and complementors, and that regulators should consider the short-term and long-term implications of entry.

Second, our findings have implications for platform owners. As our study involves a well known instrument for governing complementary innovation, it informs platform owners of the direct consequences of their decision to enter complementary markets. Our research suggests that platform owners should consider the consumer-side attention spillover mechanism as a potential way to encourage complementary innovation. More broadly, the findings of this study highlight the need to focus on value creation logic and initiatives that leverage customer voice and customer involvement (e.g., design thinking and empathy with users) to enhance customer satisfaction (Hult et al. 2017, Saldanha et al. 2017) and innovation rather than on value appropriation logic focusing on competition among complementors.

Third, our findings have implications for complementors. At least in the short run, complementary innovations in our study seem to benefit from an increased inflow of consumer attention, whereas longterm consequences are dificult to assess based on our research design. A recent article in The Verge provides anecdotal evidence about a small developer for which the release of Google Photos in the long term “drove a dagger into the heart” of their products, cutting their revenues by almost one-third (Newton 2016). While our data does not allow generalizable analyses of potential monetary consequences, the discussion on actual profits of complementors and how that afects their future propensity for innovation in the app economy is important and requires further research.

Finally, our findings have implications for start-ups and entrepreneurs active in complementary markets. These firms usually fear that platform owners enter their market because they have comparably less power to defend their position. Our findings illustrate the implications of a platform owner’s entry into a popular niche in the complementary market such as photo management. It seems likely that small complementors face a trade-of between larger, popular market niches that might be prone to entry by the platform owner and less popular market niches in which entry might be less likely.

To conclude, in this study, we assessed the consequences of Google’s entry into the market for photography apps on its own Android platform in 2015. Our analyses suggest that complementors in the afected market category were more likely to update apps after Google’s entry. Our analyses support the explanation that the increased innovation does not represent a competitive response to entry but instead results from a spillover of consumer attention. This attention spillover efect was particularly pronounced for larger and more diversified complementors. These findings provide new insights to inform platform governance for leveraging complementary innovation, and should be informative for policy makers, platform owners, and entrepreneurs engaged in app development.

## Acknowledgments

The authors thank the special issue editors, the associate editor, and the anonymous reviewers; participants at the ISR Special Issue workshop at Warwick University; participants at the International Conference on Information Systems 2016 and the Platform Strategy Symposium 2016; participants in seminars at Imperial College, Warwick Business School, University of Memphis, University of Mannheim, University of

Maryland, Tsinghua University, and University of British Columbia. We thank Marshall van Alstyne, Kevin Boudreau, Siva Viswanathan, and Carsten Sørensen for helpful comments on previous versions of this paper.

## Endnotes

<sup>1</sup>The notion of uncoordinated and generative complementary innovation contrasts with the notion of product families and product platforms in the organizational literature on distributed product development (Thomas et al. 2014). Components in traditional modular architectures are product-specific (see Yoo et al. 2010), while components in layered modular architectures are product-agnostic, meaning that they can be bundled in a variety of unforeseen ways with other platform components or external components. We also distinguish between purposed and unpurposed innovation: Purposed innovation means that the platform owner seeks innovation in particular areas, ways, and points in time; unpurposed innovation means that the platform owner seeks to stimulate unprompted innovation without coordination.

<sup>2</sup> The Google Play Store is a distribution service ofered by Google. At the time of the study, it is the oficial app store for the Android operating system. The Google Play Store allows users to browse and download applications developed for Android and published through Google. The Google Play Store also ofers music, books, movies, and various other digital content.

<sup>3</sup> Google had largely refrained from releasing its own Android apps in the past that would have interfered with complementors. While Google ofered apps for their own services in Google Play, including email, camera or calendar, these services existed long before the Android platform. By contrast, Google’s major competitor, Apple, had entered complementary markets several times, e.g., in the cases of iBooks (2010), Find My Friends (2010), and Garage Band (2011). The release represented Google’s decision to decouple the photography features from its social network Google<sup>+</sup> and to combine it with the functionality of Google’s web and desktop photo service Picasa. See Online Appendix B for a timeline of events that lead to the introduction of the Google Photos Android app. Several articles in the trade press speculated that with Photos, Google not only intended to get a foothold in the market for photography apps but also to fuel Google’s advertising, cloud storage, and web service businesses. Parallel to the release of the Google Photos Android app, Google released a Google Photos web service and a Google Photos app to Apple’s App Store. In this paper, we focus solely on the impact of Photos on the market of photography apps on the Android platform. Although the trade press described Google<sup>+</sup> and Picasa as having superior functionality compared to their competitors, they also stated that each lacked an appropriate user base. In 2016, Google discontinued Picasa and announced a decision “to focus entirely on a single photo service in Google Photos” (Sabharwal 2015).

<sup>4</sup> Our choice of the pre-entry and post-entry periods is informed by prior work (Li and Agarwal 2017) but also resulted from trading of variance and standard errors. Longer periods may increase variance but may blur complementors’ reactions to entry because, with increasing length, we cannot exclude confounding events. In particular, Google released an update to its Android software development kits (SDKs) in late September, a new version of the Android operating system in October, and updated Photos with new features in December. To deliberately avoid potentially confounding events, we restricted our observation period to March–September.

<sup>5</sup> We ensured the validity of the computer-assisted text analysis by backward-coding a subset of the release notes. We drew a random sample of 100 release notes from our data set and let two independent research assistants code the release notes into minor and major updates based on our agreed on definitions. The results of this procedure increased our confidence that the algorithms used were accurately identifying major updates as the research assistants agreed in 96 of 100 cases with the algorithm-based coding. See Online Appendix D for exemplary release notes and their classification.

<sup>6</sup> Relying on the number of reviews is also advantageous compared to methods that infer demand from publicly available data on app ranks, such as that proposed in Garg and Telang (2013). Rank-based methods restrict potential investigations to ranked apps, whereas our approach ofers the advantage to study a representative sample.

<sup>7</sup> We assessed the plausibility of these mechanisms through informal conversations with complementors and industry experts to gain insights into the unique setting of this case.

<sup>8</sup> First, because Photos is listed in the “photography” category, it competes for consumer attention mostly with apps in the “photography” category rather than apps in the “social” category. Second, the social aspect of Photos, at least at the time of its introduction in 2015, is much less pronounced than for apps listed in the “social” category that also ofer photo functionality (e.g., Google<sup>+</sup>, Instagram). Although Photos has social functionality (e.g., tagging friends, sharing), most of the utility of the app derives from having a fully-fledged tool for organizing, editing, and safely storing photos. In fact, an important social feature of the app, i.e., shared albums, was first introduced three months after the end of our observation period. Therefore, we hypothesized that photography apps would be much more afected by the release of Photos as several hundred apps ofered functionality for editing, organizing, and storing photos. Finally, apps in the “social” category show very diverse functionality or purpose (e.g., Facebook, Blogger or Badoo), which might make it dificult to conclude that major updates of these apps are related to overlaps with Photos. We thank an anonymous reviewer for suggesting this additional analysis as a robustness check.

<sup>9</sup> We thank an anonymous reviewer for suggesting this discussion.

## References

Adner R, Kapoor R (2010) Value creation in innovation ecosystems: How the structure of technological interdependence afects firm performance in new technology generations. Strategic Management J. 31(3):306–333.

Anderson EG, Parker GG, Tan B (2014) Platform performance investment in the presence of network externalities. Inform. Systems Res. 25(1):152–172.

Angrist JD, Pischke JS (2009) Mostly Harmless Econometrics: An Empiricist’s Companion (Princeton University Press, Princeton, NJ).

Bao Y, Datta A (2014) Simultaneously discovering and quantifying risk types from textual risk disclosures. Management Sci. 60(6):1371–1391.

Barnett WP, Hansen MT (1996) The Red Queen in organizational evolution. Strategic Management J. 17(1):139–157.

Barnett WP, Pontikes EG (2008) The Red Queen, success bias, and organizational inertia. Management Sci. 54(7):1237–1251.

Baron RM, Kenny DA (1986) The moderator–mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations. J. Personality Soc. Psych. 51(6): 1173–1182.

Bertrand M, Duflo E, Mullainathan S (2004) How much should we trust diferences-in-diferences estimates? Quart. J. Econom. 119(1):249–275.

Boudreau K (2017) Amateurs: Low-cost development, market participation and innovation on digital platforms. Working paper, Northeastern University, Boston.

Boudreau K, Jeppesen LB, Miric M (2017) Freemium, network efects and digital competition: Evidence from the introduction of game center on the Apple appstore. Working paper, Northeastern University, Boston.

Boudreau KJ (2012) Let a thousand flowers bloom? An early look at large numbers of software app developers and patterns of innovation. Organ. Sci. 23(5):1409–1427.

Boudreau KJ, Hagiu A (2009) Platform rules: Multi-sided platforms as regulators. Gawer A, ed. Platforms, Markets and Innovation (Edward Elgar Publishing, Cheltenham, UK), 163–191.

Boudreau KJ, Jeppesen LB (2015) Unpaid crowd complementors: The platform network efect mirage. Strategic Management J. 36(12):1761–1777.

Brandenburger AM, Nalebuf BJ (1996) Co-Opetition (Doubleday, New York).

Brown SL, Eisenhardt KM (1995) Product development: Past research, present findings, and future directions. Acad. Management Rev. 20(2):343–378.

Ceccagnoli M, Forman C, Huang P, Wu DJ (2012) Cocreation of value in a platform ecosystem: The case of enterprise software. MIS Quart. 36(1):263–290.

Choi JP, Stefanadis C (2001) Tying, investment, and the dynamic leverage theory. RAND J. Econom. 21(1):52–71.

Cusumano MA, Gawer A (2002) The elements of platform leadership. MIT Sloan Management Rev. 43(3):51–58.

de Reuver M, Sørensen C, Basole RC (2017) The digital platform: A research agenda. J. Inform. Tech. 1–12.

Derfus PJ, Maggitti PG, Grimm CM, Smith KG (2008) The Red Queen efect: Competitive actions and firm performance. Acad. Management J. 51(1):61–80.

Eaton B, Elaluf-Calderwood S, Sørenson C, Yoo Y (2015) Distributed tuning of boundary resources: The case of Apple’s iOS service system. MIS Quart. 39(1):217–243.

Eisenmann T, Parker G, Van Alstyne MW (2006) Strategies for twosided markets. Harvard Bus. Rev. 84(10):92–101.

Farrell J, Katz ML (2000) Innovation, rent extraction, and integration in systems markets. J. Indust. Econom. 48(4):413–432.

Foerderer J, Kude T, Schuetz S, Heinzl A (2018) Knowledge boundaries in enterprise software platform ecosystems: Antecedents and consequences for platform governance. Inform. Systems J. 1–25.

Garg R, Telang R (2013) Inferring app demand from publicly available data. MIS Quart. 37(4):1253–1264.

Gawer A (2014) Bridging difering perspectives on technological platforms: Toward an integrative framework. Res. Policy 43(7):1239–1249.

Gawer A, Cusumano MA (2002) Platform Leadership: How Intel, Microsoft, and Cisco Drive Industry Innovation (Harvard Business School Press, Boston).

Gawer A, Henderson R (2007) Platform owner entry and innovation in complementary markets: Evidence from Intel. J. Econom. Management Strategy 16(1):1–34.

Ghazawneh A, Henfridsson O (2013) Balancing platform control and external contribution in third-party development: The boundary resources model. Inform. Systems J. 23(2):173–192.

Gilbert RJ, Katz ML (2001) An economist’s guide to U.S. v. Microsoft. J. Econom. Perspect. 15(2):25–44.

Hagiu A, Spulber D (2013) First-party content and coordination in two-sided markets. Management Sci. 59(4):933–949.

Hoberg G, Phillips G (2010) Product market synergies and competition in mergers and acquisitions: A text-based analysis. Rev. Financial Stud. 23(10):3773–3811.

Huang P, Mithas S, Tafti A (2018) Platform sponsor’s investments and user contributions in knowledge communities: The role of knowledge seeding? MIS Quart. 42(1):213–240.

Huang P, Ceccagnoli M, Forman C, Wu DJ (2013) Appropriability mechanisms and the platform partnership decision: Evidence from enterprise software. Management Sci. 59(1):102–121.

Huber T, Kude T, Dibbern J (2017) Governance practices in platform ecosystems: Navigating tensions between co-created value and governance costs. Inform. Systems Res. 28(3):563–584.

Hult GTM, Morgeson FV, Morgan NA, Mithas S, Fornell C (2017) Do managers know what their customers think and why? J. Acad. Marketing Sci. 45(1):37–54.

Katz ML, Shapiro C (1994) Systems competition and network efects. J. Econom. Perspect. 8(2):93–115.

Kemerer CF, Slaughter S (1999) An empirical approach to studying software evolution. IEEE Trans. Software Engrg. 25(4):493–509.

Li Z, Agarwal A (2017) The impact of platform integration on consumer demand in complementary markets: Evidence from Facebook’s integration of Instagram. Management Sci. 63(10): 3438–3458.

Liu Q, Steenburgh TJ, Gupta S (2014) The cross attributes flexible substitution logit: Uncovering category expansion and share impacts of marketing instruments. Marketing Sci. 34(1):144–159.

Long JS, Freese J (2006) Regression Models for Categorical Dependent Variables Using Stata (Stata Press, College Station, TX).

March JG (1991) Exploration and exploitation in organizational learning. Organ. Sci. 2(1):71–87.

Mithas S, Kude T (2017) Digitization and disciplined autonomy. IEEE IT Professional 19(5):4–10.

Newton C (2016) Life and death in the app store. The Verge. Accessed November 16, 2016. http://www.theverge.com/2016/3/ 2/11140928/app-store-economy-apple-android-pixite-bankruptcy.

Parker G, Van Alstyne M, Choudhary P (2016) Platform Revolution: How Networked Markets Are Transforming the Economy-And How You Can Make Them Work for You (W. W. Norton, Boston).

Parker G, Van Alstyne MW, Jiang X (2017) Platform ecosystems: How developers invert the firm. MIS Quart. 41(1):255–266.

Parker GG, Van Alstyne MW (2005) Two-sided network efects: A theory of information product design. Management Sci. 51(10): 1494–1504.

Rochet JC, Tirole J (2003) Platform competition in two-sided markets. J. Eur. Econom. Assoc. 1(4):990–1029.

Sabharwal A (2015) Moving on from Picasa. Oficial Google Picasa Blog. Accessed March 15, 2017. http://googlephotos.blogspot .de/2016/02/moving-on-from-picasa.html.

Sahni NS (2016) Advertising spillovers: Evidence from online fieldexperiments and implications for returns on advertising. J. Marketing Res. 53(4):459–478.

Saldanha TJ, Mithas S, Krishnan MS (2017) Leveraging customer involvement for fueling innovation: The role of relational and analytical information processing capabilities. MIS Quart. 41(1):367–396.

Swanson EJ (2015) Upload the pictures, and let Google Photos do the rest. New York Times (June 3). http://www.nytimes.com/ 2015/06/04/technology/personaltech/upload-the-pictures -and-let-google-photos-do-the-rest.html.

Thomas LD, Autio E, Gann DM (2014) Architectural leverage: Putting platforms in context. Acad. Management Perspect. 28(2): 198–219.

Tiwana A (2015) Evolutionary competition in platform ecosystems. Inform. Systems Res. 26(2):266–281.

Tiwana A, Konsynski B, Bush AA (2010) Platform evolution: Coevolution of platform architecture, governance, and environmental dynamics. Inform. Systems Res. 21(4):675–687.

Wareham J, Fox PB, Cano Giner JL (2014) Technology ecosystem governance. Organ. Sci. 25(4):1195–1215.

Yin PL, Davis JP, Muzyrya Y (2014) Entrepreneurial innovation: Killer apps in the iPhone ecosystem. Amer. Econom. Rev. 104(5):255–259.

Yoo Y, Henfridsson O, Lyytinen K (2010) Research commentary— The new organizing logic of digital innovation: An agenda for information systems research. Inform. Systems Res. 21(4):724–735.
