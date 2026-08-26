---
otero_id: 8352
otero_key: "ZDGP6YXC"
title: "Interleaved Design for E-Learning: Theory, Design, and Empirical Findings"
authors: "Andy Tao Li; De Liu; Sean Xin Xu; Cheng Yi"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2023/17206"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# INTERLEAVED DESIGN FOR E-LEARNING: THEORY, DESIGN, AND EMPIRICAL FINDINGS<sup>1</sup>

Andy Tao Li International Institute of Finance, School of Management, University of Science and Technology of China Hefei, Anhui China {andytaoli@ustc.edu.cn}

De Liu Carlson School of Management, University of Minnesota – Twin Cities Minneapolis, MN U.S.A. {deliu@umn.edu}

Sean Xin Xu Center for AI and Management, School of Economics and Management, Tsinghua University Beijing, China {xuxin@sem.tsinghua.edu.cn}

Cheng Yi School of Economics and Management, Tsinghua University Beijing, China {yich@sem.tsinghua.edu.cn}

The rapid development of e-learning has drawn increasing attention to the issue of how learners’ learning activities can be better structured using technologies. This study focuses on how to improve e-learning performance by optimizing the structuring of learning sessions from the perspective of interleaving (i.e., mixing different topics in a learning session). Following the design science paradigm, this study chooses cognitive load theory as the kernel theory and proposes a new interleaving design—related-interleaving —that populates an interleaved session with related topics as a way of reducing cognitive load during an interleaved session. Drawing on the theoretical predictions, we design and instantiate a personalized learning system with the related-interleaving strategy by fusing educational strategies and machine learning techniques. The results from a two-month field experiment confirm that related-interleaving outperforms non-interleaving and unrelated-interleaving. Our findings also reveal that compared with unrelated-interleaving, related-interleaving benefits weak learners more and thus helps reduce learning performance disparities. This study demonstrates how personalized e-learning systems can be further improved from the perspective of interleaving.

Keywords: E-learning, interleaving, topic relatedness, machine learning, cognitive load theory, weak learner

## Introduction

The e-learning industry has grown rapidly in recent years, with over 60% of postsecondary degree seekers in the U.S. engaged in some form of e-learning.<sup>2</sup> Compared with traditional classroom-based learning, e-learning allows learners to access course materials at any time and from any location with an internet connection. Moreover, e-learning platforms can better personalize learning activities to suit each learner’s progress and style (Chen et al., 2018; Park & Lee, 2008). Despite these advantages, e-learning still faces criticism for its limited learning effectiveness (Bettinger et al., 2017; Figlio et al., 2013; Goudeau et al., 2021). Compared to learners in traditional classrooms, e-learners adopt a more passive mode of learning: they mostly consume and record information rather than actively reflecting upon it based on existing knowledge (Furenes et al., 2021; Shrivastav & Hiltz, 2013). This can lead to a limited depth of understanding and a low ability to transfer the knowledge learned from one context to another (Delgado & Salmerón, 2021).

One strategy to promote active thinking and learning effectiveness, as advocated by educational researchers, is to mix practices of different topics in the same learning session—called interleaving (Firth et al., 2021). In interleaved learning, learners are exposed to different topics in one session, and learning about the same topic is spread across multiple sessions (Rohrer et al. 2020). For example, when learning Python data structures, such as matrices, tuples, and dictionaries, an interleaved design would involve a series of sessions, each mixing exercises for different data structures instead of each focusing on one data structure. Advocates of interleaved learning suggest that it encourages learners to actively identify different topics and corresponding strategies based on their existing knowledge because they cannot simply rely on repetitive practices to solve the same type of problem over and over again (Jaeger et al., 2016). This process can improve learners’ ability to identify boundaries and connections among different topics, leading to a deeper understanding of the subject (Mielicki & Wiley, 2022; Rohrer, 2012; Rohrer et al., 2014). To our knowledge, however, e-learning platforms have not embraced interleaving. The prevailing design is still noninterleaving; that is, offering multiple practices for one topic in a session before moving on to the next topic (Hussain et al., 2019; Loghin et al., 2008). Given the potential benefits of interleaving, research is needed on how to leverage it in e-learning settings to improve e-learning effectiveness.

Existing interleaving designs, which are designed for traditional face-to-face instructions, may not work well for e-learning settings for a few reasons. First, past findings show that the effects of interleaving are not always positive (Firth et al., 2021; Rohrer et al., 2020), in part because students find interleaving more difficult than noninterleaving (Rohrer et al., 2015; Tauber et al., 2013; Yan et al., 2016). This could pose a special challenge for e-learning because learners on e-learning platforms may be more susceptible to distractions and cognitive overload (Delgado & Salmerón, 2021). In particular, online learners are often learning in environments that are not specifically designed for focused learning (Conrad et al., 2022) and online platforms themselves can also be distracting, with various pieces of information competing for attention (Dontre, 2021; Shrivastav & Hiltz, 2013; Wang, 2022). Hence, when designing interleaving for e-learning, it is important to consider how interleaving will affect the cognitive load on learners. To do so, a better theoretical understanding of the relationship between interleaving and learners’ cognitive resources is needed and interleaving needs to be designed to alleviate the concern of further overloading e-learners.

Moreover, existing interleaving designs require teachers to pick topics for each interleaved session and the same design is offered to all learners. Such traditional designs do not take advantage of the rich data on learners’ past activities and performance, while on e-learning platforms, the easily accessible data can be leveraged to offer personalized and adaptive learning sessions for each individual learner. Therefore, for interleaving to be most effective, the traditional interleaving design must be modernized to suit the highly dynamic e-learning settings.

To address the aforementioned gaps, this research offers a theory-driven interleaving design for e-learning settings that is personalized, adaptive, and cognizant of each learner’s cognitive load. To achieve this goal, we first draw on cognitive load theory (CLT) to develop an understanding of the relationship between interleaved learning and learners cognitive load. CLT is a fundamental theory of learning that focuses on the cognitive demands of learning (Sweller, 2011). Based on CLT, we propose that while interleaved learning prompts learners to make connections between different topics and expand learning opportunities, it also increases learners’ cognitive load compared to noninterleaving, which may reduce learning effectiveness. Accordingly, we propose a new interleaving design— related-interleaving—that requires an interleaved learning session to consist of related topics so that it reduces the cognitive resources required for basic processing while still offering opportunities for making connections between different topics. Based on this theoretical perspective, we also anticipate that weaker learners, who have less working memory for encoding new knowledge, are more likely to benefit from this related-interleaving design.

We then follow the design science guidelines to implement an interleaving design for e-learning that is data-driven, personalized, and adaptive. Our design framework includes the following components: (1) dynamic detection of learners’ weak topics based on their past performance using a hidden Markov model (Reddy et al., 2016; Wilson et al., 2016), (2) a knowledge map for capturing relatedness between different topics, which is dynamically updated using fuzzy association rules (Tseng et al., 2007), and (3) a scheduling engine that assembles practice materials in an adaptive, personalized manner. The scheduling engine ensures that the topics covered in each session are suitable for the learner’s progress (based on the detected weak topics) and are related (based on the knowledge map).

To evaluate our design, we compare our related-interleaving design with non-interleaving (where each learning session focuses on a single topic) and unrelated-interleaving (where interleaved topics are chosen without considering topic relatedness) in a randomized field experiment involving 510 middle school students using an e-learning platform designed by this research team. Our results show that in the context of e-learning, related-interleaving leads to better learning performance than non-interleaving and unrelatedinterleaving. Furthermore, the benefit of related-interleaving over unrelated-interleaving is more prominent for weak learners than for strong learners. This suggests that our related-interleaving design for e-learning not only improves e-learning performance overall but also reduces the performance disparities between weak and strong learners.

## Literature Review

## Research on E-learning Design

The low effectiveness of e-learning has been a major concern for educators and researchers (Bettinger et al., 2017; Figlio et al., 2013; Goudeau et al., 2021). To ensure the overall effectiveness of e-learning initiatives, there is an urgent need to develop targeted strategies and interventions that cater to the unique needs of online learners (Hansen & Reich, 2015; Kizilcec et al., 2017; Reich & Ruipérez-Valiente, 2019). In response to this challenge, information systems scholars have approached technology-based e-learning designs from multiple perspectives (Alavi & Leidner, 2001; Gupta & Bostrom, 2013; Gupta & Bostrom, 2009; Piccoli et al., 2001). One stream of research focuses on technology-enabled behavioral nudges to engage online learners (Damgaard & Nielsen, 2018) and facilitate self-regulation of the learning pace (Santhanam et al., 2008). Examples of these nudges include on-the-hour cues (Huang et al., in press), call-toactions (Huang et al., 2021), and gamified interventions (Leung et al., 2023). A second stream studies the effects of communication or collaboration support tools that facilitate online learners’ interaction with each other (Kulkarni et al., 2015) and with instructors (Dennen et al., 2007).

Our study belongs to the third stream, which focuses on the structuring of e-learning activities. For example, researchers have examined how to choose appropriate learning session lengths (Manasrah et al., 2021) and incorporate active learning activities during online lectures (Khan et al., 2017; Sandrone et al., 2021). A more recent focus is personalizing online learners’ experience, including detecting weak topics (i.e., identifying gaps in learners’ knowledge) for the purpose of recommending appropriate topics to learn next (e.g., Bauman & Tuzhilin, 2018; Wilson & Nichols, 2015)

and adapting the challenge level of learning materials (Kim et al., 2020). Several researchers have further explored how to optimize the sequence of learning sessions, with each session dealing with a different weak topic. For example, some studies have suggested arranging topics from low to high difficulty levels across sessions (Hussain et al., 2019; Jiang et al., 2022). Others have optimized the sequence of learning sessions based on topic similarity and learner preferences (Al-Muhaideb & Menai, 2011; Chen, 2008; Jeng & Huang, 2019; Kurilovas et al., 2015). This research differs from prior studies in that instead of studying the sequence of topics or learning sessions, we are concerned with how to interleave different topics in one session.

## Interleaved Session Design

Interleaved learning, as proposed in the education field, exposes learners to a few different topics in a single learning session (e.g., ABC, BCD) (Taylor & Rohrer, 2010). This contrasts with a conventional non-interleaved (or “blocking”) design, which exposes learners to a single topic repeatedly in a learning session (e.g., AAA, BBB). Educational researchers propose that interleaving different topics in one session can encourage learners to probe the connections and differences among topics and associate problems with the corresponding strategies, thus leading to better learning outcomes (Birnbaum et al., 2013; Rohrer et al., 2014; Taylor & Rohrer, 2010).

Thus far, most research on interleaved learning has focused on examining whether interleaving can outperform noninterleaving. Some studies demonstrate that interleaving is more beneficial in various subject domains, such as math, category induction, sports, and medical training (Foster et al., 2019; Kornell & Bjork, 2008; Rohrer et al., 2015). Other studies, however, suggest that interleaved learning may not always outperform non-interleaved learning (Carvalho & Goldstone, 2014; Hausman & Kornell, 2014). For example, an interleaved design is not as effective as a non-interleaved design when interleaved concepts are highly distinguishable (Carvalho & Goldstone, 2014; Zulkiply & Burt, 2013). A few recent studies further suggest that learners may struggle to process interleaved information when their memory capacities are limited, which may significantly dilute the benefits of interleaving (Firth et al., 2021; Sana et al., 2018).

The issue of how to design interleaving has received scant attention in this literature. One exception is Yan and Sana (2021), which explores interleaving at different levels; that is, whether to interleave within a domain (e.g., mixing different topics of statistics) or across domains (e.g., mixing topics of statistics and physics). Their research, however, does not address the question of how to choose topics from the same domain.

<table><tr><td colspan="2">Table 1. Theory-Driven Design Framework for an Interleaved E-learning System</td></tr><tr><td>Research goal</td><td>Improve the e-learning session design from the interleaving perspective</td></tr><tr><td>Kernel theory</td><td>Cognitive load theory (CLT) theorizes that the ultimate design goal to achieve effective learning is to manage learners&#x27; basic processing load and maximize their schema building. Based on CLT, increasing the relatedness of interleaved topics (i.e., as in related-interleaving) can reduce basic processing load and provide more opportunities for schema building, thus leading to better learning performance.</td></tr><tr><td>Meta-requirements</td><td>1. Dynamically detect the learner&#x27;s weak topics.2. Increase the relatedness of weak topics within the same learning session.3. Schedule available learning materials according to the criteria of weak topics and topic relatedness.</td></tr><tr><td>Meta-design</td><td>1. Use the hidden Markov model to dynamically identify the mastery level of each topic for a focal learner.2. Include expert knowledge and fuzzy association rules to build a knowledge map to detect topic relatedness.3. Design a scheduling engine that implements the scheduling goals.</td></tr><tr><td>Testable hypotheses</td><td>H1: Compared with unrelated-interleaving, related-interleaving leads to better learning performance.H2: Compared with non-interleaved learning, related-interleaving leads to better learning performance.</td></tr><tr><td>System instantiation</td><td>Instantiate the meta-design artifacts and implement the designed system.</td></tr><tr><td>Experimental evaluation</td><td>Empirically evaluate the testable hypotheses via a randomized field experiment and post hoc analyses on the heterogenous effect of related-interleaving.</td></tr></table>

## Designing Related-Interleaving for E-learning

This study focuses on the design of interleaving. We follow the design science research approach (Abbasi & Chen, 2008; Walls et al., 1992) to develop a system for intelligent, data-driven interleaved learning for e-learning platforms (see Table 1). In doing so, we selected CLT (Sweller, 2011) as the kernel theory to motivate our related-interleaving design. CLT is a fundamental theory about the relationship between the cognitive demands of learning and learning performance. Given the recent suggestions that a learner’s memory capacity can be a barrier to realizing the benefits of interleaving (Firth et al., 2021; Sana et al., 2018), we posit that CLT is the appropriate framework for analyzing both the benefits and costs of interleaving. This cost perspective is especially relevant when guiding the design of interleaving sessions for e-learning, as elearners typically have limited cognitive resources available (e.g., Delgado & Salmerón, 2021). Guided by CLT, we propose a new related-interleaving design to lessen the cognitive load on learners while still offering opportunities to make connections between different topics. We then identify meta-requirements for the related-interleaving design for e-learning systems and propose meta-designs that satisfy these requirements. We also report on our instantiation of an e-learning system that integrates the meta-designs. We present our design framework in Table 1 and discuss the details in the following sections.

