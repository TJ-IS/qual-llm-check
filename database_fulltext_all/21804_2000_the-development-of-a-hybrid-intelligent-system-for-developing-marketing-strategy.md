---
otero_id: 21804
otero_key: "NY5SUEBR"
title: "The development of a hybrid intelligent system for developing marketing strategy"
authors: "Shuliang Li"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00061-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The development of a hybrid intelligent system for developing marketing strategy

Shuliang Li )

Gloucestershire Business School, Cheltenham and Gloucester College of Higher Education, P.O. Box 220, The Park, Cheltenham, Gloucestershire GL50 2QF, England, UK

Accepted 27 October 1999

## Abstract

In this paper, the development of a hybrid intelligent system for developing marketing strategy is described. The hybrid system has been developed to: provide a logical process for strategic analysis; support group assessment of strategic marketing factors; help the coupling of strategic analysis with managerial intuition and judgement; help managers deal with uncertainty and fuzziness; and produce intelligent advice on setting marketing strategy. In this system, the strengths of expert systems, fuzzy logic and artificial neural networks ANNs are combined to support the process of marketing strategy Ž . development. Moreover, the advantages of Porter’s five forces model and the directional policy matrices DPM are alsoŽ . integrated to assist strategic analysis. In the paper, the software architecture of the hybrid system is discussed in details. Particularly, the group assessment support module, the fuzzification of strategic factors, and the fuzzy reasoning for setting marketing strategy are addressed. In addition, the empirical field work on evaluating the hybrid system is also summarised. The empirical evidence indicates that the hybrid intelligent system is helpful and useful in supporting the development of marketing strategy. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Marketing strategy development; Hybrid intelligent systems; Decision support systems; Expert systems; Fuzzy logic; Artificia neural networks

## 1. Introduction

Marketing strategy is the means by which the marketing objectives will be achieved 40 . In recent<sup>w</sup> <sup>x</sup> years, the use of computer-based information systems in the field of strategic marketing has been increasingly highlighted. Researchers have attempted at developing effective information systems in support of marketing strategy development. Decision support systems DSSs have been developed to Ž . support strategic marketing decisions e.g., Ž <sup>w</sup> <sup>x</sup> 6,35,37,64,66,67 . Pioneering research has been . conducted to apply expert systems in strategic marketing planning 3,7,12–14,34,38,41,42,44,62–64 . <sup>w</sup> <sup>x</sup> Fuzzy logic has been used to model market entry decisions 27 . Pioneering work has also been under-<sup>w</sup> <sup>x</sup> taken by Carlsson 11 to combine fuzzy logic and <sup>w</sup> <sup>x</sup> hyperknowledge in support of effective strategy formation. A support system for strategic management, called Woodstrat <sup>w</sup> <sup>x</sup> 14 , has been implemented successfully in Finnish forest and wood industries. Carlsson’s work 11,14 on developing the hyper-<sup>w</sup> <sup>x</sup> knowledge system was based upon the idea and theory of creating hyperknowledge environments coined by Chang et al. 68,69 . Recently, artificial<sup>w</sup> <sup>x</sup> neural networks ANNs have also been harnessed toŽ . aid the process of strategic marketing decisions <sup>w</sup> <sup>x</sup> 22,26,52,58 . More recently, efforts have been made to build hybrid systems to assist marketing strategy formulation 11,18,70 . Researchers have also devel- <sup>w</sup> <sup>x</sup> oped a hybrid artificial intelligence approach to the implementation of trading strategy 60 . <sup>w</sup> <sup>x</sup>

A framework for a hybrid intelligent system in support of marketing strategy development has been proposed by Li 29 and Li et al. 31 , with five<sup>w x</sup> <sup>w x</sup> objectives: to help strategic analysis; to couple strategic analysis with managers’ judgement; to integrate the strengths of diverse support techniques and technologies; to combine the benefits of different strategic analysis models; and to help strategic thinking. The proposed framework provides a pragmatic conceptual framework for the development of computer-based support for marketing strategy formulation and strategic marketing planning. This paper describes the development of a hybrid intelligent system for developing marketing strategy. In the following sections, the background for building a hybrid intelligent system for marketing strategy development is briefly discussed. The software architecture of the hybrid intelligent system is presented in detail. Particularly, the group assessment support, the fuzzification of marketing strategy factors and the fuzzy reasoning for setting marketing strategy are addressed. Moreover, other associated technical details are also examined. In addition, the findings of the field work on evaluating the system are also summarised. Conclusions are drawn and intended future research is outlined in Section 14.

## 2. Current provision of computer-based support for developing marketing strategy

Even with the pioneering efforts in the past, most computer applications in the marketing domain are routine and operational rather than strategic 64 .<sup>w</sup> <sup>x</sup>

Existing information systems are still rather limited in their support abilities 5 . Most reported systems <sup>w</sup> <sup>x</sup> for strategic marketing planning are either prototype or experimental 18 . Current information systems, in <sup>w</sup> <sup>x</sup> most instances, are still at early stages of development 47 , exhibiting a lack of success and a disap- <sup>w</sup> <sup>x</sup> pointing degree of satisfaction in support of marketing strategy development 29,32 .<sup>w</sup> <sup>x</sup>

A mail questionnaire survey was undertaken by Li <sup>w x</sup> <sup>w x</sup> 29 and Li et al. 32 in autumn 1997, in 900 large companies in the UK, to explore managerial requirements for computer-based support and current status of information systems in support of marketing strategy development. According to the responses from the 104 marketing directors and managing directors of these companies, 86 companies reported currently using computer-based systems to support the development of marketing strategy. Of the 86 companies, the most common computer-based support is provided by database systems 91.7% and spreadsheetsŽ . Ž . Ž . 90.5% . Nearly half 48.8% of the 86 companies reported currently using marketing information systems. Moreover, executive information systems Ž . Ž . 25% and DSSs 15.5% have also been reasonably used. But only 6% of the 86 companies reported currently using expert systems in support of marketing strategy development.

Moreover, according to the 86 British companies, most systems fail to provide even moderate help for the following five types of requirements: help couple strategic analysis with managerial judgement; provide strategic analysis assistance; help strategic thinking; cope with uncertainty and fuzziness; and help understand the factors that affect marketing strategy development. This lack of success has led to the fact that the greater number 55% of the re-Ž . sponding managers in the 86 companies are dissatisfied or very dissatisfied with the computer-based systems currently used in developing marketing strategy. Thirty-six percent of the respondents moderately satisfied. Only 9% of the respondents are satisfied, and nobody is very satisfied. It is also found that the four principal factors leading to managers’ dissatisfaction include: the individual system used is limited in support capabilities 54.3% ; the Ž . systems cannot couple strategic analysis with managerial judgement 53.6% ; the particular strategy Ž . analysis models employed are limited in function and scope 38.6% ; and the systems cannot deal withŽ . uncertainty and ambiguity 22.9% . Ž .

