---
otero_id: 8100
otero_key: "PHZHTVJZ"
title: "Designing Warning Messages for Detecting Biased Online Product Recommendations: An Empirical Investigation"
authors: "Bo Xiao; Izak Benbasat"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0592"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/PHZHTVJZ/fulltext/images/ed594b436105fe48f2e3ce90dc72eba53af2fb6f8a56feebe459c5ee5767c56f.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Designing Warning Messages for Detecting Biased Online Product Recommendations: An Empirical Investigation

Bo Xiao, Izak Benbasat

To cite this article:

Bo Xiao, Izak Benbasat (2015) Designing Warning Messages for Detecting Biased Online Product Recommendations: An Empirical Investigation. Information Systems Research 26(4):793-811. http://dx.doi.org/10.1287/isre.2015.0592

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2015, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/PHZHTVJZ/fulltext/images/e7f0c917e243332aba9325131d361de3b1171e5a2b3640c42b487f0aca55e828.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Designing Warning Messages for Detecting Biased Online Product Recommendations: An Empirical Investigation

Bo Xiao

Information Technology Management Department, Shidler College of Business, University of Hawai’i at M¯anoa, Honolulu, Hawaii 96822, boxiao@hawaii.edu

Izak Benbasat

Sauder School of Business, University of British Columbia, Vancouver, British Columbia V6T 1Z2, Canada, izak.benbasat@sauder.ubc.ca

he increasing adoption of product recommendation agents (PRAs) by e-commerce merchants makes it an important area of study for information systems researchers. PRAs are a type of Web personalization technology that provides individual consumers with product recommendations based on their product-related needs and preferences expressed explicitly or implicitly. Whereas extant research mainly assumes that such recommendation technologies are designed to benefit consumers and focuses on the positive impact of PRAs on consumers’ decision quality and decision effort, this study represents an early effort to examine PRAs that are designed to produce their recommendations on the basis of benefiting e-commerce merchants (rather than benefiting consumers) and to investigate how the availability and the design of warning messages (a potential detection support mechanism) can enhance consumers’ performance in detecting such biased PRAs. Drawing on signal detection theory, the literature on warning messages, and the literature on message framing, we identified two content design characteristics of warning messages—the inclusion of risk-handling advice and the framing of risk-handling advice—and investigated how they influence consumers’ detection performance. The results of an online experiment reveal that a simple warning message without accompanying advice on how to detect bias is a double-edged sword, because it increases correct detection of biased PRAs (hits) at the cost of increased incorrect detection (false alarms). By contrast, including in warning messages risk-handling advice about how to check for bias (particularly when the advice is framed to emphasize the loss from not following the advice) increases correct detection and, more importantly, also decreases incorrect detection. The patterns of findings are in line with the predictions of signal detection theory. With an enriched understanding of how the availability and the content design of warning messages can assist consumers in the context of PRA-assisted online shopping, the results of this study serve as a basis for future theoretical development and yield valuable insights that can guide practice and the design of effective warning messages.

Keywords: electronic commerce; product recommendation agent; personalization; bias; signal detection theory; manipulative practices; warning; message framing; online experiment

History: Fred Davis, Senior Editor; France Belanger, Associate Editor. This paper was received October 7, 2013, and was with the authors 9 months for 2 revisions.

## 1. Introduction

With the rapid growth of electronic commerce (ecommerce), consumers’ purchase decisions are increasingly made in online environments (Xiao and Benbasat 2007, 2014). As reported by Sandler Research (2015), global online retail is forecasted to reach US\$1,248.7 billion in value in 2017, representing a compound annual growth rate of 14.6% for the five-year period 2012–2017. Digital marketplaces offer consumers great convenience, an immense assortment of products, and a significant amount of product-related information. However, because of the cognitive constraints of human information processing, identifying products that meet customers’ preferences is not an easy task (Xiao and Benbasat 2007). As a result, many e-commerce websites (e.g., myproductadvisor.com, easy-wine.net, openrice.com, amazon.com, jinni.com, appmatcher.com, tripbase.com, olayforyou.com) have implemented product recommendation agents (PRAs) to assist consumers in product search, assessment, and selection.

PRAs are a type of Web personalization technology that provides individual consumers with product recommendations based on their product-related needs and preferences expressed explicitly or implicitly (Xiao and Benbasat 2007). PRAs have the potential to improve the quality of decisions made by consumers when searching for and selecting products online, while at the same time reducing their information overload and search complexity (Xiao and Benbasat 2007). Research by Limelight Networks (2010) has identified personalized recommendations as an e-commerce feature that is highly valued by consumers, a feature that can help online companies create brand loyalty, which explains the phenomenal increase in the adoption of PRAs by online merchants in different industries (e.g., electronics, automobiles, movies, books, cosmetics, food and wines, tourism, real estate; Chau et al. 2013). eBay’s decision to acquire recommendation technology Hunch (Kim 2011), Amazon’s acquisition of Goodreads (one of the popular reading recommendation engines; Murph 2013), and more recently Apple’s acquisition of Book-Lamp and its book recommendation engine (Sullivan 2014) further signal the importance of recommendation technologies to e-commerce leaders. In fact, among the Internet Retailer top 500 e-retailers for 2013, 76.4% featured product recommendations based on individual shopper’s needs and preferences (Demery 2013).

Despite the potential for PRAs to aid consumers in decision making, the degree to which PRAs truly empower consumers depends on their veracity and objectivity (Hill et al. 1996, King and Hill 1994). The ultimate objective of an online merchant adopting PRAs is to “generate more business opportunities” by providing consumers with personalized product recommendations (Chau et al. 2013, p. 180). Therefore, rather than solely maximizing the benefits of consumers in a shopping process, the merchant aims to strike a balance between consumers’ benefits and business criteria (Chau et al. 2013). On one hand, the merchant wishes to provide consumers with product recommendations personalized to their needs and preferences to attract and retain customers. On the other hand, the merchant often has a vested interest in recommending products from certain vendors and/or products with certain characteristics (e.g., high profit margin products, soon-to-be discontinued products) to attain higher-than-usual profits (in terms of markups, commissions, referral fees, etc.) or reduce losses. With such mixed motivations in mind, the merchant may implement PRAs to provide recommendations that are not solely preference matched to benefit consumers, but instead biased toward its own interests (Chau et al. 2013; Xiao and Benbasat 2011, 2015).

The cost of relying on a PRA designed to produce biased recommendations (referred to as a biased PRA hereafter) may very well negate its fundamental value (i.e., improving decision quality while reducing decision effort), because the gain in decision-making efficiency may be overshadowed by the loss in decision quality (Haubl and Murray 2006). Consequently, biased PRAs are an important concern for e-commerce. Nonetheless, there has been scant scholarly attention directed to this phenomenon; even less studied are potential support mechanisms that can be implemented to curb the effects of biased recommendations in PRA-assisted online shopping. The study reported in this paper aims to address this knowledge gap by focusing on one support mechanism, warning, and exploring how its availability and the design of its informational content can influence consumers’ performance in detecting biased e-commerce PRAs.

Consumers are found to be generally vulnerable to manipulative practices in e-commerce (e.g., Grazioli 2004; Grazioli and Jarvenpaa 2000, 2001, 2003a, b; Grazioli and Wang 2001). Warning individuals explicitly about potential manipulative practices can arouse their suspicion and alert them to cues of manipulation, thus increasing their likelihood of detecting such manipulations. However, there is the possibility that warning messages can also lead to individuals perceiving manipulation when it does not exist. Prior research has focused on the presence or absence of warning messages on detection performance, without investigating design variables that affect the effectiveness of the warning messages, an additional gap this study aims to fill.

Message content (rather than source credibility or attractiveness) is the most significant predictor of individuals’ attitude and behavior (Fishbein and Ajzen 1981). This study focuses on the content of warning messages and examines the effects of two content design characteristics, namely, the inclusion of risk-handling advice and the framing of such advice, on consumers’ performance in detecting biased recommendations from online PRAs. More specifically, this study aims to answer two key questions:

(1) Will the inclusion of risk-handling advice in a warning message enhance consumers’ performance in detecting biased recommendations from a PRA?

(2) Will the framing (positive or negative) of the risk-handling advice (included in the warning message) influence consumers’ performance in detecting biased recommendations from a PRA?

An online experiment was conducted to address these two research questions. The results of the study show that warning consumers explicitly about potential PRA bias enhances their performance in detecting bias in the PRA’s recommendations. However, warnings may also lead to false alarms. The results of this study provide strong evidence that the most effective mechanism in supporting consumers in bias detection is to provide them with warning messages that include advice (or tips) for addressing the risk of PRA bias and frame the advice to emphasize the loss of not following such advice.

To our knowledge, this is the first empirical study that examines and explicitly compares the effectiveness of different warning mechanisms in supporting consumers in detecting biased product recommendations. Not only does this study contribute to the information systems (IS) literature by examining potential factors related to warning that influence consumers’ detection performance, but it also fills a void in existing warning research by shifting the focus from the presence/absence of warning messages to their design characteristics. Furthermore, by enhancing the understanding of the broad phenomenon of manipulative business practices in e-commerce, this study contributes to the concerted effort by government agencies, consumer protection organizations, and industry associations to combat such practices.

The remainder of this paper is organized as follows. Section 2 reviews previous literature and discusses the theoretical foundation for the design of warning messages. Section 3 presents the research model and develops hypotheses. The research method and results of hypothesis testing are reported in §§4 and 5, and this paper concludes with a discussion of the results, contributions of the study, and limitations and suggestions for future research.

## 2. Literature Review and Theoretical Foundations

This section reviews prior research on biased PRAs and introduces the theory and literature guiding the design of warning messages (i.e., signal detection theory, the literature on warning messages, and the literature on message framing).

## 2.1. Prior Research on Biased PRAs

Extant research on PRAs generally assumes that such recommendation technologies are designed to provide recommendations to benefit consumers and focuses on the positive impact of PRAs on consumers’ decision quality and decision effort, as well as their evaluation and acceptance of the PRAs (for a comprehensive review, see Xiao and Benbasat 2007). However, not all PRAs are altruistic; rather, many are designed not only to assist consumers but also to steer them in a particular direction, which makes them “double agents” (Haubl and Murray 2006). Hence, e-commerce PRAs have the potential to both aid and influence consumers in their decision making (Cosley et al. 2003, Haubl and Murray 2003, Senecal 2003, Senecal and Nantel 2004).

