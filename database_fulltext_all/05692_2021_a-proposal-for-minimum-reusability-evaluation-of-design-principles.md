---
otero_id: 5692
otero_key: "G2FD2M8J"
title: "A proposal for minimum reusability evaluation of design principles"
authors: "Juhani Iivari; Magnus Rotvit Perlt Hansen; Amir Haj-Bolouri"
year: "2021"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1793697"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A proposal for minimum reusability evaluation of design principles

Juhani Iivari , Magnus Rotvit Perlt Hansen & Amir Haj-Bolouri

To cite this article: Juhani Iivari , Magnus Rotvit Perlt Hansen & Amir Haj-Bolouri (2020): A proposal for minimum reusability evaluation of design principles, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1793697

To link to this article: https://doi.org/10.1080/0960085X.2020.1793697

![](/api/attachments/G2FD2M8J/fulltext/images/c423566982cc42e50603b64a1b078950059bf7bab14b3b6ea5b11504892351b4.jpg)

Published online: 21 Jul 2020.

![](/api/attachments/G2FD2M8J/fulltext/images/84706281dab7a75aac42995a6ae834786cb95d128d34bab4a0dd2cc5e866d05d.jpg)

Submit your article to this journal

![](/api/attachments/G2FD2M8J/fulltext/images/36123cf09ebdd0bf66979774245427d0c4763ba205e27ef9d47a13ce0f928f99.jpg)

Article views: 4

![](/api/attachments/G2FD2M8J/fulltext/images/18711ebf414b238f7e7e43942a04a8890574b03781036573fe7037120190740a.jpg)

View related articles

![](/api/attachments/G2FD2M8J/fulltext/images/d89972f4572adef1586b074c47f4c5f4583c1ba08ca60d92810b0886cfe7f95a.jpg)

View Crossmark data

ISSUES AND OPINION

Check for updates

# A proposal for minimum reusability evaluation of design principles

Juhani Iivari<sup>a</sup>, Magnus Rotvit Perlt Hansen<sup>b</sup> and Amir Haj-Bolouri<sup>c</sup>

<sup>a</sup>University of Oulu, Oulu, Finland; <sup>b</sup>Department of People and Technology, Roskilde University, Roskilde, Denmark; <sup>c</sup>University West, School of Business, Economics and IT,Department of Informatics, Trollhättan, Sweden

## ABSTRACT

Many Design Science Research (DSR) papers in Information Systems (IS) suggest sets of design principles (DPs) that provide knowledge for creating instances, in diferent contexts, of IT artefacts that belong to the same class. However, despite frameworks for evaluating DSR contributions, the evaluation of DP reusability to, with and for practitioners has been largely neglected. We suggest that in order to maintain the practical relevance of DSR, papers with DPs as their key outcomes should contain a reusability evaluation of the proposed principles. We propose a framework of minimum reusability evaluation of DPs by members of the target community of practitioners. The framework comprises five criteria: (1) accessibility, (2) importance, (3) novelty and insightfulness, (4) actability and guidance, and (5) efectiveness.

ARTICLE HISTORY Received 11 December 2018 Accepted 3 July 2020

ACCEPTING EDITOR Dov Te’eni

ASSOCIATE EDITOR Jan Leimeister

KEYWORDS Design Science Research; design principles; practica relevance; reusabilit evaluation; applicability check

## 1. Introduction

Design Science Research in Information Systems (ISDSR) is a research paradigm that is widely seen to have a potential to enhance the practical relevance of IS research (R. Baskerville et al., 2018; Hevner et al., 2004; Österle et al., 2011). To paraphrase Venable and Baskerville (2012), ISDSR can be defined as research that invents a new type of IT artefacts to address a type or class of problems and evaluates its utility in addressing specific problems of that type. According to Hevner et al. (2004), the objective of ISDSR is to help to develop technology-based solutions to important, relevant and heretofore unsolved business problems.

Despite the history of ISDSR of more than 50 years, its practical relevance is still a problem: a recent special issue of EJIS, for instance, called for exemplars of DSR papers with outcomes that can be applied to the solution of real-world problems (Pefers et al., 2018). Nowadays, leading IS journals have increasingly published DSR papers with sets of DPs as their major research outcomes. For example, of the seven papers accepted to the EJIS special issue, five reported outcomes of actual DSR, and three of them suggested DPs as their major contributions (Babaian et al., 2018; Coenen et al., 2018; Seidel et al., 2018). At the same time, concerns have been expressed about the lack of reusability evaluation of DPs by practitioners who are supposed to reuse them (Cronholm and Göbel 2018; Iivari et al., 2018). This lack does not imply that the principles – by necessity – are not reusable and useful, but the neglect of reusability evaluation increases the risk of publishing DPs that are not found applicable by practitioners and not useful in practice.

The purpose of this paper is to make a proposal for minimum reusability evaluation of DPs to be expected of DP papers submitted to leading IS journals. Following Chandra Kruse et al. (2016) and Cronholm and Göbel (2018), we interpret that the purpose of design principles (DPs) is to provide knowledge for creating in diferent context instances of IT artefacts that belong to the same type or class. Adopting this interpretation, we contend that DPs are primarily intended to be reused by practitioners who create (design) instances in question (cf. Chandra et al., 2015). These instances help practitioners deal with specific problems belonging to the class of problems addressed by the type of IT artefacts in question. Therefore, to serve their purpose, DPs should be reusable by practitioners.

One of the reviewers of this paper expressed his or her unease with the word “reusability”. We attempted to find a “better” term. Among the alternatives, we considered that “applicability” and especially “reapplicability” did sound the best. The Oxford English Dictionary defines “applicable” as “Capable of being applied or put to use” and “applicability” as “The quality of being applicable”. We wished to add the prefix “re” to underline that the DPs – as any knowledge – can be used without wear and tear. However, since the focus of this paper is in the use and reuse of DPs for creating instances of IT artefacts in the above meaning, we decided to stick to the term “reusability”.<sup>1</sup> We welcome a “better” term, if the ISDSR community is able to find or invent such and agree on it.

This is an Issues and Opinions paper, since we accept that there may be diferent opinions about the issue to whom DPs in ISDSR should be targeted. Some anonymous reviewers of this paper have claimed that DPs are and should be primarily written to fellow researchers in a similar way as results of ISBSR (Information Systems Behavioural Science Research) are communicated. In their view, the significance of DPs to practice is to be addressed as practical implications. Even though DPs often are inspired by practice (as assumed in Sein et al., 2011) and are ultimately targeted to practitioners (Markus et al., 2002; Sein et al., 2011; Chandra et al., 2015; Chandra Kruse et al., 2016, Cronholm and Göbel 2018), according to the above opposite view DPs cannot be written in a practitioner language without loss of something essential. However, expressing them in the esoteric “scientific” language easily makes them nuggets of scholarly discussion only, efectively excluding practitioners from that discourse. We also contend that emulating ISBSR is not promising from the viewpoint of the practical relevance of ISDSR. Although elite IS journals such as AIS Senior Editors’ Basket Eight journals have attempted to establish practical relevance of ISBSR through the “strong-theory-will-lead-topractical-implications” principle (Lyytinen et al., 2007), its practical relevance has been a constant concern at least for 20 years (Benbasat & Zmud, 1999; Robey & Markus, 1998). More specifically, Iivari et al. (2004), based on their analysis of articles in MIS Quarterly and Information Systems Journal published 1996–2000, reports that the practical relevance of practical implications proposed in those articles is modest at best. All this risks the practical relevance of ISDSR in reality. We consider it a big loss.

As an integral part of our proposal, we suggest a framework for light reusability evaluation of DPs. It is based on the framework of “applicability checks” of IS research from Rosemann and Vessey (2008) and adapted to the evaluation of DPs in the ISDSR context. Such adaptation is needed, since ISDSR difers from ISBSR. For example, practice may be well ahead of research in the case of ISDSR, as exemplified by the recent trend of agile software development (Ågerfalk & Fitzgerald, 2006).

In principle, our proposal is related to the recent works on evaluation in ISDSR. Prat et al. (2015) and Venable et al. (2016) provide reviews of this line of research. However, they do not specifically address evaluation of DPs, and compared with the latter, our proposal is novel in the sense that it is dificult to position it into the FEDS (Framework for Evaluation in Design Science Research) of Venable et al. (2016).

After having introduced and explained our proposal, we will contrast it with the two previous works on ISDSR evaluation.

We contend that our proposal is a clear step to increase researcher–practitioner interaction (Te’eni et al., 2017) in the context of ISDSR. It should be noted, however, that our proposal is intended to be adopted and used by ISDSR researchers as authors, reviewers, and editors of DP papers, rather than being adopted by practitioners.

The structure of this paper is as follows. First, we briefly summarise research on DPs and their reuse in ISDSR and suggest that DP papers should make explicit their target community of practitioners who are supposed to reuse the proposed DPs. The third section demonstrates the weak attention of reusability evaluation of DPs in DP papers published in leading IS journals. In the fourth section, we proceed to a framework for light reusability evaluation of DPs to aid and guide said evaluation by members of the target community. Our proposal is that it could serve as a standard for a light reusability evaluation of DPs required in DP papers. “Light” here is used as an alternative to “heavy” which would imply naturalistic, rigorous evaluation (Venable et al., 2016). The “light” evaluation could complement more theoretically oriented grounding (Goldkuhl, 2004; Heinrich & Schwabe, 2014) and precede more naturalistic and rigorous evaluation (Venable et al., 2016).

In the final section, we discuss the implications of the proposal. First, we contrast our framework with the frameworks for evaluation of ISDSR contributions (Prat et al., 2015; Venable et al., 2016). Second, we proceed to the implications of our light evaluation for researchers authoring ISDSR papers with DPs as major contributions, reviewers evaluating them, and editors deciding on their fate.

## 2. Design principles and their reuse

## 2.1. Design principles and their target community of practitioners

