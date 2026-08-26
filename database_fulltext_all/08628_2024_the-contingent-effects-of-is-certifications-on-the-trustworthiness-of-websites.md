---
otero_id: 8628
otero_key: "JWUTKKNN"
title: "The Contingent Effects of IS Certifications on the Trustworthiness of Websites"
authors: "Martin Adam; Sebastian Lins; Ali Sunyaev; Alexander Benlian"
year: "2024"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00836"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2024

# The Contingent E  ffects of IS Cer    tifications on the T   rustwor thiness of Websites

Martin Adam , martin.adam@uni-goettingen.de

Sebastian Lins , sebastian.lins@kit.edu

Ali Sunyaev , sunyaev@kit.edu

Alexander Benlian , benlian@ise.tu-darmstadt.de

Follow this and additional works at: https://aisel.aisnet.org/jais

# The Contingent Effects of IS Certifications on the Trustworthiness of Websites

Martin Adam,<sup>1</sup> Sebastian Lins,<sup>2</sup> Ali Sunyaev,<sup>3</sup> Alexander Benlian<sup>4</sup>

<sup>1</sup>University of Goettingen, Germany, martin.adam@uni-goettingen.de <sup>2</sup>Karlsruhe Institute of Technology, Germany, sebastian.lins@kit.edu <sup>3</sup>Karlsruhe Institute of Technology, Germany, sunyaev@kit.edu <sup>4</sup>Technical University of Darmstadt, Germany, benlian@ise.tu-darmstadt.de

## Abstract

Information systems (IS) research has largely treated IS certifications (i.e., graphical cues that prove the endorsement of independent third parties) as universally effective at improving website visitors’ perceptions of trustworthiness. However, inconclusive findings on the effectiveness of IS certifications on websites have emerged, critically challenging their usefulness. We seek to reconcile these inconclusive findings by drawing on swift trust theory and the notion of humans as cognitive misers. Specifically, we investigate whether the effects of IS certifications are contingent on visitors’ expectations and the website’s baseline trustworthiness (i.e., the original website before adding and visitors’ processing of IS certifications). Through a multistudy investigation combining an online (N = 191) and a follow-up field experiment with up to €4 million in sales volume (N = 306), we reveal the contingent effects of IS certifications on the trustworthiness of websites: Below (but not above) a certain level of a website’s baseline trustworthiness (i.e., the trust tipping point), IS certifications significantly increase trustworthiness. We also show that IS certifications do not increase the likelihood of user registrations (i.e., trust-related behavior) when a website’s baseline trustworthiness surpasses this trustworthiness threshold. Overall, we provide an important new perspective that explains and resolves previous inconsistent findings on the (in)effectiveness of IS certifications for trustworthiness and subsequent trust-related behaviors. We equip practitioners with valuable and actionable guidance on the usefulness of IS certifications to strengthen their digital businesses.

Keywords: IS Certifications, Swift Trust, Humans as Cognitive Misers, Multistudy, Experiment

René Riedl was the accepting senior editor. This research article was submitted on August 30, 2021 and underwent four revisions.

## 1 Introduction

Information systems (IS) certifications<sup>1</sup> are graphical cues embedded in a website that independent third parties (i.e., certification bodies) provide as proof of endorsement after providers of digital services have completed a thorough attestation process (e.g., Löbbers et al., 2022; Özpolat & Jank, 2015). Wellknown IS certifications include “TRUSTe–Certified Privacy” for web shops and “ISO 9001–Quality Management Systems” for quality management standards (see Figure 1).

![](/api/attachments/JWUTKKNN/fulltext/images/8aae8c7b9eae81bd331e117c951f60795e16c5511c969f9bf86bdac1f36194a0.jpg)

![](/api/attachments/JWUTKKNN/fulltext/images/59485f31ae96ea5b9bb0140208d4ed928be6cb00407641149dc0ee337f224941.jpg)  
Note: Service providers address visitors’ perceptions of trustworthiness by employing a TRUSTe IS certification to indicate that high-quality data protection standards are in place that maintain a user’s privacy or an ISO9001 certification to signal highquality management practices.

# Figure 1. Examples of IS Certifications

IS certifications represent some of the most frequently stated reasons that websites succeed at increasing visitors’ perceived trustworthiness and thus achieving user onboarding outcomes (e.g., Lansing et al., 2019; McKnight et al., 2002; Özpolat et al., 2013). For example, IS certifications have been shown to effectively convince first-time visitors to register, purchase, and revisit websites (e.g., Liu & Goodhue, 2012; Venkatesh et al., 2016).

The growing demand for and importance of IS certifications are in line with recent trends to increase the trustworthiness of websites by issuing certifications (e.g., ISO, 2022; TrustedShops, 2020). Increasing perceived trustworthiness through IS certifications has become even more important for user onboarding outcomes, given the ever-growing skepticism of electronic markets due to the numerous data breaches and performance issues (e.g., service failures and unavailability) reported by wellrecognized companies, such as Facebook, Amazon, and Google (e.g., Al-Natour et al., 2020; Gerlach et al., 2019) and the increasing prevalence of fraud and phishing websites (e.g., Abbasi et al., 2015). Due to recent regulatory changes (European Commission, 2021), IS certifications are slowly turning into a primary mechanism for organizations to demonstrate compliance with data protection, security, and ethical requirements, such as IS certifications for cloud services (Lansing et al., 2018; Lansing et al., 2019) or AI-embedded systems (Matus and Veale 2021; Morik et al. 2021). An IS certification typically necessitates that service providers set up reliable websites and implement a costly underlying IT infrastructure to ensure adequate security, data protection, and quality management processes (e.g., Lansing et al., 2018; Lansing et al., 2019). Furthermore, acquiring and maintaining IS certifications comes at a considerable expense (e.g., ISO, 2022; Mavlanova et al., 2016), starting at approximately \$2,500 per year to display an IS certification on a common web shop and going up to \$75,000 per year for large organizations that require specific and effortful auditing (e.g., banking, medical services). As such, service providers have a strong interest in validating whether IS certifications are effective in order to justify their costs and effort.

The high demand and relevance of IS certifications resonate with recent calls in IS research to address ways of regulating IT and signaling this regulation to users (e.g., Gozman et al., 2020). Previous research has largely focused on explaining how IS certifications affect first-time visitors, why these effects occur, and how to predict them (e.g., Lansing et al., 2018; Lowry et al., 2012). Indeed, IS certifications are considered some of the most frequently cited reasons in IS research that websites succeed at increasing visitors’ perceived trustworthiness (e.g., Lansing et al., 2019; McKnight et al., 2002; Özpolat et al., 2013). However, previous research explicitly investigating IS certifications has often failed to demonstrate the effectiveness of these certifications, resulting in overall puzzling and inconclusive findings on IS certifications (e.g., Lansing et al., 2018; Lansing et al., 2019; Löbbers et al., 2022). For instance, of the IS and related studies that have investigated the effects of IS certification on a website’s trustworthiness, 71% noted a positive effect of IS certifications on trustworthiness, while 29% found no significant effect (see Figure A1 and Table A1 in the Appendix for a review). These inconsistent findings suggest the need to determine whether and under which contingencies IS certifications are an effective means to improve trustworthiness and related user onboarding outcomes, such as user registrations (e.g., Kim et al., 2016; Lansing et al., 2019). Without a proper understanding, service providers may acquire and display expensive IS certifications even though they do not benefit from them.

In this article, we argue that prior research has largely assumed that IS certifications are universally effective at increasing trustworthiness perceptions (e.g., Kim et al., 2008; Löbbers & Siegfried, 2018; McKnight et al., 2002). However, this simplistic view of the unconditional effects of IS certifications has drawbacks, neglecting the potential of important boundary conditions that may influence the effectiveness of IS certifications. Our research aims to challenge the assumption of unconditionally effective IS certifications by presuming that the effects of IS certifications are dependent on visitors’ expectations and the website’s baseline trustworthiness (i.e., the original website’s trustworthiness before visitors process IS certifications). To do so, we draw on swift trust theory (Jarvenpaa et al.,

1998; Meyerson et al., 1996) and the notion of humans as cognitive misers (Lynch et al., 1988; Taylor, 1981): Humans presumably tend to economize on their cognitive effort by only focusing on some potentially important aspects of their situation in general and by considering their behavior relative to a website specifically. When visitors encounter a new website for the first time, their most immediate concern relates to the question, “Will I regret using this website?” (e.g., McKnight & Chervany, 2001; McKnight et al., 2002). Therefore, visitors’ expectations and perceived website trustworthiness and related IS certifications are most relevant to visitors during their first encounter. However, if visitors view the unknown website and consider it already trustworthy enough before processing an IS certification, thus surpassing a trustworthiness threshold or trust tipping point (Liu & Goodhue, 2012), visitors may not need supplementary IS certifications on the website because they do not need to further process IS certifications to evaluate the website’s trustworthiness. Rather than prioritizing the presence of an IS certification, visitors may instead devote their limited cognitive resources to other reasons to elaborate on using or not using the website. Consequently, investigating whether visitors’ expectations and perceived trustworthiness of a website before processing an IS certification render the display of IS certifications less relevant is a worthwhile endeavor. We investigate the (in)effectiveness of IS certifications depending on whether the website’s baseline trustworthiness (i.e., before processing an IS certification) is below versus above the trust tipping point. More specifically, we intend to answer the following research question (RQ):

RQ: How do IS certifications influence a website’s trustworthiness and related user registrations if the website’s baseline trustworthiness is below versus above the trust tipping point?

We ran a multistudy investigation using two complementary experiments to answer our research question. First, we conducted an online experiment with 191 participants in which we investigated the effects of IS certifications on participants’ perceptions of trustworthiness below and above the baseline trustworthiness threshold of a hypothetical website. Subsequently, we conducted a randomized field experiment with 306 participants to corroborate the findings from our online experiment with real-world user registrations, identifying significant consequences for both website visitors and service providers.

The results consistently indicate that IS certifications significantly increase a website’s trustworthiness and likelihood of user registrations when the website’s baseline trustworthiness is below (but not above) an established trust tipping point. Our research mainly contributes by providing a novel and important view of the (in)effectiveness of IS certifications. We extend prior research findings by revealing a boundary condition of IS certification effectiveness and providing a revelatory explanation in the form of the trust tipping point. We unveil that IS certifications are not always effective at increasing trustworthiness because the effects of IS certifications do not occur in a vacuum and researchers must consider a website’s baseline trustworthiness. By doing so, researchers can increase the predictive power of research models on certification effectiveness. We also advance prior research by validating that the processing of IS certifications follows a cognitive-efficient logic: Visitors tend to appreciate IS certifications only when they are relevant to their decision to trust a website. These insights are crucial, as they help explain and reconcile previous inconclusive findings and provide guidance for future investigations on the effectiveness of IS certifications, which are particularly important given that IS certifications and their related designs are increasingly becoming an object of analysis in both research and practice. Additionally, we offer service providers valuable insights into whether and when IS certifications enhance their website designs to bolster their digital businesses. Given our randomized field experiment, these insights are also externally valid and backed by user behavior and related sales in the real world.

## 2 Theoretical Background

In this section, we first present the stream of literature on IS certifications and its inconclusive findings on the positive effects of IS certifications on trustworthiness. We then briefly review research on trust in IS and specifically conceptualize swift trust to better explain how visitors determine websites’ (swift) trustworthiness. Lastly, we draw on the notion of humans as cognitive misers to develop a broader conceptualization of users’ processing of IS certifications to form swift trust, setting the stage for the decisions and related onboarding outcomes that visitors subsequently face, namely, whether to trust a website (i.e., trustworthiness) and whether to register on a website (i.e., trust-related behavior).

