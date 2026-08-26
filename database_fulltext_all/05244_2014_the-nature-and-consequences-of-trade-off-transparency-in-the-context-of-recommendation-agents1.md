---
otero_id: 5244
otero_key: "JUHBVZEC"
title: "The Nature and Consequences of Trade-Off Transparency in the Context of Recommendation Agents1"
authors: "Jingjun (David) Xu; Izak Benbasat; Ronald T. Cenfetelli"
year: "2014"
journal: "MIS Quarterly"
doi: "10.25300/misq/2014/38.2.03"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# THE NATURE AND CONSEQUENCES OF TRADE-OFF TRANSPARENCY IN THE CONTEXT OF RECOMMENDATION AGENTS<sup>1</sup>

Jingjun (David) Xu W. Frank Barton School of Business, Wichita State University, 1845 Fairmount Street, Wichita, KS 67260 U.S.A. {david.xu@wichita.edu}

Izak Benbasat and Ronald T. Cenfetelli

Sauder School of Business, University of British Columbia, 2053 Main Mall, Vancouver, BC V6T 1Z2 CANADA {benbasat@sauder.ubc.ca} {cenfetelli@sauder.ubc.ca}

That recommendation agents (RAs) can substantially improve consumers’ decision making is well understood. Far less understood is the influence of specific design attributes of the RA interface on decision making and other outcome measures. We investigate a novel design for an RA interface that enables it to interactively demonstrate trade-offs among product attribute values (i.e., trade-off transparency feature) to improve consumers’ perceived product diagnosticity and perceived enjoyment. We also examine the extent to which the trade-offs among product attribute values should be revealed to the user. Further, based on the stimulus– organism–response model, we develop a theoretical model that extends the effort–accuracy framework by proposing perceived enjoyment and perceived product diagnosticity as two antecedents for perceived decision quality and perceived decision effort, respectively. In an experimental study, we find that (1) the trade-off transparency feature significantly affects perceived enjoyment and perceived product diagnosticity, (2) perceived enjoyment and perceived product diagnosticity follow an inverted U-shaped curve as the level of tradeoff transparency increases, (3) although users spend more time understanding attribute trade-offs with the trade-off transparency feature, they are more efficient in selecting a product, (4) perceived enjoyment simultaneously leads to better perceived decision quality and lower perceived decision effort, and (5) perceived product diagnosticity leads to better perceived decision quality without compromising perceptions of decision effort. Theoretically, this study increases our understanding of how the design of an RA interface can improve consumers’ product diagnosticity and enjoyment, and proposes two antecedents to improve perceived decision quality and reduce perceived decision effort. For design practitioners, our results indicate the importance of providing the trade-off transparency design feature to potential consumers.

Keywords: Interface design, task complexity, recommendation agents (RAs), trade-off transparency, perceived enjoyment, perceived product diagnosticity, perceived decision effort, perceived decision quality

## Introduction

The large variety and quantity of products available on the Internet have given rise to the need for product recommendation agents (RAs) that assist consumers in choosing the “right” products (Ricci and Werthner 2006). RAs provide assistance by eliciting the purchasing needs of consumers and then making product recommendations that satisfy these preferences (Xiao and Benbasat 2007). As e-business matures, the effectiveness enabled by RAs is recognized as a key success factor for organizations confronted with growing competitive pressures (Ahn 2006; Kamis and Stohr 2006; Liao et al. 2005; Palanivel and Sivakumar 2010).

Properly designed, RAs hold the promise of increased sales and customer loyalty (Berman 2002). However, a poorly designed RA may result in lost sales and frustrated consumers. According to Andrew Coates, CEO of AgentArts, a leading personalization and recommendation technology company, the user interface layer is “the critical difference as to how visible and accessible recommendations really are” (Leavitt 2006, p. 17). Gretzel and Fesenmaier (2006) emphasized the importance of the cues provided in the course of a user–technology interaction. While the importance of the RA’s user interface has been emphasized by practitioners (e.g., Leavitt 2006, p. 15) and scholars (e.g., Gretzel and Fesenmaier 2006), the user interface to implement the RA and the influence of the interface on various outcome measures are still not well understood (Hess et al. 2009; Kamis et al. 2010).

A central function of RAs is to capture consumers’ product attribute preferences, which then allows for the identification of products appropriate for a consumer’s interests (Xiao and Benbasat 2007). Because of the conflicting values of product attributes (Goldstein et al. 2001), trade-offs are inherent in many purchase choices (Bettman et al. 1998; Häubl and Murray 2003). For example, a laptop computer’s faster processor comes with a higher price, and its larger screen size comes with a heavier weight. In consumer decision making, a consumer’s awareness of trade-offs is a double-edged sword. On one hand, consumers often avoid trade-offs because attributes might link to important self-goals and trading them (i.e., the realization that some attribute targets may not be fulfilled) could cause a significant negative affect in certain decision contexts (Drolet and Luce 2004; Lee and Benbasat 2011; Luce et al. 1999). On the other hand, explicit considerations of the trade-offs among product attributes are helpful for more accurate decision making (e.g., Delquie 2003; Frisch and Clemen 1994). When expressing their needs and preferences to RAs, without a reasonable understanding of attribute value trade-offs, users may overestimate their real needs/desires and RAs may end up presenting them with product choices that do not fit their needs. Consequently, users might have unfavorable perceptions of RAs and discontinue using them (Wang and Benbasat 2007). Thus, a gap that needs to be filled in the literature is addressing the conflicting outcomes of trade-off awareness such that an RA input interface can make explicit to the consumer the trade-offs in product attribute values without compromising the user experience with the RA.

The first objective of this paper is to address this gap by improving the communication interface between an RA and its users during the preference elicitation stage (i.e., input stage). Specifically, we propose a trade-off transparent RA that interactively demonstrates the trade-offs among product attribute values, and we evaluate the effects of the trade-off transparency feature in terms of perceived enjoyment and perceived product diagnosticity. These two constructs respectively capture a user’s affective and cognitive experience with RAs. With such an RA, consumers are expected to have an enjoyable user experience and a better understanding of these attribute value trade-offs, allowing them, in turn, to provide better inputs to the RA that reflect their needs. For example, a trade-off transparent RA will reveal to users the trade-off relationship between price and screen size of a LCD HDTV. This trade-off transparency feature is a novel addition to RA design heretofore unconsidered in the RA research literature (e.g., Häubl and Trifts 2000; Hess et al. 2005; Kamis et al. 2008; Kamis et al. 2010; Komiak and Benbasat 2006; Tam and Ho 2005; Wang and Benbasat 2009).

That user evaluations, behavior, task performance, and decision outcomes change as the task complexity faced by users increases is well understood (Kamis et al. 2008; Jiang and Benbasat 2007a; Tan et al. 2010). With that in mind, we investigate the different levels of trade-off transparency as a form of task complexity. This can be illustrated with the selection of a laptop computer: when the level of trade-off transparency is low, users are able to evaluate fewer trade-offs among attribute values, such as those between price and a number of other attributes (e.g., hard-drive capacity). As trade-off transparency increases, users become more aware of additional trade-off relationships beyond those associated with price, such as the trade-off between weight and screen size. An individual may desire a larger screen size but fulfilling that desire comes at the expense of increased weight. When the trade-off transparency increases further, a user becomes even more aware of the need to manage a more significant number of trade-offs but their evaluation of the transparency function might be different because of the increased effort required.

As a second objective, we draw on cognitive load theory to predict that trade-off transparency should be maintained at a certain level to achieve optimal outcomes in terms of perceived product diagnosticity and perceived enjoyment. This perspective recognizes that at some level, trade-off transparency increases to a point at which it overburdens users’ cognitive limitations and is counterproductive.

The third objective of this paper is to extend and indeed challenge the effort–accuracy framework. Payne et al. (1993) state that a consumer’s decision-making process is often influenced by the trade-off between the accuracy of the decision and the effort required to make the decision: more accurate decisions come at the expense of more effort. Their research, among other studies, supported the effects of such a conflict. However, the possibility that RAs can address this dilemma to enable more accurate decisions to be made without simultaneously increasing effort has been overlooked. Grounded in the stimulus–organism–response (S-O-R) model, we develop a theoretical model that extends the effort– accuracy framework and allows us to investigate the role of trade-off awareness as an influence and possible solution to the longstanding effort–accuracy conflict.

## Theoretical Foundations

With the objective of investigating the effect of the trade-off transparency feature and its different levels, we review the S-O-R model in environmental psychology (Mehrabian and Russell 1974). The S-O-R model posits that the various stimuli within a shopping environment together affect a consumer’s affective and/or cognitive processes (organism), which in turn determine the consumer’s responses. Stimuli are cues external to the customer that rouse or incite them (Belk 1975). Stimuli may manifest themselves in different ways, for example, as a product display or a store’s environment (Jacoby 2002). In the context of online shopping, stimuli pertain to the design features of e-commerce websites with which consumers interact (Eroglu et al. 2003), such as a website’s visual appeal (Parboteeah et al. 2009) and interactivity (Jiang et al. 2010). The organism refers to the intervening processes (e.g., emotive and cognitive systems) between the stimuli and the reaction of the consumer (Bagozzi 1986). Response refers to behavioral responses or internal responses that may be expressed, such as impressions and/or judgments of quality (Jacoby 2002, p. 55).

Past psychology and marketing research has widely adopted the S-O-R model with promising results to model the impact of environmental stimuli on consumer responses in both offline and online shopping contexts (e.g., Baker et al. 1994; Eroglu et al. 2001, 2003; Fiore and Kim 2007; Sherman et al. 1997). Several studies on information systems drew on the S-O-R paradigm as a theoretical framework to explain how website features may affect web consumers and their behavior (Jiang et al. 2010; Koufaris et al. 2002; Parboteeah et al. 2009).

As such, the S-O-R model serves as an appropriate overarching framework for our own theoretical model (see Figure 1). Following the S-O-R model, this study operationalizes stimulus as the trade-off transparency feature of an online RA; organism as the user’s enjoyment (affective system) and perceived product diagnosticity (cognitive system); and response as the user’s perceived decision quality and perceived decision effort. We elaborate on the stimulus, organism, and response in each of the following subsections.

## Trade-Off Transparency as Environmental Stimulus

In the context of online shopping, environmental stimuli refer to the cues (e.g., colors, graphics, layout, and design) that are visible to online consumers and influence consumers’ cognitive and/or affective responses during the site visit. According to Eroglu et al. (2001, 2003) and Parboteeah et al. (2009), prior cues that can generate a cognitive reaction include product descriptions (e.g., price), reviews, ordering information, and shipping procedures that help in the attainment of the online consumer’s shopping goals. In contrast, cues such as decorative and vivid depictions (e.g., animation, cheerful colors, interactivity, and pleasant layout) influence a consumer’s affective experience with a shopping site, while they do not directly support a particular shopping goal. Certain cues are dual-natured as they can be perceived both cognitively and affectively, such as website background patterns (Eroglu et al. 2001), virtual product experience (Jiang and Benbasat 2007b), and visual appeal and information fitto-task (Parboteeah et al. 2009).

In this study, we investigate the effectiveness of a novel design—the trade-off transparency feature—of RAs in an e-commerce website. Horizontal scales, each with a “slider,” are used to represent the value of each product attribute (with low values on the left side and high values on the right side; see Figure 2). A user is able to indicate the preferred level of a product attribute by clicking and dragging the slider to a certain spot on the bar. The feature unique to our trade-off transparent RA is that the placement of the slider on a given level of an attribute will lead to an immediate real-time change in one or more of the values for other related attributes observable to the user. The number of attributes that shift automatically is a function of the degree of trade-off transparency that the RA is designed to have. Hence, users can directly learn of the trade-off relationships among attributes when using a trade-off transparent RA.

![](/api/attachments/JUHBVZEC/fulltext/images/1b7d924af593475058d9bf981fe1be2e54b43f4624b5089aaf2722c83c679094.jpg)  
Figure 1. Proposed Theoretical Model

The trade-off transparency feature is a type of environmental stimulus. Trade-off transparency is clearly visible to online consumers, as it conveys the values of product attributes and the relationships among the product attributes, merchandising information that can influence users’ cognition and directly facilitate the shopping goal attainment (e.g., Eroglu et al. 2003; Parboteeah et al. 2009). Prior related research into RAs (e.g., Wang and Benbasat 2007, 2009) was limited to generalized explanations about how certain attributes are related to one another and that users should not overestimate their needs when indicating their product attribute preferences to the RA. Thus, the unique feature of trade-off transparency, as implemented in this study, lies in its explicit, specific, and automatic adjustment of the values of other product attribute values as the user selects a particular value for a given attribute. This visible feature can be perceived cognitively because it provides the product information that helps consumers attain their shopping goals.

Trade-off transparency not only can be perceived cognitively, but also can be perceived affectively. Cues that lead to affective reactions include animation (Eroglu et al. 2001), attractive visual cues (Parboteeah et al. 2009), and interactivity (Jiang and Benbasat 2007b). Trade-off transparency presents the relationships between attributes in an interactive manner, and synchronically responds to a user’s attribute value selections and preferences. Extensive research in the interactivity literature supports the fact that design features such as controllability, bidirectional communication, and synchronicity lead to affective reaction (Coyle and Thorson 2001; Kettanurak et al. 2001; Park and Park 2009; Teo et al. 2003; Yoo et al. 2010). If a system can enable two-way communication and respond in real time to user inputs, then users will likely have a higher sense of positive affect (Babin et al. 1994; Hoffman and Novak 1996; Jiang et al. 2010; Starbuck and Webster 1991). Because trade-off transparency has a visual interface that dynamically provides interactive feedback to users in real time, it is expected to influence users’ affective reactions.

## Enjoyment and Product Diagnosticity as Organism