Although the above findings could be limited to the involved large companies in the UK, they do indicate that most support systems currently used for developing marketing strategy exhibit a disappointing degree of success.

## 3. The motivation for using a hybrid intelligent system in developing marketing strategy

Having recognised the problems of current system provision and the principal factors leading to managerial dissatisfaction, it should be possible to develop effective computer-based systems to support the process of marketing strategy development. However, the complexity of marketing strategy development and the requirements for effective and appropriate computer support for developing marketing strategy present a challenge to individual computer-based techniques and technologies.

It is evident that each specific technique has its own particular strengths and weaknesses that make it suitable for certain situations but not effective for others. DSSs, for instance, can assist with strategic marketing decision-making by utilising data and models to solve unstructured problems. However, conventional DSSs rely too much on limited quanti tative models and complete information 5 . Conven-<sup>w</sup> <sup>x</sup> tional DSSs are not very good at handling the cases where managers make decisions based heavily upon their own beliefs, experience and expertise. To deliver enhanced support, systems have been designed to support managers to make decisions based largely upon their own judgement e.g., 3,36 and expertise Ž <sup>w</sup> <sup>x</sup>. Že.g., 7,61,64 . Moreover, guidelines and concep- <sup>w</sup> <sup>x</sup>. tual framework have also been proposed to combine the intuition of managers and the analytic capability of the computer 31–33 . Recently, the DSS concept<sup>w</sup> <sup>x</sup> has been extended to accommodate the needs of groups of decision makers in the form of group decision support systems GDSSs 57,59 . GDSSsŽ . <sup>w</sup> <sup>x</sup> have been designed to improve meeting efficiency, effectiveness and team productivity 1,2,4 for groups <sup>w</sup> <sup>x</sup> of executives conducting strategic planning 10,21 .<sup>w</sup> <sup>x</sup> The systems have been used for a variety of planning tasks such as idea generation and evaluation, setting goals and objectives, evaluation of alternatives, identifying assumptions, and voting 1,2,16,17,21,46 . <sup>w</sup> <sup>x</sup> Although research suggests that the technology improves group functioning in some areas, and company experience suggests that the technology is useful in the planning process, the GDSS is not a final solution to planning problems 21 . If the advantages <sup>w</sup> <sup>x</sup> of GDSSs can be combined with the strengths of other techniques, such as ESs, fuzzy logic and hybrid systems, there is likely to be considerable benefit.

ESs also have both advantages and limitations in supporting marketing strategy development. While ESs can embody organised strategic marketing knowledge and generate reasoned advice or instructions for strategy formulation 38,44 , they are likely <sup>w</sup> <sup>x</sup> always to be limited in capability and applications. A conventional ES is restricted to a structured and narrow domain, and only well-defined situations can be modelled. In addition, a conventional ES cannot learn from or adapt to environmental changes <sup>w</sup> <sup>x</sup> 19,20,43,50 .

Fuzzy logic is another technique which has both advantages and limitations in support of strategic marketing decisions. Fuzzy logic can be used to deal with imprecise ‘‘linguistic’’ concepts or fuzzy terms. It aims at modelling the imprecise modes of reasoning that play an essential role in the remarkable human ability to make rational decisions in an environment of uncertainty, fuzziness and imprecision <sup>w</sup> <sup>x</sup> 65 . A potential limitation of fuzzy logic is that the membership functions and rules have to be specified manually. Moreover, fuzzy systems cannot adapt automatically to changes in the environment <sup>w</sup> <sup>x</sup> 19,20,43,50 .

ANNs can also be applied to aid the process of marketing strategy development. ANNs have salient features that are important in modelling and forecasting nonlinear systems; they are seen to have advantages over current statistical methods. They have proven to be particularly successful in forecasting and learning patterns from noisy or incomplete data. A main limitation of ANNs, however, is that they lack explanation capabilities. They are thus not suitable for applications where explanation of reasoning is critical 19,20,43,50 .<sup>w</sup> <sup>x</sup>

It is, therefore, clear that individual support techniques have their own strengths and weaknesses; a single support technique can only be fitted to assist some aspects of the marketing strategy development process. One approach to deal with this problem is to use hybrid intelligent systems. Through integrating the advantages of diverse support techniques and technologies into one hybrid system, a more powerful system than each of its components standing alone can be created, exploiting the synergy of the component parts 61 . In this study, the motivation<sup>w</sup> <sup>x</sup> for developing a hybrid intelligent system is to integrate the powers of different support techniques and technologies, such as ESs, fuzzy logic, ANNs and DSSs to support the development of marketing strategy where the required conditions are not satisfactorily met by individual techniques and technologies.

## 4. Development approaches

The development process of any advanced computing application contains inherent risk, and one means of reducing this risk is to adopt a development method. Goonatilake and Khebbal 20 propose<sup>w</sup> <sup>x</sup> a hybrid systems development cycle that is a relatively structured approach for the development of hybrid systems. According to Goonatilake and Khebbal, the construction of intelligent hybrid systems consists of six stages: problem analysis, property matching, hybrid category selection, implementation, validation, and maintenance. In this study, the development process proposed by Goonatilake and Khebbal is adopted as a general guidance for developing the hybrid intelligent system in support of marketing strategy formulation. A prototyping approach 45 is<sup>w</sup> <sup>x</sup> also used in the software implementation stage of the development of the hybrid system. In addition, the hybrid intelligent system is verified and validated according to the guidelines proposed by Klein and Methlie 25 and other researchers 30 .<sup>w x</sup> <sup>w x</sup>

## 5. Development tools

Several types of software development tools were selected to build the hybrid system. Microsoft Visual C<sup>qq</sup> was used to develop the neural network model, the individual<sup>r</sup>group assessment model and the graphical display module. The EXSYS Professional expert system development package was employed to build the fuzzy logic model and the expert system model. All the data files are managed by using EXSYS, Microsoft Visual C<sup>qq</sup> and dBASE III<sup>q</sup> data base management system.

## 6. Knowledge acquisition