## A Brief Overview of Cognitive Load Theory

CLT is one of the most widely used theories in learning and instruction (Kalyuga, 2007; Sweller, 2010). CLT is built on an understanding of the role of memory in learning activities. It recognizes that human beings use working memory for receiving and processing new information and long-term memory for storing and organizing processed information in the form of schemas (Sweller, 2011). Such cognitive schemas can be quickly retrieved and used in a flexible way to resolve problems; hence, building such schemas is an essential goal of learning. When a learner approaches new information, basic processing occurs first. This includes receiving information and retrieving existing schemas to understand the information. Then, schema building may occur (Sweller et al., 2019). The latter includes, for example, categorizing information, abstracting away unnecessary details, identifying relationships with other information, and integrating with existing schemas.

Crucially, both basic processing and schema building require working memory, which is very limited in capacity and duration (Zhu & Watts, 2010). When basic processing consumes too much working memory, schema building is reduced, leading to suboptimal learning. In particular, the amount of working memory used (or the cognitive load) for basic processing is a function of the complexity of the materials, the presentation format, and whether the learner can retrieve and apply relevant schemas from long-term memory. Applying existing schemas can drastically lessen the cognitive load needed for basic information processing (Kleider et al., 2008). Overall, a fundamental principle of CLT for effective learning session design is to manage the cognitive load for basic processing, allowing sufficient resources for schema building.

Applying CLT to instructional design, scholars have focused on methods to reduce the basic processing load, such as presenting information in an easy-to-understand format (e.g., by incorporating multimedia and diagrams) (Brunken et al., 2003; Mayer & Moreno, 2003), providing worked examples or partial solutions for practice (Renkl, 2014; Sweller et al., 2019) and incorporating multimodal information (e.g., visual and auditory information) (Ginns, 2005). A few other studies have explored approaches to deliberately increase the basic processing load within learners’ working memory capacity to provide more opportunities for schema building. For instance, it has been suggested that providing practices with higher variability for the same topic leads to better learning outcomes when the total cognitive load remains within limits (Likourezos et al., 2019).

The above studies primarily focus on designing practices or learning materials for a specific learning topic, whereas this study focuses on how to interleave different topics in a learning session. Therefore, this research addresses a gap in the literature of CLT-based instructional design and adds new perspectives on how interleaving designs may affect cognitive load and learning performance.

## CLT and Interleaving

In non-interleaved learning, learners encounter materials of the same topic repeatedly in a learning session. Observing the commonality between materials of the same topic can facilitate building schemas of this topic, which, in turn, can be used to quickly process other materials of the same topic. Noninterleaved learning thus drastically reduces learners’ cognitive load for basic processing. However, because learners can apply the same schemas in the entire session, opportunities for refining or building new schemas are also limited.

In interleaved learning, learners have opportunities to process materials for different topics in the same session, which may lead to the construction of higher-level schemas that can help learners “connect the dots” among different topics (Rohrer et al., 2014). Furthermore, learners can also contrast different topics, which exposes them to the limitation of schemas built for specific topics, potentially leading to more refined and robust schemas (Birnbaum et al., 2013; Rohrer, 2012; Rohrer et al., 2015). Thus, interleaved learning can expand schemabuilding opportunities. However, interleaved learning may also increase learners’ cognitive load and elevate the overload risk. Given that learners cannot easily leverage schemas developed for one topic to the next topic, the cognitive load for basic processing in interleaved learning can be substantially higher than that in non-interleaved learning. As learners devote more cognitive resources to basic processing, they may not have enough cognitive capacity for schema building (Sana et al., 2018). This is highly relevant in e-learning, where learners tend to operate with reduced cognitive resources, but this downside has not been adequately recognized in the literature.

To mitigate the overload risk of interleaved learning and promote its schema-building benefits, we propose an interleaving design called related-interleaving, which involves purposefully choosing highly related topics for inclusion in an interleaved learning session. <sup>3</sup> When the topic relatedness is relatively high, schemas built for one topic can be partially reused for a related topic, lessening the cognitive load for basic processing and thus mitigating the overload risk (O’Donnell et al., 2002; Sweller, 2010). For example, the schemas built for Python arrays can facilitate the understanding of matrices. Hence, these two topics can be included in the same interleaved session. Related-interleaving stands in contrast to traditional interleaving designs that do not consider topic relatedness and thus have low or no topic relatedness (“unrelated-interleaving” hereafter).

High topic-relatedness can also provide more schema-building opportunities. When topics in a learning session are highly related, more “dots” can be connected, which can facilitate the construction of high-level schemas. Furthermore, when topics are highly related, there is also a greater need to compare and contrast them, which can help learners fix misconceptions about a particular topic and develop a more robust and nuanced understanding of different topics (Birnbaum et al., 2013; Carvalho & Goldstone, 2014). For instance, when Python learners resolve a question on arrays next to one on matrices, they are likely prompted to deliberate on the connections and distinctions between the two topics and may thus form a deeper understanding of both topics.

spheroids and wedges are similar topics. However, in our study, these topics were not related because knowing how to compute volumes of spheroids does not depend on the knowledge of computing volumes of wedges, and vice versa; instead, computing volumes of spheroids (i.e., the area of the circle times 2/3 of the height) should be related to computing the area of circles, because computing volumes of spheroids depends on correctly calculating the area of circles.

![](/api/attachments/ZDGP6YXC/fulltext/images/604a832e5754261c065daf8aa0a6129d488b882e37a928342b8f3bb4097587f0.jpg)

## Meta-Requirements for Related-Interleaving

Guided by the kernel theory, we now discuss the metarequirements for our proposed design artifact. As stated in the introduction, our design goals include improving e-learning session design using related-interleaving and making learning session design more personalized and adaptive by leveraging the rich data generated in e-learning. To fulfill these goals, we propose a related-interleaving design with the following key components: weak topic detection, topic-relatedness modeling, and a scheduling engine. The weak-topic-detection component draws upon a learner’s past learning record to produce a personalized list of weak topics at a specific moment. The topic-relatedness-modeling component builds and updates a knowledge map that models relatedness among topics. The scheduling engine chooses from available learning materials that address a learner’s weak topics while meeting the criteria of related-interleaving. Next, we discuss the three components separately in further detail and how they work together as a system.

## Meta-Design I: Weak Topic Detection Using Hidden Markov Model

According to CLT, learning occurs when novel information prompts learners to build new schemas or to enhance existing ones (Sweller, 2011). By detecting each learner’s weak topics and allowing the learner to focus on unmastered topics, the session design uses the learner’s time efficiently. For this purpose, our e-learning system maintains a list of weak topics for each learner at any time. Weak topics are topics not yet mastered by a learner, as indicated by the learner’s poor performance on the topic (Bauman & Tuzhilin, 2018).

Previous work has explored several approaches to detect learners’ weak topics. One approach involves comparing a learner’s overall performance in practicing a specific topic with a predefined threshold to identify weak topics (Bauman & Tuzhilin, 2018). Another approach uses user-based collaborative filtering to suggest unmastered topics to learners with similar learning conditions (Klašnja-Milićević et al., 2011). More recently, Bayesian knowledge tracing models have been introduced to consider learners’ performance at the individual practice level and to model the hidden transition of the learner’s states in terms of topic mastery (Pelánek, 2017). This approach acknowledges that a learner can gain mastery of a topic over time through practice but may also lose mastery as time passes. It has become the prevailing approach on personalized learning platforms (Abdelrahman et al., 2023).

Our model builds on previous work on Bayesian knowledge tracing that captures temporal changes in students’ topic mastery (Pardos et al., 2013; Reddy et al., 2016). The evolution of topic mastery can be represented by the transition process in a hidden Markov model (HMM) and the observed performance on a topic can be captured by the emission process of the HMM (Chen et al., 2018). To model the evolution of a learner’s topic mastery, we built an HMM, as shown in Figure 1, consisting of (1) a hidden transition process for capturing the evolution of topic mastery and (2) an observed emission process for capturing the observed learning performance. Formally, we modeled a learner s’s mastery of the topic c at time t (defined as the time of the t-th practice of the topic) as a latent state $( y _ { s t } ^ { c } )$ with N ordered levels.<sup>4</sup> The emission $( x _ { s t } ^ { c } )$ was defined as answer correctness, which took a value of “1” if learner s answered the question on the topic c correctly at time t and $\mathbf { \bar { \nu } } ^ { 6 } 0 ^ { , }$ otherwise.

Hidden transition process: HMM assumes that the evolution of hidden states over time follows a Markov chain, in which the next state $( y _ { s t + 1 } ^ { c } )$ depends only on the current state $( y _ { s t } ^ { c } )$ and the transition covariates $( W _ { s t } ^ { c } )$ . We included a vector of covariates $( W _ { s t } ^ { c } )$ affecting state transitions, comprising both time-invariant learner characteristics $( \mathrm { e . g . }$ gender and age) and time-variant learning history $( \mathrm { e . g . }$ , the number of correct answers on topic c) (Kim & Krishnan, 2019). We provide more details about the covariates in Appendix A.

Let $p _ { s t } ^ { c } ( i , j )$ represent the probability of learner $s ^ { \prime } s$ mastery of topic c transiting from state i at time t to state j at time t+1. $P _ { s t } ^ { c } = [ p _ { s t } ^ { c } ( i , j ) ]$ is an $N \times N$ transition matrix for learner s on topic c. Following Singh et al. (2011), we assume that the topic mastery state can only transit from one state to its adjacent states and that the transition follows a random walk. Consequently, the transition matrix $\pmb { P } _ { s t } ^ { c }$ is illustrated below:

$$
\boldsymbol {P} _ {s t} ^ {c} = \left[ \begin{array}{c c c c c} p _ {s t} ^ {c} (1, 1) & p _ {s t} ^ {c} (1, 2) & \dots & 0 & 0 \\ p _ {s t} ^ {c} (2, 1) & \ddots & & & 0 \\ \vdots & & p _ {s t} ^ {c} (\mathrm{i}, \mathrm{j}) & & \vdots \\ 0 & & & \ddots & p _ {s t} ^ {c} (N - 1, N) \\ 0 & 0 & \dots & p _ {s t} ^ {c} (\mathrm{N}, \mathrm{N} - 1) & p _ {s t} ^ {c} (N, N) \end{array} \right]
$$

Following Singh et al. (2011), we assume that the hidden probability follows an ordered logit model. Specifically, we let the probability of a learner’s mastery of topic c transiting to a lower-ordered state, a higher-ordered state, or the same state, respectively, as follows:

$$
p _ {s t} ^ {c} (\mathrm{i,i-1}) = \frac {\exp {(u _ {i} ^ {l c} - \pmb {\beta} _ {i} ^ {c \prime} \pmb {W} _ {s t} ^ {c} - \delta_ {s t} ^ {c})}}{1 + \exp {(u _ {i} ^ {l c} - \pmb {\beta} _ {i} ^ {c \prime} \pmb {W} _ {s t} ^ {c} - \delta_ {s t} ^ {c})}}
$$

$$
p _ {s t} ^ {c} (\mathrm{i}, \mathrm{i} + 1) = 1 - \frac {\exp {(u _ {i} ^ {h c} - \pmb {\beta} _ {i} ^ {c \prime} \pmb {W} _ {s t} ^ {c} - \delta_ {s t} ^ {c})}}{1 + \exp {(u _ {i} ^ {h c} - \pmb {\beta} _ {i} ^ {c \prime} \pmb {W} _ {s t} ^ {c} - \delta_ {s t} ^ {c})}}
$$

$$
p _ {s t} ^ {c} (\mathrm{i}, \mathrm{i}) = 1 - \mathrm{p} (\mathrm{i}, \mathrm{i} - 1) _ {s t} - \mathrm{p} (\mathrm{i}, \mathrm{i} + 1) _ {s t}
$$

where $u _ { i } ^ { l c }$ and $u _ { i } ^ { h c } \ : ( u _ { i } ^ { l c } < u _ { i } ^ { h c } )$ are two threshold values that are used to divide the transition probabilities. $\pmb { \beta } _ { i } ^ { c }$ is the vector of topic-specific and state-dependent parameters for $W _ { s t } ^ { c } . \delta _ { s t } ^ { c }$ is the random noise.

State-dependent emission process: The probability of a learner s answering a question on topic c correctly $( x _ { s t } ^ { c } )$ at time ?? is a function of the topic mastery state $y _ { s t } ^ { c }$ and some covariates $( { Z _ { s t } ^ { c } } )$ The covariates include time-invariant learner characteristics, time-variant learning history $( \mathrm { e . g . }$ the number of correct answers on the focal topic c), and timevariant learner behavioral tendencies (e.g., the average time spent on each answer of the focal topic c and its standard deviation) (Ayabakan et al., 2016).

Learners with different topic mastery levels $( y _ { s t } ^ { c } )$ will have different distributions of correctly answering the topicrelated questions $( x _ { s t } ^ { c } )$ . We thus modeled $x _ { s t } ^ { c }$ as a Gaussian mixture distribution, which is generated by the different discrete hidden states $( y _ { s t } ^ { c } )$ . Answer correctness $x _ { s t } ^ { c }$ depended on the probabilities of the learner being in different mastery states of topic c. Following Ayabakan et al. (2016), we chose the logit model to represent the emission probability as follows:

$$
p (x _ {s t} ^ {c} = 1 _ {| y _ {s t} ^ {c} = i}) = \frac {1}{1 + e ^ {- (\gamma^ {c} + \alpha_ {i} + \theta_ {\mathbf {i}} ^ {\prime} z _ {s t} ^ {c} + \varepsilon_ {s t})}},
$$

where $\gamma ^ { c }$ represents the topic-level heterogeneity (e.g., different difficulty levels) and $\alpha _ { i }$ captures the heterogeneity associated with the mastery state $i . \pmb \theta _ { i }$ is the vector of statedependent parameters for $\pmb { Z _ { s t } ^ { c } }$ and $\varepsilon _ { s \mathrm { t } }$ is the random noise.

We then estimated the HMM by maximizing the likelihood of the observed emission sequences. More details about the estimation of the HMM are presented in Appendix A. The outcomes of this process yielded a personalized list of weak topics that are specifically tailored to the focal learner’s dynamic learning progress.

## Meta-Design II: Topic Relatedness Learning Using a Knowledge Map