There has only been limited research into the dynamics and effects of PRA bias. Aksoy and Bloom (2001) introduced bias into a PRA by using product attribute importance weights that deviated from the weights expressed by PRA users to generate recommendations. They found that users of the biased PRA had higher search effort, reduced decision quality, and degraded perception of the usefulness of the recommendations. Cosley et al. (2003) altered a movie PRA’s predicted rating (i.e., the PRA’s prediction of a user’s liking of a movie, based on the user’s profile) to be either higher, lower, or the same as the actual predicted rating. They found that such alteration significantly lowered users’ satisfaction with the PRAs’ recommendations. Haubl and Murray (2003) found that product attributes selectively included in a PRA’s preference elicitation interface had a significant impact on consumers’ revealed preferences (in terms of the relative weight they attached to different product attributes), and subsequently their purchase decisions. Focusing on PRAs for digital cameras, Xiao and Benbasat (2015) showed that consumers’ product choice at e-commerce websites was significantly influenced by biased recommendations provided by the PRAs. However, although the biased recommendations led to impairment in consumers’ actual (or objective) decision quality, they did not reduce consumers’ perceived (or subjective) decision quality, hence highlighting the serious risk consumers face when dealing with a biased PRA. Chau et al. (2013) found that biased music recommendations led to a high level of distrust in a PRA’s competence and integrity, which in turn influenced online users interactions with the PRA. To our knowledge, none of the previous studies explored interventions that can support consumers in detecting bias in the PRAs’ recommendations.

## 2.2. Theoretical Foundations

In this study, we draw on signal detection theory, the literature on warning messages, and the literature on message framing to identify the design characteristics of warning messages. We also subscribe to signal detection theory to differentiate the possible outcomes of the task of detecting biased PRAs and to explain the pathways by which warning messages and their design characteristics influence consumers’ performance in detecting biased PRAs.

2.2.1. Signal Detection Theory. Signal detection theory (Davis and Parasuraman 1981, Green and Swets 1966) provides a general framework to describe and study decisions made in uncertain or ambiguous situations (Wickens 2001). It differentiates between two classes of events—noise (i.e., the background) and signal (i.e., stimulus that deviates from background noise and thus may be detected)—and explains the performance of individuals who strive to determine the presence of a signal. The theory also recognizes two types of outcomes when individuals strive to differentiate a signal from background noise: hits (when signals are successfully detected) and false alarms (when background noises are incorrectly identified as signals). Whereas hits are indicators of detection success, false alarms indicate detection failure. Superior detection performance is achieved when the rate of hits is high and the rate of false alarms is low. In the context of detecting bias in online PRAs’ recommendations, two types of outcomes are of interest: A hit occurs when a consumer perceives bias in the recommendations of a biased PRA, and a false alarm occurs when a consumer perceives bias in the recommendations of an unbiased PRA.

Signal detection theory also accounts for two factors influencing the outcomes of error detection: discriminant ability and decision threshold<sup>1</sup> (Green and Swets 1966). Discriminant ability refers to the ease with which the person making the judgment distinguishes the signal from the noise (i.e., in the context of this study, how easy it is for an individual to determine whether a recommendation is biased or not) and is affected by both personal and situational characteristics (Scott 2006). Discriminant ability is high when the individual making the judgment is experienced or well trained in detection tasks. For instance, an experienced interrogator in a criminal investigation is more likely to detect lies in a suspect’s confession. Discriminant ability is also high when the individual making the judgment is equipped with the right tools or information. For instance, a polygraph machine or information about the criminal history of the suspect can help the interrogator detect lies. Finally, discriminant ability is high when the signal is strong. For instance, some suspects are just bad liars, and thus an interrogator can easily tell that they are lying.

In detecting signals, many times there are ambiguous cases. Decision threshold refers to the level at which the individual making the judgment sets the cutoff point for ambiguous cases (Scott 2006). It is the decision point at which the individual determines that a signal is present. Decision threshold is also affected by individual differences and situational characteristics, such as general propensity to (dis)trust and beliefs about the base rate of a signal (Scott 2006). For instance, some individuals are more distrustful than others and are thus more likely to assume that any given statement is likely a lie. Some situations also lead us to expect lies. For instance, a statement made by a car salesman in a sales negotiation with customers would be more likely to be taken as not truthful when compared to the same statement made by the same car salesman to a friend in a casual chat (Scott 2006).

Signal detection theory suggests that support mechanisms aimed to enhance consumers’ performance in detecting PRA bias can be designed to (1) improve consumers’ discriminant ability (for instance, by advising consumers on how to access the necessary knowledge to detect anomalies resulting from bias) and/or (2) lower consumers’ decision threshold for judging ambiguous cues as anomalies (for instance, by enhancing consumers’ sensitivity to potential bias via explicit warnings).

2.2.2. Warning Messages, Decision Threshold, and Discriminant Ability. One of the most studied detection support mechanisms in prior research for inducing sensitivity to potential bias is the provision of warnings. Existing evidence indicates that warning individuals explicitly about potential manipulative practices can arouse consumers’ suspicion and alert them to anomalies resulting from manipulations (Miller and Stiff 1993, Parasuraman 1984, Stiff et al. 1992). However, the positive effect of warning messages on detection success has received mixed empirical support. Whereas Biros (1998), Biros et al. (2002), Grazioli (2004), and George et al. (2004) showed that suspicious receivers had higher detection performance compared to unsuspicious ones, others (e.g., George and Marett 2004, Grazioli and Wang 2001, Marett and George 2005, Tilley 2005) did not show the positive influence of induced suspicion on detection performance. Still others (e.g., Burgoon et al. 1994, Parasuraman 1984) revealed that warning messages enhanced consumers’ performance in detecting anomalies at the cost of increased false alarms. These equivocal findings suggest that the key question may not be whether warning messages improve detection success, but rather how they should be designed (e.g., in terms of informational content, format, vividness, warning time, and location; Argo and Main 2004, Stewart and Martin 1994) to enhance their effectiveness. Nevertheless, prior detection studies have mostly focused on the presence or absence of warning messages on detection performance, without exploring design variables that may affect the effectiveness of the warning messages, a novel question this study aims to answer.

In the public policy and marketing literature, there has been extensive research on the effectiveness of product warning messages (e.g., warning labels on tobacco packages; see Argo and Main 2004). Consumer product warnings serve two major purposes: to prevent consumers from engaging in behaviors that may lead to undesirable consequences and to promote appropriate product usage behavior (Argo and Main 2004). An effective consumer product warning is one that not only communicates clearly the nature of the risk facing consumers but also provides advice on how to avoid that risk (Kelley et al. 1989, Ross 1981). The provision of such advice on what consumers could do to avoid the negative consequences described in the warning message will equip consumers with necessary knowledge and skills to manage the risky situation, thus enhancing their motivation to change their behavior in accordance with the advice received. From a meta-analysis and literature review of prior research on warning messages involving fear appeals, Witte and Allen (2000) conclude that a warning message is most effective when it also includes information about how to avert or minimize the risk highlighted in the message.

Literature on warning messages (particularly research on consumer product warnings) suggests that, in the context of our study, the effectiveness of warning messages can be enhanced by improving the design of their informational content. More specifically, in addition to warning consumers about the potential risk of PRA bias (and thus lowering their decision threshold in judging ambiguous cases), the message should also include advice on how to handle this risk (to increase consumers’ discriminant ability in detecting bias). Nonetheless, to persuade consumers to adopt the risk-handling advice included in the warning message, the advice (which can be considered a persuasive message by itself) needs to be communicated in a way that maximizes its impact on consumers’ behavioral outcome (Rothman et al. 2006); this is where insights from prior research on message framing are particularly valuable.

2.2.3. Message Framing as Persuasive Communication Strategy. Message framing is a persuasive communication strategy aimed at motivating behavior through the presentation of equivalent appeals or opinions framed in terms of either gains or losses (Gerend and Sias 2009). Levin et al. (1998) distinguish among three different kinds of framing—risky choice framing, attribute framing, and goal framing. In risky choice framing, introduced by Tversky and Kahneman (1981) and traditionally associated with the term “framing,” the outcomes of a potential choice involving options differing in the level of risk are described in different ways (e.g., “1/3 chance 600 people will be saved” versus “2/3 chance 600 people will die”). In attribute framing, a single attribute within any given context is the subject of the framing manipulation (e.g., “75% lean” versus “25% fat”). Finally, goal framing is designed to influence the implicit goals that an individual adopts by specifying the consequences of a particular behavior in either positive or negative terms. Of the three types of framing, goal framing is often applied in a persuasive communications context and thus is relevant to our study.

A goal-framing effect occurs when a persuasive message has different appeal depending on whether it stresses the positive consequences of performing an act or the negative consequences of not performing the act. A review of prior research (see Levin et al. 2002, 1998) reveals equivocal empirical evidence for the relative impact of positively framed messages (emphasizing gains) versus negatively framed ones (emphasizing losses) in influencing a given behavior. For instance, Meyerowitz and Chaiken (1987) found that women were more apt to engage in breast self-examination (BSE) when presented with information stressing the negative consequences of not performing the BSE than when presented with information stressing the positive consequences of performing the BSE. Likewise, Banks et al. (1995) showed that women receiving a loss-framed message (emphasizing the risks of not being screened) were more likely to obtain a mammogram in the next 12 months than those who received a gain-framed message (emphasizing the benefits of being screened). On the other hand, Detweiler et al. (1999) found that beachgoers who had received a gain-framed brochure about skin cancer were significantly more likely to seek out a free sample of sunscreen. Rothman et al. (1993) also showed that gain-framed messages had a greater impact on the use of sunscreen for females. Such mixed findings have led researchers to explore moderating variables that can enhance, eliminate, or even reverse the goal-framing effect.

One potential moderating variable has to do with the nature of the behavior advocated in the persuasive message (Rothman et al. 2006, Rothman and Salovey 1997). Prospect theory postulates that whereas people are risk taking when a decision problem is formulated in terms of loss, they are risk averse when they are faced with gain-framed decision problems (Tversky and Kahneman 1981). Consistent with this perspective, the impact of a given frame (positive or negative) on behavior “should depend on whether the behavior under consideration is perceived to reflect a risk averse or risk seeking course of action” (Rothman et al. 2006, p. S205), which in turn depends on “the extent to which people perceive the behavior will afford an unpleasant outcome” (Rothman et al. 2006, p. S205). More specifically, when people are considering a detection behavior (e.g., cancer screening or annual health checkup) that is likely to involve some unpleasant outcome (e.g., detecting a health problem) and is thus considered risky, negatively framed appeals or opinions should be more persuasive. By contrast, positively framed appeals or opinions are more effective when people are considering a prevention behavior (e.g., applying sunscreen or using mouth rinse) that is less likely to involve unpleasant outcomes (Rothman et al. 2006, Rothman and Salovey 1997) and is thus considered a risk-averse course of action. In other words, the performance of detection (prevention) behavior is best facilitated by a negatively framed (positively framed) message (Detweiler et al. 1999). Existing empirical evidence is largely supportive of the detection–prevention classification (for a review, see Rothman et al. 2006).

