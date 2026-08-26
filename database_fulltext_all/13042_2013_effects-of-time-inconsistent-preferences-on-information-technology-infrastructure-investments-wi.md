---
otero_id: 13042
otero_key: "K6H8EN73"
title: "Effects of time-inconsistent preferences on information technology infrastructure investments with growth options"
authors: "Sarah S Khan; Moutaz Khouja; Ram L Kumar"
year: "2013"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2012.4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
RESEARCH ARTICLE

# Effects of time-inconsistent preferences on information technology infrastructure investments with growth options

Sarah S. Khan, Moutaz Khouja\* and Ram L. Kumar

Belk College of Business, UNC Charlotte Charlotte, NC, U.S.A.

\*Correspondence: Moutaz Khouja, Business Information Systems and Operations Management, UNC Charlotte, 351C Friday, 9201 University City Blvd, Belk College of Business, Charlotte, NC 28223, U.S.A. Tel: þ 1 704 687 7653; Fax: þ 1 704 687 6330; E-mail: mjkhouja@uncc.edu

## Abstract

Increasing information technology (IT) infrastructure spending and the capability of such projects to provide a platform for a firm to realize value from IT marks their importance. Effective management of IT infrastructure investments includes identification of embedded growth options in the infrastructure, and exercising them in a timely manner. Extant research has recognized that while managers could use real options thinking in IT investment management, managerial bias could affect the timing of option exercise and their realized value. We analyze the effect of time-inconsistent preferences of present-biased managers on the exercise time of real growth options and the realized value using a discrete time option valuation model. The results show that presentbiased managers are more likely to exercise options early when the net payoffs are low, the option payoffs have high volatility, and the risk free discount rate is small. In addition, present biased managers are more likely to exercise a growth option early in its life when the project is performing well. We provide implications for practice and IT governance. European Journal of Information Systems (2013) 22, 206–220. doi:10.1057/ejis.2012.4; published online 21 February 2012

Keywords: IT investments; IT Infrastructure; real options; growth options; time preferences; present biased preferences

## Introduction

Information technology (IT) investments are a collection of technological components and human skills that serve the needs of an organization. It provides a platform to facilitate large-scale connectivity, effective interoperation of an organization<sup>0</sup>s IT applications, and strategic alignment of IT (Kumar, 2004; Colin & Dhaliwal, 2011). They are complex endeavors which include decisions about large-scale enterprise systems, networks, and databases (Gal et al, 2008). IT infrastructure investments have been under a spotlight due to their increasing importance. According to CIO magazine (2010), IT infrastructure spending was expected to grow 9.2% in 2010, which is above the 6.6% average of other IT products and services.

Investment in IT infrastructure may enable other projects and their completion along with the infrastructure itself may yield significant value (Dos Santos, 1991; Bardhan et al, 2004). For example, investment in software platforms such as operating systems, database systems, workflow/workgroup systems, and application packages such as SAP R/3 or ORACLE enable firms to realize value from their application systems (Taudes et al, 2000). Investment in a data architecture or telecommunications network may provide a firm with an opportunity to implement a new product differentiation strategy that employs these infrastructures (Kambil et al, 1993). Investment in web technologies provides the firm with numerous e-business opportunities and process automation (Bardhan et al, 2004). Investment in electronic banking services allows firms to deploy point-of-sale debit services (Benaroch & Kauffman, 1999, 2000). These examples illustrate how IT infrastructure projects have embedded ‘growth’ options, where firms have a ‘right’ but not an obligation to initiate future projects (Kambil et al, 1993; Taudes et al, 2000).

IT infrastructure investments contain options whose exercise brings forth further opportunities for investment as well as generating cash flows (Panayi & Trigeorgis, 1998). Hence growth options enabled by IT infrastructure projects play a significant role in their economic justification. These investments are categorized as high risk due to their capital intensive nature, irreversibility, and valuation difficulty<sup>1</sup> (Dos Santos, 1991; Kambil et al, 1993). Traditional financial metrics (Discounted Cash Flows, Net Present Value, Internal Rate of Return, and Return on Investment) have been shown to undervalue IT infrastructure projects because they ignore the value of the opportunity for managers to intervene during the project’s course (Taudes et al, 2000). Hence real options analysis is advocated because it takes into account the uncertainty involved in IT investments while considering managerial flexibility in decision making (Benaroch & Kauffman, 1999; Benaroch, 2002; Kumar, 2002; Tiwana et al, 2006).

The value of real options depends on the time of their exercise (Dos Santos, 1991; Kumar, 1999). IT literature assumes managers as rational economic agents who would exercise these options on time. This rationality assumption has several implications. Economic agents maximize utility by eliminating any state of the world that yields the same outcome regardless of one<sup>0</sup>s choice (cancellation), adhering to transitivity of preferences (transitivity), selecting the dominant option when one option is better than another in one state and at least as good in all other states (dominance), by showing same preferences in the face of different representations of the same choice problem (invariance), and by showing same preferences about the future plan at different points in time (time-consistent preferences) (Tversky & Kahneman, 1986). However, some information systems (IS) literature provides evidence that managers may not possess all the above characteristics (Tiwana et al, 2006), and so does the literature on time-inconsistent preferences (Frederick et al, 2002). We therefore examine the implications of IT managers being bounded rational agents with time-inconsistent preferences, applying real options thinking in managing growth options.

This paper examines the relationship between managerial bias and time of option exercise. We focus on a growth option whose value depends on the option exercise time (Dos Santos, 1991; Kumar, 1996, 2002) and realization of option value depends on its optimal exercise. The economic literature suggests that people could have a bias for the present (Thaler, 1981; Loewenstein & Prelec, 1992), which in turn, could affect real options thinking. We explore the effects of time-inconsistent preferences on IT growth option exercise time and its realized value. Using a two time periods binomial model for option valuation, and utility model for inter-temporal preferences, we derive a closedform expression for the critical value of the present-bias self-control parameter below which a manager will exercise the option too early. We provide insights on how present-bias interacts with option parameters and extend the analysis to more than two periods’ option in a numerical experiment. The results indicate that present-bias impacts growth option value via suboptimal exercise timing. A manager with time-inconsistent preferences may fail to foresee that he will evaluate the payoffs differently in the future than today leading to suboptimal exercise time. Furthermore, a present-biased manager is more likely to exercise a growth option early when the project is performing well. Organizations aware of the present bias preferences of the managers can develop incentives geared towards minimizing the risks from early growth option exercise. Findings of this study may apply to other investments embedding real growth options such as manufacturing infrastructure and R&D.

The following section summarizes the relevant literature on real options in IT investments along with the literature on time-inconsistent preferences. Subsequently, a model of time-inconsistent preferences for growth options with two exercise periods is presented along with a numerical example and sensitivity analysis. A numerical experiment examining the problem with more than two exercise periods is then conducted. Finally, discussion and implications are presented.

## Literature review

## Incentivizing IT growth options

There is extensive IS literature on IT infrastructure investments embedding growth options. Dos Santos (1991) justified investment in IT infrastructure projects by conceptualizing them as having embedded growth options. He used Margrabe’s financial options framework (Margrabe, 1978) to justify the value of initial investment with optional future projects. Panayi & Trigeorgis (1998) valued IT investment proiects in telecommunication infrastructure utilizing a growth options framework. Taudes (1998) developed a general valuation model for IT software growth options in the context of embedded IS functions in an IT platform. Benaroch & Kauffman (1999, 2000) used a traditional call option to evaluate the deployment of IT point-of-sale debit services as a growth opportunity. Hilhorst et al (2008) proposed a method to select a preferred IT infrastructure from competing alternatives using Dempster-Shafer theory along with real options theory.

Although real options use is justified and advocated in IS literature, formal real options models are rarely used by managers in practice due to the complexity and difficulty in calculating the value of real options (Tiwana et al, 2007). Research has shown that even if managers are not aware of the method, or are not formally using it, their intuitions and decisions agree with the qualitative prescriptions of the framework most of the times. This phenomenon is referred to as real options thinking (Busby & Pitts, 1997) and is considered as an alternative to formal real options analysis (Fichman et al, 2005). Some studies have claimed that in the absence of explicit real options methods or training, managerial intuition typically responds in the correct direction to the factors that determine normative real options values (McGrath, 1997, 1999; McDonald, 2000; Miller & Shapira, 2004). According to this view, formal or heuristic real options analysis adds logical support and quantitative precision to managerial intuition but does not differ qualitatively from it. In case of IT investments, studies indicate that managerial intuition may not always conform to real options theories, due to managerial bias (Tiwana et al,

2007; Lankton & Luft, 2008). Incentives may be appropriate in order to foster real options thinking.

## Real options and managerial biases