Knowledge acquisition is the extraction of knowledge from sources of expertise and its transfer to the knowledge base. The knowledge in the domain of marketing strategy development was obtained from three types of sources: published literature, the 104 replies from a large-scale mail questionnaire survey, and interviews with experienced managers. The knowledge base contains general guidelines and expertise for setting marketing objectives and marketing strategy for large companies which are principally involved in the manufacture and sale of industrial goods, and provision of industrial services. The general factors considered for marketing strategy development are derived from published literature <sup>w</sup> <sup>x</sup> 15,24,38–40 , the 104 replies from the large-scale mail questionnaire survey 29,32 and interviews with<sup>w</sup> <sup>x</sup> marketing managers 30 . The general guidelines for<sup>w</sup> <sup>x</sup> developing marketing strategy are based on the literature 15,23,24,40 . The system allows users to con-<sup>w</sup> <sup>x</sup> sider and define their own strategic factors based on their specific circumstances. In addition, the definition and modification of relevant fuzzy membership functions remain open to users although fuzzy membership functions have been recommended by the system developer. Marketing managers can modify or adjust relevant fuzzy membership functions according to their own insights, experience and judgement. It is worth mentioning that the knowledge base can only provide some general guidelines and advice for marketing strategy development. Modifying the knowledge base for specific industries and deliver more detailed descriptions on marketing strategy would be an important option for future research.

## 7. The architecture of the hybrid intelligent system

The system aims at supporting the following three stages of marketing strategy development process:

strengths, weaknesses, opportunities and threats Ž . SWOT analysis; portfolio summary of the current product<sup>r</sup>market status; and setting marketing objectives and strategy.

To support the above three stages effectively, the hybrid intelligent system will:

<sup>Ø</sup> provide a logical process for strategic analysis;

<sup>Ø</sup> support group assessment of strategic marketing factors;

<sup>Ø</sup> help the coupling of strategic analysis with managerial judgement;

<sup>Ø</sup> help managers handle uncertainty and fuzziness;

<sup>Ø</sup> provide intelligent advice on developing marketing strategy.

To attain the above objectives, the hybrid intelligent system has been developed to integrate the strengths of ESs, fuzzy logic, ANNs and decision support technologies, and combine the benefits of different strategic analysis models. The system consists of five relatively independent, self-contained processing subsystem modules that share and exchange information, and undertake distinct functions to help solve parts of the strategic marketing decision problems to which they are best suited. These modules are co-ordinated by intercommunicating software control mechanisms. The integration of different support techniques and technologies is achieved by intercommunicating hybrids 20 and <sup>w</sup> <sup>x</sup> loose coupling 43 . The system architecture is illus- <sup>w</sup> <sup>x</sup> trated in Fig. 1, which is an application structure of the conceptual framework proposed by Li 29,30 <sup>w</sup> <sup>x</sup> and Li et al. 31 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/NY5SUEBR/fulltext/images/6a00b7831d751079097a29134819531bbfbc561598ca1d9d340a8eb63272a08b.jpg)  
Fig. 1. The architecture of the hybrid intelligent system.

Within this system, an artificial neural network model is developed to analyse and forecast the market growth and market share to support managers assessment of market attractiveness and business strengths. An indiÕidual<sup>r</sup>group assessment model is designed to evaluate the internal and external strategic factors, based upon the opinions of an individual or a group of managers. It also helps managers apply their judgement by scoring the strategic factors and assigning weights relative importance to them. AŽ . fuzzification component is used to deal with the fuzziness and imprecision existing inherently in various strategic factors. It works jointly and co-operatively with the expert system module to handle imprecise ‘‘linguistic’’ concepts, fuzzy terms and uncertainty in the assessment of market attractiveness and business strengths. A fuzzy expert system model is developed to represent expertise on marketing strategy development; to build the knowledge base; to provide strategic analysis guidance; and to generate intelligent advice or reasoned recommendations. A graphical display module is developed to provide graphical portrayal and presentation of strategic positions of products and markets in the portfolio matrices. Database technology, when necessary, is optionally used to collect and provide historical records on market growth, market share and sales history for the neural network model. Data files are used to pass and return data and information between different functional modules. Managers’ access to these functional modules and data files is accomplished by using a set of graphical user interfaces.

To combine the advantages of different strategy analysis models, Porter’s five forces model and the directional policy matrices DPM are integrated into Ž . the hybrid system. Because Porter’s five forces model <sup>w</sup> <sup>x</sup> 53,54 provides a structured framework for analysing industry competition, it is employed to evaluate competition and industry profitability in the assessment of market attractiveness. The DPM models 15,39,40<sup>w</sup> <sup>x</sup> offer a detailed methodological approach to analyse strategic factors and to establish marketing objectives and strategy. The nine-box DPM model 15<sup>w</sup> <sup>x</sup> and the four-box DPM model 39,40 are applied to <sup>w</sup> <sup>x</sup> summarise the state of products and markets, and establish associated marketing objectives and strategy.

## 8. Graphical user interfaces

Graphical user interfaces are designed to help managers input strategic information and evaluate various strategic factors. Particularly, user interfaces are developed to assist managers in assessing Porter’s five forces, market attractiveness factors and business strengths factors. A sample user interface is given in Fig. 2, which is used for evaluating market attractiveness factors. It can be seen, from the figure, that ANN forecasting results are displayed in a information window as information support. Scroll bars are used to graphically ask for inputs to various market attractiveness factors. Similarly, edit windows are also designed to help managers assign weights for relevant factors. The system also allows users to check and revise their strategic inputs before clicking the OK button.

## 9. The neural network forecasting model

The neural network model is designed to support managers in estimating market growth and market share. The ANN model used for the market growth rate and market share forecasting is the Generalized Delta Rule procedure for supervised learning, which is also called error back propagation algorithm 51 .<sup>w</sup> <sup>x</sup> To forecast market growth or share, the ANN model is first trained to model the growth or share across historic time periods. The output from the model is the growth rate or share 1 year ahead; the inputs are the growth rate or share on the previous year, together with growth rates or shares on several preceding years, plus the year of the predicted growth rate or share 28 .<sup>w</sup> <sup>x</sup>

The topology of the ANN model for the market growth and share forecasting with 1 year of lead time is as follows:

Input neurons: $t - 1 , I ( t - 1 ) , I ( t - 2 ) , I ( t - 3 )$

Hidden neurons: four hidden neurons

Output neuron: O tŽ .

where t<sup>s</sup>year of predicted growth rate or share, I xŽ . Ž . <sup>s</sup> growth rate or share at year x, O t <sup>s</sup> predicted growth rate or share at year t.

The forecasting results are stored in a market growth or market share file, which will be used as information inputs to the indiÕidual<sup>r</sup> group assessment model.

![](/api/attachments/NY5SUEBR/fulltext/images/26828afb87a7ab064a4853eb88f5c45aeaefaed570aa712eeeddca55796bf821.jpg)  
Fig. 2. A screen of evaluating market attractiveness factors.

## 10. The group assessment support module

