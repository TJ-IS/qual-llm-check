---
otero_id: 2942
otero_key: "HD8EQ5CS"
title: "The design features of forecasting support systems and their effectiveness"
authors: "Robert Fildes; Paul Goodwin; Michael Lawrence"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.01.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The design features of forecasting support systems and their effectiveness

Robert Fildes <sup>a,T</sup>, Paul Goodwin <sup>b,1</sup>, Michael Lawrence <sup>c,2</sup>

<sup>a</sup> Dept. Management Science, Lancaster University Management School, Lancaster LA1 4YX, United Kingdom <sup>b</sup> The Management School, University of Bath, Bath BA2 7AY, United Kingdom <sup>c</sup> School of Information Systems, University of New South Wales, Sydney 2052, Australia

Available online 16 February 2005

## Abstract

Forecasts play a key role in the management of the supply chain. In most organisations such forecasts form part of an information system on which other functions, such as scheduling, resource planning and marketing depend. Forecast accuracy is, therefore, an important component in the delivery of an effective supply chain. Typically, the forecasts are produced by integrating managerial judgment with quantitative forecasts within a forecasting support system (FSS). However, there is much evidence that this integration is often carried out poorly with deleterious effects on accuracy. This study integrates the literatures on forecasting and decision support to explain the causes of the problem and to identify design features of FSSs that might help to ameliorate it. It is also argued that, by studying the supply chain forecasting task, DSS researchers could learn much about decision support in general and also make a significant contribution to the improvement of forecasting practice <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Decision support systems; Forecasting support systems; Combining statistical methods and judgment; User participation; Supply chain

## 1. Introduction

Forecasts of demand play a key role in shaping the activities of companies that are based in supply chains. Decisions relating to purchasing, marketing, manufacturing, staffing, financial planning and logistics are all dependent on such forecasts. For most of these companies, a particular type of a DSS, known as a Forecasting Support System (FSS) is employed to prepare the forecasts (in 2001 the international market for such systems was worth \$250 m in the U.S. and UK alone.). Keen and Scott Morton [28] define the task appropriate for a support system as one where the manager’s judgment plus the model embedded in the system can provide a more effective solution than either alone. This synergy is typical of most supply chain forecasting tasks. For example, statistical models are adept at finding patterns in large volumes of data, while managers can take into account the effects of special events like future product promotions. Such special factors are often treated as noise by statistical models, because the reliable estimation of their effects is precluded by a paucity of data.

The key features of FSSs that assist this integration of model and judgment are the following: (1) a database that includes the time series history for many items, together with related data such as prices and an event history of factors like sales promotion campaigns; (2) a set of quantitative forecasting techniques such as exponential smoothing [9], and (3) facilities that allow the application of managerial judgments. The final critical aspect is that the FSS supports a process that is repeated at regular intervals, allowing the forecast and outcomes to be compared. Indeed, the forecasts errors, themselves, can form a part of the database.

Despite the potential benefits of using <sup>b</sup>the manager plus the system<sup>Q</sup> to obtain forecasts, there is much evidence that this potential is underexploited by FSS users in supply chain companies. On the one hand, managers tend to rely too heavily on their own judgments in circumstances where quantitative models would be more reliable. On the other hand, when the use of judgment is appropriate, most commercial FSS packages offer, at best, only limited facilities to support managers in arriving at their judgments.

This paper draws on the DSS and forecasting literatures to consider how this situation might be improved and, where appropriate, it proposes a research agenda for improving such systems. Unlike applications considered in much other DSS research, forecasting provides regular evidence on the support system’s effectiveness. It therefore allows for the evaluation of alternative user-interface designs and of the support system’s model components, thereby providing insights that are potentially valuable for DSS research in general.

The paper first considers the nature of the forecasting task in supply chain companies. The ideal usage of an FSS is then explained in Section 3 and we show that usage in practice often departs from this ideal. Section 4 examines the key question of how future research into FSS design can be directed to improving forecasting. Conclusions are drawn in Section 5 where the ideal attributes of an FSS are identified. It is argued that DSS researchers have much to offer, and also much to gain, by researching how these attributes might be attained.

## 2. The nature of the supply chain forecasting task

This section outlines some key aspects of the forecasting task in supply chain companies to demonstrate the diverse requirements that a well designed FSS must meet. It draws on interviews with forecasters and observations of the forecasting process that were carried out in three UK food and drink companies. Where appropriate, information from published questionnaire-based studies is also used.

## 2.1. Nature of information available

Data that will be relevant to forecasting come from a wide variety of sources and the FSS needs to provide easy access to these different sources. The types of data include:

i) time series data at various levels of aggregation (e.g. past sales by product group, individual product, pack size, country, individual customer, quarter, month or week). Often the series need to be cleaned to remove the effects of past special events which might otherwise distort statistical extrapolations. This data cleaning is usually carried out judgmentally. A wide variety of characteristics may be observed in these cleaned series, ranging from white noise to trended and seasonal patterns and there is also likely to be significant variation in the levels of noise associated with different series.

ii) information on customers’ activities such as price promotions and delisting of products.

