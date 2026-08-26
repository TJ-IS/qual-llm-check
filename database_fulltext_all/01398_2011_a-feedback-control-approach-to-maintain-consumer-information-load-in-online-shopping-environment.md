---
otero_id: 1398
otero_key: "JZU6JCUE"
title: "A feedback control approach to maintain consumer information load in online shopping environments"
authors: "Anjala S. Krishen; Robyn L. Raschke; Pushkin Kachroo"
year: "2011"
journal: "Information & Management"
doi: "10.1016/j.im.2011.09.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A feedback control approach to maintain consumer information load in online shopping environments

Anjala S. Krishen <sup>a,</sup>\*, Robyn L. Raschke <sup>b</sup>, Pushkin Kachroo <sup>c</sup>

<sup>a</sup> Department of Marketing, University of Nevada Las Vegas, 4505 Maryland Parkway, Las Vegas, NV 89154-6010, United States

<sup>b</sup> Department of Accounting, University of Nevada Las Vegas, Las Vegas, NV 89154, United States

<sup>c</sup> Department of Electrical and Computer Engineering, University of Nevada Las Vegas, Las Vegas, NV 89154, United States

## A R T I C L E I N F O

Article history: Received 17 February 2009 Received in revised form 19 May 2011 Accepted 14 August 2011 Available online 12 September 2011

Keywords: Feedback control Information load Adaptive DSS Consumer decision-making Consumer choice e-Commerce adaptive systems

## A B S T R A C T

The heterogeneity of e-commerce users requires online shopping environments to advance from a simple framework to one that is adaptive. This need results from the negative consequences of user frustration due to information load. We used a feedback control theory based approach to address the online consumer information overload issue in an adaptive manner. To demonstrate the efficacy of this feedback control approach, a design science method evaluated the feedback controller. The main effect was that the dynamic adaptivity did not have to rely on summarizing data for inference to the individual. The proposed feedback control design is therefore a robust and viable option for organizations to incorporate into their online shopping environments to accommodate user variation of information load for e-commerce adaptivity.

\- 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

We used a feedback control model to maintain a reasonable consumer information load in the context of online shopping. The negative impact of increased information overload in such environments affects consumer emotions and shopping behavior, as well as decision quality [12]. However, information overload varies from person to person. To accommodate such variation, online shopping websites are moving from a simple, single model to one of adaptivity.

The issue of increased information load remains problematic as users of online shopping websites search for products and often receive an overwhelming number of possible product variations. Information overload occurs when too much information is provided, leading to increased frustration and stress. For example, when attempting to purchase a computer at a computer e-commerce website, the customer may be presented with a list of over 900 possible configurations. A large list of product options requires longer to absorb and can be overwhelming, leading to buyer frustration and sub-optimal decision making [9].

Prior research has examined information overload issues in the context of decision support tools that adapt to the user. Such adaptive decision support tools provide search and navigation, presentation, recommendations, and the use of agents [15,16]. Adaptive search tools improve navigability while adaptive presentation tools improve content understanding. Recommenda tion agents are another means of adapting to the user; they may provide content links or suggest alternative products.

Although beneficial, these tools have limitations; they require prior data input from each individual (i.e. answering questions on his or her preferences). While adaptive tools may relieve the effects of information overload, they are not a panacea. Furthermore, information filtering does not consider differences between individuals. We followed a design science method [4] of building and evaluating a feedback controller for online shopping websites as a means to address this issue.

The appeal of feedback control within an e-commerce shopping environment is that it is adaptable to the individual and does not require a request for direct user input. The feedback control design takes into account the user’s online behavior; using it allows the website to control information load by determining the number of choices to display to the customer. The design notes the time taken to decide for the number of choices provided when the user interacts with the website. Thus, if the first iteration provided too little choice, then the next set of choices would be larger. In this way, the information load is maintained essentially constant. It is beneficial to use dynamic online behavior as an input for controlling information load, as this takes individual differences in information processing abilities into consideration.

We used the design steps of feedback control theory to stabilize the information load and evaluate the efficacy of the feedback controller by developing a simulation of the process. The results showed that the design stabilized information load, and was a viable method for adapting to individual user needs.

## 2. Related work

## 2.1. Adaptive decision support in online shopping environments

From an e-commerce perspective, the goal of adaptivity is to customize product choice to the individual user’s needs, whereas, from a user perspective, an e-commerce website that provides too little or too much information on product choice is likely to be unacceptable. Lack of information is limiting and can lead to the risk of a sub-optimal decision, while too much information can lead to sub-optimal decision making, because the user is overwhelmed and becomes frustrated. Decision support systems provide several ways to approach adaptivity in the hope of providing the right amount of information [5].

Traditional DSS incorporate three components: data, model, and interface; whereas an adaptive DSS integrates an additional component within its architecture, adaptation. Dynamic systems possess the property of adaptive self-modification, whereas all others are classified as static.