The strategy development process often needs the opinions of a panel of managers 21,56 . Porter 55<sup>w</sup> <sup>x</sup> <sup>w x</sup> also argues that strategic planning should employ multifunctional planning teams with such members as line managers and the general manager involved. One of the salient features of the hybrid intelligent system is its group assessment support facility for developing marketing strategy or strategic marketing planning. In this system, the marketing strategy problem is decomposed into various relevant factors. These factors are arranged in a hierarchic structure.

Managers determine the scores and corresponding weights for relevant strategic factors based upon both their specific circumstances and their own judgement. The evaluation scores for a specific factor from different managers are averaged. The weights relative importance for a specific factor Ž . assigned by individual managers are aggregated. Managerial insights and judgement on the weight of each factor are then synthesized to determine the relative importance of the strategic criteria.

The computing principle for the group assessment support is stated as below. Assuming that we have n strategic factors to consider; there are k managers in the assessment group; each manager in the group is asked to score each factor in a scale of 1–10, and to assign a weight to each factor in a range of 0–1. Let $S _ { i j }$ be manager i’s score for factor j, $W _ { i j }$ be manager $i \ ' \mathrm { s }$ weighting for factor $j ,$ then the averaged score $\overline { { S } } _ { j }$ for factor $j$ is computed using Eq. 1 .Ž .

$$
\bar {S} _ {j} = \left(\sum_ {i = 1} ^ {k} S _ {i j}\right) / k \quad (j = 1, 2, \dots , n)\tag{1}
$$

The aggregated weight $\overline { { W } } _ { i }$ for factor $j$ is gained using Eq. 2 .Ž .

$$
\overline {{{W}}} _ {j} = \left(\sum_ {i = 1} ^ {k} W _ {i j}\right) / \left(\sum_ {l = 1} ^ {n} \sum_ {i = 1} ^ {k} W _ {i l}\right) \quad (j = 1, 2, \dots , n)\tag{2}
$$

Where

$$
W _ {i j} = \left( \begin{array}{c c c c} w _ {1 1} & w _ {1 2} & \dots & w _ {1 n} \\ w _ {2 1} & w _ {2 2} & \dots & w _ {2 n} \\ \dots & \dots & \dots & \dots \\ w _ {k 1} & w _ {k 2} & \dots & w _ {k n} \end{array} \right) \quad \text { and } \quad \sum_ {i = 1} ^ {n} W _ {k i} = 1
$$

Finally, the industry profitability score, market attractiveness score and the business strengths score are computed, respectively. Take the calculation of market attractiveness score as an example, there are m factors affecting the market attractiveness, then the attractiveness score A is obtained using Eq. 3 .Ž .

$$
A = \sum_ {j = 1} ^ {m} \overline {{S}} _ {j} \overline {{W}} _ {j}\tag{3}
$$

where the score A ranges from 1 to 10.

Through combining and aggregating the opinions of a group of mangers, a ‘‘middle of the road’’ assessment may be obtained. In this way, a panel of managers’ opinions and judgements can also be incorporated into the strategic factors assessment process. This group support facility is implemented in the module of individual or group assessment model.

The group assessment support model is designed as a collaborator rather than a substitute or replacement for GDSSs. If it works co-operatively with an effective GDSS by cultivating the strengths of GDSSs in supporting group meeting and consensus building for assessing strategic marketing factors, the hybrid system would deliver more powerful support for the process of marketing strategy development or strategic marketing planning.

## 11. Fuzzification of marketing strategy factors

According to literature 9,27 and the mail ques-<sup>w</sup> <sup>x</sup> tionnaire survey 29,32 , marketing strategy develop-<sup>w</sup> <sup>x</sup> ment involves a high degree of uncertainty and ambiguity. Imprecise measures, fuzziness and uncertainty of strategic factors all present challenges to computer-based support. Subjectivity of the decision making process and unclear decision rules make the application of computer support in this field more difficult.

Fuzzy logic can be applied to cope with fuzziness and uncertainty in the process of marketing strategy development and strategic marketing planning. However, progress towards the application of fuzzy logic in support of strategic marketing decisions has been slow. Previous work handles strategic criteria of DPM matrices by using a ‘‘crisp’’ or ‘‘clear-cut’’ method. In the previous applications of the DPM model, market attractiveness and business strengths are evaluated in a crisp way, which is actually a case of conventional set theory. For example, if the market attractiveness score is equal to or less than 3.3, then market attractiveness is considered to be ‘‘low’’. If the score is greater than 3.3, say 3.33 or 3.4, then market attractiveness is considered ‘‘medium’’. There is a clear-cut, sudden change from ‘‘low’’ to ‘‘medium’’. However, in real situations, if we consider the score 3.3 is ‘‘low’’, then the score 3.33 or 3.4 would also be ‘‘low’’, but with a lesser degree.

To be more realistic, we do not want to separate ‘‘low’’ and ‘‘medium’’ crisply from each other. We hope to measure the strategic criteria as ‘‘low’’ or ‘‘medium’’ to a certain degree. A more realistic and practical representation of the above problem is that of a fuzzy set where there is a gradual decline in confidence of the ‘‘low’’ set and a gradual increase in the ‘‘medium’’ set as the market attractiveness score increases. This is represented in a fuzzy membership function diagram in Fig. 3.

In Fig. 3, fuzzy logic is employed to assign degrees of confidence to the possible options of ‘‘low’’, ‘‘medium’’, or ‘‘high’’ for market attractiveness. Similarly, it is also used to determine the degrees of confidence to possible values of ‘‘weak’’, ‘‘medium’’, or ‘‘strong’’ for business strengths. In this system, as the market attractiveness score increases, the confidence in each of the three values

![](/api/attachments/NY5SUEBR/fulltext/images/5eb12ded21860ac369654d5c1b23aeb40814eb671373960006bedfa4bd1091d9.jpg)  
Fig. 3. Market attractiveness with fuzzy membership functions.

Ž . Ž low, medium, and high will smoothly increase and in some cases, fall off gradually , rather than change. abruptly at a threshold value. At a score of 3.3, the ‘‘low’’ attractiveness would have a confidence of 0.7 and ‘‘medium’’ attractiveness would get a confidence of 0.3. Once the fuzzy membership functions are defined, a new assessment score can be classified into their corresponding fuzzy values.

Marketing strategy factors and some strategic analysis models can be fuzzified through converting them into membership functions. In this study, in order to ease and simplify the calculation of the inferential logic, we use trapezoidal membership functions 27 for representing the relevant fuzzy<sup>w</sup> <sup>x</sup> sets. Take the nine-box DPM model 15,40 as an <sup>w</sup> <sup>x</sup> example, once the market attractiveness and business strengths are fuzzified, the DPM matrix becomes the diagram in Fig. 4.

Within this fuzzified DPM matrix, strategic options change gradually with certain confidence due to a change in either criterion of market attractiveness or business strengths, rather than change abruptly. Furthermore, even within the same box, the degree of applying a specific strategic option may vary, depending on the actual values of strategic factors and the membership functions.