## 2.1 IS Certifications

Service providers draw on IS certifications as one of the most prevalent website assurance elements for shaping visitors’ perceptions of trustworthiness and decisions to register on a website. IS certifications have become one of the most important antecedents of a website’s trustworthiness because they signal institution-based trust (e.g., Gefen et al., 2003; Lansing et al., 2019; Löbbers et al., 2022) and are particularly valued by small and medium-sized service providers (Kim et al., 2016; Sunyaev & Schneider, 2013). As these service providers lack a strong, trust-building market position, they often embed IS certifications in their websites to compensate for their lack of trustworthiness (Kim et al., 2016).

Despite the expected positive effects of IS certifications, several researchers have highlighted the emergence of inconsistent findings regarding the missing effects of IS certifications on visitors’ perceived trustworthiness (e.g., Hoffmann et al., 2014; Hu et al., 2010; Lansing et al., 2018). To overcome the conundrum of inconsistent findings, prior research has started to examine contingency factors shaping IS certification effects, including the structural elements of IS certifications (Lansing et al., 2018), visitors’ culture (Kim et al., 2016), and their understanding of such certifications (Lowry et al., 2012). These studies have found more nuanced results that challenge the universality of the beneficial effects of IS certifications. Nevertheless, further research is needed to solve this puzzle (e.g., Lansing et al., 2018; Özpolat & Jank, 2015). To reconcile previous inconsistent findings and offer guidance for both research and practice on when and why (costly) IS certifications are effective in increasing visitors’ trustworthiness, we first need to shed light on how new visitors determine the trustworthiness of websites. For this purpose, we need to understand what constitutes and determines the trustworthiness of websites.

## 2.2 Trust in IS Research and Swift Trust in Websites

A substantial stream of IS literature has examined trust in electronic markets, with most studies examining trust in websites and the corresponding providers (e.g., Benlian et al., 2012; Kim et al., 2016; Liu & Goodhue, 2012). Much of this literature addresses one of three general questions in the online domain: (1) what are the antecedents of trust, (2) what is the nature of the trust construct, and (3) what are the consequences of trust? The first category focuses on the impact of various drivers (e.g., website aesthetics, trust-assuring arguments, personalization) of trust (e.g., Cyr et al., 2010; Gefen et al., 2003; Kim & Benbasat, 2009). The second category comprises studies that aim to understand the trust construct and its relation to other constructs, such as distrust and risk (e.g., Dimoka, 2010; Lewicki et al., 1998). The third and last category—the category in which this article is primarily positioned—focuses on how trust-related perceptions translate into trust-related intentions and ultimately behaviors, particularly in the context of unknown websites (e.g., Liu & Goodhue, 2012; McKnight et al., 2002).

In the case of user onboarding on websites, visitors may encounter a novel website with which they have no prior experiences and interactions (e.g., McKnight et al., 2002; McKnight et al., 2004). This is the realm of initial or “swift” trust (Jarvenpaa et al., 1998; Meyerson et al., 1996). Unlike other forms of trust that rely on experience, familiarity, and/or prior interactions, swift trust develops in unfamiliar settings in which individuals usually require a certain amount of trust before they can engage in an action (e.g., working together in a group) and often face constraints (e.g., limited time, short attention span) (e.g., Blomqvist & Cook, 2018; Li et al., 2009). Swift trust can be divided into trustworthiness (i.e., trusting beliefs), trusting intentions, and trust-related behaviors, thus differentiating between a visitor’s perceptions of a website’s characteristics and their intentions and actions when interacting with the website, whereas trustworthiness usually leads to trusting intentions and behavior (e.g., Clemons et al., 2016; McKnight et al., 2002; Pennington et al., 2003). Accordingly, we investigate swift trustworthiness in a website and the resulting swift trust-related behavior. Specifically, swift trustworthiness is a visitor’s trusting belief that a website and the respective service provider are benevolent (i.e., has care and motivation to act in the visitor’s interests), competent (i.e., has the ability to do what the visitor needs), and honest (i.e., displays honesty and promise-keeping in the interactions with the visitor) (McKnight et al., 2004; Venkatesh et al., 2016). Swift trust-related behavior refers to visitors actions that demonstrate dependence on a website and make visitors vulnerable, such as registering and purchasing website offerings (McKnight et al., 2002).

While encountering the website, visitors do not face a single decision about whether to use a website’s service but several decisions that ultimately lead to the usage decision (e.g., Adam et al., 2024; McKnight et al., 2004; Xu et al., 2017). Visitors to the website are usually at an introductory stage (i.e., swift trustworthiness-forming), which is closely followed by a subsequent exploratory stage (i.e., elaborating on trust-related behaviors). At the introductory stage of the user onboarding process, visitors usually form swift trustworthiness conceptions before they consider the website’s specific offerings. This early stage in the relationship sets the tone for visitors’ subsequent onboarding decisions: only if visitors form positive beliefs about the website during this initial period will they consider exploring and evaluating the website and its offerings. Consequently, a website must foster visitors’ swift trustworthiness to induce them to use and interact with it. A visitor’s decision to declare a website trustworthy may turn into an observable trustrelated behavior (e.g., user registration) but it may also remain unobservable—for example, visitors may trust a website but fail to find anything they need on the website, resulting in no observable trust-related behavior (e.g., Gefen et al., 2003). Prior research supports these links between trustworthiness and website usage (e.g., Jarvenpaa et al., 2000; Liu & Goodhue, 2012; McKnight et al., 2004).

Once visitors have decided to trust a website, they move to the exploratory stage and may decide to further engage with the website, e.g., by registering on it (i.e., user registration), before engaging in any transactions. In our context, we refer to user registration as such a trust-related behavior (e.g., Huang et al., 2021; Roethke et al., 2020). While user registration is not always needed to offer a service, it is usually critical for service providers because it is often required to provide personalized services and enable purchases. Thus, it is a crucial enabler for the economic viability of service providers. For instance, a cloud or audit service provider can only develop high-quality personalized services and thus generate revenue if visitors have first registered via the user onboarding process.

Since visitors are usually in introductory and subsequent exploratory stages when they undertake different cognitive processes to pursue different objectives (i.e., swift trust formation vs. user registration), visitors are receptive to different website design elements that allow them to manage different decisions during the onboarding process (e.g., Adam et al., 2024; Huang et al., 2019; Lambrecht et al., 2011). To theorize how visitors use their cognitive resources to assess the (swift) trustworthiness of websites and when they make decisions about trust-related behaviors, we draw on the notion of humans as cognitive misers and its role in the trust tripping point.

## 2.3 Humans as Cognitive Misers and the Trust Tipping Point

The notion of humans as cognitive misers (Lynch et al., 1988; Taylor, 1981) highlights the limited cognitive resources of individuals and the demand for fast and efficient information processing. Accordingly, individuals strive to make decisions without consuming too many resources (Simon, 1956) and are often willing to engage in a more economical rather than a more elaborate and cumbersome informationprocessing mechanism, thereby potentially compromising the accuracy of the results (e.g., Payne et al., 1996). For present purposes, an individual’s information processing can be summarized as follows: “No more information is retrieved for use in attaining a processing objective than is sufficient to allow the objective to be attained. When this minimal amount has been retrieved, the search terminates” (Wyer & Srull, 1986, p. 331). Accordingly, we consider visitors as cognitive misers who seek to reduce cognitive complexity and resource consumption by making decisions using whatever information is salient during the decision-making process when encountering an unknown website. Other relevant information is retrieved from long-term memory or is collected externally if the original salient information is insufficiently diagnostic to attain the task objective (Feldman & Lynch, 1988; Lynch et al., 1988). Applied to the electronic market context, visitors only pay attention to website design elements that promise a significant gain in achieving a predefined goal (e.g., deciding whether to trust a website). Once they reach this goal, visitors do not waste mental effort on further processing information to pursue this objective and instead shift attention toward a different aim.

According to the premises of the cognitive miser notion and swift trust theory, visitors face two countervailing tendencies when deciding whether to trust a website. On the one hand, visitors are cognitive misers with limited cognitive resources and thus prefer fast and efficient information processing. As such, they usually favor heuristics, such as considering any presented website and related offerings as true (i.e., truth bias) (Levine et al., 1999; Millar & Millar, 1997). On the other hand, visitors have serious concerns about websites and the related potential threats (e.g., identity theft, monetary losses, spyware) (e.g., Lins et al., 2022), and “there is … considerable evidence that users perceive significant risks and uncertainty in interacting with web-based vendors” (McKnight et al., 2002, p. 298). However, such skepticism incurs high cognitive costs for visitors, which is contrary to their preference to reduce the cognitive complexity involved in decision-making (Lynch et al., 1988; Taylor, 1981). As a result, visitors face “the tension between appropriate but cognitively expensive skepticism on the one hand, and the human desire to reduce cognitive complexity on the other” (Liu & Goodhue, 2012, p. 1249). This tension manifests in visitors’ subjective and individual trustworthiness threshold, a so-called trust tipping point, in that they engage in cognitive processes (e.g., searching for and processing trust signals) to increase their trust in a website until they consider the website to be trustworthy enough (Liu & Goodhue, 2012). At this (subjective) tipping point, a visitor reduces the priority of trustworthiness in their mental calculus and devotes cognitive resources to other user onboarding decisions that represent trustrelated behaviors, such as user registration. Whereas trust signals may be an intuitive means to support visitors’ formation of trustworthiness in a website, these signals may be less valuable if visitors perceive the website to be already sufficient to reach the trus tipping point. We will examine this proposition in more detail in the following.

## 3 Research Framework and Hypotheses Development

In the following, we argue that IS certifications have a causal effect on trustworthiness but only when the website’s trustworthiness is below (H1) but not above (H2) the trust tipping point (see Figure 2).

![](/api/attachments/JWUTKKNN/fulltext/images/d806f104aa6f831eec394dce0245b6c82da373a9292594a77d08fd80d0dbea2f.jpg)  
Figure 2. Effects of IS Certifications Below and Above the Trust Tipping Point

## 3.1 The Effect of IS Certifications Below the Trust Tipping Point

According to the notion of humans as cognitive misers (Lynch et al., 1988; Taylor, 1981), individuals attempt to reduce the cognitive complexity of their decisionmaking processes. As such, an individual’s attitude toward an offering depends on their beliefs about not only the offering per se but also a reference point to which the individual can compare the offering to facilitate the decision (Schwarz & Bohner, 2001). Individuals derive their (subjective and often subconscious) reference point from either the memory of a known offering they trusted or an ideal view of an offering (Feldman & Lynch, 1988; Lynch et al., 1988). Consistent with the anchoring-and-adjustment heuristic (Tversky & Kahneman, 1974), visitors then compare the new offering with their reference point instead of computing an absolute judgment of the website’s offering to reduce their cognitive effort. This approach is in line with swift trust research in that individuals who lack knowledge and rich experiences often engage in category-driven information processing during the formation of (swift) trustworthiness and thus tend to use expectations built on categories from related experiences and knowledge in similar situations (e.g., Blomqvist & Cook, 2018; Hung et al., 2004; Meyerson et al., 1996).

