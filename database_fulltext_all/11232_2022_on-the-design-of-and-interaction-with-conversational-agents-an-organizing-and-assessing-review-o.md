---
otero_id: 11232
otero_key: "FJARTSNG"
title: "On the Design of and Interaction with Conversational Agents: An Organizing and Assessing Review of Human-Computer Interaction Research"
authors: "Stephan Diederich; Alfred Benedikt Brendel; Stefan Morana; Lutz Kolbe"
year: "2022"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00724"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2022

# On the Design of and Interaction with Conversational Agents: An Organizing and Assessing Review of Human-Computer Interaction Research

Stephan Diederich , diederich@icloud.com

Alfred Benedikt Brendel , Alfred\_benedikt.brendel@tu-dresden.de

Stefan Morana , stefan.morana@uni-saarland.de

Lutz Kolbe , lkolbe@uni-goettingen.de

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# On the Design of and Interaction with Conversational Agents: An Organizing and Assessing Review of Human-Computer Interaction Research

Stephan Diederich<sup>1</sup>, Alfred Benedikt Brendel<sup>2</sup>, Stefan Morana<sup>3</sup>, Lutz Kolbe<sup>4</sup>

<sup>1</sup>University of Göttingen, Germany, diederich@icloud.com <sup>2</sup>TU Dresden, Germany, alfred\_benedikt.brendel@tu-dresden.de <sup>3</sup>Saarland University, Germany, stefan.morana@uni-saarland.de <sup>4</sup>University of Göttingen, Germany, lkolbe@uni-goettingen.de

## Abstract

Conversational agents (CAs), described as software with which humans interact through natural language, have increasingly attracted interest in both academia and practice because of improved capabilities driven by advances in artificial intelligence and, specifically, natural language processing. CAs are used in contexts such as people’s private lives, education, and healthcare, as well as in organizations to innovate or automate tasks—for example, in marketing, sales, or customer service. In addition to these application contexts, CAs take on different forms in terms of their embodiment, the communication mode, and their (often human-like) design. Despite their popularity, many CAs are unable to fulfill expectations, and fostering a positive user experience is challenging. To better understand how CAs can be designed to fulfill their intended purpose and how humans interact with them, a number of studies focusing on human-computer interaction have been carried out in recent years, which have contributed to our understanding of this technology. However, currently, a structured overview of this research is lacking, thus impeding the systematic identification of research gaps and knowledge on which future studies can build. To address this issue, we conducted an organizing and assessing review of 262 studies, applying a sociotechnical lens to analyze CA research regarding user interaction, context, agent design, as well as CA perceptions and outcomes. This study contributes an overview of the status quo of CA research, identifies four research streams through cluster analysis, and proposes a research agenda comprising six avenues and sixteen directions to move the field forward.

Keywords: Conversational Agent, Chatbot, Digital Assistant, Virtual Human, Robot, Organizing Review, Assessing Review, Human-Computer Interaction

Dorothy E. Leidner was the accepting senior editor. This research article was submitted on January 14, 2019 and underwent three revisions.

## 1 Introduction

Technological advances continue to drive digital transformation and change the way we live, work, and interact with one another (Davenport & Kirby, 2016; McAfee & Brynjolfsson, 2017). Advances in artificial intelligence (AI) such as machine learning and natural language processing are essential drivers in this development, transforming machines into seemingly intelligent entities capable of conversing in natural language and creating meaning through written or spoken words (Brynjolfsson & McAfee, 2016). Benefiting from these advances, conversational agents (CAs) are increasingly attracting research and practice interest (McTear, 2017). Interacting with a system using natural language promises to improve ease of use and ensure faster completion of user requests while creating the feeling of a human-like interaction (Følstad & Brandtzæg, 2017). For users, CAs can function in various contexts, ranging from digital personal assistants in mobile devices, such as Apple’s Siri or Google Assistant, to specific purposes like in-car assistance (Laumer et al. 2019). For organizations, CAs offer the possibility of automating and innovating processes in areas such as human resources (Liao et al., 2018), customer service (Ashktorab et al., 2019), and sales (Vaccaro et al., 2018).

Recent examples developed by Facebook and Google underline the popularity and potential of CAs. After launching its new Messenger platform, more than 100,000 bots appeared on Facebook within the first year (Johnson, 2018). Further, Google demonstrated the future potential of CAs at its 2018 developer conference by having their assistant autonomously make a hairdresser’s appointment via a telephone conversation with a real person on the other end (Welch, 2018). Gartner predicts that 70% of white-collar workers will interact with systems using conversational interfaces in their daily work by 2022 (Goasduff, 2019). Despite their potential, many CAs do not meet expectations and are discontinued because of flaws related to their design, such as unappealing appearance, lacking conversational abilities, or unrealizable user expectations (Ashktorab et al., 2019; Ben Mimoun et al., 2012; Lahoual & Fréjus, 2019; Luger & Sellen, 2016). The complexity of designing such agents is particularly driven by the human’s social responses to the cues incorporated in these artifacts, such as interaction via natural language, human names, or the social roles of these agents (Feine et al., 2019; Seeger et al., 2018). Such social responses affect the individual’s perception of these agents and foster high user expectations, which are often not in line with the agents’ actual capabilities (Ben Mimoun et al., 2012; Luger & Sellen, 2016). In summary, designing CAs and understanding how they interact with humans remains challenges in terms of research as well as practice (Schuetz & Venkatesh, 2020).

In research, a multitude of studies, particularly in the field of human-computer interaction (HCI), have contributed to addressing this challenge. In particular, a renewed interest in research on CAs has emerged in the information systems (IS) and computer science (CS) communities (McTear, 2017; Rzepka & Berger, 2018). Researchers from both disciplines have investigated CAs with different technological properties, such as voice versus text communication modes (Cho, 2019; Schroeder & Schroeder, 2018), and virtual versus physical embodiment (Araujo, 2018; Seymour et al., 2018). Researchers have also explored different contexts, such as interactive tutoring (Fryer et al., 2017) and customer service (Xu et al., 2017). Moreover, prior studies have focused on different aspects related to the perception of such agents and interaction outcomes— for example, anthropomorphism (Araujo, 2018; Seeger et al., 2018), trust (Benlian et al., 2020; Elson et al., 2018; Schuetzler et al., 2014), and number of digital products sold (Kim et al., 2018). In short, the design of and interaction with present-day CAs offer many research opportunities, and a variety of studies are available in this research area.

However, this variety of studies also comes with the challenge of acquiring an overview of the topic. Existing reviews on CAs focus on selected aspects of the interaction with and design of CAs, such as trust (Zierau et al., 2020) and social cues (Feine et al., 2019); they also investigate CAs in specific contexts, such as the digital workplace (Wolff et al., 2019), or, more abstractly, review AI-based applications (Rzepka & Berger, 2018). An overview of CA research covering different contexts, types of CAs, and users’ perceptions is not available. Without such an overview, however, researchers face difficulties in systematically identifying and addressing the research gaps and knowledge upon which to build. To address this issue, we organize existing studies on CAs, assess the status quo, and contribute potential avenues for future work in this area.

The remainder of this article is organized as follows: first, we provide a brief overview of CAs and introduce the framework for our analysis. Next, we describe our research approach, present the overarching observations identified in our literature review, and discuss four research streams based on a cluster analysis. Building on these results, we derive six avenues containing sixteen specific directions for future research in this area.

## 2 Research Background

CAs are based on the idea of interacting with users through natural language as in human-to-human conversations (Dale, 2016; McTear et al., 2016). CAs are variously and interchangeably called digital assistants, chatbots, interactive agents, etc. (Maedche et al., 2019; Stieglitz et al., 2018). Different definitions are given for CAs—for example, an agent that “interacts with users, turn by turn by using natural language” (Comendador et al., 2015, p. 137), “computer programs designed to respond to users in natural language, thereby mimicking conversations between people” (Miner et al., 2016, p. 619), and a concept intended to “achieve some result by conversing with a machine in a dialogic fashion, using natural language” (Dale, 2016, page 811). While each of these definitions highlights different characteristics of CAs, such as turn-taking (Comendador et al., 2015) or mimicking conversations (Miner et al., 2016), they all share the idea of natural language interaction. For the purposes of this research, we consider CAs to be technological artifacts with which users interact through natural language, both in written and spoken form.

## 2.1 An Overview of Conversational Agents

The basic idea of interacting with technological artifacts through natural language has already emerged by the 1960s, when Joseph Weizenbaum (1966) developed ELIZA. While the fundamental idea of natural language interaction is the same for all CAs, agents assume different forms, which are distinguished by communication mode, embodiment, and the context in which they are used (Cassell et al., 1999; Cowell & Stanney, 2005; Gnewuch et al., 2017):

Communication mode: CAs can communicate via voice (Cowan et al., 2015), text (Schroeder & Schroeder, 2018), or both (Cho, 2019)

Embodiment: CAs can be disembodied (Araujo, 2018), virtually embodied (Diederich et al., 2019), or physically embodied (Nunamaker et al., 2011)

Context: CAs can be used for general-purpose conversations or be domain specific—for example, intended for a specific task or business function (Gnewuch et al., 2017).

Multiple studies have addressed the interaction with CAs regarding user responses such as user trust (Elson et al., 2018; Seeger et al., 2017), authenticity (Wünderlich & Paluch, 2017), and empathy (Leite et al., 2013; McQuiggan & Lester, 2007). CAs have been studied in different contexts—for example, in legal research (Sugumaran & Davis, 2001), lie detection (Nunamaker et al., 2011), financial advising (Morana et al., 2020), and data analytics (Matsushita et al., 2004). Concerning their application in organizations, recent research has attended to different business functions, including human resources (Diederich, Brendel, & Kolbe, 2020; Liao et al., 2018) and marketing and sales (Qiu & Benbasat, 2009; Vaccaro et al., 2018). In practice, different CAs have emerged over time—for example, IKEA’s Anna (Wakefield, 2016).

In the past, because of CAs’ reliance on simple pattern matching, they were limited in terms of both understanding a user’s intent (i.e., the meaning behind a message) and providing purposeful feedback (Berg, 2015; Knijnenburg & Willemsen, 2016), which often led to CAs being discontinued (Ben Mimoun et al., 2012). However, with advances in natural language processing, as well as machine learning, CA capabilities have greatly improved in recent years, contributing to a renewed interest in terms of both research and practice (McTear, 2017; Oracle, 2016). Today, most smartphones are equipped out-of-the-box with voice-based CAs—for example, Google Assistant and Siri (Burton & Gaskin, 2019)—and devices such as Amazon’s Alexa are used in private households (Purington et al., 2017) and team collaborations (Winkler et al., 2019). Further, companies are exploring the potential of physically embodied CAs to provide services, such as SoftBank’s humanoid robot “Pepper” (Stock & Merkle, 2018a).

Similarly, text-based CAs, often referred to as chatbots, are increasingly available in different contexts. For example, the Dutch airline KLM introduced a text-based CA that helps users to find and book flights (Vogel-Meijer, 2018), the coffee shop chain Starbucks designed a CA called “Barista” to support ordering products (Perez, 2016), and the American railroad company Amtrak answers five million requests per year through its “Julie” CA (NextIT, 2018). Regarding CAs with a virtual interactive embodiment, IPSoft developed an agent known as “Amelia,” which, for example, automates information technology (IT) service desk tasks for a medical supplies manufacturer and offers customer services for a telecom provider (Ipsoft, 2020) (see Figure 1).

## 2.2 Human-Computer Interaction

Human-computer interaction (HCI) research as a research domain dates back to the early 1980s (Card et al., 1980; Carroll, 2020). More recent HCI research has investigated “the ways humans interact with information, technologies, and tasks, especially in business, managerial, organizational, and cultural contexts” (Zhang et al., 2002, p. 333). The first ACM Computer-Human Interaction (CHI) Conference, the premier conference on HCI, was established in 1982. Since then, this research field has also expanded into other disciplines, such as CS, (cognitive) psychology, human factors, and IS. In the IS discipline, after Gerlach and Kuo (1991) recognized the interdisciplinary nature of HCI, numerous conceptual and empirical publications on HCI appeared in various disciplines (Carroll, 2020; Olson & Olson, 2003; Zhang & Li, 2004).

The interaction between humans and computers can be related to the concept of sociotechnical systems. A sociotechnical system relies on the interplay of three key elements (Goodhue & Thompson, 1995; Heinrich et al., 2011): the human that wants to achieve a specific goal, the task that the user must accomplish to achieve the goal, and the technology (i.e., software, hardware, or data) that the user utilizes to complete the task. Taking a sociotechnical perspective, Zhang and Li (2005) assessed the intellectual development of HCI research in the IS discipline, proposing an extended framework consisting of humans interacting with technology in a specific context, which ultimately leads to a set of outcomes and perceptions. This framework adds the dimension of perception change through technology to the understanding of HCI.

![](/api/attachments/FJARTSNG/fulltext/images/9dd48c8acb45986af0f57351b79bafb9b0f9c3cb42bd795967d27039b4bb7239.jpg)  
Figure 1. Examples of Conversational Agents

In CA research, the anthropomorphic design, related human-like perception, and the application context are key research objects, whereas the sociotechnical framework provides a valuable lens to investigate the continuously growing body of knowledge on the interaction between humans and CAs. Therefore, drawing on the framework by Zhang and Li (2005), we derive a framework to organize the existing research, conduct a literature review, and analyze the identified studies in order to determine current trends as well as outline an agenda for future work.

## 3 Method: A Review of HCI Research on CAs

In this section, we outline our study’s research framework, as well as the method we used to identify and analyze research on CAs in IS and CS research.

## 3.1 A Framework for Human-Computer Interaction via Natural Language

As a lens for our review of CA studies, we draw on and adapt the research framework proposed by Zhang and Li (2005). Drawing on this framework, we review four dimensions of CA studies: context, human, agent, and perceptions and outcomes (see Figure 2).

First, we consider the context in which the CA is applied. On an abstract level, we can distinguish between professional and private contexts. Professional contexts comprise, for example, the internal use of CAs for individual task support (e.g., scheduling appointments, see Bittner & Shoury, 2019; Fast et al., 2017), CAs in team collaboration (e.g., managing tasks within a team, see Bittner et al., 2019; Seeber et al., 2019a), and the customer interface (e.g., providing services, see Diederich et al., 2021; Vaccaro et al., 2018; Wünderlich & Paluch, 2017). In private life, CAs are primarily used for individual task support (e.g., searching for information online, see Porcheron et al., 2018), education (Graesse et al., 2017), and personal health (Yokotani et al., 2018). Further, studies that do not fit any of these two contexts are classified as “other” (e.g., CAs for legal research, see Sugumaran & Davis, 2001), and articles that do not fit a specific context are considered “generic” (e.g., Candello et al., 2019).

Second, the dimension human refers to the user interacting with the CA. In general, users’ characteristics include demographic aspects such as age, gender, cultural background, experience both with CAs and with the task at hand, as well as aspects related to individual dispositions, including a user’s personality or cognitive style (Zhang & Li, 2005)

The third dimension, agent, includes characteristics of the CA itself. These characteristics comprise the primary communication mode, i.e., the agent adjusted for interaction via speech, text, or both (Gnewuch et al., 2017), as well as the agent’s embodiment, which can be physical, as with service robots (Stock & Merkle, 2018b), virtual as with interactive avatars (Seymour et al., 2018) or static avatars (Wünderlich & Paluch, 2017), or nonexistent—for example, a CA without any visual embodiment (Abul et al., 2018). Further, CAs exhibit different design components comprising an identity (e.g., name), verbal communication (e.g., expression of emotions), and nonverbal communication (e.g., response delays to mimic thinking and typing, see Seeger et al., 2018).

Finally, perceptions and outcomes refer to the investigated topic in terms of the use and impact of the technology. This dimension shows how users perceive a CA during an interaction and demonstrates the interaction’s impact. Following Zhang and Li’s (2005) suggestions, these topics can be divided into eight distinct categories, as shown in Table 1.

![](/api/attachments/FJARTSNG/fulltext/images/e811ecd8d79440ac3b70b71897e5a850c4f7a5835ea2d8aa4b448da7f8c2e90a.jpg)  
Figure 2. Research Framework

Table 1. Categories and Exemplary Constructs in the Dimension Perceptions and Outcomes

<table><tr><td>Categories</td><td>Exemplary constructs</td></tr><tr><td>Perception</td><td>Humanness, similarity, reciprocity, social distance, social presence</td></tr><tr><td>Acceptance</td><td>Usefulness, ease of use</td></tr><tr><td>Attitude</td><td>Attitude, satisfaction, preference</td></tr><tr><td>Performance</td><td>Productivity, effectiveness, efficiency</td></tr><tr><td>Emotion</td><td>Affect, hedonic quality, enjoyment, humor, intrinsic motivation</td></tr><tr><td>Trust</td><td>Trust, risk, loyalty, security, privacy</td></tr><tr><td>Learning</td><td>Learning models, learning processes, general training</td></tr><tr><td>Ethics</td><td>Ethical belief, ethical behavior, ethics</td></tr><tr><td>Relationship</td><td>Influence, interdependence, interference, agreement/disagreement</td></tr></table>

Table 2. Research Approach

<table><tr><td></td><td>Step 1: Collect literature</td><td>Step 2: Code studies</td><td>Step 3: Conduct analyses</td></tr><tr><td>Input</td><td>Search query</td><td>Literature database</td><td>Coded literature database</td></tr><tr><td>Method</td><td>Literature search</td><td>Closed coding</td><td>Concept matrix, cluster analysis</td></tr><tr><td>Steps</td><td>Conduct database search and identify relevant CA studies</td><td>Code CA studies using dimensions from the research framework</td><td>Create concept matrix and descriptive statistics, conduct clustering</td></tr><tr><td>Results</td><td>Literature database</td><td>Coded literature database</td><td>Concept matrix and four research streams (cluster)</td></tr></table>

To complement the dimensions of the research framework, we further included the research method, unit of analysis, and the theoretical grounding of the study in our review. We thereby sought to better understand the methodological focus of current CA research and theories used to inform CA design, and provide insights into the user’s interaction with CAs. Following Bariff and Ginzberg’s (1982) explanations, we differentiate between studies on the individual level (e.g., user reactions toward CAs), the group level (e.g., CAs as team members), the organizational level (e.g., use cases for CAs in enterprises), and the interorganizational level. To analyze the methods used in the studies, we drew on the research methods that Banker and Kauffman (2004) described and used in their assessment of IS research.

## 3.2 Identification, Coding, and Analysis of CA Literature

To collect and analyze existing studies on CAs in IS and CS research, we followed a process based on the combination of the systematic literature review guidelines by Webster and Watson (2002), vom Brocke et al. (2009), and Bandara et al. (2015). Since our goal is to provide an organizing and assessing review of research on CAs (Leidner, 2018), we focus on the research outcomes of the studies in the scope of this review, choosing to organize them conceptually (Cooper, 1988) using the HCI research framework adapted from Zhang and Li’s (2005) seminal work. We took a three-step approach (Table 2): collecting literature for the review (Step 1), coding the studies qualitatively using the research framework (Step 2), and conducting analyses (Step 3) by creating a concept matrix, investigating CA research over time and clustering the studies to identify research streams.

To begin, we first identified the relevant outlets for our search process in Step 1. The IS and CS communities have conducted extensive work on CAs as part of HCI research; thus, we purposefully selected journals from these fields. For the IS discipline, we focused on the Basket of Eight journals, and for CS, we selected four well-regarded journals that focus on HCI (i.e., Advances in Human-Computer Interaction, ACM Transactions on Computer-Human Interaction, Computers in Human Behavior, and International Journal of Human-Computer Studies) for our search. We extended the data search by adding high-quality conference proceedings to take more recent work into account, as renewed interest in CA research emerged only a few years ago (Pfeuffer, 2019; Rzepka & Berger, 2018). Thus, we complemented our review with proceedings from major IS conferences (ICIS, ECIS, HICSS, AMCIS, and PACIS) and the major CS conference (ACM CHI Conference on Human Factors in Computing Systems). To collect appropriate studies, we used the Web of

Science, AISeL, ACM Digital Library, and the websites of the respective outlets. We conducted the search in January 2019 and updated it in November 2019, using the following search query:

## ((Conversational OR Interactive OR Virtual) AND Agent) OR Chatbot OR Digital Assistant)

The query returned 8,768 results in all, for which we scanned titles, abstracts, and content to identify studies that focus on CAs. Further, we conducted a forward and backward search to identify additional studies. After this search and filtering process, 262 studies remained in our database (Table 3, outlets in alphabetical order).

