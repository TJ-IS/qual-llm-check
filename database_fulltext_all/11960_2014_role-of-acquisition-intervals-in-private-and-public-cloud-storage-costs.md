---
otero_id: 11960
otero_key: "RKE3PE6Z"
title: "Role of acquisition intervals in private and public cloud storage costs"
authors: "Gabriella Laatikainen; Oleksiy Mazhelis; Pasi Tyrväinen"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.09.020"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Role of acquisition intervals in private and public cloud storage costs

Gabriella Laatikainen ⁎, Oleksiy Mazhelis, Pasi Tyrväinen

Department of Computer Science and Information Systems University of Jyväskylä, Jyväskylä, Finland

## a r t i c l e i n f o

Article history: Received 26 November 2012 Received in revised form 17 September 2013 Accepted 22 September 2013 Available online 9 November 2013

Keywords: Storage services Cloud storage Cost mode Acquisition interval

## a b s t r a c t

The volume of worldwide digital content has increased nine-fold within the last <sup>fi</sup>ve years, and this immense growth is predicted to continue in the foreseeable future to reach 8 ZB by 2015. Traditionally, organizations proactively have built and managed their private storage facilities to cope with the growing demand for storage capacity. Recently, many organizations have instead welcomed the alternative of outsourcing their storage needs to the providers of public cloud storage services due to the proliferation of public cloud infrastructure offerings. The comparative cost-ef<sup>fi</sup>ciency of these two alternatives depends on a number of factors, such as the prices of the public and private storage, the charging and the storage acquisition intervals, and the predictability of the demand for storage. In this paper, we study the relationship between the cost-ef<sup>fi</sup>ciency of the private vs. public storage and the acquisition interval at which the organization re-assesses its storage needs and acquires additional private storage. The analysis in the paper suggests that for commonly encountered exponential growth of storage demand, shorter acquisition intervals increase the likelihood of less expensive private storage solutions compared with public cloud infrastructure. This phenomenon is also numerically illustrated in the paper using the storage needs encountered by a university back-up and archiving service as an example. Because the acquisition interval is determined by the organization's ability to foresee the growth of storage demand, via provisioning schedules of storage equipment providers, and internal practices of the organization, among other factors, organizations that own a private storage solution may want to control some of these factors to attain a shorter acquisition interval and thus make the private storage (more) cost-ef<sup>fi</sup>cient.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

According to the IDC, the global volume of digital content has exhibited exponential growth and will grow from 1.8 ZB in 2011 to 2.7 ZB in 2012 and ultimately reach 35 ZB by 2020 [5,6]. As the volume of digital content grows, the global need for storage capacity rapidly increases, too.

To cope with the growing demand for storage, organizations may proactively build their private storage capacity or may alternatively opt for outsourcing their storage to the providers of public cloud infrastructure services, such as Amazon Simple Storage Service (S3), Box.com, and Apple iCloud. Decision makers consider several factors when they decide on possible adoption, such as cost, elasticity, data availability, security, data con<sup>fi</sup>dentiality and privacy, regulatory requirements, reliability, performance, integration with other services, personal preference, and added values [10]. However, cost considerations are perceived both as a risk and an opportunity, and the expected cost advantage is the strongest decisional factor that affects the perceived opportunities of IT executives [2].

If the organization decides to store its data in-house, it periodically estimates its future demand for storage and then proactively acquires and manages the storage infrastructure internally. Conversely, the use of cloud-based storage services gives the organization the <sup>fl</sup>exibility to rapidly increase its storage capacity as the demand for storage grows, as well as the possibility to pay only for the volume of storage the organization actually uses within each charging period.

Because the cloud infrastructure capacity is usually paid for only when used, the cloud infrastructure providers include a so-called utility (pay-per-use) premium into their pricing [29]. As a result, the unit price per unit of time of a public cloud infrastructure capacity is usually more expensive compared with the unit cost of private capacity [29,9]. Still, if the demand for infrastructure services exhibits periodical or random peaks, the adoption of public cloud infrastructure is likely to offer cost advantages to organizations over the private infrastructure: this advantage is because the high premium charged by the public cloud provider is compensated by avoiding extensive periods of time when the private infrastructure would remain idle [29,12].

However, as opposed to the <sup>fl</sup>uctuating demand for computing resources, the demand for storage often accumulates over time because newly created digital content only partially supersedes the already stored <sup>fi</sup>les. As a result, the use of public storage services may prove more expensive compared with the private solutions in the long term [27].

The cost-ef<sup>fi</sup>ciency of public vs. private storage depends on a number of factors, such as the premium charged by the provider of public cloud infrastructure, the charging period (for the public storage) and the storage acquisition interval (for the private storage), the intensity of incurred data communications, the predictability of the growth of storage needs and the storage growth pro<sup>fi</sup>le [27,30]. Due to the continuously increasing storage demand, the length of the acquisition intervals and growth predictability are among the most critical factors in storage cost analysis; however, they have to date not been studied in detail. Therefore, we study the effect of the private storage acquisition interval on the cost-ef<sup>fi</sup>ciency of private vs. public storage in this paper. This interval can be determined by the organization's ability to foresee the growth in storage demand, via the provisioning schedule of the storage equipment provider, the internal practices of the organization, etc. The paper analytically shows that for commonly encountered exponential growth of storage demand, shorter intervals for which the organization re-assesses its storage needs and acquires additional storage increase the likelihood that a private storage solution is less expensive compared with the public cloud infrastructure. Numerical experiments are employed to illustrate this dependency using the storage needs encountered by a university back-up and archiving service as an example.

The analysis of storage costs in the paper focuses on the storage needs and their growth and predictability, storage acquisition interval, as well as the costs incurred due to the transfer of data to and from the storage location. The storage costs may also be affected by additional factors, such as the economies and diseconomies of scale, the cost of capital, the required level of availability and durability and the possibility to use provenance data. Combined, these and other factors are likely to have a complex, non-linear effect on the overall costs, which makes them dif<sup>fi</sup>cult to analyze [12]. To simplify the analysis, these additional factors were assumed to either have a minor effect or similar effect on the costs of both the private and public storage solutions. Hence, these factors are outside of the scope of the paper.

The remainder of the paper is organized as follows. In the next section, the related works on the cost-ef<sup>fi</sup>cient use of cloud infrastructure are reviewed. In Section 3, an analytical model for comparing the cost ef<sup>fi</sup>ciency of private vs. public storage is introduced, in which the effect of the acquisition interval is taken into account. Numerical experiments that illustrate the effect of the acquisition interval and its interplay with various other factors are provided in Section 4. In Section 5, the practical implications and limitations of the obtained results are discussed. Finally, Section 6 summarizes the obtained results and outlines the directions for further work.

## 2. Related works

In recent years, extensive research efforts have been devoted to the cost-ef<sup>fi</sup>cient use of cloud infrastructure services in general, and cloud storage services in particular. A short overview of the recent research in this domain is provided below.

A number of works have focused on the cost-ef<sup>fi</sup>cient use of cloud infrastructure and the factors that affect it. In particular, the cost bene<sup>fi</sup>t of using cloud bursting, i.e., of<sup>fl</sup>oading the computing load during peak times to a public cloud infrastructure, has been analytically investigated in [29,28]. The cost ef<sup>fi</sup>cient allocation of computing load to the private and the public portions of a hybrid cloud infrastructure was also studied in [8,3] and in [13,12], where the communication overheads were also considered. The cost-optimal time of using the public cloud has been shown to be the inverse of the premium charged by the public cloud provider assuming negligible data communication overheads.

The economies of scale, i.e., the decline in the cost per unit of a service with the number of units produced [22], may affect the costef<sup>fi</sup>ciency of private vs. public cloud infrastructure as well. These economies of scale are manifested e.g., in the volume discount offered for the cloud infrastructure capacity, and the cost of a hybrid cloud may exceed the cost of a private or a public cloud infrastructure in the presence of such discounts [12].

The cost-optimal allocation of individual computing tasks to private and public cloud resources was also approached as a multi-integer linear programming problem in [24]. Based on the results of a simulation study, the authors found little or no cost bene<sup>fi</sup>ts in of<sup>fl</sup>oading the peaks of the workload, although the preliminary character of the study and the complex nature of the optimization model make it dif<sup>fi</sup>- cult to interpret the results. Walker [27] compared the acquisition and leasing of storage as alternative investment decisions based on their Net Present Value (NPV). The estimation of the NPV considers the dynamics of the demand for storage, the gradual decline of acquired and leased storage prices, the disk replacements due to possible disc failures, and the salvage value of the acquired discs at the end of their use time. Using numerical examples, the authors illustrated that leasing represents a cost-optimal alternative for small- and medium-sized enterprises, whereas acquiring storage is likely to be less expensive in the long term for large enterprises.