The concept of “design principle” has been gradually entered into the ISDSR literature (Gregor & Jones, 2007; Markus et al., 2002, Sein et al., 2011). Gregor and Hevner (2013) introduce DPs as generalised knowledge contributions in DSR to supplement constructs, methods, models, and instantiations (Hevner et al., 2004; March & Smith, 1995). For this paper, we adopt the definition made by Chandra Kruse et al. (2016) that the “purpose of DPs” is to provide “knowledge about creating (. . .) instances of IT artifacts that belong to the same class”. This means that DPs have been ”projected” by identifying the class of IT artefacts to which the set of DPs applies (Baskerville & Pries-Heje, 2014, 2019).

This paper uses the term “IT artefact” in a broad meaning covering, constructs, models, methods, design principles, and instantiations (Hevner et al., 2004; March & Smith, 1995; Vom Brocke et al., 2020). However, following Sein et al. (2011), Chandra Kruse et al. (2016) have instantiations in mind in the above definition of the purpose of DPs, when referring to IT artefacts. The instantiations may be either product instantiations or process instantiations (Chandra et al., 2015; Gregor & Jones, 2007). For simplicity and concreteness, this paper mainly focuses on the product instantiations.

We assume that it is normally practitioners who create the instances of the class of IT artefact, in question. This means that DPs are to be reused by practitioners and therefore should be reusable by them. This does not exclude that other audiences such as fellow researchers or students might be interested in the design knowledge represented by DPs and may also reuse them when instantiating artefacts in question. The idea of this paper is to focus on the reusability of DPs, not on the diferent interpretations of DPs and still less to take a normative stance of the most appropriate interpretation and formulation (see Cronholm and Göbel (2018), Gregor et al. (in press)). Since we are particularly worried about the practical relevance of ISDSR, our focus in this paper lies in practitioners and in the reusability of the proposed DPs.

The issue of reusability of DPs is not new. Already Markus et al. (2002) recognised it when questioning whether other development teams could follow the suggested design and development principles to produce successful systems (p. 207). However, Drechsler (2015) claims that the current ISDSR literature has neglected the audiences of its design artefacts. When considering the said audiences, he distinguishes “abstract socio-technical artifacts” and instantiated and contextualised “local socio-technical artifacts” and identifies a number of target audiences for the latter such as business executives, IT executives, business experts, IT experts, end-users, and consultants. He does not identify target audiences in more detail in the case of “abstract socio-technical artifacts” and does not identify DPs as a special category of artefacts.

Instead of proposing specific audience groups for DPs, our position is that the authors of DP papers should explicitly specify “the target community (or audience) of practitioners” (Te’eni et al., 2017), who are supposed to create instances of the class of IT artefacts in question and to reuse the principles when creating those instances. We use the word “practitioners” in the context of target community as a generic term that can be substituted by the name of the specific class of practitioners, the authors have in mind in their DP paper (e.g., “the target group of designers of requirements mining systems” in Meth et al. (2015)).

The target community of practitioners specifies the population from which the practitioners should be selected (“sampled”) and recruited to serve as informants, respondents, or participants (Prat et al., 2015) in the reusability evaluation of DPs.

## 2.2. Two types of IT product instantiations

As noted above, Drechsler (2015) distinguishes “abstract socio-technical artifacts” and instantiated and contextualised “local socio-technical artifacts”. He does distinguish two types of IT product instantiations, which we call “general instantiated IT meta-art efacts” and “specific/local instantiated IT applications”.<sup>2</sup> Both of them are concrete “material artefacts” (Jones & Jones, 2007). The conceptual separation between ERP software package and configurated and customised ERP-based information system illustrates the distinction between the two types of instantiations. The characterising adjectives – general vs. specific – come from Van Aken (2004) who separates “general solution concepts” and “specific solution concepts”, and distinction between “IT meta-art efacts” and “IT applications” from Iivari (2007).<sup>3</sup> The concept of meta-artefact emphasises that they are needed in or support the development and implementation of other artefacts and finally concrete instantiated IT applications (Drechsler & Hevner, 2018; Iivari, 2007). March and Smith (1995) make a similar separation between two types of instantiations in ISDSR ”specific information systems and tools that address various aspects of designing information systems” (March & Smith, 1995, p. 258). However, this separation has not received much attention in the ISDSR literature, even though it may be mentioned in the passing (e.g., Hevner et al., 2004).

The distinction is important for two reasons. Firstly, it implies two diferent target communities of practitioners: those who are interested in creating instances at the level of “general instantiated IT metaartefacts” and those who are interested in creating instances at the level of specific/local instantiated IT applications (e.g., information systems). DPs as prescriptive knowledge are inherently cognitive aids, interpreted, made sense of, and applied by their users to enable their reuse. Secondly, we believe that instantiation at the level of specific/local IT applications is quite diferent depending on whether there is a supporting instantiation at the level of “general instantiated IT meta-artefacts”. Development of an organisation-specific ERP information system without any ERP software package – if possible – and development of it by “instantiating” (i.e., configuring and customising) an ERP software package illustrates the point.

Figure 1 illustrates the situation. It distinguishes design knowledge (DK) including DPs (e.g., the relational data model), “general instantiated IT metaartefacts” (e.g., relational database management systems) and “specific or local instantiated IT applications” (e.g., relational databases in organisations). The unlabelled solid arrows describe the direct instantiation relations and the dotted arrows optional relationships, i.e., how an instantiated IT meta-artefact $( \mathrm { e . g . }$ Instance $\mathbf { A } _ { 0 } )$ may optionally be used in creating an instance of specific IT application (Instance $\mathrm { B } _ { 0 } )$ and in creating other instances of $\mathrm { A } _ { 1 } \ \ldots \ \mathrm { A } _ { \mathrm { n } }$ at the level of meta-artefacts.

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">DSR project</td><td colspan="3">Practice</td></tr><tr><td>Design knowledge</td><td>General instantiated IT meta-artifacts</td><td>Specific/local instan- tiated IT applications</td></tr><tr><td></td><td>Design know- ledge (DK) (incl. DPs)</td><td> ${\mathrm{{DK}}}_{\mathrm{R}} =$  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</td><td>KT ${\mathrm{{DK}}}_{\mathrm{P}} =$   ${\mathrm{{DK}}}_{\mathrm{P}}\left( \mathrm{A}\right) \cup {\mathrm{{DK}}}_{\mathrm{P}}\left( \mathrm{B}\right)$ Reuse A</td><td></td><td></td></tr><tr><td>Class A</td><td>General instantiated IT meta- artifacts</td><td>Instance  ${A}_{0}$ </td><td></td><td>Instances  ${A}_{1}\cdots {A}_{n}$ Reuse B</td><td></td></tr><tr><td>Class B</td><td>Specific/ local instantiated IT appli- cations</td><td>Instance  ${B}_{0}$ </td><td></td><td></td><td>Instances  ${B}_{1}\cdots {B}_{m}$ </td></tr></table>

Figure 1. Two types of reusing ISDSR-generated design knowledge.

Figure 1 identifies two (more or less) overlapping “bodies” of knowledge both in the case of researchers $( \mathrm { D K _ { R } } )$ and practitioners $( \mathrm { D K _ { P } } ) { \mathrm { : } }$ that concerning the design of “general instantiated IT meta-artefacts” of Class A $\mathrm { ( D K _ { R } ( A ) }$ and $\mathrm { D K _ { P } ( A ) } )$ and that concerning “specific/local instantiated IT applications” of Class $\mathrm { ~ B ~ } \left( \mathrm { D K } _ { \mathrm { R } } ( \mathrm { B } ) \right.$ and $\mathrm { D K _ { P } ( B ) } )$ ). The two communities may be decomposed into sub-communities with diferent interests (e.g., practitioner sub-communities such as consultants, vendor professionals that develop “general instantiated IT meta-artefacts”, systems developers (both in-house and in software houses) who develop “specific instantiated IT applications” in diferent application domains, project managers, etc.). IT teachers are significant in the longer-term knowledge transfer from research to practice. It is beyond the scope of this paper to address these in more detail. The essential point is that the papers proposing DPs identify the target communities of practitioners and involve practitioners who can be expected to provide reasonably valid information about the reusability of DPs in question.

We conjecture that the relevant set of DPs depends on the target community. Let us take an example of a DSR paper that suggests a novel concept of ERP with a set of DPs, including a prototype instantiation of an ERP package $\left( \mathrm { A } _ { 0 } \right)$ . Practitioners interested in creating new instances of comparable ERP packages $( \mathrm { A } _ { 1 } ,$ $\mathrm { A } _ { \mathrm { n } } )$ are likely interested in all the DPs, especially in principles of function and form (Gregor & Jones, 2007) of the prototype $\mathrm { A } _ { 0 } .$ . Meth et al. (2015) is an example of a DP paper at the A level (Figure 1), proposing its DPs to support future development and instantiation of requirements mining systems. Practitioners who are interested in adopting some of the instantiated ERP packages $( \mathrm { A } _ { 1 } \ \dotsc \ \mathrm { A } _ { \mathrm { n } } )$ , when implementing (instantiating) a specific ERP-based information system in their organisations $( \mathbf { B } _ { 1 } \ldots \mathbf { B _ { m } } )$ , may see some of the principles of form just as technical internals of the ERP package adopted, even though they indirectly adopt them as constituents of the ERP package.

Above all, Figure 1 also points out researchers design knowledge $\mathrm { D K } _ { \mathrm { R } }$ is not reused in practice directly, but it must be transferred (KT) to practitioners and adopted by them in their design knowledge $\mathrm { D K } _ { \mathrm { P } } .$ Thus, the reuse is decisively a communication process.

## 3. Reusability evaluation of design principles in current ISDSR publications

To justify our concern for the lack of reusability evaluation of DPs, this section analyzes how DPs proposed in ISDSR papers published in the leading IS journals, have been evaluated. The analysis does not attempt to be a comprehensive and systematic literature review (Kitchenham & Brereton, 2013; Vom Brocke et al., 2015). It would likely require a separate paper. Similar to the literature review on “Design Principles” by Chandra et al. (2015) (their review included articles published in the AIS Senior Scholars’ Basket of Eight journals up to the end of year 2013), we decided to conduct a corresponding literature analysis with four diferences. Firstly, we restricted our analysis to papers that explicitly are framed as DSR contributions. Secondly, the timeframe of our analysis was extended to the mid of 2018. Thirdly, and most importantly, we focused on DPs in a more specific meaning expressed above. Fourthly, our focus was “DP papers” that suggest their own DPs as their contributions.