In the second step of our research, we coded the 262 studies using the dimensions of our research framework (see Figure 2). Complementing the framework dimensions, we coded the research approach (empirical or conceptual), method (e.g., laboratory experiment or survey), unit of analysis (e.g., technology or individual), and noted the study’s theoretical grounding (e.g., similarity-attraction theory, see Byrne, 1971; Byrne & Griffitt, 1969; computers are social actors paradigm, see Nass & Moon, 2000; Reeves & Nass, 1996).

To ensure the reliability of the coding, three of the authors coded a random set of twenty studies independently in a pretest using preliminary coding guidelines. The authors then discussed the coded studies to identify discrepancies and shortcomings in the codes. Based on the results of this pretest, we adjusted the codes and the coding guidelines (e.g., adding “technology” as a unit of analysis for studies exclusively containing artifact descriptions or selection of multiple codes in the dimensions “perceptions and outcomes”) (see Appendix A). After this pretest, one author coded the remaining studies and, when required, discussed uncertainties with the other authors. Based on the coded 262 studies, we carried out three analyses in Step 3 to assess the state of research on CAs. First, we created a concept matrix to foster a conceptual understanding of the studies, going beyond descriptive content summaries, and we viewed the distribution of characteristics in the coding dimensions (Webster & Watson, 2002). Second, we conducted a cluster analysis to empirically identify research streams in the extant CA literature. Following Punj and Stewart’s (1983) recommendations, we first identified a suitable number of clusters using a hierarchical clustering approach, namely Ward’s method with squared Euclidean distance, and afterward used k-means as an iterative partitioning technique. We selected a solution with four clusters after reviewing the scree plot dendrogram and coefficient delta (see Appendix B). The k-means procedure then computed seven iterations until no further significant enhancements were realized. Finally, we created graphical representations to show how CA research had developed over time, according to both discipline (IS, CS) and research stream.

Table 3. Literature Search Results

<table><tr><td>Outlet</td><td>Search results</td><td>Relevant</td></tr><tr><td>ACM CHI Conference on Human Factors in Computing Systems</td><td>3,661</td><td>102</td></tr><tr><td>ACM Transactions on Computer-Human Interaction</td><td>144</td><td>4</td></tr><tr><td>Advances in Human-Computer Interaction</td><td>78</td><td>6</td></tr><tr><td>Americas Conference on Information Systems</td><td>1,250</td><td>9</td></tr><tr><td>Computers in Human Behavior</td><td>1,072</td><td>42</td></tr><tr><td>European Conference on Information Systems</td><td>334</td><td>7</td></tr><tr><td>Hawaii International Conference on System Sciences</td><td>287</td><td>10</td></tr><tr><td>International Conference on Information Systems</td><td>731</td><td>26</td></tr><tr><td>International Journal of Human-Computer Studies</td><td>421</td><td>47</td></tr><tr><td>Journal of Management Information Systems</td><td>1</td><td>2</td></tr><tr><td>Journal of the Association for Information Systems</td><td>246</td><td>3</td></tr><tr><td>Pacific Asia Conference on Information Systems</td><td>543</td><td>4</td></tr><tr><td>Total</td><td>8,768</td><td>262</td></tr><tr><td colspan="3">Note: Some studies were identified through backward and forward search</td></tr></table>

## 4 Results

Our organizing and assessing review offers insight into the state of CA research and allows us to derive recommendations to advance our understanding of the design of and interaction with CAs. In this section, based on our review, we first describe our general observations on CA research. Next, we outline four research streams identified through a cluster analysis of the studies in our sample.

## 4.1 Overarching Observations

In accordance with our review framework (see Figure 2), we relate our findings to the technical characteristics of the studied CAs (“agent”), the application context, the user (“human”), and the perceptions and outcomes emerging from the interaction.

## 4.1.1 Agent Dimension

Regarding the agents we investigated (see Table 4), we found that around half of the studies focused on communication with the agent via written text (e.g., chatbots, see Adam & Klumpe, 2019; Vaccaro et al., 2018, around 40% explored speech-based CAs such as digital assistants like Siri or Alexa, e.g., Burton & Gaskin, 2019; Winkler & Roos, 2019), whereas nearly 10% studied both communication modes, mostly to identify commonalities or differences in human interaction with such agents via text or speech (e.g., Schroeder & Schroeder, 2018).

Concerning the representation or embodiment of the CA, nearly half of the studies investigated agents without any form of embodiment (i.e., without a static/interactive digital avatar or physical appearance, e.g., Gnewuch et al., 2018; Schuetzler et al., 2018). One-fourth of these studies focused on virtual interactive representations (i.e., with a virtual human, e.g., Cafaro et al., 2016; Krämer et al., 2013). Further, 17% of the studies address CAs with virtual static avatars (for example, images, e.g., Seeger et al., 2018), 8% explore agents with physical embodiment (for example, service robots, e.g., Stock & Merkle, 2018a, 2018b), and a handful investigate and compare multiple embodiments (e.g., Gong, 2008; Seymour et al., 2017).

Around half of the studies focus on verbal communication (e.g., dialogue repair strategies, Corti & Gillespie, 2016) or expressing emotions (e.g., Beale & Creed, 2009; Niewiadomski & Pelachaud, 2010), around one third of the studies examine the agent’s (human) identity (for example, the impact of agent representations on user perception, e.g., Vugt et al., 2010), and one fourth explore nonverbal communication (e.g., response times, Gnewuch et al., 2018) or facial expressions (De Rosis et al., 2003). Table 4 summarizes the types of CAs investigated in the studies.

## 4.1.2 Context Dimension

Concerning the context in which CAs are applied (Table 5), 45% of the studies do not explicitly specify a context, investigating only the interaction of humans and CAs generally (e.g., Banks, 2018; Chaves &

Gerosa, 2018). Around 21% of the studies address professional contexts (e.g., customer service, Baier et al., 2018; Xu et al., 2017) or marketing and sales (Kim et al., 2018; Vaccaro et al., 2018), 12% address education (e.g., interactive tutoring systems (Hobert & Wolff, 2019; Winkler & Roos, 2019), 9% deal with health applications (e.g., digital health advisors, Gambino et al., 2019; Powers & Kiesler, 2006), or behavior change agents, Sebastian & Richards, 2017). The remaining studies (6.9%) focus on private individual task support (Porcheron et al., 2018; Purington et al., 2017), multiple contexts (e.g., Meyer von Wolff et al., 2019), specific contexts that do not fit the aforementioned categories (e.g., legal research, Sugumaran & Davis, 2001; CAs as role models, Rosenberg-Kima et al., 2008).

Table 4. Types of Agents Investigated in the Studies

<table><tr><td colspan="2">Communication mode</td></tr><tr><td>Text-based</td><td>51.9%</td></tr><tr><td>Speech-based</td><td>38.9%</td></tr><tr><td>Both</td><td>9.2%</td></tr><tr><td colspan="2">Design dimensions*</td></tr><tr><td>Verbal communication</td><td>49.2%</td></tr><tr><td>(Human) identity</td><td>31.7%</td></tr><tr><td>Nonverbal communication</td><td>24.4%</td></tr><tr><td colspan="2">Representation / embodiment</td></tr><tr><td>None</td><td>46.2%</td></tr><tr><td>Virtual interactive</td><td>24.8%</td></tr><tr><td>Virtual static</td><td>16.8%</td></tr><tr><td>Physical</td><td>8.0%</td></tr><tr><td>Multiple</td><td>4.2%</td></tr><tr><td colspan="2">Note: * Multiple selections possible</td></tr></table>

Table 5. CAs’ Application Contexts in the Studies

<table><tr><td>Generic</td><td>45.0%</td></tr><tr><td>Customer interface</td><td>13.4%</td></tr><tr><td>Education</td><td>11.8%</td></tr><tr><td>Health</td><td>8.8%</td></tr><tr><td>Private task support</td><td>6.9%</td></tr><tr><td>Other</td><td>5.0%</td></tr><tr><td>Professional task support</td><td>4.6%</td></tr><tr><td>Team collaboration</td><td>3.1%</td></tr><tr><td>Multiple</td><td>1.5%</td></tr></table>

Table 6. User Characteristics investigated in the Studies

<table><tr><td>Gender</td><td>11.8%</td></tr><tr><td>Age</td><td>10.3%</td></tr><tr><td>CA experience</td><td>6.1%</td></tr><tr><td>Personality</td><td>4.6%</td></tr><tr><td>Cultural background</td><td>2.3%</td></tr><tr><td>Task experience</td><td>1.5%</td></tr><tr><td>Cognitive style</td><td>1.1%</td></tr><tr><td>Individual education</td><td>0.0%</td></tr></table>

## 4.1.3 Human Dimension

In terms of the user, the vast majority of the studies do not distinguish between users according to their characteristics (Table 6). For example, most experimental studies show no significant differences between control and treatment groups concerning demographics, and do not investigate the potential effects that such characteristics have as control variables. The influence of demographic characteristics such as the user’s age (Chattaraman et al., 2018; Kowalski et al., 2019) or gender (Braun & Alt, 2019; Meier et al., 2019) on the perception of and interaction with CAs is discussed or controlled for in only a few of the identified studies (10-12%). Similarly, only a fraction of the studies (explore the impact of individual experience with CAs (6%) Fadhil & Villafiorita, 2017; Schroeder & Schroeder, 2018) or the task at hand (2%) (Ashktorab et al., 2019; Laumer et al., 2019). Further user characteristics, such as personality (5%) (Mou & Xu, 2017; Straßmann et al., 2018), cultural features (2%) (Duan et al., 2018; Schlesinger et al., 2018), cognitive style (1%) (Crockett et al., 2017), or the user’s education (0%) are very rarely studied.

## 4.1.4 Perceptions and Outcomes Dimension

Regarding the agent’s perception and the interaction’s outcomes, we found that many studies focus on constructs related to users’ attitudes toward the CA (24%), the agent’s perception (23%), system or task performance (20%), and acceptance (17%). Concerning attitude, Burgoon et al. (2016), for example, measure the user’s perceived sense of connectedness with the agent after the interaction, and Vugt et al. (2010) assess perceived facial similarity with an interactive CA.

Regarding perception, many of the reviewed studies focus on comparing the effect of different design options (regarding identity, verbal communication, and nonverbal communication) on perceived anthropomorphism. For example, Seeger et al. (2018) varied an agent’s verbal and nonverbal communication (use of self-references and emoticons) and its humanlike identity (a human person’s name and image), to study the impact on perceived anthropomorphism. Similarly, Gnewuch et al. (2018) and Diederich et al. (2019) studied the impact of response times and preset answer options on users’ perception of humanness in a customer service encounter with a chatbot. Araujo (2018) explored different language styles and framings to introduce the CA, and names in relation to anthropomorphism.

Concerning performance, CA researchers proposed different system-related measures, such as response success rate (e.g., Liao et al., 2018) and perceived conversational ability (e.g., Shah et al., 2016). Additionally, some reviewed studies used performance measures related to the interaction’s outcomes, considering, for example, purchase amounts for digital content provided by Alexa (Son & Wonseok, 2018) and completion time in a microtask crowdsourcing context (Mavridis et al., 2019).

Other authors draw on constructs in acceptance models, such as the technology acceptance model (TAM) (Davis, 1989) and the unified theory of acceptance and use of technology (UTAUT) (Venkatesh et al., 2003). Examples of studies measuring acceptance-related constructs are Qiu and Benbasat (2010), who assessed the perceived usefulness of a product recommendation agent depending on different demographic embodiments, and Hobert (2019) who drew on ease of use and intention to use to evaluate a CA intended to teach programming to IS and CS students.

Further studies focus on constructs related to emotion (12%), such as empathy (Leite et al., 2013; McQuiggan & Lester, 2007) and trust (Saffarizadeh et al., 2017; Sohn, 2019). Other studies focus on the relationship between the user and the agent (11%) in terms of, for example, social roles (Seering et al., 2019) and social distance (Kim & Mutlu, 2014). Constructs less frequently studied include the perceptions of CAs and interaction outcomes involving rather specific aspects, coded as other (5%)—for example, audience effects (Candello et al., 2019) and constructs related to learning (3%) such as retention of learned content (van der Meij, 2013). Finally, a single study focuses on ethics and develops a moral agency scale (Banks, 2018). Table 7 summarizes the constructs and shows their distribution in the studies.

## 4.1.5 Complementary Findings

We found different observations based on the discipline (IS, CS), research approach (empirical or conceptual), research methods, and unit of analysis. Overall, we identified 262 studies on CAs, two thirds of which were published in CS journals and conference proceedings, and one third from the IS discipline. We noted an increase in interest in CAs since 2016 in both CS and IS, but particularly in the IS discipline (see Figure C1 in Appendix C). While about half of the studies in our CS sample were published before 2016 (48%), the vast majority of IS studies (85%) were published after 2016, indicating a recent increase in the interest in CAs as a research phenomenon in the IS discipline.

The studies in our sample comprise empirical (84%) as well as conceptual work (16%). Regarding the research methods used in the reviewed studies, we observed a focus on laboratory experiments (57%) and design science research (23%), predominantly with contextspecific architectural descriptions of the designed CA artifacts (e.g., Anabuki et al., 2000; Hsu et al., 2017; and Jain et al., 2018).

Table 7. Constructs Related to Perceptions and Outcomes Investigated in the Studies

<table><tr><td>Category*</td><td>Exemplary constructs</td><td>%</td></tr><tr><td>Attitude</td><td>Connectedness with the CA (Burgoon et al., 2016)Rapport (Krämer et al., 2018)Similarity (Vugt et al., 2010)</td><td>24.0%</td></tr><tr><td>Perception</td><td>Anthropomorphism (Seeger et al., 2018)Humanness (Gnewuch et al., 2018)Uncanniness (Tinwell &amp; Sloan, 2014)</td><td>22.9%</td></tr><tr><td>Performance</td><td>Response success rate (Liao et al., 2018)Conversational ability (Shah et al., 2016)Purchase amount (Son &amp; Wonseok, 2018)</td><td>20.2%</td></tr><tr><td>Acceptance</td><td>Usefulness (Qiu &amp; Benbasat, 2010)Performance expectancy (Laumer et al., 2019)Ease of use and intention to use (Hobert, 2019)</td><td>17.2%</td></tr><tr><td>Emotion</td><td>Empathy (Leite et al., 2013; McQuiggan &amp; Lester, 2007)Enjoyment (Bell, Sarkar, &amp; Wood, 2019)Compassion (Looije et al., 2010)</td><td>12.2%</td></tr><tr><td>Trust</td><td>Cognitive and emotional trust (Saffarizadeh et al., 2017)Perception of trust (Elson et al., 2018)Privacy Concern (Sohn, 2019)</td><td>12.2%</td></tr><tr><td>Relationship</td><td>Social distance (Kim &amp; Mutlu, 2014)Social roles (Seering et al., 2019)Relationship building (T. W. Bickmore &amp; Picard, 2005)</td><td>10.7%</td></tr><tr><td>Other</td><td>Audience effects (Candello et al., 2019)Shorthand language (Hill et al., 2015)Speech portions in dialogue (Bittner &amp; Shoury, 2019)</td><td>4.6%</td></tr><tr><td>Learning</td><td>Learning outcomes (Wang et al., 2008)Retention of learned content (van der Meij, 2013)Facilitation of learning (Zhang et al., 2019)</td><td>3.4%</td></tr><tr><td>Ethics</td><td>Perceived moral agency (Banks, 2018)</td><td>0.4%</td></tr><tr><td colspan="3">Note: * Multiple selections possible</td></tr></table>

Less common research methods in the reviewed studies include qualitative research, such as conceptual literature reviews (e.g., Li, 2015); interviews (4%)— for example, concerning use cases of CAs (Laumer et al., 2019); the use of secondary data (4%) such as user reviews for natural language applications (Nguyen & Sidorova, 2017); and surveys (3%). Field study research (2%) and experiments (2%) account for only a fraction of the used methods. Concerning the unit of analysis, most studies strongly focus on the individual level (73%) and consider the topic from a purely technological perspective (26%).

Regarding the theoretical grounding of the studies in our sample, about one third of the studies (30%) explicitly draw on different theories or paradigms to evaluate human interaction with CAs or to guide their design. In particular, researchers referred to the computers are social actors (CASA) paradigm formulated by Nass and Moon (2000). Based on a review of three sets of experimental studies, Nass and Moon demonstrated that individuals mindlessly apply social rules and expectations to computers exhibiting human characteristics or behavior—for example, communication via natural language. CA researchers draw on the CASA paradigm for different kinds of studies: for example to investigate the extent to which knowledge gained through human-to-human interaction can be applied to human-CA interaction, as in gender stereotyping (e.g., Cowell and Stanney, 2005; Pfeuffer et al., 2019; Qiu & Benbasat, 2010) or to explore how users perceive different anthropomorphic agent designs (e.g., Gong, 2008; Kim et al., 2013; Lee and Choi, 2017).

Additionally, several researchers, such as Seeger et al. (2018) and Tinwell and Sloan (2014), drew on the socalled “Uncanny Valley” (Mori 1970/2012) to understand adverse emotional reactions to anthropomorphic CAs and to propose how they might be overcome. The Uncanny Valley, in short, postulates that there is not a monotonically increasing relationship between the human-likeness of a technological artifact and human affinity toward it; rather, there is a point (i.e., the Uncanny Valley) where “a person’s response to a human-like robot would abruptly shift from empathy to revulsion as it approached, but failed to attain, a lifelike appearance” (Mori 1970/2012, p. 98). Seeger et al. (2018), for example, found empirical evidence for an adverse

emotional reaction to a CA that exhibits only partial human-like characteristics, and Seymour et al. (2017) suggested that interactivity, realized through an interactive 3D avatar that matches common human nonverbal cues, can contribute to overcoming the Uncanny Valley experience. In addition to the CASA paradigm and the Uncanny Valley theory, researchers in our sample also drew on the three-factor theory of anthropomorphism (Epley et al., 2007), which explains the psychological determinants of humans anthropomorphizing inanimate objects, or not. For example, Wagner and Schramm-Klein (2019) rely on this theory to discuss the anthropomorphism perception in interactions with digital assistants like Alexa. Furthermore, several researchers adapted theories and concepts originally from human-tohuman interaction for human-CA interaction. For example, Qiu and Benbasat (2010) and Vugt et al. (2010) drew on similarity-attraction theory (Byrne, 1971; Byrne et al., 1967) to investigate the impact of demographic similarity and facial similarity between a user and an agent. Similarly, Kim et al. (2013) and Kim and Mutlu (2014) drew on the concept of social distance (Bogardus, 1947), manifested in physical proximity, organizational status, and task structure, to understand user responses to humanoid robots. Additionally, Gnewuch et al. (2017) drew on Grice’s (1975) maxims for effective conversations to derive design principles for CAs in a customer service context. Further theories and concepts adapted to human-CA interaction include social presence (e.g., Schuetzler et al., 2018 or Sohn, 2019), rapport (e.g., Krämer et al., 2018), reciprocity (e.g,. Chattaraman et al., 2018), and self-determination theory (e.g., Lechler et al., 2019).

Finally, researchers drew on established models to investigate the acceptance of CAs, such as TAM (Davis, 1989) and UTAUT (Venkatesh et al., 2003). For example, Wang and Benbasat (2005) adapted TAM to study trust in recommendation agents, and Laumer et al. (2019) drew on UTAUT to understand CA acceptance in healthcare. Table 8 summarizes the theoretical grounding of the studies.

## 4.2 Research Streams

By means of cluster analysis, we identified four streams in IS and CS research. Specifically, these streams differ in the type of investigated CA regarding communication mode and embodiment; they also differ in terms of focal design dimensions, attention to the agent’s identity, and verbal and nonverbal communication. As shown in Table 9, we label these four streams “text-based CAs,” “virtual CAs,” “speech-based CAs,” and “physical CAs.”

Table 10 shows the characteristics’ distribution in the framework for each research stream. Note that multiple selections were used for coding human characteristics (e.g., studies that investigate the effects of users’ age on CA perception), design dimensions (e.g., studies that focus on CAs’ verbal and nonverbal communication), and on perceptions and outcomes (e.g., studies measuring CA performance and perception), which means that sum rows exceed 100%.

Table 8. Theoretical Grounding Used in CA Research

