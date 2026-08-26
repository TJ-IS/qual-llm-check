---
otero_id: 2216
otero_key: "AQTDCEN6"
title: "Customer-centric prioritization of process improvement projects"
authors: "Thomas Kreuzer; Maximilian Röglinger; Lea Rupprecht"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113286"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Customer-centric prioritization of process improvement projects

Thomas Kreuzer<sup>a</sup>, Maximilian Röglinger<sup>b,⁎</sup>, Lea Rupprecht<sup>c</sup>

<sup>a</sup> Project Group Business & Information Systems Engineering of the Fraunhofer FIT, Germany

<sup>b</sup> FIM Research Center, University of Bayreuth, Project Group Business & Information Systems Engineering of the Fraunhofer FIT, Germany

<sup>c</sup> FIM Research Center, University of Augsburg, Germany

## A R T I C L E I N F O

Keywords: Business process management Business process improvement Process decision-making Customer centricity Project portfolio selection Kano model

## A B S T R A C T

Today, customers can conveniently compare products and decide how to interact with companies. With customer centricity becoming an important success factor, companies must drive customer satisfaction not only through excellent products but also through customer-centric processes. As many companies face an abundance of action possibilities, fast-changing customer needs, and scarce resources, guidance regarding the customercentric prioritization of process improvement projects is in high need. As existing approaches predominantly focus on process eficiency, we propose a decision model that accounts for the efects of process improvement on customer centricity in line with justificatory knowledge on value-based process decision-making, project portfolio selection, and the measurement of customer satisfaction. When building the decision model, we adopted the design science paradigm and used multi-criteria decision analysis as well as normative analytical modeling as research methods. We evaluated the model by discussing it with practitioners, by building a software prototype, and by applying it at a German insurance company. Overall, our research extends the prescriptive knowledge on process prioritization and customer process management.

## 1. Introduction

In the digital economy, customers can conveniently compare products and decide how to interact with companies [1]. Against the backdrop of fast-changing customer needs and intense competition, companies must not only design excellent products but also customercentric business processes to sustain corporate success [2–4]. Hence, placing customers at the center of all corporate activities, a strategy also referred to as customer centricity (CC), has evolved into an important success factor for many companies [3]. This has even led to awards such as the Digital World Award for Customer Centricity [5] or the Customer Centricity Retailer of the Year Award [6]. Moreover, ever more companies anchor CC in their corporate strategy, e.g., Amazon strives for becoming the “most customer-centric company” in the world [7].

