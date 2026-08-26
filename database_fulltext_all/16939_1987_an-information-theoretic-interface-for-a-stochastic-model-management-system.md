---
otero_id: 16939
otero_key: "39KHKJBQ"
title: "An information theoretic interface for a stochastic model management system"
authors: "Donald E. Brown"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90036-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Information Theoretic Interface for a Stochastic Model Management System

Donald E. BROWN

University of Virginia, Charlottesville, VA 22901, USA

Model management systems are intended to access, retrieve, and process models from a model base for a user in response to relatively simple commands and queries. For stochastic models a major problem is the transformation of problem specific information available to the decision maker into model parameters. The problem results from the various mixtures of incomplete, uncertain, and subjective data typical of stochastic environments. This paper proposes an interface for stochastic model management based on the information, theoretic principle of relative-entropy minimization. The Relative-Entropy Model Management System Interface (REMMSI) has the following key characteristics: (1) both subjective and objective data may be processed by the system, (2) parameter distributions are dynamically updated in the presence of new information, (3) inconsistent information provided by the user may be accepted and processed, and (4) the approach is applicable to a wide range of stochastic model management schemes.

![](/api/attachments/39KHKJBQ/fulltext/images/473c657985bb4086226bb59d5ab6ad1314c2d92dd776c9954db4c8641b37d133.jpg)

Donald E. Brown is an Assistant Professor in the Department of Systems Engineering at the University of Virginia. He received his Ph.D. in Industrial and Operations Engineering from the University of Michigan. He has designed information systems for a number of federal agencies and has also consulted for both governmental and private organizations. His current research is in the areas of knowledge representation and inference, information fusion techniques, model general design, guiding systems.

tion and management, and design aiding systems.

## 1. Introduction

The primary objective of Decision Support Systems (DSS) is to aid decision makers in semistructured problem domains. One aspect of current research in DSS has involved model management systems (MMS). These systems are intended to access, retrieve and process models from a model base for a user in response to relatively simple commands and queries. Since the modeling component is key to a DSS, the research in this area is extremely important to ensuring the extended applicability of the field.

Although no MMS are currently available a number of approaches have been proposed for their development. Some of these are based on principles from artificial intelligence, such as, semantic nets [1], predicate calculus [2], and frames [3]. Other approaches are more closely related to relational database management systems (see, for example, [4]). In all cases the primary goal is to allow the decision maker to retrieve and implement a wide range of models without mastering their technical details.

The accomplishment of this goal is a complex problem. One of the major difficulties is that models require explicit transformation of problem specific information into modeling parameters. These parameters vary widely between models even within the same problem domain. Frequently a decision maker has little or no objective data with which to derive modeling parameters. This is uniquely true for problem areas employing stochastic models. Since the questions the decision maker asks concern random phenomena, it is not surprising to find the information available frequently contains considerable uncertainty. This uncertainty is only compounded by requiring transformation of the decision maker's information into the rigid format of a model's parameters. This problem is further exacerbated by the requirement to perform this transformation every time another model is to be retrieved and run. Without an aiding mechanism these requirements on the decision maker can become exceedingly tedious.

We have said the transformation problem under uncertainty is unique to stochastic problems. While the interface proposed here is easily adaptable to deterministic environments, it is not at all clear that it is either needed or appropriate there. This is not to say that the decision makers in these instances are more capable of transforming information into parameters. However, the transformation problem is fundamentally different from the one found for stochastic models. If a deterministic model is truly the appropriate solution vehicle, then the milieu of the decision problem must contain the relevant data (hopefully in a database easily accessed by the DSS). If this is not the case then perhaps a deterministic model is not appropriate in the first place. By contrast semistructured and unstructured stochastic problems normally have various mixtures of incomplete, uncertain and subjective data from which to obtain parameters. For the remainder of this paper we focus our attention only on stochastic models and stochastic model management, although we drop the modifier and assume it to be understood.