Regarding the application to electronic markets, when visiting a website, visitors initially care about forming trustworthiness (Jarvenpaa et al., 1998; Meyerson et al., 1996) and thus may first assess the website’s trustworthiness based on simple questions relating to their reference point in the respective category, such as “Is this a famous cloud service like Dropbox?” When a visitor compares the new website to the reference point, they are expected to feel uncomfortable trusting the website until they perceive that it is close to or even better than the reference point. The trust tipping point is then the point at which the visitor (subjectively) perceives the characteristics of the website to be as close as possible to the reference point, enabling them to accept the website as trustworthy enough and allowing them to finish the cognitive evaluation of its trustworthiness. The visitor thus continues the cognitively difficult process of looking for trust signals until they perceive enough trustworthiness (i.e., the trust tipping point is reached) or abandon the process (Lynch et al., 1988; Taylor, 1981). Therefore, we hypothesize that IS certifications can increase the perceived trustworthiness of a website when its baseline trustworthiness is below the trust tipping point. We define website baseline trustworthiness as a visitor’s perceived trustworthiness of the website when the visitor encounters the website for the first time without processing the IS certification. This hypothesis is also in accordance with previous literature in that individuals form swift trust by relying on third parties and their independent information about a subject matter (Hung et al., 2004; Li et al., 2009; Robert et al., 2009) and, specifically, by processing IS certifications (e.g., McKnight et al., 2004), whereas visitors’ perceptions of a website’s trustworthiness do not significantly increase beyond a certain threshold (Liu & Goodhue, 2008; Liu & Goodhue, 2012). Based on this logic and previous empirical findings, we derive the following hypothesis.

H1: If the baseline trustworthiness of a website is below the trust tipping point, present (vs. absent) IS certifications significantly increase visitors’ perceived trustworthiness of the website.

## 3.2 The Effect of IS Certifications Above the Trust Tipping Point

Next, we want to turn to situations where the baseline trustworthiness of a website is above the trust tipping point. According to the notion of humans as cognitive misers, individuals intend to achieve efficient (and not necessarily perfect) outcomes (Simon, 1956). Therefore, individuals pay attention to and then process only those signals that promise a significant gain toward achieving a predefined goal (Wyer & Srull, 1986). Once this goal has been achieved, the individual does not waste mental effort on further processing information in pursuit of the goal and instead shifts their attention toward a new goal. This process aligns with swift trust research in that individuals change their interactions and activities once they have formed enough (swift) trustworthiness (e.g., Blomqvist & Cook, 2018; Robert et al., 2009).

In the user onboarding process context, we argue that IS certifications do not increase the website’s trustworthiness if its baseline trustworthiness is above the visitor’s trust tipping point. Once a visitor evaluates a new website as close to or even better than their reference point, the individual deems the website trustworthy enough, thus stopping the cognitively difficult task of forming perceptions of trustworthiness and focusing on other important and cognitively demanding aspects, such as evaluating the website’s services (Liu & Goodhue, 2012). However, what will happen with the previously hypothesized effect of IS certifications on increasing trustworthiness once this shift in focus occurs? We argue that an IS certification does not significantly affect trustworthiness if the website’s baseline trustworthiness is above the trust tipping point because we expect visitors to process and utilize an IS certification only if the additional cognitive effort needed to process this certification information justifies a likely improvement in decisionmaking. Consequently, once a visitor decides that the website is trustworthy enough and thus reaches their (individual) trust tipping point, we expect trustworthiness to no longer be diagnostic (i.e., relevant) for further evaluations of the website (Cohen & Reed, 2006; Feldman & Lynch, 1988). Therefore, we believe that adding IS certifications to a website does not significantly increase a visitor’s perception of its trustworthiness, as the visitor drops trustworthiness from their mental calculus. This argument is in line with previous IS research that, for instance, demonstrated that trustworthiness only affected revisit intentions as long as saturation was not reached (Liu & Goodhue, 2012). We hypothesize that IS certifications lose their relevance and thus their effect on trustworthiness when the website’s baseline trustworthiness is above the trust tipping point.

H2: If the baseline trustworthiness of a website is above the trust tipping point, existing (vs. absent) IS certifications do not significantly increase visitors’ perceived trustworthiness of the website.

## 4 Research Method

We used the complementary properties of an online experiment and a follow-up randomized field experiment to test our proposed hypotheses (e.g., Fink, 2022). The first was an online experiment (Study 1) in a setting with high internal validity to test the effects of IS certifications on trustworthiness below and above the trust tipping point (H1 and H2). Subsequently, we conducted a randomized field experiment with a service provider above the trust tipping point (Study 2) to corroborate the findings of the online experiment in a setting with high ecological validity and generalizability. In the following, we first present the online experiment (Study 1) and then the field experiment (Study 2).

## 5 Study 1: Online Experiment

To empirically test H1 and H2, we conducted a 2 (website baseline trustworthiness: below vs. above the trust tipping point) × 2 (IS certification: absent vs. present) between-subject online experiment.

## 5.1 Experimental Procedure

Consistent with previous studies (e.g., Özpolat et al., 2013), the experimental procedure consisted of four steps (see Figure 3): (1) The participants read the experimental instructions. (2) We provided the participants with a short explanation about cloud services and informed them about their upcoming interaction with the website. (3) We randomly assigned participants to one of the four treatments and let them see and evaluate their first-time experience with the website. (4) We distributed a questionnaire to participants about their perceptions of the website and collected information relevant to controls and demographics.

![](/api/attachments/JWUTKKNN/fulltext/images/06b07bdca79dcdb94e1f1a5f85a3e484b478fb009b8d658420110f5d4b76bcdc.jpg)

Figure 3. Experimental Procedure: Study 1

## 5.2 Manipulation of the Independent Variables

To examine the role of a website’s baseline trustworthiness and the respective effect of IS certifications, we designed two websites that differed in their baseline trustworthiness (i.e., websites before adding supplementary IS certifications)—i.e., medium baseline trustworthiness (i.e., below the tipping point) and high baseline trustworthiness (i.e., above the tipping point). We first created a website based on a real but rather unknown cloud service website (i.e., www.backup-utility.com) and used 30 participants to pretest its perceived trustworthiness. The data revealed an average trustworthiness rating of 5.4 on a 7-point Likert-type scale, which is above the value of 4.43 and thus considered “high” (e.g., Pimentel, 2010; Pimentel & Pimentel, 2019), inferring that visitors on average trust the website (i.e., high trustworthiness). We used this website as the “above the tipping point” site and then adjusted it to create a website that was “below the tipping point.” We subsequently reduced the website’s baseline trustworthiness by changing and/or removing design elements that have been shown to significantly increase a website’s trustworthiness in prior research. We removed or altered (1) social proof in the form of user feedback mechanisms (e.g., Hsu et al., 2014; Pavlou & Gefen, 2004) and official website partners (e.g., Koufaris & Hampton-Sosa, 2004; Sia et al., 2009), (2) structural assurances in the form of first-party assurances (e.g., Gefen et al., 2003; Ou & Sia, 2010), and (3) website aesthetics in the form of the color scheme (e.g., Cyr et al., 2010) and human-like cues (e.g., Karimov et al., 2011; Lu et al., 2016). The resulting “below-the-tipping-point” website had a perceived baseline trustworthiness of 4.3. This value is not only significantly below the “high” baseline trustworthiness website with the value of 5.4 (Mann‒Whitney test, p < 0.05) but also below the value of 4.43, which is considered “neutral” in the literature (e.g., Pimentel, 2010; Pimentel & Pimentel, 2019).

![](/api/attachments/JWUTKKNN/fulltext/images/8bb796b532701e796a3d2585bb8dfce9b96141246dc119ff156bd178f342139b.jpg)

Figure 4. Experimental Conditions (Excerpt): Study 1

For the conditions in which the IS certification was present, we displayed the TRUSTe IS certification, which is highly regarded and used by diverse companies to guarantee the processing of sensitive data according to data protection regulations. Furthermore, TRUSTe is one of the most-used IS certifications in prior research (e.g., Kim et al., 2016; Löbbers et al., 2022). In the “IS certification absent” condition, participants only saw the website without the TRUSTe IS certification. Figure 4 above shows screenshots of the most relevant parts of the employed websites and related conditions.

## 5.3 Measurement

We used validated scales from the literature for all constructs and measured items using 7-point Likerttype scales ranging from strongly disagree (1) to strongly agree (7). We focused on the website’s perceived trustworthiness as our dependent variable and adapted 11 items from McKnight et al. (2002) to measure it, covering the most common beliefs of trustworthiness (i.e., benevolence, integrity, and competence), which have also been used to measure swift trustworthiness (e.g., Blomqvist & Cook, 2018; Robert et al., 2009).

Additionally, we measured demographics (i.e., participants’ age, gender, and education) and used control variables from the extant literature that we considered most influential. These demographics and control variables helped us account for unintended effects beyond our intended changes in perceived trustworthiness and allowed for more robust analyses. We adapted items for trusting disposition from Gefen (2000), service involvement from Zaichkowsky (1985), and certification knowledge from Flynn and Goldsmith (1999) to account for the potential effects of participants’ attributes that may have influenced perceptions of trustworthiness. Additionally, we accounted for website aesthetics from Loiacono et al. (2007) to consider the visual design elements that may have influenced perceptions of trustworthiness. See Table A2 in the Appendix for all items.

As manipulation checks, we asked participants whether they saw an IS certification on the website and, if so, what it was (i.e., no IS certification, TRUSTe, Norton Secured, McAfee Secure). While this check assured that the final sample only comprised participants who noticed the correct IS certification, the effect of the IS certification on a website’s trustworthiness requires deeper information processing by the individual participant and depends on whether the participant believes that such effortful processing is necessary. Additionally, we implemented an attention check to ascertain whether participants read each item carefully.

## 5.4 Sample Description and Controls

We recruited 240 participants from Amazon Mechanical Turk (AMT), a crowdsourcing platform that has established itself as a viable platform for behavioral research and experiments (Behrend et al., 2011). Research has demonstrated that the results of surveys using AMT respondents have high reliability and provide high-quality data (e.g., Behrend et al., 2011; Lowry et al., 2016). Additionally, AMT is a suitable platform to reach internet-savvy users; such users are adequate participants in our experimental setting because they are potential visitors to cloud service websites. We restricted participation to users with a high reputation (at least 95% approval ratings and at least 5,000 conducted tasks), which is sufficient to ensure high data quality (Goodman & Paolacci, 2017). Of those 240 participants, 49 failed our manipulation and/or attention check, leaving us with a final sample of 191 participants. This sample size exceeded the minimum sample size of 144, which we estimated by conducting a power analysis using G\*Power 3.1 (Faul et al., 2009) with the following parameter specifications: 2 × 2 groups, an effect size of 0.60, an α-level of 0.05, and a power level of 0.80 (Cohen, 1992). Each respondent took an average of 7 minutes and 32 seconds to participate and received \$1.50 as remuneration. Table A3a in the Appendix provides more information on the descriptive statistics of our conditions.

Several one-way ANOVAs confirmed the successful randomized assignment to different experimental conditions. We did not identify significant differences (p > 0.05) in the participants’ gender, age, education, certification knowledge, service involvement, trusting disposition, and website aesthetics between the treatment groups. Thus, the results support the assumption that these variables were about equally distributed across our experimental groups.

## 5.5 Reliability and Validity

