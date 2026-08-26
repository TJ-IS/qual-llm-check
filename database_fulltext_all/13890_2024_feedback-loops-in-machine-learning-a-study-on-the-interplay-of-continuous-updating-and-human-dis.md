---
otero_id: 13890
otero_key: "VVM428SH"
title: "Feedback Loops in Machine Learning: A Study on the Interplay of Continuous Updating and Human Discrimination"
authors: "Kevin Bauer; Rebecca Heigl; Oliver Hinz; Michael Kosfeld"
year: "2024"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00853"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
2024

# Feedback Loops in Machine Learning: A Study on the Interplay of Continuous Updating and Human Discrimination

Kevin Bauer , kevin.bauer@uni-mannheim.de

Rebecca Heigl , rmheigl@wiwi.uni-frankfurt.de

Oliver Hinz , ohinz@wiwi.uni-frankfurt.de

Michael Kosfeld , kosfeld@econ.uni-frankfurt.de

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Feedback Loops in Machine Learning: A Study on the Interplay of Continuous Updating and Human Discrimination

Kevin Bauer,<sup>1</sup> Rebecca Heigl,<sup>2</sup> Oliver Hinz,<sup>3</sup> Michael Kosfeld<sup>4</sup>

<sup>1</sup>University of Mannheim, Germany, kevin.bauer@uni-mannheim.de <sup>2</sup>Goethe University Frankfurt, Germany, rmheigl@wiwi.uni-frankfurt.de <sup>3</sup>Goethe University Frankfurt, Germany, ohinz@wiwi.uni-frankfurt.de <sup>4</sup>Goethe University Frankfurt, Germany, kosfeld@econ.uni-frankfurt.de

## Abstract

Machine learning (ML) models often endogenously shape the data available for future updates. This is important because of their role in influencing human decisions, which then generate new data points for training. For instance, if an ML prediction results in the rejection of a loan application, the bank forgoes the opportunity to record the applicant’s actual creditworthiness, thereby impacting the availability of this data point for future model updates and potentially affecting the model’s performance. This paper delves into the relationship between the continuous updating of ML models and algorithmic discrimination in environments where predictions endogenously influence the creation of new training data. Using comprehensive simulations based on secondary empirical data, we examine the dynamic evolution of an ML model’s fairness and economic consequences in a setting that mirrors sequential interactions, such as loan approval decisions. Our findings indicate that continuous updating can help mitigate algorithmic discrimination and enhance economic efficiency over time. Importantly, we provide evidence that human decision makers in the loop who possess the authority to override ML predictions may impede the self-correction of discriminatory models and even induce initially unbiased models to become discriminatory with time. These findings underscore the complex sociotechnological nature of algorithmic discrimination and highlight the role that humans play in addressing it when ML models undergo continuous updating. Our results have important practical implications, especially considering the impending regulations mandating human involvement in ML-supported decision-making processes.

Keywords: Continuous Updating, Algorithmic Discrimination, Human Discrimination, Feedback Loops, Investment Game

John Qi Dong was the accepting senior editor. This research article was submitted on June 22, 2022 and underwent three revisions.

## 1 Introduction

With the aim of bolstering economic efficiency and societal welfare (Benbya et al., 2020; Teodurescu et al., 2021), machine learning (ML) systems are augmenting human decision-making across diverse domains, including bail decisions (Kleinberg et al., 2018), hiring processes and student admissions (Horton, 2017; Zhao et al., 2020), banking (Fu et al., 2021), and medicine (Jussupow et al., 2021). In Europe, Big Data analytics software revenue reached US\$14.6 billion in 2018 alone. Wells and Spinoni’s projections (2019) indicate an expected annual growth rate of about 8% for this market over the next five years. One central tenet of contemporary ML systems is the assumption that the same data-generation process underpins the training data and the out-of-sample data for which the systems generate predictions (Parisi et al., 2019). However, in dynamic, nonstationary environments, the underlying data-generating process that ML models aim to approximate can change over time. This phenomenon, referred to as drift (Lu et al., 2018), can lead to progressively poorer predictions. The decrease in prediction performance can originate from changes in the underlying relationship between the input features and the target variable—concept drift (Widmer & Kubat, 1996)—or changes in the distributions of the input features or the target variable—data drift (Mallick et al., 2022). As a consequence, to maintain or even improve prediction accuracy over time, it is imperative to continuously update ML models on recent data that reflect new patterns in the data-generating process (Gama et al., 2014).

The efficacy of continuous updating inherently links to the quality and structure of the collected data. Ideally, updating processes should empower models to learn from their past mistakes—that is, identify cases for which they generate inaccurate predictions. However, ML models that support or automate human decisions typically do more than merely provide neutral predictions; their usage often influences decisions, thereby endogenously shaping the structure of future data available for updates. Take, for instance, an ML model assisting a bank in loan approval. It analyzes applicant resumes and offers creditworthiness predictions to loan officers (refer to Figure 1 for an illustration). All else being equal, if the model shows a tendency to consider male applicants more creditworthy, the additional data gathered for retraining will disproportionately include men, inherently relating to the phenomenon of data drift (Mallick et al., 2022). The reason for this is that the bank lacks the ability to determine if rejected applicants would have repaid the loan—a vital piece of information required for model updating. This endogenous composition of future training data, a problem referred to as selective labeling (Lakkaraju et al., 2017; Little & Rubin, 2019), can maintain or even exacerbate inaccurate or discriminatory predictions.

In this paper, we explore the dynamic interplay between the continuous updating of ML models and algorithmic discrimination when ML predictions endogenously shape the composition of additional data available for model updating. In particular, our work focuses on the role of ongoing discrimination by human decision makers who have the final say in an ML-supported decision-making task. A steady stream of previous work has examined how algorithmic discrimination can reproduce and perpetuate discriminatory patterns ingrained in societal structures (Lambrecht & Tucker, 2019; Morse et al., 2022; Teodurescu et al., 2021). Some studies have developed theoretical arguments concerning the emergence of feedback loops when ML models continually learn from the discriminatory outcomes they helped to generate (see, for example, Cowgill & Tucker, 2019; Ensign et al., 2017; Silva & Kenney, 2019). However, as Kordzadeh and Ghasemaghaei (2022) observed in their literature review, systematic empirical exploration of the long-term dynamic effects of continuously updating ML models is lacking, particularly in terms of the role of human decisionmaking based on these predictions. We aim to fill this research gap. Regarding contexts where a continuously updated ML system both supports human decisionmaking and shapes the data available for updating, we pose the following questions:

RQ1: How does continued updating affect the fairness and economic efficiency of an ML model that initially discriminates against a certain social group due to a label imbalance in the training data?

RQ2: How does persistent discrimination by human decision makers against a certain social group affect the impact of continuous updating on model fairness and economic efficiency?

![](/api/attachments/VVM428SH/fulltext/images/0d2a9b7d161735a949b693e97cc6bf85e65f284e0b5d16dfa3e8c428fa67994f.jpg)  
Figure 1. Process Where Machine Learning Predictions Endogenously Influence the Availability of Data for Future Retraining of the Model

Addressing these questions presents complex challenges. First, it requires exogenous variations in both initial algorithmic and persistent human discrimination. Second, to accurately assess model fairness and economic efficiency, visibility into the outcomes of unexecuted counterfactual choices is needed—for instance, understanding the hypothetical repayment behavior of a declined loan applicant. We navigate these hurdles using simulations, leveraging data from two incentivized empirical studies previously conducted as part of our team’s related research projects, i.e., secondary data. In both empirical studies, participants engaged in a popular social dilemma game that mimics the structure of a sequential investment decision used, for example, in loan approval or hiring processes (Berg et al., 1995; Fehr & Fischbacher, 2003). Our simulation, grounded in empirical data, allowed us to avoid making strong theoretical assumptions about decision makers’ motives. Instead, we adopted a datadriven approach, introducing discriminatory behaviors by both ML models and humans exogenously.

Our simulations proceed as follows, intuitively speaking. Numerous bank loan officers evaluate loan applications, with each officer assessing a single application. The outcome of an approved loan may lead to either repayment or default. To make an informed decision, loan officers scrutinize the applicant’s resume and receive a prediction from an ML system about the likelihood of loan repayment. If a loan officer denies the loan, the outcome, i.e., whether the applicant would have repaid the loan or defaulted, remains unknown. However, if the loan officer approves the loan, the loan officer eventually learns whether the applicant repays or defaults. The applicant’s information, including the final repayment or default status, augments the initial dataset used to train the ML model. This enriched training data is used to periodically update the ML model. Subsequent lending decisions rely on the prediction of the updated ML model for decision support. In our simulation, we introduced initial algorithmic discrimination by the ML model and persistent discrimination against female applicants by the loan officers exogenously.

In essence, our simulations indicate that the continuous updating of ML models using endogenously generated data enables the model to “unlearn” existing algorithmic discrimination and boost economic efficiency over time. However, this self-correcting mechanism suffers under the influence of ongoing discrimination by the human decision maker in the loop. Notably, this enduring human discrimination can even adversely affect the fairness of initially unbiased models, as they effectively adopt biased human behaviors.

Our primary contribution resides in illuminating the dynamic consequences of continuously updating ML models in the presence of algorithmic and human discrimination. We highlight that continuous updating, absent enduring human discrimination, may stimulate self-correcting mechanisms. Theoretically, our findings underscore the sociotechnological nature of algorithmic discrimination. We extend the existing literature by revealing how algorithmic discrimination can diminish or emerge due to the interaction between ML system and human users in environments where continuously updating ML models is essential. We found evidence that humans in the loop can undermine the powerful learning capabilities of ML systems, inadvertently teaching the machines to maintain or even adop discriminatory behaviors over time. Our insights provide a novel, dynamic perspective on algorithmic discrimination, enhancing the comprehension of it origins and moderating factors and highlighting the potency of continuous model updating to mitigate it. Our findings also speak to broader discussions on ways to address model drift challenges (see, e.g., Mallick et al., 2022). In our context, unjustified algorithmic discrimination can be thought of as an outdated input output relationship that the model learned from training data, i.e., as resulting from a concept drift. On the other hand, human discrimination, leading to shifts in data distributions for future training, arguably relates to an ongoing data drift. From this perspective, our results illuminate the efficacy of continuous model updates in mitigating concept drift issues. However, this strategy is less effective in the presence of an ongoing data drift. From a practical standpoint, our findings about the role of human involvement are especially important in light of regulations mandating human participation in ML decision-making processes, e.g., having the final say in high-stakes decisions (e.g., General Data Protection Regulation Art. 22, or the European Commission’s Artificial Intelligence Act). Granting humans the final say in ML-supported decision-making processes runs the risk of inadvertently perpetuating or igniting algorithmic discrimination if these individuals engage in discriminatory practices. In this context, efforts aimed at identifying and mitigating (subconscious) discriminatory practices of organizational decision makers, such as awareness training, become an indispensable complementary element to ensure that continuously updated ML models exhibit desirable behaviors.

## 2 Theoretical and Conceptual Background

In this section, we first provide the conceptual underpinnings of algorithmic discrimination. Subsequently, we discuss the literature gaps our work aims to address.

## 2.1 Algorithmic Discrimination

Algorithmic discrimination: Discrimination involves statements or actions that unjustifiably disadvantage members of particular social groups. These actions typically stem from conscious or subconscious attitudes, prejudices, or emotional associations tied to characteristics such as gender, age, disability, race, language, religion, or sexual identity (Scherr, 2008). In today’s era, where algorithmic systems based on ML models frequently aid human decisions, researchers and practitioners often employ the term “algorithmic discrimination” to refer to system outputs that disproportionately benefit or disadvantage specific groups, even when no justification for the disparate treatment exists from a ground-truth perspective (Kordzadeh & Ghasemaghaei, 2022).<sup>1</sup>

Algorithmic discrimination can originate from various sources. First, it may stem from intentional or unintentional social biases encoded within the training data (Friedman & Nissenbaum, 1996; Romei & Ruggieri, 2013; Kleinberg et al., 2018). For example, if a training dataset holds more positively labeled examples for men, the ML model may predict positive labels less accurately for women. Second, it can be created by unrepresentative, or imbalanced data (Barocas & Selbst, 2016; Mehrabi et al., 2021). When the dataset underrepresents certain groups, such as women, the ML model can make more errors when predicting for this group. Imbalances occur when labels skew significantly within specific subgroups. Third, technical constraints or malpractices during model development and training may yield discriminatory outputs (Friedman & Nissenbaum, 1996; Williams et al., 2018). Biases may emerge during data integration due to inconsistent data formats or when the integration of personal information like ethnicity is mishandled (Schelter & Stoyanovich, 2020; Williams et al., 2018). It is critical to appreciate the sociotechnological nature of algorithmic discrimination (Favaretto et al., 2019; Kordzadeh & Ghasemaghaei, 2022). The social component often originates from societal and economic structural biases, which can foster the differential treatment and marginalization of certain groups. On the other hand, the technological element emanates from the perpetuated discriminatory behaviors of algorithmic systems.

Algorithmic feedback loops: Feedback loops play a significant role in algorithmic discrimination in the context of continuously updated ML models. These loops arise when the outcomes of algorithmic decisions provide new endogenous training data for subsequent model updates (Cowgill, 2018). Such loops iteratively weave together the social environment’s outcomes and the technical performance of the algorithmic output. For instance, take the loan approval process depicted in

Figure 1. If an ML model’s prediction of creditworthiness guides loan approval, this prediction will shape the data available for future updates. As the bank only observes the actual creditworthiness of successful applicants, this can induce a bias in the data for subsequent model updates, potentially affecting the quality and nature of future predictions. Notably, when divergent from the incoming data on which predictions are made, this endogenous shift in training data composition relates to data drift challenges. In such scenarios, the feature distribution in the training set varies from that of the new incoming data.

Feedback loops can inadvertently reinforce existing biases, creating “data-driven echo chambers” that perpetuate discriminatory decisions (Veale & Binns, 2017; O’Neil, 2017). For instance, a biased ML model can amplify a human decision maker’s propensity to discriminate. Feeding the outcomes of biased decisions back into the model as new training data may compound the system’s discrimination, engendering a cycle of persistent discrimination (Silva & Kenney, 2019; Williams et al., 2018). Such feedback loops have been discussed in various domains, such as hiring, policing, and recidivism decisions (e.g., Hoffman et al., 2018; Kleinberg et al., 2018; Ensign et al., 2017; Cowgill, 2018).

Measuring algorithmic discrimination: A considerable body of work in information systems (IS) and computer science focuses on creating methods to measure algorithmic discrimination (see, for example, Hardt et al., 2016; Pessach & Shmueli, 2022). Common group-level objectives include equality of false-negative and falsepositive error rates (Corbett-Davies & Goel, 2018), demographic parity (Besse et al., 2022; Calders & Verwer, 2010), and equal opportunity (Hardt et al., 2016; Radovanović & Ivić, 2021). Although each metric gauges the attainment of specific fairness objectives, they all share a fundamental premise: the systematic deviation of algorithmic outputs from the ground truth they aim to predict for certain subpopulation subgroups. It is important to recognize that achieving different fairness metrics simultaneously can be challenging and may occasionally be mathematically unachievable (Shrestha & Yang, 2019). For instance, an ML model with 100% accuracy, hence ensuring the equality of false-negative errors, won’t optimize demographic parity if distinct ground truth rates characterize different subgroups. Thus, significant trade-offs exist, making the choice of a fairness metric reliant on the system’s operational domain (Wong, 2020). In our study, we employed two of these objectives to measure how the fairness of a continuously learning ML system evolves over time: statistical parity and equality of false-negative error rates.

Statistical parity aims to ensure an equal likelihood of receiving a positive prediction (e.g., creditworthiness) for both disadvantaged and advantaged groups (Calders & Verwer, 2010). Therefore, a reduced disparity between the two groups indicates enhanced fairness (Pessach & Shmueli, 2022). We calculate the degree of statistical parity as follows:

$$
\text { Stasistical   parity } = P \big (\hat {Y} = 1 | S = 0 \big) - P \big (\hat {Y} = 1 | S = 1 \big).
$$

S represents a (legally) protected attribute on which the discrimination is based on, e.g., race or gender. $S = 0$ is the unprivileged group, i.e., the group against which the algorithm discriminates (in our simulation being a woman), and $S = 1$ is the privileged group, i.e., the group that does not experience discrimination. $Y \in$ (0,1) is the variable to predict, with $\hat { Y } = 1$ reflecting a positive prediction $( \mathrm { e . g . }$ , creditworthy) and $\hat { Y } = 0$ the negative prediction (e.g., not creditworthy). Statistical parity ranges between 0 and 1, respectively indicating maximum and minimum fairness. We opt for statistical parity because it is a straightforward measure that equalizes predictions across different social groups. This measure enjoys widespread recognition in the literature, despite its inherent weaknesses. For example, if a model flawlessly mirrors the underlying data-generating process that exhibits a gender gap in the likelihood of $Y = 1$ , this perfect model won’t achieve a statistical parity of 0 (Gupta et al., 2021). The Equality of false-negative error rates seeks to prevent an ML model from misclassifying positive instances— such as classifying creditworthy women as noncreditworthy more often than creditworthy men—for any specific group:

$$
\Delta F N R = P \big (\hat {Y} = 0 \big | S = 0, Y = 1 \big) - P \big (\hat {Y} = 0 \big | S = 1, Y = 1 \big).
$$

We consider this fairness measure, which is also constrained between 0 (minimum discrimination) and 1 (maximum discrimination), as it is particularly relevant in situations where false negatives have significant consequences, such as in healthcare, loan approval, hiring, or criminal justice systems.

Mitigating algorithmic discrimination: The expansive literature on algorithmic discrimination proposes various methods to identify and alleviate such biases. According to d’Alessandro et al. (2017), we can divide these mitigation strategies into three categories: pre-processing, in-processing, and postprocessing. Pre-processing strategies strive to eliminate disparities inherent in the dataset. Methods such as those proposed by Kamiran and Calders (2012) and Zafar et al. (2017) employ data pre-processing techniques like feature massaging and reweighting to balance the dataset based on social group characteristics. In-processing strategies involve conventional learning algorithms during model training. Researchers often use techniques like naive Bayes and decision trees for debiasing (Calders & Verwer, 2010; Zhang et al., 2018). Additional research suggests placing constraints on the classification model to mandate the satisfaction of a proxy (Woodworth et al., 2017). Lastly, post-processing strategies aim to adjust the output to counter biases. For example, Corbett-Davies et al. (2017) recommended setting separate thresholds for each group to minimize demographic disparity. Lohia et al. (2018) used a bias detector on a model’s output, adjusting model predictions by suitably editing protected attributes.

## 2.2 Contribution to the Literature

This paper enhances two streams of research in the IS literature. First, it augments the existing body of work on algorithmic discrimination. Scholars have rigorously examined how modern ML systems can produce unfavorable outcomes for particular groups, often those marginalized. Such discrimination manifests across various contexts, from recidivism risk assessments (Dressel & Farid, 2018) and education (Baker & Hawn, 2021) to recruitment (Leicht-Deobald et al., 2019), predictive policing (Ensign et al., 2017), health risk evaluations (Obermeyer et al., 2019), targeted advertising (Sweeney, 2013; Lambrecht & Tucker, 2019), crowdlending scenarios (Fu et al., 2021), and facial recognition tasks (Buolamwini & Gebru, 2018). Racial and gender biases are notably pervasive (Leavy, 2018). Our study extends this discourse by scrutinizing the temporal progression and economic implications of algorithmic discrimination in scenarios involving continuous ML model updating, an area lacking comprehensive empirical investigation (Kordzadeh & Ghasemaghaei, 2022). Grasping this dynamic is critical, as many ML models might degrade over time—due, for example, to concept or data drifts, which respectively reflect fundamental shifts in the latent data-generating process and the distribution of incoming data (Lu et al., 2018)—necessitating continuous updating based on newly collected data. We provide a more comprehensive perspective of the origins and moderating factors affecting ML systems’ functionality by explaining the interplay between continuous model updating and algorithmic discrimination. Despite its critical importance in developing countermeasures and refining policy recommendations, the complex interplay between algorithmic discrimination and continuous ML model updating remains an underexplored area in the literature.

Second, our paper complements the nascent body of studies exploring the origins and impacts of algorithmic feedback loops (Burghardt & Lerman, 2022; Cowgill, 2018). For instance, Lum and Isaac (2016) revealed that the iterative updates of a predictive policing system led to increased discrimination against minority groups. Similarly, Ensign et al. (2017) showed how feedback loops could unintentionally steer police toward the same neighborhoods, regardless of actual crime rates. Our study extends this research by investigating how the dynamics of algorithmic feedback loops depend on the behavior of humans who use these predictions for decision-making. We examine the impact of feedback loops from a sociotechnical viewpoint, questioning whether and how the emergence of vicious or virtuous cycles hinges on the behavior of humans in the loop. Specifically, we study how persistent human discrimination, influencing the distribution of newly collected data for future model updates, impacts the nature of algorithmic feedback loops. Notably, human discrimination introduces continuous biases in data collection, leading to discrepancies between training data and real-world data. Thus, human discrimination can be seen as a potential cause of data drifts that may interact with existing algorithmic discrimination in unexpected ways. Studying the role of human discrimination in algorithmic feedback loops is both timely and necessary, particularly given emerging regulations such as the European Commission’s Artificial Intelligence Act, which mandates human involvement in high-stakes decisions informed by ML models. Parallel regulatory efforts are underway in the US, with a blueprint for an AI Bill of Rights. In this context, our work provides an essential examination of the complex dynamics of human-technology interaction within ML decision support systems that continue to learn over time.

## 3 Empirical Strategy

## 3.1 Game Theoretic Framework

To answer our research questions, we leverage simulations based on a game-theoretic paradigm similar to the so-called investment game (also referred to as the trust game) (Berg et al., 1995). Importantly, our simulations build on the behavior of real people whose decisions the authors previously collected as part of two separate empirical studies (see Section 3.2 for more details). Computer simulations serve as a robust and widely accepted tool across multiple scientific fields, facilitating the analysis of dynamic processes (Kahalé, 2020). Such simulations also enable the generation of proofs of concept for novel ideas (Wong & Kwong, 2018). We opt for this research methodology primarily because the exogenous introduction of discrimination, particularly by humans, is not only ethically untenable but also practically unfeasible in experimental or field settings.

Our simulation employs a modified version of the investment game (Berg et al., 1995). This game emulates the incentives and informational structure inherent in numerous economic transactions that transpire in environments lacking robust enforcement mechanisms (Dufwenberg & Kirchsteiger, 2004; Fehr & Fischbacher, 2003). In our game, two participants, an investor and a borrower, each begin with an endowment of 10 monetary units (MU). The investor first chooses whether to retain or invest the entire 10 MU with the borrower. If the investor retains the sum, the game ends and both parties keep their initial endowment of 10 MU, representing a nontransactional scenario, e.g., where a bank loan officer does not approve a loan. Alternatively, if the investor chooses to invest, the sum doubles upon reaching the borrower, yielding a total of 30 MU. The borrower can then opt to keep the entire sum, thereby generating a payoff of 30 MU for the borrower and 0 MU for the investor. This case represents a scenario where a successful loan applicant uses the loan to make a purchase but does not end up paying back the money. However, the borrower can also choose to repay the investor. In this case, we assume that both parties earn 20 MU and are both better off compared to the nontransactional outcome (with 10 MU each), but the borrower would earn more in the case scenario where the loan is not paid back. This case represents the economically efficient scenario where a deserving loan applicant obtained credit, used it to make a purchase, and eventually paid it back. Therefore, the game culminates in one of three possible outcomes (refer to Figure 2 for an overview).

![](/api/attachments/VVM428SH/fulltext/images/3ee99078f55c6870352f4495d8178a3fc871086afbda2caf55b6dee829a7fd13.jpg)  
Figure 2. Illustration of the Investment Game Applied in Our Simulations

The investment game captures the structure inherent in many transactions occurring in environments where contracts cannot be perfectly enforced (Fehr et al., 1993; Brown et al., 2004). The investor must form beliefs about the borrower’s trustworthiness, specifically whether the borrower will make a repayment. In the absence of sufficient trust, the investor retains the funds, foregoing a potentially beneficial transaction. This mechanism is mirrored in business contexts, such as bankers deciding upon loan approval, HR managers making hiring decisions, and a supplier deciding whether to provide goods on credit to a retailer, based on their assessment of the retailer’s likelihood to pay after the sale is completed.

In our simulation, we utilized data from a previous empirical study (Study B, described in further detail below) to train an ML model that mimics the decisionmaking of real human investors. Specifically, the trained model uses information about the personal characteristics of both the investor and the borrower, as well as an available forecast about the borrower’s propensity to make a repayment in order to predict the probability that a given investor would invest 10 MU with a given borrower. We exogenously introduced investor discrimination against women by incrementally increasing the probability threshold to determine whether an investment would occur— beginning with the default of 50% and moving up incrementally to 60%, 70%, and 80% for female borrowers. While using humans for live decisionmaking has its merits, particularly concerning external validity, our simulation allows us to exogenously manipulate discrimination within a continuously updating environment in an ethical and scalable way. For readability, we hereafter refer to the ML model that predicts how an actual investor would behave simply as the “investor.” Borrower decisions are based on real human decisions from another prior empirical study (Study A, see below for more details) where we used the strategy method to measure participants’ choices assuming the investor initially made the investment. That is, we knew whether each individual borrower would or would not make a repayment if an investor were to initially invest 10 MU with them. Importantly, due to the strategy method, we knew the borrower’s conditional repayment decision regardless of the actual investor decision, i.e., we knew counterfactual outcomes. Game outcomes were determined by pairing a simulated investor decision with the borrower’s actual conditional decision.

