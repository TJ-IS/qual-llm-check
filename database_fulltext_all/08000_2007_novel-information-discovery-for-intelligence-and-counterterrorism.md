---
otero_id: 8000
otero_key: "B8HCVWS6"
title: "Novel information discovery for intelligence and counterterrorism"
authors: "D.B. Skillicorn; N. Vats"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.04.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Novel information discovery for intelligence and counterterrorism

D.B. Skillicorn <sup>⁎</sup>, N. Vats

School of Computing, Queen's University, Canada

Available online 18 May 2006

## Abstract

Intelligence analysts construct hypotheses from large volumes of data, but are often limited by social and organizational norms and their own preconceptions and biases. The use of exploratory data mining technology can mitigate these limitations by requiring fewer assumptions. We present the design of the ATHENS system, which discovers novel information, relative to a specified set of existing knowledge, in large information repositories such as the World Wide Web. We illustrate the use of the system by starting from the terms “al Qaeda” and “bin Laden”" and running the ATHENS system as if on September 12th, 2001. This provides a picture of what novel information could have been known at the time. This is of some intrinsic interest, but also serves to validate the performance of the system since much of this novel information has been discovered by conventional means in the intervening years.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Intelligence analysis; Counterterrorism; Information discovery; Novelty; Al Qaeda

## 1. Introduction

It is helpful to think of an intelligence analyst as interacting with two different spaces: an information space and a hypothesis space. The information space contains facts of various kinds (‘data’); it is typically extremely large. There are many difficult issues in the design and use of such a space, for example whether its content is controlled by the analyst (a pull model) or from some outside source (a push model); whether there are gatekeepers who control what information can appear within it; and what is the relationship between organizational barriers and separation of information spaces. Good solutions to these problems are necessary to good analysis, but they are in the domain of information retrieval, and we will not consider them further. The critical feature is that the information space is a passive object, providing no guidance about how its contents are to be understood or interpreted. So improvements in information spaces do not necessarily lead to improvements in analysis.