Ideally the MMS should be capable of obtaining available information from the decision maker and automatically transforming it into parameters for the models in the model base. This paper describes a generalized interface for an MMS that is designed to accomplish this goal. The central feature of our approach is that all of the information available to the decision maker should be used in obtaining parameters for the models, but no more. The next section outlines the need for a generalized MMS interface. Section 3 briefly reviews the principles that form the basis for our interface, which is described in section 4. An example application is in section 5 and conclusions are in section 6.

## 2. Problems with Obtaining Modeling Parameters

The construction of models to aid in decision making is a complex activity normally resulting from a lengthy problem analysis. At the heart of this process is the transformation of existing information into a problem solution. In a sense the goal of the analyst is to create a model that provides a solution using only the information currently available to the decision maker. Competing with this goal is the desire for generality. Because model building is a lengthy and time consuming process, analysts seek to develop general models applicable to a large class of problems. In practice the interaction between these two competing objectives and the distortion in communicating a problem from a decision maker to an analyst result in models whose input parameters do not correspond to the existing information in the problem domain.

Fig. 1 shows the analyst's goal in model construction and the more typical result. Instead of achieving a model whose parameters are equivalent to the existing problem information, the more common result is a model that requires conversion from problem information into modeling parameters. This conversion process is generally not well defined and is likely to be a major barrier to utilization of the model. The incompatibility between existing information and the model's parameters is treated by using a feedback loop which modifies the input parameters based on an analysis of the resulting solution. This process is continued until it is felt that the model with the modified parameters closely approximates the original decision making problem.

From an MMS standpoint the situation depicted in fig. 1 represents a significant problem. In order to use any of the models within the model base of that system the information available to the decision maker must be converted into the model's parameters. There are four approaches to this problem: (1) develop conversion routines for each problem in the problem domain, (2) require the decision maker to perform the conversion, (3) require system inputs to conform to model parameters, and (4) develop a general conversion routine that uses all existing problem information, but no more. The first approach is clearly impractical since in most problem domains the number of problem variations is typically quite large. The second approach can also be dismissed since it requires the decision maker to have a detailed technical understanding of each model in the system. In the third approach the system may employ an interface to insulate the user from the detailed workings of the models. However, in this approach the user must provide enough data to estimate all of the relevant parameters in accordance with the procedures outlined by the model developers. For models based on Bayesian methods this may require obtaining additional information in the form of probability assessments. In the fourth approach the user provides only available information. The remainder of this section will describe the major problems with the third approach and, by default, imply the importance of developing a method to implement the fourth approach.

![](/api/attachments/39KHKJBQ/fulltext/images/42dd6666ee7ca022cd5d0b384a927285dbc691e06fb5c9ad2f0a148ddbaf5602.jpg)  
Fig. 1.

There are at least five disadvantages that accrue from requiring system inputs to conform to model parameters. First the requisite data may be unavailable when needed. However, subjective information may exist; the model simply has no means of using it. This is a situation typical of the early stages of planning and design, although it also occurs in a number of other situations. It is a problem which cannot be dismissed as an improper use of models since in most instances the existing models may be the only formal means of solving the particular problem. For example, in planning for a new product it is natural to determine the optimal stockage levels using an appropriate inventory model. However, for new products the distribution for demand is unknown, although less formal information about the demand may be available. If the model can only be used with a rigid input format then it will not be used at all in numerous important situations.

Second, even if the data are available they may not be useful in deriving the appropriate modeling parameters. This frequently occurs where model parameters are obtained by maximum likelihood estimation. It is not unusual to find that these estimates do not exist for the available data (for example, see [5]). This is problematical because an appropriate model and relevant data are available, although not sufficient to generate a solution. Rather than abandon the model, it is typical to apply other estimation techniques (e.g., least squares) until parameter estimates have been obtained. These ad hoc procedures are difficult to implement in a general purpose computer-based environment and they are not amenable to the inclusion of subjective information relevant to the problem.