As postulated in the S-O-R model, organism includes the affective and cognitive reactions to the stimulus (Bagozzi 1986). Examining a user’s affective and cognitive reactions in the context of online decision support systems (DSS)<sup>2</sup> is particularly important, as they are becoming an integral part of the online purchase process (Kamis et al. 2008). Affective reactions represent an individual’s emotional response when interacting with an environmental stimulus (Sun and Zhang 2006). To represent users’ affective reactions, we propose the construct of perceived enjoyment, which is defined as intrinsic reward derived through the use of the technology or service studied (Igbaria et al. 1996, p. 129; Nysveen et al. 2005). Perceived enjoyment is an affective measure of a user’s perception of whether or not interaction with a system is interesting and fun (Csikszentmihalyi 1977; Kamis et al. 2008; Koufaris 2002; Novak et al. 2000). The IS literature has frequently studied perceived enjoyment to capture users’ affective feelings, and such studies show it to be an important affective component (Cyr et al. 2009; Kamis et al. 2008; Koufaris 2002; Sun and Zhang 2008; Van der Heijden 2004; Xu 2006/2007; Xu et al. 2013). For example, perceived enjoyment can effectively capture users’ task-relevant cues (e.g., security seals) and mood-relevant cues (e.g., colors) (Parboteeah et al. 2009). In particular, perceived enjoyment was found to be important in representing users’ affective reactions when using an online DSS (Kamis et al. 2008).

![](/api/attachments/JUHBVZEC/fulltext/images/b1b46860e636be4e4391c522b998273fbfc881bb0e0f6fdb3ef7dc9a850e4fcc.jpg)

Compared with affective reactions, cognitive reactions refer to the users’ mental processes when they interact with the stimulus (Eroglu et al. 2003). Cognitive reactions relate to how the online user processes product-related information presented on the website (Parboteeah et al. 2009). In the IS literature, one of the most frequently studied cognitive reaction variables associated with product information is product diagnosticity, which is the extent to which a consumer believes that a system is helpful for fully evaluating a product (Jiang and Benbasat 2007a; Kempf and Smith 1998; Pavlou and Fygenson 2006). For example, product diagnosticity has been used to effectively capture consumers’ understanding of different types of product presentation formats (Jiang and Benbasat 2007a) and online reviews (Mudambi and Schuff

2010). Multiple IS studies demonstrated the importance of perceived product diagnosticity in the online shopping environment with its influence on attitudes toward the product (Jiang and Benbasat 2007b), attitude toward purchasing (Pavlou and Fygenson 2006), intention to return to a website (Jiang and Benbasat 2007a), and actual purchase (Pavlou et al. 2007). In summary, the perceived enjoyment and perceived product diagnosticity constructs used in this model to represent users’ affective and cognitive reactions are consistent with past IS literature in that they are highly relevant in the DSS context. Thus, when users interact with the trade-off transparency feature, they will have higher cognitive and affective reactions, which will in turn influence users’ responses.

## Perceived Decision Quality and Perceived Decision Effort as Responses

The response portion of the S-O-R model can be elicited in many forms, ranging from internal (i.e., nonvisible) to external (i.e., detectable), the former including changes in beliefs, impressions, and judgment of quality (Jacoby 2002, p. 55). Accordingly, in the DSS context, we operationalize the responses as users’ perceived decision quality and perceived decision effort, which also align with the two central components of the effort–accuracy framework.

According to the theory of human information processing (Payne 1982; Payne et al. 1988), humans have limited cognitive capacity to process information; thus, for them to evaluate all available alternatives in detail before making a choice is not feasible. Therefore, individuals seek to attain a satisfactory, although not necessarily an optimal, level of achievement (Simon 1955). The gist of the effort–accuracy framework (Payne et al. 1993) is that, although consumers have a number of available strategies for making choices, the strategy ultimately selected depends on some compromise between the desire to make an accurate decision and the desire to minimize cognitive effort. A large portion of the behavioral research into RAs has relied on the effort–accuracy framework of cognition to investigate the beneficial impact of decision aids on reducing the cognitive effort expended by users while also increasing their decision quality (accuracy) (Häubl and Trifts 2000; Hostler et al. 2005; Todd and Benbasat 1996). For example, Benbasat and Todd (1992, 1996) demonstrated that RAs are mainly utilized by users to conserve effort, not necessarily to improve their decision quality. Schafer et al. (2002) and Fasolo et al. (2005) found that features of RAs may lead to better decision quality but also to higher decision effort. All of these studies suggested that perceived decision quality and decision effort are the two most important user responses in a DSS context, and addressing the conflict between achieving higher decision quality without also increasing decision effort remains a challenge.

Grounded in the S-O-R model, we propose two organism variables (perceived enjoyment and perceived product diagnosticity) to extend the effort–accuracy framework in explaining how perceived enjoyment and product diagnosticity can lead simultaneously to better decision quality and lower decision effort. The use of the S-O-R framework has the following advantages: (1) it provides a parsimonious and theoretically justified way of investigating the impact of the trade-off transparency feature as environmental stimuli, (2) it allows for examination of the role of the cognitive and affective reactions to the trade-off transparency feature as an organism, and (3) it provides a theoretical rationale for studying perceptions of decision quality and decision effort as a state of mind resulting from cognitive and affective change of an organism (i.e., as a response), in contrast to past research that studied effort and quality as a direct influence of RA features (e.g., Häubl and Trifts 2000).

## Hypothesis Development

The theoretical model for the study is presented in Figure 1. As described in the previous section, the proposed model is congruent with past applications of the S-O-R model in that the basic framework (i.e., stimulus, organism, and response) is consistent with environmental psychology literature. In addition, the cues used as the stimulus (i.e., trade-off transparency of RA), as well as both the cognitive and affective reactions (i.e., perceived enjoyment and product diagnosticity), are grounded in the IS domain.

## Impact of the Trade-off Transparency Feature on Perceived Enjoyment and Perceived Product Diagnosticity

Prior research on environmental stimulus in the e-commerce context found that an interface with stimulating cues has a positive influence on users’ affective feelings with the content presented (Parboteeah et al. 2009; Sproull et al. 1996) and users will form a positive affective feeling in relation to the interface. Animated images and icons were found to be more meaningful and involving than simple text presentations (Griffith et al. 2001; Morrison and Vogel 1998). As a stimulus, the trade-off transparency feature vividly shows how the product attribute values are related to each other and can interactively respond to a user’s attribute preference indication. For example, if a user moves a slider to indicate a need for a “lighter” weight for a laptop computer, the “large” value for the screen size will automatically move to a “small” value. This interactive function is expected to draw more of the user’s attention, stimulate his or her sensory experience, and subsequently lead to positive emotional effects (Jiang and Benbasat 2007b).

Further, research indicated that users will enjoy an interface that responds to their actions (Cyr et al. 2009; Hoffman and Novak 1996; Teo et al. 2003). For example, interactivity created by frequently asked questions and online guestbooks were found to have a positive impact on users’ pleasure with websites visited (Teo et al. 2003). Similarly, interactivity resulting from flash graphics on a website has been shown to influence users’ perceived enjoyment (Cyr et al. 2009). Thus, an RA that incorporates an interactive trade-off transparency feature is expected to lead to greater perceived enjoyment compared with an RA lacking such a feature.

## Hypothesis 1: The trade-off transparency feature positively influences perceived enjoyment.

In addition to the affective response, the S-O-R model also posits that environmental stimulus has an effect on an individual’s cognitive systems, including learning performance. For example, navigation aids and security seals, as environmental stimuli, have been found to positively impact users’ cognitive reactions (Parboteeah et al. 2009). In the RA context, the number of decision aid features (i.e., sorting) used has been found to positively improve users’ perceived understanding (e.g., Hess et al. 2005). Likewise, we expect that a trade-off transparent RA will increase consumers product diagnosticity.

Our arguments can be supported by the learning literature as well. The learning literature has indicated that overall learning is improved when a learner understands the constituent parts of a concept before attempting to gain a holistic understanding of the concept (Mayer and Moreno 2003; Swanson and Law 1993). If a learner does not understand one of the constituent parts, they may not fully understand the whole. An understanding of the individual parts entails not just the nature of the individual parts themselves, but also the relationship between those parts (Swanson and Law 1993).

In the current context, relationships among product attributes are important for understanding a product. A trade-off transparent RA automatically adjusts the values of related product attributes when a certain value of an attribute is specified. For example, the trade-off transparent RA demonstrates the tradeoff relationships among product attribute values, such as how price will be adjusted by changing a value of a non-price feature (e.g., hard drive). When parts (i.e., each trade-off relationship) are presented, learners can build separate component models for each of the key parts of the product. These component models can help learners form a more complete mental model (Mayer and Chandler 2001; Sweller 1999). In summary, a trade-off transparent RA shows the exact relationship among multiple pairs of attributes and provides a holistic view of the trade-off relationships. By understanding these trade-off relationships among product attribute values, users can gain a better understanding of a product. Thus, we propose the following hypothesis.

Hypothesis 2: The trade-off transparency feature positively influences perceived product diagnosticity.

## The Levels of Trade-Off Transparency

The previous section hypothesized the overall effects of the trade-off transparency feature and asserted that increased trade-off transparency leads to higher perceived enjoyment and higher product diagnosticity. However, a limited number of revealed trade-off relationships communicated to the user exists before he or she becomes cognitively overwhelmed. This can be derived from the cognitive load theory (Sweller 1988), which is concerned with techniques for reducing working memory load to facilitate changes in long-term memory associated with schema acquisition. The theory states that if the design of learning materials is to be effective, they must keep the learner’s cognitive load at a reasonable level during the learning process. IS researchers applied cognitive load theory to examine a variety of problems, including spatial information systems (Biocca et al. 2007), electronic brainstorming (Potter and Bathazard 2004), and web search results (Vegas et al. 2007).

According to cognitive load theory, learning happens best under conditions that are aligned with human cognitive architecture. Research on working memory assumes that people only have limited working memory to process incoming information. Therefore, if one’s working memory is overloaded, the learning effect will deteriorate (Baddeley 1992). As the number of trade-off relationships revealed by the trade-off transparent RA increases beyond a certain point, the trade-off transparent RA will reach its limits in improving a user’s cognitive understanding and enjoyment. As a result, past a certain level of trade-off awareness, the user might leave behind an increasingly large number of unexamined trade-off relationships.

Task complexity<sup>3</sup> is considered one of the key determinant factors of cognitive load (Kirschner et al. 2009; van Gog et al. 2011). Wood (1986) suggested that the relationship between task complexity and productivity is likely curvilinear. Increasing levels of complexity may initially be more challenging and have a positive effect on performance (e.g., Locke et al. 1981). However, past a certain level of complexity, the resulting demands on individuals may begin to exceed their capacities to respond, creating a condition of “overload” that leads to lower performance (Wood 1986). Kamis et al. (2008) found that as the number of product alternatives increases (i.e., component complexity), perceived enjoyment and usefulness followed an inverted U-shaped curve. Likewise, we expect that as the level of trade-off transparency increases, perceived enjoyment and perceived product diagnosticity will also follow an inverted U-shaped curve. Thus, we propose the following hypotheses:

Hypothesis 3: Perceived enjoyment with the tradeoff transparent RA will follow an inverted Ushaped curve as the level of trade-off transparency increases.

Hypothesis 4: Perceived product diagnosticity with the trade-off transparent RA will follow an inverted U-shaped curve as the level of tradeoff transparency increases.

## Impacts of Enjoyment and Diagnosticity on Decision Quality and Decision Effort

Perceived enjoyment can positively influence user attitudes and satisfaction with a system interface (e.g., Griffith et al. 2001; Jiang and Benbasat 2007b; Morrison and Vogel 1998), lead to a higher level of online customer loyalty (Cyr et al. 2009), greater behavioral intention to use a system (Igbaria et al. 1996; Van der Heijden 2004), and greater likelihood of returning to a website (Kourfaris 2002). In the same view, higher levels of enjoyment are believed to positively affect perceived decision quality. With greater enjoyment, users will more actively process the information provided (Andrews and Shimp 1990; Griffith et al. 2001), resulting in a greater likelihood of selecting a high-quality product alternative. Conversely, less enjoyment may hinder the processing of product information generated by the RA, consequently hampering perceptions of decision quality. Thus, we propose the following hypothesis:

## Hypothesis 5: Perceived enjoyment leads to higher perceived decision quality.

If an interface has features that engage and entertain users, we expect that the perceived decision effort associated with the RA usage will be low. The rationale is that when users are in “a state of deep involvement with software,” they are less able to register the passage of time while engaged in interaction (Agarwal and Karahanna 2000, p. 673). Another argument is that users with higher perceived enjoyment underestimate the difficulty associated with the technologies, resulting in decreasing perceptions of decision effort (Agarwal and Karahanna 2000; Venkatesh 2000). In the case of an RA, when users find that the RA interface is interesting and appealing, they will be more involved in using the RA, and their perception of the time spent using the RA will be less compared with those who find interaction with the RA boring and dull. Therefore, we propose the following hypothesis:

## Hypothesis 6: Perceived enjoyment leads to lower perceived decision effort.

Decision quality is one of the primary objectives of a decision maker (Payne 1982). We posit that higher perceived product diagnosticity leads to higher perceived decision quality. A better understanding of the trade-off relationships of product attribute values is important to prevent users from misspecifying their product preferences and to provide realistic input of attribute preferences to the RA. For example, users with better product diagnosticity are less likely to think that a laptop with a very large screen size will be extremely light. If such an unrealistic combination of attribute values (e.g., a large laptop that has an 18-inch screen and weighs only two pounds) is desired, few, if any, matching products will be found and users will subsequently consider the quality of the product recommendation to be low. On the other hand, if more realistic attribute values are provided to the RA, the RA is more likely to recommend a better set of products that fit a user’s needs; accordingly, perceived decision quality should be higher. Thus, we propose the following hypothesis:

## Hypothesis 7: Higher perceived product diagnosticity leads to higher perceived decision quality.

Higher product diagnosticity will lead users to provide more valid input to the RA; subsequently, a better set of recommended products will be obtained. As such, they will be more likely to come across products that match their needs within the initial set of products recommended by an RA. In contrast, when a user provides unrealistic product preferences (e.g., \$200 budget for a laptop with 10 hours of battery life), the RA might not be able to recommend a matching product. Subsequently, users need to spend more cognitive effort in evaluating a longer list of product alternatives to find a desired product rather than focus on the preference-matched recommended products. Prior research showed that customers with higher product knowledge are more efficient at processing information (Eisingerich and Bell 2008) to achieve their online shopping goals. Thus, we propose the following hypothesis:

Hypothesis 8: Higher perceived product diagnosticity leads to lower perceived decision effort.

![](/api/attachments/JUHBVZEC/fulltext/images/47e5c037e319544f3ab41aa7f9cc809fdae34d3a1b6f15f0b7243b2e8fc1c781.jpg)  
Figure 3. Research Model

## Impact of Decision Quality and Decision Effort on Intention

Based on the effort–accuracy framework, users are more likely to adopt an RA if the RA helps increase their decision quality and reduce the cognitive effort expended (Häubl and Trifts 2000; Hostler et al. 2005; Wang and Benbasat 2009). If decision quality is perceived to be low, users will probably discontinue utilizing the RA. Other factors being equal, if using the RA requires additional effort, users prefer to rely on their own abilities versus the RA to make a decision. Therefore, we suggest the following hypotheses:

Hypothesis 9: Perceived decision quality is positively related to intention to use RAs.

Hypothesis 10: Perceived decision effort is negatively related to intention to use RAs.

A model summarizing the hypotheses is presented in Figure 3.

## Methodology

A four (traditional RA serving as control, trade-off transparent RA with low, medium, and high level of transparency) by two (shopping for friend versus shopping for yourself) betweensubjects design was implemented to test the hypotheses.

## Manipulation of Trade-off Transparency

As the focus of the study was on the level of trade-off transparency (i.e., coordinative complexity), we kept the number of product attributes and alternatives (i.e., component complexity) constant across all experimental groups to avoid the confounding effect between component complexity and coordinative complexity. Past research used 8, 54, and 150 product alternatives to represent low, medium, and high task complexity (Kamis et al. 2008). Thus, we choose 50 product alternatives<sup>4</sup> (see Figure 4 for sample products) to represent a moderate level of component complexity (Jiang and Benbasat 2007a; Kamis et al. 2008; Miller 1956) to avoid overwhelming users given that trade-off transparency (i.e., coordinative complexity) was manipulated at three levels.

Each laptop had eight product attributes (e.g., price, hard drive, memory, processor, screen size, weight, battery, and video card). Miller (1956) offered a general rule of thumb that the span of immediate memory is about seven plus or minus two items. The eight attributes fall within this range and represent a moderate level of component complexity. Fewer product attributes (e.g., three or four) limits the ability to manipulate the trade-off transparency, while too many attributes (e.g., 10 or 12) may create a ceiling effect of task complexity, which also diminishes the effect of trade-off transparency manipulation.

Three levels of trade-off transparency (low, medium, and high) were created by manipulating the number of trade-off

<table><tr><td></td><td>I600</td><td>M650</td><td>G300</td><td>G350</td><td>M100</td></tr><tr><td>Price</td><td>$699</td><td>$464</td><td>$399</td><td>$780</td><td>$810</td></tr><tr><td>Hard Drive</td><td>500 GB</td><td>250 GB</td><td>250 GB</td><td>500 GB</td><td>500 GB</td></tr><tr><td>Video Card</td><td>256 MB</td><td>256 MB</td><td>256 MB</td><td>512 MB</td><td>1280 MB</td></tr><tr><td>Processor</td><td>1.6 GHz</td><td>1.6 GHz</td><td>1.6 GHz</td><td>2.13 GHz</td><td>3 GHz</td></tr><tr><td>Memory</td><td>4 GB</td><td>2 GB</td><td>2 GB</td><td>4 GB</td><td>4.5 GB</td></tr><tr><td>Screen Size</td><td>13.3 Inches</td><td>12.1 Inches</td><td>15.6 Inches</td><td>16 Inches</td><td>17 Inches</td></tr><tr><td>Weight</td><td>4.4 lbs</td><td>3 lbs</td><td>3 lbs</td><td>6 lbs</td><td>8.4 lbs</td></tr><tr><td>Battery</td><td>3 Hours</td><td>3 Hours</td><td>2.5 Hours</td><td>2.5 Hours</td><td>3 Hours</td></tr><tr><td>Select</td><td>Add to Cart</td><td>Add to Cart</td><td>Add to Cart</td><td>Add to Cart</td><td>Add to Cart</td></tr></table>

Figure 4. Product Recommendation  
Table 1. Low Level of Trade-Off Transparency

<table><tr><td>Attributes</td><td>Price</td><td>Hard Drive</td><td>Video Card</td><td>Memory</td><td>Processor</td><td>Screen Size</td><td>Weight</td><td>Battery</td></tr><tr><td>Price</td><td></td><td>Related</td><td>Related</td><td>Related</td><td>Related</td><td>Related</td><td>Related</td><td>Related</td></tr><tr><td>Hard Drive</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Video Card</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Memory</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Processor</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Screen size</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Weight</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Battery</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

relationships revealed by the RA. Specifically, the trade-off transparent RA revealed 7, 15, and 23<sup>5</sup> unidirectional tradeoff relationships in low, medium, and high trade-off transparency treatments, respectively. In the case of a low level of trade-off transparency (Table 1), the RA revealed the seven trade-off relationships<sup>6</sup> between the seven non-price attributes and the price attribute. This manipulation is based on the notion that the most common form of a trade-off in most marketplace settings is that between price and product quality (Hedgcock and Rao 2009). Specifically, whenever a user indicates her product preferences on each of the seven nonprice attributes, the price will automatically adjust to reflect their underlying correlations,<sup>7</sup> while the values of the rest of the non-price attributes remain constant. Note that the change in price does not lead to a change in other product attributes because of the very large number of possible combinations of non-price attributes.

Table 2. Medium Level of Trade-Off Transparency (Newly added trade-offs are bold)

<table><tr><td>Attributes</td><td>Price</td><td>Hard Drive</td><td>Video Card</td><td>Memory</td><td>Processor</td><td>Screen Size</td><td>Weight</td><td>Battery</td></tr><tr><td>Price</td><td></td><td>Related</td><td>Related</td><td>Related</td><td>Related</td><td>Related</td><td>Related</td><td>Related</td></tr><tr><td>Hard Drive</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Video Card</td><td></td><td></td><td></td><td>Related</td><td></td><td></td><td></td><td></td></tr><tr><td>Memory</td><td></td><td></td><td>Related</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Processor</td><td></td><td>Related</td><td></td><td></td><td></td><td></td><td></td><td>Related</td></tr><tr><td>Screen size</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Related</td><td></td></tr><tr><td>Weight</td><td></td><td></td><td></td><td></td><td></td><td>Related</td><td></td><td>Related</td></tr><tr><td>Battery</td><td></td><td></td><td></td><td></td><td>Related</td><td></td><td></td><td></td></tr></table>

Table 3. High Level of Trade-Off Transparency (Newly added trade-offs are italicized)

<table><tr><td>Attributes</td><td>Price</td><td>Hard Drive</td><td>Video Card</td><td>Memory</td><td>Processor</td><td>Screen Size</td><td>Weight</td><td>Battery</td></tr><tr><td>Price</td><td></td><td>Related</td><td>Related</td><td>Related</td><td>Related</td><td>Related</td><td>Related</td><td>Related</td></tr><tr><td>Hard Drive</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Video Card</td><td></td><td></td><td></td><td>Related</td><td></td><td>Related</td><td></td><td></td></tr><tr><td>Memory</td><td></td><td></td><td>Related</td><td></td><td>Related</td><td></td><td></td><td></td></tr><tr><td>Processor</td><td></td><td>Related</td><td></td><td>Related</td><td></td><td>Related</td><td>Related</td><td>Related</td></tr><tr><td>Screen size</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Related</td><td></td></tr><tr><td>Weight</td><td></td><td>Related</td><td></td><td></td><td>Related</td><td>Related</td><td></td><td>Related</td></tr><tr><td>Battery</td><td></td><td></td><td></td><td></td><td>Related</td><td>Related</td><td></td><td></td></tr></table>

RAs with a medium level of trade-off transparency (Table 2) revealed eight additional trade-off relationships in addition to those specified in the low trade-off transparency condition. One example, as noted earlier, is the correlation between screen size and weight of a laptop computer. Similar to the interpretation used with Table 1, Table 2 should be interpreted by looking at each column, heading first, and then the intersected rows. For example, when the value of the hard drive attribute (column heading) changes, the values of two other related attributes (price and processor) in the corresponding intersected rows change accordingly.

The RA with a high level of trade-off transparency (Table 3) revealed an additional eight trade-off relationships, as well as those specified in the medium trade-off transparency condition. One example is the relationship between the battery and the weight of a laptop computer. Similar to the other tables, Table 3 should be interpreted by looking at each column heading first and then the correspondent intersected rows. For example, when the value of the hard drive attribute (column heading) changes, the values of three other related attributes (price, processor, and weight) in the intersected rows change accordingly.

In the control condition, when a user indicates a certain value for a product attribute, the values of other attributes maintain constancy. However, subjects were told on a written form that, “When you indicate your preferences, please bear in mind that the better the computer component (e.g., faster processor or larger hard disk), the more expensive it is; and, the larger the screen size, the heavier it is. Hence, be careful not to overestimate your needs.”

## Manipulation of Shopping Task

The subjects’ task was to choose a laptop computer for their friend or for themselves, depending on the group to which they were assigned. We included two shopping tasks (one for themselves and one for a friend) for several reasons. On one hand, the inclusion of the friend’s task was to ensure that participants considered a full range of product attributes as described below. In addition, previous research (Bettman et al. 1998) suggested that shopping for friends helps minimize the effects of negative emotions when making attribute tradeoffs, which likely plays a confounding role if participants are asked to shop for themselves.

On the other hand, the self-shopping task enables us to compare the subject’s initial indication of product preference with the subject’s final attribute preferences input to the RA. If greater deviation exists for the trade-off transparent RA condition than the control condition, this supports the statement that a trade-off transparent RA is effective in informing users about the trade-offs existing among product attribute values. As users gain a better understanding of product attribute values, they are more able to update their initial attribute value preferences, indicated at the very beginning of the experiment. In short, the self-shopping condition is expected to provide more objective evidence to support the effectiveness of trade-off transparent RAs in increasing users’ product diagnosticity, as we will discuss in the section “Supplementary Analysis on Preference Updates.”

Each subject assigned to the condition of shopping for a friend was provided with his/her friend’s product requirements in a written form, as follows:

Martin likes to download and collect tons of classical videos onto his laptop computer. Martin often uses his computer to watch movies as well. He often uses the computer to run complicated statistical software, some of which may run for hours before producing the final output. Martin’s eyesight is less than perfect, so he desires a large monitor screen. Martin travels a lot, and he plans to use his new computer when traveling. A lighter machine with sufficient battery will definitely make it easier for him. Martin prefers NOT to spend too much money on his new laptop computer.

Those assigned to the condition of shopping for themselves were told to shop for a laptop of their own. In addition, they were asked to indicate their product preferences at the very beginning of the experiment. Instruction was as follows:

Suppose you need to buy yourself a new laptop computer in the near future. Please indicate how important each of the following computer attributes are to you, and what range of computer specifications you are planning for each attribute?

Users then indicated the value range (e.g., \$700–800) for each of the eight attributes (e.g., price).

## Subjects, Incentive, and Procedures

A power analysis for a between-subject design determined that 160 subjects (20 subjects for each group) would assure a sufficient statistical power of 0.80 to detect a medium effect size (f = .25) (Cohen 1988).

Incentives consisting of a minimum \$10 honorarium and an additional \$25 for the 20 best performers were provided to the participants. The criteria used in deciding the “best performers” were how logical and convincing their answers were to the questions asked. The participants were told, “There are no right or wrong answers here; we are just interested in getting an honest and detailed description of your perception.” Previous research (e.g., Mao and Benbasat 2000; Xu et al. 2012) indicated that such instruction is important, as it serves to motivate subjects to view the experiment as a serious online experience session and increase their involvement.

Subjects were first required to fill in a questionnaire to record their demographic and control variables. Before subjects were randomly assigned to the experimental groups (control, low, medium, or high level of trade-off transparency), they were trained to use the website to which they were assigned. In the experimental websites, they could indicate the product attribute preferences to the RA by dragging the slider on each attribute bar (Figure 2). After subjects submitted their attribute preferences to the RA, the RA accordingly recommended a list of computers that fit their needs. After that, they answered questions related to the dependent variables, such as perceived enjoyment and perceived decision quality.

## Measurements of Dependent and Control Variables

For the survey instrument, we adopted established scales for enjoyment, product diagnosticity, perceived decision quality, perceived decision effort, and intention to use an RA from prior literature. All of the items of the survey and their sources are shown in Table 4.