Where do the ML system, selective labels problem, and continuous updating come into play? There are two pertinent aspects of the investment game. First, investors make initial decisions under uncertainty and form beliefs about the likelihood of borrowers making a repayment. Here, an ML model prediction can decrease information asymmetries (Agrawal et al., 2019) by providing individual-level predictions on the borrower’s repayment likelihood, increasing the potential for economically efficient outcomes. Second, investors only observe borrower behavior if they initially opt to invest. By choosing not to invest, they forgo the opportunity to learn whether the borrower would have repaid; consequently, they cannot accrue new data points for borrowers they bypass. Hence, in a setting where investors’ decisions are swayed by ML model predictions, these predictions substantially shape the availability and structure of future data for model updates. If the selective accrual of new data leads to skewed datasets for model updates, the behavior of the updated model could potentially be distorted, possibly leading to discrimination against certain borrower groups. Thus, model predictions can trigger feedback loops (Silva & Kenney, 2019; Williams et al., 2018).

To illustrate, consider the loan approval process as described above. Suppose a loan officer uses an ML model to make an informed approval decision. The model often inaccurately predicts that female applicants are not creditworthy, while it is almost always correct for men. If these biased predictions lead the officer to deny loans to women more often than men, the bank will collect more data on male loan repayment behavior than on that of women. This escalating gender bias in the data used to update the ML model may exacerbate the model’s inaccuracies, particularly in its predictions for women. This could potentially initiate a self-perpetuating feedback loop, where the disparity in prediction quality between men and women widens (e.g., Kleinberg et al., 2018). It is important to note that such feedback loops can arise not only from initially biased ML models but also from loan officers who independently discriminate against female applicants, even when using ML predictions. As a result, training data can become increasingly unbalanced and distorted due to human behavior alone. In such a scenario, if the ML model is continually updated with the newly generated data, even an initially unbiased system may eventually start to discriminate against women.

To examine such patterns in our simulation, the investor was given not only information about the personal characteristics of the investor but also a forecast of whether the given borrower will make a repayment. The forecast originated from an ML model that we trained on data from the prior Study A (see below for more details), i.e., we utilized a functional, empirically validated ML model. We exogenously varied the extent to which this ML model generated biased predictions for female borrowers by adjusting the share of repaying female borrowers in the training data.

## 3.2 Previous Empirical Studies

We built our simulations on two secondary datasets, collected by several authors of this paper as part of different empirical studies. Study A was an incentivized field study conducted over three years from 2016 to 2019. Study A measured participants’ behavior in the investment game defined above in their role as borrowers. The data from Study A allowed us to develop an ML model predicting borrowers’ repayment decision and serves as the foundation for simulating borrower behavior. Study B, conducted in December 2020, was an incentivized online experiment where participants engaged in the outlined investment game in the role of investors. In this experiment, investors could access an ML model predicting borrowers’ repayment likelihood. Notably, this model, along with the borrowers with whom investors from Study B interacted, originated from Study A data. The data from Study B provided the basis for simulating investor decisions. We present the exact instructions given in these studies in Appendix B.1.

Study A: At the onset of each semester, first-semester economics students from a large German university were recruited to participate in an ongoing field study. The study was conducted by a subset of this paper’s authors and aimed to examine correlations between academic performance, personal characteristics, and behavioral measurements, including outcomes of sequential social dilemmas such as the investment game. The study, accessible via a link sent to students’ email addresses, comprised a comprehensive survey on personal demographics, socioeconomic background, cognitive abilities, personality traits, and, crucially for our simulations, a sequential social dilemma game incorporating our previously described investment game (a detailed description of this game can be found in Appendix B.1). Participants’ decisions were incentivized, allowing for the measurement of revealed preferences, an approach superior to simple self-reported measures due to its potential to reduce presentation and demand effects (Camerer and Hogarth, 1999). The incentives involved earning real money based on the game outcomes with other study participants, ensuring that each observation we used for our simulation represented a real person’s revealed preferences. Importantly, we elicited participants’ behaviors using the strategy method: Borrowers articulated their responses to the investor’s decision before learning about the actual decision. This method allowed us to observe borrower behaviors even if the investor chose not to invest initially, which means we know whether the borrower would have made a repayment. We determined the final game outcome by matching the borrower’s decision with that of the investor. For instance, if a participant expressed an intention to repay if the investor made an investment, and the investor participant indeed decided to invest, the game would lead to the socially optimal investment-repayment outcome <sup>2</sup> (see, e.g., Fischbacher et al., 2012, for the empirical validity of this strategy method approach). We employed the data collected in Study A for two purposes. First, we used it to train an ML model that predicts whether a borrower will repay based on 10 personal characteristics.<sup>3</sup> We introduced initial algorithmic discrimination against female borrowers by successively adjusting the share of repaying female borrowers in the training data from 50% to 37.5%, 25%, 12.5%, and 0% (we refer to these conditions as no, weak, medium, high, and maximum label imbalance, respectively). Second, we used a subset of observations that was not included in the training of the ML model to populate the pool of borrowers in our simulation.

Study B: The other secondary dataset we used for our simulation originated from an incentivized online experiment conducted with US participants on the popular platform Prolific.com. A subset of this paper’s authors collected the data as part of a study examining the interplay between ML models and users’ mental models (see Bauer et al., 2023). We implemented the experiment using oTree 3.3 (Chen et al., 2016), Python 3.8 (van Rossum & Drake, 1995), and HTML5 (W3C, 2014<sup>4</sup>). As part of Study B, participants played 20 rounds of our investment game in the role of the investor, without intermediate feedback. In each round, before participants made their investment decision, they observed 10 personal characteristics of a random borrower and an ML model’s forecast about whether the borrower would make a repayment. The model was trained using data from Study A. Additionally, the borrowers that Study B participants interacted with were also participants from Study A. After they made their decision, the next round started.<sup>5</sup> We leveraged the data from Study B for two purposes. First, we used a share of the data to build an ML model that mimics the investment choices of real participants with specific characteristics deciding to invest with a particular borrower, given the borrower’s personal characteristics and the repayment forecast. Specifically, we trained an ML model that predicted whether an investor would invest with a given borrower using (1) 20 personal characteristics of the investor, (2) 10 observed characteristics of the borrower, and (3) a repayment forecast—in total, 31 features against a binary label (see the Appendix for more details). We exogenously varied the discrimination of investors against female borrowers by successively elevating the probability threshold needed to establish if an investor would actually invest with a female borrower from 50% to 60%, 70%, and 80%. We label these conditions as no, medium, high, and very high human discrimination, respectively. For instance, in the high human discrimination condition, the model mimicking investor behavior requires a prediction that the probability of a given investor investing with a specific female borrower will exceed

70%. This threshold remained at 50% for male borrowers, irrespective of the female threshold. Second, we used a subset of observations that was not included in the training of the investor decision model to populate the pool of investors in our simulation.

## 3.3 Simulation

We implemented our simulations in Python 3.8 (van Rossum & Drake, 1995), making use of popular data science libraries including Pandas 1.53 (McKinney, 2010), NumPy 1.24.2 (Oliphant, 2006), Sklearn 1.2.2 (Pedregosa et al., 2011) and XGBoost 1.7.5 (Chen & Guestrin, 2016). Our simulations unfolded as follows (refer to Figure 3 for a simplified overview).<sup>6</sup> A pool of investors and borrowers engaged in 100 consecutive iterations of the investment game. In each iteration, we randomly paired 50 investors with borrowers, <sup>7</sup> sampling with replacement from their respective pools. Investors viewed 10 personal characteristics of the borrower they were matched with and received a forecast regarding the borrower’s likelihood of repayment upon investment.

![](/api/attachments/VVM428SH/fulltext/images/4947cb7a920970af9e246f8e3784fb65d2d16c84799be812fa3e1ef8b6c50433.jpg)  
Figure 3. Overview of the Simulation Procedure

the experiment outcomes. Specifically, the authors randomly drew a number between 0 and 20. If the drawn number was equal to 20, we contacted and paid the corresponding borrowers according to the game’s outcome. By paying borrowers, the authors aimed to make sure that participants in the experiment made their decisions knowing that there were consequences for other people.

<sup>6</sup> See Appendix C for the source code and the requirements information.

<sup>7</sup> We limited the number of games per iteration to 50 so that the growth of the training dataset was limited. We did so to avoid an initial training dataset that would have been immediately augmented with too many novel observations so that gradual learning could occur. Notably, in additional simulations, we observed that our base results on selfcorrecting effects accelerated (decelerated) when we increased (decreased) the number of pairings to 60 or 70 (30 or 40). The main results on the role of initial algorithmic discrimination and persistent human discrimination hold ceteris paribus. We present these additional analyses in Appendix B.

Armed with this information, the investor decided whether to invest. Notably, in our simulation, we mimicked investor decisions using a trained model (see below for more information). If an investment was made, the borrower decided on repayment, and a new observation encapsulating a borrower’s specific personal traits (features) and actual repayment decision (label) was appended to the dataset used to train the ML model predicting repayment.

Importantly, to avoid inappropriate overfitting and spillover effects, this observation was only included if the dataset didn’t already contain a record of this exact borrower. Conversely, if an investor declined to invest, the individual game concluded without eliciting a repayment decision from the borrower or appending a new observation to the training data. In other words, the growth of the training data was endogenous and selectively included borrowers who received an investment (Lakkaraju et al., 2017). After all decisions were made, the iteration concluded with an update of the ML model predicting repayment by training it from scratch on the expanded dataset incorporating records from all previous iterations and newly collected instances of borrowers who received an investment and made a repayment decision. <sup>8</sup> The next iteration then started, where we again randomly sampled—with replacement—and paired 50 borrowers and investors.

Investors and their decisions: At the outset of each simulation prior to the first iteration, we randomly split Study B data into two equally sized shares. We used the first share (comprising 304 unique individuals with 20 decisions each, yielding 6,080 discrete observations) to train an ML model that simulates whether an investor would choose to invest with a particular borrower, using 31 features (20 personal characteristics of the investor, 10 characteristics of the borrower, and a repayment forecast for the borrower). The employed model is a gradient boosted forest, executed using the XGBoost library in Python (Chen and Guestrin, 2016). We employed an automated process to optimize seven hyperparameters on the training dataset, implementing a three-fold cross-validation strategy in tandem with a directed Bayesian search on the parameter grid. The optimized parameters encompassed the number of trees, learning rate, data subsample used for each tree, maximum depth of a single tree, maximum features by tree and level, and the minimum child weight. We calibrated the model’s performance against the ROC-AUC score. We did so because this score (1) considers both the true positive rate and the false positive rate, (2) is invariant to the classification threshold, and (3) is typically a good choice for imbalanced datasets. Crucially, we trained this model, which simulates investor choices, only once, right before the first iteration of a simulation commenced.

The second random part of our Study B data populated our pool of investors for our simulation (303 unique participants from Study B), whose observations we excluded from the model’s training. Each investor was characterized by their 20 personal attributes, and their investment decisions for a specific borrower were simulated. When a certain investor from the pool was randomly selected in an iteration and paired with a borrower, the trained model predicted whether an investment would occur. The prediction of the likelihood of an investment occurring was based on the investor’s 20 personal characteristics, the borrower’s 10 characteristics, and a repayment forecast for the borrower, i.e., the model leveraged 31 features to predict whether a given investor would invest with a given borrower. An investment took place only if the predicted probability surpassed the threshold of 50% (in the condition where there was no human discrimination). When using the borrowers the individuals from our investor pool actually interacted with in Study B as a true out-of-sample test set and a 50% threshold, we found that, on average, the trained model correctly replicated investor decisions in approximately 70% of the cases.<sup>9</sup>

Borrowers and their repayment predictions: To train the ML model that predicts borrowers’ repayment behavior, we randomly sampled 70% of the data from Study A (without replacement).<sup>10</sup> As input features, the model used the 10 borrower characteristics that were known to the investor. Again, the underlying model was a gradient boosted forest for which we automatically optimized the same seven hyperparameters on the current training dataset using a threefold cross-validation strategy with a directed Bayesian search.<sup>11</sup> We used the remaining 30% of the data from Study A to populate the pool of borrowers in our simulation, from which we randomly drew and matched 50 borrowers with randomly drawn investors from the corresponding investor pool. On average, the unbiased ML model’s accuracy for the share of observations not included in the training before the first updating iteration was 68.4%. <sup>12</sup> As we previously measured borrowers’ repayment decisions using the strategy method in Study A, we knew whether they would make a repayment if there was an investment. Hence, we were able to determine whether the investment game between a given investor and borrower would result in (1) no investment, (2) investment but no repayment, or (3) investment and repayment by matching the unconditional investor with the conditional borrower decisions.

Treatments: We introduced treatment variations along two dimensions: (1) the degree of the initial bias of the repayment-predicting ML model against female borrowers, and (2) the degree of the persistent discrimination by investors against female borrowers. Overall, there were 5×4 different simulation conditions. For each of the 20 conditions, we conducted 15 independent simulations with different random seeds that ensured the randomized partitioning of data from Studies A and B into observations used for initially training the ML models and populating the pools of investors and borrowers. By doing so, we aimed to mitigate concerns of selection bias. To manipulate the initial bias of the ML model predicting borrowers’ repayment, we induced label imbalances (Cowgill & Tucker, 2019) for female observations in the initial training dataset prior to the simulation’s first iteration. We did so by arbitrarily altering the label from repayment to non-repayment for a certain proportion of female observations. Our simulations featured five varying levels of initial bias: no bias (repaying/non-repaying women share at 50/50), low bias (37.5/62.5), medium bias (25/75), high bias (12.5/87.5), and maximum bias (0/100). As our results show, these label imbalances prompted the initial ML model to become more random and, consequently, more error prone concerning women. Notably, we only imbalanced the data immediately prior to the simulation’s initial iteration and did not relabel any additional data that enhanced the original training data throughout the 100 consecutive iterations. To adjust the degree of investor discrimination against female borrowers, we modified the probability threshold that determined whether a particular investor would invest with the matched borrower. Specifically, we successively raised the probability threshold determining an investor’s investment with a female borrower from 50% (no discrimination) to 60% (medium), 70% (high), and 80% (very high), while the male borrower threshold remained at 50%. This variation inherently made investors less likely to invest with a female borrower, manifesting taste-based discrimination (Becker, 1957; Phelps, 1972).

Lastly, we wish to emphasize two aspects of our simulation: First, the type of machine-learning model utilized is not fundamental; we could have also used statistical methods like logistic regression. Further, our training data volume does not qualify as Big Data. The crucial aspect is a continuously updated model—using a batch learning approach—that produces a relatively accurate forecast incorporated into decision-making. Second, the use of the gender attribute is an illustrative example, reflecting a wide array of characteristics on which both algorithms and humans can base discrimination. We chose the gender attribute to underscore discrimination consequences in continuously updated systems based on the ample scientific and anecdotal evidence demonstrating algorithmic discrimination against women (e.g., Sweeney, 2013; Lambrecht & Tucker, 2019).

## 4 Results

In presenting our results, we first analyze the evolution of algorithmic discrimination and economic efficiency under continuously updating ML models in a context devoid of human discrimination, where we specifically examine the impact of varying degrees of initial training data imbalances for the minority class of female borrowers. Subsequently, we investigate the influence of ongoing human discrimination on the progression of algorithmic discrimination and economic efficiency under continuous updating.

![](/api/attachments/VVM428SH/fulltext/images/bc910b62d777e641fda19d96b586e644252d24c8fb1ad878933966ed5db5d430.jpg)  
Note: Panel (i) illustrates outcomes where the initial label imbalance for the minority class was at the maximum, whereas Panel (ii) correspond to conditions with no initial label imbalance  
Figure 4. Progression of the Mean Share of Positive Predictions and False-Negative Error Rates across Iterations, Differentiated by Gender over Time

## 4.1 Continuous Updating and Algorithmic Discrimination

Figure 4 illustrates the temporal evolution of mean shares of positive predictions and false-negative errors in the absence of human discrimination. We present separate results for female (dashed lines) and male borrowers (solid lines). Panel (i) outlines simulation results for our treatment condition with maximum initial training data label imbalance—where there are no repayment examples. Panel (ii) presents results for our control condition without initial label imbalance.

Our findings indicate that the continuous updating of machine learning (ML) models can help reduce algorithmic discrimination over time, as measured by statistical parity. In situations where there was a substantial initial label imbalance leading to disadvantageous predictions for female borrowers (see dashed line without a marker in Panel i), our ML model did not yield any positive predictions for women within the first 10 iterations. In contrast, for male borrowers, we observed a steady positive prediction share of approximately 34%. As evidenced by the convergence of the dashed and solid line without markets, this gender disparity in predictions of repayment, denoting discrimination according to statistical parity, diminished over time with continuous ML model updates. After 100 iterations, the mean positive prediction shares for female and male borrowers were 22% and 36.1%, respectively. Despite this share for female borrowers remaining considerably lower than in the control condition (- 47.3%), ongoing updates of the ML model narrowed the gender gap by approximately two thirds.

Regression results depicted in Table 1 statistically corroborate these insights. In the context of our loan approval scenario, this suggests that continuous updating reduces initial inequality in predicted loan repayment of male and female applicants, thereby approaching statistical parity. Examining falsenegative error rates, <sup>13</sup> i.e., the share of incorrect predictions that a borrower will not make a repayment (see lines with markers), the negatively sloped lines in Panel (i) show that continuous updating similarly reduces these errors for both types of borrowers over time. Initial false-negative rates for female and male borrowers equaled 59.5% and 31.6%, respectively, decreasing to 40.3% and 9.9% after 100 iterations, as evidenced by the development of lines with markers. Notwithstanding these considerable model improvements (see Table 1, Column 2), the gender gap in incorrect predictions that a borrower wil not make a repayment persisted, suggesting that continuous learning does not alleviate relative algorithmic discrimination according to this measure—at least for the maximum initial imbalance case. Intuitively, this outcome implies that continuous updating reduces the likelihood that the model will incorrectly predict a female loan applicant’s default, such that an additional 20 out of 100 loan-deserving female borrowers would receive credit. However, this improvement occurs equally for male applicants, meaning that the gender gap persists over time. In summary, continuous updating improves the ML model’s behavior in terms of positive prediction shares and false-negative rates. However, it only successfully mitigates algorithmic discrimination as measured by the former.

Next, we examine the influence of continuous updating on economic efficiency so that we can gain a better understanding of gains and losses associated with the dynamic evolution of algorithmic discrimination. Figure 5 presents the share of game outcomes mirroring outcomes under perfect information and the instances where investors chose to invest in repaying borrowers. We depict results separately for female (dashed lines) and male borrowers (solid lines). The two panels show the outcomes for our treatment condition with maximum label imbalance (see Panel i) and our control condition without initial label imbalance (see Panel ii). Several crucial insights emerged. In the treatment condition, we observed a considerable negative effect on economic efficiency when the borrower was female, resulting from the initial label imbalance. As shown by the lines without markers in Panel (i), in the first iteration, game outcomes matched the perfect information benchmark in only 42.3% of instances, in the case of a female borrower. Investments with repaying female borrowers in the first iteration were scarce (occurring in 5.7% of cases). In stark contrast, these percentages were significantly higher in our control condition, with values of 61.1% and 47.4%, respectively (see lines without markers in Iteration 1 in Panel ii).

Importantly, indicated by the positive slope of dashed lines in Panel (i), continuous updating of the model led to substantial improvements in both economic efficiency measures for female borrowers over time. Specifically, over 100 iterations, the share of game outcomes matching the perfect information benchmark rose to 62.5%, almost a 50% increase. In the context of our loan approval example, the continuous updating of the ML model thus almost doubled the number of cases where loan officers made the decision they would have made if they could have foreseen the future, accurately identifying which applicants would default and which would not. The frequency of efficient investments in repaying female borrowers, i.e., investments that maximize social welfare, skyrocketed almost sevenfold to 34.8%, signifying an impressive gain in efficiency (see dashed line with marker in Panel i). In our loan approval example, continuous updating of the ML model increased the number of repaying female applicants who could secure credit.

![](/api/attachments/VVM428SH/fulltext/images/f7cb8cbf86f0e0afaaf47c49da578c5967cdd9ea37ae3d75699c29ac08a39d52.jpg)  
Note: We depict the development of the mean share of game outcomes that are equal to outcomes under perfect information and mean shares of games where investors invest in repaying borrowers. We show results separately for female and male borrowers. The left Panel (i) depicts results for the condition where the initial label imbalance for the minority class was at the maximum, whereas the right Panel (ii) depicts results for the condition where there was no initial label imbalance.  
Figure 5. Development of the Mean Share of Game Outcomes

Despite this result, the left panel in Figure 5 indicates that continuous updating could not entirely restore economic efficiency to the level it would have attained in the absence of initial label imbalances in the training data. Nevertheless, our findings underscore significant and noteworthy improvements in economic efficiency concerning female borrowers. For male borrowers, the development of both economic efficiency measures was nearly identical, regardless of the presence or absence of initial label imbalances for women in the training data.

In presenting results for the most extreme label imbalance scenario—where no positive (repaying) examples exist for women—a question naturally arises concerning the role of the initial degree of label imbalance. Does the initial degree of label imbalance influence the ability of continuous updating to mitigate algorithmic discrimination and enhance economic efficiency?

We address this question using regression analyses reported in Table 1 (See Figures A1-A6 in the Appendix for a graphical illustration). Columns (1) and (2) use the gender gap in the ML model’s share of positive predictions and false-negative error rates as dependent variables, respectively. Columns (3) and (4) use the share of game outcomes equivalent to the perfect information benchmark and the share of investments with repaying female borrowers as dependent variables, respectively.<sup>14</sup> Independent variables comprise the time trend, dummy variables indicating the degree of initial label imbalance, and their respective interaction effects. Cases without an initial label imbalance serve as the reference category. We cluster robust standard errors at the random seed level.

Our regression analyses corroborate the robustness of our earlier findings to variation in the degree of initial label imbalance for female borrowers. More precisely, the imbalance degree moderates the self-correcting effect of continuous updating on algorithmic discrimination and economic efficiency. Columns (1) and (2) show that an increase in initial label imbalance results in a higher degree of algorithmic discrimination, as indicated by a larger gender gap in positive predictions and false-negative error rates (refer to dummy variables).

Table 1. OLS Regression Estimates

<table><tr><td></td><td colspan="2">Fairness measures(gender gap)</td><td colspan="2">Economic efficiency(female borrowers only)</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Dep. variable:</td><td>Share of repay predictions</td><td>False-negative error rates</td><td>Outcome under perf. inf.</td><td>Invest in repay. borrower</td></tr><tr><td>Iteration</td><td>-0.0003(0.000)</td><td>-0.0015***(0.000)</td><td>0.0017***(0.000)</td><td>0.0018***(0.000)</td></tr><tr><td>Low lab. imb.</td><td>0.0798***(0.022)</td><td>0.0139(0.022)</td><td>-0.0211*(0.012)</td><td>-0.0699***(0.020)</td></tr><tr><td>Medium lab. imb.</td><td>0.1799***(0.018)</td><td>0.0887***(0.011)</td><td>-0.0668***(0.008)</td><td>-0.1586***(0.011)</td></tr><tr><td>High lab. imb.</td><td>0.3314***(0.020)</td><td>0.1274***(0.019)</td><td>-0.1174***(0.010)</td><td>-0.2937***(0.019)</td></tr><tr><td>Max lab. imb.</td><td>0.3936***(0.019)</td><td>0.1554***(0.021)</td><td>-0.1527***(0.011)</td><td>-0.3699***(0.019)</td></tr><tr><td>Iteration*Low lab. imb.</td><td>-0.0006**(0.000)</td><td>0.0003(0.000)</td><td>-0.0001(0.000)</td><td>0.0003(0.000)</td></tr><tr><td>Iteration*Medium lab. imb.</td><td>-0.0012***(0.000)</td><td>0.0003(0.000)</td><td>0.0002(0.000)</td><td>0.0009***(0.000)</td></tr><tr><td>Iteration*High lab. imb.</td><td>-0.0021***(0.000)</td><td>0.0010***(0.000)</td><td>0.0001(0.000)</td><td>0.0013***(0.000)</td></tr><tr><td>Iteration*Max lab. imb.</td><td>-0.0018***(0.000)</td><td>0.0013***(0.000)</td><td>0.0001(0.000)</td><td>0.0015***(0.000)</td></tr><tr><td>N</td><td>8,880</td><td>8,880</td><td>208,477</td><td>117,309</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.451</td><td>0.238</td><td>0.023</td><td>0.076</td></tr><tr><td colspan="5">Note: We report robust standard errors that are clustered at the random seed level in parentheses. The dependent variables in Columns (1) and (2) are measures for the level of algorithmic discrimination. Specifically, in Column (1), we use the mean gender gap in the share of positive predictions per iteration as dependent variable. In Column (2), we use the mean gender gap in the false-negative error rates per iteration as dependent variable. In Columns (3) and (4), the dependent variables are dummy variables respectively indicating whether a game resulted in the same outcomes as a game under perfect information would have and whether an investor invested in a repaying borrower. For Columns (3) and (4) we only used the subsample of observations where the borrower was female. * p&lt;0.1, ** p&lt;0.05, *** p&lt;0.01 denote statistical significance levels.</td></tr></table>

