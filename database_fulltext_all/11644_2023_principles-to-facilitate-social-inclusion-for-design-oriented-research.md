---
otero_id: 11644
otero_key: "WG8HNGWK"
title: "Principles to Facilitate Social Inclusion for Design-Oriented Research"
authors: "Sofie Wass; Elin Thygesen; Sandeep Purao"
year: "2023"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00814"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 24 Issue 5 Special Issue: Technology and Social Inclusion (pp. 1199-1357)

Article 9

2023

# Principles to Facilitate Social Inclusion for Design-Oriented Research

Sofie Wass

, sofie.wass@uia.no

Elin Thygesen

, elin.thygesen@uia.no

Sandeep Purao

, spurao@bentley.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Principles to Facilitate Social Inclusion for Design-Oriented Research

Sofie Wass,<sup>1</sup> Elin Thygesen,<sup>2</sup> Sandeep Purao<sup>3</sup>

<sup>1</sup>University of Agder, Norway, sofie.wass@uia.no <sup>2</sup>University of Agder, Norway, elin.thygesen@uia.no <sup>3</sup>Bentley University, USA, spurao@bentley.edu

## Abstract

We develop principles that facilitate socially inclusive design-oriented research with marginalized groups. Building on the recognition that the research process must be informed by theoretical perspectives about social inclusion, our effort begins with an empirical investigation of a multiyear research project that designed several IT-based solutions for people with intellectual and developmental disabilities. We treat the efforts to design each solution as a “case,” capture primary data from multiple sources, and analyze it in light of three facets of social inclusion drawn from prior work: self-determination, belongingness, and social capital. The findings are interpreted to derive five principles for a socially inclusive design-oriented research process: (1) respecting multiperspective problem ownership and integrated solution design, (2) surfacing emic contributions to guide artifact design, (3) leveraging the support network to shape artifact design and refine research conduct, (4) customizing design-evaluate cycles with inclusive practices, and (5) pursuing authenticity in research collaborations. We elaborate each principle with connections to different facets of social inclusion, guidelines suggested by our empirical investigation, and a mapping against contemporary design-oriented research approaches. The five principles suggest key directions to facilitate a socially inclusive design-oriented research process when working with marginalized groups. The paper concludes with a discussion of implications for IS scholars, and pointers for using design-oriented approaches for greater social inclusion of marginalized populations.

Keywords: Social Inclusion, Marginalized Groups, Design-Oriented Research, Research Process, Multicase Research, Action Design Research, Intellectual and Developmental Disability, Principles

Arlene Bailey was the accepting senior editor. This research article was submitted on April 4, 2021 and underwent three revisions. This paper is part of the Special Issue on Technology and Social Inclusion.

## 1 Introduction

Social inclusion is “the ability to participate fully in one’s social world” (Bailey et al., 2020), an important concern for marginalized populations. Marginalization is “the process through which members of some segments of society find themselves out of the mainstream based on their membership in … groups based on social class, ethnicity, gender, disability, age, and others” (Given, 2008, p. 491). Information systems (IS) can enable or impede the social inclusion of such groups through the design of technologies (Díaz et al., 2016; Hsieh et al., 2008; Pethig & Kroenung, 2019). Scholars in IS have recognized the problem of social inclusion (AbuJarour et al., 2019; Carter et al., 2013; Myers et al., 2020; Trauth, 2017) and investigated it in diverse contexts (e.g., AbuJarour & Krasnova, 2017; Deng et al., 2016; Gallivan, 2013; Joshi & Schmidt, 2006; Trauth et al., 2016).

Elsewhere, considerable scholarship (Cobigo et al., 2012; Simplican et al., 2015), activism (Wolfensberger, 1983), and policy-making efforts (Atkinson & Marlier, 2010; United Nations, 2006) have been devoted to social inclusion concerns. Despite these efforts (within the IS discipline and beyond), moving toward greater social inclusion of marginalized groups remains a challenge (Pethig & Kroenung, 2019; Serenko & Turel, 2021). Scholars and policy makers maintain that without concerted and conscientious efforts, the vision of social inclusion remains at risk of being merely an ideology (Aldridge, 2019; Cobigo et al., 2012). One vehicle to realizing this vision is action- and design-oriented work to build solutions (technologies and services) that can respond to the concerns of marginalized populations (Trauth, 2017). Contemporary versions of such approaches include participatory design (Bjerknes & Bratteteig, 1995), action-design research (Sein et al., 2011), collaborative practice research (Mathiassen, 2002), and soft design science (Baskerville et al., 2009) that incorporate collaboration with external partners as an essential ingredient, i.e., these approaches already contain the potential for working with marginalized groups.

However, problems remain. For example, these designoriented approaches focus on mechanics and generating solutions (Purao & Mulgund, 2022; Semborski et al., 2022) but rarely infuse research conduct with important social inclusion considerations (e.g., AbuJarour & Krasnova, 2017; Cobigo et al., 2012; Selwyn, 2002; Taket et al., 2009). Researchers interested in using such approaches to design technologies and services for marginalized populations have little guidance about what obstacles they may face and how to overcome them (Olbrich et al., 2015). For example, to elevate users and other stakeholders to “partners” (and not subjects) in the research process (Mathiassen, 2002, p. 57), Sein et al. (2011) suggest the principle of mutually influential roles. However, such collaboration can pose challenges for both the marginalized groups and researchers. Individuals from marginalized groups must overcome cognitive (Hendriks et al., 2014; Makhaeva et al., 2016) and social barriers (Shakespeare, 2004), and researchers must break free of persistent stereotypes (Pelleboer-Gunnink et al., 2021; Werner & Abergel, 2018). Viewing individuals from marginalized groups based on the norms and standards defined by the majority can make it difficult for researchers to see the concerns that marginalized groups face from an emic perspective. It can also conceal the connections to different stakeholders and hide the scale and complexity of problems (Frauenberger et al., 2011; Waycott et al., 2015). In addition, researchers must anticipate challenges they might face in working with marginalized groups, appreciate their unique experiences, and allow prior theoretical perspectives about social inclusion (Taket et al., 2009) to guide their conduct.

Motivated by these observations, our goal in this paper is to develop principles to facilitate greater social inclusion when conducting design-oriented research with marginalized populations. We start by recognizing that any research effort generates two parallel arenas for investigation, (1) the outcome of the research effort, and (2) the research process itself. We focus on the latter, arguing for the importance of a socially inclusive design-oriented research process as a prerequisite when working with marginalized populations (Nind & Vinha, 2014; Walmsley et al., 2018). IS scholars have proposed such principles for conducting research following different genres, e.g., positivist (Benbasat et al., 1987), interpretive (Klein & Myers, 1999; Yin, 2003), qualitative (Sarker et al., 2013), critical (see Myers & Klein, 2011) and design science (Hevner et al., 2004; Sein et al., 2011). Our work follows this spirit with one key difference. Like the sources cited, we are motivated by a desire to provide guidance to enhance the research process. However, unlike the examples cited, our intent is not to provide general principles for a research genre. Instead, we focus on a particular goal: facilitating a socially inclusive design-oriented research process.

The principles we develop are grounded in a multiyear research project to develop IT-based solutions for people with intellectual and developmental disabilities (IDD) as they transition from school to work. People with IDD remain marginalized in areas such as work (Erickson et al., 2020; Gjertsen et al., 2021), education (Kuntz & Carter, 2019), and leisure (Simpson et al., 2019). The needs and values of this population (100+ million across the planet—Mulhall et al., 2018) are often excluded from consideration or merely communicated by others (Constantino et al., 2020; Mackert et al., 2016; Merrells et al., 2019; Rogers & Marsden, 2013). In response to these concerns, our research project has thus far led to the design of three IT artifacts using the action design research approach (Sein et al., 2011). In this paper, we treat the research efforts to design each IT artifact as a “case” and collect primary data from multiple sources. We analyze the data (within each case and across cases) to generate empirical findings. Finally, we synthesize these findings based on three facets of social inclusion (selfdetermination, belongingness, and social capital) to develop principles for greater social inclusion when conducting design-oriented research, which is the core contribution of this paper.

Our work has three audiences. First, we hope to provide IS scholars with possible pathways toward realizing the elusive goal of greater social inclusion in terms of how they conduct research. Second, we hope it can provide IS scholars considering the use of design-oriented approaches (to work with marginalized populations) with specific ways of infusing social inclusion considerations in their work.

Finally, we hope that our work will be of interest to IS scholars generally, who may not be directly dealing with concerns of social inclusion but might be interested in improving their understanding of its foundations in order to explore its influence on their research.

The remainder of the paper is organized as follows. Section 2 reviews the background—including prior work related to social inclusion, marginalized populations, and design-oriented approaches—in order to establish the need to incorporate social inclusion concerns in design-oriented approaches. Section 3 outlines the research method used for this study as a multi-case investigation and describes the data collection and analyses we used to draw out empirical insights. In Section 4, we develop the principles of facilitating social inclusion, grounded in the empirical findings and illustrated with selected extracts from the empirical cases along with prior theoretical positions about social inclusion. In Section 5, we return to the core concern of social inclusion to highlight our contributions, discuss the implications of our work, point to limitations, and present concluding remarks.

## 2 Background and Theoretical Development

## 2.1 The Social Inclusion Puzzle

A concise definition of social inclusion is “the ability to participate fully in one’s social world” (Bailey et al., 2020). Contemporary scholarship describes social inclusion as multidimensional (Taket et al., 2009). Origins of the term can be traced to the ideas of social “exclusion” that describe the economically disadvantaged as “the excluded” (Silver, 1995; Williams & White, 2003, p. 91), along with other terms such as participation and community inclusion (Cobigo et al., 2012). In the IS discipline, social inclusion has been defined as “the extent that individuals, families, and communities are able to fully participate in society and control their own destinies” (Warschauer, 2004, p. 8) and has been described as “an expression of concern about the ‘haves’ and the ‘have nots’ in the information society” (Trauth, 2017, p. 10). Across these research threads, scholars have acknowledged that the term must recognize social, political, economic, and cultural dimensions (Berghman, 1995; Walker & Walker, 1997) and accept social inclusion as dynamic and relational instead of absolute or dichotomous (Selwyn, 2002; Taket et al., 2009). The experience of “social inclusion” is described as intensely personal and tied to the specific capabilities of the individual and the opportunities provided to the individual (Craig et al., 2007; Trauth & Howcroft, 2006). In other words, what social inclusion means to an individual can vary across roles and environments and may evolve over time; the same behaviors and actions can lead to different degrees and forms of social inclusion in different settings (Hammel et al., 2008). Efforts to understand the social inclusion puzzle must, therefore, unpack these complexities. Here, we draw on prior research to identify three interrelated yet analytically distinct facets of social inclusion—self-determination, belongingness, and social capital. Figure 1 illustrates these facets.

The first facet, self-determination, captures the idea of being the primary causal agent in one’s own life and exercising autonomy without unwarranted influence. It highlights the individual’s ability to control events and witness their own influence (i.e., it is rooted in selfperception) (Rotter, 1966). It describes the exercise of volitional and autonomous actions by an individual based on intrinsic motivation (acting out of interest, without the need for external rewards) (Deci & Ryan, 2002). This motivation is driven by three basic psychological needs: autonomy (being the perceived source of one’s own behavior), competence (experiencing mastery and producing desired outcomes in a social environment), and relatedness (the ability to relate and connect to others) (Deci & Ryan, 2002).

![](/api/attachments/WG8HNGWK/fulltext/images/ab39ffd52f6b022424e0e4c944373780a2d67f8d9d01e26303f13340f36619a9.jpg)  
Figure 1. Social Inclusion: Key Facets

When an environment supports self-determination, individuals experience a sense of being in control of their actions, e.g., having a voice and being able to make decisions (Niemiec & Ryan, 2009). This allows individuals to recognize and exercise choices and express preferences, solve problems and make decisions, set and achieve goals, and assert themselves and their own rights (Shogren et al., 2015a). However, self-determination does not mean uncritical accountability (Bollingmo et al., 2005) or independence from others (Fay, 1996; Lorentzen, 2007). Instead, it points out that the decisions people make are related to the group that they are part of, without unwanted influence or interference.

The second facet, belongingness, describes a feeling of acceptance with the collective. It emphasizes that individuals have a strong need for acceptance and belonging to a collective such as a family, group, or community (Baumeister & Leary, 1995). Antonsich (2010, p. 645) defines belonging “as a personal, intimate, feeling of being at-home.” A core element of belongingness is simply the feeling of being part “of a group.” If the need to belong is fulfilled, it can contribute to a sense of connection to a context or a group, grounded in a reciprocal relationship (Mahar et al., 2013; Simplican et al., 2015). Belonging to a society includes the feeling of being valued and respected (Mahar et al., 2013).

Belongingness theory (Baumeister & Leary, 1995) provides a rationale (the need to belong) for interpersonal relationships in human lives. The sense of belongingness is subjective and centers on feelings of value, respect, and fit that are anchored in a group, and it is examined in terms of its permanence. This sense of belongingness can be restricted by physical or environmental factors and must be based on the individual’s own wish to belong (Mahar et al., 2013). The sense of belongingness remains an important consideration for groups who have faced social exclusion (Baumeister & Leary, 1995; Hall, 2010).

The third facet, social capital, recognizes the importance of mutual exchange, building on the norms of reciprocity and trust within social relations as a foundation for and a determinant of social inclusion.

This concept has been defined in different ways but centers on norms of reciprocity, interpersonal trust, and social engagement among members of a group (Putnam, 2000). It explains social inclusion in terms of the complex dynamics (Bollard, 2009) and mutual exchange (Western et al., 2007) in groups, rather than viewing it as the acceptance or achievement of norms and standards defined by typical members of a group (Bates & Davis, 2004; Bollard, 2009). There is a growing consensus that the concept includes “the ability of actors to secure benefits by virtue of membership in social networks or other social structures” (Portes, 1998, p. 6).

Social capital can foster bridging (outward-looking and inclusive, connecting people across social divides) and bonding (inward-looking and exclusive, reinforcing group identity) between individuals (Putnam, 2000). To do so, the group activates cognitive elements (shared values such as reciprocity, trust, altruism, and civic responsibility), which can lead to a reduced sense of marginalization and more satisfying social relationships (Western et al., 2007). However, this is a reciprocal process, dependent on a positive attitude, acceptance, meaningful participation, and a successful combination of people and settings (Overmars-Marx et al., 2014). While social capital has positive consequences, it can also result in exclusion, conformity, and the restriction of freedom (Portes, 1998). These mechanisms describe how individuals can activate the complex social relations that enable members of a group to act together to pursue shared objectives (Putnam, 2000) regarding prosocial behaviors (Bollard, 2009).

Together, the three facets describe how greater social inclusion can be pursued. The first, self-determination, acknowledges the need for individual action as a prerequisite for social inclusion; the second, belongingness, emphasizes the interpersonal relationships that foster an individual’s sense of acceptance by the collective; and the third, social capital, recognizes the competence of the individual and trusts their ability to contribute to the group, necessary for social inclusion. Table 1 summarizes these facets.

Table 1. The Social Inclusion Puzzle

<table><tr><td>Key facet</td><td>Description</td></tr><tr><td>Self-determination (Deci &amp; Ryan, 2002; Rotter, 1966)</td><td>Being the primary causal agent in one’s own life (to exercise autonomy without unwarranted influence)</td></tr><tr><td>Belongingness (Baumeister &amp; Leary, 1995; Mahar et al., 2013)</td><td>A feeling of acceptance in the collective (being a valued and respected member of the group)</td></tr><tr><td>Social capital (Portes, 1998; Putnam, 2000)</td><td>Recognition of mutual exchange (building on the recognition of competence and the norms of reciprocity and trust)</td></tr></table>

## 2.2 Marginalized Groups and Social Inclusion

Although the term “marginalized group” is often discussed alongside “social inclusion,” it is important to define it in its own right. As use of the term has evolved over the last few decades (Silver, 1995), it has become tied to more than just socioeconomic conditions (Wilson, 2006): “poverty [is] no longer the right word to use to describe the plight of those marginalized from mainstream society” (Williams & White, 2003, p. 91). Contemporary efforts define marginalized communities as: “those excluded from mainstream social, economic, educational, and/or cultural life” (Sevelius et al., 2020, p. 2009; Shepheard-Walwyn, 2018), building on prior work related to power, participation, status inconsistency, the feminist perspective, and other topics (Alm & Guttormsen, 2021). Examples of marginalized groups include but are not limited to groups excluded due to race, gender identity, sexual orientation, age, physical ability, language, and immigration status. Another study points out that the word “marginalized” describes the experiences of those who live on the fringe, are systematically excluded from full participation in society, and lack the power to improve their life situation (Shepheard-Walwyn, 2018). IS scholarship has recognized different marginalized groups, including women (Adam et al., 2002; Gallivan, 2013; Trauth et al., 2016), people with disabilities (Istenic Starcic & Bagon, 2014), those with refugee status (AbuJarour et al., 2019; Díaz Andrade & Doolin, 2016), and the elderly (Chen & Schulz, 2016; Srivastava & Panigrahi, 2019), and has addressed concerns such as access, privilege, and identity.

These efforts to define and elaborate the term “marginalized groups” have helped to further clarify that the concerns of social inclusion are not absolute or dichotomous. Instead, they point out that a dynamic and relational perspective is needed (Selwyn, 2002; Taket et al., 2009) to acknowledge the interplay between the specific capabilities of individuals and their opportunities to participate in communities of interest (Craig et al., 2007; Trauth & Howcroft, 2006). However, beyond simply overcoming social exclusion (reducing disadvantages) to actively promote opportunities for empowerment and participation (Cobigo & Stuart, 2010; Phipps, 2000), there is consensus among scholars that efforts to enhance social inclusion must ensure that individuals in marginalized groups can make valued economic contributions, become empowered citizens, have social networks, and function without stigma (Chapman et al., 1998; Commins, 1993). An important distinction here is the experience (versus the recognition) of marginalization. The experience of marginalization can encompass a sense of not belonging, not being a valued member of a community, not being able to make a valuable contribution, and not being able to access services and opportunities available to others. Marginalization can take many forms—it can be formal or informal, is often situated by time and place, and can shape aspects of individuals’ identity and lived experiences (Mowat, 2015). These challenges appear in two life domains: interpersonal relationships and community participation (Simplican, 2015). Marginalization may therefore be experienced and recognized differently by individuals and groups.

Thus far, this review has pointed out that the three facets of social inclusion identified earlier—selfdetermination, belongingness, and social capital— must be tailored for the different marginalized groups in different contexts. Examples abound: Millner et al. (2019) showed how self-determination is relevant for understanding social inclusion for individuals with serious mental illnesses. Other scholars have explored the importance of self-determination for Black and minority students in higher education (Bunce et al., 2021) and for people with disabilities (Sprague & Hayes, 2000). Gao and Liu (2021) demonstrated the importance of belongingness for ethnic minority students. Yet others have explored the importance of belongingness for migrant pupils (Ritchie & Gaulter, 2020) and unemployed individuals (Toikko & Pehkonen, 2018). And other studies (e.g., Perez-Brumer et al. 2017) have explored the relevance of bridging and bonding social capital for transgender women. Scholars have also explored the relevance of social capital for different marginalized groups, such as socioeconomically disadvantaged people (Martínez-Martínez & Rodríguez-Brito, 2020) and the elderly (Scharlach & Lehning, 2013). Our intent in pointing to these studies is to emphasize how the three facets can be examined separately and how each needs to be operationalized with particular modes for different marginalized groups.

Despite these differences, key similarities remain. For example, Maidment and Macfarlane (2009, p. 102) pointed out that social inclusion is more about selfdetermination than “assimilation into dominant or mainstream norms and values,” pointing to the significance of agency (Taket et al., 2009). For marginalized groups, the exercise of autonomy implies a decision about when and how to participate in a larger community. Across different contexts, marginalized individuals identify the quality of relationships in their support network as a central factor influencing their degree of self-determination (Nonnemacher & Bambara, 2011). Other studies have pointed out that belongingness may be perceived differently across contexts but must include a feeling of being one “of the group,” and being valued and respected (Mahar et al., 2013), which is important because individuals can belong to multiple groups (Cummins & Lau, 2003). Further studies have emphasized the need to cultivate social capital, e.g., in terms of reciprocal relationships characterized by participation and commitment of the involved individuals (Overmars-Marx et al., 2014) that enable members to collaborate in the pursuit of shared objectives (Putnam, 2000). These similarities (along with the need to tailor and operationalize the facets to different contexts) suggest a number of challenges and possibilities that scholars can pursue, using designoriented approaches in particular.