<table><tr><td>Construct Names</td><td>Measurement Items (7-point scale)</td><td>Sources</td></tr><tr><td>Perceived Enjoyment</td><td>Using the recommendation agent to select a laptop wasUnexciting......ExcitingDull......NeatNot Fun......FunUnappealing......AppealingBoring......Interesting</td><td>Griffith et al. (2001)Koufaris (2002)</td></tr><tr><td>Perceived Product Diagnosticity</td><td>This recommendation agent was helpful for me to evaluate the laptop.This recommendation agent was helpful for me to understand the performance of the laptop.This recommendation agent was helpful in familiarizing me with the laptop.</td><td>Jiang and Benbasat (2007a, 2007b)</td></tr><tr><td>Perceived Decision Quality</td><td>Laptops that suited my preferences were suggested by the recommendation agent.Laptops that best matched my needs were provided by the recommendation agent.I would choose from the same set of alternatives provided by the recommendation agent on my future purchase occasion.</td><td>Widing and Talarzyk (1993)</td></tr><tr><td>Perceived Decision Effort</td><td>The laptop selection task that I went through was too complex.The task of selecting the laptop computer using the agent was too complex.Selecting the laptop computer using the agent required too much effort.The task of selecting the laptop computer using the agent took too much time.</td><td>Pereira (2000); Wang and Benbasat (2009)</td></tr><tr><td>Intention to Use an RA</td><td>Assuming I have access to the recommendation agent, I intend to use it next time I consider buying a laptop computer.Assuming I have access to the agent, I predict I would use it next time I plan to purchase a laptop computer.Assuming I have access to the agent, I plan to use it next time I consider buying a laptop computer.</td><td>Venkatesh et al. (2003); Wang and Benbasat (2009)</td></tr></table>

## Data Analysis

## Sample

The sample used for this study consists of 160 subjects recruited in a public university, with 116 females and 44 males. The group included 13 nonstudents, 16 graduate students, and 131 undergraduates. The average age was 22.7. There was no significant difference in gender (Pearson chisquare value = 0.25, p = 0.96) or age (F = 1.55, p = 0.20) distribution across the treatment conditions.

On average, the subjects had been using the Internet for 10.5 years, and spent 31.3 hours on the Internet each week. In general, they were familiar with online shopping (5.21 on a seven-point scale). The average reported knowledge level of the product used in the task—laptop computers—was 4.9 on a seven-point scale. No significant differences were found across the treatment conditions regarding these four factors. These results indicate that the random assignment of subjects to the different experimental conditions was successful.

## Manipulation Checks

As a manipulation check, both the objective numbers of tradeoffs demonstrated to users and users’ awareness of trade-offs were measured. We measured the objective total number of trade-offs demonstrated to each user by taking the sum of the product of the number of each slider movement initiated by a user and the number of related attributes automatically adjusted. Therefore, this measure takes into account the fact that users might not click and drag all eight attribute sliders in each assigned condition.

<table><tr><td>Groups/Constructs</td><td>Total Numbers of Attribute Trade-Offs Demonstrated</td><td>Average Number of Attribute Trade-Offs Demonstrated per Slider Movement</td><td>Users’ Awareness of Trade-off (Seven-Point Scale, One-Tailed Test)</td></tr><tr><td>Control</td><td>0</td><td>0</td><td> $4.61^a$ </td></tr><tr><td>Low TOT</td><td> $10.32^b$ </td><td> $0.93^b$ </td><td> $4.91^b$ </td></tr><tr><td>Medium TOT</td><td> $28.97^c$ </td><td> $2.02^c$ </td><td> $5.22^c$ </td></tr><tr><td>High TOT</td><td> $45.14^d$ </td><td> $3.28^d$ </td><td> $5.52^d$ </td></tr><tr><td>Average</td><td>20.75</td><td>1.53</td><td>5.06</td></tr></table>

Notes: TOT refers to trade-off transparency; different superscripts in the same column indicate that the difference between means is significant (p < 0.05).

We also calculated the average number of trade-offs demonstrated for each slider movement, derived by dividing the total number of attribute trade-offs displayed to the user by the total slider movements initiated by a user. This breakdown offers insights to RA designers regarding how trade-off transparency should be designed to achieve desirable outcomes (see “Practical Contributions” for details). The comparisons among the four trade-off transparency treatments in terms of the objective number of trade-offs demonstrated and users’ awareness of attribute trade-offs<sup>8</sup> are reported in Table 5. For each measure, each pair of comparisons between different treatments was significant (p < 0.05), showing that the manipulation of trade-off transparency was successful.

## Effect of Trade-Off Transparency Levels

We conducted a MANOVA to test the effects of the four levels of trade-off transparency on perceived enjoyment and perceived product diagnosticity. MANOVA test statistics included Pillari’s trace, Wilks’ lambda, Hotelling’s trace, and Roy’s largest root. The p-values of these statistics were found to be significant (p < 0.05). Therefore, further ANOVAs were conducted separately on the two dependent variables.

A 4 × 2 ANOVA on product diagnosticity indicates that tradeoff transparency significantly affects perceived enjoyment (Table 6), while shopping task and the interaction effect were not significant. Similar results were obtained for product diagnosticity (Table 7). Contrast results detailed the difference among various levels of trade-off transparency for product diagnosticity and enjoyment (Table 8).

Table 8 indicates that medium and high levels of trade-off transparency were observed to have significantly higher perceived enjoyment than the control group; thus, H1 is partially supported. All three levels of trade-off transparency were observed to have significantly higher perceived product diagnosticity than the control group, fully supporting H2.

To test whether enjoyment with the trade-off transparent RA follows an inverted U-shaped curve as the level of trade-off transparency increases, we conducted three planned contrast tests (Nordhielm 2002; Schindler et al. 2011; Suri and Monroe 2003; Uhrich 2011), the first between the control group and the low level of trade-off transparency, the second between low and medium levels of trade-off transparency, and the third between medium and high levels of trade-off transparency. The differences (Table 8) between these three pairs of trade-off transparency were -0.255 (p > 0.05), -1.08 (p < 0.001), and 0.471 (p = 0.047). Figure 5 shows that the relationship between enjoyment and three levels of trade-off transparency resembles an inverted U-shaped curve. Similarly, for product diagnosticity (Figure 6, Table 8), the three contrast differences between the control group and low level, between low and medium level, and between medium and high level were -0.525 (p = 0.01), -0.40 (p = 0.037), and 0.483 (p = 0.012), respectively, which indicated a trend also following the inverted U-shaped curve. Thus, H3 and H4 were supported.

## Test of the Research Model

We analyzed the structural model using partial least squares (PLS) structural equation modeling, a component-based approach (Lohmöller 1989). PLS allows for simultaneous

Table 6. ANOVA Summary Table for Perceived Enjoyment

<table><tr><td>Independent Variable</td><td>Sum of Squares</td><td>df</td><td>Mean Square</td><td>F</td><td>Sig.</td></tr><tr><td>Trade-off transparency</td><td>42.838</td><td>3</td><td>14.279</td><td>12.787</td><td>0.000</td></tr><tr><td>Shopping task (shopping for a friend vs. yourself)</td><td>0.229</td><td>1</td><td>0.229</td><td>0.205</td><td>0.651</td></tr><tr><td>Trade-off transparency × shopping task</td><td>2.167</td><td>3</td><td>0.722</td><td>0.647</td><td>0.586</td></tr></table>

Table 7. ANOVA Summary Table for Perceived Product Diagnosticity

<table><tr><td>Independent Variable</td><td>Sum of Squares</td><td>df</td><td>Mean Square</td><td>F</td><td>Sig.</td></tr><tr><td>Trade-off transparency</td><td>21.567</td><td>3</td><td>7.189</td><td>11.037</td><td>0.000</td></tr><tr><td>Shopping task (shopping for friend vs. yourself)</td><td>1.360</td><td>1</td><td>1.36</td><td>2.088</td><td>0.151</td></tr><tr><td>Trade-off transparency × shopping task</td><td>1.113</td><td>3</td><td>0.371</td><td>0.570</td><td>0.636</td></tr></table>

Table 8. MANOVA Contrast Results

<table><tr><td colspan="2">Contrast</td><td>Perceived Enjoyment</td><td>Perceived Product Diagnosticity</td></tr><tr><td rowspan="2">Low TOT vs. control</td><td>Contrast Estimate</td><td>0.255</td><td>0.525</td></tr><tr><td>Significance</td><td>0.279</td><td>0.01</td></tr><tr><td rowspan="2">Medium TOT vs. control</td><td>Contrast Estimate</td><td>1.338</td><td>0.925</td></tr><tr><td>Significance</td><td>0.000</td><td>0.000</td></tr><tr><td rowspan="2">High TOT vs. control</td><td>Contrast Estimate</td><td>0.867</td><td>0.442</td></tr><tr><td>Significance</td><td>0.000</td><td>0.021</td></tr><tr><td rowspan="2">Medium vs. low TOT</td><td>Contrast Estimate</td><td>1.08</td><td>0.400</td></tr><tr><td>Significance</td><td>0.000</td><td>0.037</td></tr><tr><td rowspan="2">High vs. low TOT</td><td>Contrast Estimate</td><td>0.612</td><td>-0.083</td></tr><tr><td>Significance</td><td>0.010</td><td>0.661</td></tr><tr><td rowspan="2">High vs. medium TOT</td><td>Contrast Estimate</td><td>-0.471</td><td>-0.483</td></tr><tr><td>Significance</td><td>0.047</td><td>0.012</td></tr></table>

TOT: Trade-off transparency

Table 9. Descriptive Statistics with Means and Standard Deviations (SD)

<table><tr><td>Groups</td><td colspan="2">Enjoyment</td><td colspan="2">Product Diagnosticity</td><td colspan="2">Decision Quality</td><td colspan="2">Decision Effort</td><td colspan="2">Intention</td></tr><tr><td></td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>Control</td><td>3.89</td><td>1.3</td><td>4.44</td><td>0.76</td><td>4.37</td><td>1</td><td>3.25</td><td>1.3</td><td>3.50</td><td>1.46</td></tr><tr><td>Low</td><td>4.15</td><td>1.2</td><td>4.97</td><td>1.05</td><td>4.73</td><td>0.9</td><td>3.25</td><td>1.4</td><td>4.24</td><td>1.74</td></tr><tr><td>Medium</td><td>5.23</td><td>0.9</td><td>5.37</td><td>0.8</td><td>5.42</td><td>0.7</td><td>2.57</td><td>1.2</td><td>5.35</td><td>0.85</td></tr><tr><td>High</td><td>4.76</td><td>0.6</td><td>4.88</td><td>0.73</td><td>4.95</td><td>0.7</td><td>3.19</td><td>1.4</td><td>4.81</td><td>1.04</td></tr><tr><td>Average</td><td>4.5</td><td>1.2</td><td>4.91</td><td>0.9</td><td>4.87</td><td>0.9</td><td>3.07</td><td>1.4</td><td>4.47</td><td>1.47</td></tr></table>

Note: All measures were based on seven-point Likert scales ranging from “strongly disagree” (1) to “strongly agree”(7).

![](/api/attachments/JUHBVZEC/fulltext/images/4161b94b8752b7cc801f55f611afc10af43fd074957c10c4c3118f1949d9f848.jpg)  
Figure 5. Effect of Trade-Off Transparency on Perceived Enjoyment

![](/api/attachments/JUHBVZEC/fulltext/images/1ced68c83fd5ee9b7ffd5ca1459f3db97ac819732b24c276650e1e6b31e2fc19.jpg)  
Figure 6. Effect of Trade-Off Transparency on Perceived Product Diagnosticity

testing of the measurement model (the psychometric properties of the scales used to measure a variable) and the estimation of the structural model (the strength and direction of the relationship between the variables). PLS has an added advantage over covariance-based methods (e.g., LISREL) in that (1) it maximizes the explained variance of endogenous variables in the structural model (Chin 1998; Gefen et al. 2000; Klein and Arun 2009), which enables us to understand the amount of variance explained in the constructs, such as perceived decision quality, and (2) PLS does not make distributional assumptions for the data (Ahuja and Thatcher 2005; Chin 1998; Chin et al. 2003; Gefen et al. 2000; Venkatesh and Agarwal 2006). We used the software SMART PLS 2.0 (Ringle et al. 2005) to conduct the analyses. Table 9 depicts the means and standard deviations for the five constructs presented in the model.

## Measurement Model

Assessments of measurement models should examine (1) individual measurement item reliability, (2) internal consistency, and (3) discriminant validity (Barclay et al. 1995). To support individual item reliability, we examined the loadings of the individual measurement items on their intended constructs and compared these with a recommended tolerance of 0.70 (Barclay et al. 1995; Chin 1998). All of the measurement items met this threshold (Table 10). To show internal consistency of the constructs, we calculated composite reliability and Cronbach’s alpha for each construct. All met the recommended tolerances (> 0.70; Fornell and Larcker 1981) (Table 11).

The diagonal elements in Table 11 represent the square roots of the average variance extracted (AVE) of latent variables, while the off-diagonal elements are the correlations between latent variables. For adequate discriminant validity, the square root of the AVE of any latent variable should be greater than the correlation between this particular latent variable and other latent variables (Barclay et al. 1995). All construct pairs met this requirement. Moreover, as shown in Table 10, the loadings of a given construct’s indicators are higher than the loadings of any other, and these same indicators load more highly on their intended construct than on any other construct. This lends further support to discriminant validity.

To address the potential concern for common method bias, we performed three tests. First, we applied the Harman (1967) one-factor extraction test. This test determines whether a single method factor explains most of the variance among the instrument variables (Podsakoff and Organ 1986). If one contributes more than 50 percent of total variance, common method bias might exist (Indushobha et al. 2010; Nov and Ye 2008). Using a principal component analysis for all of the items of the five variables (Figure 7) measured in the study, we found five factors with eigenvalues greater than 1, accounting for the 80.02 percent of the total variance. As the first factor accounted for only 43.82 percent of the total variance, less than 50 percent of the total variance, it indicates a lack of a substantial common methods bias.