## 12. Fuzzy reasoning for setting marketing strategy

Fuzzy reasoning is the process of deriving conclusions from a given set of fuzzy rules acting on fuzzified strategic information. An example of the reasoning process combining Porter’s five forces model and the DPM model is shown in Fig. 5. We can see, from the figure, that managerial judgement can be applied to the input and assessment of various strategic factors. Fuzzy inference rules are developed to specify the relationships among the fuzzy strategic variables. The fuzzy rules are in the form of IF . . . THEN . . . statements. All the fuzzy rules in the knowledge base whose conditions match or partially match will contribute to the final results. If the fuzzy rules have more than one IF condition, the confidence of the IF parts would be passed and combined before assigning the confidence to the THEN part. In this way, the final intelligent advice is the contribution of all the fuzzy rules. It would offer more than one strategy option with different degrees of confidence.

![](/api/attachments/NY5SUEBR/fulltext/images/54fc3799754ae5d758b313f5da723abdc895a3a383161ac468e88249c41fdb68.jpg)  
Fig. 4. DPM with membership functions.

![](/api/attachments/NY5SUEBR/fulltext/images/9617383a8edc6834f17ecaaa2a9c3c0974fb686f707edce806858cf707b69b77.jpg)  
Fig. 5. Example of fuzzy reasoning process.

Three typical fuzzy rules for the fuzzified DPM model in the hybrid intelligent system are given in the following:

IF fuzzy market attractiveness is high

AND fuzzy business strength is strong

THEN fuzzy strategy option is ^^Protect Position ^^

IF fuzzy market attractiveness is high

AND fuzzy business strength is medium

THEN fuzzy strategy option is ^^Invest to Build ^^

IF fuzzy market attractiveness is high

AND fuzzy business strength is low

THEN fuzzy strategy option is ^^Build Selectively ^^

Hypertext screens are then used to provide further advice for strategy options. If the strategy option is to Protect Position at certain confidence level, for example, the hypertext advice provides the manager with more detailed strategic recommendation with certain degree of confidence as follows: invest to grow at maximum digestible rate; concentrate efforts on maintaining strengths.

A sample reasoning result is given in Fig. 6. The reasoning is based upon managers’ strategic inputs through a set of graphical user interfaces. As shown in Fig. 6, the calculated market attractiveness score is 7.89 crisp value , and business strength score isŽ . 7.66 crisp value . Fuzzified market attractiveness is Ž . medium with a confidence of 0.11, and high with a confidence of 0.89. Fuzzified business strength is medium at a confidence of 0.34 and strong at a confidence of 0.66. The recommended fuzzy strategy options are to Protect Position with a confidence of 0.587 and to InÕest to Build at confidence of 0.303.

![](/api/attachments/NY5SUEBR/fulltext/images/ec5a99c59079303fb9b9799ce1805048fc71f6f2b5ef67b4e9f528a724f8b2b9.jpg)  
Fig. 6. Intelligent advice on fuzzy strategy options.

A hypertext screen is displayed for further advice on Protect Position strategy. Similarly, further hypertext advice on InÕest to Build is also available.

## 13. Initial evaluation

Evaluation is defined as the process of examining a system’s ability to solve real-world problems in a particular problem domain 8,49 . It is also defined<sup>w</sup> <sup>x</sup> as the process of assessing a software system’s overall value 48 . For the purpose of this study, evalua-<sup>w</sup> <sup>x</sup> tion work has been undertaken to: test, to what extent, the system can help marketing managers develop marketing strategy; assess the system’s overall capability in support of real world marketing strategy development; obtain some evidence of the system’s value as an effective means to support marketing strategy development; gain feedback and comments from marketing managers to improve the hybrid system.

The system has been evaluated in five large British companies 30 , including a satellite equipment man- <sup>w</sup> <sup>x</sup> ufacturer, a machine tools manufacturer, a stair lifts manufacturer, an industrial materials handling equipment manufacturer, and a logistics services company. These companies have been previously involved in the mail questionnaire survey undertaken at the earlier stages of this study. Four of the five selected companies reported currently using computer-based information systems for developing marketing strategy. Prior to the evaluation process, the consistency and completeness of the system was verified according to the guidelines proposed by Klein and Methlie 25 and other researchers 30 . In<sup>w x</sup> <sup>w x</sup> addition, the system was also validated by four academic experts two information systems experts Ž and two marketing experts before it was evaluated. by potential industrial users.

The evaluation process involved data preparation, the development of marketing strategy using the hybrid system, and semi-structured questionnaires. Before the evaluation meeting, marketing directors were asked to complete a set of data forms and to prepare relevant information based on their company databases and their experience and judgement. During the evaluation meeting, marketing directors were invited to use and run the system in their own company. Specifically, managers were requested to develop marketing strategy concerning specific products and markets by using their own strategic inputs. After using and testing the system, managers were asked to answer an evaluation questionnaire.

Seven items were used to measure the provision of the hybrid system. The items for measuring system provision were designed on the basis of previous work 29,30,32 . When the managers were asked, in <sup>w</sup> <sup>x</sup> seven structured questions, about the general provision of the hybrid system, the information in Table 1 was obtained. The listed figures in each row in the table indicate the number of companies. For example, two companies reported that the system is moderately helpful in providing ‘‘strategic analysis guidance’’; three companies reported that it is very helpful in this aspect. According to marketing directors of the five involved companies, it appears that the system is moderately helpful in some aspects, very helpful in most, and extremely helpful in two.

In addition to the structured questions, open-ended questions were also used to seek comments and feedback from marketing managers. In addition to the information given in Table 1, written comments were also given by some marketing directors in evaluating the group assessment support module: ‘‘Helpful especially for quantifying subjective and overly influential judgement’’; ‘‘Useful for evaluating group decisions and their perceptions of strategic policy’’.

The user interfaces of the system was perceived to be ‘‘ visually clear’’, ‘‘adequate’’, ‘‘good’’, or ‘‘generally OK’’. The response time of the system was considered to be ‘‘acceptable’’, ‘‘very fast’’, or ‘‘good’’.

The advice or outputs generated by the system were reported to be: ‘‘They are exactly what we are doing’’; ‘‘They reflect clearly our own judgement of the strategic position of our company’’; ‘‘Surprisingly accurate’’; ‘‘Useful prompts’’; ‘‘Mostly sound in our example case worked’’; ‘‘They form the Ž . basis of our strategic planning process’’; ‘‘The output and explanatory screens seemed to confirm my own intuition about the market’’.