## 2.3 Design-Oriented Approaches

Design-oriented approaches can be distinguished across two sometimes overlapping efforts: (1) industry practice and (2) scholarly research. For example, ideas such as design thinking (Kelley & Kelley, 2012) are part of industry practice about product and service innovation. On the other hand, scholarly research on design science (e.g., Hevner et al., 2004) has emphasized knowledge generation (Baskerville et al., 2015). Scholars have also acknowledged the interdependence between industry practice and scholarly research (Purao et al., 2008; Sjöström & Ågerfalk, 2009) advocating for a flexible stance to design-oriented approaches.

In terms of industry practices related to design, several design-oriented approaches have emerged to generate creative solutions that acknowledge the primacy of the user. Examples include user-centered design (Norman & Draper, 1986), empathic design (Mattelmäki, Vaajakallio & Koskinen, 2014), and participatory design (Bjerknes & Bratteteig, 1995). The primary focus of these approaches is to ensure that potential users are part of the design effort to harness “the creativity of designers and people not trained in design” who are working with the designers (Sanders & Stappers, 2008). Through user-centered design (Norman & Draper, 1986), participants can lend their expertise to inform, ideate, and conceptualize products and technology (Sanders & Stappers, 2008, p. 6). Through the empathic design perspective, the design team can highlight the importance of sensitivity and incorporate participants’ daily experiences, emotions, and contexts as design inspiration (Mattelmäki et al., 2014). Through participatory design (Bjerknes & Bratteteig, 1995), designers and participants can collaborate to enhance mutual learning throughout the design process (Sanders & Stappers, 2008). We examine participatory design in greater depth because of its use in societal settings.

The participatory design movement coincided with the civil rights movements in the 70s (Bjerknes & Bratteteig, 1995; Bodker et al., 1995) and highlighted concepts such as democracy, ethics, and empowerment (Greenbaum & Loi, 2012; Bjerknes & Bratteteig, 1995; Spinuzzi, 2005; Robertson & Wagner, 2012). From these early ideals, the movement evolved to an emphasis on user involvement and prototyping (Bodker et al., 1995; Kyng, 2010), while retaining the focus on close participant interaction for designing artifacts that benefit users (Bodker & Pekkola, 2010; Kyng, 2010). Scholarly work has identified fundamental elements that underlie participation (Kensing & Greenbaum, 2012). First, it has been described as an ethical right for individuals to express their knowledge (Robertson & Wagner, 2012), suggesting that design should be carried out with participants (Iivari, 2004) in actual settings (Greenbaum & Loi, 2012; Kensing & Greenbaum, 2012). Second, scholars have recognized that participants’ situated knowledge is essential (Greenbaum & Loi, 2012; Kensing & Greenbaum, 2012), building on the ethical stance that multiple voices must be heard (Robertson & Wagner, 2012). Finally, scholars have emphasized the need to empower participants (Spinuzzi, 2005; Bjerknes & Bratteteig, 1995) in order to enhance their own situation (Greenbaum & Loi, 2012). We note the overlap between these ideas and the facets of social inclusion reviewed earlier.

Next, we consider design-oriented approaches rooted in scholarly research. These often take the form of research methodologies with an emphasis on knowledge generation via the design of an artifact (e.g., Hevner et al., 2004; Peffers et al., 2007). Scholars have described this mode of research as one that designs an IT artifact to address an organizational problem (Hevner et al., 2004; Sein et al., 2011) as an instance of a class of problems (Sein et al., 2011; Baskerville et al., 2009; Mathiassen, 2002). Several variations on this central theme point to the importance of including potential users and industry partners. For example, action design research has highlighted the ideas of guided emergence and reciprocal shaping (Sein et al., 2011). Collaborative practice research has emphasized work with practitioners to support and improve practices, such as the work reported by Mathiassen (2002). Another approach, described as soft design science (Baskerville, et al., 2009), draws on the soft systems approach (Checkland, 1999) to promote debate about options, working with users and iterations. We examine action design research in greater depth because of its potential for working with marginalized populations.

The action design research approach conceptualizes design as guided emergence (Sein et al., 2011 p. 44) with early and ongoing participation from industry partners. To achieve this, Sein et al. (2011) proposed the principle of mutually influential roles drawing on the tenets of action research (e.g., Baskerville, 1999; Davison et al., 2004; Susman, 1983). They also emphasized mutual learning, recognizing the contributions of industry partners and practitioners. Although they acknowledge the importance of working toward a class of problems, they privileged the context and problem instance. This ensures that the situated concerns and nuanced understanding of the problem, as experienced by the industry partners and potential users, can influence both problem understanding and solution design. Recent efforts exploring the use of action design research in actual research projects (Haj-Bolouri et al., 2018) have pointed out that this need to balance contributions from industry partners and researchers can manifest, for example, in project pacing and in the emphasis on the instance versus class of problems and solutions. Approaches such as action design research and participatory research point to the possibility that design-oriented approaches can incorporate the ideals of user empowerment (Zimmerman & Warschausky, 1998) and user involvement through the right to participate (e.g., Bjerknes & Bratteteig, 1995; Iivari, 2004; Robertson & Wagner, 2012; Spinuzzi, 2005), surfacing multiple voices (Robertson & Wagner, 2012) and privileging situated knowledge (e.g., Greenbaum & Loi, 2012; Kensing & Greenbaum, 2012). This brief review points out that designoriented approaches (industry practices as well as scholarly research) hold considerable promise for increased social inclusion of marginalized populations in design efforts.

## 2.4 The Need to Enhance Design-Oriented Approaches to Address Social Inclusion

The potential for addressing social inclusion concerns with design-oriented approaches is clear. For instance, the interventionist perspective and the action-oriented stance inherent in design-oriented approaches present the possibility of “situating the work on-the-ground, so that the real lives of real people will permeate” our efforts (Trauth, 2017, p. 9). This stance makes designoriented approaches an appropriate vehicle for inviting contributions from individuals and working with them to shape the design of solutions. Several studies have demonstrated the use of design-oriented research approaches with different marginalized groups, e.g., children with autism spectrum disorder (Frauenberger et al., 2011), young people with complex needs (Hart et al., 2020), people with dementia (Hendriks et al., 2015), children in hospital and people with chronic pain (Waycott et al., 2015), and people with chronic illness (Twomey et al., 2020). Other examples include healthcare for vulnerable populations (Sjöström et al., 2022) and for elderly people with cognitive impairment (Mettler et al., 2017). Despite such examples, much prior work has pointed to specific examples that describe the need for the different facets of social inclusion—self-determination, belongingness, and social capital—to enhance the execution of designoriented approaches to work with marginalized groups.

The need for the first facet of social inclusion, selfdetermination, has surfaced in several guises as researchers have attempted to work with marginalized groups. In some cases, this has manifested as difficulties in communication that acted as obstacles to voicing opinions (Culén & van den Velden, 2013; Hendriks et al., 2015), or unintentionally exposing vulnerabilities or disempowering participants from marginalized groups (Waycott et al., 2015). Other studies have pointed to the challenges of ensuring continuous consent to participate (Culén & van der Velden, 2013), adapting to ethical challenges in the moment (Ortiz et al., 2019), and leveraging the limited skills that researchers may have for working with marginalized people (Myers et al., 2020). The need for the second facet, belongingness, has been demonstrated in different ways as part of the work that scholars have done with marginalized groups. Some researchers have pointed to specific problems such as relating to the participants’ situations, their roles, and obligations (Hendriks et al., 2015; Ho et al., 2011; Twomey et al., 2020). Scholars have also emphasized the need to manage group dynamics and social settings in design work (Culén & van der Velden, 2013) and have pointed to the fundamental need for humanity and the importance of emphasizing and understanding the feelings of the participants (Twomey et al., 2020). The need for the last facet, social capital, has also been clearly recognized. Some research has pointed to the importance of the role of marginalized individuals within networks and the perspectives that different stakeholders may present and how these needs and expectations may be in conflict (Frauenberger et al., 2011; Waycott et al., 2015). Other studies have indicated how the complexity and severity of the problems faced by marginalized populations require relationship-building efforts (Mettler et al., 2017).

The arguments and examples point to the importance of explicitly acknowledging the different facets of social inclusion when conducting research in general, and particularly with design-oriented approaches. If we ignore the theoretical foundations of social inclusion, we face the risk of simply following a privileged perspective (Sprague & Hayes, 2000) without questioning how it may adversely impact how research is conducted when working with marginalized groups. Scholars in the IS discipline have started to acknowledge such concerns broadly as the need to recognize the nuances of the problem itself (Majchrzak et al., 2016). We point more specifically to important challenges that must be acknowledged and overcome to perform design-oriented research with marginalized groups. Core elements of design-oriented approaches as currently outlined and practiced (e.g., Bodker et al., 1995; Sein et al., 2011) provide limited guidance to researchers in this regard. Therefore, our intent is to explore whether and how design-oriented approaches can be enhanced when working with marginalized populations with a view toward addressing social inclusion.

## 3 Research Approach

The empirical basis for our work is a multiyear project aimed at designing and developing IT-based artifacts and interventions for individuals with intellectual and developmental disabilities (IDD) (a marginalized group) to facilitate their transition from school to work. In this section, we outline the setting, introduce the larger research project, describe how we selected the cases, develop the rationale for examining the research process (instead of the product), and outline our data collection and analysis efforts.

## 3.1 Setting: Individuals with Intellectual and Developmental Disabilities

Intellectual and developmental disabilities are described as challenges that are “usually present at birth … that uniquely affect the trajectory of the individual’s physical, intellectual, and/or emotional development” (NIH, 2021). According to the American Association of Intellectual and Developmental Disabilities, IDD is “characterized by significant limitations in both intellectual functioning and in adaptive behavior, which covers many everyday social and practical skills” (AAIDD, 2022; Schalock et al., 2021).<sup>1</sup> Estimates place the numbers of people with IDD at \~7 million in the US or \~200 million globally, which represent 1% to 3% of the population (Special Olympics, 2022; Friedman et al., 2018).

Scholarly conceptualizations of IDD have evolved (Oliver, 1996). Early efforts relied on the characteristics of the individual and the diagnosis, illness, or injury (a “medical” conceptualization) as the cause of disability. Later scholars criticized the “medical” model and suggested a “social” conceptualization, i.e., locating the source of disability in socially created barriers rather than individual impairments, pointing out that countering disabilities requires removal of these barriers. More recently, a “relational” understanding (combining the medical and social perspectives) has been proposed (Shakespeare, 2004; Norwegian White Paper, 2016) that suggests that disabilities arise at the intersection of an individual’s preconditions and the requirements the environment poses for the individual (Shakespeare, 2004; Goodley, 2001). Goodley and Rapley (2001) describe this as a poststructuralist perspective, where IDD is seen as a socially produced phenomenon that places “impairment” in a discursive world to understand the challenges faced by persons with IDD.

Ideas related to social inclusion have been an enduring concern for people with IDD (Louw et al., 2020; Mithen et al., 2015), who continue to face obstacles to inclusion in different spheres of society (Power, 2013). The normalization movement<sup>2</sup> (Nirje, 1969; Wolfensberger, 1983) was instrumental in surfacing these challenges. The motto “nothing about us without us” (UNDP, 2021) highlights the importance of participation and involvement and emphasizes that people with IDD know best how to live the life they want to live (Charlton, 2000). Despite such recognition (Cobigo et al., 2012), high rates of social isolation persist for individuals with IDD (Bigby et al., 2018; Perez & Crowe, 2021; Grung, 2020) with obstacles that continue to limit participation in work, education, and communities (Cavanagh et al., 2021; Overmars-Marx et al., 2014; Verdenschot et al., 2009).

The facets identified as part of our review of the social inclusion puzzle (see Section 2.1) remain relevant in this setting. Self-determination (being the primary causal agent enabling individuals to exercise autonomy without unwarranted influence) (Deci & Ryan, 2002; Rotter, 1966) is often considered a best practice (Soresi et al., 2011) and a focus of disability services (Wehmeyer, 2007). Belongingness (a feeling of acceptance within the collective and being a valued and respected member of the group) (Baumeister & Leary, 1995; Mahar et al., 2013) is seen as important to promote the feeling of being an “insider” for individuals with IDD who want to be part of a group where they can receive and contribute support (Simplican et al., 2015; Strnadova et al., 2018). Social capital (recognition of mutual exchange building on the recognition of competence and the norms of reciprocity and trust) (Portes, 1998; Putnam, 2000) is seen as a critical mechanism to establish reciprocity and trust (Bates & Davis, 2004; Bollard, 2009) and recognize individuals with IDD as competent and capable of playing a social role (Overmars-Marx et al., 2014).

## 3.2 The Research Project and Selection of Cases

The research project we drew upon for our empirical work was conducted in this setting. The immediate goal of the project was to facilitate the transition from school to work for individuals with IDD. <sup>3</sup> The project team sought to do this by designing and developing IT-based artifacts and interventions to address specific problems. The project was carried out in a Scandinavian country, where individuals with IDD number in the tens of thousands, according to official reports (Meld. St 8. 2022- 2023). Of these, about 75% remain without access to a productive working life with falling rates of participation in the labor force.<sup>4</sup> Preliminary work that inspired this research project (Meld. St 8. 2022-2023; Reinertsen, 2012) along with prior research (Papay & Bambara, 2014; Shogren et al., 2015b) have convincingly shown that the transition from school to working life remains a decisive milestone for work inclusion.

To address this problem, our work included efforts to (1) identify barriers to work participation, (2) define possibilities for new solutions, (3) design and develop IT-based artifacts and interventions, and (4) evaluate these, working with potential users and different stakeholders. The project team consisted of researchers from multiple disciplines—including nursing, disability studies, service design, and others— managers from multiple local municipalities, software design professionals, and representatives from the National Association of Persons with IDD. As the project began, the research team worked with individuals with IDD as well as their support networks, to identify directions for designing and developing IT-based artifacts.

As we pursued several possibilities of designing ITartifacts in this research project, our work presented the opportunity to consider multiple “cases” for empirical investigation and reflection. To develop the principles presented in this paper, we focused on the research process rather than the artifacts being designed. There were multiple reasons for this choice: Members of the project team clearly expressed that the eventual goal of greater social inclusion for individuals with IDD could not be appreciated unless the research team addressed social inclusion concerns during the research process itself. We also realized that the two arenas—(1) moving toward greater social inclusion as a project outcome and (2) practicing social inclusion during the research process—are intrinsically interwoven. However, they may be analytically distinct in that each has a different scholarly discourse. Exploring both arenas would have required us to continually disentangle the two in our presentation and our readers to switch contexts between the outcome and process. <sup>5</sup> Our rationale echoes the debate elsewhere (Walmsley et al., 2018) that emphasizes that process matters, and although the eventual goal is to move beyond the first generation of inclusive research, questions about the research process are important (Nind & Vinha, 2014).

With this decision to focus on the research process, we examined three cases from the project, selected due to their longevity (excluding directions discarded), potential (retaining cases with a promise of impact), and outcomes (progress beyond low-fidelity prototypes). Figure 2 summarizes the three cases and timelines.

Work on each case progressed in parallel following the action design research methodology (Sein et al., 2011) to design, develop, and continually evaluate IT-based solutions. The first case focused on the design of an IT-based solution to assist individuals with IDD in the use of public transport, a challenging concern (McMahon et al., 2015) that individuals must overcome to assert their independence and is often a prerequisite for gaining employment. The second case dealt with the design and development of an ITbased solution to assist individuals with IDD to communicate with their support network (Meininger, 2006) (by augmenting an existing app to share individual experiences). The third case centered on the design and development of an IT-based solution as a career support tool that individuals can use to articulate and present interests, skills, and abilities visually and to reflect upon and articulate potential life directions (Shogren & Wehmeyer, 2020). Appendix A briefly describes the three cases.

## 3.3 Generating Empirical Insights

To generate the empirical insights, we engaged in data collection and reflections in parallel with the design work in each case. <sup>6</sup> Data analysis efforts followed replication logic. First, we derived descriptive statements about the research process in each case, with an emphasis on concerns related to social inclusion. We compared these statements across cases, “to confirm or disconfirm the inferences drawn from previous ones” (Eisenhardt & Bourgeois, 1988, p.818) in a cumulative fashion (Eisenhardt, 1989; 1991). The resulting, generic versions of descriptive statements were interpreted in light of prior work related to social inclusion (e.g., self-determination, belongingness, and social capital), and design-oriented approaches (e.g., participatory design and action design research). Figure 3 summarizes the process to generate these insights.

![](/api/attachments/WG8HNGWK/fulltext/images/ca9d6ffa86d789b8de66d4fa2aaf171ae2fd927dfede9394092c2174cc33cc54.jpg)  
Figure 2. The Overall Project and Selection of Cases

![](/api/attachments/WG8HNGWK/fulltext/images/2a93d634feb433db94932013e0328e75d79348cd92b4682bc2acee92afffc4a2.jpg)  
Figure 3. Generating Empirical Insights

More specifically, we collected three kinds of data: (1) interviews with individuals with IDD, (2) field notes from researchers, and (3) reflections from individuals in the support network. All data was obtained in the language of the participants, transcribed, and analyzed in the original language as long as possible by keeping the data in the original language during the first phase of analysis following guidance from prior work (van Nes et al., 2010). The data was then translated into English for further analysis. During this phase, we returned to the original transcripts in the source language as needed to ensure common understanding and closeness to the data (van Nes et al., 2010). The following excerpts present examples of our data:

We prepared so well. Still, this [drama workshop] was such an awkward experience … It’s extremely important to build a social relationship and our own understanding of the participants’ needs and abilities to enable user involvement.

(an excerpt from the field notes, captured by the researcher after conducting the workshop, as part of Case 1)

So, it works really good, I think that at least … I find the app to be very good. It works at work ... and in my home. ... It, and I believe it is really good, for me really. (an excerpt from an interview with a participant, conducted at a community-based housing, as part of Case 2)

I perceived all the students to be very engaged, compared to what they have shown before. The fact that one student chose on his own initiative to add more pictures was surprising, as this student normally tries to do as little as possible. (an excerpt from a reflection by a teacher, after conducting a workshop at a school, as part of Case 3)

Appendix B gives additional examples. The total volume of data was similar across cases although the distribution across sources was different. In addition, we relied on work products (e.g., presentations and meeting notes for Cases 1 and 3 as well as work documents for Case 2) to add context during data analysis. Table 2 summarizes the different types and total volume of data collected.

Because of the intense involvement of the research team with the underlying research efforts, data analysis followed the data collection phase. Analysis progressed through three stages: identifying codes for each case, identifying code clusters and comparing across cases, and interpreting these findings through prior work. In the first stage, open coding (Bryman, 2016; Charmaz, 2006; Holton, 2007; Saldaña, 2015), one author led the effort to code the data followed by discussions of the results (first, for the data from one source, followed by data from multiple sources, and then for a case), which allowed all authors to participate in assessing and refining the emerging codes. As open coding progressed, saturation (Strauss & Corbin, 1990) was apparent as the number of new codes (which started with 24, 19, and 8 new codes from the first three documents in the first case) dropped to near-zero numbers of new codes (just 1 or 2 codes for the eleventh document), with zero new codes for the last five documents. Table 3 shows examples of source extracts and codes.

In the second stage, we generated code clusters to identify higher-order concepts in an iterative manner. However, our intent was not to “build” theory; instead, our efforts were similar to the account by Rivard (2021) and the commentary by Lee (2020). The result of this stage was descriptive statements related to social inclusion challenges for each case, e.g., “using different research techniques can help overcome communication barriers,” “feeling valued simply by participating in the research project,” and others. As we examined these statements, we noted significant overlaps across the cases. A reflective synthesis followed, drawing on our personal engagement with the cases, which resulted in more generic versions of these statements.

Table 2. Summary of Data Collected from the Cases

<table><tr><td>Source*</td><td>Case 1</td><td>Case 2</td><td>Case 3</td><td>Total</td></tr><tr><td>Interviews with individuals with IDD</td><td>Oct 2019 - Nov 201916 interviews,93 pages, 23,916 words</td><td>Sept 2019 - Sept 20204 interviews, 48 pages,7,445 words</td><td>Dec 2019 - Sept 202011 interviews, 45 pages,15,301 words</td><td>31 interviews,186 pages,46,662 words</td></tr><tr><td>Field notes from researchers</td><td>Oct 2019 – May 202011 documents, 5 pages,1,858 words</td><td>Aug 2019 – Sept 20207 documents, 2 pages,1,333 words</td><td>Dec 2019 – Sept 20206 documents, 2 pages,1,044 words</td><td>24 documents,9 pages,4,235 words</td></tr><tr><td>Reflections from the support network</td><td>-</td><td>Aug 2019 – Sept 20207 documents, 70 pages,22,861 words (notes from conversations)</td><td>Feb 2020 – Oct 202013 documents, 7 pages,2,942 words (reflection notes)</td><td>20 documents,77 pages,25,803 words</td></tr><tr><td>Other data</td><td>Presentations,meeting notes</td><td>Working documents</td><td>Presentations,meeting notes</td><td>~</td></tr><tr><td></td><td>27 documents,98 pages,25,774 words</td><td>18 documents,120 pages,31,639 words</td><td>30 documents,54 pages,19,287 words</td><td>75 documents,272 pages,~76k words</td></tr></table>

