---
otero_id: 13748
otero_key: "FBDJC6YJ"
title: "Managing Co-Creation in Information Technology Projects: A Differential Games Approach"
authors: "Emre M. Demirezen; Subodha Kumar; Bala Shetty"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0636"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/FBDJC6YJ/fulltext/images/718ff4a33325931bb11ae38edf4319dd434c6cf6b10200abeb4eae4e0e3d352a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Managing Co-Creation in Information Technology Projects: A Differential Games Approach

Emre M. Demirezen, Subodha Kumar, Bala Shetty

To cite this article:

Emre M. Demirezen, Subodha Kumar, Bala Shetty (2016) Managing Co-Creation in Information Technology Projects: A Differential Games Approach. Information Systems Research

Published online in Articles in Advance 15 Jul 2016

http://dx.doi.org/10.1287/isre.2016.0636

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/FBDJC6YJ/fulltext/images/4ad97f1aa9b99188f8315990de82dae07432f7e8e83037c11c84f36ee1a9840c.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Managing Co-Creation in Information Technology Projects: A Differential Games Approach

Emre M. Demirezen

School of Management, Binghamton University, State University of New York, Binghamton, New York 13902, edemirezen@binghamton.edu

Subodha Kumar, Bala Shetty

Mays Business School, Texas A&M University, College Station, Texas 77843 {skumar@mays.tamu.edu, bshetty@mays.tamu.edu}

W<sup>e</sup> <sup>study</sup> <sup>the</sup> <sup>relationship</sup> <sup>between</sup> <sup>a</sup> <sup>client</sup> <sup>and</sup> <sup>a</sup> <sup>vendor</sup> <sup>in</sup> <sup>value</sup> <sup>co-creation</sup> <sup>environments</sup> <sup>such</sup> <sup>as</sup> <sup>infor-</sup> mation technology projects. We consider that the client gets utility from the project throughout the development period and that the effort levels are not verifiable if not monitored. The output is contingent on the effort levels of each party, and we allow these effort levels to be dynamic. Hence, the client needs to optimally decide the terms of payment structures so as to maximize her net value. We analyze the performance of different payment structures and find the best one for the client in diverse settings. We show that the remaining time of the project and the client’s valuation of the project regulate the behavior of the effort levels and some other characteristics in the collaboration. We derive the conditions under which the client chooses not to monitor the vendor’s effort and operates in a double moral hazard environment. In addition, we find that the equilibrium effort levels or the values the parties gain from the collaboration do not necessarily increase when the output becomes more sensitive to either party’s effort. Based on the results of our model, we present several other managerial insights.

Keywords: value co-creation; collaboration; information technology services; differential game

History: Rahul Telang, Senior Editor; Hsing Kenneth Cheng, Associate Editor. This paper was received on August 17, 2014, and was with the authors 6 months for 1 revision. Published online in Articles in Advance July 15, 2016.

## 1. Introduction

Management of information technology (IT) projects has become increasingly more sophisticated and challenging. Attaining high productivity and efficiency levels is argued to be difficult because of many factors, such as significant customer involvement throughout the process (Bettencourt et al. 2002, Gopal et al. 2003, Baskerville and Pries-Heje 2004, Ramasubbu et al. 2008, Susarla et al. 2010, Susarla 2012). Hence, we contribute to the literature in this study by examining the client’s involvement in generating a service in a dynamic environment where the effort levels are not verifiable if not monitored. In particular, we derive the type of contract that is optimal for the client under different circumstances and examine the behaviors of the vendor and client with respect to changes in the characteristics of the parties and the project. In addition to IT settings, our analyses, results, and insights also apply to other “services” such as business process outsourcing, auditing, consulting, financial planning, engineering projects, and research and development (R&D) projects (with slight modifications). However, in this paper, “services” refer to IT services that are the focus of our study.

## 1.1. Dynamic Collaborative Environments

We study collaborative and dynamic IT settings in this paper and provide broad guidelines under a stylized framework. First, the collaborative relationship between the client and the vendor in our study implies that they need to work together closely on the project to create a successful service or software. Second, we consider that the relationship between the parties is ongoing (or dynamic) with regard to the value co-created in the project, payments, and effort levels. Our study mainly applies to those projects where the client’s effort is essential in the collaboration, and the output is valuable to the client even before the collaboration finishes. A specific example is an Enterprise Resource Planning (ERP) project (or some other “suite” of applications) where the client actively works with the vendor in creating different modules that are used by the client as they are ready before the end of the project or collaboration (Kale 2014).

Before explaining the collaborative and dynamic environments in detail, we start with illustrating the traditional view of the vendor–client relationship in Figure 1(a), where the efforts of two parties are substitutes. In such settings, the client (referred to as she)

(b) Collaborative vendor–client environment

(a) Traditional vendor–client environment  
Figure 1 Traditional versus Collaborative Vendor–Client Relationship  
![](/api/attachments/FBDJC6YJ/fulltext/images/fff449c1db16a8047974cd50b682ad0bd05fe26764658e5ad7d8ed0df597e51a.jpg)

offers a payment to the vendor (referred to as he) based on her business requirements, and the vendor assumes the whole responsibility in the generation of the service if he accepts the offer. Then, based on the vendor’s performance, the client receives value and makes a payment to the vendor. In the information systems (IS) literature, the relationship between a client and a vendor has been studied generally in such traditional settings (DiRomualdo and Gurbaxani 1998, Gurbaxani 2007, Susarla and Barua 2011, Whitaker et al. 2011, Mani et al. 2012). However, the specifics of the client–vendor relationship are changing toward creating value through value co-creation in service environments (Toppin and Czerniawska 2005). We illustrate this setting in Figure 1(b). The focus of this paper is to consider this collaborative view.

As shown in Figure 1(b), value co-creation implies that joint efforts are required from both the client and the vendor to create and deliver the service. IT services are becoming more complex, unstructured, and tailored to fit the unique needs of particular clients (Bettencourt et al. 2002, Harris et al. 2009). Therefore, to attain successful outcomes, clients must participate in the creation of the services. In effect, clients get involved in the IT projects in (i) the problem definition stage, (ii) the selection of the solution, and (iii) the implementation of the solution. For example, the client may provide critical input in the form of know-how or specialized equipment and assist the vendor in all stages of the project (Plambeck and Taylor 2006). On the other hand, clients often rely on the expertise of their vendors, who may bring in knowledge or components that are required for the success of the collaboration. Many examples in IS, such as IT services and software co-development projects, follow the value co-creation approach presented in Figure 1(b). We would like to note that our proposed model is general, and it also captures the traditional setting where the vendor assumes the whole responsibility in the generation of the output. We discuss this issue in more detail in Section 2.2.

![](/api/attachments/FBDJC6YJ/fulltext/images/d1c17ff7bd01e08ed6d3d0e9eba96263a3a60ce3fedce423366429855869028e.jpg)

As discussed earlier, in addition to our collaborative focus, another aspect of the environment we consider is that the relationship between the parties is ongoing and dynamic. The relationship is ongoing because the client and the vendor may collaborate until the end of the useful life of the service or software—not just during the development (Currie and Galliers 1999). Moreover, the setting in our study is dynamic in several aspects: (i) the allocation of the effort levels of both parties can change throughout time, (ii) the client can benefit from the collaboration before the project ends, and (iii) the vendor can receive payments throughout the collaboration, not just at the end of the project. It is important to clarify that we do not analyze multiple projects; rather, we analyze the dynamics of a single collaboration over time. In our setting, the payment structure is decided on upfront, whereas it could be decided on before the start of each project in the multiple project case.

The collaboration literature generally focuses on (i) the total effort required in the collaboration (not on its dynamics) and (ii) the final outcome of the project or collaboration. First, the parties do not need to adhere to the same level of work-hours throughout the collaboration. In effect, they can freely adjust their effort levels according to the needs of the project from the beginning to the end of the collaboration. However, a static analysis cannot reveal insights based on “when” and “how much” to allocate efforts on the project simultaneously. Second, a system or application being developed in a collaborative project may become an essential part of the client’s business even “during” its development—not only after the project finishes. Therefore, any manager working with projects that are developed in useful increments should consider ongoing value (Pigoski 1996). These increments might be different modules of a project that are useful to the client by themselves or valuable knowledge co-created in each stage of the collaboration. Other examples include the IT services that are built and enhanced in an incremental fashion until the end of their useful lifetime, while the client can use the intermediate versions of these services (Pigoski 1996, Currie and Galliers 1999). Accordingly, until Section 6, we consider that the project’s terminal value (i.e., the value of the project when the collaboration ends) is less important compared to the ongoing utility received from the collaboration and can be ignored. However, in Section 6, we consider the scenario where the client receives value both during and at the end of the collaboration. Note that a special case of such a setting includes environments where the value is received only at the end.

## 1.2. Our Contributions

In this section, we discuss and highlight our contributions with respect to the relevant literature. Although the literature for project management and game theoretical analysis of collaboration are vast (e.g., Kouvelis and Lariviere 2000, Gopal et al. 2003, Cachon and Netessine 2004, Roels et al. 2010, Lee et al. 2013), the problem we are analyzing has received scant attention. In our paper, the nature of the collaboration is different from most of the past studies because of the complementary effort levels. Karmarkar and Pitbladdo (1995) point out the importance of the involvement of customers in the service delivery process and call for explicit modeling of service cocreation. According to Hopp et al. (2009) and Bapna et al. (2010), there are many promising research opportunities pertaining to the management of IT services. We respond to these calls by analyzing a setting that requires joint efforts from a client and a vendor for the generation of the output. Moreover, the literature does not focus on the dynamics of collaboration between the parties as we do in our paper.

In our setting, the client (respectively, vendor) can infer the effort level of the vendor (respectively, client) based on her own effort level and the output. However, this effort level is not verifiable to the court. In this case, a double moral hazard problem arises and the payment between the parties can only be based on what is verifiable (Pearce and Stacchetti 1998, Schwartz and Edlin 2003, Krishnan et al. 2004). Therefore, an output dependent payment structure is utilized that might also be thought of as a revenuesharing agreement. Furthermore, in IT settings, the parties may be able to monitor the effort levels with some cost. If they are able and choose to do so, then the effort levels become verifiable. Hence, we also consider the setting where the effort level of the vendor is monitored (and therefore verifiable). In this case, the parties can utilize a payment structure based on the effort level.

In this study, we capture all of the dynamism discussed above by utilizing a differential game approach in a single client–single vendor setting. Differential games can be considered as a fusion of game theory and optimal control theory. Hence, they incorporate strategic decision making and continuous change simultaneously. Differential game models incorporate the dynamic effect of the current state and decision on future states and decisions. Hence, our solution allows for forward-looking behavior. Dockner et al. (2000) provides a general discussion of differential games. However, because of the inherent difficulty in solving differential games, there are a few studies that utilize differential games in the IS literature (Cavusoglu et al. 2005, Mookerjee et al. 2011, Liu et al. 2012). To our knowledge, this is the first study that considers a differential game in a value cocreation environment.

As discussed earlier, we focus on the collaborative settings. Based on the results of our models, we derive several useful managerial insights pertaining to many aspects of these environments. Most importantly, we answer the questions regarding how the client should manage the collaborative relationship. Our analysis reveals when the client should monitor the vendor’s effort and how the severity of the double moral hazard problem changes across scenarios. We find that the vendor’s effort should not be monitored when the participation cost of the vendor is very low. Furthermore, our results show that the client should not monitor the vendor’s effort if the sensitivity of output to the vendor’s effort is relatively higher than the sensitivity to the client’s effort.

Next, we derive the optimal payment terms in these settings and the evolution of the equilibrium effort levels. We find that effort levels decrease as the project progresses. This behavior is observed even when we (i) discount profits and costs or (ii) consider that the unit value of the output is high in the later stages of the project. We also examine the environments where the vendor gains experience while working on the project. In such settings, the unit effort cost of the vendor decreases with time due to self-learning. In these cases, we show that the effort levels can first increase in the earlier stages of the project and then decrease toward the end of the collaboration. We also show that if the value received at the end of the collaboration is considerably higher than the ongoing utility received, then the decrease in effort levels with time is less pronounced.

We further our analysis by answering the following question: Should the parties exert more effort if the output becomes more sensitive to either party’s effort? Our results show that the answer is not necessarily “yes,” and it depends on other characteristics of the parties. Another question that we study is the following: Will the net values gained by the parties increase if the output elasticities to the effort levels increase? Again, we find that the answer is not necessarily $' \mathrm { y e s . } ^ { \prime \prime }$ In addition, we analyze other similar questions and present useful insights for the managers of both parties. Finally, we explore another collaborative setting that is an interesting variant of the base models. One of the questions that we answer using this analysis is the following: How do our initial findings change if the parties continue to get value from the output after the project finishes? In this case, unlike the base scenario, the value to both parties always increase as the output becomes more sensitive to the effort levels.

## 2. Problem Definition and the First Best Scenario