A third problem with forcing inputs to conform to model parameters is the inflexibility of this approach to the dynamics of the decision environment. Information about a decision is normally fluid and changing. In the inventory example previously mentioned, relevant data may arrive at different times and from multiple sources concerning such things as demand for similar products in different countries or regions. The question is how to use this new information in conjunction with the previous problem solution to derive an updated solution. Application of Bayes' rule is time consuming and possibly inappropriate since it requires both assessment of a probability distribution across the entire partition of the event space and knowledge of the likelihood functions. We would like to have a method of including this new information with the previously obtained solution that does not impose additional and extraneous assessment requirements on the decision maker.

Fourth, in many cases the decision maker may not be accustomed to providing information in the format required by the applicable model. For situations where data collection is possible and capable of supporting parameter estimation, this cognitive dissonance between decision maker and model is not a problem. However, in decision environments where subjective assessments are required then a number of difficulties may arise. Considerable evidence exists to support the claim that probability distributions assessed by decision makers in complex situations are flawed (for example, [6]). Hence, by forcing the decision maker to conform the available information to the relevant model the result is of questionable validity. A better approach would allow the decision maker to input only the information about the problem available to him or her, and no more.

Finally, even when subjective information can be effectively obtained through an assessment procedure there may be additional subjective information that is ignored. In the inventory example this may be information that poor sales during the first three months after introduction of the product were due to personnel problems within the marketing agency. Results in [7] indicate that experts are particularly adept at incorporating exceptional information of this sort in decision problems. Direct parameter inputs to an MMS may easily fail to utilize this important source of information.

All of these difficulties argue forceably against developing an MMS that rigidly demands inputs only in the form of model parameters. By process of elimination we are left with the fourth approach: Develop a general interface for converting available information into parameters. The converse of the problem area described above for the third approach become goals for our approach and are described in section 4. This approach is based on results from information theory and these are summarized in the next section.

## 3. The Principle of Minimum Relative-Entropy

Information theory as a mathematical and probabilistic concept is relatively new and is based on the work of Shannon [8] and Wiener [9]. Kullback [10] provides an extensive treatment of the use of information measures for the testing of statistical hypotheses. One of these information measures proposed by Kullback and Liebler [11] was directed divergence or relative-entropy as it is currently known. Other names include cross-entropy [12], expected weight of evidence [13] and the Kullback–Liebler discriminator [14].

For discrete probability vectors, $p = (p_0, p_1, \ldots, p_M)$ and $q = (q_0, q_1, \ldots, q_M)$ the relative-entropy from $p$ to $q$ is defined as

$$
I (q, p) = \sum_ {i = 0} ^ {M} q _ {i} \ln \left(\frac {q _ {i}}{p _ {i}}\right), \quad \text { where }\tag{1}
$$

$$
\sum_ {i = 1} ^ {M} q _ {i} = \sum_ {i = 0} ^ {M} p _ {i} = 1,\tag{2}
$$

and $q_{i}, p_{i} > 0$ for $i = 0, 1, \ldots, M$ .

Justifications for the principle of are based on its properties as information measure [15], axioms of consistent inference [12], and its relationship to Bayesian inference [16]. In general relative-entropy minimization produces an updated distribution using all of the available information contained in the stated constraints and the initial distribution but no more. When information is derived from the outcomes of a sampling experiment then the relative-entropy minimum is consistent with the most likely long run result. For information in the form of a likelihood function and a prior distribution the principle of minimum relative-entropy produces the Bayesian solution. All of these characteristics make it an appropriate basis for a generalized interface to a model management system.

## 4. A Relative-Entropy Interface for Model Management

The problem of developing a generalized interface for an MMS can be treated in a straightforward manner using the principle of minimum relative-entropy. The objective of this generalized interface is to convert the existing information in a problem situation into parameters usable by the models contained in the model base. The attributes described at the end of section 2 delineate desirable features of this interface. It remains to be shown that a generalized interface based on relative-entropy is feasible and will satisfy these features.