With weak topics detected, the next question is what topics can be mixed in a learning session. As discussed earlier, CLT suggests that related-interleaving can reduce learners’ cognitive workload for basic information processing while still providing knowledge integration opportunities. Hence, our second meta-requirement is to model topic relatedness. Topic relations are typically represented in the form of the knowledge map, which is a graph model where nodes (points/vertices) represent topics and edges (arcs/links) portray the dependency relationships between topics (Atapattu et al., 2017; Balaid et al., 2016; Lee & Segev, 2012). An intuitive and common understanding of topic dependency in learning contexts is that Topic B depends on Topic A if mastering Topic A can help learners master Topic B (Tseng et al., 2007). This understanding is also consistent with the principles of CLT; that is, learners can leverage the schema built from learning Topic A to understand Topic B more efficiently.

Existing e-learning platforms employ various methods to construct knowledge maps. Some platforms depend on domain experts to manually create knowledge maps, which can often ensure a high level of reliability but requires substantial labor (Wilson & Nichols, 2015). Other platforms employ text mining techniques, such as TF-IDF and NLP, to extract knowledge maps from learning materials such as syllabi and reading materials (Bauman & Tuzhilin, 2018). In addition, a data-driven approach involves learning knowledge maps based on learners’ learning records, enabling the capture of subtle changes in topic relationships over time (Balaid et al., 2016; Tseng et al., 2007).

We chose an approach of combining expert knowledge and data insights by initializing the knowledge map using expert knowledge and then refining it dynamically based on learners’ learning records. This hybrid approach is based on the following considerations. On one hand, many teachers have some expert knowledge about topic dependency, which is a valuable source of information, especially when topic dependency data are sparse. On the other hand, building an exhaustive knowledge map is a time-consuming process and is prone to incompleteness. Therefore, the creation of a knowledge map needs to be automated using topic dependencies observed in the data. Specifically, we developed a set of expert rules $( M _ { 0 } )$ by encoding the knowledge of several senior teachers at the school where we conducted our experiment. Then, we used a data-driven method to dynamically fine-tune the knowledge map. Specifically, every day d at midnight, we retrieved all the historical learning records and discover the data-driven rule set $( M _ { d } )$ . We then combined the two rule sets to form an updated knowledge map.

We represent topic dependencies learned from the data as fuzzy association rules. The conditional dependence nature of fuzzy association rules corresponds well to the topic dependencies that we intend to capture. Specifically, we infer topic dependencies from learning data if we observe conditional dependence between learners’ performances on two topics (Tseng et al., 2007). For example, if we observe many concurrences of incorrectly answered records of Topics A and B and if learners tend to perform poorly on Topic B when they perform poorly on Topic A, we can infer that Topic B depends on Topic A (i.e., an association rule A → B).

An important decision in fuzzy association rule mining is to determine the thresholds for support (i.e., the concurrence of poor performance on both topics), ??, and confidence (i.e., the proportion of poor performance on Topic B given poor performance on Topic A), ?? (Chen & Wei, 2002; Tseng et al., 2007). Choosing higher support and confidence thresholds (?? and $\beta )$ can lead to a higher quality of the discovered rules but may result in omissions of qualified rules. In addition, in our context, these choices also have implications for the degree of conflict between the set of discovered rules $M _ { d }$ and the set of expert rules $M _ { 0 } .$ , which are held to be true but incomplete. Combining these considerations, we chose ?? and $\beta$ to maximize (?? + $\beta ) \sum _ { ( l \in M _ { 0 } \cap l \in M _ { d } ) } ( C o n f i d e n c e ( l ) )$ . This heuristic objective function trades off the agreement between the discovered rules and expert rules, as measured by the sum of the confidence of rules at the intersection of the two sets of rules, and the quality of discovered rules (combining support and confidence). Once we determined the two thresholds, we used them in subsequent rule mining to reveal the hidden dependencies among topics and then dynamically updated the knowledge map. Appendix B shows the knowledge map updating details.

For example, in the current context, “making inferences” and “retrieving relevant information” are two different learning topics in English reading comprehension. Learning how to retrieve relevant information from an article can help learners make correct inferences. Hence, “making inferences” depends on “retrieving relevant information.” Figure 2 shows the terminal state knowledge map in our context. We validated our entire approach by demonstrating the terminal-state knowledge map to the senior teachers, who agreed with the new rules generated by fuzzy association rule mining.

## Meta-Design III: Scheduling Engine for Choosing Learning Materials

With weak topics detected and topic relatedness discovered, the next question is how to deliver materials that cover mixed topics to each learner. From the perspective of CLT, learning is more effective when the learning materials are personalized and dynamically adjusted to reflect learners’ progress so that their cognitive load can be optimized. This calls for a scheduling engine. In our learning context, learners learned through exercises. Each exercise consisted of a set of multiple-choice assessment questions and each question covered a single topic (but questions in the same exercise may collectively cover a few topics). The goal of the scheduling engine was to choose the set of questions for each learning session to meet the session design objectives, including the number of topics covered, topic mastery level, and topic-relatedness.

We implemented both related-interleaving and two benchmark session designs (i.e., non-interleaving and unrelated-interleaving). For the non-interleaving design, we chose exercises that had the highest concentration on the topic with the highest weakness ranking (i.e., probability of being unmastered), with concentration defined as the percentage of questions covering a topic in an exercise. In most cases, the chosen exercise was 100% concentrated on one topic, meaning that all questions were about the same topic.

![](/api/attachments/ZDGP6YXC/fulltext/images/15a0bc9733e0dd9999215c52818141cc7b8eace95e573bc30c1936525f221245.jpg)  
Note: A circle represents a topic. An edge represents that a topic depends on a preceding topic. For example, A1 → A2 captures that topic A2 depends on topic A1.

Figure 2. Terminal-State Knowledge Map  
![](/api/attachments/ZDGP6YXC/fulltext/images/13297acae92882b124071303ebee21516ce47880701bad323907deb79a0a0020.jpg)  
Figure 3. An Example of Related-Interleaving Session Design

As an illustrative example, Figure 3 depicts a knowledge map that models the relatedness among nine topics (A to I). In this example, the learner has five unmastered topics A, B, C, D, and F (yellow-shaded). The number shown next to an unmastered topic denotes the weakness probability; i.e., the probability that the learner has not mastered the topic. Suppose we have a list of unattempted exercises covering different topics as shown in the figure. In our design, Topic A had the highest weakness probability $\left( \boldsymbol { p } = 0 . 8 6 \right)$ and would thus be the topic for the current learning session. Exercise a, which had the highest concentration of Topic A, was therefore used for the current learning session for the non-interleaving design.

For the unrelated-interleaving design, the scheduling engine chose exercises that covered the largest number of unmastered topics and broke ties by the aggregated weakness ranking of the topics covered in the exercise.<sup>5</sup> Continuing with the example in Figure 3, the schedule engine would choose Exercise c, which covers three unmastered topics with the highest weakness ranks.

For the related-interleaving design, we chose exercises that covered the largest number of unmastered topics and broke ties based on a modified topic ranking that considered both weakness and relatedness among topics. The modified topic ranking was constructed as follows. Starting from Topic A, which has the highest weakness ranking, we located all the topics that Topic A depended on in the knowledge map, such as Topic C. If Topic C was an unmastered topic, we inserted Topic C just before Topic A in the ranking. This ensured that when we selected Topic A, we also included unmastered Topic C, which Topic A depended on. We did this repeatedly for all unmastered topics to arrive at a modified ranking of topics (see Appendix C for a pseudo algorithm). We then calculated an aggregated ranking for each exercise by summing up the modified rankings of all unmastered topics covered. We selected the exercise with the highest aggregated ranking to represent a related-interleaving design (see Appendix C for a pseudo-scheduling algorithm). Continuing with the example in Figure 3, the schedule engine generated a modified topic ranking (i.e., D, C, A, B, F); based on this, the modified aggregated weakness was calculated for each exercise. Then, the schedule engine chose Exercise e for related-interleaving since its modified aggregated weakness ranked higher than the other exercises.

## Overall System Architecture

Figure 4 depicts how the three components combine to form a whole system. At each iteration, the Weak Topic Detection module learns a user’s weak topics from existing records. The Topic Relatedness Modeling module updates the knowledge map reflecting the new performance data. The Scheduling Engine module selects and ranks the weak topics and uses the ranked topics to choose unattempted exercises for the learner.

Please note that after learners completed a learning session, we stored new learning outcomes in the repository so that they could be considered when choosing materials for the next learning session. For example, because topic weakness rankings may change, newly mastered topics can be removed and the knowledge map may be adjusted as the estimations of dependencies change. Figure C1 in Appendix C provides an example of how topic weakness evolved across multiple learning sessions.

## Experimental Evaluation

After designing related-interleaving for e-learning platforms, the next step was to evaluate our design against the benchmarks. We start by formulating testable hypotheses for our experimental evaluation and then describe the study context and experiment design.

## Testable Hypotheses

We used a field experiment to test two hypotheses derived from our design goals. Based on our theory-driven design discussed earlier, compared with unrelated-interleaving, related-interleaving mitigates the overload risk and expands schema-building opportunities, thereby leading to improved learning. In addition, our previous discussion indicates that the relative advantage of interleaving versus non-interleaving primarily hinges upon whether learners are overloaded in interleaved learning. We thus propose that since relatedinterleaving possesses the strength of interleaving in schema building while reducing learners’ cognitive load, it is also likely to outperform non-interleaving. Thus, we hypothesize:

H1: Compared with unrelated-interleaving, relatedinterleaving leads to better learning performance.

H2: Compared with non-interleaved learning, relatedinterleaving leads to better learning performance.

While our main focus was on the advantage of the relatedinterleaving design, we were also interested in testing the heterogeneous effects of related-interleaving across learner types, which is useful for guiding future designs. CLT suggests that individuals differ in cognitive capacities and the amount of schemas they can leverage to lessen their cognitive load (Sweller et al., 2019). As a result, weak learners who have not built strong schemas from their past learning may face greater overload risk under interleaving than strong learners. For weak learners, unrelated-interleaving may leave few cognitive resources for schema building and prevent them from realizing the schema-building enhancement benefit, leading to suboptimal performance. Increasing topic relatedness in interleaving is thus beneficial for weak learners because it mitigates the overload risk and leaves more resources for schema building (Rau et al., 2010). Strong learners, however, with large cognitive capacities and more existing schemas to rely on, are less resource constrained and may thus not benefit as much from the reduced cognitive load of increasing topic relatedness.

Furthermore, weak learners also stand to benefit more from the increased schema-building opportunities in relatedinterleaving. This is because weak learners are generally less capable of information abstraction and connection building than strong learners. Juxtaposing related topics in the same session thus facilitates weak learners’ information connection and induction to a greater extent (Lambiotte & Dansereau, 1992; Nesbit & Adesope, 2006). Hence, we expect that in the interleaving design, increasing topic relatedness will be more beneficial for weak learners than for strong learners.

![](/api/attachments/ZDGP6YXC/fulltext/images/046687662d8462279e0f6b8f07a99dfad5b874152cce090cf6c41a5b8d6efa4d.jpg)  
Figure 4. A System Architecture for Related-Interleaving

## Study Context and System Instantiation

To evaluate the effectiveness of our proposed relatedinterleaving session design, we collaborated with a middle school in China to supplement a mandatory English course. During summer and winter breaks, English teachers at this school assign learners English reading exercises. Each exercise consists of one article and three to five multiplechoice questions for assessing learners’ comprehension. Traditionally, teachers distribute booklets that contain the same exercises for all learners. Using a third-party developer, we developed an e-learning system to replace the booklets. The system works as follows: The system assigns two exercises to each learner at the beginning of every learning session, each consisting of two consecutive days. Exercises that are not completed within the learning session will expire. After a learner submits their answers to each exercise online, the system provides immediate feedback, including displaying the correct answers, the learning topics covered, and explanations of why an answer is correct. We explain the system details in Appendix D.

There are about 200 exercises in our system database. Each question in an exercise is designed to cover one of the 14 topics designated by the education bureau for English reading. These topics are related to specific skills in reading comprehension, such as “making inferences,” “event sorting,” “summarizing the main idea,” and “retrieving relevant information.” The exercises, along with the assessment questions, are designed to reinforce and evaluate a learner’s mastery of these core topics. Experienced English teachers from leading middle schools in the region coded the topic covered by each assessment question. Some exercises had all questions covering the same topic, whereas other exercises had questions covering different topics. We leveraged such natural variations and implemented different learning session designs by choosing exercises with a desirable number of topics and a level of topic relatedness, as shown in the section on the design of the scheduling engine.

## Experiment Design and Procedure

We conducted a field experiment during the summer break from July 13 to August 31, 2017. We adopted a betweensubject design with three conditions: non-interleaving, unrelated-interleaving, and related-interleaving. Our participants included 510 eighth-grade learners from 17 different classes in the middle school, taught by nine different English teachers. We did not inform learners of their assigned conditions upfront nor did we inform the teachers. Because the system interface was identical for the three groups, it was unlikely that the learners could have inferred their assignment group. Learners from the same class were randomly assigned to the three groups with equal probability so that any teacher effect would be canceled in cross-group comparisons. After the experiment, we debriefed the learners and teachers who participated in the experiment.

![](/api/attachments/ZDGP6YXC/fulltext/images/f118b826816c28ed9fc92535c9c2315f385d68202b835013a2d9ed5c3e9ec4a1.jpg)  
Note: HMM = Hidden Markov Model; KM = Knowledge Map. ○1 , ○2 and ○3 indicate the three treatment groups.  
Figure 5. Experimental Procedure

The experimental procedure is depicted in Figure 5. Before the experiment, we collected the learners’ demographic information and their final exam scores in English, taken about one week before the experiment. These scores were later used to classify learners into weak and strong learners. Next, we randomly assigned the learners to the three groups with equal probability. The learners stayed in the same group throughout the experiment. We then conducted an online pretest that included several exercises to control for the learners’ reading comprehension skills before the experiment.

The experiment included 26 learning sessions. Before each session, the HMM automatically recalculated each learner’s topic mastery based on up-to-date learning records. The system also updated the knowledge map based on pooled performance data. The system then selected personalized exercises for the learning session based on the learner’s treatment group. After the experiment, we conducted a posttest of reading comprehension to evaluate the learners’ performance.

## Results and Analysis