In this study, we consider an IT setting where a client and a vendor enter into a collaborative agreement. The client’s objective is to find the payment structure that maximizes her value, i.e., the difference between the value of the output and all of the costs related to the collaboration. On the other hand, the vendor maximizes his value in any setting, which is the difference between the payment he receives and the costs related to participating in the collaboration. As discussed earlier, the client and the vendor receive ongoing value from the project. Therefore, the settings we analyze incorporate both strategic decision making and dynamic changes. Hence, we model the problem as a differential game. As discussed earlier, we consider problem settings that differ based on whether or not the effort levels are verifiable to third parties, such as a court. Next, we introduce our model starting with the input parameters of the parties.

## 2.1. Input Parameters

We denote the effort levels of the client and the vendor at time t by $u ( t )$ and v4t5, respectively. These levels represent the resources, like labor-hours, exerted by each party. The total time horizon of the collaboration is denoted by T . We model the cost of the client’s effort with a general power term structure as $c _ { c } u ( t ) ^ { \gamma }$ . Note that the commonly used quadratic cost function (e.g., Tsay and Agrawal 2000) is a special case of this structure. Here, $c _ { c }$ is the cost multiplier for the client’s effort. The parameter $\gamma$ is considered to be more than 1 to reflect the fact that the marginal cost of effort increases with the level of effort. In other words, the client utilizes her least costly options first. Similarly, the cost for the vendor is $c _ { v } { v } ( \hat { t ) } ^ { \delta }$ with the corresponding cost multiplier $c _ { v }$ and the cost elasticity term $\delta > 1$ . We also refer to  and  as costliness of the client and vendor, respectively. Clearly, the cost parameters $c _ { c }$ and $c _ { v }$ can be easily estimated using the cost structures of the firms. The cost elasticities of the client’s and vendor’s effort levels $( \mathrm { i . e . , ~ } \gamma$ and $\delta ,$ respectively) can also be estimated based on firms’ overtime policies, hire–fire policies, etc.

Although the client can infer the vendor’s effort level by observing the output, the business agreement cannot be based on the effort levels of the parties. The reason is that in the case of a disagreement, the parties should be able to “prove” or “verify” (to the other party and to the court) the effort levels. As discussed earlier, the effort levels of the parties are not verifiable if they are not monitored. In certain cases, the client might not have direct authority to observe the effort level of the vendor. Furthermore, if the vendor is remotely located, it may be difficult to monitor the vendor because of the dispersion of people, coordination issues, and the loss of communication richness (Carmel 1999). In these cases, the client can utilize only the output based payment structure.

In some environments, however, the effort levels can be monitored and hence are verifiable to third parties. In practice, IT-enabled services and crosslocated personnel mainly help in monitoring the effort level of the vendors. Specifically, the Internet has facilitated real-time access to information across organizations that enables decision models and software to take actions for streamlining operations (Swaminathan and Tayur 2003). RosettaNet (www.rosettanet.org) and GS1 (www.gs1.org) are global standards organizations that develop common platforms for communication between the firms to enable collaboration and automation of transactions across industries—even at the global scale. Some of the benefits of these standards and other ITenabled services are real-time data transfer and automated communication (Erhun and Keskinocak 2011). In addition, the parties in the collaboration generally have cross-located personnel, and they may hold regular meetings, conference calls, presentations, etc. (Choudhury and Sabherwal 2003). Thus, the effort level of each party can be monitored and made verifiable. In such a case, the client can utilize a payment structure based on the effort level. Furthermore, in the problem settings we analyze, if one party’s effort level is monitored, the other party’s effort level can be inferred and verified from the output that is observable. Therefore, monitoring both parties’ effort levels at the same time is not optimal. Hence, in this paper, only the vendor’s effort is monitored if the client chooses (and is able) to do so.

Clearly, the costs related to monitoring need to be taken into account if the effort levels are monitored. Monitoring of cost comprises fixed and variable costs. We denote the fixed component as $F _ { m }$ (e.g., investments in IT). In addition, it is more costly to observe the effort if the effort level is increased. In other words, it is easier to observe the vendor’s effort if it is low. As the vendor increases his effort level and utilizes more costly options such as overtime, the monitoring cost should increase as well. Therefore, we consider the monitoring cost to be positively correlated to the effort level. Hence, similar to the cost of the vendor’s effort, the variable portion of monitoring cost at time t can be written as $c _ { m } v ( t ) ^ { \delta }$ Here, the parameter $c _ { m }$ is the cost multiplier for monitoring the vendor’s effort. This formulation is flexible because the rate of change of total monitoring cost with respect to the vendor’s effort level can be adjusted by changing the value of $F _ { m } .$ . We would like to note that considering a power term different than  in the monitoring cost does not change the key insights of the paper—as long as the total monitoring cost is not negatively correlated to the effort level. Next, we discuss the output parameters of the model.

## 2.2. Output Parameters

As mentioned earlier, in many business settings, the client gets utility from the output as the collaboration is in progress.<sup>1</sup> Therefore, we model the output, which we denote by $q ( t ) ,$ , as continuous, doubly differentiable, strictly concave for positive effort levels, and nondecreasing in effort levels. Furthermore, the instantaneous increase in output is due to the collaborative work between the client and the vendor. Therefore, both parties need to exert effort to generate output. Similar to the other studies, the output is considered to be a Cobb–Douglas function (Cohen et al. 1996, Kim and Nettessine 2013). This implies that if one party exerts higher levels of effort, then the other party will have an incentive to do so as well. More specifically, we model the instantaneous increase in output as ${ \dot { q } } ( t ) = u ( t ) ^ { \alpha } v ( t ) ^ { \beta }$ with $\alpha , \beta \ge 0 ,$ and $\alpha + \beta < 1$ . The constraint $\alpha + \beta < 1$ is actually related to the concavity of the output function. In effect, we do not need to assume  + $\beta < 1$ if a set of more relaxed conditions $( \mathrm { i . e . , } \alpha < \gamma$ and $\beta < \delta )$ holds. If these relaxed conditions are also not satisfied, then it would mean that there is increasing return to scale. Hence, in such a case, the parties could increase their effort levels arbitrarily to produce more output in a less costly manner. Clearly, this does not make practical sense, and therefore we impose this constraint. Besides, as discussed before, our models can represent traditional settings where the vendor assumes the whole responsibility in the generation of the output. This is possible by setting  to 0 in the Cobb– Douglas functional form.

Several past studies empirically justify Cobb– Douglas functional form for the speed of improvement in output in several industries (e.g., see Cohen

Table 1 List of Parameters and Variables

<table><tr><td>Symbol</td><td>Definition</td></tr><tr><td colspan="2">Parameters</td></tr><tr><td> $c_c$ </td><td>Cost multiplier for the client&#x27;s effort</td></tr><tr><td> $c_v$ </td><td>Cost multiplier for the vendor&#x27;s effort</td></tr><tr><td> $c_m$ </td><td>Cost multiplier for monitoring the vendor&#x27;s effort</td></tr><tr><td> $F_m$ </td><td>Fixed portion of the cost for monitoring the vendor&#x27;s effort</td></tr><tr><td>k</td><td>Valuation of the project (i.e., the client&#x27;s value per unit output)</td></tr><tr><td> $R_c$ </td><td>Reservation utility of the client</td></tr><tr><td> $R_v$ </td><td>Reservation utility of the vendor</td></tr><tr><td> $S_c$ </td><td>Salvage value of the client</td></tr><tr><td> $S_v$ </td><td>Salvage value of the vendor</td></tr><tr><td>α</td><td>Output elasticity (or sensitivity) to the client&#x27;s effort level, α ≥ 0</td></tr><tr><td>β</td><td>Output elasticity (or sensitivity) to the vendor&#x27;s effort level, β &gt; 0</td></tr><tr><td>γ</td><td>Cost elasticity (costliness) of the client&#x27;s effort level, γ &gt; 1</td></tr><tr><td>δ</td><td>Cost elasticity (costliness) of the vendor&#x27;s effort level, δ &gt; 1</td></tr><tr><td>T</td><td>Length of planning horizon</td></tr><tr><td colspan="2">Variables</td></tr><tr><td>q(t)</td><td>Output at time t (state variable)</td></tr><tr><td>u(t)</td><td>Level of the client&#x27;s effort at time t (control variable)</td></tr><tr><td>v(t)</td><td>Level of the vendor&#x27;s effort at time t (control variable)</td></tr><tr><td>I</td><td>Transfer payment per unit output (decision variable)</td></tr><tr><td>Fd</td><td>Fixed transfer payment (decision variable)</td></tr><tr><td>H(·)</td><td>Transfer payment function (decision variable)</td></tr></table>

et al. 1996). Here, the parameters  and $\beta$ represent the output elasticity (or sensitivity) to the client’s and vendor’s efforts, respectively, that can be easily estimated using the data from the past projects. The relative weight of the output elasticity parameters should be different across different business settings. For example, in a traditional setting, where the vendor assumes almost all responsibility in the generation of the output,  should be close to 0. On the other hand, if it is a value co-creation setting, then both of these parameters should be greater than 0.

Since the client gets value from the project while it is being developed, we can define it as

$$
\int_ {0} ^ {T} k q (t) d t.\tag{1}
$$

In the above equation, k is used to convert the output to a utility measure. One possible interpretation of k is dollar value per unit output. Hence, we also refer to k as the valuation of the project. From the discussion above, we can write q4t5 as

$$
q (t) = \int_ {0} ^ {t} u (s) ^ {\alpha} v (s) ^ {\beta} d s; q (0) = 0.\tag{2}
$$

The notations are summarized in Table 1.

We would like to state that it is possible to categorize the parameters in two groups: (i) value $( \mathrm { i . e . , }$ k and T ) and cost (i.e., $c _ { c } , \ c _ { v } , \ c _ { m } , \ F _ { m } , \ R _ { c } ,$ 1 and $R _ { v } )$ parameters, and (ii) output (i.e.,  and $\beta )$ and cost (i.e.,  and ) elasticity terms. These variables can be measured in any unit. For example, T can be measured in days, weeks, or months. Since parameter k is value per unit time, by rescaling it accordingly, all of our results and insights remain the same. In short, the units of measurement for the parameters are $" \mathrm { n o t } ^ { \prime \prime }$ important. Rather, it is important how the parameters compare to each other.

## 2.3. Model Preliminaries

In the settings we analyze, the client decides the payment term. Building the discussion in the reverse setting is also possible without any further complication. The client makes an offer to the vendor and the vendor accepts it if and only if the gain is more than his reservation utility. These reservation utilities are denoted by $R _ { c }$ and $R _ { v }$ for the client and vendor, respectively. If the offer is accepted by the vendor, both parties start working together and select and adjust their effort levels dynamically. We begin with analyzing the first best (FB) setting below.

## 2.4. First Best

The FB setting represents the ideal case. Here, the client and the vendor behave as if they are a single firm, and the effort levels are verifiable without any costly monitoring practices. As a result, total value that could be generated in the collaboration is maximized. Therefore, we compare the FB solution with the solutions of the settings with output dependent and effort dependent payment structures in Section 5 to study their relative performances. The single objective in the FB case is to maximize the profit that is the difference between the total value of the output and the participation costs of the parties. Therefore, we can write the unified objective function and the constraints as

$$
\max _ {u (t), v (t)} \left\{\int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t \right.
$$

$$
\left. - \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta} d t \right\}\tag{3}
$$

subject to ${ \dot { q } } ( t ) = u ( t ) ^ { \alpha } v ( t ) ^ { \beta } ;$

$$
\int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t\tag{4}
$$

$$
- \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta} d t \geq R _ {c} + R _ {v};\tag{5}
$$

$$
u (t) \geq 0; v (t) \geq 0.\tag{6}
$$