Literature on message framing suggests that, in the context of our study, the risk-handling advice included in the content of the warning message can be framed either positively (emphasizing the gain or positive implication associated with following the advice) or negatively (emphasizing the loss or negative implication associated with not following the advice). Such framing falls into the category of goal framing, because it aims to influence the implicit goals that consumers adopt. The relative effectiveness of the two framing strategies in enhancing consumers’ detection performance will be explored in this study.

## 3. Research Model and Hypothesis Development

Just like other manipulative online practices, biased recommendations from PRAs may present serious risks (financial and/or social) to consumers shopping on the Internet (Grazioli 2004; Grazioli and Jarvenpaa 2000, 2001, 2003a, b; Grazioli and Wang 2001; Xiao and Benbasat 2011). This study focuses on one support mechanism, warning, that has been shown in prior research to help consumers better detect online manipulations (e.g., Biros et al. 2002, Grazioli 2004). Whereas extant detection research is characterized by a predominant interest in the presence or absence of warning messages on detection performance, this study goes one important step further in identifying design characteristics of warning messages and theorizing about their effects on consumers’ performance in detecting PRA bias.

Drawing from signal detection theory, the literature on warning messages, and the literature on message framing, we posit that the availability and content design of warning messages affect consumers’ performance in detecting PRA bias via their influence on consumers’ decision threshold and discriminant ability, respectively. More specifically, we propose the following:

• The mere availability of warning messages may not enhance consumers’ detection performance because they increase both hits and false alarms via lowering consumers’ decision threshold.

• Warning messages designed with proper content will improve consumers’ detection performance by increasing hits without simultaneously increasing false alarms via improving consumers’ discriminant ability.

To empirically test these propositions, we developed the following research model (Figure 1) and a set of testable hypotheses, described next.

Availability of warning message, as the name suggests, refers to whether a warning message<sup>2</sup> (an intervention aimed to lower decision threshold) is conveyed to consumers about the possibility of PRA bias.

Content design of warning message refers to the two content design characteristics of warning messages, namely, the inclusion of risk-handling advice in warning messages and the framing of the risk-handling advice, which give rise to three different types of warning messages:<sup>3</sup> (i) warning with no advice, (ii) warning with positively framed advice, and (iii) warning with negatively framed advice. Consumers who receive a warning with no advice are warned of the risk of PRA bias, but are not provided with advice for handling such risk (i.e., strategies for detecting bias in the PRA’s recommendations). Consumers who receive the other two types of warning are provided with a warning message that includes risk-handling advice (an intervention aimed to enhance discriminant ability) framed either positively (thus accentuating the gain from following the advice) or negatively (thus stressing the loss from not following the advice).

Type of PRA refers to whether the PRA at the e-commerce website is an unbiased one or a biased one. Whereas an unbiased PRA bases its recommendations solely on consumers’ expressed preferences, a biased PRA recommends products on the basis of additional business criteria (e.g., profit margin and/or commission from selling particular products; Chau et al. 2013), and thus may not recommend products that best match the consumers’ preferences.

Consumers’ detection performance is reflected in their performance in detecting bias in the PRA’s recommendations. Prior research in deception detection suggests that identifying anomalies (i.e., deviations from what is expected, usual, and normal) resulting from strategic manipulation is the first and critical step toward successful detection (Bellman et al. 2006, Johnson et al. 1993, Morrison and Robinson 1997, Robinson 1996). Thus, in this study, bias is assessed by the level of perceived anomaly in the PRA’s recommendations. Perceived bias in the PRA’s recommendations refers to the extent to which consumers believe that the PRA’s recommendations deviate from what is expected, usual, and normal.

## 3.1. Availability of Warning Message

Prior research has identified the provision of warnings as an intervention that can sensitize individuals to manipulation-related anomalies (Miller and Stiff 1993, Parasuraman 1984, Stiff et al. 1992). Likewise, in the context of our study, explicit warnings about potential bias effected by a PRA are expected to lower consumers’ decision threshold in judging ambiguous cues as anomalies (e.g., by mitigating individuals general propensity to trust others and/or increasing the expected base rates of anomalies; Scott 2006), thus enhancing the likelihood for consumers to perceive bias in the recommendations of a biased PRA and resulting in higher rates of hits. However, signal detection theory suggests that lowered decision threshold in an individual’s judgment may also lead to more situations being inaccurately perceived as anomalous, resulting in higher rates of false alarms (which occur when consumers perceive bias in the recommendations of an unbiased PRA). Findings from several studies (e.g., Burgoon et al. 1994, Parasuraman 1984) have confirmed that warning messages enhanced consumers’ performance in detecting bias at the cost of increased false alarms. We thus hypothesize the following:

Figure 1 (Color online) Research Model  
![](/api/attachments/PHZHTVJZ/fulltext/images/a4cb9d686494d66d8625d893f4c92276a044b6b82884553326f33c3296cf8b9f.jpg)

<sup>Hypothesis</sup> <sup>1</sup> <sup>(H1).</sup> Compared with those receiving no warning, consumers who are provided with a warning will be more likely to perceive bias in the recommendations of both a biased PRA (H1a) and an unbiased PRA (H1b), thus resulting in more hits and more false alarms.<sup>4</sup>

## 3.2. Content Design of Warning Message— Inclusion of Risk-Handling Advice

According to signal detection theory, interventions aimed to help individuals improve detection performance can be designed to increase individuals’ discriminant ability (e.g., by providing them with the necessary knowledge to discriminate signal from noise; Scott 2006). Compared with those affecting one’s decision threshold, interventions aimed to influence discriminant ability tend to be more effective in achieving high rates of hits without simultaneously increasing rates of false alarms (Scott 2006).

Warning with risk-handling advice is an intervention that can potentially enhance consumers’ discriminant ability, and does so by providing consumers facing an uncertain judgment decision with more information about the situation at hand and encouraging them to make independent verification using appropriate tools. Consumers who follow the advice<sup>5</sup> (either positively framed or negatively framed) included in the warning message by engaging in the behavior advocated in the advice will perform better in identifying bias in a PRA.

By contrast, a warning message with no risk-handling advice does not by itself improve consumers’ discriminant ability to compensate for the impact of lowered decision threshold. Simply warning consumers about the risk of PRA manipulation (without simultaneously providing them with strategies to handle such risk) will place consumers in a heightened state of alertness and increase their likelihood of perceiving bias in the recommendations of an unbiased PRA (resulting in increased false alarms) as well as in the recommendations of a biased PRA (resulting in increased hits).

In sum, we expect that consumers who receive a warning message that includes risk-handling advice will have more hits and fewer false alarms than those who receive a simple warning with no advice. Therefore, we hypothesize the following:

<sup>Hypothesis</sup> <sup>2</sup> <sup>(H2).</sup> Compared with those receiving a warning with no advice, consumers provided with a warning message that includes advice for handling risk will be more likely to perceive bias in a biased PRA (H2a) and less likely to perceive bias in an unbiased PRA (H2b), resulting in more hits and fewer false alarms.

## 3.3. Content Design of Warning Message— Framing of Risk-Handling Advice

The risk-handling advice included in a warning message is effective to the extent that consumers who receive the warning message follow the advice and adopt the course of action advocated in the advice. Therefore, the risk-handling advice (a persuasive message by its nature) needs to be communicated in a manner that maximizes its impact on consumers behavior.

Prior research in message framing suggests that persuasive messages can be “framed” to either emphasize the benefits of taking action (i.e., a gain-framed appeal) or accentuate the costs of failing to take action (i.e., a loss-framed appeal; Rothman et al. 2006). Lossframed appeals are more persuasive when the behavior under consideration is a detection (as opposed to prevention) behavior associated with a high likelihood of an unpleasant outcome (Rothman et al. 2006, Rothman and Salovey 1997), because potential losses (emphasized in loss-framed appeals) tend to be more motivating than potential gains (underscored in gain-framed appeals) when risky actions (exemplified by detection behavior that involves unpleasant outcomes) are contemplated (O’Keefe and Jensen 2009). Accordingly, in the context of this study, because the task of bias detection necessarily involves the possibility of an unpleasant outcome (i.e., uncovering manipulation by the PRA), advice in the warning message encouraging consumers to adopt the advocated risk-handling behavior (e.g., to use functionalities such as searching by brand or a comparison matrix to verify the PRA’s recommendations) is likely to be more effective in motivating consumers to take extra search action when the advice is framed as loss related than when it is framed as gain related. Thus, we hypothesize the following:

<sup>Hypothesis</sup> <sup>3</sup> <sup>(H3).</sup> Compared with those receiving a positively framed warning message, consumers provided with a negatively framed warning message will be more likely to perceive bias in a biased PRA (H3a) and less likely to perceive bias in an unbiased PRA (H3b), resulting in more hits and fewer false alarms.

## 4. Research Method

An online experiment was conducted to test the hypothesized relationships.

## 4.1. Experimental Design

A 4 (type of warning message: no warning, warning with no advice, warning with positively framed advice, or warning with negatively framed advice) × 2 (type of PRA: unbiased or biased) between-subject factorial design was employed.

4.1.1. Design of Warning, Advice, and Framing. For participants assigned to groups with warnings, a pop-up window with a warning message is displayed immediately before the start of the experimental task at the e-commerce website. E-commerce merchants (particularly those motivated to provide biased recommendations) are understandably reluctant to warn consumers of potential manipulative practices. As such, warning messages were implemented in this study as issued by a third party (e.g., a consumer organization) independent of the e-commerce merchant. To convey to experimental participants that the warning message was not issued by (or part of) the e-commerce website that they were visiting, the pop-up window containing the message was designed with background color and font type, size, and color distinct from those of the e-commerce website.<sup>6</sup> Participants were asked to read the message before they accessed the e-commerce website.

As explained earlier, in this study, the risk-handling advice included in a warning message was to encourage consumers to conduct independent verification of the PRA’s recommendations by comparing the recommended products with other, nonrecommended products in the same brand using functionalities such as search by brand and/or a comparison matrix, available at the e-commerce website.