When implementing CC, customer-company interactions are a key design variable as they drive customer satisfaction [2,3], which in turn afects customer retention and corporate success [8,9]. Customer company interactions are embedded in business processes – specifically in core processes such as service processes or pre-/after-sales processes of manufacturing companies, whose design and improvement is the focus of business process management (BPM) [10]. In line with the relevance of BPM, methods and tools for process design, improvement, and the prioritization of process improvement projects are available [11–13]. Most of them, however, focus on process eficiency [14,15], while neglecting CC [14,16]. For example, subject-oriented BPM focuses on interactions among process participants during process execution [17] but does not guide the design of customer-centric processes. Given the importance of CC [2,3], BPM scholars have called for complementing the eficiency perspective through a CC perspective [18]. As Potts [19] said: “[it] is not about how customers participate in [companies'] processes but about how [companies] participate in the customers' processes”. In response, customer process management (CPM), an emergent strand of BPM research, aims at driving customer satisfaction through customer-centric processes [14,18,20]. Related knowledge, however, is in its infancy. With many companies facing an abundance of action possibilities, fast-changing customer needs, and scarce resources, specifically approaches to the customer-centric prioritization of process improvement projects are missing [21]. Hence, our research question is: How can companies prioritize process improve ment projects to foster CC?

To answer this question, we adopted the design science research (DSR) paradigm [22,23] and used multi-criteria decision analysis as well as normative analytical modeling as research methods [24,25]. As the result of a design search process, we propose an economic decision model as artifact that accounts for the efects of process improvement projects on CC. As for justificatory knowledge, the model adopts ideas from value-based process decision-making, project portfolio selection (PPS), and the measurement of customer satisfaction – specifically ideas from the Kano model [26], i.e., feature types with diferent impact on customer satisfaction and the switching of feature types over time. The decision model aims at assisting process analysts in determining the portfolio of process improvement projects with the highest contribution to the firm value. It extends the prescriptive knowledge on process prioritization and CPM through exaptation [22], $\mathrm { i . e . , }$ , by ofering a novel approach to integrating CC into process decision-making.

Following the DSR reference process [23], this paper is structured as follows: In Section 2, we provide theoretical background on topics that shaped up as relevant justificatory knowledge during the design search process. In Section 3, we outline the research method and evaluation strategy. In Section 4, we first present the problem setting and derive related design objectives (DOs), before we introduce the design speci fication of the decision model. In Section 5, we report on how the evaluated the decision model. We conclude in Section 6 with a sum mary, implications, limitations and avenues for future research.

## 2. Theoretical background

## 2.1. Business process management and decision-making

BPM is the science and practice of overseeing how work is per formed to ensure consistent outcomes and take advantage of improve ment opportunities [28]. It covers the identification, design, implementation, execution, monitoring, and improvement of business processes [14], where process improvement is considered as the most value-adding BPM activity [13,28–30]. Business processes are sets of activities where individuals and technology co-create value in a targetoriented manner [28,31]. Processes are split into core, support, and management processes [28]. Core processes create value for customers who are willing to pay for products and services, support processes enable core processes, and management processes support the planning, monitoring, and controlling of other processes [11].

The literature ofers various methods and tools for process improvement and prioritization [12,14,32]. Basically, these approaches follow the same structure: First, improvement ideas are identified either based on known problems or in response to opportunities. Second, candidates for improvement projects are specified and prioritized, before processes are actually redesigned [33]. To identify improvement ideas, process enhancement patterns, design heuristics, or established creativity techniques are used [34]. Project candidates and related project portfolios are either prioritized through management tools (e.g., heat maps or scoring models) or through formal multi-criteria decision models that assess project efects on process performance while accounting for interactions among projects and processes [33,35].

Assessing the efects of process improvement projects requires quantifying process performance [36], which is a multi-dimensional construct [34,37]. The Devil's Quadrangle, for example, a popular process performance framework, incorporates time, cost, quality, and flexibility as dimensions [34]. Hence, process improvement implies trade-ofs among performance dimensions, i.e., improving one dimension (e.g., quality) may worsen other dimensions (e.g., cost) [34]. Although performance dimensions such as those included in the Devil's Quadrangle primarily focus on process eficiency, quality covers the customer perspective at least indirectly [21,38]. It can be measured in terms of error rates from an eficiency perspective and via customer satisfaction from a customer perspective [21].

To resolve trade-offs among performance dimensions as well as to evaluate processes and improvement projects from an economic perspective, value-based BPM transfers the principles of value orientation (i.e., monetary valuation, risk awareness, and long-term orientation) to process decision-making [39]. Rooted in investments analysis, value orientation is the state-of-the-art of corporate decision-making [40,41], posing that all corporate activities must be aligned with the objective to maximize the long-term firm value. Thus, companies need to quantify the value contribution of assets and decisions [40] – including business processes, improvement projects, and process prioritization decisions. To that end, value-based BPM adopts well-founded valuation functions known from corporate decision-making. The most commonly used function is the risk-adjusted expected net present value (NPV) [42], which we also use in the decision model as a result of the design search process and which we introduce in Section 4.

## 2.2. Customer centricity and satisfaction

Customer satisfaction not only is a component of the quality dimension of process performance but also key for CC in general. CC means placing customers at the center of all corporate activities, including business processes [2,21]. Although an accepted definition is missing, the key characteristic of CC is clear: focus on customer needs to increase customer satisfaction and corporate success [8,21]. CC requires understanding customer needs regarding the features of products and customer-company interactions embedded in business processes. Higher value for customers increases customer satisfaction and loyalty, which drives customer retention and corporate success in the sense of value orientation [8,21,43]. Customer satisfaction is a well-researched construct with numerous measurement approaches [1,44].

Many related approaches build on the confirmation disconfirmation (C/D) paradigm [45], assuming that customers compare expectations with perceived performance. Discrepancies cause satisfaction or dissatisfaction [46]. If expectations are confirmed, customers are satisfied. Disconfirmation emerges if perceived performance and expectations difer. Positive disconfirmation results from over-fulfilled expectations and leads to satisfied or excited customers. Negative disconfirmation occurs, if expectations are under-fulfilled, leaving customers unsatisfied. For instance, SERVQUAL determines service quality based on customer expectations regarding five dimensions [47], while the American Customer Satisfaction Index (ACSI) aims at assessing quality as perceived by customers [48]. As customer satisfaction is commonly described as an aggregation of the perceived performance of product or service features, measurement approaches aim at identifying, categorizing, and analyzing features directly or indirectly [1]. While indirect approaches rely on observation, customers are asked in direct approaches. Based on the categorization of features, customer satisfaction results from the assessment of features' performance, while considering that features may afect satisfaction diferently [21,49]. In this context, the Kano model is a well-known direct approach for categorizing features and measuring customer satisfaction [21,43,45].

In the course of our design search process, we decided to adopt ideas from the Kano model for integrating CC into process prioritization decisions. We chose the Kano model not only because of its popularity in current literature [1,21,50] but also because of its frequent use in industry, e.g., recently in design thinking [51]. Most importantly, the Kano model matched our problem setting and DOs very well. We provide more details regarding this design decision in Section 4.

The Kano model poses that the relation between the degree of fulfillment of specific product features and customer satisfaction depends on the feature in focus and is not necessarily linear [26,52]. It distinguishes between three feature types: basic, performance, and excitement. Fig. 1 illustrates the key characteristics of these types. Traditionally, feature types have been used in product or service design to derive product specifications [53]. Importantly, a one-of feature classification is not suficient, because customers' expectations and perception of features change over time [54]. A new feature that enters the market is initially unknown and does not afect customer satisfaction. After the feature got established, customers begin to feel satisfied by perceiving it. The new feature becomes an excitement requirement. After frequent use, customers start considering the feature as a performance requirement. The more customers get used to the feature, the less it satisfies them, and it finally turns to a basic requirement. To determine a feature's type, the Kano model ofers a survey-based clas sification technique [52].

![](/api/attachments/AQTDCEN6/fulltext/images/38e9e51b106adc80f2f5e39611c5862ff613563703ee4e524f0017a1b6866dcc.jpg)  
Fig. 1. Supposed function course of feature types by Kano et al. [26].

## 2.3. Project portfolio selection and scheduling

As processes are improved through projects and usually more project candidates than resources are available, PPS helps prioritize process improvement projects [14,15]. In general, PPS is the process of comparing project candidates and compiling project portfolios that align with corporate objectives without violating constraints [55,56].

Archer and Ghasemzadeh [57] proposed a PPS process with five stages: The pre-screening stage challenges the strategic fit and mandatory nature of project candidates. Afterwards, the efects of the remaining candidates are assessed in the individual project analysis stage. Candidates that violate pre-defined performance thresholds are dropped in the screening stage. The optimal portfolio selection stage then aims at compiling a project portfolio that best meets the pre-de fined performance indicators while accounting for trade-ofs, domainspecific constraints, and project interactions [32,58]. This includes the scheduling of project candidates. Project interactions are commonly distinguished into intra- and inter-temporal interactions. Intra-temporal interactions occur when analyzing a single planning period. For example, the simultaneous implementation of two projects can be prohibited if both require the same resource. By contrast, inter-temporal interactions afect projects implemented in subsequent periods [56]. This applies to projects that build on other projects (i.e., predecessor/ successor). Furthermore, project interactions can be classified as deterministic or stochastic [59]. Project efects are treated as known or expected values in the case of deterministic interactions or, in the case of stochastic interactions, as random variables. Finally, the portfolio adjustment stage allows for management adjustments.

As this PPS process can be considered as state-of-the-art, we used it in our design search process to position the decision model in the optimal portfolio selection stage and to define relevant input that can be expected at this stage (e.g., project candidates with pre-assessed performance efects).

## 3. Research method

To answer the research question, we adopted the DSR paradigm and propose an economic decision model as artifact [22]. To that end, we followed the DSR reference process [23], which includes six phases: problem identification, definition of DOs, design and development, demonstration, evaluation, and communication. We already identified and justified the research problem in Section 1. In addition, we present the problem setting in detail in Section 4, where we also derive related DOs, i.e., “description[s] of how a new artifact is expected to support solutions” [22]. These DOs are backed by relevant literature and have been validated with the experts involved in the evaluation of the de cision model.

In line with accepted DSR guidelines [23], the design and devel opment phase was a search process where the DOs defined the solution space. Furthermore, we used normative analytical modeling and multicriteria decision analysis as research methods, two methods that have already been used jointly to tackle research problems at the intersection of process-decision making and PPS [30,32,35]. Normative analytical modeling, which relates to decision models as artifact types, addresses decision problems through closed-form mathematical representations producing prescriptive results [25]. Multi-criteria decision analysis enables resolving trade-ofs among conflicting decision criteria [24]. It requires specifying decision criteria, decision variables, and constraints and pointing to non-trivial assumptions [60]. In our case, portfolios of process improvement projects represent decision variables. The potentially conflicting efects of process improvement projects on costs and customer satisfaction are resolved through an aggregation into the riskadjusted expected NPV, which is the de facto standard in corporate decision-making and hence served as decision criterion as well as objective function of the decision model [40,41]. Finally, project interactions and domain-specific constraints are considered. We present the decision model in Section 4, following Cohon's process for multi-criteria decision analysis [60].

In the design search process, we adopted justificatory knowledge from value-based process decision-making, PPS, and customer satisfaction as these areas dispose of knowledge relevant for solving the research problem at hand. As the literature on PPS and value-based process decision-making provides clear guidance (i.e., Archer and Ghasemzadeh's PPS process and objective functions for corporate decision-making, respectively) [40,57], our search process mainly focused on the conceptualization of customers' satisfaction with the process in focus and its mathematical operationalization. As outlined in Section 4, we decided to adopt ideas from the Kano model [21,26], i.e., feature types with diferent impact on customer satisfaction and the switching of feature types over time, as these ideas fit our setting very well. This design decision was approved by the experts involved in the evaluation. From a procedural perspective, the search process was closely inter woven with the decision model's evaluation. For example, we used the prototype early in the search process to experiment with mathematical specifications (e.g., related to the modeling of customer satisfaction and project efects) and the involved industry experts to get real-world feedback. Moreover, we discussed early versions of the model with fellow researchers.

To demonstrate and evaluate our decision model, we followed Sonnenberg and vom Brocke's evaluation framework [27]. This framework comprises four activities (EVAL1 to EVAL4), structured along two dimensions, i.e., ex-ante/ex-post and artificial/naturalistic [61,62]. Ex-ante evaluation is conducted before, ex-post evaluation after artifact instantiation. Naturalistic evaluation requires validating an artifact in real-world settings, whereas artificial evaluation is conducted in laboratory settings. Overlapping with the DSR process, EVAL1 intends to justify the research problem and to derive DOs, while EVAL2 strives for validated design specifications in terms of real-world fidelity and understandability. Hence, we defined the problem setting and derived DOs in Sections 1 and 4. We also conducted semi-structured interviews with industry experts to both the DOs and the decision model [27]. With EVAL3 striving for validated instantiations, we implemented the decision model as a software prototype and conducted tests based on fictitious data. The prototype<sup>1</sup> also helped challenge competing mathematical specifications during the design search process and enables applying the decision model in industry-scale settings [32]. Finally, EVAL4 requires validating artifacts in terms of applicability and usefulness in naturalistic settings, which is why we applied the decision model at a German insurance company. We report on details in Section 5.

## 4. Design specification

We now introduce the design specification of the decision model, which reflects the design search process and the feedback received during the evaluation. Below, we first outline the problem setting (Section 4.1) and derive DOs (Section 4.2). We then specify the objec tive function of the decision model (Section 4.3), which enables com paring portfolios of process improvement projects in terms of their value contribution. before integrating customer satisfaction in line with ideas from the Kano model [26] (Section 4.4). Finally, we introduce relevant projects types and their efects (Section 4.5). Fig. 2 provides an overview of the problem setting, the DOs, and the design specification of the decision model.

## 4.1. Problem setting

Many companies face the following problem setting: In the digital economy, competition is characterized by volatility, uncertainty, complexity, and ambiguity [1,63]. Due to convenient access to information, customers can easily compare products and decide how to interact with companies [64]. Hence, customers have increasing and fast-changing expectations regarding products and their interactions with companies embedded in business processes [3,21]. As for business processes, customers attach diferent importance to distinct process features, which may also change over time [54,63]. Digitalization also ofers companies novel possibilities to satisfy customer needs [65,66], which is why it forces but also enables companies to become customer-centric [2,3]. At the same time, companies strive for long-term company growth [40,41] but, owing to scarce resources, cannot implement all projects relevant for implementing CC in general and customer-centric business processes in particular [32,58]. Against this backdrop, there are two trade-ofs: one between eficiency and customer satisfaction, also known as eficiency/experience trade-of [21], and another between long-term growth and the short-term satisfaction of customer needs. Both trade-ofs require clear-headed decisions regarding the customer-centric prioritization of process improvement projects.

To address this problem setting, our decision model aims at assisting process analysts in determining the portfolio of process improvement projects with the highest contribution to a company's firm value [32], while specifically accounting for CC [21].To that end, the decision model draws from justificatory knowledge on value-based process decision-making, PPS, and the measurement of customer satisfaction. It focuses on a single interaction-intensive core process (e.g., a service process or a pre−/after-sales process of a manufacturing company) where customers are willing to pay for products or services. Importantly, the decision model focuses on that part of customer satisfaction rooted in customer-company interactions embedded in the process. Regarding the process in focus, we assume that multiple project candidates are at hand, which have been checked in early stages of the PPS process [57].

## 4.2. Design objectives

To guide the development and evaluation of the decision model, we derived two DOs from the problem setting [23,27], backed them by literature, and validated them with the experts in the evaluation. Below, we introduce and justify the DOs and outline how they are implemented in the decision model.

DO.1 Process decision-making and PPS: When prioritizing process improvement projects for CC, projects should be assessed individually and in the portfolio context, considering their efects on periodic process performance, project interactions, and domain-specific constraints. Moreover, project portfolios should be assessed in terms of their contribution to the long term firm value.

The problem setting requires selecting and scheduling process improvement projects as well as assessing the efects of selected projects on both periodic process performance and the long-term firm value. In line with the literature on value-based process decision-making, the value contribution of process improvement projects and related project portfolios is assessed in terms of their risk-adjusted expected NPV [32,39].This enables aggregating performance efects from multiple planning periods into a single economic performance measure, which reflects the state-of-the-art in corporate decision-making [32,39–41]. The consideration of multiple planning periods addresses the shortterm/long-term trade-of by accounting for limited resources and utilizing degrees of freedom as some projects may be implemented in later periods. The NPV also caters for positive (e.g., revenues) and negative (e.g., costs) monetary efects and serves as foundation for integrating non-monetary performance indicators (e.g., customer satisfaction). This is important as customer satisfaction drives revenue [21,67,68]. From a PPS perspective, the decision model is located in the optimal portfolio selection stage [57], where projects are analyzed on the portfolio level while accounting for constraints and interactions. The decision model deals with common constraints (e.g., budget restrictions) and project interactions (e.g., predecessor/successor relations) [32]. In line with the eficiency/experience trade-of [21], it considers two project types: CC projects focus on customer needs by improving existing or im plementing new process features, which leads improved customer satisfaction and revenues. Eficiency projects aim at reducing process costs.

DO.2 Process performance and customer satisfaction: When prioritizing process improvement projects for CC, process performance should be treated as a multi-dimensional construct including eficiency- and customercentric dimensions as well as trade-ofs. Moreover, the fulfillment of customer requirements related to process features should be considered, including diferent feature types and changes over time.

The selection and scheduling of process improvement projects requires process analysts to assess changes in process performance. In line with research on process performance [34], we cover eficiency in terms of process costs. Since customer satisfaction is a central goal of CC and a driver of corporate success, we measure process performance regarding quality as perceived by customers in terms of their satisfaction. In the course of an extensive design search process, we decided to draw from ideas related to the Kano model. With customer-company interactions being embedded in business processes driving satisfaction [2,3], customer requirements regarding business processes – specifically interaction-intensive core processes – are as critical to corporate success as are customer requirements regarding product features [18]. Hence, we transfer ideas underlying the Kano model from product de sign to process improvement by mapping customer requirements and requirement types to process features and feature types [21]. Customer satisfaction increases, if customers' expectations regarding process features, measured in terms of the features' degree of fulfillment, are met or exceeded [26]. Thereby, process features are afected by peri odically increasing expectations and may change their type over time.

![](/api/attachments/AQTDCEN6/fulltext/images/a08de9594465920da6c1c56ac20e37f01d792dc541818d94848551e8bbc86c94.jpg)  
Fig. 2. Overview of problem setting, design objectives and design specification.

## 4.3. Objective function

The decision model takes the set K of admissible portfolios of project improvement projects as input, i.e., portfolios that do not violate any project interaction or domain-specific constraint. It values each port folio $k \in K$ based on its risk-adjusted expected NPV and recommends implementing the portfolio with the highest value contribution [30,32]. This leads to the objective function shown in Eq. (1).

$$
k ^ {*} = \underset {k \in K} {\arg \max} N P V _ {k} = \underset {k \in K} {\arg \max} \left[ \sum_ {t = 0} ^ {T} \left[ - \frac {V _ {t}}{(1 + z) ^ {t}} + \frac {R _ {t} (S _ {t}) - C _ {t}}{(1 + z) ^ {t + 1}} \right] \right]\tag{1}
$$

We assume that process improvement projects can be implemented in various periods $t \in T$ of a planning horizon $T \in \mathbb { N } ^ { + }$ , that projects are finished within the same period, and that they take efect at the beginning of the next period [32]. The NPV is calculated as the sum of all discounted expected periodic cash flows using a risk-adjusted interest rate $z \in \mathbb { R } \textrm { + } ^ { 0 }$ [42]. The periodic cash flows consist of investments $V _ { t } \in \mathbb { R } _ { 0 } ^ { + }$ , process revenues $R _ { t } \in \mathbb { R } ^ { + }$ , and process costs $C _ { t } \in \mathbb { R } ^ { + }$ . In the decision model, process costs are assumed to cover fixed and variable costs. Investments are assumed to become manifest at the beginning of a period, while revenues and costs are due at the end of a period [32].

In line with research on customer satisfaction, process revenues depend on customer satisfaction S [67,68].

## 4.4. Integration of customer satisfaction

As justified in Sections 2 and 4.2, we draw from ideas related to the Kano model for modeling customer satisfaction. A high-level perspective would suggest classifying the process in focus, say, as an excitement process [21]. However, as customer requirements may vary throughout the process, it is appropriate to consider sub-processes p ∈ P [65]. Each sub-process is characterized by features i ∈ I relevant for customers. Thereby, the variable $y _  i , $ indicates whether a process feature i is an excitement (E), a performance (P), or a basic (B) feature in period t in line with the Kano model [26].

We define the result of customers' comparison of perceived performance and expectations related to a process feature i, sub-process p, and period t as the degree of fulfillment $f _ { i , \ p , }$ . Specific indicators used to measure perceived performance and customer expectations depend on the feature. For instance, the execution time of a sub-process may require a quantitative scale in minutes, whereas the assessment of customer support calls for qualitative indicators such as employees' kindliness and competence. To enable the comparison of degrees of fulfillment, we standardize their values to [−1; 1], where an over-fulfillment leads to positive values and vice versa [21,69]. If the perceived performance meets expectations, f is 0.

As stated in Section 4.1, customer requirements and hence feature types may change over time. We refer to the period where a process feature changes its type as switching point. Moreover, periodically increasing expectations negatively influences customers' perception of a feature's degree of fulfillment [1]. This implies that – given constant feature performance and increasing customer expectations – a feature's degree of fulfillment decreases periodically. We call this efect decay and use the variable $d _ { i , p , \ t } \in \mathbb { R } _ { 0 } ^ { + }$ to model the decay of feature i in sub process p and period t (Eq. (2)).

$$
f _ {i, p, t} = f _ {i, p, 0} - \sum_ {z = 0} ^ {t} d _ {i, p, z}\tag{2}
$$

As customers may consider the performance of a feature diferently important for distinct sub-processes, the decision model enables assigning weights $w _ { i , \ p , \ t } \in [ 0 ; 1 ]$ . For each feature, the sum of all weights along the process equals 1 per period. The overall performance of a feature i in period t is defined as the aggregated degree of fulfill ment $F _ { i , \ t } , { \mathrm { i . e . } }$ , the weighted average of all $f _ { i , p , }$ <sub>t</sub> along the process (Eq. (3)).

$$
F _ {i, t} = \sum_ {p = 0} ^ {P} f _ {i, p, t} w _ {i, p, t}\tag{3}
$$

Finally, the aggregated degrees of fulfillment $F _ { i , \astrosun }$ must be transformed into customer satisfaction $S _ { t }$ by applying a company-specific transformation function U, which takes the aggregated degrees of fulfillment and the feature types as input $( \operatorname { E q . }$ (4)). The transformation function determines the customer satisfaction $S _ { i , \astrosun }$ <sub>t</sub> per feature and aggregates feature-specific satisfaction values into the overall customer satisfaction per period. Just like the degree of fulfillment, customer satisfaction takes values between [−1; 1] [69].

$$
S _ {t} = U (F _ {i, t}, y _ {i, t})\tag{4}
$$

The Kano model provides general ideas regarding the relationship between the degree of fulfillment and customer satisfaction for diferent feature types. However, due to the variety of application fields, there is no accepted mathematical operationalization [21,69]. Although existing approaches account for the characteristics of distinct feature types listed in Fig. 1, the quantification difers. For instance, Buhl et al. [69] use a polynomial function, whereas Aflerbach and Frank [21] apply an exponential function to model excitement features. Against this backdrop, the decision model includes a declarative overview of relevant characteristics a company-specific transformation function must fulfill. Based on extant research [45,46,52], Table 1 diferentiates between must-have characteristics, which focus on the intended course of the transformation function, and optional characteristics, which can be integrated if useful.

When integrating customer satisfaction in the objective function (Eq. (1)), we use the linear relationship between customer satisfaction and periodic revenues $[ 6 7 , 6 8 ]$ . Hence, we define $R ^ { 0 } \in \mathbb { R } ^ { + }$ as revenues and $\mathbf { \bar { \boldsymbol { s } } } ^ { 0 } \in [ - 1 ; 1 ]$ as the customer satisfaction in the decision point. Moreover, $R ^ { \operatorname* { m a x } } \in \mathbb { R } ^ { + }$ refers to the highest revenues achievable by improving customers' satisfaction with the process in focus. On this foundation, periodic revenues $R _ { t }$ can be determined based on the changes in customer satisfaction $\Delta S _ { t } = S _ { t } - S _ { 0 }$ and the initial revenues $R ^ { 0 } .$ . Mathematically, the linear relationship between customer satisfaction and revenues is a line through $( \bar { \cal S } ^ { 0 } ; { \cal R } ^ { 0 } )$ and $( S ^ { \mathrm { m a x } } ; R ^ { \mathrm { m a x } } )$ with

## Table 1

Must-have and optional characteristics of the transformation function.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Must-have characteristics
Feature Type: Basic

1. Positive $F_{i,t}$ values do not lead to positive $S_{i,t}$
2. Negative $F_{i,t}$ values lead to maximal dissatisfaction possible with strictly decreasing slope
3. Maximal dissatisfaction leads to $S_t = -1$ [26,69,70]
Feature Type: Performance

4. Positive $F_{i,t}$ values lead to positive $S_{i,t}$, following a positive linear function
5. Negative $F_{i,t}$ values lead to negative $S_{i,t}$, following a negative linear function
6. Negative $F_{i,t}$ have a stronger effect then positive $F_{i,t}$
Feature Type: Excitement

7. Negative $F_{i,t}$ values do not lead to negative $S_{i,t}$
8. Positive $F_{i,t}$ values lead to maximal satisfaction possible with strictly increasing slope

Optional characteristics
9. A maximal reachable $S_{i,t}$ as an upper bound
10. A minimal attained $S_{i,t}$ as a lower bound
11. Positive or negative $S_{i,t}$ for neutral $F_{i,t} = 0$
12. Weighting between $S_{i,t}$ for the aggregation of $S_t$
</div>

$s ^ { \mathrm { m a x } } = 1$ , as shown in Eq. (5).

$$
R _ {t} (S _ {t}) = R ^ {0} + \Delta S _ {t} \left(\frac {R ^ {\mathrm{max}} - R ^ {0}}{1 - S ^ {0}}\right)\tag{5}
$$

## 4.5. Project types and performance efects

The decision model covers CC and eficiency projects. Both types can target specific sub-processes, a specific feature across sub-processes, or both. CC projects primarily aim at increasing the degree of fulfillment of distinct features. As a side efect, they may afect costs, $\mathbf { e . g . }$ , by implementing new features that cause administration efort. By contrast, eficiency projects primarily aim at reducing costs, e.g., through process automation. As a side efect, they may afect the degree of fulfillment of distinct features. We assume that the efects of a given project j ∈ J on the degree of fulfillment of feature i in sub-process p and on costs can be expressed as absolute values $e _ { j , \textit { i , p } } \in \mathbb { R }$ and $c _ { j } \in \mathbb { R } ,$ , respectively [32]. To account for efects on the degree of fulfillment, we extend the calculation of $f _ { i , p , }$ from Eq. (2) by integrating $e _ { j , \ i , \ p }$ for all projects completed up to period t − 1 (Eq. (6)). We denote this set of projects as $J _ { t - 1 } { } ^ { \mathbf { u p } _ { - } \ t \mathbf { o } }$ . By definition, the degree of fulfillment can never be $> 1$ or $< - 1$ . Hence, positive and negative project efects may be lost if they would improve or worsen the degree of fulfillment beyond that value range.

$$
f _ {i, p, t} = f _ {i, p, 0} + \sum_ {j \in J _ {t - 1} ^ {\mathrm{up-to}}} e _ {j, i, p} - \sum_ {z = 0} ^ {t} d _ {i, p, z}\tag{6}
$$

The costs $C _ { t }$ in a given period t can be calculated as the sum of the initial process costs $C _ { 0 } \in \mathbb { R } ^ { + }$ and the cost efects $c _ { j }$ of all projects completed up to period $t \mathrm { ~ - ~ } 1 \mathrm { ~ } ( \mathrm { E q . ~ } ( 7 ) )$ . Finally, all projects cause investments $\nu _ { j }$ in the period for which they are scheduled. The investments $V _ { t }$ in a given period t are calculated as the sum of investments for all projects scheduled for that period (Eq. (8)). We denote this set of projects as J .

$$
C _ {t} = C _ {0} + \sum_ {j \in J _ {t - 1} ^ {\mathrm{up-to}}} c _ {j}
$$

$$
V _ {t} = \sum_ {j \in J _ {t}} v _ {j}\tag{7}
$$

(8)

## 5. Evaluation

## 5.1. Ex-ante evaluation: design validation and expert interviews

EVAL2 strives for validated design specifications in terms of real world fidelity and understandability. To that end, we conducted semistructured interviews with industry experts [62,71], which also provided input for refining the DOs and the model. Each interview took about one hour and was attended as well as recorded by one researcher. To recruit experts, we used the following criteria: Experts had to have at least 5 years of working experience in a leading position and to be qualified in BPM, CPM, or PPS. We also aimed to cover various professional and corporate contexts through the experts' background and the companies' size and industry. In total, we recruited six experts (Table 2). Below, we report on the interviews structured along the DOs.

DO.1 Process decision-making and PPS: The experts agreed with our approach to compare project portfolios based on their NPV, as it is widely used in corporate decision-making. Although it is hard to estimate the NPV accurately, they confirmed that it serves as a benchmark for comparing decision alternatives. They approved that the linear relationship between customer satisfaction and revenues, which has been found in the literature, holds for their companies. Likewise, the experts highlighted the importance of considering project interactions and constraints. However, they criticized that the decision model did not account for all facets of PPS occurring in industry settings, e.g., the implementation of projects may take longer than one period. Such circumstances can be addressed via workarounds, e.g., longer projects can be split and connected through predecessor/successor interactions. The experts considered the distinction between CC and eficiency projects as appropriate, although both types can have cost and customer efects. They also confirmed that this distinction enables thinking about how to address the eficiency/experience trade-of as well as the tradeof between long-term growth and the short-term satisfaction of fast changing customer needs.

Table 2  
Overview of the interview partners and their companies.

<table><tr><td>Job Title</td><td>Work Experience in Years</td><td>Academic Background</td><td>Industry</td><td>Employees (as of year)</td><td>Annual Revenue (as of year)</td></tr><tr><td>Head of credit and contract management</td><td>&gt;10</td><td>Finance and Information Management</td><td>Product – Brewery group</td><td>8000 (2018)</td><td>2.2 bn. EUR (2018)</td></tr><tr><td>Head of Innovation</td><td>&gt;5</td><td>Business Administration</td><td>Service – Financial Service Provider</td><td>&gt;6700 (2018)</td><td>8.0 bn. EUR (2018)</td></tr><tr><td>Executive Assistant</td><td>&gt;5</td><td>Business Administration</td><td>Service – Financial Service Provider</td><td>140,000 (2018)</td><td>130.6 bn. EUR (2018)</td></tr><tr><td>Chief Operating Officer</td><td>&gt;5</td><td>Business Administration</td><td>Service – Software and Service Provider</td><td>&lt;50 (2018)</td><td>n.a.</td></tr><tr><td>IOT Project Manager</td><td>&gt;5</td><td>Business Administration and Information Systems</td><td>Product – Tools and Manufacturing</td><td>29,004 (2018)</td><td>Approx. 6200 bn. EUR (2018)</td></tr><tr><td>Senior Consultant – Project management</td><td>&gt;10</td><td>Business Administration</td><td>Service – Financial consulting</td><td>&lt;50 (2018)</td><td>n.a.</td></tr></table>

DO.2 Process performance and customer satisfaction: The experts supported the idea of a decision model based on the Kano model, as it is widely used in practice. They acknowledged switching points as an appropriate way to consider the life cycle of features. However, the initial version of the decision model only included one overall switching. As most experts asked for feature-specific switching points, we extended the decision model. The experts also outlined that the decision model entails high data collection efort and that not all companies may be able to collect the input. As they specifically referred to the degree of fulfillment and weights for sub-processes, we adapted the decision model such that an application based on aggregated parameters is possible.

Overall. the experts confirmed that the problem setting outlined in Section 4.1 is relevant and that process improvement from a CC perspective is a key challenge. They also considered the decision model as viable for tackling this challenge. Before implementing the decision model as a prototype and applying it at a German insurance company, we incorporated the experts' feedback. We report on findings regarding the evaluation criteria in Section 5.3 and revert to limitations in Section 6.

## 5.2. Ex-post evaluation: real-world application

## 5.2.1. General setting

To validate the applicability and usefulness of the decision model in a naturalistic setting (EVAL4), we applied the prototype<sup>2</sup> at a German insurance company (INSURANCE). Due to confidentiality, we had to anonymize and slightly modify the case data. INSURANCE is a personal and property insurer and one of the largest insurers in Germany, employing > 6700 people and generating revenues of > 8 MEUR in 2018. INSURANCE pursues a multi-channel strategy that enables maintaining an extensive distribution network in its target regions and adequate insurance protection. Due to intensive competition, CC is of utmost relevance for INSURANCE and a key paradigm of process design. Hence, INSURANCE was an ideal company for evaluating the decision model. The case is based on a real decision problem at INSURANCE, which matched the problem setting of our decision model. It related to INSURANCE's Insurance Advice Process, for which six improvement project candidates had already been identified. When applying our model, INSURANCE'S Head of Innovation, who is responsible for process innovation and customer interaction, acted as our key contact point and informant. However, he involved experts from other organizational units whenever necessary, especially for estimating and collecting input data.

The Insurance Advice Process consists of five sub-processes (Fig. 3): Data Entry, Quick Check, Back-Ofice Analysis, Customer Ofer, and Consulting and Conclusion. It mirrors a strategic collaboration between INSURANCE and another financial service provider (SERVICE) that manages financial afairs like banking accounts and investments for its customers but does not ofer insurances. The Insurance Advice Process ofers a free insurance check for all customers of SERVICE.

Based on INSURANCE's in-depth insights from previous improvement endeavors, customer surveys conducted, and input from custome agents, seven features need to be considered relevant for customers. These include one basic feature (Data Privacy), five performance features (Process Flexibility, Customer Efort, Execution Time, Employee Competence, and Transparency) as well as one excitement feature (Innovation Factor). Together with the accounting department, the informant provided us with process-related cash flows and planning parameters taken from INSURANCE's decision-making policy (Table 3).

In the case at hand, INSURANCE assumed the maximum revenues to be significantly higher than current revenues. The informant also stated that the process currently met customer expectations almost exactly and that, accordingly, customer satisfaction was acceptable but not excellent. Furthermore, based on the results of customer surveys and customer agents' appraisals, the initial degrees of fulfillment and weights per process feature and sub-process could be identified (Table 4).

Following INSURANCE's forecasts regarding customer expectations, decays and switching points will occur for some features during the planning horizon. The features' degrees of fulfillment are assumed to decrease as shown in Table 5. Moreover, the decay per feature was assumed to be constant across all sub-processes. Moreover, Process Flexibility was assumed to switch from a performance to a basic feature in period 3, as customers start taking it for granted to interact anywhere and anytime with INSURANCE. The same applies to Transparency in period 5 due to an increased industry standard regarding fast and easy access to personal data and ongoing transactions via mobile app.

To determine customer satisfaction, we drew on Buhl et al. [69], using a transformation function that implements all must-have characteristics from Table 1. This results in the following parameters: For basic features, customer satisfaction is not afected, if customer expectations are exceeded $( \mathrm { i . e . , }$ , over-fulfillment) but falls rapidly to the minimum $( S _ { i , \textit { t } } = \textit { - } 1 )$ ) for slight under-fulfillment $( F _ { i , \textit { t } } \leq \ - \ 0 . 3 )$ Dissatisfaction with basic features leads to overall dissatisfied custo mers $( S _ { t } = { \mathrm { ~ - ~ } } 1 )$ [26,46]. As for performance features, satisfaction i linearly connected with over-fulfillment and under-fulfillment with a maximum of $S _ { i , \textit { t } } = \ : 0 . 7$ and a minimum of $S _ { i , \ t } = \ - \ 0 . 8 .$ . All performance features are weighted equally strong. For excitement features, customer satisfaction follows a continuously growing slope where overfulfillment leads to the maximum satisfaction $( S _ { i , \textit { t } } = \ 1 )$ and under fulfillment does not afect satisfaction.

![](/api/attachments/AQTDCEN6/fulltext/images/e206abf6f0342ceb702fc99d26407da8605d5e7ec5aabf871d95d865013cb56b.jpg)  
Fig. 3. Insurance advice process.

Table 3  
Process-related data.

<table><tr><td>Current revenues  $R^{0}$ </td><td>Current costs  $C_{0}$ </td><td>Maximum revenues  $R^{\text{Max}}$ </td><td>Current satisfaction  $S_{0}$ </td><td>Risk-adjusted interest rate z</td><td>Planning horizon T</td></tr><tr><td>75.00 MEUR</td><td>70.35 MEUR</td><td>87.00 MEUR</td><td>-0.04</td><td>3%</td><td>6</td></tr></table>

Table 4  
Matrix of the initial degrees of fulfillment and weights for all process features.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="10">Sub-process p</td><td rowspan="2"></td></tr><tr><td colspan="2">Data entry</td><td colspan="2">Quick check</td><td colspan="2">Back-office analysis</td><td colspan="2">Customer offer</td><td colspan="2">Consulting &amp; conclusion</td></tr><tr><td>Feature i</td><td> $y_{i,0}$ </td><td> $f_{i,p,0}$ </td><td> $w_{i,p,0}$ </td><td> $f_{i,p,0}$ </td><td> $w_{i,p,0}$ </td><td> $f_{i,p,0}$ </td><td> $w_{i,p,0}$ </td><td> $f_{i,p,0}$ </td><td> $w_{i,p,0}$ </td><td> $f_{i,p,0}$ </td><td> $w_{i,p,0}$ </td><td> $F_{i,0}$ </td></tr><tr><td>Data privacy</td><td>B</td><td>0.50</td><td>0.20</td><td>0.50</td><td>0.20</td><td>1</td><td>0.20</td><td>1</td><td>0.20</td><td>1</td><td>0.20</td><td>0.80</td></tr><tr><td>Process flexibility</td><td>P</td><td>-0.30</td><td>0.25</td><td>-0.20</td><td>0.25</td><td>0</td><td>0</td><td>0</td><td>0.25</td><td>0</td><td>0.25</td><td>-0.13</td></tr><tr><td>Customer effort</td><td>P</td><td>0.20</td><td>0.25</td><td>0</td><td>0.25</td><td>0</td><td>0</td><td>-0.20</td><td>0.25</td><td>-0.30</td><td>0.25</td><td>-0.08</td></tr><tr><td>Execution time</td><td>P</td><td>0</td><td>0</td><td>0.30</td><td>0.25</td><td>-0.50</td><td>0.25</td><td>-0.30</td><td>0.25</td><td>0</td><td>0.25</td><td>-0.13</td></tr><tr><td>Employee competence</td><td>P</td><td>0.20</td><td>0.10</td><td>0.30</td><td>0.30</td><td>0</td><td>0</td><td>0.30</td><td>0.30</td><td>0.30</td><td>0.30</td><td>0.29</td></tr><tr><td>Transparency</td><td>P</td><td>0</td><td>0.20</td><td>-0.30</td><td>0.20</td><td>0</td><td>0.20</td><td>0</td><td>0.20</td><td>0</td><td>0.20</td><td>-0.10</td></tr><tr><td>Innovation factor</td><td>E</td><td>0</td><td>0.20</td><td>0</td><td>0.20</td><td>0</td><td>0.20</td><td>0</td><td>0.20</td><td>0</td><td>0.20</td><td>0</td></tr></table>

Table 5  
Decrease of the degrees of fulfillment.

<table><tr><td> $d_{i,p,t}$ </td><td colspan="6">Period t</td></tr><tr><td>Feature i</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Data privacy</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td></tr><tr><td>Process flexibility</td><td>0.15</td><td>0.15</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Customer effort</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td></tr><tr><td>Execution time</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td></tr><tr><td>Employee competence</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td></tr><tr><td>Transparency</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0.05</td><td>0</td><td>0</td></tr><tr><td>Innovation factor</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td><td>0.02</td></tr></table>

## 5.2.2. Analyzing the project candidates

As already mentioned, six project candidates had already been identified. Together with the informant, we classified them as CC or eficiency projects, which led to four CC projects and two eficiency projects focusing on improving the sub-process Back-Ofice Analysis. Project descriptions, efects, and constraints are shown in Table 6. Investment and cost efects are based on INSURANCE's internal estimations.

Owing to the expected increase of customer expectations, the informant stated that the main target of the projects in focus is to compensate for decreases in customer satisfaction. INSURANCE aims at keeping the current level of customer satisfaction. It seemed unrealistic that the projects lead to strong improvements of customer satisfaction. The informant derived the project efects based on the features' current degrees of fulfillment in two steps. First, he evaluated which projects afect which process features for which sub-processes based on his insights into the process and expectations of other experts working at INSURACNE. Second, the informant estimated efect intensities, considering current and future degrees of fulfillment, and the projects' ability to compensate for increasing customer expectations. In case a project can compensate for increasing customer expectations, the overall efect was assumed to be positive, otherwise negative. The resulting estimations are shown in Table 7.

## 5.2.3. Selecting the optimal project portfolio

According to the INSURANCE's decision-making policy, projects could only be implemented in the first four periods to ensure that their efects materialize within the planning horizon. We also restricted the implementation to two projects per period as no more project managers were available. After that, we determined the NPV of all admissible project portfolios. To illustrate the range of the NPV in the case at hand, Table 8 shows the values for the optimal and the worst project portfolio as well as for the project portfolio where the only mandatory project is implemented. Fig. 4 illustrates the associated development of customer satisfaction over time.

Table 6  
Input parameter of the process improvement projects.

<table><tr><td>Project</td><td>Description</td><td>Type</td><td>Investment</td><td>Cost effect</td></tr><tr><td>P1</td><td>Implementation of optical character recognition (OCR)Facilitates the data entry of third-party insurance policies and leads to a considerable time saving during the execution of the sub-process  $p_1$ .</td><td>EFF</td><td>0.55 MEUR</td><td>-0.35 MEUR</td></tr><tr><td>P2</td><td>Legacy tariff database in the back-officeOffers employees easy access to detailed information about third-party insurance policies. Additionally, the offering is tailored more individually to the customers&#x27; needs.</td><td>EFF</td><td>0.30 MEUR</td><td>0.20 MEUR</td></tr><tr><td>P3</td><td>Legacy tariff database for the Quick CheckFollow-up project for P2. Enables to use the legacy tariff database in the sub-process Quick Check. This improves several process features from a customer&#x27;s point of view and leads to a better and faster initial evaluation of customer needs.Restriction: P3 can only be performed if P2 was implemented in a previous period.</td><td>CC</td><td>0.70 MEUR</td><td>0.10 MEUR</td></tr><tr><td>P4</td><td>End customer accessSpecifically targets Transparency and improves customer access to process-related data. This enables customer to gain more insights into the reason behind the received offering and ongoing processes but at the same time makes them feel less secure regarding privacy.</td><td>CC</td><td>1.50 MEUR</td><td>0.40 MEUR</td></tr><tr><td>P5</td><td>Improvement of mobile applicationImproves and extends the functionalities of INSURANCE&#x27;s customer mobile application, especially with respect to Process Flexibility.</td><td>CC</td><td>0.70 MEUR</td><td>0.20 MEUR</td></tr><tr><td>P6</td><td>Implementation of PSD2 requirementsImplements mandatory PSD2 requirements and enables customers to share financial data from or with third-party companies more easily. This leads to a reduction of effort within the sub-process Data Entry.Restriction: P6 is mandatory and must be completed in period 3.</td><td>CC</td><td>0.50 MEUR</td><td>0.14 MEUR</td></tr></table>

In the optimal project portfolio, all projects are implemented: Period 1 comprises the projects P1 and P4. P1 is an eficiency project that considerably reduces costs and improves the performance feature Execution Time. The earlier P1 is implemented, the more costs can be saved during the planning horizon. P4 targets the improvement of the performance features Process Flexibility and Transparency. These features become basic features in period 3 and 5. Furthermore, P4 has a positive efect on the excitement feature Innovation Factor. Period 2 comprises the projects P2 and P5. P2 implies the integration of a legacy tarif database in the back-ofice, positively afecting the performance features Execution Time and Employees Competence but also strongly increasing periodic costs. As P2 is a mandatory predecessor of project P3 (Table 6), the early implementation of P2 indicates that the benefits of P3 will exceed the negative efects of P2. Project P5 targets INSURANCE's mobile application and positively afects the performance features Process Flexibility, Customer Efort, and Execution Time as well as the excitement feature Innovation Factor. Additionally, there is a slightly negative efect on the basic feature Data Privacy, which however is exceeded by the positive efects. Specifically, the improvement of Process Flexibility is important as it becomes a basic feature in the next period. In period 3, projects P3 and P6 should be implemented. P3 enables using the legacy tarif database also during the Quick Check, which improves the performance features Customer

Table 7  
Project efects on the features' degrees of fulfillment.

<table><tr><td rowspan="2"></td><td colspan="10">Sub-process p</td></tr><tr><td colspan="2">Data entry</td><td colspan="2">Quick check</td><td colspan="2">Back-office analysis</td><td colspan="2">Customer offer</td><td colspan="2">Consulting &amp; conclusion</td></tr><tr><td>Feature i</td><td colspan="2"> $e_{j,i,p}$ </td><td colspan="2"> $e_{j,i,p}$ </td><td colspan="2"> $e_{j,i,p}$ </td><td colspan="2"> $e_{j,i,p}$ </td><td colspan="2"> $e_{j,i,p}$ </td></tr><tr><td rowspan="3">Privacy</td><td>P1: -</td><td>P4: -0.10</td><td>P1: -</td><td>P4: -0.10</td><td>P1: -</td><td>P4: -0.10</td><td>P1: -</td><td>P4: -0.10</td><td>P1: -</td><td>P4: -</td></tr><tr><td>P2: -</td><td>P5: -0.10</td><td>P2: -</td><td>P5: -0.10</td><td>P2: -</td><td>P5: -0.10</td><td>P2: -</td><td>P5: -0.10</td><td>P2: -</td><td>P5: -</td></tr><tr><td>P3: -</td><td>P6: -0.20</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td></tr><tr><td rowspan="3">Process Flexibility</td><td>P1: -</td><td>P4: 0.30</td><td>P1: -</td><td>P4: 0.20</td><td>P1: -</td><td>P4: 0.20</td><td>P1: -</td><td>P4: 0.20</td><td>P1: -</td><td>P4: -</td></tr><tr><td>P2: -</td><td>P5: 0.20</td><td>P2: -</td><td>P5: 0.20</td><td>P2: -</td><td>P5: 0.20</td><td>P2: -</td><td>P5: 0.20</td><td>P2: -</td><td>P5: -</td></tr><tr><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td></tr><tr><td rowspan="3">Customer Effort</td><td>P1: -</td><td>P4: -</td><td>P1: -</td><td>P4: -</td><td>P1: -</td><td>P4: -</td><td>P1: -</td><td>P4: -</td><td>P1: -</td><td>P4: -</td></tr><tr><td>P2: -</td><td>P5: 0.05</td><td>P2: -</td><td>P5: 0.05</td><td>P2: -</td><td>P5: 0.05</td><td>P2: -</td><td>P5: 0.05</td><td>P2: -</td><td>P5: -</td></tr><tr><td>P3: -</td><td>P6: 0.20</td><td>P3: 0.30</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td></tr><tr><td rowspan="3">Execution Time</td><td>P1: -</td><td>P4: -</td><td>P1: -</td><td>P4: 0.20</td><td>P1: 0.40</td><td>P4: 0.20</td><td>P1: -</td><td>P4: 0.20</td><td>P1: -</td><td>P4: -</td></tr><tr><td>P2: -</td><td>P5: -</td><td>P2: -</td><td>P5: 0.10</td><td>P2: 0.60</td><td>P5: 0.10</td><td>P2: -</td><td>P5: 0.10</td><td>P2: -</td><td>P5: -</td></tr><tr><td>P3: -</td><td>P6: 0.20</td><td>P3: 0.40</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td></tr><tr><td rowspan="3">Employee Competence</td><td>P1: -</td><td>P4: -</td><td>P1: -</td><td>P4: -</td><td>P1: -</td><td>P4: -</td><td>P1: -</td><td>P4: -</td><td>P1: -</td><td>P4: -</td></tr><tr><td>P2: -</td><td>P5: -</td><td>P2: -</td><td>P5: -</td><td>P2: -</td><td>P5: -</td><td>P2: 0.40</td><td>P5: -</td><td>P2: -</td><td>P5: -</td></tr><tr><td>P3: -</td><td>P6: -</td><td>P3: 0.30</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td></tr><tr><td rowspan="3">Transparency</td><td>P1: -</td><td>P4: 0.40</td><td>P1: -</td><td>P4: 0.40</td><td>P1: -</td><td>P4: 0.40</td><td>P1: -</td><td>P4: 0.40</td><td>P1: -</td><td>P4: -</td></tr><tr><td>P2: -</td><td>P5: -</td><td>P2: -</td><td>P5: -</td><td>P2: -</td><td>P5: -</td><td>P2: -</td><td>P5: -</td><td>P2: -</td><td>P5: -</td></tr><tr><td>P3: -</td><td>P6: -</td><td>P3: 0.25</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td></tr><tr><td rowspan="3">Innovation Factor</td><td>P1: -</td><td>P4: 0.40</td><td>P1: -</td><td>P4: 0.40</td><td>P1: 0.40</td><td>P4: 0.50</td><td>P1: -</td><td>P4: 0.40</td><td>P1: -</td><td>P4: -</td></tr><tr><td>P2: -</td><td>P5: 0.25</td><td>P2: -</td><td>P5: 0.10</td><td>P2: -</td><td>P5: 0.10</td><td>P2: -</td><td>P5: 0.10</td><td>P2: -</td><td>P5: -</td></tr><tr><td>P3: -</td><td>P6: 0.20</td><td>P3: 0.50</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td><td>P3: -</td><td>P6: -</td></tr></table>

Table 8  
Optimal and worst project portfolio

<table><tr><td>Portfolio</td><td>Project implementation sequence</td><td>Net present value</td></tr><tr><td>Optimal project portfolio</td><td>({P1, P4}, {P2, P5}, {P3, P6}, {}</td><td>31.8 MEUR</td></tr><tr><td>Mandatory-only project portfolio</td><td>({}, {}, {P6}, {}</td><td>-12.7 MEUR</td></tr><tr><td>Worst project portfolio</td><td>({P6}, {P2}, {P3}, {}</td><td>-14.7 MEUR</td></tr></table>

Efort, Execution Time, Employee Competence, and Transparency as well as the excitement feature Innovation Factor. P6 is mandatory and must be implemented until period 4 (Table 6). Thus, it is included in the optimal portfolio, although it negatively afects the NPV. No project is scheduled for period 4 as all available projects have already been implemented.

From the informant's and all other involved experts' point of view, the results are comprehensible and comply with INSURANCE's considerations of implementing all projects. As shown in Fig. 4, the optimal project portfolio helps INSURANCE achieve its goal of slightly increasing customer satisfaction regarding the Insurance Advice Process. The findings of the worst portfolio comply with the informant's assessment that fulfilling basic features is key and should be accomplished before investing in performance and excitement features in the case at hand. Finally, the mandatory-only portfolio shows that INSURANCE must invest in order to only maintain the current level of customer satisfaction and that implementing only mandatory projects even destroys firm value in terms of the NPV.

## 5.2.4. Robustness analysis

Having selected the optimal project portfolio, we performed a robustness analysis to account for potential estimation errors. This step complies with the PPS process that recommends conducting robustness analyses in the portfolio adjustment stage [13]. For the robustness analysis, we agreed with the informant to focus on the fulfillment matrix (Table 4), which was mainly based on expert estimations at INSURANCE. We examined increases and decreases of the initial ful fillment values up to an absolute deviation of +/ − 0.5.In detail, we modified all initial fulfillment values by 0.01 units per run, repeated the selection of the optimal project portfolio for each modification, and analyzed the decision model's behavior.

In case of increased initial fulfillment values, the optimal project portfolio did not change and the NPV increased, as the projects entail higher degrees of fulfillment and customer satisfaction over time. However, in case of decreased initial fulfillment values, we found a diferent efect. Fig. 5 shows the NPV related to the decrease of the initial degrees of fulfillment. It is important to note that each run of the robustness analysis is based on diferent initial values and, thus, the optimal project portfolios need not be identical. An analysis of the optimal project portfolios showed that the optimal portfolio changes exactly once in the case at hand. We refer to both portfolios as optimal portfolio A and optimal portfolio B. Portfolio A equals the optimal portfolio that results from the initial degrees of fulfillment and from all increased values. Portfolio B recommends implementing project P1 in period 1 and P6 in period 3, i.e., ({P1},{},{P6},{}). At the same time, the optimal NPV significantly drops from about 27 MEUR to −0.3 MEUR. As the switch from portfolio A to portfolio B happens at a de crease of −0.2 – compared to the initial degrees of fulfillment as presented in Table 4 – we analyzed this point in more detail.

For portfolio A, the NPV continuously declines for decreases in the initial degrees of fulfillment from 0 to −0.2. Subsequently, the optimal portfolio changes from portfolio A to portfolio B, including a significant drop in NPV. For portfolio B, the NPV increases again for further de creases in the initial degrees of fulfillment by −0.2 to −0.5. This efect is rooted in the interplay of feature fulfillments and customer expectations. For lower initial degrees of fulfillment, projects can only realize lower positive efects on customer satisfaction and the NPV. At a certain point, the initial degrees of fulfillment are so low that the projects can no longer compensate for increasing customer expectations and related negative efects on customer satisfaction. Specifically, an under-fulfillment of basic features leads to dissatisfied customers, which cannot be compensated by performance or excitement features – no matter how extensively they are fulfilled [26,70]. Consequently, the decision model returns a diferent optimal project portfolio, i.e., portfolio B in the case at hand, which does not focus on improving revenues through customer satisfaction but on reducing process costs. Hence, the switch of the optimal project portfolio reflects a switch from a revenueto a cost-driven process improvement strategy. Accordingly, portfolio B includes the eficiency project P1 in period 1, as it reduces process costs, and the mandatory project P6 in period 3 as it is mandatory. All other projects do not improve customer satisfaction strongly enough but would negatively afect the NPV through the required investments and their increasing efect on process costs.

![](/api/attachments/AQTDCEN6/fulltext/images/8a48c5a021fb2eb4fe0807b18d54c323df09bde1755fe196f16705b3eee9cacb.jpg)  
Fig. 4. Customer satisfaction for optimal, worst, and mandatory-only project portfolio.

![](/api/attachments/AQTDCEN6/fulltext/images/288ab9a7de2c5cfdd4c91f1f4db443272e0292de944edfc4624f64d0d062b5f8.jpg)  
Fig. 5. Robustness analysis for a step-wise decrease of the initial fulfillment values.

We also found that the NPV of portfolio B increases when further decreasing the initial fulfillment values. This efect is rooted in the calculation of the process revenues. The impact of customer satisfaction on process revenues in a specific period not only depends on customer satisfaction in that period but also on the initial customer satisfaction (Eq. (5)). Hence, lower initial customer satisfaction only allows for a lower impact of customer satisfaction on revenues. Consequently, the relative impact of cost (savings) is stronger (Eq. (1)). Although the decision model still yields interpretable results, this efect shows that the model specifically fits processes for which customer satisfaction is a relevant value driver. If a process hardly depends on customer satisfaction, related efects need not be modelled in such detail as done in the decision model and related data collection efort is not justified. In such cases, one should focus on cost efects as no eficiency/experience trade-of needs to be resolved. Hence, we recommend applying the decision model only to those processes whose value is driven by customer satisfaction.

## 5.3. Synopsis

To evaluate the decision model, we followed the recommendations by Sonnenberg and vom Brocke [27]. First, we justified the research problem and derived DOs in Sections 1 and 4 (EVAL1). As we continuously accounted for the DOs when developing the decision model, we consider them as addressed.

Regarding understandability and real-world fidelity, we conducted interviews with industry experts (EVAL2), who approved the decision model's understandability for experts involved in process decisionmaking. The experts also underscored the model's real-world fidelity, stating that it covers most situations occurring in their daily business. The experts' main criticism was that the decision model entails high data collection efort. However, they confirmed that this is a common drawback of decision models – particularly of investment models covering a multi-period planning horizon. In response to this feedback, we ensured that decision model allows for a simplified application based on aggregated input parameters.

Moreover, we implemented the decision model as a software prototype to provide a proof of concept (EVAL3), which we applied at a German insurance company to provide a proof of value (EVAL4). In the INSURANCE case, the decision model yielded interpretable results and the required input data could be collected. The robustness analysis showed that the decision model can cope with estimation inaccuracies (e.g., regarding the initial degrees of fulfillment) and yields consistent results even in case of deviations. Moreover, slight over- and underestimations of the degrees of fulfillment did not afect the optimal project portfolio, whereas substantial under-estimations caused a switch from a revenue- to a cost-driven improvement strategy. The prototype easily coped with the complexity at hand, supporting both the calculation of the optimal portfolio and the robustness analysis. Hence, we conclude that the decision model is applicable and that its results are useful for process analysts involved in process decisionmaking.

## 5.4. Recommendations for application

Based on our experience from the INSURANCE case, we would like to share recommendations for an eficient application of the decision model. First, we recommend using the prototype, as even small problems instances cannot be calculated manually. Second, we recommend collaborating with a key informant (e.g., a process analyst or owner) who knows the process in-depth and who is suficiently connected within the organization to drive and coordinate the collection of input data. Third, we recommend conducting multiple workshops with the informant (e.g., introducing the overall motivation and background, collecting relevant input data, and discussing results), where additional experts are invited whenever needed. Fourth, we recommend using secondary data from existing sources (e.g., enterprise information systems, performance measurement systems, customer surveys, lists of completed and ongoing projects) wherever possible – even if it must be adjusted and pre-processed. Primary data (e.g., appraisals of customer agents) should only be collected if needed. In such cases, proven techniques should be used, e.g., Kano's survey-based technique for feature classification. If data needs to be estimated (e.g., for project efects or weights of sub-processes), multiple experts should be involved to ofset subjective bias and to get a feeling for value ranges, which supports the performance of robustness analyses. Fifth, we recommend applying the decision model repeatedly and for multiple processes to continuously reduce data collection efort.

## 6. Conclusion and outlook

For many companies, CC has evolved into an important success factor. Apart from the design of excellent products, customer-centric business processes are key when implementing CC. With companies commonly facing an abundance of action possibilities, fast-changing customer needs, and scarce resources, we analyzed how they can prioritize process improvement projects to foster CC. To that end, we proposed an economic decision model that assists process analysts in the selection and scheduling of process improvement projects for a predefined process by leveraging knowledge from value-based process decision-making, PPS, and the measurement of customer satisfaction – specifically ideas from the Kano model. Hence, the decision model distinguishes basic, performance, and excitement process features whose degree of fulfillment drives customer satisfaction and revenues in diferent ways. Moreover, features can switch their type over time. The decision model applies to interaction-intensive core processes for which customer satisfaction is a key value driver. Based on an aggregation of monetary and non-monetary project efects, portfolios of process improvement projects are compared by their value contribution measured in terms of the risk-adjusted expected NPV. This enables addressing both the eficiency/experience trade-of of process design and the trade-of between long-term company growth and the shortterm satisfaction of fast-changing customer needs. We evaluated the decision model by discussing it with industry experts, by implementing a prototype, and by applying it at an insurance company.

Our research has theoretical and managerial implications. From a theoretical perspective, the decision model adds to the prescriptive knowledge on process prioritization and CPM through exaptation, i.e., by contextualizing, combining, and extending known solutions to an under-researched problem class [22]. That is. the decision model offers a novel approach to the customer-centric prioritization of process improvement projects. This is an important contribution as knowledge on CPM has been rather conceptual so far and specifically lacks guidance on how to implement CC through customer-centric processes [3]. While there are works that deal with the prioritization of processes and process improvement projects, our work is the first to account for CC in process decision-making. To the best of our knowledge, our work is the first to combine the switching of feature types with PPS, which may also be used beyond process improvement. Moreover, our findings also show that the ideas of the Kano model not only support product but also process design. At the same time, the decision model is not inextricably tied to the Kano model, as other feature types, measurement scales/ functions, and efect types can be incorporated. Finally, the decision model contributes to CC in general by providing a means for putting it into practice.

From a managerial perspective, process analysts can use the deci sion model, the recommendations for application, and the publicly available prototype to prioritize process improvement activities. Our discussions with industry experts and the real-world application confirmed the relevance of the problem setting and our solution. The evaluation also revealed that the decision model supports process decision-makers to think about how to combine the eficiency and the customer perspective on business processes.

Our research comes with limitations that stimulate future research. First, as almost any mathematical model, the decision model builds on simplifying assumptions. For instance, it considers input parameters as deterministic or expected values and captures risk only via a risk-adjusted interest rate. In practice, the degree of fulfillment of process features and their development over time are uncertain such that stochastic modeling would increase real-world fidelity. Increased realworld fidelity, however, comes with increased data collection efort, which hampers applicability. As the decision model was designed to be applicable in industry settings, we opted for a deterministic model and recommend performing robustness analyses to ofset uncertainty and estimation inaccuracies. Second, the decision model only focuses on customer satisfaction as driven by customer-company interactions embedded in business processes, not on that part driven by product features. In the future, it may be extended to deal with both parts of customer satisfaction. Third, the decision model is restricted to a single core process, but interactions among processes as well as the fact that customers may interact with a company in several processes may afect the optimal project portfolio. Hence, the decision model should be extended to cover multiple processes. Fourth, the decision model has been evaluated in practice. Although this case confirmed applicability and usefulness, it hardly enabled assessing how eficiently the model can be applied. Although we partly addressed this issue by presenting recommendations for application and by enabling a simplified application based on aggregated parameters, eficiency was not a key evaluation criterion of our work, which focused on the design search process and an overall evaluation. Hence, the decision model should be applied in more cases to establish a knowledge base, to identify ideas for tailoring it to various contexts, and to refine the recommendations for application. To facilitate such case studies, we recommend enhancing the prototype such that it provides more sophisticated analysis functionality and can be extended more easily.

## CRediT authorship contribution statement

Thomas Kreuzer: Conceptualiziation, Data curation, Methodology, Project administration, Writing - original draft, Writing - review & editing. Maximilian Röglinger: Conceptualiziation, Data curation, Methodology, Project administration, Writing - original draft, Writing - review & editing. Lea Rupprecht: Conceptualiziation, Data curation, Methodology, Project administration, Writing - original draft, Writing - review & editing.

## Acknowledgments

This research was (in part) carried out in the context of the Project Group Business and Information Systems Engineering of the Fraunhofer Institute for Applied Information Technology FIT.

## References

[1] H. Gimpel, S. Hosseini, R. Huber, L. Probst, M. Röglinger, U. Faisst, Structuring digital transformation: a framework of action fields and its application at ZEIsS Journal of Information Technology Theory and Application 19 (2018)

[2] J.R. Galbraith, Designing the Customer-Centric Organization: A Guide to Strategy, Structure, and Process, Jossev-Bass, San Francisco, California, 2005.

[3] J. Moormann, E.Z. Palvölgyi, Customer-centric business modeling: setting a re search agenda: article 5, 2013 IEEE 15th Conference on Business Informatics Proceedings, 2013.

[4] I.O. Karpen, L.L. Bove, B.A. Lukas, M.J. Zyphur, Service-dominant orientation: measurement and impact on performance outcomes, J. Retail. 91 (2015) 89–108, https://doi.org/10.1016/j.jretai.2014.10.002.

[5] D. Bushaus, Salesforce wins award for customer centricity, inform.tmforum.org/ features-and-analysis/2016/05/salesforce-wins-award-for-customer-centricity , Accessed date: 4 July 2019.

[6] P. Towers, Retailer Awards series: Stylerunner, https://www.insideretail.com.au/ news/retailer-awards-series-stylerunner-201612 , Accessed date: 4 July 2019.

[7] Amazon, Earth's most customer-centric company, https://www.amazon.jobs/en working/working-amazon, (2019) , Accessed date: 4 July 2019.

[8] W. Reinartz, M. Kraft, W.D. Hoyer, The customer relationship management process: its measurement and impact on performance, J. Mark. Res. 41 (2004) 293–305, https://doi.org/10.1509/jmkr.41.3.293.35991.

[9] J. van den Bergh, S. Thijs, Ö. Isik, S. Viaene, The World Is Not Enough: Customer Centricity and Processes, Business Processes Trends, (2012).

[10] M. Hammer, What is business process management? Handbook on Business Process Management 1, Springer, Berlin, 2010, pp. 3–16.

[11] P. Harmon, The scope and evolution of business process management, Handbook on Business Process Management 1. Springer. Berlin. 2010. pp. 37–81.

[12] W. van der Aalst, Business process management: a comprehensive survey, ISRN Software Engineering (2013) 1–37, https://doi.org/10.1155/2013/507984.

[13] G. Zellner, A structured evaluation of business process improvement approaches, Bus. Process. Manag. J. 17 (2011) 203–237, https://doi.org/10.1108 14637151111122329.

[14] J. Recker, J. Mendling, The state of the art of business process management re search as published in the BPM conference, Bus. Inf. Syst. Eng. 58 (2016) 55–72. https://doi.org/10.1007/s12599-015-0411-3.

[15] M. Voss, Impact of customer integration on project portfolio management and its success—developing a conceptual framework, Int. J. Proj. Manag. 30 (2012) 567–581, https://doi.org/10.1016/j.ijproman.2012.01.017.

[16] M. Benner, M.L. Tushman, Exploitation, exploration, and process management: the productivity dilemma revisited, Acad. Manag. Rev. 28 (2003) 238–256, https://doi. org/10.5465/amr.2003.9416096.

[17] A. Fleischmann, W. Schmidt, C. Stary, S. Obermeier, E. Börger, Subject-oriented Business Process Management, Springer, Heidelberg, 2012.

[18] M. Rosemann, Proposals for future BPM research directions, in: C. Ouyang, Jung Jae-Yoon (Eds.), Asia Pacific Business Process Management, AP-BPM 2014, 2014, pp. 1–15.

[19] C. Potts. recrEAtion: Realizing the Extraordinary Contribution of Your Enterprise Architects (Take It With You). Technics Publications. LJC. 2010.

[20] P. Trkman, W. Mertens, S. Viaene, P. Gemmel, From business process management to customer process management, Bus. Process. Manag. J. 21 (2015) 250–266, https://doi.org/10.1108/BPMJ-02-2014-0010.

[21] P. Aflerbach, L. Frank, Customer experience versus process eficiency: towards an analytical framework about ambidextrous BPM. Proceedings of the 37th International Conference on Information Systems (ICIS). 2016

[22] S. Gregor, A.R. Hevner, Positioning and presenting design science research for maximum impact, MISQ 37 (2013) 337–355, https://doi.org/10.25300/MISQ 2013/37.2.01.

[23] K. Pefers, M.A. Rothenberger, B. Kuechler (Eds.), Design Science Research in Information Systems. Advances in Theory and Practice: Lecture Notes in Computer Science. Springer. Berlin, Heidelberg, 2012

[24] R.L. Keeney, H. Raifa, R.F. Meyer, Decisions with Multiple Objectives: Preferences and Value Tradeoffs. Cambridge Univ. Press, Cambridge. 1999.

[25] J. Meredith, A. Raturi, K. Amoako-Gyampah, B. Kaplan, Alternative research paradigms in operations, J. Oper. Manag. 8 (1989) 297–326, https://doi.org/10. 1016/0272-6963(89)90033-8.

[26] N. Kano, N. Seraku, F. Takahashi, S. Tsuji, Attractive quality and must-be quality, Journal of Japanese Society for Ouality Control 14 (1984) 147–156.

[27] C. Sonnenberg, J. Vom Brocke, Evaluation patterns for design science research artefacts, Practical Aspects of Design Science, Springer, Berlin, Heidelberg, 2012, pp. 71–83.

[28] M. Dumas, M. La Rosa, J. Mendling, H.A. Reijers, Fundamentals of Business Process Management, Springer, Berlin, Heidelberg, 2018.

[29] P Harmon. The state of business process management 2018 BPTrends 2018

[30] L. Bitomsky, J. Huhn, W. Kratsch, M. Röglinger, Process meets project prioritizatior a decision model for developing process improvement roadmaps: article 102. Proceedings of the 27th European Conference on Information Systems (ECIS), Association for Information Systems, 2019.

[31] T.H. Davenport, Process management for knowledge work, in: J. Vom Brocke, M. Rosemann (Eds.), Handbook on Business Process Management 1: Introduction, Methods, and Information Systems, 2nd ed., Springer Berlin Heidelberg, Berlin, Heidelberg, 2015, pp. 17–35.

[32] M. Lehnert, A. Linhart, M. Röglinger, Value-based process project portfolio man agement: integrated planning of BPM capability development and process improvement, Bus, Res. 9 (2016) 377–419. https://doi,org/10.1007/s40685-016- 0036-5.

[33] B. Povey, The development of a best practice business process improvement methodology, Benchmarking for Quality Management & Technology 5 (1998) 27–44. https://doi.org/10.1108/14635779810206795

[34] H.A. Reijers, S. Liman Mansar, Best practices in business process redesign: an overview and qualitative evaluation of successful redesign heuristics, Omega 33 (2005) 283–306, https://doi.org/10.1016/j.omega.2004.04.012.

[35] A. Linhart, J. Manderscheid, M. Röglinger, H. Schlott, Process improvement roadmapping - how to max out your process: article 6, Proceedings of the 36th International Conference on Information Systems (ICIS). 2015

[36] D. Heckl, J. Moormann, Process performance management, Handbook on Business Process Management, 2 Springer, Berlin, 2014, pp. 115–135.

[37] M. Franco-Santos, L. Lucianetti, M. Bourne, Contemporary performance measurement systems: a review of their consequences and a framework for research, Manag. Account. Res. 23 (2012) 79–119, https://doi.org/10.1016/j.mar.2012.04.001.

[38] D.B. Wagner, C. Suchan, B. Leunig, J. Frank, Towards the analysis of information systems flexibility: proposition of a method, Wirtschaftsinformatik Proceeding 2011, 2011.

[39] J. Vom Brocke, C. Sonnenberg, Value-orientation in business process management, Handbook on Business Process Management, 2 Springer, Berlin, 2014, pp. 101–132.

[40] H.U. Buhl, M. Röglinger, S. Stöckl, K.S. Braunwarth, Value orientation in proces management, Bus. Inf. Syst. Eng. 3 (2011) 163–172, https://doi.org/10.1007/ s12599-011-0157-5.

[41] A. Damodaran, Investment Valuation: Tools and Techniques for Determining the Value of Any Asset. 3rd ed., Wiley. Hoboken. N.J. 2012.

[42] M. Bolsinger, Bringing value-based business process management to the operational process level, IseB 13 (2015) 355–398, https://doi.org/10.1007/s10257-014- 0248-1.

[43] L. Gronholdt, A. Martensen, K. Kristensen, The relationship between customer satisfaction and loyalty: cross-industry diferences, Total Qual. Manag. 11 (2000) 509–514. https://doi.org/10.1080/09544120050007823.

[44] I. Martinaityte, C. Sacramento, S. Aryee, Delighting the customer: creativity-oriented high-performance work systems, frontline emplovee creative performance. and customer satisfaction, J. Manag. 45 (2019) 728–751, https://doi.org/10.1177 0149206316672532

[45] R.L. Oliver, Satisfaction: A Behavioral Perspective on the Consumer, 2nd ed., Sharpe, Armonk, NY, 2010.

[46] K. Matzler, F. Bailom, H.H. Hinterhuber, B. Renzl, J. Pichler, The asymmetric relationship between attribute-level performance and overall customer satisfaction: a reconsideration of the importance–performance analysis, Ind. Mark. Manag. 3 (2004) 271–277, https://doi.org/10.1016/S0019-8501(03)00055-5.

[47] A. Parasuraman, V.A. Zeithaml, L.L. Berry, A conceptual model of service quality and its implications for future research, J. Mark. 49 (1985) 41, https://doi.org/10. 2307/1251430.

[48] E.W. Anderson, C. Fornell, Foundations of the American Customer Satisfaction Index, Total Qual. Manag. 11 (2000) 869–882, https://doi.org/10.1080/ 09544120050135425

[49] B. Bartikowski, S. Llosa, Customer satisfaction measurement: comparing four methods of attribute categorisations, Serv. Ind. J. 24 (2004) 67–82, https://doi.org 10.1080/0264206042000275190

[50] T. Materla, E.A. Cudney, J. Antony, The application of Kano model in the healthcare industry: a systematic literature review, Total Qual. Manag. Bus. Excell. 30 (2019) 660–681. https://doi.org/10.1080/14783363.2017.1328980

[51] Deloitte, Design Thinking & Kano Model - Revolutionalizing Agile Delivery, http:// www.baconvention.com/wp-content/uploads/2016/08/DesignThinking\_ KanoModel.pdf, (2016) , Accessed date: 12 January 2020

[52] K. Matzler, H.H. Hinterhuber, F. Bailom, E. Sauerwein, How to delight your customers, Journal of Product & Brand Management 5 (1996) 6–18. https://doi,org/ 10.1108/10610429610119469.

[53] J.H. Mayer, Using the Kano model to identify attractive user-interface software components. Proceedings of the 33rd International Conference on Information Systems (ICIS). 2012

[54] N. Kano, Life cycle and creation of attractive quality, Proceedings of the 4th QMOD Conference, 2001.

[55] T. Frey, P. Buxmann, IT project portfolio management - a structured literature review: Article 167. Proceedings of the 20th European Conference on Informatior Systems (ECIS), 2012.

[56] J.W. Lee, S.H. Kim, An integrated approach for interdependent information system project selection, Int. J. Proj. Manag. 19 (2001) 111–118, https://doi.org/10.1016/ S0263-7863(99)00053-8.

[57] N.P. Archer, F. Ghasemzadeh. An integrated framework for project portfolio selection, Int. J Proi, Manag, 17 (1999) 207–216, https://doi org/10 1016/S0263 7863(98)00032-5

[58] A. Darmani, P. Hanafizadeh, Business process portfolio selection in re-engineering projects, Bus. Process. Manag. J. 19 (2013) 892–916, https://doi.org/10.1108 BPMJ-08-2011-0052

[59] W. van der Aalst, M. La Rosa, F.M. Santoro, Business process management, Bus. Inf. Syst. Eng. 58 (2016) 1–6, https://doi.org/10.1007/s12599-015-0409-x

[60] J.L. Cohon, Multiobjective Programming and Planning, Academic Press, New York, 2011.

[61] J. Pries-Heje, R. Baskerville, J. Venable, Strategies for design science research evaluation: Article 87, Proceedings of the 16th European Conference on Information Systems (ECIS). 2008

[62] J. Venable, J. Pries-Heje, R. Baskerville, A comprehensive framework for evaluation in design science research, Design Science Research in Information Systems. Advances in Theory and Practice, Springer, Berlin. Heidelberg, 2012, pp. 423–438

[63] N. Bennett, J. Lemoine, What a diference a word makes: understanding threats to performance in a VUCA world, Business Horizons 57 (2014) 311–317, https://doi. org/10.2139/ssrn.2406676.

[64] S. Hosseini, M. Merz, M. Röglinger, A. Wenninger, Mindfully going omni-channel

An economic decision model for evaluating omni-channel strategies, Decis. Support. Syst. 109 (2018) 74–88.

[65] M.S. Denner, L.C. Püschel, M. Röglinger, How to exploit the digitalization potential of business processes, Bus. Inf. Syst. Eng. 11 (2018) 177, https://doi.org/10.1007 s12599-017-0509-x

[66] S. Berger, M.S. Denner, M. Röglinger, The Nature of Digital Technologies - Development of a Multi-Layer Taxonomy, ECIS, 2018.

[67] E.W. Anderson, V. Mittal, Strengthening the satisfaction-profit chain, J. Serv. Res. 3 (2000) 107–120, https://doi.org/10.1177/109467050032001.

[68] T.S. Gruca, L.L. Rego, Customer satisfaction, cash flow, and shareholder value, J. Mark. 69 (2005) 1–130, https://doi.org/10.1509/jmkg.69.3.1.66358.

[69] H.U. Buhl, D. Kundisch, A. Renz, N. Schlackmann, Spezifizierung des Kano-Modells zur Messung von Kundenzufriedenheit, Wirtschaftsinformatik Proceedings, 2007, p. 52.

[70] M. Conklin, K. Powaga, S. Lipovetsky, Customer satisfaction analysis: identification of key drivers, Eur. J. Oper. Res. 154 (2004) 819–827, https://doi.org/10.1016/ S0377-2217(02)00877-9

[71] M.D. Myers, M. Newman, The qualitative interview in IS research: examining th craft, Inf. Organ. 17 (2007) 2–26, https://doi.org/10.1016/j.infoandorg.2006.11. 001.

![](/api/attachments/AQTDCEN6/fulltext/images/a21be0b362629013ac31a298185993d5a89125c498ccac1f22707234500ecc1d.jpg)  
Thomas Kreuzer studied Industrial Engineering (B.Sc.) with a focus on finance, operations, and information management as well as information-oriented business adminis tration (M.Sc.) at the University of Augsburg. Since June 2018, Thomas is a research associate with the Research Center Finance & Information Management (FIM) in the area of business process management.

![](/api/attachments/AQTDCEN6/fulltext/images/45d85a4e01d2c9ba2ea4c496baf5bf1a79ca39f5a745d0f77dda4038fb8a38ef.jpg)

Maximilian Röglinger is Professor of Information Systems at the University of Bayreuth. Maximilian serves as Deputy Academic Director of the Research Center Finance & Information Management (FIM), where he heads the business process management (BPM) group. Maximilian is also working with the Project Group Business & Information Systems Engineering of the Fraunhofer FIT. Most of Maximilian's work centers around BPM, customer relationship management, and digital transformation. He publishes in journals like Business & Information Systems Engineering, Decision Support Systems, European Journal of Information Systems, Journal of the Association for Information Systems, and Journal of Strategic Information

Systems. Maximilian is highly engaged in projects with companies such as Deutsche Bahn, Deutsche Bank, Hilti, Infineon Technologies, Schott, and Siemens. Maximilian earned his PhD at the University of Augsburg and holds a Diploma in Business and Information Systems Engineering from the University of Bamberg.

![](/api/attachments/AQTDCEN6/fulltext/images/337403b637ecb2931462705eefbe1b2cb59dbe34efa5d359a28077423f31a2c3.jpg)

Lea Rupprecht studied Business Mathematics (M.Sc.) at the University of Augsburg. Since March 2014, Lea is a research associate with the Research Center Finance & Information Management (FIM), working at the intersection of customer relationship management and business process management. Lea has also been working with the Project Group Business & Information Systems Engineering of the Fraunhofer FIT in projects with companies such Deutsche Bahn, Deutsche Bank, and Senacor Technologies.