Second, we tested for multicollinearity among the five variables. To formally test for the presence of collinearity, we calculated the variable inflation factor (VIF) for the five constructs in the model. The results indicated that all of the VIFs were lower than 2, with the highest VIF being 1.83. Tabachnik and Fidell (1996) and Thatcher and Perrewé (2002) suggest that when VIFs exceed 10, collinearity biases the result. Because the VIFs did not exceed 2, our analysis indicated that collinearity did not influence the results.

Finally, we followed the marker-variable technique suggested by Lindell and Whitney (2001), Malhotra et al. (2006), and Pavlou et al. (2007). They proposed that a theoretically unrelated construct (termed a marker variable) should be used to adjust the correlations among the principal constructs. In our case, regulation focus (i.e., promotion or prevention focus, Higgins 1998), a theoretically unrelated construct, was identified. High correlations among any of the items of the study’s principal constructs and regulation focus indicate common method bias, as the construct of regulation focus should be weakly related to our study’s five principal constructs. Since the average correlation among the regulation focus and the five principal constructs was r = .05 (average pvalue = 0.39), minimal evidence existed of common method bias. Thus, these three tests suggested that common method bias is not a major concern in this study.

## Structural Model

We next analyzed the structural model to examine the significance and strength of relationships hypothesized. The results shown in Figure 7 indicate that enjoyment positively influenced perceived decision quality (β = 0.41; p < 0.001) and negatively influenced perceived decision effort (β = -0.29; p < 0.001), which supports H5 and H6. Product diagnosticity positively influenced perceived decision quality (β = 0.37; p < 0.001), supporting H7,but did not influence perceived decision effort (β = -0.09; p > 0.05), thus H8 was not supported. Finally, perceived decision quality positively influenced intention to use an RA (β = 0.47; p < 0.001) and perceived decision effort negatively influenced intention (β = -0.19; p < 0.01), supporting H9 and H10. Perceived decision quality and perceived decision effort jointly explained 31 percent of the variance in intention to use an RA, with perceived decision quality contributing a larger proportion to that explanation.

We also examined whether the effects of perceived enjoyment and product diagnosticity on intention were fully or partially mediated through perceived decision quality and/or perceived decision effort. To test for mediation, we utilized the fourstep procedure proposed by Baron and Kenny (1986).<sup>9</sup> As a first step, Figure 7 demonstrates the effect of enjoyment and product diagnosticity (independent variables) on decision quality and decision effort (potential mediators). We then tested the direct effect of enjoyment and product diagnosticity (independent variables) on intention (dependent variables). The paths from enjoyment $( \beta = 0 . 6 2 , \rho < 0 . 0 0 1 )$ and product diagnosticity $( \beta = 0 . 1 6 , \rho < 0 . 0 5 )$ to intention were both significant. Next, when decision quality and decision effort (potential mediators) were added to the equation together with enjoyment and product diagnosticity to predict intention, the effect of product diagnosticity on intention was no longer significant with a coefficient of 0.10 (p > 0.05), while the effect of enjoyment on intention remained significant, although with a lower coefficient of 0.48. Thus, decision quality fully mediated the relationship between product diagnosticity and intention, while decision quality and decision effort only partially mediated the relationship between enjoyment and intention.

Table 10. Loading and Cross Loading of Measures

<table><tr><td></td><td>TOT</td><td>ENJ</td><td>PD</td><td>DQ</td><td>DE</td><td>INT</td></tr><tr><td>Enjoyment (ENJ1)</td><td>0.266</td><td>0.885</td><td>0.373</td><td>0.46</td><td>-0.215</td><td>0.638</td></tr><tr><td>Enjoyment (ENJ 2)</td><td>0.283</td><td>0.931</td><td>0.366</td><td>0.53</td><td>-0.303</td><td>0.601</td></tr><tr><td>Enjoyment (ENJ 3)</td><td>0.347</td><td>0.919</td><td>0.407</td><td>0.558</td><td>-0.300</td><td>0.657</td></tr><tr><td>Enjoyment (ENJ 4)</td><td>0.218</td><td>0.871</td><td>0.459</td><td>0.543</td><td>-0.296</td><td>0.571</td></tr><tr><td>Enjoyment (ENJ 5)</td><td>0.269</td><td>0.916</td><td>0.444</td><td>0.529</td><td>-0.269</td><td>0.637</td></tr><tr><td>Product Diagnosticity (PD1)</td><td>0.308</td><td>0.434</td><td>0.835</td><td>0.537</td><td>-0.175</td><td>0.449</td></tr><tr><td>Product Diagnosticity (PD2)</td><td>0.33</td><td>0.366</td><td>0.871</td><td>0.464</td><td>-0.125</td><td>0.363</td></tr><tr><td>Product Diagnosticity (PD3)</td><td>0.24</td><td>0.341</td><td>0.839</td><td>0.404</td><td>-0.160</td><td>0.281</td></tr><tr><td>Decision Quality (DQ1)</td><td>0.311</td><td>0.484</td><td>0.519</td><td>0.863</td><td>-0.279</td><td>0.383</td></tr><tr><td>Decision Quality (DQ2)</td><td>0.282</td><td>0.494</td><td>0.51</td><td>0.88</td><td>-0.258</td><td>0.399</td></tr><tr><td>Decision Quality (DQ3)</td><td>0.242</td><td>0.495</td><td>0.467</td><td>0.893</td><td>-0.311</td><td>0.449</td></tr><tr><td>Decision Quality (DQ4)</td><td>0.228</td><td>0.503</td><td>0.409</td><td>0.77</td><td>-0.189</td><td>0.557</td></tr><tr><td>Decision Effort (DE1)</td><td>-0.061</td><td>-0.271</td><td>-0.167</td><td>-0.307</td><td>0.931</td><td>-0.313</td></tr><tr><td>Decision Effort (DE2)</td><td>-0.049</td><td>-0.281</td><td>-0.167</td><td>-0.345</td><td>0.928</td><td>-0.304</td></tr><tr><td>Decision Effort (DE3)</td><td>-0.112</td><td>-0.327</td><td>-0.268</td><td>-0.384</td><td>0.919</td><td>-0.326</td></tr><tr><td>Decision Effort (DE4)</td><td>-0.128</td><td>-0.233</td><td>-0.127</td><td>-0.094</td><td>0.678</td><td>-0.229</td></tr><tr><td>Intention to Use (INT1)</td><td>0.347</td><td>0.657</td><td>0.432</td><td>0.515</td><td>-0.330</td><td>0.975</td></tr><tr><td>Intention to Use (INT2)</td><td>0.382</td><td>0.669</td><td>0.411</td><td>0.511</td><td>-0.328</td><td>0.981</td></tr><tr><td>Intention to Use (INT3)</td><td>0.394</td><td>0.686</td><td>0.441</td><td>0.524</td><td>-0.318</td><td>0.979</td></tr></table>

Table 11. Internal Consistency and Discriminant Validity of Constructs

<table><tr><td></td><td>CR</td><td>CA</td><td>ENJ</td><td>PD</td><td>DQ</td><td>DE</td><td>INT</td></tr><tr><td>Enjoyment (ENJ)</td><td>0.96</td><td>0.94</td><td>0.91</td><td></td><td></td><td></td><td></td></tr><tr><td>Product Diagnosticity (PD)</td><td>0.89</td><td>0.81</td><td>0.45</td><td>0.85</td><td></td><td></td><td></td></tr><tr><td>Decision Quality (DQ)</td><td>0.91</td><td>0.87</td><td>0.58</td><td>0.56</td><td>0.85</td><td></td><td></td></tr><tr><td>Decision Effort (DE)</td><td>0.92</td><td>0.87</td><td>-0.32</td><td>-0.21</td><td>-0.34</td><td>0.86</td><td></td></tr><tr><td>Intention to Use an RA (INT)</td><td>0.98</td><td>0.97</td><td>0.68</td><td>0.44</td><td>0.52</td><td>-0.34</td><td>0.98</td></tr></table>

Note: Composite reliability = CR; Cronbach’s alpha = CA; diagonal elements are the square root of AVE.

![](/api/attachments/JUHBVZEC/fulltext/images/a53cdc939b626a13e4b465acd8608b3363dfe28b895b0a2314a2c961e34e4046.jpg)  
Figure 7. Results of Research Model

## Supplementary Analysis on the Effect of Product Diagnosticity on Decision Effort

The nonsignificant result for the effect of product diagnosticity on perceived decision effort was not expected. We hypothesized that a better understanding of product attribute value trade-offs led to matching products recommended in the first place, which should save users’ effort. However, this hypothesis was not supported. One possibility is that while users saved effort in evaluating product recommendations given better matching products recommended by the RA, they also spent greater effort understanding the trade-off relationships among product attribute values. Prior research indicated that the more decision aid features used, the longer the decision time (Hess et al. 2005); thus, that users would spend more time indicating their preference with the trade-off transparency feature is reasonable to expect.

To further investigate this possibility, we compared the time spent to indicate product preferences and the time used to evaluate product recommendations between the trade-off transparent RAs and the control group (see Figure 8). The results indicated that, compared with the control group, subjects using the medium and high levels of the trade-off transparency feature spent significantly more time $( \mathtt { p } < 0 . 0 5 )$ indicating their product preferences, but subjects using any one of the three levels of the trade-off transparency feature spent significantly less time $( \mathtt { p } < 0 . 0 5 )$ evaluating product recommendations. When these two sets of times in preference indication and product evaluation were added up, no difference in total time was found between using trade-off transparent RA and traditional RA. The bottom line is that while perceived decision effort is not affected either positively or negatively by product diagnosticity, perceived decision quality improved because of higher product diagnosticity.

## Supplementary Analysis on Preference Updates

Recall that half the subjects (N = 80) were asked to shop for a product for themselves and the other half for a fictitious friend. The group of participants who shopped for themselves provided objective data for us to understand whether users’ perceived product diagnosticity is indeed affected by the use of a trade-off transparent RA. Our reasoning is that if consumers better understand the product attribute value trade-offs through the trade-off transparency feature, they are more likely to update their product preferences indicated to the RA compared with their product preferences indicated before the experiment.

To measure the influence of the trade-off transparent RA on users’ preference updates, we identified the deviation of users’ initial indication of product preference at the beginning of the experiment (see “Manipulation of Shopping Task”) from users’ final attribute preference provided to the RA (Figure 2). For example, one instance of a deviation is if a user indicated that the initial preferred price was \$300–\$400 but then revised his or her desired price value higher than \$400. We only considered the deviations of those attributes considered “most important” and “important” by users. We counted the number of such instances of value deviations that occurred for each subject and generated a score for each subject. Then we compared the deviation score between the experimental groups using a trade-off transparent RA and the traditional RA. In short, a deviation score of 1 means that a subject modified his/her original preference range for one attribute considered “most important” or “important.”

The average score for the three trade-off transparent RAs was $0 . 8 9 ^ { 1 0 }$ and the score for the control group was 0.29. The difference was statistically significant $( \mathtt { p } < 0 . 0 0 1 )$ , meaning that the trade-off transparent RA was effective in informing users’ about the trade-offs among product attribute values to help users better understand the product attributes and change their initial preferences indicated at the very beginning of the experiment. The objective measurement of preference updates corroborated Hypothesis 2 regarding the effect of the trade-off transparent RA on perceived product diagnosticity. The correlation $( 0 . 3 4 , \mathsf { p } < 0 . 0 1 )$ between objective preference updates and perceived product diagnosticity supported this argument. Further, the correlation (0.23, p < 0.05) between objective preference updates and perceived decision quality substantiated the arguments for H7 (i.e., the effect of perceived product diagnosticity on perceived decision quality). This result is consistent with the findings from prior research that users with greater domain knowledge have higher perception of decision quality (Kamis and Stohr 2006).

![](/api/attachments/JUHBVZEC/fulltext/images/c8b88c13a939b425bb95b03d30f9400516acc4bdc077c60c9bee036c4d81be2d.jpg)  
Figure 8. Time in Preference Indication and Product Evaluation

## Supplementary Analysis on the Two Shopping Tasks

This study included two shopping tasks (one self-shopping task and one for a friend). The buying for a friend task with its prescribed set of product features (see “Manipulation of Shipping Task”) is necessary to ensure that participants considered a full range of product attributes. In addition, the self-shopping condition can provide more empirical evidence on the effect of trade-off transparency, as analyzed in the previous subsection.

As the inclusion of the two shopping tasks was done more for a methodological than theoretical reason, we do not explicitly hypothesize their differences. Here, we analyze whether any differences exist between these two tasks. We conducted a two (shopping tasks) by four (levels of trade-off transparency)

MANOVA on the three variables (e.g., users’ awareness of trade-off) presented in Table 5. No significant interaction effect was found between two shopping tasks and four levels of trade-off transparency on the three variables, indicating that task types did not moderate the effects of trade-off transparency.

In terms of the main effect of the shopping task, we found that subjects in the friend task condition experienced a significantly higher number of attribute value trade-offs demonstrated than in the condition of shopping for themselves (p < 0.05). This result is consistent with our expectation that subjects in the friend task considered a greater number of product attributes and accordingly initiated more slider movements than those in the self-shopping task. However, we found no significant differences between these two shopping tasks regarding the average number of attribute value trade-offs demonstrated per slider movement (p = 0.830) and a user’s awareness of trade-offs $( \mathtt { p } = 0 . 4 1 )$ . In fact, this result reflected our intended experimental manipulation of the levels (i.e., none, low, medium, and high) of trade-off transparency revealed (see Table 5). The data confirmed that our manipulation of the trade-off transparency levels was successful and held for the two shopping tasks. Taken together, the results indicate that what matters to users’ perceptions of trade-off transparency is the average number of attribute value trade-offs demonstrated per slider movement, not the total number of attribute value trade-offs demonstrated. Relevant practical implications are provided in the “Practical Contributions” subsection presented later.

