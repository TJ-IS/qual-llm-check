---
otero_id: 580
otero_key: "TKKRA898"
title: "Selection priority of process areas based on CMMI continuous representation"
authors: "Sun-Jen Huang; Wen-Ming Han"
year: "2006"
journal: "Information & Management"
doi: "10.1016/j.im.2005.08.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Selection priority of process areas based on CMMI continuous representation

Sun-Jen Huang <sup>\*</sup>, Wen-Ming Han

Department of Information Management, National Taiwan University of Science and Technology, 43, Sec. 4, Keelung Road, Taipei 106, Taiwan

Received 5 April 2004; received in revised form 2 May 2005; accepted 23 August 2005 Available online 7 October 2005

## Abstract

An essential decision that must be made by software organizations that adopt the continuous representation of the capability maturity model integration (CMMI) for software process improvement concerns a suitable path that best meets their business obiectives and mitigates the organization's risk. However, the CMMI models released by the Software Engineering Institute do not give their adopters any guidance on how to make such a decision. Thus, managers often make subjective selections of the areas in which to implement process improvement. Our study presents a decision support model that assists managers in determining the priorities of the CMMI process areas based on the characteristics of the is being developed. The proposed model was validated by using the ISBSG repository, and an example is presented to demonstrate the application of the model. Given the fact that hardly any research has yet been done on how to select the CMMI process areas to initialize process improvement, this study provides a starting point for the community in considering this important issue.

Keywords: Capability maturity model integration; Software process improvement; Critical success process areas; Project management; Information system characteristics

## 1. Introduction

A well-defined software development process can improve software quality and reduce the risks of software development projects. The Software Engineering Institute (SEI) at Carnegie Mellon University firstly released the capability maturity model for software (SW-CMM) Version 1.0 in 1991 to evaluate the maturity of software development of US Department of Defense contractors and provide a roadmap for software process improvement (SPI). The SEI solicited feedback from its adopters and then released SW-CMM

Version 1.1 in 1993 [23]. Thereafter, SW-CMM Version 1.1 became a widely accepted benchmark for software organizations in both the initiation of their SPI efforts and evaluation of the maturity of their software development processes [1,8,16]. According to the SEI maturity profile in August 2004 [25], software organizations spent an average of 2 years to raise the level of their process maturity if they choose the staged representation of a CMMI model.

Since SEI released SW-CMM Version 1.1, it has been applied to different areas; hence, many capability maturity models have been announced. These included the software acquisition CMM (SA-CMM) [6], system engineering CMM (SE-CMM) [11], integrated product development CMM (IPD-CMM) [26] and people CMM (P-CMM) [2]. These models were developed by various organizations, and so they had overlapping scopes of applications and lacked consistency in architecture, terminology, and assessment methodology. These problems have increased the cost and time to implement multiple model-based process improvement. Therefore, SEI released capability maturity model integration (CMMI) in 2001 to integrate existing capability maturity models. Its primary advantages are: in the elimination of the inconsistencies and duplication and thus streamline the enterprise-wide process improvement, in the reduction of the cost and time associated with model-based process improvement, and thus in the increase of return on investment of organizational SPI efforts [3,4].

To accommodate different process-improvement needs for software organizations, the CMMI product team provided them with two choices (staged or continuous representation) to increase the maturity of their processes. The CMM staged representation provided a framework for organizing the evolutionary steps into five levels of maturity (initial, managed, defined, quantitatively managed, and optimizing). These are ordinal scales for measuring the maturity of an organization’s software process that can also be used for its internal process improvement. SEI then added the continuous representation to the CMMI for providing flexibility to enable software organizations to choose their improvement paths. The continuous representation allows comparisons of a specific process area across software organizations. This representation therefore allowed process improvement to be compared with that of the ISO/IEC 15504 standard.

When a software organization adopts the continuous representation of a CMMI model, the foremost decision of the project manager is to select the order of implementing the process areas that best meet the organizational business objective [4]. An unsuitable path can negatively affect the results of the activities, thus reducing enthusiasm for software process improvement. However, the CMMI models currently released do not provide any guidance to software organizations adopting the CMMI continuous representation on the priorities of developing the process areas.

Recent reviews of empirical studies of software project management have indicated that a software framework must be configured according to the specific characteristics of the project [14,22,24,27]. Also an improvement path must be configured according to the specific software development environment. The characteristics of the software being developed crucially influence the choice of the path. We therefore designed a decision support model based on information system characteristics (ISC) to help adopters choose a suitable improvement path for their SPI efforts.

Table 1 Process areas in CMMI-SW/SE staged representation

<table><tr><td>Maturity level (ML)</td><td>Focus</td><td>Process area</td></tr><tr><td>ML 5: Optimizing</td><td>Continuous process improvement</td><td>Organization innovation and deployment (OID)Causal analysis and resolution (CAR)</td></tr><tr><td>ML 4: Quantitatively managed</td><td>Quantitative management</td><td>Organization process performance (OPP)Quantitative project management (QPM)</td></tr><tr><td>ML 3: Defined</td><td>Process standardization</td><td>Requirements development (RD)Technical solution (TS)Product integrated (PI)Verification (VER)Validation (VAL)Organizational process focus (OPF)Organizational process definition (OPD)Organizational training (OT)Integrated project management (IPM)Risk management (RSKM)Decision analysis and resolution (DAR)</td></tr><tr><td>ML 2: Managed</td><td>Basic project management</td><td>Requirements management (REQM)Project planning (PP)Project monitoring and control (PMC)Supplier agreement management (SAM)Measurement and analysis (MA)Process and product quality assurance (PPQA)Configuration management (CM)</td></tr><tr><td>ML 1: Initial</td><td>ad hoc process</td><td>None of process areas</td></tr></table>

## 2. Capability maturity model integration

The CMMI product suite consists of process improvement models, appraisal methods, and training materials. The CMMI process improvement framework integrated three source models (SW-CMM v2.0 draft C, EIA/IS 731, and IPD-CMM v0.98) into a single framework. The current CMMI models accommodate multiple disciplines (software engineering (SW), system engineering (SE), integrated product and process development (IPPD) and supplier sourcing (SS)) to support enterprise-wide process improvement and thus yield the benefits of an integrated model.

The primary value of CMMI is in evaluating a contractor’s ability to perform software development and to improve their capability. In the CMMI model, a process area (PA) is a cluster of related practices that are performed collectively to satisfy a set of goals, which are considered essential in making significant improvement. All CMMI process areas can be either continuous or staged.