<table><tr><td>Theory</td><td>Seminal work</td><td>Exemplary studies</td></tr><tr><td>Computers are social actors (CASA)</td><td>Nass &amp; Moon (2000)</td><td>Cowell &amp; Stanney (2005), Gong (2008)</td></tr><tr><td>Uncanny valley</td><td>Mori (1970/2012)</td><td>Strait et al. (2015), Tinwell &amp; Sloan (2014)</td></tr><tr><td>Three-factor theory of anthropomorphism</td><td>Epley et al. (2007)</td><td>Seeger et al. (2018), Wagner &amp; Schramm-Klein (2019)</td></tr><tr><td>Similarity-attraction theory</td><td>Byrne (1971), Byrne et al. (1967)</td><td>Qiu &amp; Benbasat (2010), Vugt et al. (2010)</td></tr><tr><td>Social distance</td><td>Bogardus (1947)</td><td>Kim &amp; Mutlu (2014)</td></tr><tr><td>Grice&#x27;s maxims</td><td>Grice (1975)</td><td>Gnewuch et al. (2017)</td></tr><tr><td>Social presence</td><td>Gefen &amp; Straub (2003)</td><td>Schuetzler et al. (2018)</td></tr><tr><td>Rapport</td><td>Tickle-Degnen &amp; Rosenthal (1990)</td><td>Krämer et al. (2018)</td></tr><tr><td>Reciprocity</td><td>Moon (2000)</td><td>Chattaraman et al. (2018)</td></tr><tr><td>Self-determination theory</td><td>Ryan &amp; Deci (2000)</td><td>Quynh &amp; Sidorova (2018), Lechler et al. (2019)</td></tr><tr><td>Technology acceptance model</td><td>Davis (1989)</td><td>Wang &amp; Benbasat (2005)</td></tr><tr><td>Unified theory of acceptance and use of technology</td><td>Venkatesh et al. (2003)</td><td>Laumer et al. (2019)</td></tr></table>

Table 9. Research Streams for Conversational Agents

<table><tr><td>#</td><td>Research stream</td><td>Description</td></tr><tr><td>1</td><td>Text-based CAs</td><td>Research on CAs with interaction via written text and no embodiment or virtual static representation.</td></tr><tr><td>2</td><td>Virtual CAs</td><td>Research on CAs with interaction via written text and spoken natural language, and with embodiment through virtual interactive avatars.</td></tr><tr><td>3</td><td>Speech-based CAs</td><td>Research on CAs with interaction via spoken natural language and without any virtual or physical embodiment.</td></tr><tr><td>4</td><td>Physical CAs</td><td>Research on CAs with interaction via spoken natural language and with physical embodiment.</td></tr></table>

Table 10. Cross-Tab Analysis

<table><tr><td></td><td>Text-based CAs</td><td>Virtual CAs</td><td>Speech-based CAs</td><td>Physical CAs</td></tr><tr><td>Number of studies</td><td>112</td><td>69</td><td>58</td><td>23</td></tr><tr><td>Percentage</td><td>42.7%</td><td>26.3%</td><td>22.1%</td><td>8.8%</td></tr><tr><td colspan="5">Human</td></tr><tr><td>Gender</td><td>14.3%</td><td>10.1%</td><td>8.6%</td><td>13.0%</td></tr><tr><td>Age</td><td>8.0%</td><td>13.0%</td><td>12.1%</td><td>8.7%</td></tr><tr><td>CA experience</td><td>4.5%</td><td>2.9%</td><td>12.1%</td><td>8.7%</td></tr><tr><td>Personality</td><td>3.6%</td><td>8.7%</td><td>1.7%</td><td>4.3%</td></tr><tr><td>Cultural background</td><td>2.7%</td><td>1.4%</td><td>3.4%</td><td>0.0%</td></tr><tr><td>Task experience</td><td>1.8%</td><td>0.0%</td><td>1.7%</td><td>4.3%</td></tr><tr><td>Cognitive style</td><td>0.9%</td><td>2.9%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Individual education</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td colspan="5">Context</td></tr><tr><td>Generic</td><td>34.8%</td><td>66.7%</td><td>43.1%</td><td>34.8%</td></tr><tr><td>Customer interface</td><td>20.5%</td><td>2.9%</td><td>10.3%</td><td>17.4%</td></tr><tr><td>Education</td><td>15.2%</td><td>7.2%</td><td>6.9%</td><td>21.7%</td></tr><tr><td>Health</td><td>9.8%</td><td>10.1%</td><td>3.4%</td><td>13.0%</td></tr><tr><td>Private task support</td><td>6.3%</td><td>0.0%</td><td>17.2%</td><td>4.3%</td></tr><tr><td>Other</td><td>6.3%</td><td>4.3%</td><td>5.2%</td><td>0.0%</td></tr><tr><td>Professional task support</td><td>3.6%</td><td>4.3%</td><td>6.9%</td><td>4.3%</td></tr><tr><td>Team collaboration</td><td>1.8%</td><td>1.4%</td><td>6.9%</td><td>4.3%</td></tr><tr><td>Multiple</td><td>1.8%</td><td>2.9%</td><td>0.0%</td><td>0.0%</td></tr><tr><td colspan="5">Agent</td></tr><tr><td colspan="5">Communication mode</td></tr><tr><td>Text-based</td><td>98.2%</td><td>37.7%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Speech-based</td><td>0.0%</td><td>43.5%</td><td>84.5%</td><td>100.0%</td></tr><tr><td>Both</td><td>1.8%</td><td>18.8%</td><td>15.5%</td><td>0.0%</td></tr><tr><td colspan="5">Embodiment</td></tr><tr><td>None</td><td>55.4%</td><td>1.4%</td><td>100.0%</td><td>0.0%</td></tr><tr><td>Virtual interactive</td><td>4.5%</td><td>85.5%</td><td>0.0%</td><td>4.3%</td></tr><tr><td>Virtual static</td><td>36.6%</td><td>2.9%</td><td>0.0%</td><td>4.3%</td></tr><tr><td>Physical</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>91.3%</td></tr><tr><td>Multiple</td><td>3.6%</td><td>10.1%</td><td>0.0%</td><td>0.0%</td></tr><tr><td colspan="5">Design dimensions</td></tr><tr><td>Verbal communication</td><td>55.4%</td><td>33.3%</td><td>62.1%</td><td>34.8%</td></tr><tr><td>(Human) identity</td><td>30.4%</td><td>59.4%</td><td>6.9%</td><td>17.4%</td></tr><tr><td>Nonverbal communication</td><td>5.4%</td><td>65.2%</td><td>8.6%</td><td>34.8%</td></tr><tr><td colspan="5">Perceptions and outcomes</td></tr><tr><td>Attitude</td><td>18.8%</td><td>40.6%</td><td>19.0%</td><td>13.0%</td></tr><tr><td>Perception</td><td>22.3%</td><td>33.3%</td><td>12.1%</td><td>21.7%</td></tr><tr><td>Performance</td><td>22.3%</td><td>10.1%</td><td>25.9%</td><td>26.1%</td></tr><tr><td>Acceptance</td><td>17.0%</td><td>13.0%</td><td>22.4%</td><td>17.4%</td></tr><tr><td>Emotion</td><td>7.1%</td><td>23.2%</td><td>8.6%</td><td>13.0%</td></tr><tr><td>Trust</td><td>13.4%</td><td>13.0%</td><td>6.9%</td><td>17.4%</td></tr><tr><td>Relationship</td><td>6.3%</td><td>14.5%</td><td>8.6%</td><td>26.1%</td></tr><tr><td>Other</td><td>4.5%</td><td>1.4%</td><td>8.6%</td><td>4.3%</td></tr><tr><td>Learning</td><td>3.6%</td><td>1.4%</td><td>5.2%</td><td>4.3%</td></tr><tr><td>Ethics</td><td>0.0%</td><td>1.4%</td><td>0.0%</td><td>0.0%</td></tr></table>

## 4.2.1 Research Stream 1: Text-Based CAs

Studies in the first research stream focus on CAs with which users interact via written text that either has no embodiment or only a virtual static representation (e.g., with an image). Thus, we refer to this stream as “textbased $\mathrm { C A s } ,  { \mathfrak { s } }$ which has attracted the research community’s interest as a type of CA, particularly since 2016, when more text-based CA studies were published than virtual CA, speech-based CA, or physical CA studies (see Figure C2 in Appendix C).

In particular, research in this stream investigates questions related to verbal communication (55%), focusing on topics such as how to repair conversation breakdown (Ashktorab et al., 2019; Corti & Gillespie, 2016), how to design effective agent communication and its user impact (Adler et al., 2016; Derrick & Ligon, 2014; Hu et al., 2018; van der Meij, 2013), and how to gauge the influence of message interactivity on users’ perception of an agent (Adam & Klumpe, 2019; Go & Sundar, 2019).

About one third of the studies in this stream explore aspects related to the (human) identity of an agent (30%)—for example, how the agent’s gender influences the user (Pfeuffer et al., 2019; Qiu & Benbasat, 2010), and how the degree of an agent’s human-likeness representation (e.g., a comic image of a robot versus a photo of an actual human person) impacts user perception (Gong, 2008). Further studies do not focus on specific design dimensions but address overarching topics such as chatbot use cases (Laumer et al., 2019; Meyer von Wolff et al., 2019) and affordances (Stoeckli et al., 2018).

Regarding context, many text-based CA studies do not specify a particular application area or focus on the customer interface of organizations (35%)—for example, online customer services (e.g., Gnewuch et al., 2018; Hu et al., 2018; Xu et al., 2017) or marketing and sales (e.g., Al-Natour et al., 2009; Vaccaro et al., 2018; Van den Broeck et al., 2019). Other frequently studied contexts include education (15%) and health (10%). In the context of education, text-based agents have been investigated for learning languages (Fryer et al., 2017), collaborative problem solving (Hayashi, 2013; Herborn et al., 2018), and programming education (Hobert, 2019). In the area of health, researchers have focused on, for example, chatbots for therapy (Bell et al., 2019; Constantin et al., 2019), raising individual health awareness (Meier et al., 2019), or supporting people with allergies (Hsu et al., 2017). Research on text-based CAs has addressed constructs related to perception (e.g., humanness), attitude (e.g., attractiveness), performance (e.g., responsiveness), and acceptance (e.g., perceived usefulness). Regarding text-based agents, prior studies have mainly investigated how design variations concerning the agent’s identity (e.g., Araujo, 2018; Go & Sundar, 2019) or verbal communication (e.g., Hu et al., 2018; Schuetzler et al., 2014) influence how the user perceives the agent’s anthropomorphism or humanness.

Complementary to the question of how to design human-like text-based agents, researchers have discussed whether anthropomorphic design might trigger perceptions of uncanniness in the interaction (e.g., Gnewuch et al., 2018; Wünderlich & Paluch, 2017). Finally, prior studies have investigated the outcomes of anthropomorphic perception in chatbots regarding, for example, service encounter satisfaction (Gnewuch et al., 2018), brand perception (Araujo, 2018), and learning results (Jin, 2010).

## 4.2.2 Research Stream 2: Virtual CAs

Research in the second stream, termed “virtual CAs,” comprises work on agents represented by virtual animated avatars with which users interact via written and spoken natural language. The research interest in both the IS and CS disciplines regarding virtual agents as a type of CA has been steady, particularly in comparison to studies on text-based agents and speechbased CAs (see Figure C2 in Appendix C). In contrast to research focused on verbal communication in the first stream, studies on virtual CAs investigate, in particular, nonverbal communication (65%) and the (human) identity of an agent (59%). For example, Krämer et al. (2013) explored how an agent’s smile impacts user perception and behavior, finding that humans reciprocate the agent’s smile. Similarly, several studies in this stream have explored the impact of the agent’s gaze on the user, e.g., in terms of catching the user’s eye (Vertegaal et al., 2000, 2001), as well as the effects of facial similarity between the agent and the user (Vugt et al., 2010) and the agent’s digital gesturing behavior (Biancardi et al., 2017). Finally, Seymour et al. (2018) presented emerging natural face technology for creating a realistic visual presence of an agent and proposed a research agenda that includes fundamental philosophical questions arising from agent representations becoming increasingly realistic.

Virtual agents have mostly been studied without a specific context being described (67%). However, when a specific context was given, studies have mostly focused on applications in health (10%) or education (7%). Regarding health, prior research has explored virtual CAs as a means of changing stigmatizing attitudes toward mental health (Sebastian & Richards, 2017) as well as the potential advantages virtual agents could have over clinical psychologists in mental health interviews (Yokotani et al., 2018). In the educational context, Carlotto and Jaques (2016) studied animated pedagogical agents and suggested that an agent’s movement and gestures contribute less to learning outcomes than interaction via speech. Similarly, Gulz and Haake (2006) explored how the design of agent animations impact student learning motivations.

Finally, previous studies on virtual CAs have mainly concerned users’ attitudes toward them as well as user perceptions and emotions, which are often related to the agent’s nonverbal communication behavior. For example, Burgoon et al. (2016) studied how a match between user expectations and the agent’s behavior influenced individuals’ attitudes toward the agent, finding that positive deviations from user expectations have a particularly substantial positive effect on perceived connectedness, receptivity, and dependability. Regarding emotions, other studies have investigated interactive designs expressing politeness (Niewiadomski & Pelachaud, 2010) and displaying empathy (McQuiggan & Lester, 2007; Yang et al., 2017), which are direct responses to users’ inputs. More recent studies have further explored how an agent’s interactive representation and nonverbal communication behavior impact the agent’s persuasiveness (Harjunen et al., 2018; Hyde et al., 2015; Looije et al., 2010; Rosenthal-von der Pütten et al., 2018) in decision-making tasks, for example.

## 4.2.3 Research Stream 3: Speech-Based CAs

The third research stream, termed “speech-based CAs,” includes primarily speech-based CAs (85%) without any physical or virtual embodiment. Similar to research on text-based CAs, the number of publications that focus on speech-based agents has substantially increased since 2016 (see Figure C2 in Appendix C). Research in this stream concentrates on verbal communication with an agent (62%) or topics not directly related to technological aspects, such as use cases (Baier et al., 2018), team settings with agents for collaborative work (Bittner et al., 2019), and the psychological impact of interacting with CAs in a commanding voice (Burton & Gaskin, 2019). Research in this stream often draws on widely distributed assistants, such as Amazon’s Alexa (Son & Wonseok, 2018; Winkler et al., 2019; Winkler & Roos, 2019), Apple’s Siri (Burton & Gaskin, 2019), and Google Assistant (Cho, 2019). Concerning verbal communication, research on speech-based CAs has addressed conversation design for useful task guidance (Vtyurina & Fourney, 2018), for fostering a positive user experience (Burmester et al., 2019), and for combining social and functional ways of communicating (Clark et al., 2019).

Similar to research on virtual CAs, studies in this stream often do not specify a particular context (43%). However, in contrast to the two previously mentioned streams, several studies on speech-based agents focus on individual task support in a private context—for example, using Alexa and Google as smart home components (Kowalski et al., 2019; Porcheron et al., 2018; Purington et al., 2017). Further studied contexts include digital assistants at the customer interface (10%), for advisory services (Dolata et al., 2019) or advertising (Kim et al., 2018), in education (7%), for learning languages (Morton et al., 2012), and for team collaboration (Winkler et al., 2019a).

The aspects that this research stream investigates relate particularly to performance (26%), acceptance (22%), and attitude (19%). Concerning performance, research on speech-based CAs has, for example, explored the number of tasks completed in teams (Winkler et al., 2019a; Winkler et al., 2019b), conversation turns, and time required to retrieve information from the assistant (Le Bigot et al., 2006), and the agents’ social dialogue capabilities (Ward & Tsukahara, 2003). Regarding acceptance, researchers have studied, for example, the influence of an agent’s answers to user questions on perceived usefulness (Jung et al., 2019) and the impact of the agent’s personification and social interaction capabilities on user satisfaction (Purington et al., 2017). Finally, in terms of attitude, studies on speechbased agents have investigated aspects such as gender stereotypes arising from an agent’s female voice (Hwang et al., 2019) and the impact of an agent’s answers on perceived politeness and pleasantness (Jucks et al., 2018).

## 4.2.4 Research Stream 4: Physical CAs

The fourth research stream comprises research on CAs with a physical embodiment (91%) that interact via spoken natural language. We refer to this stream as “physical CAs.” The research interest on CAs with a physical embodiment has been comparatively steady, similar to the research stream on virtual agents (see Figure C2 in Appendix C). Studies in this stream emphasize verbal (35%) and nonverbal communication (35%). Concerning verbal communication, researchers have, for example, investigated how speech style, including calling users by their names, influences the perceived social distance between the user and the physically embodied agent (Kim et al., 2013) as well as how different sales strategies impacted the number of goods conversational robots sold in a department store (Watanabe et al., 2015). Research focusing on nonverbal communication has focused on designing different types of behaviors, such as nodding and maintaining eye contact, and evaluating the impact of such behaviors on users and their perceptions of the physical CA (Lee et al., 2004; Saerbeck et al., 2010; Sakamoto et al., 2005; Szafir & Mutlu, 2012; Yamada et al., 2013). Studies on physical CAs rarely specify a particular context (35%), but studies that do investigate CAs in educational contexts (22%), at the customer interface (17%), or in health contexts (13%). In the context of education, studies have explored physical CAs as learning partners that support social and cognitive aspects in the learning process (Huang, 2012; Saerbeck et al., 2010; Zhang et al., 2019). At the customer interface, physical CAs have been investigated as a means of supporting product sales (Bertacchini et al., 2017; Watanabe et al., 2015) or innovatively providing customer service (Stock & Merkle, 2018b). Finally, physical CAs have been studied in health contexts as caregivers (Kim et al., 2013) or as a way to promote regular physical exercise (Kanaoka & Mutlu, 2015).

Regarding the perceptions and outcomes of interactions with physical CAs, prior studies have focused on the relationship between the user and agent (26%), on the CA’s performance (26%), and on the user’s perception of the physical agent (21%). Concerning the relationship between the physically embodied agent and the user, Sangseok and Lionel (2019), for example, have investigated how team members identify with a physically embodied CA while completing a collaborative task and how this impacts subgroup formation. A further example is Lee et al.’s (2012) work, which discusses how users assign social roles to physical CAs and how the user’s relationship to an agent with a physical embodiment influences the user’s behavior toward other users (e.g., protecting the agent or jealousy). Concerning performance, scholars have researched, for example, the number of products sold by a sales agent (Watanabe et al., 2015) as well as the learning results associated with physical CAs (Szafir & Mutlu, 2012). Regarding perceptions of physical agents, researchers have studied aspects such as social presence (Pereira et al., 2014), humanness (Kim et al., 2013), and social behavior (Xu et al., 2013).

## 5 Discussion

To date, researchers interested in CAs have not been able to consult an overarching framework, classification, or suitable organizing device to compare and analyze existing CA research. Because of the variety and number of extant studies and the lack of an organizing structure, it has been difficult for researchers to identify relevant future research topics or areas. Our framework, adapted from established research by Zhang and Li (2005), offers support to researchers by classifying and organizing existing research and offering potential avenues for future CA research.

## 5.1 An Agenda for Conversational Agent Research in IS

Based on our analysis of the identified CA studies, we propose six avenues for future research that address research gaps that have not yet been investigated and need to be studied from an IS perspective. For each avenue, we motivate and formulate specific directions for future research activities to address the identified gaps in the body of IS knowledge and advance the understanding of the interaction between humans and CAs (summarized in Table 11).

## 5.2 User Characteristics and Adaptive CA Designs

We found that only a quarter of the reviewed studies investigated how individual human characteristics influence the perception of and interaction with CAs; among these, however, several empirical studies found significant effects. For example, Schroeder and Schroeder (2018) observed that younger and male users are more likely to trust CAs. Rosenthal-von der Pütten et al. (2018) found that older users are more easily persuaded by a CA that shows dominance than by one with submissive behavior. Vugt et al. (2010) discovered that female users are more likely to use a CA with facial similarity, while male users are more likely to prefer a CA with facial dissimilarity. In addition to age and gender, studies indicate that characteristics such as experience with CAs (e.g., Ashktorab et al., 2019; Otoo & Salam, 2018), personality traits (e.g., Krämer et al., 2018; Seeger et al., 2020), and cognitive style (e.g., Hubal et al., 2008) influence how users perceive and interact with CAs. These studies mostly considered human characteristics as complementary to the key constructs they investigate. However, for characteristics like age and gender, experience with CAs, the task at hand, and the user’s personality appear to significantly influence how humans perceive and interact with CAs in different contexts (i.e., the usage scenario of the CA, e.g., health, education, and private task support; see Table A1 in Appendix A for further contexts).

