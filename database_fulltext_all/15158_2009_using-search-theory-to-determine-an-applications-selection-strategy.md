---
otero_id: 15158
otero_key: "JK6NJ466"
title: "Using search theory to determine an applications selection strategy"
authors: "Michael Wybo; Jacques Robert; Pierre-Majorique Léger"
year: "2009"
journal: "Information & Management"
doi: "10.1016/j.im.2009.05.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using search theory to determine an applications selection strategy

Michael Wybo \*, Jacques Robert, Pierre-Majorique Le´ger

HEC Montreal, 3000 chemin de la Cote-Sainte-Cath., Montreal, Quebec, Canada H3T 2A7

## A R T I C L E I N F O

Article history: Received 29 October 2007 Received in revised form 13 March 2009 Accepted 15 May 2009 Available online 6 June 2009

Keywords: Software selection COTS Search theory Make versus buy IT procurement Applications selection

## A B S T R A C T

The literature on software selection focuses mainly on identifying and ensuring the evaluation of those attributes of alternative commercial software products relevant to meeting the functional and nonfunctional requirements of the acquiring organisation. Once these attributes are determined, however, the firm acquiring the product must still decide on its selection strategy: which products should be evaluated, in what order, and at what point is it no longer beneficial to continue to evaluate additional products. We applied search theory to solve this problem of determining the selection strategy. This resulted in an optimal strategy but changes the way we view and manage software acquisition. In particular, the approach suggested that software acquisition may be better managed as an ongoing process instead of as a project with a distinct start and end. The approach formally incorporated the strategic importance of the application to the firm in determining the optimal strategy, a consideration that does not appear in the normal requirements-based approach to software selection.

\- 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Organisations have several ways of acquiring business applications. Acquisition through development generally begins with requirements definition and proceeds sequentially through architecture, design, and implementation. Key areas of research from the development perspective include, among others, the codification of software engineering best practices [2], the management of development teams, and software development project management [8]. Alternatively, organisations may acquire applications through selection. In this approach, the firm must find the pre-existing solution that best fits functional, architectural, design, and implementation preferences from amongst a set of potential solutions over whose functions, architecture, design, and coding it has no control. Where the creation of well defined requirements is of primary importance in the development approach, the most important activity in selection is the evaluation and scoring of alternative available applications [10].

Over time the selection approach has become the dominant means of acquiring applications, accounting for approximately 70% of corporate business software expenditures [5]. Evaluating and selecting application products are the ‘‘primary sources of effort’’ in the selection approach [22] and have been observed to account for the majority of time and expense in companies selecting enterprise systems [17].

Most of the literature on application selection focuses on ensuring the collection and evaluation of all the selection relevant attributes of a software product, such as functionality, cost, vendor characteristics, integration requirements, vendor support, and ease of use. We decided to develop the ‘‘how much evaluation is enough’’ line of inquiry but approach the problem from a different perspective. Determining which attributes to evaluate is an important decision with significant consequences. Yet once the evaluation criteria have been chosen the organisation must still apply them and to do so must decide which applications should be evaluated, in what order, and at what point to stop evaluating additional applications. We refer to these decisions as the firm’s selection strategy. To arrive at an optimal selection strategy we employed a generalized economic search theory that maximizes the benefits from a selection process taking into account the characteristics of the different alternatives and the costs associated with investigating them. The result of this approach is an optimal search strategy that specifies which options to investigate, the order in which they should be investigated, and when to stop.

The principal parameters of the search theory-based selection model are (1) the initial information that the firm has about a particular application before beginning any detailed evaluation, (2) the importance of the type of application to the firm, which allows us to evaluate the value of additional information about alternatives, (3) the costs of performing a detailed evaluation on a particular application, which is assumed to vary with each application, and (4) the score obtained by a particular application after a detailed evaluation of the relevant attributes.

One important assumption that we make is that the firm making the selection is faced with a number of software applications from which to choose. The business applications industry has experienced significant consolidation in recent years. Nonetheless, and especially for the midrange market, there is a large choice of viable products. For example, a search on the site http://www.erp.technologyevaluation.com for a fictitious medium-sized firm in the food and beverage distribution business generated 86 potential and 9 disqualified vendors based on industry requirements and firm characteristics. The site http:// www.vendor-showcase.com lists 102 Discrete Manufacturing ERP vendors, 110 vendors of accounting software, 58 Supply Chain Management vendors, 32 vendors of CRM applications, and 15 companies offering Product Lifecycle Management applications.

## 2. Literature review

Research in organisational buying behaviour has dealt with buying problems and the process of choosing suppliers and products (see [6] for a comprehensive review of the foundation concepts in this field and [21] for a distillation of criteria used by purchasing managers to help select suppliers). Unlike many other industrial purchases, however, software selection is generally managed as a project as opposed to a permanent, ongoing business process. It would be rare to find a full time ‘‘software selection team’’ analogous to a full time ‘‘software development team’’. Thus the selecting firm’s personnel may have little experience with selection activities. For many, participation in the selection project will be a new task.

From a risk management perspective software selection is a low experience, large adverse consequence, and highly complex purchasing problem [20]. Although other products share this profile, applications software has some unique characteristics. Business applications are typically characterized by a lack of standards regarding terminology, functionality, data definitions and structures, navigation and user interface, underlying technology, architecture, and coding. For example, different applications may take very different approaches to implementing a nested bill of materials. This lack of a dominant design, sometimes even within the same vendor’s product line, is compounded by the malleable nature of software in general and the ability of the same product to be parameterized and configured to operate in different ways.

These characteristics require evaluation criteria for purchased software that are not present in acquisition by development. The commercial-off-the-shelf (COTS) products literature has for many years addressed the issue of identifying and evaluating these attributes, some of which are listed in Fig. 1.

Early evaluation strategies focused on purely functional characteristics of systems and applications. For example the CODASYL Systems Committee published a ‘‘Feature Analysis’’ document that described essential technical characteristics of DBMS [4]. An evaluation of six commercial DBMS conducted by the