An analysis of time trends (iteration variable and interaction terms) suggests that continuous updating promotes a quicker reduction in the gender gap regarding positive predictions when the initial imbalance for women is higher. Specifically, high and maximum imbalance levels exhibit a recovery rate twice as high as low and medium levels, respectively (approx. 0.2% vs. 0.1% per iteration). Conversely, time trends in falsenegative error rates present an opposing trend: it is lower for high and maximum label imbalances cases (ca. -0.1 percentage points per iteration). As a result, we find a significant decline in the gender gap in the false-negative error rate for the low and medium imbalance conditions only—however, not in the most extreme case (the coefficients for Iteration and Iteration\*High/Max lab. imb. cancel each other out). Column (3) shows that the increase in the share of game outcomes that match the perfect information benchmark (for female borrowers) is consistent across conditions (approx. +0.2 percentage points per iteration). However, the initial degree of economic efficiency diminishes with increasing label imbalance. Regarding the optimal investment with repaying female borrowers (Column 3), the positive time trend is higher in medium, high, and maximum label imbalance conditions (respectively +0.09, +0.13, +0.15 percentage points) than in situations with low or no initial label imbalance (reference category).

In summary, our findings highlight that the observed selfcorrection properties of continuous updating are moderated by the degree of initial label imbalance in the training data. This holds, in particular, for algorithmic discrimination as measured by the gender gap in falsenegative error rates. These results, when interpreted in the context of our loan approval example, suggest that the extent of historical discrimination against female applicants, as reflected in the training data, influences the effectiveness of continuous model updating in mitigating the gender gap in the ML prediction model. This result holds for both the gap in the likelihood that the model will predict male and female applicants to be creditworthy (statistical parity) and the gap in the likelihood that it will incorrectly predict creditworthy male and female applicants not to be creditworthy (false-error rate). Notably, independent of the discrimination encoded in the initial training data, continuous learning always increases the number of optimal loan approval decisions for female applicants and thus the number of repaying female borrowers who can secure credit.

Result 1: In the presence of a label imbalance in the initial training dataset, continuous updating can help improve model performance, mitigate algorithmic discrimination (according to statistical parity), and enhance economic efficiency over time. The selfcorrection capabilities are contingent on the degree of the initial level of algorithmic discrimination.

Despite our findings suggesting that the continuous updating of the ML model reduces algorithmic discrimination and enhances economic efficiency, a pivotal question remains: If human decision makers who use the ML prediction as a decision aid continue to discriminate against women, would the ML model learn to perpetuate these discriminatory patterns under continuous updating? If this were to prove true, continuous updating could impair initially fair and economically efficient ML models over time, creating substantial risks and undermining the above-described benefits. In the second part of our analyses below, we examine the role of discrimination by human decision makers.

## 4.2 The Role of Human Discrimination

To study the role of discrimination by a human decision maker, we examine how our results differed in simulations where we exogenously decreased investors’ probability to invest with female borrowers. Figure 6 shows that the share of positive predictions (the two panels at the top) and false-negative rates (two panels at the bottom) for female borrowers depends on the level of human discrimination and the degree of the initial label imbalance. To illustrate the change over time in a parsimonious way, we present the visualization for the first and the last iteration only.

Figure 6 reveals that the effectiveness of continuously updating an ML model in mitigating algorithmic discrimination diminishes in the presence of discrimination by human decision makers. Specifically, the extent of human discrimination negatively impacts the growth of positive predictions for female borrowers across iterations, regardless of the initial label imbalance. For instance, a comparison of the upper two panels shows that at the maximum label imbalance (x-axis), the share of positive predictions (y-axis) for women increases from 0% in Iterations 1 (left panel) to 22% in Iteration 100 (right panel) if there is no human discrimination (z-axis). However, this growth is significantly curtailed, reaching merely 1.2%, 6.9%, 14.3% under very high, high, and medium human discrimination, respectively.

Conversely, human discrimination against women does not alter the share of positive predictions for male borrowers (see Figure A7 in the Appendix), regardless of the initial label imbalance. For example, at maximum label imbalance, the positive predictions for men minimally fluctuate, moving from 34.4% to 36.1% without human discrimination and to 33.8% with very high human discrimination (36.3% and 34.2% for high and medium levels of human discrimination, respectively). Our regression analyses (see Table A2 in the Appendix) statistically corroborate these findings. Regression estimates in Column (1) suggest that for an initially unbiased model under high and very high human discrimination, the gender gap widens by about 0.07 percentage points per iteration, or 7 percentage points across all 100 iterations.

![](/api/attachments/VVM428SH/fulltext/images/a0c30604290e1d1f716bdcc8ccf54ea638fe7f6410e4bfcf7e7f9c3fab384bb6.jpg)  
Note: We illustrate how the mean share of positive predictions and mean false-negative error rates for female borrowers in Iterations 1 and 100 depend on the initial label imbalance in the training data and the degree of human discrimination by the investor. A comparison of panels for Iterations 1 and 100 for the two measures of algorithmic discrimination provides insights into their conditional development across iterations. Abbreviations: False-neg. rate = false-negative rate; Init. lab. imb. = initial label imbalance; Human discr. = human discrimination.  
Figure 6. Development of the Mean Share of Positive Predictions and False-Negative Error Rates

Figure 6 also shows that an increase in human discrimination undermines the reduction in falsenegative error rates for female borrowers over time. For instance, the lower two panels show that with a high initial label imbalance (x-axis), the false-negative error rate (y-axis) for female borrowers decreases from 55.4% in Iteration 1 (left panel) to 35.8% in Iteration 100 (right panel) if there is no human discrimination (z-axis). However, under very high human discrimination, this rate only drops to 52.2% in Iteration 100 (49.6% and 46.9% for high and medium levels of human discrimination, respectively).

We found that the false-negative error rates for male borrowers remained unaffected by the level of human discrimination. With a high initial label imbalance, these rates varied from around 30% to 15%, 14.4%, 14.5%, and 17.2% under conditions of very high, high, medium, and no human discrimination, respectively. Again, our regression analyses (see Table A3 in the Appendix) underscore these patterns statistically, suggesting that higher levels of human discrimination exacerbate the negative effect on the reduction of algorithmic discrimination over time. Interestingly, regression analysis also suggests a significant increase in the gender gap over time under high or maximum initial label imbalance combined with high or very high levels of human discrimination (see Columns 4 and 5).

In sum, these results emphasize that the capacity of continuous ML model updating to mitigate algorithmic discrimination critically relies on the absence of discriminatory behavior by human decision makers. If such behaviors persist—potentially giving rise to the initial label imbalance in the training data—continuous updating has a minimal effect on improving the ML model’s behavior toward the discriminated group. Our findings even suggest that human discrimination can cause ML models, originally trained on balanced data and displaying no algorithmic discrimination, to adopt increasingly discriminatory behaviors, as measured by statistical parity. In the context of our loan approval example, the results reveal that the efficacy of continuously updated ML models notably declines if a loan officer persistently discriminates against female applicants, regardless of the creditworthiness assessment generated by the ML model. Consequently, the ML model’s prediction may persistently demonstrate gender disparity across two key dimensions: the ML model’s propensity to deem female applicants as creditworthy and its erroneous categorization of creditworthy female borrowers as unqualified for credit. Alarmingly, in instances of extreme bias exhibited by the loan officer, even ML models that are originally unbiased may begin to assimilate the discriminatory behaviors manifested by the human participant in the process.

![](/api/attachments/VVM428SH/fulltext/images/8cdf5237912a8ceb1710bb8bc61c7ee0c8e9505ec9f0fd0758c5b8d9fd900931.jpg)  
Note: We illustrate how the mean share of games that result in the outcome as if the game was played under perfect information and the mean share of games where investors invest with a repaying borrower in Iterations 1 and 100 depend on the initial label imbalance in the training data and the degree of human discrimination by the investor. We depict results in case the borrower is female- A comparison of panels for Iterations 1 and 100 for the two measures of algorithmic discrimination provides insights into their conditional development across iterations. Abbreviations: Outcome under perf. inf. = outcome under perfect information; Init. lab. imb. = initial label imbalance; Human discr. = human discrimination.

## Figure 7. Development of the Mean Share of Games under Perfect Information

Figure 7 portrays changes in our two economic efficiency measures (share of outcomes as under perfect information in the upper two panels; share of investments with repaying borrowers in the lower two panels) for female borrowers from Iteration 1 to 100, conditional on combinations of initial label imbalances (x-axis) and the extent of persistent human discrimination (z-axis).<sup>15</sup> Echoing our results on the role of human discrimination in mitigating algorithmic discrimination over time, we found that the ability of continuous updating to enhance economic efficiency decreases as human discrimination intensifies. For instance, a comparison of the upper two panels shows that when the initial label imbalance is at its maximum (x-axis), the share of game outcomes with female borrowers that match the perfect information benchmark (y-axis), grows from 42.3% In Iteration 1 (left panel) to 62.5% in Iteration 100 (right panel) if there is no human discrimination (z-axis). A similar comparison of the two panels at the bottom reveals that the share of investments with repaying borrowers also grows from 5.7% in Iteration 1 (left panel) to 34.9% in Iteration 100 (right panel).

Conversely, under conditions of medium, high, and very high human discrimination, the share of perfect information game outcomes (investments with repaying borrowers) only grows to 52%, 49.1%, and 46.1% (18.5%, 8.6%, and 1.5%), respectively, in Iteration 100. Importantly, the finding regarding investments with repaying borrowers reveals that discrimination against female borrowers does not cause an over-proportional increase in training data with examples of repaying women, a scenario that could facilitate faster mitigation of the label imbalance problem in the data. Instead, discrimination appears to hinder the collection of observations for female borrowers. For male borrowers, our results do not indicate any impact of human discrimination against female borrowers on economic efficiency. Our statistical analyses, as detailed in Tables A6 and A7 in the Appendix, corroborate these findings. Furthermore, they reveal a decrease in the self-correction capabilities associated with continuous updating with increasing levels of human discrimination.

Taken together, our analyses reveal that in the context of continuously updated ML decision support, human discrimination has a dual negative impact. Not only does it immediately degrade economic efficiency by leading humans to make suboptimal decisions—in this case, failing to invest in female borrowers who would actually repay in the future—it also hampers the ability of continuous updating to enhance model performance and, subsequently, the efficiency of human decisionmaking over time.

Result 2: The continuous updating of ML models loses its ability to mitigate algorithmic discrimination and improve economic efficiency when human decision makers who use ML predictions as decision support continue to discriminate against the minority class (female borrowers).

## 5 Discussion and Conclusion

## 5.1 Summary of Main Findings

Drawing on extensive simulations, our paper demonstrates that the continuous updating of machine learning (ML) models, based on data they endogenously help generate, can enhance performance, alleviate algorithmic discrimination, and boost the economic efficiency of ML models initially grappling with label imbalances in the original training dataset. The ability for self-correction inversely depends on the degree of initial label imbalance: the more biased the ML model’s predictions are at the outset, the less capacity it has for recovery through continuous updating over time. Crucially, our research indicates that persistent discrimination by humans— who make the final decisions in ML-supported tasks— significantly impedes the self-correction abilities associated with the continuous updating of ML models. Our findings even suggest that ongoing human discrimination can lead ML models, originally trained on balanced data and demonstrating no algorithmic discrimination, to exhibit increasingly discriminatory behavior over time.

## 5.2 Theoretical Contributions and Implications

Our study responds to recent calls for empirical investigations into the sociotechnological nature of algorithmic discrimination in environments where ML models continue to learn based on data they help to generate (e.g., Kordzadeh & Ghasemaghaei, 2022; Dolata et al., 2022). Our results highlight the vital role of continuously updating ML models in the evolution of algorithmic discrimination over time. We provide empirical evidence that modern ML models, initially producing biased outcomes due to imbalances in the training data, can self-correct if they regularly receive the data they help generate. In the absence of persistent human discrimination, we uncovered a feedback loop in which the ML model becomes increasingly unbiased by updating using novel training data it helped generate. To the best of our knowledge, we are the first to document a bias-reducing feedback loop, thereby showcasing the impressive learning capabilities of contemporary ML models. Theoretically, this selfcorrection mechanism underscores the dynamic nature inherent to these models, adding a new dimension to the algorithmic fairness literature by shifting from static, one-time biases to a more temporal perspective: a comprehensive understanding of algorithmic discrimination and fairness must incorporate not just the initial conditions under which a model is trained, but also the dynamic environments where these models operate and evolve. Our results suggest that continuous model updating could serve as a mechanism for mitigating bias in ML systems and might act as a force to supplement traditional data cleaning and debiasing efforts (Shrestha et al., 2019) to reduce discrimination risks.

On the other hand, our simulations reveal that the positive impact of continuous updating on algorithmic discrimination (and economic efficiency) largely hinges on the sociotechnological environment, which includes the degree of the system’s initial bias and, perhaps more importantly, the persistence of biased decision-making by humans in the loop. We found that the greater the extent of human discrimination in a dynamic system where ML models are continuously updated, the less likely it is that self-correcting mechanisms will occur. We even observed that unbiased models learn biased behaviors from humans over time. This happens because humans interfere with the endogenous creation of new observations, further reducing the chance that the existing training data can be supplemented with observations enabling the model to make better predictions for the initially disadvantaged group. This observation supports the arguments of IS researchers to consider (and examine) algorithmic discrimination as a sociotechnological phenomenon (e.g., Favaretto et al., 2019). According to our findings, in environments where ML models are continuously updated, the behavior of human decision makers who observe ML predictions but have the final say may be a crucial factor in understanding and potentially even anticipating persistent algorithmic discrimination. Biases in human decision-making may directly influence the behavior of continuously updated ML models. While modern machine learning models inherently possess the capability to “unlearn” initial biases over time given sufficiently diverse and unbiased data, human biases can impede this process. This insight is especially relevant in the current era of growing political and social divisions in human societies (e.g., Allcott et al., 2020). When people increasingly adopt biased attitudes and behaviors, biased, continuously updated ML models are less likely to correct themselves over time. Thus, human behavior serves as a channel through which larger sociopolitical trends can influence the performance of ML technologies. In a broader sense, our work thereby underscores that the potential learning of ML systems from human decision makers is a critical factor to consider when designing effective sociotechnological systems. This complements prior work pointing to the dynamic, possibly bidirectional learning processes between humans and ML systems (e.g., Abdel-Karim et al., 2023, Bauer et al., 2023).

From the perspective that algorithmic and human discrimination in our study can be understood as relating to the phenomenon of ML model drift, our findings suggest that the success of continuous updating in addressing concept drift hinges on the presence of data drift. Specifically, if we consider that the imbalance in the initial training dataset stems from a data-generating process distinct from subsequent simulation iterations, then the ML model’s bias against women essentially emerges from a concept drift (Widmer & Kubat, 1996). This means the initial ML model approximates a once-accurate but now outdated data-generating process. The observed feedback loop, where the ML model progressively becomes less biased, then demonstrates its ability to overcome concept drifts when updated with new training data it influences. Conversely, persistent human discrimination shifts the training data’s gender composition, increasingly diverging from the borrower pool over iterations. However, the core relationship between borrower attributes and their repayment propensity remains unchanged. Thus, ongoing human discrimination aligns with an ongoing data drift (Mallick et al., 2022), as the incoming data’s composition on which the model predicts, deviates from its training data. With biased decision-making by humans in the loop undermining the discriminating ML model’s capacity to self-correct, i.e., overcome concept drift through continuous updating, one may interpret our findings as evidence for an adverse interaction between a data and a concept drift that allows algorithmic discrimination to persist. This observation provides a new perspective on the dynamic between concept and data drift challenges, enriching prior research on drift origins and its mitigation (see, e.g., Lu et al., 2018; Jameel et al., 2020; Sahiner et al., 2023).

## 5.3 Practical Implications

From a practical standpoint, our results underscore the necessity for organizations and policymakers to consider both the dynamic and the sociotechnological nature of algorithmic discrimination. Our findings, highlighting the influence of human behavior on the discriminatory outcomes of continuously updated ML models, suggest that organizations should not only focus on reducing bias within ML models but also diligently address potential bias within the human decision-making processes that these models support. The implication for organizations is that they need to invest in comprehensive anti-discrimination and unconscious bias training for their decision makers. This training could span various areas, such as understanding the potential of unconscious biases and the potential impact of these biases on ML models. Initiatives like these could be instrumental in creating an awareness of biases, reducing their influence on human decision-making and, consequently, on continuously updated ML models. In addition, organizations should consider developing guidelines and protocols for their decision makers that explicitly detail how to interact with ML models and their predictions. Furthermore, our results highlight additional technical benefits of organizational policies and procedures that emphasize the importance of diversity and inclusiveness. These may help mitigate (unseen) discriminatory behaviors of ML models in the long term. Organizations adopting a dynamic sociotechnological perspective might succeed in creating a more equitable, effective, and efficient use of ML models. This approach aligns with societal expectations and regulatory requirements.

From a policymaker’s perspective, our findings regarding human involvement become particularly significant in light of impending regulations that mandate human participation in ML decision-making processes. These regulations pertain to final decisions in high-risk scenarios such as loan approval and hiring processes, as outlined in Article 22 of the General Data Protection Regulation and the European Commission’s Artificial Intelligence Act. However, our findings indicate a potential risk when humans have the final say in ML-supported decision-making processes. If individuals engage in discriminatory practices and the models update continuously, there is a risk of unintentionally perpetuating or amplifying algorithmic discrimination, as human discrimination hinders the selfcorrecting capacities of ML models. Therefore, in conjunction with these regulations, we advocate measures aimed at identifying and mitigating (subconscious) discriminatory practices by organizational decision makers. These measures could serve as essential complementary elements to ensure that continuously updated ML models demonstrate desirable behaviors when organizations implement regulatory requirements that involve humans in the decision loop.

## 5.4 Limitations and Future Research

Like any study, this study also has limitations—which, we believe, provide valuable directions for future research to enhance our understanding of how algorithmic discrimination evolves in environments where ML models undergo continuous updates. One such limitation involves our assumption that investors in our simulation neither recognize the ML system’s bias nor its general performance and reliability. Consequently, they can neither learn from the ML model nor adjust their reliance on the ML model based on observed performance. We impose this assumption to reduce complexity and because our empirical data did not permit us to include such conditions without making additional conjectures about human investors’ learning capacities. However, this naturally constrains the social dynamics of algorithmic discrimination. On the one hand, it is plausible that ML system users recognize its discriminatory output, thereby reducing their reliance on the model’s predictions over time (Jussupow et al., 2020). When humans override biased ML predictions, they can effectively help generate new training observations that would not have been available if they had followed the prediction. In a retraining process, these new observations could help the ML system overcome its biases, positioning the human user in a vital role of exploration. On the other hand, previous research has shown that humans can learn from ML-based systems due to induced reflections (Abdel-Karim et al., 2023). In this context, it is conceivable that human investors learn to discriminate against female borrowers if they observe the ML model doing so. As a result, a complex, selfreinforcing interplay between human and algorithmic discrimination may emerge, thereby preventing selfcorrection processes. Future work should integrate both perspectives and evaluate the dynamics of a human-in-the-loop system where the human and ML system engage in a bidirectional learning circle.

Another limitation of our study pertains to the batch learning methodology employed to update models. This technique retrains the learning algorithm on all the currently available training data, essentially generating a new model from the full dataset (Asatiani et al., 2020). This approach does not incorporate new data incrementally but processes the entire dataset anew. We chose this method for its empirical simplicity and efficiency, particularly with tree-based techniques like the gradient boosted forest we used. Future research might explore the robustness of our results under online learning processes, where model parameters are continuously updated based on incoming data. Unlike batch learning, online learning does not typically retrain the model from scratch; it refines the current model using only new data. This might reduce the influence of the original training data’s composition, as updates are based solely on novel information. Understanding the role of the updating process in self-correcting effects is crucial, especially in contexts where retraining models from scratch is computationally prohibitive.

A third limitation of our study is that we did not consider the impact of continuous model updating when human decision makers treat female borrowers advantageously, i.e., positively discriminate by being more likely to invest, all other things being equal. Affirmative action policies promoting equal opportunity could prompt this type of positive discrimination. Under these conditions, the self-correcting mechanism of continuous learning might work more effectively, as the generation of more diverse training data could help the ML model unlearn discriminatory patterns. In this regard, continuous model updating might enhance the benefits of affirmative action policies by augmenting data and improving ML predictions for minority or disadvantaged groups over time. Although we did not examine this aspect of human and ML model interaction, we hope that future research will address this in order to help policymakers anticipate the sociotechnological consequences of particular policies.

Finally, our study does not address scenarios in which the decisions of human users, influenced by the observed ML prediction, subsequently affect the ground truth that the ML model aims to predict. In our simulation, for instance, an investor’s choice not to invest with a certain borrower did not inherently alter the borrower’s underlying likelihood of repayment in the future. Nonetheless, numerous situations exist where this is the case. Consider, for example, a situation where a judge uses a continuously updated ML model as a decision support tool when determining whether to release a defendant on bail. In case the ML model incorrectly predicts a high recidivism risk score and the defendant consequently remains incarcerated, the time spent in jail could indeed increase the likelihood of the defendant reoffending in the future. As a result, the ML prediction not only endogenously shapes the data available for future updates but also alters the “ground truth” the model aims to predict. In a sense, predictions that are incorrect ex ante become a self-fulfilling prophecy ex post (Falk & Kosfeld, 2006; Bauer & Gill, 2023). The added complexity of this endogeneity to the analysis of the evolution of algorithmic discrimination is noteworthy, even though it was not the focus of this study. We propose this as a fruitful avenue for future research because it may provide a more holistic view on the dynamic consequences of algorithmic discrimination.

## 5.5 Concluding Remarks

A final remark is worth making. Of course, our work is not meant to be an argument, much less a plea, for the hasty deployment of untested, potentially discriminatory ML systems in organizational or business processes with the hope that continuous updating might alleviate adverse ML behaviors.

Indeed, self-correcting mechanisms may require time to take effect, during which disadvantaged social groups may continue to endure discriminatory practices. Rather, we perceive our findings as a testament to the substantial learning capabilities of modern ML models undergoing continuous updating. We argue that these capabilities can complement other interventions aimed at addressing algorithmic discrimination, such as the proper preprocessing of training data. This approach is particularly effective when organizations take measures to ensure that their employees do not engage in (subconscious) discriminatory practices during ML-supported decision-making processes. However, overreliance on the self-correcting aspects of continuous updating processes could cause significant damage to both an organization’s economic performance and reputation if ML systems are deployed hastily without rigorously testing for and addressing algorithmic discrimination.

## References

Abdel-Karim, B., Pfeuffer, N., Carl, V., & Hinz, O. (2023). How AI-Based Systems Can Induce Reflections: The Case of AI-Augmented Diagnostic Work, MIS Quarterly, 47(4)

Ågerfalk, P. J. (2020). Artificial intelligence as digital agency. European Journal of Information Systems, 29(1), 1-8.

Adomavicius, G., Bockstedt, J. C., Curley, S. P., & Zhang, J. (2018). Effects of online recommendations on consumers’ willingness to pay. Information Systems Research, 29(1), 84- 102.

Agrawal, A., Gans, J. S., & Goldfarb, A. (2019). Exploring the impact of artificial intelligence: Prediction versus judgment. Information Economics and Policy, 47, 1-6.

Allcott, H., Boxell, L., Conway, J., Gentzkow, M., Thaler, M., & Yang, D. (2020). Polarization and public health: Partisan differences in social distancing during the coronavirus pandemic. Journal of Public Economics, 191, Article 104254.

Arrow, K. J. (1972). Some mathematical models of race discrimination in the labor market. In A. H. Pascal (Ed.), Racial discrimination in economic life (pp. 187-204). D.C. Heath.

Asatiani, A., Malo, P., Nagbøl, P. R., Penttinen, E., Rinta-Kahila, T., & Salovaara, A. (2020). Challenges of explaining the behavior of blackbox AI systems. MIS Quarterly Executive, 19(4), 259-278.

Athey, S. (2018). The impact of machine learning on economics. In A. Agrawal, J. Gans, & A. Goldfarb (Eds.), The economics of artificial intelligence: An agenda (pp. 507-547). University of Chicago Press.

Baker, R. S., & Hawn, A. (2021). Algorithmic bias in education. International Journal of Artificial Intelligence in Education, 32, 1052-1092.

Barocas, S., & Selbst, A. D. (2016). Big data’s disparate impact. California Law Review, 104(3), 671ff.

Bauer, K., & Gill, A. (2023). Mirror, mirror on the wall: Algorithmic assessments, transparency, and self-fulfilling prophecies. Information Systems Research, 35(1), 226-248.

Bauer, K., von Zahn, M., & Hinz, O. (2023). Expl (AI) ned: The impact of explainable artificial intelligence on users’ information processing. Information Systems Research, 34(4), 1582- 1602.

Becker, G. S. (2010). The economics of discrimination. University of Chicago Press.

Benbya, H., Davenport, T. H., & Pachidi, S. (2020). Artificial intelligence in organizations: current state and future opportunities. MIS Quarterly Executive, 19(4), ix-xxi.