As discussed, the objective function in Equation (3) is simply the difference between the total value generated in the collaboration and the cost of effort for the client and the vendor. Equation (4) depicts how the output accumulates over time. In addition, the client and the vendor would collaborate only if they can generate value together more than the total of their reservation utilities $R _ { c }$ and $R _ { v }$ . This fact is reflected in Constraint (5). Constraint (6) states the technical detail that the effort levels cannot be negative. The solution of this optimal control problem is provided in the following lemma. All of the proofs are available in the online appendix (available as supplemental material at http://dx.doi.org/10.1287/isre.2016.0636).

<sup>Lemma</sup> <sup>1.</sup> If the parties decide to collaborate, the optimal effort levels for the client and the vendor in the FB scenario are

$$
\begin{array}{l} u (t) = \left(\frac {k \alpha (T - t)}{\gamma c _ {c}}\right) ^ {\delta / (\gamma (\delta - \beta) - \alpha \delta)} \left(\frac {\beta \gamma c _ {c}}{\alpha \delta c _ {v}}\right) ^ {\beta / (\gamma (\delta - \beta) - \alpha \delta)}, \\ v (t) = \left(\frac {k \beta (T - t)}{\delta c _ {v}}\right) ^ {\gamma / (\gamma (\delta - \beta) - \alpha \delta)} \left(\frac {\alpha \delta c _ {v}}{\beta \gamma c _ {c}}\right) ^ {\alpha / (\gamma (\delta - \beta) - \alpha \delta)}. \end{array}
$$

It is easy to see that the optimal effort levels presented in Lemma 1 decrease as the project progresses (i.e., as t increases). As we discuss later, this behavior is not observed in every setting. When the client and the vendor choose these effort levels, the total value generated in the collaboration is as provided in the lemma below.

<sup>Lemma</sup> <sup>2.</sup> If the parties decide to collaborate, the total value generated in the collaboration is

$$
\begin{array}{c} \frac {T (\gamma (\delta - \beta) - \alpha \delta) ^ {2}}{((2 \gamma - \alpha) \delta - \beta \gamma) \gamma \delta} (k T) ^ {\gamma \delta / (\gamma (\delta - \beta) - \alpha \delta)} \\ \cdot \left(\left(\frac {\alpha}{c _ {c} \gamma}\right) ^ {\alpha \delta} \left(\frac {\beta}{c _ {v} \delta}\right) ^ {\beta \gamma}\right) ^ {1 / (\gamma (\delta - \beta) - \alpha \delta)}. \end{array}
$$

Note that the client and the vendor decide to collaborate if the value presented in Lemma 2 is more than the total of their reservation utilities (i.e., if Constraint (5) is satisfied). Later, we use this FB value to compare it with the values in other models. Next, we analyze three different generalizations of the model and discuss how the key insights change in these cases.

2.4.1. Time-Variable Value. In some environments, the unit value of the output in the collaboration might be more in the later stages of the project. Therefore, we analyze what happens if the client’s value per unit output $\mathbf { \bar { \Phi } } _ { k }$ is not constant but increases in time $( \mathrm { i . e . , }$ $d k ( \bar { t } ) / d t > 0 )$ . Should the effort levels increase as the project progresses or should they again decrease similar to that in Lemma 1? We find that the effort levels still decrease through time even if the output becomes more valuable toward the end of the collaboration. In addition, we find that considering k as time-invariant or time-variant does not change the main insights of the paper. Therefore, for simplicity, we treat k as a time-invariant constant in this paper.

2.4.2. Discounting Benefits and Costs. It is easy to modify our model such that the benefits and costs are discounted. For example, if the discount factor is $r ,$ objective function value in the FB model becomes

$$
\begin{array}{c} \max _ {u (t), v (t)} \bigg \{\int_ {0} ^ {T} k e ^ {- r t} q (t)   d t - \int_ {0} ^ {T} c _ {c} e ^ {- r t} u (t) ^ {\gamma}   d t \\ - \int_ {0} ^ {T} c _ {v} e ^ {- r t} v (t) ^ {\delta}   d t \bigg \}. \end{array}
$$

We solve this problem with the current value Hamiltonian method. However, interestingly, the solution reveals that discounting profits and costs does not alter the key insights. For example, in the presence of discounting, we find that the effort levels still strictly decrease with time. Furthermore, since the planning horizon is short to medium term, discounting against inflation is not very meaningful. Hence, for the rest of our analysis, we set the discount term $( \mathrm { i . e . , } r )$ to zero.

2.4.3. Self-Learning of Vendor. Now, we analyze the scenario where the vendor’s effort cost decreases with time due to learning effects. At the earlier stages of the collaboration, the vendor might have limited knowledge of the project, and the cost of his effort might be high. In such cases, as the learning literature suggests (Abernathy and Wayne 1974), the vendor’s participation cost would be high at the beginning but will decrease with time due to self-learning or experience gain. Specifically, for a given learning rate w, we model the change in the cost-per-unit effort for the vendor as $\dot { c } _ { v } ( t ) = - w c _ { v } ( t )$ 0 It implies that the instantaneous decrease in the cost is proportional to the learning rate and the current level of the cost itself. Hence, we have $c _ { v } ( t ) = c _ { 0 } e ^ { - w t }$ . Here, $c _ { 0 }$ denotes the starting level of the per-unit effort cost. We can now write the aggregated objective function of client and vendor, and the constraints, as

$$
\begin{array}{c} \max _ {u (t), v (t)} \left\{\int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t \right. \\ \left. - \int_ {0} ^ {T} c _ {0} e ^ {- w t} v (t) ^ {\delta} d t \right\} \end{array}
$$

subject to $\dot { q } ( t ) = u ( t ) ^ { \alpha } v ( t ) ^ { \beta } .$

$$
\begin{array}{l} \int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t \\ \qquad - \int_ {0} ^ {T} c _ {0} e ^ {- w t} v (t) ^ {\delta} d t \geq R _ {c} + R _ {v}, \\ u (t) \geq 0; v (t) \geq 0. \end{array}
$$

The equilibrium effort levels for both parties when there is self-learning for the vendor are provided in the following lemma.

<sup>Lemma</sup> <sup>3.</sup> If the parties decide to collaborate, and if there is self-learning for the vendor, the equilibrium effort levels for the client and the vendor are

$$
\begin{array}{r l} & u (t) = e ^ {t w \beta / (\gamma (\delta - \beta) - \alpha \delta)} \bigg (\frac {k \alpha (T - t)}{\gamma c _ {c}} \bigg) ^ {\delta / (\gamma (\delta - \beta) - \alpha \delta)} \\ & \qquad \cdot \bigg (\frac {\beta \gamma c _ {c}}{\alpha \delta c _ {0}} \bigg) ^ {\beta / (\gamma (\delta - \beta) - \alpha \delta)}, \\ & v (t) = e ^ {t w (\gamma - \alpha) / (\gamma (\delta - \beta) - \alpha \delta)} \bigg (\frac {k \beta (T - t)}{\delta c _ {0}} \bigg) ^ {\gamma / (\gamma (\delta - \beta) - \alpha \delta)} \\ & \qquad \cdot \bigg (\frac {\alpha \delta c _ {0}}{\beta \gamma c _ {c}} \bigg) ^ {\alpha / (\gamma (\delta - \beta) - \alpha \delta)}. \end{array}
$$

Here, in contrast to the no-learning case, the equilibrium effort levels of both parties do not always decrease with time. In fact, at first they both increase with time and then decrease. Since it becomes gradually less costly for the vendor to spend effort, the vendor increases his effort at the beginning of the collaboration. However, similar to the base model, as the end of the collaboration approaches, he starts decreasing his effort level. The first and second order conditions of effort levels with respect to time reveal that the vendor’s effort has an increasing– decreasing behavior with the reflection point at $t = T - \gamma / ( w ( \gamma - \alpha ) )$ . Here, if $T \leq \gamma / ( w ( \gamma - \alpha ) )$ , then t is greater than $T - \gamma / ( w ( \gamma - \alpha ) )$ even at $t = 0$ . Therefore, the vendor’s effort strictly decreases with time– similar to that in the no-learning scenario. However, when $T \geq \gamma / ( w ( \gamma - \alpha ) )$ , the vendor increases and decreases his effort level with time. Because of this, the client also has incentive to increase and decrease her effort level in accordance with the vendor. This is due to the collaborative nature of the project.

Consideration of the vendor’s learning in the model, however, does not alter the behavior of the other results significantly. Therefore, we treat the cost multiplier for the vendor $\left( \mathrm { i . e . , ~ } c _ { v } \right)$ as a constant in the main analysis. However, we report the results for the vendor’s learning case in each setting and discuss the key differences from the no-learning case. Learning by the vendor could also be enhanced by the client’s level of engagement or with training programs. This might further raise complex double moral hazard issues. Our model can be modified to incorporate these issues as well. However, for brevity, we limit our discussion to the case when the vendor’s effort cost decreases with time due to learning effects. In Section $^ { 3 , }$ we discuss the setting where the effort levels are not monitored and hence are not verifiable.

## 3. Unverifiable Effort Levels

The FB approach assumes that (i) effort levels are verifiable to third parties such as a court and (ii) the single objective of the parties is to maximize the total value in the collaboration. However, in most business settings, effort levels of parties are not verifiable without monitoring, and parties have different and often conflicting objectives. Therefore, a double moral hazard problem arises in many business settings. Accordingly, in this section, we assume that effort levels of both parties are not verifiable if they are not monitored. Note that the client can observe her own effort level and can infer the vendor’s effort by observing the output. However, the client cannot transfer payments based on the vendor’s effort level. The reason is that, in cases of disagreements between the client and the vendor, the parties should be able to “prove” or “verify” (to the other party and to the court) the effort levels they claim they have exerted in the project and also what they think about the effort level of the other party. Therefore, the client offers the vendor a portion of the output and a fixed fee<sup>2</sup> $\begin{array} { r } { ( \mathrm { i . e . , ~ } \int _ { 0 } ^ { T } l q ( t ) \dot { d t } + F _ { d } ) } \end{array}$ Here, l denotes the transfer payment per unit output, and $F _ { d }$ is the fixed fee. The structure of the costs for both client and vendor stays unchanged compared to the FB model. Hence, the objective functions of the client and vendor, and the constraints, can be written $\mathsf { a s } ^ { 3 }$

$$
\max _ {u (t), l, F _ {d}} \left\{\int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t - \int_ {0} ^ {T} l q (t) d t - F _ {d} \right\}
$$

$$
\max _ {v (t)} \left\{\int_ {0} ^ {T} l q (t) d t + F _ {d} - \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta} d t \right\}
$$

subject to $\dot { q } ( t ) = u ( t ) ^ { \alpha } v ( t ) ^ { \beta }$ 3

$$
\begin{array}{l} \int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t \\ \qquad - \int_ {0} ^ {T} l q (t) d t - F _ {d} \geq R _ {c}; \\ \int_ {0} ^ {T} l q (t) d t + F _ {d} - \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta} d t \geq R _ {v}; \\ u (t) \geq 0; v (t) \geq 0. \end{array}
$$

In this setting, the client chooses her equilibrium effort level u4t5 and the vendor chooses his equilibrium effort level v4t5. The first constraint shows the evolution of output through time. The second and third constraints state that the client and vendor will participate in the collaboration only if they receive value more than or equal to their reservation utilities.

The solution of this differential game for a given l reveals the equilibrium effort levels of the parties that is presented in the lemma that follows assuming that the participation constraints hold.

<sup>Lemma</sup> <sup>4.</sup> If the parties find it beneficial to collaborate and if the effort levels are not monitored, the equilibrium effort levels for the client and the vendor are

$$
\begin{array}{l} u (t) = \bigg ((T - t) ^ {\delta} \bigg (\frac {l \beta}{\delta c _ {v}} \bigg) ^ {\beta} \bigg (\frac {(k - l) \alpha}{\gamma c _ {c}} \bigg) ^ {\delta - \beta} \bigg) ^ {1 / ((\gamma - \alpha) \delta - \beta \gamma)}, \\ v (t) = \bigg ((T - t) ^ {\gamma} \bigg (\frac {l \beta}{\delta c _ {v}} \bigg) ^ {\gamma - \alpha} \bigg (\frac {(k - l) \alpha}{\gamma c _ {c}} \bigg) ^ {\alpha} \bigg) ^ {1 / ((\gamma - \alpha) \delta - \beta \gamma)}. \end{array}
$$

As we show in the proof of this lemma, the solution is a degenerate feedback Nash equilibrium solution. Therefore, the solution is subgame perfect by construction (Selten 1975). Players that choose feedback decision rules do not commit to a predetermined control path before they begin interacting. Rather, they utilize control recipes that allow them to react to different output levels they might observe (i.e., q4t5 may be higher or lower than expected, because the other party may extract more effort than expected or shirk) (Sorger 1989). As Sorger (1989) states, the subgame perfect equilibrium implies that the solution provides credible threats, because no player can benefit from deviating from his announced strategy. In our solution, since the equilibrium is degenerate (i.e., effort trajectories are not functions of the state variable q4t5), the solution is the same for any observed level of the output variable.

Effort levels of both parties are strictly concave and decreasing in time due to Remark 1 that is provided in the online appendix. In addition, both effort levels converge to zero at the project completion time. In the next subsection, we derive the optimal payment terms based on Lemma 4.

## 3.1. Optimal Payment Terms

The client has no incentive to leave the vendor any value more than what is needed to make him participate in the collaboration. Hence, the client makes the vendor’s participation constraint binding. Therefore, $\begin{array} { r } { F _ { d } = - \int _ { 0 } ^ { T } \dot { l q } ( t ) d \dot { t } + \int _ { 0 } ^ { T } c _ { v } v ( t ) ^ { \delta } d t + R _ { v } } \end{array}$ . After substituting $F _ { d }$ and the equilibrium effort levels provided in Lemma 4 into the objective function of the client, it is easy to observe that the client’s value is concave in l. Therefore, the first and second order conditions with respect to l reveal the optimal payment terms that we present in Lemma 5.

<sup>Lemma</sup> <sup>5.</sup> If the parties find it beneficial to collaborate and if the effort levels are not monitored, the optimal payment per unit output, and the fixed payment terms are given by

$$
l ^ {*} = k \frac {\beta (\gamma - \alpha) - \sqrt {\alpha \beta (\gamma - \alpha) (\delta - \beta)}}{\beta \gamma - \alpha \delta},
$$

