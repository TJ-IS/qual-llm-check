---
otero_id: 9806
otero_key: "Y5A3BGJH"
title: "The ambiguous proposal evaluation problem"
authors: "Mehdi Rajabi Asadabadi; Ofer Zwikael"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113359"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The ambiguous proposal evaluation problem

Mehdi Rajabi Asadabadi<sup>a,b,⁎</sup>, Ofer Zwikael<sup>a,⁎</sup>

![](/api/attachments/Y5A3BGJH/fulltext/images/2ec50d80340ed32c676dae3358f27218fe58bd6a5f6756dd16317b464365aba2.jpg)

<sup>a</sup> College of Business and Economics, The Australian National University, Canberra, Australia

<sup>b</sup> School of Business, The University of New South Wales, Canberra, Australia

## A R T I C L E I N F O

Keywords: Proposal selection problem Ambiguous specifications MCDM methods Fuzzy set theory

## A B S T R A C T

A complex decision-making challenge senior managers commonly face is the selection of the winning bid from multiple project proposals. Project selection decisions become more complex when providers deliberately choose to introduce ambiguity to their project proposals rather than address the client's predetermined set of desired specifications. In particular, providers suggest in their proposals a range of values for some product specifications. Providers introduce ambiguity for various reasons, such as future technological advances and strategio misrepresentation. Further, such disruptive behaviour is tolerated by clients for reasons such as ambition, lack of knowledge, uncertain needs, complexity and a lack of competition. This paper defines the ambiguous proposal evaluation problem and develops a solution which enables such proposals to be compared and ranked. The solution is developed through the utilisation of fuzzy logic in combination with a multi-criteria decision-making method, and is illustrated on a procurement project. The contribution of this paper is firstly to define a practical problem in the literature and secondly to develop a solution which enables ranking ambiguous options.

## 1. Introduction

The decision which project proposal to select in a bid process is a complex one for senior managers, with significant future implication for their organisation. The process of selecting the winning bid from multiple project proposals commonly commences with the project client organisation's request for proposals from external providers [41]. While the proposals are expected to comply with a predetermined set of desired specifications, known as project scope [7], providers often in troduce ambiguity into the scope of their proposals [2]. This ambiguity makes the proposal evaluation process challenging as the client organisation becomes unable to clearly compare the proposals. This is labelled in this paper as the “ambiguous proposal evaluation problem” and is defined as clients evaluating various project proposals that in clude ambiguity in their scope.

Ambiguity is generally introduced to the scope by potential providers for reasons such as uncertainty with regard to future technological advances [31] and strategic misinterpretation for increasing their fu ture potential earnings [17]. This providers' disruptive behaviour typically involves the introduction of a range of values for product specifications rather than a confirmation that they will meet the predetermined scope required by the client precisely. Interestingly, clients commonly tolerate this disruptive behaviour for various reasons, such as hoping to materialise upside of the ambiguity later in the project [16] and lack of suficient domain knowledge to discuss and specify the details [3]. Given the aforementioned reasons from both providers and clients, the ambiguous proposal evaluation problem is common and has significant implication on the decision making process when selecting a winning bid. In particular, this ambiguity may cause decision failure in selecting the best proposal and may result in the selection of a proposal which is unable to deliver the client's original expectations.

However, the existing literature does not discuss the problem of evaluating and comparing proposals with ambiguous specifications. Although the research acknowledges the existence of uncertainty in the selection process [36], it commonly assumes clarity in the available options. The consideration of uncertainty in the selection process has so far been in regard to ‘obtaining the weightings of the evaluation criteria’, or ‘assigning scores to the options with respect to the criteria’ – which fails to consider the possibility of having ambiguous options. Despite its significance, the ambiguous proposal evaluation problem seems to be understudied in the research.

Therefore, this study attempts to address the following research question: “How can ambiguous proposals be compared and ranked effectively to support decision making?”. To address this research question, the paper develops a solution utilising fuzzy logic in combination with a multi-criteria decision-making method (MCDM), namely best worst method (BWM). In the proposed solution, to enable a comparison of the available options, subject-matter experts from the client side modify the range of values suggested in the available proposals. Taking into account their level of confidence in the modified specification, the relative importance of each product characteristic and the client's desired ranges for the specifications, a satisfactory score for each proposal is computed and the proposals are ranked. The paper contributes to the Decision Science literature by developing new knowledge to support decision making under ambiguity. In particular, the paper defines and solves the ambiguous proposal evaluation problem and provides a suitable platform for making efective decisions regarding the evaluation and approval of ambiguous project proposals. The paper further enhances the current knowledge on capabilities of decision support systems by showing that even when options are ambiguous, individuals can use decision support systems and do not have to proceed subjectively or intuitively.

The remainder of this paper is as follows. Section 2 provides a brief review of the relevant papers. Section 3 discusses the problem and provides a case illustration. The solution is proposed in Section 4 and illustrated in Section 5.

## 2. Literature review

This review covers the most relevant literature related to the am biguous proposal evaluation problem, in particular requirement speci fication, as well as prior applications of BWM and fuzzy logic in the field of project evaluation.

## 2.1. Requirement specification

The existing literature on requirement specification is mostly in the context of software engineering. This is probably due to the complexity of requirement identification and the dificulties in requirement defi nition in the field of software engineering.