• Correctness

• Flexibility

• Availability / Robustness

• Installation / Ease of Upgrade

• Security

• Portability

• Product Performance

• Functionality

• Understandability

• Price

• Ease of Use

• Maturity

• Version compatibility

• Vendor Support

• Inter-component Compatibility

• Training

• Vendor Concessions

Fig. 1. Sample evaluation attributes for COTS products [1].

US National Bureau of Standards assessed these products on their implementation of core DBMS functionality [16]. The more recent COTS literature explores means to assess software applications for their fit with both the functional and non-functional requirements of the acquiring organisation [12]. The general structure of these approaches is:

1. Inspect all of the modules of each available product to check whether it has modules that satisfy some or all of the functional requirements.

2. Check whether the product also satisfies the non-functional requirements, such as the interoperability of the product modules with other systems or the viability of the vendor.

3. Select the product that best satisfies both the functional and non-functional requirements.

The principal weakness in this approach is the need to evaluate a potentially large number of modules and applications (n) on a potentially large set of attributes (k). This evaluation can quickly become un-manageable. Ochs et al. [14] developed the COTS acquisition process (CAP) method to reduce the need to conduct (n x k) evaluations by comparing applications on a subset of attributes, eliminating applications that do not meet these criteria, and then applying the next subset of attributes to the remaining applications. The requirements driven COTS product evaluation process (RCPEP) [11] uses a ‘‘trade study’’ in which vendors respond in writing to one question per requirement. These responses are scored and a weighted average is calculated based on the importance of each requirement. As an alternative to starting from well defined requirements, the procurement oriented requirements engineering (PORE) [13] approach collects information about the features of existing products in parallel with requirements definition. This approach reduces the number of evaluations by avoiding requirements that cannot be satisfied.

Boehm and Port [1] and Port and Chen [15] asked the question of ‘‘how much’’ evaluation was enough but again framed the problem as one of determining which product attributes to evaluate. This approach does not address the question of ‘‘how many’’ applications one should evaluate before making a decision and thus provides little guidance in determining the organisation’s overall strategy for managing the selection process. Regardless, the importance of a robust set of selection attributes should not be underestimated. For example, the selection process must recognise that modifying a COTS application requires that all future versions must also be modified. Evaluating ‘‘Correctness’’ should indicate to the purchasing party whether and which modifications might be required to make the application useable. Evaluating ‘‘Ease of Upgrade’’ should indicate the potential difficulties and expenses involved in taking future versions of a modified application. Failure to include these and other functional and non-functional evaluation criteria can significantly reduce the value of the selected application to the organisation.

Kauffman and Leszcyc [7] did develop a model to determine the optimal number of suppliers to be evaluated but assumed ‘‘a relatively homogeneous product manufactured to an industrial standard’’ where products differed mainly on price and availability, characteristics not shared by business applications.

Unrelated to software selection, Weitzman [19] developed an optimal solution to a generalized search problem that he characterized as:

‘‘There are a number of different opportunities or sources, each yielding an unknown reward. The uncertainty about the reward from a source can be eliminated, at a fee, by searching or sampling.

Each source has its own independent probability distribution for the reward, search cost, and search time. Sources are sampled sequentially, in whatever order is desired. When it has been decided to stop searching, only one opportunity is accepted, the maximum sampled reward’’.

This search problem conforms closely to the applications selection problem. The firm is faced with a number of potential applications from which to choose and the relative benefits of these alternatives are unknown at the outset.

The lack of a dominant design and standards, and the necessity of evaluating the product as well as the vendor, tend to make the time and effort associated with evaluating an application a characteristic of the application itself and independent of other applications. We can consider that each application ‘‘has its own independent probability distribution for the reward, search cost, and search time’’ and that there will be little, if any, reduction in the costs of evaluating applications as the number of products being evaluated increases. This would not apply to certain standardised functionality, such as ANSI SQL compliance in relational DBMS from different vendors. However, evaluating the SQL extensions specific to one vendor does not necessarily reduce the effort or costs of evaluating the extensions provided by another or of evaluating the financial viability or the maintenance and support capabilities of the different vendors themselves.

Acquisition by selection imposes a set of evaluation criteria that differ from those involved in acquisition by development. The conduct of this evaluation itself consumes the major part of the effort and expense of selecting an application. In order to improve on this process researchers have asked how much evaluation is useful, but in the context of determining which application attributes or requirements should be evaluated in detail rather than asking how the overall selection strategy should be specified. A generalized search model whose assumptions correspond closely to the characteristics of the application selection problem can be used to specify the selection strategy.

## 3. Applying search theory to applications selection

We viewed the problem of software selection as a search problem where the firm sought to determine the best selection among a finite set of opportunities and where each opportunity corresponds to a particular application package or solution. We assumed that the firm would define a search strategy (the order in which applications should be evaluated and the conditions under which the firm should end the evaluation and pick the solution) that maximized the benefits from the selected solution while minimizing its acquisition costs. Viewed this way, software selection can be modelled as an economic maximizing problem.

## 3.1. Basic parameters of the model

Since neither organisations nor applications exist in a vacuum we assume that the firm already has some initial information about n potential software applications, $i \in \{ 1 , 2 , . . . , n \}$ and we denote by $\theta _ { i }$ the specific initial information that the firm has about Application i. The variable $\theta _ { i }$ may represent many things, such as the buyer’s past experience with the software, information obtained from other firms, general marketing information, articles in the trade press, etc.

The acquiring firm expects to derive some benefit from the solution it chooses. It may express this benefit in many ways, including improvements in efficiency or performance, reductions in resource use, improved customer retention, increased market share, compliance with industry regulations, or strategic necessity. The ability of any particular application to deliver these benefits can be assessed in terms of relevant functional and non-functional attributes, as discussed above. The degree to which these attributes are considered important to evaluate and are included in the evaluation criteria may be determined using one the requirements-based approaches identified in the COTS literature.