$$
\begin{array}{r l} & F _ {d} ^ {*} = T ^ {((2 \gamma - \alpha) \delta - \beta \gamma) / ((\gamma - \alpha) \delta - \beta \gamma)} \frac {(\gamma - \alpha) \delta - \beta \gamma}{(2 \gamma - \alpha) \delta - \beta \gamma} l ^ {*} \\ & \qquad \cdot \left(\left(\frac {(k - l ^ {*}) \alpha}{\gamma c _ {c}}\right) ^ {\alpha \delta} \left(\frac {l ^ {*} \beta}{\delta c _ {v}}\right) ^ {\beta \gamma}\right) ^ {1 / ((\gamma - \alpha) \delta - \beta \gamma)} \\ & \qquad \cdot \left(\frac {\beta - \delta}{\delta}\right) + R _ {v}. \end{array}
$$

By setting the payment terms l and $F _ { d }$ to the levels presented in Lemma 5, the client maximizes the total value in the system and her utility. This is because the vendor receives only his reservation utility irrespective of the other parameter values. It is an interesting finding that the optimal payment term $l ^ { * }$ does not depend on the cost-per-unit effort terms for either party $( \mathrm { i . e . , ~ } c _ { c } \ \mathrm { ~ o r ~ } c _ { v } )$ . We show in the proof of this lemma that $l ^ { * }$ is between 0 and $k ,$ hence we can think of $l ^ { * } / k$ as the optimal share. The output elasticity terms ( and $\beta \bar { ) }$ , as well as the cost elasticity terms $( \gamma$ and $\delta ) ,$ might be similar across different settings. Therefore, in a given industry or even across different industries, we would expect to see common share terms (e.g., 50%–50%, or $6 0 \% \mathrm { - } 4 0 \% )$ in revenuesharing settings irrespective of the participation costs of the parties and the client’s valuation of the project. This fact is actually evidenced in Bhattacharyya and Lafontaine (1995), and we complement their finding in a continuous value co-creation setting. On the other hand, the fixed payment term $F _ { d } ^ { * }$ depends on the cost-per-unit effort terms for both parties. Therefore, we would expect more variability in this fixed term. This finding is also observed in real business settings (Bhattacharyya and Lafontaine 1995).

Since the optimal payment term $l ^ { * }$ is insensitive to the per-unit cost terms $( c _ { c }$ and $c _ { v } ) .$ , we summarize the behavior of $l ^ { * }$ with respect to the other relevant parameters in the next proposition.

<sup>Proposition</sup> <sup>1.</sup> The optimal payment term $l ^ { * }$ strictly decreases with  and $\delta ,$ and strictly increases with $\beta$ and $\gamma .$

Proposition 1 implies that if the output becomes more sensitive to the client’s effort $( \mathrm { i . e . , }$ if  increases) or if the vendor’s marginal cost parameter increases $( \mathrm { i . e . } , \ \mathrm { i f } \delta$ increases), the optimal payment term decreases. This result can be explained as follows. As  increases, the ratio of output sensitivity to cost sensitivity with respect to the client’s effort $( \mathrm { i } . \mathrm { e } . , \ \alpha / \gamma )$ increases. In effect, this ratio represents the client’s productivity. Similarly, $\beta / \delta$ represents the vendor’s productivity. Therefore, as either  or  increases, the relative productivity of the client (i.e., $( \alpha / \gamma ) / ( \beta / \delta ) )$ increases. Hence, the client tends to exert relatively more effort in the collaboration. In other words, the client attempts to reduce the effort level of the vendor that is achieved by reducing the payment term. Using a similar argument, if the output becomes more sensitive to the vendor’s effort (i.e., if $\beta$ increases) or if the client’s marginal cost parameter increases $( \mathrm { i . e . , }$ if  increases), the relative productivity of the vendor increases. Hence, in this case, it is beneficial for the client to increase the optimal payment term to entice the vendor to work more in the collaboration.

## 3.2. Behavior of Effort Levels

Using the results in Lemmas 4 and 5, we can easily characterize the effort levels of both parties in the double moral hazard case. We find that the efforts of both parties increase with $k$ and decrease with $c _ { c }$ or $c _ { v } .$ Let us first explain this result. The client increases her effort level with an increase in the valuation of the project $( \mathrm { i . e . , ~ } k )$ to increase the output. Hence, because of the complementary nature of the project, the vendor also increases his effort. On the other hand, the client reduces her effort level when her cost-per-unit effort $( \mathrm { i } . \mathrm { e } . , \ c _ { c } )$ increases to reduce her effort cost. Again, because of the complementarity, the vendor also decreases his effort. Finally, the impact of the vendors’ cost-per-unit effort $( \mathrm { i } . \mathrm { e } . , c _ { v } )$ can be explained in a similar manner. Now, in the next proposition, we present the impacts of output sensitivity parameters and marginal cost terms on the effort levels of the parties. Note that the threshold values in Proposition 2 and all of the subsequent propositions are provided in the online appendix.

<sup>Proposition</sup> <sup>2.</sup> In the output dependent structure:

(a) With an increase in output elasticity to the client’s effort $( i . e . , \alpha ) .$ , the client’s effort increases iff $k > O _ { \alpha c }$ and the vendor’s effort increases iff $k > O _ { \alpha v } ,$

(b) With an increase in output elasticity to the vendor’s effort $( i . e . , \beta )$ , the client’s effort increases iff $k > O _ { \beta c }$ and the vendor’s effort increases $i f f k > O _ { \beta v } ,$

(c) With an increase in cost elasticity to the client’s effort $( i . e . , \gamma ) .$ , the client’s effort decreases iff $k > O _ { \gamma c }$ and the vendor’s effort decreases $i f f \ k > O _ { \gamma v } .$

(d) With an increase in cost elasticity to the vendor’s effort $( i . e . , \delta )$ , the client’s effort decreases $i f f \ k > O _ { \delta c }$ and the vendor’s effort decreases iff $k > O _ { \delta v }$

Let us begin with analyzing part (a) of Proposition 2. When the output elasticity to the client’s effort $( \mathrm { i } . \mathrm { e } . , \alpha )$ increases, the output improves at a faster rate with an increase in client’s effort (see Equation (2)). As a result, the client has an incentive to increase her effort level when  increases. Moreover, because of the complementary effort levels, the vendor has an incentive to increase his effort level as well. However, increasing their effort levels is costly for both parties. Hence, they need to consider the trade-off between the benefit and the cost of increased efforts. Since the benefit of increased output is higher for highvaluation projects (see Equation (1)), both the client and the vendor increase their effort levels when  increases in such projects. Part (b) of Proposition $2$ can be explained in a similar manner.

Furthermore, as the time passes in the collaboration, the benefit of increased effort reduces. Hence, toward the end of the project, it is less beneficial for the parties to increase their efforts even for the high-valuation projects. As a result, we find that the threshold levels in the proposition increase with the time elapsed in the collaboration and approach infinity at the end of the project. This implies that, at the later stages of collaboration, both parties decrease their effort levels as  increases, irrespective of the valuation of the output. In particular, if $\dot { k } < ( ( T - t ) / T ) O _ { \alpha c }$ (respectively, $\bar { k } <$ $( ( T - t ) / T ) O _ { \alpha v } ) .$ , the client’s (respectively, the vendor’s) effort level decreases in  throughout the collaboration. Otherwise, the client’s (respectively, the vendor’s) effort level first increases, then decreases in 0 Note that all of the thresholds in Proposition 2 have similar properties with respect to time, but we omit the details for brevity.

Next, part (c) of Proposition 2 states that both parties decrease their effort levels with an increase in cost elasticity to the client’s effort $( \mathrm { i . e . , ~ } \gamma )$ for highvaluation projects. In such projects, the client’s effort level is comparatively high and therefore her cost increases at a faster rate with . As a result, the client has an incentive to reduce her effort level with an increase in $\gamma$ despite the fact that the reduced effort level decreases the output. Consequently, the vendor reduces his effort level as well. Finally, as the cost elasticity to the vendor’s effort (i.e., ) increases, it becomes costlier for the vendor to exert more effort. As a result, the vendor has an incentive to reduce his effort level with an increase in . In turn, the client also has an incentive to decrease her effort level. However, the decrease in effort levels of both parties also decreases the output. Hence, as explained in the discussion of part (a) of Proposition 2, the effort levels of both parties decrease with an increase in  only for the high-valuation projects.

Part (a) (respectively, part (b)) of Proposition 2 indicates that, if it is possible to increase the relative responsibility of the client (respectively, the vendor) in the project (possibly in the design stage of the project), then the parties may need to increase or decrease their effort levels. Hence, if there are already constraints or limitations on the workforce levels, the parties should be cautious and be prepared for the changes in the relative responsibility levels. Furthermore, parts (c) and (d) of Proposition 2 highlight that the parties should not always increase their effort levels if the effort becomes less costly. The project environment, in particular the unit value of output, determines how the client and the vendor should respond to changes in the costliness of effort levels.

## 3.3. Client’s Net Value

Given the optimal payment terms in Lemma $5 ,$ we can calculate the client’s value that is presented below.

<sup>Lemma</sup> <sup>6.</sup> If the parties find it beneficial to collaborate and $i f$ the effort levels are not monitored, the client’s net value is

$$
\begin{array}{r l} & T ^ {((2 \gamma - \alpha) \delta - \beta \gamma) / ((\gamma - \alpha) \delta - \beta \gamma)} \frac {(\gamma - \alpha) \delta - \beta \gamma}{(2 \gamma - \alpha) \delta - \beta \gamma} \\ & \quad \cdot \left(\left(\frac {(k - l ^ {*}) \alpha}{\gamma c _ {c}}\right) ^ {\alpha \delta} \left(\frac {l ^ {*} \beta}{\delta c _ {v}}\right) ^ {\beta \gamma}\right) ^ {1 / ((\gamma - \alpha) \delta - \beta \gamma)} \\ & \quad \cdot \left(k - \frac {(k - l ^ {*}) \alpha}{\gamma} - \frac {l ^ {*} \beta}{\delta}\right) - R _ {v}, \\ & \qquad w h e r e l ^ {*} = k \frac {\beta (\gamma - \alpha) - \sqrt {\alpha \beta (\gamma - \alpha) (\delta - \beta)}}{\beta \gamma - \alpha \delta}. \end{array}
$$

In Section $5 ,$ we analyze the behavior of the client’s net value presented above and compare it with that in the FB solution and in the setting discussed in Section 4. Now, in the next subsection, we study the case where the vendor has self-learning.

## 3.4. Self-Learning of Vendor

As Lemma 4 suggests, the effort levels of both parties decrease with time. However, it may not be true when the vendor’s participation cost decreases with time due to self-learning. Hence, in this subsection, we analyze the scenario with self-learning of the vendor. As in the self-learning case of the FB scenario, for a given learning rate w, we model the change in the cost-per-unit effort for the vendor as $\dot { c } _ { v } ( t ) = - w c _ { v } ( t )$ We take the starting level of the vendor’s participation cost $( \mathrm { i } . \mathbf { e } . , c _ { v } ( 0 ) )$ as $c _ { 0 } . \mathrm { \ : S o } ,$ , the main difference from the base model is the objective function of the vendor that is presented below

$$
\max _ {v (t)} \left\{\int_ {0} ^ {T} l q (t) d t + F _ {d} - \int_ {0} ^ {T} c _ {0} e ^ {- w t} v (t) ^ {\delta} d t \right\}.
$$

The equilibrium effort levels for both parties can be calculated easily (not reported for brevity). Unlike in the no-learning case examined in the previous subsections, these effort levels do not necessarily decrease in time. The reason is that, since it becomes gradually less costly for the vendor to spend effort, the vendor increases his effort at the beginning of the collaboration. Because of the collaborative nature of the project, the client increases her effort as well. Hence, the parties create more output, which in turn results in a higher payment to the vendor. However, toward the end of the collaboration, both parties start decreasing their effort levels as they do in the no-learning case. Now, in Section 4, we present the model when the effort level of the vendor is observed.

## 4. Monitoring Vendor’s Effort

If the effort levels of both parties are not verifiable, the client has a double moral hazard problem as analyzed in the previous section. However, as discussed in Section 2.1, in some settings, the vendor’s effort can be made verifiable through IT systems, regular meetings, site visits, submitting of progress reports, etc. The cost for making the vendor’s effort verifiable via monitoring has a fixed portion $F _ { m }$ as well as a variable part $c _ { m } v ( t ) ^ { \delta }$ , as discussed in Section 2.1. This formulation represents various scenarios for the monitoring cost, because the magnitude of the rate of change of total monitoring cost with respect to the vendor’s effort level can be adjusted by changing the value of $F _ { m } .$ . In addition, considering a power term other than  does not change the key insights of the paper. In this setting, we consider that the vendor assumes the monitoring costs. However, we show later that the allocation of the monitoring costs between the client and the vendor does not affect the maximum value that can be generated by the parties. In the next subsection, we present the game played between the parties.

## 4.1. Game Between the Parties When the Vendor’s Effort Is Monitored