Based on these initial findings, we suggest that there is a promising research opportunity to explicitly investigate the impact of individual user characteristics (e.g., gender, age, personality, cultural background, etc.) on the interaction between humans and CAs. This applies to different contexts and to aspects of the agent’s perception, as well as to the interaction’s outcomes. For example, future research could evaluate how cultural differences between users influence the perception of features regarding the agent’s identity (e.g., name, social role), verbal communication (e.g., formal or informal language, expression of emotions), and nonverbal communication (e.g., use of gestures and facial expressions, emoticons). Similar to the various culturally modifiable interface components of graphical user interfaces (Reinecke & Bernstein, 2013), we argue that a variety of CA features will likely influence how users perceive agents, depending on the user’s cultural background. In short, a sound understanding of the impact of individual user characteristics, considering the context as well as the agent’s design features, can enable a better understanding of the differences and commonalities regarding CA perceptions and interaction outcomes. In summary, we propose the following research direction (D):

D1.1: Investigate the impact of user characteristics on the interaction between humans and CAs regarding human perception and interaction outcomes across different contexts.

Table 11. Agenda for Conversational Agent Research in IS

<table><tr><td>Research avenue</td><td>Directions for future CA studies</td></tr><tr><td>Avenue 1:User characteristics and adaptive CA designs</td><td>D1.1: Investigate the impact of user characteristics in the interaction between humans and CAs regarding human perception and interaction outcomes across different contexts.D1.2: Investigate how CAs can be designed to adapt themselves to individual users and their characteristics during an interaction.D1.3: Study the potential that CA configuration or CA co-creation has for the user, and the resulting impact on user perceptions and interaction outcomes.</td></tr><tr><td>Avenue 2:CAs on group and organizational levels of analysis</td><td>D2.1: Investigate which parts of collaborative group work can be fulfilled by CAs and the resulting impact on team behavior and performance.D2.2: Examine how CAs should be designed to efficiently support human team collaboration and how these designs influence team members&#x27; perception of and interaction with CAs.D2.3: Analyze which types of (organizational) tasks and processes are suitable for innovation and automation with CAs.D2.4: Investigate the positive and negative impact and the potential mitigation strategies when automating human work using (anthropomorphic) CAs.</td></tr><tr><td>Avenue 3:CAs with virtual interactive and physical embodiments</td><td>D3.1: Explore the impact of rich virtual interactive or physically embodied CAs on user perception combined with currently available conversational capabilities.D3.2: Investigate designs of virtual interactive and physical CA embodiment to increase agent acceptance, adoption, and performance across different contexts.</td></tr><tr><td>Avenue 4:Transferability of knowledge gained in CA studies</td><td>D4.1: Partially replicate experimental CA studies to investigate whether existing prescriptive and descriptive knowledge can be transferred across between different CA instances (i.e., combinations of human, agent, and context) and adapted accordingly.</td></tr><tr><td>Avenue 5:Ethical implications of designing and interacting with CAs</td><td>D5.1: Explore when, where, and how applying persuasive CAs is ethically justifiable.D5.2: Develop CA&#x27;s design elements to address the ethical dimensions of the user interaction, and investigate how users perceive these design elements.D5.3: Investigate the unintended side-effects of CA design and study how to prevent negative side-effects.</td></tr><tr><td>Avenue 6:Longitudinal CA research in a field study setting</td><td>D6.1: Conduct field studies to verify, extend, or refute existing knowledge gained from experimental research in controlled settings.D6.2: Investigate the interplay between the limited conversational capabilities of CAs and the combination of multiple (anthropomorphic) design features of CAs.D6.3: Study how the relationship between users and CAs takes shape during the initial use of the CA, and how it develops in multiple interactions over a longer period of time.</td></tr></table>

With our improved understanding of user characteristics and their influence on the interaction between CAs and their users, we propose investigating how CAs can be designed to adapt themselves to individual users during an interaction. In practice, CAs are typically implemented using a “one size fits all” approach in which all users receive the same agent and set of responses, regardless of characteristics such as age, experience with such agents, and personality (Følstad & Brandtzæg, 2017). Therefore, investigating adaptive designs securely founded on empirical data and theory (Kocaballi et al., 2019) represents a lucrative research opportunity. We suggest that CAs with efficient adaptive designs for heterogeneous user groups are likely to increase agents’ acceptance, adoption, and performance, in line with studies on other types of IT artifacts, such as recommendation agents with graphical user interfaces (Al-Natour, Benbasat, & Cenfetelli, 2006). Researchers might be able to draw on established theories and constructs from human-to-human interaction, such as communication accommodation theory (Giles, Coupland, & Coupland, 2010), similarity attraction theory (Byrne, 1971; Byrne et al., 1967), matching and mirroring (Burgoon, Stern, & Dillmann, 1995), and mimicry (Kozlowski & Ilgen, 2006), to inform adaptive CA designs. For example, researchers could explore how CAs can efficiently tailor their verbal communication (e.g., selection of words or syntax) to different user groups in the same way that humans adjust their language style in interactions (Pickering & Garrod, 2004). Because moving away from “one size fits all” approaches is likely to substantially increase the complexity of an implementation, we further suggest evaluating and comparing different adaptive CA designs in order to identify the most efficient features, drawing on the three design dimensions of agents, namely (human-like) identity and verbal- and nonverbal communication.

## D1.2: Investigate how CAs should be designed in order to adapt themselves to individual users and their characteristics during an interaction.

As an alternative approach to user-adaptive designs, researchers should investigate the potential of configurable agents that would allow users to co-create CAs that fit their preferences. Studies on several types of technological artifacts, such as mobile devices (Carter et al., 2013) and avatars (Belk, 2013), have shown that humans can identify with certain inanimate objects, thereby promoting emotional attachment. As explained by the psychological process of self-extension (Belk, 1988), seeing objects as a part of one’s individual identity fosters this identification and the resulting emotional attachment. Building or configuring one’s own technology has been shown to trigger the process of selfextension for different types of artifacts, such as robots (Groom et al., 2008; Robert & Sangseok, 2018) and avatars (Ducheneaut et al., 2009). Fostering identification with CAs through configurable designs or co-creation is likely to have a positive impact on, for example, enjoyment of the interaction (Li et al., 2006) and team performance in collaborative settings (Robert & Sangseok, 2018), as demonstrated by studies on other types of technological artifacts. Thus, we propose that researchers should investigate the possibilities of CA configuration or co-creation, including shaping the agent’s identity (name, gender, appearance). Researchers should also study how this would impact users’ agent perceptions and interaction outcomes. In considering such designs, we suggest that researchers particularly investigate users’ social responses to agents and how this impacts the relationship between users and (human-like) CAs.

D1.3: Study the potential of CA configuration or CA cocreation for the user and the resulting impact this has on user perceptions and interaction outcomes.

## 5.3 CAs on Group and Organizational Levels of Analysis

Considering the unit of analysis, the majority of the studies in our sample focused on individual interaction with CAs (73%) or on technological descriptions of CA designs (26%). Notable exceptions at group and (inter)organizational levels of analysis include Bittner et al. (2019), who developed a taxonomy of design option combinations for CAs in collaborative work, and Cardona et al. (2019), who studied adoption and diffusion of conversational technology in the German insurance sector. Apart from these studies, the large majority of CA research focuses on the individual level, i.e., the interaction between a single user and a single CA.

In line with researchers in the area of computersupported collaborative work, such as Seeber et al., (2019a) and Seeber et al. (2019b), we suggest investigating CAs in group settings. We argue that, driven by advances in natural language processing and machine learning, CAs with significantly improved capabilities have emerged (McTear, 2017). Also, with their human-like characteristics, CAs may be able to alter the role of IT from one of providing tools that enhance team performance to eventually becoming artificial teammates (Malone, 2018). Such technological progress has given rise to numerous questions related to the design of CAs in team settings and to group interaction with these agents. For example, which roles in a team can an anthropomorphic CA assume, i.e., in what situations is the CA able to fulfill a gap where a human team member is missing? What are the advantages and limitations of a CA in this role? While a large body of collaboration research is available on team compositions and the roles of team members (e.g., Belbin, 2010), we lack an understanding about which of the roles CAs can fulfill and what the implications are when technology assumes such roles. While we expect research on CA roles in team settings to initially focus on operational tasks, such as managing the task, gathering information, or scheduling meetings, we anticipate that even more capable CAs will emerge, which would be able to assume roles typically associated with human team members. For example, CAs equipped with present-day sensing capabilities are already able to recognize individuals’ sentiments (Bertacchini et al., 2017; Feine et al., 2019) and may be able to, for example take measures where appropriate, such as proposing a break to improve the general mood within the team. Thus, we suggest investigating this and similar team roles by drawing on the conversational technology available in practice to better understand which parts of collaborative work CAs can fulfill and how an artificial teammate will impact team behavior and performance.

## D2.1: Investigate which parts of collaborative group work can be fulfilled by CAs and the resulting impact on team behavior and performance.

Further, future studies should investigate the impact that different agent designs have, such as text-based or speech-based communication in Research Streams 1 and 3, or embodiment in collaboration settings, as in Research Streams 2 and 4. For example, do team members perceive the same agent differently depending on the communication mode, i.e., depending on whether member-CA interaction takes place via spoken or written natural language? And what is the impact of a higher degree of agent anthropomorphism on the acceptance, adoption, and use of a CA within a team? According to extant research on the impact that CA anthropomorphism has on the individual perception of such agents (e.g., Araujo, 2018; Go & Sundar, 2019; Rosenthal-von der Pütten & Krämer, 2014) and on the understanding of computers as social actors (Nass & Moon, 2000), we expect the agent’s increased human-likeness to strengthen social responses to an agent within a team. This can be both positive (e.g., regarding CA acceptance in the team or collective enjoyment of the interaction) and negative (e.g., regarding shared feelings of frustration when the agent is not able to fulfill high expectations fostered by a human-like design). While some of these social responses might be similar to individual interaction with and perception of CAs, we do not understand how group settings (i.e., multiple humans interacting with one or more CAs at the same time) influence such responses. Therefore, we propose studying how CAs should be designed to be efficient in team collaboration and how such designs influence the way that team members perceive and interact with (anthropomorphic) CAs.

## D2.2: Examine how CAs should be designed to efficiently support human team collaboration and how these designs influence team members’ perception of and interaction with CAs.

In addition to generating a better understanding of the potential and limitations of CAs in team collaboration, we propose studying such agents at the organizational level. Currently, the majority of CA studies in organizations focuses on the customer interface, investigating contexts like customer service (e.g., Hu et al. (2018), Stock & Merkle (2018b), Wünderlich & Paluch, 2017) or marketing and sales (e.g., Hanus & Fox, 2015; Kim et al., 2018; Vaccaro et al., 2018). Further, we found single studies in other, quite specific contexts, such as for onboarding new employees (Liao et al., 2018) or for assisting workshop moderation (Strohmann et al., 2018). However, we still lack an understanding of the key characteristics that determine whether introducing a CA makes sense in a specific context. At present, studies in new organizational contexts emerge in a bottom-up approach, possibly driven by practical interests. Thus, we posit research potential for identifying the types of tasks for which CAs can be useful in a more abstract, contextindependent way. For example, these task types can be characterized by their rather structured nature and according to occurrence frequency. However, we do not know whether such tasks necessarily comprise an interaction that usually takes place between two humans, i.e., a task where an anthropomorphic agent could at least partially substitute for human contact. Nor do we know whether such tasks typically involve interaction with complex software, where the CA is intended to increase ease of use. A sound understanding of task types suitable for automation and innovation by means of CAs could assist us in moving from the practical, opportunity-driven identification of application contexts to a top-down approach in which such contexts could be determined by systematically reviewing tasks and processes within an organization.

## D2.3: Analyze which types of (organizational) tasks and processes are suitable for innovation and automation with CAs.

Additionally, future research could investigate the consequences that the introduction of CAs has on the human workforce. Davenport and Kirby (2016) discuss how cognitive technology (or AI technology in general) can support humans in performing various tasks. Similarly, Brynjolfsson and McAfee (2016) elaborate on how IT is facilitating automation, thus leading to task performance shifting from the human to the computer and thereby announcing the second machine age. They argue that, with these advances, more and more tasks traditionally performed by humans are being automated, replacing workers with intelligent IT, which has positive (e.g., fewer simple, repetitive tasks performed by people) as well as negative consequences (e.g., employees fearing job losses). Building on this, researchers should explore how human workers perceive the CA take-over of tasks they previously performed. For example, in a customer service context, more and more first-level support is being performed by CAs (Huang & Rust, 2018) and human operators that answer basic service requests are no longer required. While this can be interpreted positively (e.g., no need to answer the same simple question multiple times a day) there are also potentially negative consequences (e.g., living in fear of losing one’s job to a machine). There are more contexts in organizations where CAs can support or substitute human workforce members, such as in sales and invoice processing. While automating human tasks is an ongoing effort, in the context of CA, substituting and automating previously human work has a new component. CAs, especially when designed to be human-like, are perceived as social actors (Nass & Moon, 2000; Reeves & Nass, 1996). Therefore, CAs taking over human tasks may involve not only automation with some form of intelligent IT but could also entail another social actor taking over a human’s task. Further research should investigate the impact that this ongoing change has on human work performance and evaluate how to better utilize positive effects while mitigating potential negative effects. It is also important to investigate whether the specific nature of the CA, i.e., whether it is perceived as a social actor, has an impact on automation.

D2.4: Investigate the positive and negative impacts as well as potential mitigation strategies when automating human work using (anthropomorphic) CAs.

## 5.4 CAs with Virtual Interactive and Physical Embodiments

We disclosed above that the recently increased research interest in CAs, in particular, comprises the research streams of text-based CAs (Research Stream 1) and speech-based CAs without embodiment (Research Stream 3). In contrast, the streams of virtual CAs (Research Stream 2) and physical CAs (Research Stream 4) remain on a steady, comparatively low level of studies per year (see Figure C2 in Appendix C). We explain this observation by referring to the high availability of text-based CAs and speech-based agents for (experimental) research and the current interest in such types of CAs in practice. Nevertheless, we believe that there are substantial research opportunities to study physical and virtual CAs.

Recent studies on virtual agents highlight the strong social reactions humans show in response to virtual CAs. For example, Harjunen et al. (2018) found that participants in an experiment were comparatively more likely to accept unfair offers by a CA that smiled and touched them through a haptic glove. Krämer et al. (2018) discovered that socially responsive nonverbal agent behavior in terms of nodding, smiling, and posture shifts can reduce the participant’s need to engage in social activities after the interaction. Further, Seymour et al. (2018) highlighted the versatile potential and the implications of natural face technology, which creates a realistic visual presence, and called for “blue ocean” research in this area. Current interactive CAs, such as Amelia by IPsoft (2020), underline this potential of virtual CAs in practical application, particularly in organizational contexts like customer service and IT service desk automation. Similar to emerging research on virtual agents, recent studies on physically embodied CAs, such as Desideri (2018), Stock & Merkle (2018b), and Stock et al. (2019), demonstrate CAs’ potential with a physical embodiment. For example, Stock & Merkle (2018b) investigated customer responses to behavioral cues during customer service encounters and found positive emotional reactions to the humanoid robot’s behavior. Desideri et al. (2018) investigated whether humanoid robots can offer mental health assessment benefits that improve on clinical psychologists’ achievements.

In short, new forms of realistic virtual interactive or physically embodied CAs are likely to have a substantial impact on user perception, complementing the verbal communication that IS research on CAs is currently addressing. We expect these additional and rich design features associated with such forms of embodiment to immediately attract users’ attention in the interaction and to strengthen social responses, as indicated by the aforementioned early studies. Thus, we propose systematically studying the impact of virtual interactive and physical embodiment in combination with the advanced natural language interaction offered by present-day CAs.

D.3.1: Explore the impact of rich virtual interactive or physically embodied CAs on user perception combined with currently available conversational capabilities.

In addition to better understanding the impact of these CA embodiment forms on user perception, we propose research on how such embodiment should be designed for different contexts to increase CA acceptance, adoption, and performance. For example, we could ask what a pleasant embodiment of a virtual interactive customer service CA should look like and how a CA’s physical embodiment should be designed to efficiently support product sales in stores. Currently available forms of CA embodiment, such as IPsoft’s Amelia for virtual interactive CAs and SoftBank’s humanoid robot Pepper, offer unprecedented design features, such as facial movement (e.g., eye blinking or smiling) and gestures (e.g., waving or moving the head toward a speaking person), in combination with advanced conversational capabilities. However, we lack a solid understanding of how these features should be designed and combined with one another in order to influence user perceptions to achieve specific goals (e.g., increase trust in the CA or foster the perception of anthropomorphism) across different contexts. Thus, we propose:

D.3.2: Investigate virtual interactive and physical CA embodiment designs to increase agent acceptance, adoption, and performance across different contexts.

## 5.5 Transferability of Knowledge Gained in CA Studies

Besides new insight into the state of the art in CA research from a given ex ante perspective (i.e., we preselected dimensions for coding and all analyses depended on this selection), different ex post observations emerged from our analysis. We found several studies that transferred and combined knowledge from different contexts (e.g., Seeger et al., 2018; Gnewuch et al., 2017; Tavanapour et al., 2019) and different types of CAs (e.g., Araujo, 2018; Jeong et al., 2019; Wagner & Schramm-Klein, 2019). Justifying design decisions (Gregor et al., 2020) or proposing hypotheses using existing prescriptive and descriptive knowledge represent appropriate scientific methodology (Bhattacherjee, 2012). However, during our analysis, the question emerged as to when and under which circumstances prescriptive and descriptive knowledge can be adapted from one instance to another—for example, when a specific type of user interacts with a specific type of agent in a specific context (see Figure 2).

In our sample of 262 studies, 148 articles investigated the interaction between humans and a CA (or specific design variants of a CA) for a given context and measured specific outcomes (the type of users, CA design, and context—referred to as “instance” in the following). We found studies that successfully adapted knowledge from one instance to their research context in another instance. For example, Adam and Klumpe (2019) investigated a text-based CA in the context of human resources, which facilitates onboarding processes and successfully draws on Lee and Choi's (2017) findings that reciprocal behavior and selfdisclosure by a speech-based agent have a positive effect on user satisfaction in the context of marketing and sales. Their study provides arguments for the transferability of knowledge from one instance to another in the context of CAs.

However, there is also research on CAs that has investigated similar aspects but found mixed results, making it difficult to adapt knowledge from one instance to another instance. Nass and Moon (2000) found that users perceived a CA’s female voice as less friendly and less competent than the corresponding male voice, thus supporting their assumption that “individuals would mindlessly gender stereotype computers” (Nass & Moon, 2000, p. 85). In contrast, Forlizzi et al. (2007) found that female-looking CA avatars were preferred to male-looking avatars. Moreover, female-looking avatars received higher satisfaction ratings than male avatars. Although the two studies do not assess exactly the same outcomes, they illustrate the problem regarding the transferability of existing prescriptive and descriptive CA knowledge. While Nass and Moon’s (2000) study supports selecting a male-gendered CA to receive positive outcomes, Forlizzi et al. (2007) provide arguments for selecting a female-gendered CA to create similar positive outcomes.

Against this background, the practice of transferring implications from observations between instances (e.g., from a physical CA with embodiment to an agent with a virtual embodiment) is questionable and potentially risky. Currently, researchers should only cautiously adopt knowledge from a single instance because there is insufficient literature on the transferability and adaptability of CA knowledge. Considering existing research, we were unable to identify any study empirically investigating how or how well knowledge can be transferred between different CA instances and what the prerequisites for a successful transfer might be. Similarly, we found no research that addresses this aspect from a conceptual or theoretical point of view. Therefore, it is still unknown how well, for example, observations regarding the effect of designing the CA as gendered (e.g., a CA having a male or female name or an avatar representing a specific gender) can be transferred between a text-based chatbot (Research Stream 1) and a physical CA (Research Stream 4). The two CA types offer a different set of potential design elements to be used in communicating and portraying the CA’s gender or, more generally, the agent’s degree of humanness. Thus, one can expect differences in the users’ perception of the resulting CAs. The same is true for other CA design features (e.g., nonverbal communication of positive emotions through emoticons in a text-based agent, compared to a smiling interactive agent) and for different contexts (e.g., from a CA in education to a CA in customer services). In essence, the question remains regarding the circumstances under which existing prescriptive and descriptive knowledge can be transferred and adapted across CA instances. Our research framework can be helpful in systematically analyzing the commonalities and differences among user groups (i.e., human users and their characteristics), contexts (e.g., customer service or education), CA types (i.e., agent), and resulting perceptions and outcomes across different instances. We assume that some effects are observable across several instances, while others might be specific to a particular group of users, application context, or CA type. In short, we propose that experimental CA studies should be partially replicated by deliberately varying one dimension from the original study (human, context, agent) and then investigating the effect that this has on user perception of the agent and the outcome(s) of the interaction.

