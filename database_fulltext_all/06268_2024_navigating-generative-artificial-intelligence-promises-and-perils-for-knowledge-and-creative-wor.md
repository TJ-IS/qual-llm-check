---
otero_id: 6268
otero_key: "2226VUGW"
title: "Navigating Generative Artificial Intelligence Promises and Perils for Knowledge and Creative Work"
authors: "Hind Benbya; Franz Strich; Toomas Tamm"
year: "2024"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00861"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
2024

# Navigating Gener ative Artificial Intelligence Pr  omises and P  erils for Knowledge and Creative Work

Hind Benbya , h.benbya@deakin.edu.au

Franz Strich , f.strich@deakin.edu.au

Toomas Tamm

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Navigating Generative Artificial Intelligence Promises and Perils for Knowledge and Creative Work

Hind Benbya,<sup>1</sup> Franz Strich,<sup>2</sup> Toomas Tamm<sup>3</sup>

<sup>1</sup>Centre for Artificial Intelligence and the Future of Business, Deakin University, Australia, h.benbya@deakin.edu.au <sup>2</sup>Centre for Artificial Intelligence and the Future of Business, Deakin University, Australia, f.strich@deakin.edu.au <sup>3</sup>Centre for Artificial Intelligence and the Future of Business, Deakin University, Australia, toomas.tamm@deakin.edu.au

## Abstract

Generative artificial intelligence (GenAI) is rapidly becoming a viable tool to enhance productivity and act as a catalyst for innovation across various sectors. Its ability to perform tasks that have traditionally required human judgment and creativity is transforming knowledge and creative work. Yet it also raises concerns and implications that could reshape the very landscape of knowledge and creative work. In this editorial, we undertake an in-depth examination of both the opportunities and challenges presented by GenAI for future IS research.

Keywords: Generative Artificial Intelligence, Creativity, Knowledge workers, knowledge management, Large Language Models, Research Agenda, Image Generation Models

Dorothy E. Leidner was the accepting editor. This editorial was submitted on October 15, 2023 and underwent one revision.

## 1 Introduction

Generative Artificial Intelligence (GenAI) broadly refers to a class of AI models that produce new content in the form of text, video, images, or other media in response to prompts. For example, GenAI systems can write convincing documents, create digital art, compose music, engage and debate with humans, and produce software. Although GenAI techniques have been around for some time (Benbya et al., 2020, 2021), the recent public release of tools such as ChatGPT, GitHub Copilot, and DALL-E followed by Google’s Bard and Microsoft’s Bing have brought the potential of such solutions to the forefront. Contemporary GenAI systems have attracted significant attention from diverse stakeholders and generated intense debates about GenAI impact on business and society.

GenAI ability to perform tasks that previously required human judgment and creativity has elicited discussions about the potential of this emerging technology to disrupt traditional roles and transform the way we work, its impact on the labor market, its economic implications, and its effects on employee productivity (Brynjolfsson et al., 2023, Noy & Zhang, 2023). But it also raised concerns about the potential legal and ethical challenges created by GenAI, such as copyright infringement in AI-generated art (Gillotte, 2019) data privacy and security (Siau & Wang, 2020), and malicious use of deepfakes (Vasist & Krishnan, 2022).

While GenAI has expanded the scope of tasks that AI tools can accomplish, its potential impact is perceived to be more significant for knowledge<sup>1</sup> and creative<sup>2</sup> work.

Recent studies estimate that GenAI (e.g., large language models) will affect several information-intensive tasks of about 80% of all workers, with a smaller subset of knowledge-intensive workers seeing most of their tasks impacted (Eloundou et al., 2023). Early studies suggest that rather than replacing jobs, the potential of GenAI lies in supporting workers by performing certain timeconsuming tasks, thereby improving business processes and enabling the creation of new products and services. Preliminary evidence also suggests that GenAI is likely to benefit novices and less skilled workers (Noy & Zhang, 2023).

GenAI models like GPT-4<sup>3</sup> are also becoming capable of producing ideas that humans consider to be original, novel, and unique (Guzik et al., 2023). The increasing ability of GenAI systems to carry out creative tasks has raised questions about the future of creative industries and the potential threat of substitution for creative workers (Huhn, 2022; Wolff, 2022). In addition, as such tools enter creative domains, they prompt inquiries regarding whether and to what extent such tools can meet human creativity across several settings (Stevenson et al., 2022).

As GenAI has the potential to significantly alter knowledge and creative work, this article uses two complementary perspectives to explore the multifaceted opportunities and challenges of GenAI for knowledge and creative work and the implications for future IS research. Knowledge and creative work share many similarities. For example, creative workers require an understanding of various forms of knowledge (Loo, 2017), and creativity is a distinctive and dominant feature of knowledge work (Frenkel et al. 1995), which also entails many creative processes. We explore how GenAI transforms knowledge work in terms of four organizational capabilities: knowledge creation, knowledge retrieval, knowledge sharing, and knowledge application. Furthermore, since GenAI is expanding the scope of creative tasks that can be carried out with AI tools and introduces new transformational capabilities, we discuss the effects of GenAI on creative work in terms of three capabilities: creativity automation, modal conversion, and machine creativity.

## 2 Generative AI: A Primer on Large Language and Image Generation Models

This section provides a brief overview of GenAI models with an emphasis on large language models (LLMs) and image generation models including generative adversarial networks because they are particularly relevant to the context of knowledge and creative work.

## 2.1 Large Language Models

Although the origin of language models can be traced back to early development in natural language processing (NLP) in the 1950s, it is mostly advancements in transformer architecture that enabled the creation of larger LLMs which served as the foundation for ChatGPT and other generative AI language models.

LLMs are neural network models with billions of parameters that rely on a transformer architecture to generate new content in every new trial, even those that use the same prompts (Vaswani et al., 2017). Such architecture enables a high degree of parallelization, which allows the model to train on much larger datasets than before, retain exponentially more parameters, and capture long-range dependencies in the data to thereby intelligently comprehend language contexts.

## 2.2 Image Generation Models

Image generation models are deep learning models that can generate images from text prompts. Early models began to be developed in the mid-2010s, with notable advancements made by generative adversarial networks and variational autoencoders, which reconstruct images from sampled white noise. More recent advancements include GenAI based in diffusion models, a class of generative models inspired by thermodynamics that adopt a unique approach to image generation by gradually adding noise to an image until it becomes completely degraded (Ho et al., 2020).

## 3 GenAI Implications for Knowledge Work