We let $x _ { i }$ denote the score obtained by solution i after it has been subjected to a detailed evaluation of the chosen attributes. Before this detailed evaluation $x _ { i }$ is random and unknown to the decision-maker, it can be determined only after the firm invests in a detailed evaluation of Application i. In practice this score is usually the result of assigning weights to the different evaluation attributes, multiplying these by some rating of each application for that criteria, and summing the products, although various other techniques may use more complex arithmetic (for example, see [9,18]). This gives a numerical indication of the value of the product and is the information on which selection is based.

In the case of software applications, and underlying the importance of the selection strategy, the benefits to the organisation of an application are usually known only after some period of use [3]. We therefore let the variable $\pi _ { i }$ represent the benefit less acquisition costs accruing to the firm if solution i is selected. We note that the variable $\pi _ { i }$ is unknown to the decision-maker, it will be observed only after solution i is selected and implemented and the firm uses the application in its operations.

The variables $\pi _ { i , \phantom { i } } \ x _ { i } ,$ and $\theta _ { i }$ represent different types of information about solution i. The parameter $x _ { i }$ contains more information than $\theta _ { i }$ since it is the result of a detailed evaluation of solution i. Similarly, $\pi _ { i }$ contains more information than $x _ { i }$ since it represents what is known about the application after its extended use. In the case of software selection, the organisation must base its selection decision on $x _ { i } ,$ the score resulting from a detailed evaluation of the product.

![](/api/attachments/JK6NJ466/fulltext/images/64045f645e4c27e6e317dc4bb104fae3196117f8a29a408310c252c05243dac6.jpg)  
Fig. 2. The probability of attaining an evaluation score based on initial information.

We model the variables $\pi _ { i }$ and x as random because their values are unknown in advance. We let $\textstyle F ( x _ { i } | \theta _ { i } )$ denote the cumulative distribution of x given $\theta _ { i } .$ . The shape of the cumulative probability distribution $\textstyle F ( x _ { i } | \theta _ { i } )$ captures the buyer’s perceptions of what they would actually discover after conducting a detailed evaluation of a particular application based on any prior information they may hold about that application. Fig. 2 shows $F ( x _ { i } | \theta _ { i } )$ for two different software applications and is a proxy for the probability distribution of the benefits of the application if it were to be selected.

The distribution $\textstyle F ( x _ { i } | \theta _ { i } )$ for Application A captures the perception of the acquiring firm, based on its prior information, that there is a probability of 0.25 (1.0–0.75) that if it invests in a detailed evaluation of Application A it will find a score as high or higher than 70. If Application A has been widely adopted in the industry there may be a broad general knowledge of its capabilities. The perception may be that investing in a detailed evaluation has a small probability of changing what one already believes about the product. In contrast, Application B may be a newer product adopted by a small number of companies and for which there is some reliable positive initial information. Based on this initial information there may be a greater perceived probability (0.4) that a detailed evaluation will result in a score as high as or higher than 70.

We let $E ( \pi _ { i } | x _ { i } )$ denote the expected value of $\pi _ { i }$ given $x _ { i \cdot }$ This relates the expected benefits accruing to the firm from the adoption of an application with the information gathered from a detailed evaluation of that application:

$$
\pi_ {i} = \alpha + \beta x _ {i} + \varepsilon_ {i}\tag{1}
$$

$$
E [ \pi_ {i} | x _ {i} ] = \alpha + \beta x _ {i}\tag{2}
$$

The parameter $\beta$ measures how a one point change in the evaluation score (x ) is related to the future expected benefits from Application i. If $\beta$ is large then detailed information that might change the evaluation score by a small amount is valuable, since small changes have a large impact on eventual benefits. A small $\beta$ indicates that this additional information is not very important.

Two contextual factors can influence the parameter $\beta .$ In the first case $\beta$ will increase with the strategic importance of the selection. As an example, in most organisations the ‘‘magnitude of the adverse consequences’’ to the firm of selecting the wrong CRM application is greater than for selecting the wrong remote E-mail client. A 10 point difference in the $x _ { i }$ of two CRM products is likely to have more significant implications on the benefits the firm derives from the choice of a particular CRM application than a 10 point difference in the $x _ { i }$ for two email clients would have on the benefits from implementing one of the remote email applications. The parameter $\beta$ in this case will be higher for the CRM acquisition than for the remote email application. Note that $\beta$ is determined for the selection and is not a characteristic of a particular application.

![](/api/attachments/JK6NJ466/fulltext/images/e102edaaaa877ff2f7654369ae9b16388edf46eceb4b3bbc30898a33cde1b0a7.jpg)

Secondly, regardless of the questions asked and the information collected, there may still be significant unknowns concerning the benefits to the firm of adopting a particular type of application. It may be inherently difficult to measure the attributes of interest or, even if it were possible, detailed information on these attributes might shed little light on its potential benefits to the firm. This may occur when the only reference sites are in industries significantly different from the acquiring firm, or if its business model is significantly different, or when the type of application is new and there is little or no collective understanding of it. In such cases, even though the application itself may be important to the firm, the parameter $\beta$ can be low because increases in x are only weakly related to the expected benefits of adopting the application.

Finally, we represent by $c _ { i }$ the costs the firm must incur in performing a detailed evaluation of Application i. As per the general model, we assume that different applications will have different costs associated with performing their detailed evaluation. In practice, it may be quite easy to evaluate a product when the vendor is located in the same geographic region and the product is used by reference companies in the same industry with similar business processes. However, a product whose vendor resides in another country, whose reference customers are in unrelated industries and/or with unfamiliar business processes, and whose technology platform is one with which the acquiring firm has no experience is more difficult to evaluate. An evaluation of such a product may require significant travel of the evaluation team and the services of business process and technology consultants to help the firm rate the product along the chosen evaluation criteria.