## Discussion

The results support the theorization that the trade-off transparent RA is effective in improving perceived enjoyment and perceived product diagnosticity. Levels of trade-off transparency make a difference in improving users’ perceived enjoyment and product diagnosticity. While the medium level of trade-off transparency leads to a more optimal level of enjoyment and product diagnosticity, the higher level generates a counterproductive effect. Perceived enjoyment improves perceived decision quality and reduces perceived decision effort, and product diagnosticity positively influences perceived decision quality without compromising perceived decision effort. Perceived decision quality significantly increases intention to use an RA, and perceived decision effort significantly decreases this intention.

The effect of the trade-off transparency feature on product diagnosticity and perceived enjoyment is consistent with the S-O-R model, suggesting that environmental cues can affect organism change of cognition and affection. The trade-off transparent RA not only provides information on the product attribute values related to one another, but also sheds light on exactly how users’ attribute choices are related to, and are constrained by, one another. This can make users aware of the potential attribute value trade-offs they had not previously recognized, thus leading to better product diagnosticity. In addition, as more interactive cues (dynamic user interface vs. versus written text) were provided in the trade-off transparent RA versus the traditional RA, this RA triggered more sensory channels and, in general, was more emotionally attractive (Jiang and Benbasat 2007b; Nisbett and Ross 1980). In addition, given the exploratory nature of the experience during interaction with the trade-off transparent RA, users positive affect was aroused (Kettanurak et al. 2001), which led to high perceived enjoyment.

Multiple IS studies have underscored the importance of both cognitive and affective perceptions in the context of online shopping (Gefen et al. 2003; Koufaris 2002; Van der Heijden 2003, 2004). The evaluation criteria of the trade-off transparent RA included both cognitive (product diagnosticity) and affective (enjoyment) measures of the user experience with an

RA. In a trade-off situation, conventional wisdom seeks to minimize the extent of necessary trade-offs (Lee and Benbasat 2011; Luce et al. 2001). However, our results indicated that through proper interface design, attribute value trade-offs of a product can be appropriately communicated to consumers and lead to better cognitive and affective outcomes.

The prediction regarding the positive effect of product diagnosticity on perceived decision effort was not supported. However, we expect that product diagnosticity could reduce perceived decision effort in the real world for two reasons. First, based on prior literature, we provided 50 product alternatives in the experiment to avoid overwhelming consumers. In reality, the number of products would be much higher than 50 (e.g., Amazon.com provides over 4,000 laptop computer alternatives). Thus, the study is a very conservative test of the effects of RAs in terms of reducing perceived decision effort. As the number of product alternatives increases, the effects of higher product diagnosticity are expected to be more robust in reducing decision effort. Second, the supplementary analysis indicates that the time spent understanding attribute value trade-offs can be recouped in the product evaluation stage. We contend that the former time component is a one-shot investment and will be greatly reduced when the RA is used a second time or more. In other words, as users’ familiarity with the trade-off transparent RA increases over time, perceived decision effort will be greatly reduced in the long run.

## Contributions, Limitations, Future Research, and Conclusions

## Theoretical Contributions

The results of the study make important theoretical contributions. First, the RA interface used to elicit product preferences is critically important (Kamis et al. 2010), but how to design RA interfaces to enable users to provide better input has not been established. Most of the extant RA studies (e.g., Häubl and Trifts 2000; Hess et al. 2005; Kamis et al. 2008; Kamis et al. 2010; Komiak and Benbasat 2006; Tam and Ho 2005; Wang and Benbasat 2009) only elicited users’ product preference without informing them of the attribute trade-offs; in such cases, users might mis-specify their product preferences, provide unrealistic input of attribute preferences to the RA, and end up being presented with unmatched product choices. Consequently, users might have negative perceptions of the RA and stop using it (Wang and Benbasat 2007). We advance the RA literature by proposing the tradeoff transparent RA to address this issue. We contribute to this knowledge gap by applying S-O-R theory to explain the differences between the trade-off transparent RA and the traditional RA.

We assessed the impact of trade-off transparent RAs relative to the traditional RA in terms of enjoyment and product diagnosticity. Trade-off awareness is beneficial for accurate decision making (Delquie 2003) but may generate unfavorable feelings (Luce et al. 1999). We demonstrated that with the trade-off transparent RA, users not only have a better understanding of attribute value trade-offs but also experience positive emotions with the interface. As theorized, this is because of the additional content conveyed (i.e., relationship among product attribute values) and the interactive presentation. This study highlighted the feasibility of introducing trade-off awareness to users without jeopardizing their positive emotional experience, and underscored the importance of the user interface design for online RAs.

Grounded in the S-O-R model, we derived two constructs (perceived product diagnosticity and perceived enjoyment) as representations of the cognitive and affective dimensions, which serve as antecedents of users’ response (perceptions of decision quality and decision effort). The two constructs are important in that previous research primarily focused on how RA characteristics can directly affect perceived decision quality and decision effort (Xiao and Benbasat 2007); the underlying mechanism that explains why certain RA characteristics can lead to better decision quality and decision effort has been largely ignored. Recent decision support studies recognized the importance of examining both cognitive and affective variables when studying online RAs (Kamis et al. 2008). To the best of our knowledge, this is the first study to examine the role of enjoyment and product diagnosticity within the effort–accuracy framework of cognition. This study will help researchers better understand why high perceived decision quality and low perceived decision effort can be achieved by the use and adoption of RAs. This extended effort–accuracy framework can also serve as a framework to evaluate alternative RA interface designs.

We investigated the effects of different levels of trade-off transparency. Task complexity is an important factor that affects users’ evaluation of RAs (Xiao and Benbasat 2007). While recent RA studies investigated the effect of the number of product attributes (e.g., Jiang and Benbasat 2007a) and number of product alternatives (e.g., Kamis et al. 2008), limited attention has been paid to examining the effects of the trade-off relationships of a product. According to Wood’s (1988) classification of task complexity, the number of product attributes, and the number of product alternatives belong to component complexity, while relationships among product attributes are under the category of coordinative complexity. Thus, we also contribute to the broad literature of task complexity, as previous studies in this area predominately focused on component complexity, and little research has been done on coordinative complexity, another important dimension of task complexity.

This study contributes to this knowledge gap by analyzing how the different number of trade-off relationships revealed by an RA influences users’ evaluations. We showed that the effect of trade-off transparency levels on enjoyment and product diagnosticity is nonlinear. As we predicted, both variables followed an inverted U-shaped path as the trade-off transparency level increased. Showing such nonlinear effects on both variables is a significant contribution to the theoretical and practical understanding of the dynamics of how users interact with an RA. The inverted U-shaped relationship between the trade-off transparency level and enjoyment (product diagnosticity) is an indication that increasing the number of trade-off relationships demonstrated in a preferential choice task does not guarantee an increase in enjoyment and product diagnosticity. In fact, consumers may be overwhelmed if too many trade-off relationships are revealed, and their enjoyment and product diagnosticity can decrease. As research on the design of the RA interface increases, we hope that the results will highlight the need for researchers to consider more than simple linear effects.

The results of the effect of enjoyment and product diagnosticity on perceptions of decision quality and decision effort provide unique insights. Both enjoyment and product diagnosticity improve perceived decision quality without increasing perceived decision effort. In particular, a higher level of enjoyment has a negative impact on the perception of decision effort. Effort and accuracy are an inherent trade-off in the consumer’s decision-making process (Payne et al. 1993). Prior empirical research also showed that higher decision quality is typically associated with higher decision effort (Fasolo et al. 2005; Schafer et al. 2002). We demonstrate that proper interface design can simultaneously achieve both objectives of better perceived decision quality and lower perceived decision effort.

## Practical Contributions

While the preceding comments focus on theoretical developments, the results regarding the impact of trade-off transparency on user perceptions have practical implications for online companies, particularly those with mass customization capabilities and the desire to introduce user customization of products on their websites. On the one hand, a trade-off transparent RA enables consumers to better understand the product attribute value trade-offs and provides appropriate attribute input to the RA to enable the RA to provide better product recommendations, thus leading to better perceived decision quality. On the other hand, the interactive interface of a trade-off transparent RA can increase one’s enjoyment and enhance the shopping experience, which leads to better perceived decision quality. Meanwhile, users with higher enjoyment are more engaged in the enjoyable interface and easily forget the passage of time. Together, these motivate users to return to their websites to continue to utilize RAs in product choice. Thus, practitioners are advised to incorporate the trade-off transparency function into the RA design on their websites.

Our results indicate that employing the medium level of tradeoff transparency in practice leads to the best outcomes in terms of perceived enjoyment and product diagnosticity. Even a low level of trade-off transparency significantly improves product diagnosticity over the control group. In addition, a low level of the trade-off transparency feature only consumes a small amount of a user’s time for understanding the relationship between price and non-price attributes, but it significantly reduces the time in product evaluation (see “Supplementary Analysis on the Effect of Product Diagnosticity on Decision Effort”). Thus, practitioners who desire quick implementation of the trade-off transparency feature might start with a low level of trade-off transparency that is easier to implement, and then gradually upgrade to the medium level.

We found a curvilinear relationship between perceived enjoyment and the number of trade-off relationships revealed to the user. A similarly curvilinear relationship was found between product diagnosticity and the number of trade-off relationships revealed to the user. Both of these findings highlight the danger of overwhelming consumers with too much information. Under conditions of greater trade-off transparency, consumers may become less interested in the website interface and may risk making poor decisions. Thus, when designing an RA interface, practitioners should select the appropriate product trade-off relationships to demonstrate. Table 5 sheds lights on how to exactly classify low, medium, and high levels of trade-off transparency. For example, a medium level of trade-off transparency means that, on average, approximately two attribute trade-offs should be demonstrated per slider movement initiated by a user. We believe these numbers, representing each trade-off transparency level, can be generalized to other contexts with different products, given longstanding support for the human mind’s capability of juggling a certain degree of information in working memory (e.g., Miller 1956).

## Limitations and Future Research

Several limitations exist to this study that provide avenues for future research. First, the experiment’s participants were mostly university students, as a student shopping for a computer is a common occurrence and a natural fit for our research design. However, readers should exercise caution in generalizing the results of this study to other demographic groups. To generalize the study results, conducting additional studies with different subject demographics and in different settings is necessary.

The second limitation is that the study was conducted in a context in which the participants evaluated an RA in the early stage of their interaction with it. When users become more familiar with the RA, the model results may be different. For example, the perceived effort to understand attribute value trade-offs may be reduced when users become more accustomed to it. As such, the effects of product diagnosticity on perceived decision effort may become significant. In addition, the effect of perceived effort may accordingly exert stronger influences on user intention. Future research is required to further examine the relative importance of various factors on post-adoption perceptions and behavior toward online RAs.

Another limitation is that some of the findings on trade-off transparency are only applicable to customizable products with a sufficient number attributes with trade-offs. Products with fewer trade-offs involved may not benefit completely from the results of this study. However, the marketing literature has indicated that trade-offs between price and product quality are common in marketplace settings (Hedgcock and Rao 2009). Thus, at the least, the results regarding the low level of trade-off transparency and its downstream impact are still applicable to most products.

## Conclusions

This study addressed an important gap in research in terms of understanding the role of product diagnosticity and enjoyment in influencing users’ perceived decision quality and decision effort by proposing and testing an extended effort–accuracy framework. The inclusion of these two variables sheds light on how higher perceived decision quality can be achieved without trading off decision effort. This extended effort– accuracy framework can be adopted to evaluate alternative RA interface designs in the future. Additionally, we extended previous RA research by proposing the trade-off transparency feature, a novel design aspect not previously considered in RA or even human–computer interaction research. Such a design feature is important, as MIS research has paid scant attention to IT artifacts and their design and development (Benbasat and Barki 2007; Benbasat and Zmud 2003; Orlikowski and Iacono 2001). Based on the S-O-R model, we evaluated the advantages of the trade-off transparent RA relative to the traditional RA in terms of enjoyment and product diagnosticity. Providing the trade-off transparency function is more costly and complicated for designers. Thus, an important determination to make is whether the trade-off transparent RA that elicits user preferences will enable users to better enjoy and understand the product and, subsequently, culminate in better decision quality and lower effort perceptions. The results indicate that being aware of attribute value trade-offs and, meanwhile, maintaining a favorable degree of enjoyment is feasible. Finally, in contrast to past research that focused on component complexity, we examined the role of coordinative complexity (level of trade-off transparency) in influencing perceived enjoyment and product diagnosticity. The results not only contribute to the literature on task complexity and task-technology fit, but also inform RA developers as to the kind of RA that is more beneficial given a specific set of circumstances.

## Acknowledgments

The authors would like to thank the senior editor, Joe Valacich, the associate editor, John Wells, and the three anonymous reviewers for their valuable comments and suggestions that have substantially improved the quality of this paper. The authors thank the Social Sciences and Humanities Research Council of Canada (SSHRC) for its support. They would also like to thank Jan DeGross for her efforts in typesetting this paper.

## References

Agarwal, R., and Karahanna, E. 2000. “Time Flies When You’re Having Fun: Cognitive Absorption and Beliefs about Information Technology Usage,” MIS Quarterly (24:4), pp. 665-694.

Ahn, H. J. 2006. “Utilizing Popularity Characteristics for Product Recommendation,” International Journal of Electronic Commerce (11:2), pp. 59-80.

Ahuja, M. K., and Thatcher, J. B. 2005. “Moving Beyond Intentions and Toward the Theory of Trying: Effects of Work Environment and Gender on Post-Adoption Information Technology Use,” MIS Quarterly (29:3), pp. 427-459.