## 2.1. Staged representation

The staged representation of CMMI organizes process areas into five maturity levels—initial (ML 1), managed (ML 2), defined (ML 3), quantitatively managed (ML 4) and optimizing (ML 5). It describes the evolution of improvements to the software development process, beginning with basic improvement practices and progressing through a predefined and proven set of successive levels.

In the staged representation, maturity levels provide a recommended order for approaching process improvement. The focus of each of five maturity levels and the predefined set of process areas are shown in Table 1. The maturity levels of an organization are measured by the achievement of the specific and generic goals that apply to each set of process areas.

## 2.2. Continuous representation

The continuous representation of a CMMI model consists of the same process areas as the staged representation. However, no process area is assigned to a particular maturity level. All process areas are organized into four process area categories—process management, project management, engineering, and support, as shown in Table 2. The continuous representation gives software organizations the flexibility to select process areas they want to improve, enabling them to select the order that best meets their business objectives or reduces the risk.

Table 2  
Process areas in CMMI-SW/SE continuous representation

<table><tr><td>Category</td><td>Process area</td><td>Maturity level</td></tr><tr><td rowspan="6">Project management</td><td>Project planning (PP)</td><td>ML 2</td></tr><tr><td>Project monitoring and control (PMC)</td><td>ML 2</td></tr><tr><td>Supplier agreement management (SAM)</td><td>ML 2</td></tr><tr><td>Integrated project management (IPM)</td><td>ML 3</td></tr><tr><td>Risk management (RSKM)</td><td>ML 3</td></tr><tr><td>Quantitative project management (QPM)</td><td>ML 4</td></tr><tr><td rowspan="5">Process management</td><td>Organizational process focus (OPF)</td><td>ML 3</td></tr><tr><td>Organizational process definition (OPD)</td><td>ML 3</td></tr><tr><td>Organizational training (OT)</td><td>ML 3</td></tr><tr><td>Organization process performance (OPP)</td><td>ML 4</td></tr><tr><td>Organization innovation and deployment (OID)</td><td>ML 5</td></tr><tr><td rowspan="6">Engineering</td><td>Requirements management (REQM)</td><td>ML 2</td></tr><tr><td>Requirements development (RD)</td><td>ML 3</td></tr><tr><td>Technical solution (TS)</td><td>ML 3</td></tr><tr><td>Product integrated (PI)</td><td>ML 3</td></tr><tr><td>Verification (VER)</td><td>ML 3</td></tr><tr><td>Validation (VAL)</td><td>ML 3</td></tr><tr><td rowspan="5">Support</td><td>Configuration management (CM)</td><td>ML 2</td></tr><tr><td>Process and product quality assurance (PPQA)</td><td>ML 2</td></tr><tr><td>Measurement and analysis (MA)</td><td>ML 2</td></tr><tr><td>Decision analysis and resolution (DAR)</td><td>ML 3</td></tr><tr><td>Causal analysis and resolution (CAR)</td><td>ML 5</td></tr></table>

The continuous representation uses six capability levels to measure the achievement of a specific process area for an organization. They are numbered 0 through 5: incomplete, performed, managed, defined, quantitatively managed, and optimizing. A capability level consists of related specific and generic practices for a process area that can improve the organization’s processes associated with that area. Capability levels build on one another, providing a recommended order for process improvement.

To initial the process improvement, an organization must first select a representation, either continuous or staged. The SEI official documentations have described some possible advantages and disadvantages of selecting each of the two representations.

## 3. Establishing a decision support for CMMI

Numerous factors affect the decision of the selection priority of process areas when a software organization chooses to use CMMI continuous representation. These factors may include the current status of the development environment, cost efficiency considerations, and the requirements of the acquirers of the IS. In the software development environment, the IS characteristic (ISC) is a key factor that affects the importance of the CMMI process areas on performance.

An ISC, such as transaction rate and the friendliness of the user interface, is an attribute that represents a specific behavioral characteristic. IS can be distinguished by their characteristics. For example, batch processing systems have lower transaction rate than real-time ones [18].

Each type of software systems has different characteristics [10,12,20], so the relative importance of each process area varies [21]. For example, executive information systems (EIS) emphasize an unstructured capability to help senior managers identify problems, find and evaluate alternative solutions, and compare and select alternatives. Therefore, the process areas of both requirements management and requirements development for EIS are more important than for a transaction processing system. The process area of configuration management is relatively important for IS developed on multiple sites. A software organization must apply more SPI effort to the technical solution when developing a real-time information system.

## 3.1. Used characteristics of IS

Allan Albrecht initially proposed function point analysis (FPA) to measure the functional size of software. The international function point user group (IFPUG) was announced in 1984 to clarify the counting rules and promote its use and evolution. The most recent Release 4.2 of the function point counting practice manual (CPM) was delivered in 2004 and its unadjusted function point (UFP) became an internationally standardized method of measuring functional size. This has become one of the most widely used metrics in the software measurement community and has been expanded to estimating development cost, outsourcing contracts, and conducting benchmark studies.

Table 3 Information system characteristics

<table><tr><td>General system characteristics</td><td>Definition</td></tr><tr><td>Transaction rate (TR)</td><td>TR describes the degree to which the rate of business transactions influenced the development of the application</td></tr><tr><td>Distributed data processing (DDP)</td><td>DDP describes the degree to which the application transfers data among components of the application</td></tr><tr><td>Data communication (DC)</td><td>DC describes the degree of influence for each general system characteristic</td></tr><tr><td>Installation easy (IE)</td><td>IE describes the degree to which conversion from previous environments influenced the development of the application</td></tr><tr><td>Complex processing (CP)</td><td>CP describes the degree to which processing logic influenced the development of the application</td></tr><tr><td>Heavily used configuration (HUC)</td><td>HUC describes the degree to which computer resource restrictions influenced the development of the application</td></tr><tr><td>Multiple sites (MS)</td><td>MS describes the degree to which the application has been developed for multiple locations and user organizations</td></tr><tr><td>Performance (PER)</td><td>PER describes the degree to which response time and throughput performance considerations influenced the application development</td></tr><tr><td>Reusability (REU)</td><td>REU describes the degree to which the application and the code in the application have been specifically designed, developed, and supported to be usable in other applications</td></tr><tr><td>Online data entry (ODE)</td><td>ODE describes the degree to which data is entered through interactive transactions</td></tr><tr><td>Online update (OU)</td><td>OU describes the degree to which internal logical files are updated online</td></tr><tr><td>End user efficiency (EUE)</td><td>EUE describes the degree of consideration for human factors and ease of use for the user of the application measured</td></tr><tr><td>Operational easy (OE)</td><td>OE describes the degree to which the application attends to operational aspects, such as start-up, back-up, and recovery processes</td></tr><tr><td>Facilitate charge (FC)</td><td>FC describes the degree to which the application has been developed for easy modification of processing logic or data structure</td></tr></table>