As such the specific cost components in a detailed evaluation can differ for each particular application. We use c to represent the total cost of performing a detailed evaluation for Application i and do not attempt to model all the varied and potential component costs associated with evaluating any particular alternative.

## 3.2. The search potential of an application

The search potential of each application is designated as $x _ { i } ^ { * }$ and is related to the cost of investigating the solution $( c _ { i } ) ,$ , the initial information about that solution before conducting a detailed evaluation $( \theta _ { i } ) ,$ , and the importance of information gathered about alternative applications as a predictor of their future expected benefits $( \beta ) .$ . As such it incorporates all the relevant information about an application available prior to a detailed investigation. The parameter $\beta$ is determined for the selection and is equal for all alternatives being evaluated. We can calculate the search potential x<sup></sup> of any application i as:

$$
x _ {i} ^ {*} = \left\{z | c _ {i} = \beta \left(\int_ {z} ^ {\infty} [ 1 - F (x _ {i}, \theta_ {i}) ] d x\right) \right\}\tag{3}
$$

![](/api/attachments/JK6NJ466/fulltext/images/485a7fd4ac4883999c8220a82a17ff2e24551d13a856168372a9f4b8c3dd3da4.jpg)  
Fig. 3. Calculation of the search potential of an application.

The calculation of $x _ { i } ^ { * }$ is illustrated in Fig. 3. The shaded area of each graph corresponds to the integral $\begin{array} { r } { \int _ { x _ { \cdot } ^ { * } } ^ { \infty } [ 1 - F ( x _ { i } , \theta _ { i } ) ] d x . } \end{array}$ . The <sup>i</sup>benefits of evaluating a particular application correspond to this area multiplied by $\beta .$ Alternatively this area can found by $c _ { i } / \beta$ and results in the point $x _ { i } ^ { * }$ (where the benefits of evaluating this application are equivalent to the costs of performing the evaluation). As it becomes less expensive to perform a detailed evaluation, this ratio gets smaller and the corresponding area decreases. Decreasing this area results in a larger value for $x _ { i } ^ { * } ,$ which is an indicator of the degree to which the firm can expect to increase its total benefits if it conducts a detailed evaluation of Application i. Because it incorporates the initial information about applications, the cost of evaluating them, and the importance of the information gathered in the evaluation, the statistic $x _ { i } ^ { * }$ can be used to compare the expected benefits of investing in a detailed evaluation of different applications for which the initial information and cost of performing a detailed evaluation differ.

## 3.3. The optimal selection strategy

The optimal selection strategy specifies the order in which alternative candidate solutions should be evaluated in detail and at which point evaluations should stop and a selection be made. This strategy was fully specified and proven to be optimal in [19] and involves the following procedure:

1. Rank the applications according to their respective search potential so that $x _ { 1 } ^ { * } \geq x _ { 2 } ^ { * } \geq x _ { 3 } ^ { * } \geq \cdot \cdot \cdot \geq x _ { n } ^ { * }$

2. Evaluate the applications in this order,

3. Select the first application whose obtained score after the detailed evaluation is greater than the $x ^ { * }$ of the next application to be evaluated.

The optimal strategy assumes a sequential search, as follows. The firm decides to evaluate an application, for example Application 1, and conducts the evaluation at some cost $c _ { 1 } .$ This detailed evaluation generates an evaluation score $x _ { 1 } .$ . The decision to perform a detailed evaluation of Application $^ { 2 , }$ with associated cost $c _ { 2 } ,$ will depend on whether the following holds:

$$
[ \alpha + \beta x _ {1} ] <   \int_ {x _ {1}} ^ {\infty} [ \alpha + \beta x ] d F (x, \theta_ {2}) + [ \alpha + \beta x _ {1} ] F (x _ {1}, \theta_ {2}) - c _ {2}\tag{4}
$$

or using integration by parts

$$
c _ {2} <   \beta \int_ {x _ {1}} ^ {\infty} [ 1 - F (x, \theta_ {2}) ] d x\tag{5}
$$

The left-side of Eq. (4) corresponds to the expected benefits if the firm ends the search now and selects Application 1, the rightside corresponds to the expected benefits if the firm evaluates Application 2 and bears the search cost $c _ { 2 } .$ It will be optimal to evaluate Application 2 if and only if the right side is greater, that is if and only if the search potential $x _ { 2 } ^ { * }$ of Application 2 is greater than the $x _ { 1 }$ score obtained from the detailed evaluation of Application 1.

![](/api/attachments/JK6NJ466/fulltext/images/7cead3f68943aa92d868fe26b63b559f2ae038f76b1693d62a6e22830c60a805.jpg)

## 4. The impact of changes in the parameters on the selection strategy

Given some initial software selection situation with parameters $\left\{ F ( \cdot ) , \{ \theta _ { i } , c _ { i } \} _ { i \in \{ 1 , \ldots , n \} } ; \beta \right\}$ we can compute the optimal selection strategy which will be characterized by some $x _ { 1 } ^ { * } \geq x _ { 2 } ^ { * } \geq \cdot \cdot \cdot \geq x _ { n } ^ { * } .$ From these parameters it is possible to evaluate how different events can change the search potential for different applications and consequently affect the probability that each solution i is selected. In addition, it is possible to compute (1) the expected number of applications that will undergo a detailed evaluation, (2) the total costs of conducting the detailed evaluations, and (3) the expected benefit of the selected application net of the costs of the selection process. Thus we can demonstrate how changes in the primitive parameters of the model impact the search potential of the various applications and in turn the selection outcomes.

## 4.1. Factors affecting the search potential and order of evaluation