As we adopted established constructs for our measurement, we conducted a confirmatory factor analysis (CFA) to test the instrument’s convergent and discriminant validity for the dependent variables (Levine, 2005). Tables A2 and A4 in the Appendix report the CFA results. Our constructs are above the recommended level of 0.70 (Nunnally & Bernstein, 1994) for both measures regarding high internal consistency (i.e., Cronbach’s alpha and composite reliability). Values for the average variance extracted (AVE) for each construct ranged from 0.80 to 0.97, exceeding the relevant threshold of 0.50 (Hair et al., 2016). All items fulfilled the minimum loading requirements between the item and its corresponding underlying factor. Thus, all constructs met the norms for convergent validity. In addition, for satisfactory discriminant validity, the square root of the AVE from the constructs was greater than the variance shared between the construct and other constructs in the model (Fornell & Larcker, 1981). Additionally, the heterotraitmonotrait ratio of correlations (Henseler et al., 2015; Voorhees et al., 2016) was less than the threshold value of 0.85 for all constructs, indicating no discriminant validity problems. Therefore, the constructs in our study are both theoretically and empirically distinguishable.

## 5.6 Hypothesis Testing

We conducted ANOVAs to compare the effect of IS certification on the website’s trustworthiness across the four different conditions. The results in Figure 5 support the assertion that (1) the IS certification significantly increases the website’s trustworthiness if the website’s baseline trustworthiness is below the trust tipping point (p < 0.01) and (2) the IS certification does not significantly increase the website’s trustworthiness if its baseline trustworthiness is above the trust tipping point $( p > 0 . 1 )$ .

To further test our hypotheses with controls, we conducted a series of hierarchical linear regressions on the dependent variable trustworthiness (see Table 1). We therefore first entered all controls (Block 1) and then inserted our manipulation IS certification (i.e., 0 = absent, 1 = present) in the regression analyses (Block 2). We did this independently for the two websites below and above the trust tipping point.

As demonstrated in Table 1, IS certification had a significant effect $( \beta = 0 . 5 5 , p < 0 . 0 1 )$ ) on trustworthiness when the website’s baseline trustworthiness was below the trust tipping point, supporting H1. However, IS certification had no significant effect $( \beta ~ = ~ 0 . 1 6 ,$ p > 0.05) on trustworthiness when the website’s baseline trustworthiness was above the trust tipping point, in line with H2. These findings support our hypotheses that IS certifications have different effects below and above the trust tipping point.

![](/api/attachments/JWUTKKNN/fulltext/images/fc3bba10a695331efe388dcfa0f8b9da3b9128155e120f6b350b54ff9849cd88.jpg)  
Figure 5. Website’s Trustworthiness across the Four Conditions: Study 1

Table 1. Linear Regression Analyses: Study 1

<table><tr><td rowspan="3"></td><td colspan="4">Perceived trustworthiness: below the trust tipping point</td><td colspan="4">Perceived trustworthiness: above the trust tipping point</td></tr><tr><td colspan="2">Block 1</td><td colspan="2">Block 2</td><td colspan="2">Block 1</td><td colspan="2">Block 2</td></tr><tr><td>Coefficient</td><td>Std. error</td><td>Coefficient</td><td>Std. error</td><td>Coefficient</td><td>Std. error</td><td>Coefficient</td><td>Std. error</td></tr><tr><td>Intercept</td><td>1.35*</td><td>0.66</td><td>1.00</td><td>0.64</td><td>0.73</td><td>0.56</td><td>0.63</td><td>0.58</td></tr><tr><td colspan="9">Manipulation</td></tr><tr><td>IS Certification</td><td></td><td></td><td>0.55**</td><td>0.19</td><td></td><td></td><td>0.16</td><td>0.17</td></tr><tr><td colspan="9">Controls</td></tr><tr><td>Age</td><td>-0.00</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td></tr><tr><td>Gender</td><td>-0.17</td><td>0.21</td><td>-0.14</td><td>0.20</td><td>0.24</td><td>0.18</td><td>0.231</td><td>0.18</td></tr><tr><td>Education</td><td>-0.02</td><td>0.07</td><td>-0.03</td><td>0.07</td><td>-0.08</td><td>0.06</td><td>-0.08</td><td>0.06</td></tr><tr><td>Certificate knowledge</td><td>0.14*</td><td>0.06</td><td>0.12</td><td>0.06</td><td>0.15*</td><td>0.06</td><td>0.14*</td><td>0.06</td></tr><tr><td>Service involvement</td><td>0.19**</td><td>0.07</td><td>0.21**</td><td>0.07</td><td>0.09</td><td>0.07</td><td>0.10</td><td>0.07</td></tr><tr><td>Trusting disposition</td><td>0.14</td><td>0.08</td><td>0.14</td><td>0.07</td><td>0.22*</td><td>0.08</td><td>0.23*</td><td>0.08</td></tr><tr><td>Website aesthetics</td><td>0.30***</td><td>0.06</td><td>0.30***</td><td>0.06</td><td>0.40***</td><td>0.08</td><td>0.39***</td><td>0.08</td></tr><tr><td> $R^2$ </td><td>0.44</td><td></td><td>0.48</td><td></td><td>0.58</td><td></td><td>0.58</td><td></td></tr><tr><td>Adjusted  $R^{2}$ </td><td>0.40</td><td></td><td>0.44</td><td></td><td>0.54</td><td></td><td>0.54</td><td></td></tr></table>

While we first looked separately at the effects of IS certification on trustworthiness for the two websites, we subsequently performed a multigroup analysis (Garson, 2016) to gain deeper statistical insights into the differences between these websites. Comparing the coefficients for both websites further demonstrated a marginally significant difference in the effects of IS certification on trustworthiness between the groups (p < 0.1). This result supports the assertion that the effect of IS certifications differs for websites above and below the trust tipping point.

## 6 Study 2: Randomized Field Experiment

## 6.1 Purpose

We note that the online experiment in Study 1 was characterized by high internal validity (including controls) but was constrained in ecological validity. We sought to address this limitation in Study 2, corroborating the high internal validity of the controlled online experiment with the high ecological validity of a randomized field experiment. As such, the randomized field experiment took place in a real-life and externally valid setting in which contemporary IS certifications are embedded in websites and in which we had a large sample of self-involved users.

Overall, Study 1 and Study 2 aimed to investigate the effectiveness of IS certifications above the trust tipping point (H2). Since common scholarly knowledge generally reflects the assumption that IS certifications are effective (e.g., Lansing et al., 2018; Özpolat et al., 2013), investigating the ineffectiveness of IS certifications above the trust tipping point is the more interesting hypothesis to further corroborate and is thus the focus of Study 2.

## 6.2 Context

We collaborated with Qualifyze (www.qualifyze.com), a European service provider in a business-to-business (B2B) context. This service provider increases transparency and safety across the pharmaceutical supply chain by providing its visitors (i.e., representatives of pharmaceutical companies) with access to an extensive network of qualified auditors. Visitors usually arrive at the service provider’s website via a Google search for audit services. On the website, they can request supplier audits in just a few clicks and purchase these audits after registration, sharing the same audits with several users and thus reducing the audit burden for suppliers and users. Data integrity, cybersecurity, and a holistic service approach are at the forefront of everything the service provider does.

Thanks to our collaboration, we received proprietary access to a setting that is particularly interesting and relevant for research and practice involving the application of IS certifications: (1) The service provider offers audits of and for other companies in a B2B setting, meaning that its business heavily depends on the use of trustworthiness to attract users (e.g., McKnight et al., 2017), making it a specifically interesting case for the application of IS certifications. (2) Visitors are experts in the field of audits, making them familiar with the presented IS certification. (3) Visitors are highly involved because if they decide to purchase from this service provider, they have to spend several thousand euros for an audit and have a real task that requires a service that fits. Nevertheless, since they are expected to make user registration decisions largely on the spot (Häubl & Murray, 2003; Payne et al., 1992), website design elements are expected to influence their decisions. Moreover, visitors in our sample were unaware of our study while making reallife decisions with real financial consequences for them and the service provider. On average, within the first year, every registered user buys five audits at between €2,300 and €2,700 per audit, resulting in an average revenue of €12,500 per registration.

## 6.3 Experimental Design and Procedure

After several workshops with its existing users on how to improve the website design, the service provider decided to test how user registrations change when adding an IS certification to the website. Together with the service provider, we chose the ISO 9001 certification, a standard for quality management systems that helps service providers meet users’ and other stakeholders’ needs within statutory and regulatory requirements related to services (Poksinska et al., 2002). We chose this IS certification because it is the most issued ISO certification, with more than 1 million valid certificates worldwide (ISO, 2022), and has frequently been analyzed in past research (Lins et al., 2022). Overall, the service provider conducted a between-subject design (IS certification: absent vs. present) in a field experiment to isolate the distinct effects of IS certifications.

Visitors participated in an initial visitor-provider encounter in which the service provider attempted to turn visitors into registered users through a registration process. Consistent with previous studies on IS certifications (e.g., Özpolat et al., 2013), the experimental procedure consisted of an interaction with one of two possible websites (see Figure 6):

1. The visitor landed on the website and was randomly assigned to one of the two experimental conditions. The visitor became familiar with the unknown website.

2. The visitor searched for an existing audit using the website’s functions.

3. The visitor saw the requested audit in a pop-up window that had the design of one of the experimental conditions in Step 1. Visitors first had to register with their company email address to access and purchase an audit. Consistent with previous studies on information elicitation and frequent application in practice, we designed user registration so that users had to provide their commercial email address in a pop-up window to register. Without this registration, users could only search and see whether a recent audit for a selected company existed but could not see the exact details (e.g., specifications) or purchase the respective audit.

4. The visitor repeated Steps 2 and 3 and was thus exposed to the same pop-up designs until they had seen and evaluated enough audits, resulting in either a registration allowing them to purchase the requested audits or their departure from the website. After registration, the visitor (now user) was contacted by a service provider employee with information to enable access to the available audits.

## 6.4 Website and Manipulation Designs

We conducted a pretest to examine whether visitors perceive the website as trustworthy and regard it as above their trust tipping point. We replicated the website and asked 29 participants from the crowdworking platform Prolific.com to evaluate its trustworthiness (i.e., the baseline trustworthiness before adding supplementary IS certification). All participants were required to have a background in audits for pharmaceutical companies to reflect the actual visitors to the website, and they browsed the website for at least three minutes before evaluating it. The data revealed an average “high” trustworthiness value of 5.4, which is above the suggested value of 4.43, allowing us to infer that the average visitor trusts the website (e.g., Pimentel, 2010; Pimentel & Pimentel, 2019). We thus found that support for the website was adequate for our above-the-trust-tippingpoint investigation.

The presentation and saliency of the IS certification were based on practices commonly used on websites that focus on information elicitation. Figure 7 depicts the characteristics of the two conditions in our study. In Condition 1, the control condition (i.e., IS certification absent), the pop-up only displayed rudimentary information about the audits. In condition 2 (i.e., IS certification present), we added the ISO 9001 certification to the design of the popups in the control condition.

IS Certification  
![](/api/attachments/JWUTKKNN/fulltext/images/9d5ba2b00153d9099a04374e5ef5069b1f9a0bf48d86b23b382871e11c2eb4f6.jpg)  
Figure 6. Experimental Procedure: Study 2

![](/api/attachments/JWUTKKNN/fulltext/images/fd2fc3136ffebf800c9b7304ca5537c18177a2dfb2d759a68a3b70400fb4ae1c.jpg)  
Figure 7. Experimental Conditions: Study 2

## 6.5 Dependent Variable: User Registration