iii) information on other relevant variables, such a weather forecasts, the timing of major sporting events and competitors’ activities and sales.

iv) forecasts made in earlier periods—supply chain companies commonly use a rolling forecasting system where earlier forecasts are updated as the forecast period approaches.

v) forecasts—for example, statistical forecasts, forecasts made by accounts managers on the basis of their contacts with customers and forecasts of the effects of price reductions derived from <sup>d</sup>off-line<sup>T</sup> econometric models. This means that different forecasts often have to be reconciled within the FSS.

vi) information on errors associated with past forecasts which can provide feedback to the forecasters.

## 2.2. The task

The actual forecasting task will involve two main stages. The first involves the derivation of the statistical (model-based) forecasts. Depending on the FSS, this will either be done automatically (with algorithms being used to estimate the optimal forecasting method and its associated parameter values) or the user will choose the forecasting method and, possibly, the parameter values. The second stage involves judgmental adjustment of the statistical forecasts to take into account special factors and other available information. The outcome of this second stage is a set of final forecasts that are then used to plan supply chain operations.

In many supply chain companies a large number of forecasts need to be made at frequent intervals, (e.g. the requirement to make forecasts for over 10,000 products is common, [9]). The scale of the problem, with forecasts often needed weekly, and sometimes daily, ensures that much of the task has to be automated, and the time available for the application of management judgment may be severely restricted.

## 2.3. Nature of forecasters

Many FSS users have received little or no formal training in statistical forecasting methods, though they may have several year’s experience of producing forecasts [10]. In some organisations FSSs are used by groups of managers who meet to review its model based forecasts and agree on any judgmental interventions. This means that the FSS has to be able to present output which can be assimilated easily from a screen and provide speedy and flexible facilities for analysis.

## 3. Ideal versus actual FSS use

We can characterise a typical time series as consisting of three components:

1. Regular patterns or relationships (e.g. trends, seasonality, stable relationships between advertising expenditure and sales);

2. Irregular components arising from foreseeable events like promotions, either transitory or leading to non-reversionary changes in the medium term;

3. Noise—which is unpredictable.

Where there is sufficient data for the quantitative method to identify regular patterns, ideally, the statistical model in the FSS should fully explain them. Irregular, but foreseeable, events should be explainable by the forecaster. The judgmental forecaster is not as accurate as the quantitative forecasting method for the regular component. This limitation arises from the various human information processing inadequacies that have been identified in a wide variety of circumstances, including time series forecasting (see for example [26,38]). However, the quantitative model is unable to accurately forecast the irregular component as, by definition, it includes only those situations where there are inadequate data from which to build a formal model.

There is plenty of evidence that a combination of statistical methods and judgment can lead to more accurate forecasts. For example, Blattberg and Hoch [4] and Lawrence et al. [35] found that a simple average of judgmental and statistical forecasts was more accurate then either type of forecast used on its own. Similarly, when judgmental adjustments are applied to statistical forecasts there is evidence that accuracy will improve if the forecaster has important domain knowledge that was not available to the statistical method [7,12,17,40].

However, there is also much evidence that FSS use in practice is far from ideal. When it comes to making judgmental adjustments to quantitative forecasts provided automatically by the system, a number of problems arise. First judgment is not restricted to its <sup>d</sup>ideal role<sup>T</sup>. People attempt to forecast perceived regularities, when this is unnecessary, and to forecast noise—largely because these two components are usually confused [17,18,22,38,48]. This means that they make unnecessary and damaging adjustments to the quantitative forecasts and are then over-confident in the accuracy of their adjusted forecasts [34]. Often these adjustments are not even made as identifiable and separate judgmental inputs. For example, in two of the case organisations, forecasters adjusted either the parameters of the forecasting method or its components (i.e. estimates of level, trend or seasonal factors) in attempts to improve the method’s forecasts of the underlying time series pattern. This meant that the statistical output of the FSS was already strongly influenced by the forecaster’s judgment, though it had the appearance of having being obtained through an objective process.

When making judgmental adjustments to take into account foreseeable special events, like sales promotions, people ignore the quantitative forecast altogether, even when it offers an accurate prediction of the underlying regular time series pattern [17]. For example, in one of the organisations studied, little attention was paid to the model-based forecasts when a product was being promoted. Moreover, the size of such adjustments is likely to suffer from the widely documented problems resulting from the use of inadequate heuristics and their associated biases [16].

When users have the ability to the choose statistical model with which to produce their forecasts, their choice is often quite poor [37]. Default parameter values or sub-optimal methods are often selected [9] and forecasters attempt to make up for this (unnecessary) shortfall by making large judgmental adjustments to the quantitative forecast. However, these adjustments are a poor substitute for improved quantitative forecasts [19,36].

If the ideal balance between the system’s statistical forecasts and the human inputs could be achieved, there are several reasons why more accurate forecasts would be expected. First, the fact that the quantitative forecasts are better able to filter out the noise [44] means that they will be less likely to identify false underlying signals. In the absence of special conditions, and assuming that there are sufficient past data, they will reliably predict the mean of the probability distribution that notionally underlies the data generation process. Secondly, confining the judgmental forecaster’s attention to the irregular component will also make the best use of the forecaster’s available effort [25]. In addition, if the forecaster’s judgment partially duplicates the role of the model-based forecast, this may mean that the effects of some factors that drive the forecast variable will be double counted [16].