We distinguish the multiple approaches to adaptivity from an e-commerce perspective by focusing on two general characteristics: first, ‘‘how past user information is utilized’’ (individual and aggregate information) and second, ‘‘how the choice set is presented’’. The first characteristic is for the purpose of providing the current user with product options, ranging from the aggregate (using information from previous visitors to the website to adapt to the current user), to the individual level. The second characteristic relates to the choice set presented to the user; this ranges from discrete (that contains a finite number of alternatives) to continuous. In terms of e-commerce, a user who intends to purchase a computer may enter ‘computers’ in the search box with the results showing a choice set of all computers that the ecommerce vendor has in stock. This discrete choice set is not adapted in any way to characteristics of the current or previous user purchases.

Prior research on aggregation approaches, including the use of recommendation agents (RA), has shown that they are useful in lowering information load. There are two types of recommenders: content based (using information from past purchases or preferences for new recommendations) and collaborative filtering (based upon user’s ratings of products). The assumption is that users who give similar ratings on the same products have similar tastes.

Aggregate customization is another way of using information in aggregate to create a customized experience for the user. Arora and Huber [1] used aggregate customization of product choice sets. In their study, they expected that choice set information from a small sample of users could be used to create a common customized design for the average user. In addition, Bucklin and Sismeiro [2] used web server log files to create models for predicting user browsing behavior. One drawback of the aggregate models is their inability to account for individual differences from summary data.

Acknowledging the difficulty of capturing user differences with aggregate information, some researchers focused on adaptivity at the individual level. Toubia et al. [14] proposed an alternative approach for choice sets based on a question-design method. Their choice set individually adapts to the user based upon previously answered questions. Other researchers included the use of algorithms that provided individual adaptivity of user choice sets as well as an application of optimal control theory to determine the optimal choice set available to individuals [10].

## 2.2. Feedback control

For our feedback control solution, we use the real-time online behavior of the user and do not require specific input. Thus, the user’s online behavior becomes the system input that determines the desired output (e.g. number of choices). Utilizing a user’s online behavior takes into consideration his or her information processing ability and the differences between individuals when shopping online. From the perspective of real-time adaptivity, feedback control is common in engineering, control, operations, and transportation disciplines. Recent research, however, has expanded feedback control theory to a larger number of application areas.

Since uncertainties or disturbances exist within any real system, the objective of the design is to control the output. For our purposes, the feedback controller designed for online shopping environments controls the load by manipulating the number of choices displayed to the individual. Control systems can either be open or closed loop. An open loop system does not take into account real-time information about how the system is performing. A closed loop system however, incorporates the feedback of the system output to change the input to obtain the desired output.

Feedback control theory is based on a mathematical model of the system that is to be controlled. This model is used to develop a mathematical model that provides the desirable closed loop properties of the system. A nominal model is created because the parameters of the model are not precisely known. The mathematical model, however, is generally robust because of the (negative) feedback nature of the system.

Performance criteria derived from the fundamentals of control theory have been developed and used to evaluate the feedback controller under various information load conditions. The criteria are stability, settling time, steady state error, and robustness. For our feedback controller, a stable system means that the information load is bounded by having a large enough choice set to satisfy the number of choices computed by the feedback controller. Settling time is the time taken to converge to the desired information load and achieve steady state. Steady state error is the difference between the desired and the actual information load. Lastly, the feedback controller performance is evaluated by its robustness; that it performs well in spite of uncertainties or disturbances.

One advantage of a feedback control design is that the model of the system to be controlled does not have to be exact, but it should contain its essential dynamic features. Any mismatch between the model and the actual system is normally handled by the robustness of the feedback controller. The ability of feedback controllers to handle uncertainty is powerful and useful. Indeed, even if we do not know the exact model of a system to be controlled or if the model is complex, it is still worth utilizing a simplified version of the model.

## 2.3. Information load

For an online shopping site, a feedback control approach can adapt to individual differences by noting the individual’s information load and comparing it to the desired load predetermined by the e-commerce vendor, to control the number of choices that are sent to the customer. For our purposes, information load was defined as the number of choices presented over a given period of time. Individual differences occur, creating varied thresholds of information load. For example, one person may be able to review three product options in a minute while someone else can only review one. The ability to control the individual’s information load is thus a way to control individual users and reduce issues of increased information load (overload). In addition, by placing the feedback control design at the online shopping website, the information load is maintained in the context of the specific products of interest to the consumer. A feedback control design using the online behavior of the individual’s information load within each context thus provides a viable means of adapting to an individual’s needs.

Chen et al. [3] found that experienced online consumers processed information more efficiently and effectively with less perceived information load than novice online consumers. In addition, Huang [6] examined the effect of information load on a consumer’s behavior through his or her desire to continue shopping versus her/his desire to avoid the online website and found that information load affected his or her emotions which, in turn, influenced the decision to further use the site. Thus, she suggested that e-tailers should maintain information load at levels that can stimulate or elicit pleasure.