The Release 4.2 defines 14 general system characteristics (GSC) for evaluating the overall complexity of a software application, given by as value adjustment factor. Each characteristic has associated descriptions that help determine the degree of influence (DI) of that characteristic, which ranges from zero to five, indicating no influence to strong influence.

We used the GSC as ISC to build a decision support model, because the definitions and guidelines of all GSC are both clear and objective in determining their DI. Furthermore, numerous history data about GSC were available to verify our model. Table 3 defines the GSC and Table 4 presents the guidelines for determining the DI of the transaction rate characteristic. For other characteristics, refer to [15].

## 3.2. Procedures in building the model

A questionnaire was first designed to investigate the importance of each information system characteristic on the CMMI process areas, and then the optimal aggregation method (OAM) [19] was employed to aggregate individual expert fuzzy opinions into a group consensus. The OAM ensures that the aggregation is good and deals with any situation in which the experts do not agree. The optimization is an opinion with the minimum of the sum of weighted dissimilarities between the aggregated opinion and each individual opinion.

The model-building procedures are described in the following steps:

(1) A questionnaire<sup>1</sup> was first developed based on 22 process areas in the CMMI-SE/SW continuous representation and 14 ISCs; then it was pre-tested by six SPI personnel in domestic software companies and six graduate students at the authors’ university. In our analysis, the pre-test of the expert questionnaire yielded a high average Cronbach alpha of 0.82, indicating that the questionnaire was highly internally consistent<sup>2</sup>. After pre-testing, 30 questionnaires were sent to senior SPI managers and consultants in the software industry and scholars in universities in Taiwan, who had attended two SEI official courses (introduction to CMMI and intermediate of CMMI) to ensure the reliability of the collected data. Fifteen valid questionnaires were obtained after one follow-up latter or telephone call, yielding a net response rate 50%.

Determination of degree of influence for transaction rate characteristic

<table><tr><td>Score as</td><td>Descriptions to determine degree of influence</td></tr><tr><td>0</td><td>No peak transaction period is anticipated</td></tr><tr><td>1</td><td>Peak transaction period (e.g., monthly, quarterly, seasonally, annually) is anticipated</td></tr><tr><td>2</td><td>Weekly peak transaction period is anticipated</td></tr><tr><td>3</td><td>Daily peak transaction period is anticipated</td></tr><tr><td>4</td><td>High transaction rate(s) stated by the user in the application requirements or service level agreements are high enough to require performance analysis tasks in the design phase</td></tr><tr><td>5</td><td>High transaction rate(s) stated by the user in the application requirements or service level agreements are high enough to require performance analysis tasks and, in addition, require the use of performance analysis tools in the design, development, and/or installation phases</td></tr></table>

(2) Each questionnaire respondent $i \ ( i = 1 , \ 2 , \ . \ . \ . , \ n )$ constructed a positive triangular fuzzy number $E _ { i } =$ $( a _ { i } ^ { \mathrm { l o w } } , b _ { i } ^ { \mathrm { m e a n } } , c _ { i } ^ { \bar { \mathrm { u p p e r } } } )$ to represent the ith expert’s subjective estimate of the importance of each information system characteristic that affects the CMMI process areas. The scale incorporates strong influence, high influence, medium influence, weak influence and slight influence.

(3) The aggregation weights were set to $0 < W _ { i } ^ { x } < 1$ and $\begin{array} { r } { \sum _ { i = 1 } ^ { \bar { n } } \bar { W } _ { i } ^ { x } = 1 } \end{array}$ , where i represents the ith expert, n the number of experts (the value is 15 in our study), and x refers to the xth iteration (whose value is set to 0 initially).

(4) Let $R ^ { x + 1 } = f ( R _ { 1 } , R _ { 2 } , R _ { 3 } , . . . , R _ { n } )$ be the consensus of opinions; then calculate the opinion distance $d ( R ^ { x + 1 }$ $E _ { i } )$ between the aggregated result $R ^ { x + 1 }$ and expert opinion $E _ { i } ,$ , which is a positive triangular fuzzy number.

$$
d \left(R ^ {x + 1}, E _ {i}\right) = \left(\sum_ {i = 1} ^ {3} \left(\left| R ^ {x + 1} - E _ {i} \right|\right)\right)\tag{1}
$$

Let u be the universe of discourse and define as $m a x ( u ) - m i n ( u )$ ; then the opinion similarity denoted by $S ( R ^ { x + 1 } , E _ { i } )$ between the aggregated result $R ^ { x + 1 }$ and expert opinion $E _ { i }$ is computed pairwise and its computation is defined as

Table 5  
Weights of all information system characteristics that affect process areas