## 4. Designing FSSs to improve effectiveness

How should FSSs be designed to overcome the inefficiencies that have just been identified? The forgoing discussion implies that such systems should have two key objectives: (i) to improve the forecaster’s ability to realise when judgmental intervention is appropriate and (ii) to enable the user to apply accurate judgmental interventions when these are appropriate. The DSS literature (Silver [49]) suggests two broad approaches to design that can be used to bring about these improvements: <sup>d</sup>restrictiveness<sup>T</sup> and <sup>d</sup>decisional guidance<sup>T</sup>. Silver defines restrictiveness as <sup>b</sup>the degree to which, and the manner in which, a DSS limits its users’ decision-making processes to a subset of all possible processes<sup>Q</sup>. For example, a system could exclude facilities for judgmental adjustments of forecasts or, at least, prohibit judgmental adjustment in certain circumstances. Decisional guidance is <sup>b</sup>the degree to which, and the manner in which, a DSS guides its users in constructing and executing decision-making processes by assisting them in choosing and using its operators<sup>Q</sup>. These two approaches are not necessarily mutually exclusive, but a highly restrictive system offers little scope or need for guidance.

This section considers how the concepts of restrictiveness and guidance can potentially be used in FSS design. Areas where further research is needed are also identified.

## 4.1. Using restrictiveness in FSS design

As we have indicated, restrictiveness can determine the manner in which forecasts are obtained by denying the user the opportunity to employ particular processes or requiring that alternative processes are adopted. Restrictiveness may take the form of limiting the character of the display–for example only tabular displays of data may be available so that counterproductive heuristics associated with graphical displays are precluded [23]–or limiting access to particular sets of data (e.g. in many FSSs only the most recent 3 years of time series data are accessible).

Alternatively, restrictiveness can determine the order in which a process is executed or the type of process employed. In forecasting, it may in some circumstances be desirable to deny the user the opportunity to choose the statistical method or to choose its parameter values, particularly where the user is untrained in forecasting [10].

Decomposition is another process that could be required by a system when the user wishes to make a judgmental adjustment. The assumption underlying decomposition is that a set of decomposed judgments are more accurate than a single holistic judgment because the process allows the judgmental task to be broken down into a series of easier tasks (e.g. [8]). For example, separate judgmental adjustments could be made for the effects of the weather, promotions and the behaviour of competitors and these separate judgments subsequently aggregated. An experiment involving Webby’s prototypical FSS, Griffin, showed that forecasters were able to take more information into account and to produce more accurate forecasts when they used decomposition [54]. However, the benefits of decomposition are likely to be highly contingent on the specific nature of the forecasting task and may, in some cases, be negative [19]. Thus <sup>d</sup>absolute<sup>T</sup> restrictiveness can be dangerous if it is wrongly applied. Also, the increased number of judgments required by decomposition may render the FSS unacceptable to potential users.

However, restrictiveness can be administered in more subtle ways. Rather than absolutely requiring or prohibiting particular processes, it can operate by making some processes deliberately easy to use and others more difficult. Research by Payne et al. [46] showed that decision makers seek to balance effort and accuracy considerations. This suggests that FSS designers could manipulate users towards using methods with better expected forecasting performance by making more desirable forecasting strategies less effortful than less desirable strategies. An example is the default provision of optimal parameters when applying exponential smoothing. Todd and Benbasat [52] suggested that the effort associated with the desirable strategy should be very low, perhaps even automated in pointing the user towards the desirable [forecasting] strategy.

At first sight this appears to conflict with research on judgmental forecasting where people presented with automated quantitative forecasts regularly make the effort to judgmentally adjust these forecasts. However, when the effort involved in adjustment is low and is perceived to be associated with an increase in accuracy, this small extra effort is regarded as worthwhile (the adjustment may simply involve using a mouse to click on a graph in order to indicate the revised forecast). Indeed, Goodwin [15] showed how the propensity to make damaging adjustments was reduced by designing an adjustment process that involved only a small amount of extra effort: simply requiring users to request an adjustment led to a significant reduction in damaging adjustments. Requiring users also to click on a list to select the reason for their adjustment led to further reductions. This was achieved without deterring the forecaster from making adjustments when it was clear they were required in order to improve accuracy.

There are a number of ways in which the relative effort associated with the desirable strategy can be made easier in an FSS. These include the following:

a) Providing automated quantitative forecasts, where these are appropriate, and making the judgmental adjustment of these more demanding;

b) Designing easy-to-use facilities that are necessary to obtain the appropriate quantitative forecast Fildes and Beard [9] suggested that these facilities should:

i) allow data series to be adjusted easily for exceptional and missing observations;

ii) enable identification of series by type (e.g., new product, intermittent demand, declining demand);

iii) provide the ability to forecast at both individual item and aggregate levels so common aggregate effects can be driven down the product hierarchy;