## 3. Model development and structure

Fig. 1 shows the steps in designing and evaluating the feedback controller; the variable being controlled was information load. First, we developed a simulated e-commerce website. Second, we designed the feedback controller by analyzing user log data from a study that employed a price/quality algorithm to determine the choice set presented to participants per iteration [11]. Subjective measures of satisfaction, task confidence, attention to choice stimulus, and frustration were obtained from a survey of our participants to determine whether the anticipated increased information load conditions had occurred. Manipulation checks indicated that increased information load conditions did occur. The algorithm employed was based on simple feedback heuristics and did not follow any mathematical modeling that would guarantee system performance. This algorithm was tested as a proof of concept to observe the effect of information load-based feedback on the users. The user log data was analyzed from experimental data that used a simulated e-commerce shopping environment within the task of purchasing a computer under various information load conditions.

We intended to examine the efficacy of a feedback control design created to maintain information loads at an individual level. Analyzing the user log data from a study that simulated an ecommerce shopping environment was ideal, because the user log contained data on the time taken over the number of choices presented per iteration for all participants. Different load conditions were provided in the user log data and it thus gave sufficient input so that the system dynamics could be estimated from the corresponding information load.

Once the feedback control law had been developed, the feedback control model was evaluated. The feedback control model was intended to maintain the desired set point and reach stability. In our case, the information load at the individual level was required to be at a set point that was not too high (where the individual might encounter information overload) or too low (when the individual may lose interest). When the feedback controller was found to be stable, we evaluated the performance for its efficiency (settling time), accuracy (steady state error), and robustness.

Fig. 2 shows the feedback control block diagram. Information load was calculated by dividing the number of choices a user was presented at a given time by how much time the user took to make a selection from the list. The goal of the controller was to maintain a desired information load level. Though there are many disturbances that can affect how many choices a user can process in a given time, an adequately performing control system is able to maintain the desired load by controlling the number of choices presented to the individual. Since low and high levels of information load have negative effects, a mid-value of information load was used as a way to evaluate the effectiveness of the feedback controller. After the information load is known (website users abandon the shopping cart when the information load is >0.8 or <0.2), the feedback control law calculates how many choices should be shown in a list to a user based on how much time the user took to process the previous list.

Feedback control based on the nominal model is generally robust to uncertainties. We utilize this fact in our design of a feedback controller for online shopping. The purpose of the nominal model is to imitate the behavior observed from the user data collected from the simulated online shopping website. Based on this behavior, our model structure follows the law of diminishing returns. More specifically, feedback control designs have been used in traffic control [7], game theory [8], and vehicle control [13], etc.

![](/api/attachments/JZU6JCUE/fulltext/images/8ddd7e828393044b3d40298605e7d3dc1c951a5ffa61d53d51f7847eccaa9d45.jpg)  
Fig. 1. Step-by-step study procedure.

![](/api/attachments/JZU6JCUE/fulltext/images/257ba904a046f981810d96802da1b637bc600222a021fb3a3ddb31593e575521.jpg)  
Fig. 2. Feedback control architecture block diagram.

Thus, we propose the following nominal model, which most closely represents the shape of the polynomial when number of choices, u(t), is plotted against information load x(t) from the user log data:

$$
\frac {d x (t)}{d t} = a (1) + a (2) x (t) + \frac {a (3) u (t)}{1 + a ^ {2} (4) u ^ {2} (t)}\tag{1}
$$

Here, x(t) is the information load at time t, and u(t), the input variable, is the corresponding number of choices. There are four constants: a(1), a(2), a(3), and a(4). A more physically representative model would use a discrete event system or a hybrid model but we believe that an ordinary differential model was adequate for our design. We also chose the control variable to be real valued in design, but we used the closest integer value for implementation. Further details for our model structure are given in Appendices A and B.

## 4. Evaluation of the efficacy of the feedback controller

Although online user log data was used to create the feedback controller, evaluation of the efficacy of the design is needed to ensure rigor from a design science perspective. Performance criteria were used to examine the efficacy of the feedback controller. Thus, our process was iterative. Each step increased the evaluation rigor of the feedback controller. If it did not perform as intended, there was no need to continue with the evaluation. Our evaluation thus consisted of the following iterative steps: first, we determined how the feedback controller performed using an iterative nonlinear least squares estimation to establish stability, efficiency, and accuracy; second, we added a stochastic disturbance to evaluate robustness for these same performance criteria;

third, we adjusted the feedback controller to see how well it performed in stabilizing the system after accounting for bias adjustments from uncontrolled disturbances (gain); and fourth, we performed simulations to evaluate the feedback controller under varied initial information load scenarios.