The ability to train GenAI models on an organization’s existing knowledge offers an opportunity to harness the extensive collective expertise shared among employees as well as insights from customers and stakeholders. GenAI can assist in extracting, analyzing, and sharing knowledge from structured and unstructured data sources alike, such as proprietary documents, emails, instant messages, videos, and meetings. As such, this emerging technology offers new opportunities to recombine and leverage a company’s knowledge assets and transform knowledge work. We explore the opportunities of GenAI and the tensions it raises for knowledge work in terms of four capabilities: knowledge creation, knowledge retrieval, knowledge sharing, and knowledge application.

## 3.1 Knowledge Creation

The use of GenAI for knowledge creation holds valuable opportunities for organizations. First, the adoption of GenAI enables organizations to process diverse unstructured and structured data sources to uncover hidden patterns, relationships, and insights within these communication channels. For instance, GenAI can automatically create meeting notes with realtime transcription, provide meeting summaries, or extract information from videos. Existing tools such as Otter, Supernormal, or Colibri can be used in conjunction with online collaboration tools such as MS Teams or Zoom to process and analyze every spoken word. Notably, extracted tacit knowledge can be reintegrated into existing feedback loops, enabling the AI model to continuously learn and reducing the need for human-in-the-loop processes (Brea & Ford, 2023). GenAI can identify insights not readily apparent to human decision makers to serve as stimuli for novel ideas, encouraging employees to explore new avenues and innovations (Brea & Ford, 2023; Haefner et al., 2021). For instance, in the pharmaceutical and material science industry, GenAI can be used to analyze data from scientific literature, patents, and databases, and propose new chemical compounds or materials with desirable properties (Lee et al., 2023; Ni et al., 2023). Processes known as de novo molecular design can accelerate the R&D process by suggesting potential candidate molecules, which researchers can then synthesize and evaluate, leading to the discovery and creation of innovative solutions.

However, the use of GenAI for knowledge creation also triggers several tensions. An organization’s use of previously accumulated knowledge may introduce the risk of carrying forward knowledge artifacts, which could negatively impact the value of newly created content. For example, organizations risk (1) rolling over outdated practices, (2) using circular arguments that lead to innovation stagnation, or (3) creating misleading information. Thus, GenAI’s reliance on previous data as a foundation for knowledge creation could paradoxically act as a barrier to innovative thought that aspires to break free from the past. This could foster an environment where GenAI’s output echoes the limitations of its inputs.

To outline current GenAI systems’ limitations, OpenAI openly issued a warning that GenAI “sometimes writes plausible sounding but incorrect or nonsensical answers” (OpenAI, 2023), a phenomenon also known as hallucination. The inability to verify knowledge produced by GenAI might contribute to misinformation and distortion in decision-making (Deng & Lin, 2023; Doss et al., 2023). Finally, GenAI is unable to codify the context in which knowledge exists or to fully extract subjective experiences. Consequently, organizations risk diluting tacit knowledge into less useful or even misleading forms of explicit information.

The use of GenAI for knowledge creation offers several opportunities for future research. Table 1 provides an overview of our knowledge research questions (KRQs). First, based on GenAI’s promising ability to capture organizations’ tacit knowledge and synthesize explicit knowledge, GenAI may decrease the frequency and quality of human-human interactions, leading to negative implications for the generation and development of tacit knowledge within organizations in the long run (KRQ1). Second, the continuous interplay of AI-generated knowledge and human expertise necessitates a deeper understanding of self-inferring feedback loops and the mechanisms through which tacit knowledge emerges from GenAI interactions (KRQ2). By exploring the potential of GenAI to dynamically curate tacit or explicit knowledge creation, future research can shed light on the opportunities and potential dark sides in the evolving landscape of knowledge management.

## 3.2 Knowledge Retrieval

The automated, systematic, and intelligent processing of varying data sources offers considerable benefits for employees’ knowledge retrieval. First, GenAI can assist organizations with the codification and transformation of tacit knowledge into explicit knowledge (Jarrahi et al., 2023a). For instance, through NLP and interactive dialogue, GenAI can preserve tacit knowledge in a format that can be easily accessed and shared. Moreover, while most LLMs currently cannot produce or reproduce technically versatile knowledge, LLMs are increasingly being released that are trained on smaller high-quality datasets to provide domain-specific and accurate knowledge. Promising examples include the AI research assistants Elicit and Scite as well as powerful open source LLMs such as BLOOM (176Bparameters) and Falcon (180B-parameters). Moreover, GenAI’s advanced processing and understanding of natural language queries is likely to provide more precise search results in the future. GenAI’s abilities will increasingly correspond to the capabilities of a human listener, overcoming previous constraints of algorithmic interactions (Jarrahi 2023b; Tarafdar et al., 2023). Moreover, based on the query’s sentiment, GenAI can provide suggestions on related subjects or topics to consider, providing a more holistic and efficient approach to knowledge retrieval.

However, knowledge retrieval can also be associated with security and data breach threats resulting in huge financial and reputational losses for organizations. With GenAI’s advanced understanding of natural language inquiries, users could exploit or trick GenAI to access privileged information (Renaud et al., 2023). Just as social engineering impersonates colleagues to access organizations’ sensitive information, employees could trick the GenAI logic-based understanding of formalized rules to access privileged information. A prominent example of users exploiting GenAI includes the use of DAN (Do Anything Now) to overcome GenAI’s moral and ethical implications (Taylor, 2023). By tricking the chatbot, users were able to create discriminatory and offensive content.

Moreover, the deployment of GenAI for knowledge work also presents significant challenges concerning data privacy. Italy’s temporary ban on the use of ChatGPT highlights the growing unease surrounding the potential implications of GenAI on data privacy and security (Hacker et al., 2023). Users may inadvertently share sensitive information with the GenAI system, which is subsequently stored and potentially reintegrated into the knowledge base of a third-party’s system (Renaud et al., 2023). Consequently, companies such as Samsung, Deutsche Bank AG, Verizon, JP Morgan, and others have banned the use of GenAI (Gurman, 2023; Lukpat, 2023; Mello et al., 2023). Notably, even if knowledge could potentially stay within the organization through the use of company-tailored GenAI models, it may become accessible to other users of the same system through iterative feedback loops. Departments handling sensitive information, such as HR and R&D, may also face unique challenges when integrating GenAI into their knowledge management processes (Vrontis et al., 2022). For example, HR departments managing employee personal data must ensure compliance with data protection regulations, such as the GDPR in the EU, and prevent unauthorized access or the disclosure of confidential information (Forrest, 2023; Hacker et al., 2023).

The realm of GenAI offers numerous prospects for future research. First, current GenAI systems often rely on local search routines, wherein the precision of the information request is of great importance. Analogous to search engine optimization, a field dedicated to AIenhanced information retrieval could emerge, which would focus on optimizing the accessibility and discoverability of knowledge within GenAI-driven systems (KRQ3).

## 3.3 Knowledge Sharing