There are different ways to construct the framing of risk-handling advice. Rothman and Salovey (1997) note that whereas positively framed messages can focus on attaining a desirable outcome or not attaining an undesirable outcome (both gains), negatively framed messages can emphasize the attainment of an undesirable outcome or the failure to attain a desirable outcome (both losses). Accordingly, in this study, we manipulated positively framed advice by accentuating both the gains of performing the risk-handling behavior (i.e., increased chance of distinguishing an unbiased PRA from a manipulative one and reduced risk of being misled by biased recommendations), and constructed negatively framed advice by stressing both losses of failing to perform the target behavior (i.e., reduced chance of distinguishing an unbiased PRA from a manipulative one and increased risk of being misled by biased recommendations). Because the warning message was rather long when the risk-handling advice was included, relevant texts in the advice were set in bold and italicized to enhance the perceptual salience of the behavior being promoted and the positive/negative consequences. Table 1 illustrates the operationalization of different types of warning messages and the risk-handling advice (framed positively or negatively).

Table 1 Design of Warning Messages and Risk-Handling Advice

<table><tr><td>Type of warning message</td><td>Components</td><td>Text of warning message</td></tr><tr><td>Warning with no advice</td><td>Simple warning</td><td>When shopping at online stores that provide automated Shopping Advisors, $^{a}$  please be aware that some advisors may provide product recommendations biased toward certain brands or toward products with certain characteristics.</td></tr><tr><td rowspan="2">Warning with positively framed advice</td><td>Simple warning</td><td>... (Same text as in the warning with no advice condition here.)</td></tr><tr><td>Positively framed risk-handling advice</td><td>Consumers are advised to verify the Shopping Advisor&#x27;s recommendations by comparing recommended products with other, nonrecommended products in each of your preferred brands, using functionalities such as comparison matrix and searching by brand that are available at the website.Research shows that consumers who verify the Shopping Advisor&#x27;s product recommendations have increased chance of distinguishing an unbiased Shopping Advisor from a manipulative one and reduced risk of being misled by biased recommendations.</td></tr><tr><td rowspan="2">Warning with negatively framed advice</td><td>Simple warning</td><td>... (Same text as in the warning with no advice condition here.)</td></tr><tr><td>Negatively framed risk-handling advice</td><td>Consumers are advised to verify the Shopping Advisor&#x27;s recommendations by comparing recommended products with other, nonrecommended products in each of your preferred brands, using functionalities such as comparison matrix and searching by brand that are available at the website.Research shows that consumers who fail to verify the Shopping Advisor&#x27;s product recommendations have reduced chance of distinguishing an unbiased Shopping Advisor from a manipulative one and increased risk of being misled by biased recommendations.</td></tr></table>

<sup>a</sup>In the experiment, a PRA is referred to as an automated shopping advisor.

4.1.2. Design of Websites, PRAs, and Bias. Prior experimental studies examining biased recommendations have either introduced the bias randomly (e.g., by increasing/decreasing the predicted product ratings or consumer indicated product attribute importance weight; e.g., Aksoy and Bloom 2001, Cosley et al. 2003) or presented only products from one particular product vendor (which is essentially an outright lie and is sure to induce suspicion from consumers; e.g., Chau et al. 2013, Komiak and Benbasat 2008). Although PRA bias can be effected in various ways, this study focuses on PRAs that recommend products from among a reduced set of products the online merchant intends to promote (rather than from among all of the products available at the e-commerce website), to enhance the likelihood of consumers choosing the promoted products. This is akin to manipulations in personal selling situations, for example, in which salespersons are motivated to recommend from a subset of products whose commission rates are high from product vendors or products they are pressured (by managers, for instance) to sell (e.g., products whose stock levels are high in the warehouse or that have a high profit margin; Chau et al. 2013), rather than recommending products that best match customers’ preferences.

Two experimental websites (one featuring a biased PRA and the other providing an unbiased PRA) were developed for this study. Each website featured the same 96 digital cameras from eight brands,<sup>7</sup> with 12 products in each brand. The product features for the 12 digital cameras in each brand were carefully designed such that six products (referred to as the promoted products) were dominated by the other six products (referred to as the dominant products). Each promoted product was paired with a dominant product in the same brand. In each pair, the dominant product performed better on two important attributes than the promoted product, but offered the same price. Two content-filtering PRAs for digital cameras were adapted from Wang and Benbasat (2005). Each website had 48 dominant products and 48 promoted products. Table 2 illustrates how the two PRAs were designed.

A credible lie is one that will not trigger the target’s suspicion. The bias that we implement in this study is a credible lie for two reasons. First, our manipulation of bias is detectable if consumers exert effort to view

## Table 2 The Design of PRAs

Both biased and unbiased PRAs

• The PRAs use needs-based questions (adapted from Wang and Benbasat 2005) to elicit users’ product-related preferences.

• The PRAs calculate a fit score for every available product based on users expressed preferences.

• The PRAs generate a list of 12 products, with six products displayed on each page.<sup>a</sup>

• Users can use the built-in comparison matrix to compare products.

• Users can utilize the built-in search-products-by-brand functionality to view additional products that are not recommended by the PRA.

Unbiased PRA

• The PRA selects 12 products from among all 96 available products that have the highest fit scores and presents them in the recommendation list (ordered by fit score).

Biased PRA

• The PRA selects 12 products from among the 48 promoted products that have the highest fit scores and presents them in the recommendation list (ordered by fit score).

• None of the 48 dominant products will be included in the two-page recommendation list.

<sup>a</sup>Human beings are limited in the amount of information that can be processed simultaneously. According to Miller (1956), the magical number is seven, plus or minus two. In other words, the number of items that can be held in individuals’ short-term memory is limited to seven, plus or minus two. Therefore, in our study, displaying six recommended products on each page is appropriate for controlling the participants’ cognitive load.

and compare extra products in their preferred brands. However, it is not as easily detected as the practice of recommending products from a single brand<sup>8</sup> (even when consumers indicate a preference for other brands). Second, to make a credible lie, a liar needs to get inside the target’s head (i.e., to take into account the perspective of the target; Wise 2010); the PRA implemented in our study does exactly that by taking into account the expressed preferences of consumers when producing the biased recommendations.

## 4.2. Sample

Participants for this study were 496 e-commerce shoppers recruited from a North American panel maintained by a marketing research firm that specializes in market research sampling and custom panel recruitment. The sample size ensured a 0.8 power for the required hypothesis tests to detect a medium effect of 0.15. An invitation to participate in the study was broadcast by the marketing firm via email to members of the panel. Individuals were provided with a point-based incentive (redeemable for various prizes) for their assistance in the study, available through the marketing firm.

## 4.3. Experimental Task and Procedures

All participants were randomly assigned to one of the eight experimental groups. They were told that an online camera store, ForeverCam.com, was testing an automated shopping advisor implemented to assist consumers in choosing digital cameras while shopping in the store. Their task was to visit ForeverCam.com and evaluate the shopping advisor (as well as its product recommendations) at the website. They were also provided with the camera-related preferences of a friend, Pat, and asked to use these preferences to evaluate the shopping advisor’s product recommendations.<sup>91</sup> <sup>10</sup>

To motivate participants to take the experimental task seriously, participants were informed before the experiment that, in addition to the point-based incentive provided by the online marketing firm, those who provided detailed, well-supported justifications of their evaluation of the PRA would also get a \$25 cash reward.

Participants were first asked to complete a short questionnaire that collected demographic data (e.g., age, gender) and background information (e.g., level of experience with computers and online shopping, preexisting risk perception regarding online shopping, product expertise). They were then asked to read a tutorial on how to navigate their assigned e-commerce website and use the PRA embedded in the website. Next, they were asked to read a tutorial on digital camera attributes and complete a quiz aimed at testing their understanding of important digital camera attributes. After that, participants were asked to read task instructions and then click on a “Start Shopping” button. Participants in the control condition (i.e., the no warning condition) were immediately directed to the e-commerce website to complete the experimental task. For participants in one of the three warning conditions, a pop-up window appeared with a warning message before they were directed to the e-commerce website. Upon completion of the experimental task, participants were asked to fill out a questionnaire that included the measures of the dependent variable.

## 4.4. Measurement of Dependent Variable

The focal dependent variable, perceived bias in the PRA’s recommendation, was assessed by participants’ perception of anomaly in the PRA’s recommendations (see Table 3). An anomaly is a deviation from what is expected, usual, or normal, for instance, the presence of inconsistencies between consumers’ requirements and a PRA’s product recommendations, or the observation that products not recommended by the PRA actually fit consumers preferences better than those recommended (Johnson et al. 1993, Johnson et al. 2001). Based on this definition, three measurement items for perceived bias (on sevenpoint scales) were newly developed for this study. Whereas a high level of perceived bias associated with an unbiased PRA indicates the presence of false alarms in detecting bias, a high level of perceived bias associated with a biased PRA indicates hits.

Table 3 Manipulation Checks

<table><tr><td>Experimental treatment</td><td>Manipulation check</td><td>Statistical test</td></tr><tr><td>PRA bias</td><td>Measured with “perceived bias” (on a seven-point Likert scale from “strongly disagree” to “strongly agree”):I noticed inconsistencies between Pat’s requirements and the shopping advisor’s product recommendations.I found that in each of Pat’s preferred brands, some nonrecommended products actually fit Pat’s preferences better than the products recommended by the shopping advisor; that is to say, products that best meet Pat’s preferences were not included in the shopping advisor’s recommendations.I have noticed other things (not mentioned above) that are unexpected, unusual, or abnormal in the shopping advisor’s product recommendations.</td><td>ANOVA</td></tr><tr><td>Availability of warning message</td><td>Measured before the showing of the warning message (on a seven-point Likert scale from “strongly disagree” to “strongly agree”)There is considerable risk involved in shopping online.Shopping online could lead to undesirable consequences.There is a high potential for loss involved in shopping online.Measured immediately after the showing of the warning message but before the start of the experimental task (on a seven-point Likert scale from “strongly disagree” to “strongly agree”)Using the shopping advisor to select digital cameras at ForeverCam.com could lead to undesirable consequences.There might be considerable risk involved in using the shopping advisor to select digital cameras at ForeverCam.com.There should be no risk involved in using the shopping advisor to select digital cameras at ForeverCam.com.There might be a high potential for loss involved in using the shopping advisor to select digital cameras at ForeverCam.com.</td><td>ANCOVA</td></tr><tr><td>Content design of warning message—inclusion of risk-handling advice</td><td>Measured subjectively with the following item (on a seven-point Likert scale from “strongly disagree” to “strongly agree”):Just before you started the evaluation task at ForeverCam.com, you read a message that contains not only a warning to consumers but also practical advice for handling risks associated with the automated shopping advisor.Captured objectively (with computer logs):Whether the participants used the search-by-brand  $functionality^a$  (as advised in the warning message)</td><td>ANOVA</td></tr><tr><td>Content design of warning message—framing of risk-handling advice</td><td>Measured subjectively with the following two radio-button type items (after the display of the warning message to participants in the warning with advice experimental conditions):I feel that...o the message stresses the negative implications of failing to verify the shopping advisor’s recommendations.o the message stresses the positive implications of verifying the shopping advisor’s recommendations.I believe that...o I stand to lose important benefits by failing to verify the shopping advisor’s recommendations.o I stand to gain important benefits by verifying the shopping advisor’s recommendations.</td><td>Cross-tab analysis</td></tr></table>