As previously, buyer perceptions based on initial information are represented by two different distributions $F ( x _ { i } | \theta _ { i } )$ for which the costs of performing a detailed evaluation are equal. If we assume that $\beta = 1 0$ and that the cost of evaluating each application is equal to 10 then $c _ { i } / \beta = 1 0 / 1 0 = 1$ . The value o $\mathbf { \dot { x } } _ { i } ^ { * }$ that corresponds to this area for Application A is $x _ { A } ^ { * } = 8 0$ and for Application B is $x _ { B } ^ { * } = 8 9$ indicating that Application B has a greater search potential than Application A (see Fig. 3). We would evaluate Application B before evaluating Application A. Assuming that the best score obtained from detailed evaluations conducted so far is $x _ { i } = 8 5 ,$ , it would be worthwhile to evaluate Application B but not Application A.

Now assume that the costs of evaluating the two applications are very different and that the cost of evaluating Application B is 100. Perhaps it is the product of an overseas vendor and the only reference site using it is located on another continent so that it will be necessary to send a team out to evaluate it in detail, or suppose that the reference site and the acquiring firm are in different industries or that Application B is based on a technology unfamiliar to the acquiring firm’s technical staff. Using the same approach c $\beta = 1 0 0 / 1 0 = 1 0$ and this area corresponds to $x _ { B } ^ { * } = 6 3$ . This is illustrated in Fig. 4. Given this change in evaluation costs for Application B, its search potential is now less than the search potential of Application A.

Assume now that some positive and reliable initial information was obtained concerning Application $\mathsf { B } ,$ perhaps the vendor’s sales representative learned that the firm is in the market for an application and shared with the buyer the functional specifications document for a ‘‘soon to be released’’ new browser-based version that enables access by remote users. Changes in initial information $\theta _ { i }$ change buyer perceptions about an application and these are captured in the changed shape of the distribution $F ( x _ { i } | \theta _ { i } )$ . If the relative costs of evaluating Application B did not change, the area $c _ { B } / $ $\beta = 1 0 0 / 1 0 = 1 0$ now corresponds to $x _ { B } ^ { * } = 8 4 ,$ , as shown in Fig. 5. The search potential of Application B now exceeds that of Application $\mathsf { A } .$

![](/api/attachments/JK6NJ466/fulltext/images/f69c9922b1cf02a5de1c43098fc8992b44401156bf905e407f8e68f186e8b395.jpg)  
Fig. 4. Application B costs more to evaluate.

![](/api/attachments/JK6NJ466/fulltext/images/05e5ae1dcbd701cf88c86eed9daa512afab545825dd32c8fb9f8a1921e622a0b.jpg)

![](/api/attachments/JK6NJ466/fulltext/images/dce5bce436c78e6335610c2b06b28d220eb2a3af3b421e953cceb4448eb62156.jpg)  
Fig. 5. New initial information about Application B.

![](/api/attachments/JK6NJ466/fulltext/images/4acbf8fd0928351ffb61350376feab7014016d482bfd2b4a29aed6828517a882.jpg)  
Fig. 6. An increase in b.

The impacts of changes in the costs of conducting a detailed evaluation and in the initial information about an application are such that, by holding the importance of the application constant, increasing (decreasing) the costs of evaluating an application will lower (raise) its search potential and reliable positive (negative) information about an application will increase (decrease) its search potential. However, a change in the value of the parameter $\beta$ is ambiguous with respect to its impact on the search potential of the applications being considered for evaluation. As the case in Fig. 6 shows, the acquiring firm may realize that the acquisition of this particular type of application is more important to meeting its strategic objectives than originally thought. This corresponds to an increase in the value of $\beta ,$ perhaps to $\beta = 2 0$ . Using the costs associated with evaluating each application, the area for Application A is now $c _ { A } / \beta = 1 0 / 2 0 = 0 . 5$ and for Application B $c _ { B } / \beta = 1 0 0 /$ $2 0 = 5 .$ From the corresponding $F ( x _ { i } | \theta _ { i } )$ this generates $x _ { A } ^ { * } = 8 6$ and $x _ { B } ^ { * } = 9 0$ . Application B still has the greater search potential.

![](/api/attachments/JK6NJ466/fulltext/images/2b70bd2c04951b5ce06c7c860298886d544f9ff374ff35e0e19a988a938bc3ce.jpg)

But now consider the case in Fig. 7. Instead of an increase in the importance of the application, the firm determines that the application is less strategically important than was first believed. This may cause the estimate of $\bar { \beta }$ to decrease from 10 to 5 and results in $x _ { A } ^ { * } = 7 4$ and $x _ { B } ^ { * } = 7 0 .$ . Application A now has the greater search potential.

![](/api/attachments/JK6NJ466/fulltext/images/e3ac252e16efd206d07a2493158d91b6defe8e6c53e976cfc48081d9299c05af.jpg)  
Fig. 7. A decrease in b.

Increasing (decreasing) the value of $\beta$ holding the costs of evaluation and initial information constant will increase (decrease) the value of all $x _ { i } ^ { * }$ although the magnitude in the change of x<sup></sup> may differ from one application to another, depending on what the buyer expects to find by conducting a detailed evaluation of that application.

## 4.2. The probability of being selected

In a sequential search, when all solutions are ex ante perceived as identical, the investigator will be indifferent about the order in which solutions are investigated, but not the vendors. Thus we can expect that vendors will act in ways to influence the parameters that can affect the search potential of their application since the probability that a particular application will be selected depends on its position in the selection strategy. This position is a function of its search potential $x ^ { * } ;$ : the earlier in the order of evaluation, the greater the probability of it being selected. This probability can be determined formally as show in Eq. (6) of Appendix $\mathsf { A } .$

If the $x ^ { * }$ are initially very close to one another, then a small change in $x _ { i } ^ { * }$ may have a large impact on the probability that solution i is selected as even a small change may leapfrog a large number of other applications to achieve an earlier place in the order of evaluation. On the other hand, when the $x ^ { * }$ are initially very different, a large change in $x _ { i } ^ { * }$ may be necessary to cause a change in order. Application i will be selected after the evaluation of the application with the next highest $x ^ { * }$ if:

![](/api/attachments/JK6NJ466/fulltext/images/50a03355d079659fac108e5f67a204c3d5e61f088ea09dc6b2d8bb8622518327.jpg)

