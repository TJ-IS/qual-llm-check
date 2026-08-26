---
otero_id: 2766
otero_key: "7Y3KDN3F"
title: "mHealth App recommendation based on the prediction of suitable behavior change techniques"
authors: "Xiaoxin Mao; Xi Zhao; Yuanyuan Liu"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113248"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# mHealth App recommendation based on the prediction of suitable behavior change techniques

![](/api/attachments/7Y3KDN3F/fulltext/images/d7b6222f00ec64bd9ba42ef97c4db60af2af4ec8cd76cb7cd707628487354483.jpg)

Xiaoxin Mao<sup>a,b</sup>, Xi Zhao<sup>a,b,c,</sup>∗, Yuanyuan Liu<sup>a</sup>

<sup>a</sup> School of Management, Xi’an Jiaotong University, Xi’an 710049, China

<sup>b</sup> Shaanxi Engineering Research Center of Medical and Health Big Data, Xi’an 710049, China

<sup>c</sup> The Key Lab of the Ministry of Education for Process Control & Eficiency Engineering, Xi’an 710049, China

## A R T I C L E I N F O

Keywords: Multi-source data mHealth App App recommendation Behavior change techniques

## A B S T R A C T

In light of individuals' increasing concern regarding their physical health, mobile health applications (mHealth Apps) have gained popularity in recent years as important tools for addressing health problems. However, users find it challenging to choose appropriate mHealth Apps, as these Apps incorporate diverse behavior change techniques (BCTs), and their individual behavioral intervention efects on users vary. This study proposes a novel BCT-based mHealth App recommendation method to suggest suitable mHealth Apps to users. Specifically, we encode mHealth Apps to obtain information on the BCT adopted by the Apps. Based on the combination of BCT in each mHealth App and its usage information, we construct a User-BCT matrix to represent users' preferences concerning BCTs. We also construct a user profile for each user, which considers their characteristics related to BCTs. Next, we build a prediction model that links each user's profile to BCTs, and use the AdaBoost algorithm to predict suitable BCTs for a target user. Finally, we recommend mHealth Apps with the highest BCT-matching levels to a target user. We also investigate the performance of the proposed method using a real dataset. The experimental results demonstrate the advantages of the proposed method.

## 1. Introduction

Advances in the mobile internet field have led to the development of various mobile applications (Apps) that provide users with a wide range of services [1]. In particular—considering that individuals are in creasingly concerned with their physical health—health and fitness Apps (mHealth Apps) are becoming more popular and have developed into important tools for addressing health problems [2-4]. The mHealth Apps considered in this study are health and fitness-related applications that run on mobile devices. These Apps aim to provide behavioral intervention to users to improve both health behaviors and overall health [5]. The majority of mHealth Apps can be divided into three categories: (1) food intake, (2) physical activity, and (3) weight management [3]. Fig. 1 shows several examples of currently available mHealth Apps. Krebs and Duncan [3] reported that approximately 60% of individuals in the United States have downloaded at least one health related mobile App and that most subscribers use them at least once a day. The use of these Apps has been increasing over time, causing users to become more reliant on them, which, in turn, requires careful design considerations to deliver a user-centered experience that ensures that the interventions in the Apps are effective [6].

mHealth Apps mainly intervene concerning unhealthy behaviors, with the obiective of improving overall health. Timely intervention is critical to positive outcomes and there are multiple existing studies on the benefits of using technology to enhance the efectiveness of user interventions [7,8]. Furthermore, the sustained use of intervention strategies is essential for altering undesirable habits [7]. Users benefit from the mHealth Apps when they commit to a routine for a suficiently long period. As noted by Danaher et al., “a key ingredient in determining the impact of any Web-based behavior change program is the extent to which participants are exposed to the program [10].” Therefore, it is necessary to encourage users to adhere to the regular use of mHealth Apps to facilitate efective interventions.

Although a sustained commitment to mHealth Apps is beneficial to users, abandonment of Apps and their interventions is widespread [11]. Murnane et al. [11] determined that there are many users who initially download but then later uninstall an mHealth App. The primary reason is usually the abandonment of an original health goal. One of the reasons for this action may be that the user does not experience a positive impact while using the App, therefore concluding that it is not suitable. For many users, it is dificult to identify suitable mHealth Apps for personal use. In practice, most users choose mHealth Apps based on the

![](/api/attachments/7Y3KDN3F/fulltext/images/dd122e8e5dad09622d97ba42730cc0ebbe4906513f2a05b6b744fd340b81f6f4.jpg)  
Fig. 1. Several examples of mHealth Apps.

App ranking in the App Store, or by seeking advice from friends and relatives [11]. However, this approach does not necessarily identify suitable mHealth Apps for every user, and an unsuitable App that ofers ineficient behavioral intervention will result in abandonment after a few attempts. Moreover, given that the number of available mHealth Apps is constantly increasing, this problem is becoming progressively worse [12, 13]. The inundation of mHealth Apps makes it dificult for users to choose an App with appropriate behavioral intervention, leading them to readily give up after an exhaustive search [12]. It is therefore necessary to propose an mHealth App recommendation method to suggest suitable Apps with efective behavioral intervention for users.

Numerous App recommendation methods have recently been proposed in the literature. These methods utilize various techniques, such as incorporating context analysis [14], considering user preferences [15], and adopting social network information [16], among others [17, 18]. Contrary to these methods that focus on recommending general Apps to users, mHealth App recommendation can be regarded as an extended application and exploration of behavioral intervention based on which suitable Apps are suggested to individual. Consequently, the analysis of suitable intervention techniques adopted by mHealth Apps is an important issue. Although extensive research has been conducted on general App recommendation dificulties, little attention has been paid to the mHealth App recommendation problem specifically. The direct application of existing App recommendation methods to address this problem may result in biased recommenda tions, as they ignore the intervention techniques used in mHealth Apps and fail to suggest appropriate behavioral intervention techniques to users. Therefore, this study explores the behavioral intervention techniques adopted in mHealth Apps and proposes a novel mHealth App recommendation method for users, with the intention of improving the health of users.

To solve the aforementioned problems, this study analyzes the intervention techniques adopted in mHealth Apps and attempts to introduce behavioral change techniques (BCTs) into the recommendation framework. BCTs have been widely adopted by mHealth Apps to improve users' health behaviors as well as their overall health [19, 20]. There are currently many mHealth Apps that incorporate various BCTs for diferent users. Appropriate BCTs can meet the personalized needs of users, and perceived personalization can significantly increase users' intention to adopt mHealth Apps by increasing their trust [21]. More over, as users are intrinsically motivated to use mHealth Apps to improve their overall health, suitable BCTs can enhance users' internal motivation, which has been shown to be a good predictor of users' behavioral intention regarding subsequent use of the mHealth App [22]. Therefore, considering BCTs is very important for addressing the problem of mHealth Apps recommendation. However, a BCT afects each user individually; therefore, the relationship between user characteristics and suitable BCTs should be explored and exploited in the recommendation framework. We therefore include user characteristics in the recommendation framework to improve the performance of mHealth Apps recommendation (including precision, recall, and Fmeasure) by analyzing the relationship between the characteristics of the users and BCTs. This enables us to predict appropriate BCTs for users.

Several recent studies have shown that certain BCTs play diferent roles in afecting the behaviors of users with diferent characteristics. For example, Socialreward exerts diferent efects on users with diferent ages and genders [23, 24], while Socialsupport has diverse efects on users with diferent telephone communication behaviors [25]. However, there are still some unexplored relationships between BCTs and user characteristics, as some user characteristics cannot be observed or measured directly. Identifying a suitable proxy for some characteristics related to diferent BCTs is therefore vital. With the development of information technology, an increasing volume of individuals' data can be collected and extracted [26, 27]. These data serve as an important source of information for logging the daily behavior of individuals [28], such as telephonic communication behavior, cell-phone usage beha vior, and activity-travel behavior [29-32]. In this study, we describe the BCT-related characteristics of users and integrate them with BCT to provide personalized recommendations by using data collected from one of China's largest mobile operators.

This study proposes a novel BCT-based mHealth App recommendation method (BHAR). Unlike existing App recommendation methods for general Apps, our method focuses on the category of mHealth Apps and considers user-friendly BCTs. Specifically, based on the combination of BCTs in each mHealth App and the usage information of each mHealth App, we construct a User-BCT matrix to represent the preference information of users for each BCT. Moreover, we construct a profile for each user that considers their characteristics related to BCTs. Next, we build a prediction model that links each user's profile to BCTs and use the AdaBoost algorithm to predict suitable BCTs for a target user. Finally, we recommend several mHealth Apps with the highest BCT-matching levels to a target user. To demonstrate the effectiveness of our solution, we apply the proposed approach to a real dataset from a mobile phone operator. The results show that considering the BCTs adopted in the mHealth App recommendation problem results in an improvement of the recommendation performance.