D4.1: Partially replicate experimental CA studies to investigate whether existing prescriptive and descriptive knowledge can be transferred across different CA instances (i.e., combinations of human, agent, and context) and adapt accordingly.

Eventually, by conducting studies where one or two dimensions are deliberately changed from the original work, our knowledge of CA design and interaction will mature from a plethora of seemingly related observations into a systematic framework, consisting of generalized statements on overarching phenomena, such as CA gender stereotyping.

## 5.6 Ethical Implications of Designing and Interacting with CAs

We found only a single study investigating ethical aspects related to human interaction with CAs. Banks (2018) proposes and validates a scale to measure the agent’s behavior regarding morality and dependency on its implementation. Considering this substantial lack of research on ethical implications of the design of and interaction with CAs, we formulate three directions for future research in the following section.

Clearly, CAs can be a tool for persuasion (Lehto & Oinas-Kukkonen, 2017), especially given that they have already been shown to be capable of influencing the user’s cognition, emotions, and behavior. CAs offer developers options to achieve other goals besides supporting users in making decisions or completing tasks. For example, researchers, such as Adler et al. (2016), Derrick and Ligon (2014), or Harjunen et al. (2018) have adapted established approaches for persuasion known from human-to-human interaction for designing CAs, e.g., emotional persuasion strategies (Adler et al., 2016). However, subconsciously manipulating users comes with great ethical implications. Referring to the literature on digital nudging (Lembcke et al., 2019), various aspects must be considered and weighed against one another before interference with users’ free will can be considered to be ethically justified: (1) the individual’s freedom of choice should be preserved, (2) the intention behind the design should be transparent, and (3) the goal-oriented intention of the interference should be justified.

Similar considerations have been presented in other seminal models and frameworks, such as the principles of ethical and persuasive technology design. Berdichevsky and Neuenschwander (2002) proposed rules for building trustworthy AI, as characterized by Floridi (2019). Nonetheless, to the best of our knowledge, there is currently no dedicated discourse on the ethical design of CAs. Extending from general considerations on the ethics of persuasion in other disciplines, future research should systematically identify, analyze, and discuss the unique aspects of CA design. For instance, CA capabilities have drastically improved in recent years (McTear, 2017), enabling CAs to display empathy via sentiment analysis (Diederich et al., 2019), which invokes an area of unique ethical challenges (e.g., justifying chatbots that dynamically adapt to the emotional state of the user, making it increasingly more difficult for the user to make a free decision). Similarly, we need to investigate other new means that CAs have for taking on a humanlike appearance and interacting with users.

## D5.1: Explore when, where, and how applying persuasive CAs is ethically justifiable.

Against this background, there is also a need for research on design elements that are specifically intended to make CAs “more ethical.” For instance, a common feature of CAs is self-disclosure that they are not human (Grudin & Jacques, 2019; O’Leary, 2019) because users may find it difficult to distinguish increasingly human-like CAs from actual humans (Welch, 2018). Similar features could be developed for specific aspects of the communication between humans and CAs. For instance, a CA could let the user know that its social cues (e.g., having a name, avatar, using self-references) are intended to change the user’s perception of the CA in a certain way (e.g., letting the CA appear more trustworthy) to achieve a certain goal (e.g., riding a bike more often). Understanding how users perceive such features is an important new area of research. For instance, referencing the previous example of trustworthiness, a CA explaining its persuasive design to the user might not lead to the user becoming more aware of such an intention but could instead increase the perception of trustworthiness (e.g., “the CA takes care of the ethical dimensions of our interaction, therefore, I can trust it”).

## D5.2: Develop CA’s design elements to address the ethical dimensions of the user interaction, and investigate how users perceive these design elements.

Beyond the CA’s clear design intention to be persuasive (or, in the future, ethically aware), there are also unintended effects that need to be considered. For example, children interacting with voice-based CAs, such as Amazon’s Alexa, can, by design, be encouraged to say “please” when issuing voice commands (BBC 2019), a behavior that may then potentially be extended to human-to-human interactions as well. However, frequently formulating commands that are fulfilled instantly could also lead to similar behavior of children in human-to-human interactions (Truong, 2016). Further, a recent UNESCO (2019) report outlined that voice-based CAs can reinforce gender stereotypes as users continuously interact with mostly female CA voices in a commanding tone. Similarly, researchers have established gender bias in the design of text-based CAs, finding that developers show a clear preference for implementing CAs with obvious female-gender traits (e.g., having a traditional female name) (Feine et al., 2019). Therefore, in expanding current research clearly focused on the expected and intended effects of certain CA designs, we need research on the unintended side-effects of CAs and also on the developers’ biases and assumptions, which may lead to these side-effects.

D5.3: Investigate the unintended side-effects of CA design and study how to prevent negative sideeffects.

## 5.7 Longitudinal CA Research in a Field Study Setting

Most studies in our sample (84%) consist of empirical research, often in a controlled setting (57%), using both on-site laboratory and online experiments. In contrast, only a few studies (4%) were carried out in a field study setting despite the high availability of CAs in different contexts in practice. For example, Adam and Klumpe (2019), conducted a randomized field experiment with 2,095 visitors of an e-commerce website to investigate the impact of message interactivity and an agent’s information self-disclosure in onboarding new customers. In agreement with studies in controlled experimental settings, on information disclosure (e.g., Pickard et al., 2016; Saffarizadeh et al., 2017) and on message interactivity (e.g., Schuetzler et al., 2014), scholars have found a positive effect of both constructs on actual user behavior regarding information disclosure. Thus, the work by Adam and Klumpe (2019) provides empirical support for insights from different laboratory experiments with field data. The study thereby validated existing findings with actual user information sharing behavior in a real-world scenario. Toxtli et al. (2018) provided a further example of initial fieldwork in CA research by implementing and deploying a text-based CA for task management. Based on data from information workers’ interaction with the agent and from a survey, the authors investigate the human nature of interactions and discuss issues related to response failure or the handling of multithreaded conversations.

These exemplary studies underline CA research potential in the field. First, field studies can help to overcome shortcomings related to the external validity of the rich body of knowledge on CAs gained in controlled experimental settings (Dennis & Valacich, 2001; Karahanna et al., 2018). As shown in Adam and Klumpe’s (2019) study, knowledge gained in single or multiple laboratory experiments can be applied in field study settings. By conducting field studies on the design of and human interaction with CAs, existing knowledge can be validated (see Adam & Klumpe, 2019), extended (see Toxtli et al., 2018, who identified new aspects for study), or (partially) refuted. Thus, we formulate the following direction for future research studies:

D6.1: Conduct field studies to verify, extend, or refute existing knowledge gained from experimental research in controlled settings.

While assuming that many insights gained from laboratory experiments remain valid in the field, it will be particularly interesting to study how human perception of CAs changes when insights from different kinds of studies are combined. For example, various studies, such as Gnewuch et al. (2018), Go and Sundar (2019), and Araujo (2018), identify positive effects of different social cues on user perception (e.g., response delays to simulate a CA typing, message interactivity, or a human-like avatar), intended to make agents appear human-like. A question now is what happens if these rich social cues, identified in separate experiments, are combined in a single CA in the field. Will it be able to induce a high level of perceived anthropomorphism and, if so, will users perceive this agent as appealing or uncanny? Additionally, as indicated in Toxtli et al.’s (2018) study, we lack a solid understanding of the complex interplay of different design aspects in the field. For example, does existing research help us to know how the limited conversational capabilities of present-day CAs, often manifested in the agent’s inability to provide a purposeful response, practically influence users’ perception of agents with a human-like design. In short, current CA research offers rich knowledge gathered in controlled experimental settings. However, we do not know whether these insights hold true in the field, where various aspects, related both to the design of the agent itself and to the application context, influence users’ CA interaction and perceptions.

To advance the overall understanding of the design of CAs and human interaction with them, it would be good to move from investigating single specific aspects in controlled settings to combining existing knowledge from laboratory experiments and applying it in the field. As initial field studies such as Toxtli et al. (2018), indicate, several issues that substantially impact user perception are likely to remain in practice. Also, a complex interplay of different design aspects, so far investigated separately in different studies, could influence human-CA interaction in as yet unforeseeable ways.

D6.2: Investigate the interplay between the limited conversational capabilities of CAs and the combination of multiple (anthropomorphic) design features of CAs.

Further, we propose that researchers conduct CA studies over an extended period of time using longitudinal research. Many of the studies in our sample investigate research questions in experimental settings where participants engage in single or a few interactions with an agent. While this approach certainly has benefits for investigating the isolated impact of different design alterations on human perceptions of an agent, we argue that observing users’ perceptions of CAs over the course of multiple interactions can help us understand the emerging relationships between human users and (human-like) agents. As CAs exhibit various social cues—first and foremost, interacting via natural language as opposed to graphical user interfaces—they trigger social responses, as shown in many empirical studies in our sample (e.g., Hong & Williams, 2019; Lee & Choi, 2017; Xu & Lombard, 2017). Users are likely to form relationships with CAs over the course of multiple interactions where such agents can assume a variety of roles ranging from simple digital assistants to companions or even friends. As Bickmore and Picard’s (2005) early study shows, CAs can be designed to leverage human relationship-building approaches that support establishing social connections. Such features can induce higher levels of trust and likability. Similarly, adverse experiences, such as misunderstandings or an agent’s failure to appropriately complete a user’s request, are likely to negatively impact user perceptions of CAs. This will also influence the relationship between the user and the CA. We need information on how users will react if their befriended agent is suddenly unable to adequately answer a simple question. Will the reaction be similar to that of a computer’s failure or will it trigger a stronger social reaction similar to being disappointed by a good friend?

Further, as the specific capabilities of a CA are initially hidden from the user to some extent, they may require deeper investigation and learning, as compared to graphical user interfaces (Følstad & Brandtzæg, 2017). Then, it will be interesting to see how the adoption and use of CAs change over longer periods of time. Thus, we propose that researchers investigate the emerging relationship between users and CAs over time, and we suggest applying an interaction-centric approach (Al-Natour & Benbasat, 2009) that recognizes the different roles an agent can assume for a specific user and in a specific context.

D6.3: Study how the relationship between users and CAs takes shape during the initial use of the CA, and how it develops in multiple interactions over a longer period of time.

## 5.8 A Springboard for CA Studies in the IS Discipline

Our review analyzes and discusses the findings of 262 publications on CA design. However, given the selection criteria of our review approach, we were only able to investigate a subset of the available CA research that has been published in IS and CS as well as other disciplines, such as didactics and pedagogy, medicine, ethics, and psychology. In Table 12, we provide a nonexhaustive list of CA research that we consider important for researchers and practitioners alike as a starting point for addressing the proposed avenues.

## 5.9 Practical Implications

Our overview of the status quo of CA research and of avenues to advance the field is primarily targeted at (HCI) scholars in the IS and CS disciplines with an interest in this technological phenomenon. However, this paper also offers three key implications for practitioners.

First, the adapted research framework (Figure 2) can support CA conceptualization and implementation in practice by highlighting aspects that should be considered during the design process. For example, the framework can enable designers to reflect the relevant characteristics of the user group for whom the CA is intended (e.g., concerning age, gender, cultural background, or experience with CAs and the task at hand) or the key aspects related to how users perceive agents and interaction outcomes (e.g., measures to evaluate the agent).

Second, the coded literature can help practitioners to identify empirically grounded design approaches to influence certain design aspects related to how CAs are perceived. For example, designers can draw on the literature database in identifying conversational strategies that build trust in a CA (e.g., Schroeder & Schroeder, 2018; Stock et al., 2019) or foster enjoyment in the interaction (e.g., Beale & Creed, 2009; Liao et al., 2018). Similarly, the literature database can be useful in identifying undesirable effects on user perception because of an agent’s design. Such effects could relate to privacy concerns (Sohn, 2019) or feelings of uncanniness (Seeger et al., 2018; Strait et al., 2015; Tinwell & Sloan, 2014).

Third, our research contributes ideas for field studies collaborating between CA researchers and practitioners. In particular, longitudinal studies could be beneficial in validating findings from controlled experimental research in the field and helping to identify and overcome CAs’ shortcomings in practice. In our opinion, the substantial potential for both research and practice lies in such collaborative studies because, in practice, CAs often do not meet (high) user expectations (Luger & Sellen, 2016) and much of the insights gained in research have not been transferred to application in the field.

## 5.10 Limitations

Although we conducted our organizing and assessing review and subsequent analysis according to established guidelines, potential limitations should be considered. First, in our review and analysis, we have a restricted view of the available literature because of the applied review methodology. We followed established guidelines in order to be as rigorous as possible, given our self-chosen review constraints (i.e., selecting keywords, timeframe, and outlets). We believe our selection of keywords and outlets is representative and sufficient for the scope of this review article. In total, we found 262 publications in various outlets that allowed us to draw a holistic picture of state-of-the-art CA research. However, our selection of the outlets could be open to criticism. We decided to focus on an IS perspective and selected Basket of Eight journals and leading conferences as main sources for our review.

Table 12. Springboard to Further CA Research

<table><tr><td>Authors</td><td>Title</td><td>Discipline</td></tr><tr><td>Bickmore &amp; Cassell (2005)</td><td>“Social Dialogue with Embodied Conversational Agents”</td><td>CS</td></tr><tr><td>Cassell (2000)</td><td>“Embodied Conversational Interface Agents”</td><td>CS</td></tr><tr><td>Gulz &amp; Haake (2006)</td><td>“Design of Animated Pedagogical Agents: A Look at Their Look”</td><td>D</td></tr><tr><td>Graesser, Hu, &amp; Person (2001)</td><td>“Teaching With the Help of Talking Heads”</td><td>D</td></tr><tr><td>Graesser et al. (2014)</td><td>“Learning by Communicating in Natural Language with Conversational Agents”</td><td>P &amp; D</td></tr><tr><td>Graesser &amp; McNamara (2010)</td><td>“Self-Regulated Learning in Learning Environments with Pedagogical Agents that Interact in Natural Language”</td><td>D</td></tr><tr><td>Johnson et al. (2000)</td><td>“Animated Pedagogical Agents: Face-To-Face Interaction in Interactive Learning Environments”</td><td>D</td></tr><tr><td>Laranjo et al. (2018)</td><td>“Conversational Agents in Healthcare: A Systematic Review”</td><td>M</td></tr><tr><td>Louwerse et al. (2009)</td><td>“Embodied Conversational Agents as Conversational Partners”</td><td>P</td></tr><tr><td>Massaro et al. (1999)</td><td>“Developing and Evaluating Conversational Agents”</td><td>P</td></tr><tr><td>Montenegro et al. (2019)</td><td>“Survey of Conversational Agents in Health”</td><td>M</td></tr><tr><td>Moreno (2012)</td><td>“Multimedia Learning with Animated Pedagogical Agents”</td><td>D</td></tr><tr><td>Provoost et al. (2017)</td><td>“Embodied Conversational Agents in Clinical Psychology: A Scoping Review”</td><td>M &amp; P</td></tr><tr><td>Vaidyam et al. (2019)</td><td>“Chatbots and Conversational Agents in Mental Health: A Review of the Psychiatric Landscape”</td><td>M &amp; P</td></tr><tr><td>Veletsianos &amp; Russell (2014)</td><td>“Pedagogical Agents”</td><td>D</td></tr><tr><td>Wik &amp; Hjalmarsson (2009)</td><td>“Embodied Conversational Agents in Computer-Assisted Language Learning”</td><td>D</td></tr><tr><td>Luxton (2020)</td><td>“Ethical Implications of Conversational Agents in Global Public Health</td><td>M &amp; E</td></tr><tr><td>McGreevey et al. (2020)</td><td>“Clinical, Legal, and Ethical Aspects of Artificial Intelligence-Assisted Conversational Agents in Health Care”</td><td>M &amp; E</td></tr><tr><td>European Commission (2019)</td><td>“Ethics Guidelines for Trustworthy AI”</td><td>E</td></tr><tr><td>Floridi (2019)</td><td>“Establishing the Rules for Building Trustworthy AI”</td><td>E</td></tr><tr><td colspan="3">Note: CS = computer science, D = didactics and pedagogy, M = medicine, P = psychology, E = ethics</td></tr></table>

Also, we selected a representative subset of CS outlets to identify research published outside of IS research. Future research could include further non-IS outlets to broaden our rather IS-centered impression of research on human-CA interaction.

Second, a limitation of all review articles is the ongoing availability of new publications. We conducted the search process in January 2019 and updated it in November 2019. Considering the rate of publications over time (see Figure C1 in Appendix C), we can assume that even more publications have become available while writing this article. Future work could enrich the presentation of our CA research. One way to tackle this problem could be implementing an online database that enables authors to submit their studies and their respective classification following our framework. This would offer a reasonably recent overview of the available research and provide a means to discover further trends and opportunities for future research. Similar online databases exist, for example, to search for variables and items (Larsen & Bong, 2016) or the social cues of conversational agents (Feine et al., 2019).

Third, our analysis and discussion are dependent on our sample. As outlined, we followed a rigorous process in our review and assumed our set of publications to be representative for discussing the status quo of HCI-related CA research from an IS perspective. Moreover, by including research published in non-IS outlets, we provide an even more holistic picture; however, a different sample of publications might result in different findings. Nevertheless, we believe that our identified research streams are insightful, relatively stable, and consistent, independent of potential changes in the underlying data—for example, the appearance of new publications.

Fourth, our framework could be extended with more dimensions and more granular characteristics. The framework allowed us to classify the studies sufficiently to provide a holistic picture of the research status quo of CA. Nevertheless, future work could, for instance, extend the agent dimension with a more detailed set of characteristics that would provide a more productive overview of research on this specific aspect. To illustrate, Feine et al. (2019) differentiate CAs’ design features into four categories (i.e., verbal, visual, auditory, and invisible) with multiple subcategories. Similarly, future research could enrich the human dimensions evaluated and the context with more detailed characteristics. The resulting insights of the interaction might enable us to further investigate the transferability and adaptability of knowledge.

## 6 Conclusion

In this article, we organize a rich body of knowledge on the interaction between humans and CAs in the IS and CS disciplines. We contribute a framework adapted from established research that allows the vast body of knowledge on CAs to be classified. The framework enables the research community to understand the interaction between humans and CAs in specific contexts and can guide future research on CAs. Based on the findings of our literature review, we assess the status quo of CA research and propose six avenues with sixteen actionable directions to move CA research forward. We invite researchers to address the outlined directions for future studies and contribute valuable knowledge to this exciting research area.

## Acknowledgments

We would like to thank our senior editor Dorothy E. Leidner and the anonymous reviewers for their support, encouragement, and valuable feedback, which helped us substantially improve the paper throughout the review process.

## References

Abul, M., Siddike, K., Spohrer, J., Demirkan, H., & Kohda, Y. (2018). People’s interactions with cognitive assistants for enhanced performances. Proceedings of the Hawaii International Conference on System Sciences.

Adam, M., & Klumpe, J. (2019). Onboarding with a chat: The effects of message interactivity and platform self-disclosure on user disclosure propensity. Proceedings of the European Conference on Information Systems.

Adler, R. F., Iacobelli, F., & Gutstein, Y. (2016). Are you convinced? A Wizard of Oz study to test emotional vs. Rational persuasion strategies in dialogues. Computers in Human Behavior, 57, 75-81.

Al-Natour, S., & Benbasat, I. (2009). The adoption and use of it artifacts: A new interaction-centric model for the study of user-artifact relationships. Journal of the Association for Information Systems, 10(9), 661-685.

Al-Natour, S., Benbasat, I., & Cenfetelli, R. T. (2006). The role of design characteristics in shaping perceptions of similarity: The case of online shopping assistants. Journal of the Association for Information Systems, 7(12), 821-861.

Al-Natour, S., Benbasat, I., & Cenfetelli, R. T. (2009). The antecedents of customer self-disclosure to online virtual advisors. Proceedings of the International Conference on Information Systems.

Anabuki, M., Kakuta, H., Yamamoto, H., & Tamura, H. (2000). Welbo: An embodied conversational agent living in mixed reality spaces. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Araujo, T. (2018). Living up to the chatbot hype: The influence of anthropomorphic design cues and communicative agency framing on conversational agent and company perceptions. Computers in Human Behavior, 85, 183-189.