Fig. 2 is a functional diagram of a relative-entropy model management system interface (REMMSI). There are six major subsystems in REMMSI: the preprocessor, relative-entropy minimizer, nonlinear programming module, inconsistency resolution module, data analyzer and the parameter database. Input to the system comes from the decision maker and represents information contained in the problem environment. The outputs of REMMSI are distributions for the parameters of the relevant model(s). Although it is called an interface the actual location of REMMSI within the architecture of the DSS is immaterial. It is possible, for instance, to include a natural language processor or other user interface prior to the REMMSI preprocessor. The important feature of REMMSI is that it must be in a position to convert the user supplied information into distributional information on the modeling parameters.

![](/api/attachments/39KHKJBQ/fulltext/images/6ffe4fbdf84807bc5fe86d04b453adb5fc019ca4059bb5df41ead539b8891564.jpg)  
Fig. 2. Relative-entropy model management system interface.

Operationally the systems begins by determining the relevant model or models and, hence, the relevant parameters for the decision maker's stated problem. This function is accomplished by the MMS accessing the model base. Once the relevant parameters are known the preprocessor queries the user, either directly or through another interface, about available information for each parameter. This information may be either data collected through sampling or subjective assessments by the user. In addition, the user may provide subjective information in the form of bounds, moments or functions of the parameters. Since the parameter values are unknown they are treated as random variables with unknown distributions. The preprocessor converts the user's answers into constraints on the parameters' distributions. Because the information provided is always about linear functions of the parameters the constraints formed are linear equality and inequality constraints.

The relative-entropy minimizer uses the constraints and initial distributions from both the preprocessor and parameter data base to form the relative-entropy minimization problem in (1) subject to (2) and the stated constraints. The parameter database stores the current distribution and constraints for each parameter used by the models in the model base. Without any prior information the parameters are assumed to have a diffuse initial distribution over the appropriate interval. Consistency among constraints is ensured by a procedure described below. Once the relative-entropy minimization problem has been formulated it is solved using routines in the nonlinear programming module. The updated distribution obtained by this process replaces the initial parameter distribution stored in the parameter database.

When sampling data are available the data analyzer attempts to obtain maximum likelihood estimates. If these do not exist then the user is queried for additional information with which to form constraints and a minimum relative-entropy distribution is obtained. If no additional information is available then a least squares solution is found and used as a mean value constraint for (1).

Once obtained, the updated distributions for each of the relevant parameters are passed to the MMS. The appropriate model is run and a solution to the decision maker's original problem is found. In general distributional information is passed to the MMS. It is expected that each model will use the distributional information by simple conditioning. However, if required, point estimates such as the mean or mode may also be used.

The above process is repeated for new information provided by the user. The initial distribution stored in the database is now the distribution found from the previous relative-entropy minimization. The new constraint information provided by the user is combined with that previously provided to find a new updated distribution. It is entirely possible and, in fact, to be expected that the information provided by the user will not be consistent. Inconsistent information becomes mutually exclusive constraints as generated by the preprocessor. Of course the solution to the problem in (1) subject to mutually exclusive constraints is empty. To handle this problem procedures are resident in the inconsistency resolution module to formulate a region over which the relative-entropy minimization may be performed. This is accomplished by forming disjoint sets which represent the inconsistent constraints. For example, let $E_{u}$ and $E_{v}$ represent subspaces defined by two inconsistent equality constraints. Then a new subspace, $E'$ , would be formed where $E' = E_{u} \cup E_{v}$ . In general, let $\Lambda_{2}, \Lambda_{3}, \ldots, \Lambda_{n}$ be sets corresponding to the inconsistent constraints. Since each $\Lambda_{1}$ is the finite intersection of closed and convex sets then the $\Lambda_{i}$ are closed and convex. The overall constraint set for this problem may now be defined as

$$
\Lambda = \cup_ {i = 1} ^ {n} \Lambda_ {i}.
$$

The relative-entropy minimizer now formulates the mathematical programming problem as the minimum of (1) subject to (2) and $q \in \Lambda$ .