Our first evaluation of the feedback controller used the model from which we obtained the parameters using the iterative nonlinear least squares estimation scheme. This model had the number of choices shown as the control variable and the information load as the state variable. For some initial value of the state variable, the feedback controller was designed to determine the set of choices to present to the user in the simulation. The results of the simulations are shown in Fig. 3, Panel A. The plots in this figure show the evolution of the system when we applied the control law (Appendix B), which was given in terms of another variable v(t) which we termed the pseudocontrol.

The pseudocontrol was derived for the desired mid-range rate of information of 0.5, a value which was arbitrarily chosen to evaluate our model. We designed for a closed loop system, since the control law that was applied at any given time depended on the actual information load of the system that was being measured, and the input to the system made it evolve towards the desired information load.

The simulations in the first step of the evaluation process show how the information load and the pseudocontrol evolved in time when we used the feedback controller. The simulation results validated the feedback controller by showing that, after some transients, a given fixed desired information load (0.5) was tracked by the system for two different initial conditions of information load.

## 4.1. Evaluation of the feedback controller with stochastic dynamics

Our second evaluation was to consider how well the feedback controller performed when the model was converted into a stochastic model by introducing a stochastic disturbance into the input. Within the context of an online shopping environment, these uncontrolled disturbances can be computer, communications, or human related. We used a uniformly distributed disturbance between 0 and 1 with a corresponding gain term. The stochastic term was used to account for random behavior of users that can be expected beyond nominal behavior.

![](/api/attachments/JZU6JCUE/fulltext/images/71f614fab7790afce3ae1854d7852a6b0818c7cb96a06d2c79b94029822438f3.jpg)  
Panel A: Feedback controller simulation results

![](/api/attachments/JZU6JCUE/fulltext/images/e674250d1e40795bc65a2013ab73eb64ad1026df6ce33ef410d2ed3aebfd021f.jpg)

![](/api/attachments/JZU6JCUE/fulltext/images/fa8e803a6895269fa8832617acc9c386ff3d591b64c8ec897cd8ba47f87dce49.jpg)

![](/api/attachments/JZU6JCUE/fulltext/images/17d02e2179b7692141e7fb463db66caadf80f6db47450984120d6f627e16f143.jpg)

Panel B: Feedback controller with introduction of controlled disturbance  
![](/api/attachments/JZU6JCUE/fulltext/images/f5bfa8855829115dcf41e2d70d8ac31a7db73f13560de51aaa310c3641d96434.jpg)

![](/api/attachments/JZU6JCUE/fulltext/images/783229ac2626283e19bd903d6c4fd5f99bf0b1198c30579a98ceceaab4e76c88.jpg)

Panel C: Feedback controller with uncontrolled disturbance and gain bias of 5  
![](/api/attachments/JZU6JCUE/fulltext/images/ddfb624b8656f3d6d3bc99b623df420f70cba5b6cf2cd7d959365fd8f914d0b6.jpg)

![](/api/attachments/JZU6JCUE/fulltext/images/84d973d69c35ad8b530ae9ab331e5cc2dd36c7c76eda531c77febf2aa67ae4db.jpg)  
Panel D: Feedback controller with uncontrolled disturbance and gain bias of 20  
Fig. 3. Feedback controller simulation results under various conditions.

The addition of stochastic noise to the dynamics transforms the ordinary differential equation model of the system into a stochastic differential equation model:

$$
d X _ {t} = \left[ a (1) + a (2) X _ {t} + \frac {a (3) u (t)}{1 + a ^ {2} (4) u ^ {2} (t)} \right] d t + b d W _ {t}\tag{2}
$$

Here, the deterministic state variable has been replaced by its counterpart, a random process. With stochastic disturbance included in the simulation, we obtain the information load tracking for two different initial conditions as shown in Fig. 3, Panel B. In this condition, we used the same control law but added noise into the system dynamics (2), and observed that the closed system performance was encouraging. Here we saw that the feedback controller responded and maintained a steady state with the introduction of uncontrolled disturbances. For the same disturbance, the pseudocontrol is shown on the right at Panel B.

One difference in the result when we used stochastic dynamics was that there was a bias in the information load that the system was able to track. Because uncontrolled disturbances affected the system and there was not a 1 to 1 linear relationship between the actual and the desired information load, an adjustment was required to tune the controller (its gain bias). By tuning the feedback controller, it was assumed that the controller would display stability and exemplify accuracy in order to control and deal with the uncontrolled disturbances. Understanding the behavior of this gain bias will help us further adjust the feedback controller to a steady state mode and stabilize the feedback controller to our intended information load target.

Table 1  
Monte Carlo simulation parameter settings.

<table><tr><td>Parameters</td><td>Settings</td></tr><tr><td>Initial time</td><td>0</td></tr><tr><td>Final time</td><td>5</td></tr><tr><td>Time increment</td><td>0.05</td></tr><tr><td>Initial information load</td><td>Low/high</td></tr><tr><td>Desired information load</td><td>0.5</td></tr><tr><td>Simulation runs</td><td>50</td></tr><tr><td>Plotted runs</td><td>5</td></tr></table>