<table><tr><td rowspan="2"></td><td colspan="7">ML 2</td><td colspan="4">ML 3</td></tr><tr><td>REQM</td><td>PP</td><td>PMC</td><td>SAM</td><td>CM</td><td>MA</td><td>PPQA</td><td>RD</td><td>TS</td><td>PI</td><td>VER</td></tr><tr><td>TR</td><td>0.43</td><td>0.50</td><td>0.35</td><td>0.45</td><td>0.24</td><td>0.56</td><td>0.39</td><td>0.37</td><td>0.45</td><td>0.69</td><td>0.50</td></tr><tr><td>DDP</td><td>0.61</td><td>0.60</td><td>0.48</td><td>0.55</td><td>0.47</td><td>0.61</td><td>0.50</td><td>0.78</td><td>0.66</td><td>0.83</td><td>0.56</td></tr><tr><td>DC</td><td>0.59</td><td>0.57</td><td>0.69</td><td>0.67</td><td>0.53</td><td>0.79</td><td>0.74</td><td>0.69</td><td>0.68</td><td>0.64</td><td>0.71</td></tr><tr><td>IE</td><td>0.72</td><td>0.72</td><td>0.57</td><td>0.76</td><td>0.55</td><td>0.50</td><td>0.61</td><td>0.74</td><td>0.68</td><td>0.80</td><td>0.74</td></tr><tr><td>CP</td><td>0.68</td><td>0.51</td><td>0.37</td><td>0.49</td><td>0.40</td><td>0.64</td><td>0.41</td><td>0.78</td><td>0.46</td><td>0.62</td><td>0.49</td></tr><tr><td>HUC</td><td>0.71</td><td>0.47</td><td>0.40</td><td>0.43</td><td>0.51</td><td>0.48</td><td>0.32</td><td>0.59</td><td>0.61</td><td>0.43</td><td>0.58</td></tr><tr><td>MS</td><td>0.73</td><td>0.62</td><td>0.55</td><td>0.61</td><td>0.36</td><td>0.59</td><td>0.59</td><td>0.76</td><td>0.71</td><td>0.70</td><td>0.60</td></tr><tr><td>PER</td><td>0.69</td><td>0.47</td><td>0.51</td><td>0.51</td><td>0.57</td><td>0.64</td><td>0.44</td><td>0.61</td><td>0.61</td><td>0.54</td><td>0.58</td></tr><tr><td>REU</td><td>0.52</td><td>0.52</td><td>0.57</td><td>0.59</td><td>0.39</td><td>0.69</td><td>0.56</td><td>0.68</td><td>0.60</td><td>0.65</td><td>0.63</td></tr><tr><td>ODE</td><td>0.62</td><td>0.61</td><td>0.56</td><td>0.67</td><td>0.73</td><td>0.68</td><td>0.73</td><td>0.69</td><td>0.77</td><td>0.62</td><td>0.65</td></tr><tr><td>OU</td><td>0.51</td><td>0.56</td><td>0.38</td><td>0.62</td><td>0.53</td><td>0.50</td><td>0.51</td><td>0.59</td><td>0.58</td><td>0.72</td><td>0.57</td></tr><tr><td>EUE</td><td>0.73</td><td>0.52</td><td>0.63</td><td>0.75</td><td>0.71</td><td>0.65</td><td>0.74</td><td>0.69</td><td>0.69</td><td>0.65</td><td>0.65</td></tr><tr><td>OE</td><td>0.50</td><td>0.58</td><td>0.40</td><td>0.75</td><td>0.49</td><td>0.52</td><td>0.59</td><td>0.56</td><td>0.66</td><td>0.75</td><td>0.58</td></tr><tr><td>FC</td><td>0.65</td><td>0.44</td><td>0.46</td><td>0.66</td><td>0.37</td><td>0.49</td><td>0.64</td><td>0.72</td><td>0.65</td><td>0.65</td><td>0.55</td></tr></table>

ML 3

<table><tr><td></td><td>VAL</td><td>OPF</td><td>OPD</td><td>OT</td><td>IPM</td><td>RSKM</td><td>DAR</td><td>OPP</td><td>QPM</td><td>CAR</td><td>OID</td></tr><tr><td>TR</td><td>0.44</td><td>0.20</td><td>0.52</td><td>0.31</td><td>0.48</td><td>0.27</td><td>0.56</td><td>0.37</td><td>0.31</td><td>0.52</td><td>0.23</td></tr><tr><td>DDP</td><td>0.65</td><td>0.47</td><td>0.33</td><td>0.35</td><td>0.56</td><td>0.65</td><td>0.69</td><td>0.57</td><td>0.55</td><td>0.59</td><td>0.47</td></tr><tr><td>DC</td><td>0.60</td><td>0.44</td><td>0.70</td><td>0.61</td><td>0.49</td><td>0.46</td><td>0.70</td><td>0.46</td><td>0.70</td><td>0.69</td><td>0.37</td></tr><tr><td>IE</td><td>0.70</td><td>0.47</td><td>0.71</td><td>0.65</td><td>0.35</td><td>0.79</td><td>0.73</td><td>0.71</td><td>0.64</td><td>0.57</td><td>0.33</td></tr><tr><td>CP</td><td>0.51</td><td>0.38</td><td>0.61</td><td>0.36</td><td>0.56</td><td>0.70</td><td>0.62</td><td>0.70</td><td>0.62</td><td>0.53</td><td>0.34</td></tr><tr><td>HUC</td><td>0.48</td><td>0.50</td><td>0.50</td><td>0.61</td><td>0.37</td><td>0.32</td><td>0.37</td><td>0.36</td><td>0.47</td><td>0.35</td><td>0.37</td></tr><tr><td>MS</td><td>0.72</td><td>0.57</td><td>0.59</td><td>0.69</td><td>0.62</td><td>0.51</td><td>0.55</td><td>0.47</td><td>0.52</td><td>0.53</td><td>0.43</td></tr><tr><td>PER</td><td>0.48</td><td>0.47</td><td>0.42</td><td>0.66</td><td>0.37</td><td>0.50</td><td>0.51</td><td>0.33</td><td>0.47</td><td>0.35</td><td>0.41</td></tr><tr><td>REU</td><td>0.54</td><td>0.28</td><td>0.30</td><td>0.51</td><td>0.40</td><td>0.64</td><td>0.73</td><td>0.51</td><td>0.60</td><td>0.63</td><td>0.28</td></tr><tr><td>ODE</td><td>0.50</td><td>0.50</td><td>0.63</td><td>0.70</td><td>0.57</td><td>0.37</td><td>0.72</td><td>0.65</td><td>0.62</td><td>0.46</td><td>0.51</td></tr><tr><td>OU</td><td>0.52</td><td>0.45</td><td>0.56</td><td>0.53</td><td>0.55</td><td>0.55</td><td>0.60</td><td>0.50</td><td>0.49</td><td>0.46</td><td>0.38</td></tr><tr><td>EUE</td><td>0.72</td><td>0.72</td><td>0.70</td><td>0.69</td><td>0.72</td><td>0.65</td><td>0.71</td><td>0.72</td><td>0.54</td><td>0.61</td><td>0.55</td></tr><tr><td>OE</td><td>0.53</td><td>0.41</td><td>0.56</td><td>0.56</td><td>0.36</td><td>0.66</td><td>0.62</td><td>0.59</td><td>0.58</td><td>0.34</td><td>0.38</td></tr><tr><td>FC</td><td>0.53</td><td>0.56</td><td>0.58</td><td>0.59</td><td>0.53</td><td>0.57</td><td>0.61</td><td>0.53</td><td>0.46</td><td>0.52</td><td>0.44</td></tr></table>

