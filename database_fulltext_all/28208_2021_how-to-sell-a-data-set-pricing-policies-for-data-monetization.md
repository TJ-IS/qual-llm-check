---
otero_id: 28208
otero_key: "CVTDX6BR"
title: "How to Sell a Data Set? Pricing Policies for Data Monetization"
authors: "Sameer Mehta; Milind Dawande; Ganesh Janakiraman; Vijay Mookerjee"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1027"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# How to Sell a Data Set? Pricing Policies for Data Monetization

Sameer Mehta,<sup>a</sup> Milind Dawande,<sup>b</sup> Ganesh Janakiraman,<sup>b</sup> Vijay Mookerjee<sup>b</sup>

<sup>a</sup> Rotterdam School of Management, Erasmus University, 3062 PA Rotterdam, Netherlands; <sup>b</sup> Naveen Jindal School of Management, The University of Texas at Dallas, Richardson, Texas 75080-3021

Contact: mehta@rsm.nl, https://orcid.org/0000-0002-0410-3248 (SM); milind@utdallas.edu, https://orcid.org/0000-0001-6956-0856 (MD); ganesh@utdallas.edu, https://orcid.org/0000-0001-7386-4318 (GJ); vijaym@utdallas.edu, https://orcid.org/0000-0001-5583-3585 (VM)

Received: February 10, 2020 Revised: October 4, 2020; February 9, 2021 Accepted: March 21, 2021 Published Online in Articles in Advance: September 10, 2021

https://doi.org/10.1287/isre.2021.1027

Copyright: © 2021 INFORMS

Abstract. The wide variety of pricing policies used in practice by data sellers suggests that there are signi<sup>fi</sup>cant challenges in pricing data sets. In this paper, we develop a utility framework that is appropriate for data buyers and the corresponding pricing of the data by the data seller. Buyers interested in purchasing a data set have private valuations in two aspects—their ideal record that they value the most, and the rate at which their valuation for the records in the data set decays as they differ from the buyers’ ideal record. The seller allows individual buyers to <sup>fi</sup>lter the data set and select the records that are of interest to them. The multidimensional private information of the buyers coupled with the endogenous selection of records makes the seller’s problem of optimally pricing the data set a challenging one. We formulate a tractable model and successfully exploit its special structure to obtain optimal and near-optimal data-selling mechanisms. Speci<sup>fi</sup>cally, we provide insights into the conditions under which a commonly used mechanism—namely, a pricequantity schedule—is optimal for the data seller. When the conditions leading to the optimality of a price-quantity schedule do not hold, we show that the optimal price-quantity schedule offers an attractive worst-case guarantee relative to an optimal mechanism. Further, we numerically solve for the optimal mechanism and show that the actual performance of two simple and well-known price-quantity schedules—namely, two-part tariff and two-block tariff—is near optimal. We also quantify the value to the seller from allowing buyers to <sup>fi</sup>lter the data set.

History: Ram Gopal, Senior Editor; Juan Feng, Associate Editor. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2021.1027.

Keywords: data monetization multidimensional mechanism design price-quantity schedules

## 1. Introduction

The use of targeted marketing is a prevalent and growing activity across industries and businesses. There are many ways in which <sup>fi</sup>rms execute targeted marketing campaigns, for instance, by outsourcing such campaigns to marketing <sup>fi</sup>rms/social media platforms (Lee et al. 2018), or by acquiring data on their potential customers from data aggregators and executing the campaigns in-house (ANA 2018). The latter approach, wherein data are transferred from the seller to the buyer, is widely used and is the context in which our work is situated. Major players (known as data brokers) in this data-selling market include Acxiom, Nielsen, Oracle, Teradata, and Experian.

In this paper, we develop a utility framework that is appropriate for a data buyer and the corresponding pricing of the data by the data seller. To motivate the need for these contributions, we begin by examining several real-world data-selling <sup>fi</sup>rms and the pricing policies they use.

<sub>•</sub> BookYourData (BYD), https://www.bookyourdata .com

– Context: BYD offers ready-made lists of contacts of business individuals across different industries, job titles, job functions, and job levels. Examples include a list of healthcare professionals, a list of chief executive of<sup>fi</sup>cers and chief <sup>fi</sup>nancial of<sup>fi</sup>cers (CFOs), a list of chiefs and vice presidents of information technology <sup>fi</sup>rms, and a list of computer equipment manufacturers. A record in a list consists of contact information such as name, email address, job function, job department, and country. These niche data sets are typically used by marketers who are interested in targeting a speci<sup>fi</sup>c set of business individuals.

– Pricing: BYD provides a variety of <sup>fi</sup>ltering options to buyers so that they can select a subset of records of their choice from any given list. For instance, from the list of healthcare professionals, a buyer can use location <sup>fi</sup>lters such as country, state, zip code, specialty <sup>fi</sup>lters such as dentists, chiropractors, or website-domain <sup>fi</sup>lters such as.com,.gov,.org, to target the healthcare professionals of interest. BYD uses a nonlinear price-quantity schedule to price the set of records selected by a buyer (see Figure 1(a)). That is, the price for any set of records depends only on the number of records in that set and not on the identity of the records; speci<sup>fi</sup>cally, the price is an increasing and concave function of the number of records.

CLASSIC (basic info)  
Figure 1. (Color online) Different Pricing Policies Used by Data Sellers

<table><tr><td colspan="2">(a) Book Your Data</td></tr><tr><td># OF RECORDS</td><td>PRICES</td></tr><tr><td>250 - 500</td><td>$79.00 - $129.00</td></tr><tr><td>500 - 1,000</td><td>$129.00 - $239.00</td></tr><tr><td>1,000 - 2,500</td><td>$239.00 - $399.00</td></tr><tr><td>2,500 - 5,000</td><td>$399.00 - $659.00</td></tr><tr><td>5,000 - 10,000</td><td>$659.00 - $1,099.00</td></tr><tr><td>10,000 - 25,000</td><td>$1,099.00 - $2,199.00</td></tr><tr><td>25,000 - 50,000</td><td>$2,199.00 - $3,299.00</td></tr><tr><td>50,000 - 100,000</td><td>$3,299.00 - $5,499.00</td></tr></table>

<sub>(c)</sub> Direct Mail

<table><tr><td></td><td>Number of Records</td><td>Price Per Record</td></tr><tr><td rowspan="4">Base Schedule</td><td>1 - 5,000</td><td>$0.049/record</td></tr><tr><td>5,001 - 10,000</td><td>$0.045/record</td></tr><tr><td>10,001 - 15,000</td><td>$0.039/record</td></tr><tr><td>20,001+</td><td>$0.034/record</td></tr><tr><td rowspan="8">Filter-based Schedule</td><td>Record Type</td><td>Price Per Record</td></tr><tr><td>Age</td><td>$0.0035/record</td></tr><tr><td>Dwelling Type</td><td>Free</td></tr><tr><td>Estimated Current Home Value</td><td>$0.005/record</td></tr><tr><td>Estimated Income</td><td>$0.002/record</td></tr><tr><td>Exact Age</td><td>$0.005/record</td></tr><tr><td>Gender</td><td>Free</td></tr><tr><td>Homeowner Status</td><td>$0.004/record</td></tr></table>

## SalesLead (SL), http://sales-lead.org

– Context: SL maintains a variety of data sets of American businesses in the form of professionbased lists and state/province-based lists. For example, the Accountant Sales Leads data set contains records of United States-based accountants, whereas the Alabama Sales Leads data set contains records of different businesses (accountants, realestate agents, etc.) based in Alabama. Each record in a data set consists of contact information such as mailing address, geolocation, email address, phone number, website, and Google pagerank. These data sets are available for purchase in the form of buyall-or-buy-nothing packages.

## <sub>(b)</sub> Sales Lead

Accountant Sales Leads, only \$49.00

Contains 199,496 records including 12,350 emails! Purchase accountants.zip now for \$49.00

Insurance Sales Leads, only \$49.00

Contains 308,724 records including 25,941 emails! Purchase insurance.zip now for \$49.00

Real Estate Sales Leads, only \$49.00

Contains 387,396 records including 63,101 emails! Purchase real-estate.zip now for \$49.00

Alabama Sales Leads, only \$49,00

Contains 300,796 records including 28,205 emails! Purchase alabama-sales-leads.zip now for \$49.00

<sub>(d)</sub> TelephoneLists

<table><tr><td>USA</td><td>Canada</td></tr><tr><td>$239 per State or or $199 each for more than 1 state</td><td>$239 per province or $199 each for more than 1 province</td></tr><tr><td>$1,995 entire USA</td><td>$995 entire Canada</td></tr><tr><td colspan="2">TARGETED (demographic info)</td></tr><tr><td colspan="2">USA only</td></tr><tr><td colspan="2">$79 per zip code</td></tr><tr><td colspan="2">$399 per state or $359 each for more than 1 state</td></tr><tr><td colspan="2">$3,495 entire USA</td></tr></table>

– Pricing: SL uses a simple <sup>fl</sup>at-fee pricing policy. Unlike BYD, the buyers here do not have an option of <sup>fi</sup>ltering records of their choice within a data set; that is, they can only purchase the entire data set. Further, although the data sets differ signi<sup>fi</sup>cantly in the number of records they contain, SL often charges the same price for each of them. For example, each of the four data sets shown in Figure 1(b) is priced at \$49.

DirectMail (DM), https://www.directmail.com

– Context: Targeted mailing lists are one of the key products that DM offers its clients as part of a marketing solution. The mailing lists include business lists as well as consumer lists such as new movers and new homeowners. The consumer lists also have information on the lifestyle and interests of the corresponding individuals.

– Pricing: DM uses a price schedule that is based on the number of records selected and the set of <sup>fi</sup>lters used to obtain those records. To illustrate this pricing policy, let us consider the following example: Suppose a buyer is interested in purchasing a new homeowners list. the buyer uses the <sup>fi</sup>lters age, gender, and homeowners to select a total of 7,000 records. Then, the price per record is de<sup>fi</sup>ned by the total quantity (7,000) and the three speci<sup>fi</sup>c <sup>fi</sup>lters used by the buyer to arrive at the buyer’s chosen set of records. The pricing policy is shown in Figure 1(c). For our example, the base price per record is equal to \$0.045 (calculated from the base schedule) and the <sup>fi</sup>lter-based price per record is equal to \$0.0035 \$0 \$0.004 \$0.0075 (calculated from the <sup>fi</sup>lter-based schedule). Thus, the total price per record is equal to \$0.045 \$0.0075 \$0.0525; the buyer pays a total amount of \$367.5 for the selected 7,000 records.

TelephoneLists (TL), https://www.telephonelists.biz – Context: TL is a telemarketing <sup>fi</sup>rm that specializes in offering phone lists as data sets. The data set consists of information on consumers (contact details, demographics, etc.) as well as businesses (number of employees, sales volume, etc.) in the United States and Canada. A key feature of its data set is the do-not-call <sup>fl</sup>ag for each record, which is critical information for telemarketers to avoid calling <sup>fl</sup>agged individuals.

– Pricing: For one-time buyers, TL offers its data based on the desired zip codes and/or states/provinces. Thus, the extent of <sup>fi</sup>ltering here is limited— buyers can select the zip codes of their choice but cannot <sup>fi</sup>lter the records further within those zip codes. Interestingly, the pricing is based not on the number of records purchased but on the number of zip codes and/or states/provinces selected by the buyer (see Figure 1(d)).

Common across these examples is the structure of the data set that the <sup>fi</sup>rms offer for sale—data are represented in rows and columns; each row is a record, that is, information about an entity, and, for a given row, each column represents an attribute of that record. The pricing policies in these examples are reasonably simple. BYD offers a price-quantity schedule, SL uses <sup>fl</sup>at-fee pricing, DM employs a price schedule that is based on the quantity as well as the <sup>fi</sup>lters used to select the data, and TL charges based on the number of zip codes/states/provinces. Although business needs dictate that pricing should be simple and easily understood, it is not clear if the use of a simple pricing policy results in the seller sacri<sup>fi</sup>cing a signi<sup>fi</sup>cant amount of revenue. A natural way to examine this is by obtaining an optimal pricing structure for such data sets, a question that we address.

It is important to clarify that the context we envision in this paper is the selling of publicly available information that the data seller has worked to compile and process. In contrast, there is also a stream of literature on market models that expressly considers privacy of data and compensating individuals for the sharing of information; see, for example, Gar<sup>fi</sup>nkel et al. (2006), Li et al. (2014), and Cai et al. (2019).

The selling of data is more nuanced than that of information goods such as telephone minutes and bandwidth in the sense that, for a buyer, it is not just the amount of data (i.e., the number of records) that matters but also the type of the data. For instance, presented with the same data set, a buyer interested in targeting those in need of apartment rentals will likely be interested in records that are quite different from those that appeal to a buyer who wants to reach out to healthcare professionals. Thus, the ability to <sup>fi</sup>lter the data has an important implication on buyers’ decisions; it allows heterogeneous buyers to endogenously choose the records that interest them. We will incorporate this notion of <sup>fi</sup>ltering in developing an appropriate utility framework for buyers. Also, note that since the amount of data is not the sole criterion for a buyer, it is not immediately clear whether a data seller should use a pricing policy based only on the amount.

We envision the data set for sale to consist of many records, one corresponding to each row of the data set. The attributes of the records form the columns of the data set. Thus, if there are N columns in the data set, then each record can be viewed as an Ndimensional vector. Each buyer has an ideal record (which may or may not necessarily be part of the data set) that the buyer values the most. For instance, in a data set of healthcare providers, an ideal record for a medical equipment marketer in Dallas, Texas, might be that of a cardiologist who has more than 20 years of experience, accepts Medicaid insurance, has a Yelprating of at least four stars, and is located in Dallas. We employ the notion of a distance metric to measure how close a speci<sup>fi</sup>c record in the data set is to a buyer’s ideal record. The ideal record as well as the decay in utility with distance can both differ across buyers. Thus, the buyers are heterogeneous in two aspects: one, their respective ideal records, which are Ndimensional vectors; and two, the rate at which their utility for records in the data set decreases as they move away from their ideal records. Thus, each buyer is endowed with N 1 -dimensional private information. Buyers use their private information and the seller’s pricing policy to purchase the records of their choice. Anticipating the buyers’ decisions, the seller’s goal is to design a pricing policy to maximize the seller’s expected revenue.