We measured user registration (i.e., swift trust-related behavior) as a binary variable in the form of a point estimator P:

$$
P (u s e r r e g i s t r a t i o n) = \frac {\sum_ {k = 1} ^ {n} x _ {k}}{n}
$$

where n denotes the total number of unique visitors in the respective condition who searched for at least one audit and were thus exposed to a treatment at least once, and $x _ { k }$ is a binary variable that equals 1 when the visitor registered (i.e., becoming a registered user) by providing a genuine email address and 0 otherwise.

We determined the provision of a genuine email address by sending a verification email to the entered email address and assessing the existence of the toplevel domain. Thus, we only included genuine email addresses in the main analyses, as only genuine email addresses are of value for service providers and can thus be considered a success indicator for IS certifications.

## 6.6 Sample Description

We recorded all variables via clickstream analysis during the entirety of the experiment in the spring of 2020. A total of 3,683 visitors with a unique IP address reached the website during that period. Of those, 306 (8.3%) searched for audits and were thus exposed to one of our experimental conditions at least once. This sample size exceeded the minimum sample size of 72, which we calculated in a power analysis using G\*Power 3.1 (two groups, effect size of 0.6, α-level of 0.05, and power level of 0.8) (Cohen, 1992; Faul et al., 2009). As every visitor reflected, on average, an opportunity for €12,500 in additional revenue for a successful registration, the entire field experiment of those 306 visitors represented a sales setting with a potential sales volume of up to €4 million. Of those 306 visitors, 44 (14.4%) registered on the website. Since all provided email addresses were genuine, no further differentiation was meaningful. Furthermore, no departing visitors returned to the website within the time frame of the experiment, and users who were already registered were not included in the sample. Table 2 provides details of the descriptive statistics of the analyzed data set.

## 6.7 Results

To further substantiate our findings regarding H2, we conducted a binary logistic regression on the dependent variable user registration and investigated the effect of IS certification (i.e., 0 = absent, 1 = present) above the trust tipping point while controlling for the number of exposures (i.e., the number of popups including the experimental treatments that a visitor was assigned to) and extrinsic product cues (i.e., 0 = absent, 1 = present), that is, whether the website additionally displayed other cues (e.g., service information) that may have influenced the user registration decision.

The results in Table 3 support the assertion that IS certification does not significantly increase the likelihood of eliciting user registration (p > 0.1) if the baseline trustworthiness is above the trust tipping point, providing additional support for H2, in that IS certifications have no significant effect on user registrations when the website’s baseline trustworthiness is above the trust tipping point. We also conducted a Mann-Whitney nonparametric test (Field, 2017), which demonstrated similar results (p > 0.1) and thus the robustness of our findings.

Table 2. Descriptive Statistics: Study 2

<table><tr><td>Condition</td><td>N</td><td>Conversion rate</td></tr><tr><td>1: IS Certification absent</td><td>173</td><td>15.6%</td></tr><tr><td>2: IS Certification present</td><td>133</td><td>12.8%</td></tr></table>

Table 3. Binary Regression Analysis: Study 2

<table><tr><td rowspan="2"></td><td colspan="3">User registration</td></tr><tr><td>Coefficient</td><td>Std. error</td><td>Exp (B)</td></tr><tr><td>Intercept</td><td>-2.21***</td><td>0.32</td><td>0.11</td></tr><tr><td colspan="4">Manipulation</td></tr><tr><td>IS certification</td><td>-0.26</td><td>0.35</td><td>0.77</td></tr><tr><td colspan="4">Control</td></tr><tr><td>Exposures</td><td>0.02*</td><td>0.01</td><td>1.02</td></tr><tr><td>Extrinsic product cues</td><td>0.63+</td><td>0.36</td><td>1.89</td></tr><tr><td>Nagelkerke&#x27;s  $R^2$ </td><td>0.04</td><td></td><td></td></tr><tr><td>-2 (log-likelihood)</td><td>245.45</td><td></td><td></td></tr><tr><td>Omnibus-tests  $\chi^2$ </td><td>6.56+</td><td></td><td></td></tr><tr><td colspan="4">Note: N = 306. +p &lt; 0.1, *p &lt; 0.05, **p &lt; 0.01, ***p &lt; 0.001</td></tr></table>

## 7 Discussion

This article was motivated by inconsistent findings in the literature on whether and how IS certifications influence a website’s trustworthiness and the related likelihood of user registrations if a website’s baseline trustworthiness is below versus above the trust tipping point. Our results show that an IS certification significantly increases the trustworthiness of a website and thus the likelihood of user registrations if its baseline trustworthiness is below (but not above) the trust tipping point.

## 7.1 Contributions to Research

We contribute to research on IS certifications by providing a revelatory explanation of the (in)effectiveness of IS certifications for users’ perceptions of trustworthiness and related user onboarding outcomes. Previous literature on IS certifications has been overly reliant on the assumption that IS certifications are unconditionally effective at increasing trustworthiness (e.g., Kim et al., 2008; Löbbers & Siegfried, 2018; McKnight et al., 2002). Specifically, researchers have studied whether IS certifications increase trustworthiness via A/B tests where the absence and presence of IS certifications have been investigated (e.g., McKnight et al., 2004; Özpolat et al., 2013). This view overlooks potential contextual factors that impact IS certification effectiveness, resulting in calls for further research to solve the puzzle of certification effectiveness (e.g., Kim, 2008; Kim et al., 2008; Lansing et al., 2018; Löbbers & Benlian, 2019). Our article aligns with recent certification research examining how users cognitively process and interpret IS certifications in more detail. Related studies have revealed, for example, that users’ perceptions of an IS certification are influenced by their personality traits (Löbbers & Benlian, 2019), their culture (Kim et al., 2016), and their perceptions of the certification’s structural elements (Lansing et al., 2018). We extend these research findings by emphasizing the importance of investigating IS certifications while accounting for a website’s baseline trustworthiness. In this vein, we reveal that the effects of IS certifications do not occur in a vacuum and that researchers must consider a website’s baseline trustworthiness when evaluating the effectiveness of IS certifications. This perspective is important because it provides a more comprehensive explanation of the contingent effects of IS certifications on websites. This helps researchers understand that failures to identify the effect of an IS certification may not result from the design and choice of the IS certification but from the design of the website on which the IS certification is displayed and, specifically, whether visitors already deem the website trustworthy enough before processing the IS certification.

With the notion of humans as cognitive misers, we offer the perspective that visitors tend to appreciate IS certifications only when they are relevant to their decision to trust the website. Our findings thereby advance prior research on IS certifications (e.g., Lins et al., 2023; Lowry et al., 2012; Yang et al., 2006) by revealing that the processing of IS certifications follows a cognitive-efficient logic. We show that visitors pay attention to and then process IS certifications only if certifications signal a significant gain toward resolving their concerns related to the website. However, if visitors perceive a website’s baseline trustworthiness as already trustworthy enough, they do not waste mental effort on further processing IS certifications. As such, our paper contributes by identifying a mechanism that switches on or off a visitor’s motivation to process information in the form of IS certifications. Our insights thus suggest that researchers should consider how visitors actually process IS certifications to increase the predictive power of research models on certification effectiveness. By providing support for the existence of a tipping point in a laboratory and field experiment, we reconcile inconsistent findings of past research on IS certifications and complement research focusing on moderating (e.g., Löbbers & Benlian, 2019; Lowry et al., 2012; Siegfried et al., 2020) and mediating effects (e.g., Hu et al., 2010; Lins et al., 2023), thus impacting linear certification effects.

In addition to our contributions to IS certification research, we also provide empirical evidence for the formation of swift trustworthiness in user onboarding in electronic markets. Particularly, we show that swift trustworthiness is not only an important facilitator for collaborations (Jarvenpaa et al., 1998; Meyerson et al., 1996) but also a crucial factor that visitors care about in the early stages of user onboarding. Moreover, we demonstrate that swift trustworthiness only increases until a tipping point and that trustworthiness is a necessary enabler for subsequent onboarding decisions—without which important visitor-website interactions would not occur. These insights increase our understanding of the applicability of swift trust to electronic markets and reveal that swift trustworthiness is not an ever-growing factor that indefinitely influences visitor-website interactions.

## 7.2 Implications for Practice

We also provide service providers with valuable lessons on whether and under which boundary conditions IS certifications are effective for the trustworthiness of websites and thus worth acquiring and displaying. In particular, the insights from our field experiment are valuable and useful because they are based on real visitor behaviors that go above and beyond the behavioral intentions examined in most previous studies on IS certifications. In fact, as a result of our cooperation with the service provider and our findings from the field experiment, the company removed the IS certification from the respective web pages because the costs of being allowed to display it on the website and those generated from changing and maintaining internal processes to adhere to its requirements (i.e., several thousand euros) did not pay off, as the baseline website was already above the trust tipping point. Indeed, the website with IS certification (user registration rate: 12.8%) performed slightly worse than the website without IS certification (user registration rate: 15.6%). Beyond the revelation for this specific service provider, these insights can be generalized and applied to other websites and service providers.

For service providers who intend to improve their website design to achieve better user onboarding outcomes, we demonstrate that deploying IS certifications can be worthwhile but that they depend on the website’s baseline trustworthiness. Thus, our explanation of the role of the trust tipping point is also an easily actionable approach. For example, instead of assuming that IS certifications are always effective and displaying them whenever possible, service providers could conduct surveys and measure visitors expectations and the related (average) perceived baseline trustworthiness of their website and ask visitors whether they perceive the website to be as trustworthy as similar websites (i.e., their reference point). Based on the responses and numbers of visitors who find the website above the trust tipping point, service providers could then decide whether displaying an IS certification is worthwhile or whether they should focus instead on displaying other cues (e.g., related to the attributes of the product or service). Indeed, once the trust tipping point is surpassed for a critical number of users, any additional trust signal is an inefficient use of scarce website space and the service provider’s resources (e.g., monetary investments and effort to comply with IS certifications). If service providers intend to focus on more universally applicable design elements that are effective irrespective of the trust tipping point, they should focus on other design elements, such as those contributing to website aesthetics (as the control variable in our online experiment implicitly indicates). Nevertheless, we emphasize that even if service providers decide not to display IS certifications on their websites, they still need to comply with the rules underlying the acquisition of IS certifications and thus refrain from ethical misconduct, which could harm the business and the visitor-website relationship in the long run.

## 7.3 Limitations and Future Research

This study has some limitations, which provide several avenues for future research. First, the article is an initial empirical investigation into the explicit relationship between IS certifications and swift trust theory. We sought to move beyond predominantly positive views on IS certifications to explain the inconsistent findings in past research from a new perspective. Future studies could further develop and evaluate this new perspective by evaluating, for example, whether the findings are valid with different IS certifications (beyond TRUSTe and ISO 9001) as well. As we were not able to control for the successful randomization of participants in field experiments due to missing data (e.g., demographics), future research could also replicate and extend our field findings by conducting similar analyses with a secured equal distribution of participants’ traits across conditions (e.g., through stratified randomization), could perform robustness checks with additional variables to account for possible selection bias, and could even analyze the effects of participants’ traits for potential moderation. Moreover, since trust tipping is highly dependent on visitors’ individual expectations and related perceptions, the context of websites and the individual differences of visitors will determine how much trustworthiness visitors expect. For instance, a shopping website may have a lower (average) trust tipping point than an online banking website due to much higher investment amounts and the related expectations and reference points of visitors. Consequently, future research could investigate the effects of IS certifications in more extreme cases of the trust tipping point (e.g., very low or very high) to enhance the robustness of our approach and reveal the importance of the application context in the effectiveness of IS certifications. For instance, if a website’s baseline trustworthiness is far below the trust tipping point, an IS certification may also not have a positive effect because visitors may have given up on processing any information on the website, including IS certifications. Accordingly, within-subject experiments (e.g., exposure of one individual to several websites of different IS certification-related designs) may be worthwhile to account for individual differences in the effectiveness of IS certifications.