In this model, similar to that in Section 3, we have a fixed payment term $( F _ { v } )$ and a variable payment term $\begin{array} { r l r } {  { ( \int _ { 0 } ^ { T } p \bar { v ( t ) ) } } } \end{array}$ that depends on the total effort exerted by the vendor. Here, p is the payment per level of vendor effort. Hence, the objective functions of the client and vendor, the expression that represents the evolution of the output, and the participation constraints can be written as

$$
\begin{array}{c} \max _ {u (t), p, F _ {v}} \left\{\int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t \right. \\ \left. - F _ {v} - \int_ {0} ^ {T} p v (t) \right\} \end{array}\tag{7}
$$

$$
\begin{array}{c} \max _ {v (t)} \left\{F _ {v} + \int_ {0} ^ {T} p v (t) - \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta} d t \right. \\ \left. - \int_ {0} ^ {T} c _ {m} v (t) ^ {\delta} d t - F _ {m} \right\} \end{array}\tag{8}
$$

subject to

(9)

$$
\dot {q} (t) = u (t) ^ {\alpha} v (t) ^ {\beta};\tag{10}
$$

$$
\begin{array}{l} \int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t - F _ {v} \\ - \int_ {0} ^ {T} p v (t) \geq R _ {c}; \end{array}\tag{11}
$$

$$
F _ {v} + \int_ {0} ^ {T} p v (t) - \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta} d t
$$

$$
- \int_ {0} ^ {T} c _ {m} v (t) ^ {\delta} d t - F _ {m} \geq R _ {v};\tag{12}
$$

$$
u (t) \geq 0; v (t) \geq 0.\tag{13}
$$

The client maximizes her value by optimizing the effort trajectory u4t5 throughout the planning horizon, as well as p and $F _ { v } .$ Similarly, the vendor optimizes his effort trajectory v4t5 for all t. We first obtain the equilibrium effort levels, the optimal levels of payment terms $F _ { v }$ and $p ,$ and the net values of both parties. These results are presented in the online appendix. We find that this payment structure does not generate the maximum value to the client. In other words, the value of the client in this setting is less than that in the FB case minus the monitoring cost. In effect, the performance of this payment structure suffers not only from the costs pertaining to monitoring but also from the fact that the client and the vendor have rather different objectives—the parties play a game. Hence, in the next subsection, we analyze another payment structure with the goal of improving the value to the client.

## 4.2. Optimal Payment Structure When the Vendor’s Effort Is Monitored

In this subsection, we show that the client can align the two separate objectives of the parties by designing a payment structure that eliminates any game played between the parties. This is possible because the client is able to verify the vendor’s effort level, which allows her to prescribe the vendor’s effort throughout the collaboration. We write the objective functions of the client and the vendor, and the constraints, as below, where H 4 · 5 denotes the payment structure

$$
\begin{array}{l l} \max _ {u (t), H (\cdot)} & \left\{\int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t - H (\cdot) \right\} \\ \max _ {v (t)} & \left\{H (\cdot) - \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta} d t - \int_ {0} ^ {T} c _ {m} v (t) ^ {\delta} d t - F _ {m} \right\} \\ \text {subject to} & \dot {q} (t) = u (t) ^ {\alpha} v (t) ^ {\beta}; \\ & \int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t - H (\cdot) \geq R _ {c}; \\ & H (\cdot) - \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta} d t \\ & - \int_ {0} ^ {T} c _ {m} v (t) ^ {\delta} d t - F _ {m} \geq R _ {v}; \\ & u (t) \geq 0;   v (t) \geq 0. \end{array}
$$

By analyzing the above system, we can derive the best payment structure where the client covers the vendor’s total cost and reservation utility if the vendor exerts more effort than a threshold. Hence, this payment structure is similar to a tit-for-tat strategy. Such payment structures are also used in practice—e.g., in research projects (see, e.g., http://www.acq.osd.mil/osbp/sbir/docs/ GenFFP.pdf) and government contracts (see, e.g., https://www.law.cornell.edu/cfr/text/48/part-16).

<sup>Proposition</sup> <sup>3.</sup> When the vendor’s effort is monitored, the optimal payment term is as follows:

$$
H (\cdot) = \left\{ \begin{array}{l l} \int_ {0} ^ {T} c _ {v} \bar {v} (t) ^ {\delta} d t + \int_ {0} ^ {T} c _ {m} \bar {v} (t) ^ {\delta} d t + F _ {m} + R _ {v}, \\ \quad \text {   if   } v (t) \geq \bar {v} (t), \\ 0, & \text {   if   } v (t) <   \bar {v} (t). \end{array} \right.
$$

Here, v4t5 ¯ is the value $o f v ( t )$ in the solution of Problem P presented below.

Problem P:

$$
\begin{array}{l} \max _ {u (t), v (t)} \int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t \\ \qquad - \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta} d t - \int_ {0} ^ {T} c _ {m} v (t) ^ {\delta} d t - F _ {m} \end{array}
$$

subject to ${ \dot { q } } ( t ) = u ( t ) ^ { \alpha } v ( t ) ^ { \beta } ;$

$$
\begin{array}{l} \int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t - \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta} d t \\ \qquad - \int_ {0} ^ {T} c _ {m} v (t) ^ {\delta} d t - F _ {m} \geq R _ {c} + R _ {v}; \\ u (t) \geq 0; v (t) \geq 0. \end{array}
$$

Since the client can set the payment structure based on the vendor’s effort, she ensures that the vendor’s effort level is such that it maximizes the total net value in the system. Therefore, v4t5¯ is the solution of the following system that considers both parties as a unified firm. The client chooses her effort level as a best response to the vendor’s effort $v ( t )$ and covers only the effort cost of the vendor and the costs related to monitoring in addition to his reservation utility. Hence, the client claims all of the net value in the collaboration. This is the reason why the allocation of the monitoring cost (between the client and the vendor) does not affect the total value generated in the collaboration. Based on this discussion, we now present the following corollary.

<sup>Corollary</sup> <sup>1.</sup> The optimal payment structure presented in Proposition 3 always yields more value to the client compared to that in the payment structure analyzed in Section 4.1.

Based on the result of Corollary 1, when the vendor’s effort is monitored, we analyze the results only for the case when a contact is written between the parties. Now, by solving Problem P, it is easy to derive the equilibrium effort levels of the parties that are presented in Lemma 7. Obviously, if the value generated is less than the total of the reservation utility terms $( \mathrm { i } . \mathrm { e } . , R _ { c } + R _ { v } )$ , the parties do not collaborate.

<sup>Lemma</sup> <sup>7.</sup> When the vendor’s effort is monitored, the equilibrium effort levels for the client and the vendor are

$$
\begin{array}{l} u (t) = \bigg (\frac {k (T - t) \alpha}{\gamma c _ {c}} \bigg) ^ {\delta / (\gamma (\delta - \beta) - \alpha \delta)} \bigg (\frac {\beta \gamma c _ {c}}{\alpha \delta (c _ {v} + c _ {m})} \bigg) ^ {\beta / (\gamma (\delta - \beta) - \alpha \delta)}, \\ v (t) = \bigg (\frac {k (T - t) \beta}{\delta (c _ {v} + c _ {m})} \bigg) ^ {\gamma / (\gamma (\delta - \beta) - \alpha \delta)} \bigg (\frac {\alpha \delta (c _ {v} + c _ {m})}{\beta \gamma c _ {c}} \bigg) ^ {\alpha / (\gamma (\delta - \beta) - \alpha \delta)}. \end{array}
$$

The equilibrium level of the client’s effort $( \mathrm { i } . \mathrm { e } . , u ( t ) )$ presented in Lemma 7 is strictly concave and decreasing with time. In the next subsection, we study the behavior of effort levels in more detail.

## 4.3. Behavior of Effort Levels

In this subsection, we analyze the impacts of different characteristics of the client and the vendor on the effort trajectories presented in Lemma 7. We begin with studying the impacts of $c _ { c } , \ c _ { v } ,$ and k on the effort levels. Clearly, with an increase in the valuation of the project $( \mathrm { i . e . , ~ } k )$ , the client increases her effort level to generate more output. This entices the vendor to increase his effort level as well. Thus, the effort levels of both parties increase with k. Next, when exerting effort becomes less costly for the client $( \mathrm { i } . \mathrm { e } . , c _ { c }$ decreases), the client increases her effort level, and therefore the vendor also increases his effort. Similarly, for the vendor, when either the unit effort cost $( \mathrm { i } . \mathrm { e } . , \ c _ { v } )$ or the cost of monitoring effort $( \mathrm { i . e . , } ~ c _ { m } )$ decreases, he increases his effort level. As a result, the client also increases her effort level. These results are somewhat expected. Now, in the following proposition, we present some other results that are not very intuitive. These results provide useful insights for the managers of both firms.

<sup>Proposition</sup> <sup>4.</sup> When the vendor’s effort level is monitored:

(a) With an increase in output elasticity to the client’s effort $( i . e . , \alpha )$ , the client’s effort increases iff $k > E _ { \alpha c }$ and the vendor’s effort increases iff $k > E _ { \alpha v }$

(b) With an increase in output elasticity to the vendor’s effort $( i . e . , \beta )$ , the client’s effort increases $i f f k > E _ { \beta c }$ and the vendor’s effort increases iff $k > E _ { \beta v } .$

(c) With an increase in cost elasticity to the client’s effort $( i . e . , \gamma )$ , the client’s effort decreases $i f f \ k > E _ { \gamma c }$ and the vendor’s effort decreases iff $k > E _ { \gamma v } .$

(d) With an increase in cost elasticity to the vendor’s effort $( i . e . , \delta ) .$ , the client’s effort decreases $i f f \ k > E _ { \delta c }$ and the vendor’s effort decreases iff $k > E _ { \delta v }$

The output improves at a faster rate with an increase in the client’s effort when the output elasticity to the client’s effort $( \mathrm { i } . \mathrm { e } . , \ \alpha )$ increases (see Equation (2)). As a result, the client has an incentive to increase her effort level for the purpose of improving output when  increases. Subsequently, the client tends to request more effort from the vendor by utilizing the payment structure presented in Proposition 3. However, increased efforts increase the participation costs of the client and the vendor in the collaboration. Therefore, the client should consider the tradeoff between the benefits and the costs of increased efforts. Since the benefit of increased output is higher for high-valuation projects (see Equation (1)), both parties increase their effort levels with  for such projects. In addition, the benefit of increased effort reduces in the later stages of the collaboration. Thus, the client has less incentive to increase her effort even for the high-valuation projects toward the end of the project. In effect, we find that $E _ { \alpha c }$ increases in time and approaches infinity at the end of the project. Therefore, irrespective of her valuation of the output, the client decreases her effort level as  increases at the later stages of collaboration. We would like to note that all of the thresholds in Proposition 4 have similar properties with respect to time. Other parts of the proposition can be explained similarly. Hence, we do not repeat the discussion for brevity.

Proposition 4 helps us glean several managerial insights. For example, even though the parties collaborate in a more transparent setting due to monitoring, increasing the sensitivity of the project output to one party’s effort does not necessarily increase the effort of that party. Hence, the parties should be cautious in their workforce planning when changing responsibility levels. Moreover, as it is the case in the double moral hazard setting, because of the time dependence of the thresholds in the proposition, parties should decrease their effort levels more toward the end of the project if the project output becomes more sensitive to the effort level of either party.

## 4.4. Client’s Net Value

Given the equilibrium effort levels presented in Lemma 7 and the payment structure presented in Proposition 3, we can derive the net value of the client that is presented below. By design of the payment structure, the vendor receives only his reservation utility.

<sup>Lemma</sup> <sup>8.</sup> When the vendor’s effort is monitored, the client’s net value is

$$
\begin{array}{l} \frac {T (\gamma (\delta - \beta) - \alpha \delta) ^ {2}}{((2 \gamma - \alpha) \delta - \beta \gamma) \gamma \delta} (k T) ^ {\gamma \delta / (\gamma (\delta - \beta) - \alpha \delta)} \\ \cdot \left(\left(\frac {\alpha}{c _ {c} \gamma}\right) ^ {\alpha \delta} \left(\frac {\beta}{(c _ {v} + c _ {m}) \delta}\right) ^ {\beta \gamma}\right) ^ {1 / (\gamma (\delta - \beta) - \alpha \delta)} - F _ {m} - R _ {v}. \end{array}
$$

In the next subsection, we analyze the case when there is self-learning of the vendor.

## 4.5. Self-Learning of Vendor

As Lemma 7 suggests, the effort levels of both parties decrease with time. However, this is not necessarily true when the vendor’s participation cost decreases with time due to self-learning. As in the earlier models with self-learning, for a given learning rate w, we model the change in the cost-per-unit effort for the vendor as $\dot { c } _ { v } ( t ) = - w c _ { v } ( t )$ 0 The main difference from the base model is the objective function of the vendor that is presented below

$$
\max _ {v (t)} \left\{H (\cdot) - \int_ {0} ^ {T} c _ {0} e ^ {- w t} v (t) ^ {\delta} d t - \int_ {0} ^ {T} c _ {m} v (t) ^ {\delta} d t - F _ {m} \right\}.
$$