With this brief overview, we now summarize our main contributions.

## 1.1. Our Contributions

As is clear from the previous discussion, one approach for the buying and selling of data can be based on the formalization of several context-speci<sup>fi</sup>c characteristics, for example, the notion of an ideal record for a buyer (which is the buyer’s private information) and the corresponding heterogeneity across buyers, the decay in a buyer’s utility for a record as a function of its distance from the buyer’s ideal record (also private to the buyer) and the corresponding heterogeneity across buyers, and the <sup>fi</sup>ltering of data to enable the endogenous selection of records. Thus, the formulation of a tractable model to obtain an optimal dataselling mechanism is itself a nontrivial task. Although multidimensional mechanism design problems are well-known to be intractable in general, we successfully exploit the special structure of our model to examine it both analytically and numerically. Here, it is important to clarify that there can be other potential approaches for the buying and selling of data, for example, negotiations or long-term contracts. Our approach is well-suited due its simplicity, tractability, and scalability.

We show that when the data set exhibits a special structure, a price-quantity schedule is an optimal data-selling mechanism (Theorem 2 and Corollary 2). Under a price-quantity schedule, the price for a given number of records does not depend on the identity of the records chosen by the buyer. However, as discussed earlier, the records of interest differ across buyers since each buyer naturally prefers to buy records that are closest to the buyer’s ideal record. Put differently, for a given cardinality of records, say q, different buyers would prefer different sets of q records. Thus, one would expect an optimal pricing policy to specify a price for each potential set of records that a buyer can select. Clearly, it would be impractical to even specify such a set-based pricing schedule due to its exponential size, let alone compute the optimal pricing policy. Thus, the signi<sup>fi</sup>cance of our result lies in the implication that in the search for an optimal pricing mechanism, the seller can restrict attention to schedules in which price depends only on the number of records chosen by the buyer and not on the identity of those records.

A natural question then arises: Even when the assumptions that result in the optimality of pricequantity schedules do not hold, can an optimal pricequantity be provably near optimal? We answer this question in the af<sup>fi</sup>rmative by establishing a worstcase (theoretical) bound on the seller’s revenue from an optimal price-quantity schedule with respect to that from an optimal mechanism (Theorem 3). Further, we numerically examine two popular classes of pricequantity schedules: (i) two-part tariffs (speci<sup>fi</sup>ed by a <sup>fi</sup>xed-fee and a price per record), and (ii) two-block tariffs (a piece-wise linear function with two different slopes). We obtain the optimal schedule within each of these classes and demonstrate that it achieves an attractive performance relative to the optimal mechanism (Section 6.4 and Section E in the online appendix).

We also examine the value that accrues to the seller from allowing the buyers to <sup>fi</sup>lter data (Section E.3 in the online appendix). For buyers, the ability to <sup>fi</sup>lter the data allows them to endogenously select any subset of records that is of interest to them. In the absence of <sup>fi</sup>ltering, buyers face a take-it-or-leave-it offer from the seller—either purchase all the records in the data set at the stated price or buy nothing. Since this mechanism is a feasible solution to the seller’s mechanism design problem (in which <sup>fi</sup>ltering is allowed), it is clear that, under the setting of our analysis, the seller can only bene<sup>fi</sup>t by offering the <sup>fi</sup>ltering option. This value of <sup>fi</sup>ltering depends on the fraction of records in the data set that yield positive utility to the buyer: The lower this fraction, the more important it is for the buyer to use <sup>fi</sup>ltering to identify the desired set of records and, thus, higher is the value of <sup>fi</sup>ltering.

## 1.2. Organization of the Paper

We review the literature related to our work in Section 2. Section 3 presents the preliminaries of our model and Section 4 formulates the multidimensional mechanism design problem. In Section 5, we formulate a relaxation of this problem and obtain an optimal mechanism for the relaxed problem. Using the solution of the relaxed problem, we show that, under certain assumptions, a price-quantity schedule is an optimal solution to the multidimensional mechanism design problem. Section 6 analyzes the scenario where these assumptions are not met. Here, we <sup>fi</sup>rst show that an optimal mechanism may not necessarily belong to the class of price-quantity schedules and then obtain a worst-case performance guarantee offered by an optimal price-quantity schedule. We also develop an approach to numerically evaluate the optimal mechanism and use this as a benchmark to examine the performance of two popular price-quantity schedules as well as to assess the value of <sup>fi</sup>ltering to the data seller. Section 7 concludes the paper.

## 2. Related Literature

Our work is related to the following streams of literature: (i) pricing of information goods, (ii) commodi<sup>fi</sup>cation of data and information, and (iii) multidimensional mechanism design. We now review each of these streams.

## 2.1. Pricing of Information Goods

The classical papers of Mussa and Rosen (1978) and Maskin and Riley (1984) focus on the nonlinear pricing of goods. The former work considers the pricing of a single unit of a good and assumes that a buyer’s utility is contingent on the buyer’s type and the quality of the good purchased. The latter work develops a more general utility framework, where a buyer’s utility is in<sup>fl</sup>uenced by the buyer’s type and the quality as well as the quantity of the good purchased. Spence (1980) develops a utility framework for selling bundles of goods to consumers, and solves the pricing problem for a given set of bundles. In general, the buying and selling of data offers a richer environment than this classical setting in the sense that, even for a data set of a given quality (e.g., a <sup>fi</sup>xed set of attributes for each record in the data set), the buyers’ utilities are not only affected by their type and the quantity of records purchased (i.e., how much data?), but also by the speci<sup>fi</sup>c subset of records purchased (i.e., which records in the data?). Further, in the classical setting, only the type of the buyer is private knowledge, whereas in the dataselling context, the buyer is endowed with multidimensional private information—namely, the vector of attributes of the buyer’s ideal record (i.e., one that the buyer values the most) and the rate at which the buyer’s valuation for a record decays as its distance from the buyer’s ideal record increases. We contribute to this stream by developing an appropriate and tractable utility framework that incorporates these context-speci<sup>fi</sup>c features.

Two related substreams are those that investigate the notion of bundling for pricing information goods (Bakos and Brynjolfsson 1999, Geng et al. 2005, Wu et al. 2008, Wu et al. 2018) and payment mechanisms (Sundararajan 2004, Choudhary 2010, Chen and Huang 2016). In the data-selling context, when the seller allows buyers to <sup>fi</sup>lter a data set, they are able to bundle the records of their choice, that is, select a customized subset of records from that data set. This is akin to the seller offering all possible bundles of records. Our analysis allows the seller to offer the <sup>fi</sup>ltering option to buyers; we also quantify the value of this option to the seller. Since the price for a set of records may depend on the identity of the records, the most general pricing schedule for data is one that lists a separate price for each subset of records. Our analysis begins with this general form and shows how, under certain conditions, the simpler quantity-based pricing mechanism (i.e., price-quantity schedule) is optimal.

## 2.2. Commodification of Data and Information

Agarwal et al. (2019) study the challenges associated with creating a two-sided market for buying and selling data for machine learning tasks. Bhargava et al. (2020) derive heuristic mechanisms for selling goods (such as sales leads data) for a setting where buyers can either have shared or exclusive access to the data set; the latter option is more expensive. As will be discussed in Section 3, exclusivity does not play a role in our setting. The fact that the buyers are not concerned about exclusive access to the data set allows us to focus our analysis on the trade between the seller and one buyer. Besides this contextual difference, our paper also differs from Bhargava et al. (2020) in technical aspects. For instance, our model captures the preferences of the buyers across all the columns in the data set (by representing a record with N columns as an Ndimensional vector) as well as the preferences over different records in the data set (through the decay parameter t). On the <sup>fl</sup>ip side, Bhargava et al. (2020) model the preferences of a buyer over a single item, which can be viewed either as a single record or the entire data set. Thus, if one views the entire data set as a single item, then the model in Bhargava et al. (2020) assumes that the buyer can buy either the entire data set or nothing at all.

Kushal et al. (2012) analyze a simplistic model for pricing data in which a buyer’s utility does not depend on the identity of the records bought but only on the quantity. Assuming that there is no heterogeneity among data buyers (i.e., they all have the same willingness to pay), the authors analyze two speci<sup>fi</sup>c models for pricing data, namely unit pricing and step pricing. Muschalle et al. (2012) survey pricing approaches adopted by established data vendors from different market environments. Bergemann et al. (2018) analyze a setting where buyers, endowed with initial private information, seek supplemental data from sellers who provide statistical experiments as information products—that is, signals that reveal information about the payoff-relevant state—and derive an optimal menu of statistical experiments for the seller. Bimpikis et al. (2019) study the problem of selling information (such as demand forecasts) to competing <sup>fi</sup>rms and show that the seller’s strategy is primarily driven by the nature and intensity of competition among the buyers.

Gar<sup>fi</sup>nkel et al. (2006) consider a market where the private information of individuals in the form of numeric data is transacted. The authors develop a security mechanism that safeguards private information of the individuals and a market model that compensates individuals for the use of their private information. Li et al. (2014) develop a theoretical framework for selling private data where buyers can purchase noisy queries and the data owners are compensated for the privacy loss that they incur for each query. Cai et al. (2019) propose a framework for trading web browsing histories of individuals by considering their diverse privacy preferences as well as the utility of the end consumers.

## 2.3. Multidimensional Mechanism Design

The seminal work of Myerson (1981) characterizes an optimal mechanism for selling a single unit to buyers who are endowed with single-dimensional private information. Although there is no general framework thus far to obtain a similar result for multidimensional mechanism design problems, we exploit structural properties of our setting to obtain an optimal mechanism for our multidimensional mechanism design problem, under reasonable conditions. When these conditions do not hold, we obtain a feasible mechanism that offers an attractive performance guarantee. Thus, our work contributes to the literature on approximate mechanisms for multidimensional problems; see, for example, Chawla et al. (2007) and Chawla et al. (2010). Further, to compute an optimal mechanism, we discretize the space of private information and formulate the multidimensional mechanism design problem as a linear program; examples of studies in which a similar approach has been used include Cai et al. (2011) and Lavi and Swamy (2011).

## 3. Model Preliminaries

We begin by describing the key elements of our model:

Data set: The focal data set, denoted by D, is assumed to be represented in a tabular form comprised of rows and columns; an illustrative example is shown in Table 1. Each row, which we refer to as a record, consists of information on an entity such as an individual or a <sup>fi</sup>rm. The columns of the data set represent the attributes associated with each record. The columns can be categorized into two sets: (i) <sup>fi</sup>lterable columns, consisting of the columns that the buyers use to <sup>fi</sup>lter the data (e.g., State, Provider\_Type, Has\_Ambulance, and Yelp\_Rating in Table 1), and (ii) non<sup>fi</sup>lterable columns, typically consisting of columns that provide contact information of the entities (e.g., Name and Phone\_No in Table 1). Thus, each record consists of a <sup>fi</sup>lterable part and a non<sup>fi</sup>lterable part. Henceforth, we will use the term “columns” to refer to the <sup>fi</sup>lterable columns of the data set. For instance, in the illustrative data set shown in Table 1, columns four to seven are <sup>fi</sup>lterable. Similarly, we will use the term “record” to refer to its <sup>fi</sup>lterable part. Note that this nomenclature implies that two records of the data set can be identical (e.g., records 9 and 10 in Table 1). The data set in Table 1 consists of 10 records and four columns.

We assume that the data set D consists of N real-valued columns<sup>1</sup> and that there is no missing entry. Thus, each record can be viewed as a vector in $\mathbb { R } ^ { N }$ . Let $\chi _ { i }$ denote the possible range of values of column $i , i = 1 , 2 , . . . , N ,$ and let $\chi = \times _ { i = 1 } ^ { N } \chi _ { i }$ denote the Cartesian product of these ranges. Thus, χ denotes the record space; that is, the set of all possible values a record in the data set can take. Let $g ( \cdot )$ denote the density function of records in the data set D. Thus, the number of records in the in<sup>fi</sup>nitesimal hypercube $[ { \pmb x } , { \pmb x } + d { \pmb x } ]$ is equal to g x dx. A metric $\rho : \mathbb { R } ^ { N } \times \dot { \mathbb { R } } ^ { N }  \mathbb { R } .$ measures the distance between any two records; thus, the distance between two records, say x and y, is ρ<sub>(</sub>x, y<sub>)</sub>.

Data seller: The monopolistic data seller’s goal is to design a pricing policy that maximizes the seller’s expected revenue. The seller allows each buyer to <sup>fi</sup>lter the data through the <sup>fi</sup>lterable columns of the data set and select a set of records to purchase. For each record selected by a buyer, the seller provides the entire record (i.e., the <sup>fi</sup>lterable part and the non<sup>fi</sup>lterable part of the record). Note that the same record(s) can be sold to multiple buyers.

Data buyers: Buyers are interested in purchasing records of their interest from the data set. Examples include a furniture retailer interested in purchasing a list of new movers in the buyer’s area of service and a pharmaceutical marketer interested in targeting physicians in Texas who have more than 20 years of experience. We assume that the purchase of a data set by one buyer does not affect the utilities, and consequently the decisions, of the other buyers. This assumption is satis-<sup>fi</sup>ed under several reasonable data-selling contexts. For instance, when the data set offered by the seller is for general-purpose use such as telemarketing or mass-advertising campaigns, or when the business interests of the buyers are nonoverlapping, or when buyers operate in different geographies or serve different demographics. Our communication with each of the four data sellers discussed in Section 1 con<sup>fi</sup>rmed that an exclusive access to the records in the data set is not a concern for their clients. Thus, the purchase decision of one buyer does not affect the utilities and, consequently, the decisions of the other buyers. This assumption allows us to focus our analysis on a single buyer.