We limited our analysis to DSR papers published in leading IS journals, since they likely apply more stringent acceptance criteria than conferences. Taking the purpose of this paper, it is justified, since it underestimates rather than exaggerates the problem – the weak evaluation of DPs by real practitioners in published DP papers.

Our initial identification of relevant papers was performed using Google Scholar in July 2018. An article was included if it actually adopted the DSR paradigm or applied a DSR methodology and proposed a clear set of DPs as its key contribution. We also looked for indicators whether the DPs were targeted to practitioners as assumed by our interpretation of DPs. If the paper used the term “design principle” or “design guideline”, we accepted any formulation of it as valid. This search procedure led to a set of 17 articles (EJIS 4, ISJ 2, ISR 2, JAIS 3, JIT 0, JMIS 1, JSIS 2, MISQ 3). Even though there were borderline cases (e.g., Siponen & Iivari, 2006), their inclusion or exclusion being a matter of interpretation, we excluded them believing that the identified set of 17 DP papers represent the state of the art of the empirical evaluation of DPs in the leading IS journals.

Each article was analysed for possible empirical evaluation of the proposed DPs. We distinguished three sub-categories of such evaluation: proof-of-concept, internal practitioner evaluation, and external practitioner evaluation. Proof-of-concept of a set of DPs is demonstrated as the set of DPs is used to instantiate a concrete system or real-world action. The distinction between internal and external practitioner evaluation is based on the position of practitioners relative to the project – whether or not they belong to the DSR project (including members of its possible client organisation) or not. In both cases, the evaluation of DPs may be direct (focusing on the DPs themselves) or indirect (evaluating an instantiation of the DPs). The distinction between internal and external practitioners corresponds to that between internal validity (credibility) and external validity (transferability) (R.L. Baskerville et al., 2015). While this correspondence underlines the significance of external evaluation (“validity”) of DPs, it is essential in the DSR context to evaluate not only the truth or trustworthiness of the findings but also the utility of the focal artefact (DPs in our case).

Appendix A reports the results of our analysis. It indicates that all the papers – Germonprez et al. (2017) as an exception – demonstrated the “proof of concept” of the suggested principles. We found in 12 papers, evidence of “internal” reusability evaluation of the proposed DPs. In eleven cases it took place indirectly, only Giessmann and Legner (2016) demonstrating explicit internal evaluation. Most importantly from the viewpoint of this paper, 12 of the 17 articles did not include any “external” reusability evaluation of the proposed DPs. And three of the remaining five had it in a very limited or special sense of not using real practitioners (Babaian et al., 2018; Lukyanenko et al., 2017) or implicitly using the commercial success of the system as evidence of the value of the proposed DPs (Markus et al., 2002). Overall, the results demonstrate that the external reusability of the proposed DPs is weakly addressed in the DP papers published in the leading IS journals.

However, papers such as Meth et al. (2015) and Coenen et al. (2018) are examples of sophisticated evaluation of their DPs (see Appendix A). At the same time, they are examples of fairly heavy evaluation of DPs and therefore may impose high standards for the reusability evaluation expected and required from each DP paper. Such standards can easily force researchers to emphasise evaluation rather than innovativeness. One should note that researchers are always obliged to compromise between a “full” evaluation of DPs and what is practically possible. To have a “full” evaluation a researcher should be able to assure the internal validity and the external validity of the findings on which the evaluation is based. Assuming DSR Strategy 2 (Iivari, 2015), in which the DPs are developed in a specific practical setting of the client, the researcher should have 1) a credible account that a system (or action) instantiating the DPs resulted in specified outcomes – positive and negative – in that specific practical setting and that the DPs significantly contributed to those outcomes, and 2) that the specified DPs can be transferred to other settings so that the DPs help practitioners to instantiate them and the resulting system (or action) leads to the similar outcomes as in the original setting of the DSR project and that the DPs significantly contribute to those outcomes.

In order to promote the practical relevance of the suggested DPs we maintain that a framework for light evaluation could serve as a standard for the minimum reusability evaluation of the proposed principles expected from DP papers, which can be applied when:

● the authors wish to publish their major DSR ideas (expressed as a set of DPs) as soon as possible before their “full” evaluation (one reason is to get the “ownership” of the ideas),

● and/or careful testing and empirical evaluation of the DPs are not possible at the time of invention, because there is not necessary technology available (as in the case of Codd’s (1970) relational model at that time),

● and publication outlets are ready to publish innovative DSR ideas (DPs), even though they are tentative and not carefully tested and empirically evaluated (this is analogous to publishing pure theory building papers).

## 4. A framework for light reusability evaluation

Multiple frameworks have been proposed to analyse the practical relevance and applicability of IS research outcomes (Benbasat & Zmud, 1999; Drechsler et al., 2016; Gill & Hevner, 2013; Klein et al., 2006; Rosemann & Vessey, 2008).

Due to its relative simplicity, we chose Rosemann and Vessey (2008) as our starting point for our framework compared to later proposals based on evolutionary economics (Gill & Hevner, 2013) or artefact’s “resonance” (Drechsler et al., 2016) with practitioners. Rosemann and Vessey (2008) suggest seven steps for the applicability check where the first step is to prepare materials that describe the context, objectives, and expected utility of the research. When applied to DPs, we argue that one needs to describe the class of systems or problems addressed by the set of DPs as well as any boundary conditions considered essential in the reuse of the DPs (Chandra et al., 2015). Since DPs are abstractions meant to be decoupled from specific contexts, we claim that DPs can be evaluated more independently of the research context in which they originated and in turn allow for a faster and more easy (light) evaluation than the applicability check (Rosemann & Vessey, 2008).

Rosemann and Vessey (2008) identify three dimensions of research relevance – accessibility, importance, suitability – with a primary target of traditional behavioural research – whether positivistic or interpretive in its origin. The applicability of design artefacts is not specifically addressed in their paper. Emphasising some diferences between ISDSR and ISBSR, we suggest a framework with five criteria: (1) accessibility, (2) importance, (3) novelty and insightfulness, (4) actability and guidance, and (5) efectiveness (Figure 2). Figure 2 illustrates the resultant framework with associated references to be discussed below.

“Accessibility” and “importance” correspond to the first two dimensions of research relevance in

Rosemann and Vessey (2008). Their framework does not include the criterion “novelty and insightfulness” – likely presuming that novelty and insightfulness to the scientific community imply novelty and insightfulness to the practitioner community, too. We do not see this assumption self-evident, especially in the context of ISDSR. Referring to “suitability” in Rosemann and Vessey (2008), we distinguish two aspects in it: actability and guidance on the one hand and efectiveness on the other hand. Actability means that the DPs can be acted on and carried out in practice. Efectiveness refers to possible efects or consequences of the proposed set of DPs.

The dotted arrows in Figure 2 suggest that the set of five criteria is not “flat”, but their order is relevant: if interpreted dichotomously (Yes/No), the five criteria form an order so that if the answer to n<sup>th</sup> criterion is “no”, the remaining criteria can be considered irrelevant (note that we do not assume that the criteria are measured using a dichotomous scale). Since we claim that members of the target community of practitioners should serve as respondents or informants in the reusability evaluation, accessibility is a necessary precondition for all further evaluation. If practitioners do not understand the DPs, it is impossible for them to assess their importance, novelty and insightfulness, and so on. If they do not find the DPs important, their novelty and insightfulness is not an issue anymore. Following the logic of information economics (Marschak, 1974), we argue that if the set of DPs just confirms what is already known by the respondent, it cannot be expected to change the respondent’s action and therefore to afect its efectiveness (novelty can be interpreted to cover the novelty of the source of the set of DPs (publication and its authors), too, if it is consid ered relevant by a practitioner). Therefore, the actability and suficient guidance is not an issue in this situation.

Let us illustrate the logic of Figure 2 by a simple example. Imagine that one of the authors of this paper is driving with his wife in Sweden from Örebro to Stockholm. His Swedish is not very good but his wife masters it better. He follows the fastest route suggested by the navigator. While driving, he listens to music on the radio. The broadcasting is interrupted a second time by a warning that there is a trafic jam on the highway between Södertälje and Stockholm due to an accident and drivers are advised to take an alternative route if possible. Let us analyse this situation using the framework (see Table 1):

![](/api/attachments/G2FD2M8J/fulltext/images/c17fbb239a3fb246149d17c434ff3760f06da49a7165fff033d3e580cb656903.jpg)  
Figure 2. Evaluation criteria of reusability of by practitioners.

Our focus lies on the reusability of the whole set of DPs proposed. Some criteria can be applied to each DP individually (accessibility, actability, and guidance) whereas other criteria can be meaningfully applied only to the whole set of proposed DPs.

The following five sections introduce each of the criteria in more detail. The presentation is exemplified by a set of DPs recently published by one of the authors of this paper (Hansen & Pries-Heje, 2017). The purpose of this after-the-fact reflection is neither to criticise the paper nor to conduct a systematic evaluation of the DPs in question, but 1) to illustrate how the criteria of Figure 2 can be applied when evaluating DPs and 2) to provide some evidence of how they might help to improve DPs papers in the future.

Hansen and Pries-Heje (2017) propose five principles for “designing IT tools that can support the facilitation and improvement of knowledge networks” (p. 61): “The principle of enabling continuous process improvement (DP1), The principle of creating participatory value (DP2), The principle of visualising dimensional status (DP3), The principle of comparing to contextual ideals (DP4), The principle of visualising potential action-taking (DP5)” (Hansen & Pries-Heje, 2017, p. 70). The DPs were targeted at designers of decision support systems who want to design systems that support the flow of knowledge in network groups (groups of people that share experiences and knowledge facilitated by a facilitator).

## 4.1. Accessibility