The main contributions of this study can be summarized as follows; first, we newly explore the problem of mHealth App recommendations with the intent to introduce BCTs in the recommendation framework. The incorporation of BCTs helps to determine the suitability of an mHealth App for a specific user. Second, we characterize user profiles based on four factors: demographic characteristics, telephonic communication behavior, cell-phone usage behavior, and activity-travel behavior. Characterizing user profiles contributes to a detailed description of the individual and the accurate identification of their needs. Third, we build a prediction model incorporating user characteristics and suitable BCTs using the AdaBoost algorithm to predict suitable BCTs for users. The exploration of the relationship between user characteristics and BCTs indicates which group of users a given BCT is well suited for and how a BCT works for them. Fourth, we propose a BCTbased mHealth App recommendation method, which is a novel method to suggest suitable mHealth Apps with higher BCTs-matching levels to users. This method connects users and mHealth Apps through BCTs, providing a new perspective for investigating recommendation problems, especially for a specific type of App. The results reveal that this method is superior to several baseline methods, which demonstrates the efectiveness of the proposed approach.

The remainder of this paper is as follows: In Section 2, we review existing works related to our study. Then, we define the BCT-based mHealth App recommendation problem and propose a BCT-based mHealth App recommendation method in Section 3. In Section 4, we use data collected from a mobile phone operator to verify the efectiveness of our proposed method. Finally, we conclude our study by highlighting its significance and considering the directions of future research in Section 5.

Table 1  
An example of diferent BCTs adopted in mHealth Apps.

<table><tr><td>BCT</td><td>Gudong</td><td>Yuedongquan</td></tr><tr><td>Goal setting (outcome)</td><td>•</td><td></td></tr><tr><td>Review outcome goal(s)</td><td>•</td><td></td></tr><tr><td>Self-monitoring of outcomes of behavior</td><td>•</td><td></td></tr><tr><td>Biofeedback</td><td></td><td>•</td></tr><tr><td>Feedback on outcome(s) of behavior</td><td></td><td>•</td></tr><tr><td>Information about health consequences</td><td>•</td><td></td></tr><tr><td>Monitoring of emotional consequences</td><td>•</td><td></td></tr><tr><td>Habit formation</td><td></td><td>•</td></tr><tr><td>Graded tasks</td><td>•</td><td></td></tr><tr><td>Material incentive (behavior)</td><td></td><td>•</td></tr><tr><td>Material reward (behavior)</td><td></td><td>•</td></tr><tr><td>Social reward</td><td>•</td><td></td></tr><tr><td>Social incentive</td><td>•</td><td></td></tr><tr><td>Future punishment</td><td></td><td>•</td></tr><tr><td>Behavior cost</td><td></td><td>•</td></tr><tr><td>Remove punishment</td><td></td><td>•</td></tr><tr><td>Vicarious consequences</td><td>•</td><td></td></tr></table>

## 2. Related works

## 2.1. mHealth Apps and BCTs

The prevalence and rapid growth of information technology is the basis of the development of mobile Apps that significantly afect our daily lives. Recently, mHealth Apps have become increasingly popular, as they can assist users in developing healthy habits and addressing their health problems [2-4]. mHealth Apps are mainly used as an intervention tool to improve the health of the user, in contrast to general Apps that provide users with various platforms, resources, or services. mHealth Apps adopt BCTs to modify the health behavior of users and to promote physical health [19, 20, 33, 34]. In this regard, Michie et al. [35] define BCT as a systematic procedure that is an active component of an intervention designed to change one's behavior. Some scholars have studied the applications of BCTs in the areas of health and fitness. Chiang et al. [36] proposed a comprehensive framework for the behavior change wheel that aims to help address the current knowledge gap regarding how two-way mHealth interventions for medication adherence may work. Adopting the behavioral change technique taxonomy from Michie et al. [35], we obtained the definition and classification of BCTs. BCTs are divided into 16 abstract categories. Each category is divided into several additional specific categories, with 93 specific categories in total [35]. For example, Social support as one abstract category includes three specific categories: Social support (unspecified), Social support (practical), Social support (emotional). The full taxonomy and definitions of BCTs are shown in the Appendix. Generally, the combination of BCTs can difer between Apps that are in the same domain (e.g., exercise guiding Apps); therefore, they can uniquely influence user behavior based on distinct combinations [33]. Table 1 shows an example of two mHealth Apps and the BCTs they adopted. Gudong and Y uedongquan both focus on exercise guiding but adopt diferent combinations of BCTs. Therefore, it is important to determine the suitable combination of BCTs for each user.

## 2.2. User characteristics related to BCTs

Diferent BCTs are suitable for users with diferent personalities and characteristics [35]. For example, Social reward may be suitable for a specific user, while Action planning may not. Several investigators have studied the relationship between BCTs and users' characteristics, and a summary of their results are presented in Table 2. BCTs such as Social reward, Social incentive, and Social support have diferent efects on the behavioral changes of users with diferent genders and ages [23, 24, 37- 39]. For example, Social support yields diferent results in users with diferent telephone communication behaviors, because individuals that frequently use the telephone for communication may rely more on their social network [25]. Moreover, given that users with diferent phone usage behaviors have diferent levels of addiction to mobile phones, Reward and threat are more efective for users with higher mobile phone usage behaviors due to their addiction [40]. Further, for users with diferent activity-travel behaviors, Action planning is an efective way to increase the activity of users and exerts diferent efects. Specifically, Action planning produces a marginal efect on users with low activity and no efect on those with sedentary behaviors [41]. Therefore, sui table BCTs vary for users with diferent characteristics. However, there are still unexplored relationships between BCTs and user characteristics and determining the appropriate combination of BCTs is still a challenge. In this study—considering the aforementioned relevant characteristics—we analyze suitable BCTs of users and predict the appropriate combination of BCTs according to their characteristics, including demographic characteristics, telephonic communication behaviors, cell-phone usage behaviors. and activity-travel behaviors.

Table 2  
The examples of characteristics and related BCTs.

<table><tr><td>Characteristics</td><td>BCTs</td></tr><tr><td>Demographic characteristics</td><td>Social reward [23-25]</td></tr><tr><td>Telephone communication behaviors</td><td>Social support [25]</td></tr><tr><td>Phone usage behaviors</td><td>Reward and threat [40]</td></tr><tr><td>Activity-travel behaviors</td><td>Action planning [41]</td></tr></table>

## 2.3. App recommendation methods

Considering the availability of existing Apps and the rapid increase in number of new Apps, it becomes both challenging and time-con suming for people to select appropriate Apps [42]. Recently, various App recommendation approaches have been proposed and applied [14- 18]. Cao and Lin [42] summarized the related literature on this topic and divided these studies into App recommendation methods using diferent techniques including similarity measures, context analysis, user preference incorporation, social information utilization, and other approaches. For example, Davidsson and Moritz [14] integrated context with user feedback to construct an App recommendation model and Jang et al. [15] proposed a method to suggest suitable Apps by considering the dynamic preferences of users. Pan et al. [16] analyzed networks based on the historical App usage data of users to propose a recommendation method, while Yin et al. [18] proposed Mobi-SAGE to suggest Apps considering both user interest and privacy preferences. To address the problem of mHealth App recommendation, as users hope to improve their health levels with the help of mHealth Apps, it is necessary to explore BCT information in mHealth Apps and match suitable BCTs with users. Therefore, the major diference between general App recommendation and mHealth App recommendation is the considera tion of BCTs. Directly applying general methods to mHealth App recommendation will result in biased results. Therefore, incorporating BCTs as a key element for recommendation is vital, given the context of mHealth Apps. A better understanding of suitable BCTs for individuals and their incorporation into the recommendation process will yield improved and personalized outcomes for users. In this study, an mHealth App recommendation method is proposed that predicts suitable BCTs for users, which provides a new perspective of traditional App recommendation research.

![](/api/attachments/7Y3KDN3F/fulltext/images/4bffdb80ef9888b25f2bae4579b70c91827958960b5f6dd337371b575e454b6b.jpg)  
Fig. 2. The framework of the BHAR.

## 3. BCT-based mHealth App recommendation (BHAR)

## 3.1. Problem formulation

In this section, we formulate the problem of mHealth App recommendation within the context of BCTs. Suppose that there are m historical users $U = \{ u _ { 1 } , \cdots , u _ { i } , \cdots , u _ { m } \}$ and n mHealth Apps $A = \{ a _ { 1 } , \cdots$ $, a _ { j } , \cdots , a _ { n } \}$ . For each historical user $u _ { i } , i = 1 , \cdots , m ,$ , we collected in dividual characteristics and usage information concerning mHealth Apps. We aim to analyze the underlying preferences of users regarding BCTs and construct a suitable BCT prediction model that connects user characteristics to BCTs. This model enables us to predict suitable BCTs and recommend mHealth Apps to a target user, of whom we only know their individual characteristics.