<sup>a</sup>Because all of the participants in this study made use of the comparison matrix functionality during the experimental task, we focus our data analysis on the search-by-brand functionality.

## 4.5. Pretest

A series of pretests were conducted prior to the main experiment (i) to validate the measurement for perceived bias and (ii) to ensure that the manipulations of warning, risk-handling advice, and framing in our study were successful and that the bias manipulation was reasonable (i.e., neither too easy nor too difficult to detect).

## 5. Data Analysis and Results

This section begins by reporting demographic data about participants in the experiment. Manipulation check results are reported in §5.2. Results of hypothesis testing are presented in §5.4.

## 5.1. Demographic Data

Table E1 in the online appendix (available as supplemental material at http://dx.doi.org/10.1287/isre.2015 .0592) outlines the characteristics of the participants who volunteered for the experiment. More females participated in the study than males. The majority of participants were between 30 and 49 years old. Over 50% of the participants used the Internet for at least 20 hours each week. Also, more than half of the participants made at least five purchases online during the past 12 months. The demographic profile of the participants is similar to that of online shoppers reported elsewhere (e.g., Pew Research Center 2014). On average, participants rated their own product expertise (with digital cameras) at 3.69 (on a sevenpoint scale), suggesting that the participants did lack high expertise in the intended product category. There were no significant differences among the eight experimental groups in terms of product expertise or other demographic/background characteristics.

## 5.2. Manipulation Checks

Manipulation checks were conducted (see Table 3) for the experimental treatments.

5.2.1. PRA Bias. Results of analysis of variance (ANOVA) show that the treatment for PRA bias was successful. Perceived bias was significantly higher for participants in the biased PRA condition than for those in the unbiased PRA condition $( M = 3 . 6 1$ versus 2.53, $F ( 1 , 4 9 4 ) = 7 3 . 1 8 2 , p < 0 . 0 0 1 )$

5.2.2. Availability of Warning Message. Analysis of covariance (ANCOVA) results show that, controlling for participants’ preexisting risk perceptions regarding shopping online, those provided with a warning message perceived shopping with the assistance of PRA to be significantly more risky than those not provided with such a message $( M = 4 . 1 4 \mathrm { \ v e r s u s \ } 3 . 4 3 ,$ $\bar { F } ( 1 , 4 9 3 ) = 3 4 . 9 3 8 , p < 0 . 0 0 1 )$ . Further analysis reveals no significant difference among the three warning conditions in terms of risk perceptions associated with the use of the PRA (M = 4031 versus 4.00 versus 4.10, $F ( 2 , 3 6 8 ) = 1 . 6 6 9 , p = 0 . 1 9 )$

5.2.3. Content Design of Warning Message— Inclusion of Risk-Handling Advice. Results from both ANOVA and cross-tab analysis show that the treatment for inclusion of risk-handling advice (i.e., whether riskhandling advice is included in the warning message) was successful. ANOVA shows that participants’ perception of the extent to which the warning message they read contained practical risk-handling advice was significantly higher in the warning with advice condition than in the warning without advice condition (M = 5066 versus 5.25, $F ( 1 , 3 7 0 ) = 4 . 1 2 7 , p < 0 . 0 5 )$ . Cross-tab analysis shows that it was significantly more likely for the participants to use the search-by-brand functionality (the risk-handling act advocated in the advice included in the warning message) in the warning with advice condition than in the warning with no advice condition (43.1% versus $1 2 . 9 \% , \chi ^ { 2 } ( 1 , N = 4 9 6 ) = 5 6 . 2 2 4 , p < 0 . 0 0 1 )$

5.2.4. Content Design of Warning Message— Framing of Risk-Handling Advice. Results of cross-tab analysis show that the treatment for the framing of riskhandling advice in the warning message was successful. It was significantly more likely for the participants to perceive the warning message they read as emphasizing the loss associated with and negative implications of failing to adopt the risk-handling behavior advocated in the message in the warning with negatively framed advice condition than in the warning with positively framed advice condition (65.3% versus 43.5%, $\chi ^ { 2 } ( 1 , \dot { N } = 2 4 8 ) = 1 1 . 8 5 , p < 0 . 0 1 )$

Figure 2 Mean Value of Perceived Bias in Different Experimental Conditions  
![](/api/attachments/PHZHTVJZ/fulltext/images/af01631334156cbbfa97ce606cdd4060252568e1955d0907be3c5c27e31506e8.jpg)

## 5.3. Measurement Model

There is only one dependent variable for this study, namely, perceived bias in the PRA’s recommendations. The Cronbach’s alpha for perceived bias is 0.74, indicating good internal consistency.

## 5.4. Results of Hypothesis Tests

The mean values of perceived bias for different experimental conditions are illustrated in Figure 2.

An ANOVA with planned contrasts was conducted to test for the hypothesized differences in perceived bias among different warning conditions. Table 4 presents the results of contrast analysis.

5.4.1. Warning vs. No Warning. As shown in Figure 2 and Table 4, perceived bias was significantly higher for participants who received a warning than those receiving no warning in the biased PRA condition $( t ( 2 4 4 ) = 4 . 5 4 \bar { 7 } , p < 0 . 0 0 1 )$ , but not in the unbiased PRA condition $( t ( 2 4 4 ) = 1 . 1 9 6 , p = 0 . 2 3 3 )$ , suggesting that participants provided with a warning about potential PRA bias had significantly more hits, but not more false alarms, than those in the no warning condition. These results support H1(a), but not H1(b).

Further analysis comparing the no warning condition to each of the three warning conditions (i.e., warning with no advice, warning with positively framed advice, and warning with negatively framed advice) reveals an interaction between the availability and the content design of warning messages. More specifically, in the biased PRA condition, participants who received any one of the three types of warning messages had a significantly higher level of perceived bias than those receiving no warning $( t ( 2 4 4 ) = 2 . 2 5 0 , p < 0 . 0 5 ; t ( 2 4 4 ) =$ $2 . 7 1 6 , p < 0 . 0 1 ; t ( 2 4 4 ) = 6 . 0 3 9 , p < 0 . 0 0 1 )$ . By contrast, in the unbiased PRA condition, although participants who received either a warning with no advice or a warning with positively framed advice had a significantly higher level of perceived bias than those receiving no warning $( t ( 2 4 4 ) = 2 . 1 2 0 , p < 0 . 0 5 ; t ( 2 4 4 ) = 1 . 8 4 2 , p = 0 . 0 6 7 )$ , the difference in perceived bias was not significant between participants who received a warning with negatively framed advice and those receiving no warning (t42445 = 10161, p = 00247). Thus, when there was no bias in the PRA’s recommendations, providing participants with a warning message that included negatively framed advice did not increase their perception of PRA bias, as did the provision of the other two types of warning messages. In sum, the provision of any type of warning message resulted in an increased hit rate. In addition, compared to the no warning condition, whereas warning with no advice and warning with positively framed advice led to a higher false alarm rate, warning with negatively framed advice did not result in an increase in false alarms.

Table 4 ANOVA Planned Contrasts for Noticing of Anomaly

<table><tr><td>Group A</td><td>Group B</td><td>Diff. in  $mean^a$ </td><td>df</td><td>t</td><td>Sig.</td><td>Related hypothesis</td></tr><tr><td colspan="7">Unbiased PRA condition</td></tr><tr><td> $Warning^b$ </td><td>No warning</td><td>0.21</td><td>244</td><td>1.196</td><td>0.233</td><td>H1(b)</td></tr><tr><td> $Warning with advice^c$ </td><td>Warning with no advice</td><td>-0.38</td><td>244</td><td>2.054</td><td>0.041</td><td>H2(b)</td></tr><tr><td>Warning with negatively framed advice</td><td>Warning with positively framed advice</td><td>-0.64</td><td>244</td><td>3.003</td><td>0.003</td><td>H3(b)</td></tr><tr><td colspan="7">Biased PRA condition</td></tr><tr><td> $Warning^d$ </td><td>No warning</td><td>0.99</td><td>244</td><td>4.547</td><td>0.000</td><td>H1(a)</td></tr><tr><td> $Warning with advice^e$ </td><td>Warning with no advice</td><td>0.57</td><td>244</td><td>2.457</td><td>0.015</td><td>H2(a)</td></tr><tr><td>Warning with negatively framed advice</td><td>Warning with positively framed advice</td><td>0.88</td><td>244</td><td>3.324</td><td>0.001</td><td>H3(a)</td></tr></table>

<sup>a</sup>Difference in mean is the Group A mean minus the Group B mean.  
<sup>b</sup>Includes warning with no advice, warning with positively framed advice, and warning with negatively framed advice.  
<sup>c</sup>Includes warning with positively framed advice and warning with negatively framed advice.  
<sup>d</sup>Includes warning with no advice, warning with positively framed advice, and warning with negatively framed advice.  
<sup>e</sup>Includes warning with positively framed advice and warning with negatively framed advice.

5.4.2. Warning with Advice vs. Warning with No Advice. There was a significant difference in perceived bias between participants who received a warning with advice (positively framed or negatively framed) and those who received a warning with no advice, both in the unbiased PRA condition $( t ( 2 4 4 ) = 2 . 0 5 4 , p < 0 . 0 5 )$ and in the biased PRA condition $( t ( 2 4 4 ) = 2 . 4 5 7 , p < 0 . 0 5 )$ indicating that participants assigned to the warning with advice conditions had significantly more hits and significantly fewer false alarms than those assigned to the warning with no advice condition. These results support H2(a) and H2(b).

Further analysis reveals an interaction between the two content design characteristics of warning messages (i.e., the inclusion and the framing of risk-handling advice). More specifically, there was no significant difference in perceived bias between the warning with positively framed advice group and the warning with no advice group, in either the unbiased PRA condition $( t ( 2 4 4 ) = \hat { 0 . 2 7 8 } , p = 0 . 7 8 2 )$ or the biased condition $( t ( 2 4 4 ) = - 0 . 4 6 6 , p = 0 . 6 4 2 )$ . On the other hand, for participants who received a warning with negatively framed advice, perceived bias was significantly higher (lower) in the biased (unbiased) PRA condition than those receiving a warning with no advice $( t ( 2 4 4 ) = 3 . 7 9 0 , p < 0 . 0 0 1 _ { \cdot }$ $t ( 2 4 4 ) = 3 . 2 8 0 , p < 0 . 0 1 )$ . Thus, whereas the inclusion of negatively framed risk-handling advice in a warning message significantly improved participants’ detection performance, a warning message with positively framed advice did not outperform a warning message with no advice in supporting bias detection.

5.4.3. Warning with Negatively Framed Advice vs. Warning with Positively Framed Advice. In the biased (unbiased) PRA condition, the perception of bias was significantly higher (lower) for those who received a warning with negatively framed advice than for those receiving a warning with positively framed advice 4t42445 = 30324, p < 0001; t42445 = 30003, p < 0001), suggesting that participants assigned to the warning with negatively framed advice condition had more hits and fewer false alarms than those assigned to the warning with positively framed advice condition. These results support H3(a) and H3(b).