Table 1. Illustrative Data Set Consisting of Information on Healthcare Providers

<table><tr><td>ID</td><td>Name</td><td>Phone_no.</td><td>State</td><td>Provider_Type</td><td>Has_Ambulance</td><td>Yelp_Rating</td></tr><tr><td>1</td><td>Castellanos Family Practice</td><td>6269158992</td><td>CA</td><td>Family practice</td><td>No</td><td>4.5</td></tr><tr><td>2</td><td>Charles A. Leroy</td><td>9095921461</td><td>CA</td><td>Health clubs</td><td>No</td><td>5</td></tr><tr><td>3</td><td>Edward P. Miranda</td><td>4153799815</td><td>CA</td><td>Plastic surgery</td><td>No</td><td>4</td></tr><tr><td>4</td><td>Fremont Urgent Care</td><td>5107961050</td><td>CA</td><td>Physicians</td><td>Yes</td><td>3</td></tr><tr><td>5</td><td>AFC Exp. Urgent Care</td><td>4127815300</td><td>PA</td><td>Physicians</td><td>Yes</td><td>4</td></tr><tr><td>6</td><td>Ethan Milgrom</td><td>2149822264</td><td>TX</td><td>Physicians</td><td>No</td><td>4.5</td></tr><tr><td>7</td><td>Chantilly Family Medicine</td><td>5713161557</td><td>VA</td><td>Family practice</td><td>No</td><td>5</td></tr><tr><td>8</td><td>Regan Family Care</td><td>6169587326</td><td>CA</td><td>Family practice</td><td>No</td><td>4</td></tr><tr><td>9</td><td>Focus MD – Richmond</td><td>8048590748</td><td>VA</td><td>Physicians</td><td>No</td><td>3.5</td></tr><tr><td>10</td><td>Gavin Kole</td><td>8146807413</td><td>VA</td><td>Physicians</td><td>No</td><td>3.5</td></tr></table>

Recall from Section 1 the notion of a buyer’s ideal record, namely one the buyer values the most; this record does not necessarily have to be part of the focal data set. We denote the buyer’s ideal record by $\overline { { \mathbf { x } } } \in \boldsymbol { \chi } \subseteq \mathbb { R } ^ { N }$ . The N-dimensional vector x is private information of the buyer; that is, only the buyer knows the location of x in the record space χ. The seller only has a distributional knowledge of $\overline { { \mathbf { x } } } ;$ let $F ( \cdot )$ and $f ( \cdot )$ denote, respectively, the cumulative distribution function and the probability density function of x. We will interchangeably refer to the buyer’s ideal record as the buyer’s location type. We assume that the utility of any record $\mathbf { x } \in \chi$ to the buyer decreases as its distance $\rho ( { \overline { { \mathbf { x } } } } , \mathbf { x } )$ from the buyer’s ideal record x increases. Further, we assume that a parameter $t \in [ 0 , \tau ]$ , which is (also) private to the buyer, characterizes the rate of this decrease. We refer to t as the buyer’s decay type, of which the seller only has distributional knowledge; let $H ( \cdot )$ and $h ( \cdot )$ denote, respectively, cumulative distribution function (c.d.f.) and the probability distribution function (p.d.f.) of the decay type on the support <sub>[</sub>0, τ<sub>]</sub>. We assume that the distribution of the decay type is regular; that is, $\frac { h ( t ) } { 1 - H ( t ) }$ is nondecreasing in t. In summary, the buyer has private information in two aspects—namely, the location type $\overline { { \mathbf { x } } } \in \boldsymbol { \chi } \subseteq \mathbb { R } ^ { N }$ and the decay type, $t \in [ \bar { 0 } , \tau ] \cdot$ —and is characterized by the N 1 -dimensional tuple x, t .

Let us denote the utility to a buyer of decay type t from purchasing a record located at a distance $d \geq 0$ from the buyer’s ideal record by $v ( d , t )$ . Thus, for a buyer of type $( { \dot { \overline { { \mathbf { x } } } } } , t )$ , the utility obtained from purchasing a record $\mathbf { x } \in \chi$ is given by $v ( \rho ( \overline { { \mathbf { x } } } , \mathbf { x } ) , t )$

As is routine in the mechanism design literature, we assume certain reasonable properties on a buyer’s utility function $v ( d , t ) , d \geq 0 , t \in [ 0 , \bar { \tau } ]$ , that help keep the analysis tractable:

P1. Nonnegative $( v ( d , t ) \geq 0 )$ and $C ^ { 2 }$ (twice continuously differentiable).

P2. Decreasing with distance: $\begin{array} { r } { \frac { \partial v ( d , t ) } { \partial d } \leq 0 } \end{array}$ for all t.

P3. A higher value of decay type receives a higher utility: $\begin{array} { r } { \frac { \partial v ( d , t ) } { \partial t } \geq 0 , v ( d , 0 ) = 0 } \end{array}$ for all d.

P4. Concave in the decay type (Maskin and Riley 1984): $\begin{array} { r } { \frac { \partial ^ { 2 } v ( d , t ) } { \partial t ^ { 2 } } \leq 0 } \end{array}$ for all d.

P5. Nonincreasing absolute risk aversion (Maskin and Riley 1984): $\begin{array} { r } { \frac { \partial } { \partial t } \Big ( - \frac { \partial v ( d , t ) } { \partial d } / v ( d , t ) \Big ) \leq 0 . } \end{array}$

Finally, we assume that for every record purchased, the buyer incurs a (publicly known) targeting $\mathrm { c o s t } ^ { 2 }$ of $c \geq 0$ per record. The cumulative utility to a buyer of type $( { \overline { { \mathbf { x } } } } , t )$ from purchasing a set of records<sup>3</sup> $\mathcal { S } \subseteq \mathbf { \dot { \mathcal { D } } }$ can then be written as:

$$
V (\mathcal {S}; \overline {{\mathbf {x}}}, t) = \int_ {\mathcal {S}} \left(v (\rho (\overline {{\mathbf {x}}}, \mathbf {x}), t) - c\right) ^ {+} g (\mathbf {x}) d \mathbf {x}.\tag{1}
$$

For tractability, we make the following assumptions on a buyer’s cumulative utility $V ( S ; \overline { { \mathbf { x } } } , t )$ :

A1. For any Lebesgue-measurable set ${ \mathcal { S } } \subseteq { \mathcal { D } } ,$ , the function $V ( S ; \overline { { \mathbf { x } } } , t )$ is differentiable and absolutely continuous in t.

A2. There exists a positive and <sup>fi</sup>nite constant $\Lambda ,$ such that:

$$
| V (\mathcal {D}; \overline {{\mathbf {x}}}, t) - V (\mathcal {D}; \overline {{\mathbf {x}}}, t ^ {\prime}) | \leq \Lambda | (t - t ^ {\prime}) | \quad \forall t, t ^ {\prime} \in [ 0, \tau ], \overline {{\mathbf {x}}} \in \chi .
$$

Table 2 summarizes our main notation.

We are now ready to formulate the mechanism design problem for the seller.

## 4. Problem Formulation

Using the revelation principle (Myerson 1981), we restrict our attention, without loss of generality, to the class of direct mechanisms that are incentive compatible and individually rational for the buyer; that is, mechanisms in which (i) it is optimal for the buyer to reveal the buyer’s location and decay type truthfully to the seller, and (ii) the buyer obtains a nonnegative payoff upon participating.

A direct mechanism $\mu$ is characterized by a pair of functions $( { \mathcal { M } } ^ { \mu } , { \mathcal { P } } ^ { \mu } )$ , where $\mathcal { M } ^ { \mu } : \chi \times [ 0 , \tau ] \stackrel { \cdot } {  } \hat { \mathcal { D } }$ is an allocation function and $\mathcal { P } ^ { \mu } : \chi \times \lbrack 0 , \tau \rbrack \to \mathbb { R }$ is a payment function. Thus, in a direct mechanism $\mu ,$ if the buyers reveals the buyer’s type as $\textstyle ( { \overline { { \mathbf { y } } } } , s )$ , then the buyer receives the set of records $\mathcal { M } ^ { \mu } ( \overline { { \mathbf { y } } } , s ) \subseteq \mathcal { D }$ from the data set, where $\mathcal { M } ^ { \mu } ( \overline { { { \bf y } } } , s )$ is assumed to be a Lebesguemeasurable set, and pays an amount ${ \mathcal { P } } ^ { \mu } ( { \overline { { \mathbf { y } } } } , s )$ to the seller (corresponding to the set of records $\mathcal { M } ^ { \mu } ( \overline { { { \mathbf { y } } } } , s ) )$ For the buyer of type $( { \overline { { \mathbf { x } } } } , t )$ , the utility the buyer obtains from purchasing the set of records by reporting the buyer’s type as $\textstyle ( { \overline { { \mathbf { y } } } } , s )$ is:

Table 2. Our Main Notation

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $\mathcal{D}$ </td><td>The focal data set that the seller wishes to sell to the buyer</td></tr><tr><td>N</td><td>Number of columns in the data set  $\mathcal{D}$ </td></tr><tr><td> $\chi \in \mathbb{R}^{N}$ </td><td>The record space</td></tr><tr><td> $\overline{\mathbf{x}} \in \chi$ </td><td>Ideal record of the buyer (private information)</td></tr><tr><td> $t \in [0, \tau]$ </td><td>Decay rate parameter (private information)</td></tr><tr><td> $\rho$ </td><td>The distance metric used to measure the distance between any two records in the data set</td></tr><tr><td> $v(d, t)$ </td><td>The utility to the buyer of decay type  $t$  from a record that is at distance  $d$  from the buyer&#x27;s ideal record</td></tr><tr><td> $V(\mathcal{S};\overline{\mathbf{x}},t)$ </td><td>The net utility to the buyer of type  $(\overline{\mathbf{x}},t)$  from consuming a set  $\mathcal{S} \subseteq \mathcal{D}$  of records</td></tr></table>

$$
V (\mathcal {M} ^ {\mu} (\overline {{\mathbf {y}}}, s); \overline {{\mathbf {x}}}, t) = \int_ {\mathcal {M} ^ {\mu} (\overline {{\mathbf {y}}}, s)} \big (v \big (\rho (\overline {{\mathbf {x}}}, \mathbf {x}), t \big) - c \big) ^ {+} g (\mathbf {x}) d \mathbf {x}.\tag{2}
$$

As is common in the mechanism design literature, we assume that the buyer has a quasi-linear utility function. Thus, the net utility to the buyer of type $( { \overline { { \mathbf { x } } } } , t )$ when the buyer reports the buyer’s type as $\textstyle ( { \overline { { \mathbf { y } } } } , s )$ is given by $V ( \mathcal { M } ^ { \mu } ( \overline { { \mathbf { y } } } , s ) ; \overline { { \mathbf { x } } } , t ) - \mathcal { P } ^ { \mu } ( \overline { { \mathbf { y } } } , s )$ . The incentive-compatibility constraints can now be stated as follows:

$$
\begin{array}{r l} & V (\mathcal {M} ^ {\mu} (\overline {{\mathbf {x}}}, t); \overline {{\mathbf {x}}}, t) - \mathcal {P} ^ {\mu} (\overline {{\mathbf {x}}}, t) \geq V (\mathcal {M} ^ {\mu} (\overline {{\mathbf {y}}}, s); \overline {{\mathbf {x}}}, t) \\ & \quad - \mathcal {P} ^ {\mu} (\overline {{\mathbf {y}}}, s) \forall (\overline {{\mathbf {x}}}, t), (\overline {{\mathbf {y}}}, s) \in \chi \times [ 0, \tau ]. \end{array}\tag{IC-MD}
$$

The (IC-MD) constraints (where MD signi<sup>fi</sup>es multidimensional) state that, under the mechanism $\mu ,$ it is optimal for the buyer to reveal the buyer’s type truthfully. The individual rationality constraints can be stated as follows:

$$
V (\mathcal {M} ^ {\mu} (\overline {{\mathbf {x}}}, t); \overline {{\mathbf {x}}}, t) - \mathcal {P} ^ {\mu} (\overline {{\mathbf {x}}}, t) \geq 0 \forall (\overline {{\mathbf {x}}}, t) \in \chi \times [ 0, \tau ].\tag{IR-MD}
$$

The (IR-MD) constraints impose that the buyer receives a nonnegative payoff in the Bayesian Nash Equilibrium upon truthfully revealing the buyer’s type. The mechanism design problem for the seller can now be formulated as:

$$
\begin{array}{l} \max _ {\mu} \mathbb {E} _ {(\overline {{\mathbf {x}}}, t)} \big [ \mathcal {P} ^ {\mu} (\overline {{\mathbf {x}}}, t) \big ] \\ \text {s.t. (IC - MD), (IR - MD).} \end{array}\tag{\((\mathrm{P}^{\mathrm{MD}})\}
$$

Notice that $( \mathrm { P ^ { M D } } )$ is an N 1 -dimensional mechanism design problem. It is well-known that the analysis of such a problem in full generality is intractable (see, e.g., Daskalakis et al. 2014). In view of this dif<sup>fi</sup>- culty, our structural analysis will proceed as follows:

We will start by de<sup>fi</sup>ning a relaxation of problem $( \mathrm { P } ^ { \mathrm { M D } } )$ . This relaxation is obtained by assuming that the location type, x, of the buyer is public knowledge and only the decay type, t, is private to the buyer. This assumption results in a single-dimensional mechanism design problem, of which we will obtain an optimal solution (Theorem 1, Section 5).

Then, in Section 5.1, we will consider the special case in which the records in the data set are uniformly distributed over the record space. More precisely, for an arbitrary buyer with location type $\overline { { \mathbf { x } } } \ ( \mathrm { i . e . , }$ the buyer’s ideal record is x), the mass of data that is within a distance $R \left( \geq 0 \right)$ from x is independent of x for all values of R. For this special case, we establish a useful result: the characterization of the optimal mechanism is independent of the location type and depends only on the decay type of the buyer (Theorem 2). This then enables the important conclusion that an optimal mechanism for problem $( \mathrm { P ^ { M D } } )$ can be implemented as a price-quantity schedule (Corollary 2).

Next, in Section 6, we study the case when the uniformity assumption mentioned previously does not hold. In Section 6.1, we observe that, in this case, an optimal solution to problem $( \mathrm { P ^ { M D } } )$ may not necessarily belong to the class of price-quantity schedules. Thus, a natural question arises: Does an optimal price-quantity schedule provide a near-optimal solution to problem $( \mathrm { P ^ { M D } } ) ?$ In Section 6.2, we answer this in the af<sup>fi</sup>rmative by establishing Theorem 3, which proves an attractive performance guarantee offered by an optimal pricequantity schedule. This performance guarantee is a proper generalization of Theorem $^ { 2 , }$ in the sense that, when the uniformity assumption is satis<sup>fi</sup>ed, Theorem 3 reduces to Theorem 2.

Although Theorem 3 establishes a theoretical guarantee on the performance of the optimal price-quantity schedule, we show that its actual performance relative to an optimal mechanism (evaluated numerically) is even better! To this end, we analyze a discrete setting in which the private information of the buyer is de<sup>fi</sup>ned by discrete distributions. The advantage of discretization is that the optimal mechanism design problem can now be formulated as a linear program; we do this in Section 6.3. The solution to this linear program allows us to numerically evaluate the performance of pricing policies of our interest; that is, price-quantity schedules. We analyze two commonly used pricequantity schedules, two-part tariffs and two-block tariffs, and demonstrate their attractive performance (Section E of the online appendix).

With this overview, we now proceed with our analysis.

## 5. A Relaxation of Problem $( \mathsf { P } ^ { \mathsf { M D } } )$

Consider the problem obtained by assuming that the location type, x, of the buyer is public knowledge (i.e., it is known to the data seller) and only the buyer’s decay type, $t ,$ is private. Thus, the seller’s mechanism design problem is now single dimensional. A direct mechanism σ x for the relaxed problem<sup>4</sup> consists of the following:

An (Lebesgue-integrable) allocation function, $\begin{array} { r } { \mathcal { M } ^ { \sigma } : [ 0 , \tau ]  \mathcal { D } , } \end{array}$ , that maps the decay type revealed by the buyer to a set of records in the data set D. Since the location type x is publicly known here (and hence is a parameter), we will use the notation $\mathcal { M } ^ { \sigma } ( \cdot ; \overline { { \mathbf { x } } } )$ to denote the allocation function.

A payment function, $\mathcal { P } ^ { \sigma } : [ 0 , \tau ]  \mathbb { R }$ , that speci<sup>fi</sup>es the payment to be made by the buyer corresponding to the set of records allocated to the buyer. Consistent with the notation for the allocation function, we will denote the payment function by $\mathcal { P } ^ { \sigma } ( \cdot ; \overline { { \mathbf { x } } } )$

For the buyer with location type ${ \overline { { \mathbf { x } } } } ,$ the incentive compatibility and the individual rationality constraints under the mechanism σ are:

$$
\begin{array}{r l} & V (\mathcal {M} ^ {\sigma} (t; \overline {{\mathbf {x}}}); \overline {{\mathbf {x}}}, t) - \mathcal {P} ^ {\sigma} (t; \overline {{\mathbf {x}}}) \geq V (\mathcal {M} ^ {\sigma} (s; \overline {{\mathbf {x}}}); \overline {{\mathbf {x}}}, t) \\ & \quad - \mathcal {P} ^ {\sigma} (s; \overline {{\mathbf {x}}}), \forall s, t \in [ 0, \tau ], \end{array}\tag{IC-SD(x)}
$$

$$
V (\mathcal {M} ^ {\sigma} (t; \overline {{\mathbf {x}}}); \overline {{\mathbf {x}}}, t) - \mathcal {P} ^ {\sigma} (t; \overline {{\mathbf {x}}}) \geq 0 \forall t \in [ 0, \tau ],\tag{IR-SD(x)}
$$

and the optimal mechanism design problem for the seller is:

$$
\begin{array}{c} \max _ {\sigma} \mathbb {E} _ {t} \left[ \mathcal {P} ^ {\sigma} (t; \overline {{\mathbf {x}}}) \right] \\ \text { subject   to } (\mathrm{IC-SD} (\overline {{\mathbf {x}}})), (\mathrm{IR-SD} (\overline {{\mathbf {x}}})). \end{array} \tag {$P^{\mathrm{SD}}(\overline{\mathbf{x}})$}
$$

Unlike a standard single-dimensional mechanism design problem in which the seller allocates a single object, our allocation function $\mathcal { M } ^ { \sigma }$ needs to allocate a set of records from the data set to the buyer. Therefore, to apply the steps of the Myersonian approach (Myerson 1981) for solving problem $( \mathrm { P } ^ { \mathrm { S D } } ( \dot { \bar { \mathbf { x } } } ) )$ 1 (SD is short for single dimensional), we need several additional results; see claims 1–5 in Section A of the online appendix, which presents the complete derivation of the optimal solution to problem $( \mathrm { P } ^ { \mathrm { S D } } ( \bar { \mathbf { x } } ) )$ ). Here, we outline the key steps involved in deriving the optimal solution:

Payment in terms of allocation: Using the constraints (IC-SD x¯ ) and (IR-SD x¯ ) along with the envelope theorem (Milgrom and Segal 2002, corollary 1), we obtain the following relationship between the payment and allocation functions of a mechanism:

$$
\mathcal {P} ^ {\sigma} (t; \overline {{\mathbf {x}}}) = V (\mathcal {M} ^ {\sigma} (t; \overline {{\mathbf {x}}}); \overline {{\mathbf {x}}}, t) - \int_ {0} ^ {t} V _ {t} (\mathcal {M} ^ {\sigma} (s; \overline {{\mathbf {x}}}); \overline {{\mathbf {x}}}, s) d s,\tag{3}
$$

where

$$
V _ {t} (\mathcal {S}; \overline {{\mathbf {x}}}, t) := \frac {\partial V (\mathcal {S} ; \overline {{\mathbf {x}}} , t)}{\partial t}.
$$

Problem simpli<sup>fi</sup>cation: The relationship between the allocation and the payment function in (3) enables us to formulate the (point-wise) revenue-maximization problem $( \mathrm { P } ^ { \mathrm { S D } } ( \bar { \mathrm { x } } ) )$ of the data seller solely in terms of the allocation function:

$$
\begin{array}{l} \max _ {\mathcal {M} ^ {\sigma} (t; \overline {{\mathbf {x}}}) \subseteq \{\mathbf {x} \in \mathcal {D}: v (\rho (\overline {{\mathbf {x}}}, \mathbf {x}), t) - c \geq 0 \}} \\ \int_ {\mathcal {M} ^ {\sigma} (t; \overline {{\mathbf {x}}})} \bigg (v (\rho (\overline {{\mathbf {x}}}, \mathbf {x}), t) - c - \frac {\partial v (\rho (\overline {{\mathbf {x}}} , \mathbf {x}) , t)}{\partial t} \Big (\frac {1 - H (t)}{h (t)} \Big) \bigg) g (\mathbf {x}) d \mathbf {x} \\ \text {s.t.} \big (\mathrm{IC-SD} (\overline {{\mathbf {x}}}) \big), \big (\mathrm{IR-SD} (\overline {{\mathbf {x}}}) \big). \end{array}
$$

Optimizing over sets: Notice that the previous formulation is a set-optimization problem: For every decay type t that the buyer reveals, an optimal mechanism σ allocates a set of records, $\begin{array} { r } { \mathcal { M } ^ { \sigma } ( t ; \overline { { \mathbf { x } } } ) . } \end{array}$ , to the buyer in a way that maximizes the data seller’s expected revenue. Let

$$
w (d, t) := v (d, t) - c - \frac {\partial v (d , t)}{\partial t} \bigg (\frac {1 - H (t)}{h (t)} \bigg).\tag{4}
$$

The function $w ( \cdot , \cdot )$ can be viewed as the buyer’s virtual value function, a well-known concept in the mechanism design literature. The integrand of the objective function can then be written as $w ( \rho ( \overline { { \mathbf { x } } } , \mathbf { x } ) , t ) g ( \mathbf { x } )$ and the revenue-maximization problem of the data seller becomes

$$
\begin{array}{r l} & {\underset {\mathcal {M} ^ {\sigma} (t; \overline {{\mathbf {x}}}) \subseteq \{\mathbf {x} \in \mathcal {D}: v (\rho (\overline {{\mathbf {x}}}, \mathbf {x}), t) - c \geq 0 \}} {\max} \int_ {\mathcal {M} ^ {\sigma} (t; \overline {{\mathbf {x}}})} w (\rho (\overline {{\mathbf {x}}}, \mathbf {x}), t) g (\mathbf {x}) d \mathbf {x}} \\ & {\quad \mathrm{s.t.} \big (\mathrm{IC-SD} (\overline {{\mathbf {x}}})), \big (\mathrm{IR-SD} (\overline {{\mathbf {x}}}) \big).} \end{array}
$$

De<sup>fi</sup>ne $r : [ 0 , \tau ] \to \mathbb { R } _ { + }$ as:

$$
r (t) = \left\{ \begin{array}{l l} \max \{d: w (d, t) \geq 0 \} & \text { if } \exists d \text { s.t. } w (d, t) \geq 0 \\ 0 & \text { otherwise. } \end{array} \right.
$$

The following result states the solution to previous optimization problem.

Theorem 1. For a given location type ${ \overline { { \mathbf { x } } } } ,$ the mechanism OPT-SD defined by

$$
\mathcal {M} ^ {\mathrm{OPT-SD}} (t; \overline {{\mathbf {x}}}) = \bigl \{\mathbf {x} \in \mathcal {D}: \rho (\overline {{\mathbf {x}}}, \mathbf {x}) \leq r (t) \bigr \},\tag{5}
$$

$$
\begin{array}{l} \mathcal {P} ^ {\mathrm{OPT-SD}} (t; \overline {{\mathbf {x}}}) = V (\mathcal {M} ^ {\mathrm{OPT-SD}} (t; \overline {{\mathbf {x}}}); \overline {{\mathbf {x}}}, t) \\ - \int_ {0} ^ {t} V _ {t} (\mathcal {M} ^ {\mathrm{OPT-SD}} (s; \overline {{\mathbf {x}}}); \overline {{\mathbf {x}}}, s) d s, \end{array}\tag{6}
$$

is an optimal solution to problem $( \mathrm { P } ^ { \mathrm { S D } } ( \bar { \mathbf { x } } ) )$

In other words, Theorem 1 states that for a buyer of type x, t , it is optimal to allocate the buyer all the records in the data set that are within a distance $r ( t )$ from the buyer’s ideal record x and charge a price that is equal to the bene<sup>fi</sup>t that the buyer enjoys from those records less the information rent.<sup>5</sup>

Recall that the density of the records in the data set is given by g x . Thus, if the data buyer purchases a set of records, say $s ,$ from the data set, then the quantity of records purchased by that buyer is simply $\textstyle \int _ { \mathcal { S } } g ( \mathbf { x } ) d \mathbf { x }$ . Under the OPT-SD mechanism de<sup>fi</sup>ned earlier, the quantity of records, which we denote by $\mathcal { Q } ^ { \mathrm { O P T - S D } }$ $( t ; \overline { { \mathbf { x } } } )$ , purchased by a buyer of type $( { \overline { { \mathbf { x } } } } , t )$ is given by $\begin{array} { r l } { \int _ { \mathcal { M } } \mathrm { o p r } \mathbf { - } \mathrm { s D } _ { ( t ; \overline { { \mathbf { x } } } ) } g ( \mathbf { x } ) d \mathbf { x } } \end{array}$ . This correspondence between the allocation set $\mathcal { M } ^ { \mathrm { O P T - S D } }$ and the quantity of records $\mathcal { Q } ^ { \mathrm { O P T - S D } }$ enables us to characterize the opt-sd mechanism by the pair of functions $( \mathcal { Q } ^ { \mathrm { O P T - S D } } , \mathcal { P } ^ { \mathrm { O P T - S D } } )$ .

Note that buyers with different decay types could purchase the same quantity of data; that is, for a given quantity q and location type ${ \overline { { \mathbf { x } } } } ,$ there may exist two (or more) decay types, say $t _ { 1 } , t _ { 2 } ; t _ { 1 } \ne t _ { 2 } ,$ such that $\mathcal { Q } ^ { \mathrm { O P T - S D } } ( t _ { 1 } ; \overline { { \mathbf { x } } } ) = \dot { \mathcal { Q } } ^ { \mathrm { O P T - S D } } ( t _ { 2 } ; \overline { { \mathbf { x } } } )$ Let $\Gamma ^ { \mathrm { S D } } ( q ; \overline { { \mathbf { x } } } ) : = \{ t :$ $\mathcal { Q } ^ { \mathrm { O P T - S D } } ( t ; \overline { { \mathbf { x } } } ) = q \}$ denote the set of decay types of the buyers with location type x who consume a quantity q under the OPT-SD mechanism. If $\Gamma ^ { \mathrm { S D } } ( q ; \overline { { \mathbf { x } } } ) \neq \boldsymbol { \cal { O } }$ , then let $t ^ { \mathrm { S D } } ( q ; { \overline { { \mathbf { x } } } } ) : = \operatorname* { s u p } \{ t : t \in \Gamma ^ { \mathrm { S D } } ( q ; { \overline { { \mathbf { x } } } } ) \}$ . To generate a pricequantity schedule, let us set the price for any buyer with location type x and decay type in $\Gamma ^ { \mathrm { S D } } ( q ; \overline { { \mathbf { x } } } )$ (thus, the buyer buys quantity $q$ under the OPT-SD mechanism) to the price for the buyer with location type x and decay type $t ^ { \mathrm { S D } } ( q ; \overline { { \mathbf { x } } } )$ . Then, it follows immediately that, presented with the price-quantity schedule de-<sup>fi</sup>ned in (7), each buyer will self-select the quantity that the buyer is allocated under the OPT-SD mechanism.

Corollary 1. For a given location type x, the OPT-SD mechanism can be implemented as a price-quantity schedule:

$$
\mathcal {P} ^ {\mathrm{SD-PQ}} (q; \overline {{\mathbf {x}}}) = \left\{ \begin{array}{l l} \mathcal {P} ^ {\mathrm{OPT-SD}} (t ^ {\mathrm{SD}} (q; \overline {{\mathbf {x}}}); \overline {{\mathbf {x}}}) & \text {if} \Gamma^ {\mathrm{SD}} (q; \overline {{\mathbf {x}}}) \neq \varnothing \\ \infty & \text {otherwise.} \end{array} \right.\tag{7}
$$

Note that under the OPT-SD mechanism, the set of records allocated to the buyer, $\mathcal { M } ^ { \mathrm { O P T - S D } } ( t ; \overline { { \mathbf { x } } } )$ , and consequently the quantity of records, $\mathcal { Q } ^ { \mathrm { O P T - S D } } ( t ; \overline { { \mathbf { x } } } )$ , depends on both the location type x and the decay type t of the buyer. Accordingly, Corollary 1 speci<sup>fi</sup>es the pricequantity schedule $\check { \mathcal { P } } ^ { \mathrm { S D - P Q } }$ for a given location type x.

We now examine the previous analysis under a special case where the data set D is uniform (de<sup>fi</sup>ned precisely next). In this case, we show that (i) the pricequantity schedule becomes independent of the location type x, and (ii) the relaxation $( \mathrm { P } ^ { \mathrm { S D } } ( \bar { \mathbf { x } } ) )$ can be used to derive an optimal solution for our original problem, namely $( \mathrm { P } ^ { \mathrm { M D } } )$ . Together, these two results enable us to obtain an optimal solution to $( \mathrm { P ^ { \mathrm { M D } } } )$ that can be conveniently implemented as a price-quantity schedule (which is independent of the location type).

## 5.1. Analysis of Uniform Data Sets

Let $\bar { R } ( \tau ) : = \operatorname* { m a x } \{ d : v ( d , \tau ) - c \geq 0 \}$ . Recall that $\begin{array} { r } { \frac { \partial v ( d , t ) } { \partial d } \leq 0 } \end{array}$ (property P2) and $\begin{array} { r } { \frac { \partial v ( d , t ) } { \partial t } \geq 0 } \end{array}$ (property P3). Thus, for any buyer of type $t \in [ 0 , \tau ]$ , the maximum distance from the buyer’s ideal record that the buyer traverses to select the desired records $\bar { R } ( \tau )$

Definition (<sup>Uniform Data Set</sup>). A data set D is said to be uniform if the density of records, $g ( \mathbf { x } )$ , is such that for any two ideal records ${ \overline { { \mathbf { x } } } } , { \overline { { \mathbf { y } } } } \in \chi ,$ the following property holds: For all $R , 0 \leq R \leq \bar { R } ( \tau )$ , we have

$$
\int_ {\left\{\mathbf {x} \in \mathcal {D}: \rho (\overline {{\mathbf {x}}}, \mathbf {x}) \leq R \right\}} g (\mathbf {x}) d \mathbf {x} = \int_ {\left\{\mathbf {x} \in \mathcal {D}: \rho (\overline {{\mathbf {y}}}, \mathbf {x}) \leq R \right\}} g (\mathbf {x}) d \mathbf {x}.\tag{8}
$$

In other words, in a uniform data set, for any two buyers with types $( { \overline { { \mathbf { x } } } } , t )$ and $( \overline { { \mathbf { y } } } , t ) ,$ , and for any value of $R \leq \bar { R } ( \tau )$ the quantity of data that lies within a distance of R from their respective ideal records is equal. We will refer to a data set that is not uniform as a nonuniform data set.

Example 1. Table $^ { 3 , }$ panel a shows a data set that consists of six records and two columns. Table $^ { 3 , }$ panel b shows a numerical representation of the data set obtained by mapping the categorical values in each of the three columns to real numbers. There are only two potential buyers interested in purchasing this data set: A and B. The ideal record for buyer A is “Female–High,” that is, record 3 in the data set. Similarly, the ideal record for buyer B is “Male–Unemployed,” that is, record 4 in the data set. The distance between any two records in the data set is measured using the Manhattan metric (rectilinear distance or the $l ^ { 1 }$ norm). For example, the distance between record 2 (0–2) and record $ { 4 } \_ { \mathrm { ~ \normalfont ~ \left( 1 - 0 \right) ~ } }$ is $| 0 - 1 | + | 2 - 0 | = 3$ . The utility function $v ( \cdot , \cdot )$ is de<sup>fi</sup>ned as $v ( d , t ) = t \cdot ( 4 - d )$ and the targeting cost, $c ,$ is set to 0.5. Observe that $v ( \cdot , \cdot )$ satis<sup>fi</sup>es properties P1–P5 stated in Section 3. Let $\tau = 2 ;$ thus, the decay type of both the buyers can take values in 0, 2 . Note that (i) $\bar { R } ( \bar { \tau } ) = 3 . 7 5 < 4 ,$ , and (ii) the distance between any two records in our data set is an integer. Thus, to show that the uniformity condition (equality (8)) is satis<sup>fi</sup>ed for all distances $R \leq 3 . 7 5 ,$ it suf<sup>fi</sup>ces to check that an equal number of records lies within integer value distances of $0 , ~ 1 , ~ 2$ , and 3 from the respective ideal records of A and B. Table 4 veri<sup>fi</sup>es this condition.

Proposition 1 shows that the OPT-SD mechanism exhibits a special structure when D is a uniform data set.

Table 3. Illustrative Example of a Uniform Data Set

<table><tr><td>Record ID</td><td>Gender</td><td>Income</td></tr><tr><td colspan="3">Panel A: A uniform data set</td></tr><tr><td>1</td><td>Female</td><td>Unemployed</td></tr><tr><td>2</td><td>Female</td><td>Middle</td></tr><tr><td>3</td><td>Female</td><td>High</td></tr><tr><td>4</td><td>Male</td><td>Unemployed</td></tr><tr><td>5</td><td>Male</td><td>Low</td></tr><tr><td>6</td><td>Male</td><td>High</td></tr><tr><td colspan="3">Panel B: Numerical representation of the data set</td></tr><tr><td>1</td><td>0</td><td>0</td></tr><tr><td>2</td><td>0</td><td>2</td></tr><tr><td>3</td><td>0</td><td>3</td></tr><tr><td>4</td><td>1</td><td>0</td></tr><tr><td>5</td><td>1</td><td>1</td></tr><tr><td>6</td><td>1</td><td>3</td></tr></table>

Proposition 1. $I f D$ is a uniform data set, then the quantity of data purchased by a data buyer of type <sub>(</sub>x, t<sub>)</sub>, and the corresponding price that the buyer pays, under the OPT-SD mechanism is independent of the buyer’s location type x. Mathematically, $i f { \mathcal { D } }$ is a uniform data set, then for all t $[ 0 , \tau ]$ and ${ \overline { { \mathbf { x } } } } , { \overline { { \mathbf { y } } } } \in \chi ,$

$$
\begin{array}{r l} & {\mathcal {Q} ^ {\mathrm{OPT-SD}} (t; \overline {{\mathbf {x}}}) = \mathcal {Q} ^ {\mathrm{OPT-SD}} (t; \overline {{\mathbf {y}}}), a n d} \\ & {\mathcal {P} ^ {\mathrm{OPT-SD}} (t; \overline {{\mathbf {x}}}) = \mathcal {P} ^ {\mathrm{OPT-SD}} (t; \overline {{\mathbf {y}}}).} \end{array}
$$

This simpli<sup>fi</sup>cation in the structure of the OPT-SD mechanism helps us obtain an optimal solution for the multidimensional mechanism design problem $( \mathrm { P } ^ { \mathrm { M D } } )$ . The following result states the solution.

Theorem 2. If D is a uniform data set, then the mechanism OPT-MD defined by

$$
\mathcal {M} ^ {\mathrm{OPT-MD}} (\overline {{\mathbf {x}}}, t) = \bigl \{\mathbf {x} \in \mathcal {D}: \rho (\overline {{\mathbf {x}}}, \mathbf {x}) \leq r (t) \bigr \}, a n d\tag{9}
$$

$$
\begin{array}{r l} & {\mathcal {P} ^ {\mathrm{OPT-MD}} (\overline {{\mathbf {x}}}, t) = V (\mathcal {M} ^ {\mathrm{OPT-MD}} (\overline {{\mathbf {x}}}, t); \overline {{\mathbf {x}}}, t)} \\ & {- \int_ {0} ^ {t} V _ {t} (\mathcal {M} ^ {\mathrm{OPT-MD}} (\overline {{\mathbf {x}}}, s); \overline {{\mathbf {x}}}, s) d s} \end{array}\tag{10}
$$

is an optimal solution to problem $( \mathrm { P ^ { M D } } )$ . Moreover, for all $t \in [ 0 , \tau ]$ and ${ \overline { { \mathbf { x } } } } , { \overline { { \mathbf { y } } } } \in \chi$

$$
\mathcal {Q} ^ {\mathrm{OPT-MD}} (\overline {{\mathbf {x}}}, t) = \mathcal {Q} ^ {\mathrm{OPT-MD}} (\overline {{\mathbf {y}}}, t), a n d\tag{11}
$$

$$
\mathcal {P} ^ {\mathrm{OPT-MD}} (\overline {{\mathbf {x}}}, t) = \mathcal {P} ^ {\mathrm{OPT-MD}} (\overline {{\mathbf {y}}}, t),\tag{12}
$$

where $\begin{array} { r } { \mathcal { Q } ^ { \mathrm { O P T - M D } } ( \overline { { \mathbf { x } } } , t ) = \int _ { \mathcal { M } } \mathrm { O P T - M D } _ { ( \overline { { \mathbf { x } } } , t ) } g ( \mathbf { x } ) d \mathbf { x } . } \end{array}$

Theorem 2 states when D is a uniform data ${ \mathrm { s e t } } ,$ a buyer of decay type t purchases the set of records that are within a distance $r ( t )$ from the buyer’s ideal record. Furthermore, the quantity of records purchased by the buyer and the corresponding price are both independent of the buyer’s location type. Thus, $\forall \mathbf { x } \in \boldsymbol { \chi } ,$ , we have

$$
\begin{array}{l} \mathcal {Q} ^ {\mathrm{OPT-MD}} (t) := \mathcal {Q} ^ {\mathrm{OPT-MD}} (\overline {{\mathbf {x}}}, t), \text {and} \\ \mathcal {P} ^ {\mathrm{OPT-MD}} (t) := \mathcal {P} ^ {\mathrm{OPT-MD}} (\overline {{\mathbf {x}}}, t). \end{array}
$$

Let $\Gamma ^ { \mathrm { M D } } ( q ) : = \{ t : \mathcal { Q } ^ { \mathrm { O P T - M D } } ( t ) = q \}$ denote the set of decay types of the buyers who consume a quantity q under the OPT-MD mechanism. If $\Gamma ^ { \mathrm { M D } } ( q ) \neq \emptyset ,$ , then let $t ^ { \mathrm { M D } } ( q ) : = \operatorname* { s u p } \big \{ t : t \in \Gamma ^ { \mathrm { M D } } ( q ) \big \}$

Corollary 2. If D is a uniform data set, then the optimal mechanism OPT-MD can be implemented as the following price-quantity schedule:

$$
\mathcal {P} ^ {\mathrm{MD-PQ}} (q) = \left\{ \begin{array}{l l} \mathcal {P} ^ {\mathrm{OPT-MD}} (t ^ {\mathrm{MD}} (q)) & \text {if} \Gamma^ {\mathrm{MD}} (q) \neq \emptyset \\ \infty & \text {otherwise.} \end{array} \right.\tag{13}
$$

We will now turn our attention to the analysis of nonuniform data sets; that is, data sets for which condition (8) is not satis<sup>fi</sup>ed. The optimality of pricequantity schedules for uniform data sets raises several natural questions: First, are price-quantity schedules optimal for nonuniform data sets as well? Second, if not, then what performance guarantee does an optimal price-quantity schedule offer for such data sets? We examine these questions in the next section.

## 6. Analysis for Nonuniform Data Sets

We start this section by demonstrating that, for a nonuniform data set, no optimal mechanism to problem $( \mathrm { P ^ { M D } } )$ may belong to the class of price-quantity schedules; that is, each price-quantity schedule may be suboptimal. Nevertheless, Theorem 3 establishes the usefulness of price-quantity schedules for nonuniform data sets by establishing an attractive performance guarantee offered by an optimal price-quantity schedule. This result is a natural generalization of Theorem 2 in the sense that, for a uniform data set, Theorem 3 reduces to Theorem 2.

## 6.1. Suboptimality of Price-Quantity Schedules for Nonuniform Data Sets

For a nonuniform data set D, the following simple but illustrative example demonstrates that an optimal price-quantity schedule is suboptimal for problem $\mathsf { \bar { ( P ^ { M D } ) } }$ ).

Example 2. As shown in Figure 2, the records in the data set are located at four positions, A, B, C, and D, on the real number line. Recall from Section 3 that the number of records is normalized to 1. The mass of records at location A is 0.4 and at each of locations $\mathrm { \mathrm { B } } , \mathrm { C } ,$ and D, is 0.2. The distance between any two records is the Euclidean distance between the positions of those records on the number line. Thus, $\rho ( \mathrm { A } , \mathrm { C } ) =$ $2 , \rho ( { \mathrm { A } } , { \mathrm { D } } ) = 3 , \rho ( { \mathrm { B } } , { \mathrm { C } } ) = 1 , \rho ( { \mathrm { A } } , A ) = 0 .$ , and so on. The distributional information that the data seller possesses about the location type (i.e., the ideal record) of the data buyer is as follows: The ideal record of the data buyer is located at position A with probability 0.5 and at position C with probability 0.5. The decay type of the data buyer is publicly known and is deterministically equal to 1. The utility function $v ( \cdot , \cdot )$ is de<sup>fi</sup>ned as $\overset { \cdot } { v } ( \overset { \cdot } { d , t } ) = t \cdot ( 2 - \overset { \cdot } { d } ) ^ { + } = \overset { \cdot } { ( 2 - \overset { \cdot } { d } ) ^ { + } }$ Observe that $v ( \cdot , \cdot )$ satis<sup>fi</sup>es properties P1–P5 stated in Section 3. Thus, a buyer whose ideal record is located at A receives a utility of 2 (per unit record) from purchasing records located at $\scriptstyle \mathrm { A , }$ 1 from purchasing records located at B, and 0 from records located at C and D. This fall in the utility that the data buyer derives from purchasing records that are located farther from the buyer’s ideal record is depicted by the (red) solid line in Figure 2. Similarly, a buyer whose ideal record is located at C receives a utility of 2 from purchasing records located at C, 1 from purchasing records located at B and D each, and 0 from records located at A (depicted by the (blue) dotted line in Figure 2). The targeting cost c is equal to 0.

Table 4. Veri<sup>fi</sup>cation of Uniformity Condition

<table><tr><td>Distance (R)</td><td>Number of records that lie within a distance (R) from the ideal record of A</td><td>Number of records that lie within a distance (R) from the ideal record of B</td></tr><tr><td>0</td><td>1 (record 3)</td><td>1 (record 4)</td></tr><tr><td>1</td><td>3 (records 2, 3, 6)</td><td>3 (records 1, 4, 5)</td></tr><tr><td>2</td><td>3 (records 2, 3, 6)</td><td>3 (records 1, 4, 5)</td></tr><tr><td>3</td><td>5 (records 1, 2, 3, 5, 6)</td><td>5 (records 1, 2, 4, 5, 6)</td></tr></table>

Figure 2. (Color online) Illustrative Example  
![](/api/attachments/CVTDX6BR/fulltext/images/d8a29723365c999c13e0e2cf20c23eeee2cea17d859944e00c27ed8d01a304b4.jpg)

Consider a buyer whose ideal record is located at A. This buyer’s valuation for the records located at positions C and D is 0. Thus, the total mass of records for which this buyer has a positive valuation is 0.4 (mass of the records located at $\mathrm { A } ) + 0 . 2$ (mass of the records located at $\mathrm { B } ) ~ = ~ 0 . 6$ . Thus, corresponding to a total quantity of 0.6 records, this buyer would be willing to pay $\dot { 0 } . 4 \times 2 + 0 . 2 \times 1 = 1$ . Similarly, consider a buyer whose ideal record is located at C. This buyer’s valuation for records located at position A is 0. The total mass of records for which this buyer has a positive valuation is 0.2 (mass of the records located at $\mathrm { C } ) \ + \ 0 . 2$ (mass of the records located at $\mathrm { B } ) \ + \ 0 . 2$ (mass of the records located at $\mathrm { D } ) = 0 . 6$ . Thus, corresponding to a total quantity of 0.6 records, this buyer would be willing to pay $0 . { \dot { 2 } } \times 2 + 0 . 2 \times 1 + 0 . 2 \times { \dot { 1 } } =$ 0.8. In summary, both the buyers are willing to purchase the same quantity of data (albeit, different sets of records) but have different willingness to pay for that same quantity. Therefore, a price-quantity schedule (which speci<sup>fi</sup>es one price for a given quantity of data) cannot fully exploit the heterogeneity in the valuations of the buyers for the same quantity of data.

Consider, instead, the following pricing policy: The data seller offers two bundles of records: (i) records at positions A and B are bundled together and offered for a price of 1, and (ii) records at positions $\mathrm { \mathrm { B } } , \mathrm { C } ,$ and D are bundled together and offered for a price of 0.8. Under this pricing policy, buyers whose ideal record is at position A purchase the <sup>fi</sup>rst bundle for a price of 1 and the buyers whose ideal record is at position C purchase the second bundle for a price of 0.8. This pricing policy yields a strictly higher revenue than any price-quantity schedule.

## 6.2. Performance of Price-Quantity Schedules for Nonuniform Data Sets

Although the previous example shows that an optimal price-quantity schedule is not, in general, optimal for $( \mathrm { P ^ { M D } } )$ , can it be provably near optimal? We answer this question in the af<sup>fi</sup>rmative by establishing a worstcase bound on the performance of an optimal pricequantity schedule. Before proceeding, we state a few simplifying assumptions and introduce additional notation needed for our analysis.

Assumption 1. For every data buyer of type x, t , there exists a record x such that $v ( \rho ( { \overline { { \mathbf { x } } } } , \mathbf { x } ) , t ) - c \leq 0$

This assumption implies that not all the records in the data set are useful (i.e., generate a positive utility) to the buyer. For instance, for any given buyer, a typical realworld data set will contain records that are not of any interest to that buyer. We make this technical assumption solely to simplify the boundary value of the virtual value function, $w ( \cdot , \cdot )$ , under the OPT-SD mechanism; more precisely, under this assumption, $w ( r ( t ) , t ) = 0 \ \forall \ t$

Recall from Section 5 that $\Gamma ^ { \mathrm { S D } } ( q ; \overline { { \mathbf { x } } } )$ denotes the set of decay types of the buyers with location type x who consume a quantity q under the OPT-SD mechanism. Further, recall that if $\Gamma ^ { \mathrm { S D } } ( q ; \overline { { \mathbf { x } } } ) \neq \boldsymbol { \ O }$ , then $t ^ { \mathrm { S D } } ( q ; { \overline { { \mathbf { x } } } } ) = \operatorname* { s u p } \big \{ t : t \in \Gamma ^ { \mathrm { S D } } ( q ; { \overline { { \mathbf { x } } } } ) \big \}$ . Let

$$
\epsilon_ {t} := \sup _ {q, \overline {{\mathbf {x}}}, \overline {{\mathbf {y}}}} \big | t ^ {\mathrm{SD}} (q; \overline {{\mathbf {x}}}) - t ^ {\mathrm{SD}} (q; \overline {{\mathbf {y}}}) \big |.\tag{14}
$$

Let $\delta ( q ; { \overline { { \mathbf { x } } } } )$ denote the minimum distance that a buyer, whose ideal record is located at x, traverses to accumulate a quantity q of records in the data set. Formally,

$$
\delta (q; \overline {{\mathbf {x}}}) = \min d, \quad \text { subject   to } \quad \int_ {\left\{\mathbf {x} \in \mathcal {D}: \rho (\overline {{\mathbf {x}}}, \mathbf {x}) \leq d \right\}} g (\mathbf {x}) d \mathbf {x} = q.
$$

For $\delta ( q ; { \overline { { \mathbf { x } } } } )$ , we assume the following.

Assumption 2. There exists a finite constant $\epsilon _ { \delta }$ such that

$$
\max _ {0 \leq q \leq 1} \bigl | \delta (q; \overline {{\mathbf {x}}}) - \delta (q; \overline {{\mathbf {y}}})) \bigr | \leq \epsilon_ {\delta} \forall \overline {{\mathbf {x}}}, \overline {{\mathbf {y}}} \in \boldsymbol {\chi}.\tag{15}
$$

In other words, this assumption imposes that for any two buyers who differ in their location type, the maximum difference in the distances these buyers traverse from their respective ideal records to consume the same quantity of records is bounded. For instance, a well-designed data set of healthcare professionals in a metropolitan area will typically include records that are evenly spread out over that area and is therefore likely to have a small value of $\epsilon _ { \delta }$

The constants $\epsilon _ { \delta }$ and $\epsilon _ { t }$ capture the extent of nonuniformity in the data set. Note here that, for uniform data sets, we have $\epsilon _ { \delta } = \epsilon _ { t } = 0$

For a given distance d and decay type $t ,$ let

$$
L (d, t) := \frac {\partial v (d , t)}{\partial t} \cdot \frac {1 - H (t)}{h (t)}.\tag{16}
$$

We assume the following for the function $L ( d , t )$

Assumption 3. There exist finite constants $M _ { \delta } , M _ { t } \geq 0$ such that

$$
\left| \frac {\partial L (d , t)}{\partial d} \right| \leq M _ {\delta} \forall t, \text { and }\tag{17}
$$

$$
\left| \frac {\partial L (d , t)}{\partial t} \right| \leq M _ {t} \forall d.\tag{18}
$$

The function $L ( d , t )$ can be explained as follows. Recall from (4) that the virtual value, w(d, t), of a buyer of decay type t for a record(s) located at a distance d from the buyer’s ideal record, is the valuation, $v ( d , t ) - c$ minus the term $\textstyle { \frac { \partial v ( d , t ) } { \partial t } } \cdot { \frac { 1 - H ( t ) } { h ( t ) } }$ . This latter term is denoted by $L ( d , t )$ in (16). The expectation of $L ( d , t )$ with respect to the decay type t is the information rent to the buyer under the OPT-SD mechanism. Assumption 3 states that the rate of change of the function $L ( d , t )$ with respect to its arguments is bounded. Clearly, this assumption holds for well-behaved functions whose values change smoothly.

Let us now formally de<sup>fi</sup>ne the optimal revenue that the data seller can obtain from making a take-itor-leave-it offer for purchasing the entire data set. Using the notation de<sup>fi</sup>ned in Section 4, the bene<sup>fi</sup>t from consuming the entire data set D for a buyer of type $( { \overline { { \mathbf { x } } } } , t )$ is $V ( \overline { { \mathcal { D } } } ; \overline { { \mathbf { x } } } , t )$ . Let $F ^ { \mathcal { D } }$ denote the distribution of $V ( \mathcal { D } ; \overline { { \mathbf { x } } } , t )$ and let p denote the price at which the seller decides to sell the data set D. Let $\mathrm { R E V } ^ { \mathrm { O P T - F U L L } }$ denote the optimal revenue to the data seller obtained by selling the entire data set. That is,

$$
\mathrm{REV} ^ {\mathrm{OPT-FULL}} = \max _ {p} p (1 - F ^ {\mathcal {D}} (p)).\tag{19}
$$

Let $\mathbb { R E V } ^ { \mathrm { O P T - P Q } }$ denote the revenue of the data seller from using an optimal price-quantity schedule. Since a take-it-or-leave-it pricing policy belongs to the class of price-quantity schedules, it follows that $\begin{array} { r } { \mathrm { R E V } ^ { \mathrm { \tiny { \delta P T - P Q } } } \ge \mathrm { \tiny ~ R E V } ^ { \mathrm { \tiny { O P T - F U L L } } } } \end{array}$ . Finally, let $\mathrm { R E V } ^ { \mathrm { O P T } }$ denote the revenue of the seller under an optimal mechanism $( \mathrm { i . e . , }$ an optimal solution to our original mechanism design problem $( \mathrm { P ^ { M D } } ) )$ . Recall that $\epsilon _ { t }$ and $\epsilon _ { \delta }$ are as de<sup>fi</sup>ned in (14) and (15), respectively.

Theorem 3. For any data set ${ \mathcal { D } } ,$ the worst-case performance guarantee offered by an optimal price-quantity schedule, relative to an optimal mechanism, is:

$$
\frac {\mathrm{REV} ^ {\mathrm{OPT}}}{\mathrm{REV} ^ {\mathrm{OPT-PQ}}} \leq 1 + \frac {\epsilon_ {\delta} M _ {\delta} + \epsilon_ {t} M _ {t}}{\mathrm{REV} ^ {\mathrm{OPT-FULL}}}.\tag{20}
$$

Theorem 3 provides us a way to assess the performance of an optimal price-quantity schedule (relative to an optimal mechanism, over all mechanisms) based on the extent of nonuniformity in the data set. To see this, note that, when D is a uniform data set, we have $\epsilon _ { \delta } = \epsilon _ { t } = 0 ,$ , and consequently $\mathrm { R E V } ^ { \mathrm { O P T } } = \mathrm { R E V } ^ { \mathrm { O P T - P Q } } ,$ which is the result we had established earlier in Theorem 2 (Corollary 2). The second term in the performance guarantee depends on the extent of nonuniformity in the data set, as measured by the constants $\epsilon _ { \delta }$ and $\epsilon _ { t }$ .

We now present a brief overview of the nontrivial steps involved in the proof of Theorem 3. Recall from Corollary 1 (Section 5) that the OPT-SD mechanism can be implemented as a price-quantity schedule, $\mathcal { P } ^ { \mathrm { S D - P Q } } ( q ; \overline { { \boldsymbol { x } } } )$ , that is contingent on the location type of the buyer. Put differently, when the location type, ${ \overline { { \mathbf { x } } } } ,$ of a buyer is known, offering the buyer a type-speci<sup>fi</sup>c price-quantity schedule, $\mathcal { P } ^ { \mathrm { S D - P Q } } ( q ; \overline { { \mathbf { x } } } )$ , is an optimal mechanism. Using the price-quantity schedules for each ${ \overline { { \mathbf { x } } } } ,$ we construct a price-quantity schedule, $\mathcal { P } ^ { \mathrm { B O U N D } } ( q )$ , in which, for any quantity $q ,$ the rate of change of price with respect to q is the lowest such rate, over all location types ${ \overline { { \mathbf { x } } } } ,$ of the schedules $\mathcal { P } ^ { \mathrm { S D - P Q } } ( q ; \overline { { \mathbf { x } } } )$ . The schedule $\mathcal { P } ^ { \mathrm { B O U N D } } ( q )$ possesses two interesting properties: (i) it does not depend on the location type of the buyers, and (ii) the quantity of records that a buyer of type x, t purchases under the schedule $\mathcal { P } ^ { \mathrm { B O U N D } } ( q )$ is at least as much as that under the schedule $\mathcal { P } ^ { \mathrm { S D - } \mathrm { P Q } } ( q ; \overline { { \mathbf { x } } } )$ . These two properties, along with Assumptions 1, 2, and 3, help us obtain a bound on the ratio of the revenue $\mathrm { R E V } ^ { \mathrm { O P T } }$ from the optimal mechanism to that of the revenue $\mathrm { R E V } ^ { \mathrm { B O U N D } }$ from the schedule $\mathcal { P } ^ { \mathrm { B O U N D } } ( q )$ . However, computing the revenue $\mathrm { R E V ^ { B O U N D } }$ from the schedule $\mathcal { P } ^ { \mathrm { B O U N D } } ( q )$ is analytically as well as computationally dif<sup>fi</sup>cult. On the other hand, computing the revenue ${ \mathrm { R E V } } ^ { \mathrm { O P T - F U L L } }$ of the optimal take-it-or-leave-it policy is relatively easy. Therefore, using the fact that the revenue ${ \mathrm { R E V } } ^ { \mathrm { { O P T - } \check { P Q } } }$ from the optimal price-quantity schedule is greater than or equal to max REV<sup>BOUND</sup>, REV<sup>OPT-FULL</sup> , we obtain the performance guarantee in Theorem 3.

Next, using an example, we illustrate the strength of the worst-case bound in Theorem 3.

Example 3. The records in the data set are located on the circumference of a unit circle, symmetrically across the diameter $\operatorname { A B } ;$ see Figure 3. The density (mass) of records at an angle θ from OB, $\theta \in \left[ - \pi , \pi \right]$ , is $\begin{array} { r } { \frac { 1 } { 2 \pi } + \alpha - \frac { 2 \alpha | \theta | } { \pi } , } \end{array}$ , where $\alpha \in [ 0 , { \textstyle \frac { 1 } { 2 \pi } } ]$ is a parameter. The parameter α captures the extent of nonuniformity of the distribution of records in the data set: for $\alpha = 0 ,$ the records are uniformly distributed over the circle $( \mathrm { i . e . , }$ Equation (8) is satis<sup>fi</sup>ed); as α increases, a larger mass of records is concentrated at point B relative to that at point A. The distance between any two records is the length of the shorter of the two arcs along the circle that joins their locations. The utility function $v ( \cdot , \cdot )$ is de<sup>fi</sup>ned as $v ( d , t ) : = t \cdot ( \pi - d )$ . Observe that this utility function satis<sup>fi</sup>es properties P1–P5 stated in Section 3. The value of the per-record targeting cost, $c ,$ takes values from the set 0:05, 0:1, 0:2 . The location type of the buyers is uniformly distributed over the circumference of the circle and the decay type of the buyers is uniformly distributed in 0, 1 . For this setting, we evaluate the bound in Theorem 3 for different values of α in its range $[ 0 , { \textstyle \frac { 1 } { 2 \pi } } ] ;$ see Figure 4.

Figure 3. Records in the Data Set Represented on a Unit Circle  
![](/api/attachments/CVTDX6BR/fulltext/images/2e805afd913807b034c11db3561f907da4d5475d354b91738c357d752533b30c.jpg)

For $\alpha = 0 ,$ , the records in the data set are uniformly distributed and the value of the bound is 1; that is, an optimal price-quantity schedule is an optimal mechanism. As the value of $\alpha$ increases, the distribution of the records in the data set becomes increasingly nonuniform. It is worth noting that even for the highest possible value of $\alpha ,$ the value of the worst-case bound is below 2. We also note that for a <sup>fi</sup>xed value of $\alpha ,$ the bound increases with an increase in the targeting cost, c. Speci<sup>fi</sup>cally, as c increases, while the values $\epsilon _ { \delta } , M _ { \delta } , \epsilon _ { t } ,$ and $M _ { t } ,$ remain unaffected, the revenue ${ \mathrm { R E V } } ^ { \mathrm { { \dot { O P T } } - \mathrm { \ddot { F U L L } } } }$ from selling the entire data set decreases (since the willingness to pay of the buyer decreases). Thus, the worst-case bound in Theorem 3 increases.

Figure 4. (Color online) Value of the Worst-Case Performance Guarantee (Right Side of (20) in Theorem 3) with Respect to the Extent of Nonuniformity in the Data Set  
![](/api/attachments/CVTDX6BR/fulltext/images/efcc8dbd6fa722776ddb08ed2ef3e160912dd3520949b4a023e87c93f1050f61.jpg)

Although we now have a theoretical (worst-case) assessment of the performance of an optimal pricequantity schedule, a better evaluation of the actual performance of price-quantity schedules can be obtained via a numerical study. To this end, we develop an approach to compute an optimal mechanism for nonuniform data sets and then use this as a benchmark to examine two popular price-quantity schedules, namely two-part tariffs and two-block tariffs.

## 6.3. Optimal Mechanism for Nonuniform Data Sets

We start with the key elements of our setting:

Distribution of records: We assume that the record space $\boldsymbol { \chi }$ (see Section 3) is discretized; speci<sup>fi</sup>cally, $\chi =$ $\left\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { M } \right\}$ for some $M < \infty$ . Each record in the data set $\mathcal { D }$ takes a value from $\chi .$ As before, we refer to the value $\mathbf { x } _ { i } \ ( \mathrm { s a y } )$ of a record as its location. Further, as we had done before for convenience, we normalize the number of records in $\mathcal { D }$ to 1. Let $g _ { i }$ denote the mass of records at location $\mathbf { x } _ { i } ,$ and $\textstyle \sum _ { i = 1 } ^ { M } g _ { i } = 1$ . Using this notation, the set of records that are feasible for a buyer to purchase can be written as:

$$
\mathcal {Y} = \{(y _ {1}, y _ {2}, \dots , y _ {M}): y _ {i} \leq g _ {i} \forall i \in \{1, 2, \dots , M \} \},
$$

where $y _ { i }$ denotes the mass of record $\mathbf { x } _ { i } , i \in \{ 1 , 2 , \dots , M \}$ purchased by the buyer.

Private information: The location type of the data buyer $( \mathrm { i . e . , }$ the data buyer’s ideal record) $\overline { { \mathbf { x } } } \in \{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots \mathbf { \mu } \mathbf { \cdot } \mathbf { \sigma } \mathbf { \cdot } \mathbf { x } _ { M } \}$ . The seller has distributional knowledge of the buyer’s location type: Let f denote the probability mass function of the buyer’s location type over $\{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots { } . . . \mathbf { x } _ { M } \} ; f _ { i }$ denotes the probability that the location type of the buyer is $\mathbf { x } _ { i } , i \in \{ 1 , 2 , \dots , M \}$ . Similar to the record space, we assume that the space of the decay types $[ 0 , \tau ]$ of the buyer is also discretized and takes $T ( < \infty )$ distinct values $\{ t _ { 1 } , t _ { 2 } , \ldots , t _ { T } \}$ . The seller has distributional knowledge of the buyer’s decay type: Let h denote the probability mass function of the decay type over the set $\{ t _ { 1 } , t _ { 2 } , \ldots , t _ { T } \} ; h _ { j }$ denotes the probability that the decay type of the buyer is $t _ { j } , j \in \{ 1 , \bar { 2 } , \dots , T \}$