In the above objective function, we denote the starting level of the effort cost of the vendor $\left( \mathrm { i } . \mathbf { e } . , \ c _ { v } ( 0 ) \right)$ as $c _ { 0 }$ 0 We do not provide the details of the payment structure that coordinates this system for brevity. However, our analysis reveals that the effort levels do not necessarily decrease in time unlike in the nolearning case examined earlier. The reason is that, since it becomes gradually less costly for the vendor to spend effort as he gains experience in the collaboration, the client increases her own effort knowing that the vendor will increase his effort because of the collaborative nature. Hence, they can generate more output in a less costly manner. Next, we analyze the behavior of the client’s value and several other results in Section 5.

## 5. Further Discussion and Managerial Insights

In this section, we discuss our findings and outline managerial insights regarding (i) how the value generated in the collaboration is affected by different characteristics of the parties and (ii) the client’s choice of payment structure under different circumstances.

## 5.1. Client’s Net Value

When the effort levels are not observed, the client utilizes an output dependent payment structure as discussed in Section 3. On the other hand, the effort level of the vendor is monitored in Section 4, where an effort dependent payment structure is used. In this subsection, we present the results and insights that are similar for both settings. First, with the help of the fixed fee, the client extracts all value from the collaboration, leaving the vendor only his reservation utility. Hence, we use the client’s value and total value interchangeably in this section. Next, it is easy to observe from Lemmas 6 and 8 that the client’s value increases with the valuation of the project $( \mathrm { i . e . , ~ } k )$ and decreases with the cost-per-unit effort of the parties $( \mathrm { i . e . , ~ } c _ { c }$ and $c _ { v } )$ . In addition, the client’s value decreases with the parameters related to monitoring the vendor’s effort $( \mathrm { i . e . , ~ } c _ { m }$ and $F _ { m } )$ if his effort is monitored. Clearly, these results are intuitive. Now we present some other results that might be regarded as counterintuitive. First, Proposition $^ 5$ discusses how the client’s value is affected by the output sensitivity to effort levels.

<sup>Proposition</sup> <sup>5.</sup> In both output dependent and effort dependent payment structures, when the output sensitivity to the client’s $o r$ vendor’s effort $( i . e . , \alpha \ o r \ \beta )$ is low, an increase in the same output sensitivity decreases the net value of the client

$$
\frac {d (C l i e n t ^ {\prime} s V a l u e)}{d \alpha} <   0 \quad w h e n \alpha i s l o w, \quad a n d
$$

$$
\frac {d (C l i e n t ^ {\prime} s V a l u e)}{d \beta} <   0 \quad w h e n \beta i s l o w.
$$

Intuitively, if the output becomes more sensitive to the effort level of either party, the client’s net value should increase. However, as shown in Proposition $5 ,$ when the relative responsibility in the generation of the output is low for either the client $( \mathrm { i } . \mathrm { e } . , \alpha$ is low) or the vendor $( \mathrm { i . e . , ~ } \beta$ is low), then increasing the responsibility of the same party does not necessarily increase the client’s value (or total value). However, after the sensitivity increases substantially, the value starts to increase. This result is illustrated using two examples in Figure 2. In Figure 2, we consider a scenario where the effort level of the vendor is monitored with the following parameter values: $T = 1 0 , \ \gamma = 3 ,$ $\delta = 2 . 5 , \ k = 1 0 , \ c _ { c } = 2 , \ c _ { v } = 1 . 2 ,$ , and $c _ { m } = 0 . 3$ . These values are reasonable in the sense that the vendor’s cost parameters are less than those of the client, i.e., $\delta < \gamma$ and $c _ { v } < c _ { c }$ . Furthermore, the value of $\beta$ is 0.8 in Figure $2 ( \mathsf { a } ) .$ , and the value of  is 0.5 in Figure $2 ( \mathrm { b } ) . ^ { 4 }$

In Figures 2(a) and 2(b), the client’s net value increases with the sensitivity parameters only if these parameters are not low. Recall that as the sensitivity to the client’s effort $( \mathrm { i } . \mathrm { e } . , \alpha )$ increases, the effort levels may increase or decrease (see Propositions 2 and 4). Let us first consider the scenario when the effort levels increase with . Note that the client’s value increases in output $( \mathrm { i . e . , } \ k u ^ { \alpha } v ^ { \beta } )$ and decreases in effort costs $( \mathrm { i } . \mathrm { e } . , c _ { c } u ^ { \gamma }$ and $c _ { v } v ^ { \delta } )$ . When  is low, to have a considerable increase in output, the client’s effort level needs to improve substantially. Hence, when $\alpha$ is low, with an increase in $\alpha ,$ the value of incremental increase in output (because of the client’s increased effort) is less than the costs of increased efforts. On the other hand, when  is not low, since the output is relatively more sensitive to the effort levels, the value of incremental increase in output (because of increased efforts) is more than the cost of increased effort for the client. A similar argument exists for the case where the client’s effort decreases with $\alpha .$ Hence, as shown in Figure $2 ( \mathsf { a } )$ , when $\alpha$ is low, the client’s net value decreases with $\alpha ,$ but the reverse is true at the higher values of $\alpha .$ The behavior with respect to $\beta$ (in Figure 2(b)) can be explained in a similar manner. These results indicate that the client needs to be very careful when increasing the responsibility level of either party in the project. To maximize her value, the client should ensure that when the responsibility of a party is low in the collaboration, the responsibility level either remains the same or increases substantially.

## 5.2. Comparison with the First Best

The FB approach assumes that the client and the vendor act as a single firm. In addition, it is assumed that the effort levels are verifiable without incurring any monitoring cost. Hence, the FB approach presents the maximum value that can be generated in the collaboration. In this subsection, we examine how the payment structures compare with the FB case under different circumstances. We start with the output dependent payment structure that is utilized in the double moral hazard setting.

5.2.1. Performance of the Output Dependent Payment Structure. First, we conduct a numerical study to analyze how the percentage difference in the client’s value (between the FB scenario and the output dependent payment structure) changes with the output sensitivity parameters  and $\beta .$ In this study, we find that as the output becomes more sensitive to the effort of either party, the percentage difference increases. In other words, the disadvantage of the unverifiable effort levels amplifies when the output becomes more sensitive to the effort of either party. This is attributed to the fact that the client faces a more severe double moral hazard problem when the output becomes more sensitive to the effort of either party. The details of this numerical study are omitted for brevity, but we summarize the finding in the following observation.

<sup>Observation</sup> <sup>1.</sup> The percentage difference in the client’s value between the FB scenario and the output dependent payment structure increases as the output becomes more sensitive to either the client’s effort or the vendor’s effort $( \mathrm { i . e . , }$ either  or $\beta$ increases).

We next analyze a scenario where the total of the sensitivity parameters $( \mathrm { i . e . , ~ } \alpha + \beta ) .$ , is kept constant, instead of keeping one sensitivity parameter constant while varying the other. Changing the sensitivity parameters while keeping their total constant can

## Figure 2 (Color online) Impact of the Output Elasticity Parameters on Client’s Value

(a) Net value with output elasticity to client’s effort  
![](/api/attachments/FBDJC6YJ/fulltext/images/768a880b650286e008f104c1b8c09278c39c25b5479daa7faeb4a178b7112478.jpg)  
be thought of as a shift in the assignment of responsibilities between the parties in the generation of the output. This analysis is presented in Figure 3 with $k = 1 2 ,$ $T = 1 0 ,$ $\gamma = 1 . 9 ,$ $\hat { \delta } = 1 . 7 ,$ $c _ { c } = 2 ,$ $c _ { v } = 1 . 6 ,$ and $\alpha + \beta = 0 . 9 .$ . Figure 3(a) shows that the client’s value is higher when the output sensitivity is comparatively higher to either party’s effort (i.e., higher  or $\beta )$ compared to the case where the output is almost equally sensitive to the efforts of both parties $( \mathrm { i } . \mathrm { e } . , \alpha \approx \beta )$ . In other words, when a single party assumes most of the responsibility in the collaboration, the client’s value is higher. This result serves for comparative purposes, because depending on the nature of the project and the characteristics of the parties, it may not be possible to shift the sensitivity of the output dramatically toward any of the parties in the design phase of the project. Therefore, the important insight here is the fact that the client’s net value would be higher in projects where the output depends more on the effort level of a single party. Moderate responsibilities for both parties in the generation of the output might not be in the best interest of the client in the output dependent payment structure. We summarize this finding below.

<sup>Observation</sup> <sup>2.</sup> In the output dependent payment structure, the client’s value is higher when the output sensitivity is comparatively higher to either party’s effort (i.e., higher  or $\beta )$ compared to the case when the output is almost equally sensitive to the efforts of both parties $( \mathrm { i . e . , } \alpha \approx \bar { \beta } )$ ).

Figure 3(a) does not provide any intuition regarding how the output dependent payment structure compares with the FB and whether the decreasing– increasing behavior is due to the game that is played between the parties. Therefore, in Figure 3(b), we present the percentage difference in the client’s net value between the FB case and the output dependent payment structure (while keeping $\alpha + \beta$ constant) with the same parameter values as in Figure 3(a).

(b) Net value with output elasticity to vendor’s effort  
![](/api/attachments/FBDJC6YJ/fulltext/images/b4465ca09d986c5b827984579641cf737cea18fc34512d52c4807cec7aea7496.jpg)

Based on the finding in Observation 1, we may expect that as the output becomes more sensitive to the vendor’s effort $( \mathrm { i . e . , }$ as $\beta$ increases), the client will face a more severe double moral hazard problem. Therefore, one may conclude that the performance difference between the FB case and the output dependent payment structure increases with $\beta .$ However, as Figure 3(b) suggests, this intuition is not always correct. When the output depends more on either party’s effort (i.e., either  or $\beta$ is high), the performance difference between the payment structures is less. This result can be explained as follows. When the responsibility of one party is high and the other party is low (represented by both ends of the graph), the client has a “one-sided” moral hazard problem. Hence, in these cases, the performance of the output dependent payment structure is better. However, when the output depends on both parties’ efforts, the client faces a “double” moral hazard problem. Therefore, the output dependent payment structure performs worst around the middle of the horizontal axis in the figure. We conduct additional numerical experiments and find that the percentage differences between the payment structures do not depend on $k ,$ T , $c _ { c } ,$ and $c _ { v } .$ Although the overall behavior remains the same, as $\gamma$ and  increase, the percentage difference between the output dependent payment structure and the FB case decreases. We provide the details of these experiments in the online appendix. The main finding is summarized in the following observation.

<sup>Observation</sup> <sup>3.</sup> The percentage difference in the client’s net value between the FB case and the output dependent payment structure is lower when the output sensitivity is comparatively higher to one party’s effort (i.e., higher  or $\beta )$ compared to the case when the output is almost equally sensitive to the efforts of both parties (i.e., $\alpha \approx \beta )$

Hence, the key takeaway here is that when the output is almost equally sensitive to the efforts of

## Figure 3 (Color online) Output Dependent Payment Structure: Impact of the Assignment of Responsibilities Between Parties

(a) Net value in the output dependent payment structure

![](/api/attachments/FBDJC6YJ/fulltext/images/4b97326d0623f6ec5c24a4a19ed89e63f1ea3581944947ad908c5b4201afb078.jpg)  
(b) Percentage difference between the first best case and the output dependent payment structure

both parties, the client might need to check the performance of the effort dependent payment structure that relieves the double moral hazard problem at the expense of monitoring costs. We examine this issue further in the next subsection.

5.2.2. Performance of the Effort Dependent Payment Structure. The first two results of the output dependent payment structure $( \mathrm { i . e . , }$ Observations 1 and 2) are also valid in the effort dependent case. Hence, for brevity, we do not discuss these results in detail. However, the behavior summarized in Observation 3 is different here. More specifically, when the total of the output sensitivity parameters $( \mathrm { i . e . , } \alpha + \beta )$ is kept constant, the percentage difference in the client’s net value between the FB case and the effort dependent payment structure always increases with $\beta$ (compared to the increasing–decreasing behavior in the output dependent payment structure). We illustrate this result in Figure 4 using $k = 1 2 ,$ $T = 1 0 ,$ $\gamma = 1 . 9 ,$ $\delta = 1 . 7 ,$ $c _ { c } = 2 ,$ c = 102, $c _ { m } = 0 . 3$ , and $\alpha +$ $\beta = 0 . 9$ . Since the vendor’s effort is monitored in the effort dependent payment structure, the client does not face a moral hazard problem as is the case in Figure 3(b). This explains why the behavior in Figure 4 is not inverse-U shaped. Rather, since the vendor has more responsibility when $\beta$ is high, he exerts relatively more effort. Hence, since the monitoring is more costly when the vendor spends more effort, the performance of the effort dependent payment structure (compared to the FB case) deteriorates as $\beta$ increases. We also examine whether the behavior presented in Figure 4 changes with different parameter values. Since the changes in the behavior are not significant, we relegate the detailed discussion to the online appendix and summarize our finding in the next observation.

<sup>Observation</sup> <sup>4.</sup> When the total of the output sensitivity parameters $( \mathrm { i . e . , } \alpha + \beta )$ remains constant, the

