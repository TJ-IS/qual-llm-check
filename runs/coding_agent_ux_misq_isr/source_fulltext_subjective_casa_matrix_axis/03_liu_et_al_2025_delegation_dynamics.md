# FIND THE GOOD. SEEK THE UNITY: A HIDDEN MARKOV MODEL OF HUMAN-AI DELEGATION DYNAMICS<sup>1</sup>

Junming Liu Department of Information Systems, College of Business, City University of Hong Kong Hong Kong SAR, CHINA {junmiliu@cityu.edu.hk}

Wei Thoo Yue Department of Information Systems, College of Business, City University of Hong Kong Hong Kong SAR, CHINA {Wei.T.Yue@cityu.edu.hk}

Alvin Chung Man Leung Department of Information Systems, College of Business, City University of Hong Kong Hong Kong SAR, CHINA {acmleung@cityu.edu.hk}

Xin Zhang School of Management, University of Science and Technology of China Hefei, China {zx01@ustc.edu.cn}

As AI becomes integral to enterprise decision-making, this study explores the collaborative dynamics between managers and AI systems, focusing on human willingness to delegate tasks to AI. Grounded in the “agentic” systems delegation framework and instance-based learning theory, we employed a hidden Markov model in a longitudinal study of the dynamic delegation decision-making process involving 875 store managers. We found that there is a potential polarization in managers’ delegation willingness, with managers who recognize the capability of AI exhibiting high delegation willingness and fostering increased collaboration with AI over time—in contrast to their counterparts who are inclined to reduce AI’s involvement. During human-AI interactions, managers’ continuous performance appraisal of AI shapes their dynamic delegation willingness, which in turn affects their assessment of AI capability. This process forms a delegation feedback loop that drives the dynamics of delegation behaviors. Our study indicates that managers with a high willingness to delegate tend to outperform their counterparts and offers valuable insights for human-AI collaborative intelligence in organizational settings.

Keywords: Artificial intelligence, IS delegation, hidden Markov model, performance appraisal, collaborative intelligence

## Introduction

Artificial intelligence (AI) is reshaping traditional business process management through its ability to leverage massive datasets and adapt to complex execution environments that enable automated and augmented decision-making (Brynjolfsson & McAfee, 2017; Wilson & Daugherty, 2018;

Davenport & Rajeev, 2018; Manyika et al., 2017). While AI shines in handling complex analytical decisions autonomously and even surpasses human experts in specific areas (Agrawal et al., 2019; Fu et al., 2021), humans retain an edge in navigating ambiguity and incorporating contextual nuances due to their reasoning superiority (Fu et al., 2021). Given that effective collaboration between human decision makers and AI systems is crucial for organizations, it is important to delve deeper into the nuances of human-AI interaction that can foster such collaborative intelligence.

Recent literature has recognized the dynamic nature of humans’ interaction with AI artifacts, especially in the process of humans delegating tasks to AI (Grisold & Schneider, 2023). The existing information systems (IS) literature, however, has primarily taken a static perspective on IS adoption and use by assuming predefined rules or workflow (Davis, 1989; Joshi, 1991; Kim & Malhotra, 2005; Lapointe & Rivard, 2005; Markus, 1983). The static approach may lead to inaccurate assessments of AI capabilities and miss the unique dynamics of human-AI collaboration, where humans and AI constantly gather data and knowledge and adapt their behaviors accordingly throughout their interactions. For example, global retail giant Walmart has implemented an AI-driven inventory management system to enhance operational efficiency, emphasizing the crucial role of continuous employee feedback in refining and training these AI systems and underscoring the importance of recognizing the dynamic nature of human-AI interaction as the operating environment evolves over time (Musani, 2023).

In response to this research, Baird and Maruping (2021) presented a theoretical framework for IS delegation that explores interactions between humans and agentic systems that can engage in complex activities with limited direct supervision. The framework echoes the dynamic nature of the delegation relationship between human and agentic IS artifacts, highlighting the evolving notions of human delegation decisions and key mechanisms underlying the process. Throughout delegation feedback loops, perceived AI capability shapes human willingness to delegate and influences the corresponding delegation decisions.

Beyond the agentic delegation framework (hereafter ADF) proposed by Baird and Maruping (2021) that explores the dynamics of human-AI interaction in delegating tasks, other research has delved into the underlying cognitive processes of individuals engaging in repeated decision-making. Notably, Gonzalez et al.’s (2003) instance-based learning theory (IBLT) offers a fundamental perspective on how humans make decisions in dynamic environments by relying on past experiences. This involves retrieving relevant instances of similar experiences that can inform current choices. While not directly focused on human-AI collaboration or AI delegation, the theory’s emphasis on learning from previous experience resonates with the notion of evolving human-AI relationships in

ADF. In recent years, IBLT has shaped the development of AI and machine learning algorithms, specifically in crafting models that emulate human decision-making (Gupta et al., 2021; Zhao et al., 2023). ADF and IBLT both underscore the dynamic nature of decision-making, where individuals adapt choices based on accumulated experiences and knowledge.

This study employed a hidden Markov model (HMM) to analyze the dynamic nature of store managers’ decisions on delegating their daily operational tasks to a newly implemented AI system. While ADF and IBLT provide a sound theoretical lens on this process, HMM offers a distinct approach to modeling and understanding the dynamics of human-AI interactions. Following the growing literature on utilizing HMM to model various forms of user behavior dynamics,<sup>2</sup> we employed HMM based on the premise that the delegation decisions and their outcomes would be observable while the evolving process related to managers’ willingness to delegate would remain unobservable. Hence, managers’ delegation decisions would be driven by the unobservable latent process. In essence, HMM provides an approach to leverage human-AI interaction data to identify the unobservable delegation willingness from a sequence of observable delegation decisions.

We collected real-world field data of 875 store managers decisions on AI delegation and delegation outcomes for storekeeping units (SKUs) ordered from the factory over time. This AI system, powered by the sequence-to-sequence deep learning algorithm (Sutskever et al., 2014), is embedded into the enterprise resource planning (ERP) system to execute replenishment decisions without the involvement of managers. A store manager can monitor the replenishment decisions made by AI and opt to override any of them when appropriate; i.e., the manager can override 0% to 100% of these decisions made by the AI system. This human-AI collaboration scenario, often referred to as “human-in-the-loop automation,” allows humans to interact with AI for better sales performance compared to end-to-end automation without human involvement (Nunes et al., 2015; Lebovitz et al., 2022). By studying how managers collaborate with the AI system over time, we built upon ADF and IBLT to offer a more nuanced understanding of AI delegation dynamics.

Study results confirm that managers’ evaluations of AI performance based on their assessment of delegation outcomes shape their perceptions of AI’s capability and influence their willingness to delegate. We also found a potential polarization of delegation willingness developed throughout the adaptive process of continuous performance assessment and delegation.

That is, managers who recognize the capability and contribution of AI delegate more tasks to AI over time—in contrast to their counterparts who are less willing to involve AI in the decisionmaking process. Since the involvement of AI in decisionmaking differs among high- and low-willingness managers, delegation decisions will influence managers’ assessment of AI’s capability and contributions.

Our findings also resonate with aspects of human delegation considered in leader-member exchange (LMX) theory (Graen & Uhl-Bien, 1995; Schriesheim et al., 1998), which explores how trust and perceived performance shape human-human collaboration. LMX theory posits that managers treat team members differently in forming “in-group” and “out-group” relationships, a dynamic that may also manifest in interactions with AI, thus impacting their willingness to delegate. Notably, regarding the performance outcome as a result of AI delegation, high-willingness managers are seen to have a better sense of AI’s incapability, as reflected by their tendency not to delegate to AI while achieving better sales performance under specific conditions or circumstances.

## Research Background

## Human-AI Delegation Dynamics

The recent emerging phenomenon of humans delegating tasks to agentic IS has received increasing attention. Baird and Maruping (2021) proposed the ADF, which focuses on the delegation relationships between humans and a new generation of agentic IS artifacts that can assume responsibility for tasks originally assigned to human agents. ADF suggests that the decision to delegate tasks to agentic IS artifacts is primarily motivated by humans’ pursuit of goal attainment and task completion. In related research, Fügener et al. (2021) conducted experimental studies of human-AI collaboration and found that poor delegation decisions were made by humans who could not assess their own capabilities compared with AI. Dennis et al. (2023) considered AI agents to be new team members and examined humans’ willingness to collaborate with AI members.

Different from existing IS studies that treat delegation decisions in more isolated settings, ADF suggests that willingness to delegate follows a continuous and dynamic appraisal process mandated by repeated evaluations in the delegation feedback loops. Mirroring the delegation feedback loops in ADF, IBLT underscores the dynamic nature of how humans make decisions as a cognitive process based on their past experiences (Gonzalez et al., 2003). While ADF focuses on the influence of managers perceived AI capability based on delegation outcomes in a feedback loop, the IBLT suggests that decision makers adapt their judgment strategies from interaction experience to refine the existing knowledge base by incorporating feedback on action outcomes (Gupta et al., 2021; Zhao et al., 2023). Integrating IBLT into ADF thus provides valuable insights into how humans refine their decision-making processes over time through human-AI interactions.

