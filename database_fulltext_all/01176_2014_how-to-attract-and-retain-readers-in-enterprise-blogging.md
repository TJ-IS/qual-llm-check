---
otero_id: 1176
otero_key: "EVQ6AAHK"
title: "How to Attract and Retain Readers in Enterprise Blogging?"
authors: "Param Vir Singh; Nachiketa Sahoo; Tridas Mukhopadhyay"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2013.0509"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [165.123.34.86] On: 04 March 2015, At: 03:25 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## HSR

## Information Systems Research

![](/api/attachments/EVQ6AAHK/fulltext/images/39d593eddae4c376f3f1bdc1c90ae6a996be3a9cac182dd4fd55be3573fb65af.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## How to Attract and Retain Readers in Enterprise Blogging?

Param Vir Singh, Nachiketa Sahoo, Tridas Mukhopadhyay

## To cite this article:

Param Vir Singh, Nachiketa Sahoo, Tridas Mukhopadhyay (2014) How to Attract and Retain Readers in Enterprise Blogging?. Information Systems Research 25(1):35-52. http://dx.doi.org/10.1287/isre.2013.0509

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/EVQ6AAHK/fulltext/images/49de5f3c38d2d4621db18bc89a8eff13e385c1b857f0f1c0bbe414f7619193fd.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# How to Attract and Retain Readers in Enterprise Blogging?

Param Vir Singh

Tepper School of Business and iLab, Heinz College, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, psidhu@cmu.edu

Nachiketa Sahoo

School of Management, Boston University, Boston, Massachusetts 02215; and iLab, Heinz College, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, nachi@bu.edu

Tridas Mukhopadhyay

Tepper School of Business and iLab, Heinz College, Carnegie Mellon University Qatar, Doha, Qatar, tridas@cmu.edu

W<sup>e</sup> <sup>investigate</sup> <sup>the</sup> <sup>dynamics</sup> <sup>of</sup> <sup>blog</sup> <sup>reading</sup> <sup>behavior</sup> <sup>of</sup> <sup>employees</sup> <sup>in</sup> <sup>an</sup> <sup>enterprise</sup> <sup>blogosphere.</sup> <sup>A</sup> <sup>dynamic</sup> model is developed and calibrated using longitudinal data from a Fortune 1,000 IT services firm. Our modeling framework allows us to segregate the impact of textual characteristics (sentiment and quality) of a post on attracting readers from retaining them. We find that the textual characteristics that appeal to the sentiment of the reader affect both reader attraction and retention. However, textual characteristics that reflect only the quality of the posts affect only reader retention. We identify a variety-seeking behavior of blog readers where they dynamically switch from reading on one set of topics to another. The modeling framework and findings of this study highlight opportunities for the firm to influence blog-reading behavior of its employees to align it with its goals. Overall, this study contributes to improved understanding of reading behavior of individuals in communities formed around user generated content.

Keywords: blogs; employee blogs; enterprise 2.0; blog reading; dynamic models; user generated content; text mining

History: Ram Gopal, Senior Editor; Kartik Hosanagar, Associate Editor. This paper was received on November 23, 2010, and was with the authors 21 months for 2 revisions.

## 1. Introduction

Blogs are one of the earliest Web 2.0 technologies to be adopted within organizations. Prominent adopters of organizational blogs are Microsoft, Sun Microsystems, Google, Adobe, IBM, Infosys, etc. Employees spend considerable time in designing, thinking, reading, and writing posts. It has been argued that the value of knowledge shared among employees through blog posts makes up for such expense (Efimova 2007, Huang et al. 2010).

Encouraged by positive media reports and given the lukewarm acceptance of traditional knowledgesharing initiatives, firms are increasingly adopting nontraditional channels such as blogs and wikis for sharing knowledge among employees (Huang et al. 2010, Lucier and Torsilieri 1997, Efimova 2007). However, the nature of this social medium is such that it allows users the opportunities to engage in both work-related and nonwork-related activities. Examining blogs at a large IT services firm, we find that fewer work-relevant articles are being published than nonwork-relevant articles. Moreover, work-relevant articles are read less often, when compared on a per post basis, than nonwork-relevant posts. For every work-relevant article, three nonwork-relevant articles are published. Further, for every person reading a work-relevant post, four people read nonworkrelevant posts.

Firms are confronted with the challenge of promoting posting as well as reading of content that helps employees in their work. However, research in understanding blog-reading behavior has been difficult since blog reading, unlike publishing on blogs or commenting on blogs, is usually invisible to external observers. In this study we take a step toward shedding some light on the blog-reading behavior of employees with the help of a unique data set collected from a large IT services firm. We seek to understand this behavior and how it develops so that an organization may take steps to influence it to its advantage.

In Figure 1 we plot the reading frequency of a randomly selected reader on work and nonwork posts over 22 months. This figure reveals that the reading amount on topics vary over time. For example, in period 7 the employee reads a lot of nonwork related content, whereas in period 16 she reads a lot of work-related content. This example indicates that the reader’s preferences change over time, and there are dynamics in the reading behavior of employees where they switch reading on one topic to another. These dynamics present several opportunities and vulnerabilities for bloggers as well as firms. It is particularly important for understanding what factors may affect attraction and retention of readers on topics. Ideally, firms would like to move employees from reading nonwork-related content to reading work-related content. Hence, it is important to understand what factors affect the switching of a reader from reading on nonwork topics to work topics, and vice versa.

Figure 1 Reading Frequency on Work and Nonwork Topics Over Time for a Randomly Selected Reader  
![](/api/attachments/EVQ6AAHK/fulltext/images/a540ce0c9f4eb4d372b04c6326c494331af07020f7c849c7b8f2ad19b23453b0.jpg)  
Notes. Four subtopics. WTK: Work-related Technical Knowledge, WMK: Work related Managerial Knowledge, NWK: Nonwork related Knowledge, and NWE: Nonwork-related Entertainment.

The dynamics in the reading behavior can be separated into two parts: attraction and retention. Attraction refers to attracting a reader to read on a topic, and retention refers to holding on to the reader to continue reading on the topic over time. A reader is first attracted toward a topic; she then either continues to read on the topic or moves to another topic. If the reader continues to read for a long time on the same topic, it would imply that the topic has high retention. To understand the dynamics in the reading behavior, we develop a dynamic model that incorporates both attraction and retention of readers and allows one to segregate the impact of various factors on attracting and retaining readers on a topic.

The attraction and retention of readers can be affected by several factors. In this study we focus on two such factors: quality and sentiment of the blog posts. It is also important to identify whether blog readers are inherently variety seekers. The dynamics in Figure 1 could just be a result of blog readers being inherently variety seekers. These factors (quality and sentiment of blog posts and variety-seeking nature of readers) are important because they are quantifiable, and potential interventions can be introduced to affect these factors. Specifically, we ask the following questions: How do the post characteristics (quality and sentiment) affect the magnitude of readership and the retention of readers on a topic? And, are blog readers variety seekers?

We model the readership dynamics in the same spirit as the dynamic state-space models by Hamilton (1989) and Rabiner (1989). Most of the blogging content consumption models assume static reader behavior (e.g., Aggarwal et al. 2012). There are two key advantages of our dynamic state-space model over the traditional static models when studying individual behavior. The first advantage is that our dynamic model is more generalizable. It allows for dynamics in individual behavior without enforcing them. Hence, when there are dynamics in the individual behavior, our model will be superior to static models and will provide consistent estimates of factors that affect behavior. In contrast, in the absence of dynamics in behavior, the dynamic state-space model would collapse to a static model. On the other hand, when there are dynamics in user behavior, the static model would give us erroneous estimates of the factors affecting user behavior. The second advantage of the dynamic model is its ability to provide insights into when and how the individual behavior should be influenced. More specifically, it allows the segmentation of individuals according to their reading behavior in terms of types and volume of posts read at any time. This segmentation allows one to investigate the varying impacts of post characteristics across individuals on their movement from reading on one set of topics to another. This provides insight into the strategic targeting of individuals in different states to effectively induce higher work-related readership. Such insight cannot be obtained from the standard static framework.

The main contribution of this research is in providing a dynamic model that provides managers with the ability to understand blog-reading behavior of employees. Using our model, managers can dynamically classify an employee to a reading state (specified by an individual’s preference to read on each topic) and assess the dynamic effects of post characteristics on employee transitions to the most preferred state. The other key contribution of this study pertains to the results obtained using our dynamic model. We find a variety-seeking behavior displayed by blog readers whereby readers frequently switch from reading one set of topics to another. We find that both post quality and sentiment affect reader retention, whereas only sentiment affects reader attraction.

The rest of the paper proceeds as follows. In §2, we introduce the research setting. In §3, we present the literature review and develop theoretical arguments. In §4, we present the dynamic model. The data, variable construction, and descriptive statistics are provided in §5, followed by estimation procedures and model selection in §6. Results and discussion are presented in §7, followed by conclusions, contributions, and limitations in §8.

## 2. Research Setting

Our research setting is a large, Fortune 1,000 information technology services, business process outsourcing, and consulting firm. Fortune named this firm one of the fastest growing companies in 2009. Its annual revenues in year 2009 were a few billion dollars, and it employs more than 75,000 employees. It is a United States-based firm with significant operations in Europe, Asia, and Americas. Over the years its global presence led to the emergence of localized silos of knowledge and reduced knowledge flow from one location to another. Even within the same location, knowledge sharing was not efficient. To facilitate knowledge and information sharing across as well as within locations, the firm has undertaken several measures. Prominent among these measures is the use of Web 2.0 technologies within the enterprise. It has been one of the earliest adopters of Web 2.0 technologies in its industry. Given a primarily technologically educated workforce, it is not surprising that these technologies have been well accepted by its employees. The focus of this study is on employee blogs within this firm.

The firm adopted the use of employee blogs in mid-2006. These blogs are hosted on an internal platform and are accessible only to the employees of the firm. Every employee is allowed to maintain her own blog on this platform. The blog is accessible to all the employees of the firm. The identity of the blog writer is also revealed on the blog. The firm does not restrict the kind of posts that can be written by the employees. Navigation of the blogosphere is facilitated by a search tool that allows readers to search for specific key words. Relevant and more popular posts are listed earliest in the search result. The readers can also visit a blog if they know the direct link or can navigate through the hyperlinks presented in the search results.

To analyze the type of content that is being shared on the internal blogosphere, the firm broadly classifies the blog categories into four broad topics: nonwork entertainment posts (NWE), nonwork knowledge posts (NWK), work-related managerial knowledge posts (WMK), and work-related technical knowledge posts (WTK). Approximately three out of four posts have been in the nonwork topics (NWE and NWK). Similarly, employees tend to read nonwork-related categories (1.2 million) more compared to work-related categories (0.24 million). The writing and reading of blogs is voluntary, and the firm does not provide any direct incentives for using these Web 2.0 technologies. However, an internal analysis by the firm revealed that the employees who read work-related posts saw an increase in their productivity compared to others. The upper management of the firm is encouraged by this finding. Although they want employees to read more workrelated topics, they do not want to constrain employee behavior in any way that may reduce the employees’ use of the blogging platform. This leads to the motivation of the current work (i.e., to understand the factors that affect the dynamics in reading behavior of the employees).

## 3. Literature Review and Theoretical Development

In this section, we first introduce the emerging literature on blogs and explain how we contribute to this literature. Then we develop a theoretical framework to explain blog-reading behavior as a function of the characteristics of blog readers and posts. Finally, we briefly introduce the literature on empirical dynamic models.

Researchers have studied several aspects of blogs over the years. These studies have analyzed how blogs affect product sales (Mishne and Glance 2006), outcome of important events (Adamic and Glance 2005), and perceptions about the hosting firm (Aggarwal et al. 2012). Some have also shed light on why people write blog posts (Huang et al. 2010, Nardi et al. 2004, Furukawa et al. 2007), why bloggers cite others’ posts and leave comments on posts (Adamic and Glance 2005), and how commenting and citing relationships change over time (Sahoo et al. 2008).

Despite the recent studies of blog writing, citing, and commenting, few have examined the activity that is the foundation of them all: blog reading. It is more pervasive than the aforementioned activities and can be considered necessary for citing and commenting; yet, it is largely invisible to the end users of the blogs. Lack of availability of such data to the end users has led to a gap in the research on blogging. It is interesting to note that blog-reading data has been available to the blog hosts in the form of Web server access logs for a long time. The current research has been made possible because of a successful sharing agreement of such data between the host company and our research team.

## 3.1. Factors Affecting Dynamics in Blog-Reading Behavior

3.1.1. Inherently Variety-Seeking vs. Inertial Nature. Our interest is in understanding the reading dynamics and to identify factors that affect these dynamics. One potential explanation for these dynamics is that blog readers are inherently variety seekers. Individuals switch from one set of topics to another to satisfy their inherent desire for variety (McAlister 1982). A need for variety can stem from different types of incentives for different topics. Huang et al. (2010) suggest that blog reading is driven by a number of incentives. Work-related blogs may contain knowledge, which may lead to better performance. Nonwork-related blogs, on the other hand, provide entertainment/leisure value to the reader. Although these incentives are different, employees have value for all of them. Employees can achieve a balance by reading on a variety of topics at the same time. However, given the limited amount of time employees typically have to participate in blogging, they seek a balance between reading different types of blog posts across time. Hence, they can achieve this balance by switching between reading different topics over time, which could lead to dynamics in reading over time.

However, blog reading requires readers to find the topics they like and then adapt to the bloggers’ content and style of writing. This adaptation creates significant switching costs for the blog readers. These factors lead us to expect that inherently blog readers would be driven by inertia. Hence, it is an empirical question whether blog readers are inertial or variety seekers.

3.1.2. Textual Characteristics of the Blog Content. Changes in individuals’ behavior have been attributed to changes in situational variables (e.g., individual’s interactions) (McAlister and Pessemier 1982, McAlister 1982). Oliver (1997) suggests that situational variables can affect user satisfaction and thereby change user behavior. In the context of blog reading, situational factors can affect the extent of satisfaction that a reader derives from reading on a specific topic and hence can affect the readership dynamics leading to variety seeking. Hence, another potential explanation for the dynamics in reading behavior is that individuals switch from one set of topics to another because they get dissatisfied with the content on the topic. The situational variables of particular interest in our context of study are the characteristics of the post content.

Quality of the language in the blog post. One way of measuring quality is through the readability, comprehensiveness, and grammatical correctness of posts (Ghose and Ipeirotis 2011, Lu et al. 2013). Lu et al. (2013) find that readers trust reviewers who write readable and comprehensive reviews. This leads one to believe that readers would be attracted to well-written blogs. However, there are different aspects of the quality of writing, and readers may respond to them differently. We discuss some of them in detail below.

i. Readability. Readability of an article depends on several factors. An article can be grammatically correct yet hard to read if it has long sentences, uses uncommon words, or uses complex words (e.g., words with many syllables). Optimal readability of the text and the grade level appropriate for a certain reader has been linked to the level of education the reader has received (Kincaid et al. 1975). Individuals with lower-grade-equivalent education may read and understand only very simple text, whereas readers with higher level education appreciate more complex text. This suggests that when a reader with certain education level is presented with articles with a wide range of readability levels, her satisfaction with the articles will increase with the readability grade level only up to the optimal level of difficulty, after which it will reduce. This optimal level of difficulty is a function of an individual’s education level. If a reader reads a post that would be more appropriate for someone with a much higher (much lower) education level, she may not be satisfied with the post. Hence, the reader would be most satisfied with the post that is appropriate for her education level. Because, the posts in our sample have a wide range of readability scores, some are very low (requiring very low education level) and some are very high (requiring very high education level), we posit that readability will have an inverse U-shaped impact on both attracting readers and retaining them.

ii. Grammatical correctness. Studies have shown that grammatical errors increase readers’ effort, reduce readers’ recall of the subject, and reduce the credibility of the author (Beason 2001, Appelman and Bolls 2011). In the context of online reviews, Ghose and Ipeirotis (2011) show that readers find grammatically correct reviews to be most helpful. Despite the proliferation of casual use of language in social media, especially when using mobile devices to access them (Cingel and Sundar 2012), evidence suggests that grammatical errors damage the credibility of the writers and turn off the readers (Beason 2001). Therefore, we posit that grammatical errors in posts will have a negative impact on both attracting and retaining readers.

iii. Comprehensiveness. A comprehensive article consists of a detailed examination of various aspects of the topic being discussed. Therefore, this is a positive quality of an article. So one would expect that more comprehensive posts should attract more readers. However, because of the considerable amount of content a comprehensive post may have, it would require more effort from the reader. The literature on satiation shows that a higher intensity of consumption of a product hastens satiation (McAlister and Pessemier 1982, McAlister 1982). Therefore, in the context of blogs, we posit that although comprehensiveness should attract more readers, it would have an inverse U-shaped effect on retention where less comprehensive posts do not provide enough information and very comprehensive posts hasten satiation.

Sentiment of the blog post.

i. Negativity. Apart from how well or poorly an article is written, the meaning of what is written can influence its readership. One such quality is the positive or negative sentiment expressed in a post. In our corporate blog data set, we find there are numerous congratulatory or celebratory blog posts. Although these contain valuable information about the company and information that could be useful for the employee, they rarely contain critical examination of the issues that can provide deeper insight. The posts containing such critical examination often have less than profusely positive sentiments. This leads us to believe that articles with less positive sentiments would be more meaningful to their readers and thereby attract more readers. However, studies have also found that extremely negative sentiments in posts can reduce the readership of the posts, as reader may construe the bloggers to be disgruntled employees and their views to be unfair (Aggarwal et al. 2012). So we posit that a moderate amount of negativity would be best for attracting and retaining readers in comparison to extreme negativity.

ii. Controversialness. A second type of sentiment is the sentiment a post evokes among its readers. Although this could be related to the sentiment expressed by the writer in the post, it has more to do with the topic of the post and position taken by the author. One useful way to analyze the sentiments among readers is to see if they have diverse reactions toward the post as seen by the sentiments expressed in their comments. This would indicate that the author’s position on the topic is controversial. Controversial topics often contain valuable insight, since they occur at the intersection of multiple meaningful alternative points of view (Lunstrum 1965). They have been shown to motivate readers to do more in-depth research of the topic and participate in the discussion (Lunstrum 1981). In the context of blogs, we expect the information about the controversial posts to spread through word-of-mouth more rapidly than a post that is merely well written. Therefore, we expect the readership to increase with the degree of controversy in the blog post.

## 3.2. Empirical Models of Behavior Dynamics

Past literature provides some guidance for modeling the dynamics in behavior. Heckman (1981) suggests modeling behavior dynamics as state dependence. A number of studies have followed this approach. However, except for a few, most studies have incorporated state dependence through a single variable (e.g., total number of posts read in the past) that accounts for the past in an otherwise static model. Recent studies by Singh et al. (2011) and Netzer et al. (2008) have emphasized that state dependence should be modeled more comprehensively. They argue that a single-state variable in an otherwise static model may not be able to capture the true dynamics. Besides, it does not allow us to structurally account for the impact of situational variables that may be of interest to managers. In this study, we account for dynamics in a more elaborate fashion by allowing the parameters of an individual to change dynamically as a result of situational variables and unobserved effects.

## 4. Modeling Framework

The modeling framework we develop is designed to explain the dynamics in employees’ reading volume on topics across months. Our objective is to understand how textual characteristics (sentiment and quality) of the blog posts and the status of the bloggers affect employees to read more on topics, and how textual characteristics and the diversity of content read by the reader affects her switching from one set of topics to another. Hence, we seek a mathematical structure that allows reading and switching behaviors to depend upon several explanatory variables.

In our dynamic model, there are a finite number of hidden states. All other things being equal, each state corresponds to a unique reading behavior. At any given point in time, an individual resides in only one state. Given the state, several factors, some of which are observed, affect her reading volume on different topics. She can transition from one state to another. This Markovian transition is affected by several factors, some of which are observed, such as her reading outcome in a given period.

Our model works as follows. There are S latent states. In period $t ,$ an individual probabilistically belongs to a latent state. The state probabilistically determines her levels of reading across topics in period t. The reading outcomes in period t probabilistically determine whether the individual will stay in the same state or switch to another state in period t + 1. In this way, the reading process is structurally modeled through an integrated framework that links the unobserved but evolving states with the realized reading outcomes. Figure 2 graphically illustrates how we model an individual’s transitions between states as a function of her reading outcome and how her reading outcome depends upon the latent states.

## 4.1. Modeling Blog-Reading Dynamics

Let $S _ { i t } = \{ 1 , 2 , \dots , S \}$ represent the state of individual i in period t. Let $N _ { i j t } = \{ 1 , 2 , \dots , N \}$ be the count of posts read by individual i on Topic j in time period $t ,$ where $\mathbf { N } _ { i t } = \{ N _ { i 1 t } N _ { i 2 t } , \ldots , N _ { i k t } \}$ represent the set of readings across k topics for individual i at time t.

Figure 2 Graphical Representation of Dynamic Model of Blog Reading  
![](/api/attachments/EVQ6AAHK/fulltext/images/d69f84133ab6770ba8710da8e6bee21beec235287065dd329e6230d52f2294f2.jpg)

Our dynamic model is comprised of three elements:

(i) The initial state distribution $( \pmb { \pi } _ { i } )$ . The probability that individual i is in state s at time period 1 is $P ( S _ { i 1 } = s ) = \pi _ { i s }$ . Here, Ï is $S \times 1$ vector whose sth element is $\pi _ { s }$

(ii) The Markovian state-transition probability distribution $( \mathbf { Q } _ { i , t - 1 , t } )$ . The probability that individual i will transition from state s in period $t - 1$ to state $s ^ { \prime }$ in period t is $P ( S _ { i t } = s ^ { \prime } \mid S _ { i t - 1 } = s ) = q _ { i t s s ^ { \prime } }$ . Here, $\mathbf { Q } _ { i , t - 1 , i }$ is a $S \times S$ matrix, whose element corresponding to sth row and s<sup>0</sup>th column is $q _ { i t s s ^ { \prime } }$

(iii) The state dependent reading outcome. The probability that individual i will read n posts in period $t ,$ where n is a vector of size $1 \times k ,$ conditional on her state is $P ( \mathbf { N } _ { i t } = \mathbf { n } \mid S _ { i t } = s ) = a _ { i t \mid s }$

4.1.1. Markov State-Transition Probabilities. The state-transition distribution, $\mathbf { Q } _ { i , t - 1 , t } ,$ is defined as follows:

$$
\mathbf {Q} _ {i, t - 1, t} = \left( \begin{array}{c c c c c} q _ {i t 1 1} & q _ {i t 1 2} & \dots & q _ {i t 1 S - 1} & q _ {i t 1 S} \\ q _ {i t 2 1} & q _ {i t 2 2} & \dots & q _ {i t 2 S - 1} & q _ {i t 2 S} \\ & & \vdots & & \\ q _ {i t S - 1 1} & q _ {i t S - 1 2} & \dots & q _ {i t S - 1 S - 1} & q _ {i t S - 1 S} \\ q _ {i t S 1} & q _ {i t S 2} & \dots & q _ {i t S S - 1} & q _ {i t S S} \end{array} \right),
$$

where $0 \leq q _ { i t s s ^ { \prime } } \leq 1$ and $\textstyle \sum _ { s ^ { \prime } } q _ { i t s s ^ { \prime } } = 1$ for ∀ s. Each one of these matrix elements represents a probability of transition. We model an individual’s propensity to transition as a function of the textual characteristics and the diversity of the content she reads. Let $\mathbf { X } _ { i t }$ be the vector of such observed variables that affect the state-transition probabilities. The state transitions can also be affected by factors unobservable to the researcher. If we assume that the unobserved part of the propensity to transition is independently and identically distributed of the extreme value type, then we can represent the state-transition probabilities as coming from a multinomial logistic model as

$$
q _ {i t s s ^ {\prime}} = \frac {\exp (\pmb {\rho} _ {s s ^ {\prime}} \pmb {X} _ {i t} + \mu_ {s s ^ {\prime}})}{\sum_ {s ^ {\prime \prime} = 1} ^ {S} \exp (\pmb {\rho} _ {s s ^ {\prime \prime}} \pmb {X} _ {i t} + \mu_ {s s ^ {\prime}})}, \quad \sum_ {s ^ {\prime}} q _ {i t s s ^ {\prime}} = 1.
$$

Here, $\mathbf { p } _ { s s ^ { \prime } }$ is a vector of state-specific parameters, and $\mu _ { s s ^ { \prime } }$ is the current and target-state-specific intercept. Note that the marginal effect of a covariate is not only current- but also target-state-specific. This allows for different impacts of time-varying covariates, depending on the individual’s current and target states.

4.1.2. State-Dependent Reading Outcome. The reading outcome is a vector of count variables. It is likely that the counts across topics for an individual are jointly determined. Since there are k topics, we model their counts as a k-variate negative binomial distribution. The k-variate negative binomial model is also known in literature as the Dirichlet multinomial model. Following Arbous and Kerrich (1951), the joint distribution of the counts conditional on individual’s state is given as

$$
\begin{array}{c} P (\mathbf {N} _ {i t} \mid S _ {i t} = s) = \frac {\Gamma (\alpha + \sum_ {j} N _ {i j t})}{\Gamma (\alpha) \prod_ {j} N _ {i j t} !} \alpha^ {\alpha} \bigg (\frac {1}{\eta_ {i s}} \bigg) ^ {\alpha + \sum_ {j} N _ {i j t}} \\ \cdot \prod_ {j} (\lambda_ {i j s}) ^ {N _ {i j t}} s, \end{array}\tag{1}
$$

with $\begin{array} { r } { \eta _ { i s } = \alpha + \sum _ { j } \lambda _ { i j s } } \end{array}$ . Here, $\alpha > 0$ is the dispersion parameter of the k-variate negative binomial distribution. $\lambda _ { i j s }$ is the parameter for $N _ { i j t } ,$ and following the standard practice in econometrics literature is parameterized as $\lambda _ { i j s } = \exp ( { \cal Z } _ { j t } ^ { \prime } { \bf \vec { \beta } } _ { j } + \kappa _ { j s } + \Psi _ { j t } + \delta _ { i j s t } )$ . Here $\mathbf { Z } _ { j t } ^ { \prime }$ is the vector of covariates that affect the average amount of reading by an individual on topic $j , \mathbf { \boldsymbol { \mathsf { \{ \beta } } }  _ { j }$ is a topic-specific vector of unknown parameters, $\kappa _ { j s }$ the topic and state-specific intercept, $\Psi _ { j t }$ is an unobserved demand shock for topic j at time $t ,$ and $\delta _ { i j s t }$ is the error term that follows a log-gamma distribution and is uncorrelated with $Z _ { j t }$ . Note that we have assumed the coefficients corresponding to $\mathbf { Z } _ { j t }$ to be the same across states to keep the number of parameters to be estimated manageable. As a result, the difference in the reading behavior across states is primarily captured by $\kappa _ { j s } .$

4.1.3. Initial State Distribution. The initial state distribution (Ï) is derived analytically as $\mathbf { \pi } _ { \overline { { { \mathbf { 1 } } } } \overline { { { \mathbf { \Lambda } } } } } = \pi \bar { \Phi } ,$ where ê<sup>¯</sup> is a transition matrix, which is calculated at mean values of covariates (McDonald and Zucchini 1997).

4.1.4. Number of States. The number of states for the dynamic model is determined by comparing the log marginal density for models with a different a number of states.

4.1.5. The Likelihood Function for Observed Reading Outcome. Consider, for individual $i , \ \mathsf { a }$ fixed state sequence $\mathbf { S } ( i ) = S _ { i 1 } , S _ { i 2 } , \ldots , S _ { i T } ,$ , where $S _ { i t }$ is the initial state for individual i and $S _ { i t }$ ∈ $\{ 1 , 2 , \ldots , S \}$ , and an observed outcome sequence $\mathbf { N } ( i ) = N _ { i 1 } , N _ { i 2 } , \ldots , N _ { i T }$ . For convenience, we use the following compact notation, Ë, to represent the complete parameter set of the model. The probability that we observe the outcome sequence N4i5 given the state sequence S4i5 and the parameter set Ë is

$$
P (\mathbf {N} (i) \mid \boldsymbol {\lambda}, \mathbf {S} (i)) = \prod_ {t = 1} ^ {T} P (\mathbf {N} _ {i t} \mid \boldsymbol {\lambda}, S _ {i t}).
$$

The probability of a state sequence $\mathbf { S } ( i )$ is given by

$$
P (\mathbf {S} (i) \mid \boldsymbol {\lambda}) = \pi (S _ {i 1}) q _ {i 1 S _ {i 1} S _ {i 2}} \dots q _ {i 1 S _ {i t} S _ {i t + 1}} \dots q _ {i 1 S _ {i T - 1} S _ {i T}}.
$$

The probability that $\mathbf { N } ( i )$ and $\mathbf { S } ( i )$ occur simultaneously is

$$
P (\mathbf {N} (i), \mathbf {S} (i) \mid \boldsymbol {\lambda}) = P (\mathbf {N} (i) \mid \boldsymbol {\lambda}, \mathbf {S} (i)) P (\mathbf {S} (i) \mid \boldsymbol {\lambda}).\tag{2}
$$

Hence, the probability of the observed outcome sequence N4i5 given the model parameter set Ë is the likelihood of observing this sequence and is obtained by summing Equation (2) over all possible values of state sequence $\bar { \mathbf { S } } ( i )$ (Rabiner 1989):

$$
L (\mathbf {N} (i)) = P (\mathbf {N} (i) \mid \boldsymbol {\lambda}) = \sum_ {\forall \mathbf {S} (i)} P (\mathbf {N} (i), \mathbf {S} (i) \mid \boldsymbol {\lambda}) P (\mathbf {S} (i) \mid \boldsymbol {\lambda}).
$$

4.2. Unobserved Cross-Sectional Heterogeneity Until now, our dynamic model only incorporates inter-temporal heterogeneity. We further introduce cross-sectional (individual-level) heterogeneity in the dynamic model through a hierarchical Bayesian framework. To keep the number of parameters manageable, we allow the intercepts for the reading outcome equations $\left( \kappa _ { j s } \right)$ and the state-transition equations $\left( \mu _ { s s ^ { \prime } } \right)$ to be individual specific. Hence, in our model, $\kappa _ { i j s }$ and $\mu _ { i s s ^ { \prime } }$ 0 are reader-specific random-effects parameters. Observed individual characteristics that may affect the reading levels are introduced into the model in a hierarchical manner.

Let $\mathbf { \theta } _ { i } = \{ \kappa _ { i 1 1 } , \ldots , \kappa _ { i k S } , \mu _ { i 1 1 } , \ldots , \mu _ { i S S } \}$ be the set of individual-specific random-effect parameters. It can be written as a function of observed and unobserved individual characteristics as

$$
\pmb {\theta} _ {i} = \pmb {\tau} ^ {\prime} \mathbf {D} _ {i} + \pmb {\varepsilon} _ {\pmb {\theta} _ {i}},
$$

where $\mathbf { D } _ { i }$ is a vector of individual characteristics for individual $i , \pmb { \tau }$ is a matrix of parameters, relating the individual characteristics to the random effect parameters (È ), and $\mathfrak { \varepsilon _ { \theta _ { i } } } \sim M V N ( \mathbf { 0 } , \mathfrak { L _ { \theta } } )$

## 4.3. Simultaneous Demand and Supply

Our setting can be viewed as a demand-supply situation, where the bloggers produce posts and the readers consume posts. Hence, it is important to account for simultaneity of demand and supply in our setting. The rationale is that the bloggers may set the supply-side variables (volume of posts produced on a topic) by allocating their resources based on their expectations of the reader’s response. If this happens, the variables that we have assumed to be explanatory in the demand model are determined from within the system of study. For example, bloggers may determine how many posts to produce on a topic after taking into account reader preferences and variables that may not be observed by the researcher, which results in an endogenous relationship between supply and demand.

As we are primarily interested in the demandside dynamics, we follow the limited-information approach widely used in the literature to estimate simultaneous demand and supply models. The limited-information approach has been preferred in the literature because it does not require specification of the supply-side relationship (Yang et al. 2003, Villas-Boas and Winer 1999). Instead, it assumes that the observed supply-side variables are stochastic with an error term that is correlated with the demandside error. It is the covariance between the demand and supply errors that causes endogenous relationship. This approach uses instrumentals for predicting endogenous variables. If the instruments are orthogonal to the supply-side errors, the values of predicted supply-side variables can be viewed as exogenous covariates in the demand-side model. Widely used instruments are the lagged values of the variables (Yang et al. 2003, Villas-Boas and Winer 1999).

We consider the volume of posts produced on a topic at time $t ~ ( \mathbf { W } _ { j t } )$ to be endogenous. Note that these variables are topic specific and time specific. For each of these variables, we use two instruments: one period (t − 1) and two period (t − 2) lagged values of the variable for the topic. Let $w _ { j t }$ represent one of the variables from $\mathbf { W } _ { j t }$ . Then, we specify the supply equation as follows:

$$
w _ {j t} = \omega_ {0} + \omega_ {1} w _ {j t - 1} + \omega_ {2} w _ {j t - 2} + \xi_ {j t}.
$$

Similarly, we can express the equation for $\mathbf { W } _ { j t }$ in matrix form as

$$
\mathbf {W} _ {j t} = \mathbf {V} _ {t} \boldsymbol {\omega} + \boldsymbol {\xi} _ {j t}.
$$

The variance covariance between the demand common shock and the supply equation error is given as

$$
\operatorname{cov} \binom{\boldsymbol {\Psi} _ {j t}}{\boldsymbol {\xi} _ {j t}} = \left( \begin{array}{c c} \Sigma_ {d} & \Sigma_ {d z} ^ {\prime} \\ \Sigma_ {d z} & \Sigma_ {z} \end{array} \right).
$$

Here $\Sigma _ { d z }$ captures the correlation between supply error and demand shock and will not be zero if endogeneity is present. We conduct tests for the validity and strengths of all the instrumental variables.

## 5. Data, Variable Construction, and Descriptive Statistics

Data for our analysis come from three archival sources of the firm. First, the blog post database contains complete details about blog posts. In this database, each blog and each post are uniquely identified. It also contains blogger ID, post content, posting date, and comments made on the post. Second, the blog reading database contains who read what post at what time. We have access to this information from January 1, 2007 to October 31, 2008. Third, the human resource database contains information on employee demographics (gender and country), position in the organization, and employee department within the organization. Note that the firm identifies bloggers and readers by their unique employee IDs.

These three sources give us rich information over a period of 22 months. Approximately 71,000 posts were written during this period. On average each post was 300 words long. There were approximately 286,000 comments (on average 33 words long) posted by readers to these posts, indicating a healthy user involvement. We randomly selected 1,200 unique readers and split them into two data sets: 1,000 readers in a calibration data set and 200 readers for test data set. The calibration data set has approximately 74% males, 9% high status, 25% middle status, 59% Asians, 19% North Americans, and 67% technical readers. There are a total of approximately 38,000 post readings by these 1,000 employees during the 22-month period.

## 5.1. Variable Construction

5.1.1. Post Classification Into Topics. The blog reading behavior of an employee is modeled using the number of posts she reads on different topics. There are a number of ways to determine the topic of the post. In this particular data set, blog articles are assigned to one of the four topics by the firm (WTK, WMK, NWE, NWK). However, this provides a very coarse classification, and any user-defined misclassification would not be corrected. Another way to determine the topics of the articles is to analyze the key words that occur in the article using a topic-modeling approach. One of the most popular topic-modeling approaches is latent Dirichlet allocation (LDA) (Blei et al. 2003). It is an unsupervised method to generate a predefined number of topics from a set of documents. Each topic can be described by weight distribution over the key words that occur in the document set. In addition, using this topic model, each document can be associated to each of the generated topics with certain probability.

This unsupervised approach was used to determine the topics for each of the posts in our data set. We used the LDA implementation in the MALLET (Machine Learning for Language Toolkit) package to generate 10 different topics (Blei et al. 2002).<sup>1</sup> For each topic, the top 10 key words are shown in Table 1. Each document was assigned to the most probable topic. Just looking at the top 10 key words for each topic, we notice that the first two topics (1 and 2) are clearly work related and the last 7 (4–10) are clearly nonwork-related. Topic 3 turns out to be a mixture of work-related and nonwork-related posts. These results indicate there is much higher variation in the nonwork-related content than the work-related content. The dependent variable modeled is created from these assigned topics by counting the number of articles an employee reads in each such generated topic in a month.

We constructed three sets of variables based on our discussion in §3.

Reading set. These are the variables that affect the amount of posts read in each period per category. It corresponds to the matrix Z.

State-transition set. These include variables that affect the state-transition probabilities. The statetransition set corresponds to matrix X.

Reader characteristic set. These variables constitute reader characteristics that are used to account for reader-specific heterogeneities for both the amount of reading and state transitions. This corresponds to matrix D.

Table 1 Top 10 Key words for a Topic

<table><tr><td>Topic</td><td>Keywords</td></tr><tr><td>1</td><td>Project, business, company, team, software, testing, feedback, work, management.</td></tr><tr><td>2</td><td>Data, code, design, system, http, file, click, sql, Java, application.</td></tr><tr><td>3</td><td>Company name, post, blog, read, time, knowledge, people, organization, write, book.</td></tr><tr><td>4</td><td>Life, people, social, person, success, good, things, motivation, time, work.</td></tr><tr><td>5</td><td>Man, love, asked, day, father, boy, girl, wife, friend, home.</td></tr><tr><td>6</td><td>Water, body, food, day, eat, blood, heart, brain, fat, time.</td></tr><tr><td>7</td><td>God, world, light, earth, years, sun, place, lord, soul, tree.</td></tr><tr><td>8</td><td>Day, time, started, back, night, dream, friend, guy, hour.</td></tr><tr><td>9</td><td>Car, man, road, phone, sir, police, money, back, news, doctor.</td></tr><tr><td>10</td><td>India, team, movie, country, world, music, game, cricket, film, play.</td></tr></table>

5.1.2. Reading Set. Reading Set Main Variables. We use text-mining techniques to calculate measures for post quality in terms of readability, comprehensiveness, grammatical errors, and sentiment (negativity and controversy). The post-textual characteristics are calculated for each post and then averaged across all posts on the topic in a given month. For more details on each of these measures, please see the appendix to this paper (available as supplemental material at http://dx.doi.org/10.1287/isre.2013.0509).

Quality of language in the blog post. Readability is measured as the Flesch Reading Ease Score, which has a range of 0–100, with 0 meaning very hard and 100 meaning very easy to read (Kincaid et al. 1975).

Comprehensiveness is measured as the number of sentences in the text of a post—generally longer texts contain more information and thus are expected to be more comprehensive (Lu et al. 2013).

Grammatical error of the blog post is measured as the number of grammatical errors in the text of a post using the link grammar parser on each sentence of the post (Grinberg et al. 1995).

Sentiment quality of the blog post. Negativity of a post is one if the post has negative sentiment else zero. Sentiments expressed in the posts are classified as positive or negative using a Bayesian classifier (Clement and Sharp 2003) that is trained over word n-grams of order 5. The order was selected using cross-validation over a sentiment classification data set (Pang and Lee 2004). Our classifier was initially trained over this data set and then recalibrated using relevance feedback from the blog data set.

Controversialness of a post is calculated as the standard deviation of the sentiments in the reader comments to the post. A controversy of zero indicates that the sentiment in readers’ comments on the post is undivided, and its value away from zero indicates higher division in reader opinion.

Reading Set Control Variables. Volume of Posts and Status of Blogger. Besides our main variables, there are two important factors that may affect the magnitude of reading on a topic. The first is the volume of posts written on the topic. The second is the status of the blogger who writes a post. It is obvious why the volume of posts would affect the magnitude of reading on a topic. Hence, we briefly explain here why status of a blogger would matter. Status of the blogger who is disseminating information by writing articles can have an impact on whether an article is read. It has been argued that the employees with higher statuses in the organization have greater access to information, since they act as aggregators of information from the employees directly under them in the organizational hierarchy (Feld 1959, Greve 2005). Therefore, employees seeking greater access to information would read articles written by those with higher status in the organization. However, as roles become more specialized, essential skills and knowledge of the company is seen to reside within individual employees in the company and not necessarily at the upper echelon of the organization hierarchy (Grant 1996). In a software services company (our research site), such essential knowledge resides in the employees with technical roles, as opposed to in the upper management. Therefore, when such employees write technical articles they would be expected to have higher readership than technical articles written by employees in nontechnical roles including high-level managers.

To control for the blogger status and the volume of posts on a topic, we construct three measures: High-Post, MiddlePost, and LowPost. We first classify the status of an individual as high, middle, or low based on her rank in the organization. For example, a representative high status individual in our study would be at the rank of a chief or a VP, whereas a middle status would be at the rank of a senior manager, and the low status would be at the rank of a developer. We then construct variables HighPost, MiddlePost, and LowPost, which indicate the number of posts written by high, middle, and low status employees in the current period, respectively.

5.1.3. State-Transition Set. Inherent Desire for Variety. The variety seeking behavior can be observed at two levels—across periods and within period. If an individual switches from reading on one set of topics in one period to reading on another set of topics in the next period, then it represents the across period (inter-temporal) variety seeking behavior. This behavior is captured by off-diagonal state transition probabilities. If individuals were completely inertial then the off diagonal elements in the state transition matrix would be zero.

In comparison, an individual could also satisfy her desire for variety by reading across a number of topics within one period. This reading on diverse topics in a period can potentially moderate the inter-temporal variety seeking behavior. This is because the expected inter-temporal variety that one could get from switching for one state to another would decrease with the diversity of topics she reads in the current period. To capture this effect, we construct a variable, diversity, to capture the variety of content consumed by the reader in a period. We employ the Shannon diversity index to measure variety in content consumption by an individual. Let $p _ { i j t }$ represent the proportion of posts read by individual i in a period t that belong to topic j. Then the diversity (Shannon diversity) of content consumption by the reader is

$$
D i v e r s i t y _ {i t} = - \sum_ {j} p _ {i j t} \log (p _ {i j t}).
$$

When an individual reads an equal proportion of posts across topics, the value of $D i v e r s i t y _ { i t }$ is equal to log4k5. As the individual’s reading becomes focused on a few topics, the value of $D i v e r s i t y _ { i t }$ becomes smaller.

Quality of language and sentiment of blog posts. The variables representing the quality of language and sentiment are similar to the reading set variables (readability, comprehensiveness, grammatical error, negativity, and controversialness). However, in this case they are constructed from posts that employees read in the current period. Note that the variables in the statetransitions set are calculated at reader-month level.

5.1.4. Reader Characteristics Set. To control for reader-specific heterogeneity, we include several reader characteristics. We control for status-specific effects by including two indicator variables representing high status (HighS) and middle status (MiddleS)

reader. Further, to account for differences that may exist among employees with technical expertise and others, we use a binary variable (Tech), which equals one if an employee is from a technical department and zero otherwise. We include an indicator variable Asia (NAmerica), which equals one when the reader is from Asia (North America) and zero otherwise. Further, to account for gender-specific effects, we construct an indicator variable, Gender, which equals one for male and zero otherwise.

## 5.2. Descriptive Statistics

Tables 2 and 3 provide descriptive statistics of reading set and state transition set variables. On average, the mean readability is at a moderate level, ranging from a low of 46.74 for topic 1 to 58.46 for topic 2. On average, topic 9 has the shortest posts (23.08 sentences), and topic 7 has the longest posts (60.14 sentences). Topics 1 and 2 have on average more grammatical errors than other topics. On average, a very small number of posts display negative sentiment across topics, and posts are moderately controversial across topics. Table 3 highlights some interesting statistics. By comparing average negativity and controversialness of posts shown in Table 3 with the corresponding values in Table 2, one can notice that readers are more attracted to negative and controversial posts. The mean value of variety is 0.74, indicating that individuals on average read a variety of topics rather than focusing on only one. The values of the other characteristics are on average similar in Tables 2 and 3.

Table 2 Descriptive Statics for the Reading Set Variables

<table><tr><td>Topics</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td></td><td>Mean</td><td>Mean</td><td>Mean</td><td>Mean</td><td>Mean</td><td>Mean</td><td>Mean</td><td>Mean</td><td>Mean</td><td>Mean</td></tr><tr><td>Variables</td><td>Variance</td><td>Variance</td><td>Variance</td><td>Variance</td><td>Variance</td><td>Variance</td><td>Variance</td><td>Variance</td><td>Variance</td><td>Variance</td></tr><tr><td rowspan="2">Readability</td><td>46.74</td><td>58.46</td><td>47.99</td><td>51.13</td><td>49.30</td><td>45.61</td><td>53.46</td><td>52.81</td><td>47.24</td><td>53.01</td></tr><tr><td>13.81</td><td>21.81</td><td>20.70</td><td>16.31</td><td>12.48</td><td>15.67</td><td>16.53</td><td>17.83</td><td>16.22</td><td>18.33</td></tr><tr><td rowspan="2">Comprehensiveness</td><td>24.76</td><td>35.51</td><td>45.20</td><td>43.62</td><td>35.01</td><td>34.29</td><td>60.14</td><td>40.81</td><td>23.08</td><td>31.81</td></tr><tr><td>15.24</td><td>12.15</td><td>16.23</td><td>17.03</td><td>17.57</td><td>12.93</td><td>16.35</td><td>15.30</td><td>17.48</td><td>16.61</td></tr><tr><td rowspan="2">Grammatical Error</td><td>3.60</td><td>3.74</td><td>2.16</td><td>1.75</td><td>1.73</td><td>1.58</td><td>1.52</td><td>2.33</td><td>1.66</td><td>2.09</td></tr><tr><td>2.64</td><td>2.44</td><td>2.53</td><td>3.64</td><td>1.45</td><td>3.82</td><td>1.41</td><td>2.18</td><td>1.69</td><td>2.48</td></tr><tr><td rowspan="2">Negativity</td><td>0.15</td><td>0.10</td><td>0.15</td><td>0.15</td><td>0.01</td><td>0.05</td><td>0.05</td><td>0.14</td><td>0.19</td><td>0.10</td></tr><tr><td>0.13</td><td>0.11</td><td>0.02</td><td>0.10</td><td>0.03</td><td>0.17</td><td>0.08</td><td>0.18</td><td>0.05</td><td>0.12</td></tr><tr><td rowspan="2">Controversialness</td><td>0.24</td><td>0.31</td><td>0.19</td><td>0.23</td><td>0.24</td><td>0.22</td><td>0.18</td><td>0.24</td><td>0.21</td><td>0.22</td></tr><tr><td>0.12</td><td>0.09</td><td>0.11</td><td>0.09</td><td>0.13</td><td>0.13</td><td>0.11</td><td>0.09</td><td>0.10</td><td>0.04</td></tr><tr><td rowspan="2">HighPost</td><td>42.95</td><td>36.10</td><td>39.18</td><td>36.81</td><td>39.14</td><td>36.39</td><td>36.63</td><td>41.47</td><td>41.23</td><td>41.25</td></tr><tr><td>19.01</td><td>13.38</td><td>19.15</td><td>21.89</td><td>18.47</td><td>20.10</td><td>19.18</td><td>16.09</td><td>17.88</td><td>14.64</td></tr><tr><td rowspan="2">MiddlePost</td><td>82.11</td><td>65.82</td><td>66.45</td><td>68.52</td><td>51.45</td><td>86.51</td><td>77.60</td><td>68.96</td><td>85.96</td><td>61.31</td></tr><tr><td>28.95</td><td>35.54</td><td>26.50</td><td>27.21</td><td>34.95</td><td>45.73</td><td>29.61</td><td>37.60</td><td>33.42</td><td>42.82</td></tr><tr><td rowspan="2">LowPost</td><td>225.55</td><td>264.25</td><td>163.56</td><td>188.58</td><td>145.52</td><td>172.54</td><td>175.03</td><td>155.61</td><td>163.88</td><td>139.01</td></tr><tr><td>45.82</td><td>55.84</td><td>60.78</td><td>75.68</td><td>49.66</td><td>56.50</td><td>54.34</td><td>39.54</td><td>51.49</td><td>40.64</td></tr></table>

Table 3 Descriptive Statistics of State-Transition Set Variables

<table><tr><td>Variables</td><td>Mean</td><td>Variance</td></tr><tr><td>Readability</td><td>53.01</td><td>24.19</td></tr><tr><td>Comprehensiveness</td><td>39.79</td><td>23.92</td></tr><tr><td>Grammatical Error</td><td>1.89</td><td>2.87</td></tr><tr><td>Negativity</td><td>0.24</td><td>0.10</td></tr><tr><td>Controversialness</td><td>0.38</td><td>0.16</td></tr><tr><td>Diversity</td><td>0.74</td><td>0.22</td></tr></table>

## 6. Estimation, Model Selection Criterion, and Model Comparison

## 6.1. Estimation Procedure

The model is estimated using a standard Markov chain Monte Carlo (MCMC) hierarchical Bayes estimation procedure, using a Gibbs Sampler, and the Metropolis-Hastings algorithm coded in Matlab. To reduce the autocorrelation between draws of the Metropolis-Hastings algorithm and to improve the mixing of the MCMC procedure, we used an adaptive Metropolis-adjusted Langevin algorithm (Atchade 2006). In the hierarchical Bayes procedure for the dynamic model, the first 100,000 observations were used as burn-in, and the last 25,000 were used to calculate the conditional posterior distributions. Convergence is assessed by inspecting the time series of draws (Gelman and Rubin 1992). The full estimation procedure is provided in the appendix to this paper.

## 6.2. Model Selection Criterion

The number of states for the dynamic model is determined by comparing the log-marginal density for models with different number of states (up to six states). The log-marginal density is calculated as the harmonic mean of individual log likelihood across iterations (Newton and Raftery 1994). The dynamic model with five states outperforms all other models on the log-marginal density criterion. As the dynamic model with five states explains the data best, we will only discuss results from this model.

## 6.3. Comparison with Alternative Model Specifications

We also compare our model with alternative specifications in terms of out-of-sample predictive power. To evaluate the predictive power of a model, we used the estimated results to predict, in the holdout sample, the amount of reading in each topic in each month. We construct two additional models as baseline models for comparison. The first model is a static model that neither allows for cross-sectional nor inter-temporal unobserved heterogeneity. In this specification, we only model the amount of reading across topics as a function of reading set variables. The second model is a variation of our dynamic model. In this model, we do not allow for unobserved cross-sectional heterogeneity. Everything else is the same. For all three models, we calculated the root mean square prediction error (RMSPE), which is given in Table 4. As is clear from the results, the outof-sample predictive ability of our dynamic model is superior to both the static model and the dynamic model that does not account for cross-sectional unobserved heterogeneity.

Table 4 Model Predictive Power Comparison

<table><tr><td>Models of reading behavior</td><td>Number of states</td><td>RMSPE (%)</td></tr><tr><td>Static model</td><td>1</td><td>39.4</td></tr><tr><td>Dynamic model without cross-sectional unobserved heterogeneity</td><td>4</td><td>21.9</td></tr><tr><td>Dynamic model with cross-sectional unobserved heterogeneity</td><td>5</td><td>12.7</td></tr></table>

## 7. Results and Discussions

We performed several preliminary checks on the data. Initial investigations revealed that the post-textual characteristics and their squares were highly correlated, which raised concerns of multicollinearity. To reduce the correlations, we standardized the posttextual characteristics, which reduced the correlations to an acceptable level. The variance inflation factor (VIF) for the transformed data is less than two, which ensures that multicollinearity is no more a problem. We also standardized HighPost, MiddlePost, and Low-Post to allow easier interpretation of their effects.

The limited information approach requires the proposed instruments to be conditionally independent of the dependent variable and that the instruments have some explanatory power on the endogenous variables. Sargan (1958) proposed an overidentification test to check that the instruments are exogenous. We followed Sargan (1958) and regressed the residuals for each topic from the reading outcome model on all the exogenous variables for that topic. Under the null hypothesis that all instrumental variables are uncorrelated with the reading outcome (demand) error, $n R ^ { 2 }$ is distributed as $\chi _ { q } ^ { 2 } ,$ , where $q$ is the number of instrumental variables from outside the model minus the total number of endogenous explanatory variables and n is the number of observations. If the test statistic exceeds the critical value we reject the null hypothesis and conclude that at least some of the instrumental variables are not exogenous. The results indicate that we cannot reject the null as the test statistic is significantly below the critical values for all the cases. Stock and Yogo (2005) proposed a weak-instrument test to check that the instruments have power in explaining the endogenous variables to the case of linear regression models with multiple endogenous variables.

To the best of our knowledge, there is no weak identification test for the instrumental variable regression for nonlinear models such as ours. Several studies that involve nonlinear models have applied the Stock and Yogo (2005) to test for weak identification. We conducted two tests to identify whether our instruments are weak. First, when we regress the endogenous variables on the instruments we find that the instruments significantly predict (all $p < 0 . 0 1 )$ the corresponding endogenous variables. These results were also supported by the corresponding F statistics calculated by estimating the endogenous variables with and without the corresponding instruments. Second, for each of our instruments the Stock and Yogo (2005) test rejects the hypothesis that the quality of the instruments is below the highest level at the 5% significance level. Therefore, weak instruments do not appear to be a concern. We also find significant correlations between the demand and supply shocks, indicating the presence of endogeneity.

## 7.1. Reading Set Effects

Table 5 presents results from the hierarchical Bayesian estimation of the reading outcome parameters. Although we estimated the individual, topic, and state-specific intercepts $\left( \kappa _ { i j s } \right) .$ , we report only the parameters that do not change across states and individuals $( \beta _ { j } )$ because of space limitations. Contrary to what we argued, the parameters in Table 5 indicate that the variables that represent the quality of the language of the post (readability, comprehensiveness, and grammatical error) have no significant impact on the readership of any topic. In contrast, the variables that represent the sentiment of the post (negativity and controversialness) have a significant impact on the readerships for all topics. Before we interpret the effects, please note that all variables are standardized. As we argued, negativity has a curvilinear impact on the readership across topics. The amount of reading on a topic is low when negativity is at extreme values (very high or very low) and high when it lies in between. Readers are more likely to read on topics that have moderate amounts of negative posts, but not excessively or negligibly negative posts. Further, as argued in §2, controversialness has a positive linear effect across topics. The amount of reading on a topic increases with thecontroversialness of posts on that topic. A potential reason why sentiment of the posts on a topic impacts readership but the quality of the language of the post does not is that the sentiment appeals to the emotions of the readers, and they are more likely to discuss such posts with their peers, attracting them to read the posts. In contrast, the quality of the language of the posts does not appeal to the emotions of the readers and hence is less likely to be discussed with others. As a result, an individual would get to know these characteristics only after reading the posts themselves.

The number of posts on a topic positively affects the amount of posts read on the topic as indicated by positive and significant coefficients for Highpost, Middlepost, and Lowpost across all topics. When comparing the coefficients for high, middle, and low posts for a topic, we find only Highpost and Lowpost coefficients are statistically significantly different from each other for only topics 1 and 2. This indicates that workrelated posts by low-status employees attract more readers, and for nonwork-related posts, blogger status does not have a significant effect on attracting readers.

Table 5 Hierarchical Bayesian Parameter Estimates of Dynamic Model of Reading Behavior [Reading Outcome Parameters 4 5]<sup>†</sup>

<table><tr><td rowspan="2"></td><td colspan="10">Topic</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td colspan="11">Post characteristics</td></tr><tr><td>Readability</td><td>0.21</td><td>0.36</td><td>0.29</td><td>0.54</td><td>0.47</td><td>0.27</td><td>0.19</td><td>0.34</td><td>0.17</td><td>0.47</td></tr><tr><td> $Readability^2$ </td><td>-0.03</td><td>0.07</td><td>0.21</td><td>0.07</td><td>0.11</td><td>0.09</td><td>0.06</td><td>0.12</td><td>0.32</td><td>0.19</td></tr><tr><td>Comprehensiveness</td><td>0.29</td><td>0.11</td><td>0.47</td><td>0.39</td><td>0.29</td><td>-0.06</td><td>0.04</td><td>0.19</td><td>-0.04</td><td>0.14</td></tr><tr><td> $Comprehensiveness^2$ </td><td>0.01</td><td>0.05</td><td>0.13</td><td>0.28</td><td>0.06</td><td>-0.03</td><td>-0.02</td><td>-0.21</td><td>0.21</td><td>0.07</td></tr><tr><td>Grammatical error</td><td>0.03</td><td>-0.07</td><td>-0.12</td><td>-0.03</td><td>-0.05</td><td>-0.01</td><td>0.02</td><td>-0.09</td><td>-0.13</td><td>-0.26</td></tr><tr><td> $Grammatical error^2$ </td><td>0.01</td><td>0.04</td><td>-0.04</td><td>-0.01</td><td>-0.06</td><td>-0.01</td><td>-0.07</td><td>-0.11</td><td>-0.05</td><td>-0.16</td></tr><tr><td>Negativity</td><td>-0.22*</td><td>0.16*</td><td>-0.04</td><td>0.11</td><td>0.18*</td><td>-0.38**</td><td>-0.66**</td><td>-0.39**</td><td>-0.73**</td><td>-0.46**</td></tr><tr><td> $Negativity^2$ </td><td>-1.87**</td><td>-0.79**</td><td>-0.49**</td><td>-0.63**</td><td>-0.94**</td><td>-1.91**</td><td>-0.93**</td><td>-1.08**</td><td>-1.31**</td><td>-1.59**</td></tr><tr><td>Controversialness</td><td>1.34**</td><td>1.98**</td><td>1.87**</td><td>0.94**</td><td>0.77**</td><td>0.85**</td><td>1.21**</td><td>1.29**</td><td>0.74*</td><td>1.63**</td></tr><tr><td> $Controversialness^2$ </td><td>0.07</td><td>0.13</td><td>0.26</td><td>0.18</td><td>0.09</td><td>0.04</td><td>0.13</td><td>0.18</td><td>0.11</td><td>0.32</td></tr><tr><td colspan="11">Blogger characteristics</td></tr><tr><td>High post</td><td>0.25*</td><td>0.24*</td><td>0.89**</td><td>0.96**</td><td>0.81**</td><td>0.74**</td><td>0.57**</td><td>0.71**</td><td>1.05**</td><td>0.96**</td></tr><tr><td>Middle post</td><td>0.93**</td><td>0.57**</td><td>0.94**</td><td>1.17**</td><td>0.42*</td><td>0.56**</td><td>0.38*</td><td>0.52**</td><td>0.73**</td><td>0.63*</td></tr><tr><td>Low post</td><td>1.76**</td><td>2.04**</td><td>0.51**</td><td>0.69**</td><td>0.48**</td><td>0.39*</td><td>0.45**</td><td>0.49**</td><td>0.58**</td><td>0.74**</td></tr></table>

<sup>∗</sup>The 95% confidence interval does not include zero.  
<sup>∗∗</sup>The 99% confidence interval does not include zero.  
<sup>†</sup>Reader-specific random effects parameters (reading outcome intercepts) and the effect of reader-specific demographic variables that explain these intercepts though included in estimation are not reported here to conserve space.

Table 6 Mean Amount of Reading on a Topic in Each State

<table><tr><td rowspan="2"></td><td colspan="11">Topic</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>Total</td></tr><tr><td>State 1</td><td>0.28</td><td>0.38</td><td>0.35</td><td>4.10</td><td>4.62</td><td>1.75</td><td>4.39</td><td>7.03</td><td>0.60</td><td>0.15</td><td>23.65</td></tr><tr><td>State 2</td><td>0.14</td><td>0.13</td><td>1.27</td><td>0.14</td><td>0.11</td><td>5.42</td><td>0.78</td><td>4.90</td><td>7.10</td><td>7.69</td><td>27.68</td></tr><tr><td>State 3</td><td>4.85</td><td>5.81</td><td>2.75</td><td>0.05</td><td>1.16</td><td>0.09</td><td>0.58</td><td>0.05</td><td>1.21</td><td>1.60</td><td>18.16</td></tr><tr><td>State 4</td><td>6.63</td><td>3.66</td><td>1.81</td><td>2.34</td><td>1.15</td><td>0.06</td><td>0.52</td><td>0.01</td><td>0.30</td><td>0.25</td><td>16.72</td></tr><tr><td>State 5</td><td>0.08</td><td>0.07</td><td>0.09</td><td>0.08</td><td>0.06</td><td>0.05</td><td>0.09</td><td>0.05</td><td>0.06</td><td>0.08</td><td>0.76</td></tr></table>

In Table 6, we present the mean amount of reading in each topic in each state. The five states differ in their amount of reading on each topic. The average amount of posts read in each state is also reported in the table. We find that in states 1, 2, and 5 very little work-related topics are read. Reading in states 1 and 2 is predominantly focused on nonwork-related topics. State 5 appears to represent a dormant state where the reader does not read a lot on any topic but samples from every topic. However, significant amount of work posts are read in states 3 and 4.

## 7.2. State-Transition Set Effects

The state-transition effects are easier to interpret when presented in the form of transition probabilities. Hence, we present all the state-transition set effects in the form of transition matrices and discuss how changes in the state-transition set variables induce change in the state-transition probabilities. The probabilities in this subsection are all calculated using only the statistically significant parameters $( \rho _ { s s ^ { \prime } }$ and $\mu _ { i s s ^ { \prime } } )$ . This means we only report statistically significant transition probabilities. The parameters for the state-transition set are also reported in the appendix to this paper.

Let us start by examining the baseline transition probability matrix (Table 7(A)). These are the transition probabilities for a low status, nontechnical employee from Asia, who has read posts that were at the mean level of readability, grammatical error, comprehensiveness, negativity, controversy, and diversity. This transition matrix is very revealing. The values across the diagonal represent the stickiness (how likely is the reader to continue in the same state) of the states. Table 7(A) shows that state 5 is the stickiest, followed by $4 , 1 , 3 ,$ and 2. The substantial and significant nondiagonal transition probabilities highlight a varietyseeking behavior of blog readers. A reader frequently switches from reading one set of topics to another. Over the timeline of the study, a reader would switch several times from one state to another. More interestingly, state 5, which represents dormant reader behavior, appears to be the most likely state where a reader may move when she moves out of states 1 to 4.

Table 7(A) Baseline Transition Probabilities

<table><tr><td> $t \setminus t + 1$ </td><td>1 (%)</td><td>2 (%)</td><td>3 (%)</td><td>4 (%)</td><td>5 (%)</td></tr><tr><td>1</td><td>73.0</td><td>4.6</td><td>2.2</td><td>2.7</td><td>17.6</td></tr><tr><td>2</td><td>9.1</td><td>64.7</td><td>4.2</td><td>2.4</td><td>19.5</td></tr><tr><td>3</td><td>2.8</td><td>3.9</td><td>64.9</td><td>8.5</td><td>19.9</td></tr><tr><td>4</td><td>5.4</td><td>5.2</td><td>6.2</td><td>74.4</td><td>8.8</td></tr><tr><td>5</td><td>6.8</td><td>6.3</td><td>4.3</td><td>5.5</td><td>77.1</td></tr></table>

Next, let us consider the effect of the readingspecific variables in the state-transition set on the transition probabilities. Because we incorporate both linear and quadratic terms for each variable to test for curvilinear effects, we report the probabilities when the focal variable is one standard deviation below the mean value, and in the parenthesis we also report the probabilities when the focal variable is one standard deviation above the mean value. In all tables in this subsection, all the settings, other than the focal variable, are the same as those of Table 7(A) to facilitate easier comparison.

Table 7(B) presents the transition probabilities with the same setting as in Table 7(A) (baseline probability) but with readings in time t having one standard deviation lower (higher) diversity than the mean value. Let us compare the probabilities along the diagonals of Tables $\bar { 7 } ( \mathrm { A } )$ and 7(B). When the reading is at mean value of diversity, the probability to stay in state 1 is 73%; when it is at one standard deviation below the mean value $( \mathrm { i . e . , }$ the reading is focused on very few topics), the probability to stay in state 1 is 48.9%; when it is one standard deviation above the mean value (i.e., reading is almost equally distributed over all the topics), the probability to stay in state 1 is 91.2%. This indicates that the probability to stay in state 1 increases as the diversity in the content read by the reader in a period increases. A similar pattern is observed for all other states (except state 5, where diversity has no significant impact). This indicates that diversity in reading within period negatively moderates the inter-temporal variety seeking behavior.

Table 7(C) shows the effect of readability on the state transitions. Readers are sensitive to the readability of posts. As argued, readability has a curvilinear relationship with state-transition probabilities. For states 1–4, a moderate level of readability of posts is best for increasing stickiness of the state, and stickiness decreases as readability moves to very low or very high levels. In contrast, stickiness of state 5 increases when readability moves to very high or very low values. Note that state 5 represents dormant behavior where a reader does not read much. When readability is at a moderate level, the reader would be more satisfied with the content, increase her amount of reading, and as a result switch to a more active state. In comparison, when readability is very high or very low, the reader would be dissatisfied with the content, not increase her reading, and stay in the dormant state. Further, posts that are harder or too easy to read increase the likelihood of readers moving to the dormant state.

Table 7(B) Transition Probabilities for One Standard Deviation Below (Above) Mean Diversity

<table><tr><td> $t \setminus t + 1$ </td><td colspan="2">1 (%)</td><td colspan="2">2 (%)</td><td colspan="2">3 (%)</td><td colspan="2">4 (%)</td><td colspan="2">5 (%)</td></tr><tr><td>1</td><td>48.9</td><td>(91.2)</td><td>9.4</td><td>(1.9)</td><td>4.4</td><td>(0.9)</td><td>5.5</td><td>(1.1)</td><td>31.8</td><td>(5.0)</td></tr><tr><td>2</td><td>14.2</td><td>(4.5)</td><td>38.6</td><td>(84.1)</td><td>6.6</td><td>(2.1)</td><td>3.8</td><td>(1.2)</td><td>36.8</td><td>(8.0)</td></tr><tr><td>3</td><td>3.2</td><td>(2.3)</td><td>4.5</td><td>(3.2)</td><td>54.2</td><td>(74.0)</td><td>9.8</td><td>(7.1)</td><td>28.3</td><td>(13.4)</td></tr><tr><td>4</td><td>8.4</td><td>(3.1)</td><td>8.0</td><td>(2.9)</td><td>9.6</td><td>(3.5)</td><td>56.0</td><td>(86.7)</td><td>18.1</td><td>(3.7)</td></tr><tr><td>5</td><td>6.8</td><td>(6.8)</td><td>6.3</td><td>(6.3)</td><td>4.3</td><td>(4.3)</td><td>5.5</td><td>(5.5)</td><td>77.1</td><td>(77.1)</td></tr></table>

Table 7(C) Transition Probabilities for One Standard Deviation Below (Above) Mean Readability

<table><tr><td> $t \setminus t + 1$ </td><td colspan="2">1 (%)</td><td colspan="2">2 (%)</td><td colspan="2">3 (%)</td><td colspan="2">4 (%)</td><td colspan="2">5 (%)</td></tr><tr><td>1</td><td>54.5</td><td>(67.2)</td><td>7.4</td><td>(6.0)</td><td>3.5</td><td>(2.8)</td><td>4.3</td><td>(3.5)</td><td>30.2</td><td>(20.4)</td></tr><tr><td>2</td><td>13.4</td><td>(11.3)</td><td>43.2</td><td>(52.1)</td><td>6.2</td><td>(5.2)</td><td>3.6</td><td>(3.0)</td><td>33.6</td><td>(28.3)</td></tr><tr><td>3</td><td>3.1</td><td>(2.9)</td><td>4.3</td><td>(4.0)</td><td>59.0</td><td>(63.6)</td><td>9.5</td><td>(8.9)</td><td>24.2</td><td>(20.6)</td></tr><tr><td>4</td><td>9.2</td><td>(6.4)</td><td>8.7</td><td>(6.1)</td><td>10.6</td><td>(7.4)</td><td>47.8</td><td>(68.4)</td><td>23.7</td><td>(11.8)</td></tr><tr><td>5</td><td>3.5</td><td>(6.0)</td><td>3.3</td><td>(5.6)</td><td>2.2</td><td>(3.8)</td><td>2.9</td><td>(4.9)</td><td>88.1</td><td>(79.6)</td></tr></table>

Table 7(D) Transition Probabilities for One Standard Deviation Below (Above) Mean Comprehensiveness

<table><tr><td> $t \setminus t + 1$ </td><td colspan="2">1 (%)</td><td colspan="2">2 (%)</td><td colspan="2">3 (%)</td><td colspan="2">4 (%)</td><td colspan="2">5 (%)</td></tr><tr><td>1</td><td>64.3</td><td>(64.3)</td><td>6.0</td><td>(6.0)</td><td>2.8</td><td>(2.8)</td><td>3.5</td><td>(3.5)</td><td>23.4</td><td>(23.4)</td></tr><tr><td>2</td><td>12.0</td><td>(11.9)</td><td>44.5</td><td>(51.8)</td><td>5.6</td><td>(5.5)</td><td>3.2</td><td>(3.2)</td><td>34.7</td><td>(27.6)</td></tr><tr><td>3</td><td>3.1</td><td>(3.3)</td><td>4.4</td><td>(4.6)</td><td>46.2</td><td>(56.3)</td><td>9.6</td><td>(10.2)</td><td>36.7</td><td>(25.6)</td></tr><tr><td>4</td><td>7.3</td><td>(6.7)</td><td>7.0</td><td>(6.4)</td><td>8.4</td><td>(7.7)</td><td>61.2</td><td>(67.0)</td><td>16.0</td><td>(12.2)</td></tr><tr><td>5</td><td>6.8</td><td>(6.8)</td><td>6.3</td><td>(6.3)</td><td>4.3</td><td>(4.3)</td><td>5.5</td><td>(5.5)</td><td>77.1</td><td>(77.1)</td></tr></table>

Table 7(E) Transition Probabilities for One Standard Deviation Below (Above) Mean Grammatical Errors

<table><tr><td> $t \setminus t + 1$ </td><td colspan="2">1 (%)</td><td colspan="2">2 (%)</td><td colspan="2">3 (%)</td><td colspan="2">4 (%)</td><td colspan="2">5 (%)</td></tr><tr><td>1</td><td>84.7</td><td>(64.1)</td><td>3.6</td><td>(4.8)</td><td>1.9</td><td>(2.5)</td><td>2.3</td><td>(3.1)</td><td>7.5</td><td>(25.5)</td></tr><tr><td>2</td><td>5.7</td><td>(9.0)</td><td>81.9</td><td>(41.9)</td><td>3.1</td><td>(4.8)</td><td>1.8</td><td>(2.8)</td><td>7.5</td><td>(41.5)</td></tr><tr><td>3</td><td>2.8</td><td>(2.6)</td><td>4.0</td><td>(3.6)</td><td>70.6</td><td>(58.8)</td><td>8.7</td><td>(7.9)</td><td>13.8</td><td>(27.2)</td></tr><tr><td>4</td><td>5.8</td><td>(4.5)</td><td>5.5</td><td>(4.3)</td><td>6.6</td><td>(5.2)</td><td>79.3</td><td>(61.7)</td><td>2.8</td><td>(24.3)</td></tr><tr><td>5</td><td>9.9</td><td>(4.4)</td><td>9.2</td><td>(4.1)</td><td>6.3</td><td>(2.8)</td><td>8.0</td><td>(3.6)</td><td>66.6</td><td>(85.0)</td></tr></table>

Table 7(D) shows the effect of comprehensiveness on state transitions. For states 1–4, as expected we find a curvilinear relationship between comprehensiveness and state stickiness. Reading very long posts (one standard deviation higher than mean comprehensiveness) or very short ones (one standard deviation below the mean comprehensiveness) reduces the stickiness of states 1–4. For state 5, comprehensiveness has no impact on its stickiness. However, the probability of moving to the dormant state increases the most as reading involves very short or very long posts.

Table 7(E) presents the impact of grammatical errors on the state-transition probabilities. The transition probabilities indicate that for states 1–4 grammatical errors negatively affect the stickiness of the states, as discussed earlier. This negative effect is more pronounced for states 1 and 2, where reading is focused on nonwork-related topics. Hence, the results indicate that readers of nonwork posts are more put off by grammatical errors than readers of work posts. However, the stickiness of the dormant state increases with grammatical errors as readers get dissatisfied and prefer to stay dormant. Further, grammatical errors significantly increase the transition to the dormant state from all other states.

Negativity displays a nonlinear relationship with stickiness. As discussed before, extreme values (too high or too low) of negativity reduce stickiness of a state. As shown in Table 7(F), one standard deviation higher negativity above mean reduces stickiness across states 1–4. However, as before, the effect is more pronounced for states with focus on nonwork readings. The dormant state becomes more sticky as the negativity becomes too high or too low.

Table 7(F) Transition Probabilities for One Standard Deviation Below (Above) Mean Negativity

<table><tr><td> $t \setminus t + 1$ </td><td colspan="2">1 (%)</td><td colspan="2">2 (%)</td><td colspan="2">3 (%)</td><td colspan="2">4 (%)</td><td colspan="2">5 (%)</td></tr><tr><td>1</td><td>67.2</td><td>(39.6)</td><td>5.8</td><td>(10.7)</td><td>2.7</td><td>(5.0)</td><td>3.4</td><td>(6.2)</td><td>20.9</td><td>(38.4)</td></tr><tr><td>2</td><td>12.0</td><td>(16.1)</td><td>45.3</td><td>(26.8)</td><td>5.6</td><td>(7.4)</td><td>3.2</td><td>(4.3)</td><td>33.9</td><td>(45.5)</td></tr><tr><td>3</td><td>2.9</td><td>(2.8)</td><td>4.1</td><td>(3.9)</td><td>61.0</td><td>(63.1)</td><td>8.9</td><td>(8.5)</td><td>23.1</td><td>(21.7)</td></tr><tr><td>4</td><td>10.8</td><td>(7.4)</td><td>10.3</td><td>(7.0)</td><td>12.4</td><td>(8.5)</td><td>42.5</td><td>(63.4)</td><td>24.0</td><td>(13.7)</td></tr><tr><td>5</td><td>0.9</td><td>(2.1)</td><td>0.8</td><td>(1.9)</td><td>0.6</td><td>(1.3)</td><td>0.7</td><td>(1.7)</td><td>96.9</td><td>(93.0)</td></tr></table>

Table 7(G) Transition Probabilities for One Standard Deviation Below (Above) Mean Controversialness

<table><tr><td> $t \setminus t + 1$ </td><td colspan="2">1 (%)</td><td colspan="2">2 (%)</td><td colspan="2">3 (%)</td><td colspan="2">4 (%)</td><td colspan="2">5 (%)</td></tr><tr><td>1</td><td>59.9</td><td>(86.8)</td><td>7.0</td><td>(2.9)</td><td>3.3</td><td>(1.4)</td><td>4.1</td><td>(1.7)</td><td>25.6</td><td>(7.2)</td></tr><tr><td>2</td><td>13.4</td><td>(5.9)</td><td>52.7</td><td>(75.0)</td><td>6.2</td><td>(2.7)</td><td>3.6</td><td>(1.6)</td><td>24.2</td><td>(14.8)</td></tr><tr><td>3</td><td>4.2</td><td>(1.6)</td><td>5.8</td><td>(2.2)</td><td>45.4</td><td>(80.4)</td><td>12.7</td><td>(4.9)</td><td>32.0</td><td>(10.8)</td></tr><tr><td>4</td><td>7.7</td><td>(3.6)</td><td>7.3</td><td>(3.4)</td><td>8.8</td><td>(4.2)</td><td>62.5</td><td>(83.5)</td><td>13.8</td><td>(5.2)</td></tr><tr><td>5</td><td>4.3</td><td>(10.0)</td><td>4.0</td><td>(9.4)</td><td>2.4</td><td>(7.3)</td><td>3.5</td><td>(8.1)</td><td>85.8</td><td>(65.2)</td></tr></table>

Table 7(G) presents the effect of controversialness on state-transition probabilities. As discussed earlier, an increase in controversy of the posts increases stickiness across states 1–4. In contrast, the stickiness of the dormant state decreases with controversialness. With higher controversialness, readers become more engrossed in the topic and, hence, read more, in effect switching to a more active state.

## 7.3. Posterior Analysis of Reader Behavior

A reader’s state in any given period can be probabilistically recovered using the filtering approach (Hamilton 1989). The filtering approach utilizes only the information known up to time t to recover a reader’s state in period t:

$$
\begin{array}{r l} & P (S _ {i t} = s \mid \mathbf {N} _ {i 1}, \mathbf {N} _ {i 2}, \ldots , \mathbf {N} _ {i T}) \\ & \qquad = \pi_ {i} \boldsymbol {\Lambda} _ {i 1} \mathbf {Q} _ {i, 1, 2}, \boldsymbol {\Lambda} _ {i 2} \dots \mathbf {Q} _ {i, t - 1, t \cdot s} P (\mathbf {N} _ {i t} \mid s) / L _ {i t}, \end{array}
$$

where $\mathbf { Q } _ { i , t - 1 , t \cdot s }$ is the sth column of the transition matrix $\mathbf { Q } _ { i , t - 1 , t } , \mathbf { \Phi } _ { { \Lambda } _ { i t } } = \mathrm { d i a g } ( P ( \mathbf { N } _ { i t } \mid S _ { i t } = 1 ) , P ( \mathbf { N } _ { i t } \mid S _ { i t } = 2 ) |$ $\dots , P ( \mathbf { N } _ { i t } \mid S _ { i t } = S ) )$ , and $L _ { i t }$ is the likelihood of the observed sequence of reading outcomes for individual i up to time t.

In any given period, a reader can be classified as being in a particular state according to the posterior probability distribution calculated above. Figure 3(a) depicts the trend over time of the distribution of readers in the five states, where the four curves plot the boundaries that separate the five states. Overall, the fraction of readers in a state is fairly stable over time. Approximately 22% of the readers belong to state 1, 21% belong to state 2, 10% belong to state 3, 11% belong to state 4, and the remaining belong to state 5. This indicates that at any time approximately 35% of readers are in the dormant state. Although the overall distribution of readers across states appears to be stable over time, the readers themselves move across states frequently as shown in Figures 3(b) and (c). One interesting observation from Figure 3 is that once a reader transitions to a state, she stays there for quite some time before transitioning again.

Figure 3 Reader’s Posterior States Over Time  
![](/api/attachments/EVQ6AAHK/fulltext/images/2510d1487f064e6b2a3c21ba005ff064be2236fe96269a91b1d563412fa4be48.jpg)

(b)  
![](/api/attachments/EVQ6AAHK/fulltext/images/3486ed7fc735f03dac34c63324e83145d6d125241e852735a834f35ac65cee29.jpg)  
(c)

![](/api/attachments/EVQ6AAHK/fulltext/images/0c5da8d20982fd2277de7298575c1fa3ea7899ea58766b53b7d14dd7499b83a6.jpg)

## 7.4. Robustness Checks

We conduct several checks to test the robustness of our results. An alternate explanation could be that individuals follow bloggers rather than topics. The variety-seeking behavior that we observe may be due to the fact that the bloggers they follow switch topics from one period to another. As a result, the readers are reading different topics from one period to another, and they become dormant for those time periods when the bloggers they follow do not post. To address this concern, we constructed a variable $b l o g g e r \_ p o s t _ { i j t } ,$ which counts the number of posts on topic j in period t written by bloggers who reader i follows. We include this variable in the reading set variables and reestimate our model. The results are robust to the inclusion of this variable in the model. We performed another analysis to check the robustness of our results to this concern. We identify the most probable state of individual i at time t. We then identify all the instances where the individual switched from one state to another. We find that whenever this switching happens from period t to t + 1, less than 10% of the posts read by the reader in the period t + 1 are from bloggers whose posts she read in period t. This provides an additional proof that the switching behavior is not determined solely by the switching behavior of bloggers.

A second concern regarding our results could be the appropriateness of the period-length specification. We employed alternative lengths for periods (two week, three week, and six weeks) and reperformed the analysis. These alternate specifications did not produce qualitatively different results. A third concern could be that some readers just stopped reading blogs during the 22-month period. In the current model, they will transition to the dormant state and stay there once they have dropped out. This may lead to over-stickiness for the dormant state. To address this concern, we added a sixth state (the drop-out state) in the model and estimated the whole model. The results from this estimation are similar to the ones reported in the paper.

Finally, it is possible that textual characteristics are endogenous (readability, grammatical error, comprehensiveness, negativity, and controversialness). Bloggers may decide whether to write a negative or a controversial post or pay more attention to ensure grammatical correctness, appropriate readability, and comprehensiveness by taking user preferences into account. We allow the text characteristics to be endogenous and use their lagged values for the topic as instruments. Using the instrumental variables we construct the supply-side equations for the text characteristics. Results indicate that instrumenting for textual characteristics does not affect our results. Further, the results indicate that the supply-side and demandside errors for the textual characteristics are not significantly correlated indicating these variables are not endogenous.

## 8. Conclusions, Contributions, and Limitations

Enterprise blogs are an important and novel channel for knowledge flow within organizations. Firms believe such initiatives can break knowledge silos and lead to higher employee productivity. As a result, most of the Fortune 500 firms allow their employees to blog. However, allowing employees to blog also raises issues regarding the governance of such initiatives. Firms that seek employee blogs as a channel for work-related knowledge sharing find that a majority of the content consumed and produced on these blogs is nonwork related. Firms are struggling to identify ways by which they can guide bloggers to produce and readers to consume work-related content. However, such efforts may be hamstrung because of their lack of understanding of employee blog-reading behavior.

In this research, we shed light on the blogreading behavior of employees. We find that employees exhibit a dynamic reading behavior where they switch from reading on one set of topics to another quite frequently. We identify five reading states. We find that in states 1 and 2, the reading is focused on nonwork-related content, and in states 3 and 4, reading is focused on work-related content. However, only approximately 21% of readers belong to states 3 and 4 at any time. The firm would probably like to guide readers toward states 3 and 4. We also identify a dormant state where employees read very little. We find that all the states are moderately sticky. The bloggers would obviously prefer states 1–4 to be sticky, since readers read a lot in these states. On the other hand, bloggers would prefer state 5 to have very low stickiness because readers read very little in that state.

Our dynamic model allows us to separate the effects of post-textual characteristics on attracting the readers from retaining them. We find that the characteristics that appeal to the sentiment of the reader affect both attraction and retention of readers. In contrast, the characteristics that reflect the quality of the language of the post only affect reader retention. We also find that blog readers have an inherent desire for variety.

From our analysis and results, it seems that there are opportunities for the firm to influence the blogreading behavior of its employees. As our results indicate, the properties of the post-textual characteristics significantly affect reader attraction and retention. All the five textual characteristics that we use in this study can be coded automatically using textmining techniques. The firm can provide the statistics on these characteristics (readability, grammatical errors, comprehensiveness, and negativity) for bloggers as they write posts. The bloggers can improve their posts on these dimensions as they write. Firms can also provide automatic grammatical tools to aid the bloggers. As our results show, if an employee encounters poor-quality work-related posts, she is more likely to switch away from reading such posts. The firm can influence a reader by recommending her work-related posts with high quality. This would be particularly important when a reader is in dormant state.

Several firms have prohibited employees from posting negative or controversial posts (Aggarwal et al. 2012). Employees themselves are cautious in not posting something negative or controversial in fear of negative repercussions. Our results indicate that controversial and moderately negative posts attract more readers, and readers who read such posts are less likely to become dormant. Hence, it would be in the best interest of the firm to encourage its employees to express their ideas without any fear of repercussions. We find that blog readers are inherently variety seekers. When firms recommend posts to bloggers, they should account for the varietyseeking behavior. In each time period, the firm has information on which posts a reader read. The postrecommendation systems should use this information to recommend posts that may increase reading variety. Essentially, the post-recommendation systems should account for dynamic behaviors of individuals for higher effectiveness.

This study makes several contributions. This is the first study to illustrate the dynamics in the blogreading behavior of employees. We identify a varietyseeking behavior of blog readers. Further, we show that this behavior is induced by post-textual characteristics. The modeling framework and the results from our study contribute significantly to our understanding of how individuals consume user-generated content and provide guidelines to content generators to produce more popular content. They shed new light on improving content generation and suggesting personalized recommendations, which is quite challenging in the context of online content delivery systems (Murthi and Sarkar 2003).

The data structure and context of this study required us to make several methodological changes to traditional dynamic state-space models. A methodological contribution of this study is to develop a kvariate negative binomial dynamic model to capture observed and unobserved inter-temporal as well as cross sectional heterogeneities in blog-reading behavior. This is one of the first studies to account for demand-supply joint estimation in dynamic statespace models. Our modeling framework helps in highlighting the opportunities for influencing reading behavior of employees to align it with firm goals.

This study has its limitations. First, although our data set is sufficiently large to make the findings generalizable to the context of the host firm, studies using data sets from other firms are needed to ensure that our findings are generalizable. Second, we have data on blog readings within the firm. However, employees may read external blogs too. We do not have access to such readings. Although the incorporation of individual-level unobserved heterogeneity should account for such effects, future research should consider collecting data on both internal and external blog readings for a more robust analysis. Third, our reading is based on the information that a reader has accessed the blog. It may be the case that the reader did not read the blog at all or read it partially, which we do not observe. Future studies should consider collecting such information through surveys and questionnaires. Fourth, the blogging behavior of an employee could be affected by external factors such as free time available or stage of a project on which an employee is working. Data on such factors is not available to use. However, these factors are likely random factors and are accounted for in error terms. Data on such factors could potentially increase the efficiency of our results. Finally, although we have highlighted opportunities for firms to influence employee reading behavior, only by carrying out experiments or counterfactuals can one test the true effect of our suggestions.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2013.0509.

## References

Adamic L, Glance N (2005) The political blogosphere and the 2004 US elections: Divided they blog. Internat. Conf. Knowledge and Data Mining, Chicago, IL.

Aggarwal R, Gopal R, Sankaranarayanan R, Singh PV (2012) Blog, blogger, and the firm: Can negative posts by employees lead to positive outcomes? Inform. Systems Res. 23(2):306–322.

Appelman A, Bolls P (2011) Article recall, credibility lower with grammar errors. Newspaper Res. J. 32(2):1–14.

Arbous A, Kerrich J (1951) Accident statistics and the concept of accident-pronenss. Biometrics 7(4):340–432.

Atchade Y (2006) An adaptive version for the Metropolis adjusted Langevin algorithm with a truncated drift. Methodology Comput. Appl. Probab. 8(2):235–254.

Beason L (2001) Ethos and error: How business people react to errors. College Composition Comm. 53(1):33–64.

Blei D, Bagnell D, McCallum A (2002) Learning with scope, with application to information extraction and classification. Proc. 18th Conf. Uncertainty in Artificial Intelligence 4UAI5 (Morgan Kaufmann, San Francisco), 53–60.

Blei D, Ng A, Jordan M (2003) Latent Dirichlet allocation. J. Machine Learn. Res. 3:993–1022.

Cingel DP, Sundar SS (2012) Texting, techspeak, and tweens: The relationship between text messaging and English grammar skills. New Media and Society 14(8):1304–1320.

Clement R, Sharp D (2003) Ngram and Bayesian classification of documents for topic and authorship. Literary and Linguistic Comput. 18(4):423–447.

Efimova L (2007) Getting value from employee weblogs: A knowledge management approach. Jezzard H, ed. Applying Web 2.0: Innovation, Impact and Implementation, Proc. Online Inform. London, 43.

Feld MD (1959) Information and authority: The structure of military organization. Amer. Sociol. Rev. 24(1):15–22.

Furukawa T, Matsuo Y, Ohmukai I, Uchiyama K, Ishizuka M (2007) Social networks and reading behavior in the blogosphere. Internat. Conf. Weblogs Soc. Media, Boulder, CO.

Gelman A, Rubin D (1992) Inference from iterative simulation using multiple sequences. Statist. Sci. 7(4):457–472.

Ghose A, Ipeirotis P (2011) Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Trans. Knowledge and Data Engrg. 23(10):1498–1512.

Grant RM (1996) Toward a knowledge-based theory of the firm. Strategic Management J. 17:109–122.

Greve H (2005) Interorganizational learning and heterogeneous social structure. Organ. Stud. 26(7):1025–1047.

Grinberg D, Lafferty J, Sleator D (1995) A robust parsing algorithm for link grammars. Proc. Fourth Workshop on Parsing Tech.

Hamilton JD (1989) A new approach to the economic analysis of non-stationary time series and the business cycle. Econometrica 57(2):357–384.

Heckman J (1981) Rosen S, ed. Heterogeneity and State Dependence, Studies in Labor Markets (University of Chicago Press, Chicago), 91–139.

Huang Y, Singh PV, Ghose A (2010) Show me the incentives: A dynamic structural model of employee blogging behavior. Internat. Conf. Inform. Systems, Saint Louis, MO.

Kincaid JP, Fishhourne RP, Rogers RL, Chissom BS (1975) Derivation of new readability formulas (automated readability index, fog count and flesch reading ease formula) for Navy enlisted personnel. Technical report. (Naval Tech. Training Command, Millington, TN).

Lu Y, Jerath K, Singh PV (2013) The emergence of opinion leaders in a networked online community: A dyadic model with time dynamics and a heuristic for fast estimation. Management Sci. 59(8):1783–1799.

Lunstrum JP (1965) The treatment of controversial issues in social studies instruction. The High School J. 49(1):13–21.

Lunstrum JP (1981) Building motivation through the use of controversy. J. Reading 24(8):687–691.

Lucier C, Torsilieri J (1997) Why knowledge programs fail: A C.E.O.’s guide to managing learning. Strategy and Business 4th Quarter:14–28.

McAlister L (1982) A dynamic attribute satiation model of varietyseeking behavior. J. Consumer Res. 9(2):141–150.

McAlister L, Pessemier E (1982) Variety seeking behavior: An interdisciplinary review. J. Consumer Res. 9(3):311–322.

McDonald I, Zucchini W (1997) Hidden Markov and Other Models of Discrete Valued Time Series (Chapman and Hall, Boca Raton, FL).

Mishne G, Glance N (2006) Predicting movie sales blogger sentiment. Proc. AAAI-CAAW-06, Spring Sympos. Computational Approaches to Analyzing Weblogs (AAAI Press, Menlo Park, CA), 155–158.

Murthi B, Sarkar S (2003) The role of the management sciences in research on personalization. Management Sci. 49(10):1344–1362.

Nardi BA, Schiano D, Gumbrecht M, Swartz L (2004) Why we blog. Comm. ACM 47(12):41–46.

Netzer O, Lattin J, Srinivasan V (2008) A hidden Markov model of customer relationship dynamics. Marketing Sci. 27(2):185–204.

Newton M, Raftery A (1994) Approximate Bayesian inference by the weighted likelihood bootstrap. J. Roy. Statist. Soc. B 56(1): 3–48.

Oliver R (1997) Satisfaction: A Behavioral Perspective on the Consumer (McGraw-Hill, New York).

Pang B, Lee L (2004) A sentimental education: Sentiment analysis using subjectivity summarization based on minimum cuts. Proc. 42nd Meeting Assoc. Computational Linguistics (ACL, Stroudsburgh, PA), 271–278.

Rabiner LR (1989) A tutorial on hidden Markov models and selected applications in speech recognition. Proc. IEEE 77(2):257–285.

Sahoo N, Krishnan R, Callan J (2008) Formation of citation and reply ties over intra-organizational blog network. Conf. Inform. Systems Tech., Washington, DC.

Sargan J (1958) The estimation of economic relationships using instrumental variables. Econometrica 26(3):393–415.

Singh PV, Youn N, Tan Y (2011) A hidden Markov model of developer learning dynamics in open source software projects. Inform. Systems Res. 22(4):790–807.

Stock J, Yogo M (2005) Testing for weak instruments in linear IV regression. Andrews DWK, Stock JH, eds. Identification and Inference for Econometric Models: Essays in Honor of Thomas Rothenberg (Cambridge University Press, Cambridge, UK).

Villas-Boas J, Winer R (1999) Endogeneity in brand choice models. Management Sci. 45(10):1324–1338.

Yang S, Chen Y, Allenby G (2003) Bayesian analysis of simultaneous demand and supply. Quant. Marketing Econom. 1:251–275.