Accessibility as the first criterion of reusability of DPs underlines that the DPs must be expressed in a way that they can successfully be communicated to their reusers. Rosemann and Vessey (2008) characterise accessibility to the presentation style – tone, style, structure, and semantics tailored to the target audience (Benbasat & Zmud, 1999) – rather than the substance of research. Following this line of reasoning, we define accessibility of DPs as the degree to which the members of the target community can understand and comprehend the set of design principles and whether they are individually and collectively intelligible.

Accessibility implies that the set of DPs should be expressed in understandable language, using comprehensible terminology, and ultimately the DPs should make sense to the practitioners so that they can meaningfully evaluate their importance, novelty and insightfulness, actability and guidance, and efectiveness (see below). Accessibility also covers that practitioners understand and comprehend the class of IT artefacts, the instances of which the proposed set of DPs helps to create.

Referring to our example (Hansen & Pries-Heje, 2017), the first question is whether the target practitioners understand the purpose of the five DPs: to guide design of ”IT tools that can support the facilitation and improvement of knowledge networks”. The first two principles “The principle of enabling continuous process improvement (DP1)” and “The principle of creating participatory value (DP2)”, although possibly intuitively clear to target practitioners in question, have been expressed at a quite abstract level so that, after a deeper analysis, they may not be understandable without explanations. What is “continuous improvement” and what is “participatory value”? If improvement encounters temporal setbacks, is it still continuous? Does “participatory value” mean “value produced/created to participants” or “value produced/ created by participation” or both or something else? The principle is elaborated in Hansen and Pries-Heje (2017) by explaining that participatory value should be provided for all stakeholders, including the facilitator and those who sponsor the network group, through functions of formal agreements and shared, explicit evaluations of the value given through the network.

In any case, the principles might be understandable for the authors themselves but it is not made clear to which group of practitioners the DPs are targeted. If the DPs in Hansen and Pries-Heje (2017) had been more explicitly targeted to a group of explicitly defined practitioners, the wording of the proposed DPs would likely have been reconsidered more carefully.

If the concepts referred to in DPs are not clear to ordinary practitioners, there is a clear risk that they remain unnoticed by them (it may be unrealistic to expect that practitioners dive deeper into the underlying theories) or that DPs remain too open to interpretation – possibly misleading one – by the practitioners. As a consequence, we see it important that DPs – if not written in plain English in scientific articles – would have a practitioner-oriented version, in which the principles are briefly explained using a language accessible to the target community of practitioners.

## 4.2. Importance

Rosemann and Vessey (2008) interpret that research is important when it “meets the needs of practice by addressing a real-world problem in a timely manner, and in such a way that it can act as the starting point for providing an eventual solution” (p. 3). This interpretation does not clarify much in the context of this paper, since DP papers – as ISDSR contributions almost by definition propose contextualised instances of the class of IT artefact as eventual solution to the real-world business problems (Hevner et al., 2004). Instead of defining “importance” as such, which we regard as a primitive concept (not defined in terms of previously defined concepts), we suggest the importance of DPs in the light reusability evaluation is estimated in terms of the importance of the realworld problems they eventually help to address: The logic underlying the suggestion is that the importance of a set of DPs is an increasing function of the importance of the real-world problems that the set of DPs is assumed to indirectly address by helping to create contextualised instances of the class of IT artefacts – the contextualised instances forming eventual solutions to the real-world problems in question.

Generally speaking, ISDSR can be assumed to increase the practical relevance of IS research, especially in Strategy 2 when taking in a close cooperation with client organisations (Iivari, 2015). However, contrary to Rosemann and Vessey (2008), we contend that even close cooperation between researchers and practitioners cannot guarantee the practical relevance of research for two reasons. Firstly, numerous IS failures (Dwivedi et al., 2015) demonstrate that even practitioners may fail to identify the real problem, construct appropriate requirements, implement the system technically, or to get the system accepted and used. If an ISDSR project attempts to build a system to address a heretofore unsolved problem (Hevner et al., 2004), this risk of failure is still higher compared to (seemingly) routine IS development. Although a failed ISDSR project may lead to significant learning from the failure (Petroski, 1992), lessons from it would be mistakes to be avoided. Such lessons of what not to do provide very limited guidance for what to do (see Section 4.4 on “actability and guidance” below).

Secondly, practitioners within the same application domain may perceive the practical importance of the problem, the systems to address it, and the related DPs diferently due to diferences in their context (e.g., country and resources available) and situational factors (e.g., priority). These diferences lead us to expect variation in practitioners’ perceptions of importance of any set of DPs.

As an extreme example, a start-up company (MyOrigo) developed in the beginning of the first decade of the ongoing decennium a working prototype of MyDevice, a mobile phone that included DPs such as a touch-sensitive interface, auto-switching portrait/landscape feature, swiping, virtual QWERTY “keyboard” that pops up when needed and could be used for web browsing (https://www.theregister.co.uk/ 2003/07/02/reg\_testdrives\_myorigo\_motion\_control/ ). The company introduced its prototype to Nokia in

2002, but Nokia was not interested in it. Later the same year, MyDevice was introduced to Apple at Cupertino, Steve Jobs popping in the meeting, and playing with the MyDevice for a while. The rest is history.

Therefore, evaluation of DPs should not be restricted to practitioners from a single client organisation (as often is the case in the internal practitioner evaluation) but involve a “sample” of external members from the target community of practitioners. If there turns out to be clearly diferent clusters of opinions about the importance, perhaps there is a systematic reason for the diferences so that the target community should be re-considered and possibly made more focused.

When considering the set of five DPs proposed by Hansen and Pries-Heje (2017) the first question is whether “IT support for facilitation and improvement of knowledge networks” forms an important problem to the target practitioners. Hansen and Pries-Heje (2017) do not report any evaluation of importance by members of the target community of practitioners, but their DSR project was initiated by practitioners: Companies who are members of knowledge networks in the Danish region of Thy (in Northern Jutland) recognised and approached the researchers for possible solutions to the problem of identifying and assessing purpose and value from network groups. Furthermore, the authors evaluate the proof of concept artefact with two facilitators from similar organisations that both see the assessment tool important for their knowledge groups.

## 4.3. Novelty and insightfulness

When reviewing DSR papers, the novelty is usually evaluated by fellow researchers only. Evaluation of DPs should be extended to cover practitioners’ perception of novelty too, i.e., whether they see the set of DPs novel and insightful (much in line with Information Economics (Marschak, 1974)), not only confirmation of what they already know. This means that the DPs should have a potential to surprise practitioners (Drechsler, 2015). While “novelty and insightfulness” are not part of the Rosemann and Vessey (2008) applicability check, they (likely) assume that scientific novelty ensures practical novelty. However, it is important to keep in mind that what is new and innovative may difer in the case of researchers and practitioners. It is especially so, when practice is ahead of (academic) research. Leading systems development methods at their time such as Structured Analysis, Information Engineering, and agile methods (XP and Scrum), for example, were developed by consultants rather than by scholarly researchers (Ågerfalk & Fitzgerald, 2006).

It is dificult for us, as researchers rather than as practitioners, to assess the novelty of the five design principles proposed by Hansen and Pries-Heje (2017). However, one could argue that the novelty and insightfulness were indirectly evaluated through the evaluation of the artefact by two external facilitators, though an explicit evaluation of the DPs themselves with practitioners who design tools for or organise knowledge networks could definitely have addressed the concern for novelty.

## 4.4. Actability and guidance

As Rosemann and Vessey (2008) only briefly characterise their “suitability” as meeting the needs of practice, Kuechler and Vaishnavi (2011) introduce the concept of “actionability” to complement the applicability check framework. Actionability means that the research results contain immediate utility and are “applicable to a problem of immediate or recurring concern” (Kuechler & Vaishnavi, 2011, p. 128). Drechsler (2015) adopts it as one of three criteria of resonance (accessibility, actionability, and actual use). We point out, however, that, at least in principle, an “actionable” (or actable in our terminology) result (e.g., an IT artefact) may be ineficient or totally misguided. Therefore, we distinguish actability and guidance (introduced in this section) from efectiveness (to be discussed in the next section).

We suggest that the set of DPs should be actable and provide appropriate guidance. Actability means that the set of DPs can be acted and carried out in practice, i.e., it is under the control of the practitioners in question and is realistic to be carried out. Appropriate guidance, on the other hand, requires a delicate balance so that the set of DPs provide suficient guidance without being too restrictive.

Referring to the low number of DPs identified in most of the 17 DP papers in Appendix A (mode 4, median 4–5, and mean 5.7), it is also clear that the proposed DPs provide only partial knowledge for designing instances of the class or type of systems that the DPs claim to support. Chandra Kruse et al. (2016) point out that design knowledge comprises also tacit knowledge, implying that no set of codified DPs is suficient for designing instances in question. The target practitioners may nevertheless find a set of DPs to provide more or less suficient guidance for the design problem when one considers the existing pre-knowledge and expertise among the members of the target community. A set of DPs interpreted literally on the other hand, may at least in principle be too restrictive, even though Chandra Kruse et al. (2016) emphasise creative application of them. So, we see that DPs should be delicately balanced so that they provide suficient guidance without being too restrictive.<sup>4</sup> They should focus on the essential and distinctive aspects of the type of systems, the design of which they attempt to support, complementing the expected, general IS development knowledge of practitioners of the target community.

To exemplify, the first two principles of Hansen and Pries-Heje (2017) do not provide a clear idea of how they could be acted upon. Much of their explanation of the first principle: “The principle of enabling continuous process improvement (DP1)” emphasises the explicit nomination of a facilitator and describes what the facilitator as a change agent is expected to do. This is clearly actable. However, it is not easy to follow how “The principle of creating participatory value (DP2)” can be made actable. Actability could have been improved by mentioning what or who create the participatory value, e.g.: “The principle of letting participants create value through X”. The third principle: “The principle of visualising dimensional status (DP3)” is an example of a somewhat actable DP. DP3 is explained with “the need for a structural overview of the knowledge network in order to assess it and make a decision. Some sort of measurement system can potentially help participants determine whether their investment is worth pursuing and capable of generating economical value” (Hansen & Pries-Heje, 2017, p. 71). The choice of words such as “some sort of measurement system” does not provide very strong actability or guidance for practitioners as they would not know which structural patterns need to be visualised. However, Hansen and Pries-Heje (2017) do provide a concrete example of such visualisation – a radar chart describing “network size”, “purpose and success criteria”, “member composition”, “knowledge level and type”, “knowledge-sharing and interaction”, “facilitation and leadership”, and “activities”. In conclusion by hindsight, the DPs in Hansen and Pries-Heje (2017) could have been formulated in somewhat more actable terms.

## 4.5. Efectiveness: relative advantage and usefulness

We contend that suitability (Rosemann & Vessey, 2008) implicitly assumes that the “research object”, if made use in practice, would have a positive efect there. If the object does not have any efect or it is detrimental, it is not suitable. Efectiveness of a set of DPs refers to efects or consequences – both intended and unintended – of reusing the DPs in question in the adopting unit (e.g., an organisation or an individual). We note that DPs and related instantiations may have efects at diferent levels (individuals, groups, organisations, communities, markets, society, global). We recommend, however, that the focus of the light reusability evaluation is confined to the level of the adopting unit.

Evaluation of efectiveness of the DPs – i.e., how they might afect the adopting unit’s (e.g., an organisation’s or individual’s) performance is a complicated issue. First, there is a question of how the DPs afect the development process of the system in the adopter’s context and then there is a question of how the instantiated system might afect the adopter’s performance. Complete evaluation would require a naturalistic approach (Venable et al., 2016) so that a realinstantiated system is used by real users in a real organisational context over a longer period so that possible efects of the system can be identified.

One should note that even in this case it is extremely dificult to determine the influence of the system because numerous confounding factors or other complications. For example, Digital Equipment Corporation developed in the shift of the 1970s and 1980s an expert system (XCON) for configuring VAX computers and an associated system (XSEL) for salespersons (Barker & O’Connor, 1989). These systems were widely hailed as great successes also in the IS literature (e.g., Mumford, 1991; Sviokla, 1990). However, it turned out that the rule base of XCON continued to expand and change (with over 10.000 rules as of September 1988, Barker & O’Connor, 1989) so that maintainability was seriously challenged (Günter & Cunis, 1992). Later Keil (1995) made use of XSEL (using a pseudonym CONFIG) as an exemplary case of project escalation, noting that the development of the system and the support for it were terminated at the end of 1992.

Despite these dificulties, practitioners of the target community may be able to reasonably estimate – better than nothing – the potential relative advantage of a proposed system, especially if the instantiated system or its prototype can be demonstrated to them.

In some situations, there is no question about the necessity of the proposed system. This makes the situation simpler, since it is easier to evaluate the impact of DPs on the IS development (instantiation) process than their efect on the performance of the adopting unit. Depending on the task supported, the evaluation may take place in terms of criteria specific to the task.

In the initial problem of identifying and assessing purpose and value from network groups expressed by practitioners (Hansen & Pries-Heje, 2017) efectiveness can be assessed in two aspects: 1) the extent to which the tool creates value to the participants, and 2) the extent to which practitioners can recontextualise the DPs in their current form and instantiate a similar knowledge network artefact that also creates value.