Second, and more broadly, the tipping point concept may also apply to explain the effectiveness of other trust signals and constructs beyond IS certifications. Consequently, researchers may wish to examine other trust signals (e.g., star ratings), context-dependent constructs and related tipping points (e.g., privacy concerns, risk, and distrust), and the website trustworthiness level at which they are employed. In this vein, it would also be interesting to investigate whether there is a difference in the trustworthiness of websites when separating trust in people (e.g., benevolence) and trust in technology (e.g., reliability). Furthermore, trustworthiness and the related trust tipping point may also be investigated regarding its emotional components as well as its cognitive components. Finally, the investigation of more decisions and user onboarding outcomes (e.g., purchases, product returns, complaints) may be a fruitful avenue for future research. Such research endeavors would allow researchers and practitioners to generate a better understanding of the effectiveness of IS certifications in various website environments.

## 8 Conclusion

Prior research on IS certifications has been overly reliant on the presumption that these certifications are universally effective. This perspective limits the understanding of their effectiveness in that these certifications are implicitly assumed to be independent of a website’s baseline trustworthiness (i.e., before adding supplementary IS certifications), resulting in inconclusive findings on their effectiveness. The purpose of our article was to reconcile these inconclusive findings by departing from the linear and unconditional effects of IS certifications. Drawing on the notion of humans as cognitive misers and swift trust theory, we tested our assertions using a multimethod investigation through the complementary properties of an online and a randomized field experiment. The results consistently indicate that an IS certification is significantly effective when a website’s baseline trustworthiness is below (but not above) the trust tipping point. These findings have strong implications for understanding the (in)effectiveness of IS certifications on perceptions of trustworthiness and user onboarding outcomes. They not only explain the effectiveness of IS certifications from a novel perspective but also equip practitioners with valuable guidance on deploying IS certifications.

## Acknowledgments

The authors gratefully acknowledge funding support from the German Research Foundation (DFG) as part of the project “A Decompositional Analysis of IT Certifications in Electronic Markets and their Impact on Customer and Platform Provider Perceptions” (project number 327130595). In addition, the authors would like to thank the senior editor and the anonymous reviewers for their valuable comments and suggestions to improve this paper.

## References

Abbasi, A., Zahedi, F. M., Zeng, D., Chen, Y. Chen, H., & Nunamaker Jr., J. F. (2015). Enhancing predictive analytics for anti-phishing by exploiting website genre information. Journal of Management Information Systems, 31(4), 109-157.

Adam, M., Roethke, K., & Benlian, A. (2024). Human versus automated sales agents: How and why customers responses shift across sales stages. Information Systems Research, 34(3), 1148- 1168

Aiken, K. D., & Boush, D. M. (2006). Trustmarks, objective-source ratings, and implied investments in advertising: Investigating online trust and the context-specific nature of internet signals. Journal of the Academy of Marketing Science, 34(3), 308-323.

Al-Natour, S., Cavusoglu, H., Benbasat, I., & Aleem, U. (2020). An empirical investigation of the antecedents and consequences of privacy uncertainty in the context of mobile apps. Information Systems Research, 31(4), 1037- 1063.

Behrend, T. S., Sharek, D. J., Meade, A. W., & Wiebe, E. N. (2011). The viability of crowdsourcing for survey research. Behavior Research Methods, 43(3), 800.

Benlian, A., Titah, R., & Hess, T. (2012). Differential effects of provider recommendations and consumer reviews in e-commerce transactions: An experimental study. Journal of Management Information Systems, 29(1), 237-272.

Blomqvist, K., & Cook, K. S. (2018). Swift trust: State-of-the-art and future research directions. In R. H. Searle, A-M. I. Nienaber, S. B. Sitkin (Eds.), The Routledge companion to trust (pp. 29-49). Routledge.

Clemons, E. K. et al. (2016). Global differences in online shopping behavior: Understanding factors leading to trust. Journal of Management Information Systems, 33(4), 1117-1148.

Cohen, J. (1992). Quantitative methods in psychology: A power primer. Psychological Bulletin, 112(1), 155-159.

Cohen, J. B., & Reed, A. (2006). A multiple pathway anchoring and adjustment (MPAA) model of attitude generation and recruitment. Journal of Consumer Research, 33(1), 1-15.

Cyr, D., Head, M., & Larios, H. (2010). Colour appeal in website design within and across cultures: A

multi-method evaluation. International Journal of Human-Computer Studies, 68(1-2), 1-21.

Dimoka, A. (2010). What does the brain tell us about trust and distrust? Evidence from a functional neuroimaging study. MIS Quarterly, 34(2), 373-396.

Faul, F., Erdfelder, E., Buchner, A., & Lang, A.-G. (2009). Statistical power analyses using g\* power 3.1: Tests for correlation and regression analyses. Behavior Research Methods, 41(4), 1149-1160.

Feldman, J. M., & Lynch, J. G. (1988). Self-generated validity and other effects of measurement on belief, attitude, intention, and behavior. Journal of Applied Psychology, 73(3), 421-435.

Field, A. (2017). Discovering statistics using IBM SPSS statistics. SAGE.

Fink, L. (2022). Why and how online experiments can benefit information systems research. Journal of the Association for Information Systems, 23(6), 1333-1346.

Fisher, R., & Zoe Chu, S. (2009). Initial online trust formation: The role of company location and web assurance. Managerial Auditing Journal, 24(6), 542-563.

Flynn, L. R., & Goldsmith, R. E. (1999). A short, reliable measure of subjective knowledge. Journal of Business Research, 46(1), 57-66.

Fornell, C., & Larcker, D. F. (1981). Evaluating structural equation models with unobservable variables and measurement error. Journal of Marketing Research, 18(1), 39-50.

Garson, G. D. (2016). Partial least squares: Regression and structural equation models. Statistical Associates Publishers.

Gefen, D. (2000). E-commerce: The role of familiarity and trust. Omega, 28(6), 725-737.

Gefen, D. (2004). What makes an ERP implementation relationship worthwhile: Linking trust mechanisms and ERP usefulness. Journal of Management Information Systems, 21(1), 263- 288.

Gefen, D., Karahanna, E., & Straub, D. W. (2003). Trust and TAM in online shopping: An integrated model. MIS Quarterly, 27(1), 51-90.

Gerlach, J., Buxmann, P., & Dinev, T. (2019). “They’re all the same!” stereotypical thinking and systematic errors in users’ privacy-related judgments about online services. Journal of the Association for Information Systems, 20(6), 787-823.

Goodman, J. K., & Paolacci, G. (2017). Crowdsourcing consumer research. Journal of Consumer Research, 44(1), 196-210.

Gozman, D., Butler, T., & Lyytinen, K. (2020). Call for papers for a special issue of the Journal of Information Technology on “Regulation in the Age of Digitalization.” Journal of Information Technology. https://journals.sagepub.com page/jin/call-for-papers

Hair, J. F., Hult, G. T. M., Ringle, C., & Sarstedt, M. (2016). A primer on partial least squares structural equation modeling (pls-sem). SAGE.

Häubl, G., & Murray, K. B. (2003). Preference construction and persistence in digital marketplaces: The role of electronic recommendation agents. Journal of Consumer Psychology, 13(1-2), 75-91.

Henseler, J., Ringle, C. M., & Sarstedt, M. (2015). A new criterion for assessing discriminant validity in variance-based structural equation modeling. Journal of the Academy of Marketing Science, 43(1), 115-135.

Hoffmann, C. P., Lutz, C., & Meckel, M. (2014). Digital natives or digital immigrants? The impact of user characteristics on online trust. Journal of Management Information Systems, 31(3), 138-171.

Hsu, M.-H., Chuang, L.-W., & Hsu, C.-S. (2014). Understanding online shopping intention: The roles of four types of trust and their antecedents. Internet Research, 24(3), 332-352.

Hu, X., Wu, G., Wu, Y., & Zhang, H. (2010). The effects of web assurance seals on consumers initial trust in an online vendor: A functional perspective. Decision Support Systems, 48(2), 407-418.

Huang, N., Mojumder, P., Sun, T., Lv, J., & Golden, J. M. (2021). Not registered? Please sign up first: A randomized field experiment on the ex ante registration request. Information Systems Research, 32(3), 914-931.

Huang, N., Sun, T., Chen, P., & Golden, J. M. (2019). Word-of-mouth system implementation and customer conversion: A randomized field experiment. Information Systems Research, 30(3), 805-818.

Hung, Y.-T., Dennis, A. R., & Robert, L. (2004). Trust in virtual teams: Towards an integrative model of trust formation. Proceedings of the 37th Annual Hawaii International Conference on System Sciences.

ISO (2022). The iso survey. https://www.iso.org/theiso-survey.html

Jarvenpaa, S. L., Knoll, K., & Leidner, D. E. (1998). Is anybody out there? Antecedents of trust in global virtual teams. Journal of Management Information Systems, 14(4), 29-64.

Jarvenpaa, S. L., Tractinsky, N., & Vitale, M. (2000). Consumer trust in an internet store. Information Technology and Management, 1(1), 45-71.

Karimov, F. P., Brengman, M., & Van Hove, L. (2011). The effect of website design dimensions on initial trust: A synthesis of the empirical literature. Journal of Electronic Commerce Research, 12(4), 272-301.

Kim, D., & Benbasat, I. (2009). Trust-assuring arguments in b2c e-commerce: Impact of content, source, and price on trust. Journal of Management Information Systems, 26(3), 175- 206.

Kim, D. J. (2008). Self-perception-based versus transference-based trust determinants in computer-mediated transactions: A crosscultural comparison study. Journal of Management Information Systems, 24(4), 13- 45.

Kim, D. J., Ferrin, D. L., & Rao, H. R. (2008). A trustbased consumer decision-making model in electronic commerce: The role of trust, perceived risk, and their antecedents. Decision Support Systems, 44(2), 544-564.

Kim, D. J., Yim, M.-S., Sugumaran, V., & Rao, H. R. (2016). Web assurance seal services, trust and consumers’ concerns: An investigation of ecommerce transaction intentions across two nations. European Journal of Information Systems, 25(3), 252-273.

Kim, K., & Kim, J. (2011). Third-party privacy certification as an online advertising strategy: An investigation of the factors affecting the relationship between third-party certification and initial trust. Journal of Interactive Marketing, 25(3), 145-158.

Koufaris, M., & Hampton-Sosa, W. (2004). The development of initial trust in an online company by new customers. Information & Management, 41(3), 377-397.

Lambrecht, A., Seim, K., & Tucker, C. (2011). Stuck in the adoption funnel: The effect of interruptions in the adoption process on usage. Marketing Science, 30(2), 355-367.

Lansing, J., Benlian, A., & Sunyaev, A. (2018). "Unblackboxing" decision makers' interpretations of is certifications in the context of cloud service certification. Journal of the

Association for Information Systems, 19(11), 1064-1096.