Mastroeni and Naldi [11] further revised Walker's model by replacing the deterministic estimation of the pricing dynamics and disc failure dynamics in [27] with probabilistic models. Based on these models, the authors arrive at a probabilistic distribution of differential NPV values and use its median to determine the economically justi<sup>fi</sup>able alternative. Note that in both [27] and [11], the costs are accounted on a yearly basis; thus, the role of acquisition intervals shorter than a year is not visible in these models.

Uttamchandani et al. [26] introduced BRAHMA, a tool that applies constraint-based optimization to cost-optimally supply the storage demand with a mixture of in-house and public cloud storage resources. The tool suggests an optimal placement both for the storage and for the system administrators based on customer storage needs and the projected growth thereof over a look-ahead period, as well as associated service level objectives. The tool helps to identify the optimal sourcing if the customer and the storage service provider have a heterogeneous set of devices and human resources that have different costs. However, to the best of our knowledge, the tool assumes a perfect knowledge of the customer demand growth and fails to consider the storage acquisition intervals; as a result, the cost of the over-provisioned storage is not visible when using the tool.

Constraint-based optimization has also been employed by Trummer et al. [25] to optimally allocate applications to the cloud along with their storage resources. The authors' approach assumes that the resource requirements are known in advance, which is similar to the BRAHMA tool. The effects of imperfect knowledge and resulting storage overprovisioning are not considered.

In addition to acquiring storage capacities, organizations may maximize the cost-ef<sup>fi</sup>ciency of cloud solutions by storing only the provenance for data and regenerating the rest when needed [1]. Yuan et al. proposed different strategies to <sup>fi</sup>nd the best trade-off of storage and computational costs by storing the appropriate intermediate data in cloud storage [31,33,32]. Muniswamy-Reddy et al. emphasized the need for incorporating provenance services in cloud storage providers, analyzed several alternative implementations to collect provenance data, and use the cloud as a backend [17,16,15].

Finally, Weinman [30] considered the delay with which the required resource is provisioned and analyzed both the cost of over-provisioning (i.e., unused resources) and under-provisioning (i.e., the opportunity cost of unserved demand). The author discussed the role of provisioning time given a possibility to predict the future demand over a speci<sup>fi</sup>c forecast visibility; however, the paper only considered cases with a zero forecasting visibility.

In summary, while a number of works have focused on the costef<sup>fi</sup>cient use of private and public infrastructure resources, relatively little attention has been devoted to the role of the acquisition intervals in the cost-ef<sup>fi</sup>cient use of private vs. public storage capacity. Therefore, a storage cost model is introduced below in which the effect of the acquisition interval is taken into account.

## 3. Storage cost model

In this section, the cost constituents of alternative storage approaches are considered, and their total costs are compared. Different cost constituents need to be taken into account depending on whether the storage solution is owned and managed privately by the organization or offered by a public cloud infrastructure provider.

For private storage, the relevant cost constituents include the cost of hardware and software acquisition, integration, con<sup>fi</sup>guration, upgrade costs, as well as the recurring costs of renting <sup>fl</sup>oor space, power, bandwidth, and the cost of administration and maintenance. The cost of private storage is a function of the demand, its growth pattern and predictability, the time interval between storage acquisitions, and the pricing of the necessary equipment, software, and personnel, as well as various other expenses.

Conversely, the cost of public cloud storage consists of the usagedependent costs of storage capacity, data transfer, and input/output requests (based on the pricing set by Amazon S3). Depending on the charging policy of the provider, the cost of the storage may be determined by the maximum volume of storage occupied during the charging period: for instance, Amazon Web Services (AWS) offerings apply charges based on the maximum storage capacity used in $1 2 \ \mathrm { h } . ^ { 1 }$

In addition to the difference in cost constituents, storage is differentially acquired, provisioned, and charged for. Namely, private storage needs to be acquired in advance to meet the expected demand growth until the next acquisition time, and it incurs volume-dependent costs irrespective of storage use. However, public storage can be deployed virtually instantly as the demand grows, and it is charged based on the volume of the storage actually used within the charging period. Furthermore, in-house storage needs to be acquired in excess depending on the accuracy of storage prediction (which is not necessary in public cloud storage). Nevertheless, the price of a unit of in-house storage can be signi<sup>fi</sup>cantly lower than the price of the public cloud. Therefore, we suggest that the cost ef<sup>fi</sup>ciency of private vs. public storage depends on the price difference of the private and public storage, the interval at which the storage can be acquired, and the accuracy with which the future needs for the storage can be predicted.

Organizations may apply different data storage strategies to trade some of the storage costs to computational costs. In some applications, they may only store the provenance data and regenerate the data when needed, or they may compress data to minimize the overall storage-related expenses. However, incorporating these factors in the analytical model results in a complex analysis task due to the great number of alternative solutions that can be envisioned. Furthermore, based on our knowledge, public cloud providers do not yet offer provenance or compression services to the public [17,16]. Consequently, we assumed that provenance data or compression are not used to reduce storage costs because of space limitations.

The remainder of the section is organized as follows. In the next subsection, we introduce a storage cost model to compare the costs of private and public solutions. We then study the effect of the length of the acquisition period on the cost-ef<sup>fi</sup>ciency of private vs. public storage for exponential (Section 3.2), linear (Section 3.3), and logarithmic growth (Section 3.4). The role of data transfer costs in the storage costs is then analyzed in Section 3.5. Finally, the sensitivity of the cost difference function to the acquisition interval and utility premium are introduced in Section 3.6.

## 3.1. General storage cost model

Let us de<sup>fi</sup>ne the demand function s(t) ↦ ℝ that maps from time to the quantity of needed resources. Due to the increasing growth of storage needs, we can assume that the function is positive and increasing. Let $P _ { p } ( s ( t ) )$ denote the price of a unit of storage set by the public storage provider, and let $P _ { o } ( s ( t ) )$ denote the total cost of owning a unit of private storage capacity over time t. Both prices are shown as functions of the volume of used or acquired storage capacity s(t), to indicate that the prices can be a subject to volume discounts, as is in the case of AWS storage, for example. Note that $P _ { p } ( s ( t ) )$ can be found by consulting price lists of public IaaS vendors, whereas $P _ { o } ( s ( t ) )$ needs to be estimated by summing the total costs of acquisition and using the storage over the total period of planned use, T (e.g., the depreciation period) to ultimately derive the share of the total costs during the time, t.

Let us <sup>fi</sup>rst consider the case of using private storage capacity. Let us assume that the organization is acquiring private storage capacity with an acquisition interval, τ. The organization then needs to predict how much storage it would require within time, τ, i.e., until the next acquisition time. For instance, if τ = 12 month, the <sup>fi</sup>rm needs to predict the increase of its storage needs over the next year and acquire the storage accordingly. The cost of acquiring in-house storage capacity, $c _ { o } ,$ can then be estimated as follows:

$$
c _ {o} = \hat {s} (\tau) p _ {o} (\hat {s} (\tau)) \tau ,\tag{3.1}
$$

where $\hat { s } ( \tau )$ is the organization's estimate of the maximum storage needed within the next acquisition interval.

We assume that the <sup>fi</sup>rm will acquire a storage capacity suf<sup>fi</sup>- cient to meet the maximum storage needs. Furthermore, because predicting the future storage needs with 100% accuracy is dif<sup>fi</sup>- cult, we assume that the organization is likely to over-estimate its storage needs and over-provision its storage capacity to avoid a situation in which it would not be able to meet customer expectations, i.e.,

$$
\hat {s} (\tau) = k _ {e} k _ {s} s (\tau),\tag{3.2}
$$

where $k _ { e } \geq 1$ represents an estimation error. The coef<sup>fi</sup>cient of redundancy, $k _ { s } \ge 1$ , is introduced to account for the fact that a portion of the storage capacity is used for purposes other than storing data — for instance, to maintain a level of redundancy suf-<sup>fi</sup>cient for the required level of failure-resistance.

Thus, the cost of private storage in the acquisition interval, τ, can be calculated as follows:

$$
c _ {o} = k _ {e} k _ {s} p _ {o} (s (\tau)) s (\tau) \tau .\tag{3.3}
$$

Let us now study how the length of the acquisition interval affects the total cost of a private solution.

Proposition 1. The cost of private storage increases as the length of the acquisition interval increases.