Ashktorab, Z., Jain, M., Liao, V. Q., & Weisz, J. D. (2019). Resilient chatbots: Repair strategy preferences for conversational breakdowns. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Baier, D., Rese, A., & Röglinger, M. (2018). Conversational user interfaces for online shops? A categorization of use cases. Proceedings of the International Conference on Information Systems.

Bandara, W., Gorbacheva, E., Beekhuyzen, J.,

Furtmueller, E., & Miskon, S. (2015). Achieving rigor in literature reviews: Insights from qualitative data analysis and tool-support. Communications of the Association for Information Systems, 34(8), 154-204.

Banker, R. D., & Kauffman, R. J. (2004). 50th anniversary article—The evolution of research on information systems: A fiftieth-year survey of the literature in management science. Management Science, 50(3), 281-298.

Banks, J. (2018). Perceived moral agency scale: Development and validation of a metric for humans and social machines. Computers in Human Behavior.

Bariff, M. L., & Ginzberg, M. J. (1982). MIS and the behavioral sciences: Research patterns and prescriptions. The Data Base for Advances in Infromation Systems, 14(1), 19-26

Beale, R., & Creed, C. (2009). Affective interaction: How emotional agents affect users. International Journal of Human Computer Studies, 67(9), 755- 776.

Belbin, R. M. (2010). Management teams: Why they succeed or fail. Routledge.

Belk, R. W. (1988). Possessions and the extended self. Journal of Consumer Research. 15(2), 139-168

Belk, R. W. (2013). Extended self in a digital world. Journal of Consumer Research, 40(3), 477-500.

Bell, S., Sarkar, A., & Wood, C. (2019). Perceptions of chatbots in therapy. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Ben Mimoun, M. S., Poncin, I., & Garnier, M. (2012). Case study-Embodied virtual agents: An analysis on reasons for failure. Journal of Retailing and Consumer Services, 19(6), 605-612.

Benlian, A., Klumpe, J., & Hinz, O. (2020). Mitigating the intrusive effects of smart home assistants by using anthropomorphic design features: A multimethod investigation. Information Systems Journal, 30(6), 1010-1042.

Berdichevsky, D., & Neuenschwander, E. (2002). Toward an ethics of persuasive technology. Communications of the ACM, 42(5), 51-58.

Berg, M. (2015). NADIA: A simplified approach towards the development of natural dialogue systems. In C. Biemann, S. Handschuh, A. Freitas, F. Meziane, & E. Métais (Eds.), Natural Language Processing and Information Systems (pp. 144-150). Springer.

Bertacchini, F., Bilotta, E., & Pantano, P. (2017). Shopping with a robotic companion. Computers

in Human Behavior, 77, 382-395.

Bhattacherjee, A. (2012). Social science research: Principles, methods, and practices. Creative Commons.

Biancardi, B., Cafaro, A., & Pelachaud, C. (2017). Could a virtual agent be warm and competent? Investigating user’s impressions of agent’s nonverbal behaviours. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Bickmore, T., & Cassell, J. (2005). Social dialogue with embodied conversational agents. In Jan C. J. van Kuppevelt, L. Dybkjær, N. O. Bernsen (Eds.) Advances in natural multimodal dialogue systems (pp. 23-54). Springer

Bickmore, T. W., & Picard, R. W. (2005). Establishing and maintaining long-term human-computer relationships. ACM Transactions on Computer-Human Interaction, 12(2), 293-327.

Bittner, E. A. C., Oeste-Reiß, S., & Leimeister, J. M. (2019). Where is the bot in our team? Toward a taxonomy of design option combinations for conversational agents in collaborative work. Proceedings of the Hawaii International Conference on System Sciences.

Bittner, E., & Shoury, O. (2019). Designing automated facilitation for design thinking: A chatbot for supporting teams in the empathy map method. Proceedings of the Hawaii International Conference on System Sciences.

Bogardus, E. S. (1947). Measurement of personal-group relations. Sociometry, 10(4), 306-311.

Braun, M., & Alt, F. (2019). Affective assistants: A matter of states and traits. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Brynjolfsson, E., & McAfee, A. (2016). The second machine age: Work, progress, and prosperity in a time of brilliant technologies. Norton.

Burgoon, J. K., Bonito, J. A., Lowry, P. B., Humpherys, S. L., Moody, G. D., Gaskin, J. E., & Giboney, J. S. (2016). Application of expectancy violations theory to communication with and judgments about embodied agents during a decision-making task. International Journal of Human Computer Studies, 91, 24-36.

Burgoon, Judee K., Stern, L. A., & Dillmann, L. (1995). Interpersonal adaptation: Dyadic interaction patterns. Cambridge University Press.

Burmester, M., Schippert, K., Zeiner, K. M., & Platz, A. (2019). Creating positive experiences with digital companions. Proceedings of the ACM CHI

Conference on Human Factors in Computing Systems.

Burton, N., & Gaskin, J. (2019). “Thank you, Siri”: Politeness and intelligent digital assistants. Proceedings of the Americas Conference on Information Systems.

Byrne, D. (1971). The attraction paradigm. Academic Press.

Byrne, D., & Griffitt, W. (1969). Similarity and awareness of similarity of personality characteristics as determinants of attraction. Journal Of Experimental Research In Personality, 3(3), 179-186.

Byrne, D., Griffitt, W., & Stefaniak, D. (1967). Attraction and similarity of personality characteristics. Journal of Personality and Social Psychology, 5(1), 82-90.

Cafaro, A., Vilhjalmsson, H. H., & Bickmore, T. (2016). First impressions in human-agent virtual encounters. ACM Transactions on Computer-Human Interaction, 24(4), 1-40.

Candello, H., Pinhanez, C., Pichiliani, M., Cavalin, P., Figueiredo, F., Vasconcelos, M., & Carmo, H. Do. (2019). The effect of audiences on the user experience with conversational interfaces in physical spaces. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Card, S. K., Moran, T. P., & Newell, A. (1980). The keystroke-level model for user performance time with interactive systems. Communications of the ACM, 23(7), 396-410.

Cardona, D. R., Schönborn, S., Werth, O., & Breitner, M. H. (2019). A mixed methods analysis of the adoption and diffusion of chatbot technology in the German insurance sector. Proceedings of the Americas Conference on Information Systems.

Carlotto, T., & Jaques, P. A. (2016). The effects of animated pedagogical agents in an English-as-aforeign-language learning environment. International Journal of Human Computer Studies, 95, 15-26.

Carroll, J. M. (2020). Human computer interaction: Brief intro. In The Encyclopedia of Human-Computer Interaction (2nd ed.). Interaction Design Foundation. https://www.interactiondesign.org/literature/book/the-encyclopedia-ofhuman-computer-interaction-2nd-ed/interaction - design-brief-intro

Carter, M., Grover, V., & Thatcher, J. B. (2013). Mobile devices and the self: Developing the concept of mobile phone identity. In I. Lee (Ed.), Strategy, Adoption, and Competitive Advantage of Mobile

Services in the Global Economy. IGI Global.

Cassell, J., Bickmore, T., Billinghurst, M., Campbell, L., Chang, K., Vilhjálmsson, H., & Yan, H. (1999). Embodiment in conversational interfaces. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Cassell, Justine. (2000). Embodied conversational interface agents. Communications of the ACM, 43(4), 70-78.

Chattaraman, V., Kwon, W.-S., Gilbert, J. E., & Ross, K. (2018). Should AI-based, conversational digital assistants employ social- or task-oriented interaction style? A task-competency and reciprocity perspective for older adults. Computers in Human Behavior, 90, 315-330.

Chaves, A. P., & Gerosa, M. A. (2018). Single or multiple conversational agents? An interactional coherence comparison. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Cho, E. (2019). Hey Google, can I ask you something in private? The effects of modality and device in sensitive health information acquisition from voice assistants. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Clark, L., Pantidi, N., Cooney, O., Doyle, P., Garaialde, D., Edwards, J., … Cowan, B. R. (2019). What makes a good conversation? Challenges in designing truly conversational agents. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Comendador, B. E. V., Francisco, B. M. B., Medenilla, J. S., Nacion, S. M. T., & Serac, T. B. E. (2015). Pharmabot: A pediatric generic medicine consultant chatbot. Journal of Automation and Control Engineering, 3(2), 137-140.

Constantin, A., Lai, C., Farrow, E., Alex, B., Jeuring, J., Pel-Littel, R., & Nap, H. H. (2019). “Why is the doctor a man?” Reactions of older adults to a virtual training doctor. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Cooper, H. M. (1988). Organizing knowledge synthesis: a taxonomy of literature reviews. Knowledge in Society, 1(1), 104-126.

Corti, K., & Gillespie, A. (2016). Co-constructing intersubjectivity with artificial conversational agents: People are more likely to initiate repairs of misunderstandings with agents represented as human. Computers in Human Behavior, 58, 431- 442.

Cowan, B. R., Branigan, H. P., Obregón, M., Bugis, E.,

& Beale, R. (2015). Voice anthropomorphism, interlocutor modelling and alignment effects on syntactic choices in human-computer dialogue. International Journal of Human Computer Studies, 83, 27-42.

Cowell, A. J., & Stanney, K. M. (2005). Manipulation of non-verbal interaction style and demographic embodiment to increase anthropomorphic computer character credibility. International Journal of Human Computer Studies, 62(2), 281- 306.

Crockett, K., Latham, A., & Whitton, N. (2017). On predicting learning styles in conversational intelligent tutoring systems using fuzzy decision trees. International Journal of Human Computer Studies, 97, 98-115.

Dale, R. (2016). The return of the chatbots. Natural Language Engineering, 22(5), 811-817.

Davenport, T. H., & Kirby, J. (2016). Just how smart are smart machines? MIT Sloan Management Review, 57(3), 21-25.

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. Management Information Systems Quarterly, 13(3), 319-340.

De Rosis, F., Pelachaud, C., Poggi, I., Carofiglio, V., & De Carolis, B. (2003). From Greta’s mind to her face: Modelling the dynamics of affective states in a conversational embodied agent. International Journal of Human Computer Studies, 59(1-2), 81- 118.

Dennis, A. R., & Valacich, J. S. (2001). Conducting experimental research in information systems. Communications of the Association for Information Systems, 7(5), 1-41.

Derrick, D. C., & Ligon, G. S. (2014). The affective outcomes of using influence tactics in embodied conversational agents. Computers in Human Behavior, 33, 39-48.

Desideri, L., Ottaviani, C., Malavasi, M., di Marzio, R., & Bonifacci, P. (2018). Emotional processes in human-robot interaction during brief cognitive testing. Computers in Human Behavior, 90, 331- 342.

Diederich, S., Brendel, A. B., & Kolbe, L. M. (2020). Designing anthropomorphic enterprise conversational agents. Business & Information Systems Engineering, (62), 193-209.

Diederich, S., Brendel, A. B., Lichtenberg, S., & Kolbe, L. M. (2019). Design for fast request fulfillment or natural interaction? Insights from an online experiment with a conversational agent. Proceedings of the European Conference on

Information Systems.

Diederich, S., Janßen-Müller, M., Brendel, A. B., & Morana, S. (2019). Emulating empathetic behavior in online service encounters with sentiment-adaptive responses: Insights from an experiment with a conversational agent. Proceedings of the International Conference on Information Systems.

Diederich, S., Lembcke, T.-B., Brendel, A. B., & Kolbe, L. M. (2021). Understanding the impact that response failure has on how users perceive anthropomorphic conversational service agents: Insights from an online experiment. AIS Transactions on Human-Computer Interaction, 13(1), 82-103.

Diederich, S., Lichtenberg, S., Brendel, A. B., & Trang, S. (2019). Promoting sustainable mobility beliefs with persuasive and anthropomorphic design: Insights from an experiment with a conversational agent. Proceedings of the International Conference on Information Systems.

Dolata, M., Kilic, M., & Schwabe, G. (2019). When a computer speaks institutional talk: Exploring challenges and potentials of virtual assistants in face-to-face advisory services. Proceedings of the Hawaii International Conference on System Sciences .

Duan, W., Yamashita, N., Hwang, S. Y., & Fussell, S. R. (2018). “Let me ask them to clarify if you don’t want to”: A clarification agent for nonnative speakers. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Ducheneaut, N., Don Wen, M. H., Yee, N., & Wadley, G. (2009). Body and mind: A study of avatar personalization in three virtual worlds. Proceedings of the Conference on Human Factors in Computing Systems.

Elson, J. S., Derrick, D. C., & Ligon, G. S. (2018). Examining trust and reliance in collaborations between humans and automated agents. Proceedings of the Hawaii International Conference on System Sciences.

Epley, N., Waytz, A., & Cacioppo, J. T. (2007). On seeing human: A three-factor theory of anthropomorphism. Psychological Review, 114(4), 864-886.

European Commission. (2019). Ethics guidelines for trustworthy AI. European Union Publications Office. https://op.europa.eu/en/ publicationdetail/-/publication/d3988569-0434-11ea-8c1f-01aa75ed71a1

Fadhil, A., & Villafiorita, A. (2017). An adaptive

learning with gamification & conversational UIs. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Fast, E., Chen, B., Mendelsohn, J., Bassen, J., & Bernstein, M. (2017). Iris: A conversational agent for complex tasks. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Feine, J., Gnewuch, U., Morana, S., & Maedche, A. (2019). Gender Bias in chatbot design. Proceedings of CONVERSATIONS 2019 (pp. 79- 93).

Feine, J., Gnewuch, U., Morana, S., & Maedche, A. (2019). A taxonomy of social cues for conversational agents. International Journal of Human-Computer Studies, 132(December), 138- 161.

Feine, J., Morana, S., & Gnewuch, U. (2019). Measuring service encounter satisfaction with customer service chatbots using sentiment analysis. Proceedings of the International Conference on Wirtschaftsinformatik.

Floridi, L. (2019). Establishing the rules for building trustworthy AI. Nature Machine Intelligence, 1(6), 261-262.

Følstad, A., & Brandtzæg, P. B. (2017). Chatbots and the new world of HCI. Interactions, 24(4), 38-42.

Forlizzi, J., Zimmerman, J., Mancuso, V., & Kwak, S. (2007). How interface agents affect interaction between humans and computers. Proceedings of the 2007 Conference on Designing Pleasurable Products and Interfaces (pp. 209-221).

Fryer, L. K., Ainley, M., Thompson, A., Gibson, A., & Sherlock, Z. (2017). Stimulating and sustaining interest in a language course: An experimental comparison of Chatbot and Human task partners. Computers in Human Behavior, 75, 461-468.

Gambino, A., Shyam Sundar, S., & Kim, J. (2019). Digital doctors and robot receptionists: User attributes that predict acceptance of automation in healthcare facilities. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Gefen, D., & Straub, D. (2003). Managing User Trust in B2C e-Services. E-Service Journal, 2(2), 7-24.

Gerlach, J. H., & Kuo, F. Y. (1991). Understanding human-computer interaction for information systems design. MIS Quarterly, 15(4), 527-549.

Giles, H., Coupland, N., & Coupland, J. (2010). Accommodation theory: Communication, context, and consequence. In H. Giles, J. Coupland, N. Coupland, K. Oatley (Eds.),

Contexts of Accommodation. Cambridge University Press. https://doi.org/10.1017/ cbo9780511663673.001

Gnewuch, U., Morana, S., Adam, M. T. P., & Maedche, A. (2018). Faster is not always better: Understanding the effect of dynamic response delays in human-chatbot interaction. Proceedings of the European Conference on Information Systems.

Gnewuch, U., Morana, S., & Maedche, A. (2017). Towards designing cooperative and social conversational agents for customer service. Proceedings of the International Conference on Information Systems.

Go, E., & Sundar, S. S. (2019). Humanizing chatbots: The effects of visual, identity and conversational cues on humanness perceptions. Computers in Human Behavior, 97, 304-316.

Goasduff, L. (2019). Chatbots will appeal to modern workers. Gartner. https://www.gartner.com/ smarterwithgartner/chatbots-will-appeal-tomodern-workers/

Gong, L. (2008). How social is social responses to computers? The function of the degree of anthropomorphism in computer representations. Computers in Human Behavior, 24(4), 1494- 1509.

Goodhue, D. L., & Thompson, R. L. (1995). Tasktechnology fit and individual performance. MIS Quarterly, 19(2), 213-236.

Graesser, A. C., Cai, Z., Morgan, B., & Wang, L. (2017). Assessment with computer agents that engage in conversational dialogues and trialogues with learners. Computers in Human Behavior, 76, 607-616.

Graesser, A. C., Hu, X., & Person, N. (2001). Teaching with the help of talking heads. Proceedings of the IEEE International Conference on Advanced Learning Technologies.

Graesser, A. C., Li, H., & Forsyth, C. (2014). Learning by communicating in natural language with conversational agents. Current Directions in Psychological Science, 23(5), 374-380.

Graesser, A., & McNamara, D. (2010). Self-regulated learning in learning environments with pedagogical agents that interact in natural language. Educational Psychologist, 45(4), 234- 244.

Gregor, S., Kruse, L. C., & Seidel, S. (2020). The anatomy of a design principle. Journal of the Association for Information Systems, 21(6), 1622- 1652.

Grice, H. P. (1975). Logic and conversation. In P. cole & J. L. Morgan (Eds.), Syntax and Semantics: Vol. 3. Speech Acts (pp. 41-58).

Groom, V., Takayama, L., Ochi, P., & Nass, C. (2008). I am my robot: The impact of robot-building and robot form on operators. Proceedings of the 4th ACM/IEEE International Conference on Human-Robot Interaction.

Grudin, J., & Jacques, R. (2019). Chatbots, humbots, and the quest for artificial general intelligence. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Gulz, A., & Haake, M. (2006). Design of animated pedagogical agents: A look at their look. International Journal of Human Computer Studies, 64(4), 322-339.

Hanus, M. D., & Fox, J. (2015). Persuasive avatars: The effects of customizing a virtual salespersons appearance on brand liking and purchase intentions. International Journal of Human Computer Studies, 84, 33-40.

Harjunen, V. J., Spapé, M., Ahmed, I., Jacucci, G., & Ravaja, N. (2018). Persuaded by the machine: The effect of virtual nonverbal cues and individual differences on compliance in economic bargaining. Computers in Human Behavior, 87, 384-394.

Hayashi, Y. (2013). Pedagogical conversational agents for supporting collaborative learning. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Heinrich, L. J., Heinzl, A., & Riedl, R. (2011). Wirtschaftsinformatik: Einführung und Grundlegung. Springer.

Herborn, K., Stadler, M., Mustafić, M., & Greiff, S. (2018). The assessment of collaborative problem solving in PISA 2015: Can computer agents replace humans? Computers in Human Behavior, 104, Article 104624.

Hill, J., Randolph Ford, W., & Farreras, I. G. (2015). Real conversations with artificial intelligence: A comparison between human-human online conversations and human-chatbot conversations. Computers in Human Behavior, 49, 245-250.

Hobert, S. (2019). Say hello to “coding tutor”! Design and evaluation of a chatbot-based learning system supporting students to learn to program. Proceedings of the International Conference on Information Systems.

Hobert, S., & Wolff, R. M. von. (2019). Say hello to your new automated tutor: A structured literature review on pedagogical conversational agents. Proceedings of International Conference on

Wirtchaftsinformatik (pp. 301-314).

Hong, J. W., & Williams, D. (2019). Racism, responsibility and autonomy in HCI: Testing perceptions of an AI agent. Computers in Human Behavior, 100, 79-84.

Hsu, P., Zhao, J., Liao, K., Liu, T., & Wang, C. (2017). AllergyBot; Chatbot technology intervention for young adults with food allergies dining out. Proceedings of the CHI Conference Extended Abstracts on Human Factors in Computing Systems.

Hu, T., Xu, A., Liu, Z., You, Q., Guo, Y., Sinha, V., … Akkiraju, R. (2018). Touch your heart: A toneaware chatbot for customer care on social media. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Huang, C.-M. (2012). Designing effective behaviors for educational embodied agents. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Huang, M. H., & Rust, R. T. (2018). Artificial intelligence in service. Journal of Service Research, 21(2), 155-172.

Hubal, R. C., Fishbein, D. H., Sheppard, M. S., Paschall, M. J., Eldreth, D. L., & Hyde, C. T. (2008). How do varied populations interact with embodied conversational agents? Findings from inner-city adolescents and prisoners. Computers in Human Behavior, 24(3), 1104-1138.

