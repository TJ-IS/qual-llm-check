---
otero_id: 11950
otero_key: "MMR693Q9"
title: "An analysis of the traditional IS security approaches: implications for research and practice"
authors: "Mikko T Siponen"
year: "2005"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000537"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
European Journal of Information Systems (2005) 14, 303–315.

# An analysis of the traditional IS security approaches: implications for research and practice

Mikko T. Siponen

Department of Information Processing Science, University of Oulu, Linnanmaa, P.O. BOX 3000, Oulun yliopisto FIN-90014, Finland

Correspondence:

Mikko T. Siponen, University of Oulu, Department of Information Processing Science, Linnanmaa, P.O. BOX 3000, FIN-90014 Oulun yliopisto, Finland. Tel: þ 358 8 553 1984; Fax: þ 358 8 553 1890; E-mail: Mikko.T.Siponen@oulu.fi

## Abstract

Scholars have developed several modern information systems security (ISS) methods. Yet the traditional ISS methods – ISS checklists, ISS standards, ISS maturity criteria, risk management (RM) and formal methods (FM) – are still among the most used ISS methods. This study makes sense of these traditional ISS methods by comparing their underlying key assumptions. The main finding is that the traditional ISS methods regurgitate several features and assumptions that are required to be dealt with by traditional ISS methods developers and practitioners.

doi:10.1057/palgrave.ejis.3000537

Keywords: information security management; secure systems design

## Introduction

The expanding use of IS has increased the importance of information systems security (ISS). It is reported that 75% of surveyed organizations have confronted different security attacks (Bagchi & Udo, 2003, p. 684). In order to ensure that organizations’ assets are protected against such threats, several ISS methods have been put forward. While scholars have classified ISS methods into three (Baskerville, 1988, 1993) or five generations (Siponen, 2005), there is relatively little evidence on the use of the later-generation methods in practice. In contrast, the earlygeneration ISS methods (the first and second generation using the terminology by Baskerville, 1993 and Siponen, 2005), ISS checklists, ISS standards, maturity criteria, risk management (RM), and formal methods (FM), are reported to be the most commonly used ISS methods. Furthermore, these early-generation ISS methods have enjoyed a great deal of research and development efforts. For these reasons, it is necessary to take a critical look at the underlying assumptions and features of these early-generation ISS methods, called traditional ISS methods.

This paper analyses traditional (early generation) ISS methods: ISS checklists (e.g., Kraus, 1972; AFIPS, 1979; Wood et al., 1987), ISS standards (e.g., BS7799, 1993; Sanders et al., 1996; GASSP, 1999; Janczewski, 2000) and maturity criteria (e.g., Murine & Carpenter, 1984; Ferraiolo & Sachs, 1996; Hefner, 1997; SSE-CMM, 1998a, b), RM (e.g., Guarro, 1987; ; Halliday et al., 1996), and FM (Anderson, 1993; Barnes, 1998).

A critical analysis of these traditional ISS methods is valuable for researchers and practitioners alike. While these methods are widely used in practice, they are developed in isolation. Not surprisingly, the ISS market is glutted with an array of traditional ISS methods. Indeed practitioners are hard pressed to understand how these traditional ISS methods differ from one another (e.g., what is the difference between ISS standards and ISS maturity criteria?). This situation also prevents the upholding of a cumulative research tradition; hence, method developers may ‘invent the wheel again and again’. Without unveiling the assumptions and features of the traditional ISS methods, there is a risk that method developers concentrate on the nuance between these methods while ignoring fundamental problems, thereby inadvertently repeating certain undesirable assumptions.

The rest of this paper is organized as follows. The second section describes the traditional ISS methods and the criteria used to select the traditional ISS methods for this analysis. The third section presents the research strategy and framework for analysis. The fourth sifts through the ISS checklists, ISS standards, ISS maturity criteria, the RM methods and FM from the viewpoint of the analytical framework. The fifth section discusses the implications of this study. Finally, the key findings are summarized in the conclusions section.

## The research strategy and analytical framework

## Selection of traditional ISS methods

Baskerville (1988, 1992) classified ISS methods into three, and Siponen (2005) into five generations. Of these methods, classes of traditional ISS methods – checklists, ISS standards, ISS maturity criteria, RM and FM – reside in the first and second generations (Baskerville, 1992; Siponen, 2005). Interestingly, these methods are widely used in practice and enjoy ongoing development efforts by practitioners and scholars. ISS checklists and RM methods are reported to be widely used in practice (Baskerville, 1992; Fitzgerald, 1993; von Solms, 1996; Eloff & von Solms, 2000a, b; von Solms & Haar, 2000). The importance of ISS standards, such as Generally Accepted System Security Principles (GASSP, 1999), BS7799 (1993)/BS ISO/IEC17799 (2000) and ISS maturity criteria, such as SSE-CMM (1999a, b), have been highlighted widely by security practitioners and scholars (e.g., Fitzgerald, 1995; Ferraiolo & Sachs, 1996; Eloff & von

Solms, 2000a, b; Hopkinson, 2001; Janczewski, 2000; von Solms, 1996, 1997, 1998, 1999). Alternatively, computer (science) security scholars see the use of FM as the key to secure systems (Anderson, 1993; Barnes, 1998).

As it is possible in a journal article to analyse only a fraction of all the existing works within each of these classes of traditional ISS methods, selection criteria were employed. Webster & Watson (2002, pp. XV–XVI) suggest that a review article should not confine itself to methods originating in a certain geographical region and should not concentrate on premier journals only, ignoring articles presented in conferences. First, we selected ISS methods manifesting each class in different publication forums: journals, conferences and books. A selection of studies from these forums gives a richer picture of the underlying assumptions of the traditional ISS methods rather than restricting the selection of approaches to journals or books alone.

As the second criterion, we tried to include representatives of different geographical origins within each class of ISS methods. This criterion makes sense in two respects. It shows that the classes may not be geographically bound, and while ensuring that we do not favour a certain continent. The third criterion is to include in each class some studies that suggest alternative methods compared with the mainstream of that class. The fourth criterion was to choose representatives of both old and recent methods if possible.

Description of the traditional ISS methods This section describes the traditional ISS methods (Figure 1).

Checklists ISS checklists assume that ISS solutions and procedures can be observed and turned into a list: a checklist. From checklists practitioners can pick out the ISS solutions they need (Baskerville, 1993). The checklists selected for the analysis are the AFIPS checklist (1979), SAFE (Kraus, 1972), a business-oriented checklist (Moulton & Moulton, 1996) and a comprehensive control checklist (Wood et al., 1987).

The AFIPS, Kraus and Wood et al. checklists are perhaps the most well-known (Baskerville, 1992), and have been published in the form of books. The checklist of Moulton & Moulton (1996) represents a more recent journal approach.

![](/api/attachments/MMR693Q9/fulltext/images/1e64d2f06f058b7d660d5d2a37cb5837f6d2cddb2d778babca914b0b7cb0943b.jpg)  
Figure 1 The five classes of traditional ISS methods.

The AFIPS checklist is a generic ISS manual for ‘a variety of organizations: commercial, governmental, non-profit, small and large’ (AFIPS, 1979, p. 9). Rather than offering an all-inclusive list of the right ISS safeguards, it aims to provoke new and constructive thoughts on ISS. Typical of other checklists, AFIPS is also divided into areas, each of which includes from tens to hundreds of specific ISS questions.