![](/api/attachments/FBDJC6YJ/fulltext/images/be59c90dc7c8eafd5091b84628df74a0c55ae95e64d98dfc93b588f0cd78be62.jpg)

Figure 4 (Color online) Effort Dependent Payment Structure: Impact of the Assignment of Responsibilities Between the Parties  
![](/api/attachments/FBDJC6YJ/fulltext/images/6894d5d5cd8765accef89bf29bda7eda0d74ba5d332faa14416d6118ec5d8bbe.jpg)  
percentage difference in the client’s net value between the FB case and the effort dependent payment structure increases with the output sensitivity to the vendor’s effort $( \mathrm { i . e . , } \beta )$

Hence, from Observations 3 and $^ { 4 , }$ we conclude that it is more likely for the effort dependent payment structure to be beneficial to the client if the vendor assumes minor responsibility in the project. On the other hand, if the vendor assumes almost all responsibility in the project, interestingly, the output dependent payment structure seems to be more promising. We analyze this issue in more detail in the next subsection, where we compare output and effort dependent payment structures and derive the conditions when one of them is preferred over the other.

## 5.3. Comparison of the Payment Structures

In this section, we compare the effort dependent and output dependent payment structures with respect to different characteristics of the parties. This analysis would assist managers of the client firm in selecting the most beneficial payment structure while establishing a value co-creation environment. Compared to the

FB case, the output dependent payment structure has inefficiency due to unverifiable effort levels. On the other hand, the effort dependent payment structure has inefficiency due to costs pertaining to the monitoring of the vendor’s efforts.

If the cost multiplier for monitoring the vendor’s effort $( \mathrm { i } . \mathrm { e } . , c _ { m } )$ or the fixed portion of the cost for monitoring $( \mathrm { i . e . , } F _ { m } )$ increases, the client tends to utilize the output dependent payment structure as she does not require the monitoring of the vendor’s effort. These results are monotonic as expected. However, as we study in this section, other characteristics of the parties affect the client’s selection of the payment structure in nonmonotonic ways. In the next proposition, we begin with studying how the vendor’s cost multiplier term $( \mathrm { i } . \mathrm { e } . , c _ { v } )$ affects which payment structure is better.

<sup>Proposition</sup> <sup>6.</sup> When the fixed cost for monitoring the vendor’s effort $( i . e . , \ F _ { m } )$ is negligible, output dependent payment structure dominates the effort dependent payment structure iff the vendor’s cost multiplier term $( i . e . , ~ c _ { v } )$ is sufficiently low. More specifically, the output dependent payment structure dominates iff

$$
\begin{array}{l} c _ {v} <   \left(\left(\frac {(\gamma - \alpha) \delta - \beta \gamma}{(\gamma - \alpha) (\delta - \beta) + \sqrt {\alpha \beta (\gamma - \alpha) (\delta - \beta)}}\right) ^ {((\gamma - \alpha) \delta - \beta \gamma) / (\beta \gamma)} \cdot \left(\frac {\beta \gamma - \alpha \delta}{\alpha (\beta - \delta) + \sqrt {\alpha \beta (\gamma - \alpha) (\delta - \beta)}}\right) ^ {\alpha \delta / (\beta \gamma)} \cdot \frac {\beta \gamma - \alpha \delta}{c _ {m} (\beta (\gamma - \alpha) - \sqrt {\alpha \beta (\gamma - \alpha) (\delta - \beta))}} - \frac {1}{c _ {m}}\right) ^ {- 1}. \end{array}
$$

When the cost multiplier term $c _ { v }$ is low, the vendor’s equilibrium effort is relatively high and, therefore, the total monitoring cost is high. Hence, in such a case, the severity of the double moral hazard problem is less than the costs related to monitoring the vendor’s effort. Therefore, as shown in Proposition $^ { 6 , }$ when it is less costly for the vendor to exert effort, the client should choose not to monitor the vendor’s effort and utilize the output dependent payment structure. If the fixed cost for monitoring the vendor’s effort $( \mathrm { i } . \mathrm { e } . , F _ { m } )$ is not negligible, then the threshold value for $c _ { v }$ is higher than the value presented in Proposition 6. We do not present the expression for brevity, but the key insight remains the same.

Proposition 6 reveals another interesting finding. When $F _ { m }$ is not significant, the client’s valuation of the project $( \mathrm { i . e . , } k )$ and the cost multiplier for the client’s effort $( \mathrm { i } . \mathrm { e } . , c _ { c } )$ do not play a role in determining which payment structure is better, as they do not appear in the threshold expression in Proposition 6. Recall that the client’s valuation of the project and her participation cost affect the equilibrium effort levels of both parties and, more importantly, the client’s net value in the project. The reason why they do not affect which payment structure is better is that the percentage changes in the client’s net value in both of these payment structures are the same as k or $c _ { c }$ varies. However, we find that if the fixed cost for monitoring the vendor’s effort $( \mathrm { i . e . , } F _ { m } )$ is significant, k and $c _ { c }$ indeed affect the client’s decision of which payment structure to use in the collaboration. In such a case, if the vendor’s cost multiplier term $c _ { v }$ is more than the threshold presented in Proposition $6 ,$ then an increase in k favors the effort dependent payment structure while an increase in $c _ { c }$ favors the output dependent payment structure. On the other hand, if $c _ { v }$ is below that threshold, then an increase in k favors the output dependent payment structure while an increase in $c _ { c }$ favors the effort dependent payment structure.

Let us now analyze how output sensitivity parameters  and $\beta$ affect which payment structure is better. It is not possible to derive the thresholds with respect to  and $\beta$ analytically, because the difference in the client’s value between the payment structures is highly nonlinear with respect to them. Hence, we conduct an extensive number of numerical studies and present two representative examples in Figure 5. In these graphs, $^ { \prime \prime } \mathrm { E D C ^ { \prime \prime } }$ and $" \mathrm { O D C ^ { \prime \prime } }$ represent the regions where the effort dependent payment structure and the output dependent payment structure, respectively, are preferred. The phrase $\mathrm { \Omega } ^ { \prime \prime } \mathrm { N O } ^ { \prime \prime }$ denotes the region where there is not enough value co-created with either payment structure and, therefore, no collaboration. In this example, the parameter values are: $T = 1 0 , \ \gamma = 2 . 1 , \ \delta = 1 . { \bar { 7 } } , \ k = { \bar { 1 } } 2 , \ c _ { c } = 2 . 0 , \ c _ { v } = 1 . 0 $ $c _ { m } = 0 . 3 , ~ R _ { c } = 4 0 0 ,$ and $R _ { v } = 2 0 0$ with different values of output sensitivity to the client’s and vendor’s efforts. In Figure 5(a), the fixed cost for monitoring the vendor’s effort $( \mathrm { i . e . , } F _ { m } )$ is zero. On the other hand, in Figure 5(b), $F _ { m } = 1 4$ . In other words, $F _ { m }$ is not negligible in Figure 5(b). We conduct several other numerical experiments with different parameter values. The details of these experiments and the results are presented in the online appendix.

Figure 5(a) reveals that the output dependent payment structure dominates the effort dependent payment structure only when the output sensitivity to the vendor’s effort $( \mathrm { i . e . , } \beta )$ is considerably higher than the output sensitivity to the client’s effort $( \mathrm { i } . \mathrm { e } . , \alpha )$ . However, if the output is equally sensitive to both parties’ efforts or relatively more sensitive to the client’s effort, the effort dependent payment structure yields more value to the client. In addition, we observe from both figures that when the output sensitivities to the effort levels of both parties are very low, they do not collaborate (see the bottom-left area labeled $^ { \prime \prime } \mathrm { \dot { N } O ^ { \prime \prime } } )$ . In such a case, neither payment structure can generate more value than the total reservation utilities of the parties.

Figure 5 Client’s Choice of Payment Structure  
![](/api/attachments/FBDJC6YJ/fulltext/images/e85aadf8f681f57fa8c425e0f340bb182a4f1df962a60f4bca492eefdfae0fb3.jpg)

As stated earlier, the difference between the settings depicted in Figures 5(a) and 5(b) is that the fixed cost for monitoring the vendor’s effort $( \mathrm { i } . \mathrm { e } . , F _ { m } )$ is not negligible in Figure 5(b). In Figure 5(b), the set of parameter values where the output dependent payment structure dominates the effort dependent payment structure is nonconvex. This might not be intuitive at first, but can be explained as follows. For example, in Figure 5(b), when $\alpha = 0 . 2 0$ and $\beta$ is lower than 0.15, the output dependent payment structure dominates. The reason is that, in such a case, the output does not depend highly on either party’s effort level, and the net value of the client is low. Hence, the client avoids paying for the fixed payment term of monitoring (e.g., investment in monitoring systems or equipment) and chooses to use the output dependent payment structure. On the other hand, when $\alpha = 0 . 2 0$ and $\beta$ is between 0.15 and 0.45, the effort dependent payment structure dominates. This is because when the output depends on the effort levels of both parties, the severity of the double moral hazard problem increases as discussed in Section 5.2.1. However, when $\alpha = 0 . 2 0$ and $\beta$ is more than 0.45, again the output dependent payment structure is preferred. In this case, the vendor exerts relatively more effort, and therefore the total cost of monitoring is increased. In addition, because the client spends relatively less effort compared to the vendor, the severity of the double moral hazard problem is decreased as explained in Section 5.2.1. As discussed earlier, we verified that these results hold for other problem instances as well. Hence, we summarize these findings in the following observation.

<sup>Observation</sup> <sup>5.</sup> (a) When the fixed cost for monitoring the vendor’s effort $\left( \mathrm { i . e . , ~ } F _ { m } \right)$ is negligible, the output dependent payment structure is better than the effort dependent payment structure only when the output sensitivity to the vendor’s effort $\left( \mathrm { i . e . , ~ } \beta \right)$ is considerably higher than the output sensitivity to the client’s effort $( \mathrm { i . e . , ~ } \alpha )$ . However, if the output is equally sensitive to both parties’ efforts or relatively more sensitive to the client’s effort, the effort dependent payment structure yields more value to the client.

![](/api/attachments/FBDJC6YJ/fulltext/images/f5dc700e2fd3e7bfa71787cf42adbaee32fd3b45d15e7f06def86cfbbfd6de46.jpg)

(b) When the fixed cost for monitoring the vendor’s effort $( \mathrm { i . e . , } F _ { m } )$ is not negligible, the set of parameters where the output dependent payment structure dominates the effort dependent payment structure is nonconvex and is similar to that in Figure 5(b).

Now, in Section 6, we present an extension of our models and provide useful insights.

## 6. Salvage Value

Here, we consider that the client or the vendor gets utility from the output both during the collaboration period and after the collaboration. For example, the client can use the output even after the collaboration ends. In this scenario, the value obtained after the collaboration period can be considered as a salvage value. On the other hand, the vendor can build a reputation or history from his business collaboration. His success, reflected in the output, might be considered by other potential clients as a signal of how successful the vendor would be in his future businesses. This can be considered as a salvage value of the project to the vendor.

For brevity, we present the results only for the effort dependent payment structure in this section. Hence, given the salvage value parameters $S _ { c }$ and $S _ { v }$ for the

Figure 6 (Color online) Value to the Client with Respect to the Output Sensitivity to Client’s Effort  
![](/api/attachments/FBDJC6YJ/fulltext/images/6f187c8ea6b38850efe69e30cd6aa19d832278514da5fe0e842440bb90d9712b.jpg)  
client and the vendor, the objective functions of the parties and the constraints are presented below

$$
\begin{array}{l l} \max _ {u (t), H (\cdot)} & \left\{\int_ {0} ^ {T} k q (t)   d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma}   d t - H (\cdot) + S _ {c} q (T) \right\} \\ \max _ {v (t)} & \left\{H (\cdot) - \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta}   d t \right. \\ & \left. - \int_ {0} ^ {T} c _ {m} v (t) ^ {\delta}   d t - F _ {m} + S _ {v} q (T) \right\} \end{array}
$$

subject to $\begin{array} { r } { \dot { q } ( t ) = u ( t ) ^ { \alpha } v ( t ) ^ { \beta } . } \end{array}$ 3

$$
\begin{array}{l} \int_ {0} ^ {T} k q (t) d t - \int_ {0} ^ {T} c _ {c} u (t) ^ {\gamma} d t \\ \quad - H (\cdot) + S _ {c} q (T) \geq R _ {c}; \\ H (\cdot) - \int_ {0} ^ {T} c _ {v} v (t) ^ {\delta} d t - \int_ {0} ^ {T} c _ {m} v (t) ^ {\delta} d t \\ \quad - F _ {m} + S _ {v} q (T) \geq R _ {v}; \\ u (t) \geq 0; v (t) \geq 0. \end{array}
$$

The payment structure that the client would utilize in this setting is very similar to the one presented in Proposition 3. Hence, we omit the details. However, we present the equilibrium effort levels in the following lemma.

<sup>Lemma</sup> <sup>9.</sup> In the presence of salvage values for both the client and vendor, their equilibrium effort levels in the effort dependent payment structure are