Berente, N., Gu, B., Recker, J., & Santhanam, R. (2021). Managing artificial intelligence. MIS Quarterly, 45(3), 1433-1450.

Berg, J., Dickhaut, J., & McCabe, K. (1995). Trust, reciprocity, and social history. Games and Economic Behavior, 10(1), 122-142.

Bergson, A. (1983). Pareto on social welfare. Journal of Economic Literature, 21(1), 40-46.

Besse, P., del Barrio, E., Gordaliza, P., Loubes, J. M., & Risser, L. (2022). A survey of bias in machine learning through the prism of statistical parity. The American Statistician, 76(2), 188-198.

Bridge, O., Raper, R., Strong, N., & Nugent, S. E. (2021). Modelling a socialised chatbot using trust development in children: lessons learnt from Tay. Cognitive Computation and Systems, 3(2), 100-108.

Brown, M., Falk, A., & Fehr, E. (2004). Relational contracts and the nature of market interactions. Econometrica, 72(3), 747-780.

Buolamwini, J., & Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in commercial gender classification. Proceedings of the Conference on Fairness, Accountability and Transparency (pp. 77-91).

Burghardt, K., & Lerman, K. (2022). Emergent instabilities in algorithmic feedback loops. arXiv. https://arxiv.org/abs/2201.07203

Calders, T., & Verwer, S. (2010). Three naive Bayes approaches for discrimination-free classification. Data Mining and Knowledge Discovery, 21(2), 277-292.

Camerer, C. F., & Hogarth, R. M. (1999). The effects of financial incentives in experiments: A review and capital-labor-production framework. Journal of Risk and Uncertainty, 19(1), 7-42.

Carlsson, F., Johansson-Stenman, O., & Nam, P. K. (2014). Social preferences are stable over long periods of time. Journal of Public Economics, 117, 104-114.

Charness, G., Gneezy, U., & Halladay, B. (2016). Experimental methods: Pay one or pay all. Journal of Economic Behavior & Organization, 131, 141-150.

Chen, T., & Guestrin, C. (2016). Xgboost: A scalable tree boosting system. In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 785-794).

Chen, D. L., Schonger, M., & Wickens, C. (2016). oTree: An open-source platform for laboratory, online, and field experiments. Journal of Behavioral and Experimental Finance, 9, 88- 97.

Cheung, H. K., King, E., Lindsey, A., Membere, A., Markell, H. M., & Kilcullen, M. (2016). Understanding and reducing workplace discrimination. Research in Personnel and Human Resources Management, 34, 101-152.

Chi, J., Tian, Y., Gordon, G. J., & Zhao, H. (2021). Understanding and mitigating accuracy disparity in regression. Proceedings of the International Conference on Machine Learning (pp. 1866-1876).

Chouldechova, A. (2017). Fair prediction with disparate impact: A study of bias in recidivism prediction instruments. Big Data, 5(2), 153- 163.

Chouldechova, A., Benavides-Prado, D., Fialko, O., & Vaithianathan, R. (2018). A case study of algorithm-assisted decision making in child maltreatment hotline screening decisions. Proceedings of the Conference on Fairness, Accountability and Transparency (pp. 134- 148).

Corbett-Davies, S., Pierson, E., Feller, A., Goel, S., & Huq, A. (2017). Algorithmic decision making and the cost of fairness. Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 797-806).

Corbett-Davies, S., & Goel, S. (2018). The measure and mismeasure of fairness: A critical review of fair machine learning. arXiv. https://arxiv.org/ abs/1808.00023

Cowgill, B. (2018). The impact of algorithms on judicial discretion: Evidence from regression discontinuities [Unpublished manuscript]. Columbia Business School.

Cowgill, B., & Tucker, C.E. (2017). Algorithmic bias: A counterfactual perspective (Working paper). NSF Trustworthy Algorithms.

Cowgill, B., & Tucker, C. E. (2019). Economics, fairness and algorithmic bias. SSRN https://papers.ssrn.com/sol3/papers.cfm?abstra ct\_id=3361280

Csaszar, F. A., Jue-Rajasingh, D., & Jensen, M. (2022). When less is more: how statistical discrimination can decrease predictive accuracy. Organization Science, 34(4), 1383- 1399.

Cunningham, G. B. (2009). The moderating effect of diversity strategy on the relationship between racial diversity and organizational performance. Journal of Applied Social Psychology, 39(6), 1445-1460.

d’Alessandro, B., O’Neil, C., & LaGatta, T. (2017). Conscientious classification: A data scientist’s guide to discrimination-aware classification. Big Data, 5(2), 120-134.

Dastin, J. (2018). Amazon scraps secret AI recruiting tool that showed bias against women. In K. Martin (Ed.), Ethics of data and analytics (pp. 296-299). Auerbach Publications.

Domnich, A., & Anbarjafari, G. (2021). Responsible AI: Gender bias assessment in emotion recognition. https://arxiv.org/abs/2103.11436

Dolata, M., Feuerriegel, S., & Schwabe, G. (2022). A sociotechnical view of algorithmic fairness. Information Systems Journal, 32(4), 754-818.

Dressel, J., & Farid, H. (2018). The accuracy, fairness, and limits of predicting recidivism. Science Advances, 4(1), Article eaao5580.

Dufwenberg, M., & Kirchsteiger, G. (2004). A theory of sequential reciprocity. Games and Economic Behavior, 47(2), 268-298.

Ebrahimi, S., & Hassanein, K. (2019). Can the use of data analytics tools lead to discriminatory decisions? Proceedings of the 52nd Hawaii International Conference on System Sciences.

Ensign, D., Friedler, S. A., Neville, S., Scheidegger, C., & Venkatasubramanian, S. (2017). Runaway feedback loops in predictive policing. arXiv. https://arxiv.org/abs/1706.09847

Ewens, M., Tomlin, B., & Wang, L. C. (2014). Statistical discrimination or prejudice? A large sample field experiment. Review of Economics and Statistics, 96(1), 119-134.

Falk, A. & Kosfeld, M. (2006). The hidden costs of control. American Economic Review, 96(5), 1611-1630.

Favaretto, M., De Clercq, E., & Elger, B. S. (2019). Big Data and discrimination: perils, promises and solutions. A systematic review. Journal of Big Data, 6(1), 1-27.

Fazelpour, S., & Danks, D. (2021). Algorithmic bias: Senses, sources, solutions. Philosophy Compass, 16(8), Article e12760.

Fehr, E., & Fischbacher, U. (2003). The nature of human altruism. Nature, 425(6960), 785-791.

Fehr, E., Kirchsteiger, G., & Riedl, A. (1993). Does fairness prevent market clearing? An experimental investigation. The Quarterly Journal of Economics, 108(2), 437-459.,

Feldman, M., Friedler, S. A., Moeller, J., Scheidegger, C., & Venkatasubramanian, S. (2015). Certifying and removing disparate impact. Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 259-268).

Fischbacher, U., Gächter, S., & Quercia, S. (2012). The behavioral validity of the strategy method in public good experiments. Journal of Economic Psychology, 33(4), 897-913.

Forret, M. L., & Dougherty, T. W. (2004). Networking behaviors and career outcomes: differences for men and women? Journal of Organizational Behavior, 25(3), 419-437.

Friedman, B., & Nissenbaum, H. (1996). Bias in computer systems. ACM Transactions on Information Systems, 14(3), 330-347.

Fu, R., Huang, Y., & Singh, P. V. (2021). Crowds, lending, machine, and bias. Information Systems Research, 32(1), 72-92

Fudenberg, D., & Tirole, J. (1991). Game theory. MIT Press.

Gupta, U., Ferber, A., Dilkina, B., Steeg, G. (2021). Controllable guarantees for fair outcomes via contrastive information estimation. Proceedings of the AAAI Conference on Artificial Intelligence, 35(9), 7610-7619.

Guryan, J., & Charles, K. K. (2013). Taste‐based or statistical discrimination: The economics of discrimination returns to its roots. The Economic Journal, 123(572), F417-F432.

Haas, C. (2019). The price of fairness—A framework to explore trade-offs in algorithmic fairness. Proceedings of the 40th International Conference on Information Systems.

Hardt, M., Price, E., & Srebro, N. (2016). Equality of opportunity in supervised learning. Proceedings of the 30th Conference on Neural Information Processing Systems.

Heidari, H., Ferrari, C., Gummadi, K., & Krause, A. (2018). Fairness behind a veil of ignorance: A welfare analysis for automated decision making. Proceedings of the 32nd Conference on Neural Information Processing Systems.

Hoffman, M., Kahn, L. B., & Li, D. (2018). Discretion in hiring. The Quarterly Journal of Economics, 133(2), 765-800.

Hormel, U., & Scherr, A. (2010). Diskriminierung. VS Verlag für Sozialwissenschaften.

Horton, J. J. (2017). The effects of algorithmic labor market recommendations: Evidence from a field experiment. Journal of Labor Economics, 35(2), 345-385.

Hu, L., & Chen, Y. (2020). Fair classification and social welfare. Proceedings of the Conference on Fairness, Accountability, and Transparency (pp. 535-545).

Jameel, S. M., Hashmani, M. A., Alhussain, H., Rehman, M., & Budiman, A. (2020). A critical review on adverse effects of concept drift over machine learning classification models. International Journal of Advanced Computer Science and Applications, 11(1). http://dx.doi. org/10.14569/IJACSA.2020.0110127

Johansson, F., Shalit, U., & Sontag, D. (2016, June). Learning representations for counterfactual inference. Proceedings of the International Conference on Machine Learning (pp. 3020- 3029).

Jussupow, E., Spohrer, K., Heinzl, A., & Gawlitza, J. (2021). Augmenting medical diagnosis decisions? An investigation into physicians decision-making process with artificial intelligence. Information Systems Research, 32(3), 713-735.

Kahalé, N. (2020). Randomized dimension reduction for Monte Carlo simulations. Management Science, 66(3), 1421-1439.

Kamiran, F., & Calders, T. (2012). Data preprocessing techniques for classification without discrimination. Knowledge and Information Systems, 33(1), 1-33.

Kleinberg, J., Lakkaraju, H., Leskovec, J., Ludwig, J., & Mullainathan, S. (2018). Human decisions and machine predictions. The Quarterly Journal of Economics, 133(1), 237-293.

Kleinberg, J., Ludwig, J., Mullainathan, S., & Sunstein, C. R. (2020). Algorithms as discrimination detectors. Proceedings of the National Academy of Sciences, 117(48), 30096- 30100.

Kordzadeh, N., & Ghasemaghaei, M. (2022). Algorithmic bias: review, synthesis, and future research directions. European Journal of Information Systems, 31(3), 388-409.

Köchling, A., & Wehner, M. C. (2020). Discriminated by an algorithm: a systematic review of discrimination and fairness by algorithmic decision-making in the context of HR recruitment and HR development. Business Research, 13(3), 795-848.

Kusner, M. J., & Loftus, J. R. (2020). The long road to fairer algorithms. Nature, 578(7793), 34-36.

Lahey, J. N. (2008). Age, women, and hiring an experimental study. Journal of Human Resources, 43(1), 30-56.

Lakkaraju, H., Kleinberg, J., Leskovec, J., Ludwig, J., & Mullainathan, S. (2017). The selective labels problem: Evaluating algorithmic predictions in the presence of unobservables. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 275-284).

Lakkaraju, H., & Rudin, C. (2017). Learning costeffective and interpretable treatment regimes. Proceedings of the 20th International Conference on Artificial Intelligence and Statistics (pp. 166-175).

Lambrecht, A., & Tucker, C. (2019). Algorithmic bias? an empirical study of apparent genderbased discrimination in the display of stem career ads. Management Science, 65(7), 2966- 2981.

Langer, N., Gopal, R. D., & Bapna, R. (2020). Onward and upward? An empirical investigation of gender and promotions in Information Technology Services. Information Systems Research, 31(2), 383-398.

Leavy, S. (2018). Gender bias in artificial intelligence: The need for diversity and gender theory in machine learning. Proceedings of the 1st International Workshop on Gender Equality in Software Engineering (pp. 14-16).

Leicht-Deobald, U., Busch, T., Schank, C., Weibel, A., Schafheitle, S., Wildhaber, I., & Kasper, G. (2019). The challenges of algorithm-based HR decision-making for personal integrity. Journal of Business Ethics, 160(2), 377-392.

Lin, J., & Zhou, D. X. (2017). Online learning algorithms can converge comparably fast as batch learning. IEEE Transactions on Neural Networks and Learning Systems, 29(6), 2367- 2378.

Little, R. J., & Rubin, D. B. (2019). Statistical analysis with missing data. Wiley.

Lohia, P. K., Ramamurthy, K. N., Bhide, M., Saha, D., Varshney, K. R., & Puri, R. (2019). Bias mitigation post-processing for individual and

group fairness. Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (pp. 2847-2851).

Lu, J., Liu, A., Dong, F., Gu, F., Gama, J., & Zhang G. (2018), Learning under concept drift: A review. IEEE Transactions on Knowledge and Data Engineering, 31(12), 2346-2363.

Lum, K., & Isaac, W. (2016). To predict and serve? Significance, 13(5), 14-19.

Mallick, A., Hsieh, K., Arzani, B., & Joshi, G. (2022). Matchmaker: Data drift mitigation in machine learning for large-scale systems. Proceedings of Machine Learning and Systems 4 (pp. 77-94).

Manresa-Yee, C., & Ramis, S. (2021). Assessing gender bias in predictive algorithms using eXplainable AI. Proceedings of the 21st International Conference on Human Computer Interaction.

Martin, K. E. (2019). Designing ethical algorithms. MIS Quarterly Executive, 18(2), 129-142.

McKinney, W. (2010). Data structures for statistical computing in Python. Proceedings of the 9th Python in Science Conference (pp. 51-56).

Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., & Galstyan, A. (2021). A survey on bias and fairness in machine learning. ACM Computing Surveys, 54(6), 1-35.

Miettinen, T., Kosfeld, M., Fehr, E., & Weibull, J. (2020). Revealed preferences in a sequential prisoners’ dilemma: A horse-race between six utility functions. Journal of Economic Behavior & Organization, 173, 1-25.

Mishler, A., Kennedy, E. H., & Chouldechova, A. (2021). Fairness in risk assessment instruments: Post-processing to achieve counterfactual equalized odds. Proceedings of the ACM Conference on Fairness, Accountability, and Transparency (pp. 386-400).

Morse, L., Teodorescu, M. H. M., Awwad, Y., & Kane, G. C. (2022). Do the ends justify the means? Variation in the distributive and procedural fairness of machine learning algorithms. Journal of Business Ethics, 181, 1083-1095.

Nagbøl, P. R., Asatiani, A., Malo, P., Penttinen, E., Rinta-Kahila, T., & Salovaara, A. (2021). Sociotechnical envelopment of artificial intelligence: An approach to organizational deployment of inscrutable artificial intelligence systems. Journal of the Association for Information Systems, 22(2), 325-252.

Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias

in an algorithm used to manage the health of populations. Science, 366(6464), 447-453.

Oliphant, T. E. (2006). A guide to NumPy. Trelgol Publishing.

O’Neil, C. (2017). Weapons of math destruction: How big data increases inequality and threatens democracy. Crown.

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.

Pessach, D., & Shmueli, E. (2022). A review on fairness in machine learning. ACM Computing Surveys, 55(3), 1-44.

Pianykh, O. S., Langs, G., Dewey, M., Enzmann, D. R., Herold, C. J., Schoenberg, S. O., & Brink, J. A. (2020). Continuous learning AI in radiology: implementation principles and early applications. Radiology, 297(1), 6-14.

Phelps, E. S. (1972). The statistical theory of racism and sexism. The American Economic Review, 62(4), 659-661.

Prates, M. O., Avelar, P. H., & Lamb, L. C. (2020). Assessing gender bias in machine translation: a case study with Google Translate. Neural Computing and Applications, 32(10), 6363- 6381.

Rambachan, A., Kleinberg, J., Mullainathan, S., & Ludwig, J. (2020). An economic approach to regulating algorithms (NBER Working Paper No. w27111). National Bureau of Economic Research.

Romei, A., & Ruggieri, S. (2013). Discrimination data analysis: a multi-disciplinary bibliography. In B. Custers (Ed.), Discrimination and privacy in the information society (pp. 109-135). Springer.

Ruggs, E. N., Martinez, L. R., & Hebl, M. R. (2011). How individuals and organizations can reduce interpersonal discrimination. Social and Personality Psychology Compass, 5(1), 29-42.

Sahiner, B., Chen, W., Samala, R. K., & Petrick, N. (2023). Data drift in medical machine learning: implications and potential remedies. The British Journal of Radiology, 96(1150), Article 20220878.

Schelter, S., & Stoyanovich, J. (2020). Taming technical bias in machine learning pipelines.

Bulletin of the Technical Committee on Data Engineering, 43(4), 39-50.

Scherr, A. (2008). Diskriminierung: eine eigenständige Kategorie für die soziologische Analyse der (Re-) Produktion sozialer Ungleichheiten in der Einwanderungsgesellschaft? In K.-S. Rehberg (Ed.), Die Natur der Gesellschaft: Verhandlungen des 33. Kongresses der Deutschen Gesellschaft für Soziologie in Kassel 2006. (Vol. 1, pp. 2007- 2017). Campus.

Schmid, T. (2021). Batch-like online learning for more robust hybrid artificial intelligence: Deconstruction as a machine learning process. Proceedings of the AAAI Spring Symposium: Combining Machine Learning with Knowledge Engineering.

Shaikh, M., & Vaast, E. (2022). Algorithmic Interactions in Open Source Work. Information Systems Research, 34(2), 744-765.

Shrestha, Y. R., Ben-Menahem, S. M., & Von Krogh, G. (2019). Organizational decision-making structures in the age of artificial intelligence. California Management Review, 61(4), 66-83.

Shrestha, Y. R., & Yang, Y. (2019). Fairness in algorithmic decision-making: Applications in multi-winner voting, machine learning, and recommender systems. Algorithms, 12(9), 199.

Silva, S., & Kenney, M. (2019). Algorithms, platforms, and ethnic bias. Communications of the ACM, 62(11), 37-39.

Singh, A., & Joachims, T. (2018, July). Fairness of exposure in rankings. Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (pp. 2219-2228).

Someh, I., Davern, M., Breidbach, C. F., & Shanks, G. (2019). Ethical issues in big data analytics: A stakeholder perspective. Communications of the Association for Information Systems, 44, Article 34.

Sonnemaker, T. (2021). 2020 brought a wave of discrimination and harassment allegations against major companies like Amazon, McDonald’s, and Pinterest: These are some of the year’s high-profile legal battles. Business Insider. https://www.businessinsider.com/ every-company-that-was-sued-discriminationand-harassment-lawsuits-2020-2021-1

Srivastava, M., Heidari, H., & Krause, A. (2019). Mathematical notions vs. human perception of fairness: A descriptive approach to fairness for machine learning. Proceedings of the 25th ACM SIGKDD International Conference on

Knowledge Discovery and Data Mining (pp. 2459-2468).

Sturm, T., Gerlach, J. P., Pumplun, L., Mesbah, N., Peters, F., Tauchert, C., ... & Buxmann, P. (2021). Coordinating human and machine learning for effective organizational learning. MIS Quarterly, 45(3), 1581-1602

Sweeney, L. (2013). Discrimination in online ad delivery. Queue, 11(3), 10-29.

Suen, H.-Y., Chen, M. Y.-C., & Lu, S.-H. (2019). Does the use of synchrony and artificial intelligence in video interviews affect interview ratings and applicant attitudes? Computers in Human Behavior, 98, 93-101.

Teodorescu, M. H., Morse, L., Awwad, Y., & Kane, G. C. (2021). Failures of fairness in automation require a deeper understanding of human-ML augmentation. MIS Quarterly, 45(3), 1483- 1500.

Van Rossum, G., & Drake Jr., F. L. (1995). Python tutorial. Centrum voor Wiskunde en Informatica.

Von Zahn, M., Feuerriegel, S., & Kuehl, N. (2021). The cost of fairness in AI: Evidence from ecommerce. Business & Information Systems Engineering, 64, 335-348.

Veale, M., & Binns, R. (2017). Fairer machine learning in the real world: Mitigating discrimination without collecting sensitive data. Big Data & Society, 4(2), 2053951717743530.

Wang, T., He, C., Jin, F., & Hu, Y. J. (2021). Evaluating the effectiveness of marketing campaigns for malls using a novel interpretable machine learning model. Information Systems Research, 33(2), 659-677.

Wells, D., & Spinoni, E. (2019). Western Europe big data and analytics software forecast, 2018- 2023. International Data Corporation. https://www.idc.com/getdoc.jsp?containerId= EUR145601519

Widmer, G., & Kubat, M. (1996). Learning in the presence of concept drift and hidden contexts. Machine Learning, 23(1), 69-101.

Williams, B. A., Brooks, C. F., & Shmargad, Y. (2018). How algorithms discriminate based on data they lack: Challenges, solutions, and policy implications. Journal of Information Policy, 8(1), 78-115.

Wong, K. F. E., & Kwong, J. Y. (2018). Resolving the judgment and decision-making paradox between adaptive learning and escalation of commitment. Management Science, 64(4), 1911-1925.

Wong, P. H. (2020). Democratizing algorithmic fairness. Philosophy & Technology, 33(2), 225- 244.

Woodworth, B., Gunasekar, S., Ohannessian, M. I., & Srebro, N. (2017). Learning non-discriminatory predictors. Proceedings of the Conference on Learning Theory (pp. 1920-1953).

Yao, S., & Huang, B. (2017). Beyond parity: Fairness objectives for collaborative filtering. Proceedings of the 31st Conference on Neural Information Processing Systems.

Zafar, M. B., Valera, I., Rogriguez, M. G., & Gummadi, K. P. (2017). Fairness constraints: Mechanisms for fair classification. Proceedings of the 20th International Conference on Artificial Intelligence and Statistics (pp. 962- 970).

Zhang, B. H., Lemoine, B., & Mitchell, M. (2018). Mitigating unwanted biases with adversarial learning. Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics, and Society (pp. 335- 340).

Zhao, H., & Gordon, G. (2019). Inherent tradeoffs in learning fair representations. Proceedings of the 33rd Conference on Neural Information Processing Systems.

Žliobaitė, I. (2017). Measuring discrimination in algorithmic decision making. Data Mining and Knowledge Discovery, 31(4), 1060-1089.

## Appendix A: Supplementary Material

## A.1 Additional Results

Low Initial Imbalance for Minority Class in Training Data  
![](/api/attachments/VVM428SH/fulltext/images/d4bad9d519125732f7789d592e80fa6781c139d59a41e35b5b3cb7d6bacb0416.jpg)  
Note: We depict the development of the mean share of positive predictions and mean false-negative error rates across iterations. We show results separately for female and male borrowers. We show results for the condition where the initial label imbalance for the minority class was low.

Figure A1. Development of the Mean Share of Positive Predictions and False-Negative Error Rates under Low Initial Label Imbalance  
![](/api/attachments/VVM428SH/fulltext/images/3a0e48bcec96cbfe96656f6d1654851b5dc591c3b7ba4f93a5eb5600205eea9b.jpg)  
Note: We depict the development of the mean share of game outcomes that are equal to outcomes under perfect information and mean shares of games where investors invest in repaying borrowers. We show results separately for female and male borrowers. We show results for the condition where the initial label imbalance for the minority class was low.

Figure A2. Development of the Mean Share of Game Outcomes Investment Shares by Gender under Low Initial Label Imbalance

Medium Initial Imbalance for Minority Class in Training Data

![](/api/attachments/VVM428SH/fulltext/images/0bf517fdfb867a371434e80f2d3beb2856fc4e9faf1cdfc72e9e7e752349acea.jpg)  
Note: We depict the development of the mean share of positive predictions and mean false-negative error rates across iterations We show results separately for female and male borrowers. We show results for the condition where the initial label imbalance for the minority class was medium.

Figure A3. Development of the Mean Share of Positive Predictions and False-Negative Error Rates under Medium Initial Label Imbalance  
![](/api/attachments/VVM428SH/fulltext/images/099bba9a9fffa134eda3a55eede57641a7b8ea5880ae24a775b741e9e8333b1f.jpg)  
Note: We depict the development of the mean share of game outcomes that are equal to outcomes under perfect information and mean shares of games where investors invest in repaying borrowers. We show results separately for female and male borrowers. We show results for the condition where the initial label imbalance for the minority class was medium.  
Figure A4. Development of the Mean Share of Game Outcomes Investment Shares by Gender under Medium Initial Label Imbalance

High Initial Imbalance for Minority Class in Training Data

![](/api/attachments/VVM428SH/fulltext/images/b250c6ccf8901f0ffcf92adf5f52348ed386765ac8c016f52b79bc11157d2541.jpg)  
Note: We depict the development of the mean share of positive predictions and mean false-negative error rates across iterations. We show results separately for female and male borrowers. We show results for the condition where the initial label imbalance for the minority class was high.

Figure A5. Development of the Mean Share of Positive Predictions and False-Negative Error Rates under High Initial Label Imbalance  
![](/api/attachments/VVM428SH/fulltext/images/f2d0f292fd7762470321493aa3d578d7690ae56c7a8e350adf90a68e539f736d.jpg)  
Note: We depict the development of the mean share of game outcomes that are equal to outcomes under perfect information and mean shares of games where investors invest in repaying borrowers. We show results separately for female and male borrowers. We show results for the condition where the initial label imbalance for the minority class was high.