Note: \* See additional examples in Appendix B.

Table 3. Examples of Open Coding

<table><tr><td>Source</td><td>Extract</td><td>Code(s)</td></tr><tr><td>Interviews with individuals with IDD (Case 3)</td><td>“I believe it is important that they listen to my answers, so that I get a good, so that I feel that I get a good response.”</td><td>Feeling of being appreciated</td></tr><tr><td>Field notes from researchers (Case 2)</td><td>It was interesting to get to know how they use the communication support tool together with the young people and formulate the text and content based on what the young people find interesting.</td><td>Assistance from support network</td></tr><tr><td>Reflections from the support network (Case 3)</td><td>“I think that the humor that is used and the pleasant and ‘informal’ setting that you create each time contributes greatly to them being relaxed, daring to talk and to convey their opinions, and have a continued desire to follow this further.”</td><td>Importance of socializing</td></tr></table>

In the final stage, we examined the findings by returning to two streams of prior work—key facets of social inclusion and design-oriented approaches (see Section 2)—to explore whether and how the findings clarified, added to, refined, or questioned any concepts or suggestions from prior work. As an example, our findings reflected recommendations in prior work about selfdetermination (e.g., ensuring that individuals from the marginalized groups are part of the conversation), and extended problems noted in prior work about the use of design-oriented approaches (e.g., difficulties in reaching shared problem awareness). This stage allowed the authors to reengage with the literature and provided opportunities to reframe the findings, where necessary. As another example, we noted that problems related to enrolling external actors were acknowledged (albeit with different descriptors) in prior work related to social inclusion (social capital) as well as design-oriented research (situated understanding versus class of problems). The resulting empirical findings were captured as 10 distinct themes linked to prior work. Appendix C summarizes these and provides links to prior work.

## 3.4 Deriving Principles

The empirical findings provided the basis for the last step, which required a conceptual move from empirical findings (descriptive statements from the three cases, supported by prior work) to principles (prescriptive statements about practicing social inclusion when conducting design-oriented research).

It is important to clarify the nature of the principles we developed because ideas about design principles are a contemporary research focus (Gregor et al., 2020) in design-oriented approaches. Our effort is not to derive such design principles about the IT artifacts or to ensure that user needs are incorporated in the design. Instead, our efforts are closest in spirit to several prior efforts by IS scholars who have suggested “principles to clarify a research genre” (e.g., Myers & Klein, 2011). There is, however, one key difference. The principles we developed were aimed at a particular goal: principles for a socially inclusive design-oriented research process. To communicate this intent clearly, we examined the different ways scholars have used the phrase “principles” or “design principles.” Table 4 describes each, along with a brief example that surfaces these distinctions. The last row in the table points to the focus of this research: achieving a goal (greater social inclusion) during the application of a research genre (design-oriented research) in a particular context (working with marginalized populations).

Table 4. Different Types of Principles

<table><tr><td>Type</td><td>Purpose</td><td>Example</td></tr><tr><td>General design principles</td><td>Providing broad design guidelines (e.g., interactive systems—Shneiderman, 1987).</td><td>Enable frequent users to use shortcuts (from Shneiderman, 1987).</td></tr><tr><td>Principles for the process of designing</td><td>Providing guidance to developers to ensure software design and engineering practices are followed appropriately.</td><td>User-centered agile software development should be based on separate product discovery and product creation phases (from Brhel et al., 2015).</td></tr><tr><td>Design principles for a class of artifacts</td><td>Providing guidance to the designers about the features or structure of artifacts that belong to a class (Hevner et al., 2004).</td><td>Provide features to store and categorize ideas, so that the system affords noticing and bracketing to users in environmental sustainability transformations (from Seidel et al., 2017).</td></tr><tr><td>Principles to clarify a research genre</td><td>Providing guidance to researchers by clarifying a research genre (e.g., Klein &amp; Myers, 1999; Yin, 2003; Myers &amp; Klein, 2011; Hevner et al., 2004).</td><td>The principle of revealing and challenging prevailing beliefs and social practices (from Myers &amp; Klein, 2011).</td></tr><tr><td>Principles to achieve certain goals during the conduct of research</td><td>Providing guidance to researchers to achieve certain goals (greater social inclusion) during the conduct of research in a genre (design-oriented research) in a particular context (working with marginalized populations)</td><td>Principles to facilitate social inclusion during the conduct of design-oriented research (the focus of our work)</td></tr></table>

Table 5. Principles to Facilitate Social Inclusion

<table><tr><td>#</td><td>Principle</td></tr><tr><td>1</td><td>Principle of respecting multi-perspective problem ownership and integrated solution design</td></tr><tr><td>2</td><td>Principle of surfacing emic contributions to guide artifact design</td></tr><tr><td>3</td><td>Principle of leveraging the support network to shape artifact design and refine research conduct</td></tr><tr><td>4</td><td>Principle of customizing design-evaluate cycles with inclusive practices</td></tr><tr><td>5</td><td>Principle of pursuing authenticity in research collaborations</td></tr></table>

With this clarification, we moved from empirical findings to principles by (1) locating problem-solution pairs in our findings to articulate lessons for future researchers engaged in design-oriented research, (2) identifying exemplars across cases to point to specific operationalization of the lessons, and (3) further intensifying our engagement with the literature to highlight important conceptualizations and theoretical precursors to elaborate and support the principles. For example, we noted that a cluster of empirical findings (See Appendix C, Theme 2, contributions in the form of anecdotes, experiences, and insights, Theme 3, contributions in the form of reflections about the research problem and process, and Theme 9, participation based on personal reasons) may suggest that it is important to pay attention to “emic contributions” during the research process (see Appendix D for the mapping between empirical findings and the principles).

This led us to return to the data to identify examples that can illustrate possibilities for applying the principle. We also engaged with the literature to highlight how the key facets—social capital and self-determination— manifested as the need for sustained efforts and mutual exchange among members of a group (Bates & Davis, 2004, Bollard, 2009), having a voice, and being able to make decisions (Deci & Ryan, 2002; Niemiec & Ryan, 2009).

The work in this stage, therefore, required not only engagement with prior work but also significant reflection and introspection that contributed to the emergence of new frames and the discovery of evocative labels for each principle. During the iterative process we followed to develop the principles, it was apparent that the empirical grounding and engagement of the research team in the underlying design-oriented research efforts were indispensable, as it allowed the authors to provide depth and richness to each principle. The elaboration of each principle, therefore, includes not only pointers to prior work but also demonstrates links to the empirical grounding with illustrative quotes. We articulate and elaborate these next.

## 4 Principles to Facilitate Social Inclusion

From the review of prior work, it should be clear that the nuances of social inclusion are such that any principles we develop cannot address the entire breadth of possibilities to facilitate greater social inclusion. Nor is this our claim. The principles we develop are derived from the empirical findings from our multicase investigation. Appendix D provides the readers with a window into the path from the empirical findings (descriptive) and the principles (prescriptive). Table 5 summarizes the principles,<sup>7</sup> which we elaborate next, with pointers to prior work and illustrative quotes.

## 4.1 Principle of Respecting Multi-Perspective Problem Ownership and Integrated Solution Design

The inspiration for this principle is the realization that “problems” faced by individuals in marginalized populations tend to be large and complex (Bigby et al., 2010; Majchrzak et al., 2016; Mettler et al., 2017; Simplican et al., 2015). The design work to address these ill-formulated, wicked problems (Rittel & Webber, 1973) can result in “solutions” that disrupt existing roles and responsibilities, demand new policies and funding, and challenge the value priorities of different actors (see Bailey & Osei-Bryson, 2018). When such concerns arise in organizational settings, the “problem owners” may be invited for a conversation or to be a part of the research team (see, e.g., Sein et al., 2011, p. 40). In contrast, when working with a marginalized population, the research team is faced with diffused problem ownership across the complex network of stakeholders (Frauenberger et al., 2011; Waycott et al., 2015). A single stakeholder may often find it difficult to assume ownership of the complete problem or take on the responsibility for designing a solution. In most communities, a network of professionals, public and private organizations, and state agencies are responsible for delivering services to marginalized populations (Overmars-Marx et al., 2014). It is this complex set of stakeholders who must participate in defining the problem and designing new solutions (Benton & Johnson, 2015).

This principle, therefore, directs attention to an important element of the research process: acknowledging established norms and roles (Portes, 1998) within this network of actors. These norms and roles define a sphere where individual actors can hold and activate various forms of social capital to initiate a change in the status quo. Participating in a conversation with this network of actors can directly impact the ability of individuals from marginalized groups to secure benefits (Cobigo et al., 2012; Portes, 1998). To promote this participation, the research team must play an active role in bridging: connecting individuals from the marginalized groups to actors in the network (Almedom, 2005; Overmars-Marx et al., 2014; Putnam, 2000), facilitating dialog among actors dispersed across different organizations, and enabling work toward shared objectives to address the problems of the marginalized group (Putnam, 2000). These concerns, which we describe with the phrases “problem ownership” and “integrated solution design” remain relevant throughout the research process, from early stages of problem definition to later stages, where evaluation and implementation possibilities are considered.

The problem of problem ownership surfaced several times in our empirical investigation. Stated simply, this means that it is important to convince the stakeholders to take on some responsibility to “do something about it” instead of pointing to others to solve the problem. Consider Case 1 (transportation support tool). Here, the problems that the individuals with IDD faced were seen simply as unique and idiosyncratic (e.g., traced to specific concerns such as short delays, missed connections, or unforeseen interruptions). This illdefined problem space (although experienced by individuals with IDD as extremely difficult and challenging) was never completely “owned” by any actor within the transportation ecosystem. One of the stakeholders acknowledged this directly:

The number of involved actors in this project makes it complicated to identify who’s the owner of the problem and the solution or if there’s even someone who wants to take on either the problem or the solution. Everyone agrees [that there is a problem] … but who should solve it?

Similar challenges were seen in Case 3 (career support tool). Here, problem complexity was traced to the many services that different organizations offer to individuals with IDD. The career support tool was intended to encourage choices from individuals with IDD, sometimes based on the services available, and at other times, beyond these services. For the stakeholders, this presented questions about how to work with other agencies in the network and how to work within their own and national mandates while responding to the possibilities voiced by individuals with IDD. It was therefore essential to work with different stakeholders to gain insights into different aspects of the problem. One researcher noted:

It went fine to explain the transition but, as pointed out, it’s easy to get stuck in the big problems in connection to the transition. When do the problems begin and end, how should we define the problem, and how do we decide who’s most important to assist?

Potentially useful approaches to overcoming the problem of problem ownership were thus identified as simply acknowledging the quandary, facilitating continued dialog among the stakeholders, ensuring the presence of individuals from the marginalized groups with the stakeholders, and helping the group (re)imagine how different parts of the problem could be addressed by different stakeholders.

The corollary is the idea of integrated solution design. It asks stakeholders to demonstrate willingness and exercise the ability to move toward such a solution. Here, the effort of the research team is directed at enrolling the different stakeholders to transition from the old ways of working to a new set of roles and responsibilities. This can be challenging because no single stakeholder may wish to act unilaterally. We observed that although the research project had involvement from the marginalized group, participation from several organizations, and the surrounding community in both planning and research conduct, solution commitment (using the artifact being designed as the anchor) was difficult to achieve. Regarding Case 1 (transportation support tool), the research team was able to conceive a first solution. However, attempts to design and develop the solution led to difficult conversations and surfaced obstacles. An excerpt from the field notes from a researcher illustrates this:

They were also very positive, but were also concerned about the challenges of turning this into a service. One idea might be to persuade them to do a job. Then we can present our findings as a design brief and give an assignment to the Agency to develop and possibly implement as it is in their mandate.

Therefore, the research team curbed their ambition and instead vetted other ideas with different stakeholders. As conversations progressed, several complexities surfaced to address the transportation problems for individuals with IDD, such as coping with uncertainty, demands on memory, and obstacles to verbal comprehension. An excerpt from the field notes illustrates how the research team explored alternative solutions to secure commitment:

The idea is to twist the focus of the innovation from management of transportation towards a focus on management of unforeseen situations (stress/coping). One of the ideas centers on use of VR/AR in connection to learning how to deal with difficult situations, such as for instance missing the bus or getting off at the wrong bus stop.

For Case 3 (career support tool), this concern manifested slightly differently. Although benefits for the marginalized group were easy to articulate (e.g., a move toward increased autonomy), it was challenging to make a business case and find a solution owner. The emphasis on transition (from school to work) meant that several stakeholders at different levels were involved (i.e., municipal, regional, and national), but it was not straightforward to convince any of them to be the primary owner.

Table 6. Principle of Respecting Multi-perspective Problem Ownership and Integrated Solution Design

<table><tr><td colspan="2">Throughout the research process, cultivate a network of stakeholders along with the marginalized groups to define the problems and develop a commitment to integrated solution design.</td></tr><tr><td>Guidelines</td><td>Examples from the empirical investigation</td></tr><tr><td>1. Encourage problem ownership</td><td>Acknowledge the problem of problem ownershipFacilitate ongoing dialog among the stakeholdersEnsure presence of the marginalized group with the stakeholdersHelp different stakeholders (re)imagine ownership of parts of the problem</td></tr><tr><td>2. Foster commitment to integrated solution design</td><td>Accept difficulties with ambitious, comprehensive solutionsAllow stakeholders to contribute to workable solutionsArticulate potential benefits for each stakeholder</td></tr></table>

We needed to articulate how the artifact being designed could not function as an isolated element; instead, it needed to be placed in the larger network of practices and capabilities of the stakeholders. Excerpts from conversations with two stakeholders illustrate how the team tried to articulate potential benefits to convince different stakeholders, and explore different business models:

Cost benefits with improved transitions—for instance, if five persons go directly into work after high school, then they can save half a position in a day care center … if the student isn’t offered a position, it might result in one of the parents not being able to work or only partially—a cost for the society.

Regarding payment/financing, I noticed this especially with teaching aids and assistive technology … Here I think there are some established paths that we can walk without stepping on new ones.

Potentially useful approaches to address the resistance to solution commitment thus included accepting difficulties with ambitious solutions, allowing the stakeholders to contribute more workable solution alternatives, and ensuring that potential benefits are articulated differently for different stakeholders, Table 6 summarizes this principle.

## 4.2 Principle of Surfacing Emic Contributions to Guide Artifact Design

This principle is inspired by the recognition that individuals from marginalized groups possess unique skills and abilities (Lemay, 2006; Shakespeare, 2004) and that different individuals (or even the same individual in different circumstances) can express these abilities in a number of ways (Cobigo, 2012; Lemay, 2006; Simplican et al., 2015). The ideas of individual differences have been emphasized by IS scholars as well (Trauth & Connolly, 2021). Much prior work has stressed the ethical right of participants to express their knowledge (Robertson & Wagner, 2012). Scholars also point out that design efforts that use this knowledge should enhance the situation of participants (Greenbaum & Loi, 2012). However, such calls implicitly rely on the physical, cognitive, and emotional ability of these participants to contribute to problem solving (Hendriks et al., 2013). This can be demanding for individuals in marginalized groups (as we found in the cases we investigated).

Therefore, this principle suggests that researchers go beyond traditional stereotypes (Pelleboer-Gunnink et al., 2021; Werner & Abergel, 2018) that merely view individuals with IDD in relation to the norms and standards defined by the majority and instead view each individual as a source of solutions (Nind & Vinha, 2014). It alerts the research team that a socially inclusive design-oriented research process requires sustained efforts (Bates & Davis, 2004; Bollard, 2009) to ensure that individual participants are valued for their contributions, which surface their emic perspectives. This calls for a process characterized by trust (Portes, 2008; Putnam, 2000; Western et al., 2007), a positive attitude, acceptance, and meaningful participation (Overmars-Marx et al., 2014). These ideas emphasize the need for a supportive environment where individuals from the marginalized group can exercise self-determination, i.e., experiencing a sense of being in control of their actions, having a voice, and making decisions (Deci & Ryan, 2002; Niemiec & Ryan, 2009). The principle recognizes that the research team must anticipate, encourage, and appreciate varied contributions that reflect the unique lived experiences of each individual in the marginalized population, seeing them as competent and trusted partners instead of limiting their role.

These concerns were visible throughout the research process. For example, the research team noted that some individuals (with IDD) expressed and elaborated problems whereas others wanted to share ideas and suggestions for possible solutions. This was noted in all three cases. Across the cases, there was diversity among the participants’ skills and abilities. However, limited reading, writing, and communication skills were more prominent during the work in Case 2.

The participants’ contributions in each case reflected their skills and abilities, shaped by the context of the case, and how they chose to express them. The nature of the contributions also varied as the cases progressed from early problem definition to later design cycles. For example, in Case 2 (communication support tool), the contributions took the form of describing experiences about the use of a preexisting solution, preferred content and displays, and content sharing. The research team facilitated this with feedback sessions about the evolving design. The following interaction between a member of the support network and individuals with IDD illustrates this:

Member of the support network: Is there anything you feel like saying about the app? Is there something that you miss, is there something?

Participant A: Yes! Recordings!

Participant B: It’s nice to make a recording if you’re on a hike or something…

Participant C: Yes, I believe that it’s because you in a way can remember better. That’s really good for me.

In Case 3 (career support tool), the contributions from the participants were slightly different and enabled an iterative transformation of a paper prototype to a highfidelity solution. The participants provided anecdotes, experiences, and insights, and included ideas, feedback on the proof of concept, structuring of information content, design elements, and insights about the user experience. The following excerpt from a designer (a member of the research team) illustrates this:

They are super engaged, something that they have been all the way that I have worked with them. This is noticed in communication with me and the team before the actual test as well, the mood is light and engaged. They are clearly more serious before and during the user test, and it seems as if they were excited and wanted to carry out the test seriously.

Another excerpt from a participant interview, responding to a question about their contribution to the project, shows how the participant was proud of the specific design ideas they contributed to the prototype:

It was that circle, and in that app I said that you could press the square and not only the logotype. … And one of the questions were about smileys or one of those sad faces. I believe that it was me who came up with that.

The empirical investigation also revealed that the researchers remained open to new possibilities about what the individual participants could contribute, including commentary and reflections at higher levels of abstraction. For example, participants sometimes commented on the research project and the research process. They also reflected on the very idea of being considered part of a marginalized group and how this could surface as problems of social inclusion. Consider Case 1 (transportation support tool). Here, the participants offered descriptive anecdotes and narratives (routines and interactions with others), experiences, and personal insights (challenges and coping strategies). All of these provided essential inputs for problem elaboration and artifact design. They also contributed commentaries about the research process itself and reflected on concerns about social inclusion (surfacing concepts such as lack of respect, injustice, stigma, and independence).

The spectrum of contributions sometimes caught the researchers unaware. These emic accounts appeared across all phases of the research effort, as illustrated by the three participant excerpts below. The first talks about stigma, describing travel with work colleagues who had more visible disabilities. The second, from a different participant, describes a lack of respect from the transportation operator. The third, from the same participant, shares some negative emotions but highlights the decision to engage in a conversation with the researchers.

I meet people from work at the bus and so. But some of them are so loud that it is embarrassing. If they say hi and so. Hi [name of participant] and see you tomorrow, they shout. Then I think; nice now the entire bus knows who I am. … I don’t know how to say that I dislike it, without hurting them kind of. So, I just let it happen.

And one of the things that irritates me the mos with transport support services and the exchange is the little respect the operator has for the customer [the person with IDD] who will use it, because imagine if I happened to catch a plane when I finished work. Going to [National Airport] … I always book to have a good margin, but I still a see lack of respect.

We tend to think we should not be a bother. That’s probably what has made me fall into the depressive soup that I’m in now. Since we get so much help with other things, there should be no room for other things [emotions]. ... therefore I have a tendency to overanalyze ... When I got the request from the supervisor, now I thought a lot about whether it is right of me to join since I am as depressed as I was then.