Beyond knowledge creation and retrieval, GenAI’s potential lies in answering employee queries and providing personalized feedback which would enable knowledge sharing and foster tailored learning experiences. Moreover, GenAI has the potential to revolutionize the way that employees change their career fields and tasks by making it easier for them to acquire new skills and knowledge (Lim et al., 2023). By enhancing the permeability between different roles and industries, GenAI can help address labor shortages and promote a more adaptable workforce (Brynjolfsson et al., 2023). This encompasses a range of adjustments, such as modifying the learning pace and tailoring the complexity of the content to accommodate each learner’s distinct needs (auditive vs. visual representation of learning content). For instance, Khan Academy recently announced the introduction of its GenAI, Khanmigo, to provide oneto-one interactive tutoring for all its students (Kahn, 2023), enabling a personalized learning environment that traditional learning institutions will find hard to match. Notably, GenAI’s value also extends beyond individual learning by supporting organizations in mapping out intricate networks of expertise to uncover valuable but overlooked pieces of information and suggesting where they might be applied. Thus, organizations are increasingly deploying GenAI agents as an invaluable asset for knowledge sharing to redistribute information among employees internally (Olan et al., 2022).

However, despite the ability of GenAI models to understand patterns and relationships within large datasets, such models may struggle to fully grasp the context or intricacies of unique technical or legal constraints within a specific project or industry. Organizational knowledge sharing requires a nuanced understanding of the operational contexts, which is highly important for effective decision-making and strategic planning. The challenge of context inclusion in AI intensifies with complex path dependencies, as it must comprehend both the current situation and the impact of past decisions. Consequently, there is a risk that GenAI may not sufficiently account for contextual factors, leading to the sharing of knowledge that is accurate in its data representation but misaligned with context-specific applicability. Finally, there is a risk that employees may become overly reliant on AIgenerated content for knowledge sharing, sidelining human expertise and insights (Giermindl et al., 2022). This overreliance can lead to a loss of valuable human input, which is crucial to navigating complex situations and addressing novel problems.

The emergence of GenAI introduces several areas of inquiry in the context of knowledge sharing. First, future research could investigate the extent to which GenAI can be employed to streamline the knowledge sharing process between individuals, particularly for new hires navigating professional landscapes. GenAI has the potential to significantly enhance the exchange of insights and expertise among employees and bolster the fluidity and flexibility of employees across various functions (KRQ4). Second, the use of GenAI for knowledge sharing will flatten knowledge hierarchies and make specialized expertise more widely accessible to employees. The exclusive positions held by highly specialized knowledge workers and managers as information gatekeepers will be potentially democratized, allowing for broader knowledge distribution (KRQ5).

Table 1. Research Avenues for GenAI and Knowledge Work

<table><tr><td>Capability</td><td>Theme</td><td>RQ #</td><td>Research questions</td></tr><tr><td>Knowledge creation</td><td>Social interactions</td><td>KRQ1</td><td>How does GenAI affect knowledge workers&#x27; quality and quantity of social relationships and processes?Which routines/processes will knowledge workers engage in once they substitute their colleagues with GenAI for knowledge transmission?How does the use of GenAI transform organizations&#x27; social fabric relating to colleagues and team dynamics and their social interactions?</td></tr><tr><td></td><td>Tacit knowledge</td><td>KRQ2</td><td>What are organizational shifts in producing, codifying, and generating explicit and tacit knowledge when using GenAI?How can employees derive tacit knowledge from codified explicit knowledge created by GenAI?How can the dangers of self-inferring feedback loops created by GenAI be mitigated?</td></tr><tr><td>Knowledge retrieval</td><td>Prompt engineering</td><td>KRQ3</td><td>What skills will be necessary for leveraging GenAI&#x27;s potential and how can these skills be acquired?Which future input forms for GenAI will be available (speech, etc.) and how will that affect users?</td></tr><tr><td>Knowledge sharing</td><td>Adaptive learning</td><td>KRQ4</td><td>How can GenAI bridge career paths?To what extent can GenAI tackle labor shortage by retraining employees?How do domain-specific differences affect employees&#x27; permeability between industries as a consequence of GenAI-induced retraining?</td></tr><tr><td></td><td>Information gatekeepers</td><td>KRQ5</td><td>How does GenAI affect the specialized role of knowledge workers and (middle) managers as information gatekeepers?How can organizations manage the shift in power dynamics resulting from equal access to information across hierarchies?</td></tr><tr><td>Knowledge application</td><td>Occupational identity</td><td>KRQ6</td><td>How does GenAI transform employee&#x27;s occupational identity?Which mechanisms do employees use to protect their identities?How will GenAI and potential reputational losses affect employees&#x27; need for social recognition inside and outside the organizational settings?</td></tr><tr><td></td><td>Ethical framework</td><td>KRQ7</td><td>To what extent do organizations try to shift responsibility for content generated by AI to an individual level?How does GenAI challenge traditional notions of ownership and accountability when decisions are based on knowledge generated from AI systems?What are the pillars for developing comprehensive ethical frameworks to respond to the emerging demands of GenAI?</td></tr></table>

## 3.4 Knowledge Application

One of the most promising areas of GenAI is related to its potential contribution to employee productivity. Recent research highlights an improvement of more than 55% in performance and task accomplishment when utilizing GenAI (Ziegler et al., 2022). Furthermore, augmenting and automating processes allows employees with varying degrees of experience and knowledge skills to perform comparable tasks (Strich et al., 2021). Notably, low-skilled or novice workers especially seem to be positively impacted in their performance when using GenAI. For example, in coding, GenAI can assist less-experienced programmers in writing efficient and error-free code, while in banking, it can help novice financial analysts make accurate predictions and provide insightful recommendations (Brynjolfsson et al., 2023; Mayer et al., 2020).

However, with the advance of GenAI’s capability to augment or automate most codifiable work processes across a broad range of industries, employees may be challenged in their perception of their roles and their occupational identity (“Who am I?” and “What do I do?”) (Strich et al., 2021). Work roles grounded in explicit knowledge will lose prominence and require a fundamental shift, while positions grounded in tacit knowledge, often associated with understanding sentiment, will remain valuable in the future. Consequently, the importance of knowledge gatekeepers will drastically decline because GenAI reduces the need for human oversight in knowledge dissemination.

Knowledge application with GenAI points toward multiple promising avenues for future research. First, employees have traditionally relied on their expertise to apply knowledge across various organizational processes. With GenAI being increasingly embedded in knowledge-based tasks, it is imperative to understand its consequent effects on the work identities and roles of employees (KRQ6), including the interplay and interdependence of augmentation and automation (Raisch & Krakowski, 2021). Moreover, the application of AI-generated content for decisionmaking processes will potentially shift the responsibilities between users and GenAI, reducing ownership and accountability in decision outcomes for managers and employees. Therefore, future research needs to provide ethical frameworks to account for GenAI’s transformative capabilities in knowledge application (KRQ7).