It is also desirable to inform the user when inconsistency occurs in the information provided. This allows the user to withdraw potentially mistaken prior impressions as new information becomes available. Internally this operation deletes constraints from the parameter database.

REMMSI enjoys many of the attributes of a generalized interface. Each of these attributes is the converse of one of the problems associated with the approach described in section 2 of conforming inputs to model parameters. Table 1 summarizes our comparison of REMMSI with direct assessment methods for each of these attributes. Obviously the primary cost of using REMMSI instead of a direct assessment technique is the computational overhead needed to run it. Hence, the decision to employ REMMSI involves a trade-off between the advantages described below, and the cost of additional computations at the front end of an MMS. For most large systems, the benefits of REMMSI should far outweigh the additional computational burdens.

The first attribute of REMMSI is the capability to use the model when objective data are unavailable. This capability is clearly possessed by REMMSI since it can use subjective inputs from the decision maker or the diffuse initial distribution in its data base and still execute the models. REMMSI also possesses the second attribute since a procedure is available to use the models when existing data does not allow for parameter estimation.

A comparison of REMMSI with systems that require direct input of model parameters.

<table><tr><td>Attributes</td><td>Direct parameter input</td><td>REMMSI</td></tr><tr><td>Data unavailable</td><td>Models unusable</td><td>Models usable</td></tr><tr><td>Data insufficient for parameter estimation</td><td>Models unusable</td><td>Models usable</td></tr><tr><td>Changing information</td><td>Reassessment</td><td>Dynamic updating</td></tr><tr><td>Information format</td><td>Restricted by mode used</td><td>Constraints on the unknown distribution</td></tr><tr><td>Subjective information</td><td>Requires separate procedures</td><td>Explicitly incorporated</td></tr></table>

The third attribute, the capability to incorporate new information, is also a feature of this interface. As new information becomes available the relative-entropy minimizer explicitly adds new constraints to the optimization problem. Thus, the parameter distributions are dynamically updated as the decision environment changes. Even when the new information conflicts with previous inputs the system is capable of appropriately using this information to run the applicable model.

While REMMSI allows for the inclusion of available subjective information, the fifth attribute, there are limitations on the structure of the information that can be used. In particular information must be capable of conversion into constraints by the preprocessor. While this includes a wide variety of subjective inputs there are clearly information structures that are excluded. A potential avenue for the solution of this problem is discussed in the conclusions. Hence, REMMSI does not have all of the capabilities implied by the fourth and fifth attributes. However, it is significantly better in these areas than any other approach. The actual impact of this shortcoming is dependent on the problem environment and the amount and variety of subjectivity present. For many problem domains the approach inherent in REMMSI should prove more than adequate in accommodating the information available. In addition, this approach is general, making REMMSI easily adaptable to the plethora of model management systems being studied.

## 5. An Example Application

This section describes the application of REMMSI to a software reliability DSS. Software reliability is a field possessing numerous stochastic models that purport to describe the failure process of software. Many of the models are conceptually different. Some view reliability as a function of time and others view it as a function of program runs. Here we illustrate the use of REMMSI with the Jelinski-Moranda model (JMM) [17]. The use of REMMSI with other models is a straightforward extension of the process described here.

The JMM assumes a constant system failure rate between successive failures. Let $\lambda_{i}$ be the failure rate between failures i and $i+1$ . Then the JMM assumes $\lambda_{i}=L(K-i)$ , where L is a constant of proportionality and K is the number of faults or bugs initially present in the software. The time to failure density function after i failures is $f_{i}(t)=\exp L(K-i)t$ . Both of the parameters, K and L, must be estimated.

For our example, we suppose a software development manager would like to estimate the length of time required to completely debug a system under development. To help answer this question the MMS accesses one of the models, the JMM, in the model base. Under the assumptions of the JMM, the answer to the manager's question is

$$
\sum_ {i = 1} ^ {K} 1 / L i,\tag{3}
$$