The hypothesis space contains the hypotheses (‘knowledge’) derived from the information space. These hypotheses have a natural quality metric based on (a) the evidence that supports them in the information space, and (b) their explanatory power. A good hypothesis is one for which there is good evidence in the information space, and which has some predictive power (in Popper's terms, is falsifiable [10]). Such hypotheses become the basis for action in the real world. A poor hypothesis is one that is not supported by the data, or one that does not explain much (it is either bad or useless).

The central task of an intelligence analyst is to populate the hypothesis space with high-quality hypotheses.

The standard way to do this is to use the analyst's skills, intuition and hunches to develop hypotheses and then validate them (or not) against the data in the information space. This process is often iterative; an initial hypothesis is partly validated, but the evidence against it suggests an alteration that creates a better hypothesis.

It is clear what the limitations of this process are. Hypotheses that are inconceivable to the analyst are never examined against the knowledge base. In practical terms, possible but unlikely hypotheses are never examined either. The process is fundamentally limited by analyst (and organizational) norms and preconceptions. This seems to be at the heart of what the 9/11 Commission [17] described as a “failure of imagination” in the runup to the September 2001 attacks against the World Trade Center.

One possible enhancement for intelligence analysis is exploratory data mining, a family of techniques that are able to build models from data without prespecified hypotheses. Of course, this approach contains its own preconceptions, both in the choice of model building technique, and in the parameters used to build each model. However, these preconceptions are of a different kind, assumptions about structure in the data, rather than the social and political norms that can often affect a human analyst. Techniques such as social network analysis and link analysis have been used to search for criminal behavior [1,7], for patterns in communication [12,16], and for counterterrorism [3,11]. Techniques such as matrix decompositions [13] have also been used for counterterrorism. Overviews of this approach are the works of Popp et al. [9] and Taipale [15].

The techniques mentioned above assume that the information space is a single dataset that can be processed directly using flat file or database storage. They cannot be directly applied to an information space such as the World Wide Web. The content of the entire World Wide Web is surely no more than a few hundred petabytes (which is well within the range of high-performance data mining systems) but the content is arranged in an awkward and highly distributed way. Techniques are needed that can handle both the pragmatics of size and distribution, and also the fact that almost all of the content of the World Wide Web is irrelevant to most hypotheses.

We present the ATHENS system, which can be used to attack the hypothesis-generation problem using large information repositories such as the web as its information space. Search engine technology is adequate for discovering all of the information about a topic for which reasonable descriptors (keywords) are known. Several search engine enhancements are even capable of organizing the results of a search in useful ways, for example clustering similar pages [5], or ordering so that the most interesting pages (by some metric) are presented first. This already represents a step towards the intelligence analyst's goals. However, the major drawback with the search engine approach is the need for descriptors; a search engine cannot search for something that the analyst does not know about, and so is limited by the analyst's preconceptions in the same way as other directed tools.

The ATHENS system is explicitly designed to find novel information (that is whose existence is not known to the analyst), but novel information contextualized by what the analyst does already know. In other words, ATHENS does not produce random nuggets of new information, but rather enables answers to questions such as: “I know all about topic X; which other topics Y, Z are related to X but are not easily findable knowing only X”.

To use ATHENS, an analyst provides a set of keywords representing knowledge that is already familiar. The system returns clusters of new information that is relevant to the familiar knowledge but too indirectly connected to be easily discovered by browsing from the pages containing the familiar knowledge.

We illustrate the use of ATHENS by showing the results from the initial keywords “bin Laden” and “al Qaeda”, executing the system as if on September 12th, 2001. These results are of considerable intrinsic interest, since they show what knowledge would have been readily accessible had ATHENS been in existence then. These results also allow us to validate the ATHENS system because much of the information related indirectly to the query concepts has been discovered in the intervening years [4,6]. Overall, much useful information that has come to light over the past few years would have been available contemporaneously using ATHENS. Significantly, however, these results support the claim that, at least from public data, the September 11th attacks could not have been predicted.

ATHENS is a general-purpose system for exploring large information repositories. For example, it has been used to understand the structure of different organizations with respect to particular areas of expertise or knowledge [18].

## 2. The ATHENS system

Search engines are designed to find and retrieve the most relevant documents corresponding to a user query. However, this does not suit them well for open-ended, exploratory knowledge discovery. Suppose a user searches using keyword X. The list of retrieved documents will contain references to other topics, some of which may be new to the user. However, the ordering of the search results will tend to spread these references to new topics Yand Z at random through the list, so it is hard for the user to notice them.

Furthermore, if a user does notice topic Y, a search on Y is likely to produce another large list of documents which will mention further new topics. In other words, the occurrence of new information in search results is both random and growing in size.

For example, a Google search for “osama bin laden” returns 582,000 pages. Only 9440 of these pages also mention Hambali, a major link between al Qaeda and South-East Asian Salafist terrorists, the first page ranked at position 121. A new search on “hambali” returns 20,100 pages.

It is apparent that the process of elucidating the important connections within al Qaeda using this approach quickly becomes impractical. The problem is that the World Wide Web, considered as a graph whose edges represent co-occurrence of terms, has high degree. Searching out from a known set of terms or pages reaches a huge number of pages within only a few steps. Furthermore, there are few hints about which ‘directions’ in this graph are likely to be productive.

The ATHENS system provides a focused way to look for novel information in systems such as the web. It begins with a set of terms, representing the user's existing knowledge. This initial information is used to create a representation of the user's background knowledge, from which new, contextualized search queries are constructed. The results of these queries are clustered, both to remove less useful information and to organize what is found. After this phase, the content retrieved by the system is a good representation of what the user knows or could easily discover using standard techniques. The entire process is now repeated, starting from each of the first-level clusters, to retrieve content that is both relevant (because of the contextualized search) and novel (because it goes beyond what can be easily discovered).

The key steps of the ATHENS discovery procedure are:

Closure: This step identifies the central content that the user's list of keywords represents. It is implemented by searching using the keywords, selecting the most relevant pages returned, and extracting a concise description of their content. In the current implementation, this description is a set of nouns ranked by importance. Closure ensures that the starting point for information discovery is not skewed by the user's particular choice of keywords (or from a different perspective, permits users to be casual in their choice of initial keyword lists).

• Probe: This step begins the process of acquiring new information from the foundation of the closure. New queries are generated by combining terms from the original keywords with terms from the closure.

• Cluster: This step organizes the information returned by the probe queries. Pages are clustered using a spectral partitioning technique. Those pages that do not fall into clusters are discarded; each remaining cluster is presented as a unit of novel information, with a set of descriptive words extracted from it.

• Iterate: The iterate step repeats the three steps above, using the cluster descriptors as the starting points for the second iteration.

## 2.1. Algorithm

Given an initial search query Q (a set of keywords), the following operations are applied:

## 1. Closure

Retrieve a subset S of the most relevant web pages for Q using an underlying search engine. In the current implementation, ATHENS uses the Google WebAPI to retrieve search results. This API enables searches to include phrases as well as single words, and to restrict queries to particular domains or time ranges (other search engines and other information repositories can be used by making a few low-level changes in the system).

Create a list of nouns and their frequencies for each page using the MontyTagger, a parts-ofspeech tagger [8]. The nouns from the original query (which must necessarily be present) are removed at this stage (the motivation for using nouns is that, in English, they best capture the content of the page).

Combine the noun lists from all pages into a single list, summing their frequencies. Note that this automatically gives longer pages (those with more content) more influence, which we consider desirable in this context. A stopword list is used to remove common words.

Eliminate the less discriminating nouns by comparing their relative frequency in the combined list to their relative frequency in the BNC corpus [2], a large collection of written and spoken English. Only those nouns whose relative frequency in the retrieved pages is greater than in ordinary English are retained. There are clearly other ways to select a better set of relevant keywords, but the current method has the advantage of being context-independent and so is expected to perform reasonable well in most query domains.

Order the list by descending differential relative frequency (i.e. how much the relative frequency differs from that of the BNC).

## 2. Probe

Form a set, Q, from the original search terms by leaving out one term each time. Form the cartesian product of Q with the list of nouns constructed during the previous step, ordering the product by the order of the list.

Select some prefix of this ordered list and use each set of terms as a search query. Create noun lists from the returned pages as in Step (1).

Create a page–page matrix, P, whose ijth entry represents the similarity between page i and page j. Let $L _ { i }$ and $L _ { j }$ be the noun lists for pages i and j respectively, and $f _ { n _ { i } }$ be the frequency of noun n in page i. Then the Jaccard similarity between pages i and j is

$$
\frac {i \cap j}{i \cup j}
$$

where

$$
i \cap j = \sum_ {\text { nouns }} \min (1, f _ {n _ {1}}, f _ {n _ {2}})
$$

and

$$
i \cup j = | L _ {1} | + | L _ {2} |
$$

## 3. Cluster

• Compute L, the normalized adjacency matrix of P, whose off-diagonal elements are

$$
L _ {i j} = \frac {P _ {i j}}{\sqrt {d _ {i} d _ {j}}}
$$

where di is the degree of page i, the row sum in P. The diagonal elements of L are set to 0. L is a normalized representation of P.

• Perform SVD on L and truncate to k dimensions so that

$$
L \approx U _ {k} S _ {k} V _ {k} ^ {\prime}
$$

where $U _ { k }$ (respectively $S _ { k } , \quad V _ { k } )$ is the U (respectively S, V ) matrix of the SVD, truncated to k columns. L can be thought of as a generalized adjacency matrix in which paths of all lengths (not just length 1) make a contribution to the connections between each pair of nodes.

Cluster the pages by putting two pages in the same cluster if the magnitude of their vector sum exceeds α of the sum of their magnitudes. A page which does not fall within any existing cluster becomes the seed of a new cluster.

• For each cluster, generate a descriptive set of nouns, and a web page consisting of links to the pages in the cluster.

4. Iterate: Repeat the steps above for each cluster, using a prefix of the descriptive set of nouns as the initial keyword set.

ATHENS requires an underlying environment that is able to produce ranked lists of responses to a search query. Hence it is easily portable to other settings. It is also, at present, limited to English because of the dependencies of the tagger and the use of the BNC to determine how unusual each word is. These deficiencies are pragmatic rather than fundamental. Further technical details, as well as further examples of the use of the system, can be found in Ref. [14].

## 3. Validation

Validating a system that claims to produce novel information is difficult because there is no other way to determine how well it is doing. In particular, if ATHENS misses important novel information, there is no way to know that it is missing.

There are two big issues that make validation difficult. The first is that humans using ATHENS exhibit ontological bias — they expect the system to return clusters that are not only novel and relevant, but are also ontologically similar to the initial query. Because ATHENS, and the tools on which it is built, are essentially syntactic, clusters sometimes surprise users because they seem (superficially) to be “off topic”. Although this can be perceived as a weakness of ATHENS, it is arguably one of its strengths, since it presents information that is less biased by user expectations than a more semantic system would.

Humans also expect the individual pages within a cluster to be similar only in ways that humans would consider similar. However, we have discovered clusters in the Web that are tightly coupled, but would never be considered by humans as a “topic”. Again this could be considered a weakness but is probably really a strength. However, one consequence is that the 15-term descriptions of clusters can create the impression of a jumble rather than a cluster. This is usually dispelled by detailed consideration of the web pages that make up the cluster, but has made human validation difficult.

The claim that ATHENS discovers novel information is straightforward to validate. We need only to show that the content it returns is not explicit in the initial query terms. Because the system explicitly excludes search terms that have been used before, it always discovers pages, and so content, that are novel. The more important claim is that this novel information is important, relative to the original query, and this is much harder to validate.

An extensive series of evaluations were carried out in which a human subject expert was asked to list, in advance, a set of novel topics that ATHENS should discover relative to a given query. These experts were then given the results from an ATHENS run and asked to describe each cluster as uninteresting, novel as expected (i.e. was present on their list), or unexpectedly novel (i.e. not on their list but should have been). The percentage of clusters rated as interesting (expectedly or unexpectedly) ranged from 18 % (for a small technical topic) to 89 % (for a contemporary search similar to the one described below).

## 4. Experiment

We now illustrate the application of ATHENS by beginning from the initial keywords “bin Laden” and “al Qaeda” as the system would have performed on September 12th, 2001.<sup>1</sup> The purpose of this example is to illustrate what novel information would have been available immediately after the attack. The presumption is that data immediately relating to Osama bin Laden was known and understood. We now know that this was not entirely the case, but that aspect of the problem is not addressed here. ATHENS provides an answer to what information might have been missed, and what information might have been underappreciated because it was too diffuse to be detected.

The following parameters were used: number of pages in Closure: 10, number of pages in Probe: 5, number of new queries in Probe: 20, α: 1.92, and cluster representation: 3 terms (first phase), and 15 terms (second phase). The ATHENS system is not very sensitive to the precise value of these parameters, but the values used here were determined by extensive experimentation using a wide variety of queries. For example, choosing 10 pages for Closure amounts to saying that the top 10 pages returned by a Google search are typically a good sample of the pages relevant to a particular set of keywords; most people's experience with Google would validate this.

<table><tr><td>cluster</td><td>descriptor</td></tr><tr><td>1</td><td>Kherchtou Nairobi Mohamed</td></tr><tr><td>2</td><td>Mohamed Odeh United</td></tr><tr><td>3</td><td>Pakistan Taliban Afghanistan</td></tr><tr><td>4</td><td>Afghanistan American United</td></tr><tr><td>5</td><td>Kosovo Islamic Western</td></tr><tr><td>6</td><td>Muslim Peninsula Americans</td></tr><tr><td>7</td><td>Mullah Rabbani Taliban</td></tr><tr><td>8</td><td>York States United</td></tr><tr><td>9</td><td>Pakistan India Terrorism</td></tr></table>

Fig. 1. First-level cluster descriptors.

Similarly, choosing a smaller value for α would produce more and smaller clusters, but would not change the content significantly.

We first show the three-word queries generated as cluster centers after the first phase (Fig. 1). These clusters are not part of the output of the system, but they are useful in better understanding the output of the second phase. All of the descriptors at this stage have an obvious relevance, although it is clear that Set 8 are very general, so we might expect that its derivatives at the next level might be insufficiently contextualized to be useful. The problem here is that the ATHENS system is purely syntactic. Hence it correctly discovers that “New York” is a relevant term but does not understand that it is a phrase and its words should be kept together. “York” as a search term loses context.

Table 1 shows the 15-term descriptors generated for each second-level cluster. The system generates HTML pages containing the complete list of URLs corresponding to each cluster. These pages are the most useful way to interact with the results of the ATHENS system. However, the 15-term descriptors provide a way to summarize the system's output.

The 15-term descriptors are generated from the complete list of nouns in the pages of a cluster, with stopwords removed. Apart from acting as a compact description of each cluster, they are also useful as a set of search terms to find further content related to each cluster.

One of the striking things about these clusters is that they mention almost all of the countries that have turned out to be important in the history of al Qaeda and the fight against terrorism: Afghanistan, Albania, America, Australia, Azerbaijan, Bosnia, Egypt, India, Iran, Iraq, Israel, Japan, Kenya, Morocco, Pakistan, Philippines, Russia, Saudi Arabia, Serbia, Somalia, Sudan, United States, Tanzania, Yemen, Yugoslavia, as well as regions such as Kashmir.

Table 1  
Descriptors for second-level clusters

<table><tr><td>Label</td><td>Cluster identifier and search terms</td></tr><tr><td>1.1</td><td>Odeh Hage Rick Halperin York Albright United Embassy States Judge American Florida Americans Kenya Tanzania</td></tr><tr><td>1.2</td><td>Blair Hutchinson Poage Piper Rick Halperin Texas Ashley Flaherty Engleton Chester County Elmore Allan Rensch</td></tr><tr><td>1.3</td><td>Texas Halperin Rick United States Gaudin Kenya Salazar Press Hage Clinton Messages Odeh Calif District</td></tr><tr><td>2.1</td><td>Nairobi York Kenya Osama Tanzania Americans Franken States Washington Roger Cossack Embassy Khamis August Khalfan</td></tr><tr><td>2.2</td><td>American States Somalia Islamic president General Nations Saudi August Ladin Egypt Israel Morocco UNOSOM State</td></tr><tr><td>2.3</td><td>Fazul Dalitz Hage Islamic American Owhali Nairobi Osama Jews Afghanistan Arab Sudan States EmergencyNet ERRI</td></tr><tr><td>2.4</td><td>Reza Washington York Embassy Bombing Prosecution State April Department Hage Saudi Federal States Government East</td></tr><tr><td>2.5</td><td>Chair Abdul Razak Professor States Malaysia Ohio Sulaiman University Scholar America Prime Minister Southeast</td></tr><tr><td>3.1</td><td>Iran Islamic Kabul United Islam Sunni States Shia Muslim India Sharif American Russian Alliance Tehran</td></tr><tr><td>3.2</td><td>RAWA Peshawar Women Kabul Afghanistan International Association Revolutionary April Afghans Secretary Minister NWFP Chief Party</td></tr><tr><td>3.3</td><td>Islamic United Indian Kandahar Kabul States Omar Islam Bamiyan Buddhas Secretary Buddha December India Taleban</td></tr><tr><td>3.4</td><td>Iran Islamic Taleban September Tehran Sharif Islamabad Saudi Mazar Republic York Aziz Arabia Kabul Islam</td></tr><tr><td>3.5</td><td>Iran Sharif Kabul United Mazar President Nations Teheran Afghans York Mission Shia August Security States</td></tr><tr><td>3.6</td><td>Islamic Kabul Kandahar Islam Kashmir Afghans General United Mujahideen Iran India Sharif Asia Americans Muslim</td></tr><tr><td>3.7</td><td>Islami Islamic Hikmatyar Hizb Rabbani Khalis Islamist Pashtun Jamiat Mujahideen Kabul Burhanuddin Muslim Party Mohammad</td></tr><tr><td>3.8</td><td>Islamic Muslim Muslims Quran Allah Prophet Quranic Mohammed Ambassador Islam Shukriya America Hashemi Kabul Hindus</td></tr><tr><td>3.9</td><td>Government August Opinion Business Brig Imtiaz Bank Hindu India Intelligence Nan-garhar Tech Catalyst Investment Banking</td></tr><tr><td>3.10</td><td>Islamabad Sudan Internet Friday Osama Lahore InfoTimes Career Service Karachi Kashmir Services Peshawar Quetta Nation</td></tr><tr><td>4.1</td><td>Hoover Taliban Kandahar Kabul Soviets Taliban Islamic Azad Jamiat Jihaaad Straight Communist Mike Journalists Cindy</td></tr><tr><td>4.2</td><td>Taliban States Iran Pakistan Middle East Islamic Brown University Americas William Beeman html Economic Bombings</td></tr><tr><td>4.3</td><td>President Islamic Kyrgyzstan Kyrgyz Taliban Central States Akayev Republic Veterans Libya Iran Egypt Situation Bush</td></tr><tr><td>4.4</td><td>Islamic State Embassy International Kabul Department Asia Pakistan Travelers Sharia Globe Washington Medical Information Global</td></tr><tr><td>4.5</td><td>Taleban Islamic Pakistan Taliban Iran Osama International Amnesty Nations Kabul General States Islam Saudi Muslim</td></tr><tr><td>4.6</td><td>Iran States India Islamic Tehran Pakistan York Russian State President Anglo Department World Britain Washington</td></tr><tr><td>4.7</td><td>States State Islands President Vidal Okinawa Address Japan Union Soviet Sutton Island Inaugural America January</td></tr><tr><td>4.8</td><td>States Rights Human July April Colombia March Argentina Detention Death Committee Torture Americas International Violations</td></tr><tr><td>4.9</td><td>Islands Jan28 Island Mar31 Republic Jan4 Apr31 South North Codes Country Guinea Arab Cape British</td></tr><tr><td>4.10</td><td>Islands Africa Assigned ASIA Republic Island South Coded East Arab Yemen French Azerbaijan Central West</td></tr><tr><td>4.11</td><td>Dollar Franc Pound Islands French States Peso East Countries Caribbean Dinar Zealand Rupee Island Guinea</td></tr><tr><td>4.12</td><td>Muslim Islamic Muslims Quran Taliban Allah Prophet Quranic Mohammed Shukriya Islam Kabul Hindus Sikhs Perfect</td></tr><tr><td>5.1</td><td>Albanians Albanian Orthodox Serb Church Serbian Serbs Muslim Metohija Europe Bosnia Christian Muslims Serbia Catholic</td></tr><tr><td>5.2</td><td>Albanians Albanian Albania Muslims Muslim Serbian NATO Serbs Europe Kosovars Kosovar Macedonia West Yugoslavia Balkans</td></tr><tr><td>5.3</td><td>NATO Yugoslavia Serbs Bosnia Albanians Serbian Albanian Milosevic Serbia Yugoslav Serb Muslims Bosnian Muslim Balkans</td></tr><tr><td>5.4</td><td>Albania Bosnia Muslim Iran Serbs Iranian Saudi Albanians Saudis Israel Afghanistan April Croatian Yugoslav Albanian</td></tr><tr><td>6.1</td><td>Islam Islamic Muhammad Allah United States World Christian Mohammad Melungeon English Christians Elijah Prophet North</td></tr><tr><td>6.2</td><td>Almighty Jihad Islamic Islam Jews Crusaders Shaykh Muhammad Group Egypt Arabian Front Statement Iraq Imam</td></tr><tr><td>6.3</td><td>Philippines Marcos Filipinos Base Pacific Indigenous Filipino President Clark Force Island Subic Naval Japan Army</td></tr><tr><td>6.4</td><td>Islam Philippines Filipinos Mindanao Moro Christian Peace Agreement Filipino Christians Islamic ARMM South Philippine Province</td></tr><tr><td>6.5</td><td>Republic Vietnam Vung Mindanao Philippines China Pacific Saigon Japan Empire United Japanese Singapore World Dairen</td></tr><tr><td>7.1</td><td>RAWA Afghanistan Peshawar April Afghans Pakistan Tuesday Saudi Police Revolutionary Association Kabul Women Khalili Road</td></tr><tr><td>7.2</td><td>Mirror China Afghan Afghanistan President Japan Islamic State Chinese Tech Advanced Sitemap Parliament European Massoud</td></tr><tr><td>8.1</td><td>School District Local Nevada Middle Schools Public High County City Unified Junior Shelley Valley East</td></tr><tr><td>8.2</td><td>Census County Pennsylvania Listings Genealogy Records Data USGenWeb Septennial Update Ancestry Sign MyFamily Software Policy</td></tr><tr><td>8.3</td><td>County Census Genealogy GenSource Guide Found Records Common Archives Policy Pennsylvania Ancestry Directory Highlighted Tree</td></tr><tr><td>8.4</td><td>Pennsylvania Times Daily Journal Post Herald Gazette Australia Star Sunday Morning Pittsburgh National Sharon Pakistan</td></tr><tr><td>8.5</td><td>Gazette Boston Pennsylvania Advertiser Journal London Massachusetts Weekly South Carolina American Virginia Bath Hampshire Great</td></tr><tr><td>8.6</td><td>University College Michigan Illinois Virginia Xavier Wisconsin Tech Boston Univ Millersville Southern School Tennessee Central</td></tr><tr><td>9.1</td><td>South Asia Bush President States Kashmir United American China Russia Ambassador Foreign Brookings Afghanistan Policy</td></tr><tr><td>9.2</td><td>Kashmir October Jammu Kashmiri Killings Times Terrorists Information Poonch Terrorist Islamic Pandits Network Tribune Srinagar</td></tr><tr><td>9.3</td><td>Kashmir Islamic Islamabad State Muslim Department Afghanistan Singh China Delhi Asia Nuclear Kashmiri South Government</td></tr><tr><td>9.4</td><td>South Reuters Durban Paul Africa Sept Richardson Aligned Movement 12th Delegates Comprehensive Nuclear Test Treaty</td></tr><tr><td>9.5</td><td>Kashmir Jammu Islamic Clinton Sharif Hindus Hindu Times Kashmiri Iraq President Lord Avebury Indian Minister</td></tr></table>

Recall that the African embassy bombing suspects were on trial in the U.S. during the summer of 2001. The clusters 1.1–1.3 concern the death penalty issue, with some connections to the embassy bombings, but to other death penalty cases as well. Clusters 2.1–2.4 focus on the embassy bombing trials, as well as related bombing operations in Somalia. At this time, the connection between these bombings and Osama bin Laden was not considered well-established, and there was a tendency to regard him as a financial backer, rather than as a terrorist leader.

Clusters 3.1–3.10 can be summarized as dealing with Afghan and regional politics. Cluster 3.1 concerns Islamic religious politics; cluster 3.2 concerns the role of women in Afghanistan; cluster 3.3 concerns the destruction of statues of the Buddha in Afghanistan by the Taliban; cluster 3.4 concerns the Taliban; cluster 3.5 concerns relations between the Taliban and Pakistan; cluster 3.6 has similar content but in a wider context; cluster 3.7 concerns mujahideen groups and leadership; cluster 3.8 consists of pro-Taliban propaganda; cluster 3.9 concerns the role of heroin in the region; and cluster 3.10 concerns perceived U.S. aggression towards Pakistan.

Clusters 4.1–4.12 can be summarized as history and geography. Clusters 4.1–4.6 provide background on Islamic countries from the former Soviet Union through to India. Cluster 4.7 concerns U.S. history and geography. Cluster 4.8 concerns human rights, while cluster 4.12 contains anti-Taliban propaganda. Clusters 4.9– 4.11 are nice examples of shifts in ontologies: 4.9 gives telephone country codes; 4.10 contains details of country-specific properties such as postage stamps; and 4.11 contains details of currencies. These clusters might be considered as indicating the extent to which the initial search terms reflect a global phenomenon.

Clusters 5.1–5.4 have content specific to the Balkans, both the conflicts following the breakup of Yugoslavia, and the subsequent civil war in Kosovo.

Clusters 6.1–6.5 can be summarized as history. Cluster 6.1 is about clashes between religions, particularly in the past two centuries. Cluster 6.2 contains some of the historical material used by Salafist Islam to justify its jihad against the west. Cluster 6.3 concerns the older history of the Philippines, and cluster 6.4 the more recent Islamic history. Finally, cluster 6.5 is a summary of Pacific history. This set of clusters is particularly interesting because it makes the connection between Middle Eastern al Qaeda and the Islamic terrorist organizations in the Far East, including the Moro Islamic Liberation Front.

Clusters 7.1–7.2 are the least consistent. Cluster 7.1 contains further material on the oppression of women in Afghanistan; while cluster 7.2 contains Chinese commentary on the Taliban.

Clusters 8.1–8.6, as expected, are internally cohesive, are not sufficiently contextualized to be useful. The occurrence of the word ‘York’ produces several clusters concerning York County in Pennsylvania. Cluster 8.4 and 8.5 concern newspapers, while cluster 8.6 concerns radio stations.

Clusters 9.1–9.5 are generally concerned with the situation in Kashmir and its connections. Cluster 9.1 concerns Indian, Pakistani, and Afghan terrorism. Cluster 9.2 focuses on terrorism in Kashmir. Cluster 9.3 concerns terrorism in the wider Asian context. Cluster 9.4 concerns the nuclear non-aligned movement, as a result of the development of nuclear weapons by both India and Pakistan. Finally, cluster 9.5 concerns that likelihood that Pakistan will follow the path of Iraq towards rogue statehood.

Because this search was executed as if at an earlier time, we have another opportunity to validate its results because of public investigations into the structure and operation of al Qaeda in the four years since the September 11th attacks. It is striking how much overlap there is between the final list of clusters and the material covered in broadly investigative books such as Refs. [4] and [6].

How effective would the content of these clusters have been at guiding decision making in the immediate aftermath of the September 11th attacks? Almost certainly, most of this content was available, in some form, to intelligence organizations. The structure imposed by ATHENS might have been suggestive about the relative importance of various aspects. For example, it is clear from these results how widespread the connections were between al Qaeda and Islamic terrorism groups and factions in other settings (for example, Salafist terrorists who are non-Arabs, or are geographically remote from the historical center of Islamic terrorism); and how weak the connections between al Qaeda and Iraq were. These results might also have provided further evidence for the importance of bin Laden as a guiding hand behind many trends that seemed, at the time, to be unconnected. It is certainly the case that the clusters collected here provide a fairly complete primer on Salafist Islamic terrorism that would have informed, for example, the media of the scale of the problem in the immediate aftermath of the attacks.

<table><tr><td>cluster</td><td>descriptor</td></tr><tr><td>1</td><td>Iraq, Bush, Saddam</td></tr><tr><td>2</td><td>Saudi, Afghanistan, Islamic</td></tr><tr><td>3</td><td>Islamic, Qaida, Jihad</td></tr><tr><td>4</td><td>Afghanistan, United, States</td></tr><tr><td>5</td><td>Iraq, Hussein, Rumsfeld</td></tr><tr><td>6</td><td>Saudi, Osama, Arabia</td></tr><tr><td>7</td><td>Bush, Carlyle, Saudi</td></tr><tr><td>8</td><td>Saudi, Qaida, Friday</td></tr><tr><td>9</td><td>Pakistan, Bush, Taliban</td></tr><tr><td>10</td><td>Terrorism, Osama, August</td></tr><tr><td>11</td><td>Military, Organization, Espionage</td></tr><tr><td>12</td><td>Harthi, East, Middle</td></tr><tr><td>13</td><td>September, Paperback, Saudi</td></tr></table>

Fig. 2. First-level cluster descriptors in 2004.

What is missing is any connection between al Qaeda in its Middle East incarnation, and Salafist terrorist groups in Europe, including the related groups in countries such as Algeria and Morocco. This appears to be justified by the scarcity, at that time, of any web content making connections between these two subgroups; such pages as do exist are mostly about the Balkans (which are contained in Clusters 5.1–5.4).

Fig. 2 shows the first-level cluster descriptors for the same query in 2004. It is clear from these terms how much al Qaeda has had a global impact, as much from United States responses as from the initial attacks. The increased visibility of Iraq is entirely expected. Note the increased emphasis on Saudi Arabia, partly due to bin Laden's connection there (clusters 6 and 8) and partly for other reasons (clusters 2 and 13).

## 5. Conclusions

Intelligence analysts need tools that allow them to work with large information spaces, and which help them to break out of preconceptions to consider a larger fraction of the hypotheses that the available data may support. Exploratory data mining can help with the second problem, but is not directly useful for information repositories such as the World Wide Web.

The ATHENS system is designed to address both problems by piggybacking on existing tools such as search engines to fetch appropriate subsets of the huge available data; and by using contextualized searches to go beyond the limitations of an analyst's existing knowledge.

We have demonstrated the use of the system by generating the knowledge it would have produced if started from “al Qaeda” and “bin Laden” on September 12th, 2001. The results demonstrate the effectiveness of the system, and are also of some inherent interest.

Software: The ATHENS system is available from www.cs.queensu.ca/home/skill/athens.html.

## References

[1] W.E. Baker, R.B. Faulkner, The social organization of conspiracy: illegal networks in the heavy electrical equipment industry, American Sociological Review 58 (December 1993) 837–860.

[2] British National Corpus (BNC), www.natcorp.ox.ac.uk, 2004.

[3] T. Coffman, S. Greenblatt, S. Marcus, Graph-based technologies for intelligence analysis, CACM 47 (3) (March 2004) 45–47.

[4] J. Corbin, Al-Qaeda: In Search of the Terror Network that Threatens the World, Thunder's Mouth Press, 2002.

[5] M. Granitzer, W. Keinreich, V. Sabol, G. Dosinger, WebRat: supporting agile knowledge retrieval through dynamic, incremental clustering and automatic labelling of Web search results, Twelth IEEE International Workshops on Enabling Technologies: Infrastructure for Collaborative Enterprises (WETICE'03), 2003, pp. 1080–1383.

[6] R. Gunaratna, Inside al Qaeda, 3rd edition, Berkley Publishing Group, 2003.

[7] D. Jensen, J. Neville, Data mining in social networks, Invited Presentation to the National Academy of Sciences Workshop on Dynamic Social Network Modeling and Analysis, November, 2003.

[8] H. Liu, MontyTagger v1.2, 2003. web.media.mit.edu/hugo/ montytagger.

[9] R. Popp, T. Armour, T. Senator, K. Numrych, Countering terrorism through information technology, CACM 47 (3) (March 2004) 36–43.

[10] K. Popper, The Logic of Scientific Discovery, Hutchinson, London, 1959.

[11] M. Sageman, Understanding Terror Networks, University of Pennsylvania Press, 2004.

[12] D.B. Skillicorn, Detecting related message traffic, Workshop on Link Analysis, Security and Counterterrorism, SIAM Data Mining Conference, 2004, pp. 39–48.

[13] D.B. Skillicorn, Finding unusual correlation using matrix decompositions, Second Symposium on Intelligence and Security Informatics, 2004.

[14] D.B. Skillicorn, N. Vats, The Athens system for novel information discovery, Technical Report 2004-489, Queen's University School of Computing Technical Report, October 2004.

[15] K.A. Taipale, Data mining and domestic security: connecting the dots to make sense of data, Columbia Science and Technology Law Review 2 (December 2003).

[16] J.R. Tyler, D.M. Wilkinson, B.A. Huberman, Email as spectroscopy: Automated discovery of community structure within organizations. HP Labs, 1501 Page Mill Road, Palo Alto CA, 94304, 2003.

[17] United States Government, Final Report of the National Commission on Terrorist Attacks Upon the United States, 2004.

[18] N. Vats, D.B. Skillicorn, Information discovery within organizations using the Athens system, Proceedings of 14th Annual IBM Centers for Advanced Studies Conference (CASCON 2004), October 2004.

David Skillicorn is a Professor in the School of Computing at Queen's University, where he heads the Smart Information Management Laboratory. He is also the coordinator for Research in Information Security in Kingston (RISK). He is an adjunct Professor at the Royal Military College of Canada. His research interests are in data mining, particularly for counterterrorism and fraud; he has also worked extensively in parallel and distributed computing.

Nikhil Vats was a graduate student in the School of Computing at Queen's University, where he developed the ATHENS system. He now works for Certicom, a security company.