While several models have been introduced for real options analysis of IT projects (Dos Santos, 1991; Kumar, 1999, 2002; Benaroch, 2002; Schwartz & Zozaya-Gotostiza, 2003), firms continue to use intuition instead of the formal analyses to manage flexibility in the projects (Fichman et al, 2005; Lankton & Luft, 2008). Hence, investment decision making in IT projects remains a mix of formal real options analysis, and qualitative real options thinking, with conventional financial methods.

A stream of MIS literature exploring causes of managerial risk in investment decisions from a behavioral perspective has been growing. Table 1 highlights the major findings of some of these studies that view the divergence between real options thinking and real options analysis as a major cause of risk in IT project management.

Effective options thinking requires managers to recognize and enhance opportunities to create options within IT projects, value these options, and manage projects to fully extract this value (Fichman et al, 2005). The largest value of an option is realized when it is exercised at the optimal time (Kumar, 2002). Hence, exercising real options suboptimally (when it is worth waiting or when the optimal exercise time has passed) reduces their value. This behavior is most likely to occur when managers apply real options thinking. Prior research has examined factors consisting of personal characteristics of managers including preferences based on their attitude towards risk (Tiwana et al, 2006, 2007; Lankton & Luft, 2008) that result in real options thinking being different from real options analysis. For example, an option to abandon is less preferred by managers compared to an option to grow, switch, and/or scale (Tiwana et al, 2007). External factors such as market competition also affect managers’ risk preferences (Lankton & Luft, 2008). Adding to this list, we build a case for present-biased managers, who may fail to realize the optimal value of the growth option by exercising it too early.

Table 1 Research identifying various managerial biases affecting real options thinking

<table><tr><td>Study</td><td>Findings</td><td>Explanation</td></tr><tr><td>Lankton &amp; Luft (2008)</td><td>As uncertainty increases, individuals judge deferral options as more valuable than growth options.Competitor&#x27;s presence decreases deferral option value while increasing growth option value.</td><td>Option-specific decisions are based on expected utility payoffs and anticipated regret, consistent with behavioral economic theories.</td></tr><tr><td>Tiwana et al (2007)</td><td>IT managers show bounded rationality bias in real option valuation for growth, scaling, switching, and abandonment options.For option to scale, managers value the flexibility to change scale irrespective of project NPV, unlike in the case of staging and deferral options.</td><td>Managers only search for more information to support the project when project&#x27;s NPV is low. With high NPV they do not assess real options.</td></tr><tr><td>Tiwana et al (2006)</td><td>Managers correctly recognize and value real options in troubled IT projects.Managers intuitively value growth options more than operational options (stage, scale, switch, defer, and abandon).</td><td>Possible reasons for differences across option types include signaling effects, exercise difficulty, framing effects, and anti-failure bias.</td></tr><tr><td>Benaroch et al (2006a)</td><td>Managers follow options-based risk management mostly based on intuition.Intuitive decisions lead to suboptimal or counter-productive practices.</td><td>Managers intuitively think of forms of flexibility (options thinking) as the level of risk rises.</td></tr></table>

## Time-inconsistent preferences

Time-inconsistent preference refers to the preference for immediate utility over delayed utility (Frederick et al, 2002). Experimental studies suggest that people have time-inconsistent preferences (Thaler, 1981; Loewenstein & Prelec, 1992). It means when two rewards are far away in time, people act relatively patiently (e.g., they prefer two apples in 101 days, rather than one apple in 100 days). However, when both rewards are brought forward in time, they act more impatiently (e.g., they prefer one apple today, rather than two apples tomorrow). Hence these individuals give greater weight to earlier reward as it gets closer. These time-inconsistent preferences are also known as ‘present-biased’ preferences (O’Donoghue & Rabin, 1999a). We will use this term from here on.

From a theoretical perspective, Phelps & Pollak’s (1968) study is the first to analyze the dynamically inconsistent time-preferences. Later O’Donoghue & Rabin (1999a) proposed a utility model for a person’s inter-temporal preferences at time $t ,$ which captures the salience of the present over the future. These ‘present-biased’ preferences are represented by a simple model referred to as ‘quasi-hyperbolic’ or $( \beta , \delta ) \cdot$ - preferences.

$$
U ^ {t} (u _ {t}, u _ {t + 1}, \dots u _ {T}) \equiv \delta^ {t} u _ {t} + \beta \sum_ {\tau = t + 1} ^ {T} \delta^ {T} u _ {\tau}.
$$

With $u _ { t }$ as the instantaneous utility an individual receives at period $t ,$ the utility function $U ^ { t }$ represents his intertemporal preferences at time $t .$ In this model, parameter d is a simple discount rate for future utilities, and $\beta = ( 0 , 1 ]$ is a self-control parameter, that represents a time-inconsistent preference for immediate gratification. For $\beta = 1$ , these preferences are time-consistent; but for $\beta < 1$ the individual has a bias for now over the future. In other words, as b decreases, people are more present-biased.

To better understand how these preferences address self-control problems, consider the following example similar to the one given by O’Donoghue & Rabin (2003). Suppose an IT manager can choose to invest in two technologies, ipad2 in period 2 or Samsung galaxy 10.1 in period $^ { 3 , }$ but can’t invest in both, due to scarcity of resources. If Samsung galaxy 10.1 gives higher utility as a productivity tool (in terms of connectivity, backward integration with existing systems, etc.) than ipad2, these options yield the following instantaneous utilities (u ):

ipad2 in period 2 : u ¼ 0; u ¼ 4; and u ¼ 0: Samsung galaxy 10:1 in period 3 : u ¼ 0; u ¼ 0; and u ¼ 6:

The instantiations future utilities $( u _ { 2 }$ and $u _ { 3 } )$ are lumpsum utilities for the respective time period $( t = 2 , 3 )$ adjusted for time value of money that takes into account utilities from all future periods as well. An IT manager’s utility, with self-control parameter $\beta = 1 / 2$ (assuming $\delta = 1 )$ in period 1, will be $U _ { 1 } = m a x [ 1 / 2 u _ { 2 } , 1 / 2 u _ { 3 } ]$ . Hence, the manager prefers to invest in Samsung galaxy $^ { 1 0 . 1 , }$ because it yields intertemporal utility of $( 1 / 2 ) 6 = 3$ whereas investing in ipad2 would yield intertemporal utility of $( 1 / 2 ) 4 = 2$ . When period 2 arrives, the manager’s preferences change to $U _ { 2 } = m a x [ u _ { 2 } , 1 / 2 u _ { 3 } ]$ and he now prefers to invest in ipad2, because doing so yields intertemporal utility of 4 whereas waiting for Samsung galaxy 10.1 would yield intertemporal utility of 3. Such impatience towards technological investments has been observed in organizations (CIO, 2011).

Several studies have utilized time-inconsistent preferences to study problems in different areas (Fredrick et al, 2002). Also, the use of quasi-hyperbolic discounting to conceptualize ‘present-biased’ preferences of managers is seen in different fields as shown in Table 2. We integrated this basic model with real option model to evaluate the effect(s) of present-bias on growth option exercise decision.

The key to understanding present-bias preferences is to consider a person at each decision time period as a separate agent who maximizes utility with regards to his current preferences while his ‘future selves’ will determine future behavior according to the preferences that prevail at that time (O’Donoghue & Rabin, 1999a). Therefore, a person’s belief about his future selves’ preferences becomes important, because evaluating future preferences differently does not mean that person has a bias for present. It is the self-awareness of the timeinconsistent preferences that plays a role, since an individual who is aware of his time inconsistency will anticipate their future choices and choose consequently (Caillaud & Jullien, 2000), as compared to the individuals who lack such awareness. There are four types of assumptions about individuals’ self-awareness, based on their actual self-control parameter $\beta ,$ and their perceptions about future self-control parameter $\hat { \boldsymbol { \beta } }$ (O’Donoghue & Rabin, 2003). If the person believes that in the future he will encounter self-control problem, that is ${ \hat { \boldsymbol { \beta } } } < 1 ,$ he will choose his current behavior to maximize his current preferences (determined by his true self-control parameter $\beta ) .$ With this formulation, people with standard time-consistent (TC) preferences (do not have a bias for present and are fully aware of it) have $\hat { \boldsymbol { \beta } } = \boldsymbol { \beta } = 1$ sophisticates (have a bias for present and are aware of it) have $\hat { \boldsymbol { \beta } } = \boldsymbol { \beta } < 1$ , naı¨ves (have a bias for present but believe otherwise) have $\beta < \hat { \boldsymbol { \beta } } = 1 .$ , and partial naı¨ves (have a bias for present and are partially aware of it) have $\beta < \hat { \boldsymbol { \beta } } < 1$