when K and L are known. Since they are not known, REMMSI is used to obtain their distributions and, thus, to answer the manager's query.

REMMSI begins by obtaining the manager's prior distribution for $K$ . Let $p_i = \Pr\{K = i\}$ be the probabilities representing the manager's prior beliefs about the number of bugs present in the program. The values for the $p_i$ for this example are shown in table 2. From this table it is apparent that the manager believes the number of faults in the system lies between 11 and 30 with values between 15 and 25 as most likely. REMMSI combines this information with past data from similar projects. Suppose upper and lower bounds on the average number of faults found in similar developments are 18 and 15, respectively. Once these are entered into REMMSI the preprocessor develops the constraints

Initial and updated probabilities for the number of faults in the system (K).

<table><tr><td>K</td><td>Initial probabilities</td><td>Updated probabilities</td></tr><tr><td>11</td><td>0.025</td><td>0.069</td></tr><tr><td>12</td><td>0.025</td><td>0.061</td></tr><tr><td>13</td><td>0.025</td><td>0.054</td></tr><tr><td>14</td><td>0.025</td><td>0.048</td></tr><tr><td>15</td><td>0.025</td><td>0.042</td></tr><tr><td>16</td><td>0.075</td><td>0.112</td></tr><tr><td>17</td><td>0.075</td><td>0.099</td></tr><tr><td>18</td><td>0.075</td><td>0.087</td></tr><tr><td>19</td><td>0.075</td><td>0.077</td></tr><tr><td>20</td><td>0.075</td><td>0.068</td></tr><tr><td>21</td><td>0.075</td><td>0.060</td></tr><tr><td>22</td><td>0.075</td><td>0.053</td></tr><tr><td>23</td><td>0.075</td><td>0.047</td></tr><tr><td>24</td><td>0.075</td><td>0.042</td></tr><tr><td>25</td><td>0.075</td><td>0.037</td></tr><tr><td>26</td><td>0.025</td><td>0.011</td></tr><tr><td>27</td><td>0.025</td><td>0.010</td></tr><tr><td>28</td><td>0.025</td><td>0.008</td></tr><tr><td>29</td><td>0.025</td><td>0.007</td></tr><tr><td>30</td><td>0.025</td><td>0.006</td></tr></table>

$$
1 5 \geq \sum_ {i = 1 1} ^ {3 0} i q _ {i},\tag{4}
$$

$$
1 8 \leq \sum_ {i = 1 1} ^ {3 0} i q _ {i},\tag{5}
$$

where $q = (q_{11}, \ldots, q_{30})$ is the updated probability mass function for K. The relative-entropy minimizer in REMMSI forms the mathematical program: minimize (1) subject to (2), (4), and (5). The solution is found by the nonlinear programming module and is shown in table 2.

In a similar manner REMMSI finds the distribution for $L$ . It is assumed the range of $L, [l_0, l_m]$ , is partitioned into a discrete number, $I$ , of subintervals. Let $l(i)$ be the midpoint for subinterval $i$ and $q_i' = \Pr\{L = l(i)\} (i = 1, \ldots, I)$ be the sought after distribution for $L$ . For this example, we let $l_{0}=0,\quad l_{m}=2.0,\quad and\quad I=20.$ We suppose the manager has no stated prior distribution for L; REMMSI uses a diffuse prior. However, the manager does believe the system under development will average 1.2 failures per month for each fault in the system. Additionally, he or she estimates the standard deviation of this failure rate to be 0.3. With this information REMMSI forms the constraints

Updated probabilities for the failure rate per fault-month (L) by standard deviation constraint.