The SAFE checklist (Kraus, 1972) encompasses 11 ISS areas (e.g., personnel practices, physical security). Furthermore, each area consists of several checkpoints, which are phrased in the form of concrete questions (e.g., ‘Are fingerprints taken and entered into the personnel records of job applicants?’). SAFE leaves the way open for adding areas of one’s own making and the corresponding new checkpoints.

The checklist of Moulton & Moulton (1996) endeavors to provide a fast and easy-to-access checklist for managers (Moulton & Moulton, 1996, p. 377). It poses questions in nine areas of ISS (Moulton & Moulton, 1996, p. 380).

The comprehensive controls checklist (Wood et al., 1987) offers an easy tool for ISS personnel to identify appropriate controls. It is organized into two main sections: ISS (with 11 subsections) and survivability (with two subsections).

ISS Standards Like a checklist, ISS standards aim to capture the best (industrial proven) practice and put it in the standards. However, standards differ from the checklists in three respects. First, ISS standards’ aim is to build international, authoritative and generic ISS standards, while the checklists’ goal is not as ambitious (but simply to offer organizations a list to begin with their ISS efforts). The second difference is presentational: while checklists do include a place where one can tick a box, standards do not. Third, ISS standards are typically expressed in terms of imperatives or goals (e.g., GASSP’s Ethics principles 2.1.3: ‘Information should be used, and the administration of information security should be executed, in an ethical manner’; GASSP, 1999, p. 36), where checklists typically present questions (e.g., ‘Are computer security related policies generally understood by staff?’; Wood et al., 1987, p. 29). The ISS standards chosen in this analysis are the BS ISO/IEC17799 (2000), GASSP (1999) and the baseline ISS guideline (Sanders et al., 1996). BS ISO/ IEC17799 (2000), the latest version of BS7799, is selected for this study due to the global attraction it received by scholars and practitioners (e.g., Kwok & Longley, 1997; von Solms, 1998; Eloff & von Solms, 2000a, b). GASSP (1999) represents another authoritative and international ISS standard (GASSP, 1999, pp. 29 and 33). Although GASPP is a North American-driven standard, it has an international board directing its development. While these two standards, BS ISO/IEC17799 (2000) and GASSP, were mainly developed by ISS practitioners, the baseline

ISS guideline was created by an academic research group (Sanders et al., 1996), and for this reason it has been included in the analysis.

ISS maturity criteria The ISS maturity criteria aim is to offer an objective scale for classifying ISS maturity. They typically offer five maturity levels (one poor, five high). The rationale for making an ISS maturity assessment is to show the level of ISS maturity to business partners and customers. Similar to ISS standards, ISS maturity criteria can also be used to improve an organization’s ISS without motivation for burnishing the organization’s image of trustworthiness to the public and partners.

Three ISS maturity criteria exist: the System Security Engineering Capability Maturity Model (SSE-CMM version 3.0), the ISS Maturity Grid (Stacey, 1996) and ISS metrics (Murine & Carpenter, 1984). These ISS maturity criteria were chosen for this analysis.

SSE-CMM (version 3.0) has received most attention (measured in articles in security forums) in the domain of maturity criteria. It is based on five maturity stages.

The ISS Maturity Grid (Stacey, 1996), which is influenced by the Quality Management Maturity Grid of Crosby (1979), also consists of five stages. The ISS metrics (Murine & Carpenter, 1984) in turn is based on the Software Quality Metrics.

Risk Management RM techniques aim to manage and control ISS risk. The general RM method (Saltmarsh & Browne, 1983), the LRAM approach (Guarro, 1987), the X-ifying RM method (Frisinger, 2001), the businessfocused RM method (Halliday et al., 1996) and the communication approach (Baskerville, 1991) were selected for this analysis.

The generic RM approach (Saltmarsh & Browne, 1983) is derived from existing RM techniques. This represents an approach published as a chapter of a book.

Contrary to the generic RM method (Saltmarsh & Browne, 1983), the business-focused RM method (Halliday et al., 1996) views the existing RM techniques as inappropriate for non-military and small organizations (and is therefore included in this analysis). They see that traditional RM methods are ‘more expensive than the acceptance of the risks’ (Halliday et al., 1996, p. 21). To address this problem, they propose a new RM method.

The X-ifying RM method (Frisinger, 2001) explores generic risk factors in different lines of business. This method is a representative of work published in a conference, and as a Scandinavian approach, it introduces geographical variation into this study.

LRAM provides a quantitative RM method developed by the U.S. Air Force (Guarro, 1987), in which risk can be presented in figures (representative of work published in a journal).

The communication approach (Baskerville, 1991) proposes that RM is a flawed technique for risk calculus, at least in the light of natural science posture, as it is guesswork (Baskerville, 1991). Alternatively, he suggests that the value of RM lies in providing a communication tool between developers and managers.

Formal methods FM methods insist that ISD should be based on formally validated components or carried out by FM. The FM community believes that the use of logic provides an appropriate way to ensure that the IS is secure. The use of FM in Anderson (1993) and Barnes (1998) is selected to represent the FM class.

## Framework for the analysis

A key question in a literature review is the selection of an appropriate conceptual framework used to organize and analyse the literature (Webster & Watson, 2002); The traditional ISS methods in this case. Fortunately, several such frameworks are available in IS literature. Iivari & Kerola (1983) have carried out a feature analysis of ISD methods, while Dhillon & Backhouse (2001), Hirschheim et al. (1995, 1996) and Iivari et al. (2001) have analysed ISD and ISS methods in the light of four sociological paradigms by Burrell & Morgan (1979). Alternatively, Iivari & Hirschheim (1996), Iivari (1991) and Iivari et al. (1998) analysed ISD methods in the view of research methods, organizational role and research objectives. Of these possible frameworks, we selected research methods, the organizational role of IS, research objectives and applicability to ISD as the conceptual framework for this study (Table 1). The rationale for selecting these is that while these viewpoints are successfully used to analyse different methods (Iivari, 1991; Iivari & Hirschheim, 1996; Iivari et al., 1998; Siponen, 2005), they are not employed to scrutinize the traditional ISS methods.

What are the research objectives of different ISS methods? Analysis of the traditional ISS methods in the light of the perceived research objectives is useful to highlight the possible goals of the researchers. Following Chua (1986), potential research objectives include (a) means-end oriented/technical, (b) interpretive, or (c) critical objectives. A means-end-oriented view holds that the aim of research is to produce knowledge in order to achieve certain concrete goals or ends and to increase human control over phenomena (Chua, 1986). The natural sciences are typically means-end oriented, although we can find means-end-oriented research aimed at finding causal explanation in the social or IS sciences, too.

Interpretive research means increasing people’s understanding of the meaning of their actions (Chua, 1986, p. 615), and it is therefore interpretive in nature, as opposed to research aimed at establishing causal relationships or statistical generalizations. The importance of interpretive research is widely advocated by historians, theologians, educationalists, social scientists, and has recently gained increased attention in the IS world (Hirschheim, 1985; Walsham, 1996; Klein & Myers, 1999). The aim of critical research is ‘ythe identication and removal of domination and ideological practice (Chua, 1986, p. 615).

What are the organizational roles attributed to ISS? They are (a) technical, (b) socio-technical, or (c) social. The technical view considers IS to be a technical artefact; the emphasis in ISD is on technical matters, with social implications being at best afterthoughts (Iivari & Hirschheim, 1996). From the technical view, poor technical quality and user resistance account for ISS problems, and users have no active role in ISS development.

The socio-technical view contends that technical and organizational systems are equally important (Iivari & Hirschheim, 1996), and the lack of an asymmetry between social and technical systems is seen as the source of ISS problems (Iivari & Hirschheim, 1996). In the socio-technical view, users have a moderate impact on ISS activities. Users’ preferences are recognized, and if users’ preferences are in conict with the ISS requirements, a compromise is sought.