iv) include the availability of an experimental module to allow comparison of different methods;

v) allow the database to be split easily to enable models to be evaluated as to their relative <sup>d</sup>real-time<sup>T</sup> performance [defined as the estimation and hold-out (test) data segments in the forecasting literature [11]].

c) Providing menu structures that deliberately encourage users towards the adoption of appropriate strategies [49].

d) Making it easy for the user to identify series where judgmental intervention is likely to be appropriate; a typical example in an FSS is through exception reporting of extreme forecast errors (possibly via tracking signals).

## 4.2. Using decisional guidance in FSS design

Guidance, the second way in which an FSS design can influence users, can be either inadvertent or deliberate [45,49]. Guidance is inadvertent when it leads to unintended consequences. For example, in a forecasting task, [33] it was found that that confidence associated with point forecasts was influenced by several factors including the scale of the graph that was used to display the time series.

The DSS literature discusses two forms of deliberate decisional guidance—guidance that is intentionally built into the system by its designer. The first, informative guidance, provides unbiased and relevant information without suggesting what the user should do, while the second, suggestive guidance, proposes a course of action to the user. For example, informative guidance can be used to inform the user about the relative advantages of different courses of action, to provide a record of past behaviour in circumstances similar to the current one and to present tables, graphs and analyses of data [49]. Suggestive guidance would use such evidence to recommend a particular forecasting model.

Each of these forms of guidance can be employed in three modes. In predefined guidance, suggestions or information displays are prepared and programmed into the system by the designer in advance of its use. Dynamic guidance has no predefined content. Instead, the system learns about the users behaviour and generates suggestions or information that it considers to be appropriate. For example, the system may suggest courses of action that a given user has systematically disregarded. Finally, participative guidance allows users to be involved in the content of the guidance they receive. For example, in the choice of a forecasting method, the system may supply scores to measure the performance of different methods on attributes such as simplicity, robustness, transparency, accuracy and cost. By supplying weights to prioritise these attributes the user enables the system to provide suggestions on the most appropriate method, given his or her objectives [24].

The purpose of guidance is to improve the calibration of the user’s confidence in their chosen course of action. (Calibration refers to the extent to which that confidence equates with the objective accuracy of that act.) For example, in making choices about which quantitative forecasting model to employ and whether judgmentally to adjust the resulting forecasts, FSS users will, at least implicitly, be making assessments of their confidence in the relative accuracy of these alternatives. Poor calibration can be manifested as overconfidence, which can result in the selection of a poor course of action, or under confidence, which may mean that accurate strategies are foregone. Thus, the widely observed tendency of users to make damaging adjustments to quantitative forecasts [17,38] or to overweight their less accurate judgmental forecasts relative to quantitative forecasts [39] can be explained by their overconfidence in the accuracy of their judgment. Overconfidence also partly explains why judgment or judgmental adjustment is the preferred approach to forecasting in many circumstances [30]. If calibration can be improved by offering guidance then perceived accuracy will be closer to true accuracy and therefore, according to Payne et al. [46] user effort will be more appropriately applied and a better choice of strategies should follow.

What roles can informative and suggestive guidance play in designing an FSS and which form of guidance is likely to be the most effective?

## 4.2.1. Informative guidance

In current commercial forecasting software, predefined-informative guidance is dominant. Graphs or tables of time series and the provision of statistical forecasts, together with measures of their past accuracy, are all examples of informative guidance which are likely to be found in any commercial system. Built-in guidance summarising the relative merits of alternative forecasting methods is less common, though some packages use expert systems to choose statistical forecasting methods and provide the user with an account of why a given method was chosen.

One type of informative guidance that is potentially valuable to forecasting is feedback, which can be provided with the intention of fostering learning. Feedback can take a number of forms [2,3] including:

i) simply supplying the user with the latest outcome (e.g. the latest sales figure; outcome feedback),

ii) giving the user information on his or her forecasting accuracy (performance feedback),

iii) informing the user about his or her apparent forecasting strategy (cognitive process feedback), and

iv) giving the user statistical information about the task (e.g. correlations of possible predictor variables with the forecast variable or details of the underlying time series structure; task properties feedback).

Feedback can offer merely informative guidance when it is does not include an evaluative function. Where forecasting approaches are compared, the feedback guidance is suggestive [41].

How effective is informative guidance? The evidence on whether it will improve forecasting is mixed and may be contingent on the mode, presentation and context of the guidance. Informative guidance has been found to be generally effective when applied to decision tasks that were unrelated to forecasting. For example, Singh [50] found that providing a record of the strategies that users had already investigated (memory support) improved decision quality. Montazemi et al. [41] also found that informative guidance was beneficial.

In forecasting, informative guidance (in the form of explanations of the circumstances where particular methods were deemed appropriate) was found to improve decisions in a task involving the selection of a forecasting method [13,45]. However, its use in tasks where the user has to decide whether to make a judgmental adjustment to the statistical forecast has not been widely researched, though one study [17] found circumstances that providing explanations of statistical forecasting methods improved the way that judgment was used. Similarly the effectiveness of providing feedback has yet to be established. In particular, reports of the effectiveness of outcome feedback as a learning aid have been mixed (e.g. see [21,29]). Indeed, there is a possibility that in forecasting it may actually damage performance by drawing attention to the most recent observation (which will contain noise) and thereby accentuating the tendency to overweight this observation in the subsequent forecast. This was the most prominent form of feedback in the companies studied.