Drawing on the centerpiece of ADF and IBLT, we propose a research framework to explore the dynamics of delegation decisions in performance feedback loops. In this process, managers shape their willingness to delegate based on their experience collaborating with the AI system. Hence, managers cognitive evaluations of AI capability will continuously evolve based on partially observed delegation outcomes, impacting future delegation decisions. While the delegation decision is observable, the willingness to delegate, based on concepts such as attitude towards systems use (Venkatesh et al., 2003) and perceived usefulness (Davis, 1989), remains unobservable. Figure 1 presents our conceptual framework for this delegation dynamics in the theoretical context of unobservable and observable components. Here, informed by research on humanhuman collaboration, we conceptualize a “team” in the context of human-AI collaboration as a collective entity comprising both human members and AI systems working towards common goals (Graen & Uhl-Bien, 1995; Schriesheim et al., 1998).

## Willingness-to-Delegate in Decision Automation

In our research context, the company conducted weekly assessment meetings, in which managers received reports on three key performance indicators (KPIs): (1) Team<sup>3</sup> vs. Human, (2) Team vs. AI, and (3) Team vs. Team. The first appraisal indicator depicts how human-AI collaboration is considered superior to humans working independently without AI, where we expect humans to be more willing to delegate if the human-AI team outperforms humans alone. The second appraisal indicator shows how well AI can accomplish its work without human supervision, wherein humans would be less likely to delegate decision-making tasks to AI if it leads to worse performance. Finally, the third indicator provides insight into how well a team performs compared to other teams.

![](/api/attachments/PP4YH43X/fulltext/images/af93d523d976dda33c00e211c699f42bb00a0aff7dba7242a94b55592f8fa092.jpg)  
Figure 1. Conceptual Framework of the Delegation Dynamics

The unique field setting and context allowed us to examine managers’ attitudes toward collaborating with AI. As all managers have access to AI in this appraisal, differences in team performance and delegation decisions allowed us to examine whether managers have different delegation willingness when teaming with AI. We applied the conceptual framework of delegation dynamics presented in Figure 1 to our research context using a hidden Markov model, which offers a distinct approach to modeling and understanding the dynamics of managers’ delegation willingness and decision-making.

## Hidden Markov Model of AI Delegation Dynamics

## Research Context

We studied AI delegation dynamics using a retail company sample that employs an AI system to conduct daily replenishment decisions for perishable bakery and dairy products. The company supports a complete supply chain from factory production to store retailing for more than 1,000 retail stores. Due to high demand volatility and the short shelf-life of perishable goods, this company hires and trains store managers to make daily replenishment decisions. During our study period from January 2017 to June 2018, 875 stores initially implemented the AI system. The AIpowered system integrates external (e.g., weather conditions and holidays) and internal supply chain data (e.g., sales and inventory) using a deep learning and inventory model to automate replenishment decisions.

Before implementing the AI system, each store manager had to manually conduct approximately 70 replenishment tasks every day. After the AI system was deployed and integrated into the enterprise resource planning (ERP) system, replenishment operations could be conducted automatically without managers’ involvement. Store managers were allowed to interrupt the automation processes and override the AI’s decisions. Those store managers who did not want to delegate a replenishment task to AI needed to submit a brief comment explaining their reason for not delegating. Although the store managers did not understand the inner operations of the AI algorithms, they could observe and discuss store sales performance in their weekly manager meetings. These meetings provided a platform for managers within the same region to share and discuss the performances within their specific regions. The three KPIs (Team vs. Human, Team vs. AI, and Team vs. Team,) were calculated by the company and presented to store managers in the weekly meeting to assess the performance of the AI system and the human-AI team.

## Model Setting

We used HMM to study the delegation dynamics presented in Figure 1. In our context, this model consists of three major elements: (1) a finite set of latent states, defined as the level of managers’ willingness to delegate; (2) a transition matrix, defined as the probabilities of state transitions; and (3) a sequence of observed delegation decisions. The overall mechanism can be understood as follows. In period ??, a store manager ?? resides in a particular latent willingness state ?? .

By the end of period ??, managers observe the three KPIs of this period, which may drive them to transit to any of the ?? discrete latent states ranked from lowest to highest in the order of willingness to delegate in period ?? + 1 . The transition follows a Markov process and is influenced by the observed KPIs in period ?? . Hence, different transition probabilities can be estimated to reveal the impact of the KPIs on the willingness state transition process. Managers’ willingness to delegate, characterized by the latent state, can be tracked by the probability distribution of delegation decisions in which managers in a higher state are likely to delegate more tasks to AI.

To explore how performance appraisals influence the evolving delegation decisions, we formulated the three elements formally, denoted in HMM by $\lambda = ( \pi _ { i } , Q _ { i } , A _ { i } )$ . The three elements for manager ?? and the corresponding assumptions are as follows:

1. The initial distribution of willingness state $\pi _ { i } \in \mathcal { R } ^ { 1 \times n }$ is an ??-dimensional vector with the $j ^ { \mathrm { t h } }$ element $\pi _ { i } ( j )$ representing the probability that the manager’s initial state of willingness to delegate is ?? in period $t = 1$ before the delegation output is observed: $\pi _ { i } ( j ) =$ $P ( S _ { 1 } = j )$ . We assume the initial state $\pi _ { i }$ follows a uniform distribution among all latent states.<sup>4</sup>

2. The state transition probability matrix $Q _ { t } \in \mathcal { R } ^ { n \times n }$ characterizes the probabilities of transitions across different latent willingness states from time ?? to ?? + 1, with the element $q _ { j k t } = P ( S _ { t + 1 } = k | S _ { t } = j )$ representing the probability of transition to willingness state ?? in period ?? + 1 under the condition that the manager is in state ?? in period ??. We assume that the next state depends only upon the current state, indicating that the historical appraisals gathered in previous states are all present in the most recent state.

3. The emission probability $A _ { t } \in \mathcal { R } ^ { n \times n }$ is a diagonal probability matrix that characterizes the probability of observing the manager’s delegation decisions in period ?? , with the $j ^ { \mathrm { t h } }$ diagonal element $a ( O _ { t } | S _ { t } = j )$ representing the probability of observed delegation decision $O _ { t }$ under the condition that the manager is in willingness state ?? in period ?? . We assume the delegation decisions are independent and conditional based on the current latent state.

## Latent Transition of Delegation Willingness

The transition process across different willingness states of manager ?? is driven by the performance indicators $\pmb { R } _ { i t }$ obtained by the end of period ??. Accordingly, the manager’s latent propensity $Z _ { i j t }$ is:

$$
Z _ {i j t} = \beta_ {i j} \pmb {R} _ {i t} + u _ {i j k} + \xi_ {i},\tag{1}
$$

where the performance indicators in vector $\pmb { R } _ { i t }$ are in various forms, including sales improvement when comparing performances of the human-AI team to human without AI involvement (Team vs. Human) $T H _ { t } ,$ the performance of AI without human involvement (Team vs. AI) $T A _ { t }$ , and the performance of other human-AI teams (Team vs. Team) $T T _ { t }$ Since managers in different states may have different views on delegation outcomes, we define $\beta _ { i j }$ as a vector of statedependent coefficients representing the marginal effect of the factors conditioned on the current willingness state ?? . The intercept $u _ { i j k }$ represents the inherent transition threshold from state ?? to state ?? . The manager-specific factor $\xi _ { i }$ indicates a random effect term to control for manager heterogeneity in state transition. The transition probability $q _ { j k t }$ is modeled as an ordered logit function of the latent propensity. For notational simplicity, we dropped the manager index ??.