<table><tr><td rowspan="2">Failure rate L</td><td colspan="3">Updated probabilities</td></tr><tr><td>(SD = 0.2)</td><td>(SD = 0.3)</td><td>(SD = 0.4)</td></tr><tr><td>0.0–0.1</td><td>0.0000</td><td>0.0001</td><td>0.0027</td></tr><tr><td>0.1–0.2</td><td>0.0000</td><td>0.0003</td><td>0.0048</td></tr><tr><td>0.2–0.3</td><td>0.0000</td><td>0.0010</td><td>0.0081</td></tr><tr><td>0.3–0.4</td><td>0.0000</td><td>0.0026</td><td>0.0129</td></tr><tr><td>0.4–0.5</td><td>0.0002</td><td>0.0062</td><td>0.0197</td></tr><tr><td>0.5–0.6</td><td>0.0010</td><td>0.0132</td><td>0.0285</td></tr><tr><td>0.6–0.7</td><td>0.0046</td><td>0.0253</td><td>0.0392</td></tr><tr><td>0.7–0.8</td><td>0.0159</td><td>0.0435</td><td>0.0513</td></tr><tr><td>0.8–0.9</td><td>0.0432</td><td>0.0670</td><td>0.0640</td></tr><tr><td>0.8–1.0</td><td>0.0913</td><td>0.0929</td><td>0.0758</td></tr><tr><td>1.0–1.1</td><td>0.1505</td><td>0.1156</td><td>0.0855</td></tr><tr><td>1.1–1.2</td><td>0.1933</td><td>0.1292</td><td>0.0917</td></tr><tr><td>1.2–1.3</td><td>0.1933</td><td>0.1297</td><td>0.0936</td></tr><tr><td>1.3–1.4</td><td>0.1506</td><td>0.1170</td><td>0.0908</td></tr><tr><td>1.4–1.5</td><td>0.0914</td><td>0.0949</td><td>0.0838</td></tr><tr><td>1.5–1.6</td><td>0.0432</td><td>0.0690</td><td>0.0736</td></tr><tr><td>1.6–1.7</td><td>0.0160</td><td>0.0452</td><td>0.0615</td></tr><tr><td>1.7–1.8</td><td>0.0046</td><td>0.0265</td><td>0.0489</td></tr><tr><td>1.8–1.9</td><td>0.0010</td><td>0.0140</td><td>0.0370</td></tr><tr><td>1.9–2.0</td><td>0.0002</td><td>0.0066</td><td>0.0266</td></tr></table>

$$
\sum_ {n = 1} ^ {2 0} l (n) q _ {n} ^ {\prime} = 1. 2,\tag{6}
$$

$$
\left(\sum_ {n = 1} ^ {2 0} [ l (n) - 1. 2 ] ^ {2} q _ {n} ^ {\prime}\right) ^ {1 / 2} = 0. 2,\tag{7}
$$

and then minimizes (1) (with $p_{i}=1$ and $q_{i}^{\prime}$ replacing $q_{i}$ ) subject to (2), (6) and (7). The solution is shown in table 3 along with solutions for differing assessments of the standard deviation of the failure rate per fault-month (SD=0.2 and SD=0.4). These data clearly demonstrate that REMMSI uses the information provided by the user in an intuitively satisfying manner. If the information available indicates confidence in the assessments then the result produced and used by REMMSI is correspondingly precise. Similarly, with more vague information the interface generates a flatter distribution.

The updated distributions, q and $q'$ , are used to answer the software developer's original question concerning debugging time. Assuming K and L are independent, the solution is given by (3) and simple conditioning as

$$
\sum_ {n = 1} ^ {I} \sum_ {k = 1} ^ {M} \sum_ {i = 1} ^ {k} \frac {1}{l (n) i} q _ {k} q _ {n} ^ {\prime}.\tag{8}
$$

Using (8) and the data in tables 1 and 2 (SD = 0.3) the expected time to completely debug the system is 3.1 months.

In summary, our problem was to respond to the user's query using information of the form (4)-(7). REMMSI did this by solving (1) with the information in (4)-(7) as constraints to obtain $q$ and $q'$ for the parameters $K$ and $L$ , respectively. In doing this we assumed the available information was expressable as constraints, and, for this example, we also assumed $K$ and $L$ were independent. The results in tables 1 and 2 show that, in addition to being based on a theoretically sound procedure, REMMSI produces intuitively appealing results.