The social view emphasizes the development of organizational systems before technical matters, and in this view the key to ISS success is socio-organizational desirability and meeting users’ preferences.

What research approaches have been used? By revealing the approaches used we are able to identify how the traditional ISS methods have been developed and validated and what evidence they are based on. IS research approaches are first divided into ‘approaches studying reality’ and ‘mathematical modelling’. Approaches studying reality are subdivided into ‘approaches stressing what reality is’ and ‘research stressing utility of artefacts’. The former is subdivided into ‘conceptual– analytical approaches’ and ‘approaches to empirical studies’. Approaches to empirical studies are in turn divided into ‘theory testing’ and ‘theory-creating’ approaches. The latter is divided into ‘artefact-building approaches’ and ‘artefact-evaluating approaches’. The concept ‘research approach’ operates at a higher level of abstraction than that of ‘research method’, which means that one research approach can be addressed by means of several research methods.

Table 1 Framework for the analysis

<table><tr><td>Viewpoints</td><td>References</td></tr><tr><td>(1) What are the research objectives?</td><td>Chua (1986) and Habermas (1984, 1987)</td></tr><tr><td>(2) What are the organizational roles of ISS?</td><td>livari &amp; Kerola (1983), livari &amp; Hirschheim (1996)</td></tr><tr><td>(3) What research approaches have been used?</td><td>Järvinen (1997, 2000)</td></tr><tr><td>(5) Are the ISS methods applicable to ISD?</td><td>Baskerville (1988; 1992)</td></tr></table>

The table presents the five viewpoints and their sources.

Are the ISS methods applicable to ISD? A situation where an ISS method cannot be integrated into ISD entails many problems (Baskerville, 1992). Such obstacles include conicting requirements between the normal and security functionality of IS, increased costs (security is added afterwards), user resistance, ISS problems (since it is more difficult to add security afterwards into IS) and malfunctions (Baskerville, 1992). Hence, it is important to explore which traditional ISS methods are applicable to ISD (Baskerville, 1993, p. 410). Accordingly, we separate three views with respect to the applicability of ISS methods to ISD. A traditional ISS method is (1) applicable to a certain (set of) ISD method or process, (2) potentially applicable, or (3) not presently applicable to an ISD. Potentially applicable means that even though the ISS method does not explicitly recognize the integration possibilities, we see similarities or a connection with ISD methods, making the integration possible. In a case where the ISS method is not applicable to ISD, the method does not provide any hint on how the present version of the approach can be integrated into ISD, nor do we see any connection to the phases of ISD.

## Results of the analysis

## Checklists

The research objectives All the checklists (SAFE by Kraus, 1972; AFIPS, 1979; Wood et al., 1987 and the Moulton & Moulton, 1996) encompass the means-end-oriented research objective. In addition, the AFIPS checklist also entails critical research.

The AFIPS checklist criticizes extant ISS methods for focusing on ‘horror stories’ and lacking practical advice on how to secure IS (AFIPS, 1979, p. 2), a critical research objective. To improve this problem, the AFIPS checklist offers a practical and cost-effective tool for managers to identify the necessary ISS controls: ‘ya primary purpose of this manual is to serve as a practical aid in the planning and the implementation of a thorough, effective computer security program’ (AFIPS, 1979, p. 2), a means-end-oriented research objective.

Similarly, SAFE advances a cost-efficient tool for improving ISS in organizations: ‘It [this checklist] enables management in all kinds of organizations to take immediate steps to deal with EDP securityy’ (Kraus, 1972, p. 2); again, a means-end-oriented view.

In the same vein, the Moulton & Moulton (1996) also provides an easy-to-use and ‘ya practical ten minute [ISS] checklist for business managers.’ (Moulton & Moulton, 1996, p. 377), a means-end-oriented research objective.

Like other checklists, the comprehensive control checklist (Wood et al., 1987) also aims to offer a practical and cost-efficient ISS tool: ‘The focus of the checklist has been to provide practical and cost-effective specific ideas for systems controls.’ (Wood et al., 1987, p. 8). This is a clear indication of the means-end-oriented view.

The organizational role of ISS SAFE entails a sociotechnical view; the comprehensive control checklist (Wood et al., 1987, pp. 1, 3–4); Moulton & Moulton’s (1996) checklist, lies between technical and socio-technical. The organizational role of the AFIPS (1979) checklist is technical.

The AFIPS checklist is also control oriented: ‘Security means control’ (AFIPS, 1979, p. 2). Accordingly, both the ISS problems and ISS success are related to the existence of proper ISS controls: ‘ycontrols should reduce mistakes’ (AFIPS, 1979, p. 2). This checklist also includes controls from ‘training and indoctrination programs’ to ‘codes of ethics’ to ensure that employees follow the given ISS procedures. These means are, however, used as instruments to enforce the ISS policy. Consequently, users have no direct impact on ISS. Such control orientation implies that AFIPS’ organizational role is technical.

SAFE (Kraus, 1972, p. 1) sees that management prudence is the key issue to protecting against different ISS treats and incidents. This indicates that the cause of ISS problems and ISS success is related to the management’s (dis)interest: social role. SAFE includes controls for both the technical and social system: a socio-technical view on ISS design priority. Like the AFIPS checklist, SAFE prescribes several checkpoints to monitor that employees comply with the defined ISS policy. The users’ impact on ISS is minimal (technical view on users’ impact on ISS). Hence, we deem SAFE as socio-technical.

The Moulton & Moulton (1996) checklist covers both social and technical systems (socio-technical role on ISS design priority). All risks are handled technically. Users have no impact on ISS. Instead managers need to ensure by control and other means that employees follow the given security policy (Moulton & Moulton, 1996, pp. 383): a technical role in relation to users’ impact on ISS. These granted, we judge the organizational role of ISS as being between technical and socio-technical.

The comprehensive control checklist (Wood et al., 1987, pp. 1, 3–4) sees that ISS problems result from hackers to disgruntled employees and industrial spies on the one hand, and managers’ ignorance and lack of building security in IS in the design stage, on the other. While managers’ ignorance may suggest a social role, other problems mentioned (hackers, lack of technical design at the beginning of ISD) are technical ISS problems. Hence, the socio-technical role is the cause of ISS problems. The comprehensive control checklist (Wood et al., 1987) states that ‘the focus of the checklist has been to provide practical and cost-effective specific ideas for systems controls’. Such controlling is extended to the social system as well: users have no active role in ISS, rather they are motivated and enforced with punishment in compliance with the ISS policy (technical role). Hence, the comprehensive control checklist (Wood et al.,

1987) lies between the technical and socio-technical views.

The research approaches used The AFIPS (1979), SAFE (Kraus, 1972) and Moulton & Moulton (1996) checklists are based on conceptual development, reflecting the authors’ experiences and opinions on the best set of ISS controls. While the comprehensive controls checklist (Wood et al., 1987) states that the checklist is developed on the basis of a U.S. Air Force project (Wood et al., 1987, p. v), no further information on this is given. Hence, we deemed the research approach as conceptual analysis.