Kluger and DeNisi’s [31] preliminary feedback intervention theory suggests that, for feedback to improve learning, it has to help the user to reject erroneous hypotheses. Consistent with this, a large body of psychological research suggests that feedback is most effective in promoting learning when it takes the form of task properties feedback [2] and this result has been found to apply in the forecasting context [47]. Task properties feedback provides statistical information on the task which may contrast with users’ hypotheses and hence leads to a rejection of erroneous hypotheses. However, the relative merits of task properties feedback present a dilemma in the context of an ideal FSS. If we restrict the role of judgment to that of estimating the effect of events for which there is a paucity of statistical data, then by definition, there will be an absence of data to formulate the task properties feedback. More research is therefore needed on the effectiveness of providing performance or cognitive process feedback in a forecasting context.

## 4.2.2. Suggestive guidance

Suggestive guidance can be used to directly suggest courses of action or to give advice. Alternatively, suggestive guidance may be used to challenge the user’s position and assumptions by using a process, referred to by Kasper [27] as dialectic inquiry. The intention is that the user’s calibration will improve as the support system engenders, what Kasper calls, an <sup>d</sup>accurate feeling of knowing<sup>T</sup>.

Suggestive guidance has been found to be effective in improving decision making in studies by Montazemi et al. [41], Singh [50] and Parikh et al. [45]. As indicated earlier, Parikh et al.’s study involved the task of selecting a forecasting method. However, there is much evidence that systems that merely give advice without any supporting explanation lead to miscalibration [27]. This is because they fail to reveal assumptions or encourage alternative views of the problem [20]. As Muir [43] points out, such systems place the user in the difficult position of needing to make changes, when appropriate, to the recommendations of a system which is presumed to be more competent than them. In contrast, suggestive guidance that fosters dialectical inquiry appears likely to improve calibration. This guidance may take the form of the generation of lists of items that challenge or disconfirm the user’s position or include the requirement to provide a justification for one’s course of action [1,32]. These devices have the effect of engaging the user and are therefore likely to encourage deeper and more reflective thinking.

## 4.3. The way forward?

There are major gaps in our knowledge of how systems should be designed to support forecasters in their decisions on when to intervene judgmentally and how to carry out such interventions. However, it is possible to obtain some broad pointers from the literature as to where the most promising avenues for FSS design improvements might lie.

First, guidance is likely to be more productive than restrictiveness. Absolute restrictiveness, where the system is deliberately designed to prohibit the use of particular processes, is dangerous, since the designer is unlikely to be certain that the included processes are the most appropriate to use, especially in a dynamic environment where the underlying conditions of use may change. Highly restrictive systems are likely to be much simpler to use. They will therefore be more acceptable to the many poorly trained users [10] who carry out forecasting in organisations and, hence, are more commercially attractive. However, such restrictiveness may also be associated with impoverished sets of methods, which generate forecasts mechanically and thereby forgo the potential benefits of user engagement. Secondly, restrictiveness, which is based on making some processes deliberately harder to use, is likely to be frustrating to users and is also unlikely to be an attribute that commercial software companies would wish to promote.

In contrast, guidance offers many potential advantages. Flexible systems with many features can be made easier to use, if they incorporate guidance in the choice of methods [49]. This is particularly important because Venkatesh and Davis’ extension of the technology acceptance model (TAM2) [6,53] identified ease of use as a key factor that determine users’ acceptance of IT tools. Guidance also means that forecasts that the user obtains will ultimately be that particular user’s forecasts so that a sense of ownership of the forecasts is sustained. Such forecast will have been derived through a process of partnership between the system and the user and the evidence is that, if the forecaster has a sense of participation in the derivation of forecast, then the forecasts are more likely to be acceptable [37].

Guidance is also likely to be crucial in achieving another key criterion that is required for the acceptance of a system in the TAM2 model: <sup>d</sup>result demonstrability<sup>T</sup>. Result demonstrability is defined as <sup>b</sup>the tangibility of the results of using the innovation<sup>Q</sup> [42]. In an FSS the fundamental determinant of result demonstrability is likely to be the perceived accuracy of the forecasts. This perception will be much more realistic if users understand that that forecast errors consist partly of an irreducible error due to random factors and hence, there is a bound on forecast accuracy. Bunn and Taylor [5] discuss a method that estimates this irreducible uncertainty and therefore provides a benchmark for what the FSS can reasonably be expected to achieve. Also, individual large errors may be rare but they will also be salient [51] and may create the perception that the system is less accurate than it really is. This suggests that it may be wise for the FSS to use guidance to draw the user’s attention to performance over a relative long period, and if possible, to demonstrate its accuracy relative to non-use of the system. Confusion between forecasts, decisions, targets, plans and budgets may also bias users’ perceptions of accuracy, so using guidance to convey what the FSS is designed to achieve is crucial [14]. All of this suggests that result demonstrability will be achieved by guidance in the form of clear explanations of forecasts and accuracy measures.