Andrews, J., and Shimp, T. 1990. “Effects of Involvement, Argument Strength, And Source Vividness on Central and Peripheral Processing of Advertising,” Psychology and Marketing (7:3), pp. 195-214.

Babin, B. J., Darden, W. R., and Griffin, M. 1994. “Work and/or Fun: Measuring Hedonic and Utilitarian Shopping Value,” Journal of Consumer Research (20:4), pp. 644-656.

Baddeley, A. 1992. “Working Memory: The Interface Between Memory and Cognition,” Journal of Cognitive Neuroscience (4:3), pp. 281-288.

Bagozzi, R. P. 1986. Principle of Marketing Management, Chicago: SRA.

Baker, J., Grewal, D., and Parasuraman, A. 1994. “The Influence of Store Environment on Quality Inferences and Store Image,” Journal of the Academy of Marketing Science (22:4), pp. 328-339.

Barclay, D., Higgins, C., and Thompson, R. 1995. “The Partial Least Squares (PLS) Approach to Causal Modeling: Personal Computer Adoption and Use as an Illustration,” Technology Studies (2), pp. 285-324.

Baron, R. M., and Kenny, D. A. 1986. “The Moderator–Mediator Variable Distinction in Social Psychological Research: Conceptual, Strategic, and Statistical Considerations,” Journal of Personality and Social Psychology (51), pp. 1173-1182.

Belk, R. 1975. “Situational Variables and Consumer Behavior,” Journal of Consumer Research (2:3), pp. 157-164.

Benbasat, I., and Barki, H. 2007. “Quo vadis TAM,” Journal of the Association Information Systems (8:4), pp. 211-218.

Benbasat, I., and Todd, P. 1992. “The Use of Information in Decision Making: An Experimental Investigation of the Impact of Computer-Based Decision Aids,” MIS Quarterly (16:3), pp. 373-393.

Benbasat, I., and Todd, P. 1996. “The Effects of Decision Support and Task Contingencies on Model Formulation: A Cognitive Perspective,” Decision Support Systems (17:4), pp. 241-252.

Benbasat, I., and Zmud, R. W. 2003. “The Identity Crisis Within the IS Discipline: Defining and Communicating the Discipline’s Core Properties,” MIS Quarterly (27:2), pp. 183-194.

Berman, B. 2002. “Should Your Firm Adopt a Mass Customization Strategy?,” Business Horizons (45:4), pp. 51-60.

Bettman, J. R., Luce, M. F., and Payne, J. W. 1998. “Constructive Customer Choice Processes,” Journal of Consumer Research (25:3), pp. 187-217.

Biocca, F., Owen, C., and Tang, A. 2007. “Attention, Issues in Spatial Information Systems: Directing Mobile Users’ Visual Attention Using Augmented Reality,” Journal of Management Information Systems (23:4), pp. 163-184.

Chin, W. W. 1998. “The Partial Least Squares Approach for Structural Equation Modeling,” in Modern Methods for Business Research, G. A. Marcoulides (ed.), Mahwah, NJ: Lawrence Erlbaum, pp. 295-336.

Chin, W. W., Marcolin, B., and Newsted, P. 2003. “A Partial Least Squares Latent Variable Modeling Approach for Measuring Interaction Effects: Results from a Monte Carlo Simulation Study and an Electronic-Mail Emotion/Adoption Study,” Information Systems Research (14:2), pp. 189-217.

Cohen, J. 1988. Statistical Power Analysis for the Behavioral Sciences, Hillsdale, NJ: Lawrence Erlbaum Associates.

Coyle, J. R., and Thorson, E. 2001. “The Effects of Progressive Levels of Interactivity and Vividness in Web Marketing Sites,” Journal of Advertising (30:3), pp. 65-77.

Csikszentmihalyi, M. 1977. Beyond Boredom and Anxiety, San Francisco: Jossey-Bass.

Cyr, D., Head, M., and Ivanov, A. 2009. “Perceived Interactivity Leading to E-Loyalty: Development of a Model for Cognitive– Affective User Responses,” International Journal of Human– Computer Studies,” (67:10), pp. 850-869.

Delquie, P. 2003. “Optimal Conflict in Preference Assessment,” Management Science (49:1), pp. 102-115.

Drolet A., and Luce, M. F. 2004. “The Rationalizing Effects of Cognitive Load on Emotion-Based Trade-Off Avoidance,” Journal of Consumer Research (31:1), pp. 63-77.

Eisingerich, A. B., and Bell, S. J. 2008. “Perceived Service Quality and Customer Trust: Does Enhancing Customers’ Service Knowledge Matter?,” Journal of Service Research (10:3), pp. 256-268.

Eroglu, S. A., Machleit K. A., and Davis L. M. 2001. “Atmospheric Qualities of Online Retailing: A Conceptual Model and Implications,” Journal of Business Research (54:5), pp. 177-184.

Eroglu, S. A., Machleit, K. A., and Davis L. M. 2003. “Empirical Testing of a Model of Online Store Atmospherics and Shopper Responses,” Psychology & Marketing (20: 2), pp. 139-150.

Fasolo, B., McClelland, G. H., and Lange, K. A. 2005. “The Effect of Site Design and Interattribute Correlations on Interactive Web-Based Decisions,” in Online Consumer Psychology: Understanding and Influencing Behavior in the Virtual World, C. P. Haughvedt, K. Machleit, and R. Yalch (eds.), Mahwah, NJ: Lawrence Erlbaum Associates, pp. 325-344.

Fiore, A. M., and Kim, J. 2007. “An Integrative Framework Capturing Experiential and Utilitarian Shopping Experience,” International Journal of Retail & Distribution Management (35:6), pp. 421-442.

Fornell, C., and Larcker, D. F. 1981. “Evaluating Structural Equation Models with Unobservable Variables and Measurement Error,” Journal of Marketing Research (18), pp. 39-50.

Frisch, D.,and Clemen, R. T. 1994. “Beyond Expected Utility: Rethinking Behavioral Decision Research,” Psychological Bulletin (116), pp. 46-54.

Gefen, D., Karahanna, E., and Straub, D. W. 2003. “Trust and TAM in Online Shopping: An Integrated Model,” MIS Quarterly (27:1), pp. 51-90.

Gefen D., Straub D. W., and Boudreau M.-C. 2000. “Structural Equation Modeling and Regression: Guidelines for Research Practice,” Communications of the Association for Information Systems (4:7), pp. 1-77.

Goldstein, W. M., Barlas, S., and Beatie, J. 2001. “Talk About Tradeoffs: Judgments of Relative Importance and Contingent Decision Behavior,” in Conflict and Tradeoffs in Decision Making, E. U. Weber, J. Baron, and G. Loomes (eds.), New York: Cambridge University Press, pp. 175-204.

Gretzel U., and Fesenmaier, D. R. 2006. “Persuasion in Recommender Systems,” International Journal of Electronic Commerce (11:2), pp. 81-100.

Griffith D. A., Krampf, R. F., and Palmer, J. W. 2001. “The Role of Interface in Electronic Commerce: Consumer Involvement with Print Versus On-Line Catalogs,” International Journal of Electronic Commerce (5:4), pp. 135-153.

Harman, H. H. 1967. Modern Factor Analysis, Chicago: University of Chicago Press.

Häubl, G., and Murray, K. B. 2003. “Preference and Persistence in Digital Marketplaces: The Role of Electronic Recommendation Agents,” Journal of Consumer Psychology (13:1), pp. 75-91.

Häubl, G., and Trifts, V. 2000. “Consumer Decision Making in Online Shopping Environments: The Effects of Interactive Decision Aids,” Marketing Science (19:1), pp. 4-21.

Hedgcock, W., and Rao, A. R. 2009. “Trade-Off Aversion as an Explanation for the Attraction Effect: A Functional Magnetic Resonance Imaging Study,” Journal of Marketing Research. (46:1), pp. 1-13.

Hess, T. J., Fuller, M., and Campbell, D. E. 2009. “Designing Interfaces with Social Presence: Using Vividness and Extraversion to Create Social Recommendation Agents,” Journal of the Association for Information Systems (10:12), pp. 889-919.

Hess, T., Fuller, M., and Mathew, J. 2005. “Involvement and Decision-Making Performance with a Decision Aid: The Influence of Social Multimedia, and Gender,” Journal of Management Information Systems (22:3), pp. 15-54.

Higgins, E. T. 1998. “Promotion and Prevention: Regulatory Focus as a Motivational Principle,” in Advances in Experimental Social Psychology, P. M. Zanna (ed.), New York: Academic Press, pp. 1-46.

Hoffman, D. L., and Novak, T. P. 1996. “Marketing in Hypermedia Computer-Mediated Environments: Conceptual Foundations,” Journal of Marketing (60:3), pp. 50-117.

Hostler, R. E., Yoon, V. Y., and Guimaraes, T. 2005. “Assessing the Impact of Internet Agent on End Users’ Performance,” Decision Support Systems (41:1), pp. 313-323.

Igbaria, M., Parasraman, S., and Baroudi, J. J. 1996, “A Motivational Model of Microcomputer Usage,” Journal of Management Information Systems (13:1), pp. 127-143.

Indushobha C. S., Saggi, N., and Pindaro, D. 2010 “An Empirical Analysis of the Business Value of Open Source Infrastructure Technologies,” Journal of the Association for Information Systems (11:11). pp. 708-729.

Jacoby, J. 2002. “Stimulus–Organism–Response Reconsidered: An Evolutionary Step in Modeling (Consumer) Behavior,” Journal of Consumer Psychology (12:1), pp. 51-57.

Jiang, Z., and Benbasat, I. 2007a. “The Effects of Presentation Formats and Task Complexity on Online Consumers’ Product Understanding,” MIS Quarterly (31:3), pp. 475-500.

Jiang, Z., and Benbasat, I. 2007b. “Investigating the Influence of Interactivity and Vividness on Online Product Presentations,” Information Systems Research (18:4), pp. 454-470.

Jiang, Z., Chan, J., Tan, B., and Chua, W. 2010. “Effects of Interactivity on Website Involvement and Purchase Intention,” Journal of the Association for Information Systems (11:1), pp. 34-59.

Kamis, A. A., Koufaris, M., and Stern, T. 2008. “Using an Attribute-Based Decision Support System for User-Customized Products Online: An Experimental Investigation,” MIS Quarterly (32:1), pp. 159-177.

Kamis, A. A., Stern, T., and Ladik, D. M. 2010, “A Flow-Based Model of Web Site Intentions When Users Customize Products in Business-to-Consumer Electronic Commerce,” Information Systems Frontiers (12:2), pp. 157-168.

Kamis A. A., and Stohr, E. A. 2006. “Parametric Search Engines: What Makes Them Effective When Shopping Online for Differentiated Products?,” Information & Management (43:7), pp. 904-918.

Kempf, D. S., and Smith, R. E. 1998. “Consumer Processing of Product Trial and the Influence of Prior Advertising: A Structural Modeling Approach,” Journal of Marketing Research (35), pp. 325-337.

Kettanurak, V., Ramamurthy, N. K., and Haseman, W. D. 2001. “User Attitude as a Mediator of Learning Performance Improvement in an Interactive Multimedia Environment: An Empirical Investigation of the Degree of Interactivity and Learning Styles,” International Journal of Human–Computer Studies (54:4), pp. 541-583.

Kirschner, F., Paas, F., and Kirschner, P. A. 2009. “Individual and Group-Based Learning from Complex Cognitive Tasks: Effects on Retention and Transfer Efficiency,” Computers in Human Behavior (25:2), pp. 306-314.

Klein, R., and Arun R. 2009. “Interfirm Strategic Information Flows in Logistics Supply Chain Relationships,” MIS Quarterly (33:4), pp. 735-762.

Komiak X. S., and Benbasat, I. 2006. “The Effects of Personalization and Familiarity on Trust in and Adoption of Recommendation Agents,” MIS Quarterly (30:4), pp. 941-960.

Koufaris, M. 2002. “Applying the Technology Acceptance Model and Flow Theory to Online Consumer Behavior,” Information Systems Research (13:2), pp. 205-223.

Lazarus, R. S. 1991. Emotion and Adaptation, New York: Oxford University Press.

Leavitt, N. 2006. “Recommendation Technology: Will it Boost E-Commerce?,” IEEE Computer Society (39:5), pp. 13-16.

Lee, Y. E., and Benbasat, I. 2011. “Effects of Attribute Conflicts on Consumers’ Perceptions and Acceptance of Product Recommendation Agents: Extending the Effort–Accuracy Framework,” Information Systems Research (22:4), pp. 867-884.

Liao, S. S., Li, Q. D., and Xu, D. J. 2005. “A Bayesian Network-Based Framework for Personalization in Mobile Commerce Applications,” Communications of the AIS (15), pp. 494-511.

Lindell, M. K., and Whitney D. J. 2001. “Accounting for Common Method Variance in Cross-Sectional Research Designs,” Journal of Applied Psychology (86:1), pp. 114-121.

Locke, E. A., Shaw, K. R, Saari, L. M., and Latham, G. P. 1981. “Goal Setting and Task Performance: 1968-1980,” Psychological Bulletin, 90, pp. 125-152.

Lohmöller J. B. 1989. Latent Variables Path Modeling with Partial Least Squares, Heidelberg: Physica Verlag.

Luce, M. F., Bettman, J. R., and Payne, J. W. 1999. “Emotional Tradeoff Difficulty and Choice,” Journal of Marketing Research (36:2), pp. 143-159.

Luce, M. F., Bettman, J. R., and Payne, J. W. 2001. Emotional Decisions: Tradeoff Difficulty and Coping in Consumer Choice, Chicago: The University of Chicago Press.