Drawing on the first aspect, “value” can be closely related to efectiveness, since ultimately the value of a network group is highly dependent on its efects. However, it is dificult to ascertain how well the activities and interaction among participants in a network group provide a value, in particular when a group has had been a long time in existence (on the other hand, a long existence of a group provides some evidence of its value). So, the problem in Hansen and Pries-Heje (2017) was implicitly turned into the question of how the facilitation and management of network groups can be supported by IT tools. In this situation, the efectiveness evaluation of proposed DPs is made more tractable, i.e., how the set of DPs supports design of IT tools that support facilitation and management of network groups. In the case of the second aspect, the efectiveness of the set of DPs was only evaluated indirectly through the instantiated artefact that the researchers themselves built and the fact that parts of the artefact were implemented into practice afterwards. However, following and evaluating how efectively the DPs communicated how practitioners could design knowledge networks that create value was not evaluated directly.

## 5. Discussion and concluding remarks

We found that the issue of DP reusability has been neglected in ISDSR papers proposing DPs – targeted to practitioners – as their key contributions. To remedy the situation, we proposed that DP papers should comprise at least the minimum reusability evaluation of the suggested DPs, meaning that the authors of DP papers (1) specify the target community of practitioners of the proposed sets of DPs and (2) conduct evaluation of the proposed DPs in terms of the five criteria of the framework for light evaluation of DPs using members of the target community of practitioners as informants, respondents or participants. Minimum means that we do by no means exclude stronger evaluation, if the respective authors are ready to conduct such. As pointed out in the end of Section 3 a “full” evaluation may not always be realistic or may even be dysfunctional in some situations. Below will argue that all this would have a profound impact on authoring, reviewing and editing of DP papers.

Next, we will contrast our framework with the frameworks for evaluation of design science research of Prat et al. (2015) and Venable et al. (2016). After that, we will proceed to the question of how our light evaluation could be used in DSR by authors, reviewers and editors.

Venable et al. (2016) propose their FEDS framework for evaluation in design science. They distinguish naturalistic evaluation and artificial evaluation on the one hand and formative evaluation and summative evaluation on the other hand. The former distinction makes it possible to characterise the continuum of light and heavy evaluation. Naturalistic evaluation as outlined in Venable et al. (2016) is a clear example of heavy evaluation. Artificial evaluations may vary in their heaviness depending on which aspects – people, system, or situation – are considered real and which are considered artificial and/or just surrogates (e.g., students representing real users or real practitioners). In our light version, the evaluation of DPs takes place in an artificial setting, by real practitioners, but not necessarily with a real instantiation of the principles in any system.

Venable et al. (2016) do not specifically discuss the evaluation of DPs and thus do not suggest clear guidelines for the said evaluation. It is dificult to position our framework in their FEDS model. Since the light evaluation is predominantly artificial on the artificialnaturalistic dimension and can be used both formatively and summatively, it would be a horizontal line on the artificial side, resembling the purely technical strategy in Venable et al. (2016). Although predominantly artificial, the light evaluation of DPs does not focus on the technical issues as Venable et al. (2016) assume artificial evaluations to be oriented.

Prat et al. (2015) develop a taxonomy of evaluation methods in ISDSR based on six dimensions of evaluation – criterion of evaluation, evaluation technique, form of evaluation, secondary participants, level of evaluation, and relativeness of evaluation – based on a systematic analysis of 121 DSR papers published in the Senior Scholar Basket 8 journals. They do not specifically address evaluation of DPs but consider them to be IT artefacts. Referring to their dimensions, our light evaluation framework suggests an evaluation method that: a) applies a question-based technique (note that Prat et al. (2015) do not limit the questionbased technique to the questionnaire only, but includes focus groups as well), b) is based on (subjective) perceptions in the case of form of evaluation, c) has practitioners (of the target community) as secondary participants, d) evaluates an abstract artefact in the case of level of evaluation, and e) is focused on either relative absence of comparable artefacts or relative to comparable artefacts. In the case of goals, Prat et al. (2015) end up with a complex hierarchy of 34 criteria at the lowest level. As explained above, our light framework for the reusability evaluation of DPs by practitioners is based on five criteria, only actability and efectiveness having clear equivalents in Prat et al. (2015). Although especially “actability and guidance” and “efectiveness” can be decomposed into a few aspects, our framework is considerably simpler than that of Prat et al. (2015).

Gregor and Hevner (2013) emphasise flexibility in judging the needed evaluation in DSR papers, pointing out that mere “proof-of-concept” may be suficient in the case of a very innovative artefact. Despite that, we contend that generally each DP paper – suggesting a set of DPs to be reused by practitioners – should have a minimum reusability evaluation of the proposed principles. We believe that our framework is so light that it could serve as a standard for such minimum DP evaluation.

Figure 3 exhibits the way of utilising the proposed framework in the DSR process, supporting both research design, practical reusability evaluation, paper authoring, and paper reviewing. As for research design, researchers aiming at a DSR paper with a set of DPs as its major contribution should be prepared to have at least a minimum reusability evaluation. We advise to recruit at least a small “sample” of members of the target community for participating in the evaluation. If the target community of practitioners consists of subgroups (Drechsler, 2015), it is up to the authors of each DP paper to assess, which subgroups can realistically be recruited in the evaluation efort and are reasonably capable to evaluate the reusability of proposed set of DPs. We do not wish to be too restrictive in this respect. The most important point is that DPs are also evaluated by members of the target community of practitioners, external to the DSR project in question. One possibility is to use members of local, regional, national or international professional associations or conference participants, for example.

![](/api/attachments/G2FD2M8J/fulltext/images/506bfb6716207d77261f7de966dfe7a7dc1b6ad54984911851f12f0c4da533c1.jpg)  
Figure 3. Utilising the light evaluation framework.

The framework aids concrete reusability evaluation to be performed by authors involving real practitioners by suggesting five criteria used as issues to be discussed especially in the case of formative evaluation. One can also realistically expect that even the light reusability evaluation involving real practitioners helps to improve the reusability of proposed DPs. Our example of Hansen and Pries-Heje (2017) shows that our framework, if had been available at the time of their research project, had pushed the authors to focus more on the “accessibility” and “actability & guidance” of their DPs. Furthermore, more attention to the target audience of practitioners could also have been impacted. After further reflection, the target audience of design practitioners, who design tools for knowledge network groups, maybe quite a niche and too specific, or even just based of of the professional backgrounds of the authors themselves. Such a realisation could be expanded to comprise consultants with technical knowledge on the novice level, though with strong domain knowledge.