The support delivered by the system was perceived to be: ‘‘Allows many ‘what–if’ scenarios to be used to evaluate competitive strategy’’; ‘‘Confirms instincts’’; ‘‘Codifying input and maintain an ‘audit’ trial, useful in developing strategy over a period of time’’; ‘‘A means of rapidly handling quantitative and qualitative data’’; ‘‘Useful tool in assessing individual ‘projects’ as well as sectors’’; ‘‘Challenging–useful framework; greater clarity of thinking; forced to think through the factors’’.

General provision of the hybrid system for developing marketing strategy

<table><tr><td>Item</td><td>No answer</td><td>No help at all</td><td>Somewhat helpful</td><td>Moderately helpful</td><td>Very helpful</td><td>Extremely helpful</td></tr><tr><td>Strategic analysis guidance for developing marketing strategy</td><td></td><td></td><td></td><td>2</td><td>3</td><td></td></tr><tr><td>Help understand the factors that affect marketing strategy development and how they interact</td><td></td><td></td><td></td><td>3</td><td>2</td><td></td></tr><tr><td>Help the coupling of strategic analysis with managerial judgement</td><td></td><td></td><td></td><td>1</td><td>4</td><td></td></tr><tr><td>Support and supplement managerial judgement and intuition</td><td></td><td></td><td></td><td>1</td><td>3</td><td>1</td></tr><tr><td>Help strategic thinking in the process of developing marketing strategy</td><td></td><td></td><td></td><td>2</td><td>3</td><td></td></tr><tr><td>Help deal with fuzziness and uncertainty</td><td></td><td></td><td>1</td><td>1</td><td>3</td><td></td></tr><tr><td>Support group assessment of strategic marketing factors based on a group of managers&#x27; opinions</td><td>1</td><td></td><td>1</td><td></td><td>2</td><td>1</td></tr></table>

Furthermore, comments on how to improve the system were also offered by marketing managers: ‘‘More description details on strategic elements of strategy’’; ‘‘ Provide an easier approach to compareŽ . with businesses and to compare with competitors’’; ‘‘ For group assessment support module would pre-Ž . fer to discuss the scores in an open form to meet the group expectations’’; ‘‘New but would like to establish the sensitivity of the model of changes in assumptions, then be able to assess the confidence in decision making’’; ‘‘Support managerial debate’’.

## 14. Conclusions and future research

The development of a hybrid intelligent system for marketing strategy development has been described in the paper. Aiming at offering enhanced support, the system has been developed to combine the strengths of an ES, fuzzy logic, an ANN model and decision support technologies. It has also been designed to integrate the benefits of Porter’s five forces model and the DPM models in support of strategic analysis. At least, the following salient features have been implemented in the system:

1. It provides managers with an organised method to conduct strategic analysis;

2. It supports the group assessment of marketing strategy factors based upon the opinions of a panel of managers;

3. It employs an ANN forecasting model to help managers assess market growth and market share;

4. It helps the coupling of strategic analysis with managerial judgement;

5. It harnesses fuzzy logic to handle fuzziness and uncertainty in evaluating strategic criteria;

6. It utilises a fuzzy expert system to conduct fuzzy reasoning for developing marketing strategy.

The system has been evaluated with marketing directors in five large British companies. Marketing directors’ responses to the system were very favourable. Empirical evidence indicates that the hybrid system is useful and helpful in support of the key aspects of marketing strategy development. The advice or outputs generated by the hybrid system were reported to be mostly sound, surprisingly accurate, and clearly reflecting managerial judgement. The system has potential as an effective means for developing marketing strategy.

The work and related findings reported here, however, are exploratory and preliminary. Further efforts on improving the system functions and further evaluation work with more industrial users will be a matter of priority of the future work.

## Acknowledgements

The author would also like to acknowledge the following people for their comments: Mr. Russell Kinman for his comments on the hybrid system and the earlier version of the evaluation questionnaire design; Dr. Yanqing Duan for her comments on the earlier version of the software system; Dr. John S. Edwards for his comments on the earlier version of the evaluation questionnaire design; Dr. Steve Clarke and Mr. Brian Lehaney for their comments on the system. The author also wishes to thank the following company directors for their involvement and support in evaluating the hybrid system: Mr. Andrew Roberts, Marketing Director, MARTRA MARCONI Space, UK; Mr. Ian Smith, General Manager, Marketing and International Sales, Bridgeport Machines, UK; Mr. Peter Gilbert, Marketing Director, Stannah Stairlifts, UK; Mr. Kim Martin, Marketing Manager, Dexion, UK; Mr. Steve Russell, Business Development Director, Swift Transport Services, UK. The author is very grateful to the editor and the anonymous reviewers whose valuable comments have helped improve this paper.

## References

<sup>w</sup> <sup>x</sup> 1 M. Aiken, D. Hawley, W. Zhang, Increasing meeting efficiency with a GDSS, Industrial Management and Data System 94 8 1994 13–16.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 M. Aiken, M. Vanjani, J. Krosp, Group decision support systems, Review of Business 16 3 1995 38–42.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 P. Alpar, Knowledge-based modelling of marketing managers’ problem solving behaviour, International Journal of Research in Marketing 8 1991 5–16.Ž .

<sup>w</sup> <sup>x</sup> 4 M. Alavi, Group decision support systems: a key to business team productivity, Journal of Information Systems Management 8 3 1991 36–41.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 C. Amaravadi, S. Samaddar, S. Dutta, Intelligent marketing information systems: computerised intelligence for marketing decision making, Marketing Intelligence and Planning 13 2Ž . Ž . 1995 4–13.

<sup>w</sup> <sup>x</sup> 6 S. Belardo, P. Duchessi, J.R. Coleman, A strategic decision support system at Orell Fussli, Journal of Management Information Systems 10 4 1994 135–157.Ž . Ž .

<sup>w</sup> <sup>x</sup>7 O.J. Borch, G. Hartvigsen, Knowledge-based systems for strategic market planning in small firms, Decision Support Systems 7 2 1991 145–157.Ž . Ž .

<sup>w</sup> <sup>x</sup>8 D. Borenstein, Towards a practical method to validate decision support systems, Decision Support Systems 23 1998Ž . 227–239.

<sup>w</sup> <sup>x</sup> 9 D. Brownlie, J.C. Spender, Managerial judgement in strategic marketing: some preliminary thoughts, Management Decision 33 6 1995 39–50.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 L. Campbell, Technology update: group decision support systems, Journal of Accountancy 170 1 1990 47–50.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 C. Carlsson, Fuzzy logic and hyperknowledge: a new, effective paradigm for active DSS, Proceedings of HICSS-30, IEEE Computer Society Press, Los Alamitos, 1997, pp. 324–333.