$$
q _ {j k t} = \left\{ \begin{array}{l l} 1 - \frac {\exp (\beta_ {j} \boldsymbol {R} _ {t} + u _ {j k} + \xi)}{1 + \exp (\beta_ {j} \boldsymbol {R} _ {t} + u _ {j k} + \xi)} & k > j \\ \frac {\exp (\beta_ {j} \boldsymbol {R} _ {t} + u _ {j k} + \xi)}{1 + \exp (\beta_ {j} \boldsymbol {R} _ {t} + u _ {j k} + \xi)} & k <   j \\ 1 - \sum_ {k \neq j} q _ {j k t} & k = j \end{array} \right.\tag{2}
$$

## State-Dependent Delegation Decision

As store managers in different latent states may have different delegation decisions, we used the percentage of tasks $O _ { i t }$ delegated to AI as the delegation decision made by manager ?? in period ??, based on which state of willingness to delegate can be identified. Let $\pmb { S } _ { i } = S _ { i 1 } , S _ { i 2 } , \ldots , S _ { i T }$ represent the sequence of willingness states and $\pmb { O } _ { i } = O _ { i 1 } , O _ { i 2 } , \dots , O _ { i T }$ represent the sequence of observed delegation decisions, where the probability that we observe $\pmb { O } _ { i }$ from manager ?? conditioned on the latent willingness state sequence $\pmb { S } _ { i }$ is defined as:

$$
P (\pmb {O} _ {i} | \pmb {S} _ {i}) = \prod_ {t = 1} ^ {T} P (O _ {i t} | \lambda , S _ {i t}),\tag{3}
$$

where $P ( O _ { i t } | \lambda , S _ { i t } )$ is the probability of observing manager ??’s delegation decision $O _ { i t }$ when the manager is in state $S _ { i t }$ in period ?? . We used the Gaussian function to model the probability of an observed outcome (Rabiner, 1989). Specifically, for a single period of observation, the probability of the delegation decision under the condition that the manager is in willingness state ?? is defined as:

$$
\begin{array}{r} P (O _ {i t} | \lambda , S _ {i t} = j) = \exp (- (O _ {i t} - (\rho_ {i j} \pmb {W} _ {t} + \eta_ {i j} + \delta_ {i})) ^ {2} \end{array}\tag{4}
$$

where ${ \pmb W } _ { t }$ is a vector of random variables, including implementation time, implementation time squared, the number of days with bad weather, and the number of holidays. We estimated both $\rho _ { i j }$ and $\eta _ { i j }$ as state-dependent parameters. Parameters $\rho _ { i j }$ represent the influence of control variables in vector ${ \pmb W } _ { t }$ . The parameter $\eta _ { i j }$ is the state-dependent emission intercept indicating the percentage of tasks to be delegated by manager ?? in state ?? without the influence of environmental conditions and implementation time. The manager-specific factor $\delta _ { i }$ indicates a random effect term to control for manager heterogeneity in delegation decisions.

<table><tr><td colspan="5">Table 1. Summary Statistics</td></tr><tr><td>Variables</td><td>Descriptions</td><td>Mean (Std)</td><td>Skewness</td><td>Kurtosis</td></tr><tr><td colspan="5">Dependent variables ( $O_{it}$ )</td></tr><tr><td> $Delegation_t$ </td><td>Percentage of tasks delegated to AI in period  $t$ </td><td>76.21% (15.89%)</td><td>-0.3812</td><td>-0.1383</td></tr><tr><td colspan="5">Control variable ( $W_{it}$ )</td></tr><tr><td> $Implementation\ Age_t$ </td><td>Number of weeks since the AI system was implemented</td><td>48 (13)</td><td>0.0</td><td>-1.2</td></tr><tr><td> $Bad\ Weather_t$ </td><td>Number of days with bad weather (rainy, snowy, etc.) in period  $t$ </td><td>3.73 (1.89)</td><td>-0.3312</td><td>-0.8351</td></tr><tr><td> $Holiday_t$ </td><td>Number of holidays in period  $t$ </td><td>0.16 (0.52)</td><td>3.7425</td><td>15.6567</td></tr><tr><td colspan="5">Performance indicators ( $R_{it}$ )</td></tr><tr><td>Team vs. Human ( $TH_{it}$ )</td><td>The manager&#x27;s sales improvement in period  $t$  after AI implementation</td><td>5.97% (31.50%)</td><td>0.2420</td><td>1.8879</td></tr><tr><td>Team vs. AI ( $TA_{it}$ )</td><td>Sales performance comparison between “order by pure system” and “order after the manager&#x27;s modification” in period  $t$ </td><td>9.27% (10.67%)</td><td>0.5480</td><td>2.1033</td></tr><tr><td>Team vs. Team ( $TT_{it}$ )</td><td>Difference of sales improvement between the retail store and the regional average after AI implementation in period  $t$ </td><td>2.58% (26.92%)</td><td>0.1781</td><td>1.2884</td></tr></table>

## Maximum Likelihood Estimation

Given the model setting, we modeled the probability of the sequence of delegation decisions $\pmb { O } _ { i }$ as the probability of delegation decisions conditioned on the states of willingness to delegate. We identified the optimal parameter set $\lambda ^ { * }$ including parameters $( u , \beta , \xi )$ in (2) and $\eta , \rho , \delta$ in (4) in the HMM by maximizing the likelihood of the probability (or equivalently minimizing the negative log-likelihood) that the sequence of delegation decisions $\pmb { O } _ { i }$ may happen:

$$
P (\pmb {O} _ {i} | \lambda) = \sum_ {\forall S _ {i}} \prod_ {t = 1} ^ {T} P (O _ {i t} | \lambda , S _ {i t}) P (S _ {i t})\tag{5}
$$

$$
\lambda^ {*} = \underset {\lambda} {\arg \min} - l o g P (\pmb {0} _ {i} | \lambda)\tag{6}
$$

## Data and Variable Description

We collected daily delegation decisions and outcomes of 875 store managers who implemented the AI system for more than 30 weeks. Table 1 provides the variable definitions and summary statistics at the store-week level.

<table><tr><td colspan="10">Table 2. Model Selection</td></tr><tr><td rowspan="2">Model</td><td rowspan="2"># States</td><td colspan="4">Single-period model</td><td colspan="4">Three-period model</td></tr><tr><td>Log-L</td><td># Variables</td><td>BIC</td><td>AIC</td><td>Log-L</td><td># Variables</td><td>BIC</td><td>AIC</td></tr><tr><td rowspan="5">HMM</td><td>One</td><td>-369.5</td><td>10</td><td>-403</td><td>-390</td><td>-341.1</td><td>13</td><td>-385</td><td>-367</td></tr><tr><td>Two</td><td>-177.3</td><td>20</td><td>-245</td><td>-217</td><td>-179.3</td><td>23</td><td>-257</td><td>-225</td></tr><tr><td>Three</td><td>-128.5</td><td>32</td><td>-237</td><td>-193</td><td>-126.5</td><td>35</td><td>-245</td><td>-197</td></tr><tr><td>Four</td><td>-256.1</td><td>46</td><td>-412</td><td>-348</td><td>-243.2</td><td>49</td><td>-409</td><td>-341</td></tr><tr><td>Five</td><td>-289.9</td><td>62</td><td>-500</td><td>-414</td><td>-266.1</td><td>65</td><td>-486</td><td>-396</td></tr></table>

Manager ??’s delegation decisions $O _ { i t }$ in period ?? is defined as the percentage of tasks delegated to AI. The system implementation age and age squared are control variables that characterize the implementation stage’s short-term and longterm effects. The number of days with bad weather conditions and holidays were used to control for the complexity of the replenishment tasks, which the AI system may lack the intuitive ability to apprehend. The three KPIs were used to model the state transition process, with details of variable measurements provided in the Appendix. On average, a store manager made about 502 product replenishment requests per week, 119 of which were retained by the manager, with the rest being delegated to AI.

## Estimation and Results

## Model Selection

We adopted the Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm to maximize the likelihood function for parameter estimation. We compared the proposed HMM with a threeperiod model<sup>5</sup> that recalled the past three periods of performance appraisals to characterize state transitions. To ensure the convergence of our results, we optimized HMM with different initial parameters. Following prior literature (Chen et al., 2018; Singh et al., 2011), we adopted the log-likelihood, Bayesian information criterion (BIC), and Akaike information criterion (AIC) as model evaluation metrics to determine the best model structure.

The performance comparison is reported in Table 2. The results show that the one-state HMM performed poorly, confirming that different willingness states existed and the delegation decisions were state-dependent. Based on the estimation results, we used the single-period three-state HMM, which performed best as our main model. Table 3 presents the estimation results for the three-state HMM. Next, we report the main results that reveal the dynamics of AI delegation.

## State-Dependent Delegation Decisions

The longitudinal modeling of delegation decisions allowed us to gain some interesting insights into how managers with different willingness states delegate replenishment tasks to AI. As shown in Table 3, the estimates of the emission intercept (?? in Equation (4) indicate the state-dependent delegation decisions in the initial stage at time ?? = 0, when the AI system was introduced to cooperate with the store managers’ tasks of replenishment decisions. The results show that store managers in different latent states were involved with different delegation decisions, with the estimates of coefficients for the latent State 1, State 2, and State 3 being 0.0895 $( p < 0 . 0 5 )$ 0.1831 $( p < 0 . 0 1 )$ , and 0.2949 $( p < 0 . 0 1 )$ , respectively. When comparing the difference between the emission intercepts, the coefficient for State 3 is significantly higher, presenting a difference of $0 . 1 1 1 8 \left( p < 0 . 0 5 \right)$ compared with that for State 2 and 0.2054 $( p < 0 . 0 1 )$ compared with that for State 1. The differences in the state-dependent emission intercepts indicate that the percentage of tasks delegated to AI increases with a higher level of the latent state, and the willingness to delegate varies from low to high with the level of the latent state. Specifically, considering the manager-specific heterogeneity in the emission function, store managers in State 1 had the lowest willingness to delegate. Managers in State 3 had the highest level of willingness, delegating 93.96% of tasks on average. State 2 in the middle is denoted as the medium state. Hence, we denote the three latent states (State 1, State 2, and State 3) as the low-willingness state (L), medium state (M), and high-willingness state (H), respectively. Despite the presence of the AI system, managers in the low-willingness state tended to act independently of AI for most tasks, whereas those in the high-willingness state tended to rely on the AI system.

<table><tr><td colspan="4">Table 3. Estimation Results of Three-State HMM</td></tr><tr><td>Variable</td><td>State 1 (L)</td><td>State 2 (M)</td><td>State 3 (H)</td></tr><tr><td colspan="4">Emission factors ( $\rho, \eta$ )</td></tr><tr><td>Emission intercept</td><td>0.0895**</td><td>0.1831***</td><td>0.2949***</td></tr><tr><td>Implementation age</td><td>-0.3028***</td><td>-0.1730***</td><td>-0.1043**</td></tr><tr><td>Implementation age squared</td><td>-0.0906**</td><td>0.024</td><td>0.1231**</td></tr><tr><td>Bad weather</td><td>-0.0013</td><td>-0.0241**</td><td>-0.0560**</td></tr><tr><td>Holiday</td><td>-0.0055</td><td>-0.0531**</td><td>-0.0958**</td></tr><tr><td>Manager-specific heterogeneity</td><td> $\xi=0.6447^{***}$ </td><td></td><td></td></tr><tr><td>Transition Threshold ( $\mu$ )</td><td></td><td></td><td></td></tr><tr><td>To State 1 (L)</td><td></td><td>-0.2407***</td><td>-1.9616***</td></tr><tr><td>To State 2 (M)</td><td>1.2601***</td><td></td><td>-1.3114***</td></tr><tr><td>To State 3 (H)</td><td>1.7822***</td><td>0.1569***</td><td></td></tr><tr><td>Manager-specific heterogeneity</td><td> $\delta=0.2297^{***}$ </td><td></td><td></td></tr><tr><td>Transition factors( $\beta$ )</td><td></td><td></td><td></td></tr><tr><td>Team vs. Human</td><td>-0.2631**</td><td>-0.2393***</td><td>-0.4953***</td></tr><tr><td>Team vs. AI</td><td>0.5691***</td><td>0.2079***</td><td>1.1328***</td></tr><tr><td>Team vs. Team</td><td>0.2567***</td><td>0.1567***</td><td>-0.4460***</td></tr></table>

Note: \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01 (two-tailed t-test for all variables).

![](/api/attachments/PP4YH43X/fulltext/images/3b2716ba9b79bb518061e35ca24d5d23e185a2998e4e635207edf81ac817ea39.jpg)

Figure 2. State-Dependent Time Trend of Delegation Decisions

Figure 2 depicts the time trend of delegation decisions made by managers in different willingness states, characterized by the emission function. The coefficients for implementation age and implementation age squared for managers in the low-willingness state are $- 0 . 3 0 2 8 \left( p < 0 . 0 1 \right)$ and -0.0906 $( p < 0 . 0 5 )$ , respectively. This indicates that managers in the low-willingness state delegated fewer tasks to AI in both the short term and the long term. We observed a similar trend for managers in the intermediate state initially but with a smaller downtrend in the short term. For managers in the high willingness state, we also found that they delegated fewer tasks to AI in the short term. Still, the coefficient for implementation age squared is 0.1231 $( p < 0 . 0 5 )$ , indicating that in the long term, the percentage of tasks delegated to AI increased with time.

Moreover, the coefficients for “bad weather” and “holiday” for managers in the high-willingness state are -0.0560 $( p < 0 . 0 5 )$ and -0.0958 $( p < 0 . 0 5 )$ , respectively. The delegation decisions of managers in the low-willingness states were not statistically different under different environmental conditions. This indicates that as the number of bad weather days or holidays increased, high-willingness managers delegated fewer tasks to AI. In contrast, we did not find that these environmental conditions significantly affected managers’ delegation decisions in the low-willingness state. As these rare environmental conditions introduced task complexities for the AI system due to its limited training records, we speculate that high-willingness managers were more careful in assessing AI’s capability in conducting complex tasks. To verify this conjecture, we conducted additional analysis of the assessment reports generated by managers in different willingness states. The results show that rare environmental conditions are the main reason that high-willingness managers did not delegate tasks to AI (discussed in the State-Dependent Delegation Performance section below). Our findings lend support to the notion that managers’ delegation decisions depend on their categorization of delegation willingness. These categorizations resemble how human managers perceive subordinates to be more or less trustworthy with an “in-group” and “out-group” categorization, as posited by LMX theory.

## State-Dependent Transition in Delegation Willingness

We modeled the state transition process characterized by the transition matrix ?? in Equation (2) by estimating the transition threshold $\mu ,$ the coefficients of transition factors ?? conditioned on managers’ willingness state, and manager-specific heterogeneity ?? . As shown in Table 3, the estimation results reveal the impact of the intrinsic transition propensity and performance appraisals on the transitions of managers’ willingness to delegate.

## Intrinsic Transition Propensity

The study results show that transition thresholds corresponding to managers’ intrinsic propensity to transit across different willingness states are significant. The threshold for moving from the low-willingness state to the intermediate state is 1.2601 $( p < 0 . 0 1 )$ ) . Moving directly from the low-willingness state to the high-willingness state is possible, but it has a higher transition threshold of 1.7822 $( p < 0 . 0 1 )$ ) , 0.5221 $( p < 0 . 0 5 )$ higher than that of moving from the low-willingness state to the high-willingness state. The threshold for transition from the high-willingness state to the intermediate state is -1.3114 $( p < 0 . 0 1 )$ , indicating that managers inherently prefer to stay in their current willingness state.

In any case, transitioning from the low-willingness state to the high-willingness state is the most difficult process. We computed the intrinsic transition probability by feeding the estimated transition thresholds $\mu$ and manager-specific heterogeneity ?? into the transition probability functions in Equation (2) and removing the coefficients of transition factors $( \beta = 0 )$ . Correspondingly, the transition threshold of 1.2601 for a transition from the low-willingness state to the intermediate state is equivalent to an intrinsic transition probability of 22.10%. This shows that without the impact of the perceived performance appraisals $( R _ { i t } )$ , the probability that store managers in the low-willingness state will transit to the intermediate state is only about 22.10%. Table 4 presents the probability of intrinsic propensity to transition across different willingness states. We found that managers in the lowwillingness state were extremely sticky in terms of remaining in their current state, with an intrinsic propensity of 63.51%. Once store managers reached the high-willingness state, they generally preferred to maintain their state, with a probability of 66.45%. This result adds to ADF by revealing the impact of managers’ initial categorization of delegation willingness and status quo. Despite the influence of performance appraisal, which affected managers’ future delegation decisions in the feedback loop, managers were likely to inherently polarize into and remain at either the low- or high-willingness states.

## Impact of Performance Appraisals

The results also show that all the estimated coefficients of the state-dependent transition factors are significant, indicating that different performance indicators influence the dynamic transitions of managers’ delegation willingness.

Team vs. Human: Sales improvement from team cooperation was benchmarked against the sales performance of store managers working alone, before the AI system was deployed. As seen in Table 3, the coefficients of Team vs. Human performance comparisons are -0.2631 (p < 0.05) , -0.2393 (p < 0.01) , and -0.4953 $( p < 0 . 0 1 )$ for managers in the low-, intermediate-, and high-willingness state, respectively. This indicates that superior performance as a team can motivate managers to move to a higher willingness state or reinforce their AI delegation willingness. We further conducted a sensitivity analysis<sup>6</sup> on how the Team vs. Human KPI signals affected delegation willingness. With this KPI increasing from -30% to +30%, we calculated the transition probability by feeding the estimated coefficients for transition factors into the transition probability functions in Equation (2) and removing the coefficients of other KPIs. Figure 3 depicts the transition probability $P ( S _ { t + 1 } =$ $k | S _ { t } = j )$ , which is the probability of a single manager transiting to willingness state ?? in the next period ?? + 1 given the current willingness state ?? in period ??, in terms of Team vs. Human for managers in the low- to high-willingness states. As the indicator increased from -30% to 30%, the probability that the low willingness-to-delegate managers would stay in the current low state decreased from 71.90% to 67.59% (Figure 3a). In contrast, the high willingness-to-delegate managers who would stay in the current high state increased from 55.62% to 63.40% (Figure 3c). While the coefficients of the transition factors for the medium-willingness state were significant, their impact on the transition process can be ignored (Figure 3b). The high intrinsic propensity mainly drove the transition probability conditional on the medium state. Therefore, in the following, we focus on the impact of performance appraisals for the lowand high-willingness states.

willingness state of the highest probability, we used it to evaluate the impact of KPI on the transitions of delegation willingness.

<table><tr><td colspan="4">Table 4. Probability of Intrinsic Propensity to Transition</td></tr><tr><td> $t \rightarrow t + 1$ </td><td>Low</td><td>Medium</td><td>High</td></tr><tr><td>Low</td><td>63.50%</td><td>22.10%</td><td>14.40%</td></tr><tr><td>Medium</td><td>44.01%</td><td>9.90%</td><td>46.09%</td></tr><tr><td>Large</td><td>12.33%</td><td>21.22%</td><td>66.45%</td></tr></table>

![](/api/attachments/PP4YH43X/fulltext/images/37e8a77083993de9fd6781cf6dccf6c04e2e7abe63db9b14b00664e5a869bbb1.jpg)  
(a) Managers of low willingness

![](/api/attachments/PP4YH43X/fulltext/images/212f1001ccef3e27862bf4fe023118c5509210181e2b7bbf1b65988a1fd94baa.jpg)  
(b) Managers of medium willingness

![](/api/attachments/PP4YH43X/fulltext/images/413dfb06730781ec274a16eb81f171fd048417a49e6cfde53d13e003f16779e6.jpg)  
(c) Managers of high willingness  
Figure 3. State-Dependent Sensitivity Analysis of Team vs. Human

Team vs. AI: We next consider the impact of a performance comparison between the team and a pure AI system without human intervention. The corresponding coefficients are 0.5691 $( p < 0 . 0 1 )$ ), 0.2079 $( p < 0 . 0 1 )$ , and 1.1328 $( p < 0 . 0 1 )$ for the low-, intermediate-, and high-willingness states, respectively. This indicates that when the team performs better than the AI system alone, managers’ willingness to delegate may transit to or stay in a low-willingness state. In contrast, when managers realize AI can outperform on the tasks that were not delegated, managers will tend to transit to or stay in a highwillingness state and delegate more tasks to AI.