1. all previously evaluated applications have an evaluation score x less than $x _ { i } ^ { * }$ (the condition under which Application i will be evaluated);

2. Application i turns out to have the highest evaluation score x among all the applications evaluated so far and;

3. $x _ { i } \geq x ^ { * }$ for the application following Application i in the order of evaluation (the condition under which the search ends so that the next application is not investigated).

## 4.3. The expected net benefit for the buyer

The expected net benefit for the buyer is the benefit of the selected solution $( \pi _ { i } )$ minus the expected evaluation costs of all evaluated solutions. This is formally calculated using Eq. (8) of Appendix A. One can verify that holding the order of evaluation constant, the expected net benefit of the selection process increases with a decrease in evaluation costs of any Application $i ,$ with an increasing number of potential solutions n, and with a larger $\beta .$

Furthermore, the expected net benefit increases if the buyer receives positive prior information about any application i that shifts the distribution $F ( x _ { i } , \theta _ { i } )$ to the right. Even though the net benefit of the selection process increases with these changes, holding the selection strategy constant results in a sub-optimal process. Adjusting the selection strategy to take into account the impact of these changes on the $x _ { i } ^ { * }$ will tend to increase the net expected benefits of the selection process and, at a minimum, will generate benefits equal to those before the selection strategy is adjusted.

## 4.4. The expected number of evaluated solutions and evaluation costs

The basic model also allows calculation of the expected number of evaluated solutions and total cost of the selection process. The expected number of evaluated solutions is the sum of the probabilities that each individual solution i will be evaluated under the optimal search rule. Similarly, the expected evaluation costs for the acquisition are the sum of each $c _ { i }$ times the probability that each application i is evaluated. These results are developed formally in Eq. (9) in Appendix A.

Here, insofar as the order of evaluation changes with changes in the values of $\beta , c _ { i } , \mathrm { o r } \theta _ { i } ,$ there is no clear prediction of the impact on the expected number of evaluated solutions or on the total costs of the selection process. In general, an increase in the value of $\beta$ will increase all $x _ { i } ^ { * } .$ . If the order of evaluation does not change, this overall increase in the $x _ { i } ^ { * }$ will increase both the expected number of evaluated solutions and the total evaluation costs. However, this need not hold if the order of evaluation changes. $\mathsf { A }$ solution that looks highly promising but that is very costly to evaluate may move up (earlier) in the order of evaluation. This would lead to a higher expected search costs but a lower expected number of evaluated solutions. Alternatively, if this solution moves down (later) in the order of evaluation the opposite may occur.

Similarly, a decrease in $c _ { i } ,$ or an increase in $\theta _ { i }$ will increase the value of $x _ { i } ^ { * }$ . If the order in which solutions are evaluated remains unchanged, it will increase the probability that solution i is evaluated and increase the expected number of evaluated solutions. An increase in $\theta _ { i }$ will also lead to an increase in the expected total evaluation costs. However, whether the magnitude of the decrease in $c _ { i }$ will offset the costs associated with evaluating a larger number of solutions is uncertain. If the order of evaluation does change there is little that can be said about how the number of evaluated solutions or the total evaluation costs will be affected.

The results of changes to the parameters of the model are summarized in Table 1.

## 5. Implications of applying search theory to the determining a selection strategy

Two important insights gained from taking a search theoretic approach to software selection are (1) the role that the firm’s initial information about alternative products can play in the outcome of its selection decision, and (2) the explicit consideration of the value of the application to the firm in determining the selection strategy.

The buyer’s perceptions of what they would actually discover if they were to undertake a detailed evaluation of a product, represented in the model by the distribution F(x ju ) plays a key role in influencing the particular application selected. Assuming approximately equivalent costs to evaluate different alternatives, expected high evaluation scores result in high search potential. If this potential is not realised after a detailed evaluation, the firm will have needlessly conducted a detailed evaluation of an application which did not merit such an investment. The selection process will be longer and more costly than it would otherwise be as buyers will need to proceed further down the list of rankordered applications before making a choice. Similarly, an expected low score will result in a low search potential and promising applications may be erroneously placed further down the rank-ordered list than they merit. In this case the firm risks choosing too early and selecting a less appropriate alternative or prolonging the time and cost of the selection process by conducting detailed evaluations of products whose search potential were not realised because it was underestimated.

A search theoretic approach forces the evaluators to focus on the problem of ensuring that their perceptions of the capabilities of alternative software products are in line with reality. Software selection, rather than being viewed as a project with a distinct beginning and end, may more profitably be viewed and managed as an ongoing process having long periods of low level intelligence gathering and awareness building punctuated by intense periods of detailed evaluation and choice. Thus one result of taking this perspective is to cause a re-examination of the way in which we acquire software.

One potential impact of not re-examining the way we acquire software is, that in cases where money and time are scarce resources, an established application product may be at a disadvantage against newer, competing products in the selection process. Buyers may be encouraged to investigate new applications for which they have only a small amount of promising information at the expense of existing products about which they may feel they already know enough. When resources are scarce firms may actually substitute their initial information about products that they ‘‘know’’ for a detailed evaluation, thereby raising the potential for mis-ranking products and increasing the chance of making a sub-optimal choice. This problem may arise most acutely in small and medium-sized firms where resources are constrained. From a practical perspective, this means that vendors of established products must be conscientious in their efforts to inform the market of improvements to their product and not simply rely on past marketing successes.

Table 1  
The result of changes in the parameters on model outcomes.

<table><tr><td></td><td>Increase in  $c_i$ </td><td>Increase in  $\beta$ </td><td>Increase in  $\theta_i$ </td><td>Increase in n</td></tr><tr><td> $x_i^*$ </td><td>Decreasing</td><td>Increasing</td><td>Same or increasing</td><td>n/a</td></tr><tr><td>Rank order of Application i</td><td>Same or later</td><td>Ambiguous</td><td>Same or earlier</td><td>Same or later</td></tr><tr><td>Probability of i being selected</td><td>Decreasing</td><td>Ambiguous</td><td>Same or increasing</td><td>Same or decreasing</td></tr><tr><td>Expected net benefit</td><td>Same or decreasing</td><td>Increasing</td><td>Same or increasing</td><td>Same or increasing</td></tr></table>