<sup>w</sup> <sup>x</sup> 12 C. Carlsson, Expert systems as conceptual frameworks and management support systems for strategic management, International Journal of Information Resources Management 2 Ž . Ž .4 1991 14–22.

<sup>w</sup> <sup>x</sup> 13 C. Carlsson, O. Kokkonen, P. Walden, Woodstrat: a support system for strategic management, in: E. Turban Ed. , Infor-Ž . mation Technology for Management Improving Quality and Productivity, Wiley, New York, 1996, pp. 148–154.

<sup>w</sup> <sup>x</sup> 14 C. Carlsson, P. Walden, O. Kokkonen, Effective strategic management with hyperknowledge: the Woodstrat case, The Finnish Paper and Timber Journal 78 5 1996 278–290.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 G.S. Day, Analysis for Strategic Market Decisions, West Publishing, St. Paul, MN, 1986.

<sup>w</sup> <sup>x</sup> 16 G. DeSanctis, R.B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 5Ž . Ž .1987 589–609.

<sup>w</sup> <sup>x</sup> 17 A.R. Dennis, J.F. George, L.M. Jessup, J.F. Nunamaker Jr., D.R. Vogel, Information technology to support electronic meetings, Management Information Systems Quarterly 12 4Ž . Ž . 1998 591–624.

<sup>w</sup> <sup>x</sup> 18 Y. Duan, P. Burrell, A hybrid system for strategic marketing planning, Marketing Intelligence and Planning 13 11 1995Ž . Ž . 5–12.

<sup>w</sup> <sup>x</sup> 19 S. Goonatilake, Intelligent systems for finance and business: an overview, in: S. Goonatilake, P. Treleaven Eds. , Intelli-Ž . gent Systems for Finance and Business, Wiley, 1995.

<sup>w</sup> <sup>x</sup> 20 S. Goonatilake, S. Khebbal, Intelligent hybrid systems: issues, classifications and future directions, in: S. Goonatilake, S. Khebbal Eds. , Intelligent Hybrid Systems, Wiley, 1995.Ž .

<sup>w</sup> <sup>x</sup> 21 L.M. Jessup, S. Kukalis, Better planning using group support systems, Long Range Planning 23 3 1990 100–105. Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 T.W. Chien, V. Lin, B. Tan, W.C. Lee, A neural networksbased approach for strategic planning, Information and Management 35 1999 357–364.Ž .

<sup>w</sup> <sup>x</sup> 23 A.C. Hax, N.S. Majluf, The use of the growth-share matrix in strategic planning, Interfaces 13 1 1983 46–60.Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 A.C. Hax, N.S. Majluf, The use of the industry attractiveness-business strength matrix in strategic planning, Interfaces 13 2 1983 54–71.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 M.R. Klein, L.B. Methlie, Knowledge-Based Decision Support Systems with Applications in Business, Wiley, Chichester, England, 1995.

<sup>w</sup> <sup>x</sup> 26 R.J. Kuo, K.C. Xue, A decision support system for sales forecasting through fuzzy neural networks with asymmetric fuzzy weights, Decision Support Systems 24 2 1998Ž . Ž . 105–126.

<sup>w</sup> <sup>x</sup> 27 J.B. Levy, E. Yoon, Modelling global market entry decision by fuzzy logic with an application to country risk assessment, European Journal of Operational Research 82 1 1995Ž . Ž . 53–78.

<sup>w</sup> <sup>x</sup> 28 S. Li, Some issues of neural nets in forecasting, Presented at OR39: Operational Research Society Annual Conference, Bath, England, 9–11 September 1997.

<sup>w</sup> <sup>x</sup> 29 S. Li, Computer-Based Support for Developing Marketing Strategy, Research Report for Transfer from MPhil to PhD, Luton Business School, University of Luton, England, April 1998.

<sup>w</sup> <sup>x</sup> 30 S. Li, Computer-based support for marketing strategy development: investigation of managers’ needs for support, current provision, and hybrid intelligent support systems, Unpublished PhD Thesis, University of Luton, England, May 1999.

<sup>w</sup> <sup>x</sup> 31 S. Li, Y. Duan, R. Kinman, J. Edwards, A framework for a hybrid intelligent system in support of marketing strategy development, Marketing Intelligence and Planning 17 2Ž . Ž . 1998 70–77.

<sup>w</sup> <sup>x</sup> 32 S. Li, R. Kinman, Y. Duan, J. Edwards, Computer-based support for marketing strategy development: review and questionnaire survey, European Journal of Marketing 34 Ž . 2000 Forthcoming.

<sup>w</sup> <sup>x</sup> 33 F. Kuo, Managerial intuition and the development of executive support systems, Decision Support Systems 24 2 1998Ž . Ž . 89–103.

<sup>w</sup> <sup>x</sup> 34 M.J. Liberatore, A.C. Stylianou, Using knowledge-based systems for strategic market assessment, Information and Management 27 1994 221–232.Ž .

<sup>w</sup> <sup>x</sup> 35 G.L. Lilien, P. Kotler, K.S. Moorthy, Marketing Models, Prentice Hall, Englewood Cliffs, NJ, 1992, pp. 573–597.

<sup>w</sup> <sup>x</sup> 36 J.S. Lim, M. O’Connor, Judgemental forecasting with interactive forecasting support systems, Decision Support Systems 16 4 1996 339–357.Ž . Ž .

<sup>w</sup> <sup>x</sup> 37 J.D.C. Little, Decision support systems for marketing managers, Journal of Marketing 43 3 1979 9–27.Ž . Ž .

<sup>w</sup> <sup>x</sup> 38 M.H.B. McDonald, Marketing planning and expert systems: an epistemology of practice, Marketing Intelligence and Planning 7 7Ž . Ž .<sup>r</sup>8 1989 16–23.

<sup>w</sup> <sup>x</sup> 39 M.H.B. McDonald, Some methodological comments on the

directional policy matrix, Journal of Marketing Management 6 1 1990 59–68.Ž . Ž .

<sup>w</sup> <sup>x</sup> 40 M.H.B. McDonald, Strategic Marketing Planning, Kogan Page, London, 1996.

<sup>w</sup> <sup>x</sup> 41 M.H.B. McDonald, H.N. Wilson, State-of-the-art development in expert systems and strategic marketing planning, British Journal of Management 1 3 1990 159–170.Ž . Ž .

<sup>w</sup> <sup>x</sup> 42 R. McIvor, G. Scullion, M. McTear, Development of a strategic management interactive learning expert system, International Journal of Information Resource Management 3 Ž . Ž .2 1992 11–23.

<sup>w</sup> <sup>x</sup> 43 L.R. Medsker, Hybrid Neural Networks and Expert Systems, Kluwer Academic Publishers, Norwell, MA, 1994.