The cumulative utility to the buyer of type $( \mathbf { x } _ { i } , t _ { j } ) , i \in$ $\{ 1 , 2 , \ldots , M \}$ and $j \in \left\{ 1 , 2 , \dots , T \right\}$ , from consuming the set of records Y is

$$
\sum_ {k = 1} ^ {M} (v (\rho (\mathbf {x} _ {i}, \mathbf {x} _ {k}), t _ {j}) - c) ^ {+} y _ {k}.\tag{21}
$$

For easy exposition, we de<sup>fi</sup>ne $v _ { i k , j } : = v ( \rho ( \mathbf { x } _ { i } , \mathbf { x } _ { k } ) , t _ { j } )$ A direct mechanism for our discretized record and type space consists of:

An allocation rule $\pmb { \mathcal { M } } : \{ \pmb { x } _ { 1 } , \pmb { x } _ { 2 } , . . . \pmb { x } _ { M } \} \times \{ t _ { 1 } , t _ { 2 } ,$ $\dots , t _ { T } \} \to \mathcal { V }$ that maps the type of the data buyer to the set of feasible records that the buyer can purchase, and

A payment rule $\mathcal { P } : \{ \mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \dotsc \mathbf { x } _ { M } \} \times$ $\{ t _ { 1 } , t _ { 2 } , \dots , t _ { T } \}  \mathbb { R }$ that speci<sup>fi</sup>es the amount that the buyer pays to the seller for purchasing the set of records speci<sup>fi</sup>ed by .

The allocation rule $\mathcal { M } ( \mathbf { x } _ { i } , t _ { j } )$ is a vector $\pmb { \mathscr { M } } _ { i j } : = ( \mathscr { M } _ { i j 1 } , \mathscr { M } _ { i j 1 } , \dots , \mathscr { M } _ { i j M } ) ,$ , where the component $\mathcal { M } _ { i j k }$ is the mass of the record $\mathbf { x } _ { k }$ allocated to the buyer of type $( \mathbf { x } _ { i } , t _ { j } )$ . The payment $\mathcal { P } ( \mathbf { x } _ { i } , t _ { j } )$ is a scalar that can be succinctly denoted by $\mathcal { P } _ { i j } .$ The revenue-maximization problem for the data seller can now be formulated as the following linear program:

$$
\max _ {\mathcal {M} _ {i j}, \mathcal {P} _ {i j}} \sum_ {i = 1} ^ {M} \sum_ {j = 1} ^ {T} f _ {i} h _ {j} \mathcal {P} _ {i j}   \text {   subject   to:   }\tag{P \( ^{MD-LP} \)}
$$

$$
\sum_ {k = 1} ^ {M} (v _ {i k, j} - c) ^ {+} \mathcal {M} _ {i j k} - \mathcal {P} _ {i j} \geq \sum_ {k = 1} ^ {M} (v _ {i k, j} - c) ^ {+} \mathcal {M} _ {r s k} - \mathcal {P} _ {r s}
$$

$$
\forall i, j, r, s,\tag{IC-LP}
$$

$$
\sum_ {k = 1} ^ {M} (v _ {i k, j} - c) ^ {+} \mathcal {M} _ {i j k} - \mathcal {P} _ {i j} \geq 0 \forall i, j,\tag{IR-LP}
$$

$$
0 \leq \mathcal {M} _ {i j k} \leq g _ {k} \forall i, j, k,
$$

$$
\mathcal {P} _ {i j} \geq 0 \forall i, j.\tag{22}
$$

(23)

In this formulation, the objective function represents the expected revenue to the data seller. Equations (IC-LP) and (IR-LP) are the incentive compatibility and the individual rationality constraints, respectively, for the data buyer. The constraints in (22) represent feasible allocations to the buyer. Finally, (23) states that the buyer pays a nonnegative amount to the seller. The linear program $( \mathrm { P ^ { M D - L P } } )$ consists of $\mathcal { O } ( M ^ { 2 } T )$ decision variables and $\mathcal { O } ( M ^ { 2 } T ^ { 2 } )$ constraints.

Next, to highlight the effectiveness of price-quantity schedules even for nonuniform data sets, we examine the performance of two widely used price-quantity schedules: namely, two-part tariffs and two-block tariffs. We explain these two schemes next.

## 6.4. Popular Price-Quantity Schedules: Two-Part Tariffs and Two-Block Tariffs

A two-part tariff is characterized by two parameters, $\left( p _ { f } , p _ { u } \right)$ , where $p _ { f }$ denotes the <sup>fi</sup>xed price and $p _ { u }$ denotes the per-record price. Precisely, in our context, the price that the data buyer pays for purchasing a quantity $q$ of records, denoted by $\check { \mathrm { P } } ^ { \mathrm { T P } } ( q )$ , is:

$$
\mathrm{P} ^ {\mathrm{TP}} (q) = \left\{ \begin{array}{l l} 0 & \mathrm{if} q = 0, \\ p _ {f} + p _ {u} \cdot q & \mathrm{if} q > 0. \end{array} \right.
$$

A two-block tariff is characterized by three parameters, $( \lambda , p _ { \lambda } , p )$ . If $\lambda ~ = ~ 0 ,$ , then the two-block tariff reduces to a two-part tariff with <sup>fi</sup>xed price $p _ { \lambda }$ and per-record price $p .$ If $\lambda > 0$ , then the buyer pays a perrecord price of $\frac { p _ { \lambda } } { \lambda }$ for purchasing the <sup>fi</sup>rst λ quantity of records and a per-record price of $p$ for purchasing the records in excess of $\lambda .$ Thus, the price that a buyer pays for purchasing a quantity of $q$ records, denoted by $\mathsf { \Pi } ^ { \mathsf { P } ^ { \mathrm { T B } } } ( q )$ , is:

$$
\mathrm{P} ^ {\mathrm{TB}} (q) = \left\{ \begin{array}{l l} 0 & \text {if q = 0 ,} \\ p _ {\lambda} + p \cdot q & \text {if \lambda = 0 ,} \\ \frac {p _ {\lambda}}{\lambda} \cdot q & \text {if \lambda > 0 and q\leq\lambda ,} \\ p _ {\lambda} + p \cdot (q - \lambda) & \text {if \lambda > 0 and q\geq\lambda .} \end{array} \right.
$$

Next, we summarize the results of our numerical evaluation of (i) the performance of the optimal twopart tariff and the optimal two-block tariff developed earlier, relative to the optimal mechanism, and (ii) the value to the data seller for providing the option of <sup>fi</sup>ltering the data set to the buyers. The details of the analysis are in Section E of the online appendix.

Over a comprehensive test bed of instances, we show that on average, the revenue of both the twopart tariff and the two-block tariff is within 10% of the optimal revenue. We observe that the two-block tariff outperforms the two-part tariff since the former is a proper generalization of the latter. To assess the attractiveness of the two-block tariff over the two-part tariff, we consider three different classes of values of the targeting cost: low, intermediate, and high. The main takeaway of this analysis is that the attractiveness of an optimal two-block tariff over an optimal two-part tariff is accentuated for intermediate values of the targeting cost (as opposed to extreme values). For such values, there is more heterogeneity across buyers in the fraction of records that offers them a positive utility. An optimal two-block tariff better discriminates the heterogeneity in buyers’ willingness to pay by charging a steep price per record for lowquantity buyers and offering a discount for highquantity buyers.

The provision of the <sup>fi</sup>ltering option (by the data seller) enables buyers to endogenously select subsets of records that are of interest to them. In the absence of the <sup>fi</sup>ltering option, the buyers face a take-it-orleave-it offer from the seller; that is, they either have to purchase the entire data set at the stated price or buy nothing. We observe that as the targeting cost increases, the value to the seller from offering the <sup>fi</sup>ltering option increases. Note that with an increase in the targeting cost, the utility of each record to the buyer decreases, and, therefore, so does the fraction of records in the data set that yields positive utility to the buyer. This, coupled with the high heterogeneity in buyers’ valuations for the entire data set, makes a take-it-or-leave-it offer less attractive to the buyer and thereby increases the seller’s value from offering the <sup>fi</sup>ltering option.

Remark 1 (<sup>Multiple Ideal Records</sup>). Our analysis thus far assumed that the data buyers are endowed with a single ideal record. It is plausible that, in general, buyers may possess multiple ideal records. In this remark, we explain how our analysis can be extended for the case of multiple ideal records.

Recall from Section 3 that the metric $\rho : \mathbb { R } ^ { N } \times \mathbb { R } ^ { N } $ $\mathbb { R } ^ { + }$ is used to evaluate the utility of a record in the data set to a buyer (by measuring the distance between that record and the ideal record of the buyer). To account for the setting when buyers possess multiple ideal records, we generalize the notion of a metric as follows. For a nonempty set $\mathcal { T } \subseteq \chi$ in the record space and a record x in the data set D, de<sup>fi</sup>ne the function Ω as:

$$
\Omega (\mathcal {I}, \mathbf {x}) := \inf \bigl \{\rho (\overline {{\mathbf {x}}} _ {i}, \mathbf {x}) | \overline {{\mathbf {x}}} _ {i} \in \mathcal {I} \bigr \}.\tag{24}
$$

This generalization equips us to model the setting where buyers possess multiple ideal records. We now describe the key changes in our model primitives.

Let $\mathcal { T } _ { K } = \{ \overline { { \mathbf { x } } } _ { 1 } , \overline { { \mathbf { x } } } _ { 2 } , \hdots , \overline { { \mathbf { x } } } _ { K } \} \subseteq \chi , K \geq 1 _ { \ L }$ , denote the set of ideal records of a buyer and let t denote the buyer’s decay type. Thus, the buyer has private information in two aspects—namely, the set of ideal records $\mathcal { T } _ { K } \subseteq \chi$ and the decay type, $t \in [ 0 , \tau ]$ —and is characterized by the tuple $( \mathcal { T } _ { K } , t )$ . For a buyer of type $( \mathcal { T } _ { K } , t )$ , the utility obtained from purchasing a record $\mathbf { x } \in \mathcal { D }$ is now given by $v ( \Omega ( \mathcal { T } _ { K } , \pmb { x } ) , t )$ , and the utility from consuming a set of records S is given by:

$$
V (\mathcal {S}; \mathcal {I} _ {K}, t) = \int_ {\mathcal {S}} (v (\Omega (\mathcal {I} _ {K}, \mathbf {x}), t) - c) ^ {+} g (\mathbf {x}) d \mathbf {x}.\tag{25}
$$

We note a few important points here:

Recall that the utility to a buyer of decay type t from purchasing a record located at a distance d from the buyer’s ideal record was given by v(d, t). In the setting where buyers possess multiple ideal records, the utility function is still given by $v ( d , t )$ . The only difference in this new setting is that the distance d is measured by the function $\Omega ,$ whereas in the earlier setting where the buyers possessed a single ideal record, the distance was measured by the metric $\rho .$ Note that the only way in which the metric $\rho$ enters our analysis thus far is through the utility function $v ( d , t )$ , where d is the distance (as measured by the metric $\rho )$ between the (single) ideal record of the buyer and a given record.

The properties P1–P5 are related to the structure of the function $v ( d , t )$ and do not depend on the metric ρ that is used to measure d. Therefore, these assumptions remain unchanged if the distance d is measured using the function Ω.

Assumptions A1 and A2 can be restated as follows: A1. For any Lebesgue-measurable set ${ \mathcal { S } } \subseteq { \mathcal { D } } $ , the function $V ( \mathcal { S } ; \mathcal { T } _ { K } , t )$ is differentiable and absolutely continuous in t.

A2. There exists a positive and <sup>fi</sup>nite constant Λ, such that:

$$
| V (\mathcal {D}; \mathcal {I} _ {K}, t) - V (\mathcal {D}; \mathcal {I} _ {K}, t ^ {\prime}) | \leq \Lambda | (t - t ^ {\prime}) | \forall t, t ^ {\prime} \in [ 0, \tau ], \mathcal {I} _ {K} \subseteq \chi .
$$

With these changes in the model primitives, all our results thus far continue to hold for multiple ideal records (with appropriate modi<sup>fi</sup>cations in the notation).

## 7. Concluding Remarks

The business of monetizing data has grown signi<sup>fi</sup>cantly over the past decade and has created unprecedented opportunities for <sup>fi</sup>rms to market their products, advance their predictive abilities, and target customers with surgical precision. The growth in this business is primarily fuelled by the intelligence that data-driven analytics provides in making critical business decisions. Thus, the economics of data monetization has become a subject of signi<sup>fi</sup>cant practical and theoretical importance. In this study, we addressed two fundamental aspects related to data monetization: (i) the development of a utility framework that is appropriate, parsimonious, and tractable, and (ii) the analysis of optimal and near-optimal pricing mechanisms.

Our study focused on a monopolistic data seller who is interested in monetizing a data set. The ongoing explosive growth in the supply and demand of data has led to the emergence of data-selling platforms. Firms such as Data & Sons, Dawex, and Lotame cater to both sides of the market: sellers list their data sets on the platform and buyers purchase data from one or more sellers. Here, the pricing of the data can be done by the seller or by the platform on behalf of the seller. Other <sup>fi</sup>rms such as BIG and Narrative enable auction-based purchase and sale of data— buyers browse data sets from different sellers and bid their valuations, and sellers manage their transactions by selecting buyers of their choice. Such two-sided settings become richer due to several interesting constraints. On the supply side, some sellers may want to sell their data only as a monolithic unit (i.e., avoid sale of proper subsets of records) and some may want to restrict sale to a limited number of buyers. On the demand side, buyers may want exclusive access to data or may have budget and/or minimum-volume constraints. Further, from a mechanism design perspective, the analysis of two-sided data-selling platforms presents interesting theoretical challenges. For instance, different from the setting we analyzed in this study, one may face a context wherein buyers’ valuation of a data set depends on the number of other buyers who have also purchased that data set. In this case, the private information of a buyer is a function that is endogenous to the number of buyers who have shared access to the data set. We believe that our work can serve as a foundation for future work on optimal and/or approximate mechanisms for such settings and, more generally, on the design of ef<sup>fi</sup>cient data-selling platforms.

## Endnotes

<sup>1</sup> The values of categorical attributes such as State, Provider\_Type, Is\_Ambulance can be easily mapped to real numbers.

<sup>2</sup> Our underlying assumption is that the buyer’s intended use of the purchased records is to execute targeted marketing campaigns to the individuals/organizations identified in those records. For instance, such a campaign might involve reaching out to these individuals via fliers, phone calls, or emails. The parameter c is intended to capture this targeting cost per record. We note that the choice c 0 is allowed in our analysis.

<sup>3</sup> We assume that the set of records, S, that a buyer can purchase is Lebesgue-measurable. From a practical viewpoint, this is an innocuous assumption that we impose to make the marginal utility function v , Lebesgue-integrable.

<sup>4</sup> To avoid cumbersome notation, we will henceforth avoid stating the dependence of the mechanism on x explicitly and simply use σ instead of σ x .

<sup>5</sup> In the mechanism design literature, the surplus accrued to an agent by virtue of the fact that the agent is the only one in the system who knows the individual’s own private valuation (of the object under consideration) is referred to as information rent (see e.g., Krishna 2009).

## References

Agarwal A, Dahleh M, Sarkar T (2019) A marketplace for data: An algorithmic solution. Proc. 2019 ACM Conf. Econom. Comput. (Association for Computing Machinery, New York), 701–726.

ANA (2018) The continued rise of the in-house agency. (October 15), https://www.ana.net/miccontent/show/id/rr-2018-in -house-agency.

Bakos Y, Brynjolfsson E (1999) Bundling information goods: Pricing, pro<sup>fi</sup>ts, and ef<sup>fi</sup>ciency. Management Sci. 45(12):1613–1630.

Bergemann D, Bonatti A, Smolin A (2018) The design and price of information. Amer. Econom. Rev. 108(1):1–48.

Bhargava HK, Csapo G, M´ uller R (2020) On optimal auctions for¨ mixing exclusive and shared matching in platforms. Management Sci. –

Bimpikis K, Crapis D, Tahbaz-Salehi A (2019) Information sale and competition. Management Sci. 65(6):2646–2664.

Cai Y, Daskalakis C, Weinberg SM (2011) On optimal multidimensional mechanism design. ACM SIGecom Exchanges 10(2):29–33.

Cai H, Ye F, Yang Y, Zhu Y, Li J (2019) Toward privacy-preserving data trading for web browsing history. Chen Y, ed. 2019 IEEE/

ACM 27th Internat. Symp. Quality Service (IWQoS) (Association for Computing Machinery, New York), 1–10.

Chawla S, Hartline JD, Kleinberg R (2007) Algorithmic pricing via virtual valuations. MacKie-Mason J, ed. Proc. 8th ACM Conf. Electronic Commerce (Association for Computing Machinery, New York), 243–251.

Chawla S, Hartline JD, Malec DL, Sivan B (2010) Multi-parameter mechanism design and sequential posted pricing. Proc. 42nd ACM Symp. Theory Comput. (Association for Computing Machinery, New York), 311–320.

Chen Y-J, Huang K-W (2016) Pricing data services: Pricing by minutes, by gigs, or by megabytes per second? Inform. Systems Res. 27(3):596–617.

Choudhary V (2010) Use of pricing schemes for differentiating information goods. Inform. Systems Res. 21(1):78–92.

Daskalakis C, Deckelbaum A, Tzamos C (2014) The complexity of optimal mechanism design. Chekuri C, ed. Proc. 25th Annual ACM-SIAM Symp. Discrete Algorithms (Society for Industrial and Applied Mathematics, Philadelphia), 1302–1318.

Gar<sup>fi</sup>nkel R, Gopal RD, Nunez M, Rice DO (2006) Secure electronic markets for private information. IEEE Trans. Systems Man Cybernetics A Systems Humans 36(3):461–471.

Geng X, Stinchcombe MB, Whinston AB (2005) Bundling information goods of decreasing value. Management Sci. 51(4):662–667.

Krishna, V (2009) Auction Theory (Academic Press, Cambridge, MA).

Kushal, A, Moorthy S, Kumar V (2012) Pricing for data markets. Technical report, Washington University.

Lavi R, Swamy C (2011) Truthful and near-optimal mechanism design via linear programming. J. ACM 58(6):1–24.

Lee D, Hosanagar K, Nair HS (2018) Advertising content and consumer engagement on social media: Evidence from Facebook. Management Sci. 64(11):5105–5131.

Li C, Li DY, Miklau G, Suciu D (2014) A theory of pricing private data. ACM Trans. Database Systems 39(4):1–28.

Maskin E, Riley J (1984) Monopoly with incomplete information. RAND J. Econom. 15(2):171–196.

Milgrom P, Segal I (2002) Envelope theorems for arbitrary choice sets. Econometrica 70(2):583–601.

Muschalle A, Stahl F, Loser A, Vossen G (2012) Pricing approaches ¨ for data markets. Castellanos MC, Umeshwar D, Rundensteiner EA, eds. Internat. Workshop Bus. Intelligence Real-Time Enterprise (Springer, Berlin, Heidelberg), 129–144.

Mussa M, Rosen S (1978) Monopoly and product quality. J. Econom. Theory 18(2):301–317.

Myerson RB (1981) Optimal auction design. Math. Oper. Res. 6(1):58–73.

Spence AM (1980) Multi-product quantity-dependent prices and pro<sup>fi</sup>tability constraints. Rev. Econom. Stud. 47(5):821–841.

Sundararajan A (2004) Nonlinear pricing of information goods. Management Sci. 50(12):1660–1673.

Wu JF, Tawarmalani M, Kannan KN (2018) Cardinality bundling with Spence–Mirrlees reservation prices. Management Sci. 65(4):1891–1908.

Wu S, Hitt LM, Chen P, Anandalingam G (2008) Customized bundle pricing for information goods: A nonlinear mixed-integer programming approach. Management Sci. 54(3):608–622.

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