We conducted a similar sensitivity analysis to identify the impact of team sales performance, which becomes better than pure AI sales performance on the state transition probability. With the Team vs. AI performance difference increasing from - 30% to 30%, the probability that the low willingness-todelegate managers would stay in the current low state increased from 68.08% to 71.46% (Figure 4a). In contrast, the likelihood that managers in the high willingness state would stay in the current state decreased from 65.34% to 53.29% (Figure 4c). Our results show that when the team outperformed AI, their willingness to fully depend on the AI system was diminished. Managers in the high-willingness state were highly sensitive to the Team vs. AI performance comparison (Figure 4c). The impact of Team vs. AI and Team vs. Human lends support to the proposed mechanisms stipulated in ADF and IBLT that the accumulated performance evaluation from human-AI interaction experiences can shape managers’ perception of AI capability, which will adapt their future delegation decisions.

Team vs. Team: In our research context of human-AI collaboration, the company introduced the KPI of team performance comparison, which used the city-level average team performance as the baseline. Different managers and the AI system formed different teams that were collectively evaluated against other teams. As shown in Table 3, for managers in the low- and intermediate-willingness states, the estimated coefficients for outperforming other teams are 0.2567 $( p < 0 . 0 1 )$ and 0.1567 $( p < 0 . 0 1 )$ , respectively, while the estimated coefficient for managers in the high-willingness state is negative with a value of -0.4460 $( p < 0 . 0 1 )$ ) . This indicates that managers who were already in the lowwillingness state may have reinforced their stance if they achieved superior performance, compared to other colleagues. In contrast, managers in the high-willingness state tended to reinforce their inclination if they could outperform other teams. One plausible explanation for this is grounded in IBLT, which posits that managers draw upon past experiences to inform their decision-making process. In our scenario, managers with high willingness had accumulated a wealth of experience in utilizing AI capabilities through the delegation of tasks to AI during human-AI collaboration. Consequently, improvements in team performance were more likely to be attributed to the AI’s involvement in task execution. Conversely, managers with low willingness typically had limited experience with AI in their daily operational tasks. As a result, these managers were more likely to reinforce their decision to retain most tasks for themselves, as they could achieve better team performance by not delegating, compared to other teams that also implemented AI.