Among the 510 learners invited to use the system, 435 voluntarily participated and finished at least one exercise during the experiment. The three groups (non-interleaving, unrelated-interleaving, and related-interleaving) were roughly equal in size, with 140, 149, and 146 participants, respectively. Among the participants, 381 took the posttest, and 337 took the pretest. Our analyses focused on learners who took both the posttest and the pretest. We classified learners into weak and strong based on their English final exam scores before the experiment. Specifically, we defined those whose scores were above the class median as strong learners and the remaining as weak learners. We use the Posttest score (based on a 100-point scale) as our main measure of learning performance.

In Appendix E, we report a series of randomization and manipulation checks. The randomization check suggests no significant differences in terms of pre-experiment exam scores, pretest scores, and gender distributions across groups. Our manipulation check confirmed that our intervention was valid. Specifically, we found that the noninterleaving design covered 1.16 topics per exercise on average, whereas the two interleaving designs covered 3.40 topics per exercise on average. In addition, the relatedinterleaving design had 2.29 topic dependencies per exercise on average, which is a significant increase from 0.47 under the unrelated-interleaving design.

We report the summary statistics in Table 2. Among the participants, 46% were female. The learners spent 159.47 minutes in the system, on average, during the entire experiment period and each exercise took approximately 5.04 minutes to finish. The learners completed 31.65 exercises out of the 54 assigned, on average, for a 61% completion rate. The average accuracy among the completed exercises was 65%.

<table><tr><td colspan="7">Table 2. Summary Statistics</td></tr><tr><td>Variables</td><td>Description</td><td>N</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>Interleaving</td><td>=1 if the learner was randomly assigned to the unrelated-interleaving or related-interleaving group</td><td>435</td><td>0.68</td><td>0.47</td><td>0</td><td>1</td></tr><tr><td>Relatedness</td><td>=1 if the learner was randomly assigned to the related-interleaving group</td><td>435</td><td>0.34</td><td>0.47</td><td>0</td><td>1</td></tr><tr><td>Female</td><td>=1 if learner was female</td><td>435</td><td>0.46</td><td>0.50</td><td>0</td><td>1</td></tr><tr><td>FinalScore</td><td>English final exam score before the experiment</td><td>427</td><td>81.39</td><td>13.12</td><td>23.33</td><td>98.75</td></tr><tr><td>StrongLearner</td><td>=1 if learner&#x27;s pre-experiment final exam score was above the class median</td><td>427</td><td>0.51</td><td>0.50</td><td>0</td><td>1</td></tr><tr><td>Pretest</td><td>Online pretest score before the experiment</td><td>337</td><td>64.77</td><td>24.91</td><td>0</td><td>100</td></tr><tr><td>Posttest</td><td>Online posttest score after the experiment</td><td>381</td><td>69.22</td><td>28.29</td><td>0</td><td>100</td></tr></table>

## Model-Free Evidence

We first conducted a model-free analysis by comparing the posttest scores across the three groups (Figure 6). Overall, related-interleaving led to an 8.28-point increase in posttest scores compared with non-interleaving $( p = 0 . 0 2 1 )$ and a 10.90-point increase compared with unrelated-interleaving $( p < 0 . 0 0 1 )$ . Unrelated-interleaving resulted in a 2.82-point decrease compared with non-interleaving, though the effect was insignificant $( p = 0 . 4 5 9 )$

We found a similar pattern among weak learners. Relatedinterleaving enabled them to gain 7.40 points relative to noninterleaving $( p ~ = ~ 0 . 2 0 0 )$ and 15.88 points relative to unrelated-interleaving $( p = 0 . 0 0 2 )$ . Unrelated-interleaving led to an 8.47-point drop compared with non-interleaving, though the effect was insignificant $( p = 0 . 1 4 )$ . The effects among strong learners were different: related-interleaving led to a significant 10.58-point increase compared with noninterleaving $( p = 0 . 0 1 7 )$ and a less prominent 6.03-point increase compared with unrelated-interleaving (p = 0.179). For stronger learners, unrelated-interleaving did not differ from non-interleaving (β = 4.55, p = 0.291).

## Effect of Related-Interleaving on Posttest Scores

To test the effect of related-interleaving on learning performance, we modeled the learning performance of a learner ?? as follows:

$$
\begin{array}{r l} & P o s t t e s t _ {i} = \alpha + \beta_ {1} I n t e r l e a v i n g _ {i} + \beta_ {2} I n t e r l e a v i n g _ {i} \times \\ & R e l a t e d n e s s _ {i} + \pmb {x} _ {i} + \pmb {\omega} _ {i} + \epsilon_ {i}, \end{array}
$$

where $P o s t t e s t _ { i }$ represents the posttest performance of learner ?? and vector $x _ { i }$ denotes learner characteristics including the pre-experiment final exam score (FinalScore), the pretest score (Pretest), and gender (Female). Vector ${ \pmb { \omega } } _ { i }$ is a class-fixed effect. $\epsilon _ { i }$ denotes the idiosyncratic variation in learning performance.

Based on the regression results (see Table 3, Column 1), Relatedness significantly moderated the effect of Interleaving. To aid understanding, we compare related-interleaving with two other conditions in Figure 7. Compared with unrelatedinterleaving, learners in the related-interleaving group scored 10.05 points higher $( p ~ = ~ 0 . 0 0 2 )$ . Compared with noninterleaving, related-interleaving led to a 7.08-point increase (p = 0.038)<sup>6</sup>. We thus found support for hypotheses H1 and H2. Overall, we found that related-interleaving significantly increased learning performance.

We also compared the posttest performance between noninterleaving and unrelated-interleaving and found no significant difference (?? = -2.97, p = 0.374). This indicates that the traditional unrelated-interleaving design did not yield better learning performance than the non-interleaving design.

To further examine whether related-interleaving increased the amount of schema building as predicted by CLT, we also compared the three groups based on two indirect measures of schema-building loads as suggested by prior literature; namely, a learner’s topic mastery and practice accuracy after each learning session (Brunken et al., 2003; Orru & Longo, 2019). As shown in Appendix F, related-interleaving led to increased topic mastery and practice accuracy in each learning session than unrelated-interleaving and non-interleaving, supporting our theoretical predictions.

![](/api/attachments/ZDGP6YXC/fulltext/images/d68bd7a673a9337da31aede30ff0484ec6e0f2ba115e616f1cc3294c9cd3a75d.jpg)  
Figure 6. Model-Free Evidence

<table><tr><td colspan="3">Table 3. Effect of Interleaving and Topic Relatedness</td></tr><tr><td rowspan="2"></td><td>Posttest</td><td>Posttest</td></tr><tr><td>(1)</td><td>(2)</td></tr><tr><td>Interleaving</td><td>-2.97(3.33)</td><td>-19.86***(5.38)</td></tr><tr><td>Interleaving×Relatedness</td><td>10.05**(3.21)</td><td>18.81***(4.48)</td></tr><tr><td>Interleaving×StrongLearner</td><td></td><td>25.18***(6.98)</td></tr><tr><td>Interleaving×Relatedness×StrongLearner</td><td></td><td>-15.86*(6.56)</td></tr><tr><td>StrongLearner</td><td></td><td>-7.13(5.35)</td></tr><tr><td>FinalScore</td><td>0.83***(0.16)</td><td></td></tr><tr><td>Pretest</td><td>0.30***(0.06)</td><td>0.36***(0.06)</td></tr><tr><td>Female</td><td>6.10*(2.78)</td><td>6.84*(2.82)</td></tr><tr><td>Constant</td><td>-18.81(16.22)</td><td>58.46***(7.48)</td></tr><tr><td>Class fixed effect</td><td>YES</td><td>YES</td></tr><tr><td>N</td><td>306</td><td>306</td></tr><tr><td> $R^2$ </td><td>0.359</td><td>0.343</td></tr></table>

Note: Interleaving represents the effect of unrelated-interleaving relative to non-interleaving. Relatedness is meaningful only in the interleaving condition (i.e., coded as 0 for both unrelated-interleaving and non-interleaving conditions). Therefore, Interleaving × Relatedness is equivalent to Relatedness and captures the effect of related-interleaving relative to unrelated-interleaving. $^ { \star } p < 0 . 0 5 , ^ { \star \star } p < 0 . 0 1 , ^ { \star \star \star } p < 0 . 0 0 1$ . Standard errors are in parentheses.

![](/api/attachments/ZDGP6YXC/fulltext/images/e41e5f6de353458051dd504c6f89860aa749aebd2ba394a2fd031458438d071c.jpg)  
Note: The dots represent mean values. The error bars represent the 95% confidence intervals.  
Figure 7. Posttest Comparison among Three Experimental Conditions

![](/api/attachments/ZDGP6YXC/fulltext/images/44792e9f92cc0daff62f37fb5301af47070b49609e37c797a8ed20385cf8795c.jpg)  
Note: Dots represent the mean values. Error bars represent the 95% confidence intervals.  
Figure 8. Heterogeneous Effect of Topic Relatedness on Posttest Score

## Effect of Related-Interleaving by Learner Type

We further explored the heterogeneous effects of relatedinterleaving across different learners. To understand how the benefit of related-interleaving differs by learner type, we added a three-way interaction term between interleaved learning (Interleaving), topic relatedness (Relatedness), and learner type (StrongLearner).<sup>7</sup>

$$
\begin{array}{r l} P o s t t e s t _ {i} = \alpha + \beta_ {1} I n t e r l e a v i n g _ {i} & \\ & + \beta_ {2} I n t e r l e a v i n g _ {i} \times R e l a t e d n e s s _ {i} \\ & + \beta_ {3} I n t e r l e a v i n g _ {i} \times S t r o n g L e a r n e r _ {i} \\ & + \beta_ {4} I n t e r l e a v i n g _ {i} \times R e l a t e d n e s s _ {i} \\ & \times S t r o n g L e a r n e r _ {i} + \boldsymbol {x} _ {i} + \boldsymbol {\omega} _ {i} + \epsilon_ {i}. \end{array}
$$

The results in Table 3 Column 2 show a significantly negative three-way interaction, which confirms that increasing topic relatedness benefited weak learners more than strong learners. To aid understanding, we plotted the findings in Figure 8, which show that weak learners (solid line) achieved significantly better performance (an 18.81-point increase) with related-interleaving than with unrelated-interleaving. In contrast, the improvement brought by related-interleaving for strong learners (dashed line) was not significant (?? = 2.94, p = 0.538). Increasing topic relatedness also significantly reduced the performance gap between strong and weak learners from 18.04 points (with unrelated-interleaving) to 2.18 points (with related-interleaving). Appendix G shows that our heterogeneous analyses were not sensitive to the division between strong and weak learners.

Another notable finding is that a significant positive interaction exists between interleaved learning (Interleaving)

and learner type (StrongLearner) (Table 3, column 2). This indicates that traditional unrelated-interleaving (relative to non-interleaving) benefits strong learners (a 5.31-point increase in posttest scores) but hurts weak learners (a 19.86- point drop). This is consistent with the CLT framework that suggests that interleaving may significantly increase cognitive overload risks among weak learners (who have not built strong schemas previously), dampening their learning performance. For strong learners, interleaving is less likely to lead to cognitive overload because they have more existing schemas to rely on. Overall, these findings support the CLT perspective that when learners’ cognitive resources are strained (as in the case of weak learners), unrelatedinterleaving can hurt learning performance, highlighting the importance of topic relatedness.

## Discussion

## Contributions to the Literature

This study contributes to the literature in four ways. First, following the design science paradigm, we contribute to the elearning literature by developing and testing a theorygrounded interleaving design—related-interleaving. Our related-interleaving design incorporates (1) the dynamic detection of learners’ weak topics at each moment using a hidden Markov chain, (2) a knowledge-map-based representation for capturing topic dependencies and a fuzzy association rule algorithm for data-driven augmentation of the knowledge map, and (3) a scheduling engine that assembles a set of exercises that meet the requirements of relatedinterleaving, personalization, and adaptation. Based on a field experiment, we showcase how one can harness the power of machine learning in data-rich e-learning environments to make learning session design more adaptive and effective.

Second, more broadly, we extend the stream of IS research on structuring e-learning activities (Alavi & Leidner, 2001; Gupta & Bostrom, 2013; Gupta & Bostrom, 2009; Piccoli et al., 2001) by examining topic design in a learning session. Prior studies have mainly focused on weak topic detection and how to optimize the design across multiple learning sessions. We go further in showing the importance of choosing multiple weak topics to practice in one learning session. We believe that this new design, related-interleaving, can generate meaningful implications in other e-learning design elements, such as multimedia design and instructional strategies.

Third, our work contributes to the literature on interleaving. Existing literature has shown mixed evidence in terms of the interleaving effect, but there is very limited theorization about the potential downsides of interleaving. Additionally, there limited attention has been paid to how to design interleaving effectively. This study uses CLT as a theoretical framework to explain the benefits and risks of interleaving and to motivate a new related-interleaving design that mitigates the risk of cognitive overload while maintaining schema-building opportunities. Our findings confirm two novel predictions of the theory: the benefit of related-interleaving and the differential effects of interleaving across learner types. The contingency factors identified in this study—topic relatedness and learner type (i.e., strong and weak learners)—may help explain the mixed findings about interleaving in the literature. Moreover, our CLT-based framework could serve as a theoretical foundation for new interleaving research and designs. For instance, researchers could use it to investigate the optimal spacing of interleaved topics and the role of complexity level of exercises in interleaved designs.

Lastly, this study contributes to the existing CLT literature by adding that topic design in a learning session also holds important implications for cognitive load and learning performance. Prior research has used CLT to guide various aspects of instructional design, such as information presentation formats, the use of worked examples, and the modality of instructions. This research shows that CLT can also guide interleaving designs, both in terms of the number of topics in a learning session and the relationship between these topics. Building on the tenets of CLT, our research suggests a nuanced relationship between interleaving and learning performance: increasing the number of topics in a session (i.e., interleaving) can elevate cognitive load and potentially hinder learning, particularly among weak learners; however, when the topics included in the same session are more related, the risk of overload is reduced, allowing learners, especially weak learners, to benefit more from schema-building opportunities brought by interleaving and thus obtain better learning performance. Overall, our work extends the domain of CLT by revealing a complex relationship between interleaving designs, individual differences, cognitive load, and learning performance.

## Implications for Practice