For this purpose, we propose the BCT-based mHealth App recommendation (BHAR) method. The framework of this study, as presented in Fig. 2, consists of the following four major phases. First, the BCT-adopted information on historical users was obtained by constructing a User-BCT matrix. Second, a user profile was constructed based on four aspects: demographic characteristics, telephonic communication behavior, cell-phone usage behavior, and activity-travel behavior. Third, the prediction model that utilizes the AdaBoost algorithm was constructed to predict suitable BCTs for target users. Finally, the BCT-matching levels were calculated to generate the ranking of suitable mHealth Apps for target users.

## 3.2. User-BCT matrix construction

A user who adopts an unsuitable mHealth App often abandons it after a while [11]. An mHealth App that is used by an individual for a long time is more likely to be suitable. In this study, the usage time is utilized to represent the preferences of the users for each mHealth App. Therefore, let the preference of a user u on mHealth App a be represented as $p _ { i j } .$ A matrix is constructed to show the relationships between users and mHealth Apps. Each column and row of the matrix corresponds to each user and mHealth App respectively, while each entry in the matrix represents the preference of each user for each App. The preferences are evaluated using the average time a user spends on the App per day and the detailed usage time can be collected from the mobile operator. As users have diferent habits concerning the use of Apps, the same usage time for an mHealth App results in diferent preferences for each user. Specifically, for a heavy user who uses their phone for many hours each day, a short usage time of the mHealth App does not imply that they use it frequently, while for a user who hardly uses their phone, the same usage time of the mHealth App indicates that this App is among the individual's often-used Apps. Therefore, to address the scale diference, the average time is normalized in the interval [0, 1] according to Eq. (1) and the outliers are eliminated in advance.

$$
\hat {p} _ {i, j} = \frac {p _ {i , j} - m i n p _ {i}}{m a x p _ {i} - m i n p _ {i}}\tag{1}
$$

where minp and maxp represent the minimum and maximum p values of the average usage time of all the Apps for user i and $\hat { p } _ { i , j }$ indicates the normalized value of the preference for App j used by user i. It should be noted that we normalize the average time considering each user's scale for overall Apps' usage time. The final User-App matrix is obtained based on the normalized value of preference for each App, which is shown in Fig. 3 (a).

To improve the quality of the recommendation, the BCTs adopted by mHealth Apps are considered in the proposed method. Therefore, the user preferences for specific BCTs should be evaluated. To obtain information concerning the BCTs adopted by Apps, the BCTs of each mHealth App are encoded according to the definition and classification proposed in the study [35]. As there are 16 abstract BCTs and each abstract BCT includes specific BCTs, we develop the method based on the 16 abstract BCTs. Therefore, BCTs in the following refers to the abstract BCTs. The details of the coding process are included in Section 4.1. Based on the coding results, the detailed BCTs adopted by each mHealth App can be obtained. The BCTs adoption vector $B _ { a j }$ of App $a _ { j }$ can be represented as $B _ { a _ { j } } = [ b _ { j _ { 1 } } , b _ { j _ { 2 } } , \cdots , b _ { j _ { k } } , \cdots , b _ { j _ { K } } ] ,$ , where k represents the kth BCT and K represents the number of BCTs. The App-BCT matrix is then formulated, as illustrated in Fig. 3 (b). The jth row of the App-BCT matrix represents the BCT adoption vector of $\operatorname { A p p } a _ { j } .$ Each entry $b _ { j k }$ in the matrix indicates whether the BCT $b _ { k }$ is adopted by App $a _ { j } .$ Then, the User-BCT matrix can be measured by Eq. (2).

![](/api/attachments/7Y3KDN3F/fulltext/images/73e0bee652a365a2e02975acad358904b896c2e0e173a5e3af233995d93c31f4.jpg)  
(a) User-App Matrix (UA)

![](/api/attachments/7Y3KDN3F/fulltext/images/5cbd62919bc809ca8f891ab9e21f644c4cc387d44b04318928561d0efe792d09.jpg)

![](/api/attachments/7Y3KDN3F/fulltext/images/08ed8012beb05318b46fd6c5b6e7d9fd6d48841468c702fdc4f950969958dca0.jpg)  
(b) App-BCT Matrix (AB)  
(c) User-BCT Matrix (UB)  
Fig. 3. An example of the construction of the User-BCT matrix.

$$
U B = U A \times A B\tag{2}
$$

where UB represents the User-BCT matrix and UA and AB represent the User-App matrix and App-BCT matrix respectively. Each entry in the User-BCT matrix (UB) represents a possible preference of user u of BCT $b _ { k } ,$ denoted by $p ( u _ { i } , b _ { k } )$ . The values are converted into binary variables for convenience in predicting suitable BCTs for target users. For each user and each BCT, the variable $P o s s ( u _ { i } , b _ { k } )$ can be evaluated by Eq. (3).