## 4 GenAI and Creative Work

While GenAI enables the creation of new knowledge it has also expanded the scope of creative tasks that can be carried out with AI tools. GenAI systems are increasingly capable of providing final creative artifacts with little or no human intervention and, in some cases, are reaching parity with, or even surpassing, human creative performance. These developments raise many new possibilities, challenges, and questions regarding new forms of machine creativity, the automation of creative tasks, and the ability to convert between different types of creative media (e.g., from text to image).

## 4.1 Machine Creativity

The first transformative GenAI capability, from which GenAI derives its name, is at the very core of this technology—the ability to generate (i.e., create) new content. Although the concept and pursuit of machine creativity is not new (e.g., Boden, 1998), the increasing uptake and evolution of GenAI raises new possibilities and questions with regard to: (1) the characteristics and features of machine creativity, (2) the measurement of machine creativity, and (3) machine creativity techniques.

## 4.1.1 Characteristics and Features of Machine Creativity

The new possibilities of GenAI raise questions surrounding the emerging types and characteristics of machine creativity (CRQ1). These creativity-based research questions (CRQs) are summarized in Table 2. There is a need to understand the emerging forms of machine creativity and their practical applications. Related and somewhat more philosophical questions include whether the characteristics of machine creativity are any different from those of human creativity and whether machines can be “truly” creative in the same (or similar) sense as humans (e.g., Miller, 2020).

These human-machine comparisons may also lead to a better understanding of both human and machine creativity, and, in turn, help inform how to improve both (e.g., Bown, 2012). Although the creative outputs of machines and humans may be increasingly indistinguishable (Elgammal, 2019), there are fundamental differences between the creative processes that need to be followed to obtain these outputs. Research on GenAI may therefore provide useful insights for refining human creative processes and vice versa.

## 4.1.2 Measurement of Machine Creativity

Another important issue is how machine creativity can be assessed and measured (CRQ2). Building on prior studies on measures of human creative outputs (e.g., Dean et al., 2006) and how creativity support systems help improve such outputs (e.g., Wierenga & van Bruggen, 1998), future studies could explore the extent to which the measures of machine creativity converge with measures of human creativity and whether creative outputs generated by machines should be measured and appraised differently from those created by humans.

A closely related question is whether humans do (and should) differentiate between human and machine creative outputs. For example, some emerging studies on generative artworks suggest that humans prefer human paintings over artificial ones when they know their origins (e.g., Chiarella et al., 2022). Others suggest a painting’s origins do not affect the evaluation of its artistic value (e.g., Hong & Curran, 2019), and that humans often cannot even differentiate between the two (e.g., Elgammal, 2019). This raises interesting questions about the underlying reasons behind such discrepancies (e.g., system performance, the type of creative product, or other contextual factors). Overall, it appears that AI-generated creative ideas are increasingly reaching parity with humans (Haase & Hanel, 2023). However, are humans more likely to continue to dominate certain creative endeavors?

## 4.1.3 Machine Creativity Techniques

Third, taking a more practice-oriented perspective, future research could help improve GenAI techniques (CRQ3). For example, such research could explore the relative effectiveness of different types of AI techniques (either individually or in combination) for various types of creative outputs (e.g., Lamb et al. [2017] developed a taxonomy of generative poetry techniques; Sun et al. [2019] explored the effectiveness of generative artificial networks for image creation). A related question is how to attain various forms of creativity or degrees of creative novelty from GenAI (e.g., Chemla–Romeu-Santos & Esling, 2022). This issue is perhaps particularly pertinent with ML approaches, as these learn from patterns in training data and may hence struggle at the more divergent and transformational end of the creativity spectrum (Boden, 1998).

Also, studies could more broadly explore the good practices for effective GenAI system design, potentially building on prior research on the design principles for creativity support systems (e.g., Avital & Te’eni, 2009; Elam & Mead, 1987). For example, an interesting question involves the interaction of art and science in designing creative machines (Miller, 2020). New use cases and capabilities of GenAI may warrant new practices for designing such systems (e.g., Pilcicki et al., 2022) and successfully embedding them in creative processes (e.g., Siemon et al., 2022). One promising research avenue might be to examine how the principles of human-centered AI (e.g., Koster et al., 2022; Oppermann et al., 2019; Shneiderman, 2020) could be used to guide GenAI development.

## 4.2 Creativity Automation

The second transformative GenAI capability (for which machine creativity acts as a prerequisite) is the automation of creative work. Systems such as ChatGPT, DALL-E, MidJourney, and others can produce usable creative outputs and products with minimal to no expert intervention. Guided by human inputs, GenAI systems can create award-winning paintings (Roose, 2022) and photographs (Grierson, 2023). As the technology matures, it seems that GenAI’s autonomous performance will reach and surpass humans on some creative tasks (Guzik et al., 2023). This emerging creativity automation capability may impact: (1) business models and organization of creative work, (2) creative skills and capabilities, (3) the equity and ethics of creative work, and (4) creative work processes and team dynamics.

## 4.2.1 Organization and Business Models

Creativity automation raises important questions around how it will affect the accessibility and viability of different creative professions, how it will change the roles and value distribution in creative supply chains, and which new creative business models it will enable or make unviable (CRQ4). For example, creative businesses with fully digital products or highly digitalized workflows (e.g., digital game creation), may at least initially be more susceptible to AI-based automation than those that have a strong physical dimension (e.g., handicraft).

It is also worth considering the organizational benefits of GenAI. For example, are the organizational benefits of GenAI similar to those of creativity support systems (e.g., Massetti, 1996) or does creativity automation lead to new kinds of benefits? For example, one factor that may be more pertinent to creativity automation is individual attitudes toward GenAI. Both consumer and creative expert perspectives should be considered. Consumer attitudes may directly affect the value of GenAI-based creative products. Expert attitudes may affect how such products are valued and perceived at a societal level, as well as the willingness of creative organizations to adopt and use GenAI in their work. Therefore, it would be useful for future research to examine how personal characteristics, experiences, context, and the nature of the creative task may affect such perceptions.

## 4.2.2 Creative Skills and Capabilities

Another important issue is the impact of creativity automation on organizational creativity, including whether it increases overall organizational creative capabilities (e.g., Mikalef & Gupta, 2021) and how it affects specific creative skills, capabilities, and functions (CRQ5). In some contexts, AI may negatively affect both human individuality and group performance (Fügener et al., 2021). It is therefore important to examine whether the extensive adoption of GenAI may deskill creative workers and affect their ability to produce or evaluate creative outputs, both at an individual and a team level. Such studies could also examine whether this impact varies depending on the creative task, individual, or team characteristics (e.g., expertise, seniority, team composition, etc.) and help establish good practices for designing and using GenAI systems that aid rather than hinder human creativity.