![](/api/attachments/PP4YH43X/fulltext/images/cd8922af83508882a0c1cf6bf03d27175db9f1981dce8d1095ff4d0c47ef5b4b.jpg)  
(a) Managers of low willingness.

![](/api/attachments/PP4YH43X/fulltext/images/6b18d14716262ea08de4123e206713bdd73b10453705461aedc8e28a77aac8f9.jpg)  
(b) Managers of medium willingness

![](/api/attachments/PP4YH43X/fulltext/images/c218c2da726895d3aa628e9d069dcd1ed68330129e3e408cf07b254deb1a73b8.jpg)  
(c) Managers of high willingness

Figure 4. State-Dependent Sensitivity Analysis of Team vs. AI  
![](/api/attachments/PP4YH43X/fulltext/images/61053783296e3c426d7b3c38f69c13ddb56eaa9097172d84aad76ca15ee617ab.jpg)  
(a) Managers of low willingness

![](/api/attachments/PP4YH43X/fulltext/images/48215279d54211ad1dffe09fcc762cb5cb888002cac7b775761aa121313c4e7c.jpg)  
(b) Managers of medium willingness

![](/api/attachments/PP4YH43X/fulltext/images/66b75296f1ba7f52eb00bb48ce2729503fc1b4f68e633c2e67c29436b913c871.jpg)  
(c) Managers of high willingness  
Figure 5. State-Dependent Sensitivity Analysis of Team vs. Team

Figure 5 shows the sensitivity analysis of the Team vs. Team performance indicator. As the performance gap increased from -30% to 30%, the probability that the low willingness-todelegate managers would stay in the current low state increased from 67.69% to 71.83%. The likelihood that the high willingness-to-delegate managers would stay in the current high state increased from 56.61% to 62.53%. The team’s superior performance likely further reinforced the delegation willingness of managers in both the low- and high-willingness states.

## State-Dependent Delegation Performance

We used the estimated coefficients to conduct a posterior analysis of store managers’ willingness to delegate state and delegation performance. Once the parameters ?? for HMM were optimized, we employed the model to predict the state of delegation willingness in period ?? using the transition trajectories and the sequence of observed delegation decisions, and identified the willingness state in period ?? as the state with the maximum probability according to the posterior state probability:

$$
s ^ {*} = \underset {s \in \{L, M, H \}} {\operatorname{argmax}} P (S _ {t} = s, \boldsymbol {O} | \lambda) / P (\boldsymbol {O} | \lambda)\tag{7}
$$

Table 5 shows the result of Welch’s t-test on sales performance differences for managers in different willingness-to-delegate states. The results show that the average sales performance for managers in the highwillingness state was 10.92% and 9.19% higher than that of low- and medium-willingness state managers, respectively. This result implies that the state of being flexible with high willingness, as opposed to being more stagnant with low willingness, is associated with better team performance.

We further analyzed the assessment reports generated by managers in the low- and high-willingness states based on their reasons for not delegating the replenishment decisions to AI. The word cloud for the top 30 assessment reports in both groups is presented in Figure 6, with the size of the sentence representing the log frequency of reasons. We found that managers in the high-willingness state had sound reasons to override the AI decisions, often in response to the weaknesses of the AI systems, including their inability to make adjustments due to holidays, sudden changes in customer flows due to store location, and special store inventory conditions, which were mainly related to rare operational environments that the AI system could not capture due to insufficient training data.

<table><tr><td colspan="4">Table 5. Difference in Sales Performance Conditioned on Manager Willingness State</td></tr><tr><td>Sales difference</td><td>Low</td><td>Medium</td><td>High</td></tr><tr><td>Low</td><td>0</td><td>-1.732%***</td><td>-10.92%***</td></tr><tr><td>Medium</td><td>1.732%***</td><td>0</td><td>-9.19%***</td></tr><tr><td>High</td><td>10.92%***</td><td>9.19%***</td><td>0</td></tr></table>

Note: \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01, (Welch’s t-test for mean difference)

hurry hurry hurry Pay repeatedly good weather recently Not much left in stock Ah little tahs eah ah ah ah ah want performance, add goods Average sale Ha ha ha ha ha Too much to sel1 have safety stockAverage daily sales\*

(a) Reasons from low-willingness managers

Passenger traffic has risen Satisfycustomers needs I want to do performance, add goods Product sales drop Passengerflow hasincreased Students are on vacation Inventoryoverhangaffects sales good weather recently Fewer passengers during the Spring Festival holiday There are too few goods. need to add more good The number of students required for school holidays (b) Reasons from high-willingness managers

Figure 6. Word Cloud Presentation of Assessment Reports from Different Groups of Managers

In contrast, managers in the low-willingness state often failed to evaluate the AI advantage and thus overrode its decisions based on meaningless or facile reasons. For example, these managers submitted the repetition of words of a nonserious nature in the assessment reports to interrupt AI decisions (Figure 6a). The results of these reports support the proposal of ADF that managers embracing the AI system can evaluate AI performance with the consideration of environmental conditions and may have a better sense of AI’s incapability (Figure 6b). It helps explain why high-willingness managers generally maintained their inclination to embrace decisions made by the AI system and remain in the high-willingness state. This finding also adds to the insight that the important role of environmental conditions, as proposed by ADF, also depends on managers’ initial delegation willingness.

## Analysis of Store Ownership Data

We separated the data sample to differentiate store managers in franchise stores from those in direct retail stores. Franchise stores are owned by external investors whereas direct stores are directly managed by the company. This implies that store managers could face different risk exposures depending on the ownership structure. Typically, franchise store managers are also investors who accept a higher stake of risk when managing daily operations.

Among the 875 retail stores in our sample, 471 were franchises, and the rest were direct retail stores. We conducted a Welch’s ??-test on the two samples to examine the difference in delegation dynamics (Table B1). The results show that the franchise and direct retailers did not have significant differences in coefficients for emission and transition factors. The notable exceptions are the emission intercept of franchise managers in the low- and high-willingness states, which were 0.2753 ( < 0.01) lower and 0.1844 ( < 0.05) higher than that of direct retailers, respectively. This suggests that franchise managers had 27.53% fewer and 18.44% more tasks delegated to AI if they were currently in the low- and highwillingness state, respectively. In addition, the significant difference in the transition thresholds indicates that franchise managers were less likely to transit to the high-willingness state. Interestingly, the coefficients for transition factors do not show a significant difference between the two groups of managers except for the Team vs. Team indicator. This implies that compared to direct store managers, franchise managers in the high-willingness state were more sensitive to AI’s involvement and contribution to the team. The results show that franchise managers exhibited similar state-dependent behaviors to direct store managers even though they assumed more risks. But to some extent, they were more inclined to retain their own decision tasks instead of delegating to AI.

## Robustness Test