Table 7. Principle of Surfacing Emic Contributions to Guide Artifact Design

<table><tr><td colspan="2">Throughout the research efforts, appreciate differences among individuals from the marginalized group, and facilitate different forms of contributions from each individual that reflect their unique experiences.</td></tr><tr><td>Guidelines</td><td>Examples from the empirical investigation</td></tr><tr><td>1.Support contributions about problems as well as solution design</td><td>Facilitate elaboration of problem experience by individuals in the marginalized groupProvide space to share anecdotes and narratives of experiences and strugglesHelp individuals in the marginalized group understand the design possibilitiesEncourage contributions of design ideas by individuals in the marginalized group</td></tr><tr><td>2.Support reflections at higher levels of abstraction</td><td>Encourage comments about the research process from individuals in the marginalized groupRespond to the desire to help others in similar situations in the marginalized groupEncourage reflections about social inclusion by individuals in the marginalized group</td></tr></table>

In another example in Case 3 (career support tool), participants shared why they felt it was important to contribute to the efforts to design the artifact. One participant pointed out how they viewed their inputs in terms of their desire to help others who might share the same problem. An excerpt from this interview illustrates this:

I can say what I mean. I like to be part of testing. And I also like to help people. I mean those that have a similar problem like me or even worse … so I really like to help them to get a job. Then they don’t have to be at home all alone and get a kind of benefit or something like that.

Participants in Cases 1 and 3 also showed an interest in the design process and proactively interacted with the research team to learn about how apps were designed and developed and sometimes also about how their design and rollout would be funded. They appeared to take this responsibility seriously and expressed (as the excerpt above shows) how they viewed themselves as representatives of others in the marginalized group who could not be there. In contrast, the participants in Case 2 (communication support tool) had fewer abstract contributions and instead focused on sharing anecdotes and narratives of experiences and struggles. These unique and emic accounts added significant richness to the research and the articulation of this principle. Table 7 summarizes this principle.

## 4.3 Principle of Leveraging the Support Network to Shape Artifact Design and Refine Research Conduct

This principle recognizes the importance of the support network in the lives of individuals from marginalized groups. Members of the support network can contribute with an understanding of participants’ situated experiences (Greenbaum & Loi, 2012), sometimes in a manner that the individuals themselves cannot. This is important because the research team may be challenged when working with marginalized populations due to communication difficulties, ethical considerations (Ortiz et al., 2019), limited knowledge of or experience working with such groups (Myers et al., 2020), and difficulties relating to the situation of the participants (Twomey et al., 2020). Members of support networks may thus be indispensable as a source of insights (Rogers & Marsden, 2013; Sitbon & Farhin, 2019; Mackert et al., 2016) that can shape the design of the emerging artifact and help refine how the research is conducted.

This principle acknowledges how people from marginalized populations rely on quality relationships (Lorentzen, 2007; Fay, 1996) with members of the support network (e.g., familial connections, volunteers, and actors from different city and state agencies) as a path to enhance self-determination (Wehmeyer, 2007). The research team can activate these relationships (Nonnemacher & Bambara, 2011) so that members of the support network can sometimes “stand-in” and help give voice to individuals who may have trouble fully expressing themselves. The research team should recognize that this can be a double-edged sword. Activating these relationships may also have an unintended effect if members of the support network cannot voice the concerns well, if their understanding is incomplete, or if they privilege their own perspective/concerns over those of the marginalized individuals (Bollingmo et al., 2005; Nonnemacher & Bambara, 2011). Therefore, the research team must be careful that working with the support network does not exclude the marginalized individuals or prevent their participation in the research effort.

This principle thus recommends that the research team leverage the support network but also remain alert to the possibility that there may be conflicts between the perspectives offered by members of the support network and the marginalized individuals themselves. Recognizing this is important because it ensures that opportunities to participate are adapted to the person’s individual skills and abilities (Cobigo et al., 2012) while enhancing the possibilities for self-determination (Deci & Ryan, 2002; Wehmeyer & Shogren, 2017).

The empirical investigation revealed several instances where the research team sought contributions from the support network (often in the presence of individuals with IDD) but also with direct interaction with these individuals (in the absence of individuals with IDD). In an example from Case 1 (transportation support tool), the research team orchestrated data collection efforts with people with IDD to understand the challenges and coping mechanisms encountered in during daily transportation. One participant with IDD described how independent participation through photovoice can facilitate a sense of freedom and autonomy. The following excerpt provides an illustration of this:

I found it fun to take photos of what I wanted in a way. Because you did not put any boundaries on what I could do. And it was dark outside so I could not take photos of flowers or so … but it was fun to have the freedom.

There were also instances where contributions from the support network were sought in the absence of individuals from the marginalized group. For example, in Case 2, (communication support tool), features of the evolving app were discussed with members of the support network, who suggested possibilities such as limited autonomy. The following excerpt illustrates this:

And then you have that with messages, and then it is not given that the user [person with IDD] can view those messages. So, then we can send messages to the mother, for instance, if it is a message that the user does not need to have or know about, because it can create worries and things like that.

In some instances, the research team noted conflicting insights from individuals in the support network (compared to others in the support network or those from the marginalized group). For example, in Case 2 (communication support tool), some members of the support network described how individuals with IDD practiced storytelling, while other members argued that individuals with IDD find it difficult to articulate their experiences. A quote from a member of the support network illustrates this:

And the same, like during the holidays, we are closed here for four weeks. And when we come back after the holiday, there are many who want to tell about what they have been doing during the holidays. And those without a language have no opportunity for that. And then we have sort of followed them during the holidays through the app and can then talk to them about what we have seen that they have been involved in and things like that. And then one can have a dialogue on things that they are not able to convey themselves.

Another member of the support network presented a different perspective and argued that individuals with IDD were not interested in memories or stories and instead were only interested in what is happening now. She built on this argument to make suggestions for the design of the evolving solution. The following excerpt illustrates:

They do not go back into the album [of photos] and look, they do not go through the photo album again, for instance they do not swipe through if you understand. They do not have that interest.

Through these experiences, as the research process unfolded, the research team began to realize how important it is to activate contributions from members of the support network as well as individuals from the marginalized group (together and separately) to ensure that significant details about the problems and potential solutions are not overlooked. This interdependence was evident most acutely in Case 2 (communication support tool), probably because of the significant role of the support network for the problems addressed. The research team noted several examples, such as assistance in creating digital content, exploring the lack of adoption among teachers and other close associates, and the interplay between the daily routines of individuals from the marginalized group and the work habits of members of the support network. One of the individuals with IDD described how his family assisted him in using the app but his teachers had not adopted it. This is illustrated by the following quote:

Yes, mom likes it very much. My sister likes it very much, and, because of school then. [name of Teacher A], she’s going to log in, and then [name of Teacher B] and they, [name of Teacher C] have the app, but they have not accessed it yet. … [Mmm, the teachers] … So they struggle with the app.

Participation from the support network also proved critically important to recruit participants, assist with arranging design activities, and obtaining consent. For example, during the initial efforts for Case 2 (communication support tool), the involvement of the support network was indispensable during the interviews with individuals from the marginalized group. This role for the support network continued when researchers sought an understanding of how the evolving app was used or not used or could be refined. The individuals from the support network helped to overcome communication difficulties. They calmed the participants to allow them to express themselves, and added context and explanations to the ideas shared by the support network was observed across all cases in a multitude of ways. It required the research team to anticipate, manage, and leverage different ways of working with the support network and individuals from the marginalized group. Table 8 summarizes this principle.

Table 8. Principle of Leveraging the Support Network to Shape Artifact Design and Refine Research Conduct

<table><tr><td colspan="2">Throughout the research process, leverage the interdependence with the support network to obtain contributions from individuals from marginalized populations as well as members of the support network.</td></tr><tr><td>Guidelines</td><td>Examples from the empirical investigation</td></tr><tr><td>1. Seek contributions from the support network and individuals from the marginalized group</td><td>Plan to obtain contributions from both groups, together and separatelyAllow the possibility of conflicting insights within and across the groupsEncourage the support network to add context and explanationsEncourage independent contributions by members of the support network</td></tr><tr><td>2. Partner with the support network for research</td><td>Allow the support network to contribute to planning the research effortsInvite the support network to take an active role in research activities</td></tr></table>

## 4.4 Principle of Customizing Design-Evaluate Cycles with Inclusive Practices

This principle is a corollary to the principle of surfacing emic contributions to guide artifact design outlined earlier. It recognizes that the research team must organize their research efforts to respond to the distinct and unique personalities of the individuals in the marginalized group (Craig et al., 2007; Shakespeare, 2004; Trauth & Howcroft, 2006) during the design and evaluation cycles. Prior scholarship has pointed out that work with marginalized populations makes several demands on researchers that they may not know how to respond to (Myers et al., 2020), such as communication challenges (Culén & van der Velden, 2013; Hendriks et al., 2015), ethical concerns (Ortiz et al., 2019), and interpersonal relationships (Culén & van der Velden, 2013; Waycott et al., 2015). In addition, design-oriented approaches call for continuous and concurrent evaluation and engagement with the stakeholders (see Sein et al., 2011). Our investigation revealed that a heightened awareness of these demands is a prerequisite when working with marginalized populations to ensure that they are not asked to meet the dominant norms of participation (Cobigo et al., 2012; Maidment & Macfarlane, 2009). Researchers have thus stressed the importance of situated knowledge (Greenbaum & Loi, 2012; Kensing & Greenbaum, 2012) and empowering participants to contribute (Spinuzzi, 2005; Bjerknes & Bratteteig, 1995). The exercise of such empowerment is a necessary but not sufficient condition. The research team must also resist the temptation to treat the participants as a homogenous group, using uniform practice across all participants, and instead personalize the research conduct across individuals, contexts, and environments (Shakespeare, 2004).

This principle acknowledges lessons from prior work that emphasize that social inclusion concerns can manifest in various ways with different individuals (Hammel et al., 2008) based on how they view their participation in terms of intrinsic motivation (Deci & Ryan, 2002). To apply this principle, the research team must identify and use appropriate techniques<sup>8</sup> that can support participants’ ability to be in control, problem solve, and express opinions—in essence, providing opportunities for self-determination and greater autonomy (Deci & Ryan, 2002; Shogren et al., 2015a). The research team must also be open to refinements in response to emergent concerns to facilitate dynamic aspects of social inclusion (Cobigo et al., 2012; Selwyn, 2002; Taket et al., 2009).

Several instances from our empirical investigation pointed out that such work (the use of new techniques, careful planning, and refinements in response to emergent concerns) requires significant resources. The research team noted that incorporating such techniques in their work required them to appreciate the different life worlds that individuals in marginalized groups inhabit. Examples of this effort were seen in all cases and during the design and evaluation cycles of the artifact. For example, in Case 1 (transportation support tool), the research team used the photovoice technique (photos as tangible representations of situations, along with interviews) (Povee et al., 2014) to reach a more vivid understanding of problems. A quote from one participant illustrates this:

It was okay to take pictures from the bus then. It’s not that difficult to take pictures. No. Just, just find that picture of a camera on the phone. So just snap away. … That’s fine, very fine.

In the same case, the researchers also organized a drama workshop that incorporated a simulated commuting experience of using a bus (based on the idea of experiencing activities with participants— Spradley, 2016). Some participants were able to relate and felt safer in this contrived setting to offer their ideas. Others indicated that they would have preferred a more realistic setting. One of the participants noted how he would have preferred injecting more realism into the workshop:

But pretending, you may think it has always been difficult, but autism … Yes, but it all depends on what it is. Like ... I like that it’s like a movie, if it’s going to be a bus it has to look a bit like a bus. Here it did not look like a bus, it looked like chairs that were put in rows. Then there was a lady who had a hat that was the wheel... She who was supposed to be a bus driver, should have had a bus driver’s clothes. Then there could have been different people on the bus who could have taught them what happens if you get into these situations. Then you have a person who talks a little loud on the phone, a person behind you who smokes, you have another.

In another example from Case 3 (career support tool), the research team used new combinations of interviews and usability testing that allowed the research team to gain knowledge of the personal interests of each participant, facilitated informal socializing, and surfaced design issues in the prototype. The combinations allowed for a more freeflowing conversation and provided opportunities for the participants to steer the conversation in different directions. An excerpt from a researcher’s field notes illustrates this:

At first, it seemed that the prototype worked well, but considering that we knew about the students’ interests, we saw that it [the prototype] did not. Our solution resulted in the interests they had not even being presented—they opted out before seeing what the categories contained. Our investigation also showed that the research team needed to plan meticulously while remaining open to refinements in response to concerns that may arise across settings, the needs and development levels of individual participants, and different contexts.

Returning to the example of the simulated bus commuting workshop in Case 1 (transportation support tool)—the researchers needed to arrange the workshop carefully, including assigning one facilitator plus one observer for each participant. With 12 individuals from the marginalized group participating in the workshop, this effort demanded significant resources and much coordination from the research team. Another excerpt from a researcher’s field notes (captured after these sessions) provides an illustration of this:

The fact that we were a facilitator and an observer for each participant gave us a better data collection, having both roles would have made it difficult to capture all the events and insights. Unfortunately, it is resource intensive and [requires] many people to coordinate.

In Case 3 (career support tool), the researchers used both low-fidelity and high-fidelity prototypes that gave the participants different opportunities to reflect on the evolving prototype (similar to Sitbon & Farhin, 2017). Planning for sharing both kinds of prototypes, choosing the participants for each, and coordinating the feedback sessions all required significant effort from the research team. For the same case, similar investments of time and careful effort were also needed to plan a workshop that included individuals with IDD along with members of the support network. This is illustrated in an excerpt from the interview with a member of the support network, (who stressed the importance of such planning):

As I said, I believe the workshops are perfectly set up with the way the designer manages it. It is engaging and fun for the students, not least the predictability of what is going to happen, which is presented in a nice way. There is also very good communication in advance of the sessions, which makes it possible for us to meet their needs in the best possible way.

All the sessions also required ongoing monitoring and often, on-the-fly adjustments. Sometimes, these adjustments followed from suboptimal results observed by the researchers; at other times, they followed from new interaction opportunities that surfaced. As the quotes above indicate, each session required significant resources and creative ways of involving participants. For example, in Case 1, the photovoice session involved resources for introducing photovoice to the employers and teachers, gaining consent from participants and close associates, demonstrating how to take photos to the participants, practicing taking photos together with the participants, conducting the interviews, and returning to conduct interviews with participants who forgot to take photos. Table 9 summarizes this principle.

Table 9. Principle of Customizing Design-Evaluate Cycles with Inclusive Practices

<table><tr><td colspan="2">• Plan, organize, and continuously refine design and evaluative cycles in response to the skills and abilities of individual participants from marginalized populations.</td></tr><tr><td>Guidelines</td><td>Examples from the empirical investigation</td></tr><tr><td>1. Incorporate novel techniques in the conduct of research</td><td>• Consider novel techniques for interaction with individuals from the marginalized group• Adapt the techniques for individual participants and different contexts</td></tr><tr><td>2. Plan meticulously and respond to emergent concerns</td><td>• Invest significant time and resources to plan the design/evaluate sessions• Monitor the interaction sessions proactively to identify problems and opportunities• Refine the format of the session to respond to emergent problems and opportunities</td></tr></table>

## 4.5 Principle of Pursuing Authenticity in Research Collaborations

The final principle emphasizes the need for authenticity in collaborating with individuals from the marginalized group, members of the support network, and other members of the research team throughout the research project. It builds on the idea emphasized in prior work that design efforts should contribute to improving the participants’ situation (Spinuzzi, 2005; Greenbaum & Loi, 2012). It consolidates key underlying threads across the other principles by bringing to the main ideas of belongingness (Baumeister & Leary, 1995) and self-determination (Deci & Ryan, 2002; Shogren et al., 2015a). It points out that research conduct should build on the ideal of authentic work with all participants (including but not limited to marginalized individuals). This includes respect and appreciation for each team member for the role they play and the contributions they make.

In our empirical investigation, we found one dominant perspective to achieve these outcomes: fostering social connections among all members of the research team. The research project is seen as an arena, where the participants can have an opinion, express that opinion, and influence the outcomes. The importance of these tactics is echoed in much prior scholarship. In groups where participants feel valued (Mahar et al., 2013), have an “inside” role in the team, and feel attached (Hall, 2010) (Cummins & Lau, 2003; Mahar et al., 2013), they experience a sense of belongingness (Baumeister & Leary, 1995) and participate based on intrinsic motivation (Deci & Ryan, 2002).

Across all three cases, we found multiple instances that demonstrated how researchers, designers, members of the support network, and the participants (individuals with IDD) attempted to cultivate these authentic collaborations. The researchers assumed primary responsibility for these efforts to value and appreciate each participant as a full-fledged member of the research group. In Case 1 (transportation support tool) and Case 3 (career support tool), there were several instances that described what the researchers were attempting to do and how the participants felt that they were being listened to and were appreciated for their contributions. An excerpt from an interaction with one of the participants in Case 3 (describing and reflecting about contributions to the solution) illustrates this:

It is because we have been listened to, and it is as if we can participate in something we have wanted to participate in. And if we had not had something to contribute with, it would not have helped so many with that app then. So, it’s like we had been sitting there with nothing. So, you have in a way had a project where you should find out what you could do better with the app.

A second excerpt, from the same case, illustrates how one of the participants found it important to note that their suggestions were incorporated into the design:

That they listen to what you say and try to see how they can twist it into what they are trying to fix [develop] so that it becomes part of the app. And you have done that by taking our suggestion into the app so that we can test again and see if it works or not.

The researchers also pointed to the importance of listening to the individuals from the marginalized group (individuals with IDD) and supporting their efforts to voice opinions. The following excerpt, also from the same case, from an interview with one participant illustrates this:

You explained rather good and then you gave everyone the opportunity to give their opinions about the app. That you did not look down on our ideas just because someone with disabilities, that you listened … That was very good.

In Case 1 (transportation support tool), several participants expressed appreciation for the different techniques the researchers used to invite participation, and how their participation in the project was different compared to work elsewhere. Excerpts from interviews with the participants illustrate this:

Yes, it is totally different. I could talk about what I had in here (points to his heart). That I do not, I do not talk like that at work. Then I do not talk about everything. Then I concentrate on work.

Yes ... she listened. ... She said, after I had responded she asked a new question. I could answer her in a way that I wanted to … I believe it is important that they listen to my answers, so that I get a good, so that I feel that I get a good response.

Data across all three cases also pointed out that it was important to go beyond seeing the participants merely as a source of information and instead acknowledge their own, different reasons for participating. For example, some participants in Case 1 (transportation support tool) indicated that they valued the freedom of the activity, others said that they valued contributing to a cause, and others indicated that they learned new things and experienced something different when attending the workshops. Excerpts from the interviews with participants illustrate this. The first describes participants’ interest in learning about designing software apps, the second talks about their interest in learning about research, and the third describes their desire to try something new:

Yes, I have learned how much you have to think (about) to be able to create an app somehow. Because I used to think that it was not really that difficult, if you could code and stuff. ... Then I do not quite understand how people manage it. So, I think it’s pretty impressive when people can actually make apps like that.

I found it interesting … I believe it was interesting to learn how you work and reflect.

I find everything fun anyway because I feel like trying something new. So, I just jumped out of my comfort zone. So, it is actually one of my goals.

Participants in Case 1 (transportation support tool) further pointed out that their contributions to the design of the evolving IT artifact were motivated by the knowledge that when it was fully designed and deployed, it could be useful not only for them but also others. Two excerpts from interviews with participants illustrate this:

Because you learn new things. And the app was ... I will at least download it when it comes to the app store. My dad is also going to download it.

Because I believe that it can assist in my daily life … I find it really nice, that I can feel safer when I will take the bus in the future.

This principle further underscores that the research project must be viewed as a new collective that presents opportunities to pursue social connections. In Case 3 (career support tool), we witnessed the frequency of these interactions intensify as the project progressed. Multiple excerpts from interviews with the support network as well as individuals in the marginalized group illustrate this. The first points to the importance of creating informal settings to facilitate such interactions, the second acknowledges the value of informal practices (e.g., having lunch together), and the third describes direct benefits such as working together and sharing ideas.

I think that the humor that is used and the pleasant and ‘informal’ setting that you create each time contributes greatly to them being relaxed, daring to talk and convey their opinions and have a continued desire to follow this further. Very good !!!

Yea, it is in a way important that we have a break where we can talk together about different things. All of a sudden, we come up with ideas about the project you have [during lunch]. So, it is a gathering where you can talk to people, make suggestions and ask if it is good with other people or not.