Figure A6. Development of the Mean Share of Game Outcomes Investment Shares by Gender under High Initial Label Imbalance  
Table A1. OLS Regression Estimates

<table><tr><td></td><td>(1)</td><td>(2)</td></tr><tr><td>Dep. variable:(male borrowers only)</td><td>Outcome under perf. inf.</td><td>Invest in repay. borrower</td></tr><tr><td>Iteration</td><td>0.001***(0.000)</td><td>0.001***(0.000)</td></tr><tr><td>Low lab. imb.</td><td>-0.012(0.010)</td><td>-0.026(0.021)</td></tr><tr><td>Medium lab. imb.</td><td>0.004(0.006)</td><td>-0.005(0.014)</td></tr><tr><td>High lab. imb.</td><td>-0.003(0.010)</td><td>-0.029(0.022)</td></tr><tr><td>Max lab. imb.</td><td>-0.005(0.011)</td><td>-0.037(0.022)</td></tr><tr><td>Iteration*Low lab. imb.</td><td>0.000(0.000)</td><td>0.000(0.000)</td></tr><tr><td>Iteration*Medium lab. imb.</td><td>-0.000(0.000)</td><td>-0.000(0.000)</td></tr><tr><td>Iteration*High lab. imb.</td><td>0.000(0.000)</td><td>0.000(0.000)</td></tr><tr><td>Iteration*Max lab. imb.</td><td>0.000(0.000)</td><td>0.000(0.000)</td></tr><tr><td>Constant</td><td>0.684***(0.008)</td><td>0.411***(0.018)</td></tr><tr><td>Observations</td><td>240,523</td><td>107,303</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.003</td><td>0.005</td></tr><tr><td>Adj. R-squared</td><td>0.003</td><td>0.005</td></tr><tr><td colspan="3">Note: We report robust standard errors that are clustered at the random seed level in parentheses. The dependent variables in Columns (1) and (2) are dummy variables respectively indicating whether a game resulted in the same outcomes as a game under perfect information would have and whether an investor invested in a repaying borrower. We only used the subsample of observations where the borrower was male. * p &lt; 0.1, ** p &lt; 0.05, *** p &lt; 0.01 denote statistical significance levels.</td></tr></table>

## The Role of Ongoing Human Discrimination: Figures

Plots for Male Borrowers

![](/api/attachments/VVM428SH/fulltext/images/a426e0e14848c53dd575750fd5ae97519f1ea2c36c3c7a88ec205db27910098f.jpg)  
Note: We illustrate how the mean share of positive predictions for male borrowers in Iterations 1 and 100 depends on the initial label imbalance in the training data and the degree of human discrimination by the investor. A comparison of panels for Iterations 1 and 100 for the two measures of algorithmic discrimination provides insights into their conditional development across iterations. Abbreviations: Share pos. predictions = share of positive predictions; Init. lab. imb. = initial label imbalance; Human discr. = human discrimination.  
Figure A7. Development of the Mean Share of Positive Predictions by Initial Label Imbalance and Degree of Human Discrimination

![](/api/attachments/VVM428SH/fulltext/images/89405be6395cd7449a2c12fb32541a1e817b71e46b1f1d1683b2dacdf26e43fb.jpg)  
Note: We illustrate how the mean false-negative error rates for male borrowers in Iterations 1 and 100 depend on the initial label imbalance in the training data and the degree of human discrimination by the investor. A comparison of panels for Iterations 1 and 100 for the two measures of algorithmic discrimination provides insights into their conditional development across iterations. Abbreviations: False-neg. rate = false negative rate; Init. lab. imb. = initial label imbalance; Human discr. = human discrimination.

Figure A8. Development of the Mean Share of False-Negative Errors by Initial Label Imbalance and Degree of Human Discrimination  
![](/api/attachments/VVM428SH/fulltext/images/b2bf386c90396673e289aa6a407c4860661a566a4e99ba66ba71690fce5d1e35.jpg)  
Note: We illustrate how the mean share of games that result in the outcome as if the game was played under perfect information in Iterations 1 and 100 depends on the initial label imbalance in the training data and the degree of human discrimination by the investor. We depict results in case the borrower is male. A comparison of panels for Iterations 1 and 100 for the two measures of algorithmic discrimination provides insights into their conditional development across iterations. Abbreviations: Outcome under perf. inf. = outcome under perfect information; Init. lab. imb. = initial label imbalance; Human discr. = human discrimination.  
Figure A9. Development of the Mean Share of Game Outcomes by Initial Label Imbalance and Degree of Human Discrimination

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the share of positive predictions per iteration as dependent variable. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

![](/api/attachments/VVM428SH/fulltext/images/7b60d8ad3c0a2b5833771e82980b4ff96d0e7c8b2b566e445ec67f50e1f34420.jpg)  
Note: We illustrate how the mean share of games where investors invest with a repaying borrower in Iterations 1 and 100 depends on the initial label imbalance in the training data and the degree of human discrimination by the investor. We depict results in case the borrower is male- A comparison of panels for Iterations 1 and 100 for the two measures of algorithmic discrimination provides insights into their conditiona development across iterations. Abbreviations: Init. lab. imb. = initial label imbalance; Human discr. = human discrimination.

Figure A10. Development of the Mean Share of Game Outcomes by Initial Label Imbalance and Degree of Human Discrimination with a Repaying Borrower

## The Role of Ongoing Human Discrimination: Regression Analyses

## Algorithmic Discrimination