Malhotra, N., Kim S., and Patil A. 2006. “Common Method Variance in IS Research: A Comparison of Alternative Approaches and a Reanalysis of Past Research,” Management Science (52:12), pp. 1865-1883.

Mao, J., and Benbasat, I. 2000. “The Use of Explanations in Knowledge-Based Systems: Cognitive Perspectives and a Process-Tracing Analysis,” Journal of Management Information Systems (17:2), pp. 153-179.

Mayer, R. E., and Chandler, P. 2001. “When Learning Is Just a Click Away: Does Simple User Interaction Foster Deeper Understanding of Multimedia Messages?,” Journal of Educational Psychology (93), pp. 390-397.

Mayer, R. E., and Moreno, R. 2003. “Nine Ways to Reduce Cognitive Load in Multimedia Learning,” Educational Psychologist (38), pp. 43-52.

Mehrabian, A., and Russell, J. A. 1974. An Approach to Environmental Psychology, Cambridge, MA: MIT Press.

Miller, G. A. 1956. “The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity for Processing Information,” Psychology Review (63:2), pp. 81-97.

Morrison J., and Vogel, D. 1998. “The Impacts of Presentation Visuals on Persuasion,” Information & Management (33:3), pp. 125-135.

Mudambi, S. M., and Schuff., D. 2010. “What Makes a Helpful Online Review? A Study of Customer Reviews on Amazon.com,” MIS Quarterly (34:1), pp. 185-200.

Nadkarni, S., and Gupta R. 2007. “A Task-Based Model of Perceived Website Complexity,” MIS Quarterly (31:23), pp. 501-524.

Nisbett, R., and Ross, L. 1980. “Assigning Weights to Data: The ‘Vividness Criterion,’” in Human Inference: Strategies and Shortcomings of Social Judgment, R. Nisbett and L. Ross (eds.), Englewood Cliffs, NJ: Prentice-Hall, Inc., pp. 43-62.

Nordhielm C. L. 2002. “The Influence of Level of Processing on Advertising Repetition Effects,” Journal of Consumer Research (29:3), pp. 371-382

Nov, O., and Ye, C. 2008. “Users’ Personality and Perceived Ease of Use of Digital Libraries: The Case for Resistance to Change,” Journal of the American Society for Information Science and Technology (59:5), pp. 845-851.

Novak, T. P., Hoffman D. L., and Yung Y. F. 2000. “Measuring the Customer Experience in Online Environments: A Structural Modeling Approach,” Marketing Science (19:1), pp. 22-42.

Nysveen, H., Pedersen P. E., and Thorbjørnsen H. 2005. “Explaining Intention to Use Mobile Chat Services: Moderating Effects of Gender,” Journal of Consumer Marketing (22:5), pp. 247-256.

Orlikowski, W. J., and Iacono, C. S. 2001. “Research Commentary: Desperately Seeking the ‘IT’ In IT Research—A Call to Theorizing the IT Artefact,” Information Systems Research (12:2), pp. 121-134.

Palanivel, K., and Sivakumar R. 2010. “A Study on Implicit Feedback in Multicriteria E- Commerce Recommender System, Journal of Electronic Commerce (11:2), pp. 140-156.

Parboteeah, D. V., Valacich J. S., and Wells J. D. 2009. “The Influence of Website Characteristics on a Consumer’s Urge to Buy Impulsively,” Information Systems Research (20:1), pp. 60-78.

Park, M., and Park, J. 2009. Exploring the Influences of Perceived Interactivity on Consumers’ E-Shopping Effectiveness, Journal of Customer Behaviour (8:4), pp. 361-379.

Pavlou, P. A., and Fygenson, M. 2006. “Understanding and Predicting Electronic Commerce Adoption: An Extension of the Theory of Planned Behavior,” MIS Quarterly (30:1), pp. 115-144.

Pavlou, P. A., Liang, H. G., and Xue, Y. J. 2007. “Understanding and Mitigating Uncertainty in Online Exchange Relationships: A Principal–Agent Perspective,” MIS Quarterly (31:1), pp. 105-136.

Payne, J. W. 1982. “Contingent Decision Behavior,” Psychological Bulletin (92:2), pp. 382-402.

Payne, J. W., and Bettman, J. R., and Johnson, E. 1988. “Adaptive Strategy Selection in Decision Making,” Journal of Experimental Psychology: Learning, Memory, and Cognition (14:3), pp. 534-552.

Payne, J. W., Bettman, J. R., and Johnson, E. J. 1993. The Adaptive Decision Maker, Cambridge, UK: Cambridge University Press.

Pereira, R. E. 2000. “Optimizing Human–Computer Interaction for the Electronic Commerce Environment,” Journal of Electronic Commerce Research (1:1), pp. 23-44.

Podsakoff, P., and Organ, D. 1986. “Reports in Organizational Research: Problems and Prospects,” Journal of Management Studies (27), pp. 305-327.

Potter, R. E., and Bathazard, P. 2004. “The Role of Individual Memory and Attention Processes During Electronic Brainstorming,” MIS Quarterly (28:4), pp. 621-643.

Ricci, F., and Werthner, H. 2006. “Introduction to the Special Issue: Recommender Systems,” International Journal of Electronic Commerce (11:2), pp. 5-9.

Ringle, C. M., Wende, S., and Will, A. 2005. Smart PLS. Hamburg: University of Hamburg.

Schafer, J. B., Konstan, J. A., and Riedl, J. 2002. “Meta-Recommendation Systems: User-Controlled Integration of Diverse Recommendations,” paper presented at the 11<sup>th</sup> International Conference on Information and Knowledge Management, McLean, VA, November.

Schindler, S., Reinhard, M., and Stahlberg, D. 2011. “Repetition of Educational Aids Advertising Affects Attitudes, Psychological Reports,” Psychological Reports (108: 3), pp. 693-698.

Sherman, E., Mathur, A., and Smith, R. B. 1997. “Store Environment and Consumer Purchase Behavior: Mediating Role of Consumer Emotions,” Psychology and Marketing (14:4), pp. 361-378.

Simon, H. A. 1955. “A Behavioral Model of Rational Choice,” Quarterly Journal of Economics (69), pp. 99-118.

Sproull, L., Subramani, M., Kiesler, S., Walker, J. H., and Waters, K. 1996. “When the Interface Is a Face,” Human– Computer Interaction (11), pp. 97-124.

Starbuck, W. J., and Webster, J. 1991. “When Is Play Productive?,” Accounting, Management, and Information Technology (1), pp. 71-90.

Sun, H., and Zhang, P. 2006, “The Role of Affect in IS Research: A Critical Survey and a Research Model” in Human–Computer Interaction and Management Information Systems: Foundations (I), P. Zhang and D. Galleta (eds.), Armonk, NY: M. E. Sharpe, pp. 295-329.

Sun, H., and Zhang, P. 2008. “An Exploration of Affect Factors and Their Role in User Technology Acceptance: Mediation and

Causality,” Journal of the American Society for Information Science and Technology (59:8), pp. 1252-1263.

Suri, R., and Monroe, K. B. 2003. “The Effects of Time Constraints on Consumers’ Judgments of Prices and Products,” Journal of Consumer Research (30), pp. 92-104.

Swanson, R. A., and Law, B. 1993. “Whole-Part-Whole Learning Model,” Performance Improvement Quarterly (6:1), pp. 43-53.

Sweller, J. 1988. “Cognitive Load During Problem Solving: Effects on Learning,” Cognitive Science (12), pp. 257-285.

Tabachnick, B. G., and Fidell, L. S. 1996. Using Multivariate Statistics (3<sup>rd</sup> ed.), New York: HarperCollins.

Tam, K. Y., and Ho, Y. S. 2005. “Web Personalization as a Persuasion Strategy: An Elaboration Likelihood Model Perspective,” Information Systems Research (16:3), pp. 271-291.

Tan, C. H., Teo, H. H., and Benbasat I. 2010. “Assessing Screening and Evaluation Decision Support Systems: A Resource-Matching Approach,” Information Systems Research (21:2), pp. 305-326.

Teo, H. H., Oh, L. B., Liu, C., and Wei, K. K. 2003. “An Empirical Study of the Effects of Interactivity on Web User Attitude,” International Journal of Human-Computer Studies (58:3), pp. 281-05.

Thatcher, J. B., and Perrewé, P. L. 2002. “An Empirical Examination of Individual Traits as Antecedents to Computer Anxiety and Computer Self-Efficacy,” MIS Quarterly (26:4), pp. 381-396.

Todd, P., and Benbasat, I. 1996. “The Effects of Decision Support and Task Contingencies On Model Formulation: A Cognitive Perspective,” Decision Support Systems (17), pp. 241-252.

Uhrich, S. 2011. “Explaining Non-Linear Customer Density Effects on Shoppers’ Emotions and Behavioral Intentions in a Retail Context: The Mediating Role of Perceived Control,” Journal of Retailing and Consumer Services (18), pp. 405-413.

Van der Heijden, H. 2003. “Factors Influencing the Usage of Websites: The Case of a Generic Portal in the Netherlands,” Information & Management (40:6), pp. 541-549.

Van der Heijden, H. 2004. “User Acceptance of Hedonic Information Systems,” MIS Quarterly (28:4), pp. 695-704.

van Gog, T., Kester, L., and Paas, F. 2011. “Effects of Concurrent Monitoring On Cognitive Load And Performance as a Function of Task Complexity,” Applied Cognitive Psychology (25:4), pp. 584-587.

Vegas, J., Crestani, F., and de la Fuente, P. 2007. “Context Representation for Web Search Results,” Journal of Information Science (33:1), pp. 77-94.

Venkatesh, V. 2000. “Determinants of Perceived Ease of Use: Integrating Control, Intrinsic Motivation, and Emotion into the Technology Acceptance Model,” Information Systems Research (11:4), pp. 342-365.

Venkatesh, V., and Agarwal, R. 2006. “Turning Visitors into Customers: A Usability-Centric Perspective on Purchase Behavior in Electronic Channels,” Management Science (52:3), pp. 367-382.

Venkatesh, V., Morris, M. G., Davis, G. B., and Davis, F. D. 2003. “User Acceptance of Information Technology: Toward a Unified View,” MIS Quarterly (27:3), pp. 425-478.

Wang, W., and Benbasat, I. 2007. “Recommendation Agents for Electronic Commerce: Effects of Explanation Facilities on

Trusting Beliefs,” Journal of Management Information Systems (23:4), pp. 217-246.

Wang, W., and Benbasat, I. 2009. “Interactive Decision Aids for Consumer Decision Making in e-Commerce: The Influence of Perceived Strategy Restrictiveness” MIS Quarterly (33:2), pp. 293-320.

Widing, R. E., and Talarzyk, W. W. 1993. “Electronic Information Systems for Consumers: An Evaluation of Computer-Assisted Formats in Multiple Decision Environments,” Journal of Marketing Research (30:2), pp. 125-141.

Wood, R. E. 1986. “Task Complexity: Definition of the Construct,” Organizational Behavior and Human Decision Processes (37:1), pp. 60-82.

Xiao, B., and Benbasat, I. 2007. “E-Commerce Product Recommendation Agents: Use, Characteristics, and Impact,” MIS Quarterly (31:1), pp. 137-209.

Xu, D. J. 2006/2007. “The Influence of Personalization in Affecting Consumer Attitude toward Mobile Advertising in China,” Journal of Computer Information Systems (47:2), pp. 9-19.

Xu, D. J., Benbasat, I., and Cenfetelli, R. 2013. “Integrating Service Quality with System and Information Quality: An Empirical Test of the E-Service Context,” MIS Quarterly (37:3), pp. 777-794.

Xu., D. J., Cenfetelli, R., and Aquino, K. 2012. “The Influence of Media Cue Multiplicity on Deceivers and Those Who Are Deceived,” Journal of Business Ethics (106:3), pp. 337-352.

Yoo, W-S., Lee, Y., and Park, J. 2010. “The Role of Interactivity in E-tailing: Creating Value and Increasing Satisfaction,” Retailing and Consumer Services (17), pp. 89-96.

## About the Authors

Jingjun (David) Xu is an assistant professor of Management Information Systems at Wichita State University. Jingjun received his Ph.D. from the University of British Columbia in 2011. His research interests include human-computer interaction, e-commerce, computer-mediated deception, and mobile commerce. His work has been published or is forthcoming in journals such as MIS Quarterly, Information Systems Research, Journal of the Association for Information Systems, Journal of Business Ethics, Decision Support Systems, Journal of Computer Information Systems, and Communications of the Association for Information Systems.

Izak Benbasat (Ph.D. University of Minnesota, 1974; Doctorat Honoris Causa, Université de Montréal, 2009) is a Fellow of the Royal Society of Canada and Canada Research Chair in Information Technology Management at the Sauder School of Business, University of British Columbia. He currently serves on the editorial boards of Journal Management Information Systems and Information Systems Journal. He was editor-in-chief of Information Systems Research, editor of the Information Systems and Decision Support Systems Department of Management Science, and a senior editor of MIS Quarterly. He became a Fellow of the Association for Information Systems (AIS) in 2002, received the LEO Award for Lifetime Exceptional Achievements in Information Systems from AIS in 2007, and was conferred the title of Distinguished Fellow by the Institute for Operations Research and Management Sciences (INFORMS) Information Systems Society in 2009.

Ronald T. Cenfetelli is associate professor and chair of of Management Information Systems at the University of British Columbia’s Sauder School of Business. His research interests include human– computer interaction, e-business, the negative aspects of technology usage, and research methods. His research has appeared in MIS Quarterly, Information Systems Research, Journal of the AIS, and other outlets. Ron has won awards for his research, teaching, and service. He currently serves as an associate editor for MIS Quarterly, where he recently received the outstanding associate editor award. Ron had previous careers with Pfizer, Inc. And the U.S. Navy.