We consider two cases of self-awareness of managers in making IT infrastructure investments, that is TC and naı¨ve. We examine the effects of the actual self-control parameter $\beta$ of the manager on the growth option exercise decision. TC with their actual self-control parameter $\beta$ and their perceptions about future selfcontrol parameter $\hat { \boldsymbol { \beta } }$ both equal to 1 will provide one extreme case with no bias for present and as a benchmark for comparison. Naı¨ves with their actual self-control parameter $\beta$ less than 1 (showing bias for present) but their perceptions about future self-control parameter $\hat { \boldsymbol { \beta } }$ equal to 1 showing their complete unawareness about their actual biased preferences will provide the other extreme case to capture the effects of present bias on growth option exercise decision. We do not consider sophisticates and partial naı¨ves to keep the analysis simple, but they are a valid extension to this study. If the sophisticates and partial naı¨ves are considered, then for those types, $\hat { \boldsymbol { \beta } }$ is less than 1 and the analysis should reflect that. Also, TC and naı¨ve cases are the most discussed ones in the literature (Fredrick and Loewenstein, 2002).

Table 2 Literature on ‘present-biased’ preferences

<table><tr><td>Reference</td><td>Area</td><td>Problem studied</td><td>Major findings</td></tr><tr><td>O&#x27;Donoghue &amp; Rabin (1999a)</td><td>Economics</td><td>How principals should design incentives to induce time-inconsistent agents to complete tasks efficiently</td><td>Salient rewards can potentially be efficiency-enhancing as compared to punishment for delaying a task. Simple deadlines are better than simple rewards for completing a task early.</td></tr><tr><td>O&#x27;Donoghue &amp; Rabin (1999b)</td><td>Economics</td><td>How timing of costs and rewards and agents sophistication affect present biasness</td><td>Naïve people delay immediate cost activities and rush in immediate reward activities.Sophistication mitigates putting off tasks, but aggravate rush behavior.For immediate cost activities, a small present-bias can severely affect naïve decision makers. For immediate rewards activities, a small present-bias can severely affect only sophisticated people.</td></tr><tr><td>Laibson (1997)</td><td>Marketing</td><td>Decisions of a hyperbolic consumer who has access to an illiquid asset whose sale must be initiated one period before the sale proceeds are received</td><td>Financial innovation may have caused the ongoing decline in U.S. savings rates.Financial market innovation may reduce welfare by providing &#x27;too much&#x27; liquidity.</td></tr><tr><td>Caillaud &amp; Jullien (2000)</td><td>Economics</td><td>Implications of time-inconsistent preferences for individual behavior</td><td>Time-inconsistency is characterized by a positive value of commitment.A fundamental approach to the formalization of time-inconsistent preferences is to use an axiomatic approach based solely on revealed preferences.</td></tr><tr><td>Della Vigna &amp; Malmendier (2004)</td><td>Economics</td><td>How do rational firms respond to consumer biases via contract design?</td><td>Firms price investment goods below marginal cost and leisure goods above marginal cost.For all goods firms introduce switching costs and charge back-loaded fees.Contractual design targets consumer misperception of future consumption and underestimation of the renewal probability.Time-inconsistency has adverse effects on naïve consumers&#x27; welfare.</td></tr><tr><td>Gilpatric (2008)</td><td>Management</td><td>Occurrence of shrinkage in contracts</td><td>Present-biased preferences of employees, their naïveté about it, and employers&#x27; inability to penalize shrinkage, leads to shrinkage in contractual agreements.Shrinkage can be reduced if employers allow some opportunity for employees to work less hard than they anticipate.</td></tr><tr><td>Gilpatric (2009)</td><td>Marketing</td><td>Occurrence of slippage in mail-in rebate programs</td><td>Present-biased preferences of consumers and their naïveté lead to slippage in rebates.Rebates are profitable once designed to exploit these preferences.</td></tr><tr><td>Brocas &amp; Carrillo (2001)</td><td>Management</td><td>How the individual&#x27;s time-inconsistent preferences affect their decision to invest in projects yielding either current costs and future benefits or current benefits and future costs?</td><td>Competition between agents for the same project mitigates the tendency to procrastinate. Complementarity of projects aggravates the tendency to rush and to procrastinate and can decrease the expected welfare of each individual.</td></tr><tr><td>O&#x27;Donoghue &amp; Rabin (2008)</td><td>Management</td><td>How time-inconsistent preferences impact projects with multiple stages?</td><td>Naïve people might undertake costly effort to begin projects but never finish.Procrastination is more likely when the costs of completing different stages are more unequal, and when later stages are more costly that people start but do not finish projects.If the cost structure is endogenous, people are prone to choose cost structures that lead them to start but not finish projects.</td></tr></table>

As discussed before, in the IT real options framework, it is assumed that managers exercise real options on time. However, this may not be true in practice. Suppose a manager initially plans to exercise a growth option at a specific future time based on pre-determined criteria. Theoretically, the option exercise decision will be made at the pre-determined time if the criteria are met. However, there could be several cases where such options are exercised either too early or are allowed to expire (Coff & Laverty, 2007), resulting in compromised payoffs. Evidence of early commitment to premature technologies (Kogut & Kulatilaka, 1994) and early market entry with new technology (Kalish & Lilien, 1986) has been reported. Such actions of IT managers can possibly be attributed to present-bias.

It can be argued that incentives may dominate biases like effects of time-inconsistent preferences on growth option exercise decisions. This argument is situation specific. Situations can be found where incentives might not dominate time-preferences of IT managers. Time-inconsistent preferences have shown to affect entrepreneurial decisions (Brocas & Carrillo, 2001), contract designs (Gilpatric, 2008), and long-term projects (O’Donoghue & Rabin, 1999b).

## Time-inconsistent preference and real options on IT assets

A standard option has two stages, commitment stage and option exercise stage (Hull, 2008). At the commitment stage, value of the asset underlying the option is evaluated based on future payoffs from the exercise decision, and costs involved in exercising the option. For example, investment in ERP systems or DSS systems has an option for competitive expansion by utilizing it to integrate the supply chain (Collins et $^ { a l , }$ 2010). In this scenario, the growth option is the opportunity for competitive expansion. Similarly, investment in secure network infrastructure has an option for office automation by mobilizing employees via cloud computing and equipping them with mobile devices, or for flexible decision support in dynamic inter-organizational networks (Collins et al, 2010). Hence to value these options, cost of implementing the ERP/DSS system or communication network are the commitment costs for the projects and the growth options they provide, and costs involved in competitive expansion, office automation or strategic flexibility are the exercise prices of these options. The benefits from competitive expansion, office automation or strategic flexibility are the payoffs from exercising these options. To realize the value of these growth options, managers must decide whether to go for competitive expansion/office automation/strategic flexibility or not, when the necessary infrastructure is in place. This is known as exercise stage. The growth option exercise decision is made based on the current project progress and potential future payoffs (e.g., if ERP/DSS system implementation was successful, and supply chain members have the compatible technology enabling integration), and before the expiration of the option. Hence the option exercise stage is contingent to commitment stage (Dos Santos, 1991; Kumar, 1996, 2002), and realized option value depends on the exercise time.

In IS literature, real option analysis assumes managers are rational when making decisions. However, the economics literature argues that people could have a bias for the present (Thaler, 1981; Loewenstein & Prelec, 1992), and their lack of awareness about this bias leads to suboptimal choices. This, in our case, translates into the potential for IT managers exercising a growth option pre-maturely.

## The utility function for real options

We assume an IT infrastructure project with significant start up cost, where benefits can only be realized once all the costs are incurred. Typically the project without growth options will be valued using the discounted cash flow (DCF) method as

$$
\begin{array}{l} \text { Project   value } ^ {D C F} = \pi - c \text { with } \pi = P V (\pi_ {i}) \\ = \sum_ {i = 1} ^ {T} \frac {\pi_ {i}}{(1 + r) ^ {i}} \end{array} ,\tag{1}
$$

where i ¼ a period index; p ¼ all the certain payoffs from the project; c ¼ all the costs incurred to execute the project; r ¼ risk-free discount rate; and T ¼ life of project.

If p4c, the project is profitable. For IT infrastructure projects, most of the future payoffs/benefits are uncertain, which makes it difficult to determine the true economic value of the project upfront, hence leading to difficulty in their economic justification. For such cases, if a project embeds a growth option, it will have additional value from the flexibility of future decision making (Trigeorgis, 1993; Benaroch, 2002).

$$
\text { Project   value } ^ {R O} = \pi - c + \text { real   growth   option   value },
$$

where Project value<sup>RO</sup> is the net strategic value of the project, which is equal to the difference between certain payoffs from the project and costs involved to execute the project (pc), and the value of decision-making flexibility.