5.4.4. Supplementary Analyses. Supplementary analyses were conducted to explore the pathways by which the availability and design characteristics of warning messages influence participants’ performance in detecting bias. First, ANCOVA results show that, controlling for participants’ preexisting risk perceptions regarding shopping online, those provided with a warning message perceived shopping with the assistance of the PRA to be significantly more risky than those not provided with such a message (M = 4014 versus

3.43, $F ( 1 , 4 9 3 ) = 3 4 . 9 3 8 , p < 0 . 0 0 1 )$ , suggesting that the availability of warning messages indeed lowered participants’ decision threshold by increasing the expected base rate of manipulative practices. Results of a regression analysis also reveal a significant positive relationship between perceived risk of shopping with the assistance of a PRA and perceived bias in the PRA’s recommendations $( F ( 1 , 4 9 4 ) = 1 3 . 1 2 2 , p < 0 . 0 0 1 )$

In addition, results of cross-tab analysis reveal that it was significantly more likely for the participants to use the search-by-brand functionality (the risk-handling act advocated in the warning message that included advice) (1) in the warning with advice condition than in the warning with no advice condition (43.1% versus $1 2 . 9 \% , \chi ^ { 2 } ( 1 , \breve { N } = 4 9 6 ) = 5 6 . 2 2 4 , p < 0 . 0 0 1 )$ , and (2) in the warning with negatively framed advice condition than in the warning with positively framed advice condition (50% versus $3 6 . 3 \% , \chi ^ { 2 } ( 1 , N = 2 4 8 ) = 4 . 7 5 1 , p < 0 . 0 5 )$ suggesting that the two content design characteristics of warning messages did influence participants discriminant ability (by providing them with the right tool/information). An ANOVA was also run with the predictor being the use of the search-by-brand functionality and dependent variable being perceived bias. Results of the analysis show that in the biased PRA condition, the level of perceived bias was significantly higher for those who used the search-by-brand functionality than those who did not $( M = 4 . 5 3$ versus 3.23, $F ( 1 , 2 4 6 ) = 4 0 . 6 5 8 $ $p < 0 . 0 0 1 )$ . However, in the unbiased PRA condition, perceived bias did not differ significantly between those who used the search-by-brand functionality and those who did not $( M = 2 . 3 { \dot { 7 } }$ versus 2.58, F 411 2465 = 10547, $p < 0 . 1 )$ . The results suggest that participants who used the search-by-brand functionality had a higher detection performance (indicated by more hits and a similar number of false alarms) than those who did not use this functionality.

Insomuch as perceived $r i s k ^ { 1 1 }$ and use of the search-bybrand functionality<sup>12</sup> could be considered surrogates for decision threshold and discriminant ability, respectively, the results of the supplementary analyses suggest that the availability and content design (i.e., the inclusion and framing of risk-handling advice) of warning messages affect consumers’ performance in detecting PRA bias via their influence on consumers’ decision threshold and discriminant ability, respectively.

## 6. Discussion and Conclusions

This section summarizes the major findings of this study, presents its contributions to research and practice, and discusses its limitations.

## 6.1. Discussion of Findings

Most of the hypotheses advanced are supported by data (except for H1(b), which is partially supported). The three warning mechanisms examined in this study, namely, warning with no advice, warning with positively framed advice, and warning with negatively framed advice, are effective, albeit to different extents, in supporting consumers in the task of detecting PRA manipulationbased anomalies. Although all three warning mechanisms were effective in enhancing the hit rates in detecting anomalies in a biased PRA (with warning messages with negatively framed advice producing the greatest number of hits), providing consumers with a warning message with no advice or a warning message with positively framed advice also increased the likelihood that consumers would perceive bias in the recommendations of an unbiased PRA, resulting in higher false alarm rates. Overall, the results of the study show that, in the PRA-assisted shopping context, the provision of warning messages with negatively framed advice is the most effective mechanism in supporting consumers in bias detection.

In sum, the results of this study provide answers to the research questions that initially motivated the research. The inclusion of risk-handling advice in a warning message does not uniformly enhance consumers’ performance in detecting biased recommendations from a PRA; the persuasiveness of the risk-handling advice is contingent on how it is framed. More specifically, compared to positively framed advice accentuating the gain from following the advice, negatively framed advice emphasizing the loss from not following the advice is more effective in motivating consumers to engage in the risk-handling behavior advocated in the advice and thus achieve superior detection performance (indicated by more hits and fewer false alarms).

## 6.2. Contributions to Research

This study makes significant contributions to research. First, it contributes to IS literature by examining factors relevant to a potential detection support mechanism— warning—that influence consumers’ performance in detecting biased product recommendations from e-commerce PRAs. Drawing on signal detection theory and its associated mechanisms of decision threshold and discriminant ability, as well as the literature on warning and message framing, we rationalize that a warning message by its nature places consumers in a heightened state of alertness and lowers their decision threshold in judging ambiguous cues as anomalies resulting from bias, which may increase the likelihood that consumers will perceive bias in the recommendations of both a biased PRA and an unbiased one, resulting in higher rates of false alarms as well as higher rates of hits. In addition, we contend that the inclusion of risk-handling advice in a warning message (a content design characteristic identified in our study) provides consumers with strategies to address the risk of PRA bias and thus enhances consumers’ discriminant ability to compensate for the impact of lowered decision threshold, resulting in high rates of hits without simultaneously increasing false alarm rates. Because the risk-handling advice included in the warning message is effective only to the extent that consumers adopt the risk-handling behavior (i.e., taking extra search action) advocated in the advice, we further postulate that, in the context of detecting PRA bias (a detection behavior involving the possibility of unpleasant outcome), negatively framed advice included in a warning message will be more effective than positively framed advice in motivating consumers to engage in the risk-handling behavior the advice encourages.

The findings of our study provide strong evidence that although consumers are generally vulnerable to online manipulations, properly designed detection support mechanisms (such as warning) can be implemented to help consumers perform better in detecting such practices. Although all three warning mechanisms examined in this study $( \mathrm { i . e . , }$ warning with no advice, warning with positively framed advice, and warning with negatively framed advice) are effective in enhancing the hit rates in detecting bias, warning with negatively framed advice is the only intervention that achieves this without increasing false alarms. Insomuch as high hit rates and low false alarm rates are indicators of superior detection performance (Xiao 2010), this study highlights warning with negatively framed advice as the most effective mechanism in supporting consumers in detecting bias in PRA recommendations.

Second, this study fills a void in existing research in warning by examining the design characteristics of warning messages, rather than focusing on the presence or absence of warning messages. Integrating prior research in product warning labels with literature in message framing literature, this study identifies two content design characteristics of warning messages (i.e., inclusion of risk-handling advice and framing of risk-handling advice) and investigates their impact on consumers’ detection performance. The findings of this study enhance our understanding of the effectiveness of different warning designs in improving detection performance and lay a foundation for future empirical as well as theoretical work.

Third, this study adds to an increasing body of IS research in persuasive communication (e.g., Angst and Agarwal 2009, Cheng and Wu 2010, Johnston and

Warkentin 2010). Extending insights from studies of goal framing effectiveness in health decision making to the context of designing warning messages to support consumers in detecting PRA bias, this study postulates and confirms previous findings with strong empirical evidence that when the behavior being promoted is a detection (as opposed to prevention) behavior, persuasive messages framed in terms of potential losses are more effective in motivating targeted behavior than factually equivalent messages framed in terms of potential gains. The powerful effect of goal framing revealed in this study also suggests that the framing manipulation employed in this study is successful and can be adopted (and further tested) by other researchers in future research.

## 6.3. Contributions to Practice

This study reveals that consumers are extremely vulnerable to biased online PRAs, a finding consistent with prior research in manipulative online business practices (Grazioli 2004; Grazioli and Jarvenpaa 2000, 2001, 2003a, b; Grazioli and Wang 2001). The mean value of perceived bias was 3.61 for the biased PRA condition, which was at about the midpoint of the seven-point scale. Of all of the 248 participants assigned to the biased PRA condition, only 114 of them (or 46%) had an average perceived bias score over 4.0, indicating that they perceived bias in the PRA’s recommendations. Even for those who had received warnings about potential PRA bias, only 99 of them (out of 186, approximately 53%) had an average perceived score over 4.0, suggesting the difficulty for consumers to detect bias in the PRA’s recommendations. Therefore, it is imperative for government agencies (e.g., the Federal Trade Commission in the United States, the Office of Consumer Affairs in Canada), industry leaders (e.g., Amazon, Expedia, Dell), and consumer organizations (e.g., the National Consumers League in the United States, the Consumers’ Association of Canada) to not only promote consumer awareness of novel manipulative practices made possible by innovative technologies supporting e-commerce but also educate consumers on strategies to address such risks. For instance, consumers may be advised to verify PRAs’ recommendations by using the comparison and searching tools available at both the e-commerce website and outside of the website (for instance, at an independent, third-party comparison shopping platform).

In addition to promoting consumer awareness and education, it is also important for government, industry, and consumer organizations to establish guidelines for good business practice for online companies. For example, a guideline may strongly recommend, if not require, e-commerce websites featuring a PRA to implement functionalities that allow consumers to sort/search/compare all products (not only those recommended by the PRA) by brand, price, and important product features; such functionalities will enable consumers to detect bias in the PRA’s recommendations more easily. The guideline may also recommend that, in addition to providing an explanation regarding the PRA’s reasoning logic, the website should provide a fit score for each product (in the recommendation list) and a detailed explanation as to how the score is calculated. Strong, enforceable self-regulation and self-policing by industry members are critical to addressing the growing problem of PRA bias.