Hwang, G., Oh, C. Y., Lee, J., & Lee, J. (2019). It sounds like a woman: Exploring gender stereotypes in South Korean voice assistants. In Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Hyde, J., Carter, E. J., Kiesler, S., & Hodgins, J. K. (2015). Using an interactive avatar’s facial expressiveness to increase persuasiveness and socialness. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems (pp. 1719-1728).

Ipsoft. (2020). Amelia in action: A selection of stories from organizations adopting IPsoft’c cognitive agent. http://www.ipsoft.com/amelia/

Jain, M., Kota, R., Kumar, P., & Patel, S. (2018). Convey: Exploring the use of a context view for chatbots. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Jeong, Y., Kang, Y., & Lee, J. (2019). Exploring effects of conversational fillers on user perception of conversational agents. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Jin, S. A. A. (2010). The effects of incorporating a virtual agent in a computer-aided test designed for stress management education: The mediating role of enjoyment. Computers in Human Behavior, 26(3), 443-451.

Johnson, K. (2018). Facebook Messenger hits 100,000 bots. VentureBeat. https://venturebeat.com/ 2017/04/18/facebook-messenger-hits-100000- bots/

Johnson, W., Rickel, J., & Lester, J. (2000). Animated pedagogical agents: Face-to-face interaction in interactive learning environments. International Journal of Artificial Intelligence in Education, 11(1), 47-78.

Jucks, R., Linnemann, G. A., & Brummernhenrich, B. (2018). Student evaluations of a (rude) spoken dialogue system insights from an experimental study. Advances in Human-Computer Interaction, 2018(SI), Article 8406187.

Jung, H., Hwang, G., Lee, J., Oh, C., Oh, C. Y., & Suh, B. (2019). Tell me more: Understanding user interaction of smart speaker news powered by conversational search. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Kanaoka, T., & Mutlu, B. (2015). Designing a motivational agent for behavior change in physical activity. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Karahanna, E., Benbasat, I., Bapna, R., & Rai, A. (2018). Opportunities and challenges for different types of online experiments. MIS Quarterly, 42(4), iii-xi.

Kim, D., Park, K., & Park, Y. (2018). Alexa, tell me more: The effect of advertisements on memory accuracy from smart speakers. Proceedings of the Pacific Asia Conference on Information Systems.

Kim, K. J., Park, E., & Shyam Sundar, S. (2013). Caregiving role in human-robot interaction: A study of the mediating effects of perceived benefit and social presence. Computers in Human Behavior, 29(4), 1799-1806.

Kim, Y., Kwak, S. S., & Kim, M. S. (2013). Am I acceptable to you? Effect of a robot’s verbal language forms on people’s social distance from robots. Computers in Human Behavior, 29(3), 1091-1101.

Kim, Y., & Mutlu, B. (2014). How social distance shapes human-robot interaction. International Journal of Human Computer Studies, 72(12), 783-795.

Knijnenburg, B. P., & Willemsen, M. C. (2016).

Inferring capabilities of intelligent agents from their external traits. ACM Transactions on Interactive Intelligent Systems, 6(4), 1-25.

Kocaballi, A. B., Berkovsky, S., Quiroz, J. C., Laranjo, L., Tong, H. L., Rezazadegan, D., … Coiera, E. (2019). The personalization of conversational agents in health care: Systematic review. Journal of Medical Internet Research, 21(11), Article e15360.

Kowalski, J., Skorupska, K., Kopeć, W., Jaskulska, A., Abramczuk, K., Biele, C., & Marasek, K. (2019). Older adults and voice interaction: A pilot study with google home. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Kozlowski, S. W. J., & Ilgen, D. R. (2006). Enhancing the effectiveness of work groups and teams: a reflection. Perspectives on Psychological Science, 13(2), 205-212.

Krämer, N. C., Lucas, G., Schmitt, L., & Gratch, J. (2018). Social snacking with a virtual agent: On the interrelation of need to belong and effects of social responsiveness when interacting with artificial entities. International Journal of Human Computer Studies, 109, 112-121.

Krämer, N., Kopp, S., Becker-Asano, C., & Sommer, N. (2013). Smile and the world will smile with you: The effects of a virtual agent’s smile on users’ evaluation and behavior. International Journal of Human Computer Studies, 71(3), 335-349.

Lahoual, D., & Fréjus, M. (2019). When users assist the voice assistants: From supervision to failure resolution. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Laranjo, L., Dunn, A. G., Tong, H. L., Kocaballi, A. B., Chen, J., Bashir, R., … Coiera, E. (2018). Conversational agents in healthcare: A systematic review. JAMIA, 25(9), 1248-1258.

Larsen, K. R., & Bong, C. H. (2016). A tool for addressing construct identity in literature reviews and meta-analyses. MIS Quarterly, 40(3), 529- 551.

Laumer, S., Maier, C., & Gubler, F. T. (2019). Chatbot acceptance in healthcare: Explaining user adoption of conversational agents for disease diagnosis. Proceedings of the European Conference on Information Systems.

Laumer, S., Racheva, A., Gubler, F., & Maier, C. (2019). Use cases for conversational agents: An interview-based study. Proceedings of the Americas Conference on Information Systems.

Le Bigot, L., Jamet, E., Rouet, J. F., & Amiel, V. (2006).

Mode and modal transfer effects on performance and discourse organization with an information retrieval dialogue system in natural language. Computers in Human Behavior, 22(3), 467-500.

Lechler, R., Stoeckli, E., Rietsche, R., & Uebernickel, F. (2019). Looking beneath the tip of the iceberg: the two-sided nature of chatbots and their roles for digital feedback exchange. Proceedings of the European Conference on Information Systems.

Lee, C., Lesh, N., Sidner, C. L., Morency, L.-P., Kapoor, A., & Darrell, T. (2004). Nodding in conversations with a robot. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Lee, K. M., Jung, Y., Kim, J., & Kim, S. R. (2006). Are physically embodied social agents better than disembodied social agents? The effects of physical embodiment, tactile interaction, and people’s loneliness in human-robot interaction. International Journal of Human Computer Studies, 64(10), 962-973.

Lee, M. K., Kiesler, S., Forlizzi, J., & Rybski, P. (2012). Ripple effects of an embedded social agent. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Lee, S. Y., & Choi, J. (2017). Enhancing user experience with conversational agent for movie recommendation: Effects of self-disclosure and reciprocity. International Journal of Human Computer Studies, 103, 95-105.

Lehto, T., & Oinas-Kukkonen, H. (2017). Examining the persuasive potential of web-based health behavior change support systems. AIS Transactions on Human-Computer Interaction, 7(3), 126-140.

Leidner, D. (2018). Review and theory symbiosis: an introspective retrospective. Journal of the Association for Information Systems, 19(06), 552- 567.

Leite, I., Pereira, A., Mascarenhas, S., Martinho, C., Prada, R., & Paiva, A. (2013). The influence of empathy in human-robot relations. International Journal of Human Computer Studies, 71(3), 250- 260.

Lembcke, T. B., Engelbrecht, N., Brendel, A. B., & Kolbe, L. M. (2019). To nudge or not to nudge: Ethical considerations of digital nudging based on its behavioral economics roots. Proceedings of the European Conference on Information Systems.

Li, D., Browne, G. J., & Chau, P. Y. K. (2006). An empirical investigation of web site use using a commitment-based model. Decision Sciences, 37(3), 427-444.

Li, J. (2015). The benefit of being physically present: A survey of experimental works comparing copresent robots, telepresent robots and virtual agents. International Journal of Human Computer Studies, 77, 23-27.

Liao, Q. V., Hussain, M. M., Chandar, P., Davis, M., Crasso, M., Wang, D., … Geyer, W. (2018). All Work and no Play? Conversations with a question-and-answer chatbot in the wild. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Looije, R., Neerincx, M. A., & Cnossen, F. (2010). Persuasive robotic assistant for health selfmanagement of older adults: Design and evaluation of social behaviors. International Journal of Human Computer Studies, 68(6), 386- 397.

Louwerse, M. M., Graesser, A. C., McNamara, D. S., & Lu, S. (2009). Embodied conversational agents as conversational partners. Applied Cognitive Psychology, 23(9), 1244-1255.

Luger, E., & Sellen, A. (2016). “Like having a really bad PA”: The gulf between user expectation and experience of conversational agents. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems (pp. 5286-5297).

Luxton, D. D. (2020). Ethical implications of conversational agents in global public health. Bulletin of the World Health Organization, 98(4), 285.

Maedche, A., Legner, C., Benlian, A., Berger, B., Gimpel, H., Hess, T., … Söllner, M. (2019). AIbased digital assistants. Business & Information Systems Engineering, (4), 1-28.

Malone, T. W. (2018). How human-computer “superminds” are redefining the future of work. MIT Sloan Management Review, 59(4), 34-41.

Massaro, D. W., Cohen, M. M., Daniel, S., & Cole, R. A. (1999). Developing and evaluating conversational agents. In P. A. Hanhock (Ed.), Human Performance and Ergonomics (pp. 173- 194). Academic Press.

Matsushita, M., Maeda, E., & Kato, T. (2004). An interactive visualization method of numerical data based on natural language requirements. International Journal of Human Computer Studies, 60(4), 469-488.

Mavridis, P., Huang, O., Qiu, S., Gadiraju, U., & Bozzon, A. (2019). Chatterbox: Conversational interfaces for microtask crowdsourcing. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems (pp. 243- 251).

McAfee, A., & Brynjolfsson, E. (2017). Machine, platform, crowd: Harnessing our digital future. Norton.

McGreevey, J. D., Hanson, W., & Koppel, R. (2020). Clinical, legal, and ethical aspects of artificial intelligence-assisted conversational agents in health care. JAMA, 324(6), 552-553.

McQuiggan, S. W., & Lester, J. C. (2007). Modeling and evaluating empathy in embodied companion agents. International Journal of Human Computer Studies, 65(4), 348-360.

McTear, M. (2017). The rise of the conversational interface: A new kid on the block? Proceedins of the International Workshop on Future and Emerging Trends in Language Technology.

McTear, M., Callejas, Z., & Griol, D. (2016). The Conversational interface: Talking to smart devices. Springer.

Meier, P., Beinke, J. H., Fitte, C., Behne, A., & Teuteberg, F. (2019). FeelFit: Design and evaluation of a conversational agent to enhance health awareness. Proceedings of the International Conference on Information Systems.

Meyer von Wolff, R., Hobert, S., Masuch, K., & Schumann, M. (2019). What do you need today ? An empirical systematization of application areas for chatbots at digital workplaces. Proceedings of the Americas Conference on Information Systems.

Miner, A., Chow, A., Adler, S., Zaitsev, I., Tero, P., Darcy, A., & Paepcke, A. (2016). Conversational agents and mental health: theory-informed assessment of language and affect. Proceedings of the International Conference on Human Agent Interaction.

Miner, A. S., Milstein, A., Schueller, S., Hegde, R., Mangurian, C., & Linos, E. (2016). Smartphonebased conversational agents and responses to questions about mental health, interpersonal violence, and physical health. JAMA Internal Medicine, 176(5), 619-625.

Montenegro, J. L. Z., da Costa, C. A., & da Rosa Righi, R. (2019). Survey of conversational agents in health. Expert Systems with Applications, 129, 56- 67.

Moon, Y. (2000). Intimate exchanges: Using computers to elicit self-disclosure from consumers. Journal of Consumer Research, 26(4), 323-339.

Morana, S., Gnewuch, U., Jung, D., & Granig, C. (2020). The effect of anthropomorphism on investment decision-making with robo-advisor chatbots. Proceedings of the European Conference on Information Systems.

Moreno, R. (2012). Multimedia learning with animated pedagogical agents. In R. E. Mayer, The Cambridge Handbook of Multimedia Learning (pp. 507-523). Cambridge University Press.

Mori, M. (2012). The uncanny valley (K. F. MacDorman & N. Kageki, Trans.). IEEE Robotics and Automation Magazine, 19(2), 98- 100. (Original work published in 1970)

Morton, H., Gunson, N., & Jack, M. (2012). Interactive language learning through speech-enabled virtual scenarios. Advances in Human-Computer Interaction, 2012, Article 389523.

Mou, Y., & Xu, K. (2017). The media inequality: Comparing the initial human-human and human-AI social interactions. Computers in Human Behavior, 72, 432-440.

Nass, C., & Moon, Y. (2000). Machines and mindlessness: Social responses to computers. Journal of Social Issues, 56(1), 81-103.

NextIT. (2018). Helping a railroad service conduct business. http://nextit.com/case-studies/amtrak

Nguyen, Q. N., & Sidorova, A. (2017). AI capabilities and user experiences: A comparative study of user reviews for assistant and non-assistant mobile apps. Proceedings of the Americas Conference on Information Systems.

Niewiadomski, R., & Pelachaud, C. (2010). Affect expression in ECAs: Application to politeness displays. International Journal of Human Computer Studies, 68(11), 851-871.

Nunamaker, J. F., Derrick, D. C., Elkins, A. C., Burgoon, J. K., & Patton, M. W. (2011). Embodied conversational agent-based kiosk for automated interviewing. Journal of Management Information Systems, 28(1), 17-48.

O’Leary, D. E. (2019). Google’s Duplex: Pretending to be human. Intelligent Systems in Accounting, Finance and Management, 26(1), 46-53.

Olson, G. M., & Olson, J. S. (2003). Human-computer interaction: Psychological aspects of the human use of computing. Annual Review of Psychology, 54(1), 491-516.

Oracle. (2016). Can virtual experiences replace reality? The future role for humans in delivering customer experience. https://www.oracle.com/webfolder/ s/delivery\_production/docs/FY16h1/doc35/CXR esearchVirtualExperiences.pdf

Otoo, B. A., & Salam, A. F. (2018). Mediating effect of intelligent voice assistant (IVA), user experience and effective use on service quality and service satisfaction and loyalty. Proceedings of the International Conference on Information

Systems.

Pereira, A. T., Prada, R., & Paiva, A. (2014). Improving social presence in human-agent interaction. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems (pp. 1449- 1458).

Perez, S. (2016). Starbucks unveils a virtual assistant that takes your order via messaging or voice. Techcrunch. https://techcrunch.com/2017/01/ 30/starbucks-unveils-a-virtual-assistant-thattakes-your-order-via-messaging-or-voice/ ?guccounter=1

Pfeuffer, N., Toutaoui, J., Adam, M., Hinz, O., & Benlian, A. (2019). Mr. and Mrs. Conversational Agent: Gender stereotyping in judge-advisor systems and the role of egocentric bias. Proceedings of the International Conference on Information Systems.

Pickard, M. D., Roster, C. A., & Chen, Y. (2016). Revealing sensitive information in personal interviews: Is self-disclosure easier with humans or avatars and under what conditions? Computers in Human Behavior, 65, 23-30.

Pickering, M. J., & Garrod, S. (2004). Toward a mechanistic psychology of dialogue. Behavioral and Brain Sciences, 27(2), 169-190.

Porcheron, M., Fischer, J. E., Reeves, S., & Sharples, S. (2018). Voice interfaces in everyday life. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Powers, A., & Kiesler, S. (2006). The advisor robot: Tracing people’s mental model from a robot’s physical attributes. Proceedings of the 2006 ACM Conference on Human-Robot Interaction.

Provoost, S., Lau, H. M., Ruwaard, J., & Riper, H. (2017). Embodied conversational agents in clinical psychology: A scoping review. Journal of Medical Internet Research, 19(5), Article e151.

Punj, G., & Stewart, D. W. (1983). Cluster analysis in marketing research: review and suggestions for application. Journal of Marketing Research, 20(2), 134-148.

Purington, A., Taft, J. G., Sannon, S., Bazarova, N. N., & Taylor, S. H. (2017). “Alexa is my new BFF”: Social roles, user satisfaction, and personification of the Amazon Echo. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Qiu, L., & Benbasat, I. (2009). Evaluating anthropomorphic product recommendation agents: A social relationship perspective to designing information systems. Journal of Management Information Systems, 25(4), 145-

182.

Qiu, L., & Benbasat, I. (2010). A study of demographic embodiments of product recommendation agents in electronic commerce. International Journal of Human Computer Studies, 68(10), 669-688.

Quynh, N., & Sidorova, A. (2018). Understanding user interactions with a chatbot: A self-determination theory approach. Proceedings of the Americas Conference on Information Systems.

Reeves, B., & Nass, C. (1996). The media equation: How people treat computers, television and new media like real people and places. The Center for the Study of Language and Information Publications.

Reinecke, K., & Bernstein, A. (2013). Knowing what a user likes: A design science approach to interfaces that automatically adapt to culture. MIS Quarterly, 37(2), 427-453.

Robert, J. L. R., & Sangseok, Y. (2018). Emotional attachment, performance, and viability in teams collaborating with embodied physical action (EPA) robots. Journal of the Association for Information Systems, 19(5), 377-407.

Rosenberg-Kima, R. B., Baylor, A. L., Plant, E. A., & Doerr, C. E. (2008). Interface agents as social models for female students: The effects of agent visual presence and appearance on female students’ attitudes and beliefs. Computers in Human Behavior, 24(6), 2741-2756.

Rosenthal-von der Pütten, A. M., & Krämer, N. C. (2014). How design characteristics of robots determine evaluation and uncanny valley related responses. Computers in Human Behavior, 36, 422-439.

Rosenthal-von der Pütten, A. M., Straßmann, C., & Krämer, N. C. (2018). Dominant and submissive nonverbal behavior of virtual agents and its effects on evaluation and negotiation outcome in different age groups. Computers in Human Behavior, 90, 397-409.

Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. The American Psychologist, 55(1), 68-78.

Rzepka, C., & Berger, B. (2018). User interaction with AI-enabled systems: A systematic review of is research. Proceedings of the International Conference on Information Systems.

Saerbeck, M., Schut, T., Bartneck, C., & Janse, M. D. (2010). Expressive robots in education: Varying the degree of social supportive behavior of a robotic tutor. Proceedings of the ACM CHI Conference on Human Factors in Computing

Systems.

Saffarizadeh, K., Boodraj, M., & Alashoor, T. M. (2017). Conversational assistants: Investigating privacy concerns, trust, and self-disclosure. Proceedings of the International Conference on Information Systems.

Sakamoto, D., Kanda, T., Ono, T., Kamashima, M., Imai, M., & Ishiguro, H. (2005). Cooperative embodied communication emerged by interactive humanoid robots. International Journal of Human Computer Studies, 62(2), 247-265.

Sangseok, Y., & Lionel, P. R. J. (2019). Subgroup formation in human-robot teams. Proceedings of the International Conference on Information Systems.

Schlesinger, A., Hara, K. P. O., & Taylor, A. S. (2018). Let’s talk about race: Identity, chatbots, and AI. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Schroeder, J., & Schroeder, M. (2018). Trusting in machines: How mode of interaction affects willingness to share personal information with machines. Proceedings of the Hawaii International Conference on System Sciences.

Schuetz, S., & Venkatesh, V. (2020). The rise of human machines: How cognitive computing systems challenge assumptions of user-system interaction. Journal of the Association for Information Systems, 21(2), 460-482.

Schuetzler, R. M., Giboney, J. S., Grimes, G. M., & Nunamaker, J. F. (2018). The influence of conversational agents on socially desirable responding. In Proceedings of the Hawaii International Conference on System Sciences.

Schuetzler, R. M., Grimes, G. M., Giboney, J. S., & Buckman, J. (2014). Facilitating natural conversational agent interactions: Lessons from a deception experiment. Proceedings of the International Conference on Information Systems.

Sebastian, J., & Richards, D. (2017). Changing stigmatizing attitudes to mental health via education and contact with embodied conversational agents. Computers in Human Behavior, 73, 479-488.

Seeber, I., Bittner, E., Briggs, R. O., de Vreede, T., de Vreede, G.-J., Elkins, A., … Söllner, M. (2019a). Machines as teammates: A research agenda on ai in team collaboration. Information & Management, 57(2), Article 103174.

Seeber, I., Waizenegger, L., Seidel, S., Morana, S., Benbasat, I., & Lowry, P. B. (2019b). Collaborating with technology-based autonomous

agents: Issues and research opportunities. Internet Research, 30(1), 1-18.

Seeger, A.-M., Pfeiffer, J., & Heinzl, A. (2017). When Do we need a human? Anthropomorphic design and trustworthiness of conversational agents. Proceedings of the Special Interest Group on Human-Computer Interaction.

Seeger, A.-M., Pfeiffer, J., & Heinzl, A. (2018). Designing anthropomorphic conversational agents: Development and empirical evaluation of a design framework. Proceedings of the International Conference on Information Systems.