<sup>w</sup> <sup>x</sup>44 L. Moutinho, B. Curry, F. Davies, The COMSTRAT model: development of an expert system in strategic marketing, Journal of General Management 19 1 1993 32–47.Ž . Ž .

<sup>w</sup> <sup>x</sup> 45 J.D. Naumann, A.M. Jenkins, Prototyping: the new paradigm for systems development, Management Information Systems Quarterly 6 3 1982 29–44.Ž . Ž .

<sup>w</sup> <sup>x</sup> 46 J.F. Nunamaker Jr., D.R. Vogel, A.R. Heminger, B. Martz, R. Crohowski, C. McGoff, Group support systems in practice: experience at IBM, in: R. Blanning, D. King Eds. ,Ž . Proceedings of the Twenty-Second Annual Hawaii International Conference on Systems Sciences, Vol. III, IEEE Computer Society Press, 1989.

<sup>w</sup> <sup>x</sup> 47 T.V. O’Brien, D.D. Schoenbachler, G.L. Gordon, Marketing information systems for consumer products companies: a management review, Journal of Consumer Marketing 12 5Ž . Ž . 1995 16–36.

<sup>w</sup> <sup>x</sup> 48 R.M. O’Keefe, O. Balci, E.P. Smith, Validating expert system performance, IEEE Expert 2 4 1987 81–90.Ž . Ž .

<sup>w</sup> <sup>x</sup> 49 T.J. O’Leary, M. Goul, K.E. Moffitt, A.E. Radwan, Validating expert systems, IEEE Expert 5 3 1990 51–58. Ž . Ž .

<sup>w</sup> <sup>x</sup> 50 B.A. Osyk, B.S. Vijayaraman, Integrating expert systems and neural nets: exploring the boundaries of AI, Information Systems Management 12 2 1995 47–54.Ž . Ž .

<sup>w</sup> <sup>x</sup> 51 Y. Pao, Adaptive Pattern Recognition and Neural Networks, Addison-Wesley Publishing, 1989.

<sup>w</sup> <sup>x</sup> 52 H.L. Poh, A neural network approach for decision support, International Journal of Applied Expert Systems 2 3 1994Ž . Ž . 196–216.

<sup>w</sup> <sup>x</sup> 53 M.E. Porter, Competitive Strategy: Techniques for Analysing Industries and Competitors, The Free Press, New York, 1980.

<sup>w</sup> <sup>x</sup> 54 M.E. Porter, Industry structure and competitive strategy: keys to profitability, Financial Analysis Journal July–August Ž 1980 30–41..

<sup>w</sup> <sup>x</sup> 55 M.E. Porter, Corporate strategy: the state of strategic thinking, The Economist May 23, 1987 21–22, 27–28. Ž .

<sup>w</sup> <sup>x</sup> 56 M.A. Rathwell, A. Burns, Information systems support for group planning and decision marking activities, MIS Quarterly 9 1985 255–271.Ž .

<sup>w</sup> <sup>x</sup> 57 R.H. Sprague, A framework for the development of decision support systems, Management Information Systems Quarterly 4 4 1980 000.Ž . Ž .

<sup>w</sup> <sup>x</sup> 58 K.Y. Tam, M.Y. Kiang, Managerial applications of neural networks: the case of bank failure predictions, Management Science 38 7 1992 926–947.Ž . Ž .

<sup>w</sup> <sup>x</sup> 59 J.T.C. Teng, K. Ramamurthy, Group decision support systems: clarifying the concept and establishing a functional taxonomy, INFOR 31 3 1993 166–185. Ž . Ž .

<sup>w</sup> <sup>x</sup> 60 R. Tsaih, Y. Hsu, C.C. Lai, Forecasting S&P 500 stock index futures with a hybrid AI system, Decision Support Systems 23 1998 161–174.Ž .

<sup>w</sup> <sup>x</sup> 61 E. Turban, P.R. Watkins, Integrating expert systems and decision support systems, MIS Quarterly, June 1986 121–Ž . 136.

<sup>w</sup> <sup>x</sup> 62 P. Walden, C. Carlsson, Enhancing strategic market management with knowledge-based systems, HICSS-26 Proceedings, IEEE Computer Society Press, Los Alamitos, 1993, pp. 240–248.

<sup>w</sup> <sup>x</sup> 63 P. Walden, C. Carlsson, Strategic management with a hyperknowledge support system, Proceedings of the HICSS-27 Conference, 1994, pp. 241–250.

<sup>w</sup> <sup>x</sup> 64 H. Wilson, M. McDonald, Critical problems in marketing planning: the potential of decision support systems, Journal of Strategic Marketing 2 1994 249–269.Ž .

<sup>w</sup> <sup>x</sup> 65 L.A. Zadeh, Fuzzy logic, IEEE Computer 21 1988 83–93.Ž .

<sup>w</sup> <sup>x</sup> 66 J. Moormann, M. Lochte-Holtgreven, An approach for an integrated DSS for strategic planning, Decision Support Systems 10 1993 401–411.Ž .

<sup>w</sup> <sup>x</sup> 67 B. Arinze, Marketing planning with computer models: a case study in the software industry, Industry Marketing Management 19 2 1990 117–129.Ž . Ž .

<sup>w</sup> <sup>x</sup> 68 A.-M. Chang, C.W. Holsapple, A.B. Whinston, Model management issues and directions, Decision Support Systems 9 Ž . 1993 19–37.

<sup>w</sup> <sup>x</sup> 69 A.-M. Chang, C.W. Holsapple, A.B. Whinston, A hyperknowledge framework of decision support systems, Information Processing and Management 30 4 1994 473–498. Ž . Ž .

<sup>w</sup> <sup>x</sup> 70 M.J. Liberatore, A.C. Stylianou, Using knowledge-based system for strategic market assessment, Information and Management 27 1994 221–232. Ž .

![](/api/attachments/NY5SUEBR/fulltext/images/102a8e95a889c487b23df059bc7cc558253fac9e6a1d8f6450a11715f6efb38f.jpg)

Shuliang Li received his BS in Computer Science and MS in Management Science from Southwest Jiaotong University, China, and PhD pending inŽ . Decision Support Systems from University of Luton, England, UK. Since 1994, Mr. Li has been Associate Professor at the School of Economics and Management, Southwest Jiaotong University, Chengdu, China. From October 1995 to September 1996, he worked as a senior visiting scholar at the University of Ed-

inburgh, Scotland, UK. He is currently a Research Fellow at Gloucestershire Business School, England, UK, and also a Visiting Associate Professor at Southwest Jiaotong University, China. He has published four books and about 20 papers in the fields of intelligent business systems, decision support systems, and systems simulation. Mr. Li has also developed several software systems for business decision making.
