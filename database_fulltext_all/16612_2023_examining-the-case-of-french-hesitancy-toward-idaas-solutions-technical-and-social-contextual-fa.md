---
otero_id: 16612
otero_key: "AH84K4W7"
title: "Examining the case of French hesitancy toward IDaaS solutions: Technical and social contextual factors of the organizational IDaaS privacy calculus"
authors: "Christine Abdalla Mikhaeil; Tabitha L. James"
year: "2023"
journal: "Information & Management"
doi: "10.1016/j.im.2023.103779"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Examining the case of French hesitancy toward IDaaS solutions: Technical and social contextual factors of the organizational IDaaS privacy calculus

Christine Abdalla Mikhaeil, Tabitha James

## To cite this version:

Christine Abdalla Mikhaeil, Tabitha James. Examining the case of French hesitancy toward IDaaS solutions: Technical and social contextual factors of the organizational IDaaS privacy calculus. Information and Management, 2023, 60 (4), pp.103779. ⟨10.1016/j.im.2023.103779⟩. ⟨hal-04130774⟩

HAL Id: hal-04130774 https://hal.science/hal-04130774v1

Submitted on 31 Mar 2025

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L’archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la difusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d’enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

Version of Record: https://www.sciencedirect.com/science/article/pii/S0378720623000277 Manuscript\_cb33b6881ca2020e199f2f29ead25443

# Examining the Case of French Hesitancy Toward IDaaS Solutions: Technical and Social Contextual Factors of the Organizational IDaaS Privacy Calculus

Christine Abdalla Mikhaeil\*

Assistant Professor

Department of Innovation, Entrepreneurship and Information Systems

IESEG School of Management, Univ. Lille,

CNRS, UMR 9221 - LEM - Lille Economie Management,

F-59000 Lille, France

3, rue de la Digue, 59000 Lille, France Phone :+33 (0)3 20 54 58 92 c.abdallamikhaeil@ieseg.fr

Tabitha L. James

Professor

Department of Business Information Technology

Pamplin College of Business

Virginia Tech

1007 Pamplin Hall, Blacksburg, VA, 24061

Phone: 540-231-3163

tajames@vt.edu

\*Corresponding Author

# EXAMINING THE CASE OF FRENCH HESITANCY TOWARD IDAAS SOLUTIONS: TECHNICAL AND SOCIAL CONTEXTUAL FACTORS OF THE ORGANIZATIONAL IDAAS PRIVACY CALCULUS

## ABSTRACT

Identity-as-a-service (IDaaS) is a cloud security service to which companies can outsource the identity and access management (IAM) functions that administer their employee’s access to organizational resources. Engaging with the information systems (IS) privacy literature, our qualitative analysis develops a framework for an organizational privacy calculus that informs French organizational consumers’ decisions to pursue IDaaS solutions. We collect data from employees of a multinational IDaaS provider operating in Europe but headquartered in the US. Our case study reveals the organizational privacy calculus associated with transferring control of a primary security control to a multinational cloud service provider.

KEYWORDS: cloud computing, cloud security, identity-as-a-service (IDaaS), privacy calculus

## INTRODUCTION

Cloud computing involves a client paying for on-demand resources (e.g., services, applications, servers) that run on computing infrastructure that a cloud provider manages and maintains but provisions to the client [40]. It is common for companies to contract cloud resources from multiple cloud providers, which is referred to as a multicloud configuration. A hybrid cloud environment occurs when on-premises information technology (IT) resources are used in conjunction with cloud offerings. When companies combine both on-premises computing resources with multiple cloud offerings (private or public), it is referred to as a hybrid multicloud environment, and it has been reported that 94% of companies are operating such environments [14]. Managing employee access to hybrid multicloud environments is a challenge that has resulted in companies offering identity-as-a-service (IDaaS), which is a cloud-based identity and access management (IAM) service [e.g., 24].

IAM involves “people, processes, and systems that are used to manage access to enterprise resources by assuring that the identity of an entity is verified, and then granting the correct level of access based on this assured identity” [56]. IAM is a critical component of organizational security and has historically been a challenging one to implement [4, 42, 46]. Improperly managing identities and access is a major source of organizational security risk with reports citing the use of stolen credentials in 29%, and the misuse of computing resources by authorized users in 15%, of security breaches in 2019 [62]. Although critical to the security infrastructure of all organizations, IAM has been described as “a costly and time-consuming task” [44]. Notably, the IAM infrastructure built 10–15 years ago for most companies is outdated, fragile, and misaligned with the current threat landscape that is shaped by technological developments such as increasing reliance on mobile and cloud applications and Internetof-things (IoT) devices [4, 42, 46]. Consequently, it is important for companies to investigate the benefits and risks of IAM technologies such as IDaaS solutions that may help secure complex hybrid multicloud environments.

Approximately 75% of North American and 50% of European companies are considering IDaaS delivery models for their new IAM implementations [30]. However, implementing IDaaS requires companies to entrust sensitive employee identity information to a cloud service provider. Companies considering a move to IDaaS must weigh the risks of entrusting employee data and the management of a key security mechanism to a third party against the benefits of updating their IAM services to potentially be better suited for the complex hybrid multicloud environments that companies are increasingly employing for their IT infrastructures. The privacy calculus can be described as “a rational process guided by an internal cognitive assessment of (1) the anticipated costs (or risks) and (2) the perceived benefits connected to the provision of personal data” [28, p. 607]. Although the privacy calculus is often studied at the individual privacy decision level [e.g., 16, 20, 28], it has been suggested that it is applicable at the organizational level [8, 22, 38]. The privacy calculus at the organizational level entails organization-to-organization data disclosure rather than person-to-organization or person-to-person. We frame the IDaaS solution benefit–risk tradeoff as an organizational privacy calculus because a company is considering the organizational benefits of an IDaaS solution against the risks of sharing organizational data with the IDaaS provider.

Our study was prompted by a request from a multinational technology company, henceforth referred to as “TechCorp,” that was experiencing resistance to their IDaaS solution in the French market. TechCorp wanted to better understand the reasons their French clients were hesitant to purchase or implement their IDaaS offering despite TechCorp having a significant foothold in the French market for other technologies and achieving success in other markets with their IDaaS solution. We conducted an exploratory case study, during which we analyzed internal documents and interviewed employees working on the IDaaS offering. Our data were thus collected from employees of TechCorp who were engaged in marketing, selling, and implementing the IDaaS solution in the French market. Notably, TechCorp is not the company that owns the

identity data but would be the company managing the identity data if the IDaaS solution is implemented by the client. Because the IDaaS solution is a security offering and requires any company implementing it to entrust TechCorp with valuable employee identity information, we turned to the information systems (IS) privacy literature to guide our analysis, specifically the privacy calculus literature that conceptualizes information disclosure decisions as benefit–risk tradeoffs [e.g., 8, 20, 22, 28, 38].

In our case study, we examine the perceived resistance of French clients to an IDaaS offering from TechCorp, a multinational corporation headquartered in the US. TechCorp successfully offers other products in the French market, and thus TechCorp is not a new company trying to gain a foothold in the French market. However, the technical characteristics of security cloud products can be complex, and the consequences of this complexity are difficult to understand within different regulatory environments, thereby potentially creating a novel uncertainty around the IDaaS product. The sociotechnical perspective in IS “considers the technical artifacts as well as the individuals/collectives that develop and use the artifacts in social (e.g., psychological, cultural, and economic) contexts” [50, p. 696]. We propose that the context of our case study is a notable consideration because companies are considering the partial or full transference of the management of an important component of their security infrastructure to a company headquartered outside of their own country. Therefore, we consider both the perceived technical and social benefits and risks associated with the IDaaS organizational privacy calculus.

IDaaS is an IAM security solution, and hence requires organizational identity information to function; that is, the sharing of such data is not optional. Moreover, IDaaS is offered for complex hybrid multicloud environments, and cloud environments can obscure the underlying infrastructure, making understanding the risks associated with how data will be collected, stored, and transferred more difficult to explain and understand. Notably, there are four potential decisions that companies can make: (1) not purchase the IDaaS solution; (2) delay the purchase of the IDaaS solution; (3) partially

implement the IDaaS solution, which means that the IDaaS solution may manage some identities for some but not all services and data the company needs to protect; and (4) fully implement the IDaaS solution, which completely replaces the company’s old identity services with the IDaaS solution. A partial implementation may be a stepping stone to a full implementation during which companies can obtain a better feel for the benefits and risks associated with the IDaaS solution. Our research question is as follows: How do perceived technical and social benefits and risks shape the organizational privacy calculus that informs companies’ considerations of which IDaaS implementation (i.e., not at all, lagged, partial, or full) to pursue? By examining this question, we can propose and examine a novel organizational privacy calculus within its sociotechnical context. The privacy calculus has rarely been considered at the organizational level [8, 22, 38], and our IDaaS context is unique in that IDaaS implementation can be viewed as exchanging organizational information for organizational benefits. From a practical standpoint, we can provide TechCorp with guidance regarding what their employees can do to adjust their marketing materials and sales approaches to better explain the risks associated with their IDaaS solution in ways that may assuage their clients’ concerns and how to highlight the benefits associated with their IDaaS solution.

## THEORETICAL BACKGROUND

## Privacy Calculus

The concept of a privacy calculus is drawn from privacy research that describes a “calculus of behavior” [34, p. 35]. The fundamental premise of the calculus of behavior is that when an entity considers disclosing information, they must also consider the future consequences of doing so. Laufer and Wolfe [34] discuss three factors that can disturb the calculus: (1) entities may minimize the potential consequences of information disclosure, especially in cases in which there is a desired benefit obtained from the disclosure; (2) the consequences of information disclosure may be difficult to foresee; and (3) new technologies may be developed that change the consequences of disclosure.