$$
S (R ^ {x + 1}, E _ {i}) = 1 - \frac {1}{3 u} (d (R ^ {x + 1}, E _ {i}))\tag{2}
$$

where $0 \leq ( R ^ { x + 1 } , ~ E _ { i } ) \leq 1$ and $S ( R ^ { x + 1 } , \ E _ { i } ) = S ( E _ { i }$ $R ^ { x + 1 } )$

(5) Calculate the aggregated opinion $\boldsymbol { R } ^ { x + 1 }$ , which is defined as

$$
R ^ {x + 1} = \frac {1}{\sum_ {i = 1} ^ {n} (W _ {i} ^ {x}) ^ {m}} \sum_ {i = 1} ^ {n} ((W _ {i} ^ {x}) ^ {m} E _ {i})\tag{3}
$$

where $E _ { i } ( i = 1 , . . . , n )$ is the individual opinion, $W _ { i } ^ { x }$ the weight of the opinion of the ith expert at the xth iteration, m called exponential weight is introduced for reducing the influence of ‘‘noise’’ when computing the central consensus, its value is suggested to set 2 in order to obtain better convergence of individual opinions.

(6) Calculate the weight of the ith expert at the (x + 1)th iteration $\boldsymbol { W } _ { i } ^ { x + 1 }$ <sup>1</sup>, which is defined as

$$
W _ {i} ^ {x + 1} = \frac {\left(1 / (c - S (R ^ {x + 1} , E _ {i}))\right) ^ {1 / (m - 1)}}{\sum_ {i = 1} ^ {n} \left(1 / (c - S (R ^ {x + 1} , E _ {i}))\right) ^ {1 / (m - 1)}}\tag{4}
$$

where c is a constant (set to 1.5 herein) used to adjust the effect of aggregation. If c approaches infinity, then $w _ { i } = 1 / n ;$ that is, the aggregated opinion is the average of all expert opinions. If c approaches 1, then the aggregated opinion is equal to one of opinions.

Table 6 Illustrative example

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">PP</td><td colspan="2">PMC</td><td colspan="2">SAM</td><td colspan="2">REQM</td><td colspan="2">CM</td><td colspan="2">MA</td><td colspan="2">PPQA</td></tr><tr><td> $W_{pp}$ </td><td> $\mathsf{PP}_{\text{isc}}$ </td><td> $W_{\text{PMC}}$ </td><td> $\mathsf{PMC}_{\text{isc}}$ </td><td> $W_{\text{SAM}}$ </td><td> $\mathsf{SAM}_{\text{isc}}$ </td><td> $W_{\text{REQM}}$ </td><td> $\mathsf{REQM}_{\text{isc}}$ </td><td> $W_{\text{CM}}$ </td><td> $\mathsf{CM}_{\text{isc}}$ </td><td> $W_{\text{MA}}$ </td><td> $\mathsf{MA}_{\text{isc}}$ </td><td> $W_{\text{PPQA}}$ </td><td> $\mathsf{PPQA}_{\text{isc}}$ </td></tr><tr><td>TR</td><td>3</td><td>0.50</td><td>1.50</td><td>0.35</td><td>1.05</td><td>0.45</td><td>1.35</td><td>0.43</td><td>1.29</td><td>0.24</td><td>0.72</td><td>0.56</td><td>1.68</td><td>0.39</td><td>1.17</td></tr><tr><td>DDP</td><td>2</td><td>0.60</td><td>1.20</td><td>0.48</td><td>0.96</td><td>0.55</td><td>1.10</td><td>0.61</td><td>1.22</td><td>0.47</td><td>0.94</td><td>0.61</td><td>1.22</td><td>0.50</td><td>1.00</td></tr><tr><td>DC</td><td>2</td><td>0.57</td><td>1.14</td><td>0.69</td><td>1.38</td><td>0.67</td><td>1.34</td><td>0.59</td><td>1.18</td><td>0.53</td><td>1.06</td><td>0.79</td><td>1.58</td><td>0.74</td><td>1.48</td></tr><tr><td>IE</td><td>5</td><td>0.72</td><td>3.60</td><td>0.57</td><td>2.85</td><td>0.76</td><td>3.80</td><td>0.72</td><td>3.60</td><td>0.55</td><td>2.75</td><td>0.50</td><td>2.50</td><td>0.61</td><td>3.05</td></tr><tr><td>CP</td><td>4</td><td>0.51</td><td>2.04</td><td>0.37</td><td>1.48</td><td>0.49</td><td>1.96</td><td>0.68</td><td>2.72</td><td>0.40</td><td>1.6</td><td>0.64</td><td>2.56</td><td>0.41</td><td>1.64</td></tr><tr><td>HUC</td><td>2</td><td>0.47</td><td>0.94</td><td>0.40</td><td>0.80</td><td>0.43</td><td>0.86</td><td>0.71</td><td>1.42</td><td>0.51</td><td>1.02</td><td>0.48</td><td>0.96</td><td>0.32</td><td>0.64</td></tr><tr><td>MS</td><td>5</td><td>0.62</td><td>3.10</td><td>0.55</td><td>2.75</td><td>0.61</td><td>3.05</td><td>0.73</td><td>3.65</td><td>0.36</td><td>1.80</td><td>0.59</td><td>2.95</td><td>0.59</td><td>2.95</td></tr><tr><td>PER</td><td>4</td><td>0.47</td><td>1.88</td><td>0.51</td><td>2.04</td><td>0.51</td><td>2.04</td><td>0.69</td><td>2.76</td><td>0.57</td><td>2.28</td><td>0.64</td><td>2.56</td><td>0.44</td><td>1.76</td></tr><tr><td>REU</td><td>2</td><td>0.52</td><td>1.04</td><td>0.57</td><td>1.14</td><td>0.59</td><td>1.18</td><td>0.52</td><td>1.04</td><td>0.39</td><td>0.78</td><td>0.69</td><td>1.38</td><td>0.56</td><td>1.12</td></tr><tr><td>ODE</td><td>2</td><td>0.61</td><td>1.22</td><td>0.56</td><td>1.12</td><td>0.67</td><td>1.34</td><td>0.62</td><td>1.24</td><td>0.73</td><td>1.46</td><td>0.68</td><td>1.36</td><td>0.73</td><td>1.46</td></tr><tr><td>OU</td><td>5</td><td>0.56</td><td>2.80</td><td>0.38</td><td>1.90</td><td>0.62</td><td>3.10</td><td>0.51</td><td>2.55</td><td>0.53</td><td>2.65</td><td>0.50</td><td>2.50</td><td>0.51</td><td>2.55</td></tr><tr><td>EUE</td><td>2</td><td>0.52</td><td>1.04</td><td>0.63</td><td>1.26</td><td>0.75</td><td>1.50</td><td>0.73</td><td>1.46</td><td>0.71</td><td>1.42</td><td>0.65</td><td>1.30</td><td>0.74</td><td>1.48</td></tr><tr><td>OE</td><td>2</td><td>0.58</td><td>1.16</td><td>0.40</td><td>0.80</td><td>0.75</td><td>1.50</td><td>0.50</td><td>1.00</td><td>0.49</td><td>0.98</td><td>0.52</td><td>1.04</td><td>0.59</td><td>1.18</td></tr><tr><td>FC</td><td>2</td><td>0.44</td><td>0.88</td><td>0.46</td><td>0.92</td><td>0.66</td><td>1.32</td><td>0.65</td><td>1.30</td><td>0.37</td><td>0.74</td><td>0.49</td><td>0.98</td><td>0.64</td><td>1.28</td></tr><tr><td>Total</td><td></td><td></td><td>23.54</td><td></td><td>20.45</td><td></td><td>25.44</td><td></td><td>26.43</td><td></td><td>20.2</td><td></td><td>24.57</td><td></td><td>22.76</td></tr></table>