## 6. Conclusions

For MMS to be effective it is of paramount importance that information possessed by the user be readily convertible into the parameters of the selected model. For a number of reasons these systems should not require existing information to conform to the model parameters when it is entered into the system. Not the least of these reasons is the simple fact that many models will never be used.

By taking an information theoretic approach it is possible to develop an interface for an MMS that effectively uses available information. REMMSI is the embodiment of this approach. Some of the key characteristics of REMMSI are: (1) the capability to run models when the user has only subjective information or limited objective data about a parameter, (2) the facility to dynamically update parameter distributions, (3) the ability to effectively incorporate inconsistent information, and (4) the applicability of the approach to a wide range of model management schemes.

A continuing research question involves the development of techniques that will allow for the inclusion of more general forms of subjective information. The ultimate goal here would be to permit natural language expressions of this information. One approach to this problem is the use of fuzzy membership functions to describe the uncertainty of the user. These are particularly convenient because they are readily convertible into the constraints usable by REMMSI. The cost of this approach is a loss of the generally currently possessed by REMMSI since the system must maintain domain specific knowledge. Limited evidence to date suggests that REMMSI alone may be applicable to a wide range of problem domains and, thus, the need for more specific interfaces is greatly reduced.

## References

[1] Elam, J.J., J.C. Henderson and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proc. First Int. Conf. on Information Systems (Dec., 1980) 98–110.

[2] Bonczek, R.H., C.W. Holsapple and A.B. Whinston, A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management, Operations Research 29 (1981) 263–281.

[3] Dolk, D.R. and B.R. Konsynski, Knowledge Representation for Model Management Systems, IEEE Trans. Software Engin. SE-10 (1984) 619–628.

[4] Blanning, R.W., A Relational Framework for Join Implementation in Model Management Systems, Decision Support Systems 1 (1985) 69–81.

[5] Sukert, A., Empirical Validation of Three Software Error Prediction Models, IEEE Trans. Reliability R-28 (1979) 199–205.

[6] Tversky, A. and P. Kahneman, Judgement Under Uncertainty: Heuristics and Biases, Science 185 (1974) 453–458.

[7] Johnson, E.J., Expertise and Decision Under Uncertainty: Performance and Process, in: M. Chi, R. Glasser and M. Farr, eds., The Nature of Expertise (1985).

[8] Shannon, C.E., A Mathematical Theory of Communication, Bell Systems Technical Jour. 27 (1948) 379–423.

[9] Wiener, A.G., Cybernetics, 2nd ed., The MIT Press, Cambridge, MA (1948).

[10] Kullback, S., Information Theory and Statistics, Wiley, New York, NY (1959).

[11] Kullback, S. and R.A. Liebler, On Information Theory and Sufficiency, Annals of Math. Stat. 22 (1951) 79–86.

[12] Shore, J.E. and R.W. Johnson, Axiomatic Derivation of the Principle of Maximum Entropy and the Principle of Minimum Cross-Entropy, IEEE Trans. Information Theory IT-26 (1980) 26–37.

[13] Good, I.J., Probability and the Weighing of Evidence, Griffin, London (1950).

[14] Sampson, A. and R.L. Smith, Assessing Risks Through the Determinating of Rare Event Probabilities, Operations Research 30 (1982) 839–866.

[15] Hobson, A. and B.K. Cheung, A Comparison of the Shannon and Kullback Information Measures, Jour. Stat. Physics 7 (1973) 301–310.

[16] Brown, D.E., A Justification for the Principle of Minimum Cross-Entropy Entropy with Applications to Reliability and Risk Assessment, Ph.D. dissertation, University of Michigan, Ann Arbor, MI (1985).

[17] Jelinski, Z. and P.B. Moranda, Software Reliability Research, in: Walter Freiberger, ed., Statistical Computer Performance Evaluation, Academic Press, New York, NY (1972) 465–484.