IDaaS is a new technology that changes the way organizational identities and access to organizational resources are managed, shifting the management responsibility to an outside organization. Therefore, the responsibility to secure the data to manage the IAM function is also shifted to that outside organization. Moreover, the technology is cloudbased, which can lead to new and uncertain security risks, as well as be challenging to explain or understand. Relatedly, because the technology is new, the consequences of the data disclosure necessary to implement IDaaS are more difficult to foresee.

The calculus of behavior entered the IS literature when researchers needed to consider the reasons consumers disclosed data to companies and the consumers’ perceptions of the secondary use of the disclosed data [e.g., 15]. In this context, “individuals surrender a measure of privacy in exchange for some economic or social benefit, based on the ‘calculus of behavior,’ an assessment of their ability to manage any of the consequences of today’s choices in the future” [15, p. 344]. In subsequent research, the idea that individuals trade privacy for contextual benefits became the privacy calculus: “consumers behave as if they are performing a ‘cost-benefit’ analysis, or what we refer to as the ‘privacy calculus’ [cf. 34], in assessing the outcome they receive as a result of providing personal information to organizations” [17, p. 327]. The privacy calculus was originally presented as a simple cost–benefit analysis, in which information was disclosed if the benefits of disclosure exceed the risks [e.g., 16], and this conceptualization remains popular in the literature [e.g., 8]. The privacy calculus has been used to examine disclosures between consumers and companies [e.g., 20, 28, 63], individuals and other people on social media [e.g., 25, 29], and even between groups (e.g., organization-toorganization) [8].

The privacy calculus informs the privacy decision; in other words, the potential benefits that may be obtained from releasing the information are weighed against the potential risks before the privacy decision is made [8]. In the IDaaS privacy calculus, organizations working with TechCorp to determine whether to pursue an IDaaS solution and at what level (i.e., partial or full) may have different levels of knowledge about the product or the contextual details (e.g., legal or regulatory environment). This is similar to other privacy decisions, in which a customer makes a decision to release information to a company without fully understanding the future consequences (i.e., risks) of that disclosure. We acknowledge that in the case of an IDaaS solution, some details will be specified in a contract if the solution is purchased, but if the marketing and sales teams cannot first engage the consumer, then a contract may never be explored. Our interest is in determining the elements of the initial privacy calculus that determines whether a company will pursue an IDaaS solution, and how this initial privacy calculus guides whether companies hedge their risks (e.g., pursue a partial IDaaS solution) or go “all in” (e.g., pursue a full IDaaS solution).

IDaaS is an IAM mechanism, which means it requires employee identity data to be implemented. Therefore, unlike other cloud services, organizations considering potentially pursuing an IDaaS solution are faced with a unique privacy calculus because they must entrust sensitive organizational identity information to the cloud provider to achieve the benefits of IDaaS. We thus frame the decision to adopt IDaaS as an organizational privacy calculus and examine the cost–benefit tradeoff of disclosing organizational data for organizational benefits. Unlike much research that considers a privacy calculus in which the individual consumer balances the tradeoff between the potential risks of disclosing his or her own personal information in return for potential personal benefits [20, 25, 28], Greenaway et al. [22] proposed an organizational privacy calculus in which an organization balances the tradeoff between the privacy protections afforded to its customers and potential organizational objectives or benefits. Other researchers have similarly argued that groups (e.g., organizations) face tradeoffs in how they manage the customer information they steward and potential benefits from disclosing that information [8, 38]. We conceptualize an organizational privacy calculus that considers the tradeoff between the potential risks associated with an organizational data disclosure decision (i.e., to share employee identity data) with another organization and the organizational benefits that might be obtained from pursuing an IDaaS solution.

This conceptualization is different from the others because it is organizational employee data being disclosed for organizational benefits.

Dinev and Hart [20] proposed an extended privacy calculus model that includes contrary beliefs that comprise elements of a privacy calculus. Specifically, they examined how risk, privacy concern, trust, and benefits of internet use affect people’s willingness to conduct e-commerce transactions. Following the framework of a cost–benefit analysis, Dinev and Hart [20, p. 63] separate the elements into “polarities” referred to as “risk beliefs” (risk and privacy concern) and “confidence and enticement beliefs” (trust and benefits). Others have taken a similar approach but added or omitted elements or modified the relationships in the model [e.g., 19, 25, 28, 29, 63]. What is common among the privacy calculus literature is that the perceived risks of information disclosure are weighed against the perceived benefits.

IDaaS is a technical security control that needs to be embedded within a social context. Thus, there are risk beliefs and confidence and enticement beliefs about the technical security control itself, such as the level of security the control can provide, the data that need to be disclosed for the control to function, and the compatibility of the control with the existing infrastructure. However, the decision to pursue the IDaaS solution is taking place in a social context, specifically, France. Therefore, there are risks and confidence and enticement beliefs that arise from that social context such as concerns over the regulatory and legal environment and culturally embedded levels of uncertainty and trust. Such technical and social risk and confidence and enticement beliefs may or may not be knowable; however, what is key is what TechCorp’s organizational clients believe them to be when TechCorp works with them because these beliefs determine whether the IDaaS solution is pursued and at what level (i.e., partial or full).