I think it’s best when you have several [participants] really. If you do not have good ideas then others have it, and that is really good. If I have a good idea about something, then Linn does not have it, then I can voice my good idea. Then everyone liked it.

A related experience was described by participants in the same case. Two participants pointed out how working with the same researchers over time made them more secure. The following quotes illustrate this:

It is nice that it is the same people that visit us. Instead of that you kind of present yourself one more time to those who have not attended before… Because then it is in a way like you know them better and can have a conversation. Then you do not have to share about yourself every time.

Because now I know that when I’m here it is very cozy. I enjoy it when I’m here. It was a bit scary the first time I attended. But after the first time, I realized that everything went fine and it is really just fun to be part of this.

The significance of cultivating social connections was also obvious in Case 1 (transportation support tool), where it manifested as a way to overcome any hesitation in collaborating with the researchers. One of the participants noted how individuals who were part of multiple workshops found it easier to interact and contribute. The following excerpt from the field notes by a researcher illustrates this:

This group was younger and it could be noticed that some of them found it a bit embarrassing to speak their mind. This was also a group that we only had met briefly when we presented what we were going to do. Compared to the [participants in the] other group who were older and who had been part of the photovoice, it took a longer time before it felt natural and comfortable.

The principle thus highlights both tangible and intangible benefits that accrue from authentic collaborations among all members of the research team. Table 10 summarizes this principle.

## 4.6 Applying the Principles

The elaboration thus far has described the principles, provided excerpts from our empirical investigation, and summarized a few guidelines that researchers can use to assist in their efforts to operationalize the principles. As a part of this elaboration, we have also provided pointers to prior work about different facets of social inclusion summarized earlier—self-determination, belongingness, and social capital (see Section 2). Table 11 provides a summary of this mapping between the principles we have outlined and the facets of social inclusion.

As Table 11 shows, each principle is informed by one or more facets of social inclusion. The principles (along with the guidelines and examples from our empirical investigation) thus provide more accessible pathways that the researchers can incorporate into their research conduct. As pointed out by other scholars (Aldridge, 2019; Cobigo et al., 2012), without concerted efforts, the pursuit of social inclusion remains at the risk of merely an ideology. Recognizing that marginalization is a matter of both recognition and experience (Mowat, 2015), individual and contextual aspects may need to be considered to assess the applicability of the principles. The mapping we have shown above provides future scholars with a link back to research related to social inclusion as they incorporate the principles into their own research conduct.

To apply the principles, future scholars also need to consider how they might incorporate these principles as part of their research efforts. We demonstrate the feasibility of such application for two example approaches that we emphasized in our review of prior work: action design research (ADR) (Sein et al., 2011), as one possibility of scholarly research, and the participatory design approach (Spinuzzi 2005), as an example of industry practices. Tables 12a and 12b summarize this mapping. The mapping shows prima facie evidence of the possibility of integrating our principles into existing design-oriented approaches to facilitate greater social inclusion. Although the tables outline this mapping for only the two approaches we highlighted in the review of prior research (see Section 2.3), the guidelines contained can also augment other design-oriented approaches.

Table 10. Principle of Pursuing Authenticity in Research Collaborations

<table><tr><td colspan="2">• Strive for authentic collaboration with all members of the research team: recognizing their roles in the collective, and valuing their participation and contributions.</td></tr><tr><td>Guidelines</td><td>Examples from the empirical investigation</td></tr><tr><td>1. Value each participant and their contributions</td><td>• Treat each participant as a full-fledged member of the research team• Go beyond seeing the participants merely as a source of information• Acknowledge the participants’ personal reasons to contribute</td></tr><tr><td>2. Cultivate social connections within the research team</td><td>• Recognize the research project as a collective to pursue social interactions• Cultivate durable and long-duration social connections among research team members</td></tr></table>

Table 11. Mapping the Principles to the Facets of Social Inclusion

<table><tr><td colspan="2">Facets of social inclusion (see Table 1) → ↓ Principles for research conduct (see Table 5)</td><td>Self-determination</td><td>Belongingness</td><td>Social capital</td></tr><tr><td>1</td><td>Principle of respecting multi-perspective problem ownership and integrated solution design</td><td></td><td></td><td>x</td></tr><tr><td>2</td><td>Principle of surfacing emic contributions to guide artifact design</td><td>x</td><td></td><td>x</td></tr><tr><td>3</td><td>Principle of leveraging the support network to shape artifact design and refine research conduct</td><td>x</td><td></td><td></td></tr><tr><td>4</td><td>Principle of customizing design-evaluative cycles with inclusive practices</td><td>x</td><td></td><td></td></tr><tr><td>5</td><td>Principle of pursuing authenticity in research collaborations</td><td>x</td><td>x</td><td></td></tr></table>

Table 12a. Augmenting ADR with the Principles Discovered in this Research

<table><tr><td>Phases and Principles in ADR</td><td>What is needed (to address social inclusion concerns)</td><td>Principles discovered in this research</td><td>How our principles can augment ADR for greater social inclusion</td></tr><tr><td colspan="4">Phase: Problem formulation</td></tr><tr><td>Principle: Praxis-inspired research</td><td>Problems faced by individuals in marginalized populations seem to require complex solutions, working with multiple stakeholders (Bigby et al., 2010; Mettler et al., 2017; Simplican et al., 2015).</td><td>Principle 1: Principle of respecting multiperspective problem ownership and integrated solution design</td><td>Include multiple stakeholders in conversations about problem diagnosis and to cultivate collective ownership of emerging design.</td></tr><tr><td>Principle: Theory-ingrained artifact</td><td>Not applicable1</td><td>Not in scope</td><td>Not applicable</td></tr><tr><td colspan="4">Phase: Building, intervention, and evaluation</td></tr><tr><td rowspan="3">Principle: Reciprocal shaping</td><td>Individuals from marginalized groups may not be able to achieve the accepted norms for participation (Cobigo et al., 2012; Maidment &amp; Macfarlane, 2009).</td><td>Principle 2: Principle of surfacing emic contributions to guide artifact design</td><td>Ensure that unique contributions from participants are captured and interleaved with efforts to design the artifact.</td></tr><tr><td>Members of the support network (that individuals from marginalized populations rely on—Lorentzen, 2007; Fay, 1996) can often clarify and refine their concerns.</td><td>Principle 3: Principle of leveraging the support network to shape artifact design and refine research conduct</td><td>Allow inputs from the support network to add to the articulation of concerns by individuals from the marginalized group.</td></tr><tr><td>Individuals from marginalized groups possess unique skills and abilities (Lemay, 2006; Shakespeare, 2004) that must be respected and leveraged during the research conduct.</td><td>Principle 4: Principle of customizing design-evaluate cycles with inclusive practices</td><td>Infuse research conduct with specific techniques appropriate for individuals from the marginalized group.</td></tr><tr><td rowspan="3">Principle: Mutually influential roles</td><td>The complex network of stakeholders (Frauenberger et al., 2011; Waycott et al., 2015) means diffused problem ownership and uncertainty about collaborations needed to implement solutions.</td><td>Principle 1: Principle of respecting multiperspective problem ownership and integrated solution design</td><td>Cultivate commitment to the solution design and rollout plans from all stakeholders with ongoing conversations and inputs.</td></tr><tr><td>Individuals with IDD are seen as a deviation from the norm (Pelleboer-Gunnink et al., 2021; Werner &amp; Abergel, 2018) instead of a source of solutions (Nind &amp; Vinha, 2014).</td><td>Principle 2: Principle of surfacing emic contributions to guide artifact design</td><td>Value contributions and design influences from all individuals in the marginalized group as well as the support network.</td></tr><tr><td>The relational and dynamic nature of social inclusion (Selwyn, 2002; Taket, 2009) needs to be better reflected in research conduct.</td><td>Principle 5: Principle of pursuing authenticity in research collaborations</td><td>Cultivate a sense of connection among all members of the research team, including the marginalized group, and the support network.</td></tr><tr><td>Principle: Authentic and concurrent evaluation</td><td>Communication (Culén &amp; van der Velden, 2013; Hendriks et al., 2015), ethical concerns (Ortiz et al., 2019), and interpersonal relationships (Waycott et al., 2015) remain challenging.</td><td>Principle 4: Principle of customizing design-evaluate cycles with inclusive practices</td><td>Use and adapt novel techniques for surfacing design ideas, sharing the evolving artifact, and evaluation efforts with the participants.</td></tr><tr><td colspan="4">Phase: Reflection and learning</td></tr><tr><td rowspan="2">Principle: Guided emergence</td><td>A complex network of stakeholders at different levels in communities are responsible for delivering services to marginalized populations (Overmars-Marx et al., 2014).</td><td>Principle 1: Principle of respecting multiperspective problem ownership and integrated solution design</td><td>Facilitate shaping of the artifact based on design inputs from multiple stakeholders and seek their commitment to rollout.</td></tr><tr><td>Individuals in marginalized groups have distinct and unique personalities (Craig et al., 2007; Shakespeare, 2004; Trauth &amp; Howcroft, 2006).</td><td>Principle 4: Principle of customizing design-evaluate cycles with inclusive practices</td><td>Use novel techniques customized to different individuals and different contexts to elicit design suggestions.</td></tr><tr><td colspan="4">Phase: Formalization of learning</td></tr><tr><td>Principle: Generalized outcomes</td><td>Not applicable $^{2}$ </td><td>Not in scope</td><td>Not applicable</td></tr><tr><td colspan="4">Note:  $^{1}$ The theories that inspire artifact design will be specific to the project focus and therefore beyond the scope of this paper, which deals with research process.  $^{2}$ This phase is likely to involve intense reflection from the researchers to identify generalized outcomes with few social inclusion concerns.</td></tr></table>

Table 12b. Augmenting PD with the Principles Discovered in this Research