Lansing, J., Siegfried, N., Sunyaev, A., & Benlian, A. (2019). Strategic signaling through cloud service certifications: Comparing the relative importance of certifications’ assurances to companies and consumers. The Journal of Strategic Information Systems, 28(4), 1-23.

Levine, T. R. (2005). Confirmatory factor analysis and scale validation in communication research. Communication Research Reports, 22(4), 335- 338.

Levine, T. R., Park, H. S., & McCornack, S. A. (1999). Accuracy in detecting truths and lies: Documenting the “veracity effect.” Communications Monographs, 66(2), 125-144.

Lewicki, R. J., McAllister, D. J., & Bies, R. J. (1998). Trust and distrust: New relationships and realities. Academy of Management Review, 23(3), 438-458.

Li, X., Rong, G., & Thatcher, J. B. (2009). Swift trust in web vendors: The role of appearance and functionality. Journal of Organizational and End User Computing, 21(1), 88-108.

Lins, S., Becker, J.-M., Lyytinen, K., & Sunyaev, A. (2023). A design theory for certification presentations. The Data Base for Advances in Information Systems, 54(3), 75-118.

Lins, S., Kromat, T., Löbbers, J., Benlian, A., & Sunyaev, A. (2022). Why don’t you join in? A typology of information system certification adopters. Decision Sciences, 53(3), 452-485.

Liu, B. Q., & Goodhue, D. L. (2008). An exploration of the hygiene and motivator aspects of webqual constructs in predicting website reuse. Proceedings of the 41st Annual Hawaii International Conference on System Sciences.

Liu, B. Q., & Goodhue, D. L. (2012). Two worlds of trust for potential e-commerce users: Humans as cognitive misers. Information Systems Research, 23(4), 1246-1262.

Löbbers, J., & Benlian, A. (2019). The effectiveness of is certification in e-commerce: Does personality matter? Journal of Decision Systems, 28(3), 233-259.

Löbbers, J., Lins, S., Kromat, T., Benlian, A., & Sunyaev, A. (2020). A multi-perspective lens on web assurance seals: Contrasting vendors’ intended and consumers’ perceived effects. Electronic Commerce Research, 22, 1573- 1615.

Löbbers, J., Lins, S., Kromat, T., Benlian, A., & Sunyaev, A. (2022). A multi-perspective lens on web assurance seals: Contrasting vendors’ intended and consumers’ perceived effects. Electronic Commerce Research, 22, 1573-1615

Löbbers, J., & Siegfried, N. (2018). Toward a unified view of is certification: A structured literature review on theoretical lenses. Proceedings of the European Conference on Information Systems.

Loiacono, E. T., Watson, R. T., & Goodhue, D. L. (2007). Webqual: An instrument for consumer evaluation of web sites. International Journal of Electronic Commerce, 11(3), 51-87.

Lowry, P. B., D’Arcy, J., Hammer, B., & Moody, G. D. (2016). “Cargo cult” science in traditional organization and information systems survey research: A case for using nontraditional methods of data collection, including Mechanical Turk and online panels. The Journal of Strategic Information Systems, 25(3), 232-240.

Lowry, P. B. et al. (2012). Using an elaboration likelihood approach to better understand the persuasiveness of website privacy assurance cues for online consumers. Journal of the American Society for Information Science and Technology, 63(4), 755-776.

Lu, B., Fan, W., & Zhou, M. (2016). Social presence, trust, and social commerce purchase intention: An empirical research. Computers in Human Behavior, 56, 225-237.

Lynch, J. G., Marmorstein, H., & Weigold, M. F. (1988). Choices from sets including remembered brands: Use of recalled attributes and prior overall evaluations. Journal of Consumer Research, 15(2), 169-184.

Mavlanova, T., Benbunan-Fich, R., & Lang, G. (2016). The role of external and internal signals in ecommerce. Decision Support Systems, 87, 59- 68.

McKnight, D. H., & Chervany, N. L. (2001). What trust means in e-commerce customer relationships: An interdisciplinary conceptual typology. International Journal of Electronic Commerce, 6(2), 35-59.

McKnight, D. H., Choudhury, V., & Kacmar, C. (2002). The impact of initial consumer trust on intentions to transact with a web site: A trust building model. The Journal of Strategic Information Systems, 11(3-4), 297-323.

McKnight, D. H., Kacmar, C. J., & Choudhury, V. (2004). Shifting factors and the ineffectiveness of third party assurance seals: A two‐stage

model of initial trust in a web business. Electronic Markets, 14(3), 252-266.

McKnight, D. H., Lankton, N. K., Nicolaou, A., & Price, J. (2017). Distinguishing the effects of b2b information quality, system quality, and service outcome quality on trust and distrust. The Journal of Strategic Information Systems, 26(2), 118-141.

Meyerson, D., Weick, K. E., & Kramer, R. M. (1996). Swift trust and temporary groups. In R. M. Kramer & T. R. Tyler (Eds.), Trust in organizations: Frontiers of theory and research (pp. 166-195). SAGE.

Millar, M. G., & Millar, K. U. (1997). The effects of cognitive capacity and suspicion on truth bias. Communication Research, 24(5), 556-570.

Nunnally, J. C., & Bernstein, I. H. (1994). The assessment of reliability. Psychometric Theory,(3), 248-292.

Ou, C. X., & Sia, C. L. (2010). Consumer trust and distrust: An issue of website design. International Journal of Human-Computer Studies, 68(12), 913-934.

Özpolat, K., Gao, G., Jank, W., & Viswanathan, S. (2013). Research note—the value of third-party assurance seals in online retailing: An empirical investigation. Information Systems Research, 24(4), 1100-1111.

Özpolat, K., & Jank, W. (2015). Getting the most out of third party trust seals: An empirical analysis. Decision Support Systems, 73, 47-56.

Pavlou, P. A., & Gefen, D. (2004). Building effective online marketplaces with institution-based trust. Information Systems Research, 15(1), 37- 59.

Payne, J. W., Bettman, J. R., & Johnson, E. J. (1992). Behavioral decision research: A constructive processing perspective. Annual Review of Psychology, 43(1), 87-131.

Payne, J. W., Bettman, J. R., & Luce, M. F. (1996). When time is money: Decision behavior under opportunity-cost time pressure. Organizational Behavior and Human Decision Processes, 66(2), 131-152.

Pennington, R., Wilcox, H. D., & Grover, V. (2003). The role of system trust in business-toconsumer transactions. Journal of Management Information Systems, 20(3), 197-226.

Pimentel, J. L. (2010). A note on the usage of Likert scaling for research data analysis. USM R&D Journal, 18(2), 109-112.

Pimentel, J. L., & Pimentel, J. (2019). Some biases in Likert scaling usage and its correction. International Journal of Science: Basic and Applied Research, 45(1), 183-191.

Poksinska, B., Dahlgaard, J. J., & Antoni, M. (2002). The state of iso 9000 certification: A study of Swedish organizations. The TQM Magazine, 14(5), 297-306.

Rifon, N. J., LaRose, R., & Choi, S. M. (2005). Your privacy is sealed: Effects of web privacy seals on trust and personal disclosures. Journal of Consumer Affairs, 39(2), 339-362.

Robert, L. P., Denis, A. R., & Hung, Y.-T. C. (2009). Individual swift trust and knowledge-based trust in face-to-face and virtual team members. Journal of Management Information Systems, 26(2), 241-279.

Roethke, K., Klumpe, J., Adam, M., & Benlian, A. (2020). Social influence tactics in e-commerce onboarding: The role of social proof and reciprocity in affecting user registrations. Decision Support Systems, 131, 113268.

Schwarz, N., & Bohner, G. (2001). The construction of attitudes. In A. Tesser & N. Schwarz (Eds.), Blackwell handbook of social psychology: Intraindividual processes (pp. 436-457). Blackwell.

Sia, C. L. et al. (2009). Web strategies to promote internet shopping: Is cultural-customization needed? MIS Quarterly, 33(3), 491-512.

Siegfried, N., Winkler, N., & Benlian, A. (2020). Do bad experiences loom larger than good ones? The role of prior purchase experiences on the effectiveness of IS certifications. Journal of Decision Systems, 29(2), 79-101.

Simon, H. A. (1956). Rational choice and the structure of the environment. Psychological Review, 63(2), 129.

Sunyaev, A., & Schneider, S. (2013). Cloud services certification. Communications of the ACM, 56(2), 33-36.

Taylor, S. E. (1981). The interface of cognitive and social psychology. Cognition, Social Behavior, and the Environment, 1, 189-211.

TrustedShops (2020). Find secure online shops. https://www.trustedshops.co.uk/finder/

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124-1131.

Venkatesh, V., Thong, J. Y., Chan, F. K., & Hu, P. J. (2016). Managing citizens’ uncertainty in egovernment services: The mediating and

moderating roles of transparency and trust. Information Systems Research, 27(1), 87-111.

vom Brocke, J. et al. (2015). Standing on the shoulders of giants: Challenges and recommendations of literature search in information systems research. Communications of the Association for Information Systems, 37(1), 205-224.

Voorhees, C. M., Brady, M. K., Calantone, R., & Ramirez, E. (2016). Discriminant validity testing in marketing: An analysis, causes for concern, and proposed remedies. Journal of the Academy of Marketing Science, 44(1), 119-134.

Webster, J., & Watson, R. T. (2002). Analyzing the past to prepare for the future: Writing a literature review. MIS Quarterly, 26(2), xiiixxiii.

Wu, G., Hu, X., & Wu, Y. (2010). Effects of perceived interactivity, perceived web assurance and disposition to trust on initial online trust. Journal of Computer-Mediated Communication, 16(1), 1-26.

Wyer, R. S., & Srull, T. K. (1986). Human cognition in its social context. Psychological Review, 93(3), 322.

Xu, D. J., Benbasat, I., & Cenfetelli, R. T. (2017). A two-stage model of generating product advice: Proposing and testing the complementarity principle. Journal of Management Information Systems, 34(3), 826-862.

Xu, H., Teo, H.-H., & Tan, B. (2005). Predicting the adoption of location-based services: The role of trust and perceived privacy risk. Proceedings of the International Conference on Information Systems.

Yang, S. C., Hung, W. C., Sung, K., & Farn, C. K. (2006). Investigating initial trust toward etailers from the elaboration likelihood model perspective. Psychology & Marketing, 23(5), 429-445.

Zaichkowsky, J. L. (1985). Measuring the involvement construct. Journal of Consumer Research, 12(3), 341-352.

## Appendix

To take a more in-depth look at the inconsistent findings in the research and gather initial support for the existence of a trust tipping point, we conducted a literature review on the effects of IS certifications on trustworthiness. We followed the established procedures by Webster & Watson (2002) and vom Brocke et al. (2015) and inserted relevant search terms in scientific databases we deemed relevant (see Figure A1). Our initial search resulted in a set of 397 papers, which were then analyzed using the title, abstract, keywords, and content to filter those papers that would help us to pursue our research aim. We excluded 387 off-topic papers (e.g., not dealing with IS certifications and not analyzing the effect of IS certifications on trustworthiness). Subsequently, we conducted a forward and backward search and were able to identify an additional 12 papers, resulting in 22 papers in total. Lastly, we compared our outcome with the recent reviews on IS certifications (Löbbers et al., 2020; Löbbers & Siegfried, 2018) and found no additional papers.

![](/api/attachments/JWUTKKNN/fulltext/images/25e257284eeb8ccf61c47aeb04b6abc296af959405c8655caa9e3e0fde2cb9b8.jpg)  
Figure A1. Selection Process