We draw this distinction between social and technical risk and confidence and enticement beliefs based on the sociotechnical perspective in which researchers examine both the technology and the social contexts (psychological, cultural, and economic) in which the technology is or will be used [50]. Effective security, which can be defined as “systems that are secure even when used by human,” has been described as “inherently socio-technical (it depends on how human and technical aspects integrate and it may be context and culture (incl. education) dependent” [21, p. 318]. The value of traditional cloud computing has also been conceptualized to have both technical (e.g., on-demand self-service, security concerns) and social attributes (socioenvironmental competitive pressure, social relationships) [37]. Our cloud security context thus necessitates the investigation of the roles that both the technical and social contextual aspects play in how the organizational IDaaS privacy calculus materializes for TechCorp’s clients.

## Risk Beliefs

In their extended privacy calculus model, Dinev and Hart [20, p. 63] separate the elements of the privacy calculus into “polarities” referred to as “risk beliefs” (risk and privacy concern) and “confidence and enticement beliefs” (trust and benefits). In this subsection, we discuss risk beliefs, including risk and privacy and security concerns. In the next subsection, we discuss confidence and enticement beliefs, including benefits and trust.

Studies that have considered privacy concerns have sometimes also included the concept of security concern, which are related yet arguably unique concerns [6, 39, 48]. Although arguments have been made that one type of concern may subsume the other or that they can be combined into one construct, security concerns are often related to safety and protection (e.g., the confidentiality, integrity, and availability protections afforded to data), whereas privacy concerns focus on information control and confidentiality with regard to data handling and stewardship [6, 39, 48]. It has been argued that perceptions of risk and uncertainty are embodied in security and privacy concerns [39]. Security and privacy concerns are noted in many studies of cloud services [1, 3, 7, 9, 27, 31, 35, 37, 43, 54, 59]. For example, companies considering the use of cloud services often express “concern with storing sensitive data on the cloud” [7, p. 222]. Specific concerns include knowing where the data centers are housed and the “legislative practices of the jurisdiction in which they’re located” [43, p. 99].

Risk is associated with uncertainty [20], and the internet environment has been described as being characterized by risk and uncertainty [19]. IDaaS is a cloud technology, and hence, it operates over the internet and could be viewed as risky. Moreover, France is a high-uncertainty-avoidance culture, and prior privacy calculus research has found that higher uncertainty avoidance cultures have higher sensitivities to potential risks [19]. Uncertainty avoidance is a national cultural value that reflects the level of risk that people in a culture or country are willing to accept and thus is used to relate the tendency of a particular culture or country to feel threatened by uncertain situations [55]. France is a high uncertainty-avoidance country in which people are “keen to avoid uncertainty, and to try to cope by reducing as far as possible the unpredictability of life” [52, p. 5]. Cultural differences in uncertainty avoidance are likely to manifest as hesitance when technical and social contextual factors are uncertain, or simply not properly conveyed, and could be perceived to increase risk. For example, a product offering from a company headquartered in a different country that requires the release of sensitive data may appear risky, especially initially when the social context is not well understood.

Both technical and social contextual aspects of the IDaaS solution may appear risky to clients when they are initially encountered. There is often uncertainty associated with internet-based technologies [19], and cloud technologies are internet based. Because, in our case study, the IDaaS provider is headquartered outside of the European Union (EU), clients may also face initial uncertainty regarding privacy and personal data regulations and compliance. Compliance and regulatory risk is particularly important because the understanding of privacy and protection of personal data varies significantly between the EU and the US [13, 53]. Although such uncertainty may be reduced with proper education, the initial perceptions of the risks associated with an IDaaS solution may determine whether it is pursued and whether there is time to correct initial misconceptions.

## Confidence and Enticement Beliefs

The US National Institute for Standards and Technology lists five essential characteristics of cloud computing: on-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service [40]. Many of the benefits of cloud computing identified in research map to these essential characteristics [7]. For example, “increases scalability” [43, p. 98], “fast implementation,” “cost advantage,” and “accessibility” [3, p. 8] all result from being able to provision resources on demand and thus pay only for the resources the company needs. These benefits are largely technical and therefore quite standard across cloud services. Moreover, IDaaS is a security mechanism (i.e., a SECaaS offering), which means that IDaaS solutions are intended to provide beneficial security services for complex IAM needs. Specifically, the Cloud Security Alliance (CSA) defines SECaaS as “the provision of security applications and services via the cloud either to cloud-based infrastructure and software or from the cloud to the customers’ on-premise systems” [56]. Among the categories of SECaaS services, IAM is “central to the secure adoption of cloud services” [11] because it includes not only identification and authentication but also access and profile management [2].

Trust is commonly included in privacy calculus models [16, 19, 20, 28, 29]. The logic is that if trust in the involved parties is high, disclosure is more likely. Culnan and Armstrong [16] argue that organizations that can build trust with their consumers will ultimately be more readily entrusted with consumer information because trust minimizes the risks of disclosure. Trust is critical to entities considering data disclosure [19, 20, 28]. Moreover, France is described as a low-trust society [61], which suggests that TechCorp’s clients may not be inclined to easily trust. Lansing and Sunyaev [33, p. 71] developed a trust framework for cloud computing in which two types of overarching trust were considered: (1) institution-based trust, which refers to “beliefs about the general effectiveness of safety nets or safeguards provided by a marketplace, legislation, or other institutions in the cloud computing environment”; and (2) trust in the cloud ecosystem, which refers to “a generalized belief in the network of providers and the supporting

technology infrastructure across situations.” Yu et al. [65] also considered institutional trust and IT artifact trust, which map to the two types of trust defined by Lansing and Sunyaev [33]. Such trust frameworks indicate that trust (or distrust) in governments and legislation, cloud providers, and cloud technology may all play a role in an IDaaS privacy calculus. Similarly, we expect trust to be important and multifaceted in our study.

The overarching framework of our situational organizational privacy calculus for IDaaS is shown in Table 1. We will use this framework, derived from the literature, to guide our analysis.

Table 1: Situational Organizational Privacy Calculus for IDaaS

<table><tr><td>IDaaS Privacy Calculus</td><td>Technical</td><td>Social</td></tr><tr><td>Confidence and enticement beliefs (trust and benefits)</td><td>Provides improved use of IT resourcesSecurity control that can improve IAM management</td><td>Trust in institutions (e.g., governments and legislation, organizations, IT)</td></tr><tr><td>Risk beliefs (risk and privacy/security concerns)</td><td>Security concerns related to safety and protection of dataPrivacy concerns related to control and confidentiality of data</td><td>Uncertainty (perceptions of risk) associated with the regulatory environment</td></tr></table>

## RESEARCH METHODOLOGY

To explore the IDaaS privacy calculus, we conducted an exploratory single case study [64]. Case studies are valuable when “a phenomenon is broad and complex, where the existing body of knowledge is insufficient to permit the posing of causal questions, when a holistic, in-depth investigation is needed, and when a phenomenon cannot be studied

outside the context in which it occurs” [47, p. 233-234]. The case study method fits well with our task to examine the IDaaS privacy calculus in France because our interest lies in the technical and social contextual nuances informing companies’ considerations of a novel cloud service in a specific cultural context. Following the prior privacy calculus literature and our framework derived from it in Table 1, we asked about what TechCorp’s clients in the French market saw as the benefits and risks of the IDaaS solution. Our semi-structured interviews were designed knowing that exploratory case study methods may reveal unexpected benefits and risks associated with IDaaS by French clients. Our aim was to determine context-specific factors that explain the hesitancy of French clients to engage with TechCorp’s IDaaS solution, as well as to identify context-specific benefits of IDaaS that could be leveraged to increase interest in TechCorp’s IDaaS solution. Two key elements distinguish our sociotechnical context: (1) that IDaaS is a security mechanism that requires sensitive organizational employee identity data to be shared and (2) that the IDaaS is a product from a US-headquartered company being considered for use by French companies.

## Case Selection

TechCorp is a large multinational consulting and IT implementation services company that specializes in cybersecurity services. It operates in 100 countries and has more than 15,000 customers globally. Although TechCorp is headquartered in the US, TechCorp France is an integrated business unit with its own operational and technical services and sales unit.

TechCorp France’s IDaaS solution is not its first foray into IAM. For 15 years, it has offered a market-leading on-premises IAM solution that provides identity governance, administration, and access and authentication management. More recently, TechCorp launched an IDaaS solution that was successfully received in the US market. Following this success, TechCorp France embarked on a program to introduce and increase interest in the IDaaS solution in the French market. However, although IDaaS was welcomed in the US, TechCorp France has been experiencing more difficulty convincing the French market to embrace it. Determining the factors impeding the successful entry of the IDaaS solution in the French market, when it was well-received in the US, can provide useful insights for multinational companies offering security solutions about how to market their products and ease contextual concerns that impede widespread engagement with their products.

## Data collection

Data were collected through semi-structured interviews and internal documents (see Table 2). Data collection and analysis were conducted simultaneously in an iterative fashion. We relied on a key contact within the focal organization to initially facilitate access to study participants. Discussing our research objectives with our key contact helped identify participants for the study. Specifically, we identified interviewees who have significant experience with both on-premises and cloud-based IAM offerings. We relied on both purposive and snowball sampling. Our primary data were complemented by secondary data that were used to familiarize ourselves with the focal company’s IDaaS offering and their sales and marketing strategies before beginning the interviews. We also used the secondary data to deepen our understanding of the sociotechnical challenges as we progressed with our interviews.

Table 2: Details of Data Collection

<table><tr><td>Data</td><td>Data collected</td><td>Description</td><td>Use in analysis</td></tr><tr><td rowspan="4">Primary data</td><td rowspan="4">15 interviews (between 20 and 95 minutes each)</td><td>1 partner (I14)</td><td rowspan="4">To better understand the IAM market, the strategy to sell and market IDaaS, and clients' perceptions and reactions of/to the technology.</td></tr><tr><td>2 CTOs (I1 &amp;I3)</td></tr><tr><td>9 managers (I2, I5, I6, I8, I9, I10, I12, I13, I15)</td></tr><tr><td>3 salespeople (I4, I7, I11)</td></tr><tr><td rowspan="2"></td><td colspan="2">5 meetings</td><td>To discuss multiple perspectives, preliminary results, and further needed resources.</td></tr><tr><td colspan="2">1 company presentation</td><td>To ensure we captured the emic perspective and to scrutinize the relevance of the research.</td></tr><tr><td>Secondary data</td><td>36 internal documents (numbered from D1 to D36)</td><td>Internal presentations, description of solutions and use cases, training documents, strategy, annual reports, videos</td><td>To better understand the context of TechCorp France, where the IDaaS solution stands in their product portfolio, and the company's strategy.</td></tr></table>

## Data Analysis

All the collected data were analyzed in NVIVO12 Pro. We followed a three-stage coding approach.

We asked our interviewees about trends, challenges, and opportunities they observed while engaging with their clients in the French market. In our first stage of coding, we used the framework for the IDaaS privacy calculus in Table 1 as a guide to identify confidence and enticement and risk beliefs that the interviewees had observed while engaging with their clients. First, we engaged with the secondary data to learn about the technical features of the IDaaS solution and how TechCorp was marketing and selling the IDaaS solution. This led to descriptive codes primarily highlighting the technical benefits of the IDaaS solution. Second, we examined the interview data to identify technical and social contextual explanations that may explain the hesitancy of French companies to engage with the IDaaS solution. This step allowed us to extricate confidence and enticement and risk beliefs that are specific to our technical (IDaaS) and social context

(French market). For instance, our analysis revealed the importance of the social context (i.e., cultural and regulatory environment) and that the cultural tendency toward uncertainty avoidance was expressed by initial distrust in the IT (the cloud solution), as well as institutions (TechCorp and the US government). This first stage allowed the researchers to become entrenched in the data and in the experiences of the interviewees. Multiple rounds of debriefings were undertaken to discuss and challenge categories. At the end of this first stage, 51 first-order themes were identified. This process was important because we could not assume that the IDaaS privacy calculus framework derived from the literature fully explains the differences in how TechCorp’s French clients were engaging with the IDaaS solution. Moreover, our IDaaS privacy calculus framework derived from the literature is general, and our analysis helped reveal, for example, specific benefits or security/privacy concerns that TechCorp’s French clients espoused when initially considering pursuing the IDaaS solution.

In our second stage, we refined our emerging themes by returning to the literature as a guide. For example, the concerns reported by our interviewees often highlighted the fact the IDaaS provider was headquartered in the US, which began to illustrate the importance of the multifaceted role of trust (specifically, distrust) in both the IT itself but also in institutions, including both the cloud provider and the government of the country in which TechCorp’s headquarters is located. This finding led us to extend the conceptualization of trust commonly used in the privacy calculus literature to include both trust in the IT and institutional trust in both the IT provider and the government to which the IT provider was linked [33, 65]. As another example, our analysis revealed that there were security and privacy concerns related to the technical aspect of the IDaaS solution such as concerns over the loss of control over the IAM solution but also security and privacy concerns related to the social aspect of the IDaaS solution such as concerns about the geographical location of the data, which led us to extend our framework to have sociotechnical components [50]. Notably, such concerns could potentially be rectified in these early sales stages by educational and awareness efforts in which TechCorp

employees better explain the technical and social aspects of the IDaaS solution to correct misconceptions. That such concerns were prevalently related in the interviews reflects the high uncertainty present in the early stages of TechCorp clients’ IDaaS solution consideration, which led us to explore the cultural uncertainty avoidance in our social context (i.e., France) [52]. Throughout this data analysis phase, we constantly compared the data to our existing themes as well as the extant literature on the topic [57].

Finally, in our third stage, once we refined the themes to integrate them into the organizational IDaaS privacy calculus framework, we went back to both documents and transcripts with our list of codes to ensure that no themes were missed. Moreover, because our study was prompted by a request from TechCorp to investigate their clients’ hesitancy toward their IDaaS solution, we reported our results to the company in a formal presentation, which allowed for “member checks” [36]. The formal presentation of our findings to managers working on TechCorp’s IDaaS solution enabled us to ensure resonance. At the end of this final stage, 13 IDaaS confidence and enticement and risk beliefs were identified and integrated into a model of an organizational IDaaS privacy calculus for the French market. While the objectives for TechCorp were met, this case study also allowed us to examine a unique situational organizational privacy calculus [8, 22, 28] that revealed in a particular sociotechnical context which confidence and enticement and risk beliefs drove interest in a novel security technology—IDaaS. When the risk beliefs outweighed the confidence and enticement beliefs, then TechCorp’s clients would (1) not pursue an IDaaS solution, (2) delay their pursuit, or (3) partially implement the IDaaS solution to cover only some of their IAM needs. When the confidence and enticement beliefs outweighed the risk beliefs, then TechCorp’s clients would pursue a full IDaaS solution. We refined the themes until we reached theoretical saturation, at which point the 13 identified categories articulated the situational IDaaS privacy calculus framework and adequately explained the French clients’ responses to the IDaaS solution.

## RESULTS

Our interviewees related a general interest from French companies in TechCorp’s IDaaS solution because of several important benefits it could provide. However, French companies also expressed hesitancy to pursue a full IDaaS implementation because of the perception of situational risk beliefs that outweighed the situational confidence and enticement beliefs. The technical and social risk beliefs were frequently strong enough to outweigh the confidence and enticement beliefs related to the IDaaS solution, resulting in no pursuit, lagged pursuit, or interest in a partial implementation of TechCorp’s IDaaS solution. Our analysis pinpoints the technical and social risk beliefs associated with a USbuilt IDaaS solution in the French market. Our analysis also reveals technical and social confidence and enticement beliefs that can be capitalized on or improved to discourage the French hesitancy toward the IDaaS solution. The hesitancy of French clients toward TechCorp’s IDaaS solution was identified as the problem by our interviewees, which suggests that the risk beliefs of the French clients outweigh confidence and enticement beliefs. The consequences of this imbalance are that (1) French companies do not pursue the IDaaS solution, (2) French companies wait until they see others successfully implement IDaaS without major consequences before doing so themselves (i.e., lagged adoption), or (3) they pursue a partial implementation of the IDaaS solution as part of a hybrid solution that allows them to retain their legacy systems to some extent.

Our analysis identified several confidence and enticement beliefs related to the IDaaS solution. We categorize them as either technical or social confidence and enticement beliefs. We categorized as technical confidence and enticement beliefs any themes that related to the benefits of the IDaaS technology itself. We identified two perceived technical benefits of TechCorp’s IDaaS solution (see Table 3). First, TechCorp’s clients understood their need to replace and update aging IAM systems. Second, they described how legacy systems are not equipped as well as IDaaS to handle the IAM needs for

rging technologies (e.g., bots, Internet-of-things [IoT]). As one respondent noted: [On-premises solutions manage] thousands of identities, rarely millions. If the scope increases, [the] customer has to double its infrastructure, which would be hard, long and costly. With [a] cloud model, (…) the customer will handle two billion identities from IoT and customer management without changing [anything] but the price of its subscription. Cloud is already ready to welcome these billions of identities. (I4)

Table 3: Example Quotes About Technical Confidence and Enticement Beliefs in the IDaaS Privacy Calculus

<table><tr><td>See need to replace outdated systems</td></tr><tr><td>We&#x27;re on a replacement market for IAM. (I6)</td></tr><tr><td>We feel that there is a real renewal market, what is interesting to see is that today, we have seen an increase in activity since the end of 2018, customers who had already made acquisitions on identity and access management before are renewing their fleets with new needs and inevitably, this crystallizes around the cloud. (I3)</td></tr><tr><td>They are in a process of obsolescence, so they are preparing the future (...) we know that these applications [on-premises IAM] at a given time, they will either transform or die, because there too, these applications are going to the cloud. (I10)</td></tr><tr><td>In fact, we will move towards the cloud from the moment we start to think about it because either the solution is obsolete, or it costs too much. There is always a trigger. (I14)</td></tr><tr><td>See need to prepare for identity management requirements for emerging technologies</td></tr><tr><td>We have competitors in this space who like to talk a lot about what they are doing for Bot identities and how they are managing these robotic process automation tools because they also need to have the right structures in place to ensure that they only have access to what they need and to ensure that the right people have access to the bots themselves. A lot of time, during robotic process automation, people integrating it [into] their solution don&#x27;t look as heavily into, I guess, the dangers of giving a lot of entitlements. (I12)</td></tr><tr><td>IDaaS, I would say that what can differentiate it is in new use cases around IoT, Blockchain, how connected objects will communicate with each other, authentication</td></tr></table>

between connected objects, identities management of connected objects, these are things that on-premise solutions do very badly. (I11)

There are also new issues emerging, such as connected objects, everything around the IoT, that's the IAM today, we are starting to have security incidents around the IoT are objects that are hijacked for malicious purposes. We also talk about AI, today it's a bit like science fiction, it's more machine learning than AI, but in a few years, it will be a real model, the cognitive one will be something that will really help customers respond to real issues where we are no longer talking about thousands of identities but we are talking about billions. And when we talk about billions of identities, IoT, connected objects, humans are no longer enough, we would need a little AI to help humans to be able to process this mass of information. This is a bit like what is done today with big data. (I4) I think there is going to be a greater push for utilizing Identity and Access Management solution when we are adding in automation. (I12)

Interest in IDaaS in the French market is stimulated by technical benefits that include the need to replace and update aging IAM solutions and the fact that IDaaS provides the benefit of being able to handle the IAM needs for emerging technologies. IAM is a challenge to implement [44], and requirements to manage identities of nonperson entities (e.g., network-connected IoT devices) add to that challenge. IDaaS provides the ability to manage more complex technology infrastructures and to shift that management to a third party.

We categorize themes that relate to how TechCorp’s clients see their employees benefiting from the IDaaS solution and all trust issues as social confidence and enticement beliefs. We identify four social confidence and enticement beliefs related to the IDaaS solution (see Table 4). First, our interviewees described how the consumerization of IT is driving the perceived benefits of IDaaS; i.e., their employees are increasingly expecting to be able to log in to resources at anytime from any location. Consumerization of IT is the “phenomenon whereby consumer technologies and

consumer behavior are in various ways driving innovation for information technology within the organization” [10, p. 5]. People want to be able to access resources at anytime and from any place or device, and because this can be done fairly seamlessly with their personal technologies, employees also want such capabilities at work. For example, one of our interviewees noted:

What you see when you have a smartphone, you expect when you are interacting with that phone, you tap the icon and things work. When you are checking your emails, when you are checking your calendar, booking a hotel or a flight, whatever it is, you just expect that it works like that. And that consumerization [transfers] into the business world, when people are interacting with services, they expect [it] to be seamless like that. (I8)

## Table 4: Example Quotes About Social Confidence and Enticement Beliefs in the IDaaS Privacy Calculus

<table><tr><td>See solution could ease use through consumerization of IT</td></tr><tr><td>I don’t expect to have to put in passwords just to have access to my emails, I don’t expect of the customers of your company to have to come in and create a full registration, I might give my email address and might create social registration with some social providers like Facebook but I am not going to give you the answers to 50 questions about where I was born etc. You are seeing a lot more of that consumer [mindset] shifting into the business [environment]. (I8)Little by little, there has been a transformation of the solutions with more and more requirements to give the trades a hand on these solutions. The fact that the end-user, the manager, the application managers get their hands on the solution, there is a transformation in these solutions. We have arrived at scenarios where user experience has become very important and where features such as recertification of rights, experience on the workflow have become very important. (I10)</td></tr><tr><td>Distrust in cloud technology</td></tr><tr><td>Then, it will be more a question of business strategy. There are still a lot of companies that are a little cautious about putting everything in the cloud. (I5)</td></tr><tr><td>You don't have to ask yourself existential questions about the security of your data, it's all yours so if something goes wrong you can only blame yourself. But overall, you don't have to trust, you are responsible for everything, it is you who plugs the small cables and it is you who manage where your users are stored, it is you who manages the passwords and there you go. (I7)There are really a lot of questions to prepare, just because it's SaaS doesn't mean it's easy. Who is responsible ? The contract ? Where is the data? What is the given level of security? (I10)We are trying to curb this fear a little by putting data centers in Europe, but ultimately the main fear of the cloud is data leakage, my data is no longer at home, it is at someone else's and I don't not know what you are going to do with my data. The second fear is the fear of what is called the SLA (Service Level Agreement), it is the commitment that we give to a product so that it is operational, very often we will provide an SLA. For example 99.9%, that is to say that we contractually commit that our services in the cloud operate 99.9% of the year. (I7)</td></tr><tr><td>Distrust in US companiesIt's the big problem in France, especially with an American company, you have to know that American companies with the Patriot Act, in theory is supposed to give its data to the United States in case of conflict if ever the government asks for it. It freaks out a lot of people. (I7)There is a lot of questions around where is this [data] housed? Is it actually going to reach compliance? Where is the data being processed? I think there are just concerns around utilizing cloud solutions when it comes to entitlements and the data that has come with managing identities, I think in terms of the sensitivity [concerns], it is much more prevalent with the identity side than with the access side. (I12)French business are wary of American business and regulations, we have seen in the automotive industry and others that quit Iran to abide the US sanctions, change in regulations that give an advantage to US businesses. (I2)</td></tr></table>

Distrust in US government

Because markets are different, in the US, there is not the problem of where my data is stored, it is expected that it is in US data centers but in Europe the first question, is my data stored in Europe or not? (…) We also see differences in terms of what customers are [asking for, in] Europe, [there is] a lot more focus on privacy control of the actual identity. You control your identity; you decide who can use it. In [the] US, that is just starting to come now, with legislation in California for example, so that is not necessary the foremost thing on everyone’s minds. (I8)

We will still find some obstacles on where the data is stored. This is the big problem in France, especially with an American company, you have to know that American companies with the Patriot Act, in theory, are supposed to give its data to the United States in case of conflict if ever the government asks for it. It freaks out a lot of people. (I7)

IDaaS is nothing new, we have been talking about it for several years but always with a fear (…) “is there a risk that my data will go to the US with the Patriot Act?”. These are real concerns today on the security part, the solutions had to mature and show what are the mechanisms behind which are implemented to really secure the data, secure access and ensure that the data does not escape or made available to other organizations. (I14)

There is this fear in the beginning that fell at the time of the Snowden affair, where there was a fear of putting the data on the Internet. Fear of being really policed and controlled. Now, we are a bit past that. (I11)

Second, distrust was identified to play a key role in the IDaaS privacy calculus. Specifically, TechCorp’s clients frequently described distrust in the technology, the USheadquartered company, and the US government to TechCorp’s employees. Even though cloud services are becoming increasingly common, cloud security solutions are less common, and there is hesitancy on the part of TechCorp’s clients to trust either, as one interviewee stated:

This can be explained, for certain industries, for them it is out of the question to put anything in the cloud and even less security solutions. (I11)

IDaaS requires sensitive organizational employee data to be entrusted to the cloud provider. There is expressed concern regarding this data disclosure that is unique to IDaaS:

Still see [companies] heavily leaning towards on-premises deployment, I think they are looking for [and] are interested in utilizing IDaaS but I think it is a very gradual transition that is being made. Much slower than the access management side. I think it’s all the identity data of the users and their patterns of use that still gets them worried. (I12)

TechCorp is a US-headquartered company, and a security mechanism that it manages is viewed with some wariness in the French market. The IDaaS solution is seen as a technology developed by the Americans for the Americans, and adopting it is thus seen to be placing trust in the Americans to serve the best interest of the French. In a low-trust country [61], such trust may be hard to build. For example, one interviewee described a general French distrust in US companies that are economic competitors:

France is one of these countries also wanting to tighten-up around its data by saying "is it that the USA as allies are not also economic competitors in the process of draining on my data in order to get ahead of us?" It’s a reality. (I3)

In part, the distrust in the company (i.e., TechCorp) is related to the lack of trust in the US government. Although it may be difficult to trust that a cloud provider will make decisions in a client’s best interest, it may be even more difficult to trust that another country’s laws will not take precedence or that their political climate will not influence decision-making. The interviewees expressed trust in Europe’s handling of privacy and security, as one noted:

France has always been one step ahead and in particular through the CNIL and ANSSI<sup>1</sup> [regarding] where my data is stored, what is the level of protection on [it], in particular, sensitive and personal data, the GDPR confirms this. (I3)

However, the interviewees stated that their clients do not have the same trust in the US government. They explained how their clients were hesitant to place trust in a company they viewed as beholden to a US government that they did not feel may put French companies’ interests first. Moreover, TechCorp’s clients expressed uncertainty related to a lack of knowledge of the regulatory environment overseeing a cloud security solution from a multinational company. The comments below and those in Table 4 show examples of such sentiments TechCorp’s employees encountered.

Always with a fear "the data is not at home," "my data is in the cloud," "is it a sovereign cloud," "is my data really in France?" Am I afraid that my data will go to the US with the notion of the Patriot Act. These are real topics today on the security part. (I14)

There is always this fear and in particular on the French market, to know [that to some extent] the French want a French label with all the regulations that go well. And all the more I will say, it is true that there is a bit of a geopolitical side but since the arrival of Trump to power, there has also been a fear of America falling back on its critical infrastructures and therefore the need to have a vision on strategic elements. (I3)

The lack of trust in the company and the US government, combined with the perception that a cloud solution is more vulnerable to security incidents because it is offsite, result in hesitancy to adopt the IDaaS solution. These concerns generate “a lot of uncertainty in Europe, a lot of times they would ask if there is a way to do on-premises deployment.” (I12)

## Technical and Social IDaaS Risk Beliefs

Three technical risk beliefs related to TechCorp’s IDaaS solution were identified in our analysis (see Table 5). First, as in prior studies of cloud computing [3, 43], concerns regarding the loss or lack of control over the IT task or environment were found among TechCorp’s French clients. These concerns arise because control of a primary security task is being ceded to the cloud solution provider. Second, concerns were raised about the maturity of IDaaS solutions in general, for example, one interviewee stated:

But today, the problem with the IDaaS market in general, it is a market I would say [that is] still immature or which has not yet reached maturity, it is a growing market. There is no IDaaS offering that is equivalent to traditional on-premises IAM offers today. Not yet. (I6)

Third, cloud solutions are typically standardized for multiple clients, which requires clients to compromise in terms of the features and customization that can be obtained. Interviewees noted that clients in the French market were hesitant to move from customized IAM solutions that were available on-premises to a more standardized IDaaS solution.

In practice, there is still a fundamental difference between the cloud and on-premises [solution], at least [for] the governance part [of] the IDaaS and even on the authentication part, you cannot do everything you want in cloud mode. That is to say that there is bound to be a moment [even in] somewhat successful scenarios that will require a component that will be installed on-premises. If you want 100% cloud, you're going to have to compromise on scenarios, on ways of doing things, on things that just aren't possible if everything is in the cloud. And the client is not predisposed to compromise. (I7)

All three of these concerns reflect risks that TechCorp’s clients see as potential negative consequences of moving to an IDaaS solution. That is, these three technical risk beliefs articulate reasons why TechCorp’s clients may end up with a solution that they are ultimately not comfortable with or does not meet their needs.

## Table 5: Example Quotes About Technical Risk Beliefs in the IDaaS Privacy Calculus

<table><tr><td>Concerns over loss of control of IAM solution</td></tr><tr><td>In any case, we have seen it on the French market, we still have a lot of things on-premises, we want to keep our data and we work a lot with the banking sector in particular. (I14)This is a bit like what we see today, these are offers that date back more than 20 years, they have had time to evolve, all the functionalities have been integrated on-premises and the customer has his hands on what he wants. He installs them in his data center. He has</td></tr></table>

control over the code, over certain features, he can extend them etc. ... (I4)

The IT team loses some control over the solution, you can't do the same in a SaaS solution as in an on-prem solution. If you want to do something very specific to your business, it's more complicated to do it in SaaS or necessarily it's a lot more regulated and you can make less change in the solution. (I3)

## Concerns regarding IAM solution immaturity

Once [TechCorp’s IDaaS] has [a more extensive] feature set, it is going to allow us to talk more to our existing customer base about doing a gradual transition to [a] cloud solution but today that is just not the case. But eventually we are going to have to be ready to have this conversation. (I12)

After all our solutions are maybe not always I will say ahead of the other solutions, I will even say maybe sometimes a little behind. (I14)

My feeling is that companies want to go for IDaaS but we all know it's not very ready. I think we have to wait another 6 months to 1 year before we have real comprehensive and competitive offers in IDaaS. This is a market that is struggling to mature at the moment (I6)

## Inability to customize IAM solution

Do we accept something that is quick to implement but on the other hand we don't have all the flexibility in the sense that we cannot do everything we want in SaaS mode, that is? It’s limited, we fit in the mold or we do not fit in the mold, that's what I want to convey as a message. SaaS, we cannot customize the solutions as we could with on-premises solutions, typically. (I11)

From a point A to a point B, you can take the car on-premises. If you have a bus stop (cloud) near your house and a bus stop (cloud) where you want to go, you can take the bus that is less expensive but offers less possibilities. (I9)

There are a lot of customers who place a great deal of importance on the customization aspect. The problem with the cloud, so the graphics is almost the easiest thing to customize, but you can't customize everything. (I7)

If you want to offer the most generic service possible to a set of users, to a set of companies, you can't fall for the setbacks of an on-premises installation where you customize everything. Often you compromise, you do things that are a little generic so sometimes it works, sometimes it doesn't. (I7)

Four social risk beliefs related to TechCorp’s IDaaS solution were identified as themes in our analysis (see Table 6). First, although high-uncertainty avoidance prevents French companies from being technological trendsetters, they do follow technological advancements and adopt them to stay current with what is happening in the market and what their peers are doing. TechCorp’s French clients may be initially reluctant but as their peers move to cloud security solutions, they are able to use others’ experiences to better judge their own risk. As one respondent stated:

There are always clients who have this reluctance, I had a client a month ago [and a] year ago it was out of the question to talk about the cloud with him, and today because he sees that everyone is finally talking about the cloud, all his other colleagues, all the other companies, he has already deployed [cloud] solutions. Cloud, today they open the door to these technologies by saying ok. (I4)

Second, our interviewees describe French organizations to be demanding clients when it comes to the expected features of solutions. A demanding French customer base, not willing to compromise over features or accept any risk that the IDaaS solution may not meet their specifications exactly, is depicted by our interviewees:

Historically (…), in France, we have requirements that are more important than in the US (…) in France, there are really a lot of requirements and there is a lot of customization, (…) we like to develop or add features [in] these solutions and therefore we have trouble lowering its functional requirement, to have this compromise by saying ok, finally I [will] do with what there is and I [will] wait little by little for the solution to be more mature and I will benefit from new functionalities over time, we are not at all [for] this approach. (I10)

This organizational inflexibility, combined with the limitations to customize IDaaS solutions, is viewed by TechCorp’s employees as a key explanation of the hesitancy of French companies to pursue an IDaaS solution. High-uncertainty avoidance could be a factor in encountering French clients who are not predisposed to change or compromise. A solution that cannot be promised to have all the desired features may be too risky for high-uncertainty-avoidance clients.

Table 6: Social Risk Beliefs in the IDaaS Privacy Calculus  
```txt
Risk reduction from seeing peers successfully migrate

... the fact that we went to applications that are in the cloud, so people work from home and we are no longer on an IS that is completely closed, the IS has become very open. Little by little, all of this made security as well, like “why not” [move it to the cloud]... This is the change in the way we see things, our perception has been transformed so the digital transformation has also meant that we are transforming the way we consume and perceive security. So finally, we saw SaaS solutions [adopted]... we also saw the infrastructure which is in the cloud [adopted,] so I will naturally say security also [will] follow this movement. (I10)

We need to start with existing customers, successfully migrate them and make them referrals. A market that works well is when customers become sellers and say "we have installed such and such a thing and it is working well, we are happy with it." That's why we often start by trying to go see our current customers (...) This is something that we know how to do so that, little by little, there is a certain adoption of the product and then we can say "Company X has installed such solution in SaaS, it works well, we can exchange with them." These are often strategies that are quite interesting to have (I5)

They are forced to use companies that are in the cloud, to use services that are hosted in the cloud that allow them to potentially improve their productivity, speed, agility, flexibility. (I11)

Inflexibility of French Organizations

The use cases are not necessarily always the same and the US customers are perhaps ready to make sacrifices that in Europe, we have a little more of a mentality of I want this functionality there and if I do not have it no, goodbye I'll look elsewhere. So, the mentalities
```

## are not the same. (I11)

If you want 100% cloud, you're going to have to compromise on scenarios, on ways of doing things, on things that just aren't possible if everything is in the cloud. it’s not that it’s not possible, it’s possible for customers who compromise. There are security compromises, but our customers aren’t always ready to compromise. (I7)

We had big hopes for IDaaS the French Market to take off early on, but we faced a wall when we came to specific requirements. You have to stop them and tell them “no we can’t do this and that in cloud” and that doesn’t go well. They want what they want (I2)

## Concerns over geographical location of data

One of the first concerns of our customers was where the data centers are, they wanted to know physically where the data was stored. (I3)

There is always the question of where their data is stored. (I4)

It is more that US customers take for granted that there are US data centers whereas the customers outside of North America, the first question is “can my data be in my local region.” And that is also one reason to share with you, one reason why we actually build data centers first in Europe, (…) we knew that the European market main concern was “my data must stay in Europe first” so that is why we go to Europe first. (I8)

There are some who have had time to think about it, who have come to terms with the idea and now are open to the idea of going to the cloud. Then we will still find some reluctance on where are the data stored? (I7)

## Concerns over regulatory compliance

I think the difficulty of selling our solution to this market is around the compliance needs that they have today. (I12)

[Slow adoption of IDaaS] is due to the state. In fact. there were several events, there was the GDPR which forced companies to focus on this and therefore they did not necessarily equip their entire process, they put in place data protection officers, DPOs are not necessarily equipped and now when they replace their IAM solution, they ask to take into

account the GDPR. (I6)

There is also the regulatory part that will come into play and I think it is a little different from the Americans since the majority of the solutions come from there and we are a little more careful on this point. (I10)

Third, TechCorp’s clients expressed concerns over where the shared data are stored. French clients want their data stored in European data centers because that both eases concern over compliance with European regulations and distrust in the US government. For example:

You can feel it in France, it's the sovereign cloud part, the "where are my data?" "," What happens to the hosting of my data? "," Does your solution host the data in a European data center?" (I10)

Finally, the differences in the regulatory environments of France and the US bring additional client concerns to the fore. The EU is seen to be ahead of the US in terms of data protection regulations, as one interviewee stated:

I think Europe is clearly in the lead of setting up these compliance mandates and I think the US is eventually going to follow as well as other areas in the world. I think that pretty much plays a role in how they want to do the deployment. (I12)

The need to comply with EU data protection regulations factors into the decision to consider an IDaaS solution from a company headquartered in a country with less strict regulations. Such concerns may reflect misconceptions or a lack of knowledge about the technology or the regulatory environment, but they do reflect TechCorp’s clients’ initial reactions to the IDaaS solution. These social risk beliefs are guiding TechCorp’s clients’ initial reactions to the IDaaS solution and therefore determining their organizational privacy calculus that will determine whether the IDaaS solution is pursued and at what level.

## DISCUSSION

Central to an organizational privacy calculus is that for an organizational data disclosure to occur, the benefits of the disclosure must be seen to outweigh the risks [e.g., 8, 16, 22]. The hesitancy of French clients to pursue the IDaaS offered by a US-headquartered company can be explained by the organizational IDaaS privacy calculus having risk beliefs that outweigh the confidence and enticement beliefs. The perceived risks of entrusting sensitive data to manage a critical security function and the distrust of the parties involved are too high for clients in a low-trust, high-uncertainty-avoidance country [61]. As illustrated in Figure 1, if the confidence and enticements beliefs outweighed the risk beliefs, interest in full IDaaS deployments would be more frequent.

![](/api/attachments/AH84K4W7/fulltext/images/d81105ac828092b3bffa0832619359af8398afcb94c51d19b87f3bbf999f6fe2.jpg)  
Figure 1: Organizational IDaaS Privacy Calculus in the French Market

However, TechCorp experiences more interest in hybrid IDaaS solution, in which part of the client’s IAM is moved to IDaaS but some of the on-premises solution is retained, or lagged adoptions that come after French clients see the solution working for others. Our interviewees noted that the French market tends to be reactionary to new technologies or prefer an intermediary step (i.e., a hybrid solution):

What the French market as a whole, and this is not specific to the cloud, tends to say: "I want to see what's going on and I want to first have concrete feedback to know if I'm going for it."

We saw that it worked, and that anyway, we saw that it was a trend that was clearly drawn and that there was no going back planned. And so, the French market really gets into it, a bit of a reaction. (I3)

The only sale we can make to our existing [customer] base is to do a hybrid deployment and when we do that we’ll have to look at what are the additional capabilities that will augment their existing solution. (I12)

Our results suggest that the IDaaS privacy calculus currently favors the risk beliefs, resulting in an undesirable entry for this IDaaS solution into the French market. However, there are potential benefits that could be further emphasized, and TechCorp could work to educate and correct misconceptions that could help to reduce the distrust French clients express toward the IDaaS solution, TechCorp, and the US government. It is necessary to educate to increase comfort with the new technology and build trust with clients in the French market to increase interest in the IDaaS.

## Contributions to Research and Theory

The contributions of this study are threefold. First, we examine an organizational IDaaS privacy calculus. In doing so, we identify both technical and social confidence and enticement beliefs and risk beliefs related to an IDaaS solution. Although it has been suggested, few studies have focused on a situational organizational privacy calculus [8, 22]. However, organizations are frequently faced with disclosing organizational data, such as employee identity information, in exchange for organizational benefits. Such organizational privacy decisions are increasingly critical because companies are entrusted, and increasingly legally bound, to protect the data over which they have become stewards. Our study provides insight into how organizations think about the risk– benefit tradeoffs for data that they steward.

Our focus on a novel cloud security service in a high-uncertainty-avoidance country allows us to contribute to the literature on cloud computing [e.g., 3, 7, 9, 26, 27, 37, 43, 58, 60]. A privacy calculus is often situational [28]; that is, the benefits are typically tied to the context, and we identify benefits unique to IDaaS and the IAM market in France. Specifically, we find unique technical benefits of IDaaS solutions that arise because of the nature of the technology. IDaaS handles IAM, which is a security mechanism that most companies already have some version of, and thus, IDaaS is in a way an upgrade that may eventually be necessary given other technological advances (e.g., increased use of cloud for IaaS and SaaS, IoT devices). Our results show that there is a need to consider replacing outdated systems in the French market. Moreover, securing the enterprise is becoming increasingly important, especially as technology advances, and it becomes necessary to attach identities to nonperson entities (e.g., IoT devices), and IAM plays an outsized role in doing so. Our results illustrate that technological advances, such as IoT devices, make moving to cloud security solutions more attractive. These benefits are context specific, which suggests that SECaaS technologies may spur unique confidence and enticement beliefs. Therefore, our results indicate that generalizing findings across even a similar group of technologies (e.g., cloud) may not be advisable.

Second, our IDaaS privacy calculus reveals unique confidence and risk beliefs in a European market about a cloud service from a US-headquartered company. We confirm some concerns that are described in the cloud literature in our context, such as concerns over loss of control over the technology [51], location of the data [1], and regulatory issues [12, 26, 31, 43, 45, 49, 59]. However, concerns over losing control of a critical IT function and location of the data are less commonly examined in the cloud computing literature, and the prominence of these concerns in our data may reflect the sensitive nature of the data required by the IDaaS solution. We also show that the French market is aware of the regulatory differences between France and the US and that does factor into their hesitance to adopt a security solution from a US-headquartered multinational.

Notably, we illustrate the multifaceted role of distrust in the IDaaS privacy calculus. Trust, or distrust, has been understudied in the cloud computing literature [1, 23, 65]. In our context, we find that distrust of the cloud security technology, US companies, and the US government all play a role in the hesitancy toward TechCorp’s IDaaS solution seen in the French market. This is tied to the fact that to implement IDaaS, French companies must entrust the US-headquartered multinational with identity information. Our findings highlight the difficulties faced when a security technology enters a new market, especially when it is a technology that the client cannot fully control and one that manages sensitive data. We find hesitance in the French market toward IDaaS, which resulted in more interest in lagged or partial IDaaS implementations. Lagged or partial implementations allow clients time to build trust with the technology and the company before fully committing. In the rather complex regulatory environment we studied (i.e., a multinational headquartered in the US selling a cloud security product in the French market), the lack of trust may be due at least in part to misconceptions or a lack of education or awareness about the technology, cloud provider, or regulations. However, the emergence of distrust as a key factor in the organizational privacy calculus suggests that it is important for researchers to study how trust can be built in situations in which complex security controls need to be implemented in complex regulatory environments in collaborations potentially involving two or more companies.

Third, we develop a framework for the IDaaS privacy calculus that includes both technical and social confidence and enticement beliefs and risk beliefs. The merit of our framework is that it organizes the contextual explanation of the IDaaS privacy calculus into two primary aspects: (1) the technical that articulates the technological confidence and enticement and risk beliefs clients develop with respect to the IDaaS solution and (2) the social that articulates the social confidence and enticement and risk beliefs [21, 37, 50]. Therefore, we contribute to the privacy calculus literature by exploring an organizational data disclosure decision in a privacy calculus framework [e.g., 8, 20]. We also contribute to the discussion on the role of context in IS research by examining the problem within its sociotechnical context [5, 18, 21, 37, 50].

## Implications for Practice

Our data illustrate that in the French market, perceived risks currently outweigh the perceived benefits of IDaaS that hinders interest in it. However, there are notable benefits to IDaaS solutions that are likely to increase in importance. IDaaS can address the challenge of securing systems employing new technologies like IoT and robotic process automation (RPA) that have demanding IAM needs. As the use of these emerging technologies increases, IDaaS will become more attractive. Pressures from the consumerization of IT will also increase as employees expect the convenience they have with their personal technologies. Marketing materials could be developed that both demonstrate the technology, to increase comfort with a new technology, and highlight these benefits.

Our results also illustrate that different cultural contexts may emphasize unique confidence and enticement beliefs and risk beliefs, and thus the privacy calculus performed may be context dependent. In transitioning to IDaaS, French companies must adapt to a solution that is not fully under their control or customized to their specific needs, and these are critical factors contributing to their hesitance. Specifically, France is a low-trust, high-uncertainty country, and the IDaaS privacy calculus for French clients takes into account the need to relinquish control of a critical security service to a USheadquartered company. This requires trust, and our data suggest that there is a lack of trust in the technology, the company, and the US government. Multinational companies facing trust issues may consider highlighting to customers how they ensure compliance with EU regulations. Another option would be to illustrate measures that can be employed to ensure cloud solutions are meeting standards and regulations, such as service level agreements (SLAs), risk assessments, or audits [26]. Emphasizing the use of security tools and encouraging methods that can help counter security risks may ease the concerns of people with high-uncertainty avoidance [29].

Companies wishing to inspire interest in security service offerings in different cultural contexts would be advised to examine the cultural values of the markets they wish to enter and plan accordingly. In the French market, this means taking steps to build trust with clients. TechCorp is emphasizing investment in data centers located in Europe in their sales pitch. Formalizing materials that lay out where cloud data are stored and

explaining the cloud provider’s capabilities for compliance with other country’s regulations would be an advisable next step. Although we focus on the French market, business is increasingly global, and conforming to varying mandatory security and privacy regulations is not a trivial issue. Another tactic to encourage interest in IDaaS solutions may be to rely on companies who have successfully implemented IDaaS to provide testimonials [32]. People who are high on uncertainty avoidance rely on social cues to determine whether technology adoption is appropriate [55], which suggests that highlighting peers’ successful implementations may ease hesitance. Offering a test environment or free training could also increase the comfort with a new technology that is not fully customizable. Such tactics could help build trust and comfort with the new technology, the cloud provider, and ease concerns related to trust in the US government.

## Limitations and Future Research

Because SECaaS and IDaaS, specifically, are new technologies that have not fully matured with regard to capabilities, more work is needed to increase interest in such tools among small, medium, and large organizations. As companies across the world move more of their infrastructure to the cloud, understanding the situational organizational privacy calculus is going to become increasingly important for cloud providers to be competitive. Our study illustrates the challenges of aligning cultural values with complex and sensitive infrastructure outsourcing, and future work may want to expand on our findings, especially for other SECaaS offerings.

Moreover, our insights are limited by the single case design, which enabled an indepth examination of contextual conditions that contribute to the organizational IDaaS privacy calculus in France. Although some of our findings may be applicable to other European countries, research has shown that cultural values are not uniform across Europe [e.g., 41, 52], so future research may benefit from granular examinations of the organizational IDaaS privacy calculus in different countries. Future work could conduct a multiple case design to vary contextual conditions to examine the organizational IDaaS privacy calculus in other cultures or to examine the privacy calculus across multiple

SECaaS offerings. The single case design limited us to interviewing employees and reviewing documentation from the one company regarding its specific IDaaS and experiences with their clients, which provided perspective from the employees of the company selling the product. Future work could consider expanding the perspectives obtained to include other IAM stakeholders such as competitors or customers. Undertaking a longitudinal study to see how the organizational IDaaS, or SECaaS, privacy calculus evolves in a market over time could also be a fruitful avenue for future research.

## CONCLUSION

Our study examines a situational organizational privacy calculus for an IDaaS offering from a US-headquartered multinational company in the French market. We conduct a qualitative analysis through which we develop a framework for an organizational privacy calculus that informs French organizational consumers’ decisions to pursue an IDaaS solution. In the organizational IDaaS privacy calculus, potential clients weigh the perceived benefits of relinquishing control of their IAM, and hence the data to manage it, to a cloud service provider against the perceived risks of doing so. We identified technical and social confidence and enticement beliefs and risk beliefs and organized them into an IDaaS privacy calculus for the French market. Notably, we found that, in the French market that is characterized by high-uncertainty avoidance, distrust was a key factor in the organizational IDaaS privacy calculus. Although, currently, distrust and perceptions of risk are stymieing the progress of the IDaaS solution in the French market, we identified several benefits that could be highlighted to help increase interest. Our results illustrate the importance of both the technical and social context in a situational organizational IDaaS privacy calculus to better understand how context shapes hesitancy toward a new security tool.

## REFERENCES

1. Alkhater, N; Walters, R; and Wills, G. An empirical study of factors influencing

cloud adoption among private sector organisations. Telematics and Informatics, 35, 1 (2018), 38-54.

2. Alpár, G; Hoepman, J-H; and Siljee, J. The identity crisis. security, privacy and usability issues in identity management. Journal of Information System Security, 9, (2011), 23-53.

3. Asatiani, A. Why cloud? A review of cloud adoption determinants in organizations. Presented at Twenty-Third European Conference on Information Systems (ECIS), Münster, Germany, 2015, pp. 1-18.

4. Ashford, W. How to tackle the IAM challenges of multinational companies. (2020), Date Accessed: December 21, 2020, retrieved from https://www.computerweekly.com/opinion/How-to-tackle-the-IAM-challenges-ofmultinational-companies

5. Avgerou, C. Contextual Explanation: Alternative Approaches and Persistent Challenges. MIS Quarterly, 43, 3 (2019), 977-1006.

6. Bansal, G and Zahedi, FM. Trust-discount tradeoff in three contexts: Frugality moderating privacy and security concerns. Journal of Computer Information Systems, 55, 1 (2014), 13-29.

7. Battleson, DA; West, BC; Kim, J; Ramesh, B; and Robinson, PS. Achieving dynamic capabilities with cloud computing: An empirical investigation. European Journal of Information Systems, 25, 3 (2016), 209-230.

8. Belanger, F and James, TL. A theory of multilevel information privacy management for the digital era. Information Systems Research, 31, 2 (2020), 510-536.

9. Benlian, A and Hess, T. Opportunities and risks of software-as-a-service: Findings from a survey of IT executives. Decision Support Systems, 52, 1 (2011), 232-246.

10. Beraud, P. Towards Identity as a Service (IDaaS): Use Cloud Power to Solve Cloud Era Challenges. Microsoft France 2017.

11. Blount, S and Maxim, M. CA Technologies Strategy and Vision for Cloud Identity and Access Management. (2013), Date Accessed: December 31, 2020, retrieved from

http://www2.cio.com.au/campaign/370583?content=%2Fwhitepaper%2F371982%2F ca-technologies-strategy-and-vision-for-cloud-identity-and-access-management

12. Borgman, HP; Bahli, B; Heier, H; and Schewski, F. Cloudrise: Exploring cloud computing adoption and governance with the TOE framework. Presented at 2013 46th Hawaii International Conference on System Sciences, Maui, Hawaii, 2013, pp. 4425- 4435.

13. Celeste, E and Fabbrini, F. Competing jurisdictions: Data privacy across the borders. In T. Lynn, J.G. Mooney, L. van der Werff, and G. Fox (eds.), Data Privacy and Trust in Cloud Computing. Cham, Switzerland: Palgrave Macmillan, 2020, pp. 43-58.

14. Comfort, J. How a Hybrid Multicloud Strategy Can Overcome the Cloud Paradox. (2019), Date Accessed: December 31, 2020, retrieved from https://www.ibm.com/blogs/think/2019/11/how-a-hybrid-multicloud-strategy-canovercome-the-cloud-paradox/

15. Culnan, MJ. " How Did They Get My Name?": An Exploratory Investigation of Consumer Attitudes toward Secondary Information Use. MIS Quarterly, 17, 3 (1993), 341-363.

16. Culnan, MJ and Armstrong, PK. Information privacy concerns, procedural fairness, and impersonal trust: An empirical investigation. Organization Science, 10, 1 (1999), 104-115.

17. Culnan, MJ and Bies, RJ. Consumer privacy: Balancing economic and justice considerations. Journal of Social Issues, 59, 2 (2003), 323-342.

18. Davison, RM and Martinsons, MG. Context is king! Considering particularism in research design and reporting. Journal of Information Technology, 31, 3 (2016), 241- 249.

19. Dinev, T; Bellotto, M; Hart, P; Russo, V; Serra, I; and Colautti, C. Privacy calculus model in e-commerce–A study of Italy and the United States. European Journal of Information Systems, 15, 4 (2006), 389-402.

20. Dinev, T and Hart, P. An extended privacy calculus model for e-commerce

transactions. Information Systems Research, 17, 1 (2006), 61-80.

21. Ferreira, A; Huynen, J-L; Koenig, V; and Lenzini, G. A conceptual framework to study socio-technical security. Presented at International Conference on Human Aspects of Information Security, Privacy, and Trust, Heraklion, Crete, Greece, 2014, pp. 318-329.

22. Greenaway, KE; Chan, YE; and Crossler, RE. Company information privacy orientation: A conceptual framework. Information Systems Journal, 25, 6 (2015), 579- 606.

23. Heart, T. Who is out there? Exploring the effects of trust and perceived risk on SaaS adoption intentions. ACM SIGMIS Database: the DATABASE for Advances in Information Systems, 41, 3 (2010), 49-68.

24. IBM. IBM Security Verify - Secure user productivity with born-inthe-cloud identityas-a-service (IDaaS). https://www.ibm.com/downloads/cas/GXPOGPQA, 2020.

25. James, TL; Warkentin, M; and Collignon, SE. A dual privacy decision model for online social networks. Information & Management, 52, 8 (2015), 893-908.

26. Kajiyama, T; Jennex, M; and Addo, T. To cloud or not to cloud: How risks and threats are affecting cloud adoption decisions. Information & Computer Security, 25, 5 (2017), 634-659.

27. Karunagaran, S; Mathew, SK; and Lehner, F. Differential cloud adoption: A comparative case study of large enterprises and SMEs in Germany. Information Systems Frontiers, 21, 4 (2019), 861-875.

28. Kehr, F; Kowatsch, T; Wentzel, D; and Fleisch, E. Blissfully ignorant: The effects of general privacy concerns, general institutional trust, and affect in the privacy calculus. Information Systems Journal, 25, 6 (2015), 607-635.

29. Krasnova, H; Veltri, NF; and Günther, O. Self-disclosure and privacy calculus on social networking sites: The role of culture. Business & Information Systems Engineering, 4, 3 (2012), 127-135.

30. Kreizman, G. Gartner Magic Quadrant for Access Management, Worldwide. (2018),

Date Accessed: December 31, 2020, retrieved from https://www.gartner.com/en/documents/3879469/magic-quadrant-for-accessmanagement-worldwide

31. Kshetri, N. Privacy and security issues in cloud computing: The role of institutions and institutional evolution. Telecommunications Policy, 37, 4-5 (2013), 372-386.

32. Kung, L; Cegielski, CG; and Kung, H-J. An integrated environmental perspective on software as a service adoption in manufacturing and retail firms. Journal of Information Technology, 30, 4 (2015), 352-363.

33. Lansing, J and Sunyaev, A. Trust in cloud computing: Conceptual typology and trustbuilding antecedents. The DATABASE for Advances in Information Systems, 47, 2 (2016), 58-96.

34. Laufer, RS and Wolfe, M. Privacy as a concept and a social issue: A multidimensional developmental theory. Journal of Social Issues, 33, 3 (1977), 22-42.

35. Lee, S-G; Chae, SH; and Cho, KM. Drivers and inhibitors of SaaS adoption in Korea. International Journal of Information Management, 33, 3 (2013), 429-440.

36. Lincoln, YS and Guba, EG. Naturalistic inquiry. Newbury Park, CA: Sage Publications, Inc., 1985.

37. Liu, Y; Dong, S; Wei, J; and Tong, Y. Assessing cloud computing value in firms through socio-technical determinants. Information & Management, 57, 8 (2020), 103369.

38. Lobschat, L; Mueller, B; Eggers, F; Brandimarte, L; Diefenbach, S; Kroschke, M; and Wirtz, J. Corporate digital responsibility. Journal of Business Research, 122, (2021), 875-888.

39. McCole, P; Ramsey, E; and Williams, J. Trust considerations on attitudes towards online purchasing: The moderating effect of privacy and security concerns. Journal of Business Research, 63, 9-10 (2010), 1018-1024.

40. Mell, P and Grance, T. The NIST Definition of Cloud Computing (SP 800-145). National Institute of Standards and Technology, Gaithersburg, MD. 2011.

41. Miltgen, CL and Peyrat-Guillard, D. Cultural and generational influences on privacy concerns: A qualitative study in seven European countries. European Journal of Information Systems, 23, 2 (2014), 103-125.

42. Moraetes, G. Meeting Identity and Access Management Challenges in the Era of Mobile and Cloud. (2018), Date Accessed: retrieved from https://securityintelligence.com/meeting-identity-and-access-management-challengesin-the-era-of-mobile-and-cloud/

43. Morgan, L and Conboy, K. Key factors impacting cloud computing adoption. IEEE Computer, 46, 10 (2013), 97-99.

44. Nuñez, D and Agudo, I. BlindIdM: A privacy-preserving approach for identity management as a service. International Journal of Information Security, 13, 2 (2014), 199–215.

45. Oliveira, T; Thomas, M; and Espadanal, M. Assessing the determinants of cloud computing adoption: An analysis of the manufacturing and services sectors. Information & Management, 51, 5 (2014), 497-510.

46. Oltsik, J. Identity and access management infrastructure is misaligned with security. (2016), Date Accessed: December 31, 2020, retrieved from https://www.csoonline.com/article/3073525/identity-and-access-management-iaminfrastructure-is-misaligned-with-security.html

47. Paré, G. Investigating Information Systems with Positive Case Study Research. Communications of the Association for Information Systems, 13, (2004), 233-264.

48. Pavlou, PA; Liang, H; and Xue, Y. Understanding and mitigating uncertainty in online exchange relationships: A principal-agent perspective. MIS Quarterly, 31, 1 (2007), 105-136.

49. Polyviou, A and Pouloudi, N. Understanding cloud adoption decisions in the public sector. Presented at 2015 48th Hawaii International Conference on System Sciences, Kauai, Hawaii, 2015, pp. 2085-2094.

50. Sarker, S; Chatterjee, S; Xiao, X; and Elbanna, A. The sociotechnical axis of cohesion

for the IS discipline: Its historical legacy and its continued relevance. MIS Quarterly, 43, 3 (2019), 695-720.

51. Schneider, S and Sunyaev, A. Determinant factors of cloud-sourcing decisions: Reflecting on the IT outsourcing literature in the era of cloud computing. Journal of Information Technology, 31, 1 (2016), 1-31.

52. Schramm-Nielsen, J. How to interpret uncertainty avoidance scores: A comparative study of Danish and French firms. Cross Cultural Management, 7, 4 (2000), 3-11.

53. Schwartz, PM. The value of privacy federalism. Cambridge, United Kingdom: Cambridge University Press, 2015.

54. Sharma, M and Sehrawat, R. A hybrid multi-criteria decision-making method for cloud adoption: Evidence from the healthcare sector. Technology in Society, 61, (2020), 101258.

55. Srite, M and Karahanna, E. The role of espoused national cultural values in technology acceptance. MIS Quarterly, 30, 3 (2006), 679-704.

56. Stallings, W and Brown, L. Computer security: principles and practice, 3rd ed: Pearson Education Upper Saddle River, NJ, USA, 2015.

57. Strauss, A and Corbin, J. Basics of qualitative research: Grounded theory procedures and techniques. Newbury Park, CA: Sage Publications, 1990.

58. Trenz, M; Huntgeburth, J; and Veit, D. Uncertainty in cloud service relationships: Uncovering the differential effect of three social influence processes on potential and current users. Information & Management, 55, 8 (2018), 971-983.

59. Trigueros-Preciado, S; Pérez-González, D; and Solana-González, P. Cloud computing in industrial SMEs: Identification of the barriers to its adoption and effects of its application. Electronic Markets, 23, 2 (2013), 105-114.

60. van de Weerd, I; Mangula, IS; and Brinkkemper, S. Adoption of software as a service in Indonesia: Examining the influence of organizational factors. Information & Management, 53, 7 (2016), 915-928.

61. Vance, A; Elie-Dit-Cosaque, C; and Straub, DW. Examining trust in information

technology artifacts: The effects of system quality and culture. Journal of Management Information Systems, 24, 4 (2008), 73-100.

62. Verizon. Data Breach Investigations Report. (2020), Date Accessed: December 31, 2020, retrieved from https://enterprise.verizon.com/resources/reports/dbir/

63. Xu, H; Teo, H-H; Tan, BC; and Agarwal, R. The role of push-pull technology in privacy calculus: The case of location-based services. Journal of Management Information Systems, 26, 3 (2009), 135-174.

64. Yin, RK. Case Study Research: Design and Methods, 6th ed. Thousand Oaks, CA: Sage Publications, 2018.

65. Yu, Y; Li, M; Li, X; Zhao, JL; and Zhao, D. Effects of entrepreneurship and IT fashion on SMEs’ transformation toward cloud service through mediation of trust. Information & Management, 55, 2 (2018), 245-257.