Table A2. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in pos. preds.</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>-0.0002(0.000)</td><td>-0.0007***(0.000)</td><td>-0.0014***(0.000)</td><td>-0.0022***(0.000)</td><td>-0.0018***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>0.0002(0.000)</td><td>0.0003*(0.000)</td><td>0.0001(0.000)</td><td>0.0005***(0.000)</td><td>0.0004**(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0007***(0.000)</td><td>0.0005**(0.000)</td><td>0.0006**(0.000)</td><td>0.0011***(0.000)</td><td>0.0012***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0007***(0.000)</td><td>0.0008***(0.000)</td><td>0.0012***(0.000)</td><td>0.0016***(0.000)</td><td>0.0019***(0.000)</td></tr><tr><td>Observations</td><td>9,400</td><td>10,000</td><td>9,300</td><td>14,390</td><td>17,400</td></tr><tr><td>p</td><td>0.001</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.009</td><td>0.030</td><td>0.094</td><td>0.191</td><td>0.193</td></tr></table>

Table A3. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in FNR error</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>-0.0015***(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0012***(0.000)</td><td>-0.0003***(0.000)</td><td>-0.0000(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>0.0005*(0.000)</td><td>0.0004***(0.000)</td><td>0.0007***(0.000)</td><td>0.0004***(0.000)</td><td>0.0006***(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0011***(0.000)</td><td>0.0008***(0.000)</td><td>0.0011***(0.000)</td><td>0.0009***(0.000)</td><td>0.0009***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0009***(0.000)</td><td>0.0013***(0.000)</td><td>0.0017***(0.000)</td><td>0.0012***(0.000)</td><td>0.0012***(0.000)</td></tr><tr><td>Observations</td><td>9,400</td><td>10,000</td><td>9,300</td><td>14,390</td><td>17,400</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.053</td><td>0.068</td><td>0.043</td><td>0.040</td><td>0.039</td></tr><tr><td colspan="6">Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the false-negative error rates per iteration as dependent variable. * p&lt;0.1, ** p&lt;0.05, *** p&lt;0.01 denote statistical significance levels.</td></tr></table>

Economic Efficiency: Female Borrowers  
Table A4. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Outcome under perf. inf</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0016***(0.000)</td><td>0.0015***(0.000)</td><td>0.0019***(0.000)</td><td>0.0016***(0.000)</td><td>0.0015***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0004***(0.000)</td><td>-0.0003***(0.000)</td><td>-0.0005***(0.000)</td><td>-0.0005***(0.000)</td><td>-0.0005***(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0006***(0.000)</td><td>-0.0006***(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0010***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0010***(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0014***(0.000)</td><td>-0.0013***(0.000)</td><td>-0.0014***(0.000)</td></tr><tr><td>Observations</td><td>219,852</td><td>232,335</td><td>217,369</td><td>344,122</td><td>405,501</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.014</td><td>0.017</td><td>0.011</td><td>0.011</td><td>0.007</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is dummy variables indicating whether a game resulted in the same outcomes as a game under perfect information would have. We only used the subsample of observations where the borrower was female. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Table A5. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Invest w. repaying borrower</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0017***(0.000)</td><td>0.0019***(0.000)</td><td>0.0026***(0.000)</td><td>0.0028***(0.000)</td><td>0.0027***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0005***(0.000)</td><td>-0.0005***(0.000)</td><td>-0.0007***(0.000)</td><td>-0.0008***(0.000)</td><td>-0.0008***(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0008***(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0013***(0.000)</td><td>-0.0016***(0.000)</td><td>-0.0018***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0012***(0.000)</td><td>-0.0013***(0.000)</td><td>-0.0021***(0.000)</td><td>-0.0022***(0.000)</td><td>-0.0026***(0.000)</td></tr><tr><td>Observations</td><td>124,676</td><td>129,965</td><td>123,246</td><td>193,482</td><td>229,449</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.047</td><td>0.068</td><td>0.050</td><td>0.073</td><td>0.085</td></tr><tr><td colspan="6">Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is a dummy variable indicating whether an investor invested in a repaying borrower. We only used the subsample of observations where the borrower was female. * p&lt;0.1, ** p&lt;0.05, *** p&lt;0.01 denote statistical significance levels.</td></tr></table>

## Economic Efficiency: Male Borrowers

Table A6. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Outcome under perf. inf</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0009***(0.000)</td><td>0.0009***(0.000)</td><td>0.0008***(0.000)</td><td>0.0009***(0.000)</td><td>0.0009***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0000(0.000)</td><td>0.0000(0.000)</td><td>0.0001(0.000)</td><td>-0.0000(0.000)</td><td>0.0000(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0000(0.000)</td><td>0.0001(0.000)</td><td>0.0000(0.000)</td><td>0.0000(0.000)</td><td>-0.0000(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0001(0.000)</td><td>-0.0000(0.000)</td><td>0.0000(0.000)</td><td>-0.0000(0.000)</td><td>0.0000(0.000)</td></tr><tr><td>Observations</td><td>250,148</td><td>267,665</td><td>247,631</td><td>400,378</td><td>464,499</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.003</td><td>0.004</td><td>0.003</td><td>0.003</td><td>0.003</td></tr><tr><td colspan="6">Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is dummy variables indicating whether a game resulted in the same outcomes as a game under perfect information would have. We only used the subsample of observations where the borrower was male. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p < 0 . \bar { 0 1 }$ denote statistical significance levels.

Table A7. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Init lab. Imb.</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Invest w. repaying borrower</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0011***(0.000)</td><td>0.0012***(0.000)</td><td>0.0010***(0.000)</td><td>0.0012***(0.000)</td><td>0.0012***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>0.0001(0.000)</td><td>0.0000(0.000)</td><td>0.0001(0.000)</td><td>-0.0001(0.000)</td><td>-0.0001(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0000(0.000)</td><td>0.0001(0.000)</td><td>0.0001(0.000)</td><td>0.0001(0.000)</td><td>-0.0001(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0002(0.000)</td><td>0.0000(0.000)</td><td>0.0000(0.000)</td><td>-0.0002(0.000)</td><td>-0.0001(0.000)</td></tr><tr><td>Observations</td><td>112,764</td><td>120,420</td><td>111,556</td><td>176,938</td><td>206,642</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.004</td><td>0.005</td><td>0.004</td><td>0.004</td><td>0.005</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is a dummy variable indicating whether an investor invested in a repaying borrower. We only used the subsample of observations where the borrower was male. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

## A.2 Robustness Checks

Size of Minority Share of Women in Training Data: 10%

Table A8. OLS Regression Estimates

<table><tr><td></td><td colspan="2">Fairness measures(gender gap)</td><td colspan="2">Economic efficiency(female borrowers only)</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Dep. variable:</td><td>Share of repay predictions</td><td>False-negative error rates</td><td>Outcome under perf. inf.</td><td>Invest in repay. borrower</td></tr><tr><td>Iteration</td><td>-0.0004(0.000)</td><td>-0.0021***(0.000)</td><td>0.0021***(0.000)</td><td>0.0021***(0.000)</td></tr><tr><td>Low lab. imb.</td><td>0.0515**(0.023)</td><td>-0.0192(0.027)</td><td>-0.0157(0.016)</td><td>-0.0618***(0.022)</td></tr><tr><td>Medium lab. imb.</td><td>0.1088***(0.023)</td><td>0.0099(0.027)</td><td>-0.0044(0.016)</td><td>-0.0433**(0.022)</td></tr><tr><td>High lab. imb.</td><td>0.2764***(0.023)</td><td>0.0730***(0.027)</td><td>-0.0593***(0.016)</td><td>-0.1942***(0.021)</td></tr><tr><td>Max lab. imb.</td><td>0.3418***(0.021)</td><td>0.0754***(0.026)</td><td>-0.0907***(0.016)</td><td>-0.2654***(0.019)</td></tr><tr><td>Iteration*Low lab. imb.</td><td>-0.0002(0.000)</td><td>0.0011**(0.000)</td><td>-0.0003(0.000)</td><td>0.0001(0.000)</td></tr><tr><td>Iteration*Medium lab. imb.</td><td>-0.0010***(0.000)</td><td>0.0007(0.000)</td><td>-0.0000(0.000)</td><td>0.0007*(0.000)</td></tr><tr><td>Iteration*High lab. imb.</td><td>-0.0020***(0.000)</td><td>0.0011**(0.000)</td><td>-0.0003(0.000)</td><td>0.0008**(0.000)</td></tr><tr><td>Iteration*Max lab. imb.</td><td>-0.0017***(0.000)</td><td>0.0018***(0.000)</td><td>-0.0006*(0.000)</td><td>0.0005(0.000)</td></tr><tr><td>N</td><td>1,500</td><td>1,500</td><td>35,290</td><td>19,070</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.388</td><td>0.188</td><td>0.021</td><td>0.057</td></tr><tr><td colspan="5">Note: We report robust standard errors that are clustered at the random seed level in parentheses. The dependent variables in Columns (1) and (2) are measures for the level of algorithmic discrimination. Specifically, in Column (1), we use the mean gender gap in the share of positive predictions per iteration as dependent variable. In Column (2), we use the mean gender gap in the false-negative error rates per iteration as dependent variable. In Columns (3) and (4), the dependent variables are dummy variables respectively indicating whether a game resulted in the same outcomes as a game under perfect information would have and whether an investor invested in a repaying borrower. For Columns (3) and (4), we only used the subsample of observations where the borrower was female. * p&lt;0.1, ** p&lt;0.05, *** p&lt;0.01 denote statistical significance levels.</td></tr></table>

Table A9. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in pos. preds.</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>-0.0004(0.000)</td><td>-0.0006**(0.000)</td><td>-0.0014***(0.000)</td><td>-0.0024***(0.000)</td><td>-0.0021***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0002(0.000)</td><td>0.0004(0.000)</td><td>0.0002(0.000)</td><td>0.0009***(0.000)</td><td>0.0003(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0013***(0.000)</td><td>0.0002(0.000)</td><td>0.0010***(0.000)</td><td>0.0007*(0.000)</td><td>0.0014***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0008*(0.000)</td><td>0.0009**(0.000)</td><td>0.0012***(0.000)</td><td>0.0022***(0.000)</td><td>0.0019***(0.000)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.028</td><td>0.063</td><td>0.193</td><td>0.346</td><td>0.264</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the share of positive predictions per iteration as dependent variable. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Table A10. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in FNR error</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>-0.0021***(0.000)</td><td>-0.0011***(0.000)</td><td>-0.0014***(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0003(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>0.0008*(0.000)</td><td>0.0005(0.000)</td><td>0.0007(0.000)</td><td>0.0009**(0.000)</td><td>0.0001(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0012***(0.000)</td><td>0.0002(0.000)</td><td>0.0012***(0.000)</td><td>0.0011***(0.000)</td><td>0.0008**(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0016***(0.000)</td><td>0.0008*(0.000)</td><td>0.0019***(0.000)</td><td>0.0017***(0.000)</td><td>0.0014***(0.000)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.105</td><td>0.066</td><td>0.134</td><td>0.089</td><td>0.061</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the false-negative error rates per iteration as dependent variable. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Table A11. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Outcome under perf. inf(female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0021***(0.000)</td><td>0.0018***(0.000)</td><td>0.0021***(0.000)</td><td>0.0018***(0.000)</td><td>0.0016***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0005*(0.000)</td><td>-0.0006*(0.000)</td><td>-0.0006**(0.000)</td><td>-0.0005(0.000)</td><td>0.0000(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0010***(0.000)</td><td>-0.0006**(0.000)</td><td>-0.0011***(0.000)</td><td>-0.0005*(0.000)</td><td>-0.0008***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0014***(0.000)</td><td>-0.0011***(0.000)</td><td>-0.0014***(0.000)</td><td>-0.0016***(0.000)</td><td>-0.0011***(0.000)</td></tr><tr><td>Observations</td><td>28,232</td><td>28,232</td><td>28,232</td><td>28,232</td><td>28,232</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.019</td><td>0.012</td><td>0.020</td><td>0.014</td><td>0.009</td></tr><tr><td colspan="6">Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is dummy variables indicating whether a game resulted in the same outcomes as a game under perfect information would have. We only used the subsample of observations where the borrower was female. * p&lt;0.1, ** p&lt;0.05, *** p&lt;0.01 denote statistical significance levels.</td></tr></table>

Table A12. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Invest w. repaying borrower (female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0021***(0.000)</td><td>0.0021***(0.000)</td><td>0.0027***(0.000)</td><td>0.0029***(0.000)</td><td>0.0026***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0003(0.000)</td><td>-0.0009**(0.000)</td><td>-0.0008**(0.000)</td><td>-0.0008**(0.000)</td><td>-0.0001(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0012***(0.000)</td><td>-0.0009**(0.000)</td><td>-0.0015***(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0015***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0016***(0.000)</td><td>-0.0016***(0.000)</td><td>-0.0021***(0.000)</td><td>-0.0027***(0.000)</td><td>-0.0020***(0.000)</td></tr><tr><td>Observations</td><td>15,256</td><td>15,256</td><td>15,256</td><td>15,256</td><td>15,256</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.071</td><td>0.059</td><td>0.113</td><td>0.111</td><td>0.092</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is a dummy variable indicating whether an investor invested in a repaying borrower. We only used the subsample of observations where the borrower was female. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Tables A8 to A12 present the results from simulations we conducted as robustness checks. Specifically, in these robustness checks, we set the minority share of women in the training data (used to train the ML model predicting borrower repayment behavior) at 10%. In contrast, we used a share size of 20% in the results reported in our main text. We held the number of investor-borrower matches at 50, consistent with our primary simulation. The results depicted in these regression tables indicate that our primary findings remain mostly robust under this variation in our simulation’s parameters. Specifically, we see that algorithmic discrimination decreases over time, while economic efficiency increases. We once again observe that the initial degree of label imbalance in the training data negatively impacts self-correcting mechanisms (see Table A8). Tables A9 to A12 demonstrate that our insights regarding the role of persistent human discrimination are also robust. Specifically, they confirm that higher levels of persistent human discrimination reduce the likelihood of self-correcting mechanisms occurring.

Size of Minority Share of Women in Training Data: 30%  
Table A13. OLS Regression Estimates

<table><tr><td></td><td colspan="2">Fairness measures(gender gap)</td><td colspan="2">Economic efficiency(female borrowers only)</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Dep. variable:</td><td>Share of repay predictions</td><td>False-negative error rates</td><td>Outcome under perf. inf.</td><td>Invest in repay. borrower</td></tr><tr><td>Iteration</td><td>0.0000(0.000)</td><td>-0.0007**(0.000)</td><td>0.0013***(0.000)</td><td>0.0012***(0.000)</td></tr><tr><td>Low lab. imb.</td><td>0.1062***(0.023)</td><td>0.0916***(0.026)</td><td>-0.0111(0.016)</td><td>-0.0796***(0.022)</td></tr><tr><td>Medium lab. imb.</td><td>0.2521***(0.023)</td><td>0.1825***(0.026)</td><td>-0.0438***(0.016)</td><td>-0.1420***(0.022)</td></tr><tr><td>High lab. imb.</td><td>0.3125***(0.022)</td><td>0.1700***(0.027)</td><td>-0.1063***(0.016)</td><td>-0.2876***(0.021)</td></tr><tr><td>Max lab. imb.</td><td>0.4289***(0.020)</td><td>0.2193***(0.026)</td><td>-0.1772***(0.016)</td><td>-0.4230***(0.019)</td></tr><tr><td>Iteration*Low lab. imb.</td><td>-0.0009**(0.000)</td><td>-0.0005(0.000)</td><td>0.0003(0.000)</td><td>0.0009**(0.000)</td></tr><tr><td>Iteration*Medium lab. imb.</td><td>-0.0023***(0.000)</td><td>-0.0009**(0.000)</td><td>0.0006**(0.000)</td><td>0.0017***(0.000)</td></tr><tr><td>Iteration*High lab. imb.</td><td>-0.0013***(0.000)</td><td>0.0008*(0.000)</td><td>0.0001(0.000)</td><td>0.0009**(0.000)</td></tr><tr><td>Iteration*Max lab. imb.</td><td>-0.0015***(0.000)</td><td>0.0007(0.000)</td><td>0.0002(0.000)</td><td>0.0013***(0.000)</td></tr><tr><td>N</td><td>1,500</td><td>1,500</td><td>35,290</td><td>19,070</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.509</td><td>0.292</td><td>0.028</td><td>0.099</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. The dependent variables in Columns (1) and (2) are measures for the level of algorithmic discrimination. Specifically, in Column (1), we use the mean gender gap in the share of positive predictions per iteration as dependent variable. In Column (2), we use the mean gender gap in the false-negative error rates per iteration as dependent variable. In Columns (3) and (4), the dependent variables are dummy variables respectively indicating whether a game resulted in the same outcomes as a game under perfect information would have and whether an investor invested in a repaying borrower. For Columns (3) and (4), we only used the subsample of observations where the borrower was female. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p < 0 . 0 1$ denote statistical significance levels.

Table A14. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in pos. preds.</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0000(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0023***(0.000)</td><td>-0.0013***(0.000)</td><td>-0.0015***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>0.0005(0.000)</td><td>0.0006*(0.000)</td><td>0.0009**(0.000)</td><td>0.0001(0.000)</td><td>0.0003(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0002(0.000)</td><td>0.0017***(0.000)</td><td>0.0018***(0.000)</td><td>0.0008**(0.000)</td><td>0.0013***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0005(0.000)</td><td>0.0007*(0.000)</td><td>0.0023***(0.000)</td><td>0.0012***(0.000)</td><td>0.0015***(0.000)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.033</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.012</td><td>0.038</td><td>0.123</td><td>0.194</td><td>0.152</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the share of positive predictions per iteration as dependent variable. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p < 0 . 0 1$ denote statistical significance levels.

Table A15. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in FNR error</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>-0.0007**(0.000)</td><td>-0.0012***(0.000)</td><td>-0.0016***(0.000)</td><td>0.0001(0.000)</td><td>-0.0000(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>0.0006(0.000)</td><td>0.0006(0.000)</td><td>0.0010**(0.000)</td><td>-0.0003(0.000)</td><td>0.0004(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0002(0.000)</td><td>0.0017***(0.000)</td><td>0.0018***(0.000)</td><td>0.0006(0.000)</td><td>0.0010**(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0013***(0.000)</td><td>0.0017***(0.000)</td><td>0.0019***(0.000)</td><td>0.0008**(0.000)</td><td>0.0009**(0.000)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.053</td><td>0.080</td><td>0.061</td><td>0.062</td><td>0.044</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the false-negative error rates per iteration as dependent variable. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Table A16. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Outcome under perf. inf(female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0013***(0.000)</td><td>0.0015***(0.000)</td><td>0.0019***(0.000)</td><td>0.0013***(0.000)</td><td>0.0014***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0004(0.000)</td><td>-0.0004(0.000)</td><td>-0.0003(0.000)</td><td>-0.0003(0.000)</td><td>-0.0003(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0003(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0006**(0.000)</td><td>-0.0010***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0008***(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0013***(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0012***(0.000)</td></tr><tr><td>Observations</td><td>28,232</td><td>28,232</td><td>28,232</td><td>28,232</td><td>28,232</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.019</td><td>0.020</td><td>0.020</td><td>0.008</td><td>0.006</td></tr><tr><td colspan="6">Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is dummy variables indicating whether a game resulted in the same outcomes as a game under perfect information would have. We only used the subsample of observations where the borrower was female. * p&lt;0.1, ** p&lt;0.05, *** p&lt;0.01 denote statistical significance levels.</td></tr></table>

Table A17. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Invest w. repaying borrower (female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0012***(0.000)</td><td>0.0021***(0.000)</td><td>0.0029***(0.000)</td><td>0.0021***(0.000)</td><td>0.0025***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0004(0.000)</td><td>-0.0011***(0.000)</td><td>-0.0007*(0.000)</td><td>-0.0006**(0.000)</td><td>-0.0007**(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0004(0.000)</td><td>-0.0017***(0.000)</td><td>-0.0017***(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0019***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0010***(0.000)</td><td>-0.0019***(0.000)</td><td>-0.0024***(0.000)</td><td>-0.0019***(0.000)</td><td>-0.0024***(0.000)</td></tr><tr><td>Observations</td><td>15,256</td><td>15,256</td><td>15,256</td><td>15,256</td><td>15,256</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.089</td><td>0.093</td><td>0.091</td><td>0.059</td><td>0.086</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is a dummy variable indicating whether an investor invested in a repaying borrower. We only used the subsample of observations where the borrower was female. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Tables A13 to A17 present the results from simulations we conducted as robustness checks. Specifically, in these robustness checks, we set the minority share of women in the training data (used to train the ML model predicting borrower repayment behavior) at 30%. In contrast, we used a share size of 20% in the results reported in our main text. We held the number of investor-borrower matches at 50, consistent with our primary simulation. The results depicted in these regression tables indicate that our primary findings remain mostly robust under this variation in our simulation’s parameters. Specifically, we see that algorithmic discrimination decreases over time, while economic efficiency increases. We once again observe that the initial degree of label imbalance in the training data negatively impacts self-correcting mechanisms (see Table A13). Tables A14 to A18 demonstrate that our insights regarding the role of persistent human discrimination are also robust. Specifically, they confirm that higher levels of persistent human discrimination reduce the likelihood of self-correcting mechanisms occurring.

Number of Investors and Borrowers Matched per Iteration: 30  
Table A18. OLS Regression Estimates

<table><tr><td></td><td colspan="2">Fairness measures(gender gap)</td><td colspan="2">Economic efficiency(female borrowers only)</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Dep. variable:</td><td>Share of repay predictions</td><td>False-negative error rates</td><td>Outcome under perf. inf.</td><td>Invest in repay. borrower</td></tr><tr><td>Iteration</td><td>0.0002(0.55)</td><td>-0.0005(-1.04)</td><td>0.0015***(5.84)</td><td>0.0014***(3.79)</td></tr><tr><td>Low lab. imb.</td><td>0.0837***(2.90)</td><td>0.0549(1.44)</td><td>0.0042(0.20)</td><td>-0.0098(-0.34)</td></tr><tr><td>Medium lab. imb.</td><td>0.2366***(8.32)</td><td>0.1192***(3.13)</td><td>-0.0507**(-2.37)</td><td>-0.1588***(-5.82)</td></tr><tr><td>High lab. imb.</td><td>0.3271***(12.20)</td><td>0.1543***(4.19)</td><td>-0.0916***(-4.27)</td><td>-0.2435***(-9.58)</td></tr><tr><td>Max lab. imb.</td><td>0.4235***(16.83)</td><td>0.1579***(4.27)</td><td>-0.1209***(-5.63)</td><td>-0.3193***(-13.71)</td></tr><tr><td>Iteration*Low lab. imb.</td><td>-0.0008(-1.45)</td><td>-0.0005(-0.88)</td><td>0.0002(0.66)</td><td>0.0007(1.30)</td></tr><tr><td>Iteration*Medium lab. imb.</td><td>-0.0018***(-3.61)</td><td>-0.0003(-0.49)</td><td>0.0003(0.75)</td><td>0.0011**(2.18)</td></tr><tr><td>Iteration*High lab. imb.</td><td>-0.0015***(-3.09)</td><td>0.0004(0.68)</td><td>-0.0001(-0.40)</td><td>0.0005(1.11)</td></tr><tr><td>Iteration*Max lab. imb.</td><td>-0.0014***(-3.00)</td><td>0.0010*(1.73)</td><td>-0.0004(-1.04)</td><td>0.0002(0.50)</td></tr><tr><td>N</td><td>1,500</td><td>1,500</td><td>21,135</td><td>11,435</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.399</td><td>0.150</td><td>0.022</td><td>0.088</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. The dependent variables in Columns (1) and (2) are measures for the level of algorithmic discrimination. Specifically, in Column (1), we use the mean gender gap in the share of positive predictions per iteration as dependent variable. In Column (2), we use the mean gender gap in the false-negative error rates per iteration as dependent variable. In Columns (3) and (4), the dependent variables are dummy variables respectively indicating whether a game resulted in the same outcomes as a game under perfect information would have and whether an investor invested in a repaying borrower. For Columns (3) and (4), we only used the subsample of observations where the borrower was female. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p < 0 . 0 1$ denote statistical significance levels.

Table A19. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in pos. preds.</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0002(0.000)</td><td>-0.0006(0.000)</td><td>-0.0016***(0.000)</td><td>-0.0013***(0.000)</td><td>-0.0012***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0002(0.001)</td><td>0.0001(0.001)</td><td>0.0008(0.001)</td><td>0.0002(0.000)</td><td>0.0008**(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0006(0.000)</td><td>0.0000(0.001)</td><td>0.0019***(0.000)</td><td>0.0006(0.000)</td><td>0.0006*(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0001(0.001)</td><td>0.0004(0.001)</td><td>0.0007(0.001)</td><td>0.0007*(0.000)</td><td>0.0010***(0.000)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.003</td><td>0.006</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.017</td><td>0.017</td><td>0.041</td><td>0.081</td><td>0.041</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the share of positive predictions per iteration as dependent variable. $^ { * } p < 0 . 1 , ^ { * * } \bar { p } < 0 . 0 5 , ^ { * * * } p < 0 . 0 1$ denote statistical significance levels.

Table A20. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in FNR error</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>-0.0005(0.000)</td><td>-0.0010**(0.000)</td><td>-0.0008*(0.000)</td><td>-0.0001(0.000)</td><td>0.0006(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0002(0.001)</td><td>0.0008(0.001)</td><td>0.0008(0.001)</td><td>0.0002(0.001)</td><td>0.0005(0.001)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0008(0.001)</td><td>0.0011*(0.001)</td><td>0.0018***(0.001)</td><td>0.0007(0.001)</td><td>0.0003(0.001)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0003(0.001)</td><td>0.0013**(0.001)</td><td>0.0010*(0.001)</td><td>0.0008(0.001)</td><td>0.0005(0.001)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.001</td><td>0.011</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.022</td><td>0.019</td><td>0.019</td><td>0.013</td><td>0.023</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the false-negative error rates per iteration as dependent variable. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Table A21. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Outcome under perf. inf(female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0015***(0.000)</td><td>0.0018***(0.000)</td><td>0.0018***(0.000)</td><td>0.0014***(0.000)</td><td>0.0011***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0004(0.000)</td><td>-0.0008**(0.000)</td><td>-0.0006(0.000)</td><td>-0.0003(0.000)</td><td>-0.0007**(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0007*(0.000)</td><td>-0.0006(0.000)</td><td>-0.0011***(0.000)</td><td>-0.0007*(0.000)</td><td>-0.0008**(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0009**(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0012***(0.000)</td><td>-0.0009**(0.000)</td><td>-0.0009**(0.000)</td></tr><tr><td>Observations</td><td>16,908</td><td>16,908</td><td>16,908</td><td>16,908</td><td>16,908</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.012</td><td>0.016</td><td>0.010</td><td>0.006</td><td>0.003</td></tr><tr><td colspan="6">Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is dummy variables indicating whether a game resulted in the same outcomes as a game under perfect information would have. We only used the subsample of observations where the borrower was female. * p&lt;0.1, ** p&lt;0.05, *** p&lt;0.01 denote statistical significance levels.</td></tr></table>

Table A22. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Invest w. repaying borrower (female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0014***(0.000)</td><td>0.0020***(0.000)</td><td>0.0024***(0.000)</td><td>0.0019***(0.000)</td><td>0.0016***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0005(0.001)</td><td>-0.0012**(0.000)</td><td>-0.0010**(0.000)</td><td>-0.0005(0.000)</td><td>-0.0012***(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0011**(0.000)</td><td>-0.0007(0.000)</td><td>-0.0020***(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0013***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0011**(0.000)</td><td>-0.0014***(0.000)</td><td>-0.0019***(0.000)</td><td>-0.0014***(0.000)</td><td>-0.0016***(0.000)</td></tr><tr><td>Observations</td><td>9,148</td><td>9,148</td><td>9,148</td><td>9,148</td><td>9,148</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.056</td><td>0.080</td><td>0.052</td><td>0.052</td><td>0.063</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is a dummy variable indicating whether an investor invested in a repaying borrower. We only used the subsample of observations where the borrower was female. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Tables A18 to A22 display results from simulations we conducted for robustness checks. For these checks, the number of matched investors and borrowers was set to 30, in contrast to the 50 matches in the results reported in our main text. Consistent with the main simulations, we set the minority share of women in the training data (used to train the ML model predicting borrower repayment behavior) at 20%. The results depicted in these regression tables indicate that our primary findings are largely robust to this variation in the parameters of our simulation. Specifically, we see that algorithmic discrimination decreases over time, while economic efficiency increases. We once again confirm that the initial degree of label imbalance in the training data negatively affects the self-correcting mechanisms (see Table A18). Tables A19 to A22 show that our insights regarding the role of persistent human discrimination are also robust. Specifically, they show that when persistent human discrimination levels are higher, self-correcting mechanisms are less likely to occur.

Number of Investors and Borrowers Matched per Iteration: 40  
Table A23. OLS Regression Estimates

<table><tr><td></td><td colspan="2">Fairness measures(gender gap)</td><td colspan="2">Economic efficiency(female borrowers only)</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Dep. variable:</td><td>Share of repay predictions</td><td>False-negative error rates</td><td>Outcome under perf. inf.</td><td>Invest in repay. borrower</td></tr><tr><td>Iteration</td><td>0.0002(0.63)</td><td>-0.0007**(-2.08)</td><td>0.0015***(6.93)</td><td>0.0014***(4.36)</td></tr><tr><td>Low lab. imb.</td><td>0.1768***(7.42)</td><td>0.0925***(3.15)</td><td>-0.0577***(-3.17)</td><td>-0.1451***(-5.94)</td></tr><tr><td>Medium lab. imb.</td><td>0.2150***(9.32)</td><td>0.0998***(3.47)</td><td>-0.0647***(-3.54)</td><td>-0.1857***(-7.75)</td></tr><tr><td>High lab. imb.</td><td>0.3566***(15.82)</td><td>0.1712***(5.95)</td><td>-0.1184***(-6.45)</td><td>-0.3029***(-13.56)</td></tr><tr><td>Max lab. imb.</td><td>0.3886***(17.22)</td><td>0.1631***(5.68)</td><td>-0.1419***(-7.72)</td><td>-0.3402***(-15.93)</td></tr><tr><td>Iteration*Low lab. imb.</td><td>-0.0015***(-3.63)</td><td>-0.0003(-0.54)</td><td>0.0002(0.79)</td><td>0.0008*(1.89)</td></tr><tr><td>Iteration*Medium lab. imb.</td><td>-0.0011***(-2.61)</td><td>0.0007(1.56)</td><td>0.0000(0.09)</td><td>0.0008*(1.92)</td></tr><tr><td>Iteration*High lab. imb.</td><td>-0.0014***(-3.54)</td><td>0.0009**(1.97)</td><td>-0.0002(-0.51)</td><td>0.0006(1.52)</td></tr><tr><td>Iteration*Max lab. imb.</td><td>-0.0014***(-3.50)</td><td>0.0011**(2.38)</td><td>-0.0004(-1.33)</td><td>0.0004(0.94)</td></tr><tr><td>N</td><td>1,500</td><td>1,500</td><td>28,310</td><td>15,335</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.443</td><td>0.211</td><td>0.021</td><td>0.075</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. The dependent variables in Columns (1) and (2) are measures for the level of algorithmic discrimination. Specifically, in Column (1), we use the mean gender gap in the share of positive predictions per iteration as dependent variable. In Column (2), we use the mean gender gap in the false-negative error rates per iteration as dependent variable. In Columns (3) and (4), the dependent variables are dummy variables respectively indicating whether a game resulted in the same outcomes as a game under perfect information would have and whether an investor invested in a repaying borrower. For Columns (3) and (4), we only used the subsample of observations where the borrower was female. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p < 0 . 0 1$ denote statistical significance levels.

Table A24. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in pos. preds.</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0002(0.000)</td><td>-0.0013***(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0012***(0.000)</td><td>-0.0012***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>0.0005(0.000)</td><td>0.0013***(0.000)</td><td>-0.0000(0.000)</td><td>0.0008**(0.000)</td><td>0.0002(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0006(0.000)</td><td>0.0005(0.000)</td><td>0.0007*(0.000)</td><td>0.0011***(0.000)</td><td>0.0009***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0000(0.000)</td><td>0.0010**(0.000)</td><td>0.0006(0.000)</td><td>0.0012***(0.000)</td><td>0.0006*(0.000)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.004</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.017</td><td>0.035</td><td>0.050</td><td>0.072</td><td>0.145</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the share of positive predictions per iteration as dependent variable. $^ { * } p < 0 . 1 , ^ { * * } \bar { p } < 0 . 0 5 , ^ { * * * } p < 0 . 0 1$ denote statistical significance levels.

Table A25. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in FNR error</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>-0.0007**(0.000)</td><td>-0.0010***(0.000)</td><td>0.0000(0.000)</td><td>0.0002(0.000)</td><td>0.0004(0.000)</td></tr><tr><td>Iteration* Medium human discr.</td><td>0.0004(0.000)</td><td>0.0007(0.000)</td><td>-0.0000(0.000)</td><td>0.0003(0.000)</td><td>0.0001(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0006(0.001)</td><td>0.0009*(0.000)</td><td>0.0003(0.000)</td><td>0.0006(0.000)</td><td>0.0005(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0003(0.001)</td><td>0.0012***(0.000)</td><td>0.0005(0.000)</td><td>0.0007(0.000)</td><td>0.0004(0.000)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.000</td><td>0.001</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.056</td><td>0.019</td><td>0.022</td><td>0.022</td><td>0.030</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the false-negative error rates per iteration as dependent variable. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p$ < 0.01 denote statistical significance levels.

Table A26. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Outcome under perf. inf(female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0015***(0.000)</td><td>0.0018***(0.000)</td><td>0.0015***(0.000)</td><td>0.0013***(0.000)</td><td>0.0011***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0004</td><td>-0.0006*</td><td>-0.0005</td><td>-0.0007**</td><td>-0.0003</td></tr><tr><td>Iteration*High human discr.</td><td>(0.000)-0.0007**(0.000)</td><td>(0.000)-0.0010***(0.000)</td><td>(0.000)-0.0009***(0.000)</td><td>(0.000)-0.0010***(0.000)</td><td>(0.000)-0.0008**(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0008***(0.000)</td><td>-0.0012***(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0010***(0.000)</td></tr><tr><td>Observations</td><td>22,648</td><td>22,648</td><td>22,648</td><td>22,648</td><td>22,648</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.018</td><td>0.010</td><td>0.011</td><td>0.006</td><td>0.004</td></tr><tr><td colspan="6">Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is dummy variables indicating whether a game resulted in the same outcomes as a game under perfect information would have. We only used the subsample of observations where the borrower was female. * p&lt;0.1, ** p&lt;0.05, *** p&lt;0.01 denote statistical significance levels.</td></tr></table>

Table A27. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Invest w. repaying borrower (female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0014***(0.000)</td><td>0.0022***(0.000)</td><td>0.0022***(0.000)</td><td>0.0020***(0.000)</td><td>0.0017***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0005(0.000)</td><td>-0.0009**(0.000)</td><td>-0.0008**(0.000)</td><td>-0.0012***(0.000)</td><td>-0.0005*(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0008**(0.000)</td><td>-0.0015***(0.000)</td><td>-0.0016***(0.000)</td><td>-0.0015***(0.000)</td><td>-0.0014***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0008**(0.000)</td><td>-0.0017***(0.000)</td><td>-0.0017***(0.000)</td><td>-0.0017***(0.000)</td><td>-0.0018***(0.000)</td></tr><tr><td>Observations</td><td>12,268</td><td>12,268</td><td>12,268</td><td>12,268</td><td>12,268</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.087</td><td>0.049</td><td>0.066</td><td>0.058</td><td>0.084</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is a dummy variable indicating whether an investor invested in a repaying borrower. We only used the subsample of observations where the borrower was female. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels

The regression tables A23 to A27 show results from simulations that we conducted as robustness checks. Specifically, for this robustness check, the number of matched investors and borrowers equals 40. By contrast, for the results reported in our main text, this number equals 50. As in the simulations whose results we report in the main text, we set the size of the minority share of women in the training data used to train the ML model that predicts borrower repayment behavior to 20%. The depicted regression results reveal that our main findings are largely robust to this variation in the parametrization of our simulation. Specifically, we see that algorithmic discrimination decreases over time whereas economic efficiency increases. We again observe that the level of the initial degree of the label imbalance in the training data affects the self-correcting mechanisms negatively (see Table A23). Tables A24 to A27 reveal that our insights regarding the role of the level of persistent human discrimination are also robust. Specifically, the higher the level of persistent human discrimination the less likely it is that the self-correcting mechanisms will occur.

<table><tr><td></td><td colspan="2">Fairness measures(gender gap)</td><td colspan="2">Economic efficiency(female borrowers only)</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Dep. variable:</td><td>Share of repay predictions</td><td>False-negative error rates</td><td>Outcome under perf. inf.</td><td>Invest in repay. borrower</td></tr><tr><td>Iteration</td><td>-0.0003(-1.18)</td><td>-0.0013***(-4.98)</td><td>0.0016***(9.00)</td><td>0.0016***(6.34)</td></tr><tr><td>Low lab. imb.</td><td>0.0735***(3.58)</td><td>0.0386*(1.65)</td><td>-0.0058(-0.40)</td><td>-0.0298(-1.46)</td></tr><tr><td>Medium lab. imb.</td><td>0.2006***(10.15)</td><td>0.0937***(4.18)</td><td>-0.0550***(-3.70)</td><td>-0.1643***(-8.34)</td></tr><tr><td>High lab. imb.</td><td>0.2938***(14.44)</td><td>0.1305***(5.84)</td><td>-0.0982***(-6.56)</td><td>-0.2488***(-13.28)</td></tr><tr><td>Max lab. imb.</td><td>0.3526***(18.68)</td><td>0.1411***(6.20)</td><td>-0.1295***(-8.65)</td><td>-0.3238***(-18.05)</td></tr><tr><td>Iteration*Low lab. imb.</td><td>-0.0007**(-2.10)</td><td>-0.0000(-0.13)</td><td>0.0001(0.57)</td><td>0.0005(1.42)</td></tr><tr><td>Iteration*Medium lab. imb.</td><td>-0.0013***(-4.05)</td><td>0.0003(0.91)</td><td>0.0003(1.07)</td><td>0.0012***(3.39)</td></tr><tr><td>Iteration*High lab. imb.</td><td>-0.0017***(-4.68)</td><td>0.0007**(2.00)</td><td>0.0002(0.86)</td><td>0.0013***(3.72)</td></tr><tr><td>Iteration*Max lab. imb.</td><td>-0.0017***(-5.31)</td><td>0.0012***(3.26)</td><td>0.0004(1.58)</td><td>0.0017***(5.23)</td></tr><tr><td>N</td><td>1,500</td><td>1,500</td><td>42,400</td><td>23,020</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.436</td><td>0.281</td><td>0.020</td><td>0.062</td></tr><tr><td colspan="5">Note: We report robust standard errors that are clustered at the random seed level in parentheses. The dependent variables in Columns (1) and (2) are measures for the level of algorithmic discrimination. Specifically, in Column (1), we use the mean gender gap in the share of positive predictions per iteration as dependent variable. In Column (2), we use the mean gender gap in the false-negative error rates per iteration as dependent variable. In Columns (3) and (4), the dependent variables are dummy variables respectively indicating whether a game resulted in the same outcomes as a game under perfect information would have and whether an investor invested in a repaying borrower. In Columns (3) and (4), we only used the subsample of observations where the borrower was female. * p&lt;0.1, ** p&lt;0.05, *** p&lt;0.01 denote statistical significance levels.</td></tr></table>

Number of Investors and Borrowers Matched per Iteration: 60  
Table A28. OLS Regression Estimates  
Table A29. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in pos. preds.</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>-0.0003(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0016***(0.000)</td><td>-0.0020***(0.000)</td><td>-0.0020***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>0.0002(0.000)</td><td>-0.0002(0.000)</td><td>0.0004(0.000)</td><td>0.0008**(0.000)</td><td>0.0011***(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0017***(0.000)</td><td>0.0007*(0.000)</td><td>0.0008**(0.000)</td><td>0.0018***(0.000)</td><td>0.0016***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0005(0.000)</td><td>0.0009***(0.000)</td><td>0.0020***(0.000)</td><td>0.0020***(0.000)</td><td>0.0021***(0.000)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.031</td><td>0.051</td><td>0.133</td><td>0.230</td><td>0.333</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the share of positive predictions per iteration as dependent variable. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Table A30. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in FNR error</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>-0.0013***(0.000)</td><td>-0.0013***(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0006**(0.000)</td><td>-0.0001(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>0.0002(0.000)</td><td>0.0001(0.000)</td><td>0.0005(0.000)</td><td>0.0009**(0.000)</td><td>0.0009**(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0008**(0.000)</td><td>0.0013***(0.000)</td><td>0.0009***(0.000)</td><td>0.0012***(0.000)</td><td>0.0010***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0012***(0.000)</td><td>0.0010***(0.000)</td><td>0.0016***(0.000)</td><td>0.0014***(0.000)</td><td>0.0012***(0.000)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.068</td><td>0.086</td><td>0.074</td><td>0.101</td><td>0.108</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the false-negative error rates per iteration as dependent variable. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Table A31. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Outcome under perf. inf(female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0016***(0.000)</td><td>0.0017***(0.000)</td><td>0.0019***(0.000)</td><td>0.0018***(0.000)</td><td>0.0020***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0003(0.000)</td><td>-0.0003(0.000)</td><td>-0.0006**(0.000)</td><td>-0.0006**(0.000)</td><td>-0.0011***(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0006**(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0013***(0.000)</td><td>-0.0015***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0011***(0.000)</td><td>-0.0013***(0.000)</td><td>-0.0014***(0.000)</td><td>-0.0015***(0.000)</td><td>-0.0018***(0.000)</td></tr><tr><td>Observations</td><td>33,920</td><td>33,920</td><td>33,920</td><td>33,920</td><td>33,920</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.017</td><td>0.019</td><td>0.015</td><td>0.011</td><td>0.012</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is dummy variables indicating whether a game resulted in the same outcomes as a game under perfect information would have. We only used the subsample of observations where the borrower was female. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Table A32. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Invest w. repaying borrower (female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0016***(0.000)</td><td>0.0021***(0.000)</td><td>0.0028***(0.000)</td><td>0.0029***(0.000)</td><td>0.0033***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0003(0.000)</td><td>-0.0002(0.000)</td><td>-0.0010***(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0019***(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0010***(0.000)</td><td>-0.0011***(0.000)</td><td>-0.0017***(0.000)</td><td>-0.0022***(0.000)</td><td>-0.0027***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0013***(0.000)</td><td>-0.0019***(0.000)</td><td>-0.0024***(0.000)</td><td>-0.0026***(0.000)</td><td>-0.0032***(0.000)</td></tr><tr><td>Observations</td><td>18,416</td><td>18,416</td><td>18,416</td><td>18,416</td><td>18,416</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.077</td><td>0.092</td><td>0.082</td><td>0.089</td><td>0.129</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is a dummy variable indicating whether an investor invested in a repaying borrower. We only used the subsample of observations where the borrower was female. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

The regression tables A28 to A32 show results for simulations that were conducted as robustness checks. Specifically, for this robustness check, the number of matched investors and borrowers equals 60. By contrast, for the results reported in our main text, this number equals 50. As in the simulations whose results we report in the main text, we set the size of the minority share of women in the training data used to train the ML model that predicts borrower repayment behavior to 20%. The depicted regression results reveal that our main findings are largely robust to this variation in the parametrization of our simulation. Specifically, we observe that algorithmic discrimination decrease over time whereas economic efficiency increases. We again see that the level of the initial degree of the label imbalance in the training data affects the self-correcting mechanisms negatively (see Table A28). Tables A29 to A32 reveal that our insights regarding the role of the level of persistent human discrimination are also robust. Specifically, the higher the level of persistent human discrimination the less likely it is that the self-correcting mechanisms will occur.

Number of Investors and Borrowers Matched per Iteration: 70  
Table A33. OLS Regression Estimates

<table><tr><td></td><td colspan="2">Fairness measures(gender gap)</td><td colspan="2">Economic efficiency(female borrowers only)</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Dep. variable:</td><td>Share of repay predictions</td><td>False-negative error rates</td><td>Outcome under perf. inf.</td><td>Invest in repay. borrower</td></tr><tr><td>Iteration</td><td>-0.0004(-1.62)</td><td>-0.0012***(-4.37)</td><td>0.0017***(10.18)</td><td>0.0020***(8.33)</td></tr><tr><td>Low lab. imb.</td><td>0.0858***(4.40)</td><td>0.0491**(2.09)</td><td>-0.0356***(-2.60)</td><td>-0.0938***(-5.02)</td></tr><tr><td>Medium lab. imb.</td><td>0.1720***(9.14)</td><td>0.0824***(3.69)</td><td>-0.0584***(-4.25)</td><td>-0.1493***(-8.13)</td></tr><tr><td>High lab. imb.</td><td>0.2983***(15.86)</td><td>0.1353***(6.13)</td><td>-0.1094***(-7.93)</td><td>-0.2603***(-15.01)</td></tr><tr><td>Max lab. imb.</td><td>0.3438***(19.30)</td><td>0.1427***(6.55)</td><td>-0.1338***(-9.67)</td><td>-0.3242***(-19.54)</td></tr><tr><td>Iteration*Low lab. imb.</td><td>-0.0012***(-3.71)</td><td>-0.0009**(-2.48)</td><td>0.0004*(1.86)</td><td>0.0010***(3.00)</td></tr><tr><td>Iteration*Medium lab. imb.</td><td>-0.0014***(-4.33)</td><td>0.0000(0.06)</td><td>0.0004*(1.79)</td><td>0.0012***(3.53)</td></tr><tr><td>Iteration*High lab. imb.</td><td>-0.0022***(-6.85)</td><td>0.0003(0.89)</td><td>0.0007***(2.96)</td><td>0.0019***(5.92)</td></tr><tr><td>Iteration*Max lab. imb.</td><td>-0.0018***(-5.84)</td><td>0.0009**(2.49)</td><td>0.0004*(1.66)</td><td>0.0015***(4.94)</td></tr><tr><td>N</td><td>1,500</td><td>1,500</td><td>49,495</td><td>26,665</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.487</td><td>0.317</td><td>0.023</td><td>0.066</td></tr><tr><td colspan="5">Note: We report robust standard errors that are clustered at the random seed level in parentheses. The dependent variables in Columns (1) and (2) are measures for the level of algorithmic discrimination. Specifically, in Column (1), we use the mean gender gap in the share of positive predictions per iteration as dependent variable. In Column (2) we use the mean gender gap in the false-negative error rates per iteration as dependent variable. In Columns (3) and (4), the dependent variables are dummy variables respectively indicating whether a game resulted in the same outcomes as a game under perfect information would have and whether an investor invested in a repaying borrower. For Columns (3) and (4), we only used the subsample of observations where the borrower was female. * p &lt; 0.1, ** p &lt; 0.05, *** p &lt; 0.01 denote statistical significance levels.</td></tr></table>

Table A34. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in pos. preds.</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>-0.0004(0.000)</td><td>-0.0016***(0.000)</td><td>-0.0017***(0.000)</td><td>-0.0025***(0.000)</td><td>-0.0021***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>0.0007**(0.000)</td><td>0.0007*(0.000)</td><td>0.0002(0.000)</td><td>0.0007**(0.000)</td><td>0.0009***(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0003(0.000)</td><td>0.0018***(0.000)</td><td>0.0013***(0.000)</td><td>0.0015***(0.000)</td><td>0.0019***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0009***(0.000)</td><td>0.0023***(0.000)</td><td>0.0015***(0.000)</td><td>0.0022***(0.000)</td><td>0.0021***(0.000)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.027</td><td>0.138</td><td>0.179</td><td>0.308</td><td>0.364</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the share of positive predictions per iteration as dependent variable. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Table A35. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Gender gap in FNR error</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>-0.0012***(0.000)</td><td>-0.0021***(0.000)</td><td>-0.0012***(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0003(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>0.0006(0.000)</td><td>0.0013***(0.000)</td><td>0.0001(0.000)</td><td>0.0004(0.000)</td><td>0.0006*(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>0.0003(0.000)</td><td>0.0021***(0.000)</td><td>0.0011***(0.000)</td><td>0.0014***(0.000)</td><td>0.0013***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>0.0014***(0.000)</td><td>0.0027***(0.000)</td><td>0.0016***(0.000)</td><td>0.0015***(0.000)</td><td>0.0013***(0.000)</td></tr><tr><td>Observations</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td><td>1,200</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.115</td><td>0.198</td><td>0.170</td><td>0.117</td><td>0.076</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, we use the mean gender gap in the false-negative error rates per iteration as dependent variable. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Table A36. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Outcome under perf. inf(female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0017***(0.000)</td><td>0.0021***(0.000)</td><td>0.0021***(0.000)</td><td>0.0024***(0.000)</td><td>0.0021***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0004(0.000)</td><td>-0.0008***(0.000)</td><td>-0.0005**(0.000)</td><td>-0.0008***(0.000)</td><td>-0.0006***(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0008***(0.000)</td><td>-0.0011***(0.000)</td><td>-0.0012***(0.000)</td><td>-0.0015***(0.000)</td><td>-0.0015***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0012***(0.000)</td><td>-0.0017***(0.000)</td><td>-0.0016***(0.000)</td><td>-0.0020***(0.000)</td><td>-0.0019***(0.000)</td></tr><tr><td>Observations</td><td>39,596</td><td>39,596</td><td>39,596</td><td>39,596</td><td>39,596</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.019</td><td>0.021</td><td>0.019</td><td>0.016</td><td>0.014</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is dummy variables indicating whether a game resulted in the same outcomes as a game under perfect information would have. We only used the subsample of observations where the borrower was female. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

Table A37. OLS Regression Estimates

<table><tr><td></td><td colspan="5">Initial label imbalance in training data</td></tr><tr><td>Dep. variable:</td><td>No</td><td>Low</td><td>Medium</td><td>High</td><td>Max</td></tr><tr><td>Invest w. repaying borrower (female borrowers)</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Iteration</td><td>0.0020***(0.000)</td><td>0.0030***(0.000)</td><td>0.0031***(0.000)</td><td>0.0038***(0.000)</td><td>0.0035***(0.000)</td></tr><tr><td>Iteration*Medium human discr.</td><td>-0.0007**(0.000)</td><td>-0.0012***(0.000)</td><td>-0.0009***(0.000)</td><td>-0.0014***(0.000)</td><td>-0.0012***(0.000)</td></tr><tr><td>Iteration*High human discr.</td><td>-0.0012***(0.000)</td><td>-0.0019***(0.000)</td><td>-0.0021***(0.000)</td><td>-0.0024***(0.000)</td><td>-0.0027***(0.000)</td></tr><tr><td>Iteration*Very high human discr.</td><td>-0.0017***(0.000)</td><td>-0.0026***(0.000)</td><td>-0.0026***(0.000)</td><td>-0.0035***(0.000)</td><td>-0.0034***(0.000)</td></tr><tr><td>Observations</td><td>21,332</td><td>21,332</td><td>21,332</td><td>21,332</td><td>21,332</td></tr><tr><td>p</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr><tr><td>R-squared</td><td>0.086</td><td>0.101</td><td>0.101</td><td>0.102</td><td>0.134</td></tr></table>

Note: We report robust standard errors that are clustered at the random seed level in parentheses. In each column, the dependent variable is a dummy variable indicating whether an investor invested in a repaying borrower. We only used the subsample of observations where the borrower was female. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01 denote statistical significance levels.

The regression tables A33 to A37 show results for simulations that were conducted as robustness checks. Specifically, for this robustness check, the number of matched investors and borrowers equals 60. By contrast, for the results reported in our main text, this number equals 50. As in the simulations whose results we report in the main text, we set the size of the minority share of women in the training data used to train the ML model that predicts borrower repayment behavior to 20%. The depicted regression results reveal that our main findings are largely robust to this variation in the parametrization of our simulation. Specifically, we observe that algorithmic discrimination decreases over time whereas economic efficiency increases. We again see that the level of the initial degree of the label imbalance in the training data affects the self-correcting mechanisms negatively (see Table A33). Tables A34 to A37 reveal that our insights regarding the role of the level of persistent human discrimination are also robust. Specifically, the higher the level of persistent human discrimination the less likely it is that the self-correcting mechanisms will occur.

## Appendix B: Details On Prior Empirical Studies A and B

## B.1 Study A

In the field study, participants engaged in the following sequential social dilemma game: There are two parties: a trustor and a trustee who both initially receive 10 monetary units (MU). The trustor begins by deciding whether to keep or invest the entire 10 MU with the trustee. If the trustor decides to invest, the trustee receives double the amount, which is added to the trustee’s endowment—i.e., the trustee temporarily has 30 MU. If the trustor chooses to keep the 10 MU, both the trustor and the trustee temporarily possess 10 MU. After the trustor makes her decision, it is the trustee’s turn, and he decides whether to keep his entire 10 MU or send them to the trustor. If the trustor sends the 10 MU, the trustor receives double the amount, which is added to her temporarily held MU. With this structure, there are four possible outcomes:

(1) Both keep their 10 MU, i.e., no transaction takes place and both earn 10 MU; (2) the trustor keeps his 10 MU whereas the trustee transfers her 10 MU so that the trustor and trustee end up with 30 MU and 0 MU, respectively; (3) the trustor transfers her 10 MU whereas the trustee keep his 10 MU so that the trustor and trustee end up with 0 MU and 30 MU, respectively; and (4) both the trustor and trustee transfer their 10 MU to each other so that both end up with 20 MU. Note that the socially most efficient outcome is the last one. Figure B1 illustrates the game structure.

![](/api/attachments/VVM428SH/fulltext/images/8815bd7af72589984dc70c6d4564d45b71c620cb0a5fd84cf838ff21c9d66c40.jpg)  
Figure B1. Game Structure

For our simulation, we simplified the game by removing the trustee’s decision following the trustor’s decision to keep the MU. This allowed us to render the interaction mirror real-world economic transactions more closely. In the context of a loan approval (hiring) decision, for example, the full game would have allowed for the possibility that the applicant repaid the loan to the bank (worked for the firm) even if the applicant did not receive the loan (was not hired). Hence, by simplifying the game in the way we do, we sought to make the transaction setting more realistic. Additionally, the simplified structure increases the complexity of the continuous learning environment because it introduces the selective labels problem (Lakkaraju et al., 2017). If the party that goes second, i.e., the borrower in our simulation, were to always make an observable decision that is independent of the trustor, this real-world complexity would not arise.

Simplifying the game removes 63 observations from our dataset. Importantly, our results do not depend on the inclusion or exclusion of these observations. As the following table shows, we did not find significant differences in the distribution for the majority of characteristics of participants who we excluded and for those we did not observe (see Table B1). One exception is for patience and reciprocity, where we observed a significant difference at the 1% level. This result gives us confidence that we did not create endogeneity problems.

Table B1. Overview of Participants’ Characteristics.

<table><tr><td></td><td colspan="3">Excluded participants</td><td colspan="3">Included participants</td><td>Wilcoxon rank sum test</td></tr><tr><td></td><td>Count</td><td>Mean</td><td>Std. Dev.</td><td>Count</td><td>Mean</td><td>Std. Dev.</td><td>p-value</td></tr><tr><td>Competitiveness</td><td>64</td><td>.596</td><td>.229</td><td>1048</td><td>.637</td><td>.219</td><td>p=0.09</td></tr><tr><td>Openness</td><td>64</td><td>.649</td><td>.219</td><td>1048</td><td>.617</td><td>.213</td><td>p=0.12</td></tr><tr><td>Conscientiousness</td><td>64</td><td>.635</td><td>.239</td><td>1048</td><td>.634</td><td>.204</td><td>p=0.73</td></tr><tr><td>Agreeableness</td><td>64</td><td>.688</td><td>.193</td><td>1048</td><td>.658</td><td>.197</td><td>p=0.19</td></tr><tr><td>Neuroticism</td><td>64</td><td>.498</td><td>.225</td><td>1048</td><td>.517</td><td>.217</td><td>p=0.43</td></tr><tr><td>Extraversion</td><td>64</td><td>.629</td><td>.215</td><td>1048</td><td>.644</td><td>.223</td><td>p=0.55</td></tr><tr><td>Younger siblings</td><td>64</td><td>.558</td><td>.499</td><td>1048</td><td>.511</td><td>.5</td><td>p=0.38</td></tr><tr><td>Older siblings</td><td>64</td><td>.495</td><td>.503</td><td>1048</td><td>.445</td><td>.497</td><td>p=0.34</td></tr><tr><td>Gender</td><td>64</td><td>.632</td><td>.485</td><td>1048</td><td>.533</td><td>.499</td><td>p=0.06</td></tr><tr><td>Patience</td><td>64</td><td>.614</td><td>.229</td><td>1048</td><td>.543</td><td>.233</td><td>p&lt;0.01**</td></tr><tr><td>Reciprocity</td><td>64</td><td>.663</td><td>.475</td><td>1048</td><td>.5</td><td>.5</td><td>p&lt;0.01**</td></tr><tr><td colspan="8">Note: We indicate significance levels by *p&lt;0.05, **p&lt;0.01, and ***p&lt;0.001.</td></tr></table>

Instructions. Prior field study (for Study 1). We collected this data in an incentivized field study that we conducted at a large German university over three years (2016-2019). Most importantly for the experiment at hand, the field study included an incentivized one-shot, sequential social dilemma game where we anonymously matched participants in pairs of two and initially gave each participant 10 euros. Participants could either keep the 10 euros for themselves or transfer them to their opponent. Whenever one player transferred their 10 euros, we doubled the amount so that the other player received 20 euros. Players made their choices sequentially. The second player made their decision contingent on the first player’s choice. For each participant, we elicited both the conditional choice of the second player and the unconditional choice of the first player. In addition to the incentivized game, the field study included a broad set of survey items on students’ demographics, including socioeconomic background, cognitive abilities, personal traits, and other preferences. We present the exact instructions of the field study as follows:

How far do you live from your parents?

Please select only one of the following answers: I live at my parents 1-10 KM away 11-50 KM away 51-150 KM away More than 150 KM away

Have you, due to your studies, changed your place of residence? Please select only one of the following answers: Yes No How many siblings do you have? Please enter your answers below: Younger siblings [ ] Older siblings [ ] Please indicate with which hand you prefer to perform the following activities: (Always right, mostly right, both hands, mostly left, always left) Write [ ] Throw [ ] Tooth brushing [ ] Holding a spoon [ ]

What languages do you speak at home? (multiple answers are possible)

Please select all applicable answers: German Another language

Please indicate with which hand you prefer to perform the following activities (always right, mostly right, both hands equally, mostly left, mostly right):

Writing Throwing Cleaning teeth

Holding a spoon Please indicate the highest degree of both your parents. (Mother and father) University University of applied science Technical college (former GDR) Technician or master craftsman examination Apprenticeship No educational background Unknown

How do you finance yourself? (multiple answers are possible) (Please select all applicable answers:) My parents support me financially BAföG -Scholarship Job as student assistant (Hiwi) at the university • Job as a tutor at the university Job outside the university

At which type of school did you get your university entrance qualification? (Please select only one of the following answers:) High school Comprehensive school Vocational school Other

After how many school years did you receive your university entrance qualification? (Please select only one of the following answers:) After less than 12 years After 12 years After 13 years After more than 13 years

In which federal state of Germany did you acquire your university entrance qualification? (Please enter only one answer:) []

Which of the following subjects did you take at school in the upper school and what grades (between 1.0 and 4.0) did you have in these subjects in your Abitur certificate? (Please select all applicable answers:) German English Physics Math

Which of these subjects did you take as advanced courses at school? (Please select all applicable answers:) German English Physics

## Math

None of these subjects

On a scale from 1 (completely correct) to 6 (completely incorrect) please indicate the accuracy of the following statements. I chose my present course of study because... ...it particularly interested me and I wanted to. ...it corresponds to my inclinations and talents.

...as a graduate of this course of studies I expect particularly good earning and employment opportunities.

...I didn’t know what else to do. ...I was influenced in my decision by my family / friends. Is your current course of study your dream study? (Please select only one of the following answers:)

Yes No

On a scale from 1 (completely sure) to 5 (completely unsure) please indicate the accuracy of the following statements. How confident are you in your choice of study? How satisfied are you today with your choice of study? How certain are you that you will complete your studies? How certain are you that you will complete your studies at this University? Did you do one or more of the following activities before starting your current studies?

Other:

How many semesters do you estimate you will need in total until you graduate from your current course? Please enter your answer below: Please enter your answer here [ ]

Begin a further study (e.g. Master’s degree) Start working Other

Based on my grade point average, I expect to belong to... (Please select only one of the following answers:) the top [ ] percent of my year of study.

How important is it to you to maintain your grade point average in your studies or even improve? (Please select only one of the following answers:) Very important Rather important Indifferent Unimportant Very unimportant

How many hours a week do you think you should invest in your studies? Please enter your answer below: Please enter your answer here [ ]

How many hours do you think you will actually invest in your studies each week? Please enter your answer here [ ] How many hours a week do you currently invest in your studies?

Do you believe that your future earnings will depend on your final grade in your studies? Please select only one of the following answers: Completely applicable Mostly applicable Applies Mostly not applicable Completely not applicable

How do you personally assess yourself? Are you generally a person willing to take risks or do you try to avoid risks? Please answer using the following scale, where the value 0 means: “Not willing to take risks at all”, and the value 10: “Very willing to take risks”. With the values in between you can grade your assessment.

Please enter your answer here [ ]

How do you personally assess yourself? Are you generally a person who is impatient or who is always very patient? Please answer using the following scale, where the value 0 means “very impatient” and the value 10 means “very patient”. With the values in between you can grade your assessment.

Please enter your answer here [ ]

To what extent do you agree with the following statement: “I’m a narcissist.” (Note: A narcissist is selfish, selfcentered, vain.)?

Please answer using the following scale, where a value of 1 means “do not agree at all” and a value of 5 means “agree completely”. With the values in between you can grade your assessment.

Please enter your answer here [ ]

How would you assess yourself in the context of the following statements?

Please answer using the following scale, where 1 means “do not agree at all” and 5 means “agree completely”. The values in between allow you to grade your assessment. I like to find myself in situations where I am in competition with others. It is important for me to be better at a task than others. I think it’s important to win at work and at games. I try harder when I compete with others.

In the list below are different characteristics a person can have. It is likely that some characteristics will apply fully to you personally and others not at all. For others, you may be undecided.

Please answer using the following scale from 1 to 5: A score of 1 means not applicable at all; 5 means fully applicable. With the values between 1 and 5 you can grade your opinion.

I am someone who... works thoroughly is communicative, talkative is sometimes a little rough on others • is original, brings in new ideas is forgiving is rather lazy can come out of herself/himself is sociable appreciates artistic, aesthetic experiences • is easily nervous completes task effectively and efficiently • is reserved is considerate and friendly with others has a vivid imagination is relaxed, can handle stress well

For the following decision situation, another survey participant will be assigned to you randomly. You and this other person make different decisions, which then result in your payout and the payout of the other person. At the beginning you and the other person will each receive 10 Euros from us. You have the following two options to choose from:

Option A: You keep your 10 euros.

Option B: You give your 10 euros to the other person. The 10 euros are doubled, i.e. the other person receives 20 euros.

The other person also has these two options to choose from. Hence, there are four possible outcomes, depending on how you and the other person decide: If you and the other person both choose option A, you will both end up with 10 euros each. If you and the other person both choose option B, both of you will each have 20 euros. If you choose option A and the other person chooses option B, you will have 30 euros and the other person 0 euros. And vice versa, if you choose option B and the other person chooses option A, you have 0 euros and the other person has 30 euros. In the following two situations, please decide whether you would rather choose option A or option B. The situations differ in whether you or the other person makes their decision first.

Situation 1: You decide first and the other person is informed of your decision. Which option do you choose?

## A/B

Situation 2: The other person makes their decision first, and you are informed of their decision. Which option do you choose if the other person has chosen option A?

## A/B

Which option do you choose if the other person has chosen option B?

## A/B

## B.2 Study B

In the following we outline the part of the online experiment that we use for our simulations. Note that the other parts of the experiment are independent of the one used in our simulation because there is no intermediary feedback at any point. Therefore, we are confident that there are no spillover effects we need to consider. Importantly, the model we employed in Study B (also a gradient boosted forest) to predict repayment behaviors of borrowers was trained on data from Study A, i.e., the repayment prediction model in our simulation is effectively the same as the one that participants in Study B interacted with. Additionally, the borrowers that Study B participants encounter are borrowers we take from the data of Study A, i.e., the simulated investors in our simulation encounter borrowers from the same dataset as actual participants in Study B.

![](/api/attachments/VVM428SH/fulltext/images/230d739b4a58cadd793ca3a06e1240339d2120de296f9732eea67e5a6c2e27dc.jpg)  
Figure B2. Overview of Decision Tree Outcome Possibilities

Instructions: You will play 20 rounds of a game that has the same structure as in the previous parts of the experiment:

At the beginning of every round, you will be randomly matched with a new anonymous person from another study. Both you and the other person will receive 10 monetary units. Your task is always the same: You will make a decision about whether you want to keep your 10 monetary units or transfer all of them to the other person. Note: You cannot transfer only part of your endowment.

Keeping and transferring your monetary units has the following consequences:

Keeping your 10 monetary units: If you decide to keep the 10 monetary units for yourself, the game in this round ends. In this case, your personal and the other person’s earnings in this round both equal 10 monetary units, i.e., the initial endowment.

Transferring your 10 monetary units: If you decide to transfer the 10 monetary units, we will double this amount so that the other person receives 20 monetary units which are then added to this person’s initial endowment. After you transfer your monetary units, the other person will learn about your transfer and will have to decide whether to transfer 10 monetary units back to you or to keep the monetary units they now possess.

If the other person transfers 10 monetary units back to you, we will double this amount so that you will receive 20 monetary units. In this case, your personal and the other person’s earnings in this round will both equal 20 monetary units. If the other person does not transfer 10 monetary units back to you, your personal earnings will equal 0 monetary units while the other person’s earnings will equal 30 monetary units in this round.

Before you are asked to choose whether you will transfer or keep your 10 monetary units, you will receive information about 10 personal characteristics of the other person that is matched with you in a given round. This information might help you anticipate whether this other person will transfer the 10 monetary units back to you; in this case, you would receive 20 monetary units if you initially decide to make a transfer.

Note: The scale of nonbinary characteristics is: very low, low, medium, high, very high.

In every round, a machine learning system produces a prediction about whether the person currently matched with you is likely to transfer 10 monetary units back to you so that you receive 20 monetary units if you initially decide to make a transfer. To make a prediction about a specific person, the machine learning system only uses the person’s 10 personal characteristics that you also observe in the corresponding round.

The machine learning system is a gradient boosted gradient boosted random forest that was trained and tested on data from a previous study. Gradient boosted random forest classifiers, despite their simplicity, are among the most powerful machine learning algorithms available today. They are widely used in a variety of domains by scientists and practitioners alike. In a test, the system used in the experiment reaches a recall score of 79.3%, which means that it correctly recognizes roughly 4 out of 5 people who actually reciprocate in the case of a transfer. In other words, the machine learning system’s prediction might help you better anticipate whether you will receive the 20 monetary units if you initially decide to make a transfer. Below you can find additional information about the structure of the system.

As implied by its name, a gradient boosted random forest consists of a large number of individual decision trees that operate as an ensemble. Based on examples, individual decision trees learn logical rules which assign a certain label to new observations. These rules can be imagined as a sequence of consecutive questions. In the context of the game at hand, a single tree could, for example, identify the following sequence of questions: 1. Is the person open to new experiences? Yes; 2. Is the person female? No; 3. Is the person highly competitive? Yes. Result: Given the answers to the question sequence, the person will most likely return monetary units back to you if you initiate a transfer. During the training process, the algorithm (more or less) automatically identifies the most informative questions to classify people as quickly as possible. Notably, each tree in the forest tries to correct the inaccuracies of previous trees, thereby trying to boost the performance of the overall forest. Gradient boosted random forests typically comprise hundreds or even thousands of individual trees.

Each individual tree in a gradient boosted random forest spits out a prediction and the class (i.e. whether or not the other person will return the 10 monetary units) with the most votes becomes the gradient boosted random forest’s prediction. In other words: Knowing that individual trees can be (randomly) wrong, we rely on the wisdom of the crowd, so that nonsystematic errors of individual trees cancel each other out. As a type of ensemble learner, gradient boosted random forests are among the most powerful machine learning algorithms currently available.

Between rounds, you will not see the decision of the persons you are matched with. That part ends once you have played 20 rounds of the game. We will then randomly select one of the rounds. The monetary units you own at the end of this round constitute your earnings for Part 3. The other person matched to you in this round earns the number of monetary units they own at the end of this round as well. Whether the earnings are payoff-relevant for the other person is randomly determined. We will inform you about the decision of the other person, your earnings, and the other person’s earnings from the selected round at the end of the experiment.

Screenshot: The following Figure B3 shows a screenshot of the decision interface that participants faced in the online experiment.

Prediction by Machine Learning System about the other person's propensity to reciprocate a transfer  
You will most likely receive 0 monetary units, if you initially make a transfer (i.e. the other person will most likely NOT reciprocate your transfer).

<table><tr><td></td><td>Current person&#x27;s personal characteristics</td></tr><tr><td>Level of the other person&#x27;s approachability:</td><td>Medium</td></tr><tr><td>Whether the other person has older siblings:</td><td>No</td></tr><tr><td>Propensity of the other person to be warm and considerate towards others:</td><td>Medium</td></tr><tr><td>Propensity of the other person to become upset/ stressed:</td><td>Low</td></tr><tr><td>The other person&#x27;s biological sex:</td><td>Female</td></tr><tr><td>Level of the other person&#x27;s patience:</td><td>Medium</td></tr><tr><td>Level of the other person&#x27;s conscientiousness:</td><td>High</td></tr><tr><td>Whether the other person has younger siblings:</td><td>No</td></tr><tr><td>Level of the other person&#x27;s openness to new experiences:</td><td>Low</td></tr><tr><td>Level of the other person&#x27;s competitiveness:</td><td>Very high</td></tr></table>

Please make your decision and click on the "Next"-Button (appears after 5 seconds)  
What do you want to do:

Keep your 10 monetary units

Transfer your 10 monetary units

Figure B3. Screenshot of the Decision Interface

## Appendix C: Technical Details on Simulation

## C.1 Details on the Repayment-Predicting ML Model in Simulations

To gain insights into the determinants of the predictions of the ML model that aims to forecast whether borrowers will make a repayment, we use the popular SHAP (Shapley additive explanations) explainability method (Lundberg & Lee, 2017). Notably, we show results for the models’ behaviors before any updating takes place. SHAP is inspired by cooperative game theory explaining individual predictions by assuming that each feature value of the instance is a player in a game where the prediction is the payout. Estimated SHAP values describe the average marginal contribution of a feature value across all possible feature coalitions of a given instance. By averaging the SHAP values across all possible values a feature can take on, we obtained a reliable measure of this feature’s importance for the prediction task. In the following, we show SHAP values for initially biased and unbiased ML models. Each figure contains information on the overall importance of each feature for the prediction (higher position in the vertical ranking) and the features’ marginal effects for predictions about individual instances (position on the x-axis). Each dot represents a SHAP value for a feature and an instance. The color of the dots depicts the value of the feature from low (blue dots) to high (red dots). Plots jitter identical SHAP values vertically, providing insights into the SHAP value distribution per feature. Overall, Figures C1 and C2 show the relationship between the features (borrower characteristics) and the prediction (likelihood of this person making a repayment) by revealing their marginal contribution to predictions (in terms of probability) conditional on feature values.

![](/api/attachments/VVM428SH/fulltext/images/b83ea68de6aebf44c5a65c9b86a88c4601dd66987bb7e71bb7b6f584cafbe35b.jpg)  
Figure C1. SHAP Values, Example of Biased ML Model (max. initial label imbalance)

The figure for the biased ML reveals that prior to any retraining, the gender attribute (0 = female, 1 = male) is the most relevant feature to predict whether a borrower will make a repayment. Our findings indicate that being female always decreases the predicted likelihood that a repayment will occur, whereas being male always increases it.

![](/api/attachments/VVM428SH/fulltext/images/aa8878c68385d33ed3333d3fa71647f2832170620dcccf60cbf25e6ad4b2b854.jpg)  
Figure C2. SHAP Values, Unbiased ML Model

The figure for the unbiased ML reveals that prior to any retraining, the gender attribute (0 = female, 1 = male) is the least important feature to predict whether a borrower will make a repayment. By comparing the figure for the biased ML model, we find that being female (almost) always increases the predicted likelihood that a repayment will occur, whereas being male (almost) always decreases it. Importantly, apart from gender, the marginal contributions of most other features are reasonably similar for the two ML models. That is, the introduction of discrimination against women really does seem to originate from the gender attribute. It does not appear to be the case that our biasing strategy distorted the model in other dimensions as well.

Table C1. Hyperparameters Automatically Optimized in the Training Process of Investor and  
Borrower Repayment Models

<table><tr><td>Hyperparameter</td><td>Range of hyperparameter value</td></tr><tr><td>Learning rate</td><td>0.001, 0.01, 0.05</td></tr><tr><td>Minimum child weight</td><td>1, 10</td></tr><tr><td>Maximum depth of tree</td><td>3, 4, 5, 6, 7, 8</td></tr><tr><td>Subsample of observations to build a tree</td><td>0.5, 0.6, 0.7</td></tr><tr><td>Subsample of variables to build a tree</td><td>0.5, 0.6</td></tr><tr><td>Subsample of variables to make a split</td><td>0.5, 0.6</td></tr><tr><td>Number of trees</td><td>100, 300, 500</td></tr></table>

Table C2. Overview of Variables Included in the ML Models.

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td></tr><tr><td colspan="3">Investor traits included only in model that simulates investor behavior</td></tr><tr><td>Algorithm aversion 1</td><td>0.456667</td><td>0.498160</td></tr><tr><td>Algorithm aversion 2</td><td>0.456667</td><td>0.498160</td></tr><tr><td>Algorithm aversion 3</td><td>2.703.333</td><td>1.813.616</td></tr><tr><td>Algorithm aversion 4</td><td>1.856.667</td><td>1.279.217</td></tr><tr><td>Risk aversion 1</td><td>4.656.667</td><td>2.756.820</td></tr><tr><td>Risk aversion 2</td><td>5.423.333</td><td>2.357.622</td></tr><tr><td>Overconfidence 1</td><td>0.663333</td><td>0.472609</td></tr><tr><td>Overconfidence 2</td><td>0.640000</td><td>0.480040</td></tr><tr><td>Overconfidence 3</td><td>0.363333</td><td>0.481000</td></tr><tr><td>Altruism</td><td>120.190.000</td><td>190.281.480</td></tr><tr><td>Reciprocity 1</td><td>3.713.333</td><td>1.784.662</td></tr><tr><td>Reciprocity 2</td><td>8.863.333</td><td>1.491.652</td></tr><tr><td>Reciprocity 3</td><td>2.860.000</td><td>2.475.498</td></tr><tr><td>Trust</td><td>5.146.667</td><td>2.655.748</td></tr><tr><td>Age</td><td>34.990.000</td><td>12.195.683</td></tr><tr><td>Academic degree</td><td>2.090.000</td><td>1.081.093</td></tr><tr><td>Gender (Trustor)</td><td>0.560000</td><td>0.496428</td></tr><tr><td>Work experience (in years)</td><td>13.753.333</td><td>14.045.356</td></tr><tr><td>Living area</td><td>1.216.667</td><td>0.685420</td></tr><tr><td>Bayes rationality</td><td>0.873333</td><td>0.332627</td></tr><tr><td colspan="3">Borrower traits included in model to simulate investor behavior and model to predict borrower repayments</td></tr><tr><td>Openness</td><td>0.586389</td><td>0.214753</td></tr><tr><td>Conscientiousness</td><td>0.687500</td><td>0.150325</td></tr><tr><td>Extraversion</td><td>0.652583</td><td>0.217390</td></tr><tr><td>Agreeableness</td><td>0.746611</td><td>0.151998</td></tr><tr><td>Neuroticism</td><td>0.464389</td><td>0.226363</td></tr><tr><td>Gender (trustee)</td><td>0.590500</td><td>0.491783</td></tr><tr><td>Competitiveness</td><td>0.612361</td><td>0.237561</td></tr><tr><td>Patience</td><td>0.545200</td><td>0.217297</td></tr><tr><td>Younger siblings</td><td>0.497500</td><td>0.500035</td></tr><tr><td>Older siblings</td><td>0.510667</td><td>0.499928</td></tr></table>

## C.2 Software Information

Requirements file for simulation using Python 3.8

```txt
aiohttp==3.8.4
aiosignal==1.3.1
async-timeout==4.0.2
attrs==23.1.0
blinker==1.6.2
certifi==2023.5.7
charset-normalizer==3.2.0
click==8.1.3
contourpy==1.0.7
cycler==0.11.0
fairlearn==0.8.0
Flask==2.3.2
fonttools==4.39.2
frozenlist==1.4.0
idna==3.4
importlib-metadata==6.6.0
importlib-resources==5.12.0
itsdangerous==2.1.2
Jinja2==3.1.2
joblib==1.2.0
kiwisolver==1.4.4
MarkupSafe==2.1.2
matplotlib==3.7.1
multidict==6.0.4
numpy==1.24.2
openai==0.27.8
packaging==23.0
pandas==1.5.3
Pillow==9.4.0
pyaml==23.5.8
pyparsing==3.0.9
python-dateutil==2.8.2
pytz==2022.7.1
PyYAML==6.0
regex==2023.6.3
requests==2.31.0
scikit-learn==1.2.2
scikit-optimize==0.9.0
scipy==1.10.1
session-info==1.0.0
six==1.16.0
stdlib-list==0.8.0
threadpoolctl==3.1.0
tiktoken==0.4.0
tk==0.1.0
tqdm==4.65.0
urllib3==2.0.3
Werkzeug==2.3.4
xgboost==1.7.5
yarl==1.9.2
zipp==3.15.0
```

## C.3 Source Code

```python
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, recall_score, precision_score, roc_auc_score
import os
import xgboost as xgb
from skopt import BayesSearchCV
import pickle
import random
import multiprocessing

# FUNCTION FOR SIMULATIONS IN MULTIPROCESSING
def Simulation(discr_by_FM, discr_by_algo, DISCR_NAD, DISCR_NTD, train_features, label, train_features_fm, label_fm, IN_LOOP, outer, X_train_FM, y_train_FM, df_exp, df, fm_pool, p = 0.2, selection_size=50):
temp_ = ['Competitiveness_Score_SM', 'Openness_SM', 'Conscientiousness_SM', 'Agreeableness_SM', 'Neuroticism_SM', 'Extraversion_SM', 'gender_SM', 'financed_by_parents_SM', 'younger_siblings_SM', 'older_siblings_SM']

# SAVINGS PATH:
path_out = f'/XXX/outNAD{DISCR_NAD}NTD{DISCR_NTD}Out{outer}MinS{p}SelSi{selection_size}.csv'

# SEARCH SPACE XGBOOST
search_space = {
'learning_rate': [0.001, 0.01, 0.05],
'min_child_weight': [1, 10],
'max_depth': [3, 4, 5, 7, 8],
'subsample': [0.5, 0.6, 0.7],
'colsample_bytree': [0.5,0.6],
'colsample_bylevel': [0.5,0.6],
'reg_lambda': [1e-9],
'reg_alpha': [1e-9],
'n_estimators': [100, 300, 500],
}

# INITIALIZING THE CLASSIFIER
# BAYES OPTIMIZATION
opt = BayesSearchCV(
estimator=xgb.XGBClassifier(
n_jobs=-1,
objective='binary:logistic',
eval_metric='logloss',
tree_method='approx'
),
search_spaces=search_space,
scoring='roc_auc',
cv=3,
n_jobs=-1,
n_iter=25,
verbose=0,
refit=True,
random_state=outer
)

# FITTING
opt.fit(X_train_FM, y_train_FM)
fm_model = opt.best_estimator_

# MANIPULATING SM DATA
df_field = df[df['second_mover_cond_A'] == 0][train_features + [label]]
df_model = df_field.sample(frac=0.70,
replace=False,
random_state=outer)

df_simul = df_field.loc[~(df_field.index.isin(df_model.index))]

df_prep = df_model.copy()
df_women0 = df_prep[(df_prep['gender'] == 0) & (df_prep['second_mover_cond_B'] == 0)].copy()
df_women1 = df_prep[(df_prep['gender'] == 0) & (df_prep['second_mover_cond_B'] == 1)].copy()
df_men = df_prep[df_prep['gender'] == 1].copy()
n = len(df_prep)
n_minority = int(p * n)
n_majority = int((1 - p) * n)

df_men = df_men.sample(n=n_majority, replace=True)
df_women0_ = df_women0.sample(n=int(n_minority * DISCR_NAD), replace=True)
df_women1_ = df_women1.sample(n=int(n_minority * (1 - DISCR_NAD)), replace=True)
df_prep = pd.concat([df_men, df_women0_, df_women1_], axis=0).sample(frac=1).reset_index(drop=True)

# START OF LOOPING
df_pool_sm = df_simul.sample(frac=1,
replace=False,
random_state=outer)

added_ = []

# INITIAL SM MODEL TRAINING
opt = BayesSearchCV(
estimator=xgb.XGBClassifier(
n_jobs=-1,
objective='binary:logistic',
eval_metric='logloss',
tree_method='approx'
),
search_spaces=search_space,
scoring='roc_auc',
cv=3,
n_jobs=-1,
n_iter=50,
verbose=0,
refit=True,
random_state=outer
)

# FITTING
opt.fit(df_prep[train_features], df_prep[label])
sm_model = opt.best_estimator_

# SAVING THE INITIAL MODEL
pickle.dump(sm_model, open(f'/XXX/Model{DISCR_NAD}NTD{DISCR_NTD}.pkl', "wb"))
df_pool_sm.to_csv(f'/XXX/DF_SHAP_TEST{DISCR_NAD}NTD{DISCR_NTD}.csv',
sep=',',
na_rep='',
index=False)
```

```python
for inner in range(IN_LOOP):
    df_fm = fm_pool.sample(n=selection_size,
    replace=False,
    random_state=outer)

    df_sm = df_pool_sm.sample(n=len(df_fm),
    replace=False,
    random_state=inner)

    # SM MODEL TRAINING
    # BAYES OPTIMIZATION
    opt = BayesSearchCV(
    estimator=xgb.XGBClassifier(
    n_jobs=-1,
    objective='binary:logistic',
    eval_metric='logloss',
    tree_method='approx'
    ),
    search_spaces=search_space,
    scoring='roc_auc',
    cv=3,
    n_jobs=-1,
    n_iter=50,
    verbose=0,
    refit=True,
    random_state=outer

    )

    # FITTING
    opt.fit(df_prep[train_features], df_prep[label])
    sm_model = opt.best_estimator_

    # MAKING PREDICTIONS AND ESTIMATING PERFORMANCE FOR CURRENT ROUND
    df_sm['prediction'] = sm_model.predict(df_sm[train_features])
    df_sm['prediction_proba'] = sm_model.predict_proba(df_sm[train_features})[:, 1]
    roc = roc_auc_score(df_sm['second_mover_cond_B'], sm_model.predict_proba(df_sm[train_features})[:, df_sm.columns = df_sm.columns + 'SM']
    df_sm['prediction'] = df_sm['prediction_SM']
    acc = accuracy_score(df_sm['second_mover_cond_B_SM'], df_sm['prediction'])
    prec = precision_score(df_sm['second_mover_cond_B_SM'], df_sm['prediction'])
    rec = recall_score(df_sm['second_mover_cond_B_SM'], df_sm['prediction'])

    recall_score(df_sm['second_mover_cond_B_SM'], df_sm['prediction'])

    df_sm = df_sm.sample(frac=1, random_state=inner).reset_index([
    ['prediction'] + temp_ + ['second_mover_cond_B_SM', 'index', 'prediction_proba_SM']]
    df_fm = df_fm.sample(frac=1, random_state=inner).reset_index(drop=True)
    df_game = pd.concat(df_fm, df_sm], axis=1)

    df_game['choice_FM'] = fm_model.predict_proba(df_game[train_features_fm])[:, 1] > 0.5

    # INTRODUCE DISCRIMINATION AGAINST WOMEN
    if DISCR_NTD != -1:
    v = df_game['gender_SM'].values == 0
    df_game.loc[v, 'choice_FM'] = fm_model.predict_proba(df_game.loc[v, train_features_fm])[:, 1] > 0.5 + DISCR_NTD

    # ### GAME OUTCOMES ###
    conditions = [(df_game['choice_FM'] == 1) & (df_game['second_mover_cond_B_SM'] == 1), # CC outcome
    (df_game['choice_FM'] == 1) & (df_game['second_mover_cond_B_SM'] == 0), # CD outcome
    (df_game['choice_FM'] == 0)] # D outcome - DC NOT APPLICABLE

    choices = ['CC', 'CD', 'D']
    df_game['outcome'] = np.select(conditions, choices)
    df_game['iteration'] = inner
    df_game['outer_iteration'] = outer
    df_game['discr_algo'] = discr_by_algo
    df_game['discr_fm'] = discr_by_FM
    df_game['acc_prediction'] = acc
    df_game['prec_prediction'] = prec
    df_game['rec_prediction'] = rec
    df_game['rocauc_prediction'] = roc
    df_game['FP'] = np.where((df_game['prediction'] == 1) & (df_game['second_mover_cond_B_SM'] == 0),
    df_game['FN'] = np.where((df_game['prediction'] == 0) & (df_game['second_mover_cond_B_SM'] == 1),
    df_game['TP'] = np.where((df_game['prediction'] == 1) & (df_game['second_mover_cond_B_SM'] == 1),
    df_game['TN'] = np.where((df_game['prediction'] == 0) & (df_game['second_mover_cond_B_SM'] == 0),

    # TRAINING DATA LENGTH
    df_game['N_train_data'] = len(df_prep)
    df_game['NRecWomen'] = df_prep[df_prep['gender'] == 0]['second_mover_cond_B'].sum()
    df_game['NWomen'] = len(df_prep[df_prep['gender'] == 0))
    df_game['NRecMen'] = df_prep[df_prep['gender'] == 1]['second_mover_cond_B'].sum()

    # FLAG THE ALREADY ADDED OBS AND DELETE THEM
    df_append = df_game.copy()
    df_append['added'] = np.where(df_append['index'].isin(added(), 1, 0)
    df_append = df_append[(df_append['outcome'] != 'D') & (df_append['added'] == 0)][temp_ + ['second_mover_cond_B_SM']].copy()
    df_append.columns = df_model.columns
    added_ += df_game['index'][df_game['choice_FM'] == 1].to_list()

    # ADDING DATA FRAMES
    df_prep = pd.concat(df_prep, df_append], axis=0).sample(frac=1, replace=False)

    # DISCRIMINATION SHARES
    df_game['DISCR_NAD'] = DISCR_NAD
    df_game['DISCR_NTD'] = DISCR_NTD

    # SIMUL TRAITS
    df_game['MATCH_SIZE'] = selection_size
    df_game['MIN_SHARE'] = p
    df_game = df_game.drop(['index'], axis=1)

    if not os.path.isfile(path_out):
    df_game.to_csv(path_out,
    sep=', ', ', 
    na_rep=', ', 
    index=False)

    else:
    df_game.to_csv(path_out,
    sep=', ', ', 
    na_rep=', ', 
    mode='a',
    header=False,
    index=False)
```

```python
##########
# HEADER OF SIMULATION AND EXECUTION IN MULTIPROCESS
##########
##########
# HEADER OF SIMULATION
##########
# LOOP PARAMETERS
N__ = 15 # 25
OUT_LOOP = random.sample(range(10000), N_)
IN_LOOP = 100
overall = N__ * IN_LOOP

# (MINORITY SHARE, MATCH SIZE) STANDARD: [0.2, 50]
robustness_combs = [[0.2, 50],
    [0.2, 30], [0.2, 40], [0.2, 60], [0.2, 70],
    [0.1, 50], [0.3, 50]]

# AD: SHARE OF NON-COOPERATING WOMEN IN THE MINORITY OF FEMALES (P=0.2)
# TD: ADDITIONAL PROBABILITY THRESHOLD FOR WOMEN ON TOP OF 50%, E.G.,
C = [[AD, TD] for AD in [0.5, 0.625, 0.75, 0.875, 1] for TD in [0.3,0.2,0.1,0]]

fm_traits = ['algo_aver_1', 'algo_aver_1.1', 'algo_aver_2', 'algo_aver_3',
    'q_risk_aversion_1', 'q_risk_aversion_2',
    'over_conf_1', 'over_conf_2', 'over_conf_3', 'altru', 'rec_1', 'rec_2',
    'rec_3', 'trust_1', 'age', 'academic_degree', 'gender_x', 'work',
    'area', 'bayes']

temp_ = ['Competitiveness_Score_SM', 'Openness_SM', 'Conscientiousness_SM',
    'Agreeableness_SM', 'Neuroticism_SM', 'Extraversion_SM', 'gender_SM',
    'financed_by_parents_SM', 'younger_siblings_SM', 'older_siblings_SM']

temp_2 = ['Competitiveness_Score', 'Openness', 'Conscientiousness',
    'Agreeableness', 'Neuroticism', 'Extraversion', 'gender_y',
    'financed_by_parents', 'younger_siblings', 'older_siblings']

##### DEFINING LABEL AND FEATURES ###
# SM PREDICTION: CONDITIONAL RESPONSE
train_features = ['Competitiveness_Score', 'Openness', 'Conscientiousness',
    'Agreeableness', 'Neuroticism', 'Extraversion', 'gender',
    'financed_by_parents', 'younger_siblings', 'older_siblings']

label = 'second_mover_cond_B'

# FM PREDICTION: BEHAVIOR
train_features_fm = ['prediction'] + temp_ + fm_traits
label_fm = 'decision'

##########
# EXECUTION OF SIMUL FUNCTION
##########
if __name__ == "__main__":
    processes = []

    for outer in OUT_LOOP:
    for i in C:
    for j in robustness_combs:
    discr_by_FM = 1
    discr_by_algo = 1
    DISCR_NAD = i[0]
    DISCR_NTD = i[1]
    q=j[0]
    selection_size=j[1]

    #### IMPORT DATA ###
    ## SM DATA
    df = pd.read_csv(r'/XXX/training_data.csv', sep=', ', encoding='utf-8').drop(
    ['financed_by_parents'], axis=1).astype('float32')
    df['financed_by_parents'] = df['impatiencesq001']

    ## FM DATA
    overall__ = pd.read_csv(r'/XXX/transfer_complete_.csv', sep=', ', encoding='utf-8')
    overall[['bayes'] = np.where(overall['ball'] == overall['guess'], 1.0, 0.0)
    overall__ .rename(columns=dict(zip(temp_2, temp_)), inplace=True) # RENAMING TO AVOID AMBU
    overall__ = overall_[overall['gender_x'] != -1] # NON AVAILABLE OPTION
    overall__ = overall__ .dropna(how='any')

    # FOR TRAINING
    df_exp = overall__.sample(frac=0.50,
    replace=False,
    random_state=outer)
    df_exp = overall__[(df_exp['stage'] == 'treat_stage'])

    # FOR FM DECISIONS
    fm_pool = overall__ .loc[~(overall__.index.isin(df_exp.index))]
    fm_pool = fm_pool[(fm_pool['stage'] == 'belief_prior')]
    fm_pool = fm_pool[fm_traits]

    ###########
    ##### TRAINING OF PLAYER MODEL ###
    ## BALANCE TRAINING SET WITH RESPECT TO INVESTMENT DECISIONS
    temp_0 = df_exp[df_exp['decision'] == 0].sample(frac=1)
    temp_1 = df_exp[df_exp['decision'] == 1].sample(frac=0.6)
    df_exp = pd.concat([temp_0, temp_1], axis=0).sample(frac=1)
    del_temp_0, temp_1
```

```python
# TRAINING SET DEFINITION
X_train_FM = df_exp[train_features_fm]
y_train_FM = df_exp[label_fm]

## OUTER LOOP ###
final_metrics_cv = []
final_metrics = []
final_games = []
final_train_len = []
shap_values = []

# PARALELLIZATION
p = multiprocessing.Process(target=Simulation, args=(discr_by_FM, discr_by_algo, DISCR_NAI, DISCR_NTD, train_features, label, train_features_fm, label_fm, IN_LOO, outer, X_train_FM, y_train_FM, df_exp, df_q, selection_size,))
processes.append(p)
p.start()

# Limit the number of processes running at the same time to the number of cores
if len(processes) >= multiprocessing.cpu_count():
    for process in processes:
    process.join()
    processes = []  # Reset the process list

# JOIN REMAINING NUMBER OF PROCESSES
for process in processes:
    process.join()
    processes = []  # Reset the process list
p.close()
```

## About the Authors

Kevin Bauer has been an assistant professor of e-business und e-government at the University of Mannheim since January 2023. Kevin Bauer is also part of the TechQuartier as an AI specialist, where he is active as an external consultant on AI related topics. Kevin Bauer worked as a postdoctoral researcher at the SAFE Leibniz Institute where he was part of the “Digitization of the Financial Industry” research group. His primary research interests include human-machine interaction, human-centered machine learning, eXplainable AI, generative AI, and applied machine learning.

Rebecca Heigl has been a doctoral student in the chair of Information Systems and Information Management at Goethe University since April 2022. She also holds a BS in business studies from Goethe University Frankfurt and an MS in management from Johannes Gutenberg University Mainz. Her primary research interests include the economics of IS, human-AI interaction, e-commerce, social media, and generative AI.

Oliver Hinz has been the chair of Information Systems and Information Management at Goethe University Frankfurt since September 2017. He has received the prestigious Schmalenbach Prize for Young Researchers in 2008, the ECIS Ciborra Award, the 2017 Science Prize, and the 2018 Sheth Foundation/Journal of Marketing Award for his long-term impact on research in this area. According to the German business journal WirtschaftsWoche, he currently is a top researcher (ranked 11 out of over 3,000 researchers) in the management discipline in Germany. Since October 2023 he has served as the editor-in-chief of the renowned scientific journal Business & Information Systems Engineering (BISE) which is one of the oldest European journals in the area of applied informatics and information systems (first issued in 1959).

Michael Kosfeld holds the chair of Organization and Management at Goethe University Frankfurt. He graduated in mathematics from the University of Bonn in 1995 and received his PhD in economics at Tilburg University in 1999. Before joining Goethe University Frankfurt, he was employed at the Institute for Empirical Research in Economics at the University of Zurich from 2000 to 2008. His primary area of research is behavioral and organizational economics, with a particular interest in the theoretical and experimental analysis of social interaction, human-bounded rational decision-making, and the psychology of incentives. Michael Kosfeld is the director of the Frankfurt Laboratory for Experimental Economic Research (FLEX) and the Center for Leadership and Behavior in Organizations (CLBO).