Proof. The proof of the proposition is provided in A.1. □

Proposition 1 re<sup>fl</sup>ects that the length of the acquisition interval positively correlates with the volume of unused or over provisioned storage. Furthermore, the demand estimation may be more inaccurate for longer acquisition intervals. Eq. (3.3) indicates that in addition to shortening the acquisition interval length, improving the demand estimation, lowering the redundancy level or decreasing the price of storage capacity also reduces the overall private storage costs.

Consider now the case of using public storage capacity. For simplicity, we will assume that the charging interval set by the public storage provider is quite small compared with the acquisition interval; for instance, the charging period is 12 h for Amazon. We can then express the length of the acquisition interval in terms of the charging intervals; for instance, monthly charging periods and yearly acquisition intervals would correspond to $\tau = 1 2$ . Thus, the cost of public storage, $c _ { p } ,$ accumulated over the acquisition interval, τ, can be approximated as follows:

$$
c _ {p} = \int_ {1} ^ {\tau} s (t) p _ {p} (s (t)) d t.\tag{3.4}
$$

Let us also assume that the price of a unit of public storage capacity is higher than the cost of a unit of private storage. This assumption is justi<sup>fi</sup>ed by the fact that the public storage provider charges a premium for the organization's <sup>fl</sup>exibility in rapidly provisioning and de-provisioning the resources [29]; as a result, some organizations found it signi<sup>fi</sup>cantly less expensive to host their own storage facilities than to use the storage capacity of Amazon, with the difference reaching a factor of 26 [18]. Thus, the following can be rewritten: $p _ { p } = u _ { s } p _ { o } ,$ where $u _ { s }$ is the utility premium ratio, or in short, the utility premium of the public storage vendor. For the sake of brevity, the prices $P _ { P } ( s ( t ) )$ and $P _ { o } ( s ( t ) )$ are referred to as $p _ { p }$ and $p _ { o } ,$ respectively.

For simplicity, the prices are assumed to not be subject to volume discounts. Thus, Eq. (3.4) can be rewritten as follows:

$$
c _ {p} = u _ {s} p _ {o} \int_ {1} ^ {\tau} s (t) d t.\tag{3.5}
$$

To assess whether the public or private storage is less expensive, let us introduce the cost difference function $, f \colon$

$$
f (\tau) = c _ {p} - c _ {o} = u _ {s} p _ {o} \int_ {1} ^ {\tau} s (t) d t - k _ {e} k _ {s} p _ {o} s (\tau) \tau .\tag{3.6}
$$

Based on the de<sup>fi</sup>nition, this function is positive if the private solution is cheaper than the public one, and negative if the public solution is more cost-ef<sup>fi</sup>cient compared with the private storage.

Let us now compare the utility premium, $u _ { s } ,$ , and the product of the estimation error and redundancy level, k k . It follows from the discussion above that $u _ { s } \geq 1$ and $k _ { e } k _ { s } \ge 1$ . Assuming that i) a notable premium is charged by public storage vendors (not all organizations have the scale and capabilities required to attain a unit storage cost 26 times cheaper than Amazon, but attaining a 10-fold savings appears to be a feasible assumption), ii) the estimation error is a fraction of storage needs $\left( k _ { e } < 2 \right)$ , and iii) a reasonable degree of overheads is present in self-storage $( \mathbf { e } . \mathbf { g } . , k _ { s } < 2 )$ , the following is likely: u N k k . Therefore, we will assume for simplicity that $u _ { s } > k _ { e } k _ { s } ^ { ~ 2 }$

Proposition 2. Given the growth demand function $s ( \tau ) : s ( \tau ) { > } s ( 1 ) *$ $\tau ^ { \frac { u _ { s } - k _ { e } \overline { { k } } _ { s } } { k _ { e } k _ { s } } }$ , the cost difference between public and private storage as de<sup>fi</sup>ned by f(τ) decreases as the length of the acquisition interval increases.

## Proof. The proof of the proposition is provided in A.2. □

The proposition states that the cost ef<sup>fi</sup>ciency of public storage as compared with the private cloud increases in the length of the acquisition interval if the storage demand grows faster than the polynomial function $s ( 1 ) \tau ^ { w }$ , where $\begin{array} { r } { w = \frac { u _ { s } - k _ { e } k _ { s } } { k _ { e } k _ { s } } { > 0 } . } \end{array}$ . Thus, the use of the public storage is likely to be economically justi<sup>fi</sup>able when the storage demand grows rapidly and the organization's acquisition intervals are signi<sup>fi</sup>cantly longer than the charging periods of the public storage vendor. Conversely, if the storage demand grows fast and the organization can shorten the acquisition intervals to be similar to the intervals of the public storage vendor, then acquisition and maintaining of self-storage is likely to be less expensive.

Thus, the cost-ef<sup>fi</sup>ciency of private and public storage depends on the growth pro<sup>fi</sup>le of storage needs. In the next subsection, the cost-ef<sup>fi</sup>ciency of private vs. public storage is analyzed for exponential, linear and logarithmic growth.

## 3.2. Exponential growth

In many research studies, storage demand is thought to grow exponentially, with an annual growth rate estimated as high as 70% [11,5,6]. In this case, the storage demand function can be written as follows:

$$
s (t) = s (1) * g ^ {t}\tag{3.7}
$$

where $g > 0$ is the storage growth rate.

Proposition 3. If the demand for storage capacity grows exponentially with time, the cost difference of public and private storage decreases as the acquisition interval length increases.

Proof. The proof of the proposition is provided in A.3. □

Thus, the cost ef<sup>fi</sup>ciency of the private solution as compared with the public cloud decreases in the length of the acquisition time interval when the storage needs grow very rapidly. However, using the public cloud may be more economically justi<sup>fi</sup>able when the organization cannot often re-assess its storage needs.

## 3.3. Linear growth

In some of the research papers (e.g., [27]), the storage needs were assumed to grow linearly. In this case, the storage demand function is de<sup>fi</sup>ned as follows:

$$
s (t) = s (1) + g t\tag{3.8}
$$

where $g > 0$ is the growth rate.

Proposition 4. If the demand for storage capacity grows linearly with time and $\begin{array} { r } { \frac { u _ { s } } { k _ { e } k _ { s } } \ge 2 , } \end{array}$ , the cost difference between the public and private storage increases as the acquisition interval length increases.

Proof. The proof of the proposition is provided in A.4. □

Thus, the cost ef<sup>fi</sup>ciency of private storage as compared with public storage correlates with the length of the acquisition interval if the demand for storage capacity grows linearly and storage in the public cloud is relatively expensive (e.g., without redundancy requirements and perfect storage estimation, the utility premium is greater than two). In this case, the private storage may be less expensive compared with the public cloud, especially for long acquisition intervals. However, if the public cloud is inexpensive compared with the private one, the estimation error is large, or the redundancy requirements are high, then shortening the acquisition interval increases the cost advantage of private storage as compared with the public solution.

## 3.4. Logarithmic growth

When the storage demand grows slowly and the growth can be described as a logarithm function of time, the storage demand function is de<sup>fi</sup>ned as follows:

$$
s (t) = s (1) * \ln (t).\tag{3.9}
$$

Proposition 5. If the demand for storage capacity grows logarithmically with time, the cost difference between public and private storage increases as the acquisition interval length increases.

Proof. The proof of the proposition is provided in A.5. □

Thus, the cost-ef<sup>fi</sup>ciency of public cloud as compared with the private storage decreases in the length of the acquisition interval when the storage demand grows with the inverse of the exponential growth. In other words, private storage may be less expensive compared with the public cloud despite long acquisition intervals if the storage demand grows slowly.

In the next subsection, the impact of the acquisition period length on the cost-ef<sup>fi</sup>ciency of public vs. private storage is analyzed when data transfer costs are present.

## 3.5. The effect of data transfer costs

In addition to the costs of storage capacity itself, the cost of a storage solution also includes the costs incurred due to the transfer of data to and from the storage location, namely:

• the initial transfer of new data being saved (which also includes the modi<sup>fi</sup>ed versions of the previously saved items);

• the transfer of stored data back to the user in response to occasional reading requests (also including the rare retrievals of backup data).

Cheng et al. [4] analyzed the usage pattern of YouTube videos and modeled the growth of the number of views with a power-law distribution. The authors de<sup>fi</sup>ned the active life span of the videos, stating that the videos are rarely watched again after a short period of popularity. Therefore, we will assume for the sake of simplicity that the data are intensively used shortly after they are initially saved, but only occasionally requested thereafter.