A closely related issue is the impact of creativity automation on the nature of creative work, as it may affect aspects of creative roles from which creative professionals draw meaning and satisfaction. For example, the process of drawing on paper or even with a stylus is a very different experience from that of prompting a system to generate a drawing. Even if the final product looks the same, it seems likely the process would have a substantial impact on the creator’s inherent enjoyment of the task. Therefore, the automation of certain creative processes may adversely impact job enjoyment and meaningfulness, both of which are important predictors of employee satisfaction and well-being.

## 4.2.3 Equity and Ethics in Creative Work

It is essential that the ethical implications of creativity automation are understood and considered to ensure a net benefit for all key stakeholders (including creative professionals, organizations, and society) (CRQ6). For example, emerging research suggests that AI may increase the productivity divide between higher-skilled and lower-skilled creative professionals (Jia et al., 2023). The impact of GenAI on different types of creative organizations may also be uneven. For example, while GenAI may make smaller organizations more productive, large corporations (particularly GenAI platform owners) may benefit even more through economies of scale and may be able to provide creative products at such low cost that it makes the business models of some smaller providers unviable. A question that naturally follows is how to design creativity automation in a way that reduces rather than expands productivity and the skill divide between creative professionals and organizations.

Questions also need to be addressed with regard to authorship, intellectual property, and accountability. Several actors are involved in enabling outputs of creative automation, such as programmers and trainers of the GenAI models, authors of the creative works used as training inputs, users prompting the system output, etc. Guidelines and good practices are therefore needed to determine who should be regarded as the authors (Eshraghian, 2020; Smits & Borghuis, 2022), and the owners and beneficiaries of (Avrahami & Tamir, 2021; Smits & Borghuis, 2022) AI-generated creative work.

## 4.2.4 Creative Work Processes and Team Dynamics

Finally, there is a need to understand how creativity automation might impact creative work processes and team dynamics (CRQ7). It is important to consider which creative tasks within these processes are best automated, which should be augmented, and which are best left untouched by AI. For example, might individually performed creative tasks be more readily automatable than those that leverage co-creation and team-based creativity? Also, might creativity automation fundamentally transform what is possible in some creative processes and products? For example, could the effect have some similarities with the impact of additive manufacturing on product design, which has opened up previously unthinkable design options (Pedota & Piscitello, 2022)?

A closely related issue is machine-human team dynamics, including the roles and division of work between humans and GenAI, how to build symbiotic collaboration between the two for the best creative outcomes (e.g., Zhou et al., 2021), and design principles for achieving that symbiosis (e.g., Urban Davis et al., 2021). This could also include exploring the various modes of human-machine interaction in creative processes and how to choose the best mode based on the nature of the creative task. For example, apart from the text-based prompting used by many emerging GenAI systems (e.g., ChatGPT and MidJourney), there may be opportunities to utilize more immersive interfaces, such as virtual reality (Urban Davis et al., 2021) to enhance engagement and creative imagination.

## 4.3 Modal Conversion

The third transformative GenAI capability is the ability of some of these systems to convert one type of creative input into a different type of creative output. Currently, the most common example of this is converting a text-based input into another creative medium such as image, sound, or video. However, multi-modal input systems (e.g., GPT-4) are emerging and seem likely to become commonplace over time. This modal conversion capability removes many of the barriers to entry in creative domains where specialist craft skills have traditionally been required. Although this capability has some parallels with other systems that convert a set of written instructions to a different type of output (e.g., CAD and 3D printing), there is a major difference here in terms of the specificity of instructions—GenAI systems are a lot more selfdirected and “imaginative,” meaning that the output from a modal conversion process may differ substantially from what the human prompting the system originally imagined. This raises several opportunities and challenges, particularly in relation to (1) creative skills and capabilities and (2) creative work processes.

## 4.3.1 Creative Skills

Modal conversion could have a profound impact on the skills required to complete certain creative tasks, and these impacts need to be understood (CRQ8). For example, the skills required to effectively prompt a GenAI system to produce a high-quality painting are very different from the painting skills that an artist would typically need to create this type of artwork by hand. This leads to questions around good practices for defining prompts to generate creative outputs (e.g., Oppenlaender [2022a] explored prompts for image generation). It seems likely that such good practices may also be context and goal dependent. For example, good practices for GenAI use may differ substantially depending on whether the artist’s goal is for the system to reproduce their creative ideas as closely as possible or to provide inspiration and highly novel concepts.

Furthermore, modal conversion may broaden access to creative domains for those who lack the craft skills traditionally required to produce creative work in that domain (Smits & Borghuis, 2022). Apart from creating paintings without knowing how to paint, other current examples of GenAI use include creating music without any familiarity with musical instruments or notes and creating photos without knowing how to operate a camera. This potential for much broader access to such creative pursuits raises many questions around both the opportunities and challenges for hobbyists, professionals, and creative industries. For example, could the impact be somewhat similar to digitalization in photography, which has made that craft much more widely accessible over the last few decades? While digitalization has allowed many more individuals to engage with and enjoy the art form and society has benefitted from the resultant body of creative and documentary work, photography has become much less viable as a business and profession.

## 4.3.2 Creative Work Processes

Modal conversion may also affect creative work processes, human-machine creative collaboration, and the good practices for designing such processes to enhance creative outcomes (CRQ9). Emerging research has found, for example, that using text-toimage AI to convert imaginary narratives to visual representations spurs the further creative enhancement of those underlying narratives (Ali & Parikh, 2021). These further creative insights are facilitated by the differences between how the human author and generative system pictured the scene (Epstein et al., 2022). This suggests that there could be opportunities to design for mutually reinforcing creative cycles which, in turn, would lead to further questions such as how to assess the creative contribution of humans and machines in such an iterative creative process (Oppenlaender, 2022b).

## 5 Conclusion

GenAI has expanded the scope of tasks that AI tools can accomplish for knowledge and creative work. For example, GenAI systems are increasingly capable of providing final creative artifacts with little or no human intervention and supporting knowledge workers in certain time-consuming tasks, thereby improving business processes and enabling the creation of new products and services. These developments raise many new possibilities, challenges, and questions about the future of knowledge and creative industries and the potential threat of substitution for knowledge and creative workers. This article offers a balanced analysis of the GenAI potential for knowledge and creative work and discusses the challenges that might arise from GenAI use as well as the implications for future IS research.

Table 2. Research Avenues for GenAI and Creative Work