To value growth options, we use a binomial option valuation method (Cox et al, 1979) due to its simplicity, its requirements for estimating fewer parameters, easy application to a single real option case, and its previous successful implementation in IT investments (Kambil et al, 1993; Benaroch, 2002; Dai et al, 2007). This method assumes that the underlying asset value (present value of future payoffs) follows a binomial multiplicative diffusion process. Starting at time $t _ { 1 } = 1$ , the future payoffs value from the project may rise by factor u with probability $p$ or fall by factor d with probability $1 - p ,$ by the exercise decision time $t _ { 2 } = t _ { 1 } + \Delta t .$ . Hence, at the option exercise decision time in $t _ { 2 } ,$ the expected value of the option payoffs will have only two possible variations. The IT manager will take into account these movements of the future payoffs from the growth option to evaluate the project’s full value. The value of the real option, $V ,$ is calculated via backward induction by<sup>2</sup>:

$$
\begin{array}{c} V = p \max [ 0, u b - f ] + (1 - p) \max [ 0, d b - f ] / r \\ \text { for } n = 1 \end{array} ,\tag{2}
$$

where $u = e ^ { \sigma { \sqrt { \Delta t } } }$ (expected upward movement in future benefits), $d = 1 / u$ (expected downward movement in future benefits), dorou; r ¼ risk-free rate; T ¼ project life (option expiration time); s ¼ uncertainty around future payoffs; $p { = } ( r { - } d ) / ( u { - } d ) $ ; subjective probability of the event; f ¼ one time follow-up investment (to exercise the growth option), and b ¼ benefits realized after exercising the real option.

For a growth option with n periods until maturity, option value depends on the same parameters and becomes complex. As long as option value is greater than zero, Project value<sup>RO</sup> will be greater than Project value<sup>DCF</sup>. Also, since real option value is proportional to the underlying uncertainty around future benefits, value of a project with uncertainty will be higher once the embedded real option is taken into account. Hence, Project value<sup>RO</sup>4Project value<sup>DCF</sup>, when $\sigma > 0 ,$ which is in line with the findings in IS literature (Dos Santos, 1991; Kumar, 1996; Benaroch, 2002). We also assume $\Delta t = T /$ n ¼ 1 which is commonly done in the literature.

## Time-inconsistent preferences and utility

The IT manager commits to the project and obtains the embedded growth option with it at time t ¼ 1 with the expansion of the project in mind, that is by exercising the growth option if the condition ubf40 holds at time t ¼ 2. At time t ¼ 2, he will choose to exercise the option if ubf40. At the commitment stage (t ¼ 1), b will be equal to 1 for TC managers<sup>3</sup> as well as for naı¨ve managers<sup>4</sup> (naı¨ves). Although naı¨ves have a tendency of choosing present utility over future utility (with $\beta < 1 )$ they are unaware of their bias and think they will act in a time-consistent manner. Present-bias comes into play only when the rewards come near in the future (O’Donoghue & Rabin, 1999a; Caillaud & Jullien, 2000; Dellavigna & Malmendier, 2004). Hence both types of managers will evaluate and value the project equally. This correct evaluation for the project at the commitment stage by naı¨ves also holds if the growth option has more than one exercise time period.

Proposition 1: An IT manager with time-consistent (TC) preferences and an IT manager with timeinconsistent preferences (naı¨ve) will value an IT project with embedded growth option more than an IT project without a growth option.

Once committed to the project, the manager will decide about option exercise in the next period based on the evaluation of future payoffs at that time against the exercise price of the option. For a growth option with one time period to expire, that is $n = 1$ at $t = T = 2 ,$ the manager has to decide at t ¼ 2 whether to exercise the option or let it expire. He will exercise the option if bub4f else the option will not be exercised. At t ¼ 2, b will still be equal to 1 for TC managers as well as the naı¨ves because the payoff is immediate.

## Proposition 2: IT managers (both TC and naı¨ve) will exercise a growth option with one time period to expiration optimally.

Typically there is more than one opportunity to exercise an option. We depict this real option exercise decision for two points in time in Figure 1, where IT manager decides after evaluating his/her utility at each stage. Figure 1 describes the necessary parameters that determine the utility from exercising a growth option.

Let $V _ { i , j }$ be the value of the option determined in period i if it is exercised in period j. For example, $V _ { 1 , 2 }$ is the value a manager has for the option in period 1 if the option is exercised in period 2. At the commitment stage, t ¼ 1, both TC and naı¨ve will commit to the project as per Proposition 1 as long as project value is positive. Once committed to the project with growth option, the exercise decision will be based on how the project performs overtime. For a growth option with expiration time of two periods (T ¼ 3), the manager has to decide at t ¼ 2 whether to exercise the option today or wait until maturity $t = T = 3$

![](/api/attachments/K6H8EN73/fulltext/images/cd1a24906bfa3537d129f048f75662818543d9f3c3d9a1e19246e2a6312f91f8.jpg)  
Figure 1 Timeline for real growth option with two time periods until expiration.

## Two periods growth option

Real growth options are typically modeled as European options, especially in the IT context (Kumar, 1996, 2002; Benaroch et al, 2006a), which can only be exercised at expiration. However, real options often do not have a fixed exercise time (Benaroch, 2002) and can be exercised any time before expiration. For example, decisions such as an infrastructure investment in a software platform can usually be made any time until a cutoff date. Therefore, viewing a growth option as an American call option helps in capturing the option exercise flexibility.

A key property of an American call option on a nondividend paying asset<sup>5</sup> is that it is never optimal to exercise it before expiration (Cox et al, 1979; Hull, 2008). We utilize this property and assume that a growth option is an American style call option on a non-dividend paying asset. This makes it optimal to exercise the option at the expiration date, that is t\* ¼ 3 for a two-period growth option. The real option value at the project commitment stage to be exercised at t ¼ 3 is

$$
\begin{array}{c} (1 - p) ^ {2} \text {Max} [ 0, d ^ {2} b - f ] + 2 p (1 - p) \\ V _ {1, 3} = \frac {\times \text {Max} [ 0 , (u d b - f) ] p ^ {2} \text {Max} [ 0 , (u ^ {2} b - f) ]}{r 2}. \end{array}\tag{3}
$$

As long as r is positive, $V _ { i , j }$ will always be greater than zero. Practically there is no situation in IT investments where the discount rate is non-positive, hence we will not consider that case. We further make the following assumptions:

\- Benefits from exercising the option (b) exceed the exercise cost $( f ) ,$ that is $b > f .$

\- u is greater than risk-free rate r and d is less than riskfree rate r, that is $d < r < u .$

\- Risk-free rate, future payoffs, option exercise cost, and uncertainty around future payoffs are constant.

Bias for present comes into play when the rewards come near in the future (O’Donoghue & Rabin, 1999a; Caillaud & Jullien, 2000; Dellavigna & Malmendier, 2004) and per Proposition 1 both types of managers will value this project and growth option equally.

## Proposition 3: IT managers (both TC and naı¨ve) will place the same value on an IT project with growth option with two time periods to expiration.

At the first decision point t ¼ 2 the manager can exercise the option and realize immediate payoffs or wait until t ¼ 3. At t ¼ 2, a naı¨ve manager will exhibit presentbias for immediate payoffs and may exercise the option. This will give the real option value evaluated in period 2 and to be exercised in period 3 as:

$$
\begin{array}{c} (1 - p) ^ {2} \text {Max} [ 0, \beta d ^ {2} b - f ] + 2 p (1 - p) \\ V _ {2, 3} = \frac {\times \text {Max} [ 0 , (\beta u d b - f) ] p ^ {2} \text {Max} [ 0 , (\beta u ^ {2} b - f) ]}{r}. \end{array}\tag{4}
$$

Since the benefits are immediate if the option is exercised at period 2, b in Eq. (4) is less than 1 for naı¨ve managers since those benefits are realized in t ¼ 3. For some value of $\beta ,$ the Max function(s) in Eq. (4) will result in zero. As b will impact only the payoffs in next period, a naı¨ve manager may see $V _ { 2 , 3 } < V _ { 2 , 2 }$ and will choose to exercise the option early, that is t ¼ 2. The utility from such decision at t ¼ 2 is

$$
U _ {2} = \operatorname{Max} (V _ {2, 2}, V _ {2, 3}).\tag{5}
$$

Hence the utility is the maximum value from exercising the growth option today or in the next period. If $V _ { 2 , 3 } < V _ { 2 , 2 } ,$ a naı¨ve manager will choose to exercise the option early at t ¼ 2. Proposition 4 establishes the value of $\beta$ for which a naı¨ve manager will exercise the option suboptimally in period 2 instead of period 3. We refer to this value as the critical self-control parameter level and denote it by ${ \bar { \boldsymbol { \beta } } } .$