For private storage, the price of a unit of bandwidth, $p _ { b o } ,$ is likely to depend on the maximum bandwidth required during the acquisition period [23]. Thus, private storage transfer costs can be estimated as a function of the maximum storage added during the acquisition period:

$$
c _ {b o} = k _ {b} s (\tau) p _ {b o} \tau ,\tag{3.10}
$$

where $k _ { b }$ indicates the number of times a byte of stored data is transferred on average during a period of popularity, and $s ( \tau )$ is the maximum storage amount needed within the acquisition period, τ.

Conversely, the bandwidth costs when using a public storage provider are based on the actual data transfer needs within each charging period.<sup>3</sup> Assuming again that the volume of transferred data is proportional to the volume of data stored by the public storage provider, the cost of data transfer when using a public storage provider can be approximated as follows:

$$
c _ {b p} = k _ {b} p _ {b p} \int_ {1} ^ {\tau} s (t) d t,\tag{3.11}
$$

where $p _ { b p }$ is the price of a unit of bandwidth for public storage.

We assume for simplicity that the unit pricing of data communication is roughly equal to the private and the public storage $( p _ { b p } \approx p _ { b o } )$ The private and public costs can then be de<sup>fi</sup>ned as follows:

$$
c _ {o} = k _ {e} k _ {s} s (\tau) p _ {o} \tau + k _ {b} s (\tau) p _ {b o} \tau\tag{3.12}
$$

$$
c _ {p} = u _ {s} p _ {o} \int_ {1} ^ {\tau} s (t) d t + k _ {b} p _ {b o} \int_ {1} ^ {\tau} s (t) d t.\tag{3.13}
$$

Proposition 6. Given the growth demand function $s ( \tau ) : s ( \tau ) { > } s ( 1 )$ $\begin{array} { r } { \tau _ { e ^ { k _ { s } p _ { 0 } + k _ { b } p _ { b 0 } } } ^ { p _ { 0 } ( u _ { s } \mathbf { \tilde { { \Gamma } } } - k _ { e } k _ { s } ) } } \end{array}$ , the cost difference between public and private storage and data communications decreases as the length of the acquisition interval increases.

Proof. The proof of the proposition is provided in A.6. □

Thus, the presence of data communication costs strengthens the dependency of the cost difference and the acquisition interval length: the economic advantage of public storage as compared with private storage increases in the length of the acquisition interval when the storage needs grow suf<sup>fi</sup>ciently fast.

Among others, the utility premium and the length of the acquisition interval are decisive factors in the cost-ef<sup>fi</sup>ciency of public and private storage solutions. In the next subsection, the relative sensitivity to these parameters is studied to compare their impact on the cost difference between public and private storage.

3.6. Relative sensitivity to the utility premium and the length of the acquisition interval

Let us now introduce the relative sensitivity function of the function F to the parameter α:

$$
S _ {\alpha} ^ {f} = \frac {\% c h a n g e i n F}{\% c h a n g e i n \alpha} = \frac {\frac {d F}{F}}{\frac {d \alpha}{\alpha}} = \frac {d F}{d \alpha} \frac {\alpha}{F}.\tag{3.14}
$$

The relative sensitivity function, $S _ { \alpha } ^ { f } ,$ lets us pinpoint the values for which α has the strongest impact on the cost-ef<sup>fi</sup>ciency of a public compared with a private solution and allows us to determine the parameters that have the greatest effect on the output for a certain percent change in the parameters [20].

Let us now calculate the relative sensitivity of the function 3.6 to the acquisition interval, $S _ { \tau } ^ { f }$ and to the utility premium, $S _ { u _ { s } } ^ { f }$ :

$$
S _ {\tau} ^ {f} = \frac {d f}{d \tau} \frac {\tau}{f} = \frac {\tau \left(p _ {o} s (\tau) (u _ {s} - k _ {e} k _ {s}) - k _ {e} k _ {s} \tau_ {\frac {d s}{d \tau}})\right)}{u _ {s} p _ {o} \int_ {1} ^ {\tau} s (t) d t - k _ {e} k _ {s} p _ {o} s (\tau) \tau},\tag{3.15}
$$

and

$$
S _ {u _ {s}} ^ {f} = \frac {d f}{d u _ {s}} \frac {u _ {s}}{f} = \frac {u _ {s} p _ {o} \int_ {1} ^ {\tau} s (t) d t}{u _ {s} p _ {o} \int_ {1} ^ {\tau} s (t) d t - k _ {e} k _ {s} p _ {o} s (\tau) \tau}.\tag{3.16}
$$

For example, because storage demand is considered to grow exponentially in many cases, let us specify these functions in case of exponential growth. In this case, the relative sensitivity of the cost difference function, f, to the parameter τ can be de<sup>fi</sup>ned as S<sup>f</sup> and calculated as follows:

$$
S _ {\tau} ^ {f} = \frac {d f}{d \tau} \frac {\tau}{f} = \frac {\tau \left(u _ {s} g ^ {\tau} - k _ {e} k _ {s} \left(l n g g ^ {\tau} \tau + g ^ {\tau}\right)\right)}{\left(u _ {s} \frac {g ^ {\tau} - 1}{l n g} - k _ {e} k _ {s} g ^ {\tau} \tau\right)}.\tag{3.17}
$$

Conversely, the relative sensitivity of function 3.6 to the parameter u can be de<sup>fi</sup>ned as $S _ { u _ { s } } ^ { f }$ and calculated as follows:

$$
S _ {u _ {s}} ^ {f} = \frac {d f}{d u _ {s}} \frac {u _ {s}}{f} = \frac {u _ {s} \frac {g ^ {\tau} - 1}{l n g}}{u _ {s} \frac {g ^ {\tau} - 1}{l n g} - k _ {e} k _ {s} g ^ {\tau} \tau}.\tag{3.18}
$$

## 4. Illustrative numerical examples

The previous section demonstrated that the interval at which the organization re-evaluates its storage needs and acquires additional storage capacity affects the cost-ef<sup>fi</sup>ciency of private storage compared with public storage. Namely, for the commonly encountered exponential growth of storage demand, the acquisition interval positively correlates with the likelihood that the use of public storage is less expensive. In this section, the effect of the acquisition interval will be illustrated by using an example of a demand pro<sup>fi</sup>le of the back-up and archiving service provided by Oxford University to its senior members, postgraduates, and staff members [14].

![](/api/attachments/RKE3PE6Z/fulltext/images/3babbfda5dc030d231ffcbf358cf02c84d1ca5b1d2789dd336fa2a29ec723207.jpg)  
Fig. 1. Growth of the OUCS back-up and archiving storage during 1996–2011 [19].

The historical traces of the growth of backup storage provided by Oxford University Computing Services (OUCS) are documented in the OUCS annual reports available at the OUCS website.<sup>4</sup> The growth pro<sup>fi</sup>le over the period 1996–2011 is shown in Fig. 1. As evidenced in the <sup>fi</sup>gure, the demand for data storage at OUCS grew exponentially, increasing by roughly 50% on an annual basis.

With the exception of the <sup>fi</sup>rst year of observations when a threedigit growth was recorded, the yearly increase during 1998–2011 has been below 100%; in most of the years, it <sup>fl</sup>uctuated between 30% and 70%. Therefore, let us assume that the organization acquires a storage capacity suf<sup>fi</sup>cient for serving the maximum expected growth in the storage demand, with the maximum expected growth being 100% a year. Let us further assume that the volume of initially acquired capacity is 10 TB, that 100% of storage is reserved for redundancy purposes $( k _ { s } = 2 )$ , and that the additional capacity is acquired in 5 TB chunks.

In some special cases, <sup>fi</sup>rms need a long-term storage service from which their data is rarely retrieved, and data retrieval times of several hours are acceptable. In these scenarios, companies could utilize the Amazon Glacier Service, for example. With its extremely low storage costs, this service is most likely a cheaper alternative than the discbased private storage solution considered in the paper, even with short acquisition intervals. However, when <sup>fi</sup>rms need low latency or frequent access to their data, other alternatives must be considered. Focusing on this general scenario, the unit price of the public storage can be estimated by consulting the price list of Amazon S3,<sup>5</sup> for example: assuming the Reduced Redundancy Storage (RRS) is used, storing the <sup>fi</sup>rst, next 49, and next 450 TB costs \$0.076, \$0.064, and \$0.056 per GB per month, respectively. Thus, the RRS price per TB per month is \$77.82, \$65.54, and \$57.34 for the <sup>fi</sup>rst TB, the next 49 TB, and the next 450 TB of data, respectively. Note that the request pricing is not considered for the sake of simplicity.