<table><tr><td>Capability</td><td>Theme</td><td>RQ #</td><td>Research questions</td></tr><tr><td rowspan="3">Machine creativity</td><td>Characteristics &amp; features</td><td>CRQ1</td><td>·What are the fundamental characteristics of machine creativity?·Are the characteristics of machine creativity any different from those of human creativity? Can machines be “creative” in the same (or similar) sense as humans?·How can we use insights about human creative processes to better understand and improve machine creativity, and vice versa?</td></tr><tr><td>Measurement</td><td>CRQ2</td><td>·How should the creativity and quality of GenAI systems be measured? What is the best way to compare and choose between the creative outputs of different GenAI systems?·To what extent do measures of machine creativity converge with those used to measure human creativity?·Under what circumstances and to what extent can and do humans differentiate between human and machine creative outputs?</td></tr><tr><td>Techniques</td><td>CRQ3</td><td>·Which types of GenAI techniques are most effective for different types of creative tasks/outputs?·How can AI techniques to improve creative outputs be effectively combined?·How can AI systems be tailored to produce varying degrees of creative novelty?·What are the good practices for effective design of GenAI systems? What are the implications and applicability of the principles for human-centered AI in the context of creativity automation?</td></tr><tr><td>Creativity automation</td><td>Organization &amp; business modelsSkills &amp; capabilities</td><td>CRQ4CRQ5</td><td>·How does creativity automation impact creative professions? How does it affect the accessibility and viability of different creative professions?·How does creativity automation reshape the roles and value distribution in a creative supply chain?·Which new creative business models does GenAI enable? Which existing business models does it make less viable?·What are the organizational benefits of GenAI?·How do creative professionals perceive creativity automation? How do individual characteristics, context, and nature of the creative task affect such perceptions?How does the adoption of GenAI affect organizational creativity across different functions and creative domains?How does creativity automation impact the core skills of creative professionals in different creative sectors? Does this impact vary depending on individual characteristics, e.g., the level of expertise, seniority, etc.?How can we ensure that creativity automation does not stifle the development of core creative skills for humans?How does automation of different creative tasks affect the perceived meaningfulness of creative work and job satisfaction?</td></tr><tr><td rowspan="2"></td><td>Equity &amp; ethics</td><td>CRQ6</td><td>How can the use of creative automation and augmentation be balanced to ensure a net benefit to all key stakeholders (employees, organizations, and society)?How does the adoption of GenAI impact small vs large organizations in the creative sector? Are the benefits evenly distributed or does creative automation favor one organizational form over the other?How can creativity automation be designed in a manner that reduces rather than expands the productivity divide between creative professionals?How should the authorship, ownership, and accountability of GenAI outputs be determined?</td></tr><tr><td>Work processes &amp; team dynamics</td><td>CRQ7</td><td>In which creative tasks/processes does automation provide the best creative outcomes? In which augmentation? In which AI-free approach? Why?(How) does creativity automation extend and transform what is possible in different creative processes (e.g., new types of creative work and/or creative products)?How should a symbiotic machine-human relationship in creative processes be built for the best creative outcomes?What are the different modes of human-machine interaction as part of the creative process? How should the best mode be chosen based on the nature of the creative task at hand?</td></tr><tr><td rowspan="2">Modal conversion (e.g., text-to-image, text-to-sound, text-to-video)</td><td>Skills &amp; capabilities</td><td>CRQ8</td><td>How does modal conversion affect the skills and capabilities required for completing different creative tasks?What are the best practices and skills required for effective use of modal conversion?What opportunities and challenges arise from the use of modal conversion for hobbyists, professionals, and creative industries?</td></tr><tr><td>Work processes</td><td>CRQ9</td><td>How does modal conversion affect creative processes and outcomes?How should the creative contribution of humans and machines be measured and distinguished in a modal conversion process?</td></tr></table>

## References

Ali, S., & Parikh, D. (2021). Telling creative stories using generative visual aids. arXiv. https://arxiv.org/abs/2110.14810

Avital, M., & Te’eni, D. (2009). From generative fit to generative capacity: Exploring an emerging dimension of information systems design and task performance. Information Systems Journal, 19(4), 345-367.

Avrahami, O., & Tamir, B. (2021). Ownership and creativity in generative models. arXiv. https://arxiv.org/abs/2112.01516

Benbya, H. (2008) Knowledge management systems implementation: Lessons from the Silicon Valley. Chandos.

Benbya, H; Davenport, T.H.; and Pachidi, S. (2020). Artificial intelligence in organizations: current state and future opportunities. MIS Quarterly Executive, 19(4), ix, xxi

Benbya, H.; Pachidi, S.; and Jarvenpaa, S. (2021). Artificial intelligence in organizations: implications for information systems research. Journal of the Association for Information Systems, 22(2), 281-303

Boden, M. A. (1998). Creativity and artificial intelligence. Artificial Intelligence, 103(1), 347- 356.

Bown, O. (2012). Generative and adaptive creativity: A unified approach to creativity in nature, humans and machines. In J. McCormack & M. d’Inverno (Eds.), Computers and creativity (pp. 361-381). Springer.

Brea, E., & Ford, J. A. (2023). No silver bullet: Cognitive technology does not lead to novelty in all firms. Technovation, 122, Article 102643.

Brynjolfsson, E., Li, D., & Lindsay, R. R. (2023). Generative AI at work (NBER working paper, No. 31161). http://www.nber.org/papers/w31161

Chemla-Romeu-Santos, A., & Esling, P. (2022). Challenges in creative generative models for music: A divergence maximization perspective arXiv. https://arxiv.org/abs/2211.08856

Chiarella, S. G., Torromino, G., Gagliardi, D. M., Rossi, D., Babiloni, F., & Cartocci, G. (2022). Investigating the negative bias towards artificial intelligence: Effects of prior assignment of AIauthorship on the aesthetic appreciation of abstract paintings. Computers in Human Behavior, 137(C), Article 107406.

Davenport, T. (2005). Thinking for a living. Harvard Business School Press.

Dean, D., Hender, J., Rodgers, T., & Santanen, E. (2006). Identifying quality, novel, and creative ideas: Constructs and scales for idea evaluation. Journal of the Association for Information Systems, 7(10), 646-698

DiPaola, S., Gabora, L., & McCaig, G. (2018). Informing artificial intelligence generative techniques using cognitive theories of human creativity. Procedia Computer Science, 145, 158-168.

Deng, J., & Lin, Y. (2023). The Benefits and Challenges of ChatGPT: An Overview. Frontiers in Computing and Intelligent Systems, 2(2), 81-83.

Elam, J. J., & Mead, M. (1987). Designing for creativity: Considerations for DSS development. Information & Management, 13(5), 215-222.

Elgammal, A. (2019). AI Is blurring the definition of artist: Advanced algorithms are using machine learning to create art autonomously. American Scientist, 107(1), Article 18.