(7) If $\begin{array} { r } { \sum _ { i = 1 } ^ { n } \left| W _ { i } ^ { x + 1 } - W _ { i } ^ { x } \right| < \varepsilon , } \end{array}$ optimality has been attained and the iteration is terminated; otherwise, set $x = x + 1$ and go to step (5).

(8) Three defuzzification algorithms—center of gravity defuzzification [5], distance measurement defuzzification [9] and central value defuzzification [7] were used to obtain a single weight of each information system characteristic that affected a particular process area. Finally, the importance of each characteristic affecting a process area was defined as the mean of the above three defuzzification values. Table 5 summarizes the results.

## 3.3. Illustrative example

The use of the decision support model is illustrated using an example with seven process areas (PP, PMC, SAM, REQM, CM, MA and PPQA) on the managed maturity level of a CMMI model.

Step 1: Determining DI values of 14 ISC

The project manager assessed the DI for each of 14 ISC according to the function point counting practice manual. The DI of each is shown in the second column of Table 6.

## Step 2: Prioritizing the process areas

Multiplying the values of DI of all 14 characteristics by their weights, as shown in Table 5, yielded the importance of each process area for the application. Table 6 summarizes the results for the seven process areas on the CMMI managed maturity level. The total score in Table 6 indicated the relative importance of process areas based on the 14 characteristics of a specific IS. The difference between the maximum and minimum scores was 6.23, indicating the difference of importance degrees of two process areas: requirements management and configuration management.

Step 3: Identifying the critical success process areas Based on these results, two process areas (REQM and SAM) had higher weights and could thus be regarded as the critical success process areas here. Project managers, therefore, were required to spend more effort on these process areas to improve the development process.

## 4. Verification

As IS of the same type have the same characteristics, the rankings of the importance of 22 process areas for information systems of the same type should be significantly related. Therefore, the historical data in the International Software Benchmarking Standards Group (ISBSG) Repository 7 were employed to verify the effectiveness of the proposed decision support model that was used for setting the priorities of the CMMI process areas. The ISBSG is a non-profit international organization, which maintains a software measurement repository that contains numerous software project data from more than 20 countries worldwide. Most of the data were collected from the USA, Australia, Canada, the UK, The Netherlands and

![](/api/attachments/TKKRA898/fulltext/images/d986ac74c7c277cb184293d76a7ecf984380754b8968e3bbb410ec6e5868a6c1.jpg)  
Fig. 1. Historical software project data in ISBSG used to verify the model.

France. It asserts that these data are representatives of some of better software development projects around the world [17].

Repository Release 7 contains 1238 historical software project data, each containing 52 fields. This study used 16: function point standard, application type, and all 14 general system characteristics. Two criteria were imposed to select the historical data to ensure its quality: the function point standard had to be based on IFPUG 3.0 or above and all 16 fields had to be complete.

A total of 421 of the selected historical data were employed to verify the decision support model. Among these, there were eight types of IS: management information, transaction/production, office information, network management, decision support, real time, electronic data interchange, and executive information. The historical data on each type of IS is shown in Fig. 1.

The Spearman’s rank correlation coefficient, denoted by $r _ { \mathrm { s } } ,$ was used to measure the correlation of the ranks of the importance of 22 process areas for IS of the same type. The coefficient $r _ { \mathrm { s } }$ is a non-parametric measure of association that indicates whether the ranks of data in two ordered sets are highly correlated. The formula for the rank correlation coefficient $r _ { \mathrm { s } }$ is defined next; its value ranges from 1 (a perfect positive correlation) to 1 (a perfect negative correlation):

$$
r _ {\mathrm{s}} = 1 - \frac {6 \sum d _ {i} ^ {2}}{n (n ^ {2} - 1)}\tag{5}
$$

Table 7  
Spearman’s rank correlation coefficient $r _ { s }$ for each type of application

<table><tr><td>Application type</td><td> $r_s$ </td><td> $\mu$ </td><td> $\sigma$ </td></tr><tr><td>Decision support system</td><td>1–0.892</td><td>0.973</td><td>0.024</td></tr><tr><td>Executive information system</td><td>1–0.874</td><td>0.952</td><td>0.047</td></tr><tr><td>Electronic data interchange</td><td>0.993–0.928</td><td>0.972</td><td>0.026</td></tr><tr><td>Network management</td><td>1–0.910</td><td>0.950</td><td>0.042</td></tr><tr><td>Office information system</td><td>1–0.927</td><td>0.965</td><td>0.020</td></tr><tr><td>Real time system</td><td>1–0.897</td><td>0.963</td><td>0.027</td></tr><tr><td>Transaction system</td><td>1–0.881</td><td>0.957</td><td>0.024</td></tr><tr><td>Management information system</td><td>1–0.855</td><td>0.929</td><td>0.048</td></tr></table>

where $d _ { i }$ is the difference between the ranks of importance of the ith process area in two ordered sets and n is the number of process areas, which is 22.