The unit price of private storage for newly designed storage solutions can be approximated using the costs incurred by Backblaze [18]: to provision a PB of storage, Backblaze reportedly spent \$94,563 over three years for hardware, space, power, and bandwidth. The maintenance costs are also accounted for; according to Backblaze, an engineer maintains the company's 16 PB storage facilities. However, we consider it more realistic that an average <sup>fi</sup>rm, e.g., one with two datacenters, employs four engineers to provide 24/7 operations. Therefore, we assume that four engineers with a yearly salary of $\$ 44,973$ are employed to maintain the storage capacity. This assumption results in a total cost of \$634,239 per PB over three years, i.e., \$17.2 per TB per month. In addition to the storage hardware, software solutions to manage the storage (such as IBM Tivoli Storage Manager) are likely to be needed, thus further increasing the cost of the storage solution; however, we will assume for the sake of simplicity that either inexpensive or open-source software is going to be used and that its costs may be neglected.

![](/api/attachments/RKE3PE6Z/fulltext/images/4a1e02f353627431a7813d11ef7e48b7cec2bfd5094ca2b2e2a9dd7bbd07e2db.jpg)  
Fig. 2. Storage costs vs. acquisition intervals for different values of utility premium

Alternatively, the unit price of private storage can be found using the charges set by the OUCS back-up and archiving service for its research project customers. According to the OUCS service level description [21], the storage cost is £842 (\$1321.5) per TB per year, which results in a storage cost of £70.17 (\$110.32) per TB per month.

Based on these two reference examples, the utility premium, $u _ { s } ,$ may vary depending on the cost-ef<sup>fi</sup>ciency of the private solution: for example, the premium varies from \$61.56/\$110.32 = 0.58 (OUCS) to $\$ 61.56/ 517.2=3.58$ (Backblaze) per TB per month for 100 TB of storage. Therefore, we will explore a set of different values of $u _ { s } = \{ 0 . 6 ; 1 . 0 ; 1 . 5 ; 2 . 0 ; 3 . 0 ; 4 . 0 \}$

The above cost estimates consider neither the gradual price decline nor the effect of the net present value of the assets. Both of these factors are important and affect the total cost of the storage solution; however, as their effect has been studied elsewhere [27], we have decided to exclude these factors from the analysis in this study to focus on and better illuminate the effect of the acquisition interval on the total costs.

In Fig. 2, the total costs of private and public storage solutions that accumulated over the period from 1996–2011 are compared for different levels of the utility premium, $u _ { s } .$ The <sup>fi</sup>gure shows that the private storage cost increases along with the storage acquisition interval. Given the utility premium value, $u _ { s } \leq 1 . 5 ,$ the total cost of private storage always exceeds the cost of public storage, which is in line with the analysis in [29]. Conversely, given $u _ { s } \leq 2 . 0$ , private storage is less expensive when the acquisition interval is short, but becomes more expensive than public storage as the length of the interval grows, which supports the analytical reasoning presented earlier in Section 3.1 (cf. Proposition 2).

In addition, we further investigated the cost savings attributed to the decrease of the acquisition interval length compared with the overall costs. Let us now consider the private cost saving function, r:

$$
r (a) = 1 - \frac {c _ {o} ^ {a}}{c _ {o} ^ {1 2}},\tag{4.1}
$$

where α is the acquisition interval length in number of months, $c _ { o } ^ { a }$ is the total private storage cost with acquisition interval length α, and $c _ { o } ^ { 1 2 }$ is the total private storage cost when the acquisition interval is one year long. The function clearly indicates that private cost savings are independent of the price, estimation error, and redundancy level. By calculating the values of this function, we have found that the total costs of a private solution can be reduced by approx. 20% by decreasing the length of the acquisition interval from one year to one month.

Fig. 3 shows the relative sensitivity functions S<sub>τ</sub><sup>f</sup> and $S _ { u _ { s } } ^ { f }$ (de<sup>fi</sup>ned in Eq. (3.6)) for $u _ { s } = 2 .$ . The picture shows that the acquisition interval length has the strongest impact when it is near eight months for $u _ { s } = 2 \AA$ , which agrees with Fig. 2. The <sup>fi</sup>gure also shows that the utility premium has a greater (smaller) effect on the cost difference function compared with the effect of the acquisition interval if the acquisition interval is shorter (longer) than eight months.

The cumulative effect of the acquisition interval and the level of redundancy on the storage cost are illustrated in Fig. 4. The increase in the required redundancy shortens the acquisition interval for which the private storage remains cost-ef<sup>fi</sup>cient. Furthermore, for a redundancy above a certain threshold (2.2 in this example), the cost of private storage always exceeds the public storage cost even for the shortest interval.

The sum of the storage and data communication costs is portrayed in Fig. 5 as a function of the acquisition interval. The <sup>fi</sup>gure shows that the intensity of data communications (manifested in the value of k ) has an effect similar to the effect of the level of redundancy: namely, the greater the volume of data transfer incurred due to storing the data, the shorter the acquisition intervals that need to be maintained for the private storage to remain less expensive than the public storage. These <sup>fi</sup>ndings agree with the analytical reasoning presented earlier in Section 3.5 (cf. Proposition 6).

Furthermore, Fig. 6 illustrates how the estimation errors can be compensated with shorter acquisition intervals. For example, given the estimation error $k _ { e } = 1 . 6 ,$ an acquisition interval shorter than six months is needed to ensure that private storage is cheaper than the public solution. Furthermore, if the storage demand is well known $( k _ { e } \approx 1 )$ , the private solution is more cost-ef<sup>fi</sup>cient than the public solution. Conversely, if the needs are not easily estimable, the public solution is the cheaper alternative.

![](/api/attachments/RKE3PE6Z/fulltext/images/07c6d19cc9e6a5e18555091a7b64c84cfde11a75ec446395bd6d598bec00feee.jpg)  
Fig. 3. Relative sensitivity to the utility premium and acquisition interval when $u _ { s } = 2 .$

![](/api/attachments/RKE3PE6Z/fulltext/images/173f70ee393051cda5896e3dd084c635e7aa72f4bf73aca58606f9e010c32dc6.jpg)  
Fig. 4. Storage costs vs. acquisition intervals for different levels of redundancy.

## 5. Discussion

One of the bene<sup>fi</sup>ts of adopting public cloud infrastructure is the possibility to provision the required infrastructure resources instantly as the demand for the resources increases instead of acquiring them in advance. This on-demand provisioning minimizes the time during which the resources are idle and therefore allows the related costs to be reduced. This bene<sup>fi</sup>t is particularly important in case of storage resources, where the demand is steadily or rapidly increasing rather than <sup>fl</sup>uctuating.

The cost bene<sup>fi</sup>t of on-demand storage provisioning depends greatly on whether (and how much) the private storage acquisition interval is longer than the charging period of the public cloud storage, which was analytically shown in the paper. In particular, for the commonly encountered exponential growth of storage demand, the use of private storage is likely to become more cost-ef<sup>fi</sup>cient than the use of public cloud storage when the storage acquisition interval shortens and approaches the public cloud charging period. Because the acquisition interval is determined by the organization's ability to foresee the growth of storage demand, by the provisioning schedules of storage equipment providers and the internal practices of the organization (among other factors), an organization that owns a private storage solution may want to control some of these factors to attain a shorter acquisition interval and thus make the private storage (more) cost-ef<sup>fi</sup>cient. Conversely, if controlling these factors is challenging in practice, the organization may <sup>fi</sup>nd it justi<sup>fi</sup>able from a cost perspective to switch to using the public cloud storage.

![](/api/attachments/RKE3PE6Z/fulltext/images/154752ec034c591613f049b1cb00faadcec4f2a6f14222fc1b7e91e303a9b53d.jpg)  
Fig. 5. Storage and data transfer costs vs. acquisition intervals for different levels of data communication intensity.

![](/api/attachments/RKE3PE6Z/fulltext/images/5aaa0d956e9f8d377517563649399b95e8ed3f6ca12093c8552de32bb029363e.jpg)  
Fig. 6. Storage and data transfer costs vs. acquisition intervals for different estimation error levels.

The effect of the acquisition interval is further compounded by the effect of the data transfer costs that are incurred when transmitting the data to and from the cloud. Assuming that the charging model for the data transfer in the private infrastructure is based on the maximum traf<sup>fi</sup>c within the charging period and the storage demand grows quickly, the data transfer costs may make the private storage more expensive and hence may make public storage cost-bene<sup>fi</sup>cial even for shorter acquisition intervals.