Our findings have several actionable implications for practice. First, we highlight an overlooked issue in e-learning session design and offer a few alternatives—non-interleaving, unrelated-interleaving, and related-interleaving session designs. As more e-learning platforms begin to offer personalized learning materials for learners, this issue will become increasingly relevant. Second, our findings suggest that e-learning platforms should not blindly mix topics in an interleaved learning session; ensuring topic relatedness is a great way of enhancing the benefits of interleaved learning while mitigating overload risks. Third, our findings suggest that e-learning platforms should consider learners’ capacities when designing learning sessions. Interleaving generally benefits strong learners, and our proposed related-interleaving is likely the best design for strong learners. For weak learners, both related-interleaving and traditional non-interleaving designs are suitable, but unrelated-interleaving design (i.e., interleaving without enforcing topic relatedness) should be avoided. Finally, we provide several tools, such as a hidden Markov chain and a knowledge map, that can be directly appropriated by practitioners to support personalized, adaptive, and data-driven designs, such as relatedinterleaving. We hope that our work will inspire more elearning practitioners to incorporate data-driven decisions and machine intelligence into their learning designs.

## Limitations and Future Research

Our study has several limitations that could be addressed in future research. First, our findings are based on a field experiment on a specific subject (English) and population. The research could benefit from replications in other subject domains and learner populations. Second, our field experiment lasted only two months and thus may not capture long-term effects. Third, we used certain heuristics in our implementation of related-interleaving that could be further optimized. Future research might experiment with a different number of interleaved topics and different ways of choosing among weak topics. For example, for strong learners, given that handling three related topics with the highest weakness rankings worked well in our study, future studies could consider increasing the number of related topics to fully tap the potential of strong learners. However, for weak learners, our findings show that, although mixing three related topics may mitigate the downside of unrelated-interleaving, it is no better than non-interleaving. Hence, mixing fewer related topics or choosing topics with a lower weakness ranking may further lessen cognitive load and potentially benefit weak learners more. Existing CLT-based design principles could also be utilized to reduce cognitive load for weaker learners. Strategies like offering worked examples, partial solutions, and integrating multimodal information could be leveraged to further assist weak learners in gaining the full benefits of related-interleaving. In addition, future research could further explore different implementations of topic relatedness (e.g., ones focusing on topic similarity) and examine whether optimal implementations depend on specific contexts (e.g., different subject domains and learning conditions). Fourth, given our findings on how the effects of different interleaving designs differ across weak and strong learners, future research could explore how the design of interleaving should be adapted dynamically as learners gain proficiency. Finally, although our findings support CLT predictions, we were unable to directly test the theory in our field experiment. Further tests of theoretical mechanisms may be a good subject for future research.

## Acknowledgments