$$
P o s s (u _ {i}, b _ {k}) = \left\{ \begin{array}{l l} 1, & p (u _ {i}, b _ {k}) > 0 \\ 0, & p (u _ {i}, b _ {k}) = 0 \end{array} \right.\tag{3}
$$

where $P o s s ( u _ { i } , b _ { k } ) = 1$ means that BCT $b _ { k }$ is possibly suitable for user $u _ { i } ,$ and $P o s s ( u _ { i } , b _ { k } ) = 0$ indicates that BCT $b _ { k }$ may not be suitable for user u .

## 3.3. User profile construction

Several studies investigators have determined that there is a relationship between user characteristics and BCTs [23, 24]. To generate personalized recommendation for each individual, the user's characteristics are considered within the recommendation framework. In this study, we collected related data to formulate the users' characteristics. All data are anonymous and provided by a mobile phone operator in China. Based on the raw dataset collected, the characteristics of users can be calculated according to four factors: demographic characteristics, telephonic communication behavior, cell-phone usage behavior, and activity-travel behavior.

## 3.3.1. Demographic characteristics

Several researchers have studied the relationship between BCTs and users' demographic characteristics. For example, Social reward exerts diferent efects on users of diferent ages [24], while Social incentive has diferent efects on users of diferent genders [23]. It can therefore be argued that suitable BCTs vary among users with diferent ages and genders. The users' demographic characteristics of age $( D _ { 1 } )$ and gender $( D _ { 2 } )$ are considered to distinguish between users. The demographic characteristics of user $u _ { i }$ are represented as: $D C _ { i } = \{ D _ { 1 } ( u _ { i } ) , D _ { 2 } ( u _ { i } ) \}$

## 3.3.2. Telephonic communication behaviors

Users' telephonic communication behaviors can reflect their demands from and dependence on their social network. Individuals that partake in frequent telephone communication behaviors are more dependent on a social network, which indicates that Socialsupport has diferent efects for users with diferent telephone communication behaviors [25]. Therefore, suitable BCTs vary for users with diferent telephone communication behaviors. In this study, telephonic communication behaviors are evaluated using raw phone usage data, including the average number of calls made daily $( T _ { 1 } ) _ { : }$ , the average time spent on calls made daily (T ), the average number of calls received daily $\left( T _ { 3 } \right)$ , the average time spent on calls received daily $( T _ { 4 } ) ,$ the average number of messages sent and received daily $( T _ { 5 } ) ,$ and the monthly average number of non-redundant contacts $( T _ { 6 } )$ . The telephonic communication behavior of users $u _ { i }$ is represented as: $T C _ { i } = \{ T _ { 1 } ( u _ { i } ) , T _ { 2 } ( u _ { i } ) , T _ { 3 } ( u _ { i } ) , T _ { 4 } ( u _ { i } ) , T _ { 5 } ( u _ { i } ) , T _ { 6 } ( u _ { i } ) \}$

## 3.3.3. Cell-phone usage behaviors

Users with diferent cell-phone usage behaviors have diferent levels of mobile phone addiction. Reward and threat are more powerful BCTs for users with higher mobile phone usage, as they are heavily addicted to their phones [40]. Therefore, it is believed that suitable BCTs vary for users with diferent cell-phone usage behaviors. In this study, cellphone usage behaviors are evaluated according to the following aspects: the average daily number of records (C ), the average daily time of mobile web use $( C _ { 2 } ) _ { i }$ , the average daily value of internet trafic (C ), and the average number of Apps used daily (C ). The cell-phone usage behavior of user u is represented as: $C U _ { i } = \{ C _ { 1 } ( u _ { i } ) , C _ { 2 } ( u _ { i } ) , C _ { 3 } ( u _ { i } ) , C _ { 4 } ( u _ { i } ) \}$

## 3.3.4. Activity-travel behaviors

Individuals with a small range of activity usually have a sedentary behavior pattern, which reflects their lower levels of physical activity. Moreover, it may be more dificult to change sedentary users' health behavior. For users with diferent activity-travel behaviors, Action planning, exerts diferent efects as an efective way to increase user activity. Specifically, Action planning produces a marginal efect on users with low activity and even no efect on those who may have sedentary behaviors [41]. Therefore, it is argued that suitable BCTs vary for users with diferent activity-travel behaviors. In this study, activitytravel behaviors are evaluated from several aspects: the average daily stay time $\left( A _ { 1 } \right)$ , the average daily range of activity during daytime (7 am–7 pm) $( A _ { 2 } ) _ { : }$ , the average daily range of activity during nighttime (7 pm–7 am) $( A _ { 3 } ) _ { ; }$ , the average daily activity areas on a weekday $( A _ { 4 } ) ,$ the average daily activity areas on weekends $\left( A _ { 5 } \right)$ , and the average number of stations visited daily $\left( A _ { 6 } \right)$ . Specifically, we can collect data about users measured in real-time (i.e., in the hh/mm/ss format), so that daytime and nighttime data can be accurately divided. The activity area represents the range of daily travel activities of users. In this study, we collect the places visited by users per day and then calculate the activity area using the model of the minimum circumscribed circle [43]. The activity-travel behavior of user $u _ { i }$ is represented as: $A T _ { i } = \{ A _ { 1 } ( u _ { i } ) , A _ { 2 } ( u _ { i } ) , A _ { 3 } ( u _ { i } ) , A _ { 4 } ( u _ { i } ) , A _ { 5 } ( u _ { i } ) , A _ { 6 } ( u _ { i } ) \}$

Based on this analysis, user profiles can be derived according to the four factors above. The user profile of user $u _ { i }$ can be expressed as $\mathbf { P } _ { i } = \{ \mathbf { D } ~ \mathbf { C } _ { i } , \mathbf { T } ~ \mathbf { C } _ { i } , \mathbf { C } ~ \mathbf { U } _ { i } , \mathbf { A } ~ \mathbf { T } _ { i } \}$

## 3.4. Suitable BCTs prediction

In this section, we use the adaptive boosting (AdaBoost) algorithm to predict suitable BCTs for target users. As each user is represented by their profile $\mathbf { P } _ { i } = \{ \mathbf { D } ~ \mathbf { C } _ { i } , \mathbf { T } ~ \mathbf { C } _ { i } , \mathbf { C } ~ \mathbf { U } _ { i } , \mathbf { A } ~ \mathbf { T } _ { i } \}$ , we need to utilize each user's profile to make a prediction. We assume that the same dimension of the user's profile may have diferent degrees of importance when predicting diferent BCTs. In this way, we use AdaBoost to predict the suitability of each BCT for a user separately, according to their profile. This method is referred to as a binary classification problem, where a positive result indicates the suitability of a BCT for a user and a negative outcome indicates that the BCT does not match the user.

AdaBoost is a supervised machine learning algorithm that combines “weak learners” (usually in a decision tree model) to formulate a “strong learner”. This algorithm is adaptive, meaning that subsequent weak learners are tweaked in favor of those instances that are misclassified by previous learners. Within the context of this study, we use AdaBoost equipped with the decision tree model as the weak learner to characterize the potentially complex interdependencies between the characteristics of users and BCTs. Specifically, the decision tree model is capable of addressing the interactions between the users' characteristics.

Based on this analysis, diferent suitable-BCTs prediction models for each BCT are separately constructed due to the diferent relationships between the related characteristics of the users and each BCT. As there are 16 abstract BCTs, we construct 16 suitable-BCTs prediction models. To construct each suitable-BCTs prediction model using the AdaBoost algorithm, the dataset is randomly divided into training and testing subsets. For abstract BCT $b _ { k } ,$ the sample is defined as $D _ { k } \ = \ \{ ( u _ { 1 } , P o s s$ $( u _ { 1 } , b _ { k } ) ) , . . . , ( u _ { i } , P o s s ( u _ { i } , b _ { k } ) ) , . . . , ( u _ { m } , P o s s ( u _ { m } , b _ { k } ) ) \}$ , where $P o s s ( u _ { i } , b _ { k } )$ refers

$$
M <   u _ {t}, a _ {j} > = \frac {B _ {u _ {t}} \cdot B _ {a _ {j}}}{| B _ {u _ {t}} | ^ {2} + | B _ {a _ {j}} | ^ {2} - | B _ {u _ {t}} | \cdot | B _ {a _ {j}} |}\tag{4}
$$

the suitable-BCT prediction models, the predicted suitable-BCT vector of target user $u _ { t } \quad \mathrm { i s }$ acquired and represented as: $B _ { u _ { t } } = [ P o s s ( u _ { t } , b _ { 1 } ) , \ \cdots \ , P o s s ( u _ { t } , b _ { k } ) , \ \cdots \ , P o s s ( u _ { t } , b _ { K } ) ]$ . Next, the BCTmatching level between the target user and mHealth Apps can be calculated based on the suitable-BCTs vector and the BCT adoption vector with the extended Jaccard's coeficient [44, 45], which is implemented in Eq. (4). Finally, the Apps are sorted according to their matching levels in descending order and the top-n Apps with the highest matching levels are selected. An App with a higher matching level is more beneficial in terms of improving users' health behavior. Thus, we recommend the mHealth App with the highest matching level to the user.

where $B _ { u _ { t } }$ denotes the suitable-BCT vector of user u and $B _ { a j }$ denotes the BCT adoption vector of the mHealth App a<sub>j</sub>; $M < u _ { t } , a _ { j } >$ denotes the BCT-matching level between user $u _ { t }$ and the mHealth App $a _ { j } .$

Algorithm 1. The overall process of BHAR.

The detailed matching process is illustrated to determine the suitable mHealth Apps for the target user. As shown in ${ \mathrm { F i g } } . 3 ( \mathbf { b } )$ , there are six Apps $\left( A _ { 1 } \mathrm { t o } A _ { 6 } \right)$ and six BCTs (B to B ). Values (0,1) denote whether the BCT is used in the App. Given a target user, the suitable BCTs can be predicted using AdaBoost and the suitable-BCTs vector can be acquired, which is assumed to be [1, 1, 0, 1, 0, 0]. Next, the matching level between the target user and each App can be calculated from Eq. (4). The result indicates that $\mathsf { A p p } A _ { 6 }$ has the highest matching level for the target user. Therefore, the mHealth App $A _ { 6 }$ is chosen and recommended to the target user. We summarize the process of the proposed recommenda tion method in Algorithm 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 The overall process of BHAR.

Input: User-App matrix UA, App-BCT matrix AB, historical user's profile  $P_{i} = \{DC_{i}, TC_{i}, CU_{i}, AT_{i}\} (i = 1, \cdots, m)$ , target user  $u_{t}$ 's profile  $P_{t} = \{DC_{t}, TC_{t}, CU_{t}, AT_{t}\}$ 

Output: Recommended Apps to target user  $u_{t}$ 

1: [Begin]

2: Step 1: Calculate the User-BCT matrix UB according to equation (2).

3: Step 2: Calculate  $\text{Poss}(u_{i}, b_{k})$  for each historical user  $u_{i}$  and each BCT  $b_{k}$  using equation (3).

4: Step 3: For each BCT  $b_{k} (k = 1, \ldots, 16)$ , use the AdaBoost algorithm to train the suitable-BCT prediction model based on the historical users' profiles  $P_{i}$  and  $\text{Poss}(u_{i}, b_{k}) (i = 1, \ldots, m)$ .

5: Step 4: Use the constructed suitable-BCT prediction models to predict the suitability of each BCT for target user  $u_{t}$ .

6: Step 5: Calculate matching levels  $M &lt; u_{t}, a_{j} &gt;$  between target user  $u_{t}$  and each App  $a_{j}$  using equation (4).

7: Step 6: Top-n mHealth Apps are selected and suggested to the target user based on the ranking of BCT-matching levels.

8: [End]
</div>

## 3.5. mHealth App recommendation

to the binary classification $^ { ( 0 , 1 ) }$ of user $u _ { i }$ for BCT $b _ { k } . ~ P o s s ( u _ { i } , b _ { k } ) = 1$ indicates that the BCT $b _ { k }$ is possibly suitable for user $u _ { i }$ and Poss $( u _ { i } , b _ { k } ) = 0$ indicates that the BCT $b _ { k }$ may not be suitable for user u . The model error converges to a preliminary range after training and testing the samples in the AdaBoost algorithm. In this way, suitable-BCTs prediction model for each abstract BCT can be established which predicts the suitable BCTs for a target user.

For a target user, we can construct their profile based on data on their demographic characteristics, telephone communication behaviors, cell-phone usage behavior, and the activity-travel behavior, which were collected from the operator, as discussed in the previous section. Considering this prerequisite, we obtain a comprehensive description of the user based on which a suitable BCT can be predicted. On the basis of

## 4. Experimental evaluation

## 4.1. Experimental datasets

A real-world dataset composed of meta-level mobile phone usage and App usage logs were collected from 6391 mobile phone users for the period April 20th to May 20th, 2018 in Shandong, China. Information about these users—including age and gender—was also collected. $\mathrm { F i g . ~ 4 ~ ( a ) }$ shows the distribution of the users' gender, indicating 1935 female users and 4146 male users, while 310 users did not indicate their gender. Fig. 4 (b) shows the users' age distribution, indicating that 571 users are under the age of 20, 2436 users are between the ages of 20 and 30, 1522 users are between the ages of 30 and 40, 1108 users are between the ages of 40 and 50, and 754 users are over the age of 50. The data are anonymous and were provided by a mobile phone operator in China. A summary of the data is presented in

![](/api/attachments/7Y3KDN3F/fulltext/images/e7291e67c47b3f0a66f6b5a4eef846d69dc87ed3d933b617334e6b6b53798b03.jpg)  
(a)

![](/api/attachments/7Y3KDN3F/fulltext/images/48764442636b3a1595b5f791ea04c46b7b05b80ee4a1f053481ac01f853f2336.jpg)  
(b)  
Fig. 4. The percent of users with diferent gender and age.

Table 3  
A summary of the dataset.

<table><tr><td>Raw data</td><td>Format</td><td>Description</td></tr><tr><td>Age</td><td>25</td><td>The user who is 25 years old.</td></tr><tr><td>Gender</td><td>Male</td><td>The user who is male.</td></tr><tr><td>Call logs</td><td>&lt; user1; user2; t1; t2 &gt;</td><td>user1 called user2 from t1 to t2</td></tr><tr><td>Message logs</td><td>&lt; user1;user2;t &gt;</td><td>user1 sent the message to user2 at t</td></tr><tr><td>Cell-id data</td><td>&lt; user;t;Lon;Lat &gt;</td><td>user visited the location &lt; Lon,Lat &gt; at t</td></tr><tr><td>Internet logs</td><td>&lt; user;t1;t2;phonetraffic &gt;</td><td>user use phonetraffic from t1 to t2</td></tr><tr><td>App usage logs</td><td>&lt; user;t1;t1;App&#x27;sname &gt;</td><td>user use App from t1 to t2</td></tr></table>

Table 3. Based on the raw data collected, the users' characteristics were calculated according to the four factors. For example, T1 is calculated by obtaining an average of the daily number of calls during the period.

A MapReduce framework is utilized to calculate the users' char acteristics owing to the large volume of collected data. For example, to calculate the average time of calls received by a given user (u) per day, the total time of the calls received by user u must first be calculated. In the MapReduce framework, the Map phase aims to extract each piece of call log of user u: < i;u;time1;time2 > to determine the duration of each call $t _ { i u } .$ During the reduce phase, the duration of each call can be aggregated and added to the total time $T _ { u } .$ Finally, the average time spent per day on received calls by user u can be obtained by averaging the total time during the period. Other characteristics are calculated using similar measures. The detailed characteristics and the raw data used are presented in Table 4.

To obtain the necessary information on BCTs adopted by mHealth Apps, the BCTs are encoded according to the definition and classification proposed in the study [35]. We selected 10 mHealth Apps on May 1, 2018 based on the top-ranked “health and fitness” Apps available on the two major application marketplaces in China: Apple iTunes (iPhone operating system) and Ying Yong Bao (one of the biggest Android application platforms). Three coders were identified to encode these Apps using the coding method proposed earlier in the study [19]. Each coder inspected each App and coded according to whether BCTs are adopted according to the BCT taxonomy [35]. After coding, all the members resolved any coding discrepancies through discussion. The adoption information of BCTs can be obtained from the results in the coded mHealth Apps. The mHealth Apps employ diferent combinations of BCTs because they focus on diferent aspects. Based on the obtained BCT information adopted by the mHealth Apps, suitable BCTs of historical users can be calculated for further recommendation.

Table 4  
The description of dataset.

<table><tr><td>Dimension</td><td>Characteristics</td><td>Raw data used</td><td>Notation</td></tr><tr><td rowspan="2">Demographic characteristics</td><td>Age</td><td>Age</td><td> $D_1$ </td></tr><tr><td>Gender</td><td>Gender</td><td> $D_2$ </td></tr><tr><td rowspan="6">Telephonic communication behaviors</td><td>Average number of calls made daily</td><td>Call logs</td><td> $T_1$ </td></tr><tr><td>Average time spent on calls made daily</td><td>Call logs</td><td> $T_2$ </td></tr><tr><td>Average number of calls received daily</td><td>Call logs</td><td> $T_3$ </td></tr><tr><td>Average time spent on calls received daily</td><td>Call logs</td><td> $T_4$ </td></tr><tr><td>Average number of messages sent and received daily</td><td>Message logs</td><td> $T_5$ </td></tr><tr><td>Monthly average number of non-redundant contacts</td><td>Message logs</td><td> $T_6$ </td></tr><tr><td rowspan="4">Cell-phone usage behaviors</td><td>Average daily number of records</td><td>Internet logs</td><td> $C_1$ </td></tr><tr><td>Average daily time of the mobile web use</td><td>Internet logs</td><td> $C_2$ </td></tr><tr><td>Average daily value of internet traffic</td><td>Internet logs</td><td> $C_3$ </td></tr><tr><td>Average number of Apps used daily</td><td>App usage logs</td><td> $C_4$ </td></tr><tr><td rowspan="6">Activity-travel behaviors</td><td>Average daily stay time</td><td>Cell-id data</td><td> $A_1$ </td></tr><tr><td>Average daily range of activity during daytime (7 am-7 pm)</td><td>Cell-id data</td><td> $A_2$ </td></tr><tr><td>Average daily range of activity during nighttime (7 pm-7 am)</td><td>Cell-id data</td><td> $A_3$ </td></tr><tr><td>Average daily activity areas on a weekday</td><td>Cell-id data</td><td> $A_4$ </td></tr><tr><td>Average daily activity areas on weekends</td><td>Cell-id data</td><td> $A_5$ </td></tr><tr><td>Average number of stations visited daily</td><td>Cell-id data</td><td> $A_6$ </td></tr></table>

Table 5  
The importance of characteristics on each BCT.

<table><tr><td>BCT</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>B1</td><td>0.3856 ( $C_4$ )</td><td>0.2231 ( $T_6$ )</td><td>0.1137 ( $A_5$ )</td><td>0.0942 ( $T_3$ )</td><td>0.0729 ( $C_3$ )</td></tr><tr><td>B2</td><td>0.2320 ( $T_2$ )</td><td>0.2097 ( $C_4$ )</td><td>0.1047 ( $D_1$ )</td><td>0.0617 ( $C_3$ )</td><td>0.0525 ( $C_2$ )</td></tr><tr><td>B3</td><td>0.2846 ( $C_4$ )</td><td>0.1589 ( $A_4$ )</td><td>0.0559 ( $D_2$ )</td><td>0.0531 ( $T_4$ )</td><td>0.0469 ( $T_3$ )</td></tr><tr><td>B4</td><td>0.1154 ( $C_2$ )</td><td>0.0795 ( $A_1$ )</td><td>0.0773 ( $T_4$ )</td><td>0.0665 ( $A_6$ )</td><td>0.0659 ( $C_3$ )</td></tr><tr><td>B5</td><td>0.3675 ( $T_3$ )</td><td>0.1652 ( $C_4$ )</td><td>0.1384 ( $T_4$ )</td><td>0.0535 ( $A_5$ )</td><td>0.0443 ( $A_4$ )</td></tr><tr><td>B6</td><td>0.0929 ( $C_3$ )</td><td>0.0813 ( $T_3$ )</td><td>0.0737 ( $T_1$ )</td><td>0.0697 ( $C_4$ )</td><td>0.0651 ( $C_1$ )</td></tr><tr><td>B7</td><td>0.1191 ( $D_2$ )</td><td>0.1060 ( $C_3$ )</td><td>0.0959 ( $C_4$ )</td><td>0.0870 ( $A_1$ )</td><td>0.0731 ( $C_2$ )</td></tr><tr><td>B8</td><td>0.1828 ( $D_1$ )</td><td>0.1165 ( $D_2$ )</td><td>0.0861 ( $T_4$ )</td><td>0.0751 ( $C_3$ )</td><td>0.0570 ( $A_2$ )</td></tr><tr><td>B9</td><td>0.1242 ( $C_3$ )</td><td>0.0839 ( $A_1$ )</td><td>0.0837 ( $C_4$ )</td><td>0.0759 ( $C_1$ )</td><td>0.0731 ( $A_5$ )</td></tr><tr><td>B10</td><td>0.2825 ( $T_1$ )</td><td>0.1545 ( $C_4$ )</td><td>0.0876 ( $T_5$ )</td><td>0.0735 ( $C_3$ )</td><td>0.0684 ( $C_1$ )</td></tr><tr><td>B11</td><td>0.1966 ( $T_2$ )</td><td>0.0991 ( $C_2$ )</td><td>0.0822 ( $D_1$ )</td><td>0.0810 ( $C_3$ )</td><td>0.0509 ( $A_4$ )</td></tr><tr><td>B12</td><td>0.0952 ( $A_1$ )</td><td>0.0883 ( $C_3$ )</td><td>0.0847 ( $C_2$ )</td><td>0.0823 ( $D_1$ )</td><td>0.0703 ( $T_2$ )</td></tr><tr><td>B13</td><td>0.1399 ( $D_1$ )</td><td>0.0986 ( $C_4$ )</td><td>0.0812 ( $C_1$ )</td><td>0.0701 ( $C_3$ )</td><td>0.0576 ( $T_2$ )</td></tr><tr><td>B14</td><td>0.1821 ( $C_2$ )</td><td>0.1088 ( $D_1$ )</td><td>0.0747 ( $A_1$ )</td><td>0.0736 ( $C_4$ )</td><td>0.0642 ( $C_1$ )</td></tr><tr><td>B16</td><td>0.4628 ( $T_3$ )</td><td>0.1714 ( $A_2$ )</td><td>0.0601 ( $A_1$ )</td><td>0.0596 ( $A_6$ )</td><td>0.0563 ( $D_1$ )</td></tr></table>

The first column represents the notation of each BCT, for which a description can be found in the Appendix, and the following columns represent the five most important characteristics and their importance.

## 4.2. Evaluation metrics

In the recommendation systems, the top-n recommendation task is the most important, given that most online recommendation systems usually present a short list of items to users [46]. To evaluate the performance of top-n recommendations, we consider the following metrics: accuracy, precision, recall, and F-measure. These metrics have been widely used in existing literature on recommendation sys tems [47]. Within this context, Precision@n and Recall@n can be cal culated as follows:

$$
P r e c i s i o n @ n = \frac {T P @ n}{n}\tag{5}
$$

$$
R e c a l l @ n = \frac {T P @ n}{N}\tag{6}
$$

where TP@n represent the number of Apps the user preferred in the recommended top-n list and N represents the total number of mHealth Apps the user used in the long term.

F-measure unifies the precision and recall metrics into a single measure, defined as follows [48]:

$$
F \text {-measure@} n = \frac {2 ^ {*} P r e c i s i o n @ n ^ {*} R e c a l l @ n}{P r e c i s i o n @ n + R e c a l l @ n}\tag{7}
$$

We calculate the precision, recall, and F-measure for every user in

![](/api/attachments/7Y3KDN3F/fulltext/images/ff48797e94ef46196725a7b8d3f744ba50df3d3180242565830316760da067d3.jpg)  
(a) The feature importance for BCT B1.  
Fig. 5. Example of feature importance.

the testing set and report the average scores.

## 4.3. Experimental results and analysis

## 4.3.1. The selection of characteristics

In this section, we analyze the relationships between the related characteristics and suitable BCTs. Specifically, we investigate the different efects that the same characteristic has on each BCT and select the characteristics that are important for predicting the suitability of each BCT. Specifically, the AdaBoost algorithm outputs the importance of each characteristic, presented in Table 5. The first column represents the notation of each BCT (for which a description can be found in the Appendix) and the following columns represent the five most important characteristics and their importance. We observe that the most important characteristics for each BCT are diferent. Considering the different BCTs, the importance of the most important characteristics also varies significantly.

Let us take Goals and planning (B1) and Feedback and monitoring (B2) as examples for the analysis and the corresponding degrees of importance of the characteristics illustrated in Fig. 5 (a) and (b) respectively. For B1, the most important characteristics are the average number of Apps used daily $( C _ { 4 } )$ , the monthly average number of nonredundant contacts $( T _ { 6 } ) ,$ , and the average daily activity areas on weekends $\left( A _ { 5 } \right)$ . Considering B2, the average time spent on calls made daily $( T _ { 2 } ) ,$ , the average number of Apps used daily $( C _ { 4 } ) ,$ , and the users' age $( D _ { 1 } )$ . Although the most important characteristics for B1 and B2 overlap, the orders of these characteristics are diferent, which means they have diferent influences on B1 and B2.

## 4.3.2. Analysis of users' characteristics

Following the preceding analysis of the most important characteristics for predicting the suitability of each BCT, this section compares the recommendation performance of several models using diferent combinations of characteristics, including the demographic characteristics (DC), telephonic communication behaviors (TC), cell-phone usage behaviors (CU), and activity-travel behaviors (AT). Specifically, 80% of the users (n = 5113) serve as the training sample to train the model, while the remaining users (n = 1278) form the test dataset for validating the model's recommendation performance. Four variants of BHAR are designed, as shown in Table 6. Specifically, BHAR\_NO\_DC, BHAR\_NO\_TC, BHAR\_NO\_CU, and BHAR\_NO\_AT ignore the features of demographic characteristics, telephonic communication behaviors, cell-phone usage behaviors, and the activity-travel behaviors respectively. The experimental results are presented in Fig. 6.

Fig. 6 shows that removing any subset of characteristics contributes to the deterioration of the model's recommendation performance, which means that all the characteristics are important for predicting the suitability of BCTs. The diferences between the holdouts for diverse variables do not cause much of a diference, as these characteristics all play important roles in the overall recommendation. Therefore, it is necessary to consider all the characteristics in the recommendation to achieve accurate outcomes.

![](/api/attachments/7Y3KDN3F/fulltext/images/5f42429a90ff949b39a5c94c4c2f84b37c508bfa418050167994f0ce2401a707.jpg)  
(b) The feature importance for BCT B2.

Table 6  
Recommendation methods using diferent combinations of characteristics.

<table><tr><td>Methods</td><td>BHAR_NO_DC</td><td>BHAR_NO_TC</td><td>BHAR_NO_CU</td><td>BHAR_NO_AT</td></tr><tr><td>Demographic characteristics</td><td></td><td>•</td><td>•</td><td>•</td></tr><tr><td>Telephonic communication behaviors</td><td>•</td><td></td><td>•</td><td>•</td></tr><tr><td>Cell-phone usage behaviors</td><td>•</td><td>•</td><td></td><td>•</td></tr><tr><td>Activity-travel behaviors</td><td>•</td><td>•</td><td>•</td><td></td></tr></table>

![](/api/attachments/7Y3KDN3F/fulltext/images/8010de42f341d807d1be371c477659c6d8806786caebaf72f545910188e4d1e7.jpg)  
(a) Precision

![](/api/attachments/7Y3KDN3F/fulltext/images/f577c8c9243ab98f4291e108fc30de2939665baef5f8100e6858d9944cc3c724.jpg)  
(b) Recall

![](/api/attachments/7Y3KDN3F/fulltext/images/09de7d76b87fac8bfeed6f874dbfd68d26feb137e0628f604179220713e6c661.jpg)  
(c) F-measure  
Fig. 6. The recommendation performance of BHAR and its variants.

Table 7  
Prediction performance using diferent models.

<table><tr><td>Methods</td><td>AdaBoost</td><td>Random forest</td><td>Logistic regression</td></tr><tr><td>Accuracy (training sample)</td><td>0.89</td><td>0.86</td><td>0.82</td></tr><tr><td>Accuracy (testing sample)</td><td>0.85</td><td>0.83</td><td>0.79</td></tr></table>

## 4.3.3. The analysis of suitable-BCTs prediction models

This study employs AdaBoost equipped with the decision tree as the classification model to determine the suitability of BCTs. To validate the applicability of AdaBoost, we perform an additional experiment in which random forest and logistic regression models replace AdaBoost, and subsequently compare the recommendation performance. Table 7 presents the results of this comparative experiment. AdaBoost clearly outperforms both the random forest and the logistic regression models in terms of accuracy. Specifically, AdaBoost achieves an accuracy of 0.89 on the training set and 0.85 on the testing set, which are better than the accuracy levels using the other two algorithms. This suggests that AdaBoost is more suitable for solving the suitable-BCT prediction problem.

To further investigate the recommendation performance of the three models, we compare the method of BHAR using AdaBoost (BHAR\_AdaBoost) to BHAR using the random forest (BHAR\_RF) and BHAR using the logistic regression (BHAR\_LR) models. All the approaches were implemented ensuring that each variant of BHAR was equipped with diferent classification models. The results of the recommendation performance are shown in Fig. 7. The results indicate that the AdaBoost algorithm outperforms the other two models. Specifically, Fig. 7 (a) shows the results of precision for the diferent models, in which BHAR\_AdaBoost achieves the highest performance with Precision@1 = 0.44 and Precision@2 = 0.31. Panels (b) and (c) in Fig. 7 show the results for recall and F-measure respectively, where BHAR\_AdaBoost achieved 0.38 for Recall@1 and 0.41 for F-measure@ 1. These values are also higher than those of the other models. Therefore, the AdaBoost algorithm is an efective method for solving the problem of mHealth App recommendation.

![](/api/attachments/7Y3KDN3F/fulltext/images/e01ede773dc3209fae3b70c6579c857a36baab7495133e26274c68a126bbe96b.jpg)  
(a) Precision

![](/api/attachments/7Y3KDN3F/fulltext/images/5380f4b7d877686f9dcd6c27977aaedc5c03c678c0b80235ecfec036e3b15f04.jpg)  
(b) Recall

![](/api/attachments/7Y3KDN3F/fulltext/images/d6d05ce72ac33bd2b22f81a277e750a501de53d4ee34dac298c7faddfee386a4.jpg)  
(c) F-measure  
Fig. 7. The recommendation performance of diferent suitable-BCTs prediction models.

![](/api/attachments/7Y3KDN3F/fulltext/images/36587c50e5ecaac4234ef4c73f64028e75a72f9c62e2d803727ee8ec486a9fd6.jpg)  
(a) Precision

![](/api/attachments/7Y3KDN3F/fulltext/images/fe67ef3d6d87b68ebfc2e7b308e7f45b9fbd963a14bf2965b9fc7f98bf75d8a8.jpg)  
(b) Recall

![](/api/attachments/7Y3KDN3F/fulltext/images/f275a9918637c1dcbb98913bd1dda5b6f9cab7867468c9deec3e142e170f8c56.jpg)  
(c) F-measure  
Fig. 8. The recommendation performance of diferent methods.

## 4.3.4. Overall performance comparisons

To validate the overall performance of the proposed recommenda tion method, we compare BHAR to several benchmark methods using the same dataset. These include User-based collaborative filtering (UBCF) [49], Item-based collaborative filtering (IBCF) [50], Matrix factorization-based recommendations (MF) [51], and Singular value decomposition (SVD) [52]. UBCF suggests suitable items by measuring the similarities between users according to their ratings [49]. Diferent from UBCF, IBCF explores the relationships among items, based on which appropriate recommendations are suggested for users [50]. The MF method constructs factor vectors to represent the relationships between users and items [51], while SVD is similar to eigen-decomposition and appropriate for asymmetrical input and has been widely applied to the recommendation of items [52. 53]. All these methods are popular generalized recommendation methods [54, 55]. It should be noted, however, that all these baseline methods are conducted using the User-App matrix, which does not consider the BCT information or users' characteristics. In contrast, considering BCTs and users' characteristics is a new feature of the proposed recommendation method. Therefore, we perform comparative experiments to validate the performance via the introduction of BCTs and the users' characteristics.

Based on Fig. 8, which reports the outcomes of the experimental analysis, our proposed recommendation method is superior to other methods. Fig. 8 (a) illustrates the precision achieved using diferent methods, in which BHAR achieved 0.44. higher than other benchmark methods. Fig. 8 (b) shows the recall results of diferent methods, in which BHAR achieves the highest performance: 0.38 and 0.54 for Recall@1 and Recall@2 respectively. Fig. 8 (c) shows that BHAR achieves the value of F-measure@1: 0.41, which is also superior to the other methods. Therefore, it is confirmed that BHAR shows improved performance by considering BCTs and users' characteristics.

## 5. Conclusion and future work

This study presents a novel BCT-based mHealth App recommendation framework by predicting suitable BCTs for App users. Compared with conventional methods, it shows improved mHealth App recommendation performance, which is beneficial to changing the health behaviors and overall health of users. Specifically, we constructed a User-BCT matrix based on the adoption information for BCTs and de. veloped a user profile matrix to consider user characteristics related to BCTs according to four aspects. We then integrated the BCT adoption information with the user profile information and developed a prediction model using the AdaBoost algorithm to predict BCTs suitable to individual users and recommend to mHealth Apps with the highest BCT-matching levels. Moreover, we investigated the performance of the proposed approach using a real-world dataset and the experimental results demonstrate the advantage of this approach in terms of a set of metrics, compared with several benchmark methods. We determined that the consideration of additional information of BCTs on the mHealth App recommendation problem leads to an increase in the overall recommendation performance.

We envisage future research based on the following aspects: (1) considering more users' characteristics and better ways to measure users' preferences concerning BCTs, (2) exploring the measurement and analysis of the behavior of users using GPS data in the recommendation system, (3) investigating changes in user behavior over time for users in the recommendation system, and (4) addressing situations where we have no prior information about users.

Supplementary data to this article can be found online at https:// doi.org/10.1016/j.dss.2020.113248.

## CRediT authorship contribution statement

Xiaoxin Mao: Conceptualization, Methodology, Software, Writing - original draft. Xi Zhao: Methodology, Resources, Data curation, Supervision, Funding acquisition. Yuanyuan Liu: Writing - review & editing, Visualization, Supervision, Funding acquisition.

## Acknowledgments

This work is supported by the National Natural Science Foundation of China (Grant No. 91746111, Grant No. 71702143), Ministry of Education & China Mobile Joint Research Fund Program (No. MCM20160302).

## References

[1] K. Zhu, Z. Liu, L. Zhang, X. Gu, A mobile application recommendation framework by exploiting personal preference with constraints, Mobile Information Systems 2017 (2017) 9

[2] F. Grifiths, A. Lindenmeyer, J. Powell, P. Lowe, M. Thorogood, Why are health care interventions delivered over the internet? A systematic review of the published literature, Journal of Medical Internet Research 8 (2) (2006) 10.

[3] P. Krebs, D.T. Duncan, Health app use among US mobile phone owners: a national survey, JMIR mHealth and uHealth 3 (4) (2015) 101

[4] J.S. Mollee, A. Middelweerd, R.L. Kurvers, M.C. Klein, What technological features are used in smartphone apps that promote physical activity? A review and content analysis, Personal and Ubiquitous Computing 21 (4) (2017) 633–643.

[5] P. Leijdekkers, V. Gay, Mobile apps for chronic disease management: lessons learned from myFitnessCompanion®, Health and Technology 3 (2) (2013) 111–118. [6] B.E. Holtz. K.M. Murray. D.D. Hershey. J.K. Dunneback. S.R. Cotten. [6] B.E. Holtz, K.M. Murray, D.D. Hershey, J.K. Dunneback, S.R. Cotten,

A.J. Holmstrom, A. Vyas, M.K. Kaiser, M.A. Wood, Developing a patient-centered mHealth App: a tool for adolescents with type 1 diabetes and their parents, JMIR mHealth and uHealth 5 (4) (2017) e53

[7] M.A. Adriaanse, P.M. Gollwitzer, D.T. De Ridder, J.B. De Wit, F.M. Kroese, Breaking habits with implementation intentions: a test of underlying processes, Personality and Social Psychology Bulletin 37 (4) (2011) 502–513

[8] J. Stephens. J. Allen. Mobile phone interventions to increase physical activity and reduce weight: a systematic review. The Journal of Cardiovascular Nursing 28 (4) (2013) 320.

[10] B.G. Danaher, S.M. Boles, L. Akers, J.S. Gordon, H.H. Severson, Defining

participant exposure measures in web-based health behavior change programs, Journal of Medical Internet Research 8 (3) (2006) e15

[11] E.L. Murnane, D. Hufaker, G. Kossinets, Mobile health apps: adoption, adherence, and abandonment. Adiunct Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2015 ACM International Symposium on Wearable Computers, ACM, 2015, pp. 261–264.

[12] L. van Velsen, D.J. Beaujean, J.E. van Gemert-Pijnen, Why mobile health app overload drives us crazy, and how to restore the sanity, BMC Medical Informatic and Decision Making 13 (1) (2013) 23.

[13] I. Khaleel, B.C. Wimmer, G.M. Peterson, S.T.R. Zaidi, E. Roehrer, E. Cummings, K. Lee, Health information overload among health consumers: a scoping review, Patient education and counseling (2017), https://doi.org/10.1016/j.pec.

[14] C. Davidsson, S. Moritz, Utilizing implicit feedback and context to recommend mobile applications from first use. Proceedings of the 2011 Workshop on Context: awareness in Retrieval and Recommendation. ACM. 2011, pp. 19–22

[15] B.-R. Jang, Y. Noh, S.-J. Lee, S.-B. Park, A combination of temporal and general preferences for app recommendation, 2015 International Conference on Big Data and Smart Computing (BIGCOMP), IEEE, 2015, pp. 178–185.

[16] W. Pan, N. Aharony, A. Pentland, Composite social network for predicting mobile apps installation, Twenty-Fifth AAAI Conference on Artificial Intelligence, 2011.

[17] E. Costa-Montenegro, A.B. Barragáns-Martínez, M. Rey-López, Which App? A recommender system of applications in markets: implementation of the service for monitoring users' interaction, Expert systems with applications 39 (10) (2012) 9367–9375.

[18] H. Yin, L. Chen, W. Wang, X. Du, Q.V.H. Nguyen, X. Zhou, Mobi-SAGE: a sparse additive generative model for mobile App recommendation, 2017 IEEE 33rd International Conference on Data Engineering (ICDE), IEEE, 2017, pp. 75–78.

[19] C.-H. Yang, J.P. Maher, D.E. Conroy, Implementation of behavior change techniques in mobile applications for physical activity, American Journal of Preventive Medicine 48 (4) (2015) 452–455.

[20] F.H. McKay, C. Cheng, A. Wright, J. Shill, H. Stephens, M. Uccellini, Evaluating mobile phone applications for health behaviour change: a systematic review, Journal of telemedicine and telecare 24 (1) (2018) 22–30.

[21] S.Y. Komiak, I. Benbasat, The efects of personalization and familiarity on trust and adoption of recommendation agents, MIS Quarterly (2006) 941–960.

[22] S.Y. Ho, The efects of location personalization on individual's intention to us mobile services, Decision Support Systems 53 (4) (2012) 802–812.

[23] H.R. Bowles, L. Babcock, L. Lai, Social incentives for gender diferences in the propensity to initiate negotiations: sometimes it does hurt to ask. Organizational Behavior and Human Decision Processes 103 (1) (2007) 84–103.

[24] G. Kohls, J. Peltzer, B. Herpertz-Dahlmann, K. Konrad, Diferential efects of social and non-social reward on response inhibition in children and adolescents. Developmental Science 12 (4) (2009) 614–625

[25] D.J. Reid, F.J. Reid, Text or talk? Social anxiety, loneliness, and divergent preferences for cell phone use, CyberPsychology & Behavior 10 (3) (2007) 424–435.

[26] N.D. Lane, E. Miluzzo, H. Lu, D. Peebles, T. Choudhury, A.T. Campbell, A survey of mobile phone sensing, IEEE Communications Magazine 48 (9) (2010) 140–150.

[27] Y. Chen, S. Ding, Z. Xu, H. Zheng, S. Yang, Blockchain-based medical records secure storage and medical service framework, Journal of Medical Systems 43 (1) (2019) 5.

[28] G.M. Harari, S.R. Müller, M.S. Aung, P.J. Rentfrow, Smartphone sensing methods for studving behavior in evervday life. Current Opinion in Behavioral Sciences 18 (2017) 83–90.

[29] L. Pappalardo. F. Simini, Data-driven generation of spatio-temporal routines in human mobility. Data Mining and Knowledge Discovery 32 (3) (2018) 787–829.

[30] H. Huang, Y. Cheng, R. Weibel, Transport mode detection based on mobile phone network data: a systematic review, Transportation Research Part C: Emerging Technologies 101 (2019) 297–312

[31] J.D. Mazimpaka, S. Timpf, Trajectory data mining: a review of methods and applications, Journal of Spatial Information Science 2016 (13) (2016) 61–99.

[32] X. Mao, X. Zhao, J. Lin, E. Herrera-Viedma, Utilizing multi-source data in popularity prediction for shop-type recommendation. Knowledge-Based Systems 165 (2019) 253-267.

[33] A. Direito. L.P. Dale. E. Shields. R. Dobson, R. Whittaker. R. Maddison, Do physical activity and dietary smartphone applications incorporate evidence-based behaviour change techniques? BMC Public Health 14 (1) (2014) 646.

[34] D.E. Conroy, C.-H. Yang, J.P. Maher, Behavior change techniques in top-ranked mobile apps for physical activity, American Journal of Preventive Medicine 46 (6) (2014) 649–652.

[35] S. Michie, M. Richardson, M. Johnston, C. Abraham, J. Francis, W. Hardeman, M.P. Eccles, J. Cane, C.E. Wood, The behavior change technique taxonomy (v1) of 93 hierarchically clustered techniques: building an international consensus for the reporting of behavior change interventions, Annals of Behavioral Medicine 46 (1) (2013) 81–95.

[36] N. Chiang, M. Guo, K.R. Amico, L. Atkins, R.T. Lester, Interactive two-way mHealth interventions for improving medication adherence: an evaluation using the behaviour change wheel framework. JMIR mHealth and uHealth 6 (4) (2018) e87

[37] G.E. Matt, A. Dean, Social support from friends and psychological distress among elderly persons: moderator efects of age, Journal of Health and Social Behavior (1993) 187–200.

[38] L.M. Glynn, N. Christenfeld, W. Gerin, Gender, social support, and cardiovascular responses to stress, Psychosomatic Medicine 61 (2) (1999) 234–242.

[39] A.J. Nagumey, J.W. Reich, J. Newsom, Gender moderates the efects of independence and dependence desires during the social support process, Psychology and Aging 19 (1) (2004) 215.

[40] G. Dong, Y. Hu, X. Lin, Reward/punishment sensitivities among internet addicts: implications for their addictive behaviors, Progress in Neuro-Psychopharmacology and Biological Psychiatry 46 (2013) 139–145.

[41] J.P. Maher, D.E. Conroy, Habit strength moderates the efects of daily action planning prompts on physical activity but not sedentary behavior, Journal of Sport and Exercise Psychology 37 (1) (2015) 97–107.

[42] H. Cao, M. Lin, Mining smartphone data for app usage prediction and recommendations: a survey, Pervasive and Mobile Computing 37 (2017) 1–22.

[43] W.-Y. Jywe, C.-H. Liu, et al., The min-max problem for evaluating the form error of a circle, Measurement 26 (4) (1999) 273–282.

[44] S. Ding, Z. Wang, D. Wu, D.L. Olson, Utilizing customer satisfaction in ranking prediction for personalized cloud service selection, Decision Support Systems 93 (2017) 1–10.

[45] S. Ding, Z. Li, X. Liu, H. Huang, S. Yang, Diabetic complication prediction using a similarity-enhanced latent Dirichlet allocation model. Information Sciences 499 (2019) 12–24.

[46] D. Cao, X. He, L. Nie, X. Wei, X. Hu, S. Wu, T.-S. Chua, Cross-platform app recommendation by jointly modeling ratings and texts, ACM Transactions on Information Systems (TOIS) 35 (4) (2017) 37.

[47] Y. Xu, D. Zhou, J. Ma, Scholar-friend recommendation in online academic communities: an approach based on heterogeneous network, Decision Support Systems 119 (2019) 1–13.

[48] A. Castillo, D. Vander Meer, A. Castellanos, ExUP recommendations: inferring user's product metadata preferences from single-criterion rating systems, Decision Support Systems 108 (2018) 69–78.

[49] J.A. Konstan, B.N. Miller, D. Maltz, J.L. Herlocker, L.R. Gordon, J. Riedl, GroupLens: applying collaborative filtering to Usenet news, Communications of the ACM 40 (3) (1997) 77–87

[50] B. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-based collaborative filtering re commendation algorithms. Proceedings of the 10th International Conference on World Wide Web (WWW), ACM, 2001, pp. 285–295.

[51] Y. Koren, R. Bell, C. Volinsky, Matrix factorization techniques for recommende systems, Computer 42 (8) (2009) 30–37.

[52] K. Dan, A singularly valuable decomposition: the SVD of a matrix, The College Mathematics Journal 27 (1) (1996) 2–23.

[53] X. Zhou, J. He, G. Huang, Y. Zhang, A personalized recommendation algorithm based on approximating the singular value decomposition (ApproSVD), Proceedings of the The 2012 IEEE/WIC/ACM International Joint Conferences on Web Intelligence and Intelligent Agent Technology (WI-IAT), IEEE Computer Society, 2013, pp. 458–464.

[54] T.C.-K. Huang, Y.-L. Chen, M.-C. Chen, A novel recommendation model with Google similarity. Decision Support Systems 89 (2016) 17–27.

[55] Y. Pan. D. Wu. D.L. Olson. Online to offline (O2O) service recommendation method based on multi-dimensional similarity measurement. Decision Support Systems 103 (2017) 1–8.

Xiaoxin Maoreceived the bachelor degree from Central South University, China, in 2015. She is currently working toward the Ph.D. degree in management science and engineering, Xi’an Jiaotong University. Her research mainly focuses on data mining and recommendation systems

Xi Zhaoreceived the Ph.D. (Hons.) degree in computer science from the Ecole Centrale de Lyon, Lvon, France, in 2010. He conducted research in the fields of biometrics, data analytics, and pattern recognition as a Research Assistant Professor in the Department of Computer Science, University of Houston, Houston. TX. USA. He is currently a Professor with Xi’an Jiaotong University. Xi’an. China. His current research interests include behavior computing, mobile computing, and biometrics.

Yuanyuan Liureceived the Ph.D. degree from ESSEC Business School, France. She is currently an Assistant Professor in the Department of Marketing, XiŠan Jiaotong University, XiŠan, China. Her research interests include consumer behavior and behavioral decision theory.