<table><tr><td>Stages and techniques in PD</td><td>What is needed (to address social inclusion concerns)</td><td>Principles discovered in this research</td><td>How our principles can augment PD for greater social inclusion</td></tr><tr><td colspan="4">Stage: Initial exploration of work</td></tr><tr><td rowspan="3">Techniques: Primarily oriented to descriptions such as observations, interviews, visits</td><td>Individuals (or even the same individual in different circumstances) may participate differently (Cobigo, 2012; Lemay, 2006; Simplican et al., 2015).</td><td>Principle 2: Principle of surfacing emic contributions to guide artifact design</td><td>Acknowledge the differences across individuals in the marginalized group and highlight their strengths.</td></tr><tr><td>People from marginalized populations rely on quality relationships (Lorentzen, 2007; Fay, 1996) with members of the support network.</td><td>Principle 3: Principle of leveraging the support network to shape artifact design and refine research conduct</td><td>Recognize influence of and inputs from the support network to develop an understanding of the nuances of the work context.</td></tr><tr><td>Individuals in marginalized groups have distinct and unique personalities (Craig et al., 2007; Shakespeare, 2004; Trauth &amp; Howcroft, 2006).</td><td>Principle 4: Principle of customizing design-evaluate cycles with inclusive practices</td><td>Tailor use of techniques (observations, interviews, visits) to different individuals and settings to explore work context.</td></tr><tr><td colspan="4">Stage: Discovery processes</td></tr><tr><td rowspan="2">Techniques: Primarily oriented to design such as future workshops, and storyboarding</td><td>Individuals (or even the same individual in different circumstances) can express these abilities in a number of ways (Cobigo, 2012; Lemay, 2006; Simplican et al., 2015).</td><td>Principle 2: Principle of surfacing emic contributions to guide artifact design</td><td>Acknowledge differences across individuals in the marginalized group and highlight their strengths to discover design alternatives.</td></tr><tr><td>People from marginalized populations rely on quality relationships (Lorentzen, 2007; Fay, 1996) with members of the support network.Communication (Culén &amp; van der Velden, 2013; Hendriks et al., 2015), ethical concerns (Ortiz et al., 2019), and interpersonal relationships (Waycott et al., 2015) remain challenging.</td><td>Principle 3: Principle of leveraging the support network to shape artifact design and refine research conductPrinciple 4: Principle of customizing design-evaluate cycles with inclusive practices</td><td>Recognize influence of and inputs from the support network to identify design alternatives and shape the evolving solution.Tailor use of techniques (future workshops, storyboarding) to different individuals and settings to discover design alternatives.</td></tr><tr><td colspan="4">Stage: Prototyping1</td></tr><tr><td rowspan="2">Techniques: Primarily oriented to design, such as mockups, paper prototypes, and cooperative prototyping</td><td>A complex network of stakeholders at different levels in communities are responsible for delivering services to marginalized populations (Overmars-Marx et al., 2014).</td><td>Principle 1: Principle of respecting multiperspective problem ownership and integrated solution design</td><td>Cultivate ownership and rollout commitment by seeking design inputs and evaluation participation from multiple stakeholders.</td></tr><tr><td>The relational and dynamic nature of social inclusion (Selwyn, 2002; Taket, 2009) needs to be better reflected in research conduct.</td><td>Principle 5: Principle of pursuing authenticity in research collaborations</td><td>Develop genuine (not arm's length) connections with the participants during prototyping and evaluation.</td></tr><tr><td colspan="4">Note: The principles indicated as applicable to the prototyping stage may also apply in some measure to the earlier stages.</td></tr></table>

## 5 Discussion and Concluding Remarks

We begin by reiterating an important insight that we could only articulate in retrospect, following the multiyear research journey (the three cases) described in this paper. It is simply this: Working with marginalized groups with a design-oriented approach generates two parallel arenas for the research team to consider. The first arena concerns the design of specific solutions and IT artifacts in response to the needs of this marginalized population. Here, the research project may or may not pursue social inclusion (such as the work we have described) (e.g., developing an IT artifact to monitor the elderly for early detection of health problems—Tun et al., 2020). The second arena deals with the conduct and management of the research effort itself. When the research team works with individuals from a marginalized group, the pursuit of greater social inclusion remains an important concern for the second arena (research conduct) even if it is not the aim of the research project.

In other words, the research effort generates a collective that includes a multitude of researchers, external stakeholders, individuals in the marginalized group, and their support network. Pursuing greater social inclusion of the marginalized group remains a healthy concern and a goal for this collective as it engages in the research effort. Otherwise, the research team can neither engage in fruitful collaborations with individuals from the marginalized group nor respond effectively to social inclusion considerations during the design of the IT artifacts (if that is the focus of their research project). With this simple insight, we find ourselves echoing and expanding the ideas sometimes highlighted as the “nothing about us without us” movement (Charlton, 2000; Harpur, 2017; UNDP, 2021), and responding to Trauth (2017, p. 12) who points out that “[the social inclusion] orientation has implications for the research methods employed as well as for the actions and interventions that follow.”

However, such aphorisms and encouragements are not sufficient; they require translation into actionable principles and guidelines that research teams can rely on as they work with individuals from marginalized groups. The research team cannot approach the ideal of social inclusion with a dispassionate, analytical stance. Instead, as researchers, we must combine specific and ongoing efforts with personal sensitivity to address the social inclusion puzzle as we engage in the research effort.

## 5.1 Contributions

Our work has the potential to make contributions in several directions. Design-oriented research has been gaining momentum as a viable alternative for conducting research within the IS discipline over the last two decades (Hevner et al., 2004; Sein et al., 2011). The IS community has embraced it as a path toward greater relevance by tackling organizational problems and collaboration with stakeholders (Mathiassen, 2002). However, the use of design-oriented approaches to pursue important societal problems (at least within the IS field) has been limited. Although there is some recognition that the design of IT artifacts must respond to the values of marginalized stakeholders (see, e.g., Dadgar & Joshi, 2018; Purao & Wu, 2013; Sahay et al., 2017), few specific investigations have been reported, and no guidelines are available to researchers to pursue such goals.

Our first contribution is translating the complex and varied literature about social inclusion into consumable clusters of ideas for design science scholars. Through a synthesis of much prior scholarship from IS and other disciplines, we have distilled three facets of social inclusion—self-determination (Deci & Ryan, 2002; Rotter, 1966), belongingness (Baumeister & Leary, 1995; Mahar et al., 2013), and social capital (Portes, 1998; Putnam, 2000). These provided important foundations for our work and point to an understanding of social inclusion as multidimensional, dynamic, and relational (Selwyn, 2002; Taket et al., 2009) that shows how social inclusion can vary across roles and environments and evolve over time (Hammel et al., 2008). This conceptualization can provide IS scholars with specific anchors for their work that are aimed at promoting the social inclusion of marginalized groups.

The second and core contribution of our work comprises specific principles to pursue social inclusion during the research process that build on these theoretical facets. These principles highlight answers and provide pathways emphasizing (1) multi-perspective problem ownership and integrated solution design, (2) surfacing emic contributions to guide artifact design, (3) leveraging the support network to shape artifact design and refine research conduct, (4) customized design-evaluate cycles with inclusive practices, and (5) authenticity in research collaborations. They offer clear steps to incorporating social inclusion concerns into design-oriented research endeavors. At first glance, the principles may seem to encompass ideas that are “wide-ranging and somewhat obvious” (Carroll, 2003, xi). However, it is precisely these qualities that point to the need for clarification. For example, Cobigo et al. (2012) pointed out that without the awareness of and access to specific pathways, the pursuit of social inclusion will remain merely an ideology. Although some studies have outlined elements such as empathic design with attention to individual concerns (Mattelmäki et al., 2014)—for example communitybased participatory research (CBPR), with its commitment to working in partnership with participants from marginalized communities (Tremblay et al., 2018), and participatory action research (PAR), with its recognition of the capacity to participate and participantdirected improvements of practices (Kemmis et al., 2014)— clear pathways have remained difficult to articulate (Aldridge, 2017). As Walmsley et al. (2018) argue, it is necessary to move past the so-called first generation of inclusive research and the process still matters. They point out that there is a need to share insights from inclusive research practices with a wider community that can use them to make changes. Only when this is practiced, the goal of “research mak[ing] an impact on the lives of people with learning disabilities”

(Nind & Viha, 2014, p. 44) can be realized. Our work develops principles (building on different facets of social inclusion) that can be used by IS scholars seeking to make conscious efforts to facilitate greater social inclusion during the research process.

A third contribution of our work is providing an empirical grounding to the principles for facilitating a more socially inclusive design-oriented research process. Our work relies on a multiyear research project that included multiple efforts to design IT-based solutions in response to the needs of a specific marginalized population (people with IDD). Treating each effort as a case allowed us to collect primary data, which we analyzed using robust techniques (within-case and across-case analyses— Eisenhardt, 1991), thus providing an empirical grounding for the principles. Therefore, our approach of deriving the principles does not rely exclusively on conceptual argumentation and analysis<sup>9</sup> (e.g., Myers & Klein, 2011; Wynn & Williams, 2012). This is an important distinction. For example, our findings across the cases revealed efforts to refine and monitor how we conducted our research according to the skills and abilities of the individual participants—which led to the development of the principle of customized design-evaluate cycles with inclusive practices. These findings show why this remains especially important when conducting research that involves marginalized groups who have traditionally been excluded from voicing their opinions (Charlton, 2000; Harpur, 2017). The empirical grounding for our work, along with examples from multiple cases adds richness and legitimacy to the principles, emphasizing the need for specific actions (informed by prior theoretical foundations) as well as personal sensitivity (to advocate for social inclusion).

A fourth contribution of our work is the formulation of guidelines that elaborate each principle. For example, we specify two guidelines for Principle 5, authenticity in research collaborations, that point to the importance of valuing each participant and their contribution and developing social connections within the research team. Such guidelines add specific advice, unlike prior articulations of principles in other research genres that steer clear of any “procedural guidelines,” leaving this translation from the principles to specific actions to “the circumstances of each project” (see, e.g., Wynn & Williams 2012, p. 805). In contrast, the guidelines we provide describe what the research team can do to operationalize the principles and share specific examples from our empirical work. The guidelines can assist researchers in moving beyond broad prescriptions, pointing to the initial steps necessary to operationalize the principles toward the pursuit of greater social inclusion.

The fifth and final contribution of work is elaborating pathways to incorporate the principles in existing designoriented research approaches. We outlined how the principles we identify can augment existing approaches such as action design research (Sein et al., 2011) and participatory design (Spinuzzi, 2005). This mapping to existing designoriented approaches (Tables 12a and 12b) demonstrates how the principles we developed can be put into practice when the design involves work with marginalized populations. IS scholars who wish to use a specific designoriented approach to social inclusion can therefore explore ways to incorporate our principles into their own work.

## 5.2 Limitations

Prior scholarship articulating principles for conducting research (e.g., Klein & Myers, 1999; Myers & Klein, 2011; Wynn & Williams, 2012, Sarker et al., 2013) has often found it difficult to state limitations beyond caveats for the application of principles. Although our work is similar in spirit to these prior efforts, a significant contrast that marks our effort is our empirical grounding. It is thus appropriate for us to acknowledge the limitations tied to the empirical work, efforts to derive the principles based on this empirical work, and, finally, caveats for application of the principles.

We acknowledge that our empirical work draws on a research project carried out in a specific setting (a Scandinavian country) and with a specific marginalized population (people with IDD). It is possible to argue that the Scandinavian research setting might limit transferability to other settings due to differences in societal structures. We also concede that the authors hold a position of privilege and therefore may find it challenging to appreciate the life experiences of individuals in the marginalized group. However, we hope that the progressive Scandinavian social policies have helped the authors appreciate such concerns, and participation in the research project itself has provided several experiences and examples that have allowed the research team to develop an informed perspective on the possibilities for facilitating greater social inclusion. Yet another critique may be that the specific population (people with IDD) may not provide access to a sufficiently diverse set of challenges. We note that the underlying research investigation consisted of multiple cases dealing with different problems (see Appendix A for a brief description) experienced by individuals within this population. Prior work has also pointed out that people with IDD are not a homogenous group (Carulla et al., 2011). This combination of factors suggests that our empirical work naturally contained at least some diversity.

We also acknowledge that the efforts to derive the principles (the conceptual move from the empirical findings to the principles) required us to employ a form of abductive reasoning (Josephson & Josephson, 1996), privileging “inference over best explanation” (Sober, 2021) as the mode of discovery of principles (possibly introducing researcher bias and potentially overlooking alternative explanations or pathways). An important guardrail to mitigate this bias has been provided by prior work on social inclusion. It is, in fact, conceivable that one could simply reflect on this literature to develop principles to facilitate greater social inclusion. The empirical grounding for the principles provides an important translation as well as additional validation of our effort to articulate the principles. Even if imperfect (translation from empirical findings to the principles), we claim that our work can be viewed as an improvement beyond an exclusive focus on conceptual argumentation. A potential next step of our work is the development of evaluative criteria that could be used to self-monitor the social inclusiveness of design-oriented research processes.

Finally, we acknowledge that the principles we derive are one possible path to achieve greater social inclusion in design-oriented research processes. Although our elaboration adds to their credibility, they are not proposed as immutable canons nor is their use meant to limit future efforts toward greater social inclusion. We take inspiration from Myers and Klein (2011) in describing these principles not as narrowly defined criteria or appropriate for mechanistic application. Rather, information systems scholars will “need to exercise their judgement … [about] … how, and which of the principles should be applied in any given research project ” (see Klein & Myers, 1999, cited in Myers & Klein, 2011, p. 18). Therefore, our claim is that the principles we articulate are consistent with and informed by prior scholarship related to social inclusion and rely on robust findings from an empirical investigation.

## 5.3 Implications

We believe that social inclusion—“the ability to participate fully in one’s social world” (Bailey et al., 2020)—is a big idea. Decades of research (e.g. AbuJarour et al., 2019; Carter et al., 2013; Cobigo et al., 2012; Myers et al., 2020; Trauth, 2017) and policy-making efforts (Wolfensberger, 1983; United Nations, 2006) have demonstrated that the problem remains difficult and demands serious and concerted effort from multiple directions. The introduction of information technologies and IT artifacts has further complicated the space. Our social worlds are increasingly digital. The recent pandemic has helped us realize how much we have shifted to this digital world (Vial, 2019) and highlighted the problems this entails—such as access (Bailey et al., 2019), the digital divide (Carter et al., 2013; Warschauer, 2004), and changes to work practices (Selander & Jarvenpaa, 2016) and social roles (Payton & Kvasny, 2012). We have also learned that information technologies and IT-based artifacts can contribute to (or subtract from) the goal of social inclusion (in both digital and real worlds). This is particularly true for marginalized groups (Myers et al., 2020). Pursuing design-oriented research with marginalized groups remains difficult because it inherently adds further complexity to the process.

The challenge for IS scholars is, then, to ensure that we take note of research and activism related to social inclusion beyond the IS field, in addition to work from IS scholars who have explored these concerns (e.g., AbuJarour & Krasnova, 2017; Pethig & Kroenung, 2019; Trauth et al., 2016). Conceptualizations such as the relational and dynamic view of social inclusion (Selwyn, 2002; Taket et al., 2009), recognition of social inclusion as an individual aspiration (Hammel et al., 2008), and the three facets of social inclusion (see Section 2) can inform our scholarly work. However, to introduce these concepts in our work requires an approach to research that emphasizes action-oriented research “on the ground” (Trauth, 2017), working directly with marginalized groups to design technologies and services that address the real needs for social inclusion. Without such efforts, IS scholars cannot go beyond paying lip service to the ideals of social inclusion. We have attempted to respond to this perspective by articulating principles to guide research conduct that will give voice to marginalized groups.

The principles can also be used to augment other designoriented approaches beyond the mapping we have shown on participatory design (Spinuzzi, 2005), and action design research (Sein et al., 2011). For example, approaches such as collaborative practice research (Mathiassen, 2002), design science research (Hevner et al., 2004), and soft design science (Baskerville et al., 2009), all point to possibilities for incorporating the principles we have proposed. The principles can augment the lessons (Mathiassen, 2002), guidelines (Hevner et al., 2004), and activities (Baskerville et al., 2009) to enrich research conduct in ways that promote the pursuit of greater social inclusion. Our effort thus provides guidelines that IS scholars can use to improve social inclusion as they pursue action-oriented approaches while avoiding stereotypes and preconceived notions (Ortiz et al., 2019; Trauth, 2017).

Through the application of the principles, research efforts may be infused with greater sensitivity to the ideals of social inclusion. More specifically, the principles demonstrate how granting individuals the ability to control and adjust activities (self-determination—Deci & Ryan, 2002; Rotter, 1966), developing a sense of being valued and accepted in a community (belongingness— Baumeister & Leary, 1995; Mahar et al., 2013), and recognizing them as competent and trusting them for their contributions (social capital—Putnam, 2000; Portes, 1998) can be operationalized in the context of specific research efforts. The principles implicitly argue for the importance of longitudinal collaborations, where the research team can establish long-standing relations built on trust and reciprocity with the marginalized groups, responding to the relational perspective of social inclusion (Selwyn, 2002; Taket et al., 2009) so that research facilitation is linked to the exercise of individual skills and abilities by each participant in different situations.

## 5.4 Concluding Remarks

The pursuit of social inclusion is an important research direction for IS scholars. Recent scholarship (Dadgar & Joshi, 2018; Trauth, 2017; Trauth & Connolly, 2021; Pethig & Kroenung, 2019) has started to explore several avenues that IS scholarship can consider toward achieving this goal. Our focus in this research is on offering specific guidance that will allow IS scholars to more easily incorporate and realize these ideals in their work.

Our work, therefore, builds on the imperative of pursuing proactive action- (Trauth, 2017) and design-oriented approaches (Sein et al., 2011). We describe a multi-case investigation that follows action design research (Sein et al., 2011) (a specific version of such action- and designoriented approaches). Reflecting on our empirical work, we formulate and present principles for pursuing and facilitating greater social inclusion during the research conduct. Our effort to outline the principles is similar to the other efforts that have focused on different modes of research—e.g., interpretive research (Klein & Myers, 1999; Yin, 2003), critical realism (see Myers & Klein, 2011), design science (Hevner et al., 2004; Sein et al., 2011), and qualitative (Sarker et al., 2013)—with two key differences. The principles we outline are focused on the goal of pursuing greater social inclusion (not merely clarifying a methodological genre) and they are both derived from prior theoretical precursors and grounded in our empirical work.

We acknowledge that the pursuit of greater social inclusion must respect the “on-the-ground” realities (Trauth, 2017) that reflect the concerns of different marginalized groups. Therefore, our principles should not be seen as canonical nor as limiting the conduct of designoriented or action-oriented research in such contexts. It is possible that the principles we propose may be extended to respond to situated concerns (Klein & Myers, 1999). Our hope is that the principles and the associated guidelines will help IS scholars make and justify choices aimed at greater social inclusion when working with marginalized groups.

## Acknowledgments

We would like to thank the many research participants (individuals with intellectual and developmental disabilities, members of their support networks, and representatives from several external stakeholder agencies) in addition to several volunteers who participated in the research project for coordination and data collection. We also thank the Norwegian Research Council who supported this work and the University of Agder that supported work related to writing this paper. We thank the two anonymous reviewers and the editors for their constructive comments, which helped us to significantly improve the manuscript.

## References

AAIDD. (2022): Definition of Intellectual Disability. https://www.aaidd.org/intellectualdisability/definition

AbuJarour, S., & Krasnova, H. (2017). Understanding the role of ICTs in promoting social inclusion: The case of Syrian refugees in Germany. In: Ramos, I., Tuunainen, V., & Krcmar, H. (Eds.) Proceedings of the 25th European Conference on Information Systems.

AbuJarour, S., Wiesche, M., Díaz Andrade, A. D., Fedorowicz, J., Krasnova, H., Olbrich, S., Tan, C-W., Urquhart, C., & Venkatesh, V. (2019). ICT-enabled refugee integration: A research agenda. Communications of the Association for Information Systems, 44(1), 874-891.

Adam, A., Howcroft, D., & Richardson, H. (2002). Special Issue on Gender and Information Systems. Information Technology & People, 158(2), 94-118.

Aldridge, J. (2019). “With us and about us”: Participatory methods in research with “vulnerable” or marginalized groups. In Liamputtong, P. (Ed.), Handbook of research methods in health social sciences (pp. 1919- 1934). Springer.

Alm, K., & Guttormsen, D.S.A. (2021). Enabling the voices of marginalized groups of people in theoretical business ethics research. Journal of Business Ethics, 108, 303-320.

Almedom, A. M. (2005). Social capital and mental health: An interdisciplinary review of primary evidence. Social Science & Medicine, 61(5), 943-964.

Antonsich, M. (2010). Searching for belonging—An analytical framework. Geography Compass, 4(6), 644-659.

Atkinson, A. B., & Marlier, E. (2010). Analysing and measuring social inclusion in a global context. United Nations.

Bailey, A. & K. Osei-Bryson. (2018). Contextual reflections on innovations in an interconnected world: Theoretical lenses and practical considerations in ICT4D. Information Technology for Development, 24(3), 423-428.

Bailey, A., Carter, M., Thatcher, J., Urquhart, C., & Windeler, J. (2020). Special issue call for participation: Technology and social inclusion: Building a dialectic on the role of technology in inclusion and exclusion from societies, organizations, economies, and academe. Journal of the Association for Information

Systems. Retrieved from: https://aisnet.org/ news/news.asp?id=510453

Bailey, A., Henry-Lee, A., Johnson-Coke, Y., Leach, R., Clayton, A., Gee, M., & Browne, O. (2019). ICT use in the context of electricity access in a developing country: A choice framework analysis. Proceedings of the International Conference on Social Implications of Computers in Developing Countries.

Baskerville, R. L. (1999). Investigating information systems with action research. Communications of the Association for Information Systems, 2(1), Article 19.

Baskerville, R. L., Kaul, M., & Storey, V. C. (2015). Genres of inquiry in design-science research. Mis Quarterly, 39(3), 541-564.

Baskerville, R., Pries-Heje, J., & Venable, J. (2009). Soft design science methodology. Proceedings of the 4th International Conference on Design Science Research in Information Systems and Technology.

Bates, P., & Davis, F. A. (2004). Social capital, social inclusion and services for people with learning disabilities. Disability & Society, 19(3), 195- 207.

Baumeister, R. F., & Leary, M. R. (1995). The need to belong: Desire for interpersonal attachments as a fundamental human motivation. Psychological Bulletin, 117(3), 497-529.

Benbasat, I., Goldstein, D. K., & Mead, M. (1987). The case research strategy in studies of information systems. MIS Quarterly, 11(3), 369-386.

Benton, L., & Johnson, H. (2015). Widening participation in technology design: A review of the involvement of children with special educational needs and disabilities. International Journal of Child-Computer Interaction, 3, 23-40.

Berghman, J. (1995). Social exclusion in Europe: Policy context and analytical framework. In G. Roo, (Ed.), Beyond the threshold (pp. 10-28). Policy Press.

Bigby, C. (2010). A five‐country comparative review of accommodation support policies for older people with intellectual disability. Journal of Policy and Practice in Intellectual Disabilities, 7(1), 3-15.

Bigby, C., Anderson, S., & Cameron, N. (2018). Identifying conceptualizations and theories of change embedded in interventions to facilitate community participation for people with intellectual disability: A scoping review.

Journal of Applied Research in Intellectual Disabilities, 31(2), 165-180.

Bjerknes, G., & Bratteteig, T. (1995). User participation and democracy: A discussion of Scandinavian research on system development. Scandinavian Journal of information systems, 7(1), 73-98.

Bodker, S., & Pekkola, S. (2010). A short review to the past and present of participatory design. Scandinavian Journal of Information Systems, 22(1), 45-48.

Bodker, S., Gronbæk, K., & Kyng, M. (1995). Cooperative design: techniques and experiences from the Scandinavian scene. In R. M. Baecker, W. Buxton, J. Grudin, & S. Greenberg (Eds.), Readings in humancomputer interaction (pp. 215-224). Morgan Kaufmann.

Bollard, M. R. (2009). Intellectual disability and social inclusion e-book: A critical review. Elsevier Health Sciences.

Bollingmo, L., Ellingsen, K.E. & Selboe, A. (2005). Perspektiver på selvbestemmelse. In A. Selboe, L. Bollingmo & K. E. Ellingsen (Eds.). Selvbestemmelse for tjenesteytere (17-37). Gyldendal Akademisk forlag.

Bossavit, B., & Parsons, S. (2016a). “This is how I want to learn”: High functioning autistic teens co-designing a serious game. Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems.

Bossavit, B., & Parsons, S. (2016b). Designing an educational game for and with teenagers with high functioning autism. Proceedings of the 14th Participatory Design Conference.

Brhel, M., Meth, H., Maedche, A. & Werder, K. (2015). Exploring principles of user-centered agile software development: A literature review. Information and Software Technology, 61, 163-181.

Bryman, A. (2016). Social research methods. Oxford University Press.

Bryman, A. (2016). Social research methods. Oxford University Press.

Bunce, L., King, N., Saran, S., & Talib, N. (2021). Experiences of Black and minority ethnic (BME) students in higher education: Applying self-determination theory to understand the BME attainment gap. Studies in Higher Education, 46(3), 534-547.

Carroll, J. M. (2003). Making use: scenario-based design of human-computer interactions. MIT Press.

Carter, M., Armstrong, D. J., Lee, A. S., Loiacono, E. T., & Thatcher, J. B. (2013). Social inclusion in a hyperconnected world: Panel discussion at AMCIS. Proceedings of the 19th Americas Conference on Information Systems.

Carulla, L. S., Reed, G. M., Vaez-Azizi, L. M., Cooper, S.-A., Leal, R. M., Bertelli, M., . . . Dirani, L. A. (2011). Intellectual developmental disorders: towards a new name, definition and framework for “mental retardation/intellectual disability” in ICD-11. World Psychiatry, 10(3), 175-180.

Cavanagh, J., Meacham, H., Pariona-Cabrera, P., & Bartram, T. (2021). Subtle workplace discrimination inhibiting workers with intellectual disability from thriving at the workplace. Personnel Review, 50(7-8), 1739- 1756.

Chapman, P., Phimister, E., Shucksmith, M., Upward, R., & Vera-Toscano, E. (1998). Poverty and exclusion in rural Britain: The dynamics of low income and employment. York Publishing Services.

Charlton, J. I. (2000). Nothing about us without us: Disability, empowerment and oppression. University of California Press.

Charmaz. K. (2006). Constructing grounded theory: A Practical guide through qualitative analysis. SAGE.

Checkland, P., & Scholes, J. (1999). Soft systems methodology in action. Wiley.

Chen, Y. R. R., & Schulz, P. J. (2016). The effect of information communication technology interventions on reducing social isolation in the elderly: a systematic review. Journal of Medical Internet Research, 18(1), Article e18.

Cobigo, V., & Stuart, H. (2010). Social inclusion and mental health. Current Opinion in Psychiatry, 23(5), 453-457.

Cobigo, V., Ouellette-Kuntz, H., Lysaght, R., & Martin, L. (2012). Shifting our conceptualization of social inclusion. Stigma Research and Action, 2(2), 75-84.

Commins, P. (1993). Combating exclusion in Ireland 1990-1994: A midway report. European Commission.

Constantino, J. N., Sahin, M., Piven, J., Rodgers, R., & Tschida, J. (2020). The impact of COVID-19 on individuals with intellectual and developmental

disabilities: Clinical and scientific priorities. American Journal of Psychiatry, 177(11), 1091-1093.

Craig, M., Burns, T., Fitzpatrick, R., Pinfold, V., & Priebe, S. (2007). Social exclusion and mental health: conceptual and methodological review. British Journal of Psychiatry, 191, 477-483.

Culén, A. L., & van der Velden, M. (2013). The digital life of vulnerable users: Designing with children, patients, and elderly. In Aanestad M., Bratteteig T. (Eds.), Scandinavian Conference on Information Systems (pp. 53-71). Springer.

Cummins, R. A., & Lau, A. L. (2003). Community integration or community exposure? A review and discussion in relation to people with an intellectual disability. Journal of Applied Research in Intellectual Disabilities, 16(2), 145-157.

Dadgar, M., & Joshi, K.D. (2018). The role of information and communication technology in self-management of chronic diseases: An empirical investigation through value sensitive design. Journal of the Association for Information Systems, 19(2), 86-112.

Davison, R. M., Martinsons, M. G., & Kock, N. (2004). Principles of Canonical Action Research. Information Systems Journal, 14(1), 65-86.

Deci, E. L., & Ryan, R. M. (2002). The paradox of achievement: The harder you push, the worse it gets. In J. Aronsen (Ed.), Improving academic achievement (61-87). Academic Press.

Deng, X., Joshi, K. D., & Galliers, R. D. (2016). The duality of empowerment and marginalization in microtask crowdsourcing: Giving voice to the less powerful through value sensitive design. MIS Quarterly, 40(2), 279-302.

Díaz Andrade, A. D., & Doolin, B. (2016). Information and communication technology and the social inclusion of refugees. MIS Quarterly, 40(2), 405-416.

Eisenhardt, K. M. (1989). Building theories from case study research. Academy of Management Review, 14(4), 532-550.

Eisenhardt, K. M. (1991). Better stories and better constructs: The case for rigor and comparative logic. Academy of Management Review, 16(3), 620-627.

Eisenhardt, K. M., & Bourgeois III, L. J. (1988). Politics of strategic decision making in highvelocity environments: Toward a midrange theory. Academy of Management Journal, 31(4), 737-770.

Ellenkamp, J. J., Brouwers, E. P., Embregts, P. J., Joosen, M. C., & van Weeghel, J. (2016). Work environment-related factors in obtaining and maintaining work in a competitive employment setting for employees with intellectual disabilities: A systematic review. Journal of Occupational Rehabilitation, 26(1), 56-69.

Erickson, W., Lee, C., & von Schrader, S. (2020). 2018 disability status report: United States. Cornell University Yang-Tan Institute on Employment and Disability.

Fay, B. (1996). Contemporary philosophy of social science. Blackwell.

Frauenberger, C., Good, J., & Keay-Bright, W. (2011). Designing technology for children with special needs: bridging perspectives through participatory design. CoDesign, 7(1), 1-28.

Friedman, D. J., Gibson Parrish, R., & Fox, M. H. (2018). A review of global literature on using administrative data to estimate prevalence of intellectual and developmental disabilities. Journal of Policy and Practice in Intellectual Disabilities, 15(1), 43-62.

Gallivan, M. (2013). A structured review of IS research on gender and IT. Proceedings of the SIGMIS-ACM Conference on Computers and People Research.

Gao, F., & Liu, H. C. Y. (2021). Guests in someone else’s house? Sense of belonging among ethnic minority students in a Hong Kong university. British Educational Research Journal, 47(4), 1004-1020.

Given, L. M. (2008). The SAGE encyclopaedia of qualitative research methods. SAGE.

Gjertsen, H., Hardonk, S., & Ineland, J. (2021). Work inclusion for people with intellectual disabilities in three Nordic countries: The current policy and challenges. Scandinavian Journal of Disability Research, 23(1), 360-370.

Goodley, D. & Rapley, M. (2001). How do you understand “learning difficulties”? Towards a social theory of impairment. Mental Retardation, 39(3), 229-232.

Goodley, D. (2001). “Learning difficulties,” the social model of disability and impairment: Challenging epistemologies. Disability & Society, 16(2), 207-231

Greenbaum, J., & Loi, D. (2012). Participation, the camel and the elephant of design: An introduction. CoDesign, 8(2-3), 81-85.

Gregor, S., Chandra Kruse, L., & Seidel, S. (2020). Research perspectives: The anatomy of a design

principle. Journal of the Association for Information Systems, 21(6), 1622-1652.

Gupta, B., Loiacono, E. T., Dutchak, I. G., & Thatcher, J. B. (2019). A field-based view on gender in the information systems discipline: preliminary evidence and an agenda for change. Journal of the Association for Information Systems, 20(12), 1870-1900.

Haj-Bolouri, A., Purao, S., Rossi, M., & Bernhardsson, L. (2018). Action design research in practice: lessons and concerns. Proceedings of the 26th European Conference on Information Systems.

Hall, E. (2010). Spaces of social inclusion and belonging for people with intellectual disabilities. Journal of Intellectual Disability Research, 54, 48-57.

Hammel, J., Magasi, S., Heinemann, A., Whiteneck, G., Bogner, J., & Rodriguez, E. (2008). What does participation mean? An insider perspective from people with disabilities. Disability and Rehabilitation, 30, 1445-1460.

Hart, A., Flegg, M., Rathbone, A., Gant, N., Buttery, L., Gibbs, O., & Dennis, S. (2020). Learning from the resilience playtest: Increasing engagement in resilience promoting games through participatory design. CoDesign, 17(4), 435-453.

Harpur, P. (2017). Nothing about us without us: The UN Convention on the Rights of Persons with Disabilities. In Oxford Research Encyclopedia of Politics. Retrieved on June 29, 2022 from ttps://doi.org/10.1093/acrefore/978019022863 7.013.245.

Hedley, D., Uljarević, M., Cameron, L., Halder, S., Richdale, A., & Dissanayake, C. (2017). Employment programmes and interventions targeting adults with autism spectrum disorder: A systematic review of the literature. Autism, 21(8), 929-941.

Hendriks, N., Huybrechts, L., Wilkinson, A., & Slegers, K. (2014). Challenges in doing participatory design with people with dementia. Proceedings of the 13th Participatory Design Conference.

Hendriks, N., Slegers, K., & Duysburgh, P. (2015). Codesign with people living with cognitive or sensory impairments: a case for method stories and uniqueness. CoDesign, 11(1), 70-82.

Hendriks, N., Truyen, F., & Duval, E. (2013). Designing with dementia: Guidelines for participatory design together with persons with dementia. Proceedings of the IFIP Conference

on Human-Computer Interaction (pp. 649- 666).

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105.

Ho, D. K. L., Ma, J., & Lee, Y. (2011). Empathy@ design research: A phenomenological study on young people experiencing participatory design for social inclusion. CoDesign, 7(2), 95-106.

Holton, J. A. (2007). The coding process and its challenges. In A. Bryant & K. Charmaz (Eds.), The SAGE handbook of grounded theory (pp. 265- 290). SAGE.

Hsieh, J. J. P., Rai, A., & Keil, M. (2008). Understanding digital inequality: Comparing continued use behavioral models of the socioeconomically advantaged and disadvantaged. MIS Quarterly 31(1), 97-126.

Iivari, N. (2004, October). Enculturation of user involvement in software development organizations-an interpretive case study in the product development context. Proceedings of the 3rd Nordic Conference on Human-Computer Interaction (pp. 287-296).

Istenic Starcic, A., & Bagon, S. (2014). ICT‐supported learning for inclusion of people with special needs: Review of seven educational technology journals, 1970-2011. British Journal of Educational Technology, 45(2), 202-230.

Josephson, J. R., & Josephson, S. G. (Eds.). (1996). Abductive inference: Computation, philosophy, technology. Cambridge University Press.

Joshi, K. D., & Schmidt, N. L. (2006). Is the information systems profession gendered? Characterization of IS professionals and IS career. The Data Base for Advances in Information Systems, 37(4), 26-41.

Jurkowski, J. M. (2008). Photovoice as participatory action research tool for engaging people with intellectual disabilities in research and program development. Intellectual and developmental disabilities, 46(1), 1-11.

Kelley, T. & Kelley, D. (2012). Reclaim your creative confidence. Harvard business review, 90(12), 115-118.

Kensing, F., & Greenbaum, J. (2012). Heritage: Having a say. In J. Simonsen & T. Robertson (Eds.). Routledge international handbook of participatory design (pp. 41-56). Routledge.

Kemmis, S., McTaggart, R., & Nixon, R. (2014). Introducing critical participatory action research. In S. Kemmis, R. McTaggart, R.

Nixon (Eds.) The action research planner. (Vol. 1, pp. 1-31). Springer.

Klein, H. K., & Myers, M. D. (1999). A set of principles for conducting and evaluating interpretive field studies in information systems. MIS Quarterly, 67-93.

Kuntz, E. M., & Carter, E. W. (2019). Review of interventions supporting secondary students with intellectual disability in general education classes. Research and Practice for Persons with Severe Disabilities, 44(2), 103-121.

Kyng, M. (2010). Bridging the gap between politics and techniques: On the next practices of participatory design. Scandinavian Journal of Information Systems, 22(1), 49-68.

Lee, A.S., (2021). Theory building from the points of view of a native, an anthropologist, and a philosopher: Commentary on Suzanne Rivard’s “Theory building is neither an art nor a science. It is a craft.” Journal of Information Technology, 36(3), 329-333

Lemay, R. (2006). Social role valorisation insights into the social integration conundrum. Mental Retardation, 44(1), 1-12.

Lorentzen, P. (2007). Selvbestemmelse i et psykologisk perspektiv. In K. E. Ellingsen (Ed.), Selvbestemmelse. Egne og andres valg og verdier (pp. 93-114). Universitetsforlaget.

Louw, J. S., Kirkpatrick, B., & Leader, G. (2020). Enhancing social inclusion of young adults with intellectual disabilities: A systematic review of original empirical studies. Journal of Applied Research in Intellectual Disabilities, 33(5), 793-807.

Mackert, M., Mabry-Flynn, A., Champlin, S., Donovan, E. E., & Pounders, K. (2016). Health literacy and health information technology adoption: The potential for a new digital divide. Journal of Medical Internet Research, 18(10), Article e264.

Mahar, A. L., Cobigo, V., & Stuart, H. (2013). Conceptualizing belonging. Disability and Rehabilitation, 35(12), 1026-1032.

Maidment, J., & Macfarlane, S. (2009). Debating the capacity of information and communication technology to promote inclusion. In A Taket, B Crisp, A Nevill, G Lamaro, M Graham, & S Barter-Godfrey (Eds.), Theorising social exclusion (pp. 95-105). University of the Sunshine Coast, Queensland.

Majchrzak, A., Markus, M. L., & Wareham, J. (2016). Designing for digital transformation: Lessons for information systems research from the study

of ICT and societal challenges. MIS Quarterly, 40(2), 267-277.

Makhaeva, J., Frauenberger, C., & Spiel, K. (2016, August). Creating creative spaces for codesigning with autistic children: The concept of a “Handlungsspielraum.” Proceedings of the 14th Participatory Design Conference.

Martínez-Martínez, O. A., & Rodríguez-Brito, A. (2020). Vulnerability in health and social capital: a qualitative analysis by levels of marginalization in Mexico. International Journal for Equity in Health, 19(1), 1-10.

Masiero, S., & Ravishankar, M.N. (2018). Digital technologies and pro-poor finance. In Y. Dwivedi et al. (Eds.), Emerging markets from a multidisciplinary perspective (pp. 49-59) Springer.

Mathiassen, L. (2002). Collaborative practice research. Information Technology & People, 15(4), 321- 345.

Mattelmäki, T., Vaajakallio, K., & Koskinen, I. (2014). What happened to empathic design? Design Issues, 30(1), 67-77.

McMahon, D. D., Smith, C. C., Cihak, D. F., Wright, R., & Gibbons, M. M. (2015). Effects of digital navigation aids on adults with intellectual disabilities: Comparison of paper map, Google maps, and augmented reality. Journal of Special Education Technology, 30(3), 157-165.

Meininger, H. P. (2006). Narrating, writing, reading: Life story work as an aid to (self) advocacy. British Journal of Learning Disabilities, 34(3), 181-188.

Meld. St. 8 (2022-2023). Menneskerettar for personar med utviklingshemming—Det handlar om å bli høyrt og sett. Ministry of Culture and Equality. https://www.regjeringen.no/no/dokumenter/me ld.-st.-8-20222023/id2945431/

Merrells, J., Buchanan, A., & Waters, R. (2019). “We feel left out”: Experiences of social inclusion from the perspective of young adults with intellectual disability. Journal of Intellectual & Developmental Disability, 44(1), 13-22.

Mettler, T., Bächle, M., Daurer, S., & Judt, A. (2017). Parental control reversed: Using ADR for designing a low-cost monitoring system for elderly. In Proceedings of the International Conference on Information Systems.

Millner, U. C., Woods, T., Furlong‐Norman, K., Rogers, E. S., Rice, D., & Russinova, Z. (2019). Socially valued roles, self‐determination, and community participation among individuals living with

serious mental illnesses. American Journal of Community Psychology, 63(1-2), 32-45.

Mithen, J., Aitken, Z., Ziersch, A., & Kavanagh, A. M. (2015). Inequalities in social capital and health between people with and without disabilities. Social Science & Medicine, 126, 26-35.

Mowat, J. G. (2015). Towards a new conceptualisation of marginalisation. European Educational Research Journal, 14(5), 454-476.

Mulhall, P., Taggart, L., Coates, V., McAloon, T., & Hassiotis, A. (2018). A systematic review of the methodological and practical challenges of undertaking randomised-controlled trials with cognitive disability populations. Social Science & Medicine, 200, 114-128.

Myers, M. D., & Klein, H. K. (2011). A set of principles for conducting critical research in information systems. MIS Quarterly, 35(1), 17- 36.

Myers, M. D., Chughtai, H., Davidson, E., Tsibolane, P., & Young, A. G. (2020). Studying the Other or becoming the Other: Engaging with indigenous peoples in IS research. Communications of the Association for Information Systems, 47(1), 382-396.

Niemiec, C. P., & Ryan, R. M. (2009). Autonomy, competence, and relatedness in the classroom: Applying self-determination theory to educational practice. Theory and Research in Education, 7(2), 133-144.

NIH. (2022). About intellectual and developmental disabilities (IDDs). https://www.nichd.nih.gov/ health/topics/idds/conditioninfo/default

Nind, M., & Vinha, H. (2014). Doing research inclusively: Bridges to multiple possibilities in inclusive research. British Journal of Learning Disabilities, 42(2), 102-109.

Nirje, B. (1969). The normalization principle and its human management implications. In R. Kugel., & W. Wolfensberger (Eds.), Changing patterns in residential services for the mentally retarded. Government Printing Office.

Nonnemacher, S.L. & Bambara, L.M. (2011). “I’m supposed to be in charge”: Self-advocates perspectives on their self-determination support needs. Intellectual and Developmental Disabilities, 49(5), 327−340.

Norman, D. A., & Draper, S. W. (1986). User centered system design; new perspectives on humancomputer interaction. Erlbaum Associates

Norwegian White Paper. (2016). “På lik linje—Åtte løft for å realisere grunnleggende rettigheter

for personer med utviklingshemming” [Like anyone else—Eight boosts to realize basic rights for persons with intellectual disability]. Ministry of Children and Equality.

Nota, L., Santilli, S., Ginevra, M. C., & Soresi, S. (2014). Employer attitudes towards the work inclusion of people with disability. Journal of Applied Research in Intellectual Disabilities, 27(6), 511-520.

Olbrich, S., Trauth, E. M., Niedermann, F., & Gregor, S. (2015). Inclusive design in IS: Why diversity matters. Communications of the Association for Information Systems, 37(1), 767-782.

Oliver, M. (1996). Understanding disability: From theory to practice. Palgrave.

Ortiz, J., Young, A., Myers, M. D., Bedeley, R. T., Carbaugh, D., Chughtai, H., ... & Wigdor, A. (2019). Giving voice to the voiceless: The use of digital technologies by marginalized groups. Communications of the Association for Information Systems, 45(1), 20-38.

Overmars-Marx, T., Thomése, F., Verdonschot, M., & Meininger, H. (2014). Advancing social inclusion in the neighbourhood for people with an intellectual disability: An exploration of the literature. Disability and Society, 29(2), 255- 274.

Papay, C. K., & Bambara, L. M. (2014). Best Practices in transition to adult life for youth with intellectual disabilities. Career development and transition for exceptional individuals, 37(3), 136-148.

Payton, F. C., & Kvasny, L. (2012). Considering the political roles of Black talk radio and the Afrosphere in response to the Jena 6. Information Technology & People, 25(1), 81- 102.

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45-77.

Pelleboer-Gunnink, H. A., van Weeghel, J., & Embregts, P. J. C. M. (2021). Public stigmatisation of people with intellectual disabilities: a mixed-method population survey into stereotypes and their relationship with familiarity and discrimination. Disability and Rehabilitation, 43(4), 489-497.

Perez, T. S., & Crowe, B. M. (2021). Community participation for transition-aged youth with intellectual and developmental disabilities: A

systematic review. Therapeutic Recreation Journal, 55(1), 19-41.

Perez‐Brumer, A. G., Reisner, S. L., McLean, S. A., Silva‐Santisteban, A., Huerta, L., Mayer, K. H., ... & Lama, J. R. (2017). Leveraging social capital: multilevel stigma, associated HIV vulnerabilities, and social resilience strategies among transgender women in Lima, Peru. Journal of the International AIDS Society, 20(1), Article 21462.

Pethig, F. & Kroenung, J. (2019). Specialized information systems for the digitally disadvantaged. Journal of the Association for Information Systems, 20(10), 1412-1446.

Phipps, L. (2000). New communications technologies-A conduit for social inclusion. Information, Communication & Society, 3(1), 39-68.

Portes, A. (1998). Social capital: Its origins and applications in modern sociology. Annual review of sociology, 24(1), 1-24.

Povee, K., Bishop, B. J., & Roberts, L. D. (2014). The use of photovoice with people with intellectual disabilities: Reflections, challenges and opportunities. Disability & Society, 29(6), 893- 907.

Power, A. (2013). Making space for belonging: Critical reflections on the implementation of personalised adult social care under the veil of meaningful inclusion. Social Science & Medicine, 88, 68-75.

Purao, S., & Wu, A. (2013). Towards values-inspired design: The case of citizen-centric services. Proceedings of International Conference on Information Systems.

Purao, S., Baldwin, C., Hevner, A., Storey, V. C., Pries-Heje, J., Smith, B., & Zhu, Y. (2008). The sciences of design: observations on an emerging field. Communications of the Association for Information Systems, 23(1), 523-546.

Purao, S., & Mulgund, S. (2022). Designing for Selfmanagement of multiple chronic conditions by the aging-at-home. Proceedings of the International Conference on Information Systems.

Purao, S., Rossi, M., & Lindgren, R. (2011). Action Design Research. MIS Quarterly, 35(1), 37-56.

Putnam, R. D. (2000). Bowling alone: America’s declining social capital. In Crothers, L., Lockhart, C. (Eds.), Culture and politics (223- 234). Palgrave Macmillan.

Reinertsen, S. (2012). Arbeids- og aktivitetssituasjonen blant personer med psykisk utviklingshemming [The work and activity situation among people with intellectual disability]. NAKU Nasjonal tilstandsrapport.

Ritchie, A., & Gaulter, A. (2020). Dancing towards belonging: The use of a dance intervention to influence migrant pupils’ sense of belonging in school. International Journal of Inclusive Education, 24(4), 366-380.

Rittel, H. W. & Webber, M. M. (1973). Dilemmas in a general theory of planning. Policy Sciences, 4(2), 155-169.

Rivard, S. (2021). Theory building is neither an art nor a science. It is a craft. Journal of Information Technology, 36(3), 316-328.

Robertson, T., & Wagner, I. (2012). Engagement, representation and politics-in-action. In J. Simonsen & T. Robertson (Eds.). Routledge international handbook of participatory design. (pp. 64-85). Routledge.

Rogers, Y., & Marsden, G. (2013). Does he take sugar? Moving beyond the rhetoric of compassion. Interactions, 20(4), 48-57.

Rotter, J.B. (1966). Generalized expectancies for internal versus external control of reinforcement. Psychological Monograph, 80(1), 1-28.

Sahay, S., Sein, M. K., & Urquhart, C. (2017). Flipping the context: ICT4D, the next grand challenge for IS research and practice. Journal of the Association of Information Systems 18(12), 837-847.

Sahay, S., Sundararaman, T., & Braa, J., (2017). Public health informatics: Designing for change-a developing country perspective. Oxford University Press.

Saldaña, J. (2015). The coding manual for qualitative researchers. SAGE.

Sanders, E. B. N., & Stappers, P. J. (2008). Co-creation and the new landscapes of design. CoDesign, 4(1), 5-18.

Sarker, S., Xiao, X. & Beaulieu, T. (2013). Guest editorial: Qualitative studies in information systems: A critical review and some guiding principles. MIS Quarterly, 37(4), iii-xviii.

Schalock, R. L., Luckasson, R., & Tassé, M. J. (2021, March). Twenty questions and answers regarding the 12th edition of the AAIDD manual: Intellectual disability: definition, diagnosis, classification, and systems of

supports. American Association on Intellectual and Developmental Disabilities.

Scharlach, A. E., & Lehning, A. J. (2013). Ageingfriendly communities and social inclusion in the United States of America. Ageing & Society, 33(1), 110-136.

Seidel, S., Chandra Kruse, L., Székely, N., Gau, M., & Stieger D. (2017). Design principles for sensemaking support systems in environmental sustainability transformations. European Journal of Information Systems, 27(2), 221-247.

Sein, M. K., Henfridsson, O., Purao, S., Rossi, M., & Lindgren, R. (2011). Action design research. MIS Quarterly, 35(1), 37-56.

Selander, L., & Jarvenpaa, S. L. (2016). Digital action repertoires and transforming a social movement organization. MIS Quarterly, 40(2), 331-352.

Selwyn, N. (2002). “E-stablishing” an inclusive society? Technology, social exclusion and UK government policy making. Journal of Social Policy, 31(1), 1-20.

Semborski, S., Winn, J.G., Rhoades, H., Petry, L., & Henwood, B.F. (2022). The application of GIS in homelessness research and service delivery: A qualitative systematic review. Health & Place, 75, Article 102776.

Serenko, A., & Turel, O. (2021). Why are women underrepresented in the American IT industry? The role of explicit and implicit gender identities. Journal of the Association for Information Systems, 22(1), 41-66.

Sevelius, J. M., Gutierrez-Mock, L., Zamudio-Haas, S., McCree, B., Ngo, A., Jackson, A., ... & Gamarel, K. (2020). Research with marginalized communities: Challenges to continuity during the COVID-19 pandemic. AIDS and Behavior, 24(7), 2009-2012.

Shakespeare, T. (2004). Social models of disability and other life strategies. Scandinavian Journal of Disability Research, 6(1), 8-21.

Shepheard-Walwyn, E. (2018). Marginalisation of traditional groups and the degradation of nature. In T. Marsden (Ed.), The SAGE handbook of nature (Vol. 3, pp. 1037-1063). SAGE.

Shneiderman, B. (1987). Shneiderman’s “Eight Golden Rules of Interface Design” Design Principles FTW. https://www.designprinciples ftw.com/collections/shneidermans-eightgolden-rules-of-interface-design

Shogren, K. A., & Wehmeyer, M. L. (2020). Handbook of adolescent transition education for youth with disabilities (2nd ed.). Routledge.

Shogren, K. A., Wehmeyer, M. L., Palmer, S. B., Forber-Pratt, A., Little, T. J., & Lopez, S. J. (2015a). Causal agency theory: Reconceptualizing a functional model of self-determination. Education and Training in Autism and Developmental Disabilities, 50(3), 251-263.

Shogren, K. A., Wehmeyer, M. L., Palmer, S. B., Rifenbark, G. G., & Little, T. D. (2015b). Relationships between self-determination and postschool outcomes for youth with disabilities. The Journal of Special Education, 48(4), 256-267.

Sigstad, H. M. H., & Garrels, V. (2018). Facilitating qualitative research interviews for respondents with intellectual disability. European Journal of Special Needs Education, 33(5), 692-706.

Silver, H. (1995). Reconceptualizing social disadvantage: Three paradigms of social exclusion. In G. Rodgers, C. Gore, & J. B. Figueiredo (Eds.), Social exclusion: Rhetoric, reality, responses (pp. 57-80). International Institute for Labour Studies, United Nations Development Programme.

Simplican, S. C., Leader, G., Kosciulek, J., & Leahy, M. (2015). Defining social inclusion of people with intellectual and developmental disabilities: An ecological model of social networks and community participation. Research in Developmental Disabilities, 38, 18-29.

Simpson, K., Adams, D., Bruck, S., & Keen, D. (2019). Investigating the participation of children on the autism spectrum across home, school, and community: A longitudinal study. Child: Care, Health and Development, 45(5), 681-687.

Sitbon, L., & Farhin, S. (2017, November). Codesigning interactive applications with adults with intellectual disability: A case study. Proceedings of the 29th Australian Conference on Computer-Human Interaction (pp. 487-491).

Sjostrom, J., & Agerfalk, P. J. (2009). An analytic framework for design-oriented research concepts. Proceedings of the Americas Conference on Information Systems.

Sjöström, J., Ågerfalk, P., & Hevner, A. (2022). The Design of a system for online psychosocial care: Balancing privacy and accountability in sensitive online healthcare environments. Journal of the Association for Information Systems, 23(1), 237-263.

Sober, E. (2021). Inductive and abductive arguments. Taylor & Francis.

Soresi, S., Nota, L., & Wehmeyer, M. L. (2011). Community involvement in promoting inclusion, participation and self‐determination. International Journal of Inclusive Education, 15(1), 15-28.

Special Olympics. (2022): What is intellectual disability? https://www.specialolympics.org/ about/intellectual-disabilities/what-isintellectual-disability

Spinuzzi, C. (2005). The methodology of participatory design. Technical communication, 52(2), 163- 174.

Spradley, J. P. (2016). Participant observation. Waveland.

Sprague, J., & Hayes, J. (2000). Self‐determination and empowerment: A feminist standpoint analysis of talk about disability. American Journal of Community Psychology, 28(5), 671- 695.

Srivastava, S. K., & Panigrahi, P. K. (2019). Social participation among the elderly: Moderated mediation model of information and communication technology (ICT). Communications of the Association for Information Systems, 44(1), 33.

Strauss, A., & Corbin, J. (1990). Basics of qualitative research. SAGE.

Strnadová, I., Johnson, K., & Walmsley, J. (2018). “… but if you’re afraid of things, how are you meant to belong?” What belonging means to people with intellectual disabilities? Journal of Applied Research in Intellectual Disabilities, 31(6), 1091-1102.

Susman, G. (1983). Action research: A sociotechnical perspective. In G. Morgan (Ed.) Beyond method: Strategies for social research. SAGE.

Grung, R. M., Brown, M., Abdulla, S., Kiss, J. F., Orţan, F., Odrowaz-Coates, A., ... & Marsh, L. (2020). Social inclusion for people with intellectual disabilities in seven European countries. Learning Disability Practice, 24(1), 10.7748/ldp.2020.e2120.

Taket, A., Crisp, B. R., Nevill, A., Lamaro, G., Graham, M., & Barter-Godfrey, S. (Eds.). (2009). Theorising social exclusion. Routledge.

Tassé, M.J., Schalock, R.L., Thissen, D., Balboni, G., Bersani Jr, H., Borthwick-Duffy, S.A., Spreat, S., Widaman, K.F., Zhang, D. & Navas, P. (2016). Development and standardization of the diagnostic adaptive behavior scale: Application

of item response theory to the assessment of adaptive behavior. American Journal on Intellectual and Developmental Disabilities, 121(2), pp.79-94.

Toikko, T., & Pehkonen, A. (2018). Community belongingness and subjective well-being among unemployed people in a Finnish community. International Journal of Sociology and Social Policy, 38(9-10), 754-765.

Trauth, E. & Connolly, R. (2021). investigating the nature of change in factors affecting gender equity in the IT sector: A longitudinal study of women in Ireland. MIS Quarterly, 45(4) 2055- 2100.

Trauth, E. (2017). A research agenda for social inclusion in information systems. The Data Base for Advances in Information Systems, 48(2), 9-20.

Trauth, E. M., & Howcroft, D. (2006). Social inclusion and the information systems field: why now? In E. M. Trauth, D. Howcroft, T. Butler, B. Fitzgerald, & J. I. DeGross (Eds.), Social inclusion: Societal and organizational implications for information systems (pp. 3-12). Springer.

Trauth, E. M., Cain, C. C., Joshi, K. D., Kvasny, L., & Booth, K. M. (2016). The influence of genderethnic intersectionality on gender stereotypes about IT skills and knowledge. The Data Base for Advances in Information Systems, 47(3), 9- 39.

Tremblay, M. C., Martin, D. H., McComber, A. M., McGregor, A., & Macaulay, A. C. (2018). Understanding community-based participatory research through a social movement framework: a case study of the Kahnawake Schools Diabetes Prevention Project. BMC Public Health, 18(1), 1-17.

Tun, S. Y. Y., Madanian, S., & Mirza, F. (2020). Internet of things (IoT) applications for elderly care: a reflective review. Aging Clinical And Experimental Research, 33(3), 855-867.

Twomey, M. B., Sammon, D., & Nagle, T. (2020). The tango of problem formulation: A patient’s/researcher’s reflection on an action design research journey. Journal of Medical Internet Research, 22(7), Article e16916.

United Nations. (2006). Convention on the rights of persons with disabilities (CRPD). United Nations.

UNDP. (2021). Nothing about us without us. https://www.undp.org/blog/nothing-about-uswithout-us

Urquhart, C., Liyanage, S., & Kah, M. M. (2008). ICTs and poverty reduction: A social capital and knowledge perspective. Journal of Information Technology, 23(3), 203-213.

Verdonschot, M. M., De Witte, L. P., Reichrath, E., Buntinx, W. H. E., & Curfs, L. M. (2009). Community participation of people with an intellectual disability: A review of empirical findings. Journal of Intellectual Disability Research, 53(4), 303-318.

Vial, G. (2019). Understanding digital transformation: A review and a research agenda. The Journal of Strategic Information Systems, 28(2), 118-144.

Walker, A., & Walker, C. (Eds.). (1997). Britain divided: The growth of social exclusion in the 1980s and 1990s. Child Poverty Action Group.

Walmsley, J., Strnadová, I., & Johnson, K. (2018). The added value of inclusive research. Journal of Applied Research in Intellectual Disabilities, 31(5), 751-759.

Warschauer, M. (2004). Technology and social inclusion: Rethinking the digital divide. MIT Press.

Waycott, J., Wadley, G., Schutt, S., Stabolidis, A., & Lederman, R. (2015). The challenge of technology research in sensitive settings: Case studies “ensitive HCI.” Proceedings of the Annual Meeting of the Australian Special Interest Group for Computer Human Interaction (pp. 240-249).

Wehmeyer, M. L., & Shogren, K. A. (2017). Applications of the self-determination construct to disability. In M. Wehmeyer, K. Shogren, T. Little, S. Lopez (Eds.) Development of self-determination through the life-course (pp. 111-123). Springer.

Wehmeyer, M.L. (2007). Promoting selfdetermination in students with developmental disabilities. Guildford.

Werner, S., & Abergel, M. (2018). What’s in a label? The stigmatizing effect of intellectual disability by any other name. Stigma and Health, 3(4), 385-394.

Western, J., McCrea, R., & Stimson, R. (2007). Quality of life and social inclusion. International Review of Sociology—Revue Internationale de Sociologie, 17(3), 525-537.

Williams, C. C., & White, R. (2003). Conceptualising social inclusion: Some lessons for action. In Proceedings of the Institution of Civil Engineers: Municipal Engineer, 156(2), 91-95.

Wilson, L. (2006). Developing a model for the measurement of social inclusion and social capital in regional Australia. Social Indicators Research, 75(3), 335-360.

Wolfensberger, W. (1983). Social role valorization: A proposed new term for the principle of normalization. Mental Retardation, 21(6), 234- 239.

Wynn Jr, D., & Williams, C. K. (2012). Principles for conducting critical realist case study research in information systems. MIS quarterly, 787-810.

Yin, R. K. (2003). Designing case studies. Qualitative Case Study Research: Design and Methods (pp. 19-53). SAGE.

Zimmerman, M. A., & Warschausky, S. (1998). Empowerment theory for rehabilitation research: Conceptual and methodological issues. Rehabilitation Psychology, 43(1), 3-16.

## Appendix A: Brief Summaries of the Three Cases

Case 1 – Transport Support Tool: Design of a transport support tool to facilitate independent use of public transport such as buses, trams, and subways. The tool included features such as identifying the correct bus, informing about arrival time and delays, recovering from unforeseen events such as getting off at the wrong stop or missing the bus, and communicating with parents or employers.

Goal: Assist individuals with IDD in transport situations  
![](/api/attachments/WG8HNGWK/fulltext/images/eeb1a9a40b551047d25addaa251b7a0b1a4bb95f0ffafd0d9625e1f71251d01f.jpg)  
Work with people with IDD

![](/api/attachments/WG8HNGWK/fulltext/images/5537dab966a46ef21785eb88672d602f13a5f8f71485b4f6468873b9ddac9577.jpg)  
Sample screenshots

Case 2 – Communication Support Tool: An existing communication support app for users with cognitive disabilities was adjusted and redesigned. The original version included a calendar and a feed of daily activities. The research effort added elements such as storytelling, an overview of memories, tagging and grouping of photos, and others

## Goal: Assist individuals with IDD in a variety of communication situations

![](/api/attachments/WG8HNGWK/fulltext/images/fde3a938121eaaef498d6de59f873b70030708bf8c980f62cc1cc19884b4e423.jpg)  
Work with people with IDD

![](/api/attachments/WG8HNGWK/fulltext/images/6507aae708dd288a3b3fca6db4a27896de9fe1a9434f4b4d8b36d24f8e89cf08.jpg)  
Sample screenshots

Case 3 – Career Support Tool: Design of a tool for reflecting on careers and supporting students with highfunctioning IDD to consider employment options. The users are supported through features such as mapping of interests, skills and abilities, goal setting, and progress overview.

Goal: Assist individuals with IDD to reflect and develop assets for career development

![](/api/attachments/WG8HNGWK/fulltext/images/23920ed69b01829ffd36637e8551b77f444bb61808e7ea993ee0cabf8d6c1b08.jpg)  
Work with people with IDD

![](/api/attachments/WG8HNGWK/fulltext/images/5a3f0a91ca467e9cfdf83f3fe238c29e5568ff4d11910785e70ca31730f95e08.jpg)  
Sample screenshots

Appendix B: Examples of Data Collected from the Cases

<table><tr><td>Case</td><td>Example</td></tr><tr><td colspan="2">Interviews with individuals with IDD</td></tr><tr><td>Case 1</td><td>I tried to not take photos of people. Because a girl sat next to me, and when I tried to aim (the smartphone) at the vending machine, she got in the photo. So, I had to get up and stand in front of the vending machine to be able to take the photo.</td></tr><tr><td>Case 2</td><td>Participant: Pictures? Here are the pictures.Researcher: Yes, what is that?Participant: It&#x27;s on, let&#x27;s see, it&#x27;s on the beach.Proxy: [name] beach.Participant: Yes.Researcher: He&#x27;s on a trip then?Proxy: They picked berries before Christmas.Proxy: [Name of support worker] has written a text about that they picked blackberries because they are going to make blackberry cream before Christmas. So it what it says there in the text.</td></tr><tr><td>Case 3</td><td>Researcher: When have we been there every time. How do you feel about that it is the same people attending?Participant: I know you, or I know a little more about you, so it&#x27;s okay for you to be here.Researcher: Do you think it would have been different if new people came every time?Participant: It had been a little strange.Researcher: How then?Participant: That I do not know exactly what they think is good and what they think then. And it can be difficult to ask for help from them because I have never met them before.Researcher: Do you think that it&#x27;s important that we know each other a little?Participant: Yes....I know a little more about you. I&#x27;m not afraid to say things if I&#x27;m wondering.</td></tr><tr><td colspan="2">Field notes from researchers</td></tr><tr><td>Case 1</td><td>The overall reflection is that evaluation in an environment that is as natural as possible gives several insights about the contextual impact and aspects that affect or should affect the design. Without the bus workshop we would not have captured and understood the feelings that arise for instance when the bus is not showing up and when you need to interact with another person.</td></tr><tr><td>Case 2</td><td>Interesting enough, the main part of the consecutive dinner dealt with different stories, narratives, and memories that they shared. They told us about hunting experiences that they had been part of, visits to the zoo, and bike tours.</td></tr><tr><td>Case 3</td><td>Before the workshop itself, I had emailed the parents and the teacher of the young people who would participate to ask if I should adapt the workshop and the questions in any way. This allowed us to adapt the questions and the young people could be prepared for what was to happen. In the end, it was good but it was difficult to know how to formulate myself so as not to write something inappropriate. For instance, a father interpreted it as childish to draw while for me it was a given design activity.</td></tr><tr><td colspan="2">Reflections from individuals in the support network</td></tr><tr><td>Case 1</td><td>NA</td></tr><tr><td>Case 2</td><td>They bring the iPad home with them, or to the community-based housing... so then everyone at different levels [organizations] can talk to the students about what has happened during the day. Because my students have a lot of benefits form photos and not text, because they cannot read or when something is just read to them it gets so abstract but if they can see it on a photo, then it is in a way easier to relate to.</td></tr><tr><td>Case 3</td><td>It is clear that they appreciate that we are there. They show this by engaging in saying things when we ask, talking about the solution unsolicited, making suggestions for improvements. The actual test that is run one by one is a little more &quot;serious&quot;. Then they may be quieter, but this time I encouraged them to speak loudly throughout the test. It worked very well for all three. They reflected on their choices, told me what they clicked on, and further what happened after they clicked on something.</td></tr></table>

Appendix C: Summary of Empirical Findings

<table><tr><td>Empirical findings</td><td>Case 1</td><td>Case 2</td><td>Case 3</td><td>Links to prior work</td></tr><tr><td>1. Complex, large, and ill-defined solution space not “owned” by any stakeholders</td><td>√</td><td>-</td><td>√</td><td>Privileging the context and the problem instance (Sein et al. 2011); Social inclusion is multidimensional and dynamic (Selwyn, 2002; Taket et al., 2009); Social capital to acknowledge norms and roles (Portes, 1998) and bridge and establish shared objectives (Bollard, 2009; Putnam, 2000).</td></tr><tr><td>2. Contributions in the form of anecdotes, experiences, and insights from people with IDD</td><td>√</td><td>√</td><td>√</td><td>Contributions from people in actual settings (Greenbaum &amp; Loi, 2012; Kensing &amp; Greenbaum, 2012); Self-determination to be in control and having a voice (Niemic &amp; Ryan, 2009); Social capital to recognize competence and trust (Portes, 1998; Putnam, 2000).</td></tr><tr><td>3. Contributions in the form of reflections about the research problem and process from people with IDD</td><td>√</td><td>-</td><td>-</td><td>Opportunity to contribute as an ethical right (Robertson &amp; Wagner, 2012); Self-determination to be in control and having a voice (Niemic &amp; Ryan, 2009); Social capital to recognize competence and trust (Portes, 1998; Putnam, 2000).</td></tr><tr><td>4. Dependence on the support network for developing appropriate solutions for people with IDD</td><td>-</td><td>√</td><td>-</td><td>Importance of situated knowledge (Greenbaum &amp; Loi, 2012; Kensing &amp; Greenbaum, 2012), and multiple voices (Robertson &amp; Wagner, 2012); Self-determination is influenced by relationships (Nonnemacher &amp; Bambara, 2011); Social capital to acknowledge norms and roles (Portes, 1998) and bridge and establish shared objectives (Bollard, 2009; Putnam, 2000).</td></tr><tr><td>5. Conflicting insights from the support network and people with IDD</td><td>-</td><td>√</td><td>-</td><td>Importance of situated knowledge (Greenbaum &amp; Loi, 2012; Kensing &amp; Greenbaum, 2012), and multiple voices (Robertson &amp; Wagner, 2012); Self-determination is influenced by relationships (Nonnemacher &amp; Bambara, 2011).</td></tr><tr><td>6. Different research conduct to overcome barriers to communication with people with IDD</td><td>√</td><td>√</td><td>√</td><td>Important to empower participants to contribute (Spinuzzi, 2005; Bjerknes &amp; Bratteteig, 1995); Self-determination entails being able to express preferences, solve problems and make decisions (Shogren et al., 2015).</td></tr><tr><td>7. Meticulous preparation and on-the-fly adjustments for working with people with IDD</td><td>√</td><td>√</td><td>√</td><td>Important to empower participants to contribute (Spinuzzi, 2005; Bjerknes &amp; Bratteteig, 1995); Self-determination entails being able to express preferences, solve problems and make decisions (Shogren et al., 2015).</td></tr><tr><td>8. People with IDD feel valued when part of the research activity</td><td>√</td><td>√</td><td>√</td><td>Importance of mutually influential efforts (Sein et al. 2011); Belongingness and a feeling of acceptance and being part of a group that one contributes to (Baumeister &amp; Leary, 1995; Mahar et al., 2013).</td></tr><tr><td>9. Participation from people with IDD based on personal reasons</td><td>√</td><td>-</td><td>√</td><td>Design efforts should enhance the participants situation (Spinuzzi, 2005; Greenbaum &amp; Loi, 2012); Self-determination to be in control and contribute out of interest (Deci &amp; Ryan, 2002).</td></tr><tr><td>10. Personal and social connection among members of the research team</td><td>√</td><td>√</td><td>√</td><td>Importance of mutually influential efforts (Sein et al. 2011); Belongingness and a feeling of acceptance and being part of a group that one contributes to (Baumeister &amp; Leary, 1995; Mahar et al., 2013).</td></tr></table>

## Appendix D: Mapping from Empirical Findings to Principles

<table><tr><td rowspan="2" colspan="2"></td><td colspan="5">Principles</td></tr><tr><td>Principle of respecting multi-perspective problem ownership and integrated solution design</td><td>Principle of surfacing emic contributions to guide artifact design</td><td>Principle of leveraging the support network for artifact design and research conduct</td><td>Principle of customizing the design-evaluate cycles with inclusive practices</td><td>Principle of pursuing authenticity in research collaborations</td></tr><tr><td rowspan="10">Empirical findings</td><td>Complex, large and ill-defined solution space not “owned” by any stakeholders</td><td>x</td><td></td><td></td><td></td><td></td></tr><tr><td>Contributions in the form of anecdotes, experiences, and insights from people with IDD</td><td></td><td>x</td><td></td><td>x</td><td></td></tr><tr><td>Contributions in the form of reflections about the research problem and process from people with IDD</td><td></td><td>x</td><td>x</td><td>x</td><td></td></tr><tr><td>Dependence on the support network for developing appropriate solutions for people with IDD</td><td>x</td><td></td><td>x</td><td></td><td></td></tr><tr><td>Conflicting insights from the support network and people with IDD</td><td></td><td></td><td>x</td><td>x</td><td></td></tr><tr><td>Different research conduct to overcome barriers to communication with people with IDD</td><td></td><td></td><td></td><td>x</td><td></td></tr><tr><td>Meticulous preparation and on-the-fly adjustments for working with people with IDD</td><td></td><td></td><td></td><td>x</td><td></td></tr><tr><td>People with IDD feel valued when part of the research activity</td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>Participation from people with IDD based on personal reasons</td><td></td><td>x</td><td></td><td></td><td>x</td></tr><tr><td>Personal and social connection among members of the research team</td><td></td><td></td><td></td><td></td><td>x</td></tr></table>

## About the Authors

Sofie Wass works as an associate professor in information systems in the Department of Information Systems at the University of Agder. Her research interest includes design science in eHealth and public services, with a focus on the inclusion of marginalized groups.

Elin Thygesen is a trained nurse and professor of e-health. She is the academic leader of the Center for E-health, which is a priority research center at the University of Agder in Norway. In her research, she has studied how technology solutions can support different groups such as healthcare personnel, patients, and vulnerable groups. She has participated in several projects funded by the Norwegian Research Council and the EU.

Sandeep Purao is a Trustee Professor and the director of the entrepreneurship ecosystem initiative at Bentley University. He is also a visiting professor at Agder University. His research focuses on the design of technologies for social good and the sciences of design. His work has been published across disciplines in journals including MIS Quarterly, Information Systems Research, and several others. His research has been funded by the National Science Foundation, industry consortia, private foundations, and private industry.

Copyright © 2023 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