There are many ways that the control design can be changed to remedy the problem of steady state error that emerges when we use stochastic dynamics. One method would be to just increase the feedback control gain in our formula; for example, compare the plots in Fig. 3, Panel C with those in Panel D; the control law used in the closed loop system for Panel C had a gain equal to five, whereas the one for Panel D had a gain of twenty. It is clear that the performance improved in this case, as the output stabilized more rapidly in Panel D. These results show that the feedback controller can achieve a steady state with the high gain bias and thus demonstrate a high level of accuracy of the controller.

Another way to improve the performance is by modifying the control law to be:

Table 2  
Means (standard deviation) of the simulation results.

<table><tr><td rowspan="2">Time (t)</td><td colspan="2">Information load</td><td colspan="2">Mean # of choices</td></tr><tr><td>Low condition</td><td>High condition</td><td>Low condition</td><td>High condition</td></tr><tr><td>t=1</td><td>.500 (.001)</td><td>.500 (.001)</td><td>1.80 (.535)</td><td>1.92 (.601)</td></tr><tr><td>t=2</td><td>.500 (.001)</td><td>.500 (.001)</td><td>1.80 (.534)</td><td>2.00 (.606)</td></tr><tr><td>t=3</td><td>.500 (.014)</td><td>.500 (.001)</td><td>1.82 (.596)</td><td>1.92 (.665)</td></tr><tr><td>t=4</td><td>.500 (.001)</td><td>.500 (.001)</td><td>1.88 (.594)</td><td>1.98 (.589)</td></tr><tr><td>t=5</td><td>.500 (.001)</td><td>.500 (.002)</td><td>1.74 (.600)</td><td>1.94 (.712)</td></tr></table>

In this, the term L is added to the control law to counter the bias in the performance.

## 4.2. Sensitivity analysis

Finally, we performed simulations to show how the feedback controller performed under low and high initial information load conditions. We performed repeated runs of the stochastic system for both conditions. Because our desired information rate was 0.50 for the feedback controller, the low initial information load condition was less than 0.50 while the high initial information load condition was greater than 0.50. The parameters and their corresponding settings are shown in Table 1.

The results of the simulation for both the low and high information load conditions indicated that the feedback controller was performing as intended. Results of the simulation are shown in Table 2 with plots of five sample runs for both conditions shown in Fig. 4.

The results from the simulations are encouraging as the overall performance of the feedback controller maintained the information load at the desired reference point of 0.50. Our simulations imitated the varied nature of online users’ information loads while interacting with an e-commerce site. Our simulations showed that the controlled system was stable for multiple input conditions and

$$
v (t) = - [ a (1) + a (2) (x _ {d} - L) ] - [ a (2) + k ] [ e (t) + L ]\tag{3}
$$

![](/api/attachments/JZU6JCUE/fulltext/images/49bca75618a0182f5ea87c46820bc66d9cc92819169291f67dbf4cfb410181dd.jpg)

![](/api/attachments/JZU6JCUE/fulltext/images/bf9d738ae36bbd55aef645c00fefc8b5e4dfb49dbc151826a53a216ac5db4873.jpg)  
Panel A: Monte Carlo Simulation results under Low Information Condition

![](/api/attachments/JZU6JCUE/fulltext/images/ecfe480ac525966ab9e5c5842b3e9898f50780cba86aafc8ccdc9ffba0e59e18.jpg)

![](/api/attachments/JZU6JCUE/fulltext/images/94922c0fc94fbb400f636215dae85fb3c27a6b985a029c60f7f837ec226018b0.jpg)  
Panel B: Monte Carlo Simulation results under High Information Condition  
Fig. 4. Sensitivity analysis under low and high information rate conditions.

regulated to our desired reference point. This indicated that our feedback controller was a means of adapting to the individual and did not require direct input from the user.

## 5. Discussion and implications

The feedback control design used a deterministic framework which modeled the time evolution of the system. We used feedback control to determine the number of choices and addressed the problem of information load. We used time explicitly as a variable in our model because we took a derivative of information with respect to time.

We used real customer data to obtain the values of the parameters of our model and to validate it. We derived a feedback control law that guaranteed a desirable closed loop performance of the overall system. The control variable, the number of choices to be presented to the user, was then computed as a simple function of information rate. Other modeling methodologies have been employed, but most of them are either designed using heuristics, common sense approaches, or based on static models with or without optimization methods. Because our feedback control model is dynamic, our design is valuable because: (1) the number of computations to be performed is very small; (2) this number does not change at every step; and (3) no optimization algorithms have to be executed at every step. Although we are using a deterministic model, feedback control provides a solution that is robust to system uncertainties.