Spearman’s rank correlation coefficients using twotailed test and $\alpha = 0 . 0 1$ , shown in Table 7, indicated that the ranks of the priorities of 22 process areas in IS of the same type were significantly related.

## 5. Analysis and findings

One of the questions frequently asked by software organizations that are considering using the CMMI continuous representation is: What are the critical success process areas in the four categories of process areas of the model? Another question is: Which areas of a specific software system under development are needed irrespective of the representation selected for process improvement?

## 5.1. Results of analysis based on staged and continuous representations

The two most important process areas in the four categories of process areas in the CMMI continuous representation are shown in Table 8. These can be treated as the critical success process areas (CSPA) when software organizations adopt the CMMI continuous representation for their process improvement. In the project management category, the CSPA are:

Critical success process areas in the CMMI continuous representation  
Table 8

<table><tr><td>Category</td><td colspan="2">Critical success process areas</td></tr><tr><td>Project management</td><td>Supplier agreement management (ML 2)</td><td>Project planning (ML 2)</td></tr><tr><td>Process management</td><td>Organizational training (ML 3)</td><td>Organizational process definition (ML 3)</td></tr><tr><td>Support</td><td>Decision analysis and resolution (ML 3)</td><td>Measurement and Analysis (ML 2)</td></tr><tr><td>Engineering</td><td>Product integrated (ML3)</td><td>Requirements development (ML3)</td></tr></table>

Table 9  
Critical success process areas in the CMMI staged representation

<table><tr><td>Maturity level</td><td colspan="2">Critical success process areas</td></tr><tr><td>Managed</td><td>Requirements management (engineering)</td><td>Measurement and analysis (support)</td></tr><tr><td>Defined</td><td>Requirements development (engineering)</td><td>Product integrated (engineering)</td></tr><tr><td>Quantitatively managed</td><td>Quantitative project management (project management)</td><td></td></tr><tr><td>Optimizing</td><td>Causal analysis and resolution (support)</td><td></td></tr></table>

supplier agreement management and project planning. These are on the managed maturity level in the CMMI staged representation.

In the process management category, the CSPA are: organizational training and organization process definition. These are on the defined maturity level. In the support category, the CSPA are: decision analysis and resolution and measurement and analysis. These are on the defined and managed maturity levels, respectively. In the engineering category, the CSPA are: product integration and requirements development. They are on the defined maturity level. Notably, all CSPA are on the managed and defined maturity levels in the staged representation of a CMMI model.

Table 9 presents CSPA based on the maturity level in the CMMI staged representation. For the managed maturity level, the CSPA are REQM and MA, which are in the engineering and support categories, respectively. For the defined maturity level, the CSPA are RD and PI in the engineering category. For the quantitatively managed level, the critical success process area is QPM, which is in the project management category. For the optimizing maturity level, the critical success process area is CAR in the support category.

It is worth noting that REQM, RD, MA, and PI are more important than the other process areas in the CMMI managed and defined maturity levels: 80% (347/ 421) of the historical data in our study were software applications in MIS and transaction/production systems.

## 5.2. Results of analysis based on IS characteristics

Table 10 presents the two most important process areas associated with each of the IS characteristics. When a software organization develops a specific software system, the project manager should first determine the characteristics of the system and then identify the critical success process areas shown in Table 10. During the life cycle of software development, an organization should emphasize the activities and practices in those CSPA of the CMMI reference model.

Table 10  
Critical success process areas based on information system characteristics

<table><tr><td>ISC</td><td>CSPA</td><td>ISC</td><td>CSPA</td></tr><tr><td rowspan="2">Data communication</td><td>Product integration</td><td>On-line update</td><td>Requirements management</td></tr><tr><td>Measurement and analysis</td><td></td><td>Organizational training</td></tr><tr><td rowspan="2">Distributed data processing</td><td>Product integration</td><td>Complex processing</td><td>Causal analysis and resolution</td></tr><tr><td>Requirements development</td><td></td><td>Measurement and analysis</td></tr><tr><td rowspan="2">Performance</td><td>Measurement and analysis</td><td>Reusability</td><td>Technical solution</td></tr><tr><td>Process and product quality assurance</td><td></td><td>Process and product quality assurance</td></tr><tr><td rowspan="2">Heavily used configuration</td><td>Product integration</td><td>Installation ease</td><td>Product integration</td></tr><tr><td>Risk management</td><td></td><td>Supplier agreement management</td></tr><tr><td rowspan="2">Transaction rate</td><td>Requirements development</td><td>Operational ease</td><td>Supplier agreement management</td></tr><tr><td>Risk management</td><td></td><td>Process and product quality assurance</td></tr><tr><td rowspan="2">Online data entry</td><td>Requirements management</td><td>Multiple sites</td><td>Supplier agreement management</td></tr><tr><td>Organizational training</td><td></td><td>Product integration</td></tr><tr><td rowspan="2">End user efficiency</td><td>Requirements development</td><td>Facilitate change</td><td>Requirements development</td></tr><tr><td>Requirements management</td><td></td><td>Supplier management agreement</td></tr></table>

## 6. Conclusions

Pursuing efficient and effective software process improvement is a major goal of software organizations committed to producing high-quality software within a reasonable budget and time. Many software organizations worldwide are adopting the continuous representation of the CMMI model. However, they frequently encounter difficulty of selecting suitable process areas in which to initiate their effort. The current CMMI models do not, however, provide any means of determining the priorities of process areas; thus managers often make a subjective decision when selecting the CMMI process area.

Many factors, such as business objectives, project risks, and available resources, can influence an organization’s decision of an appropriate path that is suited to its environment. Thus, building a formal model that captures the factors that affect the selection of the CMMI process areas is difficult. Our model is intended to aid in this process. It was validated by using the ISBSG Repository, and an example provided. The validation revealed that significant rank correlations exist among process areas across eight types of information systems in the ISBSG, indicating the soundness of our model.

## Acknowledgements

This research was partially supported in part by the National Science Council (NSC) of Taiwan. The authors wish to thank the executive officer P.R. Hill in ISBSG for making ISBSG Repository available to us for this work, anonymous reviewers for their constructive comments, and the chief editor Dr. E.H. Sibley for his editorial effort.

## Appendix A. Selected parts of the questionnaire

To what degree do you believe the following each of general system characteristics affects the implementations of requirements management practices? Please circle the response that best represents your judgment on the following scales.