The organizations were assumed to over-provision the storage capacity in the paper to guarantee that the customer expectations are met. In some application, these guarantees may be relaxed, i.e. the provisioning of the storage may be delayed until the next acquisition time without incurring penalties. However, from the perspective of the presented cost model, such delays can be considered to shorten the acquisition intervals by the value of the tolerated delay in storage provisioning.

Furthermore, the cloud providers were assumed to charge their customers based on the maximum storage usage within a charging period in the paper, which is in line with Amazon S3 or Windows Azure Storage pricing. While Amazon measures the actual storage at least twice a day, Microsoft measures it at least daily.<sup>7</sup> Although the paper contains the results of calculations with a 12 h charging period (in line with Amazon's pricing model), the results of the analysis remain the same even with different charging interval lengths or lower prices set by the public storage provider. Conversely, storage providers may also apply other pricing models that may change the analysis slightly. However, exploring the effect of other alternative pricing models on the cost-ef<sup>fi</sup>ciency of the private vs. public storage was left for further studies because of space limitations.

Finally, the analysis in the paper assumes that the cost of a unit of private storage capacity is less than that of a unit price of public cloud storage. Moreover, the cost of a unit of capacity is likely to be signi<sup>fi</sup>cantly lower for public cloud infrastructure providers [7] due to the economies of scale exercised by them when acquiring and managing their resources. In the future, cloud infrastructure providers may have to decrease their pricing as a result of competitive forces, thus making the unit cost of private storage exceed the unit price of public storage. Should this scenario materialize, the use of public cloud storage will become advantageous from a cost perspective, even if the private storage acquisition intervals are short. For example, the Amazon Glacier dataarchiving service may provide resources for rarely accessed data with lower costs than a private solution with short acquisition intervals. However, companies that utilize this service should accept some restrictions, such as slow data retrieval and possible additional costs for early or frequent data retrieval.

## 6. Conclusions

Contemporary organizations need to cope with the rapidly growing demand for data storage. When deciding on the approach to meet the increasing storage needs, these organizations may choose to build and manage private data storage facilities or utilize the on-demand storage services offered by the providers of public cloud infrastructure. The comparative cost-ef<sup>fi</sup>ciency of these two alternatives depends on a number of factors, such as the pricing difference between public and private storage, the charging period (for the public storage) and the storage acquisition interval (for the private storage), the storage growth pro<sup>fi</sup>le and the predictability of the demand for storage.

In this paper, an analytical tool was introduced to support an organization's assessment of the cost-ef<sup>fi</sup>ciency of a private vs. a public storage solution. This study analytically showed that when assuming a fast growth in storage needs, e.g., currently common exponential growth, the use of public storage is likely to be more cost-ef<sup>fi</sup>cient for organizations with relatively long acquisition cycles, e.g., once per year. Conversely, should the organization have a possibility to reassess its storage needs and acquire additional storage often—say, every second month—the use of private storage capacity is likely to prove less expensive. The analysis shows also that in case storage demand grows slowly, for example logarithmically, the inverse regularity is observed; namely, private storage becomes more cost-ef<sup>fi</sup>cient as the acquisition intervals grow longer.

The paper also illustrated that other factors in addition to the acquisition interval, such as the utility premium charged by the public storage provider, the level of needed storage redundancy, the estimation error, and the incurred data communications, have a compound effect on the cost ef<sup>fi</sup>ciency of the private vs. public storage. More speci<sup>fi</sup>cally, a decline in the utility premium, an increase in the storage redundancy, or an increase in the estimation error shorten the maximum length of the acquisition interval that can be allowed for the private storage to be less expensive compared with the public storage.

Private storage is likely to be more cost ef<sup>fi</sup>cient for short acquisition intervals, assuming that the capacity growth is relatively easy to estimate or the data retrieval can cause intensive but steady communication with the data storage. The cloud alternative is well-justi<sup>fi</sup>ed if the organization is not suf<sup>fi</sup>ciently large to enjoy rather similar pricing of equipment and communication capacity compared with large cloud data centers or the organization does not have resources or competence to run an in-house data center. Thus, the use of public cloud storage is a likely option when launching new services in small and growing organizations that have new services whose market adoption is dif<sup>fi</sup>cult to estimate. For mature services, the storage load is easier to estimate based on the historical data, while insourcing the storage will be dif<sup>fi</sup>cult due to the excessive cost of transferring data from public cloud storage to an in-house data center.

In further work, the proposed approach could be extended in several directions. First, the time dimension of the analytical tool shall be expanded to account for the declining pricing trends, and the pricing estimates themselves could be revised to include visible volume discounts e.g., in Amazon AWS offerings, as well as additional incurred costs, such as the costs of input–output requests. In addition to a deterministic storage growth pro<sup>fi</sup>le, probabilistic pro<sup>fi</sup>les could be studied in future works. For a more holistic view, probabilistic communication patterns should also be considered. Finally, the speci<sup>fi</sup>cs of possible organization's architectural solutions could be explored when estimating the data communication overheads, because they may signi<sup>fi</sup>cantly in<sup>fl</sup>uence the data communication costs.

## Acknowledgment

This work was supported by TEKES as part of the Cloud Software Program of DIGILE (Finnish Strategic Centre for Science, Technology and Innovation in the <sup>fi</sup>eld of ICT and digital business).

## Appendix A. Proofs of the propositions

A.1. Proof of the Proposition 1

Proof. Let us take the derivative of the function $c _ { o } .$

$$
\frac {d c _ {o}}{d \tau} = k _ {e} k _ {s} p _ {o} \left(\frac {d s (\tau)}{d \tau} \tau + s (\tau)\right).\tag{A.1}
$$

Because the storage demand is increasing over time, we know that $\frac { d s ( \tau ) } { d \tau } { > } 0$ . Furthermore, $k _ { e } , k _ { s } , p _ { o } , s ( \tau )$ and τ are all positive. Thus, the derivative of the private cost function, $c _ { o } ,$ with respect to τ is positive. The function monotonically increases with the increase of the acquisition interval, i.e. the longer the acquisition interval, the more expensive the private solution is. □

A.2. Proof of the Proposition 2

Proof. The correctness of the proposition can be shown by taking derivative of function 3.6 and applying the fundamental theorem of calculus:

$$
\begin{array}{c} \frac {d f}{d \tau} = p _ {o} u _ {s} s (\tau) - p _ {o} k _ {e} k _ {s} \left(\frac {d s}{d \tau} \tau + s (\tau)\right) \\ = p _ {o} \bigg (s (\tau) (u _ {s} - k _ {e} k _ {s}) - k _ {e} k _ {s} \frac {d s (\tau)}{d \tau} \tau \bigg). \end{array}\tag{A.2}
$$

Let us denote the ratio $\begin{array} { r } { a = \frac { k _ { e } k _ { s } } { u _ { s } - k _ { e } k _ { s } } { > 0 } } \end{array}$ . Because the unit price, $p _ { o } ,$ is positive,

$$
\frac {d f}{d \tau} <   0 \Longleftrightarrow s (\tau) - a \tau \frac {d s (\tau)}{d \tau} <   0.\tag{A.3}
$$

The differential inequality A.3 is a Gronwall's inequality. Let us now de<sup>fi</sup>ne the functions

$$
\beta (\tau) = \frac {1}{\tau a}\tag{A.4}
$$

and

$$
v (\tau) = e ^ {\int_ {1} ^ {\tau} \beta (t) d t},\tag{A.5}
$$

where v(τ) N 0 and v(1) = 1.

With these denotations, inequality A.3 can be rewritten in the following form:

$$
\frac {d s (\tau)}{d \tau} > \beta (\tau) s (\tau).
$$

Note that

<sub>ð</sub>A:6<sub>Þ</sub>

$$
\frac {d v (\tau)}{d \tau} = e ^ {\int_ {1} ^ {\tau} \beta (t) d t} \frac {1}{\tau a} = \beta (\tau) v (\tau)\tag{A.7}
$$

and

$$
\frac {d \frac {s (\tau)}{v (\tau)}}{d \tau} = \frac {\frac {d s (\tau)}{d \tau} v (\tau) - \frac {d v (\tau)}{d \tau} s (\tau)}{v ^ {2} (\tau)}.\tag{A.8}
$$

We obtain the following by applying inequality A.6 to A.8:

$$
\frac {d _ {\frac {s (\tau)}{v (\tau)}}}{d \tau} > \frac {\beta (\tau) s (\tau) v (\tau) - \beta (\tau) v (\tau) s (\tau)}{v ^ {2} (\tau)} = 0.\tag{A.9}
$$

Applying the mean value theorem, it follows that

$$
\frac {s (\tau)}{v (\tau)} > \frac {s (1)}{v (1)} = s (1),\tag{A.10}
$$

thus,

$$
s (\tau) > s (1) e ^ {\int_ {1} ^ {\tau} \frac {1}{\tau a} d \tau}.
$$

Because

<sub>ð</sub>A:11<sub>Þ</sub>

$$
e ^ {\int_ {1} ^ {\tau} \frac {1}{\tau a} d \tau} = e ^ {\frac {1}{a} l n \tau} = e ^ {(l n \tau) ^ {\frac {1}{a}}} = \tau^ {\frac {1}{a}},\tag{A.12}
$$

it follows that the cost difference function, f, decreases when

$$
s (\tau) > s (1) \tau^ {\frac {u _ {s} - k _ {e} k _ {s}}{k _ {e} k _ {s}}}.
$$

□

<sub>ð</sub>A:13<sub>Þ</sub>

A.3. Proof of the Proposition 3

Proof. Eq. (3.6) takes the following form for exponential growth:

$$
f = u _ {s} p _ {o} s (1) \frac {g ^ {\tau} - g}{l n g} - k _ {e} k _ {s} p _ {o} s (1) g ^ {\tau} \tau .\tag{A.14}
$$

Let us now take the derivative of the cost difference function:

$$
\begin{array}{l} \frac {d f}{d \tau} = u _ {s} p _ {o} s (1) g ^ {\tau} - k _ {e} k _ {s} p _ {o} s (1) \big (l n g g ^ {\tau} \tau + g ^ {\tau} \big) \\ = g ^ {\tau} p _ {o} s (1) (u _ {s} - k _ {e} k _ {s} l n g \tau - k _ {e} k _ {s}). \end{array}\tag{A.15}
$$

Because $p _ { o } > 0 , s ( 1 ) > 0 ,$ and $g ^ { \tau } > 0 ,$ derivative A.15 is negative if $u _ { s } \mathrm { ~ - ~ } k _ { e } \mathrm { ~ } k _ { \mathrm { ~ } }$ ln $g \tau - k _ { e } k _ { s } < 0$ . Thus, the cost difference function decreases, if

$$
\tau > \frac {u _ {s} - k _ {e} k _ {s}}{\ln (g) k _ {e} k _ {s}}.\tag{A.16}
$$

The ratio <sup>u</sup>s<sup>−k</sup>e <sup>k</sup>s is likely to be a small constant (e.g., for realistic values $u _ { s } = 1 0 , \dot { k _ { e } } = 2 , k _ { s } = 2 ,$ , and $g = 2$ , the value of the ratio is $2 . 1 6 ,$ which indicates a one day-long acquisition interval for 12 h public charging period), below which the acquisition interval length cannot be reasonably shortened further. Thus, the cost difference between public and private storage decreases with the growth of the acquisition interval for exponential growth.

□

## A.4. Proof of the Proposition 4

Proof. The cost difference function is de<sup>fi</sup>ned as follows when the storage needs grow linearly with time:

$$
f (\tau) = u _ {s} p _ {o} \left(s (1) \tau + g \frac {\tau^ {2}}{2} - s (1) - \frac {g}{2}\right) - k _ {e} k _ {s} p _ {o} \tau (s (1) + g \tau).\tag{A.17}
$$

Let us take the derivative of function A.17 with respect to the acquisition interval, τ:

$$
\frac {d f}{d \tau} = p _ {o} (\tau g (u _ {s} - 2 k _ {e} k _ {s}) + s (1) (u _ {s} - k _ {e} k _ {s})).\tag{A.18}
$$

Let us now denote the ratio $\begin{array} { r } { q = \frac { u _ { s } } { k _ { e } k _ { s } } { > 0 } . } \end{array}$ Because $p _ { o } > 0 ,$ , function A.17 increases if derivative A.18 is positive. Thus, A.17 increases when

$$
\tau g (q - 2) + s (1) (q - 1) > 0.\tag{A.19}
$$

Let us now consider the following cases:

• $\mathrm { f } q \ge 2$ then A.19 is true because $\tau > 0 , g > 0$ and $s ( 1 ) > 0 .$ . Thus, the function A.17 monotonically increases in this case.

• If $1 < q < 2 ,$ function A.17 increases if

$$
\tau <   - \frac {s (1)}{g} \frac {q - 1}{q - 2}.\tag{A.20}
$$

• I $\lceil q \leq 1$ then inequality A.19 cannot be satis<sup>fi</sup>ed because $\tau > 0 , g > 0$ and $s ( 1 ) > 0$

In summary, the function monotonically increases $\begin{array} { r } { \mathrm { i f } \frac { u _ { s } } { k _ { e } k _ { s } } { \geq } 2 , } \end{array}$ , or if 1b <sup>u</sup>s b2 and $\tau { < } - \frac { s ( 1 ) \ u _ { s } { - } k _ { e } \ k _ { s } } { g \ u _ { s } { - } 2 k _ { e } \ k _ { s } } .$ . □

## A.5. Proof of the Proposition 5

Proof. The cost difference function takes the following form for logarithmic growth:

$$
f (\tau) = u _ {s} p _ {o} s (1) (\tau l n \tau - \tau - 1) - k _ {e} k _ {s} p _ {o} s (1) l n \tau \tau .\tag{A.21}
$$

We obtain the following by taking the derivative of the function:

$$
\begin{array}{c} \frac {d f (\tau)}{d \tau} = p _ {o} s (1) (u _ {s} l n \tau - k _ {e} k _ {s} - k _ {e} k _ {s} l n \tau) \\ = p _ {o} s (1) ((u _ {s} - k _ {e} k _ {s}) l n \tau - k _ {e} k _ {s}). \end{array}\tag{A.22}
$$

The cost difference function increases when derivative 41 is positive. Because $p _ { o } > 0$ and $s ( 1 ) > 0 ,$ , and because of the assumption $u _ { s } > k _ { e } k _ { s }$ the derivative is positive when

ke ks τ N e <sup>u</sup>s−<sup>k</sup>e <sup>k</sup>s :

<sub>ð</sub>A:23<sub>Þ</sub>

Because $e ^ { \frac { k _ { e } k _ { s } } { u _ { s } - k _ { e } k _ { s } } }$ is a small constant, the cost difference function monotonically increases for reasonable acquisition interval lengths. □

## A.6. Proof of the Proposition 6

Proof. Let us de<sup>fi</sup>ne the cost-ratio function, f:

$$
\begin{array}{l} f (\tau) = c _ {p} - c _ {o} \\ \qquad = (u _ {s} p _ {o} + k _ {b} p _ {b o}) \int_ {1} ^ {\tau} s (t) d t - (k _ {e} k _ {s} s (\tau) p _ {o} \tau + k _ {b} s (\tau) p _ {b o} \tau). \end{array}\tag{A.24}
$$

Let us now take the derivative of function A.24 with respect to the acquisition interval, τ:

$$
\frac {d f}{d \tau} = (u _ {s} p _ {o} + k _ {b} p _ {b o}) s (\tau) - (k _ {e} k _ {s} p _ {o} + k _ {b} p _ {b o}) \left(\frac {d s (\tau)}{d \tau} \tau + s (\tau)\right).\tag{A.25}
$$

$$
= (u _ {s} p _ {o} - k _ {e} k _ {s} p _ {o}) s (\tau) - (k _ {e} k _ {s} p _ {o} + k _ {b} p _ {b o}) \tau \frac {d s (\tau)}{d \tau}.\tag{A.26}
$$

Because of assumptio $u _ { s } > k _ { e } k _ { s } ,$ , we will denote the ratio $a =$ $\frac { k _ { e } k _ { s } p _ { o } + k _ { b } p _ { b o } } { p _ { o } ( u _ { s } - k _ { e } k _ { s } ) } > 0$

Derivative A.25 is negative if

$$
s (\tau) - a \tau \frac {d s (\tau)}{d \tau} <   0.\tag{A.27}
$$

Inequality A.27 is the same Gronwall's inequality as A.3 and can be solved by following the same steps. Thus, the cost difference function decreases when

$$
s (\tau) > s (1) \tau^ {\frac {p _ {0} (u _ {s} - k _ {e} k _ {s})}{k _ {e} k _ {s} p _ {o} + k _ {b} p _ {b o}}}.\tag{A.28}
$$

If the storage needs grow relatively quickly, the function monotonically decreases as the acquisition interval increases, i.e., the costef<sup>fi</sup>ciency of the public cloud as compared with the private solution increases in the length of the acquisition interval.

## References

[1] I.F. Adams, D.D. Long, E.L. Miller, S. Pasupathy, M.W. Storer, Maximizing ef<sup>fi</sup>ciency by trading storage for computation, in: Proc, of the Workshop on Hot Topics in Cloud Computing (HotCloud).

[2] A. Benlian, T. Hess, Opportunities and risks of software-as-a-service: <sup>fi</sup>ndings from a survey of it executives, Decision Support Systems 52 (2011) 232–246.

[3] C. Bodenstein, M. Hedwig, D. Neumann, in: D.F. Galletta, T.P. Liang (Eds.), Strategic Decision Support for Smart-Leasing Infrastructure-As-A-Service ICIS Associatior for Information Systems, 2011.

[4] X. Cheng, C. Dale, J. Liu, Statistics and social network of youtube videos, Quality of Service, 2008. IWQoS 2008. 16th International Workshop on, 2008, pp. 229–238.

[5] J. Gantz, D. Reinsel, Extracting value from chaos, IDC iView, available from http:// idcdocserv.com/11422011(last retrived on 29.2.2012).

[6] F. Gens, IDC Predictions 2012: Competing for 2020, Report, IDC, 2011.

[7] J. Hamilton, Cloud computing economies of scale, MIX10, 2010.

[8] M. Hedwig, S. Malkowski, C. Bodenstein, D. Neumann, Datacenter investment support system (daisy), Proceedings of the 2010 43rd Hawaii International Conference on System Sciences, HICSS '10, IEEE Computer Society, Washington, DC, USA, 2010, pp. 1–10.

[9] A. Khajeh-Hosseini, D. Greenwood, J.W. Smith, I. Sommerville, The cloud adoption toolkit: supporting cloud adoption decisions in the enterprise, Software: Practice and Experience—Special Issue on Software Architectures and Application Development Environments for Cloud Computing, 2011.

[10] A. Khajeh-Hosseini, D. Greenwood, J.W. Smith, I. Sommerville, The cloud adoption toolkit: supporting cloud adoption decisions in the enterprise, Software: Practice and Experience 42 (2012) 447–465

[11] L. Mastroeni, M. Naldi, Long-range evaluation of risk in the migration to cloud storage, Commerce and Enterprise Computing (CEC), 2011 IEEE 13th Conference on, 2011.pp.260-266

[12] O. Mazhelis, P. Tyrväinen, Economic aspects of hybrid cloud infrastructure: user organization perspective, Information Systems Frontiers (2011) 1–25.

[13] O. Mazhelis, P. Tyrväinen, Role of data communications in hybrid cloud costs, in: Proceedings of the 37th EUROMICRO Conference on Software Engineering and Advanced Applications.

[14] C. Morris, Data Backup and Archiving on the HFS, Oxford University Computing Services. 2011. (available from http://www.oucs.ox.ac.uk/hfs/. last retrived on 23.2.2012).

[15] K.K. Muniswamy-Reddy, P. Macko, M. Seltzer, Making a cloud provenance-aware, in: 1st Workshop on the Theory and Practice of Provenance

[16] K.K. Muniswamy-Reddy, P. Macko, M. Seltzer, Provenance for the cloud, in: Proceedings of the 8th USENIX conference on File and storage technologies, USENIX Association, pp. 15–14.

[17] K.K. Muniswamy-Reddy, M. Seltzer, Provenance as <sup>fi</sup>rst class cloud data, ACM SIGOPS, Operating Systems Review 43 (2010) 11–16.

[18] T. Nu<sup>fi</sup>re, Petabytes on a budget v2.0: Revealing more secrets, Backblaze blog, available from http://blog.backblaze.com/2011/07/20/petabytes-on-a-budget-v2- 0revealing-more-secrets/2011(last retrived on 15.2.2012).

[19] OUCS, OUCS Annual Report 2004–2005, Oxford University Computing Services, 2006, (available from http://www.oucs.ox.ac.uk/internal/annrep/annrep0405/, last retrived on 23.2.2012).

[20] E.D. Smith, F. Szidarovszky, W.J. Karnavas, A.T. Bahill, Sensitivity analysis, a powerful system validation technique, Open Cybernetics and Systemics Journal 2 (2008) 39–56.

[21] I. Smith, M. Fraser, Service Level Description: Back-up and Archiving Service (HFS), Oxford University Computing Services, 2011. (available from http://www.oucs.ox. ac.uk/internal/sld/hfs.xml, last retrived on 23.2.2012).

[22] G. Stigler, The economies of scale, Journal of Law and Economics 1 (1958) 54–71.

[23] B. Stiller, P. Reichl, S. Leinen, Pricing and cost recovery for internet services: practical review, classi<sup>fi</sup>cation and application of relevant models, NETNOMICS 3 (2001).

[24] J. Strebel, A. Stage, An economic decision model for business software application deployment on hybrid cloud environments, in: M. Schumann, L.M. Kolbe, M.H. Breitner, A. Frerichs (Eds.), Multikonferenz Wirtschaftsinformatik, Universittsverlag Gttingen, 2010, p. 195206

[25] I. Trummer, F. Leymann, R. Mietzner, W. Binder, Cost-optimal outsourcing of applications into the clouds, Cloud Computing Technology and Science (CloudCom), 2010 IEEE Second International Conference on, 2010, pp. 135–142.

[26] S. Uttamchandani, K. Voruganti, R. Routray, L. Yin, A. Singh, B. Yolken, Brahma: planning tool for providing storage management as a service, IEEE Internationa Conference on Services Computing (SCC 2007), 2007, pp. 1–10.

[27] E. Walker, W. Brisken, J. Romney, To lease or not to lease from storage clouds, Computer 43 (2010) 44–50.

[28] J. Weinman, Cloudonomics: a rigorous approach to cloud bene<sup>fi</sup>t quanti<sup>fi</sup>cation, The Journal of Software Technology 14 (2011) 10–18.

[29] J. Weinman, Mathematical proof of the inevitability of cloud computing, Working paper, 2011, (available from http://www.joeweinman.com last retrieved on February 28, 2012).

[30] J. Weinman, Time is money: the value of “on-demand”, Working paper, 2011, (available from http://http://www.joeweinman.com last retrieved on February 28, 2012).

[31] D. Yuan, Y. Yang, X. Liu, J. Chen, A cost-effective strategy for intermediate data storage in scienti<sup>fi</sup>c cloud work<sup>fl</sup>ow systems, Parallel & Distributed Processing (IPDPS), 2010 IEEE International Symposium on, IEEE, 2010, pp. 1–12.

[32] D. Yuan, Y. Yang, X. Liu, J. Chen, On-demand minimum cost benchmarking for intermediate dataset storage in scienti<sup>fi</sup>c cloud work<sup>fl</sup>ow systems, Journal of Parallel and Distributed Computing 71 (2011) 316–332.

[33] D. Yuan, Y. Yang, X. Liu, G. Zhang, J. Chen, A data dependency based strategy for intermediate data storage in scienti<sup>fi</sup>c cloud work<sup>fl</sup>ow systems, Concurrency and Computation: Practice and Experience 24 (2010) 956–976.

Gabriella Laatikainen is a PhD student at the Department of Computer Science and Information Systems, University of Jyväskylä, Finland. She received a degree of MSc. Mathematics and Computer Science from University of Debrecen, Hungary in 2007. Her research interests include cloud services, software pricing, business models in IT services industry.

Oleksiy Mazhelis is a post-doc researcher at the Department of Computer Science and Information Systems, University of Jyväskylä, Finland. He received a degree of MSc (Specialist) from Kharkov National University of Radio-Electronics, Ukraine in 1997, and received his licentiate and doctoral degrees from the University of Jyväskylä in 2004 and 2007, respectively. Starting from 2004, he was working in various research projects conducted in collaboration with industrial partners. His current research interests encompass techno-economics, systems analysis, machine learning, and pattern recognition, applied to the domains of software industry evolution, internet-of-things, telecommunications and cloud software, as well as intelligent transportation systems.

Pasi Tyrväinen is Professor of Information Systems and vice Dean at the Faculty of IT at the University of Jyväskylä. He received his doctoral degree at Helsinki University of Technology in 1994 and is a member of IEEE, ACM and AoM. His previous af<sup>fi</sup>liations include R&D management positions at Honeywell Industrial Control and Nokia Research Center. His research interests include enterprise content management, cloud services and software business, and studies in these areas laid the ground for establishing the ICSOB conference series on software business research in 2010. On these subjects he has written several books and published numerous articles both in business and engineering management journals.