$$
\text { Proposition } \quad 4: \begin{array}{l} \text { There   is   a } \quad \bar {\beta} = (f (p + r - 2) - b r u) / \\ (b u (2 d (p - 1) - p u), \text { such   that   for   IT } \end{array}
$$

projects with a growth option with two exercise periods:

If $\beta \leqslant \bar { \beta }$ the manager will exercise the options suboptimally in period 2 instead of period 3.

$\beta > \bar { \beta }$ the manager will exercise the option optimally in period 3.

As the expression in Proposition 4 shows, $\hat { \beta }$ is a function of $b , \ f , \ r ,$ and s. A naı¨ve IT manager with a self-control parameter less than or equal to $\hat { \beta }$ will exercise the growth option at $t = 2$ and realize the payoffs sooner than waiting until $t = 3$ to exercise the option and realize its optimal value.

Proof See the Appendix.

## Numerical example and sensitivity analysis

To illustrate the effect of present-bias we use an example with the parameters shown in Table 3.

Without present-bias, $V _ { 1 , 3 }$ is greater than $V _ { 1 , 2 } ,$ , and the optimal value for this growth option will be realized when it is exercised at maturity, that is $t = 3$ . For naı¨ve IT manager, with $\beta$ less than or equal to 0.94, he will exercise the option at $t = 2$ instead of at maturity as shown in Figure 2. The lost value due to early exercise is \$19,829. We conducted some numerical sensitivity analysis using the example to explore the relationship between $\hat { \beta }$ and the option parameters.

Table 3 Parameter values for growth option, Kambil et al (1993)

<table><tr><td>Parameters</td><td>Values</td><td> $\bar{\beta}$ </td><td> $V_{1,2}$ </td><td> $V_{1,3}$  (for  $\beta = 1$ )</td></tr><tr><td>b</td><td>$375,000</td><td>0.94</td><td>$ 90,174</td><td>$ 110,003</td></tr><tr><td>f</td><td>$320,000</td><td></td><td></td><td></td></tr><tr><td>σ</td><td>0.3</td><td></td><td></td><td></td></tr><tr><td>r</td><td>1.05</td><td></td><td></td><td></td></tr></table>

![](/api/attachments/K6H8EN73/fulltext/images/506845ae4df66e666a6ffd81b25cd27ffc8e93ea07779852ac5bf15d3c994571.jpg)  
Figure 2 Sensitivity of growth option value to $\beta .$

For growth options, the overall risk is determined by the volatility of the investment $\sigma .$ As shown in Figure 3, increase in volatility first has little effect on the option value until $\sigma$ reaches 0.1. Above $\sigma$ of 0.1, increase in volatility tends to increase option value, also known as the volatility smile (Hull, 2008). Figure 3 also shows $\hat { \beta }$ as a function of $\sigma .$ As the figure shows, in the range of $\sigma$ where volatility has little effect on option value, that is $0 < \sigma < 0 . 1 , \bar { \vec { \beta } }$ is small. For values of s above 0.1, $\hat { \beta }$ is increasing in $\sigma .$ . This relationship between $\hat { \beta }$ and s is similar to the volatility smile. For $0 < \sigma < 0 . 1 .$ , option value is relatively certain, and $\hat { \beta }$ is smaller. When IT managers know that the additional value they can realize by waiting is certain, they are more likely to wait. Hence under low volatility, a present-biased IT manager is less likely to exercise the option early. For $\sigma { > } 0 . 1$ , the option value starts increasing at a fast rate but it is more uncertain, and, hence, present-biased IT managers are less likely to wait because of the uncertainty. This result is different than some of the findings of empirical studies on growth options (Howell & Ja¨gle, 1997; Lankton & Luft, 2008).

We explore the sensitivity of $\hat { \beta }$ to the risk-free rate in Figure 4 which shows that $\dot { \bar { \beta } }$ is decreasing in the risk-free

![](/api/attachments/K6H8EN73/fulltext/images/af5c481e8f340ddc6f3ac796ff36a6f4fbb007376f343d9e6ef0a56dffd938dd.jpg)  
Figure 3 Sensitivity of critical $\beta$ and option value to the volatility.

![](/api/attachments/K6H8EN73/fulltext/images/6bbb0680ab8df3a2759bbb3cf5df034a773632160d95e7711f48529cc787e18c.jpg)  
Figure 4 Sensitivity of critical $\beta$ to the risk-free discount rate.

![](/api/attachments/K6H8EN73/fulltext/images/239682a6f36e6a284a281996f778f2d0b5935b08ad92e7180a65c8a15b484f4b.jpg)  
Figure 5 Sensitivity of critical $\beta$ to the follow-up cost.

![](/api/attachments/K6H8EN73/fulltext/images/25656c173a67eaefe947227d30e34fc5435ab7edb2409cc458ae142857cd22ba.jpg)  
Figure 6 Sensitivity of critical $\beta$ to the future payoffs.

rate r. Increase in the risk-free rate increases the probability of an increase in the option value $( \mathrm { i . e . } _ { }$ , due to the increase in $p { = } r { - } d / u { - } d )$ . This provides a higher incentive to wait to exercise the option. Therefore, IT managers will not exercise the option today and realize a lower value than they could realize if they wait until maturity. Hence, $\hat { \beta }$ decreases as the risk-free rate increases.

Real option value has an inverse relationship with the follow-up costs $f .$ The sensitivity of $\hat { \beta }$ to $f$ is shown in Figure 5. The figure shows that $\dot { \bar { \boldsymbol { \beta } } }$ increases with f which implies that for higher values of growth option exercise price, present-bias is more likely to cause early exercise. As follow-up cost increases, growth option value will decrease, which makes it more attractive to exercise early since waiting is of little additional value which is offset by present biasness.

Higher future payoffs increase the option value. We explore the sensitivity of $\hat { \beta }$ to values of future payoffs b in Figure 6 which shows that $\hat { \beta }$ is decreasing in b. For higher values of payoffs from exercising a growth option, it is less likely that managers will exercise it early. As future payoffs increase, the growth option value will increase and it is more attractive to wait for the high payoffs.

The results of the sensitivity analysis above can be confirmed for zero risk-free rate, that is $r = 1$ , for which the following expressions can be obtained:

$$
\begin{array}{c} \frac {\partial \bar {\beta}}{\partial \sigma} = \frac {e ^ {\sigma} (b - f)}{b (e ^ {\sigma} + 2) ^ {2}}; \quad \frac {\partial \bar {\beta}}{\partial f} = \frac {1}{b e ^ {\sigma} + 2 b}; \\ \frac {\partial \bar {\beta}}{\partial b} = \frac {f}{b ^ {2} (e ^ {\sigma} + 2)} \end{array} .
$$

These expressions support our numerical sensitivity analysis. The directions and the forms of the relationships hold for each case. $\hat { \beta }$ increases with increases in volatility and future payoffs and decreases with an increase in follow-up costs. Also, $\hat { \beta }$ has a non-linear relationship with volatility and future payoffs whereas it has a linear relationship with follow-up costs.

We further analyze the effects of present-bias on growth options with more than two exercise periods. We kept all the parameters same except for $f = \$ 345,000,$ and five time periods, $n = 5 .$ , to exercise the option and obtained the values of ${ \bar { \boldsymbol { \beta } } } .$ At each option exercise time $t { = } 2 , 3 , 4 , 5 \ ( t { = } 1$ is the project commitment stage), the manager evaluates his utility from exercising the option at $t ,$ or waiting until the optimal exercise time $t = 6$ . Using the binomial option valuation method, we solved $V _ { t , t } = V _ { t , 6 } , t = 2 , 3 , 4 , 5$ for $\beta .$ This allowed us to obtain $\hat { \beta } _ { t }$ for $t = 2 , 3 , 4 , 5$ which is the value of present-bias parameter below which a manager will exercise the option in period $t < 6$ instead of $^ { 6 . }$ . Table 4 gives the $\hat { \beta } _ { t }$ values, along with the cost of early exercise for each period. For a manager with $\beta { \leqslant } 0 . 8 1 6$ , he will opt for exercising at $t = 2 ,$ , given the project perform well over this period (an upward movement in payoffs). If the project did not perform well, he will not exercise the option since the realized value is negative. For a manager with $0 . 8 1 6 \leqslant \beta \leqslant 0 . 8 8 5 ,$ , he will wait for one period and exercise the option at $t = 3$ , given the project keeps performing well (i.e., two upward movements). In case the project does not perform well in $t = 3$ (a downward movement in payoffs), he will wait to exercise. This is shown by a value of $\beta = 0 . 5 1 7$ which is smaller than $\beta = 0 . 8 1 6$ and the manager would have exercised the option at $t = 2$ already. Similar results hold for $t = 4 .$ . For a manager with $0 . 8 8 5 \leqslant \beta \leqslant 0 . 9 0 9$ , he will exercise the option at $t = 4 ,$ given the project keeps performing well $( \mathrm { i . e . }$ , three upward movements). Figure 7 shows the relationship between $\hat { \beta } _ { t }$ for $t = 2 , 3 , 4$ and cost of early exercise when project is performing well throughout (only upward movements). In case the project does no perform well in $t = 4 ,$ , the manager will wait to exercise. At $t = 5 ,$ , a naı¨ve manager will not exercise the growth option at this point and will wait until maturity.

We further analyzed the effects of $\sigma , \ r ,$ and b on $\bar { \boldsymbol { \beta } } _ { t } .$ $\mathrm { ~ A ~ } 3 \times 3 \times 3$ experiment was run with $\sigma = \{ 0 . 3 , 0 . 6 , 0 . 9 \}$ $r = \{ 5 \% , 1 0 \% , 1 5 \% \}$ , and $b = \{ 1 6 5 , 0 0 0 , 1 8 0 , 0 0 0 , 1 9 5$ ,000} for an option with five time periods to exercise, $n = 5 .$ We kept $f = \$ 150,000$ since it is realistic to assume the option will not be exercised if the project did not perform

Table 4 Critical b for each time period on the growth option horizon of $\begin{array} { r } { \pmb { n = 5 } , } \end{array}$ along with cost of early exercise

<table><tr><td>Exercise time</td><td> $Project\ progress^a$ </td><td> $\bar{\beta}_t$ </td><td>exercise decision</td><td>Cost of early exercise</td></tr><tr><td>t=2</td><td>upward</td><td>0.816</td><td>If β≤0.816</td><td>$71,453.50</td></tr><tr><td rowspan="2">t=3</td><td>(upward) $^2$ </td><td>0.885</td><td>If 0.816≤β≤0.885</td><td>$56,717.50</td></tr><tr><td>(upward)(downward)</td><td>0.517</td><td>At maturity</td><td>None</td></tr><tr><td rowspan="3">t=4</td><td>(upward) $^3$ </td><td>0.909</td><td>If 0.885≤β≤0.909</td><td>$31,076</td></tr><tr><td>(upward) $^2$ (downward)</td><td>0.504</td><td>At maturity</td><td>None</td></tr><tr><td>(upward)(downward) $^2$ </td><td>0.504</td><td>At maturity</td><td>None</td></tr><tr><td>t=5</td><td>All</td><td>&gt;1</td><td>At maturity</td><td>None</td></tr></table>

<sup>a</sup>‘upward’ means single upward movement in the value of asset i.e. potential payoffs from the project, and ‘downward’ means single downward movement in the value of asset i.e. potential payoffs from the project.

![](/api/attachments/K6H8EN73/fulltext/images/94c4e26b8c15baf7d44d584c9afc09dfb1e9bbf62940e6e8f8689319abea7806.jpg)  
Figure 7 Critical $\beta$ and cost of early exercise with upward project progress.

Table 5 Average critical b needed to exercise the option in the first three periods with three upward movements

<table><tr><td></td><td> $\bar{\beta}_{2}$  needed to exercise in t=2</td><td> $\bar{\beta}_{3}$  needed to exercise in t=3</td><td> $\bar{\beta}_{4}$  needed to exercise in t=4</td></tr><tr><td colspan="4">σ</td></tr><tr><td>0.3</td><td>0.810</td><td>0.914</td><td>0.925</td></tr><tr><td>0.6</td><td>0.805</td><td>0.903</td><td>0.871</td></tr><tr><td>0.9</td><td>0.817</td><td>0.898</td><td>0.852</td></tr><tr><td colspan="4">r</td></tr><tr><td>0.05</td><td>0.815</td><td>0.850</td><td>0.704</td></tr><tr><td>0.10</td><td>0.809</td><td>0.899</td><td>0.944</td></tr><tr><td>0.15</td><td>0.808</td><td>0.966</td><td>1.000</td></tr><tr><td colspan="4">b-f</td></tr><tr><td>$15,000</td><td>0.789</td><td>0.911</td><td>0.922</td></tr><tr><td>$30,000</td><td>0.818</td><td>0.901</td><td>0.884</td></tr><tr><td>$45,000</td><td>0.825</td><td>0.904</td><td>0.842</td></tr></table>

well in t ¼ 2 (the first movement is downward). The range of b values was selected to ensure equal chance of negative feedback during the course of the project along with positive feedback. We then averaged the $\hat { \beta } _ { t }$ values across each parameter as shown in Table 5. As shown, the direction of the relationship between $\bar { \boldsymbol { \beta } } _ { 2 }$ and s (decreasing then increasing), $\bar { \boldsymbol { \beta } } _ { 2 }$ and r (decreasing), $\bar { \boldsymbol { \beta } } _ { 2 }$ and b (increasing) observed for the two-period option also hold here. The values of $\hat { \beta } _ { t }$ for any period with a down movement (not shown) were smaller than values of $\hat { \beta } _ { t }$ in prior periods where the project performed well. Therefore, there is small likelihood that the option will be exercised in periods with down movement (when project did not perform well). This can be explained by the fact that a downward movement decreases the present value of the option and makes even present-biased managers less likely to exercise it in that period. Also, Table 5 shows that the threshold for $\hat { \beta } _ { t }$ is largest $( \mathrm { i . e . , }$ strong present-bias is needed for early exercise) for options in which payoff is $\mathrm { \ h i g h } ,$ volatility is high, and the discount rate is low. For these options, a present-biased manager is encouraged to be patient due to the large reward. Potential reward may even get larger because of the high volatility, and the low eroding power small discount rate has on future payoffs.

## Discussion

Growth options help in IT infrastructure investments’ economic justification. They also facilitate the realization of IT infrastructure investments’ strategic value by providing a platform to manage IT tools that impact firms’ productivity. For the best utilization of these investments, it is important to make optimal exercise decisions for growth options embedded in them. There is a chance of suboptimal exercise decisions motivated by a manager’s desire to realize the benefits sooner. This suboptimal exercise time may even lead to the whole project having a negative value. Such occurrences are related to some previous findings in the literature. For example, it has been shown that the existence of complementarity among projects aggravates the tendency to rush (Brocas & Carrillo, 2001). Growth options can be considered complimentary projects to infrastructure investments. This complementarity could accentuate present-bias of IT managers in exercising growth options.

We examined two distinct cases of self-awareness among IT managers about their time-preferences, TC and naı¨ve. Our results indicate that at the commitment stage, IT project with growth option is valued equally irrespective of time-preferences of the manager.

This result is consistent with the real options analysis literature (Tiwana et al, 2006).

Present-bias preferences affect the growth option exercise decisions when the real option allows the IT manager multiple exercise decision time periods during project’s life. Having multiple exercise decision time periods is likely in IT infrastructure projects (Kumar, 2004). Also, infrastructure components are sequentially dependent on each other and need to be carefully coordinated. For example, implementation of new system integrators, upgrading software platforms, expanding network platforms etc., are the decisions that can be taken within a specific time period. IT managers with present-bias preferences may exercise these growth options early due to preferring immediate payoffs and their unawareness of such preferences. Business environment may impact the IT manager’s time-preferences as well. In situations like economic recession or market competition, where preference for immediate utility from IT utilization may lead IT managers to make decisions and waiting to invest does not seem feasible (even if it is so). Also if the strategic importance of a technology is high to the firm, it might impact IT managers’ decisions about investment by affecting their time-preferences due to stakeholder’s pressure and to keep the firm competitive.

We found that higher values of payoffs from exercising growth option decrease the likelihood that the manager will exercise the option early. Also, for higher values of growth option exercise price, present-bias was found to more likely cause early exercise of the option. These findings are counter-intuitive. Naı¨ves are supposed to delay immediate cost activities and rush into immediate reward, where for immediate cost activities, a small present-bias can severely affect naı¨ve decision makers (O’Donoghue & Rabin, 1999b). Higher payoffs increase option value and higher exercise costs decrease the option value. Accordingly, IT managers should be tempted to realize the value sooner than later when payoffs are high and should not rush the exercise decisions when costs involved are high. Our results point in the opposite direction. Large net payoffs (high payoffs and low follow-up costs) decrease $\hat { \beta }$ and require the manager to have more present-bias to exercise the option early. One may view this as higher net payoffs tempt the manager to wait while lower net payoffs provide the manager with little incremental value from waiting which are easily discounted by his/her present-bias. This is particularly true when the discount rate is high.

Our experiment demonstrates the importance of project’s progress on its vulnerability to early exercise. Projects progressing well overtime are most vulnerable to early exercise by naı¨ve managers. Such projects could have large immediate payoffs and therefore be vulnerable to present-biasness which penalizes future payoffs. This, in turn, results in unrealized project value due to premature exercise.

## Managerial implications

Managers with present-bias may exercise growth options early. Hence, it is not enough for managers to recognize growth options in a project and intuitively evaluate their value (options thinking). They need to conduct formal option analysis; to be aware of their time-preferences over time; to reevaluate payoffs, costs, and parameters compared with previous period’s estimates. Furthermore, the organization should have incentives in place to mitigate the effects of present-bias. Understanding the effects of time-inconsistent preferences may help in designing better incentives. For example, consider two scenarios. One with no managerial incentives and the other with incentives for periods $t = 2 , 3$ . The incentive amount depends on when the growth option is exercised, that is either at $t = 2$ or at maturity. Let $U _ { t }$ be the instantaneous utility a manager gets in period t from incentives given in that period. For the scenario with no incentives, the manager will have zero utility from incentives. For the incentives scenario, the utility of the manager from incentives in period 2 is

$$
U _ {2} (u _ {2}, u _ {3}) \equiv \operatorname{Max} [ u _ {2}, \beta u _ {3} ].
$$

Suppose the incentive amount is a certain fraction $\prime _ { \nu } \prime$ of the payoff from exercising the growth option $^ { \prime } \boldsymbol { b } _ { t } ^ { \prime }$ at time t. Hence the utility from an incentive at time $t , \ u _ { t }$ will be $u _ { t } = \nu b _ { t } ;$ whereas future incentives are discounted by b.

With the above equation, for a two-time period option, the incentives evaluated in period 2 are $u _ { 2 } = \nu b _ { 2 } ;$ $u _ { 3 } = \beta \nu b _ { 3 } / 1 + r .$ This incentive will motivate the manager to wait until $t = 3$ to exercise the growth option if $\nu b _ { 2 } { \leqslant } \beta \nu b _ { 3 } / 1 + r$ or $b _ { 3 } \ge ( 1 + r ) b _ { 2 } / \beta$ . If this condition does not hold, then offering an incentive scheme in which the manager receives a fraction of $\nu _ { 2 }$ from payoffs if the option is exercised in period 2 or a fraction of $\nu _ { 3 }$ from payoffs if the option is exercised in period 3 can be used. As long as $\nu _ { 3 } / \nu _ { 2 } > ( b _ { 2 } ( 1 + r ) ) / \beta b _ { 3 } ,$ it is utility maximizing for the manager to wait until period 3. This result is in agreement with the convexity of managerial incentives to overcome risk-averse behavior of decision makers (Coles et al, 2006).

Changes to IT governance may help mitigate the effects of present-bias. IT governance procedures will benefit from requiring formal analytical methods to valuate investment decisions. This analysis must rely on inputs from multiple managers and must have a postproject evaluation of performance to identify any existing biases. Incorporating healthy competition with IT governance can hence help control the effects of these biases as well (Brocas & Carrillo, 2001).

Another important implication for IT governance and for managing IT projects is the choice of methods and procedures for controlling risks, especially in IT infrastructure investments. Since there is a risk that a presentbiased manager will exercise an option early, especially if the project is performing well, using a systematic and objective method to update estimates needed for option evaluation is important to reduce risk. A possible way for achieving that is to conduct a ‘net change’ evaluation at each option exercise period. This implies that the evaluation begins with the estimates of option parameters, costs, and payoffs used in the previous period and changes are only made when justifications are provided based on new information. Following such approach would limit the creep of present biasness.

## Limitations and future steps

We have focused on growth options. Growth options are call-like options that are strategic in nature. Our analysis might apply to other operational call-like options such as options to defer investment, scale and switch use, but understanding the exact effects of present bias warrants further investigation. Time-inconsistent preferences may also impact put-like real options such as abandonment option. For abandonment options, the effects of present bias on exercise timing might be different from growth options because abandonment options are geared towards loss minimization in the project instead of profit maximization. Also, the effects may vary depending on the salvage value of the project, ability to put the project to another use and timing of payoffs from this switch in use.

## About the authors

Sarah S. Khan is a doctoral candidate of MIS at the Belk College of Business at the University of North Carolina-Charlotte. She is an active member of PMI and the Association for Information Systems (AIS). Her research interests include IT investments and project management, real options and e-business standards.

Moutaz Khouja is a Professor of Operations Management at the UNC-Charlotte. His research interests are in the areas of supply chain management, inventory management, and pricing. His publications have appeared in many journals including Journal of Management

## References

B I, B S and S R (2004) Prioritizing a portfolio of information technology investment projects. Journal of Management Information Systems 21(2), 33–60.

BENAROCH M (2002) Managing investments in information technology based on real options theory. Journal of Management Information Systems 19(2), 43–84.

BENAROCH M and KAUFFMAN RJ (1999) A case for using real options pricing analysis to evaluate information technology project investments. Information Systems Research 10(1), 70–86.

BENAROCH M and KAUFFMAN RJ (2000) Justifying electronic banking network expansion using real options analysis. MIS Quarterly 24(2), 197–225.

Analyzing the effects of present-bias on these options will give useful insights. It also might explain problems like escalation of commitment in IT projects. Also, we used a discrete time valuation model. Comparison among different real option valuation methods can provide better understanding of the effects of present-bias on option exercise time and realized value.

We have focused on one project with one embedded growth option. Real options may appear in compound form in IT infrastructure projects (Bardhan et al, 2004; Benaroch et al, 2006b), where exercise decision of one real option may lead to enabling further real options in the project. For example, exercising a growth option on an internet platform by a utility firm may enable electronic application and billing for customers. Analytical exploration of the impact of present-bias in such compound options where sequential interdependency exists will give insights into the long-term impacts of such decisions, in terms of timing and realized value. Also, we focused on in-house IT infrastructures. Future studies can analytically explore the impact of present-bias effects on options underlying outsourced IT infrastructures with embedded real options.

Information Systems, Computers and Operations Research, Decision Sciences, Decision Support Systems, and Omega.

Ram L. Kumar is a Professor in Belk College of Business Administration, UNC-Charlotte. He has worked for major multinational corporations such as Fujitsu before entering academics. His current research interests include portfolios of IT investments, Service Science, and Knowledge Management Systems. His research has been published in Communications of the ACM, Computers and Operations Research, Decision Sciences, International Journal of Electronic Commerce, International Journal of Production Research, Journal of MIS, and others.

B M, L Y and R K (2006a) Real options in information technology risk management: an empirical validation of risk-option relation. MIS Quarterly 30(4), 827–864.

BENAROCH M, SHAH S and JEFFERY M (2006b) On the valuation of multistage information technology investments embedding nested real options. Journal of Management Information Systems 23(1), 239–261.

BROCAS I and CARRILLO JD (2001) Rush and procrastination under hyperbolic discounting and interdependent activities. The Journal of Risk and Uncertainty 22(2), 141–164.

BUSBY J and PITTS C (1997) Real options in practice: an exploratory survey of how finance officers deal with flexibility in capital appraisal. Management Accounting Research 8(2), 169–187.

CAILLAUD B and JULLIEN B (2000) Modeling time-inconsistent preferences. European Economic Review 44(4–6), 1116–1124.

CIO (2010) Three ways to reprioritize your IT Infrastructure Investment in 2010. [WWW document] http://www.cio.com/article/561466/Three\_ Ways\_to\_Reprioritize\_Your\_IT\_Infrastructure\_Investments\_in\_2010 (accessed 1 December 2011).

CIO (2011) iPad in the enterprise: three big worries remain. [WWW document] http://www.cio.com/article/678474/iPad\_in\_the\_Enterprise\_ 3\_Big\_Worries\_Remain\_ (accessed 1 December 2011).

COFF R and LAVERTY K (2007) Real options meet organizational theory: coping with path dependencies, agency costs and organizational form. In Real Options Theory (REUER J and TONG T, Eds), JAI Press, United Kingdom.

COLES JL, DANIEL ND and NAVEEN L (2006) Managerial incentives and risktaking. Journal of Financial Economics 79(2), 431–468.

COLIN O and DHALIWAL J (2011) Alignment within the corporate IT unit: an analysis of software testing and development. European Journal of Information Systems 20(1), 48–68.

COLLINS J, KETTER W and GINI M (2010) Flexible decision support in dynamic inter-organizational networks. European Journal of Information Systems 19(4), 48–68.

COX JC, ROSS SA and RUBINSTEIN M (1979) Option pricing: a simplified approach. Journal of Financial Economics 7(3), 229–263.

D Q, K RJ and M ST (2007) Valuing information technology infrastructures: a growth options approach. Information Technology and Management 8(1), 1–17.

DELLAVIGNA S and MALMENDIER U (2004) Contract design and self-control: theory and evidence. The Quarterly Journal of Economics 119(2), 353–402.

DOS SANTOS BL (1991) Justifying investment in new information technologies. Journal of Management Information Systems 7(4), 71–89.

FICHMAN R, KEIL M and TIWANA A (2005) Beyond valuation: real options thinking in IT project management. California Management Review 47(2), 74–96.

FREDERICK S, LOEWENSTEIN G and O’DONOGHUE T (2002) Time discounting and time preference: a critical review. Journal of Economic Literature 40(2), 351–401.

GAL U, LYYTINEN K and YOO Y (2008) The dynamics of IT boundary objects, information infrastructures, and organizational identities: the introduction of 3D modeling technologies into the architecture, engineering, and construction industry. European Journal of Information Systems 17(3), 290–304.

GILPATRIC SM (2008) Present-biased preferences, self-awareness and shirking. Journal of Economic Behavior & Organization 67(3–4), 735–754.

GILPATRIC SM (2009) Slippage in rebate programs and present-biased preferences. Marketing Science 28(2), 229–238.

HILHORST C, RIBBER P, VAN HECK E and SMITS M (2008) Using Dempster-Shafer theory and real options theory to assess competing strategies for implementing IT infrastructures: a case study. Decision Support Systems 46(1), 344–355.

HOWELL SD and Ja¨GLE AJ (1997) Laboratory evidence on how managers intuitively value real growth options. Journal of Business Finance & Accounting 24(7), 915–935.

HULL JC (2008) Options, Futures and Other Derivatives, 7th edn, Pearson Prentice-Hall, New Jersey.

K S and L GL (1986) Market entry timing model for new technologies. Management Sciences 32(2), 194–205.

KAMBIL A, HENDERSON CJ and MOHSENZADEH H (1993) Strategic management of information technology: an options perspective. In Strategic Information Technology Management: Perspectives on Organizational Growth and Competitive Advantage (BANKER RD, KAUFFMAN RJ and MAHMOOD MA, Eds), pp 161–178, Idea Group Publishing, Middletown, PA.

KOGUT B and KULATILAKA N (1994) Options thinking and platform investments: investing in opportunity. California Management Review 36(2), 200–216.

KUMAR RL (1996) A note on project risk and option values of investments in information technologies. Journal of Management Information Systems 13(1), 187–193.

KUMAR RL (1999) Understanding DSS value: an options perspective. Omega 27(30), 295–304.

KUMAR RL (2002) Managing risks in IT projects: an options perspective. Information and Management 40(1), 63–74.

KUMAR RL (2004) A framework for assessing the business value of information technology infrastructure. Journal of Management Information Systems 21(2), 11–32.

LAIBSON D (1997) Golden eggs and hyperbolics discounting. Quarterly Journal of Economics 112(2), 443–477.

LANKTON N and LUFT J (2008) Uncertainty and industry structure effects on managerial intuition about information technology real options. Journal of Management Information Systems 25(2), 203–240.

LOEWENSTEIN G and PRELEC D (1992) Anomalies in intertemporal choice: evidence and an interpretation. Quarterly Journal of Economics 107(2), 573–597.

MARGRABE W (1978) The value of an option to exchange one asset for another. Journal of Finance 33(1), 177–186.

MCDONALD RL (2000) Real options and rules of thumb in capita budgeting. In Project Flexibility, Agency, and Competition (BRENNAN MJ and TRIGEORGIS L, Eds), pp 13–33, Oxford University Press, Oxford.

MCGRATH RG (1997) A real options logic for initiating technology positioning investments. Academy of Management Review 22(4), 974–996.

MCGRATH RG (1999) Falling forward: real options reasoning and entrepreneurial failure. Academy of Management Review 24(1), 13–30.

MILLER KD and SHAPIRA Z (2004) An empirical test of heuristics and biases affecting real option valuation. Strategic Management Journal 25(3), 269–284.

O’DONOGHUE T and RABIN M (1999a) Incentives for procrastinators. The Quarterly Journal of Economics 114(3), 769–816.

O’DONOGHUE T and RABIN M (1999b) Doing it now or later. American Economic Review 89(1), 103–124.

O’DONOGHUE T and RABIN M (2003) Self-awareness and self-control. In Time and Decision: Economic and Psychological Perspectives on Intertemporal Choice (LOEWENSTEIN G, READ D and BAUMEISTER R, Eds), pp 217–243, Russell Sage Foundation, New York, NY.

O’DONOGHUE T and RABIN M (2008) Procrastination on long-term projects. Journal of Economic Behavior & Organization 66(2), 161–175.

PANAYI S and TRIGEORGIS L (1998) Multi-stage real options: the cases of information technology infrastructure and international bank expansion. The Quarterly Review of Economics and Finance 38(3, Part 2), 675–692.

PHELPS E and POLLAK RA (1968) On second-best national saving and gameequilibrium growth. The Review of Economic Studies 35(2), 185–199.

SCHWARTZ ES and ZOZAYA-GOTOSTIZA C (2003) Investment under uncertainty in information technology: acquisition and development projects. Management Science 49(1), 57–70.

TAUDES A (1998) Software growth options. Journal of Management Information Systems 15(1), 165–185.

TAUDES A, FEUERSTEIN M and MILD A (2000) Options analysis of software platform decisions. MIS Quarterly 24(2), 227–243.

THALER R (1981) Some empirical evidence on dynamic inconsistency. Economics Letters 8(3), 201–207.

TIWANA A, KEIL M and FICHMAN RG (2006) Information systems project continuation in escalation situations: a real options model. Decision Sciences 37(3). 357-391

TIWANA A, WANG J, KEIL M and AHLUWALIA P (2007) The bounded rationality bias in managerial valuation of real options: theory and evidence from IT projects. Decision Sciences 38(1), 157–181.

TRIGEORGIS L (1993) The nature of option interactions and the valuation of investments with multiple real options. Journal of Financial and Quantitative Analysis 28(1), 1–20.

TVERSKY A and KAHNEMAN D (1986) Rational choice and the framing of decisions. The Journal of Business 59(4), 251–278.

## Appendix

## Proof of Proposition 4

An IT manager will exercise the option in $t = 2$ instead of $t = 3$ if $V _ { 2 , 2 } \geqslant V _ { 2 , 3 } .$ Therefore to find ${ \bar { \boldsymbol { \beta } } } ,$ we solve $V _ { 2 , 2 } = V _ { 2 , 3 }$ for b<sup>-</sup>. As shown in Figure $\mathrm { A } . 1$ , at $t = 2 ,$ the manager may only exercise the option today if uncertainty has resolved in project’s favor and payoffs looks relatively certain. This will reduce Eq. (2) for $V _ { 2 , 2 }$ to:

$$
V _ {2, 2} = p (u b - f).\tag{A.1}
$$

![](/api/attachments/K6H8EN73/fulltext/images/3f8244adbbee65c32c9aaf3a9aca9076a8a1d7a4dec52f60be4f5f3484420c29.jpg)  
Figure A1 Decision problem of naı¨ve IT manager at $t = 2 .$

In Eq. (A.1), Max terms are eliminated because by $t = 2 ,$ uncertainty is resolved and the option is only feasible to be exercised today if payoffs moved upward. Hence the downward lattice in Figure A.1 will be eliminated. Also $r = 1$ because of the present nature of the exercise decision. Similarly, at t ¼ 2 $t = 2 ,$ , Eq. (4) for $V _ { 2 , 3 }$ will be:

$$
V _ {2, 3} = \frac {2 (1 - p) p (b d u \beta - f) + p ^ {2} (b u ^ {2} \beta - f)}{r}.\tag{A.2}
$$

Again, Max terms are eliminated because by $t = 2 ,$ some uncertainty is resolved if option is exercised in the next period. As the payoffs have already moved upward by u at this point, eliminating the downward lattice of the tree at $t = 2$ indicates the adjusted option value for the decline in future payoffs at that time. For the value of option at $t = 3 ,$ the possible movement of future payoffs further by u and d will stay in the valuation because there is still uncertainty around payoffs value at $t = 3$ . The possibility of future payoffs recovering from downward movement in $t = 3$ is kept in the $V _ { 2 , 3 } .$ Future payoffs value moving down by d in $t = 3$ after moving up by u in $t = 2$ is equal to future payoffs value moving up by u in $t = 3$ after moving down by d in $t = 2 .$ . As the Max function will possibly not give a zero outcome for Max (0, dub-f ) due to our conditions $d < r < u$ and $u b { - } f { > } b { - } f { > } 0 { > } d b { - } f ,$ it was kept in the equation. Also discount rate r will apply for only one time period because when the IT manager at $t = 2 ,$ the payoffs in period $t = 3$ are only one time period away.

Solving (A.1) and (A.2) for $\hat { \beta }$ gives $\bar { \beta } = ( f ( p + r - 2 ) - b r u ) /$ $( b u ( 2 d ( p - 1 ) - p u )$ .