Applicability to the ISD None of these checklists can be integrated into ISD. The checklists by AFIPS (1979), SAFE (Kraus, 1972) and Moulton & Moulton (1996) presume that IS is already developed and these ISS checklists are added afterwards to secure the IS. Hence, we deem that these ISS standards are not applicable to ISD. The comprehensive control checklist (Wood et al., 1987) recognizes the need to integrate ISS into ISD: ‘the checklist may also be an important reference tool for those creating or reviewing the design specifications of systems in the development process’ (Wood et al., 1987, p. 8). The checklist provides high-level questions to assist in this integration. However, we see that these high-level questions provide little guidance as such on how security aspects can be dealt with at different stages of ISD. Thus, the comprehensive control checklist is not applicable to ISD.

## ISS standards

The research objective BS ISO/IEC17799 (2000), the baseline ISS guideline (Sanders et al., 1996), entails a means-end-oriented research objective, while GASSP (1999) holds both means-end-oriented and interpretive research objectives.

BS ISO/IEC17799 (2000) endeavours to capture the best ISS practice for organizations’ use: ‘a comprehensive set of controls comprising best practices in information security. It is intended to serve as a single reference point for identifying the range of controlsy’ (BS ISO/ IEC17799, 2000, National foreword): a means-endoriented research objective.

GASSP (1999) offers a standard by which organizations can improve their ISS and ensure that the right ISS solutions have been implemented (GASSP, 1999, p. 29– 30). These indicate a means-end-oriented research objective. GASSP further attempts to increase organizations’ understanding of ISS through the standard: ‘to promote awareness of information security and GASSP’ (GASSP, 1999, p. 33). This can be seen as an interpretive research objective.

The baseline ISS guideline (Sanders et al., 1996) aims to offer an effective ISS tool: ‘The guidelines are intended to provide a straightforward means of identifying security weaknesses and validating existing systems to ensure compliance’ (Sanders et al., 1996, p. 189). This implies a means-end-oriented research objective.

The organizational role of ISS The organizational role of ISS is technical (Sanders et al., 1996; BS ISO/IEC17799, 2000) and socio-technical (GASSP, 1999).

BS ISO/IEC17799 (2000, p. 2) states that different interest groups (e.g., users, managers) need to be recognized in ISS development: ‘The security that can be achieved through technical means is limitedy[ISS] needs, as a minimum, participation by all employees in the organization’ (BS ISO/IEC17799 2000, p. viii). However, the users are regarded as a component to ensure that ISS risks are minimized for their part. For example, the controls should be selected on the basis of their costeffectiveness (BS ISO/IEC17799, 2000, p. x), not social factors (e.g., user acceptance). Moreover, ISS acceptance is based on a technical system such as performance (BS ISO/ IEC17799, 2000, p. 23); again user acceptance is not mentioned. Finally, the objective of user training is to ensure that users follow the given ISS policy (BS ISO/ IEC17799 2000, p 11). Therefore, users have no active role in ISS. Recognizing these, we deem the organizational role of BS ISO/IEC17799 (2000) as technical.

GASSP views that when employees’ fail to comply with ISS procedures, ‘it is more often the result of an ineffective or imperfect communication [...] rather than the result of wrongful motive or intent on the part of the personnel’ (GASSP, 1999, p. 41). This communicational problem implies a socio-technical view of the cause of the ISS problem. GASSP’s principles cover both social and technical systems; ISS design priority is socio-technical. It also states that ISS should recognize the organization culture and ethical issues in order to achieve acceptance of ISS solutions (GASSP, 1999, p. 36): ‘Use of information and information systems should match the expectations established by social norms, and obligations’ (sociotechnical role in ISS success and users’ impact on ISS). GASSP (1999, p. 36) insists that ISS activities should be accomplished in an ethical manner. This implies that social issues are not purely instrumental means for ensuring ISS. Social issues require equal consideration with technical issues; hence GASSP’s organizational role is socio-technical.

While the baseline ISS guideline (Sanders et al., 1996) offers both technical and social controls, it is aimed at achieving technical control. Users have no active role in ISS development: they should be enforced and motivated to follow the given ISS policy. As a result, the organizational role of the baseline ISS guideline is technical.

The research approaches used ISS standards are based on conceptual analysis.

GASSP is based on ‘information security textbooks and articles’ (GASSP, 1999, p. 34); a conceptual analysis. GASSP also states that it is based on observing existing industrial conventions (GASSP, 1999, p. 33). The practices included in GASSP must ‘become generally accepted by agreement (often tacit agreement)’ (GASSP, 1999, p. 33). Since no results of the empirical observations were provided, these observations were not classified as empirical research.

The research approach adopted by BS ISO/IEC17799 (2000) is similar to GASSP. BS ISO/IEC17799 (2000) states that it has also collected industrial practices: ‘the controls documented [in the standard] are widely accepted by large, experienced organizations as recommended good practices for all situations’. However, like GASSP, we see no use of an empirical research approach.

The baseline ISS guideline uses conceptual analysis to synthesize a draft version of the standard based on ‘ybooks, papers, international standards and local knowledgey’ on ISS (Sanders et al., 1996, p. 86). The draft version of the standard was then critically analysed and re-modified by the authors and selected practitioners, resulting in its final form: conceptual analysis.

Applicability to ISD None of the ISS standards are applicable to ISD. BS ISO/IEC17799 (2000) acknowledges that ISS ‘controls are considerably cheaper and more effective if incorporated at the requirements specification and design stage’ (BS ISO/IEC17799 2000, p. viii). However, BS ISO/IEC17799 (2000) does not offer any specific guidance as to how such incorporation is done in practice.

Similarly, GASSP recognizes the need to integrate ISS into ISD: ‘The security function must be fully integrated with system life cycle process. Retrofit, repair, and other late remedies are always ineffective and may be ineffective’ (GASSP, 1999, p. 45). However, GASSP’s guidance regarding such integration remains at a high–level: for example, ISS controls must be documented (GASSP, 1999, p. 45). Such advice gives little concrete help on how to actually integrate GASSP into ISD. Consequently, we conclude that GASSP is not applicable to ISD.

The baseline guideline focuses on adding ISS after normal ISD (Sanders et al., p. 82). As a result, we conclude that the baseline guideline is not applicable to ISD.

## ISS maturity criteria

The research objective The ISS metrics (Murine & Carpenter, 1984), SSE-CMM (2003) and ISS maturity grid (Stacey, 1996) involve a means-end-oriented research objective. The ISS metrics (Murine & Carpenter, 1984) also entail a critical research objective, and the ISS maturity grid also (Stacey, 1996) encompasses an interpretive research objective.

SSE-CMM proposes an effective criterion against which the maturity of ISS can be evaluated and IS secured: ‘The SSE-CMM is being developed to advance the state of practice of security engineering with the goal of improving the quality and availability of and reducing the cost of delivering secure systemsy.’ (SSE-CMM 2003, p. 6). This indicates a means-end-oriented research objective.

ISS maturity grid (Stacey, 1996) functions as a tool for increasing and measuring the maturity of ISS: ‘ya tool introduced to aid managers in the appraisal of an enterprise’s information security program’ (Stacey, 1996, p. 33): means-end oriented research objective. By explaining the ISS activities at the poor maturity levels, we see that the ISS maturity grid (Stacey, 1996) also aims to arouse managers to see organizational ISS weaknesses in their organizations: an interpretive research objective.

The ISS metrics (Murine & Carpenter, 1984, p. 214) see that ISS problems are often solved afterwards by patching up the security vulnerabilities, which are expensive and oriented on loss recovering; a critical research objective. Instead security should be built into the IS to prevent ISS violations. The ISS metrics are developed to address this need. They advance an ISS maturity criterion with the help of which developers can secure IS ‘in a continuous, cost effective and timely manner.’ (Murine & Carpenter, 1984, p. 208): a means-end-oriented research objective.