What form of guidance is likely to be best? Singh [50] found that, when used together, informational guidance (in the form of memory support) and suggestive guidance (in the form of strategy support) led to better decisions than either form of guidance used separately. Parikh et al. [45] found that dynamicsuggestive guidance was the best form for forecastingmethod selection decisions, but dynamic-informative guidance led to the most effective user learning because users tended to follow suggestive-guidance without understanding the rationale for the advice. In contrast, informative guidance required users to analyze the information and understand its implications before making the decision.

The evidence just summarised implies that the key to providing successful guidance is to engage users in a process that causes them to reflect on their current view of the problem. Indeed, the presence or absence of user engagement may explain the mixed results that have been reported in attempts to influence users decisions on whether to make judgmental interventions. In Lim and O’Connor’s [38] study users continued to rely on their own judgment despite popup messages such as <sup>b</sup>Please be aware that you are 18.1% LESS ACCURATE than the statistical forecast provided to you<sup>Q</sup>. Such messages place no requirement on the user to actively reflect on their forecasts. In contrast, as discussed earlier, Goodwin [15] found that, when users had to provide reasons for judgmental interventions, they made fewer unnecessary judgmental adjustments without being deterred from making these adjustments when they were appropriate. Engagement is more likely to be facilitated by a dynamic (rather than pre-defined) mixture of informative and suggestive guidance which involves the user in a process of dialectic inquiry. Much more research is needed to develop designs that achieve this within FSSs [27]. In particular, research into the role of participative guidance is at an early stage [24].

## 5. Conclusions

An ideally designed FSS will have the following attributes: (i) it will be acceptable to users, (ii) it will be easy to use, (iii) it will offer a flexible range of appropriate facilities and methods, (iv) it will be viable for commercial software companies to market and (v) it will foster the appropriate mix of judgment and statistical methods. We have argued that restrictiveness will be unlikely to lead to FSSs which allow these attributes to co-exist. It may lead to ease of use, but it would reduce flexibility. In addition, the marketing appeal of packages, is likely to be diminished if features are deliberately excluded or purposely made difficult to use. In contrast, guidance does have the potential to allow an FSS to possess all of these attributes simultaneously. It can overcome the difficulties that users might experience when confronted with a large and flexible array of facilities and hence, ensure user acceptability. It is also likely to be a feature that is highly marketable and it can be designed to encourage forecasters to direct their judgment to appropriate aspects of the task. To date, however, no commercial package has been developed for use in supply chain forecasting that meets the specifications we have suggested. Those we have observed fall far short of the highly flexible and multifaceted support systems that we envisage. Thus, the development of commercially attractive and effective forecasting software appears to offer many opportunities and challenges for DSS researchers in the future.

However, DSS researchers, in general, may also learn by applying their ideas to the supply chain forecasting task. It is a quintessential semi-structured problem involving the integration of hard and soft information from multiple sources and clear roles for the application of models and judgment. The core problem is easily defined and relatively homogenous across organisations, and there is a large community of FSS users. There is scope for rapid and frequent testing of the effectiveness of different FSS designs by comparing output with actual outcomes (rather than the, say, the unknown preferences of a decision maker in a multi-attribute decision task). This testing can be carried out simultaneously over a wide range of different series. Moreover, there is the challenge of a largely non-technical population of users operating within a demanding and potentially sceptical environment.

Studies of this forecasting task have already yielded insights into the propensity of support system users to over rely on judgment and the failure of certain forms of guidance to curb this tendency. They have demonstrated the benefits that can be obtained if users develop a sense of ownership of the output of a support system and they have enabled the role of explanations in the choice of appropriate models to be investigated. In addition, the repetitive nature of the task has allowed the relative merits of different types of feedback to be assessed, while our understanding of the value of the decomposition of judgment–a fundamental principle of support methods like deci sion analysis–has been enhanced by studies in this area.

## Acknowledgements

The authors would like to thank Hans Levenbach and Marcus O’Connor for their valuable comments on earlier drafts of this paper. The work was part funded by EPSRC research grants GR/60181/01 and GR/60198/01.

## References

[1] H.R. Arkes, C. Christensen, C. Lai, C. Blumer, Two methods of reducing overconfidence, Organizational Behavior and Human Decision Processes 39 (1987) 133–144.

[2] W.K. Balzer, M.E. Doherty, R. O’Connor, Effects of cognitive feedback on performance, Psychological Bulletin 106 (1989) 410–433.

[3] P.G. Benson, D. O<sup>¨</sup> nkal, The effects of feedback and training on the performance of probability forecasters, International Journal of Forecasting 8 (1992) 559– 573.

[4] R.C. Blattberg, S.J. Hoch, Database models and managerial intuition: 50% model +50% manager, Management Science 36 (1990) 887–899.

[5] D.W. Bunn, J.W. Taylor, Setting accuracy targets for shortterm judgmental forecasts, International Journal of Forecasting 17 (2001) 159–169.

[6] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (1989) 319–340.