We conducted additional robustness tests. To ensure that the product category did not bias our results, we estimated the model using the two samples of products in the categories of bakery and dairy, respectively. The estimation result is shown in Appendix Table B2 and Table B3. Compared with our main model results shown in Table 3, these results do not exhibit a qualitatively different pattern.

## Discussion and Conclusion

The advancement of AI systems has created many new business opportunities that require human collaboration with AI. In this study, we set out to examine the dynamics of human willingness to delegate product replenishment decision tasks to an AI system.

Motivated by the theoretical lens of ADF and IBLT, we employed the HMM and found that store managers delegation willingness changes dynamically with continuous performance evaluations in delegation feedback loops. Managers’ delegation willingness can be categorized into low, medium, and high states, associated with different levels of delegation decisions. Such delegation willingness does not converge to a single state. Instead, managers’ delegation willingness tends to polarize into either low- or highwillingness states in combination with their experience collaborating with AI and performance feedback.

We found that some managers are willing to embrace AI, especially after increasing their interactions with AI over time. Yet a high willingness to delegate tasks to AI raises the concern of humans becoming unduly reliant on the AI system. Similar “social loafing” behavior has been observed in the context of team collaboration (Karau & Williams, 1993), where individual members do not pull their own weight compared to those working without AI. This concern also raises the issue of automation bias, where humans rely heavily on automated decision-making systems without critically evaluating them (Goddard et al., 2012). Nevertheless, we did not find this behavior to be common in our setting. Instead, the high-willingness managers in our sample tended to have sound reasons for overriding the AI decisions and reconfigured delegation tasks when they disagreed with AI decisions or when AI demonstrated weak performance. Notably, these managers were more likely to adjust their willingness state and reduce delegation when the AI system underperformed. However, this group clearly demonstrated confidence in AI capabilities and exhibited a willingness to delegate when AI was involved in daily operational tasks with outstanding performance.

In contrast, low-willingness managers showed less of a tendency to change their attitudes even when AI performed well. These managers were also more likely to hesitate when delegating tasks to AI. This finding demonstrates that managers in various states will attribute team performance differently. We found descriptive evidence that, on average, compared to high-willingness managers, low-willingness managers exhibited poorer sales performance. That is, the feedback they provided when overriding the system was often unconstructive, superficial, or even irrational. On the other hand, high-willingness managers often demonstrated sound reasoning in the feedback. Such results imply that lowwillingness managers exhibit a lack of interest or limited understanding of AI, which can undermine human-AI collaboration, even when unintentional.

In summary, our findings suggest that high-willingness managers with a “seeking the good” attitude are more likely to work with the AI system to create responsive AI practices for achieving collaborative intelligence. On the other hand, low-willingness managers typically have fewer interactions with AI. They tend to retain most tasks when their decisions not to delegate lead to good sales performance. These seemingly paradoxical outcomes stem from the nature of partially observed delegation outcomes within team-based assessment. Both scenarios align with IBLT, suggesting that individual instances shape diverse delegation behaviors based on prior experiences. Moreover, these findings of different delegation behaviors demonstrate the finer intricacies within ADF. Additionally, the observed polarization in a manager’s willingness to delegate—whether high or low—resonates well with the “in-group” and “out-group” relationships posited by LMX theory.

This study makes several contributions to the existing literature. First, we operationalized ADF and IBLT with a distinct dynamic model in a longitudinal study to explore the mechanism underlying the dynamics of human-AI interactions over time. While prior IS resistance literature, such as Lapointe and Rivard (2005), has documented similar reluctant behavior regarding IS use, our study offers a fresh perspective by capturing the dynamic interaction process in delegation feedback loops. This process-oriented perspective goes beyond existing information systems research by highlighting the dynamic behavioral aspects of human-AI collaboration, unveiling previously unseen new insights into this important and increasingly crucial relationship.

Second, our findings reveal the importance of managers’ initial delegation willingness and status quo, which inherently affect managers’ subsequent delegation decisions regardless of their perceived AI performance during human-AI interactions. This insight extends the appraisal mechanism proposed in ADF and IBLT, which emphasizes performance indicators but ignores the influence of initial attitudes toward agentic AI collaborators. Moreover, the observed polarization of managers’ willingness to delegate suggests that initial attitudes toward AI can lead to entrenched behaviors, which can either facilitate or hinder effective AI adoption and collaboration. This adds depth to our understanding of the dynamics involved in human-AI interactions and the factors that influence successful AI integration.

Third, we extend the human-AI collaboration literature by demonstrating how HMM can be leveraged as a novel tool to analyze the dynamics of human-AI interactions that have been conceptualized in ADF and IBLT. As far as we know, this is the first study applying HMM to model AI delegation dynamics. In our study, HMM models longitudinal human-AI interaction data and uncovers distinct delegation willingness from observable delegation decisions, which provides a better understanding of the dynamics of human-AI collaboration. This method warrants further investigation regarding humans unobservable attitudes toward AI partners in relation to the social dynamic aspects of human-AI collaboration, wherein AI is increasingly perceived as a social entity.

From a managerial standpoint, organizations designing “human-in-the-loop” AI delegation systems may face a crucial challenge in that human delegation willingness could influence how employees interact with AI over time. This issue points to the need to ascertain employees’ attitudes toward AI collaboration and actively train them to overcome challenges associated with this complex integration of skills. This aligns with the burgeoning field of explainable AI (XAI), which emphasizes transparency as a core tenet for building trust in human-AI collaboration (Gyevnar et al., 2023). We suggest the need for a clear illustration or explanation of how the AI system was designed and trained, as well as its capabilities and weaknesses, especially when performance is assessed as a team and contributions cannot be fully attributed. Nevertheless, our findings suggest that solely focusing on reconciling human and AI decisions through transparent decision-making processes, as suggested by Lebovitz et al. (2022), may be insufficient for mitigating the persistent reluctance exhibited by certain employee groups (e.g., managers with low willingness to delegate). To overcome such reluctance and establish an effective human-AI collaboration and common ground, organizations should leverage interaction data to identify potential misalignment situations and develop targeted policies that combine education and incentives to nurture positive interactions with AI.

This work has certain limitations, yielding opportunities for future research. Our HMM approach allowed us to estimate store managers’ unobserved willingness to delegate, but did not pinpoint the reasons attributed to these delegation attitudes. In addition, the usage of HMM involves certain assumptions, which may limit a fine-grained study of delegation dynamics. The key performance feedback in our research context only presented three indicators identified in weekly assessment meetings. A more comprehensive and fine-grained performance evaluation system could better facilitate human-AI collaboration in organizational operations under different operational environments and determine why and under what conditions humans are unwilling to embrace AI. There are also potential underlying mechanisms specific to the human-AI interactions that are beyond the scope of this study. For example, alignment with managers’ personal traits—e.g., risk perceptions regarding controversial technologies (Gao et al., 2024) and learning goal orientations (Leung et al., 2023)— may affect human-AI interaction relationships, which makes it easier for managers to identify AI’s complementaries and facilitate human-AI collaborative intelligence. The complexity of the human-AI collaboration and its increasing importance warrant future studies that would design field interventions to conduct causal inference on AI delegation willingness and improve organizational operations.

## Acknowledgments

The authors express their sincerest gratitude to the senior editor, Balaji Padmanabhan, for his guidance throughout the review process. We also thank the associate editor and reviewers, whose constructive comments and suggestions assisted in the development of this project. Thanks also go to attendees at the seminar workshop held at the Hong Kong University for their helpful questions and suggestions for improving the research. This work was partially supported by the Hong Kong Research Grants Council (Grants CityU 11500123) and partially supported by the National Natural Science Foundation of China (Grant 72201222, Grant 72301267), the InnoHK initiative, the government of the HKSAR, and the Laboratory for AI-Powered Financial Technologies.

## References

Agrawal, A., Gans, J., & Goldfarb, A. (2019). The economics of artificial intelligence: An agenda. University of Chicago Press.

Baird, A., & Maruping, L. M. (2021). The next generation of research on IS use: A theoretical framework of delegation to and from agentic IS artifacts. MIS Quarterly, 45(1), 315-341. https://doi.org/ 10.25300/MISQ/2021/15882

Brynjolfsson, E., & McAfee, A. (2017). The business of artificial intelligence. Harvard Business Review. https://hbr.org/2017/07/thebusiness-of-artificial-intelligence

Chen, W., Wei, X., & Zhu, K. X. (2018). Engaging voluntary contributions in online communities: A hidden Markov model. MIS Quarterly, 42(1), 83-100. https://doi.org/10.25300/MISQ/2018/ 14196

Davenport, T. H., & Rajeev, R. (2018). Artificial intelligence for the real world. Harvard Business Review, 96(1), 108-116. https://hbr.org/2018/01/artificial-intelligence-for-the-real-world

Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319-340. https://doi.org/10.2307/249008

Dennis, A. R., Lakhiwal, A., & Sachdeva, A. (2023). AI agents as team members: Effects on satisfaction, conflict, trustworthiness, and willingness to work with. Journal of Management Information Systems, 40(2), 307-337. https://doi.org/10.1080/07421222. 2023.2196773

Fu, R., Huang, Y., & Singh, P. V. (2021). Crowds, lending, machine, and bias. Information Systems Research, 32(1), 72-92.