This study also offers insights into the design and effectiveness of different warning mechanisms, not only in the context of detecting biased PRAs but also in an anomaly detection context in general. Prior empirical evidence indicates that explicit warning about the possibility of manipulation may increase the hit rate at the cost of increased false alarms (Burgoon et al. 1994, Parasuraman 1984). False alarms may be tolerated in an environment where the danger of strategic manipulation is real and deplorable, and thus boosting the hit rates is more important than reducing the false alarm rates (Xiao and Benbasat 2015). However, in many cases, false alarms are costly, because they will have to be evaluated individually to confirm/disconfirm their accuracy, which demands resources, time, and effort (George et al. 2004).

From a business perspective, the most desirable detection support mechanism is one that would enhance detection performance without incurring the additional costs associated with increased false alarms (George et al. 2004). Ultimately, the purpose of any detection support mechanism is to protect consumers in e-commerce transactions rather than deter them from engaging in e-commerce. Examining empirically the design characteristics of warning messages (a commonly used detection support mechanism), this study shows that properly designed warning messages can enhance consumers’ performance (indicated by high hit rate and low false alarm rate) in detecting anomalies resulting from strategic manipulations. The results of the study further reveal that a promising intervention is to provide consumers with warning messages that include negatively framed risk-handling advice, which encourages consumers to exploit the search and compare functionalities typically available at e-commerce websites to protect themselves from being misled when shopping online. It is understandable that online merchants may be reluctant to warn consumers of potential manipulative practices. Thus, the warning intervention can be implemented as browser extension (similar to existing antiphishing, antifraud, and privacy protection extensions to browsers<sup>13</sup>) available from third-party consumer protection organizations. Once the extension is downloaded and installed to a browser by consumers, a warning message can be triggered when consumers visit e-commerce websites that implement PRAs. Nevertheless, if a merchant does voluntarily integrate the warning mechanism to its website, the merchant may be perceived by consumers as benevolent and honest, and the consequent increased trust may lead to more customers following the recommendations of the PRA (featured at the merchant’s website) and buying from the merchant.

## 6.4. Limitations and Suggestions for Future Research

A number of limitations are involved with this study. First, the study examines one way by which online PRAs provide biased product recommendations to consumers, namely, to recommend products from a set of promoted products rather than from all available products. The application of this study’s findings to other types of manipulation techniques requires caution. Other manipulation techniques (e.g., those designed to influence consumers’ decision criteria by selectively including product attributes in the PRA’s preference-elicitation interface or by providing false decisional guidance; see Xiao and Benbasat 2011) may have different effects on consumers’ performance in detecting anomalies in PRAs; hence, additional research is needed.

Second, in this study, the different types of warning messages were implemented as being issued by a thirdparty organization independent from the e-commerce website featuring the PRA. We also suggest that in the real world, the warning intervention (as well as other similar detection support mechanisms) should be implemented as a third-party, freely downloadable browser extension. Although our study demonstrates the effectiveness of warning mechanisms (particularly the one that includes risk-handling advice) in supporting consumers in detecting biased PRAs, future research is needed to investigate whether and how such mechanisms can be employed effectively in practice. For instance, what factors will motivate consumers to exert the effort to download and install the browser extension? Under what circumstances and how often should warning messages be displayed to cause minimum interruption and annoyance to consumers’ shopping process? Could our suggested implementation of warning mechanisms induce a backlash (and further strategic actions) from online merchants? If so, how can their negative impact be mitigated? Additionally, although warning with negatively framed advice outperforms the other two types of warning messages (i.e., warning with no advice and warning with positively framed advice), it still results in a false alarm rate of 22.58% (with false alarm rates being 40.98% and 37.70% for consumers receiving the other two types of warning messages, respectively; see Table E.1 in the online appendix), suggesting the need for further improvement in the design of warning messages.

Third, the advice (included in the warning messages) examined in this study, which encourages consumers to exert extra search effort using the search and compare functionalities available at e-commerce websites, is only one example of how risk-handling advice can be phrased to provide consumers with knowledge and skills to address the risk of PRA bias. The focus of our study is not on what advice to provide, but rather on how to better design warning messages and the advice included, to motivate consumers to change their behavior in accordance with the advice (whatever that is) included in the warning messages. Given the multitude of means by which bias can be introduced by PRAs, future research is needed to explore what the most appropriate informational content of riskhandling advice is for biases introduced from various other sources.

Fourth, in our study, the “comparison matrix” and “search-by-brand” functionalities were built into the e-commerce website. We acknowledge that in reality, unscrupulous online merchants may be reluctant to provide such functionalities on their websites. Nevertheless, because functionalities that facilitate search and encourage discovery have become must-have features of e-commerce sites (Dunn 2007, Mulpuru 2013), their absence may be a cause for consumer alarm (particularly when consumers receive warning messages from an independent party). Furthermore, consumers can make use of other websites to search and compare products of interest. Online merchants delivering biased recommendations are thus caught in a bind on whether or not to provide comparison and search functionalities on their websites—in either case, the biases may be revealed. Future research may explicitly compare consumers’ detection performance when these functionalities are present or absent on e-commerce websites.

Last, this study empirically examines the effects of different design characteristics of warning messages on consumers’ bias detection performance. Future studies may explore other detection support mechanisms (both non-IT-based and IT-based; for examples, see Xiao and Benbasat 2011), which can be implemented in the e-commerce context to support consumers in detecting the strategic manipulations perpetrated by online companies.

## 6.5. Conclusion

The increasing adoption of PRAs by e-commerce merchants makes it a desirable area of study for IS researchers. This study represents an early effort to look into PRAs that base recommendations on business criteria (rather than on consumer benefits) and examine how warning messages can be designed to support consumers in detecting biased recommendations by PRAs. We have identified two content design characteristics of warning messages—the inclusion of risk-handling advice and the framing of risk-handling advice—and investigated how they influence consumers’ detection performance. Our results reveal that the provision of a simple warning message without advice is a doubleedged sword, because it increases correct detection of biased PRAs (hits) at the cost of increased incorrect detection (false alarms). By contrast, including in warning messages risk-handling advice about how to check for bias (particularly when the advice is framed to emphasize the loss from not following the advice) increases correct detection and, more importantly, also decreases incorrect detection. Our study also provides evidence suggesting that these effects are attributable to the two theoretical mechanisms of signal detection theory, namely, decision threshold and discriminant ability. With an enriched understanding of how the availability and the content design of warning messages can support consumers in the context of PRA-assisted online shopping, these results serve as a basis for future theoretical development and yield valuable insights that can guide practice.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2015.0592.

## Acknowledgments

The authors thank the Natural Science and Engineering Research Council of Canada and the Social Science and Humanities Research Council of Canada for their support of this research. The authors are grateful to the senior editor, associate editor, and anonymous reviewers for their constructive feedback during the review process.

## Appendix: Hit Rates and False Alarm Rates

Upon completion of the experimental task at the e-commerce website, participants were asked three questions (with a sevenpoint scale) about whether they had perceived bias in the PRA’s recommendations. Following Grazioli (2004), we coded the responses of participants who answered “mildly agree,” “agree,” or “strongly agree” to any of the three questions as “1,” indicating that these participants did perceive bias in the PRA’s recommendations. By contrast, responses of participants who answered otherwise (i.e., “strongly disagree,” “disagree,” or “mildly disagree”) were coded as “0,” meaning that the participants did not perceive bias in the PRA’s recommendations. Finally, responses of participants (14 in total) who answered “neutral” (i.e., the midpoint of the seven-point scale) were labeled “undecided” and excluded from the subsequent analysis. Table A.1 summarizes the results of the coding practice, on the basis of which we derived the hit rate and false alarm rate for each experimental condition.

Table A.1 Results of Coding Practice

<table><tr><td rowspan="3" colspan="2">Availability and content design of warning message</td><td colspan="2">Unbiased PRA</td><td colspan="2">Biased PRA</td><td rowspan="3">Hit rate (%)</td><td rowspan="3">False alarm rate (%)</td></tr><tr><td colspan="2">Bias perceived</td><td colspan="2">Bias perceived</td></tr><tr><td>0(No)</td><td>1(Yes)</td><td>0(No)</td><td>1(Yes)</td></tr><tr><td>No warning</td><td>Count</td><td>50</td><td>10</td><td>38</td><td>21</td><td>35.59</td><td>16.67</td></tr><tr><td>Warning with no advice</td><td>Count</td><td>36</td><td>25</td><td>23</td><td>34</td><td>59.65</td><td>40.98</td></tr><tr><td>Warning with positively framed advice</td><td>Count</td><td>38</td><td>23</td><td>21</td><td>40</td><td>65.57</td><td>37.70</td></tr><tr><td>Warning with negatively framed advice</td><td>Count</td><td>48</td><td>14</td><td>10</td><td>51</td><td>83.61</td><td>22.58</td></tr></table>

## References

Aksoy L, Bloom PN (2001) Impact of ordered alternative lists on decision quality: The role of perceived similarity. Proc. Soc. Consumer Res. Winter Conf., Scottsdale, AZ.

Angst CM, Agarwal R (2009) Adoption of electronic health records in the presence of privacy concerns: The elaboration likelihood model and individual persuasion. MIS Quart. 33(2):339–370.

Argo JJ, Main KJ (2004) Meta-analyses of the effectiveness of warning labels. J. Public Policy Marketing 23(2):193–208.

Banks SM, Salovey P, Greener S, Rothman AJ, Moyer A, Beauvais J, et al. (1995) The effects of message framing on mammography utilization. Health Psych. 14(2):178–184.

Bellman S, Johnson EJ, Lohse GL, Mandel N (2006) Designing marketplaces of the artificial with consumers in mind: Four approaches to understanding consumer behavior in electronic environments. J. Interactive Marketing 20(1):21–33.

Biros DP (1998) The effects of truth bias on artifact-user relationships: An investigation of factors for improving deception detection in artifact produced information. Working paper, Florida State University, Tallahassee.

Biros DP, George JF, Zmud RW (2002) Inducing sensitivity to deception in order to improve decision making performance: A field study. MIS Quart. 26(2):119–144.

Burgoon JK, Buller DB, Ebesu AS, Rockwell P (1994) Interpersonal deception: V. Accuracy in deception detection. Comm. Monographs 61(4):303–325.

Chau PY, Ho SY, Ho KK, Yao Y (2013) Examining the effects of malfunctioning personalized services on online users’ distrust and behaviors. Decision Support Systems 56(1):180–191.

Cheng FF, Wu CS (2010) Debiasing the framing effect: The effect of warning and involvement. Decision Support Systems 49(3):328–334.

Cosley D, Lam SK, Albert I, Konstan J, Riedl J (2003) Is seeing believing? How recommender systems influence users’ opinions. Proc. SIGCHI Conf. Human Factors in Computing Systems, Fort Lauderdale, FL, 585–592.

Davis DR, Parasuraman R (1981) The Psychology of Vigilance (Academic Press, London).