[7] M.R. Donihue, Evaluating the role judgment plays in forecast accuracy, Journal of Forecasting 12 (1993) 81 – 92.

[8] R. Edmundson, Decomposition: a strategy for judgemental forecasting, Journal of Forecasting 9 (1990) 305 – 314.

[9] R. Fildes, C. Beard, Forecasting systems for production and inventory control, International Journal of Operations and Production Management 12 (1992) 4– 27.

[10] R. Fildes, R. Hastings, The organisation and improvement of market forecasting, Journal of the Operational Research Society 45 (1994) 1– 16.

[11] R. Fildes, J.K. Ord, Forecasting competitions—their role in improving forecasting practice and research, in: M. Clements, D. Hendry (Eds.), A Companion to Economic Forecasting, Blackwell, Oxford, 2002, Ch. 15.

[12] R. Fildes, H. Stekler, The state of macroeconomic forecasting, Journal of Macroeconomics 24 (2002) 435–468.

[13] M.S. Gonul, D. O<sup>¨</sup> nkal, M. Lawrence, Effects of structural characteristics of explanations on use of a DSS. Decision Support Systems (provisionally accepted).

[14] P. Goodwin, Enhancing judgmental sales forecasting: the role of laboratory research, in: G. Wright, P. Goodwin (Eds.), Forecasting with Judgment, Wiley, Chichester, 1998, Ch. 4.

[15] P. Goodwin, Improving the voluntary integration of statistical forecasts and judgment, International Journal of Forecasting 16 (2000) 85– 99.

[16] P. Goodwin, Integrating management judgment with statistical methods to improve short-term forecasts, Omega: International Journal of Management Science 30 (2002) 127– 135.

[17] P. Goodwin, R. Fildes, Judgmental forecasts of time series affected by special events: does providing a statistical forecast improve accuracy? Journal of Behavioral Decision Making 12 (1999) 37–53.

[18] P. Goodwin, G. Wright, Improving judgmental time series forecasting: a review of the guidance provided by research, International Journal of Forecasting 9 (1993) 147 – 161.

[19] P. Goodwin, R. Fildes, M. Lawrence, Tracing the process of using a forecasting support system, Twenty-First International Symposium on Forecasting, Atlanta, 2001.

[20] S. Gregor, I. Benbasat, Explanations from intelligent systems: theoretical foundations and implications for practice, MIS Quarterly 23 (4) (1999) 497– 530.

[21] K.R. Hammond, D.A. Summers, D.H. Deane, Negative effects of outcome-feedback in multiple-cue probability learning, Organizational Behavior and Human Performance 9 (1973) 30– 34.

[22] N. Harvey, Why are judgments less consistent in less predictable task situations? Organizational Behavior and Human Decision Processes 63 (1995) 247– 263.

[23] N. Harvey, F. Bolger, Graphs versus tables: effects of data presentation format in judgmental forecasting, International Journal of Forecasting 12 (1996) 119– 137.

[24] J.J. Jiang, G. Klein, Side effects of decision guidance in decision support systems, Interacting with Computers 12 (2000) 469–481.

[25] D.R. Jones, D. Brown, The division of labor between human and computer in the presence of decision support system advice, Decision Support Systems 33 (2002) 375– 388.

[26] D. Kahneman, A. Tversky, Choices, Values and Frames, Cambridge University Press, Cambridget, 2000.

[27] G.M. Kasper, A theory of decision support system design for user calibration, Information Systems Research 7 (1996) 215– 232.

[28] P.G.W. Keen, M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, 1978.

[29] G. Keren, Facing uncertainty in the game of bridge: a calibration study, Organizational Behavior and Human Decision Processes 39 (1987) 98– 114.

[30] B. Kleinmuntz, Why we still use our heads instead of formulas: toward an integrative approach, Psychological Bulletin 107 (1990) 296– 310.

[31] A.N. Kluger, A. DeNisi, The effects of feedback interventions on performance: a historical review, a meta-analysis and a preliminary feedback intervention theory, Psychological Bulletin 119 (1996) 254–284.

[32] A. Koriat, S. Lichtenstein, B. Fischhoff, Reasons for confidence, Journal of Experimental Psychology. Human Learning and Memory 6 (1980) 107– 118.

[33] M. Lawrence, M. O’Connor, Scale, randomness and the calibration of judgemental confidence intervals, Organizational Behavior and Human Decision Processes 56 (1993) 441–458.

[34] M.J. Lawrence, W. Sim, Prototyping a financial DSS, Omega 27 (1999) 445–450.

[35] M.J. Lawrence, R.H. Edmundson, M.J. O’Connor, The accuracy of combining judgemental and statistical forecasts, Management Science 32 (1986) 1521– 1532.

[36] M. Lawrence, L. Davies, M. O’Connor, P. Goodwin, Influence of explanations and affect on DSS use and decision accuracy, International Symposium on Forecasting Dublin, 2002.

[37] M. Lawrence, P. Goodwin, R. Fildes, Influence of user participation on DSS use and decision accuracy, Omega 30 (2002) 381– 392.