$$
\begin{array}{l} u (t) = \bigg (\bigg (\frac {(S _ {c} + S _ {v} + k (T - t)) \alpha}{\gamma c _ {c}} \bigg) ^ {\delta} \\ \qquad \cdot \bigg (\frac {\beta \gamma c _ {c}}{\alpha \delta (c _ {v} + c _ {m})} \bigg) ^ {\beta} \bigg) ^ {1 / (\gamma (\delta - \beta) - \alpha \delta)}, \\ v (t) = \bigg (\bigg (\frac {(S _ {c} + S _ {v} + k (T - t)) \beta}{\delta (c _ {v} + c _ {m})} \bigg) ^ {\gamma} \\ \qquad \cdot \bigg (\frac {\alpha \delta (c _ {v} + c _ {m})}{\beta \gamma c _ {c}} \bigg) ^ {\alpha} \bigg) ^ {1 / (\gamma (\delta - \beta) - \alpha \delta)}. \end{array}
$$

![](/api/attachments/FBDJC6YJ/fulltext/images/b4c799e251a82346dcfcf6994ea5fd377b8742063ee308575fa70ca23e6a1efa.jpg)

This lemma shows that the equilibrium effort levels decrease in time similar to that in the no-salvagevalue scenario. However, clearly the rate of decrease in effort levels with time reduces as the terminal value increases. Also, the terminal effort levels here are positive, unlike that in the case with no salvage value. Next, similar to the earlier case, the client covers only the effort cost of the vendor and the costs related to monitoring in addition to the vendor’s reservation utility. Let us denote the total of the salvage value terms with $S \ ( \mathrm { i . e . , } \ S = S _ { c } + S _ { v } )$ . As expected, if we set S to zero, the equilibrium effort levels converge to the case with no salvage value. In addition, we would like to note that if we let $S / k \to \infty \mathrm { o r }$ set $k = 0$ (that implies that the client does not get utility throughout the collaboration period but only at the project completion time), our model converges to a static model with no sense of continuous analysis except the accumulation of output that is valuable only at the end.

Most results remain valid in this setting compared to those in the effort dependent payment structure studied in Section 4. However, the relationship between value and output sensitivity terms discussed in Proposition 5 and Figure 2 changes its behavior when the parties have salvage value in the project. The analytical conditions are cumbersome to present; however, the following behavior is observed in the entire set of problem instances we analyzed.

<sup>Observation</sup> <sup>6.</sup> (a) When the ratio of the total salvage value to the ongoing value during the collaboration $( \mathrm { i } . \mathrm { e } . , \ S / k )$ is low, an increase in the output sensitivity to either party’s effort (i.e.,  or $\beta )$ may decrease the client’s net value.

(b) When the ratio of the total salvage value to the ongoing value during the collaboration $( \mathrm { i } . \mathrm { e } . , \ S / k )$ is high, an increase in the output sensitivity to either party’s effort (i.e.,  or ) always increases the client’s net value.

Observation 6 is illustrated in Figure 6 using $T = 1 0 ,$ $\beta = 0 . 4 , \ \gamma = 3 , \ \delta = 2 . 5 , \ k = 1 2 , \ c _ { c } = 2 , \ c _ { v } = \mathrm { \tilde { 1 } } . 2 ,$ , and $c _ { m } = 0 . 3$ 0 We run this experiment with several other parameter values as well, but the behavior discussed in Observation 6 does not change. As shown in Figure 6(a), if we increase the importance of the terminal value in the collaboration, the behavior of decreasing the client’s value with output sensitivity starts fading away. Figure 6(b) considers the same problem instance with $S / k = 2 0 .$ , where we observe that this behavior is completely gone. Hence, as stated in Observation $6 ,$ if $S / k$ is large enough, the client’s net value always increases as the output becomes more sensitive to the effort of either party. This, in turn, reveals that the interesting behavior of the client’s value presented in Figures 2 and 6 is due to the time dynamics $( \mathrm { i . e . , }$ ongoing vs. terminal value) of the collaboration that we capture in our study.

## 7. Conclusions

In IT services, the traditional view of analyzing a vendor–client or consultant–client relationship needs to be revisited in light of the fact that the output of these relationships may depend on the effort levels of both parties, not just the vendor’s effort. Therefore, we analyze a value co-creation environment where the output necessitates the efforts of both parties. Our analyses, results, and insights apply to other domains as well, such as business process outsourcing, auditing, consulting, financial planning, engineering projects, and R&D projects.

In this paper, we also consider the fact that the effort levels of the parties may not be monitored. This leads to a double moral hazard problem; however, the client may choose to observe the effort level of the vendor with a cost. In addition, both parties may change their effort levels dynamically. Moreover, we allow the client to get utility from the output as it is developed. Considering all of these facts, we examine two different settings from a differential game perspective. We derive the equilibrium effort levels of the client and the vendor as well as the optimal payment terms and the value generated in the collaboration. We find that effort levels decrease as the project progresses even when we (i) discount profits and costs or (ii) consider that the unit value of the output is high in the later stages of the project. We also show that if the relative value received at the end of the collaboration is high, the decrease in effort levels with time is less pronounced. Next, we present and explain several results based on the sensitivity analyses of the equilibrium effort levels with respect to the parameters representing different characteristics of the parties. The client’s valuation of the project and the progress in the collaboration play an important role in the behavior of the effort levels. Depending on these factors, the equilibrium effort levels might increase or decrease with the changes in the output sensitivities to effort levels and the cost elasticities of efforts.

We also compare the performances of different payment structures to find the best one for the client under different circumstances. This analysis also reveals whether the vendor’s effort should be monitored or not. We find that, as long as the participation cost of the vendor is not very low, his effort should be monitored and the client should use an effort dependent payment structure. Otherwise, the client should not monitor the vendor’s effort and should operate under double moral hazard with an output dependent payment structure. Another interesting finding is that, if the sensitivity of output to the vendor’s effort is relatively higher than the sensitivity to the client’s effort, the client should use the output dependent payment structure and should not monitor the vendor’s effort.

Finally, we find that some of the interesting insights are due to the time dynamics considered in the paper. For example, under certain circumstances, an increase in the sensitivity of the output to either parties’ effort level does not necessarily increase the net values of the parties. However, if the relative value received at the end of the collaboration is high (compared to the ongoing utility), any increase in the output sensitivity to either party’s effort level always increases the net value.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2016.0636.

## References

Abernathy WJ, Wayne K (1974) Limits of the learning curve. Harvard Bus. Rev. 52(5):109–119.

Bapna R, Barua A, Mani D, Mehra A (2010) Cooperation, coordination, and governance in multisourcing: An agenda for analytical and empirical research. Inform. Systems Res. 21(4):785–795.

Baskerville R, Pries-Heje J (2004) Short cycle time systems development. Inform. Systems J. 14(3):237–264.

Bettencourt LA, Ostrom AL, Brown SW, Roundtree RI (2002) Client co-production in knowledge-intensive business services. California Management Rev. 44(4):100–128.

Bhattacharyya S, Lafontaine F (1995) Double-sided moral hazard and the nature of share contracts. RAND J. Econom. 26(4): 761–781.

Bose A, Pal D, Sappington DEM (2011) On the performance of linear contracts. J. Econom. Management Strategy 20(1):159–193.

Cachon G, Netessine S (2004) Game theory in supply chain analysis. Simchi-Levi D, Wu S, Shen Z, eds. Handbook of Quantitative Supply Chain Analysis: Modeling in the e-Business Era (Kluwer Academic Publishers, Boston), 13–65.

Carmel E (1999) Global Software Teams (Prentice-Hall, Englewood Cliffs, NJ).

Cavusoglu H, Mishra B, Raghunathan S (2005) The value of intrusion detection systems in information technology security architecture. Inform. Systems Res. 16(1):28–46.

Choudhury V, Sabherwal R (2003) Portfolios of control in outsourced software development projects. Inform. Systems Res. 14(3):291–314.

Cohen MA, Eliashberg J, Ho TH (1996) New product development: The performance and time-to-market tradeoff. Management Sci. 42(2):173–186.

Currie WL, Galliers B, eds. (1999) Rethinking Management Information Systems: An Interdisciplinary Perspective (Oxford, New York).

DiRomualdo A, Gurbaxani V (1998) Strategic intent for IT outsourcing. Sloan Management Rev. 39(4):67–80.

Dockner E, Jorgensen S, Long NV, Sorger G (2000) Differential Games in Economics and Management Science (Cambridge University Press, Cambridge, UK).

Erhun F, Keskinocak P (2011) Collaborative supply chain management. Kempf K, Keskinocak P, Uzsoy R, eds. Planning Production and Inventories in the Extended Enterprise: A State of the Art Handbook, Vol. 1 (Springer, New York), 233–268.

Gopal A, Sivaramakrishnan K, Krishnan MS, Mukhopadhyay T (2003) Contracts in offshore software development: An empirical analysis. Management Sci. 49(12):1671–1683.

Gurbaxani V (2007) Information systems outsourcing contracts: Theory and evidence. Apte U, Karmarkar U, eds. Managing in the Information Economy: Current Research Issues, Annals Inform. Systems, Vol. 1 (Springer, New York), 83–115.

Harris ML, Collins RW, Hevner AR (2009) Control of flexible software development under uncertainty. Inform. Systems Res. 20(3):400–419.

Hopp WJ, Iravani SMR, Liu F (2009) Managing white-collar work: An operations-oriented survey. Production Oper. Management 18(1):1–32.

Kale V (2014) Implementing SAP CRM: The Guide for Business and Technology Managers (CRC Press, Boca Raton, FL).

Karmarkar US, Pitbladdo R (1995) Service markets and competition. J. Oper. Management 12(3–4):397–411.

Kim S-H, Nettessine S (2013) Collaborative cost reduction and component procurement under information asymmetry. Management Sci. 59(1):189–206.

Kouvelis P, Lariviere MA (2000) Decentralizing cross-functional decisions: Coordination through internal markets. Management Sci. 46(8):1049–1058.

Krishnan H, Kapuscinski R, Butz DA (2004) Coordinating contracts for decentralized supply chains with retailer promotional effort. Management Sci. 50(1):48–63.

Lee CH, Geng X, Raghunathan S (2013) Contracting information security in the presence of double moral hazard. Inform. Systems Res. 24(2):295–311.

Liu D, Kumar S, Mookerjee VS (2012) Advertising strategies in electronic retailing: A differential games approach. Inform. Systems Res. 23(3):903–917.

Mani D, Barua A, Whinston AB (2012) An empirical analysis of the contractual and information structures of business process outsourcing relationships. Inform. Systems Res. 23(3):618–634.

Mookerjee V, Mookerjee R, Bensoussan A, Yue WT (2011) When hackers talk: Managing information security under variable attack rates and knowledge dissemination. Inform. Systems Res. 22(3):606–623.

Pearce DG, Stacchetti E (1998) The interaction of implicit and explicit contracts in repeated agency. Games Econom. Behav. 23(1):75–96.

Pigoski TM (1996) Practical Software Maintenance: Best Practices for Managing Your Software Investment (Wiley, New York).

Plambeck EL, Taylor TA (2006) Partnership in a dynamic production system with unobservable actions and noncontractible output. Management Sci. 52(10):1509–1527.

Ramasubbu N, Mithas S, Krishnan MS, Kemerer CF (2008) Work dispersion, process-based learning, and offshore software development performance. MIS Quart. 32(2):437–458.

Roels G, Karmarkar US, Carr S (2010) Contracting for collaborative services. Management Sci. 56(5):849–863.

Schwartz A, Edlin A (2003) Optimal penalties in contracts. Yale Faculty Scholarship Series Paper 309, New Haven, CT.

Selten R (1975) Reexamination of the perfectness concept for equilibrium points in extensive games. Internat. J. Game Theory 4(1):25–55.

Sorger G (1989) Competitive dynamic advertising: A modification of the case game. J. Econom. Dynam. Control 13(1):55–80.

Susarla A (2012) Contractual flexibility, rent seeking, and renegotiation design: An empirical analysis of information technology outsourcing contracts. Management Sci. 58(7):1388–1407.

Susarla A, Barua A (2011) Contracting efficiency and new firm survival in markets enabled by information technology. Inform. Systems Res. 22(2):306–324.

Susarla A, Subramanyam R, Karhade P (2010) Contractual provisions to mitigate holdup: Evidence from information technology outsourcing. Inform. Systems Res. 21(1):37–55.

Swaminathan JM, Tayur SR (2003) Models for supply chains in ebusiness. Management Sci. 49(10):1387–1406.

Toppin G, Czerniawska F (2005) Business Consulting: A Guide to How It Works and How to Make It Work (Profile Books Ltd., London).

Tsay AA, Agrawal N (2000) Channel dynamics under price and service competition. Manufacturing Service Oper. Management 2(4):372–391.

Whitaker J, Mithas S, Krishnan MS (2011) Organizational learning and capabilities for onshore and offshore business process outsourcing. J. Management Inform. Systems 27(3):11–42.