Demery P (2013) Site personalization has room to grow among Top 500 retailers. Internet Retailer (May 15), http://www .internetretailer.com/2013/05/15/site-personalization-has-room -grow-among-top-500-retailers.

Detweiler JB, Bedell BT, Salovey P, Pronin E, Rothman AJ (1999) Message framing and sun screen use: Gain-framed messages motivate beach-goers. Health Psych. 18(2):189–196.

Dunn T (2007) Filter and sort: Improving ecommerce product findability. Webcredible (April 1), http://www.webcredible.co.uk/ user-friendly-resources/web-usability/ecommerce-findability .shtml.

Fishbein M, Ajzen I (1981) Acceptance, yielding, and impact: Cognitive processes in persuasion. Petty RE, Ostrom TM, Brock TC, eds. Cognitive Responses in Persuasion (Lawrence Erlbaum, Hillsdale, NJ), 339–359.

George JF, Marett K (2004) Inhibiting detection and its detection. Proc. 37th Ann. Hawaii Internat. Conf. System Sci (IEEE Computer Society, Big Island, HI).

George JF, Marett K, Tilley P (2004) Deception detection under varying electronic media and warning conditions. Proc. 37th Hawaii Internat. Conf. System Sci. (IEEE Computer Society, Big Island, HI).

Gerend MA, Sias T (2009) Message framing and color priming: How subtle threat cues affect persuasion. J. Experiment. Soc. Psych. 45(4):999–1002.

Grazioli S (2004) Where did they go wrong? An analysis of the failure of knowledgeable Internet consumers to detect deception over the Internet. Group Decision Negotiation 13(2):149–172.

Grazioli S, Jarvenpaa SL (2000) Perils of Internet fraud: An empirical investigation of deception and trust with experienced Internet consumers. IEEE Trans. Systems, Man, Cybernetics 30(4):395–410.

Grazioli S, Jarvenpaa SL (2001) Tactics used against consumers as victims of Internet deception. Proc. Seventh Americas Conf. Inform. Systems (AIS, Boston), Paper 158.

Grazioli S, Jarvenpaa SL (2003a) Consumer and business deception on the Internet: Content analysis of documentary evidence. Internat. J. Electronic Commerce 7(4):93–118.

Grazioli S, Jarvenpaa SL (2003b) Deceived: Under target online. Comm. ACM 46(12):196–205.

Grazioli S, Wang A (2001) Looking without seeing: Understanding unsophisticated consumers’ success and failure to detect Internet deception. Proc. 22nd Internat. Conf. Inform. Systems (AIS, New Orleans), 193–203.

Green DM, Swets JA (1966) Signal Detection Theory and Psychophysics (John Wiley, New York).

Haubl G, Murray K (2003) Preference construction and persistence in digital marketplaces: The role of electronic recommendation agents. J. Consumer Psych. 13(1–2):75–91.

Haubl G, Murray KB (2006) Double agents: Assessing the role of electronic product-recommendation systems. Sloan Management Rev. 47(3):8–12.

Haubl G, Trifts V (2000) Consumer decision making in online shopping environments: The effects of interactive decision aids. Marketing Sci. 19(1):4–21.

Hill DJ, King MF, Cohen E (1996) The perceived utility of information presented via electronic decision aids: A consumer perspective. J. Consumer Policy 19(2):137–166.

Johnson PE, Grazioli S, Jamal K (1993) Fraud detection: Intentionality and deception in cognition. Accounting, Organ. Soc. 18(5):467–488.

Johnson PE, Grazioli S, Jamal K, Berryman RG (2001) Detecting deception: Adversarial problem solving in a low base-rate world. Cognitive Sci. 25(3):355–392.

Johnston AC, Warkentin M (2010) Fear appeals and information security behaviors: An empirical study. MIS Quart. 34(3):549–566.

Kelley CA, Gaidis WC, Reingen PH (1989) The use of vivid stimuli to enhance comprehension of the content of product warning messages. J. Consumer Affairs 23(2):243–266.

Kim R (2011) Why eBay is buying recommendation engine Hunch. Gigaom (November 21), https://gigaom.com/2011/11/21/why -ebay-is-buying-recommendation-engine-hunch/.

King MF, Hill DJ (1994) Electronic decision aids: Integration of a consumer perspective. J. Consumer Policy 17(2):181–206.

Komiak SY, Benbasat I (2008) A two-process view of trust and distrust building in recommendation agents: A process-tracing study. J. Assoc. Inform. Systems 9(12):727–747.

Levin IP, Gaeth GJ, Schreiber J (2002) A new look at framing effects: Distribution of effect sizes, individual differences, and independence of types of effects. Organ. Behav. Human Decision Processes 88(1):411–429.

Levin IP, Schneider SL, Gaeth GJ (1998) All frames are not created equal: A typology and critical analysis of framing effects. Organ. Behav. Human Decision Processes 76(2):149–188.

Limelight Networks (2010) Limelight Networks research identifies online commerce website features that create brand loyalty. (November 3), http://investors.limelightnetworks.com/press -release/limelight-networks-research-identifies-online-commerce -website-features-create-brand-l.

Marett K, George JF (2005) Group deception in computer-supported environments. Proc. 38th Ann. Hawaii Internat. Conf. System Sci (IEEE Computer Society, Big Island, HI).

Meyerowitz BE, Chaiken S (1987) The effect of message framing on breast self-examination attitudes, intentions, and behavior. J. Personality Soc. Psych. 52(3):500–510.

Miller GA (1956) The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psych. Rev. 63(2):81–97.

Miller GR, Stiff JB (1993) Deceptive Communication (Sage Publications, Newbury Park, CA).

Morrison EW, Robinson SL (1997) When employees feel betrayed: A model of how psychological contract violation develops. Acad. Management Rev. 22(1):226–256.

Mulpuru S (2013) Must-have ecommerce features. Forrester (January 29), http://www.targetmarketingmag.com/promo/ MustHaveeCommerceFeatures.pdf.

Murph D (2013) Amazon acquires Goodreads, aims to make better recommendations for Kindle users. Engadget (March 28), http:// www.engadget.com/2013/03/28/amazon-acquires-goodreads -kindle-recommendation-engine/.

O’Keefe DJ, Jensen JD (2009) The relative persuasiveness of gainframed and loss-framed messages for encouraging disease detection behaviors: A meta-analytic review. J. Comm. 59(2): 296–316.

Parasuraman R (1984) Sustained attention in detection and discrimination. Parasuraman R, Davies DR, eds. Varieties of Attention (Academic Press, London), 243–266.

Pew Research Center (2014) Internet user demographics. Accessed October 19, 2014, http://www.pewinternet.org/data-trend/ internet-use/latest-stats/.

Punj G, Moore R (2009) Information search and consideration set formation in a web-based store environment. J. Bus. Res. 62(6):644–650.

Robinson SL (1996) Trust and breach of the psychological contract. Admin. Sci. Quart. 41(4):574–599.

Ross K (1981) Legal and practical considerations for the creation of warning labels and instruction books. J. Products Liability 4(1):29–45.

Rothman AJ, Salovey P (1997) Shaping perceptions to motivate healthy behavior: The role of message framing. Psych. Bull. 121(1):3–19.

Rothman AJ, Bartels RD, Wlaschin J, Salovey P (2006) The strategic use of gain- and loss-framed messages to promote healthy behavior: How theory can inform practices. J. Comm. 56(S1): S202–S220.

Rothman AJ, Salovey P, Antone C, Keough K, Martin CD (1993) The influence of message framing on intentions to perform health behaviors. J. Experiment. Soc. Psych. 29(5):408–433.

Sandler Research (2015) Opportunities for online shopping in different countries. Accessed October 19, 2015, http://www .sandlerresearch.org/industry-views/opportunities-for-online -shopping-in-different-countries.

Scott ED (2006) Just(?) a true-false test: Applying signal detection theory to judgments of organizational dishonesty. Bus. Soc. 45(2):130–148.

Senecal S (2003) Essays on the influence of online relevant others on consumers’ online product choices. Unpublished doctoral dissertation, University of Montreal, Montreal.

Senecal S, Nantel J (2004) The influence of online product recommendations on consumers’ online choices. J. Retailing 80(2):159–169.

Stewart DW, Martin IM (1994) Intended and unintended consequences of warning messages: A review and synthesis of empirical research. J. Public Policy Marketing 13(1):1–19.

Stiff JB, Kim HJ, Ramesh CN (1992) Truth biases and aroused suspicion in relational deception. Comm. Res. 19(3):326–345.

Sullivan M (2014) Apple has acquired BookLamp and its book recommendation engine. VentureBeat (July 26), http://venturebeat .com/2014/07/26/apple-has-acquired-booklamp-and-its-book -recommendation-engine/.

Tilley PA (2005) Training, warning, and media richness effects on computer-mediated deception and its detection. Unpublished doctoral dissertation, Florida State University, Tallahassee.

Tversky A, Kahneman D (1981) The framing of decisions and the psychology of choice. Science 211(4481):453–458.

Wang W, Benbasat I (2005) Trust in and adoption of online recommendation agents. J. Assoc. Inform. Systems 6(3):72–101.

Wickens TD (2001) Elementary Signal Detection Theory (Oxford University Press, New York).

Wise J (2010) Top ten secrets of effective liars. Psychology Today (May 3), http://www.psychologytoday.com/blog/extreme-fear/ 201005/top-ten-secrets-effective-liars.

Witte K, Allen M (2000) A meta-analysis of fear appeals: Implications for effective public health campaigns. Health Ed. Behav. 27(5): 591–615.

Xiao B (2010) Product-related deceptive information practices in B2C e-commerce: Formation, outcomes, and detection. Unpublished doctoral dissertation, University of British Columbia, Vancouver.

Xiao B, Benbasat I (2007) E-commerce product recommendation agents: Use, characteristics, and impact. MIS Quart. 31(1):137–209.

Xiao B, Benbasat I (2011) Product-related deception in e-commerce: A theoretical perspective. MIS Quart. 35(1):169–195.

Xiao B, Benbasat I (2014) Research on use, characteristics, and impact of e-commerce product recommendation agents: A review and update for 2007–2012. Martínez-López FJ, ed. Research Handbook on e-Business Strategic Management, Vol. 3 (Springer, Berlin Heidelberg), 403–431.

Xiao B, Benbasat I (2015) Consumer vulnerability to biased product recommendations in online buying: The influence of perceived personalization. Working paper, University of Hawaii at Manoa, Honolulu.

Xu J, Benbasat I, Cenfetelli RT (2014) The influences of online service technologies and task complexity on efficiency and personalization. Inform. Systems Res. 25(3):420–436.