Seering, J., Luria, M., Kaufman, G., & Hammer, J. (2019). Beyond dyadic interactions: Considering chatbots as community members. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Seymour, Michael, Riemer, K., & Kay, J. (2017). Interactive realistic digital avatars: Revisiting the uncanny valley. In Proceedings of the Hawaii International Conference on System Sciences.

Seymour, Mike, Riemer, K., & Kay, J. (2018). Actors, Avatars and agents: Potentials and implications of natural face technology for the creation of realistic visual presence. Journal of the Association for Information Systems, 19(10), 953-981.

Shah, H., Warwick, K., Vallverdú, J., & Wu, D. (2016). Can machines talk? Comparison of Eliza with modern dialogue systems. Computers in Human Behavior, 58(January), 278-295.

Shamekhi, A., Liao, Q. V., Wang, D., Bellamy, R. K. E., & Erickson, T. (2018). Face value? Exploring the effects of embodiment for a group facilitation agent. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Sohn, S. (2019). Can conversational user interfaces be harmful? the undesirable effects on privacy concern. Proceedings of the International Conference on Information Systems.

Son, Y., & Wonseok, O. (2018). “Alexa, buy me a movie!”: How AI speakers reshape digital content consumption and preference. Proceedings of the International Conference on Information Systems.

Stieglitz, S., Brachten, F., & Kissmer, T. (2018). Defining bots in an enterprise context. Proceedings of the International Conference on Information Systems.

Stock, R. M., & Merkle, M. (2018a). Can humanoid service robots perform better than service employees? A comparison of innovative behavior cues. Proceedings of the Hawaii International

Conference on System Sciences.

Stock, R. M., & Merkle, M. (2018b). Customer responses to robotic innovative behavior cues during the service encounter. Proceedings of the International Conference on Information Systems.

Stock, R., Merkle, M., Eidens, D., Hannig, M., Heineck, P., Nguyen, M. A., & Völker, J. (2019). understanding employee trust in assistive robots: When robots enter our workplace. Proceedings of the International Conference on Information Systems.

Stoeckli, E., Uebernickel, F., & Brenner, W. (2018). Exploring affordances of slack integrations and their actualization within enterprises: Towards an understanding of how chatbots create value. Proceedings of the Hawaii International Conference on System Sciences.

Strait, M., Vujovic, L., Floerke, V., Scheutz, M., & Urry, H. (2015). Too much humanness for human-robot interaction. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Straßmann, C., Pütten, A. M. R. Der, & Krämer, N. C. (2018). With or against each other? The influence of a virtual agent’s (non)cooperative behavior on user’s cooperation behavior in the prisoners dilemma. Advances in Human-Computer Interaction, 2018, Article 2589542.

Strohmann, T., Fischer, S., Siemon, D., Brachten, F., Lattemann, C., Robra-Bissantz, S., & Stieglitz, S. (2018). Virtual moderation assistance: creating design guidelines for virtual assistants supporting creative workshops. Proceedings of the Pacific Asia Conference on Information Systems.

Sugumaran, V., & Davis, K. (2001). A natural languagebased multi-agent system for legal research. Proceedings of the Americas Conference on Information Systems.

Szafir, D., & Mutlu, B. (2012). Pay attention! Designing adaptive agents that monitor and improve user engagement. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Tavanapour, N., Poser, M., & Bittner, E. A. C. (2019). Supporting the idea generation process in citizen participation: Toward an interactive system with a conversational agent. Proceedings of the European Conference on Information Systems.

Tickle-Degnen, L., & Rosenthal, R. (1990). The nature of rapport and its nonverbal correlates. Psychological Inquiry, 1(4), 285-293.

Tinwell, A., & Sloan, R. J. S. (2014). Children’s

perception of uncanny human-like virtual characters. Computers in Human Behavior, 36, 286-296.

Toxtli, C., Monroy-Hernández, A., & Cranshaw, J. (2018). Understanding chatbot-mediated task management. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Truong, A. (2016). Parents are worried the Amazon Echo is conditioning their kids to be rude. Quartz. https://qz.com/701521/parents-are-worried-theamazon-echo-is-conditioning-their-kids-to-berude/

Vaccaro, K., Agarwalla, T., Shivakumar, S., & Kumar, R. (2018). Designing the future of personal fashion experiences online. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Vaidyam, A. N., Wisniewski, H., Halamka, J. D., Kashavan, M. S., & Torous, J. B. (2019). Chatbots and conversational agents in mental health: A review of the psychiatric landscape. Canadian Journal of Psychiatry, 64(7), 456-464.

Van den Broeck, E., Zarouali, B., & Poels, K. (2019). Chatbot advertising effectiveness: When does the message get through? Computers in Human Behavior, 98, 150-157.

van der Meij, H. (2013). Motivating agents in software tutorials. Computers in Human Behavior, 29(3), 845-857.

Veletsianos, G., & Russell, G. S. (2014). Pedagogical agents. In J. M. Spector, M. D. Merrill, J. Elen, & M. J. Bishop (Eds.), Handbook of Research on Educational Communications and Technology (4th ed., pp. 759-769). Springer.

Venkatesh, V., Morris, M., Davis, G., & Davis, F. (2003). User acceptance of information technology: toward a unified view. MIS Quarterly, 27(3), 425-478.

Vertegaal, R., Slagter, R., van der Veer, G., & Nijholt, A. (2000). Why conversational agents should catch the eye. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Vertegaal, R., Slagter, R., van der Veer, G., & Nijholt, A. (2001). Eye gaze patterns in conversations. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Vogel-Meijer, K. (2018). KLM: Making airline customer service soar with Messenger. Facebook. https://www.facebook.com/business/ success/klm-messenger

vom Brocke, J., Simons, A., Niehaves, B., Riemer, K., Plattfaut, R., & Cleven, A. (2009). Reconstructing the giant: On the importance of rigour in documenting the literature search process. Proceedings of the European Conference on Information Systems.

Vtyurina, A., & Fourney, A. (2018). Exploring the role of conversational cues in guided task support with virtual assistants. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Vugt, H. C. Van, Bailenson, J. N., Hoorn, J. F., & Konijn, E. A. (2010). Effects of facial similarity on user responses to embodied agents. ACM Transactions on Computer-Human Interaction, 17(2), Article 7.

Wagner, K., & Schramm-Klein, H. (2019). Alexa, are you human? Investigating the anthropomorphism of digital voice assistants - A qualitative approach. Proceedings of the International Conference on Information Systems.

Wakefield, J. (2016). Would you want to talk to a machine? BBC. https://www.bbc.com/news/ technology-36225980

Wang, N., Johnson, W. L., Mayer, R. E., Rizzo, P., Shaw, E., & Collins, H. (2008). The politeness effect: Pedagogical agents and learning outcomes. International Journal of Human Computer Studies, 66(2), 98-112.

Wang, W., & Benbasat, I. (2005). Trust in and adoption of online recommendation agents. Journal of the Association for Information Systems, 6(3), 72- 101.

Ward, N., & Tsukahara, W. (2003). A study in responsiveness in spoken dialog. International Journal of Human Computer Studies, 59(5), 603- 630.

Watanabe, M., Ogawa, K., & Ishiguro, H. (2015). Can androids be salespeople in the real world? Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Webster, J., & Watson, R. T. (2002). Analyzing the past to prepare for the future: Writing a literature review. MIS Quarterly, 26(2), xiii-xxiii.

Weizenbaum, J. (1966). ELIZA: A computer program for the study of natural language communication between man and machine. Communications of the ACM, 9(1), 36-45.

Welch, C. (2018). Google just gave a stunning demo of assistant making an actual phone call. The Verge. https://www.theverge.com/2018/5/8/ 17332070/google-assistant-makes-phone-calldemo-duplex-io-2018

Wik, P., & Hjalmarsson, A. (2009). Embodied conversational agents in computer assisted language learning. Speech Communication, 51(10), 1024-1037.

Winkler, R., Bittner, E., & Söllner, M. (2019). Hey Alexa, please help us solve this problem ! how interactions with smart personal assistants improve group performance. Proceedings of the International Conference on Information Systems.

Winkler, R., & Roos, J. (2019). Bringing AI into the classroom: Designing smart personal assistants as learning tutors. Proceedings of the International Conference on Information Systems.

Winkler, R., Söllner, M., Neuweiler, M. L., Conti Rossini, F., & Leimeister, J. M. (2019). Alexa, can you help us solve this problem? Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Wolff, R. M. Von, Hobert, S., & Schumann, M. (2019). How may i help you ? State of the art and open research questions for chatbots at the digital workplace. Proceedings of the Hawaii International Conference on System Sciences.

Wünderlich, N. V., & Paluch, S. (2017). A nice and friendly chat with a bot: User perceptions of AIbased service agents. Proceedings of the International Conference on Information Systems.

Xu, A., Liu, Z., Guo, Y., Sinha, V., & Akkiraju, R. (2017). A new chatbot for customer service on social media. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Xu, K., & Lombard, M. (2017). Persuasive computing: Feeling peer pressure from multiple computer agents. Computers in Human Behavior, 74, 152- 162.

Xu, Q., Li, L., & Wang, G. (2013). Designing engagement-aware agents for multiparty conversations. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Yamada, S., Terada, K., Kobayashi, K., Komatsu, T.,

Funakoshi, K., & Nakano, M. (2013). Expressing a robot’s confidence with motion-based artificial subtle expressions. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Yang, Y., Ma, X., & Fung, P. (2017). Perceived emotional intelligence in virtual agents. Proceedings of the ACM CHI Conference on Human Factors in Computing Systems.

Yokotani, K., Takagi, G., & Wakashima, K. (2018). Advantages of virtual agents over clinical psychologists during comprehensive mental health interviews using a mixed methods design. Computers in Human Behavior, 85, 135-145.

Zhang, P., Benbasat, I., Carey, J., Davis, F., Galletta, D. F., & Strong, D. (2002). Human-computer interaction research in the MIS discipline. Communications of the Association for Information Systems, 9, 344-355.

Zhang, P., & Li, N. (2004). An assessment of human - computer interaction research in management information systems: Topics and methods. Computers in Human Behavior, 20, 125-147.

Zhang, P., & Li, N. (2005). The intellectual development of human-computer interaction research: A critical assessment of the MIS literature (1990-2002). Journal of the Association for Information Systems, 6(11), 227-292.

Zhang, P., Li, N., Scialdone, M., & Carey, J. (2008). The intellectual advancement of human-computer interaction research: A critical assessment of the MIS literature (1990-2008). AIS Transactions on Human-Computer Interaction, 1(3), 55-107.

Zhang, Y., Song, W., Tan, Z., Zhu, H., Wang, Y., Lam, C. M., … Yi, L. (2019). Could social robots facilitate children with autism spectrum disorders in learning distrust and deception? Computers in Human Behavior, 98, 140-149.

Zierau, N., Engel, C., Söllner, M., & Leimeister, J. M. (2020). Trust in smart personal assistants: A systematic literature review and development of a research agenda. Proceedings of the International Conference on Wirtschaftsinformatik.

## Appendix A: Coding Guidelines

Table A1. Coding Guidelines

<table><tr><td colspan="2">Human</td></tr><tr><td>Age</td><td>Did the study collect and analyze the users' age (was it explicitly analyzed or discussed in-depth independent of the analysis results)?</td></tr><tr><td>Gender</td><td>Did the study collect and analyze the users' gender (was it explicitly analyzed or discussed in-depth independent of the analysis results)?</td></tr><tr><td>Education</td><td>Did the study collect and analyze the users' education (was it explicitly analyzed or discussed in-depth independent of the analysis results)?</td></tr><tr><td>Cultural background</td><td>Did the study collect and analyze the users' cultural background (e.g., ethnicity or nationality); (was it explicitly analyzed or discussed in-depth independent of the analysis results)?</td></tr><tr><td>CA experience</td><td>Did the study collect data on individual user experience with CAs or digital assistants and analyze it? Did researchers explicitly analyze or discuss the data in depth, independent of the analysis results?</td></tr><tr><td>Task experience</td><td>Did the study collect data on individual user experience with the task at hand collected and analyzed? Did researchers explicitly analyze or discuss the data in depth, independent of the analysis results?</td></tr><tr><td>Personality</td><td>Did the study collect data on user personality (e.g., introversion or neuroticism) and analyze it? Did researchers explicitly analyze or discuss the data in depth, independent of the analysis results?</td></tr><tr><td>Cognitive style</td><td>Was data on user's cognitive style (e.g., learning style) gathered and analyze (was it explicitly analyzed or discussed in-depth independent of the analysis result?</td></tr><tr><td colspan="2">Context</td></tr><tr><td>Professional task support</td><td>CAs for individual task support in a company context (e.g., the CA as a personal assistant, for information search (FAQ), or data analytics).</td></tr><tr><td>Team collaboration</td><td>CAs in professional team settings (e.g., as a moderator in meetings or for shared task management).</td></tr><tr><td>Customer interface</td><td>CAs at the customer interface (e.g., for service provision or as an additional sales channel).</td></tr><tr><td>Private task support</td><td>CAs for individual task support (e.g., in-car assistants or for personal time management).</td></tr><tr><td>Health</td><td>CAs for individual health (e.g., to promote health awareness or to provide initial, individual diagnosis).</td></tr><tr><td>Education</td><td>CAs for education (e.g., as intelligent tutoring systems).</td></tr><tr><td>Multiple</td><td>Studies that address multiple contexts.</td></tr><tr><td>Generic</td><td>Studies that do not define a specific context for the CA.</td></tr><tr><td>Other</td><td>CAs that do not fit any of the above contexts.</td></tr><tr><td colspan="2">Agent</td></tr><tr><td>Communication mode</td><td>Did the study investigate the CA's communication mode, that is, was it included in the analysis and discussed afterward?</td></tr><tr><td>Embodiment</td><td>Did the study investigate the CA's embodiment, that is, was it included in the analysis and discussed afterward?</td></tr><tr><td>(Human) identity</td><td>Did the study investigate the CA's (human) identity, that is, was it included in the analysis and discussed afterward?</td></tr><tr><td>Verbal communication</td><td>Did the study investigate the CA's verbal communication, that is, was it included in the analysis and discussed afterward?</td></tr><tr><td>Nonverbal communication</td><td>Did the study investigate the CA's nonverbal communication, that is, was it included in the analysis and discussed afterward?</td></tr><tr><td colspan="2">Perceptions and outcomes</td></tr><tr><td>Perception</td><td>Humanness, social presence, competence, authority</td></tr><tr><td>Acceptance</td><td>Use, intention to use, acceptance, resistance to use</td></tr><tr><td>Attitude</td><td>Attitude, satisfaction, preference</td></tr><tr><td>Performance</td><td>Productivity, effectiveness, efficiency</td></tr><tr><td>Emotion</td><td>Affect, hedonic quality, enjoyment, humor, intrinsic motivation</td></tr><tr><td>Trust</td><td>Trust, risk, loyalty, security, privacy</td></tr><tr><td>Learning</td><td>Learning models, learning processes, general training</td></tr><tr><td>Ethics</td><td>Ethical belief, ethical behavior, ethics</td></tr><tr><td>Relationship</td><td>Influence, interdependence, interference, agreement/disagreement, persuasiveness</td></tr><tr><td>Other</td><td>Further topics not included in the list</td></tr><tr><td colspan="2">Complementary</td></tr><tr><td>Article type</td><td>Is the article research in progress/a short paper, or is it completed research/a full paper?</td></tr><tr><td>Research approach</td><td>Is the study conceptual or empirical? Studies where, for example, conceptual frameworks are developed and empirically tested are coded as empirical.</td></tr><tr><td>Research method</td><td>What method was used in the study? For multimethod studies, the “primary” method is coded.</td></tr><tr><td>Unit of analysis</td><td>On what level of analysis was the study conducted?</td></tr><tr><td>Theoretical grounding</td><td>Which theories or research backgrounds were used in the study?</td></tr></table>

## Appendix B: Cluster Analysis

Table B1. Agglomeration Schedule (last ten steps)

<table><tr><td rowspan="2">Step</td><td colspan="2">Consolidated cluster</td><td rowspan="2">Coefficient</td><td colspan="2">First appearance</td><td rowspan="2">Next step</td><td rowspan="2">Coefficient delta</td><td rowspan="2">Cluster #</td></tr><tr><td>Cluster 1</td><td>Cluster 2</td><td>Cluster 1</td><td>Cluster 2</td></tr><tr><td>252</td><td>2</td><td>7</td><td>677.279</td><td>245</td><td>225</td><td>256</td><td>15.007</td><td>10</td></tr><tr><td>253</td><td>8</td><td>9</td><td>695.607</td><td>237</td><td>247</td><td>254</td><td>18.328</td><td>9</td></tr><tr><td>254</td><td>8</td><td>15</td><td>715.616</td><td>253</td><td>239</td><td>258</td><td>20.009</td><td>8</td></tr><tr><td>255</td><td>1</td><td>3</td><td>735.667</td><td>250</td><td>243</td><td>259</td><td>20.051</td><td>7</td></tr><tr><td>256</td><td>2</td><td>4</td><td>756.878</td><td>252</td><td>230</td><td>259</td><td>21.211</td><td>6</td></tr><tr><td>257</td><td>5</td><td>19</td><td>787.31</td><td>251</td><td>240</td><td>260</td><td>30.432</td><td>5</td></tr><tr><td>258</td><td>8</td><td>16</td><td>820.058</td><td>254</td><td>248</td><td>260</td><td>32.748</td><td>4</td></tr><tr><td>259</td><td>1</td><td>2</td><td>882.41</td><td>255</td><td>256</td><td>261</td><td>62.352</td><td>3</td></tr><tr><td>260</td><td>5</td><td>8</td><td>967.224</td><td>257</td><td>258</td><td>261</td><td>84.814</td><td>2</td></tr><tr><td>261</td><td>1</td><td>5</td><td>1063.046</td><td>259</td><td>260</td><td>0</td><td>95.822</td><td>1</td></tr></table>

Coefficients  
![](/api/attachments/FJARTSNG/fulltext/images/e0dbb5123d544d7da7e997e5a80e2774deef78a04682d77a6ab8120bf0ca2d8b.jpg)  
Figure B1. Scree Diagram (last ten steps)

## Appendix C: Studies over Time

![](/api/attachments/FJARTSNG/fulltext/images/f8a790b6bb8978bd99c4f3a40602803327589aa3791e5773454a115ddae2606e.jpg)  
Figure C1. Studies over Time by Discipline

![](/api/attachments/FJARTSNG/fulltext/images/b9db1867a7109fcb1abe2058fdff1a0d52897653389b338fcb3caf46c05ee962.jpg)  
Figure C2. Studies over Time by Research Stream (Cluster)

## About the Authors

Stephan Diederich is a former research associate at the Chair of Information Management of the University of Göttingen and a senior consultant at a large management consultancy concentrating on the digital transformation of organizations. His research focuses on conversational agents, in particular chatbots, within an organizational context, and has been published in journals such as Business and Information Systems Engineering and AIS Transactions on Human-Computer Interaction, as well as in IS conference proceedings such as the International Conference on Information Systems and the European Conference on Information Systems.

Alfred Benedikt Brendel is an associate professor of business information systems, esp. intelligent systems and services, at the Technische Universität Dresden, Germany. His research is concerned with the design of information systems in the domains of healthcare, transportation, and the digital workplace. Particularly, he focuses his research on understanding the effects human-like design information systems have on users. Alfred’s research has been published or is forthcoming in leading IS journals, such as Journal of Information Technology, Business & Information System Engineering, Information Systems Frontiers, and AIS Transactions on Human-Computer Interaction.

Stefan Morana is a junior professor of digital transformation and information systems at Saarland University. His research focuses on the human-centered design of interactive systems for digital transformation from the perspective of the individual, organizations, and society. More specifically, he investigates the design of assistant systems and conversational interfaces supporting the individual usage of information systems. His research has been published in journals such as the Journal of the Association for Information Systems, Decision Support Systems, International Journal of Human-Computer Studies, Business & Information Systems Engineering, Internet Research, AIS Transactions on Human-Computer Interaction, Communications of the Association for Information System, and in the proceedings of major information systems conferences.

Lutz Kolbe is a professor of information systems and leads the Chair of Information Management at the University of Göttingen. His research focuses on the management of information and information technology as a crucial factor for sustainable business success. Lutz manages the research and project activities of three groups covering the areas of digital transformation, digital health, and smart mobility. His publications have appeared in several IS journals and conferences, such as European Journal of Information Systems, Journal of the Association for Information Systems, and Information Systems Journal.