A third impact of bringing the influence of initial information to the fore is the question of what types of information are best suited to keeping perceptions aligned with reality (vendor literature, trade magazine articles, site visits, case studies, etc.). Although the search theoretic approach highlights this question it does not provide any insights into an answer.

The probability that the ith solution is selected when $x _ { 1 } ^ { * } = \cdot \cdot \cdot = x _ { n } ^ { * } = x ^ { * }$ , is given by:

$$
F (x ^ {*}) ^ {i - 1} [ 1 - F (x ^ {*}) ] + \int_ {0} ^ {x ^ {*}} F (s) ^ {n - 1} d F (s)\tag{7}
$$

which decreases the further down the order of evaluation the application is found.

## A.2. The expected net benefit for the buyer

The expected net benefit for the buyer is the benefit of the selected solution $( \pi _ { i } )$ minus the expected evaluation costs. For a given vector $x ^ { * } ,$ , we denote by $x _ { ( i ) } ^ { * }$ , the ith highest value of $x ^ { * }$ so that $x _ { ( 1 ) } ^ { * } \geq x _ { ( 2 ) } ^ { * } \geq \cdot \cdot \cdot \geq x _ { ( n ) } ^ { * }$

$$
\max _ {x ^ {*}} \sum_ {j = 1} ^ {n} \left[ \left(\prod_ {k <   j} F (x _ {(j)} ^ {*}, \theta_ {(k)})\right) \left(\int_ {x _ {(j)} ^ {*}} ^ {\infty} [ \alpha + \beta x ] d F (x, \theta_ {(j)}) - c _ {(j)} + \int_ {x _ {(j + 1)} ^ {*}} ^ {x _ {(j)} ^ {*}} [ \alpha + \beta x ] d \left(\prod_ {k \leq j} F (x, \theta_ {(k)})\right)\right) \right]\tag{8}
$$

A second key implication of the search theoretic approach is the importance of properly assessing the value of the expected benefits of acquiring the application. This is represented in the model by the parameter b. A large $\beta$ implies that additional information that results in small changes to the evaluation score has a large impact on expected benefits. In such a situation one would benefit from knowing as much as possible about the alternatives before making the final decision. This is a very different view from that taken in the existing selection literature, where the amount of information to be gathered is based on the number of requirements. A requirements-based approach may lead a firm to expend significant effort on a selection process for an application with complex requirements but of little strategic value. In the search theoretic approach, the amount of information to be gathered is based on the overall value of the application to the firm, thereby aligning software selection with firm strategic direction.

Our approach explicitly recognises that software acquisition is a probabilistic endeavour. One will never be certain of the true benefits that will accrue from the adoption of a software application until after the product has been implemented and incorporated into the business processes of the firm. It does however show how a firm can increase its chances of selecting the correct product, in particular, by ensuring that its initial information is in line with the capabilities of different products and that it understands the business value of the type of product being selected. With this information in hand, the approach leads to an optimal selection strategy.

The development of a sound theoretical understanding of the selection activities of organisations can benefit both those who practice in this industry and those who analyze it.

## Appendix A

## A.1. The probability that an application is selected

The probability that an application ranked ith in the evaluation process is selected is computed as:

$$
\left(\prod_ {j <   i} F \left(x _ {i} ^ {*}, \theta_ {j}\right)\right) \left[ 1 - F \left(x _ {i} ^ {*}, \theta_ {i}\right) \right] + \sum_ {k = i} ^ {n} \int_ {x _ {k + 1} ^ {*}} ^ {x _ {k} ^ {*}} \left(\prod_ {j \neq i _ {j \leq k}} F (s, \theta_ {j})\right) d F _ {i} (s, \theta_ {i}) \tag {3}\tag{6}
$$

Notice that the above expression is increasing with a decrease in search costs, $c _ { i } ^ { \prime } s ,$ and increases with the number of potential solutions, $n ,$ and the parameters $\beta$ and $\alpha .$ . Furthermore, this above expression is increasing if the buyer receives prior information $\widehat { \theta } _ { i }$ rather than $\theta _ { i }$ such that $F ( x , { \hat { \theta } } _ { i } ) \leq F ( x , \theta _ { i } )$ Þ. Hence, holding the search rule constant, the expected net benefit for the buyer increases with these changes, so a fortiori the expected net benefit if the search strategy is optimized.

## A.3. The expected number of evaluated solutions and evaluation costs

The basic model also permits us to calculate the expected number of evaluated solutions and total search cost. These are given as:

expected number of evaluated solutionsÞ $= 1 + \sum _ { i = 2 } ^ { n } \left( \prod _ { k < i } F ( x _ { i } ^ { * } , \theta _ { k } ) \right)$ expected total search cost $= c _ { 1 } + \sum _ { i = 2 } ^ { n } c _ { i } \Biggl ( \prod _ { k < i } F ( x _ { i } ^ { * } , \theta _ { k } ) \Biggr )$

(9)

The expression $\begin{array} { r l } { \big ( \prod _ { k < i } F ( x _ { i } ^ { * } , \theta _ { k } ) \big ) } & { { } } \end{array}$ corresponds to the probability that Application i will be evaluated under the optimal search rule. The expected number of evaluated solutions is the sum of the probabilities that each individual application i will be evaluated under the optimal search rule. Similarly, the expected evaluation costs for the acquisition are the sum of each $c _ { i }$ times the probability that each Application i is evaluated.