The framework also eases the authoring of DP papers by providing a standard for presenting evaluation results. We have proposed a template of questions (see Appendix B) to be instantiated in each ISDSR project (Iivari et al., 2018). Once instantiated, it can be used both formatively to evaluate what to improve the DPs and summatively to evaluate the quality of the DPs. When used formatively, the instantiation can serve as a semi-structured interview guide. If the template is used to instantiate a questionnaire to be used in a quantitative summative evaluation, its psychometric properties (such as reliability and validity) should be tested using standard procedures (Straub et al., 2004), if there are no appropriate instantiations validated earlier. If authors decide not to conduct even a minimum evaluation of their DPs, they should justify their decision in their manuscript. For example, if they propose a set of DPs not targeted to practitioners, they should state it explicitly.

Finally, the framework aids reviewing. If accepted as a standard for minimum reusability evaluation, reviewers will have a clear idea that each paper suggesting DPs should have such an evaluation or similar.

The inclusion of a concise and short summative, quantitative evaluation would also ease the reviewing process, especially for conferences where severe page limits inhibit extensive reporting of evaluations.

We wish to emphasise that the minimum evaluation does not exclude more naturalistic evaluation of the set of DPs, using real people, real system, in the real context (Venable et al., 2016). In general cases, “full” evaluation implies the question of how the instantiated system may afect the adopter’s performance, including possible longterm efects. Such efectiveness evaluation takes time and therefore is dificult to conduct within the time frame of a single DSR project. Actually, it is likely more reasonable to conduct the longterm evaluation of DPs as a separate evaluation project, if the class of system associated with the proposed set of DPs turns out to be of suficient interest in the research community and/or in the practitioner community. If the long-term efects are attempted to anticipate in the DSR project, there is naturally a lot of uncertainty. Keeping that in mind, the light evaluation of DPs may in any case provide useful, additional information to other forms of evaluation in the DSR project. As an example, we believe that most studies reported in Appendix A would have benefitted from complementary evaluation of the proposed DPs using our light framework.

## Notes

1. We recognise that DPs may have other uses, too. For example, they may be projected (Baskerville & Pries-Heje, 2019) beyond the initial class of IT artefacts and drawn on in later research – or “reused” in Vom Brocke et al.’s (2020) terminology. This “reuse” difers from our conception of “DP reuse”.

2. Since the degree of socio-technicality” (Drechsler, 2015) is not essential here, we drop it.

3. We use adjectives “specific” and “local” together, because IT applications such as social networking sites are global rather than “local”. “Specific” may be better to characterise them. On the other hand, in the case of general application packages (e.g., for text processing), “local” characterises the installed and contextualised copies of the package.

4. The question of how heavy or light systems development methods are “optimal” illustrates the point.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## References

Ågerfalk, P., & Fitzgerald, B. (2006). Flexible and distributed software processes: Old petunias in new bowls. Communications of the ACM, 49(1), 27–34. https://doi. org/10.1145/1164394.1164416

Babaian, T., Xu, J., & Lucas, W. (2018). ERP prototype with built-in task and process support. European Journal of Information Systems, 27(2), 189–206. https://doi.org/10. 1057/s41303-017-0060-3

Barker, V. E., & O’Connor, D. E. (1989). Expert systems for configuration at Digital: XCON and beyond. Communications of the ACM, 32(3), 298–315. https:// doi.org/10.1145/62065.62067

Baskerville, R., & Pries-Heje, J. (2014). Design theory projectability. In B. Doolin, E. Lamprou, N. Mitev, & L. McLeod (Eds.), Information systems and global assemblages: (re)configuring actors, artefacts, organizations (pp. 219–232). Springer.

Baskerville, R., Baiyere, A., Gregor, S., Hevner, A., & Rossi, M. (2018). Design science research contributions: Finding a balance between artifact and theory. Journal of the Association for Information Systems, 19(5), 358–376. https://doi.org/10.17705/1jais.00495

Baskerville, R., & Pries-Heje, J. (2019). Projectability in design science research. Journal of Information Technology Theory and Application (JITTA), 20(1), 53–76. https://aisel.aisnet.org/jitta/vol20/iss1/3

Baskerville, R. L., Kaul, M., & Storey, V. C. (2015). Genres of inquiry in design-science research: Justification and evaluation of knowledge production. MIS Quarterly, 39(3), 541–564. https://doi.org/10.25300/MISQ/2015/39.3.02

Benbasat, I., & Zmud, R. W. (1999). Empirical research in information systems: The practice of relevance. MIS Quarterly, 23(1), 3–16. https://doi.org/10.2307/249403

Bittner, E. A. C., & Leimeister, J. M. (2014). Creating shared understanding in heterogeneous work groups: Why it matters and how to achieve it. Journal of Management Information Systems, 31(1), 111–143. https://doi.org/10. 2753/MIS0742-1222310106

Chandra Kruse, L., Seidel, S., & Purao, S. (2016). Making use of design principles, in Proceedings of the 11th international conference on design science research in information systems, lecture notes in computer science, Springer, pp. 37–51, St. John's, NL, Canada.

Chandra, L., Seidel, S., & Gregor, S. (2015). Prescriptive knowledge in IS research: Conceptualizing design principles in terms of materiality, action, and boundary conditions, in Proceedings of the 48th Hawaii international conference on system science (HICSS), pp. 4039–4048, Kauai, HI, USA.

Chaturvedi, A. R., Dolk, D. R., & Drnevich, P. L. (2011). Design principles for virtual worlds. MIS Quarterly, 35 (3), 673–684. https://doi.org/10.2307/23042803

Codd, E. F. (1970). A relational model of data for large shared data banks. Communications of the ACM, 13(6), 377–387. https://doi.org/10.1145/362384.362685

Coenen, T., Coertjens, L., Vlerick, P., Lesterhuis, M., Mortier, A. V., Donche, V., & Maeyer, S. D. (2018). An information system design theory for the comparative judgement of competences. European Journal of Information Systems, 27(2), 1–14. https://doi.org/10. 1080/0960085X.2018.1445461

Cronholm, S., & Göbel, H. (2018). Guidelines supporting the formulation of design principles. In Proceedings of the 29th Australasian Conference on Information Systems (ACIS), Sydney.

Drechsler, A. (2015). Designing to inform: Toward conceptualizing practitioner audiences for socio-technical artifacts in design science research in the information systems discipline. Informing Science: The International Journal of an Emerging Transdiscipline, 18, 31–45. https:/ doi.org/10.28945/2288

Drechsler, A., & Hevner, A. R. (2018). Utilizing, producing, and contributing design knowledge in DSR projects, in Proceedings of international conference on design science research in information systems and technology (DESRIST 2018), 82–97, Chennai, India

Drechsler, A., Hevner, A. R., & Gill, T. G. (2016). Beyond rigor and relevance: Exploring artifact resonance, Proceedings of the 49th Hawaii international conference on system sciences (HICSS), IEEE Computer Society, pp. 4434–4443, Koloa, HI, USA

Dwivedi, Y. K., Wastell, D., Laumer, S., Henriksen, H. Z., Myers, M. D., Bunker, D., Elbanna, A., Ravishankar, M. N., & Srivastava, S. C. (2015). Research on information systems failures and successes: Status update and future directions. Information Systems Frontiers, 17(1), 143–157. https://doi.org/10.1007/ s10796-014-9500-y

Germonprez, M., Hovorka, D., & Collopy, F. (2007). A theory of tailorable technology design. Journal of Association for Information Systems, 8(2), 351–367. https://doi.org/10.17705/1jais.00131

Germonprez, M., Kendall, J. E., Kendall, K. E., Mathiassen, L., Young, B., & Warner, B. (2017). A theory of responsive design: A field study of corporate engagement with open source communities. Information Systems Research, 28(1), 64–83. https://doi.org/10.1287/ isre.2016.0662

Giessmann, A., & Legner, C. (2016). Designing business models for cloud platforms. Information Systems Journal, 26(5), 551–579. https://doi.org/10.1111/isj.12107

Gill, T. G., & Hevner, A. R. (2013). A fitness-utility model for design science research. ACM Transactions on Management Information Systems, 4(2), 237–252. https://doi.org/10.1145/2499962.2499963

Goldkuhl, G. (2004). Design theories in Information Systems - a need for multi-grounding. Journal of Information Technology Theory and Applications, 6(2), 59–72. https://aisel.aisnet.org/jitta/vol6/iss2/7

Gregor, S., Chandra Kruse, L., & Seidel, S. (in press). Anatomy of design principles. Journals of the Association for Information Systems.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337–355. https://doi.org/10.25300/ MISQ/2013/37.2.01

Gregor, S., Imran, A., & Turner, T. (2014). A “sweet spot” change strategy for a least developed country: Leveraging e-Government in Bangladesh. European Journal of Information Systems, 23(6), 655–671. https://doi.org/10. 1057/ejis.2013.14

Gregor, S., & Jones, D. (2007). The Anatomy of a design theory. Journal of the Association for Information Systems, 8(5), 312–335. https://doi.org/10.17705/1jais.00129

Günter, A., & Cunis, R. (1992). Flexible control in expert systems for construction tasks. Applied Intelligence, 2(4), 369–385. https://doi.org/10.1007/BF00058652

Hansen, M. R. P., & Pries-Heje, J. (2017). Value creation in knowledge networks: Five design principles. Scandinavian Journal of Information Systems, 29(2), 61–79. https://aisel.aisnet.org/sjis/vol29/iss2/3

Heinrich, P., & Schwabe, G. (2014). Communicating nascent design theories on innovative information systems through multi-grounded design principles, In: Proceedings of the 9th International conference on design science research in information systems, lecture notes in computer science, pp. 148–163, Miami, FL, USA.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75–105. https://doi.org/10.2307 25148625

Hustad, E., & Olsen, D. H. (2014). Educating reflective enterprise systems practitioners: A design research study of the iterative building of a teaching framework. Information Systems Journal, 24(5), 445–473. https://doi. org/10.1111/isj.12032

Iivari, J. (2007). A paradigmatic analysis of information systems as a design science. Scandinavian Journal of Information Systems, 19(2), 39–63. http://aisel.aisnet. org/sjis/vol19/iss2/5

Iivari, J. (2015). Distinguishing and contrasting two strategies for design science research. European Journal of Information Systems, 24(1), 107–115. https://doi.org/10. 1057/ejis.2013.35