Fügener, A., Grahl, J., Gupta, A., & Ketter, W. (2021). Cognitive challenges in human-artificial intelligence collaboration: Investigating the path toward productive delegation. Information Systems Research, 33(2), 678-696. https://doi.org/10.1287/isre. 2021.1079

Gao, C., Gu, B., Leung, A. C. M., Liu, X., & Ye, Q. (2024). The risk of cryptocurrency payment adoption and the role of social media: Evidence from online travel agencies. Production and Operations Management. Advance online publication. https://doi.org/10.1177/10591478241231860

Goddard, K., Roudsari, A., & Wyatt, J. C. (2012). Automation bias: A systematic review of frequency, effect mediators, and mitigators. JAMIA, 19(1), 121-127. https://doi.org/10.1136/amiajnl-2011- 000089

Gonzalez, C., Lerch, J. F., & Lebiere, C. (2003). Instance-based learning in dynamic decision making. Cognitive Science, 27(4), 591-635. https://doi.org/10.1207/s15516709cog2704\_2

Graen, G. B., & Uhl-Bien, M. (1995). Relationship-based approach to leadership: Development of leader-member exchange (LMX) theory of leadership over 25 years: Applying a multi-level multidomain perspective. The Leadership Quarterly, 6(2), 219-247. https://doi.org/10.1016/1048-9843(95)90036-5

Grisold, T., & Schneider, J. (2023). Dynamics of human-AI delegation in organizational routines. In Proceedings of the International Conference on Information Systems. https://aisel.aisnet.org/ icis2023/org\_busproc/org\_busproc/4

Gupta, A., Roy, P. P., & Dutt, V. (2021). Evaluation of instance-based learning and Q-learning algorithms in dynamic environments. IEEE Access, 9, 138775-138790. https://doi.org/10.1109/ ACCESS.2021.3117855

Gyevnar, B., Ferguson, N., & Schafer, B. (2023). Bridging the transparency gap: What can explainable AI learn from the AI Act? In Proceedings of the 26th European Conference on Artificial Intelligence. https://doi.org/10.3233/FAIA230367

Joshi, K. (1991). A model of users’ perspective on change: the case of information systems technology implementation. MIS Quarterly, 15(2), 229-242. https://doi.org/10.2307/249384

Karau, S. J., & Williams, K. D. (1993). Social loafing: A meta-analytic review and theoretical integration. Journal of Personality and Social Psychology, 65(4), 681-706. https://doi.org/10.1037/0022- 3514.65.4.681

Kim, S. S., & Malhotra, N. K. (2005). A longitudinal model of continued IS use: An integrative view of four mechanisms underlying postadoption phenomena. Management Science, 51(5), 741-755. https://doi.org/10.1287/mnsc.1040.0326

Kim, Y., & Krishnan, R. (2019). The dynamics of online consumers’ response to price promotion. Information Systems Research, 30(1), 175-190. https://doi.org/10.1287/isre.2018.0793

Kokkodis, M., Lappas, T., & Ransbotham, S. (2020). From lurkers to workers: Predicting voluntary contribution and community welfare.

Information Systems Research, 31(2), 607-626. https://doi.org/ 10.1287/isre.2019.0905

Lapointe, L. & Rivard, S. (2005). A multilevel model of resistance to information technology implementation. MIS Quarterly, 29(3), 461-491. https://doi.org/10.2307/25148692

Lebovitz, Sarah., Lifshitz-Assaf, H., & Levina, N. (2022). To engage or not to engage with AI for critical judgements: How professionals deal with opacity when using AI for medical diagnosis. Organization Science, 33(1), 126-148. https://doi.org/10.1287/orsc. 2021.1549

Leung, A. C. M., Santhanam, R., Kwok, R. C.-W., & Yue, W. T. (2023). Could gamification designs enhance online learning through personalization? Lessons from a field experiment. Information Systems Research, 34(1), 27-49. https://doi.org/10.1287/isre. 2022.1123

Manyika, J., Chui, M., Miremadi, M., Bughin, J., George, K., Willmott, P., & Dewhurst, M. (2017). A future that works: AI, automation, employment, and productivity. McKinsey Global Institute.

Markus, M. L. (1983). Power, politics, and MIS implementation. Communications of the ACM, 26(6), 430-444.

Musani, P. (2023). Decking the aisles with data: How Walmart’s AIpowered inventory system brightens the holidays. Walmart Global Tech. https://tech.walmart.com/content/walmart-global-tech/ en\_us/blog/post/walmarts-ai-powered-inventory-systembrightens-the-holidays.html

Netzer, O., Lattin, J. M., & Srinivasan, V. (2008). A hidden Markov model of customer relationship dynamics. Marketing Science, 27(2), 185-204. https://doi.org/10.1287/mksc.1070.0294

Nunes, D. S., Zhang, P., & Silva, J. S. (2015). A survey on human-inthe-loop applications towards an internet of all. IEEE Communications Surveys & Tutorials, 17(2), 944-965. https://doi.org/10.1109/COMST.2015.2398816

Rabiner, L. R. (1989). A tutorial on hidden Markov models and selected applications in speech recognition. Proceedings of the IEEE, 77(2), 257-286. https://doi.org/10.1109/5.18626

Schriesheim, C. A., Neider, L. L., & Scandura, T. A. (1998). Delegation and leader-member exchange: Main effects, moderators, and measurement issues. Academy of Management Journal, 41(3), 298-318. https://doi.org/10.2307/256909

Singh, P. V., Tan, Y., & Youn, N. (2011). A hidden Markov model of developer learning dynamics in open source software projects. Information Systems Research, 22(4), 790-807. https://doi.org/ 10.1287/isre.1100.0308

Sutskever, I., Vinyals, O., & Le, Q. V. (2014). Sequence to sequence learning with neural networks. In Proceedings of the 28th International Conference on Neural Information Processing Systems. https://dl.acm.org/doi/10.5555/2969033.2969173

Todri, V., Ghose, A., & Singh, P. V. (2020). Trade-offs in online advertising: advertising effectiveness and annoyance dynamics across the purchase funnel. Information Systems Research, 31(1), 102-125. https://doi.org/10.1287/isre.2019.0877

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: toward a unified view. MIS Quarterly, 27(3), 425-478. https://doi.org/10.2307/30036540

Wilson, H. J., & Daugherty, P. R. (2018). Collaborative intelligence: humans and AI are joining forces. Harvard Business Review. https://hbr.org/2018/07/collaborative-intelligence-humans-and-aiare-joining-forces.

Zhang, Y., Li, B., Luo, X., & Wang, X. (2019). Personalized mobile targeting with user engagement stages: Combining a structural

hidden Markov model and field experiment. Information Systems Research, 30(3), 787-804. https://doi.org/10.1287/isre.2018.0831

Zhao, M., Eadeh, F. R., Nguyen, T.-N., Gupta, P., Admoni, H., Gonzalez, C., & Woolley, A. W. (2023). Teaching agents to understand teamwork: Evaluating and predicting collective intelligence as a latent variable via hidden Markov models. Computers in Human Behavior, 139, Article 107524. https://doi.org/10.1016/j.chb.2022.107524

## About the Authors

Junming Liu is an associate professor in the Department of Information Systems at the City University of Hong Kong. He received his Ph.D. from the Rutgers Business School at Rutgers University. Before joining Rutgers, he received his B.S. degree from the School of the Gifted Young at the University of Science and Technology of China (USTC). His general areas of research are data mining, supply chain analytics, urban computing, and largescale optimization, with a focus on developing effective and efficient data mining techniques for emerging big data and supply chain applications. He has published prolifically in top venues of data mining and information systems.

Wei Thoo Yue is a professor of management information systems in the Department of Information Systems at City University of Hong Kong. He received his Ph.D. in management information systems from Purdue University. Prior to joining City University of Hong Kong, he was a faculty member at the University of Texas, Dallas. His research interests focus on the economics of information systems. His work has appeared in Management Science, Information Systems Research, MIS Quarterly, Journal of Management Information Systems, Decision Support Systems, and other journals.

Alvin Chung Man Leung is an associate professor in the Department of Information Systems, City University of Hong Kong. He received his Ph.D. in information management from the McCombs School of Business, the University of Texas at Austin. His research interests include IT business value, financial technology, technology-mediated learning, and information security. His work has appeared in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Management Science, Decision Support Systems, and other journals. He has received various research and teaching-related awards, including the AIS Early Career Award and the UGC Early Career Award.

Xin Zhang is an assistant professor of management information systems at the International Institute of Finance, School of Management, University of Science and Technology of China. He holds dual Ph.D. degrees in information systems from the City University of Hong Kong and in management science from the University of Science and Technology of China. His research interests include the economics of information systems, human-AI interaction, platform business models, and data pricing. His work has been published or accepted in leading journals such as MIS Quarterly, Information Systems Research, and Journal of Management Information Systems, as well as in premier conference proceedings including ICIS, CIST, WITS, and PACIS.

## Appendix A

## Multidimensional Performance Measurement

Measurement of sales improvement for Team vs. Human performance evaluation: Let $S a l e s _ { i t }$ represent the sales performance of store ?? operated by manager ?? in period $t , t = 0 , 1 , 2 , \ldots , T$ and $S a l e s _ { i } ^ { - }$ represent the 30-days average sales performance before the AI system was implemented. The period when the AI system was implemented is indexed $t = 0$ . The Team vs. Human $T H _ { i t }$ performance in period ?? is defined as the improvement of sales performance in period ?? compared with the pre-implementation performance:

$$
T H _ {i t} = \frac {S a l e s _ {i t} - S a l e s _ {i} ^ {-}}{S a l e s _ {i} ^ {-}} \times 100 \%\tag{A.(1}
$$

Measurement of outperforming AI for Team vs. AI performance evaluation: Let $D _ { i k d }$ represent the observed demand of product ?? in store ?? in day $\mathop { d } \left( \boldsymbol { d } \in \widehat { \mathop { t } } \right)$ and $D L _ { i k d }$ represent the demand loss when there is a stockout. The corresponding uncensored sales performance $\widehat { S a l e s } _ { \iota t }$ is estimated as the best sales performance the manager can achieve with zero stockout and zero product waste: $\widehat { S a l e s } _ { \iota t } =$ $\begin{array} { r } { \sum _ { k } \sum _ { d \in t } S P _ { k } ( D _ { i k d } + D L _ { i k d } ) } \end{array}$ , where $S P _ { k }$ is the sales price of product ??. If the replenishment decision $D _ { i k d } ^ { \prime }$ made by the AI system was not overridden by the human manager, the estimate sales performance $S a l e s _ { i t } ^ { \prime }$ achieved by the AI system is then estimated as follows:

$$
S a l e s _ {i t} ^ {\prime} = \sum_ {k} \sum_ {d \in t} S P _ {k} \times m i n (D _ {i k d} + D L _ {i k d}, D _ {i k d} ^ {\prime}) - O P _ {k} \times \max {(0, D _ {i k d} ^ {\prime} - (D _ {i k d} + D L _ {i k d}))},\tag{A.(2}
$$

where $O P _ { k }$ represents the ordering price of product ??. The first term and the second term in $\mathbf { A } . ( 2 )$ represent the revenue and cost of product waste, respectively. The factor “Team vs. $\mathbf { A } \mathbf { I } ^ { \ast } ( T A _ { i t } )$ is then calculated as the difference between the observed sales performance $S a l e s _ { i t }$ and the estimated AI performance without human involvement in the same period ??:

$$
T A _ {i t} = \frac {S a l e s _ {i t} - S a l e s _ {i} ^ {\prime}}{S a l e s _ {i} ^ {\prime}} \times 100 \%\tag{A.(3}
$$

Measurement of team competitiveness for Team vs. Team performance evaluation: The factor Team vs. Team $( T T _ { i t } )$ performance is defined as the sales comparison between store manager ?? and the regional average of all store managers in the manager set ℳ:

$$
T T _ {i t} = S I _ {i t} - \frac {\sum_ {i \in \mathcal {M}} S I _ {i t}}{| \mathcal {M} |} \times 100\tag{A.(4}
$$

## Appendix B

## Additional Results

Table B1 presents results for the analysis of store ownership. Table B2 and Table B3 present results for robustness tests using bakery and dairy product samples, respectively.

<table><tr><td colspan="4">Table B1. Estimation Results for the Analysis of Store Ownership</td></tr><tr><td>Variable</td><td>State 1 (L)</td><td>State 2 (M)</td><td>State 3 (H)</td></tr><tr><td colspan="4">Emission factors ( $\rho, \eta$ )</td></tr><tr><td>Emission intercept</td><td>-0.2753***</td><td>-0.0537</td><td>0.1844**</td></tr><tr><td>Implementation age</td><td>0.0478</td><td>0.0221</td><td>0.1081</td></tr><tr><td>Implementation age squared</td><td>-0.2716</td><td>-0.0823</td><td>0.1885*</td></tr><tr><td>Bad weather</td><td>-0.0017</td><td>0.0122</td><td>-0.1256**</td></tr><tr><td>Holiday</td><td>-0.0405</td><td>-0.0059</td><td>-0.1922**</td></tr><tr><td>Manager-specific heterogeneity</td><td> $\xi=0.0303$ </td><td></td><td></td></tr><tr><td colspan="4">Transition threshold ( $\mu$ )</td></tr><tr><td>To State 1 (L)</td><td></td><td>-0.1276</td><td>-1.9851**</td></tr><tr><td>To State 2 (M)</td><td>0.7821**</td><td></td><td>-1.0413</td></tr><tr><td>To State 3 (H)</td><td>1.4651**</td><td>-0.0943</td><td></td></tr><tr><td>Manager-specific heterogeneity</td><td> $\delta=-0.1855**$ </td><td></td><td></td></tr><tr><td colspan="4">Transition factors( $\beta$ )</td></tr><tr><td>Team vs. Human</td><td>0.0448</td><td>-0.2173</td><td>0.0051</td></tr><tr><td>Team vs. AI</td><td>0.0015</td><td>0.0103</td><td>0.0957</td></tr><tr><td>Team vs. Team</td><td>0.2564</td><td>-0.0132</td><td>-0.4099**</td></tr></table>

Note: \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01, (Welch's t-test for all variables)

<table><tr><td colspan="4">Table B2. Estimation Results of Three-State HMM for Bakery Product Delegation</td></tr><tr><td>Variable</td><td>State 1 (L)</td><td>State 2 (M)</td><td>State 3 (H)</td></tr><tr><td colspan="4">Emission factors ( $\rho, \eta$ )</td></tr><tr><td>Emission intercept</td><td>0.1147**</td><td>0.2133***</td><td>0.3176***</td></tr><tr><td>Implementation age</td><td>-0.3249***</td><td>-0.1724***</td><td>-0.1005**</td></tr><tr><td>Implementation age squared</td><td>0.0889**</td><td>0.0167</td><td>0.0604**</td></tr><tr><td>Bad weather</td><td>-0.0022</td><td>-0.0576**</td><td>-0.0609**</td></tr><tr><td>Holiday</td><td>0.0045</td><td>-0.0535***</td><td>-0.0884***</td></tr><tr><td>Manager-specific heterogeneity</td><td> $\xi=0.6202^{***}$ </td><td></td><td></td></tr><tr><td colspan="4">Transition threshold ( $\mu$ )</td></tr><tr><td>To State 1 (L)</td><td></td><td>-0.2241***</td><td>-1.8478***</td></tr><tr><td>To State 2 (M)</td><td>1.3315***</td><td></td><td>-1.3116***</td></tr><tr><td>To State 3 (H)</td><td>1.7005***</td><td>0.1797**</td><td></td></tr><tr><td>Manager-specific heterogeneity</td><td> $\delta=0.2961^{***}$ </td><td></td><td></td></tr><tr><td colspan="4">Transition factors( $\beta$ )</td></tr><tr><td>Team vs. Human</td><td>-0.2778***</td><td>-0.2383***</td><td>-0.4354***</td></tr><tr><td>Team vs. AI</td><td>0.5745***</td><td>0.2288***</td><td>0.9853***</td></tr><tr><td>Team vs. Team</td><td>0.2075***</td><td>0.1516**</td><td>-0.4223***</td></tr></table>

Note: \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01, (two-tailed t-test for all variables)

<table><tr><td colspan="4">Table B3. Estimation Results of Three-State HMM for Dairy Product Delegation</td></tr><tr><td>Variable</td><td>State 1 (L)</td><td>State 2 (M)</td><td>State 3 (H)</td></tr><tr><td colspan="4">Emission factors ( $\rho, \eta$ )</td></tr><tr><td>Emission intercept</td><td>0.0923**</td><td>0.1919***</td><td>0.2798***</td></tr><tr><td>Implementation age</td><td>-0.2922***</td><td>-0.1565***</td><td>-0.1052***</td></tr><tr><td>Implementation age squared</td><td>-0.0848**</td><td>-0.0658</td><td>0.0932**</td></tr><tr><td>Bad weather</td><td>-0.008</td><td>-0.0619**</td><td>-0.0691***</td></tr><tr><td>Holiday</td><td>0.0159</td><td>-0.0568**</td><td>-0.1015**</td></tr><tr><td>Manager-specific heterogeneity</td><td> $\xi=0.6490^{***}$ </td><td></td><td></td></tr><tr><td colspan="4">Transition threshold ( $\mu$ )</td></tr><tr><td>To State 1 (L)</td><td></td><td>-0.2769***</td><td>-1.7837***</td></tr><tr><td>To State 2 (M)</td><td>1.2866***</td><td></td><td>-1.2922***</td></tr><tr><td>To State 3 (H)</td><td>1.6842***</td><td>0.1606***</td><td></td></tr><tr><td>Manager-specific heterogeneity</td><td> $\delta=0.2850^{***}$ </td><td></td><td></td></tr><tr><td colspan="4">Transition factors( $\beta$ )</td></tr><tr><td>Team vs. Human</td><td>-0.2882**</td><td>-0.2274***</td><td>-0.5079***</td></tr><tr><td>Team vs. AI</td><td>0.5214***</td><td>0.2230***</td><td>1.2085***</td></tr><tr><td>Team vs. Team</td><td>0.2756**</td><td>0.1526**</td><td>-0.4391***</td></tr></table>

Note: \* p < 0.1; \*\* p < 0.05; \*\*\* p < 0.01, (two-tailed t-test for all variables)