Out of those 22 papers, we further removed eight that did not focus on trustworthiness (i.e., that focused only on trusting intentions). Thus, the final number of papers on the effects of IS certifications on trustworthiness was 14. Lastly, we looked at whether the papers indicated the website’s trustworthiness and whether the IS certification exhibited a significant effect on trustworthiness.

To summarize, 33% of all papers that investigated the effects of IS certifications on trustworthiness did not explicitly mention a trustworthiness mean. Moreover, in those papers that mentioned a trustworthiness mean, the data showed a rather consistent and striking pattern: Above a point that is somewhere between 4.6 and 5.0 for the perceived trustworthiness of an existing website, IS certifications did not seem to be significant. Although these findings on the trust tipping point cannot be statistically analyzed to provide significant findings due to the small sample size, these findings provided the initial tendencies and thus supported our assertion that an IS certification is dependent on the perceived trustworthiness of existing websites. Table A1 includes the papers that looked at the effect of IS certifications on trustworthiness and highlights the characteristics that are important for our paper, namely the trustworthiness mean and the significance of the used IS certifications.

Table A1. Literature Review on IS Certifications and Trustworthiness

<table><tr><td>Study</td><td>Trustworthiness (mean)</td><td>Significance of IS certifications</td></tr><tr><td>McKnight et al. (2004)</td><td>Not Available</td><td>Not Significant</td></tr><tr><td>Kim (2008)</td><td> $5.32^b$ </td><td>Not Significant</td></tr><tr><td>Kim et al. (2008)</td><td> $5.058^b$ </td><td>Not Significant</td></tr><tr><td>Kim &amp; Kim (2011)</td><td> $4.64^a$ </td><td>Significant</td></tr><tr><td>Fisher &amp; Zoe Chu (2009)</td><td> $4.015^a$ </td><td>Not Significant</td></tr><tr><td>Rifon et al. (2005)</td><td> $4.01^a$ </td><td>Significant</td></tr><tr><td>Hu et al. (2010)</td><td> $4^a$ </td><td>Significant</td></tr><tr><td>Aiken &amp; Boush (2006)</td><td> $3.82^{a,*}$ </td><td>Significant</td></tr><tr><td>Kim (2008)</td><td> $3.74^b$ </td><td>Significant</td></tr><tr><td>Gefen (2004)</td><td> $3.66^b$ </td><td>Significant</td></tr><tr><td>Gefen et al. (2003)</td><td> $3.15^b$ </td><td>Significant</td></tr><tr><td>Wu et al. (2010)</td><td>Not Available</td><td>Significant</td></tr><tr><td>Xu et al. (2005)</td><td>Not Available</td><td>Significant</td></tr><tr><td>Hoffmann et al. (2014)</td><td>Not Available</td><td>Significant</td></tr><tr><td>Mavlanova et al. (2016)</td><td>Not Available</td><td>Significant</td></tr><tr><td colspan="3">Note: $^a$ Visitors&#x27; average trustworthiness perceptions in the absence of the IS certification (if available). $^b$ Visitors&#x27; average trustworthiness perceptions calculated across all conditions (i.e., absence and presence of the IS certification)*Converted into a 7-point Likert-type scale</td></tr></table>

Table A2. Measurement Instruments: Study 1

<table><tr><td>Construct</td><td>Item (all 7-point Likert-type)</td></tr><tr><td>Trustworthiness (trusting beliefs)(McKnight et al., 2002)(α = 0.97, CR = 0.98, AVE = 0.80)</td><td>eBackupper is truthful in its dealings with me.I would characterize eBackupper as honest.eBackupper would keep its commitments.eBackupper is sincere and genuine.eBackupper is competent and effective in providing a cloud service.eBackupper performs its role of providing a cloud service very well.Overall, eBackupper is a capable and proficient Internet cloud service provider.In general, eBackupper is very knowledgeable about cloud computing.I believe that eBackupper would act in my best interests.If I required help, eBackupper would do its best to help me.eBackupper is interested in my well-being, not just its own.</td></tr><tr><td>Certificate knowledge(Flynn &amp; Goldsmith, 1999)(α = 0.97, CR = 0.98, AVE = 0.94)</td><td>I know pretty much about web seals like TRUSTe.I do NOT feel very knowledgeable about web seals like TRUSTe. (reversed)When it comes to web seals like TRUSTe, I really do NOT know a lot. (reversed)</td></tr><tr><td>Service involvement (Zaichkowsky, 1985)(α = 0.94, CR = 0.97, AVE = 0.94)</td><td>Cloud services are important to me.I am interested in cloud services.</td></tr><tr><td>Trusting disposition (Gefen, 2000)(α = 0.94, CR = 0.96, AVE = 0.86)</td><td>I generally trust other people.I generally have faith in humanity.I feel that people are generally well-meaning.I feel that people are generally trustworthy.</td></tr><tr><td>Website aesthetics (Loiacono et al., 2007)(α = 0.99, CR = 0.99, AVE = 0.97)</td><td>eBackupper is visually pleasing.eBackupper displays a visually pleasing design.eBackupper is visually appealing.</td></tr></table>

Table A3a. Descriptive Statistics: Study 1

<table><tr><td>Groups</td><td>N</td><td>Gender: female</td><td>Age (SD)</td><td>Education: mode degree</td><td>Certification knowledge (SD)</td></tr><tr><td>1: Below trust tipping point, IS certification absent</td><td>52</td><td>59.6%</td><td>39 (14)</td><td>University (44%)</td><td>3.86 (1.88)</td></tr><tr><td>2: Below trust tipping point, IS certification present</td><td>52</td><td>59.1%</td><td>39 (9)</td><td>University (34%)</td><td>4.00 (1.51)</td></tr><tr><td>3: Above trust tipping point, IS certification absent</td><td>44</td><td>61.5%</td><td>36 (15)</td><td>University (38%)</td><td>4.18 (1.40)</td></tr><tr><td>4: Above trust tipping point, IS certification present</td><td>43</td><td>55.8%</td><td>38 (13)</td><td>University (37%)</td><td>4.28 (1.69)</td></tr></table>

Table A3b. Descriptive Statistics: Study 1

<table><tr><td>Groups</td><td>N</td><td>Service involvement (SD)</td><td>Trusting disposition (SD)</td><td>Website aesthetics (SD)</td></tr><tr><td>1: Below trust tipping point, IS certification absent</td><td>52</td><td>5.13 (1.42)</td><td>4.77 (1.36)</td><td>4.18 (1.83)</td></tr><tr><td>2: Below trust tipping point, IS certification present</td><td>52</td><td>5.27 (1.21)</td><td>5.09 (1.41)</td><td>5.48 (1.20)</td></tr><tr><td>3: Above trust tipping point, IS certification absent</td><td>44</td><td>4.83 (1.57)</td><td>4.81 (1.32)</td><td>4.15 (1.85)</td></tr><tr><td>4: Above trust tipping point, IS certification present</td><td>43</td><td>4.77 (1.76)</td><td>4.71 (1.26)</td><td>5.64 (1.11)</td></tr></table>

Table A4. Construct Correlation Matrix: Study 1

<table><tr><td></td><td>1.</td><td>2.</td><td>3.</td><td>4.</td><td>5.</td><td>6.</td><td>7.</td><td>8.</td><td>9.</td></tr><tr><td>1. Age</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Gender</td><td>-0.11</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Education</td><td>0.05</td><td>-0.01</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Certification knowledge</td><td>-0.17*</td><td>0.20**</td><td>-0.042</td><td>0.97</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Service involvement</td><td>-0.00</td><td>0.05</td><td>0.018</td><td>0.25**</td><td>0.97</td><td></td><td></td><td></td><td></td></tr><tr><td>6. Trusting disposition</td><td>0.02</td><td>0.16*</td><td>0.012</td><td>0.28**</td><td>0.30**</td><td>0.93</td><td></td><td></td><td></td></tr><tr><td>7. Website aesthetics</td><td>0.09</td><td>-0.01</td><td>0.025</td><td>0.30**</td><td>0.21**</td><td>0.20**</td><td>0.99</td><td></td><td></td></tr><tr><td>8. IS certification</td><td>-0.09</td><td>0.00</td><td>0.028</td><td>0.09</td><td>-0.13</td><td>-0.06</td><td>0.01</td><td>-</td><td></td></tr><tr><td>9. Trustworthiness</td><td>0.01</td><td>0.08</td><td>-0.026</td><td>0.43**</td><td>0.40**</td><td>0.39**</td><td>0.58**</td><td>0.14</td><td>0.89</td></tr><tr><td colspan="10">Note: N = 191. * p &lt; 0.05 ** p &lt; 0.01. Bolded diagonal elements are the square root of AVE. These values should exceed interconstruct correlations (off-diagonal elements) for adequate discriminant validity</td></tr></table>

## About the Authors

Martin Adam is a chaired professor of information systems, specializing in smart services, at the University of Goettingen, Germany. His research interests include human-computer interaction as well as the digital transformation of work and people. His work has been published in various international journals, such as Journal of the Association for Information Systems, Information Systems Research, Information Systems Journal, European Journal of Information Systems, Decision Support Systems, Communications of the Association for Information Systems, Business & Information Systems Engineering, and Electronic Markets. He serves as an associate editor at Information Systems Journal, Business & Information Systems Engineering, and Electronic Markets.

Sebastian Lins is a postdoctoral researcher at the Research Group Critical Information Infrastructures (cii), Institute of Applied Informatics and Formal Description Methods, Karlsruhe Institute of Technology (KIT), Germany. He works on research challenges concerned with the design, use, and assessment of secure and trustworthy information systems. His main areas of work cover ensuring data protection and information security and performing (continuous) security assessments, thereby fostering trust in emerging technologies. His work has been published in international journals such as Information Systems Research, Journal of the Association for Information Systems, Electronic Markets, ACM SIGMIS Database, Decision Sciences, IEEE Transactions on Cloud Computing, and ACM Computing Surveys.

Ali Sunyaev is a professor of computer science at the Karlsruhe Institute of Technology (KIT), Germany. Before joining KIT, he was a professor at the University of Kassel and the University of Cologne. He received his PhD in information systems from the Technical University of Munich (TUM). His research work accounts for the multifaceted use contexts of digital technologies with research on human behavior affecting IT applications and vice versa. His research appeared in journals including Information Systems Research, Journal of Management Information Systems, Journal of Information Technology, Journal of the Association for Information Systems, IEEE Transactions on Cloud Computing, Communications of the ACM, and others

Alexander Benlian is a chaired professor of information systems, specializing in electronic services, at Darmstadt University of Technology (TU Darmstadt), Germany. He holds a PhD in business administration and management information systems from LMU Munich. His research interests include human-computer interaction, algorithmic management, digital transformation and IT entrepreneurship. His work has appeared in international journals such as MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Journal of the Association for Information Systems, Information Systems Journal, European Journal of Information Systems, Journal of Information Technology, The Journal of Strategic Information Systems, MIS Quarterly Executive, Journal of Service Research, European Journal of Operational Research, Entrepreneurship Theory & Research, Journal of Business Venturing, Decision Support Systems, Information & Management, Business & Information Systems Engineering, and several others. He is currently a senior editor of the European Journal of Information Systems and a department editor of Business & Information Systems Engineering and serves on the editorial review boards of Information Systems Research, MISQ Executive, and Electronic Markets.

Copyright © 2024 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