The organizational role of ISS The ISS maturity grid (Stacey, 1996) entails a socio-technical role. Other ISS maturity criteria (the ISS metrics by Murine & Carpenter, 1984 and SSE-CMM) hold a technical role.

The ISS metrics (Murine & Carpenter, 1984) see unauthorized access to IS as the key ISS problem, and proper access controls and auditing as the means to achieve ISS success (Murine & Carpenter, 1984, p. 207): a technical view on ISS problems and success. The design priority of ISS metrics is in the technical system, providing different ISS quality factors at different levels in the ISD cycle, while the users’ role is not mentioned (users have no role in ISS); hence, a technical role.

According to the ISS maturity grid (Stacey, 1996), those organizations at the low ISS maturity levels entail a technical organizational role: ISS is focused on technical systems. Technical ISS products are bought on the basis of advertisement talks, and these products are assumed to lead to ISS success. In the high maturity levels (4 and 5), it is realized that users’ needs and organizational applicability regarding ISS means must be recognized. In the high levels, users are ‘empowered and encouraged to evaluate and develop their own risk-based management strategies and to customize the enterprise’s existing information security program to respond to their own needs’ (Stacey, 1996, p. 27). Therefore, the higher-level organizations encompass the socio-technical organizational role of ISS.

While SSE-CMM include security awareness and training programs, they are controlled as technical components in technical systems: ‘The SSE-CMM was developed with the anticipation that applying the concepts of statistical process control to security engineering will promote the development of secure systems and trusted products within anticipated limits of cost, schedule, and quality’ (SSE-CMM 2003, p. 19). Such process control indicates a technical role: ISS problems result from a lack of systematic ISS processes, and process control is the key to ISS success. Users have no active role in ISS: a technical role.

The research approaches used All ISS standards are based on conceptual analysis.

A draft of SSE-CMM were developed in a workshop. This preliminary version was piloted in organizations (SSE-CMM, p. 8). These results were analysed in the second workshop, and the SSE-CMM were produced after ‘a consensus process’ (SSE-CMM 2003). Since no evidence of these pilots are given, we do not deem SSE-CMM as based on empirical research (hence, conceptual analysis).

The ISS maturity grid (Stacey, 1996) was derived from the quality management maturity grid (Crosby, 1979): a conceptual analysis.

ISS metrics (Murine & Carpenter, 1984) used conceptual analysis to deduce their method from software quality metrics (Murine & Carpenter, 1984, p. 208).

Applicability to ISD ISS metrics (Murine & Carpenter, 1984) are potentially applicable to ISD. Other ISS maturity criteria (The ISS maturity grid by Stacey, 1996 and SSE-CMM) are not applicable to ISD.

It might be possible to integrate the ISS metrics (Murine & Carpenter, 1984) into ISD given that the five milestones provided by the ISS metrics (e.g., analysis, design, testing) can be regarded as generic stages in ISD.

## Risk management

Research objectives The generic RM method (Saltmarsh & Browne, 1983) entails the means-end-oriented view, while the business-focused RM (Halliday et al. 1996) and X-ifying RM (Frisinger, 2001) methods hold both critical and means-end-oriented views. LRAM (Guarro, 1987) indulges in means-end-oriented and interpretive views.

The generic RM method (Saltmarsh & Browne, 1983, p. 96–106) provides a practical RM process with six phases for security managers: a means-end-oriented research objective.

The business-focused RM method (Halliday et al. 1996) criticizes the extant RM methods for concentrating on risks related to technical components, while the focus should be on the organizations’ critical business processes (Halliday et al., 1996, pp. 20–21): a critical research objective. To improve this situation, they offer a costeffective RM method ‘yby which risks can be prioritized and countermeasures can be selected and implemented on a cost-effective basis’ (Halliday et al., 1996, p. 21): a means-end-oriented research objective.

The X-ifying RM method criticizes traditional ISS methods, such as combining RM with BS7799, as offering ‘a black box with technology which solves all’ ISS problems (Frisinger, 2001, p. 294). These universal solutions fail to pay attention to organizational differences: a critical research objective. X-ifying RM endeavours to improve and rationalize the RM process by identifying generic risks in different fields of business: a means-end-oriented research objective.

LRAM put forward effective RM methods ‘it [LRAM] can be used to determine which specific security controls y can be effective and justifiabley’ (Guarro, 1987, p. 493). This indicates a means-end-oriented view. LRAM also aims to increase managers’ understanding of the business environment and its possible risks through the use of the RM methods (Guarro, 1987, p. 493). This is an interpretive research objective.