The purpose of requirements management is to manage the requirements of the project’s products and product components and to identify inconsistencies between those requirements and the project’s plans and work products. Its specific practices include as below:

 SP 1.1 Obtain an understanding of requirements.

 SP 1.2 Obtain commitment to requirements.

 SP 1.3 Manage requirements changes.

 SP 1.4 Maintain bidirectional traceability of requirements.

 SP 1.5 Identify inconsistencies between project work and requirements.

<table><tr><td>General system characteristic</td><td>Slight influence</td><td>Weak influence</td><td>Medium influence</td><td>High influence</td><td>Strong influence</td></tr><tr><td>Transaction rate</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Distributed data processing</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Data communication</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Installation easy</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Complex processing</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Heavily used configuration</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Multiple sites</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Performance</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Reusability</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Online data entry</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Online update</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>End user efficiency</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Operational easy</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Facilitate charge</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr></table>

## References

[1] J.G. Brodman, D.L. Johnson, Return on Investment from Software Process Improvement as Measured by US Industry, Soft ware Process Improvement and Practice, John Wiley & Sons, Sussex, UK, 1995.

[2] B. Curtis, W.E. Hefley, S. Miller, People Capability Maturity Model, Software Engineering Institute, CMU/SEI-95-MM-02, 1995.

[3] CMMI Product Team, Capability Maturity Model Integration, Version1.1, CMMI–SW/SE/IPPD/SS, Staged Representation, CMU/SEI-2002-TR-011, 2002.

[4] CMMI Product Team, Capability Maturity Model Integration, Version1.1, CMMI–SW/SE/IPPD/SS, Continuous Representation, CMU/SEI-2002-TR-012, 2002.

[5] C.T. Chen, Extensions of the TOPSIS for group decision-making under fuzzy environment, Fuzzy Sets and Systems 114(1), 2000, pp. 1–9.

[6] J. Cooper, M. Fisher, Software Acquisition Capability Maturity Model, CMU/SEI-2002-TR-010, 2002.

[7] S.J. Chen, C.L. Hwang, Fuzzy Multiple Attribute Decision Making Methods and Applications, Springer-Verlag, 1992.

[8] M. Diaz, J. Sligo, How software process improvement helped Motorola, IEEE Software 14(5), 1997, pp. 75–81.

[9] M. Delgado, F. Herrera, E. Herrera-Viedma, L. Martinez, Combining numerical and linguistic information in group decision making, Journal of Information Sciences 107(1–4), 1998, pp. 177–194.

[10] R.E. Doke, T. Barrier, An assessment of information systems taxonomies: time to re-evaluation, Journal of information Technology 3, 1994.

[11] Enterprise Process Improvement Collab (EPIC), Systems Engineering Capability Maturity Model, Version 1.1, 1995.

[12] P. Ein-Dor, E. Segev, A classification of information system: analysis and interpretation, Information System Research 4(2), 1993, pp. 166–204.

[13] J.P. Guielford, Fundamental Statistics in Psychology and Education, 4th ed., McGraw-Hill, New York, 1965.

[14] M. Gelderman, Task difficulty, task variability and satisfaction with management support systems, Information and Management 39(7), 2002, pp. 593–604.

[15] IFPUG, Function Point Counting Practices Manual, Release 4.2, International Function Point User Group, 2004.

[16] C. Jones, Software benchmarking, IEEE Computer 28(10), 1995, pp. 102–103.

[17] C. Lokan, T. Wright, P. Hill, M. Stringer, Organizational benchmarking—using the ISBSG data repository, IEEE Software 18(5), 2001, pp. 26–32.

[18] C.J. Lokan, An empirical analysis of function point adjustment factors, Information and Software Technology 42(9), 2000, pp. 649–659.

[19] H.S. Lee, Optimal consensus of fuzzy opinions under group decision making environment, Fuzzy Sets and System 132, 2002, pp. 303–315.

[20] G. Mentzas, A functional taxonomy of computer-based information system, International Journal of Information Management 1994, pp. 397–410.

[21] A. Noushin, The impact of software process improvement on quality: in theory and practice, Information and Management 40(7), 2003, pp. 677–689.

[22] I.T. Oya, O.R. Walter, Analysis of the characteristics of projects in diverse industries, Journal of Operations Management 16(1), 1998, pp. 43–61.

[23] M.C. Paulk, B. Curtis, M.B. Chrissis, C.V. Weber, Capability Maturity Model for Software, Version 1.1, CMU/SEI-93-TR-24, 1993.

[24] W. Royce, Software Project Management: A Unified Framework, Addison-Wesley, 1998.

[25] Software Engineering Measurement and Analysis – Maturity Profile, Software Engineering Institute, 2004.

[26] Software Engineering Institute, EPIC, An Integrated Product Development Capability Maturity Model, Carnegie Mellon University, Version 0.9, October 1996.

[27] M.V. Tatikonda, An empirical study of platform and derivative product development projects, The Journal of Product Innovation Management 16(1), 1999, pp. 3–26.

![](/api/attachments/TKKRA898/fulltext/images/06a58f24ac13a0bb20a7f6493c86b99bc7ea149d6e05556576f73d37104c9220.jpg)

Sun-Jen Huang received his BA in Industrial Management in 1988, and his MS in Engineering and Technology in 1991, both from the National Taiwan Institute of Technology, Taipei, and the PhD degree from the School of Computer Science and Computer Engineering, La Trobe University, Melbourne, Australia, in 1999. He is currently an assistant professor in the Department of Information Management, National Taiwan

University of Science and Technology, Taipei. He is also the head of the Software Engineering and Management Laboratory, which hosts several research projects from National Science Council, Taiwan. Dr. Huang is also a member of Software Quality Promotion Committee at the Chinese Society for Quality. His research interests include software measurement and analysis, project estimation, process improvement, project management and quality assurance and management. He has published articles in Information & Management, IEEE Transactions on Software Engineering, Software Practice & Experience, Journal of Systems and Software.

![](/api/attachments/TKKRA898/fulltext/images/78acc6fb556794be7118a0a2bdc3ff47fcb3e08dc21985b3236e745ae34c8f34.jpg)

Wen-Ming Han is currently a doctoral candidate in the Department of Information Management at National Taiwan University of Science and Technology (NTUST), and is also a member of the Software Engineering and Management Laboratory at NTUST, Taiwan. He received his Bachelor degree in Information Management from St. John’s & St. Mary’s Institute of Technology in 2001, and Master degree in Infor-

mation Management from NTUST in 2003, Taiwan. His current research interests include software process improvement, risk management and software size estimation.