Iivari, J., Hansen, M. R. P., & Haj-Bolouri, A. (2018). A framework for light reusability evaluation of design principles in design science research, Proceedings of international conference on design science research in information systems and technology (DESRIST 2018), Chennai, India.

Iivari, J., Hirschheim, R., & Klein, H. K. (2004). Towards a distinctive body of knowledge for information systems experts: Coding ISD process knowledge in two IS journals. Information Systems Journal, 14(4), 313–342. https://doi.org/10.1111/j.1365-2575.2004.00177.x

Keil, M. (1995). Pulling the Plug: Software Project Management and the Problem of Project Escalation, MIS Quarterly, 19(4), 421–447. https://doi.org/10.2307/ 249627

Kitchenham, B., & Brereton, P. (2013). A systematic review of systematic review process research in software engineering. Information and Software Technology, 55 (12), 2049–2075. https://doi.org/10.1016/j.infsof.2013.07. 010

Klein, G., Jiang, J. J., & Saunders, C. (2006). Leading the horse to water. Communications of the AIS, 18(1), 259–274. https://doi.org/10.17705/1CAIS.01813

Kolkowska, E., Karlsson, F., & Hedström, K. (2017). Towards analysing the rationale of information security non-compliance: Devising a Value-Based Compliance analysis method. Journal of Strategic Information Systems, 26(1), 39–57. https://doi.org/10.1016/j.jsis.2016. 08.005

Kuechler, B., & Vaishnavi, V. (2011). Promoting relevance in IS research: An informing system for design science research. Informing Science: The International Journal of an Emerging Transdiscipline, 14, 125–138. https://doi.org 10.28945/1498

Lindgren, R., Henfridsson, O., & Schultze, U. (2004). Design principles for competence management systems: A synthesis of an action research study. MIS Quarterly, 28(3), 435–472. https://doi.org/10.2307/25148646

Lukyanenko, R., Wiersma, Y., Huber, B., Parsons, J., Wachinger, G., & Meldt, R. (2017). Representing crowd knowledge: Guidelines for conceptual modeling of user-generated content. Journal of the Association for Information Systems, 18(4), 297–339. https://doi.org/10. 17705/1jais.00456

Lyytinen, K., Baskerville, R., Iivari, J., & Te’eni, D. (2007). Why the old world cannot publish? Overcoming challenges in publishing high-impact IS research. European Journal of Information Systems, 16(4), 317–326. https:// doi.org/10.1057/palgrave.ejis.3000695

March, S. T., & Smith, G. F. (1995). Design and natural science research on information technology. Decision Support Systems, 15(4), 251–266. https://doi.org/10. 1016/0167-9236(94)00041-2

Markus, M. L., Majchrzak, A., & Gasser, L. (2002). A Design theory for systems that support emergent knowledge processes. MIS Quarterly, 26(3), 179–212. https://doi. org/10.2307/4132330

Marschak, J. (1974). Economic information, decision and prediction, selected essays: volume II. D. Reidel Publishing Company

Meth, H., Mueller, B., & Maedche, A. (2015). Designing a requirement mining system. Journal of the Association for Information Systems, 16(9), 799–837. https://doi.org/ 10.17705/1jais.00408

Mumford, E. (1991). The design of large knowledge-based systems: The example of Digital Equipment’s XSEL project. Information Systems Journal, 1(2), 75–88. https://doi. org/10.1111/j.1365-2575.1991.tb00029.x

Österle, H., Becker, J., Frank, U., Hess, T., Karagiannis, D., Krcmar, H., Loos, P., Mertens, P., Oberweis, A., & Sinz, E. J. (2011). Memorandum on design-oriented information systems research. European Journal of Information Systems, 20(1), 7–10. https://doi.org/10. 1057/ejis.2010.55

Pefers, K., Tuunanen, T., & Niehaves, B. (2018). Design science research genres: Introduction to the special issue on exemplars and criteria for applicable design science research. European Journal of Information Systems, 27(2), 129–139. https://doi.org/10.1080/0960085X.2018.1458066

Petroski, H. (1992). To engineer is human: The role of failure in successful design. Vintage Books.

Prat, N., Comyn-Wattiau, I., & Akoka, J. (2015). A taxonomy of evaluation methods for information systems artifacts. Journal of Management Information Systems, 32(3), 229–267. https://doi.org/10.1080/ 07421222.2015.1099390

Robey, D., & Markus, M. L. (1998). Beyond rigor and relevance: Producing consumable research about Information Systems. Information Systems Resources Management Journal, 11(1), 7–15. https://doi.org/10. 4018/irmj.1998010101

Rosemann, M., & Vessey, I. (2008). Toward improving the relevance of information systems Research to practice: The role of applicability checks. MIS Quarterly, 32(1), 1–22. https://doi.org/10.2307/25148826

Seidel, S., Chandra Kruse, L., Székely, N., Gau, M., & Stieger, D. (2018). Design principles for sensemaking support systems in environmental sustainability transformations. European Journal of Information Systems, 27(2), 221–247. https://doi.org/10.1057/s41303- 017-0039-0

Sein, M. K., Henfridsson, O., Purao, S., Rossi, M., & Lindgren, R. (2011). Action Design Research. MIS Quarterly, 35(1), 37–56. https://doi.org/10.2307/ 23043488

Siponen, M., & Iivari, J. (2006). Six design theories for IS security policies and guidelines. Journal of the Association for Information Systems, 7(7), 445–472. https://doi.org/ 10.17705/1jais.00095

Spagnoletti, P., Resca, A., & Sæbø, Ø. (2015). Design for social media engagement: Insights from elderly care assistance. The Journal of Strategic Information Systems, 24(2), 128–145. https://doi.org/10.1016/j.jsis.2015.04.002

Straub, D., Boudreau, M.-C., & Gefen, D. (2004). Validation guidelines for IS positivist research. Communications of

the Association for Information Systems, 13(24), 380–427. https://doi.org/10.17705/1CAIS.01324

Sviokla, J. J. (1990). An Examination of the impact of expert systems on the firm: The case of XCON. MIS Quarterly, 14(2), 127–140. https://doi.org/10.2307/248770

Te’eni, D., Seidel, S., & Vom Brocke, J. (2017). Stimulating dialog between information systems research and practice. European Journal of Information Systems, 26(6), 541–545. https://doi.org 10.1057/s41303-017-0067-9

Van Aken, J. E. (2004). Management research based on the paradigm of the design sciences: The quest for field-tested and grounded technological rules. The Journal of Management Studies, 41(2), 219–246. https://doi.org/10. 1111/j.1467-6486.2004.00430.x

Venable, J., & Baskerville, R. (2012). Eating our own cooking: Toward a more rigorous Design Science of Research methods. The Electronic Journal of Business Research Methods, 10 (2), 141–153. available online at www. ejbrm.com

Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation in design science research. European Journal of Information Systems, 25(1), 77–89. https://doi.org/10.1057/ejis.2014.36

Vom Brocke, J., Simons, A., Riemer, K., Niehaves, B., Plattfaut, R., & Cleven, A. (2015). Standing on the shoulders of giants: Challenges and recommendations of literature search in information systems research. Communications of the Association for Information Systems, 37(1), 205–224. https://doi.org/10.17705 1CAIS.03709

Vom Brocke, J., Winter, R., Hevner, A., & Maedche, A. (2020). Accumulation and evolution of design knowledge in design science research – A journey through time and space. Journal of the Association for Information Systems, 21(3), 520–544. https://doi.org/ 10.17705/1jais.00611

Yang, L., Su, G., & Yuan, H. (2012). Design Principles of Integrated Information Platform for Emergency Responses: The Case of 2008 Beijing Olympic Games. Information Systems Research, 23(3), 761–786. https:/ doi.org/10.1287/isre.1110.0387

## Appendix A. State of the art of the evaluation of DPs in the leading IS journals

Table A.1 summarises the results of our review of DP papers published in leading IS journals. Codes P1 and P2 in the end of introductions of the design principles indicate our interpretations whether the particular DPs provide knowledge for creating IT product instantiations (P1) or process instantiations (P2).

Table A.1 indicates that all the papers – Germonprez et al. (2017) as an exception – demonstrated the “proof of concept” of the suggested principles. We found in 12 papers evidence of evaluation of the proposed DPs involving practitioners internal to the DSR project. In 11 of the 12 papers, the evaluation was indirect, with Giessmann and Legner (2016) as the exception, but they did not report the details of the evaluation (e.g., what exactly was evaluated in the case of their DPs).

Most importantly from the viewpoint of this paper, 12 of the 17 papers did not include any external evaluation of the proposed DPs. Most of the remaining five papers included it only indirectly, Meth et al. (2015) including some direct efectiveness evaluation of the DPs.

Overall, Meth et al. (2015) and Coenen et al. (2018) are two papers that paid most attention to the external evaluation of the proposed DPS. Meth et al. (2015) followed DSR Strategy 1 (Iivari, 2015), i.e., it was not conducted in close cooperation with any client organisation. They suggest two DPs that can support future development and instantiation of requirements mining systems. As for the external evaluation, Meth et al. (2015) extended empirical evaluation to the target community of practitioners, who could be possible reusers of the principles outside the DSR project context. The two DPs were instantiated in their prototype system. The usefulness of the first prototype was evaluated by a demonstration to practitioners (experts in requirements engineering) and the user-friendliness (usability) of second prototype was conducted in a similar way. They also introduced the first prototype in a conference on requirements engineering. They conducted a separate experimental ex post evaluation of the second prototype using students and a small number of experts in requirements mining. Quite interestingly, the prototype made it possible to compare the efectiveness of two versions of design principles (DP1, and DP1 + DP2) and to contrast them with manual requirements mining.

Coenen et al. (2018) introduce six DPs for an information system intended to support comparative judgement of competences. Four of the six DPs are principles of form and function, and two principles of implementation (Gregor & Jones, 2007). The latter two are clearly targeted to practitioners deciding on the actual functional instantiation of the artefact. Coenen et al. (2018) report five expository instantiations of the system, which altogether were analysed eleven times. The final instantiation is available as open-source software for public download and further contribution.