Diverse tools and techniques have been applied to improve the quality of requirements. A study by Vilpola and Kouri [43] deals with requirement specification in enterprise resource planning (ERP) systems. ERP is an example of complex projects that involve the definition of multiple requirements. As the number of requirements increase, the risk relevant to stating requirements ambiguously, with internal conflicts, or those that are unverifiable, also increases. Similarly, Mallek et al. [28] focus on requirement specification aiming to improve requirement verifiability. A survey is conducted to enrich the list of requirements from diferent partners. Zuo [47] proposes a framework to specify requirements aiming to improve system survivability (a system's ability to provide essential services and recover, in the case of attacks and failures). Rashid et al. [38] argue that the requirement specification process needs to extensively involve users in the process and since users are not experts in the software domain, they design a user-friendly visual requirement specification process. In a very similar study, Bang [5] develops an agile requirement specification approach in software engineering to increase the speed of the specification process through face-to-face communications. There are also examples of applications of text mining tools and techniques to identify words and sentences that have the potential to create ambiguity later in the software development process. Femmer et al. [13] develop a text-mining-based tool capable of identifying the above-mentioned ambiguity and examine methods on documents written in German utilising dictionaries and part of speech (POS) tagging. The accuracy of the method is later evaluated in another study by Femmer et al. [14]. Various tools and techniques have been developed to improve the quality of requirements in the domain of software engineering.

After reviewing the most related papers, it becomes clear that insuficient research attention has been given to the ambiguous project proposal evaluation problem. The only relevant paper is a recent study by Asadabadi et al. [1], which focuses on requirement specification in large-scale projects. They suggest focusing on information that is not stated in the project's documentation but is implied. Such information may include ambiguity and fuzziness. They develop a method, relying on fuzzy set theory, to identify and address such fuzziness. While we acknowledge the necessity of further studies on requirement specification in large-scale projects, the problem discussed here will remain novel even after such future studies. In this paper, the focus is on the case where the requirements are set unambiguously by the client. However, for the reasons explained in the introduction, the potential providers involve ambiguity in the process. This ambiguity makes the evaluation process a challenging problem for which a solution will be proposed in this paper (see Section 5). In the next section, the existing applications of MCDM methods to address project and portfolio selec tion problems are reviewed.

## 2.2. Applications of MCDM methods in project evaluation

The project selection problem usually requires evaluating the performance of the available projects with respect to selecting criteria. Research has already examined MCDM methods to evaluate the available projects and provides solutions for selection problems, especially in complex projects. A review of the research is given in this section.

Mavrotas et al. [29] study the robustness and reliability of the in formation that managers/decision makers receive. They focus on reducing the uncertainty of such information by proposing a multi-objective combinatorial optimisation approach, which utilises the Monte Carlo simulation process. Jeng and Huang [23] propose a decision model for evaluating project portfolios in the initial stages of a research program. They develop a model that relies on two techniques: ANP and Delphi. Although their study discusses an interesting case of portfolio evaluation and provides a rational list of decision criteria, their justification of ANP applications does not seem to be quite valid. For example, it is not clear how and why the criteria afect their own weightings and why such consideration makes the model more reliable. While admitting that the consideration of the ANP approach makes the selection model less sensitive to changes in criteria weightings, this is not necessarily a positive characteristic for a selection model. Karasakal and Aker [25] prioritise a set of projects by designing a hierarchal structure to identify the most important evaluation criteria, relying on the analytic hierarchy process (AHP). Fiala [15] assumes budget restrictions when developing an evaluation approach which relies on data envelopment analysis. Bonetti et al. [6] use ordered weighted mean to aggregate individual estimates in project management and exploit the synergies between experts and non-experts in an MCDM framework.

These papers are examples of the relevant applications of MCDM to address selection problems in project management. This study utilises a recent MCDM approach, namely the best worst method (BWM) [39]. In this method, firstly the best and worst criteria are selected. Then, other criteria are compared with them and relative weightings are assigned. Despite the fact that this method was proposed only recently, it has received considerable attention [26]. While applications of BWM to address diferent problems have been proposed, the method has not yet been applied to evaluate multiple proposals. In this study, BWM is used to find the importance weightings of diferent characteristics/specifications of the proposed solutions.

## 2.3. Soft computing in project evaluation

Soft computing techniques are commonly used to address a range of uncertainty-related problems in the literature [8,9,27]. There are examples of applying soft computing techniques, i.e. fuzzy models, in combination with MCDM methods to evaluate multiple projects, some of which are reviewed here.

Schaefer and Cruz (2016) focus on the project evaluation process where budget is the main constraint of the selection problem. They divide each proposal into its various tasks and develop a fuzzy-based model to compare the proposals. The application of fuzzy set theory in their study aims to cover uncertainty with regard to project budget. In a similar study, Perez and Gomez [35] develop a project evaluation approach with a fuzzy budget constraint. Considering the budget constraint, they provide a ranking of projects to help managers select those which contribute more to achieving the objectives. By contrast, Zhang et al. [45] utilise fuzzy linguistic preference relations to deal with the impreciseness and uncertainty of criteria weightings and the available historical data in project portfolio selection. Jafarzadeh et al. [21] highlight the importance of prioritising the existing projects considering the budget limitations that exist in almost every organisation. They propose a combination of data envelopment analysis and quality function deployment. In their proposed method, fuzzy logic is utilised to deal with the impreciseness of the relations among elements of quality function deployment. Zhou et al. [46] propose a group decision making model to rank projects. In the proposed group decision-making mode, fuzzy modelling is used to deal with the uncertainty of the de. cision environment. Further, they use hesitant fuzzy numbers to compute the return and risk of the projects. An extensive application of fuzzy set theory can be observed in the study on project portfolio evaluation conducted by Guo et al. [18]. Their proposed selection model is designed to select those projects which maximise strategic contribution and financial returns. To do so, parameters, such as financial returns, costs, potential risks, resources, and even the objective function, are structured using fuzzy models to reduce uncertainty in their proposed decision model.

![](/api/attachments/Y5A3BGJH/fulltext/images/b457d19f207f1c80373fa4af2e15f36e136ea5d8762ced586406e0ad9f41d8e2.jpg)  
a – Precise scope: Equally attractive proposals

![](/api/attachments/Y5A3BGJH/fulltext/images/19a0fa929265c52b21960ca82f032c036d9c817e4ab491e786f18cc793079a64.jpg)  
b – Precise scope: Proposal B is more attractive than A

![](/api/attachments/Y5A3BGJH/fulltext/images/15d16a74d6efaa6f04843f10cf9eb92c780106bc8922c2b71b8585fd9fa1e17b.jpg)  
c – Ambiguous scope: Unclear proposal ranking  
Fig. 1. Proposals with two requested specifications.

Despite the existing applications of fuzzy logic in project evaluation, no study has focused on the evaluation problem where providers intentionally involve ambiguity in the project specifications. The literature usually takes project specifications into consideration as a whole, with the name of quality or scope, and a score is assigned to it, usually based on a subjective judgment [33]. The proposal evaluation process under ambiguity has not been discussed in the literature and further studies are needed to investigate its various aspects. In a more telescopic view, the existing literature on applications of fuzzy logic to address uncertainty in MCDM problems usually focuses on uncertainty in computing the weightings of the decision criteria or assigns scores to alternatives with respect to the criteria. The aforementioned literature does consider the ambiguity of alternatives as a problem for which this paper develops a solution.

## 3. The ambiguous proposal evaluation problem

In this section we define the problem in practice and its implications to decision making and organisation performance. As mentioned in the introduction, even though clients request providers to explicitly commit to what they will deliver, potential providers typically involve ambiguity when responding to bid requests. Two key reasons for this disruptive behaviour are: (1) technological uncertainty – provider uncertainty regarding future technological advances that may occur during a long project life [31]; and (2) strategic misrepresentation - manipulation of information by the provider in order to win the project by implying that the product specifications may be better than requested, yet later meeting only the lower bounds of the ambiguous scope [17]. If the client insists on higher standards, the provider is still able to negotiate additional funding for the surplus work required to achieve the scope. Clients, on the other hand, tolerate this disruptive behaviour and do not stress providers to eliminate ambiguity before proceeding with the evaluation process for various reasons: (1) ambition - the client is ambitious, hoping that the better proposed specification ranges will materialise later in the project [16]; (2) a lack of knowledge - the client is less knowledgeable and experienced than the providers about the product which will be delivered and therefore, is less confident about their own initial specifications of the final product [3]; (3) uncertainty - the project will commonly be delivered after a long period of time, during which the specifications of the product are unlikely to remain the same, so insisting on precise specifications may be pointless [22]; (4) complexity – the client acknowledges that the number of requirements is large, and it might be dificult for providers to precisely deliver all the product's specifications [1]; and (5) a lack of competition - there is a limited number of qualified providers and it is not wise to eliminate proposals only because of ambiguity [34].

## 3.1. Problem definition

To illustrate the nature of the problem, assume that the client requests proposals to build a product with only two specifications, namely x and y, which can be considered as the scope of the project. If precise specifications are received, the evaluation process is less challenging as it can be solved as a simple MCDM problem: specifications have dif ferent weightings of importance and depending on how satisfactory each proposal is with respect to the specifications, the proposals are ranked. In other words, the suggested specifications are compared with respect to the utility curve of the client. Fig. 1a and b illustrate two diferent situations that the client may confront depending on the received proposals. The proposals may be viewed as equally attractive (Fig. 1a), or one may be located on a higher utility curve and is therefore more attractive (Fig. 1b). In the first case, the proposals have the same satisfaction level regarding the proposed scope and therefore only the performance of the proposals with regard to the other criteria (e.g. time or cost) need to be considered to select one. In the second case, the MCDM method finds the relative ranking of the two, which is then considered alongside the performance of the proposals with regard to the other criteria to select one. However, in practice, the case becomes more complicated. Providers often involve ambiguity in the specifications of the future product, as presented in Fig. 1c. More specifically, instead of precisely stating what the specifications of the product are, the providers may suggest ranges for specifications, e.g. between $x _ { I }$ and $x _ { 2 }$ and ${ \bf y } _ { 1 }$ and ${ \bf y } _ { 2 } .$ In such cases, it is quite challenging to compare these proposals with regard to the suggested specifications before moving to the next step. For instance, although both the upper and lower bounds of the ranges suggested by provider A in Fig. 1c seem to be better than those suggested by provider B, it does not necessary mean that the precise specifications delivered by provider A will be better than provider B's.

To illustrate further, in the case of procuring some engines, in their request, the client determines the need for a speed of 3500 rpm and torque of 600 nm. A provider may state in their response to this request that:

“The product will have the speed of 3,300-4,000 rpm and the torque of 450-700 nm. Note that our engines are made using xyz technology which enables them to work in high temperature, which is usually more important to organisations because...”

The above response not only involves ambiguity in the suggested specifications, but also introduces other ambiguous requirements to the product. This extra information can be used to educate the client about what they really need, the utilisation of which may require further study. Here, the extra information is disregarded, and the proposal with ambiguous scopes are evaluated.

The ambiguity of the specifications stated by the providers, as illustrated in Fig. 1c, makes the comparison process challenging. Note that even if we assume that the only reason for involving ambiguity in the process – e.g. suggesting intervals for specifications rather than specifically expressing them – is due to the providers' lack of knowledge about the final products in the early stages of projects, it is still hard to believe that these intervals are suggested impartially with no bias or exaggeration. Given this, the suggested ranges for specifications must not be the basis for decisions without analyses and modifications. While the MCDM literature provides solutions when the decision criteria, e.g. specification x and y, are ambiguous, no methodological solution has been proposed to address the problem of ambiguous alternatives, e.g. ambiguous proposals.

## 3.2. Problem case illustration: The Australian Navy submarine project

Due to the reasons explained earlier, namely ambition, lack of knowledge, uncertainty, complexity, and a lack of competition. it is often the case that there is a need to evaluate ambiguous proposals, especially in the public sector. Take the recent procurement project owned by the Australian government as an example: the Shortfin Barracuda Class submarines project. The Australian government received three proposals for this project from German, French, and Japanese companies. While the Japanese option (Soryu class submarines) was the least ambiguous choice (almost buying of the shelf), the two other proposals were considerably ambiguous regarding the specifications of future deliverables [2]. For instance, the French option would require the replacement of the nuclear engine and therefore, the entire system would need to be completely adapted, and the German option would require the combat system to be replaced and the submarine size to be doubled [24,40]. Such huge variations on billiondollar products, especially in relation to the French case, creates considerable ambiguity and uncertainty with regard to the performance of the products (to be delivered after decades). Although Tokyo was fairly confident of winning the project [19], their failure could have been expected because their proposal was quite straight forward and hence in contrast with the government's interest in ambiguous projects. Due to the sensitivity of the case, we might not be able to investigate and find detailed evidence (at least for several years), but we believe their proposal did not have a high chance of success, even though the product was well designed, and the price was completely reasonable and justifiable (about A\$15 billion cheaper than the French submarines). It is suggested that one reason for keeping the Japanese in the tendering process was to have a base for comparing the other two. We believe the Japanese could have had a chance by involving ambiguity and proposing an ambitious project which could be more appealing to the Australian government; and the ambiguity could be resolved and settled later in the project, maybe years after winning the bid. Note that terminating a project or switching to another provider becomes costlier after the project has commenced and the power of the government to do so diminishes (due to public and media pressure accusing the government of making a costly mistake) [2].

In practice, the government's neutral or avid attitude to ambiguity means that ambiguity continues to exist. This attitude is mainly due to two reasons. Firstly, when decision makers use public money, they are less concerned about the amount of money they expend (compared with the private sector). Secondly, decision makers are inherently interested in proposals that are unique even though they are ambiguous and costly. It is disappointing, but it is undeniable that governments tolerate proposals that contain ambiguity. Governments' propensity to initiate unique and ambitious projects often results in unnecessary costs and the waste of public money. This ambition is usually costly and may result in the downside of the ambiguity being realised in later stages of the project where people ultimately have to pay (in the case of Shortfin Class Submarines, it cost the Australian taxpayer \$2000 per person for a project worth A\$50 billion). Note that even in relation to undeniably unsuccessful projects, governments have to exaggerate the outcomes to lessen media and public pressure. The same reason prevents them from terminating a project, even if all signs indicate that it is best terminated. An example of the receipt of low-quality products is the Collins Class Submarines that may unfortunately still be referred to as an achievement by some public servants, despite hundreds of problematic issues with the delivered products, from fuel tanks and engines to propellers [44]. The submarines were demonstrably unable to meet the required performance due to design deficiencies and operational limitations [4,44]. The project cost considerably more than the budget and was delivered with significant delay. One of the areas that is questioned in this project is the selection of a proposal with ambiguous and ambitious specifications proposed by Kockums, a Swedish company.

Considering this study's scope, this paper only focuses on the tech nical side of the problem as follows. While there are a huge number of specifications in the case of building submarines, Fig. 2a shows the specifications of the three submarine options were reduced to two: speed and engine power. Assume that the German and French proposals propose ranges for these two specifications while the Japanese proposal is precise, as presented in Fig. 2a.

The next section suggests a model that enables ranges of specifications to be turned into precise ones for evaluation and comparison purposes, as illustrated in Fig. 2b.

## 4. Developing a solution to the problem

In this section we show how available tools and techniques from the decision-making literature can be combined to address a complex reallife problem. Assuming that we receive multiple proposals with ambiguous specifications, i.e. ranges instead of precise specifications, there are steps to follow to evaluate and select the most suitable proposal. Firstly, the ranges for each product specification need to be converted to a precise specification. To do so, the ranges are associated with complementary ranges suggested by subject-matter experts from the client side. Then, the weighted average of the ranges is computed. Specifications can be related to diferent components of the deliverables and hence may have diferent weightings of importance for the client. These weightings are computed using BWM, and the proposals are ranked in terms of their suggested specifications (scope). After this, the problem becomes a simple multi-criteria decision-making problem, in which the scope of the proposal is only one criterion among other cri teria such as time, cost and benefits. Table 1 summarises the required steps in the proposed solution.

![](/api/attachments/Y5A3BGJH/fulltext/images/a735259bdbbc453a7e2bb0f46b2b661106efb272a14e65bb63e955380f3dda7f.jpg)  
a – Proposals with ambiguous specifications (German and French submarines)

![](/api/attachments/Y5A3BGJH/fulltext/images/17b4cdf59d3b525fca856706fe7e0c76f8da24a2ed50ac085e938f79c9ccc1e9.jpg)  
B – This paper proposes a model that allows evaluation of proposals with ambiguous specifications  
Fig. 2. French, German and Japanese submarine proposals.

## 4.1. Transforming ranges into precise specifications

To address the problem, the ranges proposed by the potential providers need to be transformed into precise specifications to enable comparisons. To do so, the following steps need to be taken.

## 4.1.1. Obtaining client estimates for specification ranges

The proposed ranges need to be accompanied by estimates from the client or a group of subject-matter experts who have experience working with the provider (or are familiar with the providers' quality of work) and can anticipate the provider's overall capability to deliver the proposed project scope. We recommend the client or the domain ex perts provide estimations by relying on the available historical data in relation to how the potential providers handled previous projects. Developing a methodical approach to extract such estimations can be challenging, but in most cases, a straightforward question is suficient to obtain the client's/experts' estimates. For instance, Fig. 3 shows an example of a question which can be used to obtain the client's/experts estimates on a specification for a CNC machine (CNC stands for Computer Numerical Control), this being the travelling capacity of the CNC machine on the X axis (the higher the travelling capacity, the more attractive the CNC machine). These obtained estimates are referred to as the expert's estimates.

## 4.1.2. Graphing client satisfaction

This step is concerned with the development of the client's satisfaction graph. Two key questions, namely the satisfactory bound(s) question and the unacceptable bound(s) question [1] are utilised to graph the client's satisfaction paradigm. Taking again the example of procuring the customised CNC machine, assume that the travelling capacity of the machine on its X axis is a key specification which afects client satisfaction. The first question, shown in Fig. 4, obtains the most satisfactory specifications (specifications which have the attractiveness score of one).

The second question, shown in Fig. 5, obtains the unacceptable specifications of the product (specifications which have the attractiveness score of zero). Depending on the client's answer to the first question, only one option will be active. For example, if the client's answer to the first question is C, the second question appears with option A.

The above two questions are suficient to cover all possible graphs, as shown in Fig. 6.

## 4.1.3. Computing the Centre of gravity for each specification

The specification ranges in the project proposal and the client's estimates can be graphed, as illustrated in Fig. 7. In this figure, the a-d range is taken from the proposal and the narrower b-c range is from the client/expert (in this paper, we assume that only one expert is involved).

The range suggested by the provider (a and d) and the range esti mated by the subject matter expert (b and c) may have diferent weightings based on how certain or confident the expert is about their suggested ranges (the expert may suggest a range and also express that his level of confidence – see Fig. 3). This level of confidence, e.g. 60%, is multiplied by the ranges provided by the expert, and then its complement, e.g. 40%, by the ranges proposed by the provider. As we use fuzzy straight-line graphs in this paper, the centre of gravity is the weighted average of the bounds $( \mathbf { a } , \mathbf { b } , \mathbf { c } ,$ and d). The weighted average of the bounds is computed, and represents the estimated specification of the product to be delivered in the project. As the provider starts delivering the outputs of the project, the specifications of the delivered outputs can be compared with the ranges suggested by the provider and may be used as the basis for giving the provider a bonus to motivate them to deliver specifications which are better than those in the ranges in their proposal. The specifications can also be used to judge the experts' accuracy and fairness in suggesting specification ranges (explained in the Section 5.2). Note that transforming ranges to precise specifications may cause information loss. One may decide to keep the interval throughout the solution. Because this may add to the

## Table 1

Ambiguous proposal evaluation methodology.

<table><tr><td>Phase and step</td><td>Action</td></tr><tr><td>Phase 1 - Transform ranges in proposals to precise specifications</td><td>Ranges for specifications in the providers&#x27; proposals are transformed to precise specifications to enable comparison</td></tr><tr><td>Step 1.1 - Obtain expert estimates for specification ranges</td><td>A question is designed to obtain the expert&#x27;s estimated range for each specification of the final product</td></tr><tr><td>Step 1.2 - Graph the client&#x27;s satisfaction</td><td>Two questions are designed to obtain the client&#x27;s satisfaction bounds based on fuzzy graphs</td></tr><tr><td>Step 1.3 - Compute the centre of gravity of each specification</td><td>Each specification range suggested by providers in their proposals and the respective estimated range from step 1.1 are combined to find a precise number for each specification.</td></tr><tr><td>Step 1.4 - Compute specification attractiveness score</td><td>Values from Step 1.3 are found on the x axis of the client&#x27;s satisfaction graphs. The respective number on the y axis represents the score for that specification attractiveness</td></tr><tr><td>Phase 2 - Integrate multiple specifications into the client satisfaction score</td><td>The weightings of importance for different product specifications are computed using BWM and a client satisfaction score is computed for each proposal</td></tr></table>

![](/api/attachments/Y5A3BGJH/fulltext/images/7d7a6855281d0e0866768d64b7a528a32ee6d12232c0b27f99e5e988b4d98453.jpg)  
Fig. 3. Example of a question to obtain the domain experts' viewpoint.

complexity of the solution, it can only be preferred in cases where keeping the information have future benefits, or where access to the original information may be denied after implementing the solution.

## 4.1.4. Computing specification attractiveness scores

In step 1.3, the centre of gravity for the two specification ranges, one suggested in the proposals and the other one estimated by the ex pert, was computed. This number for each specification is found on the x axis of client's satisfaction graph, which was obtained in step 1.2. Then, the respective number on the y axis of the same graph is identified, which represents the specification attractiveness score. For instance, if the centre of gravity for travelling capacity on X axis of a CNC machine is at 5000, and the client's satisfaction graph determines 3500 as the unacceptable, and 5500 as the most satisfactory specifications of the product, the attractiveness score of this specification is 0.75.

So far, we have explained how attractiveness scores for diferent specification ranges, stated in the providers' proposals, are computed. The next section explains Phase 2, which deals with computing the client satisfaction score for each proposal.

## 4.2. Integrating multiple specifications into the client satisfaction score

Projects have outputs/deliverables with various specifications and these specifications may have diferent weightings of importance from the client's viewpoint. The weightings of importance can be obtained using an MCDM method, such as BWM. Taking into consideration the proposed specifications and the relevant weightings, the suggested scopes in the proposals are compared and the satisfaction score of each proposal is computed. A brief review of BWM is presented as follows. In BWM, firstly, the best and the worst criteria are selected. Then, the other criteria are compared with these two criteria separately. Finally, the values of the alternatives are computed. A summary of the method is as follows (adapted from [32]).

1. Nominate the best and worst criteria of the total of n existing criteria.

2. Estimate the preference of the best criterion over all the other criteria using a 1 to 9 scale (where 1 is the highest preference and 9 is the lowest preference). The results build a vector: $A _ { B } = ( a _ { B 1 } , a _ { B 2 } ,$ $\ldots , a _ { B n } )$ (where $a _ { B j }$ represents the preference of the best criterion B over criterion $j ) .$

3. Estimate the preference of all the criteria over the worst criteria using the same scale. The results form a vector: $A _ { W } = ( a _ { 1 W } , a _ { 2 W } ,$ $\ldots , a _ { n w } )$ (where the preference of criterion j over worst criterion W is

![](/api/attachments/Y5A3BGJH/fulltext/images/3f8a4d000981001e1d26ccdf1bde91f35bb459160f3e5e5a77ef595ae5f7e4dd.jpg)

shown by $a _ { j W } ) .$

4. Calculate the optimal weightings denoted by $w _ { 1 }$ to $w _ { n } .$ . A comparison which results in perfect weightings for the criteria occurs when, for each pair o $\underline { { \cdot w _ { B } } }$ and $\frac { w _ { j } } { w _ { W } } ;$ , where $w _ { B }$ stands for the weighting of the best w<sub>j</sub> criterion and $w _ { W }$ for the worst, the following equations are balanced: $\begin{array} { r } { \frac { w B } { w _ { j } } = a _ { B j } } \end{array}$ and $\frac { w _ { j } } { w _ { W } } = a _ { j W }$ . Note that this is unlikely to occur when the number of criteria is above 4 or 5. The weightings of the criteria can be computed where the maximum absolute diferences and all j are minimised.

$$
\left. \begin{array}{c} \left| \frac {w _ {B}}{w _ {j}} - a _ {B j} \right| \leq \xi , f o r a l l j \\ \left| \frac {w _ {j}}{w _ {W}} - a _ {j W} \right| \leq \xi , f o r a l l j \\ \sum_ {j} w _ {j} = 1 \\ \mathrm{w} _ {j} \geq 0, f o r a l l j \end{array} \right\}\tag{1}
$$

The symbol ξ represents the inconsistency of the comparisons. In cases where it is above the maximum values of ξ (see Table 2), the comparisons are inconsistent and need to be improved.

Applying BWM, the specifications are weighted and then the proposals are ranked. After this, the proposals are compared in terms of the other selection criteria (cost, time, and benefits), which is a simple MCDM problem and any MCDM method can be utilised to find the optimal ranking. In the next section, the method proposed in this paper is numerically illustrated.

## 5. Case study and the discussion of the results

In this section, a procurement process is selected to illustrate the solution. The proposed solution and the results are then discussed.

## 5.1. Case study

We take the example of the Australian Defence Force's procurement of a CNC machine as a case study. Assume that there are three proposals and each provider suggests specifications for the CNC machine, as shown in Table 3.

Phase 1: The first phase of the methodology is illustrated as follows. Step 1.1: Domain experts from the procuring organisation (e.g. experienced engineers or managers who are well familiar with the product) can suggest the ranges of specifications that they believe the

Fig. 4. Example of a satisfactory bound(s) determination question.

![](/api/attachments/Y5A3BGJH/fulltext/images/9fba3777c74112403f5f1ee3aa220cd3af0af551aed4df0f6ff6f50334a8689f.jpg)

providers will ultimately deliver. To suggest ranges, we recommend that the experts do not solely rely on their own intuition as it may be subjected to bias. They are recommended to obtain information about providers performance and capabilities and then then suggest their expected ranges. For instance, they can refer to the specifications of what the providers currently or previously have produced, contact them and obtain more information about their capabilities, and investigate the providers' reputation or their customer satisfaction records. After receiving the ranges suggested by the experts, they can be aggregated using approaches such as weighted average, in which experts may have diferent weightings depending on their experience. In the case dis cussed in this paper, one expert is involved. The expert suggests estimates of 4500 to 5000 for the travelling capacity on the X axis of proposal A's, 3600 to 4000 for proposal B, and 5000 to 5500 of proposal C as presented in the fourth row of Table 4. Similarly, suggested ranges for other specifications of the product are presented in Table 4.

Now there are two ranges for each product feature which represent the bounds (a,b,c,d). Table 5 provides a graphical view of these two sets of ranges. Step 1.2: In answer to the satisfactory bounds question, a team may be involved to decide; a group consisting from key stakeholders from senior decision makers to engineers, and operators who would ultimately be using the machines. The team is asked the satisfactory and unacceptable bounds questions (Figs. 5 and 6) for each specification of the product. For the first question regarding the travelling capacity on the X axis, the team choses ‘Above’ and then states 5000. The team is then asked the second question which has the active option of ‘Below’ and they state 3500, as shown in Fig. 2. This is repeated for all specifications to obtain the client's satisfaction graphs (last column of Table 5).

Note that the choice of fuzzy straight-line graphs in this paper (see Table 5) is to avoid complexity and to keep the proposed solution easier

Fig. 5. Example of an unacceptable bound(s) determination question.

to understand for a wider range of audience. More complex graphs, e.g. Gaussian, can be used in future applications where reasonable justification for using more complex graphs can be made. Step 1.3: For each graph, the centre of gravity on the x axis needs to be computed. As we used straight-line fuzzy graphs, this means computing a simple weighted average of the bounds of the ranges. In this case, we assume that the expert suggests 75% confidence in their estimates for provider A's and B's proposals, and 90% confidence in their estimates for provider C's proposal. So, for provider A and B, the weight of 75% is given to the estimates by the expert, and 25% to the ranges suggested by the providers (and 90% and 10% to the expert's estimates and provider C's proposal, respectively). The estimated specifications are computed as shown in the second, fourth, and sixth columns of Table 6. Step 1.4: For each specification of the product in each proposal, the centre of gravity was computed in Step 1.3. Each of these numbers needs to be found on the x axis of the client's satisfaction graph, and the respective number on the y axis will represent the client's satisfaction score for that specification of the proposal, or its attractiveness, as shown in the third, fifth, and seventh columns of Table 6. For the sake of brevity, the following abbreviations are used for the specifications: standard workable area (SWA), positioning accuracy (PA), travelling capacity of X axis (TCX), travelling capacity of Y axis (TCY), travelling capacity of Z axis (TCZ), spindle speed (SS), fast feed Y-Z (FFY/Z), and fast feed X axis (FFX).

Phase 2: Diferent specifications have diferent weightings of importance. In this phase, an MCDM method can be applied obtain these weightings and find the most appealing proposal. BWM is applied in this phase to compute the weightings of the specifications. The results are presented in Table 7.

The specification attractiveness scores presented in Table 6, are normalised and then multiplied by the weightings of the specifications,

![](/api/attachments/Y5A3BGJH/fulltext/images/e7990db97603986ce8bf81897fef39075a474fabb82ce1e1209298b2a4524ef2.jpg)  
Fig. 6. Examples of possible graphs from the satisfactory and unacceptable bound(s) questions.

![](/api/attachments/Y5A3BGJH/fulltext/images/91537a2d62c5fb52b395d969f9175aadeffe94a6d67f2f5957adbd6aee7e3ce3.jpg)  
Fig. 7. Fuzzy graphs for the specification ranges.

Table 2  
Consistency Index (CI) [39].

<table><tr><td>Order of matrix</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>Consistency Index (CI) (Max  $\xi$ )</td><td>0.00</td><td>0.44</td><td>1.00</td><td>1.63</td><td>2.30</td><td>3.00</td><td>3.73</td><td>4.47</td><td>5.23</td></tr></table>

presented in Table 7.

V<sub>Proposals</sub>=

$$
\begin{array}{c} S W A \\ \text {SWA PA TCX TCY TCZ SS FFY - Z FFX} \\ \left[ \begin{array}{l l l l l l l l} 0. 5 3 4 & 0. 7 4 7 & 0. 4 0 7 & 0. 4 1 7 & 0. 4 2 5 & 0. 2 9 0 & 0. 1 6 2 & 0. 0 9 3 \\ 0. 0 8 6 & 0. 2 3 0 & 0. 1 2 8 & 0. 2 7 0 & 0. 2 3 4 & 0. 4 1 5 & 0. 5 3 2 & 0. 4 6 6 \\ 0. 3 8 0 & 0. 0 2 3 & 0. 4 6 5 & 0. 3 1 3 & 0. 3 4 0 & 0. 2 9 5 & 0. 3 0 6 & 0. 4 4 1 \end{array} \right] \times \begin{array}{c} S W A \\ P A \\ T C X \\ T C Y \\ T C Z \\ S S \\ F F Y / Z \\ F F X \end{array} \left[ \begin{array}{l} 0. 1 6 4 \\ 0. 0 5 9 \\ 0. 1 1 2 \\ 0. 0 5 9 \\ 0. 0 5 6 \\ 0. 2 2 4 \\ 0. 1 6 4 \\ 0. 1 6 4 \end{array} \right] \\ = \begin{array}{c} P r o p o s a l A ^ {\prime} s s c o p e \\ = P r o p o s a l B ^ {\prime} s s c o p e \\ P r o p o s a l C ^ {\prime} s s c o p e \end{array} \left[ \begin{array}{l} 0. 3 3 2 \\ 0. 3 2 8 \\ 0. 3 4 2 \end{array} \right] \end{array} \tag {2}
$$

The results show that proposal C is the preferred option with respect to the suggested specifications (i.e. anticipated quality) with the highest weighting of 0.342. To analyse the sensitivity of the proposed solution, the results were examined under four different scenarios. In each of the scenarios, we changed values of key parameters in the model and analysed the impact of such changes on the preferred option. First, we assumed that providers increase the ambiguity of the specifications of the aforementioned three proposals by 20% (10% from each side). Results, presented in the first column of Eq. (3), show that proposal C is still the preferred option. The second column in Eq. 3 assumes 40% increase in the providers' suggested ambiguity, resulted in proposal A being preferred. The indiference point, at which proposal A and C are equally preferred was found to be at 38% increased ambiguity by providers, under which the weightings of the proposals are as presented in the third column of the equation. Second, we assumed that the am biguity of proposal C remains the same while provider A and B increase the ambiguity of their proposals for 20%. We see that the solution remains robust and recommends provider C, as presented in the fourth column of Eq. 3. Then, we assume that providers A and B increase the ambiguity in their proposals for 40%, while proposal C remains the same. The results in the fifth column shows that the solution still re commends provider C. Third, we assumed that provider A and B keep their lower bounds and try to deceive the client by solely increasing their upper bounds for 10% (see the sixth column). Although borderlined, the recommended proposal remains the same. However, if they increase this from 10% to 12%, provider A is recommended. Fourth, we analysed the sensitivity to changes in expert inputs on the proposals, measured by the suggested intervals. The sevenths and eighths columns of the matrix show the result for 10% and 20% increase in expert's suggested intervals. Whereas for 10% increase, proposal C is still recommended, for 20%, proposal A is preferred. This higher sensitivity to expert opinions is due to the confidence level that the expert had when suggesting the intervals in the case study (75% for proposal A and B, and 90% for proposal C). Looking at the results, while the proposed solution is relatively robust, we believe that proposals that are too ambiguous need to be either removed from evaluation, or the providers need to be required to revise their proposals. As a general rule, to have more reliable results, where possible, the providers need to be asked to decrease the level of the involved ambiguity in their proposals before we use the proposed solution to deal with the remained ambiguity.

$$
\left[ \begin{array}{c c c c c c c c} 0. 3 3 7 & 0. 3 4 2 & 0. 3 4 1 & 0. 3 3 6 & 0. 3 4 0 & 0. 3 3 8 & 0. 3 3 9 & 0. 3 4 7 \\ 0. 3 2 4 & 0. 3 2 0 & 0. 3 2 1 & 0. 3 2 4 & 0. 3 1 9 & 0. 3 2 5 & 0. 3 2 2 & 0. 3 1 4 \\ 0. 3 4 1 & 0. 3 4 1 & 0. 3 4 1 & 0. 3 4 2 & 0. 3 4 2 & 0. 3 3 9 & 0. 3 4 1 & 0. 3 5 1 \end{array} \right]\tag{3}
$$

As previously discussed, proposal selection is a multi-criteria decision-making problem and there are other criteria in addition to the scopes of the proposals, such as time, cost, and benefits, to be considered. This can be the next step and can again be performed using any MCDM method, which is excluded from this paper.

## 5.2. Discussion

This paper tackled this problem showed how can ambiguous proposals be compared and how can a project which outperforms the others be identified. As illustrated in the previous section, the model, first transforms the specification ranges into precise specifications. Next, the client's satisfaction paradigm is obtained by asking straightforward questions (presented in Figs. 5 and 6). Using both measures and considering how important each specification is to the client, the client's satisfaction level with the proposed scope is computed. Finally, the proposals can be compared with regard to other project criteria to select the proposal which achieves the highest client satisfaction.

Without the proposed approach presented in this paper, when a client receives ambiguous proposals, the proposal selection becomes a challenging problem. For instance, in the procurement process of the CNC machine, assume that the three proposals are the same with regard to all specifications except from Travelling capacity on Y axis (see the fifth row of Table 3). Therefore, there are three proposals and only one criterion to evaluate and select one. Even with only a single criterion, to identify the best proposal several scenarios may come to execution. First scenario: the client may be pessimistic with regard to all proposals and refer to the lower bounds of the suggested intervals and makes the decision, i.e. 550, 550, and 600 (for proposal A, B, and C respectively), which this results in selecting proposal C. Second scenario (which is mostly the case in government projects): the client may be optimistic, hoping for the upside of ambiguity [16], and refer to the upper bounds of the suggested intervals to decide, i.e. 850, 750, and 650, which this results in selecting proposal A. Third scenario: the client may decide to take the average of suggested intervals and therefore selects proposal A. Other scenarios: the client may have unethical reasons to act with bias and be optimistic for some proposals, and pessimistic for others, which create several scenarios, in each of which the decision may difer. While the case, even when one criterion is to decide, can be quite challenging, this paper suggested the involvement of subject matter experts as well as a team from the client organisation and submits a methodological approach to facilitate this multiple criteria decision making process.

Table 3  
Ranges suggested by the providers.

<table><tr><td>Specifications</td><td>Proposal A</td><td>Proposal B</td><td>Proposal C</td></tr><tr><td>Standard workable area (mm)</td><td>4500-5500</td><td>3500-4500</td><td>4500-4700</td></tr><tr><td>Positioning range (mm)</td><td>± 0.04</td><td>± 0.07</td><td>± 0.07</td></tr><tr><td>Travelling capacity X axis (mm)</td><td>4500-5500</td><td>3500-5000</td><td>5000-6000</td></tr><tr><td>Travelling capacity Y axis (mm)</td><td>550-850</td><td>550-750</td><td>600-650</td></tr><tr><td>Travelling capacity Z axis (mm)</td><td>400-450</td><td>350-400</td><td>380-450</td></tr><tr><td>Spindle speed (rpm)</td><td>25,000-30,000</td><td>28,000-31,000</td><td>25,000-28,000</td></tr><tr><td>Fast feed Y- Z (m/min)</td><td>50-70</td><td>60-80</td><td>55-75</td></tr><tr><td>Fast feed X axis (m/min)</td><td>70-90</td><td>80-95</td><td>80-90</td></tr></table>

Table 4  
Specification ranges suggested by the expert.

<table><tr><td>Specifications</td><td>Proposal A</td><td>Proposal B</td><td>Proposal C</td></tr><tr><td>Standard workable area (mm)</td><td>4750-5200</td><td>3500-3800</td><td>4500-4600</td></tr><tr><td>Positioning accuracy (mm)</td><td>± 0.05</td><td>± 0.07</td><td>± 0.08</td></tr><tr><td>Travelling capacity X axis (mm)</td><td>4500-5000</td><td>3600-4000</td><td>5000-5500</td></tr><tr><td>Travelling capacity Y axis (mm)</td><td>600-800</td><td>550-600</td><td>600-650</td></tr><tr><td>Travelling capacity Z axis (mm)</td><td>400-425</td><td>350-370</td><td>380-400</td></tr><tr><td>Spindle speed (rpm)</td><td>25,000-27,000</td><td>28,000-30,000</td><td>25,000-28,000</td></tr><tr><td>Fast feed Y - Z (m/min)</td><td>50-55</td><td>60-65</td><td>55-60</td></tr><tr><td>Fast feed X axis (m/min)</td><td>60-70</td><td>80-85</td><td>80-85</td></tr></table>

The methodology utilised two straightforward approaches to address this complicated real-world problem, fuzzy logic and BWM. Fuzzy logic was utilised to resolve the uncertainty related the specifications of the product as well as graphing the client's satisfaction paradigm. Fuzzy logic is one of several available formalisms in the literature that have been proposed to tackle uncertainty: non-monotonic reasoning [30], possibilistic logic [11], Dempster Shafer theory [42], and probability theory [37] among others [20]. This study utilised fuzzy graphs because they were capable of handling the aforementioned uncertainty, and also because they are fairly straightforward, and this facilitates future applications of the proposed approach in practice. BWM is used in this study to rank the importance of specifications from the client's organisation's perspective. BWM is a recently proposed MCDM method. In comparison with other methods such as AHP and ANP, it has a lower inconsistency and a reduced number of required pairwise comparisons [39]. Moreover, in the case of project proposal evaluation, the application of BWM can be quite straightforward as the decision maker usually knows clearly that from the client organisation viewpoint which two specifications of the product are the most and least important ones (a prerequisite key step which facilitates application of BWM method). This enables computing the weightings for the other specifications of the product with respect to the most and least important specifications.

Rather than purely relying on historical data, we ask domain experts to provide estimations of the value for two reasons. First, in complex situations decision makers prefer to rely on the knowledge and experience rather than solely follow an automated decision-making tool [10]. Secondly, in many complex projects we do not have reliable historical data, because they are limited, dated or are not fully relevant to the project in hand (as each project is diferent). For instance, in the project of procuring customised submarines, experts would be more reliable to see whether the company is capable of delivering the spe cifications that they claim rather than purely referring to historical data. Note that experts usually consider the track record of the company, or find reliable and justifiable sources of information, when they provide their opinions.

This study opens areas for future studies with regard to both the discussed problem and the proposed solution. We believe that various perspectives on ambiguous proposal evaluation can be suggested in future research, only some of which were discussed in this paper (see Section 3). In particular, a game-based modelling of the problem would be very useful to explain the complexities of the strategies used by the provider and client within the proposal evaluation process. In the solution part, there are many tools and techniques from diferent disciplines that can be utilised to empower and strengthen the proposed model. For instance, the solution does not consider that clients themselves may be ambiguity avid and suggest optimistic estimates. To resolve this, the opinions of a group of domain experts can be used. In doing so, the utilisation of crowdsourcing techniques in the process of shrinking the ranges can be quite useful. In such cases, the experts can be asked other questions, for example, about their experience working with the specific provider for whose proposal they are suggesting ranges. Such questions will guide clients to realise how well each expert knows the provider whose proposal is being judged. This can be considered as a variable contributing to assigning the weighting that should be given to each expert's viewpoint. Moreover, the concept of fairness in crowdsourcing [12] can be utilised to monitor the experts opinions. At the end of the project, the specifications of the delivered project outputs can be compared with the experts' ranges (suggested in the proposal selection process). As a result, experts can receive weightings for the accuracy of their estimations, which may be considered when they make future suggestions (alongside their claimed level of confidence).

## 6. Conclusions

Project proposal evaluation becomes a more complex challenge for decision makers when the proposals received from potential providers are ambiguous. For the reasons explained in this paper, providers have a strong motivation to include ambiguity in their proposals and the client also has suficient incentives to tolerate this ambiguity. Therefore, the existence of ambiguity in providers' proposals is common in real projects and hence, the proposal selection decision often has to be made under ambiguity. However, the literature has not yet discussed this real-world problem which we call the “ambiguous proposal evaluation” problem.

This study has shed light on the scientific and practical significance of this problem and has developed a solution to show how ambiguous proposals can be evaluated and ranked efectively. The paper specifically focused on the research question of how ambiguous proposals can be compared. The paper contributes to the literature by defining this unique problem, which is common in practice but has no methodological solution in the existing research. Moreover, to address the problem, a solution was developed which methodologically contributes to MCDM approaches by having ambiguous options to compare. More significant is the practical contribution of this paper. Fundamentally, the study was conducted to provide a possible solution to the aforementioned real-world problem.

The paper also opens multiple areas for future studies. By defining this problem in the literature, this paper is expected to stimulate future research studies to discover and discuss various possible scenarios and aspects of the problem, which may or may not be easily observable in practice. The solution suggested in this paper is just one possible solution to the ambiguous proposal selection problem. Future studies can either improve the solution proposed in this paper or provide alternative solutions using tools and techniques from crowdsourcing, MCDM, and soft computing, among others.

Table 5  
![](/api/attachments/Y5A3BGJH/fulltext/images/6cca19b7e879337e1c7dd5fc0104ff04b4b4e2cd3b6e90cb4c510b895241a49a.jpg)

Graphical representation of the specification ranges.

<table><tr><td></td><td>Proposal A</td><td>Proposal B</td><td>Proposal C</td><td>Client&#x27;s satisfaction graph</td></tr><tr><td>Standard workable area</td><td>f(x)104750 5000 5200 5500</td><td>f(x)103500 3800 4500</td><td>f(x)104500 4600 4700</td><td><img src="/api/attachments/Y5A3BGJH/fulltext/images/b9ca8a429ce6c3e2b6d8b0fb50c02342146cf5fd938be50d4324467e2793db28.jpg"/></td></tr><tr><td>Positioning accuracy</td><td><img src="/api/attachments/Y5A3BGJH/fulltext/images/b529e254d77dcdc76579a13bcd29737cb3e7fdc22bc32cb43017c81d7ac93087.jpg"/></td><td><img src="/api/attachments/Y5A3BGJH/fulltext/images/8eb4935451b7a35bd49a972ff298aa85a799b99e0d6a3d5b880cfa00efc4080e.jpg"/></td><td><img src="/api/attachments/Y5A3BGJH/fulltext/images/d5964fad8b3131d8b6d8d3529afea1e00240aac2bc65be256204bbf0e5b8e53e.jpg"/></td><td><img src="/api/attachments/Y5A3BGJH/fulltext/images/acbd8d4f74a8022d17c74e784d8c24c1ea72202f48c7a8ee3a3395c19aa46130.jpg"/></td></tr><tr><td>Travelling capacity X axis</td><td>f(x)104500 5000 5500</td><td>f(x)103500 3600 4000 5000</td><td>f(x)105000 5500 6000</td><td><img src="/api/attachments/Y5A3BGJH/fulltext/images/be893ccb7d201bec8c2b7b222f00923c4ce6bb09393ea3cd34185858f382c14f.jpg"/></td></tr><tr><td>Travelling capacity Y axis</td><td>f(x)10550 600 800 850</td><td>f(x)10550 600 750</td><td>f(x)10600 650</td><td><img src="/api/attachments/Y5A3BGJH/fulltext/images/4942d2be3f31b980b1325d18d68c532983b5da3f52ccbb74b7fd62db99016c52.jpg"/></td></tr><tr><td>Travelling capacity Z axis</td><td>f(x)10400 425 450</td><td>f(x)10350 370 400</td><td>f(x)10380 400 450</td><td><img src="/api/attachments/Y5A3BGJH/fulltext/images/b6112fecdfb595733f089c9ea80ac4c847d82a5a94970dfd63261e77ed4ce677.jpg"/></td></tr><tr><td>Spindle speed</td><td>f(x)1025000 27000 30000</td><td>f(x)1028000 30000 31000</td><td>f(x)1025000 28000</td><td><img src="/api/attachments/Y5A3BGJH/fulltext/images/20de69b3a33007415b0fd59b762fef2e582a9a29871ddaa506c23c0dacdbea06.jpg"/></td></tr><tr><td>Fast feed Y - Z</td><td>f(x)1050 55 70</td><td>f(x)1060 65 80</td><td>f(x)1055 60 75</td><td>f(x)1050 75</td></tr><tr><td>Fast feed X axis</td><td>f(x)1060 70 90</td><td>f(x)1080 85 95</td><td>f(x)1080 85 90</td><td>f(x)1065 85</td></tr></table>

![](/api/attachments/Y5A3BGJH/fulltext/images/549dff540c226b69898cd18ba22c0457f9efd1d486beaf20ef8d78b49e49ed45.jpg)

![](/api/attachments/Y5A3BGJH/fulltext/images/e01a0e73e4ce2ee976bcea4b61cbaa3d5cf7e8ea0c577a84e449fed9f44d079a.jpg)

Table 6  
The attractiveness of the specifications of the providers' proposals.

<table><tr><td></td><td>Proposal A</td><td>Attractiveness (Proposal A)</td><td>Proposal B</td><td>Attractiveness (Proposal B)</td><td>Proposal C</td><td>Attractiveness (Proposal C)</td></tr><tr><td>SWA</td><td>4981.25</td><td>0.741</td><td>3737.50</td><td>0.119</td><td>4555</td><td>0.528</td></tr><tr><td>PA</td><td>0.0475</td><td>0.313</td><td>0.070</td><td>0.000</td><td>0.079</td><td>0.000</td></tr><tr><td>TCX</td><td>4812.50</td><td>0.875</td><td>3912.50</td><td>0.275</td><td>5275</td><td>1.000</td></tr><tr><td>TCY</td><td>700</td><td>1.000</td><td>593.75</td><td>0.646</td><td>625</td><td>0.750</td></tr><tr><td>TCZ</td><td>415.63</td><td>0.578</td><td>363.75</td><td>0.319</td><td>392.5</td><td>0.463</td></tr><tr><td>SS</td><td>26,375</td><td>0.638</td><td>29,125</td><td>0.913</td><td>26,500</td><td>0.650</td></tr><tr><td>FFY/Z</td><td>54.375</td><td>0.175</td><td>64.375</td><td>0.575</td><td>58.25</td><td>0.330</td></tr><tr><td>FFX</td><td>67.50</td><td>0.188</td><td>83.75</td><td>0.938</td><td>82.75</td><td>0.888</td></tr></table>

Table 7  
The weightings of the specifications using BWM.

<table><tr><td></td><td>SS</td><td>SWA</td><td>FFY/Z</td><td>FFX</td><td>TCX</td><td>TCY</td><td>PA</td><td>TCZ</td></tr><tr><td>Best (SS)</td><td>1</td><td>1.5</td><td>1.5</td><td>1.5</td><td>2</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Worst (TCZ)</td><td>4</td><td>3.2</td><td>3.2</td><td>3.2</td><td>2</td><td>1.1</td><td>1.1</td><td>1</td></tr><tr><td>Optimal Weightings CI ( $\xi$ ) = 0.033</td><td>0.224</td><td>0.164</td><td>0.164</td><td>0.164</td><td>0.112</td><td>0.059</td><td>0.059</td><td>0.056</td></tr></table>

## Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## Credit Author Statement

This manuscript has only two authors. We state that the first author had the main responsibility to develop the paper. The second author contributed in many forms from conceptualisation to writing and revising the paper.

## Declaration of Competing Interest

## None.

## References

[1] M.R. Asadabadi, E. Chang, O. Zwikael, M. Saberi, K. Sharpe, Hidden Fuzzy Information: Requirement Specification and Measurement of Project Provider Performance Using the Best Worst Method, (2019), https://doi.org/10.1016/j.fss. 2019.06.017.

[2] M.R. Asadabadi, K. Sharpe, The ambiguity dilemma in procurement projects, J. Bus. Ind. Mark, 34 (4) (2019) 792–800. https://doi,org/10.1108/JBIM-05-2018-0157.

[3] R. Atkinson. L. Crawford. S. Ward. Fundamental uncertainties in proiects and the scope of proiect management. Int. J. Proi, Manag, 24 (8) (2006) 687–698, https:/ doi.org/10.1016/i.iiproman.2006.09.011

[4] Australian-National-Audit-Ofice, Department of Defence. New Submarine Project, Retrieyed from, 1997. https://www.anao.goy.au/work/performance-audit/new submarine-project.

[5] T.J. Bang, An agile approach to requirement specification. Paper presented at the International Conference on Extreme Programming and Agile Processes in Software Engineering, (2007), https://doi.org/10.1007/978-3-540-73101-6\_35.

[6] A. Bonetti, S. Bortot, M. Fedrizzi, R.M. Pereira, A. Molinari, Modelling group processes and effort estimation in project management using the Choquet integral: an MCDM approach, Expert Syst. Appl. 39 (18) (2012) 13366–13375, https://doi.org 10.1016/i,eswa.2012.05.066

[7] J. Burgelman, M. Vanhoucke, Project schedule performance under general mode implementation disruptions, Eur. J. Oper. Res. 280 (1) (2020) 295–311, https://doi. org/10.1016/i,eior,2019.06.050.

[8] H.K. Chan, X. Sun, S.-H. Chung, When should fuzzy analytic hierarchy process be used instead of analytic hierarchy process? Decis. Support. Syst. 125 (2019) 113114, , https://doi.org/10.1016/j.dss.2019.113114.

[9] M. Chica, Ó. Cordón, S. Damas, V. Iglesias, J. Mingot, Identimod: Modeling and managing brand value using soft computing, Decis. Support. Syst. 89 (2016) 41–55, https://doi.org/10.1016/i.dss.2016.06.007.

[10] L. Diaz-Balteiro, J. González-Pachón, C. Romero, Measuring systems sustainability with multi-criteria methods: a critical review. Eur. J. Oper. Res. 258 (2) (2017 607–616. https://doi.org/10.1016/i.eior,2016.08.075.

[11] Dubois, D., Lang, J., & Prade, H. (1994). Possibilistic logic 1.

[12] R. Faullant, J. Füller, K. Hutter, Fair play: perceived fairness in crowdsourcing

competitions and the customer relationship-related consequences, Manag. Decis. 55 (9) (2017) 1924–1941, https://doi.org/10.1108/MD-02-2017-0116.

[13] H. Femmer, D.M. Fernández, E. Juergens, M. Klose, I. Zimmer, J. Zimmer, Rapid requirements checks with requirements smells: Two case studies, Paper Presented at the Proceedings of the 1st International Workshop on Rapid Continuous Software Engineering. 2014. https://doi,org/10.1145/2593812.2593817

[14] H. Femmer, D.M. Fernández, S. Wagner, S. Eder, Rapid quality assurance with re quirements smells, J. Syst. Softw. 123 (2017) 190–213, https://doi.org/10.1016/j. jss.2016.02.047.

[15] P. Fiala, Project portfolio designing using data envelopment analysis and De novo optimisation, CEJOR 26 (4) (2018) 847–859, https://doi.org/10.1007/s10100-018- 0571-6.

[16] B. Flyvbjerg, Optimism and misrepresentation in early project development, Making Essential Choices with Scant Information, Springer, 2009, pp. 147–168, , https://doi.org/10.1057/9780230236837 8.

[17] N. Fugger, E. Katok, A. Wambach, Trust in procurement interactions, Manag. Sci. 65 (11) (2019).5110–5127, https://doi org/10.1287/mnsc 2018.3196

[18] Y. Guo, L. Wang, S. Li, Z. Chen, Y. Cheng, Balancing strategic contributions and financial returns: a project portfolio selection model under uncertainty. Soft Comput. 22 (16) (2018) 5547–5559, https://doi.org/10.1007/s00500-018-3294-7.

[19] T. Hollingsbee, France wins AUSTRALIAN submarine replacement competition, Ausmarine 38 (8) (2016) 17

[20] D.E. Holmes, Innovations in Bayesian Networks: Theory and Applications, Vol. 156 Springer, 2008.

[21] H. Jafarzadeh, P. Akbari, B. Abedin, A methodology for project portfolio selection under criteria prioritisation, uncertainty and projects interdependency–combination of fuzzy QFD and DEA, Expert Syst. Appl. 110 (2018) 237–249, https://doi. org/10.1016/j.eswa.2018.05.028.

[22] S. Jayatilleke, R. Lai, A systematic review of requirements change management, Inf. Softw. Technol. 93 (2018) 163–185, https://doi.org/10.1016/j.infsof.2017.09.004.

[23] D.J.-F. Jeng, K.-H. Huang, Strategic project portfolio selection for national research institutes, J. Bus. Res. 68 (11) (2015) 2305–2311, https://doi.org/10.1016/j. ibusres.2015.06.016.

[24] K.F. Joiner, S. Reay Atkinson, Australia’s future submarine: shaping early adaptive designs through test and evaluation, Austr. J. Multi-Discipl. Eng. 12 (1) (2016) 3–26. https://doi.org/10.1080/14488388.2016.1238025

[25] E. Karasakal, P. Aker, A multicriteria sorting approach based on data envelopment analysis for R&D project selection problem, Omega 73 (2017) 79–92, https://doi. org/10.1016/i.omega.2016.12.006.

[26] S. Kheybari, M. Kazemi, J. Rezaei, Bioethanol facility location selection using bestworst method, Appl. Energy 242 (2019) 612–623, https://doi.org/10.1016/j. apenergy.2019.03.054.

[27] P.K. Kwok, H.Y. Lau, Hotel selection using a modified TOPSIS-based decision support algorithm, Decis. Support. Syst. 120 (2019) 95–105, https://doi.org/10.1016/ j.dss.2019.02.004.

[28] S. Mallek, N. Daclin, V. Chapurlat, The application of interoperability requirement specification and verification to collaborative processes in industry, Comput. Ind 63 (7) (2012) 643–658, https://doi.org/10.1016/j.compind.2012.03.002.

[29] G. Mavrotas, J.R. Figueira, E. Siskos, Robustness analysis methodology for multiobiective combinatorial optimization problems and application to proiect selection Omega 52 (2015) 142–155, https://doi.org/10.1016/i.omega.2014.11.005.

[30],J McCarthy, Circumscription—a form of non-monotonic reasoning, Artif Intell. 13 (1–2) (1980) 27–39, https://doi.org/10.1016/0004-3702(80)90011-9.

[31] L. Melander, N. Lakemond, Governance of supplier collaboration in technologically uncertain NPD projects, Ind. Mark. Manag. 49 (2015) 116–127, https://doi.org/10. 1016/i indmarman 2015.04.006

[32] F. Nawaz, M.R. Asadabadi, N.K. Janjua, O.K. Hussain, E. Chang, M. Saberi, An

MCDM method for cloud service selection using a Markov chain and the best-worst method, Knowl.-Based Syst. 159 (2018) 120–131, https://doi.org/10.1016/j. knosys.2018.06.010

[33] R.L. Nydick, R.P. Hill, Using the analytic hierarchy process to structure the supplier selection procedure, Int. J. Purch. Mater. Manag. 28 (2) (1992) 31–36, https://doi. org/10.1111/j.1745-493X.1992.tb00561.x.

[34] D. Parker, K. Hartley, Transaction costs, relational contracting and public private partnerships: a case study of UK defence, J. Purch. Supply Manag. 9 (3) (2003) 97–108, https://doi.org/10.1016/S0969-7012(02)00035-7.

[35] F. Perez, T. Gomez, Multiobjective project portfolio selection with fuzzy constraints, Ann. Oper. Res. 245 (1–2) (2016) 7–29, https://doi.org/10.1007/s10479-014- 1556-z.

[36] D. Pramanik, S.C. Mondal, A. Haldar, A framework for managing uncertainty in information system project selection: an intelligent fuzzy approach, Int J. Manag.Sci. and Eng. Manag. (2019), https://doi.org/10.1080/17509653.2019. 1604191.

[37] Y. Prokhorov, Convergence of random processes and limit theorems in probability theory, Theory of Probability and Its Applications 1 (2) (1956) 157–214, https:// doi.org/10.1137/1101016.

[38] A. Rashid, D. Meder, J. Wiesenberger, A. Behm, Visual requirement specification in end-user participation. Paper Presented at the Multimedia Requirements Engineering, 2006. MERE’06. First International Workshop on, (2006), https://doi. org/10.1109/MERE.2006.7.

[39] J. Rezaei, Best-worst multi-criteria decision-making method, Omega 53 (2015) 49–57.

[40] B. Sam, Australia’s Submarine Decision: A Matter of Grand Strategy, (2016), https://doi.org/10.1016/i.omega.2014.11.009

[41] S. Schaefer, L. Cruz-Reyes, Static R&D project portfolio selection in public organizations, Decis. Support. Syst. 84 (2016) 53–63, https://doi.org/10.1016/j.dss. 2016.01.006.

[42] G. Shafer, Dempster-Shafer theory, Encyclopedia of artificial intelligence 1 (1992) 330–331.

[43] I. Vilpola, I. Kouri, Improving ERP Requirement Specification Process of SMEs with a Customer-Centered Analysis Method. Frontier of e-Business Research (FeBR), (2005), pp. 140–151.

[44] P. Yule, D. Woolner, The Collins Class Submarine Story: Steel, Spies and Spin, Cambridge University Press, 2008.

[45] X. Zhang, L. Fang, K.W. Hipel, S. Ding, Y. Tan, A hybrid project portfolio selection procedure with historical performance consideration, Expert Syst. Appl. (2019)

113003, , https://doi.org/10.1016/j.eswa.2019.113003

[46] X. Zhou, L. Wang, H. Liao, S. Wang, B. Lev, H. Fujita, A prospect theory-based group decision approach considering consensus for portfolio selection with hesitant fuzzy information, Knowl.-Based Syst. 168 (2019) 28–38, https://doi.org/10.1016/j. knosys.2018.12.029

[47] Y. Zuo, A framework of survivability requirement specification for critical information systems. Paper Presented at the System Sciences (HICSS), 2010 43rd Hawaii International Conference on, (2010), https://doi.org/10.1109/HICSS.2010.13.

Mehdi Rajabi Asadabadi is a research fellow at College of Business and Economics at Australian National University. He obtained a PhD in Business and Economics with 12 published journal papers during the three years of his PhD study (including journals such as European Journal of Operational Research, Knowledge Based Systems, Expert Systems with Applications, Business and Industrial Marketing, and Fuzzy Sets and Systems). He has presented at well-reputed international conferences, such as IJCAI, INFORMS, Web Intelligence, and IEEE FUZZ.

Link to Google Scholar Profile:

https://scholar.google.com/citations?hl=en&user=cfvObMkAAAAJ&view\_op=list\_ works&sortby=pubdate

Ofer Zwikael is a Professor in the College of Business and Economics at the Australian National University. His research focuses on project benefits management. Professor Zwikael is the author of four books and more than 200 scholarly peer-reviewed papers published in leading outlets, such as the Journal of Operations Management (FT50). He currently an Associate Editor for the International Journal of Project Management.

Link to Google Scholar Profile:

https://scholar.google.com/citations?hl=en&user=ibv57MwAAAAJ&view\_op=list\_ works&sortby = pubdate