[38] J.S. Lim, M. O’Connor, Judgemental adjustment of initial forecasts: its effectiveness and biases, Journal of Behavioral Decision Making 8 (1995) 149– 168.

[39] J.S. Lim, M. O’Connor, Judgmental forecasting with interactive forecasting support systems, Decision Support Systems 16 (1996) 339–357.

[40] B.P. Mathews, A. Diamantopoulos, Judgemental revision of sales forecasts: effectiveness of forecast selection, Journal of Forecasting 9 (1990) 407– 415.

[41] A.R. Montazemi, F. Wang, S.M.K. Nainar, C.K. Bart, On the effectiveness of decisional guidance, Decision Support Systems 18 (1996) 181– 198

[42] G.C. Moore, I. Benbasat, Development of an instrument to measure the perceptions of adopting an information technology innovation, Information Systems Research 2 (1991) 192– 222.

[43] B.M. Muir, Trust between humans and machines, and the design of decision aids, International Journal of Man–Machine Studies 27 (1987) 527– 539.

[44] M. O’Connor, W. Remus, K. Griggs, Judgemental forecasting in times of change, International Journal of Forecasting 9 (1993) 163–172.

[45] M. Parikh, B. Fazlollahi, S. Verma, The effectiveness of decisional guidance: an empirical evaluation, Decision Sciences 32 (2001) 303– 329.

[46] J.W. Payne, J.R. Bettman, E.J. Johnson, The Adaptive Decision Maker, Cambridge University Press, Cambridge, 1993.

[47] W. Remus, M. O’Connor, K. Griggs, Does feedback improve the accuracy of recurrent judgemental forecasts? Organizational Behavior and Human Decision Processes 66 (1996) 22–30.

[48] N. Sanders, L. Ritzman, Judgmental adjustments of statistical forecasts, in: J.S. Armstrong (Ed.), Principles of Forecasting: A Handbook for Researchers and Practitioners, Kluwer Academic Publishers, Norwell, MA, 2001, Ch. 13.

[49] M.S. Silver, Decisional guidance for computer-based support, MIS Quarterly 15 (1991) 105– 133.

[50] D.T. Singh, Incorporating cognitive aids into decision support systems: the case of the strategy execution process, Decision Support Systems 24 (1998) 145– 163.

[51] P.F. Taylor, M.E. Thomas, Short term forecasting: horses for courses, Journal of the Operational Research Society 33 (1982) 685–694.

[52] P. Todd, I. Benbasat, Evaluating the impact of DSS, cognitive effort, and incentives on strategy selection, Information Systems Research 10 (1999) 356– 374.

[53] V. Venkatesh, F.D. Davis, A theoretical extension of the technology acceptance model: four longitudinal field studies, Management Science 46 (2000) 186– 204.

[54] R. Webby, M. O’Connor, M. Lawrence, Judgmental timeseries forecasting using domain knowledge, in: J.S. Armstrong (Ed.), Principles of Forecasting: A Handbook for Researchers and Practitioners, Kluwer Academic Publishers, Boston, 2001, Ch. 13.

![](/api/attachments/HD8EQ5CS/fulltext/images/b47c5a99ed68673a809132c282eab6834ec65cbfc05f26f2a83781a51730ce6a.jpg)

Robert Fildes is Professor of Management Science in the School of Management, Lancaster University and Director of the Lancaster Centre for Forecasting. He has a mathematics degree from Oxford and a Ph.D. from the University of California in Statistics. He was co-founder in 1981 of the Journal of Forecasting and in l985 of the International Journal of Forecasting. For ten years from l988 he was Editor-in-Chief of the IJF. He was president of the Interna-

tional Institute of Forecasters between 2000 and 2004. His research interests are concerned with the comparative evaluation of different forecasting methods, the implementation of improved forecasting procedures in organizations and the design of forecasting systems.

![](/api/attachments/HD8EQ5CS/fulltext/images/b8a9e65bc38e687f40a70052e43adebef22915062864cefbd0f91e93facd9c8f.jpg)

Paul Goodwin is Senior Lecturer in Management Science in the Management School at the University of Bath. He has a degree in Economics from the University of Liverpool, a Masters degree in Management Science from the University of Warwick and a PhD in Management Science from Lancaster University. His research interests concern the role of management judgment in forecasting and decision making. He is an Associate Editor

of the International Journal of Forecasting, and three other international journals and he is a Director of the International Institute of Forecasters.

![](/api/attachments/HD8EQ5CS/fulltext/images/fab9598a304c97d27184db935752b869e2fcfeb734075e459ab8b0acb72b694a.jpg)

Michael Lawrence is Emeritus Professor of Information Systems at the University of New South Wales, Sydney, Australia and Visiting Professor at the University of Lancaster. He holds a PhD in Operations Research from the University of California, Berkeley and undergraduate degrees from the University of Sydney. His research interests are in the support of management decision making where significant management judgement needs to be coupled with

computer-based advice. As forecasting is such a decision domain, he has focused on the incorporation of judgement and computer advice in forecasting. He has been President of the International Institute of Forecasters, Editor of the International Journal of Forecasting and is Emeritus Associate Editor of Omega.