RM as a means of communication approach (Baskerville, 1991) argues that instead of a risk-predictive technique, RM should be seen as a communication tool: ‘Risk analysis is misconceived: its ostensible value as a predictive technique is less relevant than its value as an effective communications link between the security and management professionalsy’ (Baskerville (1991, p. 121). RM is seen as an exercise of guesswork, which may result in the implementation of costly and unnecessary ISS controls: a critical research objective. Rather, RM should be viewed as a communication tool, particularly for meeting managers’ decision-making needs:‘yrisk analysis [is]yan effective communication link between the security and management professionals who must make decisions concerning capital investments in information systems security’ (Baskerville, 1991, p. 121): an interpretive research objective.

The organizational role of ISS The X-ifying RM method (Frisinger, 2001) and the communication approach (Baskerville, 1991) entail a socio-technical role. The business-focused RM method (Halliday et al., 1996, p. 19) and LRAM (Guarro, 1987) subscribe to a technical role, while the generic RM method (Saltmarsh & Browne, 1983) lies between technical and social.

The generic RM method (Saltmarsh & Browne, 1983) recognizes that in the early stages of RM (stage of assets analysis), the input by different user groups is seen as important (indicating a socio-technical role). However, the acceptance of controls in the control selection phase is based only on the cost-effectiveness of controls, not on social or user acceptance (technical view). Hence, the generic RM method lies between technical and sociotechnical views.

In the X-ifying RM method (Frisinger, 2001), RM recognizes the need of paying attention and collecting ISS requirements from different user groups. This indicates a socio-technical role.

The business-focused RM method (Halliday et al., 1996, p. 19) sees the lack of network security as the main cause of ISS problems (technical view). The key to ISS success is the alignment of RM to organizations’ business strategies. To achieve this, the business-focused RM method has utilized a technical view: while managers’ empowerment is mentioned as an important issue, users do not seem to have an impact on ISS. Hence, we regard the organizational role of ISS as technical.

According to LRAM, ISS problems related to RM stem from a lack and non-use of proper quantitative RM methods (Guarro, 1987, p. 493): a technical role. LRAM aims to fill this gap, by improving RM through quantitative logic, indicating a technical role in ISS success in relation to RM. Users have no active role in LRAM: indicating a technical role in users’ impact on ISS.

The communication approach (Baskerville, 1991) focuses on improving the communication between managers and developers through the use of RM. Hence, the design priority is on the social system. Outside of developers and managers, the users’ active role in RM is not mentioned (technical role). Recognizing this, we deem the communication approach as socio-technical.

The research approaches used All RM approaches used conceptual analysis. Also, empirical research (the Xifying RM method) and mathematical modelling (LRAM) were utilized.

The generic RM method (Saltmarsh & Browne, 1983) deduced its approach from selected RM approaches; a conceptual analysis.

The business-focused RM method (Halliday et al., 1996) has used conceptual analysis to derive its conceptual RM method from Porter’s value chain to remedy weaknesses in prior RM methods.

The communication approach (Baskerville, 1991) builds an argument (conceptual analysis) to criticize traditional RM methods, and proposes an alternative role to see RM in the light of philosophy of science (conceptual analysis).

The X-ifying RM approach (Frisinger, 2001) uses a survey to find general risks in different lines of business (Frisinger, 2001, pp. 297–300), involving both theorytesting and creating research, and the survey is used as a research method. LRAM (Guarro, 1987) uses a conceptual analysis to argue in favour of quantitative approaches. Mathematical modelling is utilized to develop the RM semantics of the LRAM.

Applicability to ISD The RM methods are not applicable to ISD. The business-focused RM method (Halliday et al., 1996) proposes its own notation, which we see as unrelated to ISD methods. Moreover, they do not provide advice on how the notation can be added to ISD. Hence, we deem it as not applicable to ISD. The X-ifying RM method (Frisinger, 2001) and LRAM (Guarro, 1987) are designed to be used after IS has been built. Therefore, we judge that the X-ifying RM method (Frisinger, 2001) and LRAM are not applicable to ISD. Similarly, the communication approach (Baskerville, 1991) centres on the fundamental purpose of RM, not how RM can be integrated into ISD.

## Formal methods

Research objectives Anderson (1993) provides a tool for accomplishing a reliable and secure way to build IS:

‘Robust security designs are those that make their assumptions explicit, and so the design methodology must force the team to examine its assumptions in a systematic and careful manner.’ (Anderson, 1993, p. 40): a means-end-oriented research objective. Anderson also argues that the rigorous use of FM and public development are necessary – while currently missing practice – at least outside non-military ISD; a critical research objective.

Barnes (1998) aims to inform practitioners and researchers about the key strategies on how IS should be secured. This indicates an interpretive research objective.

The organizational role of ISS The organizational role of FM (Anderson, 1993 and Barnes, 1998) is technical. Anderson sees that ISS problems result from poor technical quality: careless use or non-use of an FM. He also sees that ISS flaws stem from closed development where the IS under development is not subordinated to public review (Anderson, 1993, p. 32). ISS success is achieved by explicitness in ISS development, achieved through the use of FM and open development (Anderson, 1993, p. 40); a technical role. Anderson recognizes the importance of proper training and management (Anderson, 1993, p. 39), but in our understanding, only as necessary components of building secure IS. Barnes (1998) agrees: ISS problems stem from the culture of secrecy, where the developers do not learn from past mistakes by developing secret cryptographic systems again and again. Also, FM and open development are the key factors leading to ISS success: ‘Formal methods, which have proven particularly useful in developing safety-critical systems, hold similar promise for addressing security problems’ (Barnes, 1998, p. 31): a technical role. For these reasons, we see that both Anderson (1993) and Barnes (1998) hold a technical view of the organizational role of ISS.

The research approach used The research approach favoured by Anderson (1993) and Barnes (1998) is mathematical modelling (use of FM).

Applicability to the ISD While Barnes (1998) does not mention how FM can be integrated into ISD, Anderson (1993, p. 38) also takes up the issue of integration, but does not suggest a concrete means by which this could happen. Thus, we deem the FM methods as not applicable to ISD.

## Discussion

Table 2 presents the results of the analysis of the traditional ISS methods.

## Research objectives

The most common research objective is means oriented, which held in 15 out of 17 methods. Only the communication approach (Baskerville, 1991) and FM by Barnes (1998) did not entail a means-end-oriented research objective. Six traditional ISS methods (out of 17 traditional ISS methods), namely AFIPS (1979) within checklists, ISS metrics (Murine & Carpenter, 1984) within maturity criteria, generic RM (Saltmarsh & Browne, 1983) method and the communication (Baskerville, 1991) approach within RM, and Anderson (1993) within FM, also entailed a critical research objective. In addition, GASSP (1999) within ISS standards, ISS maturity grid (Stacey, 1996) under maturity criteria, LRAM (Guarro, 1987) and the communication approach (Baskerville, 1991) within RM, and Barnes within FM, encompass interpretive research objective.

T<sub>a</sub> b l <sub>e</sub> 2 Th <sub>e</sub> <sub>res u</sub> l t<sub>s</sub> <sub>o</sub>f th <sub>e</sub> <sub>a n a</sub> l<sub>ys</sub> i <sub>s</sub>

<table><tr><td colspan="2">Classes of traditional ISS methods</td><td>Research objectives</td><td>Organizational role of ISS</td><td>Research approaches</td><td>Applicability to ISD</td></tr><tr><td></td><td>Methods</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">Checklists</td><td>AFIPS</td><td>Means-end oriented and critical</td><td>Technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td>SAFE</td><td>Means-end oriented</td><td>Socio-technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td>Moulton and Moulton</td><td>Means-end oriented</td><td>Between technical and socio-technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td>Wood et al.</td><td>Means-end oriented</td><td>Between technical and socio-technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td rowspan="3">ISS standards</td><td>BS ISO/IEC17799 (2000)</td><td>Means-end oriented</td><td>Technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td>GASSP</td><td>Means-end oriented and interpretive</td><td>Socio-technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td>Sanders et al.</td><td>Means-end oriented</td><td>Technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td rowspan="3">Maturity criteria</td><td>SSE-CMM</td><td>Means-end oriented</td><td>Technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td>ISS maturity grid</td><td>Means-end oriented and interpretive</td><td>Socio-technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td>ISS metrics</td><td>Means-end oriented and critical</td><td>Technical</td><td>Conceptual analysis</td><td>Potentially applicable</td></tr><tr><td rowspan="5">Risk mgt</td><td>Generic RM method</td><td>Means-end oriented</td><td>Between technical and socio-technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td>The business focused RM method.</td><td>Means-end oriented and critical</td><td>Technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td>The X-ifying RM method</td><td>Means-end oriented and critical</td><td>Socio-technical</td><td>Conceptual analysis, theory creating and testing empirical research; survey</td><td>No</td></tr><tr><td>LRAM</td><td>Means-end oriented, interpretive</td><td>Technical</td><td>Conceptual analysis, mathematical modelling</td><td>No</td></tr><tr><td>The communication approach</td><td>Interpretive, critical</td><td>Socio-technical</td><td>Conceptual analysis</td><td>No</td></tr><tr><td rowspan="2">Formal method</td><td>Barnes</td><td>Interpretive</td><td>Technical</td><td>Mathematical modelling</td><td>No</td></tr><tr><td>Anderson</td><td>Means-end oriented and critical</td><td>Technical</td><td>Mathematical modelling</td><td>No</td></tr></table>

It has been suggested that due to the social dimensions of IS, interpretive methods are needed (Hirschheim, 1985; Klein & Lyytinen, 1985; Walsham, 1996; Klein & Myers, 1999). We share this view: ISS research is not purely engineering research. ISS research is not only about the solving of concrete problems by introducing yet another method and tool. Interpretive studies are in order to enhance the practitioners’ and scholars’ understanding on complex ISS problems. Moreover, critical approaches are needed too. For Popper, science is essentially critical. Critical studies help us to recognize possible weaknesses in the dominant methods (as traditional ISS methods). Critical discussion is therefore an important tool to improve the current ISS thinking by showing the weaknesses in the status quo. Furthermore, university teachers are responsible for improving the practice through education (reform in education). Critical methods are needed for accomplishing such improvements.

The most common organizational role of ISS was the technical view, espoused by nine out of the 17 traditional ISS methods: AFIPS (1979) under ISS checklist, BS ISO/ IEC17799 (2000) and ISS baseline guideline (Sanders et al., 1996) within ISS standards, SSE-CMM (2003) and ISS metrics (Murine & Carpenter, 1984) within maturity criteria, the business-focused RM (Halliday et al., 1996) and LRAM (Guarro, 1987) methods within RM, and both FM (Anderson, 1993; Barnes, 1998) methods. A sociotechnical role is held by SAFE (Kraus, 1972) within the ISS checklist, GASSP (1999) within ISS standards, ISS maturity grid (Stacey, 1996) within maturity criteria, and the communication (Baskerville, 1991) and X-ifying RM methods under RM.

While the generic RM method (Saltmarsh & Browne, 1983) under RM, Moulton & Moulton (1996) and the comprehensive control (Wood et al., 1987) checklists within ISS checklists were between technical and sociotechnical, no traditional ISS method entailed the social view.

Consequently, while there are plenty of technical (traditional) ISS methods, practitioners have only a few socio-technical ISS methods – and no single social method – to choose from. Leading ISS commentators (Dhillon & Backhouse, 2001) have emphasized the need for socio-organizational ISS methods, since organizations are ultimately social institutions (Dhillon & Backhouse,

2001). In fact, technical methods may lead to problems in social organizations. An example of this is the users’ impact on ISS development. Regarding this, the control orientation was typical for the technical ISS methods. For example, the AFIPS (1979), the comprehensive control checklist (Wood et al., 1987) and the Moulton & Moulton (1996) checklist within checklists try to control human users in a similar manner to technical components or technical ISS problems. Codes of ethics, for instance, are utilized as instruments to manipulate employees to follow the ISS procedures (AFIPS, 1979). Such technical control, in which users are simply passive instruments and enforced or manipulated to comply with the given policy, may be problematic in the long run. It is a source of user dissatisfaction. It easily leads to ISS solutions that, in users’ perception at least, may be of little use and impede their normal work. Finally, when users’ impact on ISS development is minimal, users’ knowledge, relevant for securing systems, is not exploited properly. Consequently, traditional ISS methods must pay attention to social issues, such as users’ impact on ISS development. This is important to make sure that ISS solutions meet users’ expectations, which is necessary in ensuring that employees are motivated to comply with ISS solutions. Moreover, social methods recognizing users’ needs and concerns in ISS development guarantee that users’ knowledge on the application domain is exploited in ISS development.

## Research approaches used

The conceptual analysis was the most commonly used research approach (14 advocates out of 17). In addition, mathematical modelling was adopted by the FM methods (Anderson, 1993; Barnes, 1998) and the LRAM (Guarro, 1987) RM approach. Only the X-ifying RM method (Frisinger, 2001) used empirical, theory testing and creation, research (and survey as the research method). These results mean that practitioners do not have evidence (the one RM method being an exception) on the usefulness of these traditional ISS methods in practice.

Consequently, there is a need for rigorous qualitative and quantitative empirical studies, which explore the usability and relevance of the traditional ISS methods in practice. While all traditional ISS methods should be based on empirical studies, ISS checklists and ISS standards are excellent examples to illustrate the need of empirical studies. ISS maturity standards aim to show the security maturity level of all IS, while ISS checklists and ISS standards aim to capture the best (industrially proven) practice. Based on this best practice, the ISS standards form their international and authoritative standards that organizations should follow. Clearly, if ISS standards and ISS maturity criteria aim to meet such bold goals (show the security maturity of all IS, based on best practice, and offer the authoritative guideline), they must be based on proper empirical evidence.

Such empirical studies regarding the traditional ISS methods should cover how the different approaches affect organizations in different countries, of different sizes and in different lines of business. Such studies should address questions such as whether the ISS method adopted was worth all the investment made and what complications the use of an ISS method may have caused in organizations (IS maintainability, user and developer satisfaction) using the methods.

## Applicability to ISD

Only one traditional ISS method, ISS metrics by Murine and Carpenter, out of 17 traditional ISS method, is potentially applicable to ISD. Therefore, future traditional ISS methods, or their next versions, should provide explicit guidance on how these ISS methods can be smoothly integrated into ISD. For example, ISS methods should explicitly associate their ISS principles with the stages and methods of certain ISD methods. Additionally, qualitative studies are needed to explore the integrations of ISS methods to ISD methods (perceived problems, solutions to these problems, lessons learned, etc).

## Conclusions

We compared the underlying assumptions and features of the traditional ISS methods (ISS checklists, ISS standards, ISS maturity criteria, RM and FM methods) in light of

## About the author

Mikko Siponen is a Professor in the Department of Information Processing Science at the University of Oulu, Finland. His research focus is on IS security, IS development and ethical aspects of IS. His publication list includes 18 journal articles and more than 45 conference

## References

AFIPS (1979) Security: Checklist for Computer Center Self-Audits. AFIPS: USA.

ANDERSON R (1993) Why cryptosystems fail. Communication of the ACM 37(11), 32–44.

BAGCHI K and UDO G (2003) An analysis of the growth of computer and Internet security breaches. Communications of AIS 12, 684– 700.

BARNES BH (1998) Computer security research: a British perspective. IEEE Software 15(5), 30–33.

BASKERVILLE R (1988) Designing Information Systems Security. Information Systems Series, John Wiley: Chichester, UK.

BASKERVILLE R (1991) Risk analysis: an interpretative feasibility tool in justifying information systems security. European Journal of Information Systems 1(2), 121–130.

BASKERVILLE R (1992) The developmental duality of information systems security. Journal of Management Systems 4(1), 1–12.

BASKERVILLE R (1993) Information systems security design methods: implications for information systems development. Computing Surveys 25(4), 375–414.

research objectives, the organizational role of ISS, research approaches used and the applicability to ISD. The overall finding is that the traditional ISS methods regurgitate certain features and assumptions, which need to be taken into account by methods developers, researchers and practitioners using the traditional ISS methods. First, the prevailing research objective was means-end-oriented; more interpretive and critical studies were called for. While interpretive studies have an important role to increase practitioners’ and researchers’ understanding of the fundamentals of ISS, critical studies are needed to improve the current thinking ISS methods.

Most of the traditional ISS methods entail the technical view of the organizational role of ISS. This means that, overall, the importance of the socio-organizational nature of IS is not recognized seriously enough by traditional ISS methods. Consequently, the need for social ISS methods was highlighted. Most of the traditional ISS methods are based on conceptual development, offering little evidence on their usability and relevance in practice. Hence, the empirical studies are required to test and refine the traditional ISS methods in practical settings. Since only two traditional ISS methods can be integrated into ISD methods, future research and development related to traditional ISS methods must pay attention to this issue.

articles. He has received several academic awards, including the outstanding paper award in the 2000 volume of Information Management & Computer Security. He is currently an Associate Editor of The Journal of Information Systems Security.

BS7799 (1993) Code of practice for information security management. Department of Trade and Industry, DISC PD003. British Standard Institution, London, UK.

BS ISO/IEC17799 (2000) Code of Practice for Information Security Management. Department of Trade and Industry.

BURRELL G and MORGAN G (1979) Sociological Paradigms and organizational analysis. Heinemann: London.

CHUA WF (1986) Radical Developments in Accounting Thought. Accounting Review 61(5), 583–598.

CROSBY P (1979) Quality Is Free. NY: Penguin Books, New York, NY.

DHILLON G and BACKHOUSE J (2001) Current directions in IS security research: toward socio-organizational perspectives. Information Systems Journal 11(2), 129–156.

ELOFF MM and VON SOLMS SH (2000a) Information security management: a hierarchical framework for various approaches. Computers and Security 19, 243–256.

ELOFF MM and VON SOLMS SH (2000b) Information Security: Process Evaluation and Product Evaluation. Sixteenth Annual Working Conference on Information Security: Beijing, China.

FERRAIOLO K and SACHS JE (1996) Distinguishing security engineering process areas by maturity levels. Proceedings of the Ninth Annual Canadian Information Technology Security Symposium: Ottawa, Canada.

FITZGERALD KJ (1995) Information security baselines. Information Management and Computer Security 3(2), 8–12.

FRISINGER A (2001) Improving the protection of assets in open distributed systems by use of X-ifying risk analysis. Proceedings of the IFIP TC11 Sixteenth International Conference on Information Security: Paris, France.

GASSP (1999) Generally Accepted System Security Principles (GASSP). Version 2.0. Information Systems Security. June, vol. 8, no. 3.

GUARRO SB (1987) Principles and procedures of the LRAM approach to information systems risk analysis and management. Computer and Security 6(6), 493–504.

HABERMAS J (1984) The Theory of Communicative Action–Reason and the Rationalisation of Society, Vol I, Beacon Press, Boston, MA, USA.

HABERMAS J (1987) The Theory of Communicative Action–The Critique of Functionalist Reason, Vol II, Beacon Press, Boston, MA, USA.

HALLIDAY S, BADENHORST K and VON SOLMS R (1996) A business approach to effective information technology risk analysis and management. Information Management and Computer Security 4(1), 19–31.

HEFNER R (1997) A process standard for systems security engineering: development experiences and pilot results. Misc: Third IEEE International 1997 Software Engineering Standards Symposium and Forum, Emerging International Standards (ISESS 97).

HIRSCHHEIM R (1985) Information systems epistemology: an historical perspective. Proceedings of the IFIP WG 8.2. Working Conference on Research methods in information systems. Elsevier Science Publisher: Amsterdam.

HIRSCHHEIM R, KLEIN HK and LYYTINEN K (1995) Information Systems Development and Data Modelling: Conceptual and Philosophical Foundations. Cambridge University Press, UK.

HIRSCHHEIM R, KLEIN HK and LYYTINEN K (1996) Exploring the intellectua structures of information systems development: a social action theoretic analysis. Accounting, Management and Information Technologies 6, 1–64.

HOPKINSON JP (2001) Security standards overview. Misc: Proceedings of the Second Annual International Systems Security Engineering Conference. Orlando, FL.

IIVARI J (1991) A paradigmatic analysis of contemporary schools of IS development. European Journal of Information Systems 1(4), 249–272.

IIVARI J and HIRSCHHEIM R (1996) Analyzing information systems development: A comparison and analysis of eight IS development approaches. Information Systems 21(7), 551–575.

IIVARI J and KEROLA P (1983) A Sociocybernetic framework for the feature analysis of information systems design methodologies. In Information Systems Design Methodologies: A Feature Analysis (OLLE TW, SOL HG, TULLY CJ, Eds), pp 87–139, North-Holland: Amsterdam.

IIVARI J, HIRSCHHEIM R and KLEIN HK (1998) A paradigmatic analysis contrasting information systems development approaches and methodologies. Information Systems Research 9, 164–193.

IIVARI J, HIRSCHHEIM R and KLEIN HK (2001) A Dynamic Framework for Classifying Information Systems Development Methodologies and Approaches. Journal of Management Information Systems 17(3), 179– 218.

JANCZEWSKI L (2000) Managing Security Functions Using Security Standards. In Internet and Intranet Security Management: Risks and Solutions (JANCZEWSKI L, Eds), pp 81–105, Idea Group Publishing; USA.

JA¨RVINEN P (1997) The new classification of research approaches. In The IFIP Pink Summary – 36 years of IFIP (ZEMANEK H, Ed), pp 124–131, IFIP: Laxenburg, Austria.

JA¨RVINEN P (2000) Research questions guiding selection of an appropriate research method. Proceedings of the Eighth European Conference on Information Systems (ECIS 2000), July 3–5, Vienna.

KLEIN H and LYYTINEN K (1985) The poverty of scientism in information systems. In: Research methods in information systems (MUMFORD E et al. Eds), pp 131–161, Elsevier Science Publisher: Amsterdam.

KLEIN HK and MYERS MD (1999) A set of principles for conducting and evaluating interpretive field studies in information systems. MIS Quarterly 23(1), 67–94.

KRAUS LI (1972) SAFE: Security Audit and Field Evaluation for Computer Facilities and Information Systems. AMACOM, N.Y., USA.

KWOK L and LONGLEY D (1997) Code of practice: a standard for information security management. Proceedings of the IFIP TC11 International Conference on Information Security, Chapman & Hall, London, pp 78–90.

MOULTON RT and MOULTON ME (1996) Electronic communications risk management: a checklist for business managers. Computer and Security 15(5), 377–386.

MURINE GE and CARPENTER CL (1984) Measuring computer system security using software security metrics. In Computer Security: A global challenge (JH and Dougall EG, Eds), Finch Elsevier Science Publisher, Proceedings of the second IFIP International Conference on Computer Security (IFIP/Sec’84), Toronto, Ontario, Canada.

SALTMARSH TJ and BROWNE PS (1983) Data processing – risk assessment. In: Advances in Computer Security Management (WOFSEY MM, Ed), Vol 2, pp 93–116, John Wiley and Sons Ltd: New York.

SANDERS PW, FURRELL and WARREN MJ (1996) Baseline Security Guidelines for Health Care Management. In the SEISMED Consortium (eds), Data Security for Health Care: Volume 31: Management Guidelines, Baseline Security Guidelines for Health Care Management pp 82–107, IOS Press: The Netherlands.

SIPONEN M (2005) Analysis of modern IS security development approaches: towards the next generation of social and adaptable ISS methods. Information and organization in press.

SSE-CMM (1998a) The Model. v2.0. http://www.sse-cmm.org.

SSE-CMM (1998b) The Appraisal Method. v2.0. http://www.sse-cmm. org.

SSE-CMM (1999a) The Model. v2.0 and v3.0. http://www.sse-cmm.org.

SSE-CMM (1999b) The Appraisal Method. v2.0 and v.3.0. http:// www.sse-cmm.org.

SSE-CMM (2003) Systems security engineering capability maturity model<sup>s</sup> available at http://www.sse-cmm.org/docs/ssecmmv3final. pdf.

STACEY TR (1996) Information security program maturity grid. Information Systems Security 5(2), 22–33.

VON SOLMS R (1996) Information security management: the second generation. Computers and Security 15(4), 281–288.

VON SOLMS R (1997) Driving safely on the information superhighway. Information Management and Computer Security 5(1), 20–22.

VON SOLMS R (1998) Information security management (3): the code of practice for information security management (BS 7799). Information Management & Computer Security 6(5), 224–225.

VON SOLMS R (1999) Information security management: why standards are important. Information Management and Computer Security 7(1), 50–58.

VON SOLMS R and VAN DER HAAR H (2000) From Trusted Information Security Controls to a Trusted Information Security Environment. Information Security Sixteenth Annual Working Conference on Information Security: Beijing, China. pp 29–36.

WALSHAM G (1996) The emergence of interpretivism in IS research. Information Systems Research 6(4), 376–394.

WEBSTER J and WATSON RT (2002) Analyzing the past to prepare for future: writing a literature review. MIS Quarterly 6(2), xiii–xxii.

WOOD CC, BANKS WW, GUARRO SB, GARCIA AA, HAMPEL VE and SARTORIO HP (1987) Computer Security: A Comprehensive controls Checklist. John Wiley and Sons: New York.