The DSR approach in Coenen et al. (2018) is fairly complex when combining DSR mode 1 and DSR mode 2 (Iivari, 2015). DSR mode 1 is conducted without any client organisation, while DSR mode 2 takes place in the organisationa context of the client. Expository instantiations 1–3 were developed using mode 1 and instantiations 4–5 using mode 2. Not all details are explained in the research settings, which leads to a dificulty of interpreting the evaluation of design principles as internal or external evaluation (see Table A.1). Yet, the early instantiations 1–3 (six evaluations) seemed to be externally evaluated, since the evaluators or assessors (such as teachers) could be potential future users of the system. We interpret that the five evaluations of instantiations 4–5 were limited to the internal evaluation, each evaluation using members of the client organisation in question as assessors. The two principles of implementation were identified during the mode 2 in their DSR process. Coenen et al. (2018) do not report that they were not separately evaluated.

Among the remaining three papers with some external reusability evaluation of the DPs, Babaian et al. (2018) and Lukyanenko et al. (2017) conducted “external evaluation”, but not involving real practitioners as would-be -reusers. Babaian et al. (2018) used graduate students as subjects in the evaluation and Lukyanenko et al. (2017) evaluated the utility (impact) of the six DPs proposed by interviewing NLNature’s (a system for citizen science) users, but not external practitioners likely reusing the principles. In Markus et al. (2002) the commercial success of the system incorporating a set of DPs can be interpreted as an indirect evidence of the value of the proposed DPs.

Table A1. Empirical evaluation of DPs in the IS literature.

<table><tr><td rowspan="2"></td><td rowspan="2">Design principles (DPs)</td><td colspan="3">Empirical evaluation of DPs</td></tr><tr><td>Proof of the concept</td><td>By internal practitioners</td><td>By external practitioners</td></tr><tr><td>Markus et al. (2002)</td><td>6 DPs for designing IT support for emergent knowledge processes (pp. 1, P2)</td><td>The DPs were implemented in various prototypes of the TOP modeller and in the final system and/or followed in the development process</td><td>Indirectly when formatively evaluating different prototype versions</td><td>No, but the commercial success of the system (Top Modeller) may be used as an indirect external demonstration of the value of their DPs</td></tr><tr><td>Lindgren et al. (2004)</td><td>4 DPs for designing competence management systems (p. 1)</td><td>The DPs implemented in prototypes</td><td>Indirectly when formatively evaluating the prototypes, but not the final versions of the principles</td><td>No</td></tr><tr><td>Germonprez et al. (2007)</td><td>9 DPs for designing tailorable technologies (p. 1)</td><td>The authors followed the design of one tailorable web portal and found that the portal supported the DPs with one exception.</td><td>No</td><td>No</td></tr><tr><td>Chaturvedi et al. (2011)</td><td>11 DPs for designing agent-based virtual worlds (pp. 1, P2)</td><td>The DPs were derived from Sentient World, an agent-based virtual world simulation platform, and from its application Sentient World-Afghanistan.</td><td>Indirectly when evaluating different applications of Sentient World</td><td>No</td></tr><tr><td>Yang et al. (2012)</td><td>5 DPs for designing integrated information platforms for emergency responses (P1, P2)</td><td>The DPs were implicitly implemented in the integrated information platform for emergency responses in Beijing Olympics</td><td>Indirectly when formatively evaluating different prototype versions and the final system</td><td>No</td></tr><tr><td>Bittner and Leimeister (2014)</td><td>10 DPs for designing a collaboration process module to support heterogeneous work groups in building shared understanding (P1)</td><td>The process module ("compound thinkLet MindMerger") inspired by the ten DPs were used and evaluated in action research</td><td>Indirectly when formatively evaluating "compound thinkLet MindMerger" in an action research project comprising six groups of six members</td><td>No</td></tr><tr><td>Gregor et al. (2014)</td><td>4 DPs for designing change strategies for (governmental) intervention in least developed countries (P2)</td><td>The DPs were implicitly applied in the project carried out in Bangladesh, even though the DPs were explicitly identified after the project</td><td>Indirectly when formatively evaluating the intervention in several stages in and the completed project</td><td>No</td></tr><tr><td>Hustad and Olsen (2014)</td><td>8 DPs with an associated teaching framework for teaching Enterprise Systems classes for IS graduates (P1)</td><td>The DPs were derived from experiences of designing and redesigning the curriculum and teaching framework over eight years in one university</td><td>Indirectly when formatively evaluating the ES classes</td><td>No</td></tr><tr><td>Meth et al. (2015)</td><td>2 DPs for designing requirements mining systems (p. 1)</td><td>Principles implemented in two prototype versions</td><td>N/A, since the DSR project did not take place in cooperation with any client organisations</td><td>Indirectly when formatively evaluating prototypes and directly when evaluating the final prototype</td></tr><tr><td>Spagnoletti et al. (2015)</td><td>4 DPs for social media engagement in elderly care assistance (p. 1)</td><td>The DPs were applied in the interventions to provide personalised elderly care, supported by social media, in the case a geriatric unit of one hospital</td><td>The initial set of DPs derived from previous research were presented to and discussed with members of the geriatric unit. The final set was indirectly evaluated, when evaluating the interventions by practitioners of the geriatric unit</td><td>No</td></tr><tr><td>Giessmann and Legner (2016)</td><td>6 DPs (of form and function) for designing business models for platforms as service (P1)</td><td>The DPs were applied in designing a business model</td><td>Explicitly, summative evaluation by seven practitioners</td><td>No</td></tr><tr><td>Germonprez et al. (2017)</td><td>4 DPs for "responsive design" by corporations engaging with open source communities (P2)</td><td>Evidence from 40 organisations participating in the Linux open source community, all of them not instantiating all aspect of DPs</td><td>N/A, since the DSR project did not take place in cooperation with any client organisations</td><td>No</td></tr><tr><td>Kolkowska et al. (2017)</td><td>4 DPs for designing information security analysis methods (p. 1)</td><td>The DPs were applied in the design of a specific information security analysis method (VBC method) that was finalised and evaluated in the context of one organisation.</td><td>Indirectly when evaluating the VBC method in one organisation.</td><td>No</td></tr><tr><td>Lukyanenko et al. (2017)</td><td>6 DPs for conceptual modelling in the context of user-generated content (P1)</td><td>The DPs were applied in designing a citizen science information systems (NLNature)</td><td>Not reported</td><td>The utility (impact) of the DPs evaluated by interviewing NLNature's users, but not by external practitioners likely reusing the principles</td></tr><tr><td>Babaian et al. (2018)</td><td>4 DPs for designing collaborative ERP systems (p. 1)</td><td>Two of the DPs were implemented in a prototype</td><td>N/A, since the DSR project did not take place in cooperation with any client organisations</td><td>The two DPs were indirectly evaluated in two experiments, which summatively assessed the functional features of the prototype (each involving 12 graduate students) as well as by one expert practitioner</td></tr><tr><td>Coenen et al., 2018</td><td>6 DPs comprising 4 principles of form and function and 2 principles of implementation for the design and implementation of an information system for comparative judgement of competences (P1, P2)</td><td>The four principles of form and function were applied in designing five different Minimum Viable Product (MVP) instantiations</td><td>N/A during the first six evaluations of the MVP instantiations 1–3, since they were not developed in cooperation with any client organisations.Even though not clearly explained in Coenen et al. (2018), we interpret that the 4 DPs were indirectly evaluated (based on our interpretation that the remaining five evaluations of the MVP instantiations 4–5 in realistic organisations involved only members of the client organisations).</td><td>The four principles of form and function were indirectly evaluated six times in controlled settings, when evaluating the MVP instantiations 1–3. Most of the participants (assessors) can be regarded as external practitioners.Furthermore, MVP 3 was tested in three realistic organisation settings and MVP 2 in two.</td></tr><tr><td>Seidel et al. (2018)</td><td>4 DPs for designing IS support for organisational sensemaking in environmental sustainability transformations (P1)</td><td>The DPs were implemented in prototypes</td><td>Indirectly when formatively evaluating the prototypes</td><td>No</td></tr></table>

## Appendix B. A questionnaire template for light evaluation of reusability of design principles

The questionnaire should include a practitioner-oriented introduction of the design principles in terms of type (class) of system, the development (instantiation) of which they attempt to support (including proper introduction of the type of the system) (1–2 pages).

To what extent do you agree with the following statements (totally disagree, . . ., totally agree)?

## Accessibility

The design principles are easy for me to understand The design principles are easy for me to comprehend The design principles are intelligible to me

## Importance

In my view [Type X systems] address a real problem in my professional practice

In my view [Type X systems] address an important – acute or foreseeable – problem in my professional practice

## Novelty and insightfulness

I find that the design principles convey new ideas to me I find the design principles insightful to my own practice

## Actability and appropriate guidance

I think that the design principles can realistically be carried out in practice

I think that the design principles can easily be carried out in practice

I find that the design principles provide suficient guidance for designing [Type X systems]

I find that the design principles provide suficient direction for designing [Type X systems]

I find that the design principles are not restrictive when designing [Type X systems]

I find that the design principles provide me with suficient design freedom when designing [Type X systems]

## Efectiveness

I believe that the design principles can help design [Type X system] in practice

I find the design principles useful for designing [Type X system] in practice

Compared to my current situation, I believe that [Type X system] would improve my performance

Compared to my current situation, I believe that [Type X system] would increase my productivity

Compared to my current situation, I believe that [Type X system] would enhance my efectiveness in my job

Compared to the current situation, I believe that [Type X systems] would increase the quantity of products/services of my organisation/company

Compared to the current situation, I believe that [Type X systems] would improve the quality of products/services of my organisation/company

Compared to the current situation, I believe that [Type X systems] would improve the innovativeness of my organisation/company

Compared to my current situation, I believe that [Type X systems] would improve the reputation of excellence of my organisation/company

Compared to my current situation, I believe that [Type X systems] would improve the job morale of my organisation/company