Feedback control allows the system to make decisions in realtime, based on how the system is actually running. Thecontrol action is not pre-determined, but is a response to how the system is behaving at that time. As the goal of the feedback controller is to minimize the error between the desired and the actual information load, the server checks the amount of time to click (Output) and the feedback controller calculates the number of choices (Control Input) to be shown in the subsequent iteration. Hence, the website is adaptive to the individual and does not need prior information from the user.

There are several important managerial and theoretical implications of our research. Overloaded consumers may simply abandon their transactions and not continue with their purchases. Maintaining arousal and stimulation levels of consumers as they peruse websites is important, given the two-dimensional nature of the transactions [17]. System and information quality management is also an important consideration when designing websites. Our model can help increase the perception of information quality by modifying the number of choices per user. Finally and most importantly, we believe that a feedback control design is an important and fundamental technique to adapt a website to fit the needs and desires of a user in real-time.

Thus, the implications of our findings are that a properly executed e-commerce website can potentially mitigate issues normally experienced with failed transactions.

## 6. Conclusions

There are two main contributions of this study. First, it contributes to adaptive e-commerce research. Our approach is dynamic and does not use responses provided by the individual.

Second, our study focuses on information load as the controller variable: an increase in information load gives the user too much information whereas a decrease gives the user too little; hence an increased information load has negative consequences but too little information load does not challenge or stimulate the user. From an e-commerce perspective, consumers are likely to avoid websites if they incur negative emotional consequences.

However, limitations exist to our study. Log data were used from students participating in a simulated online shopping environment for the specific task of purchasing a computer. Although the use of student subjects is not unusual and it is expected that students primarily purchase computers for use in their studies, we measured information load for only one task.

As individuals’ information loads vary, so too may their stimulation levels. Understanding the interaction of information overload with decisional commitment can help e-commerce managers design their websites and analyze their clickstream data.

## Acknowledgement

The authors thank three anonymous reviewers as well as the I&M editor, Dr. Sibley, for reading and comments of previous versions of this article.

## Appendix A. Parameter estimation of nominal model

$$
\frac {d x (t)}{d t} = a (1) + a (2) x (t) + \frac {a (3) u (t)}{1 + a ^ {2} (4) u ^ {2} (t)}\tag{A.1}
$$

Since the nominal model (A.1) is not linearly parameterized, we use the nonlinear least squares estimator; an iterative scheme, based on the Taylor series expansion, in terms of the unknown parameters. We can rewrite (A.1) in terms of the parameters as follows:

$$
\Delta x (a, t) = f (a, x (t), u (t))\tag{A.2}
$$

where $\Delta x ( a , ~ t )$ approximates the term dx/dt, and is equal to $( x ( t + \delta t ) - x ( t ) ) / \delta t ,$ , and f(a, x(t), u(t)) equals $a ( 1 ) + a ( 2 ) x$ $( t ) + ( a ( 3 ) u ( t ) / ( 1 + a ^ { 2 } ( 4 ) u ^ { 2 } ( t ) ) ) .$

The iterative algorithm for the nonlinear least squares starts with some initial value of the parameters, and then the update is based on the following equation:

$$
\Delta x (a + \Delta a, t) = f (a, x (t), u (t)) + \Delta a \times f ^ {\prime} (a, x (t), u (t))\tag{A.3}
$$

The parameter increment equation is obtained from (A.3) above and is equal to:

$$
\begin{array}{l} \Delta a = ([ f ^ {\prime} (a, x (t)) ] ^ {T} f ^ {\prime} (a, x (t)) ^ {- 1} [ f ^ {\prime} (a, x (t)) ] ^ {T} (\Delta x (a + \Delta a, t) \\ - f (a, x (t), u (t))) \end{array}\tag{A.4}
$$

Here the first term is obtained as a pseudo inverse if the rank of the Jacobian is full, otherwise, we can use the SVD (Singular Value Decomposition) to obtain the correct inverse using the least squares principle. We continue updating the parameters until the difference per iteration in (A.4) is minimal. Applying this technique for the data collected gives $a ( 1 ) = - 0 . 0 1 8 9 , a ( 2 ) = - 0 . 3 4 0 6 ,$ $a ( 3 ) = 0 . 0 4 6 9$ , and $a ( 4 ) = 0 . 0 3 8 7$ . The input variable for the system is the number of choices shown to a user. The steady state value of the relationship between information load and the number of choices (our input variable) ultimately depends upon the parameters $a ( 3 )$ and $a ( 4 ) .$ . If we equate the right hand side of (A.1) to zero, we get the derivative in the left hand side equal to zero. This occurs when the system has reached a constant value and the system stays at that value. We can find the value of this steady-state output value by solving the following:

$$
a (1) + a (2) x _ {s s} + \frac {a (3) u _ {s s}}{1 + a ^ {2} (4) u _ {s s} ^ {2}} = 0\tag{A.5}
$$

Moving variables gives the $x _ { s s }$ in terms of $u _ { s s } .$

$$
\chi_ {s s} = \frac {- a _ {1} - ((a (3) u _ {s s}) / (1 + a ^ {2} (4) u _ {s s} ^ {2}))}{a _ {2}}\tag{A.6}
$$

Eq. (A.6) shows how the value of $u _ { s s }$ affects that of $\boldsymbol { x } _ { s s }$ and therefore for some value of $u _ { s s }$ the value of $x _ { s s }$ is maximized.

## Appendix B. Proposed feedback control

Given the nominal model, the design goal of a feedback control law attempts to regulate the information load at a prescribed constant value $x _ { d } .$ We want the error value to approach zero over time, where the error e(t) is defined as $e ( t ) = x ( t ) - x _ { d } .$

The error dynamics, as derived from our nominal model (A.1) are given by:

$$
\frac {d e (t)}{d t} = [ a (1) + a (2) x _ {d} ] + a (2) e (t) + \nu (t)\tag{A.7}
$$

where

$$
v (t) = \frac {a (3) u (t)}{1 + a ^ {2} (4) u ^ {2} (t)}\tag{A.8}
$$

Consider the following feedback control law that will guarantee exponential stability of the closed loop dynamic system. The control law is:

$$
v (t) = - [ a (1) + a (2) x _ {d} ] - [ a (2) + k ] e (t)\tag{A.9}
$$

Using the relationship (A.8), we can obtain u(t) from the calculated value of v(t) that would come from the control law (A.9). The expression we get by performing the inverse manipulation is:

$$
u (t) = \frac {a (3) \pm \sqrt {a ^ {2} (3) - 4 a ^ {2} (4) v ^ {2} (t)}}{2 a ^ {2} (4) v (t)}\tag{A.10}
$$

We require the control variable to be a real number. For that to occur, the term inside the square root should not be negative. This can be accomplished if we use the following rule for the variable v(t). We name this variable pseudocontrol since we will design the control law by treating this variable as the control variable. After obtaining the formula for this, we can find the actual control law by applying (A.10) to the pseudocontrol formula.

$$
v (t) \in \left(- \left| \frac {a (3)}{2 a (4)} \right|, \left| \frac {a (3)}{2 a (4)} \right|\right)\tag{A.11}
$$

Since, the value of u(t) cannot be negative because of its physical meaning (e.g. you cannot have a negative number of choices presented), we impose the following constraint instead:

$$
v (t) \in \left(0, \left| \frac {a (3)}{2 a (4)} \right|\right)\tag{A.12}
$$

Because of the new constraint, we modify the control law (A.9) to the following:

$$
v (t) = \min \left(\max (0, - [ a (1) + a (2) x _ {d} ] - [ a (2) + k ] e (t)), \left| \frac {a (3)}{2 a (4)} \right|\right)\tag{A.13}
$$

Eq. (A.10) gives two values for u(t). We use only the following one when the value of v(t) is close to zero:

$$
u (t) = \frac {a (3) - \sqrt {a ^ {2} (3) - 4 a ^ {2} (4) v (t) ^ {2}}}{2 a ^ {2} (4) v (t)}\tag{A.14}
$$

The reason for this becomes clear when we analyze what happens to the control variable for small values of $\nu ( t ) .$ In order to do this, we expand the square root term using Taylor series expansion, in the numerator of (A.14), retaining only the linear term for small v and simplify to get:

$$
u (t) \approx C v (t)\tag{A.15}
$$

Here, C is a constant. Therefore, lim $_ { 1 \nu \to 0 } u = 0$ . However, if we had chosen the control variable with the positive sign, this limit in the extended real system would be $\begin{array} { r } { \operatorname* { l i m } _ { \nu \to 0 } u = \infty } \end{array}$ . If we retain the negative sign for all $\nu ( t ) ,$ we get a constraint that is unreasonable. The constraint we obtain is $0 \leq u ( t ) \leq 1$ . The upper constraint is problematic, because it requires that we cannot have more than one choice. This problem no longer exists when we use the positive sign. Therefore, we use the negative sign when the value of v(t) is small, and we use the positive sign otherwise. Moreover, in implementation, since the number of choices should belong to the set of non-negative whole numbers, we round off the variable u(t) to its nearest non-negative whole number.

## References

[1] N. Arora, J. Huber, Improving parameter estimates and model prediction by aggregate customization in choice experiments, Journal of Consumer Research 28, 2001, pp. 273–283.

[2] R.E. Bucklin, C. Sismeiro, A model of web site browsing behavior estimated on clickstream data, Journal of Marketing Research 40, 2003, pp. 249–267.

[3] Y.-C. Chen, R.A. Shanga, C.Y. Kaoa, The effects of information overload on con sumers’ subjective state towards buying decision in the internet shopping envi ronment, Electronic Commerce Research and Applications 8, 2008, pp. 48–58.

[4] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28, 2004, pp. 75–105.

[5] B. Hosack, The effect of system feedback and decision context on value based decision making behavior, Decision Support Systems 43, 2007, pp. 1605–1614.

[6] M.-H. Huang, Modeling virtual exploratory and shopping dynamics: an environ mental psychology approach, Information & Management 41, 2003, pp. 39–47

[7] P. Kachroo, K. Ozbay, Feedback control solutions to network level user-equilibrium real-time dynamic traffic assignment problems, Networks and Spatial Eco nomics 5, 2005, pp. 243–260.

[8] P. Kachroo, S. Shedied, H. Vanlandingham, Pursuit evasion: the herding non cooperative dynamic game: the stochastic model, IEEE Transactions on Systems Man, and Cybernetics, Part C 32, 2002, pp. 37–42.

[9] A.A. Kamis, E.A. Stohr, Parametric search engines: what makes them effective when shopping online for differentiated products? Information & Management 43, 2006, pp. 904–918.

[10] R. Kheirandish. A.S. Krishen. P. Kachroo, Application of optimal control theory in marketing: what is the optimal number of choices on a shopping platform/ website? International Journal of Computer Applications in Technology 34 2009, pp. 207–215.

[11] A.S. Krishen, K. Nakamoto, Improving consumer quality-efficiency by using simple adaptive feedback in a choice setting, International Journal of Compute Applications in Technology 34, 2009, pp. 155–164.

[12] B.K. Lee, W.N. Lee, The effect of information overload on consumer choice quality in an on line environment, Psychology & Marketing 21, 2004, pp. 159–183

[13] P. Mellodge, P. Kachroo, Scaled instrument vehicle system: modeling, control, and hardware, International Journal of Vehicle Autonomous Systems 2, 2004, pp. 71– 103.

[14] O. Toubia, J.R. Hauser, D.I. Simester, Polyhedral methods for adaptive choicebased conjoint analysis, Journal of Marketing Research 41, 2004, pp. 116–131.

[15] Y. Wang, W. Dai, Y. Yuan, Website browsing aid: a navigation graph-based recommendation system, Decision Support Systems 45, 2008, pp. 387–400.

[16] H. Wang, H. Doong, Online customers’ cognitive differences and their impact on the success of recommendation agents, Information & Management 47, 2010, pp. 109–114.

[17] C. Wu, F. Cheng, D. Yen, The atmospheric factors of online storefront environment design: an empirical experiment in Taiwan, Information & Management 45, 2008, pp. 493–498.

![](/api/attachments/JZU6JCUE/fulltext/images/2608e3dff652e6989bf4b1052c3e32c70e24e6508aaacb6a48198694bfb329e6.jpg)  
Dr. Anjala Krishen is an assistant professor of Marketing at University of Nevada Las Vegas since 2007. She completed a B.S. in electrical engineering from Rice University in 1990, an MBA from Virginia Tech in 1996, and an M.S. and Ph.D. in Marketing from Virginia Tech in 2007. Prior to academia, she worked for 13 years in companies including American Electric Power, Enerwise Global Technologies, and Oracle Corporation. Her research focuses on decision-making in complex environments from a consumer perspective and has appeared in journals such as European Journal of Marketing, Journal of Business Research, and International Journal of Retail and Distribution Management.

![](/api/attachments/JZU6JCUE/fulltext/images/c9092232a31f9aefd7f8bb9b7cf7ddd31fc13e0a5102d0c89a246225c052aaef.jpg)  
Dr. Robyn Raschke is an assistant professor of accounting at the University of Nevada, Las Vegas. Prior to receiving her PhD, she spent over 15 years working in the San Francisco and Silicon Valley area. Her business experience ranges from working as a Vice President/Controller for several high-technology companies to consulting in the San Francisco bay area. She received her Ph.D. in Information Systems from Arizona State University. Her research interests focus on decision making and information presentation. Her work is published in Journal of Information Systems, International Journal of Accounting Information Systems, and various information system and accounting conferences.

![](/api/attachments/JZU6JCUE/fulltext/images/29044bca0197fb4586db7c56f939737311eed0aa24bd9ccb1e50912eff0d4089.jpg)  
Dr. Pushkin Kachroo is a professor in the Department of Electrical and Computer Engineering and Director of the Transportation Research Center at University of Nevada, Las Vegas. He received his Ph.D. from University of California, Berkeley in Mechanical Engineering in 1993, his M.S. from Rice University in Mechanical Engineering in 1990, and his B.Tech. from I.I.T Bombay in Civil Engineering in 1998. He has additional M.S. and Ph.D. degrees in Mathematics received in 2004 and 2007 from Virginia Tech. He has written ten books, four edited volumes and overall more than one hundred publications including journal papers. His research interests are in the theory and applications of feedback control.