Epstein, Z., Schroeder, H., & Newman, D. (2022). When happy accidents spark creativity: Bringing collaborative speculation to life with generative AI. arXiv. https://arxiv.org/abs/2206.00533, Ix-xxi

Eshraghian, J. K. (2020). Human ownership of artificial creativity. Nature Machine Intelligence, 2(3), 281-303

Fügener, A., Grahl, J., Gupta, A., & Ketter, W. (2021). Will humans-in-the-loop become borgs? merits and pitfalls of working with AI. MIS Quarterly, 45(3), 1527-1556.

Forrest, R. (2023). Could your employees’ use of ChatGPT put you in breach of GDPR? ComputerWeekly. https://www.computerweekly. com/opinion/Could-your-employees-use-of-ChatGPT-put-you-in-breach-of-GDPR

Giermindl, L. M., Strich, F., Christ, O., Leicht-Deobald, U., & Redzepi, A. (2022). The dark sides of people analytics: Reviewing the perils for organisations and employees. European Journal of Information Systems, 31(3), 410-435.

Grierson, J. (2023). Photographer admits prize-winning image was AI-generated. The Guardian. https://www.theguardian.com/technology/2023/ apr/17/photographer-admits-prize-winningimage-was-ai-generated

Gurman, M. (2023). Samsung bans staff’s AI use after spotting ChatGPT data leak. Bloomberg. https://www.bloomberg.com/news/articles/2023- 05-02/samsung-bans-chatgpt-and-othergenerative-ai-use-by-staff-afterleak?leadSource=uverify%20wall

Haase, J., & Hanel, P. H. P. (2023). Artificial muses: Generative artificial intelligence chatbots have

risen to human-level creativity. arXiv. https://arxiv.org/abs/2303.12003

Hacker, P., Engel, A., & Mauer, M. (2023). Regulating ChatGPT and other large generative AI models. arXiv. https://arxiv.org/abs/2302.02337.

Haefner, N., Wincent, J., Parida, V., & Gassmann, O. (2021). Artificial intelligence and innovation management: A review, framework, and research agenda. Technological Forecasting and Social Change, 162, Article 120392.

Ho, J., Jain, A. and Pieter, A. (2020). Denoising diffusion probabilistic models. Proceedings of the 34th International Conference on Neural Information Processing Systems (pp. 6840-6851).

Hong, J.-W., & Curran, N. M. (2019). Artificial intelligence, artists, and art: attitudes toward artwork produced by humans vs. artificial intelligence. ACM Transactions on Multimedia Computing, Communications, and Applications, 15(2S), 58:1-58:16.

Jarrahi, M. H., Askay, D., Eshraghi, A., & Smith, P. (2023a). Artificial intelligence and knowledge management: A partnership between human and AI. Business Horizons, 66(1), 87-99.

Jarrahi, M. H., Möhlmann, M., & Lee, M. K. (2023b). Algorithmic management: The role of AI in managing workforces. MIT Sloan Management Review, 64(3), 1-5.

Jia, N., Luo, X., Fang, Z., & Liao, C. (2023). When and how artificial intelligence augments employee creativity. Academy of Management Journal. Advance online publication. https://doi.org/ 10.5465/amj.2022.0426

Kahn, S. (2023, April.). How AI could save (not destroy) education [Video]. TED https://www.ted.com talks/sal\_khan\_how\_ai\_could\_save\_not\_destroy \_education/c

Koster, R., Balaguer, J., Tacchetti, A., Weinstein, A., Zhu, T., Hauser, O., Williams, D., Campbell-Gillingham, L., Thacker, P., Botvinick, M., & Summerfield, C. (2022). Human-centred mechanism design with democratic AI. Nature Human Behaviour, 6(10), Article 10.

Lamb, C., Brown, D. G., & Clarke, C. L. A. (2017). A taxonomy of generative poetry techniques. Journal of Mathematics and the Arts, 11(3), 159- 179.

Lee, J. S., Kim, J., & Kim, P. M. (2023). Score-based generative modeling for de novo protein design. Nature Computational Science, 3, 382-392.

Lim, W. M., Gunasekara, A., Pallant, J. L., Pallant, J. I., & Pechenkina, E. (2023). Generative AI and the future of education: Ragnarök or reformation? A

paradoxical perspective from management educators. International Journal of Management Education, 21(2), Article 100790.

Lukpat, A. (2023). JPMorgan restricts employees from using ChatGPT. The Wall Street Journal. https://www.wsj.com/articles/jpmorgan-restrictsemployees-from-using-chatgpt-2da5dc34

Massetti, B. (1996). An empirical examination of the value of creativity support systems on idea generation. MIS Quarterly, 20(1), 83-97.

Mayer, A. S., Strich, F., & Fiedler, M. (2020). Unintended consequences of introducing AI systems for decision making. MIS Quarterly Executive, 19(4), 239-257.

Mello, G., Shaw, W., & Levitt, H. (2023). Wall Street banks are cracking down on AI-powered ChatGPT. Bloomberg. https://www.bloomberg. com/news/articles/2023-02-24/citigroupgoldman-sachs-join-chatgpt-crackdown-fnreports#xj4y7vzkg

Mikalef, P., & Gupta, M. (2021). Artificial intelligence capability: Conceptualization, measurement calibration, and empirical study on its impact on organizational creativity and firm performance. Information & Management, 58(3), 103434.

Miller, A. I. (2020). Can AI be truly creative? American Scientist, 108(4), 244-249.

Mohr, J., & Curran, R. (2023). Knowledge management, I’d like to introduce my new friend, generative AI. Forrester. https://www.forrester.com/blogs/ knowledge-management-id-like-to-introducemy-new-friend-generative-ai/?utm\_source =forbes&utm\_medium=pr&utm\_campaign=tech

Morrow, E., Zidaru, T., Ross, F., Mason, C., Patel, K. D., Ream, M., & Stockley, R. (2023). Artificial intelligence technologies and compassion in healthcare: A systematic scoping review. Frontiers in Psychology, 13, Article 971044.

Ni, B., Kaplan, D. L., & Buehler, M. J. (2023). Generative design of de novo proteins based on secondarystructure constraints using an attention-based diffusion model. Chem, 9(7), 1828-1849

Oppenlaender, J. (2022a). A taxonomy of prompt modifiers for text-to-image generation. arXiv. https://arxiv.org/abs/2204.13988

Oppenlaender, J. (2022b). The creativity of text-to-image generation. Proceedings of the 25th International Academic Mindtrek Conference, (pp. 192-202).

Oppenlaender, J., Visuri, A., Paananen, V., Linder, R., & Silvennoinen, J. (2023). Text-to-image generation: perceptions and realities. arXiv. https://arxiv.org/abs/2303.13530