We thank the senior editor, the associate editor, and the three anonymous reviewers, whose constructive feedback enhanced the development of the paper. Author names are listed alphabetically. The corresponding authors are Andy Tao Li (andytaoli@ustc.edu.cn) and Cheng Yi (yich@sem.tsinghua.edu.cn). Andy Tao Li acknowledges support from the National Natural Science Foundation of China (Grant 72301269, Grant 72332007, and Grant 71921001) and the Fundamental Research Funds for the Central Universities (#WK2040000085). Sean Xin Xu acknowledges support from the National Natural Science Foundation of China (Grant 72421001) and from the MOE Project of Key Research Institute of Humanities and Social Sciences at Universities (#22JJD630012). Cheng Yi acknowledges support from the National Natural Science Foundation of China (Grant 72022008).

## References

Abbasi, A., & Chen, H. (2008). CyberGate: A design framework and system for text analysis of computer-mediated communication. MIS Quarterly, 32(4), 811-837. https://doi.org/10.2307/25148873

Abdelrahman, G., Wang, Q., & Nunes, B. (2023). Knowledge tracing: A survey. ACM Computing Surveys, 55(11), Article 224. https://doi.org/10.1145/3569576

Al-Muhaideb, S., & Menai, M. E. B. (2011). Evolutionary computation approaches to the curriculum sequencing problem. Natural Computing, 10(2), 891-920. https://doi.org/10.1007/s11047-010- 9246-5

Alavi, M., & Leidner, D. E. (2001). Research commentary: Technology-mediated learning: A call for greater depth and breadth of research. Information Systems Research, 12(1), 1-10. https://doi.org/10.1287/isre.12.1.1.9720

Atapattu, T., Falkner, K., & Falkner, N. (2017). A comprehensive text analysis of lecture slides to generate concept maps. Computers & Education, 115(1), 96-113. https://doi.org/10.1016/j.compedu. 2017.08.001

Ausubel, D. P., Novak, J. D., & Hanesian, H. 1968. Educational psychology: A cognitive view. Holt, Rinehart & Winston.

Ayabakan, S., Bardhan, I., & Zheng, E. (2016). What drives patient readmissions? A new perspective from the hidden markov model analysis. In Proceedings of the 37th International Conference on Information Systems.

Balaid, A., Abd Rozan, M. Z., Hikmi, S. N., & Memon, J. (2016). Knowledge maps: A systematic literature review and directions for future research. International Journal of Information Management, 36(3), 451-475. https://doi.org/10.1016/j.ijinfomgt. 2016.02.005

Bauman, K., & Tuzhilin, A. (2018). Recommending remedial learning materials to students by filling their knowledge gaps. MIS Quarterly, 42(1), 313-332. https://doi.org/10.25300/MISQ/2018/13770

Bettinger, E. P., Fox, L., Loeb, S., & Taylor, E. S. (2017). Virtual classrooms: How online college courses affect student success. American Economic Review, 107(9), 2855-2875. https://doi.org/ 10.1257/aer.20151193

Birnbaum, M. S., Kornell, N., Bjork, E. L., & Bjork, R. A. (2013). Why interleaving enhances inductive learning: The roles of discrimination and retrieval. Memory & Cognition, 41(3), 392-402. https://doi.org/10.3758/s13421-012-0272-7

Brunken, R., Plass, J. L., & Leutner, D. (2003). Direct measurement of cognitive load in multimedia learning. Educational Psychologist, 38(1), 53-61. https://doi.org/10.1207/S15326985EP3801\_7

Carvalho, P. F., & Goldstone, R. L. (2014). Putting category learning in order: Category structure and temporal arrangement affect the benefit of interleaved over blocked study. Memory & Cognition, 42(3), 481-495. https://doi.org/10.3758/s13421-013-0371-0

Chen, C. M. (2008). Intelligent web-based learning system with personalized learning path guidance. Computers & Education, 51(2), 787-814. https://doi.org/10.1016/j.compedu.2007.08.004

Chen, G., & Wei, Q. (2002). Fuzzy association rules and the extended mining algorithms. Information Sciences, 147(1), 201-228. https://doi.org/10.1016/S0020-0255(02)00264-5

Chen, Y., Li, X., Liu, J., & Ying, Z. (2018). Recommendation system for adaptive learning. Applied Psychological Measurement, 42(1), 24-41. https://doi.org/10.1177/0146621617697959

Conrad, C., Deng, Q., Caron, I., Shkurska, O., Skerrett, P., & Sundararajan, B. (2022). How student perceptions about online learning difficulty influenced their satisfaction during Canada's Covid-19 response. British Journal of Educational Technology, 53(3), 534-557. https://doi.org/10.1111/bjet.13206

Damgaard, M. T., & Nielsen, H. S. (2018). Nudging in education. Economics of Education Review, 64, 313-342. https://doi.org/ 10.1016/j.econedurev.2018.03.008

Delgado, P., & Salmerón, L. (2021). The inattentive on-screen reading: Reading medium affects attention and reading comprehension under time pressure. Learning and Instruction, 71, Article 101396. https://doi.org/10.1016/j.learninstruc.2020.101396

Dennen, V. P., Aubteen Darabi, A., & Smith, L. J. (2007). Instructorlearner interaction in online courses: The relative perceived

importance of particular instructor actions on performance and satisfaction. Distance Education, 28(1), 65-79. https://doi.org/ 10.1080/01587910701305319

Dontre, A. J. (2021). The influence of technology on academic distraction: A review. Human Behavior and Emerging Technologies, 3(3), 379-390. https://doi.org/10.1002/hbe2.229

Figlio, D., Rush, M., & Yin, L. (2013). Is it live or is it internet? Experimental estimates of the effects of online instruction on student learning. Journal of Labor Economics, 31(4), 763-784. https://doi.org/10.1086/669930

Firth, J., Rivers, I., & Boyle, J. (2021). A systematic review of interleaving as a concept learning strategy. Review of Education, 9(2), 642-684. https://doi.org/10.1002/rev3.3266

Foster, N. L., Mueller, M. L., Was, C., Rawson, K. A., & Dunlosky, J. (2019). Why does interleaving improve math learning? The contributions of discriminative contrast and distributed practice. Memory & Cognition, 47(6), 1088-1101. https://doi.org/10.3758/ s13421-019-00918-4

Furenes, M. I., Kucirkova, N., & Bus, A. G. (2021). A comparison of children’s reading on paper versus screen: A meta-analysis. Review of Educational Research, 91(4), 483-517. https://doi.org/10.3102 0034654321998074

Ginns, P. (2005). Meta-analysis of the modality effect. Learning and Instruction, 15(4), 313-331. https://doi.org/10.1016/j.learninstruc. 2005.07.001

Goudeau, S., Sanrey, C., Stanczak, A., Manstead, A., & Darnon, C. (2021). Why lockdown and distance learning during the COVID-19 pandemic are likely to increase the social class achievement gap. Nature Human Behaviour, 5(10), 1273-1281. https://doi.org/ 10.1038/s41562-021-01212-7

Gupta, S., & Bostrom, R. (2013). Research note: An investigation of the appropriation of technology-mediated training methods incorporating enactive and collaborative learning. Information Systems Research, 24(2), 454-469. https://doi.org/10.1287/isre. 1120.0433

Gupta, S., & Bostrom, R. P. (2009). Technology-mediated learning: A comprehensive theoretical model. Journal of the Association for Information Systems, 10(9), 686-714. https://doi.org/10.17705/ 1jais.00207

Hansen, J. D., & Reich, J. (2015). Democratizing education? Examining access and usage patterns in massive open online courses. Science, 350(6265), 1245-1248. https://doi.org/10.1126/ science.aab3782

Hausman, H., & Kornell, N. (2014). Mixing topics while studying does not enhance learning. Journal of Applied Research in Memory and Cognition, 3(3), 153-160. https://doi.org/10.1016/j.jarmac.2014. 03.003

Huang, N., Wang, L., Hong, Y., Lin, L., Guo, X., & Chen, G. (in press). When the clock strikes: A multimethod investigation of on-thehour effects in online learning. Information Systems Research. https://doi.org/10.1287/isre.2023.1234

Huang, N., Zhang, J., Burtch, G., Li, X., & Chen, P. (2021). Combating procrastination on MOOCs via optimal calls-to-action: Evidence from a field experiment. Information Systems Research, 32(2), 301-317. https://doi.org/10.1287/isre.2020.0974

Hussain, M., Zhu, W., Zhang, W., Abidi, S. M. R., & Ali, S. (2019). Using machine learning to predict student difficulties from learning session data. Artificial Intelligence Review, 52(1), 381- 407. https://doi.org/10.1007/s10462-018-9620-8

Jaeger, A. J., Taylor, A. R., & Wiley, J. (2016). When, and for whom, analogies help: The role of spatial skills and interleaved presentation. Journal of Educational Psychology, 108(8), 1121- 1139. https://doi.org/10.1037/edu0000121

Jeng, Y.-L., & Huang, Y.-M. (2019). Dynamic learning paths framework based on collective intelligence from learners. Computers in Human Behavior, 100, 242-251. https://doi.org/ 10.1016/j.chb.2018.09.012

Jiang, B., Li, X., Yang, S., Kong, Y., Cheng, W., Hao, C., & Lin, Q. (2022). Data-driven personalized learning path planning based on cognitive diagnostic assessments in MOOCs. Applied Sciences, 12(8), 3982. https://doi.org/10.3390/app12083982

Kalyuga, S. (2007). Enhancing instructional efficiency of interactive elearning environments: A cognitive load perspective. Educational Psychology Review, 19(3), 387-399. https://doi.org/10.1007/ s10648-007-9051-6

Khan, A., Egbue, O., Palkie, B., & Madden, J. (2017). Active learning: Engaging students to maximize learning in an online course. Electronic Journal of E-learning, 15(2), 107‑115. https://academic-publishing.org/index.php/ejel/article/view/1824

Kim, N. J., Belland, B. R., Lefler, M., &reasen, L., Walker, A., & Axelrod, D. (2020). Computer-based scaffolding targeting individual versus groups in problem-centered instruction for STEM education: Meta-analysis. Educational Psychology Review, 32(2), 415-461. https://doi.org/10.1007/s10648-019-09502-3

Kim, Y., & Krishnan, R. (2019). The dynamics of online consumers’ response to price promotion. Information Systems Research, 30(1), 175-190. https://doi.org/10.1287/isre.2018.0793

Kizilcec, R. F., Saltarelli, A. J., Reich, J., & Cohen, G. L. (2017). Closing global achievement gaps in MOOCs. Science, 355(6322), 251-252. https://doi.org/10.1126/science.aag2063

Klašnja-Milićević, A., Vesin, B., Ivanović, M., & Budimac, Z. (2011). E-learning personalization based on hybrid recommendation strategy and learning style identification. Computers & Education, 56(3), 885-899. https://doi.org/10.1016/j.compedu.2010.11.001

Kleider, H. M., Pezdek, K., Goldinger, S. D., & Kirk, A. (2008). Schema‐driven source misattribution errors: remembering the expected from a witnessed event. Applied Cognitive Psychology, 22(1), 1-20. https://doi.org/10.1002/acp.1361

Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the 'enemy of induction'? Psychological Science, 19(6), 585-592. https://doi.org/10.1111/j.1467-9280.2008.02127.x

Kulkarni, C., Cambre, J., Kotturi, Y., Bernstein, M. S., & Klemmer, S. R. (2015). Talkabout: Making distance matter with small groups in massive classes. In Proceedings of the 18th ACM Conference on Computer Supported Cooperative Work & Social Computing. https://doi.org/10.1145/2675133.2675166

Kurilovas, E., Zilinskiene, I., & Dagiene, V. (2015). Recommending suitable learning paths according to learners’ preferences: Experimental research results. Computers in Human Behavior, 51, 945-951. https://doi.org/10.1016/j.chb.2014.10.027

Lambiotte, J. G., & Dansereau, D. F. (1992). Effects of knowledge maps and prior knowledge on recall of science lecture content. The Journal of Experimental Education, 60(3), 189-201. https://doi.org/10.1080/00220973.1992.9943875

Lee, J. H., & Segev, A. (2012). Knowledge maps for e-learning. Computers & Education, 59(2), 353-364. https://doi.org/ 10.1016/j.compedu.2012.01.017

Leung, A. C. M., Santhanam, R., Kwok, R. C.-W., & Yue, W. T. (2023). Could gamification designs enhance online learning

through personalization? Lessons from a field experiment. Information Systems Research, 34(1), 27-49. https://doi.org/ 10.1287/isre.2022.1123

Likourezos, V., Kalyuga, S., & Sweller, J. (2019). The variability effect: When instructional variability is advantageous. Educational Psychology Review, 31(2), 479-497. https://doi.org/10.1007 s10648-019-09462-8

Loghin, G. C., Carron, T., Marty, J. C., & Vaida, M. (2008). Observation and adaptation of a learning session based on a multiagent system: An experiment. In Proceedings of the 4th International Conference on Intelligent Computer Communication and Processing. https://doi.org/10.1109/ICCP.2008.4648349

Manasrah, A., Masoud, M., & Jaradat, Y. (2021). Short videos, or long videos? A study on the ideal video length in online learning. In Proceedings of International Conference on Information Technology. https://doi.org/10.1109/ICIT52682.2021.9491115

Martin, S. (2014). Measuring cognitive load and cognition: metrics for technology-enhanced learning. Educational Research and Evaluation, 20(7-8), 592-621. https://doi.org/10.1080/13803611. 2014.997140

Mayer, R. E., & Moreno, R. (2003). Nine ways to reduce cognitive load in multimedia learning. Educational Psychologist, 38(1), 43-52. https://doi.org/10.1207/S15326985EP3801\_6

Mielicki, M. K., & Wiley, J. (2022). Exploring the necessary conditions for observing interleaved practice benefits in math learning. Learning and Instruction, 80, Article 101583. https://doi.org/10.1016/j.learninstruc.2022.101583

Nesbit, J. C., & Adesope, O. O. (2006). Learning with concept and knowledge maps: A meta-analysis. Review of Educational Research, 76(3), 413-448. https://doi.org/10.3102/003465430760 03413

O'donnell, A. M., Dansereau, D. F., & Hall, R. H. (2002). Knowledge maps as scaffolds for cognitive processing. Educational Psychology Review, 14(1), 71-86. https://doi.org/10.1023/ A:1013132527007

Orru, G., & Longo, L. (2019). The evolution of cognitive load theory and the measurement of its intrinsic, extraneous and germane Loads: A review. In L. Longo & M. C. Leva (Eds.), Human Mental workload: Models and applications (pp. 23-48). Springer. https://doi.org/10.1007/978-3-030-14273-5\_3

Pardos, Z., Bergner, Y., Seaton, D., & Pritchard, D. (2013). Adapting Bayesian knowledge tracing to a massive open online course in edX. In Proceedings of the 6th International Conference on Educational Data Mining, Memphis, TN.

Park, O.-c., & Lee, J. (2008). Adaptive instructional systems. In M. J. Spector, M. D. Merrill, J. van Merrienboer, & M. P. Driscoll (Eds.), Handbook of research on educational communications and technology (pp. 469-484). Lawrence Erlbaum Associates.

Pelánek, R. (2017). Bayesian knowledge tracing, logistic models, and beyond: An overview of learner modeling techniques. User Modeling and User-Adapted Interaction, 27(3), 313-350. https://doi.org/10.1007/s11257-017-9193-2

Piccoli, G., Ahmad, R., & Ives, B. (2001). Web-based virtual learning environments: A research framework and a preliminary assessment of effectiveness in basic IT skills training. MIS Quarterly, 25(4), 401-426. https://doi.org/10.2307/3250989

Rau, M. A., Aleven, V., & Rummel, N. (2010). Blocked versus interleaved practice with multiple representations in an intelligent tutoring system for fractions. In Proceedings of the 10th

International Conference on Intelligent Tutoring Systems. https://doi.org/10.1007/978-3-642-13388-6\_45

Reddy, S., Labutov, I., & Joachims, T. (2016). Learning student and content embeddings for personalized lesson sequence recommendation. In Proceedings of the 3rd ACM Conference on Learning. https://doi.org/10.1145/2876034.2893375

Reich, J., & Ruipérez-Valiente, J. A. (2019). The MOOC pivot. Science, 363(6423), 130-131. https://doi.org/10.1126/science.aav7958

Renkl, A. (2014). Toward an instructionally oriented theory of example-based learning. Cognitive science, 38(1), 1-37. https://doi.org/10.1111/cogs.12086

Rohrer, D. (2012). Interleaving helps students distinguish among similar concepts. Educational Psychology Review, 24(3), 355-367. https://doi.org/10.1007/s10648-012-9201-3

Rohrer, D., Dedrick, R. F., & Burgess, K. (2014). The benefit of interleaved mathematics practice is not limited to superficially similar kinds of problems. Psychonomic Bulletin & Review, 21(5), 1323-1330. https://doi.org/10.3758/s13423-014-0588-3

Rohrer, D., Dedrick, R. F., Hartwig, M. K., & Cheung, C.-N. (2020). A randomized controlled trial of interleaved mathematics practice. Journal of Educational Psychology, 112(1), 40-52. https://doi.org/ 10.1037/edu0000367

Rohrer, D., Dedrick, R. F., & Stershic, S. (2015). Interleaved practice improves mathematics learning. Journal of Educational Psychology, 107(3), 900-908. https://doi.org/10.1037/edu0000001

Sana, F., Yan, V. X., Kim, J. A., Bjork, E. L., & Bjork, R. A. (2018). Does working memory capacity moderate the interleaving benefit? Journal of Applied Research in Memory and Cognition, 7(3), 361- 369. https://doi.org/10.1016/j.jarmac.2018.05.005

Sandrone, S., Scott, G., &erson, W. J., & Musunuru, K. (2021). Active learning-based STEM education for in-person and online learning. Cell, 184(6), 1409-1414. https://doi.org/10.1016/j.cell.2021.01.045

Santhanam, R., Sasidharan, S., & Webster, J. (2008). Using selfregulatory learning to enhance e-learning-based information technology training. Information Systems Research, 19(1), 26-47. https://doi.org/10.1287/isre.1070.0141

Shrivastav, H., & Hiltz, S. R. (2013). Information overload in technology-based education: A meta-analysis. In Proceedings of the 19th Americas Conference on Information System.

Singh, P. V., Tan, Y., & Youn, N. (2011). A hidden Markov model of developer learning dynamics in open source software projects. Information Systems Research, 22(4), 790-807. https://doi.org/ 10.1287/isre.1100.0308

Sweller, J. (2010). Element interactivity and intrinsic, extraneous, and germane cognitive load. Educational Psychology Review, 22(2), 123-138. https://doi.org/10.1007/s10648-010-9128-5

Sweller, J. (2011). Cognitive load theory. In J. P. Mestre & B. H. Ross (Eds.), Psychology of learning and motivation (Vol. 55, pp. 37-76). Elsevier Academic Press. https://doi.org/10.1016/B978-0-12- 387691-1.00002-8

Sweller, J., van Merriënboer, J. J., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. Educational Psychology Review, 31(2), 261-292. https://doi.org/10.1007/ s10648-019-09465-5

Tauber, S. K., Dunlosky, J., Rawson, K. A., Wahlheim, C. N., & Jacoby, L. L. (2013). Self-regulated learning of a natural category: Do people interleave or block exemplars during study?

Psychonomic Bulletin & Review, 20(2), 356-363. https://doi.org/ 10.3758/s13423-012-0319-6

Taylor, K., & Rohrer, D. (2010). The effects of interleaved practice. Applied Cognitive Psychology, 24(6), 837-848. https://doi.org/ 10.1002/acp.1598

Tseng, S., Sue, P., Su, J., Weng, J., & Tsai, W. (2007). A new approach for constructing the concept map. Computers & Education, 49(3), 691-707. https://doi.org/10.1016/j.compedu.2005.11.020

Walls, J. G., Widmeyer, G. R., & El Sawy, O. A. (1992). Building an information system design theory for vigilant EIS. Information Systems Research, 3(1), 36-59. https://doi.org/10.1287/isre.3.1.36

Wang, C. (2022). Comprehensively summarizing what distracts students from online learning: A literature review. Human Behavior and Emerging Technologies, 2022, 1-15. https://doi.org/10.1155/2022/1483531

Wilson, K., & Nichols, Z. (2015). The Knewton platform. A generalpurpose adaptive learning infrastructure (Knewton White Paper). Available at https://www.profijt.nu/wp-content/uploads/2015/09/ 20150902-White-paper-The-Knewton-Platform.pdf

Wilson, K. H., Karklin, Y., Han, B., & Ekanadham, C. (2016). Back to the basics: Bayesian extensions of IRT outperform neural networks for proficiency estimation. In Proceedings of the 9th International Conference on Educational Data Mining.

Yan, V. X., Bjork, E. L., & Bjork, R. A. (2016). On the difficulty of mending metacognitive illusions: A priori theories, fluency effects, and misattributions of the interleaving benefit. Journal of Experimental Psychology: General, 145, 918-933. https://doi.org/ 10.1037/xge0000177

Yan, V. X., & Sana, F. (2021). Does the interleaving effect extend to unrelated concepts? Learners’ beliefs versus empirical evidence. Journal of Educational Psychology, 113(1), 125-137. https://doi.org/10.1037/edu0000470

Zhu, B., & Watts, S. A. (2010). Visualization of network concepts: The impact of working memory capacity differences. Information Systems Research, 21(2), 327-344. https://doi.org/10.1287/isre. 1080.0215

Zulkiply, N., & Burt, J. S. (2013). The exemplar interleaving effect in inductive learning: Moderation by the difficulty of category discriminations. Memory & Cognition, 41(1), 16-27. https://doi.org/10.3758/s13421-012-0238-9

## About the Authors

Andy Tao Li is a nontenured associate professor at the International Institute of Finance, School of Management, University of Science and Technology of China. He received his Ph.D. in information systems from Tsinghua University. His research interests are in the areas of e-learning, gamification, and social referral.

De Liu is a Xian Dong Eric Jing professor at the Carlson School of Management, University of Minnesota. He received his Ph.D. from the University of Texas at Austin, and his master’s and bachelor’s degrees from Tsinghua University. His recent research interests include gamification, internet-based auctions and market mechanisms, crowdfunding, and AI/augmented reality applications. His research has appeared in leading journals such as MIS Quarterly, Management Science, Information Systems Research, Journal of Marketing, Journal of Marketing Research, and Production and Operations Management. He previously served as an associate editor for Information Systems Research and Journal of Organizational Computing and Electronic Commerce.

Sean Xin Xu is a Starr Endowed Chair Professor and associate dean at the School of Economics and Management, Tsinghua University, China. His work has been published in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Management Science, Strategic Management Journal, and Contemporary Accounting Research, among other outlets. He won the MIS Quarterly Best Paper Award for 2013. His editorial services include senior editor for MIS Quarterly (2016- 2022) and senior editor for Information Systems Research (2023- present). Information Systems Research named him Best Associate Editor in 2013. He was named AIS Fellow in 2022.

Cheng Yi is an associate professor at the School of Economics and Management, Tsinghua University, China. She received her Ph.D. in information systems from National University of Singapore. Her research interests include human-computer interaction, electronic commerce, online consumer behavior and digital learning. Her work has appeared in journals such as Information Systems Research, Management Science, Production and Operations Management, and Journal of Management Information Systems. She currently serves as an associate editor for MIS Quarterly.

## Appendix A

## Estimation of the Hidden Markov Model

## Covariate Specification

According to Figure 1 in the main text, the transition covariates $( W _ { s t } ^ { c } )$ include time-invariant learner characteristics and time-variant learning history. The former includes gender, age, and pre-experiment exam scores and the latter includes the number of correctly answered questions on the focal topic, the number of incorrectly answered questions on the focal topic, and the total number of questions answered for all topics.

The emission covariates $( { Z _ { s t } ^ { c } } )$ also include the same time-invariant learner characteristics and time-variant learning-history variables. The emission process can also be affected by time-variant learner’s behavioral tendencies. The latter includes the average duration spent on each question of a given topic and the standard deviation of durations spent on questions of this topic.

## Maximizing the Likelihood of the Observed Learning Records over Time

We estimate a learner’s mastery level of different topics by maximizing the likelihood of the observed learning outcomes over time. The model specification and estimation are as follows.

For each specific topic $^ { c , }$ we used $X _ { s t } ^ { c }$ to represent the outcome of the $t ^ { \mathrm { { t h } } }$ assessment $( \mathrm { i . e . }$ , whether the $t ^ { \mathrm { { t h } } }$ question on topic c is correctly answered) for learner s. We define $\pmb { X _ { s } ^ { c ( T ) } } = \left( X _ { s 1 , } ^ { c } X _ { s 2 } ^ { c } , \dots , X _ { s T } ^ { c } \right)$ , representing a learner $s ^ { \prime } { \bf s }$ learning outcomes on topic c from assessment 1 to assessment T. We define $\boldsymbol { Y } _ { s } ^ { c ( T ) } = \left( Y _ { s 1 , } ^ { c } Y _ { s 2 } ^ { c } , \ldots , Y _ { s T } ^ { c } \right)$ as a learner s’s hidden mastery level history on topic c from assessment 1 to assessment T. The transition covariate matrix $( W _ { s } ^ { c ( T ) } )$ and emission covariate matrix $( \pmb { Z } _ { s } ^ { c ( \pmb { T } ) } )$ are similarly defined. The likelihood of observing the learning outcome $X _ { s } ^ { c ( T ) }$ for learner s on topic c from assessment 1 to assessment T is $\begin{array} { r } { \boldsymbol { L _ { s } ^ { c ( T ) } } = \boldsymbol { P } \left( \boldsymbol { X _ { s } ^ { c ( T ) } } \right) = \sum _ { \boldsymbol { Y } _ { \mathrm { c } } ^ { c ( T ) } } \boldsymbol { P } ( \boldsymbol { X } _ { s } ^ { c ( T ) } , ~ \boldsymbol { Y } _ { s } ^ { c ( T ) } ) } \end{array}$ . Following the Markov assumption, we can derive the likelihood as follows:

$$
L _ {s} ^ {c (T)} = \sum_ {\boldsymbol {Y} _ {s} ^ {c (T)}} P \left(\boldsymbol {X} _ {s} ^ {c (T)} \Big | \boldsymbol {Y} _ {s} ^ {c (T)}, \boldsymbol {Z} _ {s} ^ {c (T)}\right)   P (\boldsymbol {Y} _ {s} ^ {c (T)} | \boldsymbol {Y} _ {s} ^ {c (T - 1)}, \boldsymbol {W} _ {s} ^ {c (T - 1)})
$$

According to the dependencies in the Markov chain, we can decompose the $L _ { s } ^ { c ( T ) }$ as the sum over all the paths.

$$
L_{s}^{c(T)} = \sum_{\substack{Y_{s1}^{c},  Y_{s2}^{c},\dots ,Y_{sT}^{c}}}P(Y_{s1}^{c},W_{s1}^{c})  \prod_{t = 2}^{T}P(X_{st}^{c}|Y_{st}^{c},Z_{st}^{c})  P(Y_{st}^{c}|  Y_{st - 1}^{c},W_{st - 1}^{c}),
$$

where $P ( Y _ { s t } ^ { c } | Y _ { s t - 1 } ^ { c } , W _ { s t - 1 } ^ { c } )$ is the transition probability from the hidden state $Y _ { s t - 1 } ^ { c }$ at assessment t-1 to the hidden state $Y _ { s t } ^ { c }$ at assessment t, which is affected by the transition covariates $( W _ { s t - 1 } ^ { c } )$ , and $P ( X _ { s t } ^ { c } | Y _ { s t } ^ { c } , Z _ { s t } ^ { c } )$ is the emission probability of hidden state $Y _ { s t } ^ { c }$ at assessment t, which is affected by the emission covariates $( Z _ { s t } ^ { c } )$ . The joint likelihood of observing the learning outcomes for all learners and all topics from assessment 1 to assessment T is given by $\begin{array} { r } { L ^ { ( T ) } = \prod _ { s } \prod _ { c } L _ { s } ^ { c ( T ) } } \end{array}$ . We maximized the likelihood $L ^ { ( T ) }$ by choosing the value of each parameter.

During the experiment, we used the first two-week’s learning records to train the model (\~20,000 question-answer records) and applied the trained model to the remaining weeks. Following Singh et al. (2011) and Kim and Krishnan (2019), we chose the number of hidden states using the Bayesian information criterion, which indicates that the optimal number of hidden states is two, labeled as “unmastered” and “mastered,” respectively.

## Appendix B

## Knowledge Map Updating

We used the fuzzy association rules to discover topic dependencies and refine the knowledge map. The detailed knowledge map updating process is as follows. An assessment question answered by a learner is treated as a one-question record. Given that each question is mapped to one topic, we can transform a question record into a topic record. For a given topic, we pooled the records for an individual learner and got a record set. For each record set, we calculated the proportion of incorrect answers as the error rate for this topic. For example, learner s answered three questions related to Topic A and two were incorrectly answered. Thus, the error rate of Topic A for learner s is ErrorRate<sub>s</sub>(??) = 2/3. With n learners, we can calculate the support of A as the mean error rate of A:

$$
S u p p o r t (A) = \frac {1}{n} \sum_ {s = 1} ^ {n} E r r o r R a t e _ {s} (A).
$$

Therefore, a higher support is interpreted as a higher error rate.

Extending the notion of support to a set of topics, we could not use the Boolean logic operator because the error rates are numerical. Following Tseng et al. (2007), we calculated the support of a topic set using the fuzzy implication operator (FIO) minimization. Formally,

$$
\operatorname{Support} (A, B) = \frac {1}{n} \sum_ {s = 1} ^ {n} \min \left(\text { ErrorRate } _ {s} (\mathrm{A}), \text { ErrorRate } _ {s} (\mathrm{B})\right)
$$

A high value of Support(??, ??) implies that learners frequently answer both Topic A and Topic B questions incorrectly.

Following the rule of Bayesian posterior, we can derive the confidence level of association $( \mathbf { A } \ {  } \ \mathbf { B } )$ as follows:

$$
C o n f i d e n c e (A \rightarrow B) = \frac {s u p p o r t (A , B)}{s u p p o r t (A)}
$$

A high value of confidence (A → B) implies that a large portion of learners who incorrectly answered questions on Topic A also incorrectly answered questions on Topic B. With high support and confidence, we can consider Topic A to be a dependency for Topic B. To ensure that Topic A plays a significant role in Topic B’s accuracy, we followed the literature to only keep the rules whose lift, measured as ???????????????????? (?? → ??) , is larger than 1. ??????????????(??)

## Appendix C

## Pseudo Algorithm of the Scheduling Engine

## Pseudo Algorithm for Refining Topic List

\# This function modifies the weak topic list for a specific learner according to the knowledge map so that related weak topics are placed next to each other.

```txt
Function GetRefinedTopicList (WeakTopicList, KM) → RefinedTopicList {
# Inputs:
# WeakTopicList: Store the focal learner's weak topics detected by HMM
# KM: Stored the knowledge map updated by the fuzzy association rule
# Returns:
# RefinedTopicList: an ordered list of refined weak topics for the learner.
    RefinedTopicList = [];
    Sort WeakTopicList by the descending order of the probability of being unmastered;
    for (i=0; i< WeakTopicList.length(); i++) {
    WeakTopic = WeakTopicList[i] ;
    if (WeakTopic not in RefinedTopicList) {
    Append WeakTopic at the end of RefinedTopicList;
    }
    TopicDependencyList = look up all the topics that the WeakTopic depends on in KM;
    foreach TopicDependency in TopicDependencyList {
    if (TopicDependency in WeakTopicList) {
    insert TopicDependency into RefinedTopicList just before WeakTopic;
    }
    }
    }
    Return RefinedTopicList;
}
```

## Pseudo Algorithm for Schedule Exercises

```txt
This function schedules the exercises for the next learning session.
Function ScheduleExercises () → RankedExerciseList {
RankedExerciseList: a list of exercises for the focal learner in the next learning session
    RefinedTopicList = GetRefinedTopicList (WeakTopicList, KM) ;
    ExerciseList = look up all the exercises in the database that have not been assigned to the focal learner;
    foreach Exercise in ExerciseList {
    Exercise.TopicRankSum = 0 ;
    ExerciseWeakTopics = look up all the topics in the RefinedTopicList covered by the Exercise;
    foreach ExerciseWeakTopic in ExerciseWeakTopics {
    TopicRank = The position of ExerciseWeakTopic in the RefinedTopicList ;
    Exercise.TopicRankSum = Exercise.TopicRankSum + TopicRank ;
    }
    Exercise.NumberWeakTopics = ExerciseWeakTopics.length() ;
}
RankedExerciseList = sort ExerciseList by the descending order of NumberWeakTopics and the ascending order of TopicRankSum;
Return the top N Exercises in the RankedExerciseList ;
```

## An Example of Related-Interleaving across Sessions

As an illustrative example in Figure C1, the knowledge map models the relatedness among 9 topics (A to I). We use shaded circles to indicate a learner’s unmastered topics and white circles to indicate the mastered topics at the moment. The number beside an unmastered topic, as derived by the HMM, is the probability that the learner has not mastered it. Based on the modified ranking of weak topics in Session #N (D, C, A, B, F), we assign the learner exercises that cover three unmastered topics that are directly connected in the knowledge map (C, D, A). In Session #N+1, the system detects that the learner has mastered the practiced topics but becomes unfamiliar with E and H as time goes by. Consequently, the personalized list of weak topics becomes B, E, F, and H. According to the updated weak topics in modified topic ranking, we assign the learner exercises that cover three unmastered topics that are directly connected in the knowledge map (H, E, B) for Session #N+1.

![](/api/attachments/ZDGP6YXC/fulltext/images/88afe97574e75a1040fd0fb8a6131fb24c5bc834aefd4359760927b2e9b54ad0.jpg)  
Figure C1. An Example of Related-Interleaving across Sessions

## Appendix D

## System Description

When a learner logs in the system, they can click on the “personalized exercise” module and find all the personalized exercises assigned to them, including both the finished and unfinished ones, and the associated assignment dates and due dates, as shown in Figure D1.

<table><tr><td></td><td>Student name</td><td>Class ID</td><td>Status</td><td>Available from</td><td>Due by</td><td>Submit time</td></tr><tr><td>Select</td><td>*****, Chen</td><td>Grade 8, Class 3</td><td>Unfinished</td><td>2017-08-28</td><td>2017-08-29</td><td></td></tr><tr><td>Select</td><td>*****, Chen</td><td>Grade 8, Class 3</td><td>Unfinished</td><td>2017-08-28</td><td>2017-08-29</td><td></td></tr><tr><td>Select</td><td>*****, Chen</td><td>Grade 8, Class 3</td><td>Finished</td><td>2017-08-26</td><td>2017-08-27</td><td>2017-08-27 20:17:17</td></tr><tr><td>Select</td><td>*****, Chen</td><td>Grade 8, Class 3</td><td>Finished</td><td>2017-08-26</td><td>2017-08-27</td><td>2017-08-26 09:14:25</td></tr><tr><td>Select</td><td>*****, Chen</td><td>Grade 8, Class 3</td><td>Unfinished</td><td>2017-08-24</td><td>2017-08-25</td><td></td></tr><tr><td>Select</td><td>*****, Chen</td><td>Grade 8, Class 3</td><td>Finished</td><td>2017-08-24</td><td>2017-08-25</td><td>2017-08-24 21:41:17</td></tr><tr><td>Select</td><td>*****, Chen</td><td>Grade 8, Class 3</td><td>Finished</td><td>2017-08-22</td><td>2017-08-23</td><td>2017-08-23 16:40:12</td></tr><tr><td>Select</td><td>*****, Chen</td><td>Grade 8, Class 3</td><td>Finished</td><td>2017-08-22</td><td>2017-08-23</td><td>2017-08-22 16:28:06</td></tr></table>

Figure D1. Demo of a Learner-Specific List of Exercises

When a learner clicks on one exercise, the system displays an article and the corresponding assessment questions. After the learner submits the answers, the system automatically grades the answers and provides real-time feedback, including the correct answers and the reasoning processes, as illustrated in Figure D2. The learner can find all the learning records, along with the feedback, in the “learning records” section.

## Answers and reasoning processes of this article Article 38

Imagine you are walking to school when suddenly you notice a wallet in the street. After picking it up, you realize that it's full of \$10, S20, and \$50 bills. They add up to S500! What would you do?

Would you hand the wallet over to your headmaster as soon as you arrive at school? That's just what KemoyGourzang did.

"I have lost money before," Kemoy, a 10-year-old boy, told the reporter, "I knew if I had lost my wallet, I would have wanted it back."

Joy-Ann Morgan, the headmaster, immediately called the owner of the wallet, using the ID inside. The man did not realize he had lost it. Morgan said he was happy to learn that an honest kid had found it.

"This is what we want to teach our students," Morgan explained.

Kemoy has learned that doing the right thing pays off. His school district gave him a "Good Citizen" prize in honor of what he did. A person who has good citizenship is responsible and does the right thing. Kemoy has also received gifts from complete strangers, money, gift cards, and even a pair of sports shoes.

As for the owner of the wallet, he thanked Kemoy when he went to the school to get his wallet back. He also gave the student \$100 as a reward. "He told me I was the most honest person he had ever met," Kemoy said, "It makes me really happy."

## 1 How much money was there in the wallet?

Correct answer:D Your answer: D Reference:They add up to \$500!

## 2 What did Kemoy do after he picked the wallet up?

A: He handed it over to the headmaster. B:He told his friends about the money. C:He called the owner of the wallet. D:He asked a reporter for help. Correct answer:A Your answer: A Reference:Would you hand the wallet over to your headmaster as soon as you arrive at school? That's just what KemoyGourzang did.

3 Kemoy received for what he did from the school district. A:a pair of sports shoes B:a gift card C:a “Good Citizen” prize D:a \$100 bill Correct answer:C Your answer:B Reference:His school district gave him a “Good Citizen" prize in honor of what he did.

Figure D2. Snapshot of the Answer Page

## Appendix E

## Randomization and Manipulation Check

To ensure that the subjects were randomly assigned without significant differences in their prior performance across the three experimental groups (i.e., non-interleaving, unrelated-interleaving, and related-interleaving), we compared the pre-experiment exam scores (FinalScore) across the three groups. The results show no significant difference (Figure E1, All Learners). Furthermore, the average scores of weak and strong learners in the three groups were not significantly different (see Figure E1, Weak Learners and Strong Learners). In addition, the numbers of weak and strong learners were also equally distributed across the three groups. We also compared the pretest scores (Pretest) across the three groups. The results show no significant difference (Figure E2, All Learners). Furthermore, the average scores of weak and strong learners in the three groups were not significantly different (see Figure E2, Weak Learners and Strong Learners). Then we compared the gender (Female) distribution across the three groups and found no significant difference (see Figure E3).

Finally, we conducted the randomization checks in each of the 17 different classes. Table E1 reports the p-value of the pairwise comparison across the three groups by using the subsamples of each class. Table E1 also reports the p-value of ANOVA analysis for the differences between three groups in each of the 17 classes. Panel A, Panel B, and Panel C compare the pre-experiment final score, pretest score, and gender, respectively. In general, 16 out of 17 classes showed no significant difference across the three groups in terms of the pre-experiment final score, pretest score, and gender. One exception is Class 15. Class 15 showed no significant difference in terms of the pre-experiment final score and gender, but a marginal significance in terms of the pretest score across the three groups. To resolve this issue, we conducted robustness checks by removing all the students in Class 15 and found consistent results. Thus, we consider the randomization successful.

![](/api/attachments/ZDGP6YXC/fulltext/images/3b05424560e7e4cec69842075daa6825e8e689db7d137595a736f9f0ca2efce6.jpg)  
Figure E1. Randomization Check: Pre-experiment Exam Score Comparison

![](/api/attachments/ZDGP6YXC/fulltext/images/d2ff5f2db2b107bd552513a0f63c51422fdc52e86c62311364c38af839761863.jpg)

Figure E2. Randomization Check: Pretest Score Comparison

![](/api/attachments/ZDGP6YXC/fulltext/images/2862ec33e413ff07d8f5876826afb03e23559e9d5fd0961909be4e6245776a0e.jpg)

Figure E3. Randomization Check: Learner Gender

<table><tr><td colspan="18">Table E1. The p-value of Pairwise Comparison across Three Experimental Groups in Each of 17 Classes</td></tr><tr><td>ClassID</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td></tr><tr><td colspan="18">Panel A: Pre-experiment final score</td></tr><tr><td>Unrelated-interleaving – non-interleaving</td><td>0.96</td><td>0.55</td><td>0.66</td><td>0.84</td><td>0.77</td><td>0.92</td><td>0.81</td><td>0.26</td><td>0.42</td><td>0.95</td><td>0.66</td><td>0.89</td><td>0.95</td><td>0.72</td><td>0.70</td><td>0.91</td><td>0.75</td></tr><tr><td>Related-interleaving – unrelated-interleaving</td><td>0.63</td><td>0.81</td><td>0.58</td><td>0.28</td><td>0.50</td><td>0.90</td><td>0.61</td><td>0.42</td><td>0.75</td><td>0.13</td><td>0.79</td><td>0.65</td><td>0.51</td><td>0.98</td><td>0.44</td><td>0.90</td><td>0.91</td></tr><tr><td>Related-interleaving – non-interleaving</td><td>0.63</td><td>0.69</td><td>0.88</td><td>0.21</td><td>0.77</td><td>0.83</td><td>0.75</td><td>0.71</td><td>0.57</td><td>0.16</td><td>0.50</td><td>0.75</td><td>0.52</td><td>0.72</td><td>0.69</td><td>0.83</td><td>0.84</td></tr><tr><td>Three group comparison</td><td>0.85</td><td>0.83</td><td>0.85</td><td>0.40</td><td>0.79</td><td>0.98</td><td>0.87</td><td>0.50</td><td>0.70</td><td>0.27</td><td>0.78</td><td>0.89</td><td>0.75</td><td>0.92</td><td>0.74</td><td>0.98</td><td>0.95</td></tr><tr><td colspan="18">Panel B: Pretest score</td></tr><tr><td>Unrelated-interleaving – non-interleaving</td><td>0.86</td><td>0.49</td><td>0.56</td><td>0.52</td><td>0.63</td><td>0.55</td><td>0.70</td><td>0.50</td><td>0.70</td><td>0.67</td><td>0.51</td><td>0.74</td><td>0.68</td><td>0.59</td><td>0.85</td><td>0.85</td><td>0.88</td></tr><tr><td>Related-interleaving – unrelated-interleaving</td><td>0.30</td><td>0.75</td><td>0.72</td><td>0.56</td><td>0.23</td><td>0.50</td><td>0.73</td><td>0.16</td><td>0.35</td><td>0.36</td><td>0.24</td><td>0.74</td><td>0.41</td><td>0.26</td><td>0.05</td><td>0.61</td><td>0.76</td></tr><tr><td>Related-interleaving – non-interleaving</td><td>0.14</td><td>0.28</td><td>0.39</td><td>1.00</td><td>0.31</td><td>0.87</td><td>0.94</td><td>0.47</td><td>0.67</td><td>0.22</td><td>0.50</td><td>0.53</td><td>0.62</td><td>0.50</td><td>0.09</td><td>0.72</td><td>0.86</td></tr><tr><td>Three group comparison</td><td>0.30</td><td>0.54</td><td>0.68</td><td>0.77</td><td>0.40</td><td>0.74</td><td>0.91</td><td>0.36</td><td>0.64</td><td>0.46</td><td>0.48</td><td>0.81</td><td>0.71</td><td>0.52</td><td>0.11</td><td>0.87</td><td>0.95</td></tr><tr><td colspan="18">Panel C: Gender distribution</td></tr><tr><td>Unrelated-interleaving – non-interleaving</td><td>1.00</td><td>1.00</td><td>0.87</td><td>0.42</td><td>0.78</td><td>0.25</td><td>0.92</td><td>0.36</td><td>0.60</td><td>1.00</td><td>0.43</td><td>0.29</td><td>0.33</td><td>0.85</td><td>1.00</td><td>1.00</td><td>0.88</td></tr><tr><td>Related-interleaving – unrelated-interleaving</td><td>0.70</td><td>0.85</td><td>0.85</td><td>0.42</td><td>0.70</td><td>1.00</td><td>0.95</td><td>0.20</td><td>1.00</td><td>1.00</td><td>0.62</td><td>0.79</td><td>0.69</td><td>0.85</td><td>0.55</td><td>1.00</td><td>0.28</td></tr><tr><td>Related-interleaving – non-interleaving</td><td>0.73</td><td>0.85</td><td>0.70</td><td>0.97</td><td>0.54</td><td>0.25</td><td>0.97</td><td>0.68</td><td>0.57</td><td>1.00</td><td>0.75</td><td>0.48</td><td>0.56</td><td>1.00</td><td>0.52</td><td>1.00</td><td>0.31</td></tr><tr><td>Three group comparison</td><td>0.91</td><td>0.98</td><td>0.93</td><td>0.64</td><td>0.82</td><td>0.41</td><td>0.99</td><td>0.42</td><td>0.82</td><td>1.00</td><td>0.72</td><td>0.55</td><td>0.62</td><td>0.97</td><td>0.76</td><td>1.00</td><td>0.48</td></tr></table>

To check the manipulation in terms of whether the topics were successfully interleaved, we retrieved learners’ exercise records during the experiment. Each learner in the non-interleaved group completed 34.3 exercises and each exercise covered 1.16 topics on average, indicating that the learners were supplied with exercises covering only one unmastered topic most of the time. Each learner in the unrelated-interleaving group completed 34.9 exercises, with each exercise covering 3.42 topics on average. Each learner in the related-interleaved group completed 35.6 exercises, with each exercise covering 3.38 topics on average. As depicted in Figure E4, the learners in the unrelated-interleaving and related-interleaving groups received exercises covering significantly more topics than those in the non-interleaving group (p < 0.001). This pattern held for both strong learners and weak learners. Hence, the manipulation of interleaving is considered successful.

We also checked the manipulation of topic relatedness by comparing the number of topic dependencies covered by each exercise between the unrelated-interleaving group and the related-interleaving group. Learners in the unrelated-interleaving group received exercises covering 0.47 topic dependencies on average, whereas learners in the related-interleaved group received exercises covering 2.29 topic dependencies on average. As depicted in Figure E5, the learners in the related-interleaving group received exercises with significantly more topi relationships (p < 0.001). This pattern also held for both strong learners and weak learners. Hence, the manipulation of topic relatedness is considered successful.

![](/api/attachments/ZDGP6YXC/fulltext/images/ba5f614ad0bb72636eb39c5d333e48b5fa6a2c2ef608de28ac88672efb3dc1c0.jpg)  
Figure E4. Manipulation Check: Average Number of Topics Covered per Exercise

![](/api/attachments/ZDGP6YXC/fulltext/images/e92b5b07ddc54a3e315d617cdc29b031fd9a62a8fb7ce144a97a0686284aaba3.jpg)  
Figure E5. Manipulation Check: Average Number of Topic Dependencies in Each Exercise

## Appendix F

## Exploring the Effects of Related-Interleaving on Cognitive Load

To provide further evidence of whether our findings can be explained by cognitive load theory, we explored whether related-interleaving induced more cognitive load on schema building during learning sessions than unrelated-interleaving and non-interleaving. Although we did not directly observe learners’ schema-building load, the literature suggests a few indirect indicators of schema-building load, as detailed below.

First, CLT suggests that when learners engage more cognitive resources in schema building, they achieve a higher level of knowledge acquisition (Ausubel et al. 1968). Accordingly, knowledge acquisition scores are the “most common method of investigating cognitive load” (Brunken et al. 2003; Orru and Longo 2019). In our study, because we used the HMM to estimate the learner’s topic mastery after each learning session, we were able to leverage HMM estimates of topic mastery as a measure of knowledge acquisition scores. Second, similar to knowledge acquisition scores, researchers have also used learners’ accuracy of doing exercises during a learning session as an indirect measure of their schema-building load (Martin 2014; Orru and Longo 2019). We, therefore, obtained learners’ accuracy in answering questions in each learning session.

Table F1. Effect of Related-Interleaving on Topic Mastery and Session Accuracy

<table><tr><td rowspan="2"></td><td>Topic mastery</td><td>Session accuracy</td></tr><tr><td>(1)</td><td>(2)</td></tr><tr><td>Interleaving</td><td>-0.004(0.00)</td><td>0.006(0.01)</td></tr><tr><td>Interleaving × Relatedness</td><td>0.043***(0.00)</td><td>0.026***(0.01)</td></tr><tr><td>FinalScore</td><td>0.005***(0.00)</td><td>0.006***(0.00)</td></tr><tr><td>Pretest</td><td>0.005***(0.00)</td><td>0.002***(0.00)</td></tr><tr><td>Female</td><td>0.050***(0.00)</td><td>0.067***(0.01)</td></tr><tr><td>Constant</td><td>-1.176***(0.05)</td><td>-0.044(0.10)</td></tr><tr><td>Class fixed effect</td><td>YES</td><td>YES</td></tr><tr><td>Date fixed effect</td><td>YES</td><td>YES</td></tr><tr><td>Topic fixed effect</td><td>YES</td><td>NO</td></tr><tr><td>N</td><td>79772</td><td>11269</td></tr><tr><td> $R^2$ </td><td>0.229</td><td>0.196</td></tr></table>

Note: Interleaving represents the effect of unrelated-interleaving relative to non-interleaving. Relatedness is meaningful in the interleaving condition, but not in the non-interleaving condition. Therefore, Interleaving × Relatedness is equivalent to Relatedness and captures the effect of related-interleaving relative to unrelated-interleaving. \* p < 0.05, \*\* p < 0.01, \*\*\* p < 0.001. Standard errors are in parentheses.

We first compared learners’ mastery of each topic in each learning session across three experimental groups (see Table F1, Column 1), controlling for the pre-experiment final exam score (FinalScore), the pretest score (Pretest), and gender (Female). We also included the class fixed effect to incorporate class-level heterogeneity, the date-fixed effect to control for time heterogeneity, and the topic-fixed effect to incorporate topic-level heterogeneity. Then, we compared learners’ accuracy during the learning session across three experimental group (see Table F1, Column 2).

Figure F1, Column 1 shows that learners in the related-interleaving condition had 3.8% and 4.3% higher probabilities of mastering the topics learned in the session, compared with learners in the non-interleaving and unrelated-interleaving conditions, respectively. Column 2 shows that learners in the related-interleaving condition had 3.1% and 2.6% increases in session accuracy compared with learners in the noninterleaving and unrelated-interleaving conditions, respectively. Overall, evidence based on the two indirect measures indicates that relatedinterleaving led to increased schema-building load during learning sessions, which is consistent with the CLT predictions.

![](/api/attachments/ZDGP6YXC/fulltext/images/66f44ccd444fede83accca48d2c598b5c41fcd20395649fc718ca9da22a31b12.jpg)  
Note: A dot represents the mean value, and the error bar represents the 95% confidence interval.

Figure F1. Test the Schema Building by Topic Mastery and Session Accuracy

## Appendix G

## Sensitivity Analysis

In the above analyses, we categorized the learners as strong or weak based on a median split of their pre-experiment exam scores. We conducted a sensitivity analysis by varying the definition of strong learners from the top 40% to the top 60% in the class based on their final exam scores. We repeated the analyses and report the results in Table G1. Our results show that the three-way interaction (Interleaving × Relatedness × StrongLearner) is consistently negative. Thus, our findings are not sensitive to the selection of the cutting point for the division. Furthermore, the effect of relatedness for weak learners (Interleaving × Relatedness) increased from 14.56 to 24.32 when strong learners were defined as the top 60% rather than the top 40% of the class. In other words, the positive effect of topic relatedness is more pronounced for learners in the remaining 40% of the class. For these learners, increasing topic relatedness was more beneficial because it helped reduce the basic processing load caused by interleaved learning.

Table G1. Sensitivity Analyses of the Heterogeneous Effect for Different Types of Learners

<table><tr><td rowspan="2"></td><td>40%</td><td>45%</td><td>50%</td><td>55%</td><td>60%</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Interleaving</td><td>-15.92***(4.59)</td><td>-16.02**(4.98)</td><td>-19.86***(5.38)</td><td>-21.31***(5.88)</td><td>-28.17***(6.19)</td></tr><tr><td>Interleaving × Relatedness</td><td>14.56***(4.01)</td><td>17.42***(4.28)</td><td>18.81***(4.48)</td><td>21.40***(4.63)</td><td>24.32***(4.87)</td></tr><tr><td>Interleaving × StrongLearner</td><td>25.25***(6.98)</td><td>21.57**(6.96)</td><td>25.18***(6.98)</td><td>26.60***(7.24)</td><td>34.59***(7.41)</td></tr><tr><td>Interleaving × Relatedness × StrongLearner</td><td>-11.59+(6.94)</td><td>-15.50*(6.74)</td><td>-15.86*(6.56)</td><td>-19.22**(6.45)</td><td>-22.58***(6.42)</td></tr><tr><td>StrongLearner</td><td>-6.87(5.04)</td><td>-4.42(5.16)</td><td>-7.13(5.35)</td><td>-4.16(5.72)</td><td>-8.71(5.88)</td></tr><tr><td>Pretest</td><td>0.35***(0.06)</td><td>0.35***(0.06)</td><td>0.36***(0.06)</td><td>0.36***(0.06)</td><td>0.38***(0.06)</td></tr><tr><td>Female</td><td>7.01*(2.81)</td><td>6.83*(2.84)</td><td>6.84*(2.82)</td><td>6.81*(2.76)</td><td>6.76*(2.71)</td></tr><tr><td>Constant</td><td>58.55***(7.28)</td><td>56.23***(7.36)</td><td>58.46***(7.48)</td><td>56.28***(7.57)</td><td>58.32***(7.63)</td></tr><tr><td>Class fixed effect</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>N</td><td>306</td><td>306</td><td>306</td><td>306</td><td>306</td></tr><tr><td> $R^2$ </td><td>0.343</td><td>0.335</td><td>0.343</td><td>0.362</td><td>0.384</td></tr></table>

Note: <sup>+</sup> p < 0.10, \* p < 0.05, \*\* p < 0.01, \*\*\* p < 0.001. Standard errors are in parentheses.