Here, the effect of changes in $\beta , c _ { i } ,$ or u is ambiguous. Suppose that the evaluation cost of one solution, $c _ { i } ,$ decreases. The value $x _ { i } ^ { * }$ will increase. If the order in which solutions are evaluated remains unchanged, this will increase the probability that solution i is evaluated and increase the expected number of evaluated solutions. However, if the order is affected, which might occur for a sufficiently large change in $c _ { i } ,$ , we cannot make a general statement about the impact on the expected number of evaluated solutions. Indeed, a solution that looks highly promising but costly to evaluate may move up the evaluation order leading to higher expected search cost but a lower expected number of evaluated solutions.

## References

[1] B. Boehm, D. Port, Risk-based strategic software design: how much COTS evaluation is enough? Third International Workshop on Economics-Driven Software Engineering Research (EDSER-3), Toronto, Canada, 2001.

[2] P. Bourque, R. Dupuis (Eds.), SWEBOK: Guide to the Software Engineering Body of Knowledge, IEEE Computer Society, Los Alamitos, CA, 2004.

[3] E. Brynjolfson, The productivity paradox of information technology, Communications of the ACM 36 (12), 1993, pp. 67–77.

[4] CODASYL Systems Committee, Feature analysis of generalized data base management systems, CODASYL Systems Committee Technical Report, May 1971.

[5] C. Holland, B. Light, A critical success factors model for ERP implementation, IEEE Software 16 (3), 1999, pp. 30–35.

[6] W.J. Johnston, J.E. Lewin, Organizational buying behavior: toward an integrative framework, Journal of Business Research 35, 1996, pp. 1–16.

[7] R.G. Kauffman, P.T.L.P. Leszcyc, An optimisation approach to business buyer choice sets: how many suppliers should be included? Industrial Marketing Management 34, 2005, pp. 3–12.

[8] L.J. Kirsch, Portfolios of control modes and IS project management, Information Systems Research 8 (3), 1997, pp. 215–239.

[9] V.S. Lai, B.K. Wong, et al., Group decision making in a multiple criteria environment: a case using the AHP in software selection, European Journal of Operationa Research 137 (1), 2002, p. 134.

[10] S. Lauesen, COTS tenders and integration requirements, 12th International Requirements Engineering Conference, Kyoto, 2004.

[11] P.K. Lawless, K.E. Mark, et al., A formal process for evaluating COTS software products, IEEE Computer (May), 2001, pp. 58–63.

[12] K.R.P.H. Leung, H.K.N. Leung, On the efficiency of domain-based COTS product selection method, Information and Software Technology 44 (12), 2002, p. 703.

[13] N. Maiden, C. Ncube, Acquiring COTS software selection requirements, IEEE Software (March/April), 1998, pp. 46–56.

[14] M. Ochs, D. Pfahl, et al., A method for efficient measurement-based COTS assessment and selection—method description and evaluation results, 7th IEEE International Software Metrics Symposium (METRICS 2001), London, England, 2001.

[15] D. Port, Z. Chen, Assessing COTS assessment: how much is enough, International Conference on COTS-Based Software Systems, Redondo Beach, CA, 2004.

[16] U.S. Bureau of Standards, Six database management systems: feature analysis and user experiences, Technical Note 887, 1975.

[17] J. Verville, A. Halingten, A six-stage model of the buying process for ERP software, Industrial Marketing Management 32 (7), 2003, p. 585.

[18] C.-C. Wei, C.-F. Chien, et al., An AHP-based approach to ERP system selection, International Journal of Production Economics 96 (1), 2005, pp. 47–62.

[19] M.L. Weitzman, Optimal search for the best alternative, Econometrica 47 (3), 1979, pp. 641–654.

[20] E.J. Wilson, R.C. McMurrian, et al., How buyers frame problems: revisited Psychology & Marketing 18 (6), 2001, p. 617.

[21] Wu, Ing-Long, Yuh-Chen Shen, A model for exploring the impact of purchasing strategies on user requirements determination of e-SRM, Information & Manage ment 43 (4), 2006, pp. 411–422.

[22] Y. Yang, J. Bhuta, et al., Value-based processes for COTS-based applications, IEEE Software (July/August), 2005, pp. 54–62.

![](/api/attachments/JK6NJ466/fulltext/images/a076d78e84ef0ce80c81430ebdbdcebd3a64ec68fbd8dec63c2065f7e07f8772.jpg)

Michael Wybo is an associate professor in information technologies at HEC Montre´al. He coordinates the MBA program in IT and returned to research and teaching after holding executive positions in Canadian and US software firms. His research interests include software sales and selection processes and IT services best practices. He received his PhD from the Carlson School at the University of Minnesota.

![](/api/attachments/JK6NJ466/fulltext/images/5f700e736d7a69bbe32fb918fadc662c6b780941002140aef352c0d4bb88c3d6.jpg)

Jacques Robert is an associate professor in IT at HEC Montre´al. He holds a PhD in economics from the University of Western Ontario and was a professor at the Economics Department of the Universite´ de Montre´al before moving to HEC Montre´al. His research interests are applied game theory, mechanism design and experimental economics. He has published in economics, operational research, and neural computing. He is a fellow at CIRANO, co-director of the masters in e-commerce at the Universite´ de Montre´al and chairman of Baton Simulations.

![](/api/attachments/JK6NJ466/fulltext/images/3030702a1fc6208bfb93bf99f1df81f30da0eda64470056aba64c5a31b001296.jpg)

Dr. Pierre-Majorique Le´ger is an associate professor in information technologies at HEC Montre´al and director of the ERPsim Lab. He holds a PhD in industrial engineering from E<sup>´</sup> cole Polytechnique de Montre´al and has done post-doctoral studies in information technologies at HEC Montre´al and NYU Stern. His research focuses on enterprise systems, diffusion in networks, the value of IT investments and electronic collaboration in supply chains. He is a co-creator of ERPsim, a simulation game to teach ERP concepts, which is now used in more than 50 universities worldwide and many Fortune 1000 organisations such as ABB, Conoco Philips and Deloitte.