Oppermann, L., Boden, A., Hofmann, B., Prinz, W., & Decker, S. (2019). Beyond HCI and CSCW: Challenges and useful practices towards a humancentred vision of AI and IA. Proceedings of the Halfway to the Future Symposium.

Oracle. (2020). As uncertainty remains, anxiety and stress reach a tipping point at work (AI@Work Study). https://www.oracle.com/a/ocom/docs/oracle hcm-ai-at-work.pdf

Pedota, M., & Piscitello, L. (2022). A new perspective on technology-driven creativity enhancement in the fourth industrial revolution. Creativity and Innovation Management, 31(1), 109-122.

Pilcicki, R., Siemon, D., & Lattemann, C. (2022). Constraints that support creativity: Design principles for next generation creativity support systems. Proceedings of the Pacific Asia Conference on Information Systems.

Raisch, S., & Krakowski, S. (2021). Artificial intelligence and management: The automation-augmentation paradox. Academy of Management Review, 46(1), 192-210.

Renaud, K., Warkentin, M., & Westerman, G. (2023). From ChatGPT to HackGPT: Meeting the cybersecurity Threat of generative AI. MIT Sloan Management Review, 64(3), 1-4.

Roose, K. (2022). An A.I.-generated picture won an art prize. Artists aren’t happy. The New York Times. https://www.nytimes.com/2022/09/02/ technology/ai-artificial-intelligence-artists.html

Shneiderman, B. (2020). Human-centered artificial intelligence: Three fresh ideas. AIS Transactions on Human-Computer Interaction, 12(3), 109-124.

Seeber, I., Bittner, E., Briggs, R. O., de Vreede, T., de Vreede, G.-J., Elkins, A., Maier, R., Merz, A. B., Oeste-Reiß, S., Randrup, N., Schwabe, G., & Söllner, M. (2020). Machines as teammates: A research agenda on AI in team collaboration. Information & Management, 57(2), 103174.

Siau, K., & Wang, W. (2020). Artificial intelligence Ethics. Journal of Database Management, 31(2), 74-87.

Siemon, D., Strohmann, T., & Michalke, S. (2022). Creative potential through artificial intelligence: Recommendations for improving corporate and entrepreneurial innovation activities. Communications of the Association for Information Systems, 50(1), 241-260

Smits, J., & Borghuis, T. (2022). Generative AI and Intellectual Property Rights. In B. Custers & E. Fosch-Villaronga (Eds.), Law and artificial intelligence: Regulating AI and applying AI in legal practice (pp. 323-344). T.M.C. Asser Press.

Strich, F., Mayer, A. S., & Fiedler, M. (2021). What do I do in a world of artificial intelligence? Investigating the impact of substitutive decisionmaking AI systems on employees’ professional role identity. Journal of the Association for Information Systems, 22(2), 304-324.

Sun, L., Chen, P., Xiang, W., Chen, P., Gao, W., & Zhang, K. (2019). SmartPaint: A co-creative drawing system based on generative adversarial networks. Frontiers of Information Technology & Electronic Engineering, 20(12), 1644-1656.

Tarafdar, M., Page, X., & Marabelli, M. (2023). Algorithms as co-workers: Human algorithm role interactions in algorithmic work. Information Systems Journal, 33(2), 232-367.

Taylor, J. (2023). ChatGPT’s alter ego, Dan: Users jailbreak AI program to get around ethical safeguards. The Guardian. https://www.the guardian.com/technology/2023/mar/08/chatgptalter-ego-dan-users-jailbreak-ai-program-to-getaround-ethical-safeguards

Urban Davis, J., Anderson, F., Stroetzel, M., Grossman, T., & Fitzmaurice, G. (2021). Designing cocreative AI for virtual environments. Proceedings of the 13th Conference on Creativity and Cognition (Article 26).

Vasist, P., & Krishnan, S. (2022). Deepfakes: An integrative review of the literature and an agenda for future research. Communications of the Association for Information Systems, 51, 590-636

Vrontis, D., Christofi, M., Pereira, V., Tarba, S., Makrides, A., & Trichina, E. (2022). Artificial intelligence, robotics, advanced technologies and human resource management: a systematic review. The International Journal of Human Resource Management, 33(6), 1237-1266.

Wierenga, B., & van Bruggen, G. H. (1998). The dependent variable in research into the effects of creativity support systems: Quality and quantity of ideas. MIS Quarterly, 22(1), 81-87.

Zhou, L., Paul, S., Demirkan, H., Yuan, L., Spohrer, J., Zhou, M., & Basu, J. (2021). Intelligence augmentation: towards building human-machine symbiotic relationship. AIS Transactions on Human-Computer Interaction, 13(2), 243-264.

Ziegler, A., Kalliamvakou, E., Li, X. A., Rice, A., Rifkin, D., Simister, S., Sittampalam, G., & Aftandilian, E. (2022). Productivity assessment of neural code completion. Proceedings of the 6th ACM. SIGPLAN International Symposium on Machine Programming (pp. 21-29).

## About the Authors

Hind Benbya is a professor and the founding director of the Centre for AI and the Future of Business at Deakin University. She has 20+ years of international leadership experience in diverse research, engagement, and education roles, including head of school, faculty head, department chair, and director of a research center. She is a distinguished expert in IT-enabled transformation and innovation and her research focuses on artificial intelligence, especially around the implications of automation via algorithms and robotics on work and organizations. Her work has appeared in major academic and practitioner journals, including MIS Quarterly, the Journal of Management Information Systems, MIT Sloan Management Review, MISQ Executive, and Decision Support Systems. Hind has authored and edited four books, including Knowledge Management Systems Implementation: Lessons from the Silicon Valley (2008). She is the recipient of several Best Paper awards at major conferences like the Academy of Management and HICSS.

Franz Strich is a senior lecturer in information systems and business analytics at Deakin Business School. His research focuses on human-AI interaction and its impact on the changing nature of work. With an interdisciplinary background in clinical and organizational psychology, business economics, and information systems, his work provides strategic insights into the challenges of digital transformation. His work aids organizations in addressing the complexities and employee dynamics brought about by recent technological advancements. His research has been published in journals such as Journal of the Association for Information Systems, European Journal of Information Systems, Information Systems Journal, MIS Quarterly Executive, and Journal of Cultural Economics.

Toomas Tamm is a senior lecturer in information systems and business analytics at the Deakin Business School. He has previously held academic positions at the UNSW Business School and the University of Melbourne, and prior to entering academia worked in the retail and services sector as a sales consultant, web editor, and project manager. Through his research, teaching, and advisory work, Toomas aspires to help organizations and individuals make better decisions with digital technologies. He has a special interest in strategic and creative decision-making (particularly in balancing the strengths of humans and digital technology in these decision processes) and in digitalization in the environmental sector (particularly the use of digital technologies to support nature conservation efforts).

Copyright © 2024 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
