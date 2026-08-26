---
otero_id: 772
otero_key: "84AW74WQ"
title: "Auction Advisor: an agent-based online-auction decision support system"
authors: "Dawn G. Gregg; Steven Walczak"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.07.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 41 (2006) 449 – 471

www.elsevier.com/locate/dsw

# Auction Advisor: an agent-based online-auction decision support system

Dawn G. Gregg<sup>\*</sup>, Steven Walczak

University of Colorado Denver, The Business School, Campus Box 165, P.O. Box 173364, Denver, CO 80217-3364, United States

Received 1 August 2003; accepted 1 July 2004

Available online 29 September 2004

## Abstract

Online auctions are proving themselves as a viable alternative in the C2C and B2C marketplace. Several thousand new items are placed for auction every day and determining which items to bid on or when and where to sell an item are difficult questions to answer for online-auction participants. This paper presents a multiagent Auction Advisor system designed to collect data related to online auctions and use the data to help improve the decision making of auction participants. A simulation of applied Auction Advisor recommendations and a small research study that used subjects making real purchases at online auctions both indicate that online-auction buyers and sellers achieve tangible benefit from the current information acquired by and recommendations made by the Auction Advisor agents. © 2004 E1sevier R V, A1l right

Keywords: Decision support; Online auction; Information retrieval; Autonomous agent; Data analysis

## 1. Introduction

Online auctions are one of the most successful types of electronic marketplaces (with Bay alone generating over US\$15 billion in sales) [3]. Over 10 million items can be found daily for sale at onlineauction sites, like eBay, Amazon, and Yahoo. The ability to bring together auction participants at such a massive scale provides both advantages and disadvantages to buyers and sellers. The success of online auctions has given buyers access to greater product diversity with potentially lower prices. It has provided sellers with access to large numbers of potential buyers [30] and reduced transaction costs by enabling auctions to take place without regard to time or place [7]. However, this success comes at a price. Buyers must incur higher search costs to locate desired products and sellers face greater competition from the multitude of other sellers [21].

Software agents have great potential for increasing the realized benefit for both buyers and sellers participating in online auctions. They can be used to provide price histories, to set up auctions, find specific items, and place appropriate bids [19]. Numerous intelligent agents have been developed for a variety of e-commerce applications (e.g., Refs. [9,13,18,20,35, 38,45,50]). This research examines the potential impact of a system of collaborating information retrieval (IR) agents, data-analysis (DA) agents and personal agents that can automatically collect large volumes of auction data and make recommendations that have the potential to change a participant’s normal behavior, such that they can realize a measurable benefit from the change (e.g., decreased cost for buyer, increased sale, or bidding activity for a seller).

This research utilizes a design science research methodology to develop a prototype system that applies both statistical methods and heuristic rules to assist auction participants in determining appropriate pricing and bidding strategies. The research includes the development of an auction information retrieval agent, a data-analysis agent, and a bidding agent that allows auction participants to analyze current and past auction characteristics for any item being sold on eBay, Amazon, or Yahoo. The prototype system also includes a rule-based system that makes specific recommendations to end-users based on the most current auction data and on domain-specific decision rules derived from prior auction research. Both simulation tests and an experiment using 20 research subjects making real purchases are used to validate the Auction Advisor system.

This paper is organized as follows: Section 2 reviews related work with autonomous agents. Section 3 describes the various agents that comprise the Auction Advisor agent system and discusses their functionality. Section 4 discusses the validation of the Auction Advisor system, including the simulation study and small research study. Section 5 discusses the development of an auction recommendation rule base. The final section summarizes the results, and discusses potential drawbacks of the existing system and future research directions for agents operating in online auction and e-commerce domains.

## 2. Related work

The Auction Advisor system relies on intelligent agents both for the retrieval of relevant auction data and for the processing and analysis of that data to enable meaningful recommendations to be made to auction participants. Intelligent agents are programs designed to assist end-users in different ways. They can hide the complexity of difficult tasks, perform tasks on the user’s behalf, train or teach the user, help different users collaborate, or monitor events and procedures [31]. Today, agents operating in heterogeneous networked computing environments are being used for search, retrieval, and analysis of previously unimaginable quantities of data [36]. This research includes intelligent search engines [24,28,33,42,49]; agents that track user activities and data to improve end-user decision making [10,22]; and agents that find and classify specific types of information on the Web [11,15,48]. These agents do not attempt to map or understand the entire Web. Instead, they attempt to process specific types of content about which the agent has some prior knowledge.

Some agents have already been introduced in the online-auction domain. Agents found at BidXS.com and McFind.com may be used to compare offerings across multiple online-auction sites. McFind.com allows simultaneous category browsing or searching of both Amazon.com and Yahoo.com. BidXS.com provides a more complete buyers agent that allows keyword searches, searches by category, and searches by price. BidXS.com has also partnered with Strong Numbers to make past price trends available for specific online-auction items. This allows potential buyers (and sellers) to determine what other people paid for any of the items being tracked [19].

The opportunities for using agents in e-commerce applications are enormous. Agent characteristics, like autonomy, abilities to perceive, reason and act in specialized domains, as well as their capability to cooperate with other agents, make them ideal for ecommerce applications [37]. However, many current agents do not provide a comprehensive service to endusers. For example, many previously proposed information retrieval agents are capable of retrieving specific information but do not have the ability to filter, analyze, or make recommendations based on that information [43]. In addition, agents, like Strong Numbers, only provide information on a predetermined set of products.

Unlike previous auction decision support systems, the Auction Advisor system, presented in the next section, allows auction participants to analyze current and past auction characteristics for any item being sold on any auction site it supports (currently eBay, Amazon, and Yahoo). The system makes specific recommendations to end-users based on a statistical analysis of the most current auction data and using domain-specific heuristic rules derived from prior auction research. Finally, it provides buyer, seller, and information agents that allow end-users to act on the data retrieved.

## 3. Auction Advisor

The Auction Advisor agent system collects and classifies available data on both active and closed auctions. The Auction Advisor initially focuses on collecting all available data on open and closed auctions for specific products of interest. Once data for a user-specified product has been gathered, relevant statistics are calculated. These statistics are used to allow specific recommendations related to pricing and bidding to be made to buyers or sellers. Auction researchers can also use summarized data to further their understanding of online auctions. This section describes in detail the architecture of the Auction Advisor system.

Fig. 1 shows the multitier architecture of the Auction Advisor system. The system is designed in four layers. The Data layer consists of the data and rules necessary for the functioning of the Auction Advisor system. There are three primary sources of data for the system. First, the Web contains the data on current and recently closed auctions; second the Auction database contains historic data previously collected by IR agents; and finally, the Recommendation Rule Base contains the rules that govern the decision support (in the form of recommendations) provided to either buyers or sellers.

The agents are found in the other two server-side layers. The Business Logic layer contains the agents responsible for retrieving and processing/analyzing the online-auction data. These agents communicate with buyer, seller, or information agents in the User Service layer, which initiates processes as well as perform bidding and other services on behalf of the end-users. The Presentation layer consists of the user interfaces that enable auction agents to communicate and interact with users. User to agent communication is required to enable the agent to perform auction searches and bidding (the establishment of an agent contract to perform a task) and to deliver the auction knowledge and consequent heuristic auction recommendations.

![](/api/attachments/84AW74WQ/fulltext/images/2f2e7de70ad065beadfbb5c5bcbfff881d0e2e20c2a143552998f666ccbf4085.jpg)  
Fig. 1. Auction advisor agent system.

## 3.1. The information retrieval agent

The information retrieval agent (IR) is the workhorse of the Auction Advisor application. It is responsible for retrieving the HTML Web pages, parsing them to extract specific data, and validating the data to ensure the information retrieved is actually the data of interest (e.g., is the data for an auction and not meaningless text). The IR agent utilizes domain knowledge related to the structure of three top auction sites (eBay, Yahoo, and Amazon) to extract relevant auction data from HTML Web pages. The IR agent works as follows:

(1) The IR agent runs a query at an auction site either to return all the auctions in a given auction category and/or to retrieve all auctions corresponding to specific search terms.

(2) The Web page(s) returned by the auction site is parsed using an HTML parser to identify the structure and arrangement of the HTML elements within the page. The auction id, current auction price, and auction close date are extracted for each auction within the retrieved Web pages. These items are identified based on the position of the data within the Web page.

(3) The IR agent verifies that all data collected for each auction is of the appropriate data type and ranges before permanently storing the data.

(4) The IR agent also will retrieve specific item data, bid data, and participant data based on additional end-user requests.

Currently, the IR agent requires the position of specific auction data within the Web page to be defined explicitly before it can parse the page correctly. Knowledge about the structure of the eBay, Yahoo, and Amazon Websites has been encoded in the parser’s knowledge base. Continuing research is investigating the automatic decomposition of Web page HTML to enable the IR agents to acquire information from any online-auction Website without having to predefine the page structure. It is also possible that online-auction sites will eventually make online-auction data available in XML format, greatly simplifying the identification of the auction data. However, this requires the development and acceptance of an online-auction XML data definition standard.

One characteristic of the IR agent is that it is capable of interacting directly with the auction site’s user interface. The IR agent posts messages using the appropriate form elements when querying the auction site. This allows the agent to perform any action a human can perform, including searching, bidding, and posting an item for sale. Once the IR agent has acquired, verified, and stored relevant online-auction information, it automatically invokes the data-analysis agent to analyze the retrieved information.

## 3.2. Data-analysis agent

The data-analysis (DA) agent is responsible for helping the end-user select an appropriate set of search terms, calculating the relevant statistics for auctions of interest, and identifying the appropriate recommendations that can be returned to the buyer, seller, or information agent. The DA agent works as follows:

(1) The DA agent receives a list of relevant search terms from either the buyer, seller, or information agent and requests closed auction data for these types of products from the IR agent.

(2) If the items returned appear to represent multiple different types of products (based on closing prices), the data-analysis agent initiates a search refinement process with the end-user. As a part of this process, the end-user selects specific auctions that match and do not match the product type they are interested in. The data-analysis agent then generates a set of additional search terms (both to include and to exclude), which the end-user can edit, to define a more specific search.

(3) The DA agent requests the IR agent rerun the search using the revised search terms and then the DA agent calculates all of the relevant statistics related to these retrieved auctions. These statistics are summarized in Table 1.

(4) The DA agent queries the Recommendation Rule Base to identify specific recommendations that can be made to either a buyer or a seller. The development of rules for the Auction Advisor system is discussed in Section 5.

(5) Relevant auction statistics for the specified product(s) and buyer or seller action recommendations are returned to the buyer, seller, or information agent.

Table 1  
Auction statistics calculated by the data-analysis agent

<table><tr><td>Data value</td><td>Statistics calculated</td></tr><tr><td>Initial price</td><td>Median, minimum, and maximum</td></tr><tr><td>Number of bidders (for closed auctions)</td><td>Median, minimum, and maximum</td></tr><tr><td>Seller rating</td><td>Median, minimum, and maximum</td></tr><tr><td>Bidder rating</td><td>Median, minimum, and maximum</td></tr><tr><td>Auction duration</td><td>Median, minimum, and maximum</td></tr><tr><td>Auctions specifying a reserve price</td><td>%</td></tr><tr><td>Auctions specifying a buy now price</td><td>%</td></tr><tr><td>Buy now price specified</td><td>Median, minimum, and maximum</td></tr><tr><td>Open auctions found (current)</td><td>Total</td></tr><tr><td>Opened auctions for which there are bids</td><td>%</td></tr><tr><td>Current price (open auctions)</td><td>Median, minimum, and maximum</td></tr><tr><td>Closed auctions found</td><td>Total</td></tr><tr><td>Auctions for which there were bids (closed auctions)</td><td>%</td></tr><tr><td>Auctions with bids placed in the last 5 min (closed auctions)</td><td>%</td></tr><tr><td>Sales price (closed auctions)</td><td>Median, minimum, and maximum</td></tr></table>

Search refinement by the DA agent reduces information overload for users by limiting auctions to those that have higher relevancy ratings and further enables more complex searches to be performed than traditionally offered by online-auction services. Future research will examine the implementation of a user model in the data layer. The user model will track initial search terms, refined search terms, preferred categories, and other potential criteria, such as item cost and seller rating. Subsequent searches on similar terms by the same user will automatically be refined based on the preferences captured by the DA agent and stored in the user model to help reduce the required interactions between the user and the agents.

## 3.3. Buyer, seller, and information agents

Buyer, seller, and information agents are responsible for the communication with the end-user as well as for performing specific services (like bidding) on the user’s behalf. The standard user interface is shown in Fig. 2. The user specifies the required information through the agent’s interface. The required information and corresponding actions of the agent are as follows:

(1) The Buyer/Seller interface allows the user to specify the following information:

<sup>!</sup> Buy or sell. This determines the set of rules in the recommendation rule base that can be activated.

<sup>!</sup> Auction sites to be searched: the interface currently supports eBay, Amazon, and Yahoo. If the user does not specify any sites, then the agent defaults to searching all of the onlineauction Websites as a comprehensive approach.

<sup>!</sup> A description of the item to be bought or sold. This consists of a single keyword or phrase or multiple terms. Similar to most Web search engines, the auction item search enables the user to specify terms that must be in the title of the item (AND terms), terms that could be in the title (OR terms), and terms that cannot be in the title (NOT terms).

<sup>!</sup> A category that the item is likely to be found in—this helps improve search accuracy. If the user does not specify a particular product category, then the search is performed across all categories available at each online-auction Website.

<sup>!</sup> The item condition—this creates an OR (or NOT) search that uses many synonyms for <sup>b</sup>new<sup>Q</sup> commonly used in most auction titles. The default for the Auction Advisor agents is to retrieve items in any condition (i.e., condition is not used as part of the search terms).

(2) After the user specifies all necessary values (and default values assigned for optional information), the IR and DA agents are activated to collect the most recent closed item data and calculate advisory data values.

(3) If the items returned appear to represent multiple different types of products (based on closing prices), a search refinement process is initiated by the DA agent, described above, in which the end-user selects specific auctions that match and do not match the product type in which they are interested. These selections are used to generate a revised set of keywords to use in the auction search process.

![](/api/attachments/84AW74WQ/fulltext/images/173ada9612208517afd404ce67fa7fefbed5aa447f12b2b18235015f82ab2878.jpg)  
Fig. 2. Buyer/Seller agent interface.

(4) A search of open and closed auctions is conducted at all of the selected auction sites and relevant statistics, recommendations, and relevant auction data are returned to the active agent (buyer, seller, or information) for presentation to the user.

It is at this phase of the process that the buyer, seller, and information agent functionality diverges.

## 3.3.1. Buyer agent

The buyer agent interface presents statistical information, such as the average and minimum and maximum price paid for matching auctions to enable users to use their own judgment regarding the information presented and how it may relate to their current activity. Basic decision support for online bidding, such as the recommended maximum price that should be paid given current auction conditions, is also presented. In addition, a list of open auctions that have current prices at or below the recommended maximum price is presented to the end-user. The user can choose to visit the actual auction page for the items (via a hyperlink) or to use Auction Advisor to place a bid on the item.

One of the limitations of current bidding tools available at the different online-auction sites is that they do not allow users to specify their bid times or participate in multiple alternative auctions. Research has been conducted that indicates the use of bidding agents that facilitate the bidding process can be of benefit to both auction buyers and sellers [2,6,14, 18,39]. However, currently, to place a bid directly at a major auction site, bidders must go to the site and place the bid at exactly the time they want to bid. They must wait until they lose that bid before they can indicate they want to participate in another auction.

Auction Advisor’s bid manager improves the auction bidding process by managing much of the bidding process for the buyer.

<sup>!</sup> It can place bids at multiple auction sites.

<sup>!</sup> It allows bids to be timed so they are placed at exactly the time the user wants.

<sup>!</sup> It allows the buyer to select several products and will bid on them in order and will stop placing bids as soon as one of the auctions is won.

<sup>!</sup> It will not allow two bids placed on any different auctions at any one time (ensuring only one item is ever won).

<sup>!</sup> It allows the user to add new bids to the bid manager at any time prior to the end of an auction.

<sup>!</sup> It allows the user to cancel any bids prior to them being placed at one of the online-auction sites.

The advantage of multiple item bidding is that it allows users to select several items to bid on during one browsing session. The user specifies the maximum price to be paid for each item they are bidding on as well as the time they want the agent to place their bid. Auction Advisor can manage the bidding process for the user, potentially placing several bids until one of the bids wins. This can significantly reduce the time demands of auction buyers participating in online auctions.

## 3.3.2. Seller agent

The seller agent interface presents statistical information, such as the average and minimum and maximum price paid for matching auctions for each auction site. Basic recommendations, such as the recommended minimum price and reserve prices, are presented. In addition, the sales agent makes recommendations as to what auction site the item should be listed at based on recent closing auction prices and on the percentage of recent auctions that closed at or above the median closing price. The agent uses an O(n) expected-time algorithm based on a quick-sort to find the median [17].

One of the most difficult tasks for new auction sellers is the selection of appropriate titles, descriptions, and categories for their auction item. The sales agent can also assist sellers with the creation and placement of items for sale on online auctions.

<sup>!</sup> It allows the seller to select several closed auctions that are very similar to the item that he is planning on placing at auction.

<sup>!</sup> The seller agent generates the following information that can be used when deciding how to set up the auction:

<sub>o</sub> A list of keywords that should appear in the title,

Sample descriptions that can be used in developing the description for the auction,

The categories prior auctions were placed in,

<sub>o</sub> The average starting price for the prior auctions,

<sub>o</sub> If the selling price on prior auctions is substantially higher than the starting price, the agent will recommend the seller set a reserve price and suggest an appropriate reserve value.

<sup>!</sup> The seller can enter title and description information for the product they are selling and the seller agent will generate the HTML code necessary for a professional-looking Auction description.

The seller can enter the item id assigned to the auction by the auction site and the seller agent will track the status of the item for the user, including when the first bid is received, current high bid, and other bidder information such as bidder rating.

## 3.3.3. Information agent

In addition to providing accurate and current information and recommendations based on that information to buyers and sellers, the Auction Advisor agent system may also be used as a data mining and analysis system to support online-auction research and for the generation of additional rules for the auction heuristic rule base. The information agent allows an auction researcher to search specific auctions and presents statistical information, such as the average and minimum and maximum price paid for matching auctions at each auction site. The researcher then has the option to:

<sup>!</sup> Download specific auction data in XML format,

<sup>!</sup> Generate a new rule based on the data retrieved,

<sup>!</sup> Test a generated rule with data from a different auction search.

The auction data analysis and rule generation are discussed in more detail in Section 5.

While current information retrieval through the IR and DA agents is limited to the three most active online-auction Websites, new online-auction Websites may easily be added by updating an XML data file describing the auction sites. A future extension of the Auction Advisor Buyer and Seller agent interfaces will enable a user to select from the predefined list or enter a specific URI. As discussed in the Information Retrieval Agent section, current ongoing research is investigating the automatic decomposition of Web pages, thus enabling the Auction Advisor IR, buyer, and seller agents to appropriately navigate and mine any online-auction Website. Alternately, the definition of an online-auction XML ontology would also facilitate more automated navigation and mining of auction Websites.

Currently, the item search by the IR and DA agents is performed using a keyword-sensitive search. Thus, one or more keywords must appear in the title of the auction exactly as entered by the user. Future enhancements to the Auction Advisor agent system will attempt to implement a more generic search that will be able to find near-misses (for misspelled words), use synonyms for searching via the use of an online thesaurus, and incorporate some additional natural language processing capabilities. As previously indicated, a preliminary implementation of a synonym-based search has been successfully implemented for the <sup>d</sup>item condition<sup>T</sup> part of the IR agent’s search criteria. Future versions will look to expand the synonym and near-miss capabilities of the Auction Advisor agent system. Fortunately, the multitier agent architecture of the Auction Advisor agent system facilitates the incorporation (with encapsulation) of new search methods as they become available without interfering with the remainder of the Auction Advisor agent system functionality [8].

## 4. Evaluation of Auction Advisor

Once the prototype Auction Advisor system is developed, it is evaluated using a simulation experiment designed to predict the agent’s performance under real auction purchase and sales conditions. The simulation monitors actual auctions over a period of time in select product categories to determine the relevance and applicability of the Auction Advisor decision support recommendations.

## 4.1. Research hypothesis and evaluation criteria

The goal of the simulation testing was to determine if the Auction Advisor decision support recommendations made to buyers and sellers would allow them to make better purchase or sales decisions than they would without the system. This implies the research hypothesis:

H : Buy and sell decision support recommendations made by the Auction Advisor multiple agent system and based on current online-auction performance information will produce measurable benefit to buyers and sellers.

A time frame of 2 weeks is used for the simulation, enabling the Auction Advisor to participate in multiple auctions. The hypothesis is evaluated using empirical evidence from the simulation, with the following two criteria (one for buyers and one for sellers) utilized to determine if a measurable benefit has occurred.

Buyer Criteria: Suggested bid recommendations made by the Auction Advisor system are at or below the median price paid by other buyers of substantially similar products and higher than the minimum price paid for at least one substantially similar product sold during the 2-week period following the recommendation.

The buyer-side evaluation criteria is composed of two interdependent parts: that the supported bid be low enough to achieve the desired measurable benefit to the buyer (cost savings) and that the supported bid is high enough to exceed minimum bid limitations set by sellers that would otherwise exclude the Auction Advisor from locating viable auctions. The need for a bid recommendation being higher than the minimum price paid for an auction is to ensure that the bid supported by the Auction Advisor is sufficiently high to win an auction. Some auctions will not receive a bid, resulting in a minimum price of zero, thus allowing any bid (that meets the minimum bid of the auction) to win the auction. The research hypothesis is supported by the simulation evidence if one or more of the available auctions for each product examined could have been won using the maximum bid suggested by Auction Advisor, with strong empirical support gained when at least 50% of available auctions for a particular product could have been won using an Auction Advisor suggested bid price which is currently set to the median price of recent auctions on similar products.

Seller Criteria: Suggested minimum and reserve price recommendations made by the Auction Advisor system will be low enough such that bids that exceed these amounts will be placed on more than 50% of similar items being sold and will be high enough that products will not be sold at less than 50% of the median price paid for similar products sold during the 2-week period following the recommendation.

Similar to the buyer-side evaluation criteria, the seller-side evaluation criteria is also composed of two interdependent parts: that the supported minimum (opening) bid is low enough to attract buyers and that the supported reserve price or minimum bid if no reserve price is suggested is high enough to meet or exceed the seller’s valuation (expected value) of the product.

## 4.2. Simulation method and results

During the testing of the Auction Advisor, a set of 15 different products were evaluated for potential purchase or sale via an online auction. These products are listed in Table 2. The product categories selected represent only a small fraction of the 10,000 plus categories currently found at major online-auction sites. However, the target categories chosen encompassed products offered at a variety of prices and were found in a variety of different high-level category groups. The selected target categories contained groups of substantially similar items, which facilitated analysis. Additionally, several of the product categories used in the simulation have been studied by other researchers, including PCs [47], disk drives and scanners [34], beanie babies and other doll collectables [3,21], and philately [25], which will facilitate future cross-research comparisons allowing more detailed examinations of these select categories.

For each of these products, the IR agent gathered recently closed auctions from eBay, Amazon, and Yahoo to get the most current auction data and bid histories. Based on this data, the Auction Advisor made maximum bid recommendations to buyers. The agent also recommended a minimum listing price, a reserve price and an auction duration to potential sellers. The recommendations made by the Auction Advisor are summarized in Table 2.

## 4.2.1. Online-auction buyer-side results

The Auction Advisor buyer recommendations consisted of a maximum bid price as well as a list of current auctions that had current prices (including minimum opening bids on auctions with no bids yet) that were less than the suggested bid amount at the time the agent was run. For the purposes of this simulation, the suggested bid price was set equal to the median bid price received on auctions of similar items during the 2 months immediately preceding the study. Of the 374 target products for sale during the simulation period, Auction Advisor found 183 auctions covering 15 different products on which the buyer could bid. The Auction Advisor recommendations were successful for 14 out of the 15 products evaluated. Winning buyers were able to purchase at least one of each of these 14 products at or below the suggested bid price. Additionally, the suggested bid price was at or below the median price paid by other buyers of substantially similar products for 77.6% of the 183 auctions monitored during the simulation.

Table 2  
Auction Advisor (AA) recommendations to buyers and sellers

<table><tr><td rowspan="2">Product</td><td colspan="3">Buyers</td><td colspan="4">Sellers</td></tr><tr><td>AA recommend maximum bid (US$)</td><td># Auctions w/ start prices# Simulated AA auction winsAA recommend min. start price (US$)% Auctions with reserveRecommend reserve price (US$)% Auctions above AA recommended reserve/min</td><td># Simulated AA auction wins</td><td>AA recommend min. start price (US$)</td><td>% Auctions with reserve</td><td>Recommend reserve price (US$)</td><td>% Auctions above AA recommended reserve/min</td></tr><tr><td>PC celeron 1.7 Ghz</td><td>234.00</td><td>4</td><td>4</td><td>44.00</td><td>16</td><td>204.00</td><td>100.0</td></tr><tr><td>NEC 17-in. flat screen monitor</td><td>473.00</td><td>4</td><td>0</td><td>96.00</td><td>0</td><td>N/A</td><td>100.0</td></tr><tr><td>DVD drive 12x</td><td>42.00</td><td>16</td><td>15</td><td>24.00</td><td>10</td><td>30.00</td><td>37.5</td></tr><tr><td>Compaq iPaq 3835</td><td>385.00</td><td>12</td><td>6</td><td>290.00</td><td>20</td><td>337.00</td><td>88.2</td></tr><tr><td>Olympus C3020 Digital Camera</td><td>353.00</td><td>7</td><td>5</td><td>250.00</td><td>23</td><td>301.00</td><td>100.0</td></tr><tr><td>Enya, A day w/o rain CD</td><td>7.00</td><td>17</td><td>9</td><td>4.00</td><td>0</td><td>N/A</td><td>98.3</td></tr><tr><td>Training day DVD</td><td>10.00</td><td>15</td><td>8</td><td>9.00</td><td>0</td><td>N/A</td><td>83.3</td></tr><tr><td>C4 (new VF) stamp</td><td>15.00</td><td>29</td><td>29</td><td>10.00</td><td>7</td><td>N/A</td><td>48.6</td></tr><tr><td>C6 (new VF) stamp</td><td>40.00</td><td>29</td><td>29</td><td>19.00</td><td>7</td><td>N/A</td><td>76.5</td></tr><tr><td>Earnhart Coke bottle</td><td>4.00</td><td>15</td><td>11</td><td>4.00</td><td>3</td><td>N/A</td><td>70.0</td></tr><tr><td>Starbucks coffee (1 lb.)</td><td>6.00</td><td>7</td><td>5</td><td>5.00</td><td>0</td><td>N/A</td><td>40.0</td></tr><tr><td>DeWalt 7 1/4 circular saw</td><td>72.00</td><td>9</td><td>6</td><td>28.00</td><td>0</td><td>N/A</td><td>100.0</td></tr><tr><td>Red Door perfume (3.3 oz)</td><td>24.00</td><td>5</td><td>4</td><td>18.00</td><td>0</td><td>N/A</td><td>100.0</td></tr><tr><td>Oakley straight jacket sunglasses</td><td>78.00</td><td>8</td><td>6</td><td>51.00</td><td>50</td><td>59.00</td><td>90.9</td></tr><tr><td>Seiko tit. perpetual calendar watch</td><td>131.00</td><td>6</td><td>5</td><td>39.00</td><td>10</td><td>106.00</td><td>33.3</td></tr></table>

However, the NEC 17-in. flat screen monitor had no auction that could have been won at the suggested bid price. The Auction Advisor suggested bid price was established based on sales at all auction sites, which includes a set of sales from Yahoo that sold at a much lower price than the other sites. When the simulated buyer was using the Auction Advisor system, there were no NEC 17-in. flat screen monitors available at Yahoo, and thus, the suggested bid price was much lower than the average price for non-Yahoo sites. One design improvement that could be made to the Auction Advisor would be for it to detect when the current conditions are different than those used to make predictions (e.g., no monitors available at Yahoo) and to adjust its recommendations accordingly. In this case, if the Yahoo NEC 17-in. flat screen monitors auctions are excluded from the recommendation calculation, the new recommended bid price would have been US\$522.77. This bid recommendation would allow a buyer to win 50% of the NEC 17- in. flat screen monitors at eBay.

An example of the Auction Advisor buyer recommendations for one product is displayed in Table 3. The Auction Advisor recommends that the buyer pay no more than US\$353 for an Olympus C3020 Digital Camera. At the time the agent was run, there were 30 open auctions for new Olympus C3020 Digital Cameras at the 4 different auction sites. Of these 30 auctions, the Auction Advisor selected a set of 7 auctions, which had current prices below the recommended purchase price. The agent suggested a time at which the buyer would want to place the recommended bid of US\$353 for each of the 7 auctions.

Table 3 shows the auction-specific recommendations made by Auction Advisor for a user interested in purchasing a digital camera. The closing price for 5 of the 7 auctions was below the price recommended by Auction Advisor. The 23 other auctions running during the simulation time frame that all had current prices above the supported maximum bid of the Auction Advisor system increase the derived benefit from Auction Advisor further since the median price for these 30 auctions is clearly above the bid recommended by Auction Advisor.

A confounding effect that makes it difficult to determine if a buyer placing the suggested maximum bid at the recommended bid time would actually have won all of these auctions is that the recorded winning bid could have been a proxy bid that was below the winning bidder’s actual maximum bid price. However, in addition to using the Auction Advisor to locate all auctions currently below the recommended maximum bid, an auction buyer can use the bid manager to select several items to bid on during one browsing session, and then allow Auction Advisor to manage the bidding process, potentially placing several bids, until one of the bids wins. This can significantly increase the probability that a buyer using the Auction Advisor would eventually be successful in winning an auction at or below the suggested bid price.

Table 3  
Agent buyer recommendations for olympus digital camera

<table><tr><td>Auction site</td><td>Item #</td><td>Title</td><td>Current bid (US$)</td><td>Recommended bid (US$)</td><td>Winning bid (US$)</td></tr><tr><td>EBay</td><td>1373478459</td><td>BRAND NEW OLYMPUS C-3020 Digital Camera</td><td>200.00</td><td>353.00</td><td>330.00</td></tr><tr><td>EBay</td><td>1373487693</td><td>OLYMPUS C-3020 3.2 MP DIGITAL CAMERA+bonus*</td><td>311.00</td><td>353.00</td><td>311.00</td></tr><tr><td>EBay</td><td>1373964863</td><td>Olympus C-3020 Zoom Digital Camera NEW NR</td><td>315.00</td><td>353.00</td><td>340.00</td></tr><tr><td>EBay</td><td>1373504480</td><td>New Olympus C-3020 Digital Camera Kit C3020</td><td>280.97</td><td>353.00</td><td>355.01</td></tr><tr><td>EBay</td><td>1373123917</td><td>Olympus C-3020 New with Original Packing</td><td>255.00</td><td>353.00</td><td>315.00</td></tr><tr><td>EBay</td><td>1374255590</td><td>Olympus C-3020 Digital Camera New NO Reserve</td><td>9.99</td><td>353.00</td><td>350.01</td></tr><tr><td>EBay</td><td>1373876145</td><td>NEW IN BOX Olympus C-3020 ZOOM Digital Camera</td><td>153.50</td><td>353.00</td><td>360.00</td></tr></table>

## 4.2.2. Online-auction seller-side results

The Auction Advisor seller recommendations consisted of a minimum price at which to list the items and a reserve price to use if appropriate. For the purposes of this simulation, the suggested minimum price was set equal to the median minimum price, and the suggested reserve price was set equal to the 70% of the average maximum bid received on auctions of similar items during the 2 months immediately preceding the study. The purpose of a reserve price is to permit the seller to withdraw the auction item from sale if a minimum desired price has not been bid. This minimum desired price is the seller’s valuation (value) of the product. Unfortunately, the presence of reserve prices may also serve to drive away interested bidders [27]. Furthermore, two conditions eliminate any contribution to a seller’s net value from a reserve price. These conditions are: if the seller has attached a valuation of zero to the product (likely in many categories due to the nature of online auctions for eliminating excess inventory), and interdependence of bidder valuations exists (more likely given the quantity of auctions conducted online and the availability of IR agents, such as Auction Advisor) [27]. Reserve prices frequently only serve to prevent sellers from selling their auction items and are best not used in many product categories [12]. Therefore, a reserve price is only suggested if there is a large enough gap between the recommended minimum bid and the median closing bid for previous auctions and if at least 10% of auctions in the previous 2 months have set a reserve price, thus indicating the acceptance of reserve pricing strategies for a particular product.

Of the 15 items investigated as a part of this study, 82.3% of the products sold for prices higher than the suggested reserve price or opening bid price when a reserve price is not recommended (see Table 2), thus satisfying the seller-side evaluation criteria. This indicates that if the seller had set the recommended opening bid or reserve price, the seller would be likely to sell their item the first time they listed it. However, if the proposed reserve prices were set, all the auctions would not have resulted in a sale. In 17.7% of the auctions, the products sold at a price below the recommended reserve price and thus would not have been sold. In one auction at Amazon, a <sup>b</sup>Brand NEW COMPAQ IPAQ 3835<sup>Q</sup> had a minimum bid of US\$1.00, and no reserve price set. It received two bids and sold for US\$1.25, 99.68% below its average selling price of US\$385. If the sellers had set a reserve price in this auction, they would have had the opportunity to relist their product and get a more market competitive price. One way to improve the reserve price recommendation would be to allow the auction seller to specify the amount of time they are willing to wait to sell their product. The Auction Advisor could then recommend a reserve price that would provide a high probability of sale within the specified sales window.

The evaluation of current online auctions indicates that pricing and bidding strategies employed by auction participants are often not the ones that produce the best outcome. This research indicates that using the Auction Advisor system to retrieve recent price and sales histories along with validated recommendations can improve the pricing and bidding decisions of both auction buyers and auction sellers. As demonstrated in the simulation, the Auction Advisor finds all auctions regardless of online-auction service provider and the suggested maximum bid is capable of winning over 38% of the current auctions for the products for sale during the simulation at or below the recommended price. Similarly, the selling strategies supported by the Auction Advisor system resulted in over 82% first offering sales and with closing prices at or above the reserve price when applicable. Finally, the bidding and selling decision support provided by the Auction Advisor is based on a rolling 2-month window so that the most recent trends in bidding and selling are captured and utilized to guide the auction participant.

## 4.3. Additional empirical research results

Following the simulation study to evaluate the potential merit of the Auction Advisor system’s online-auction decision support, a small pilot experiment is performed using 20 research subjects making real purchases at online auctions to evaluate the buyer-side recommendations. The research population consisted mostly of students (85%) who were paid for their participation in the research experiment. The population was 60% female and 40% male with ages ranging from 18 to 65 for both genders and included undergraduate (40%), graduate (45%), and nonstudents (15%).

The research subjects are all tasked to purchase at an online auction both an external USB Zip-disk drive and a popular DVD movie. Research subjects participated in online auctions occurring between April 2003 and August 2003. They were spaced approximately 7 days apart so as not to artificially increase the net price paid through competition with each other. Participants were asked to bid in auctions until they had won one of each item or until a 2-week time period had elapsed to better correlate with the simulation study’s time frame.

One-half of the subjects used the Auction Advisor online-auction decision support system and the other half did not use any automation tools. Those research subjects that used the Auction Advisor online-auction decision support system were not given any prior instruction on how to use the system, which may bias the total time required to complete the auctions as a small up-front learning curve is expected whenever using a new system with the duration of the learning curve affected by an individual’s computer selfefficacy [1].

At the end of the experiment, quantitative results, including the prices paid, number of auctions participated in, and time to complete the experiment, were gathered for all subjects. Qualitative results regarding user’s perceptions of the Auction Advisor system were also gathered for those subjects that used the Auction Advisor system during the experiment.

Any benefit in reducing the prices paid between the Auction Advisor system users and the nonusers for the internal Zip-drive is difficult to measure, since the research subjects purchased parallel, USB, one SCSI, and one internal drive. These four types of drives have different price medians and means in the onlineauction market. Comparing USB external Zip-drive purchases, the subjects using the Auction Advisor system paid an average of US\$2 less than the other experimental subjects. However, the results were not as favorable for the parallel Zip-drive purchases. One explaining factor for this is that one of the research subjects that was using the Auction Advisor system ignored the system’s ability to automatically place bids and manually entered bids that exceeded the Auction Advisor’s maximum bid recommendation.

While the research subjects were given the option of purchasing any one of three DVD movie titles, the median and mean prices for these three DVD movie titles was nearly identical at the time of the experiment. The two lowest prices paid for a DVD and shipping were both achieved by Auction Advisor users. In fact, 80% of the five lowest prices paid were achieved using the Auction Advisor system. One further benefit was observed from the experiment’s results, which was that almost all successful auction purchases were made at eBay, since eBay is the largest online-auction service provider [19], but the fifth lowest purchase price was paid for an online auction at Yahoo by an Auction Advisor user.

The time needed to complete the experiment ranged from 12 min to over 9 h with an average of 3 h and 51 min, where time is measured as the amount of time spent at the computer trying to accomplish the goals of the experiment. Subjects using the Auction Advisor took an average of 1 h and 47 min longer to complete the experiment than did subjects that did not use the system. This is likely because the Auction Advisor decision support system users required time to learn how to use Auction Advisor.

An examination of Auction Advisor decision support system users’ bidding patterns indicated that 100% of the users used the timed bidding feature at least one time. However, of the 80% of users that tried to use the multi-item bidding feature, only half were able to use it correctly. The subjects that used multiple-item bidding correctly were able to complete the experiment in less than half the time when compared to the subjects that did not use it correctly. In addition, subjects who used multiple-item bidding correctly were also able to complete the experiment in slightly less time than users that did not use the system. In fact, two out of three of the participants that completed the experiment in 1 h or less were users of the Auction Advisor system. The next closest subject’s time that did not use the Auction Advisor system required an additional 35 min, a 58% increase in the time needed to purchase the two items. This shows that, in a practical setting and taking into account up front learning time for using Auction

Advisor, the automated online-auction search and IR can produce significant timesavings.

Qualitative data obtained from the Auction Advisor system users indicate that in addition to actual savings for the DVD movies and the USB external Zip-drives, users perceived benefit from the recommendations made by Auction Advisor. First, 60% of the users found the Auction Advisor system easy to use, with the remaining 40% finding it of average difficulty. The maximum price recommendations were perceived to be helpful by 100% of the users for buying a Zip-drive and 90% of the users for purchasing a DVD at auction and in both cases 70% of the users found the bid timing recommendations to be very beneficial, with an additional 10–20% (Zip-drive versus DVD) finding the bid timing recommendation somewhat beneficial. Finally, only 10% of the users did not perceive any cost savings from the Auction Advisor system for both products and an additional 10% did not perceive cost savings for one or the other product. The 80% that perceived cost savings coming from the bid recommendations of Auction Advisor indicated an average perceived savings of just over US\$17 on the Zip-drive and an average perceived savings of US\$5 on the DVD movie.

The follow-up experiment using real people placing actual bids at online auctions for two different products further demonstrates the measurable benefit of an agent-based online-auction decision support system. First, the automatic IR of current auction knowledge and available auctions provides knowledge of current auctions from multiple sites and presents current price medians. While cost savings for bidders was inconclusive for the Zip-drive, the DVD movie purchases demonstrated that Auction Advisor provides real cost savings. The IR and the automatic bidding features of Auction Advisor can save users time in researching and searching current auctions. However, additional work is required to determine how best to train new users to use the automated bidding features. Future research efforts will investigate the incorporation of automated help including intelligent tool tips and a tutorial to decrease user-learning time.

## 5. Auction rule development

The evaluation of the Auction Advisor system indicates that even simple rules based on current and accurate online-auction knowledge can improve the likelihood that auction participants will have better than average outcomes. Online auctions are a dynamic environment and even small changes in auction conditions (like the lack of NEC monitors available at Yahoo) can change the appropriate price that should be bid or set at any given time. The auction rule development portion of this research involves developing rules that can be used to improve the recommendations made to auction participants. The Auction Advisor system uses these rules in conjunction with recent auction data to codify and automate portions of the auction decisionmaking process.

## 5.1. Buyer rule development

Auction participants need to make a number of key decisions that can influence their auction outcomes. Buyers need to establish what the value of an auction item is given the current auction market conditions. Auction research has identified several factors that influence final auction price [5,4,21,26]. These include the average price similar items have sold for in the recent past, the availability of a specific item, and the bid increment. Buyers are also interested in the number of bidders participating in current auctions for a given item. This provides a good measure of the level of competition for a specific item (and thus, final bid price) [41].

Literature related to both traditional and online auctions is evaluated to help develop preliminary rules that may be used to improve buyer decision making. Initially, a set of three rules likely to produce a favorable outcome for buyers is developed. The three proposed buyer heuristics are:

(1) Bids need not exceed the recent median sales price on recently closed auctions: Recommended<sup>\_</sup> maximum<sup>\_</sup>bid=Median<sup>\_</sup>closed<sup>\_</sup>price;

(2) Median selling price increases as the number of bids/bidders increases [49]: Recommended<sup>\_</sup> maximum<sup>\_</sup>bid=Recommended<sup>\_</sup>maximum<sup>\_</sup> bid \* Num<sup>\_</sup>bidders<sup>\_</sup>factor;

(3) Bidders should place bids towards the end of the auction duration [4]: Recommended<sup>\_</sup>bid<sup>\_</sup> time=Close<sup>\_</sup>time—5 minutes;

Once preliminary rules are identified, they are validated using auction data from online-auction sites. To accomplish this, the information retrieval agent is used to mine auction data available from three auction sites (eBay, Yahoo, and Amazon). The information retrieval agent gathers publicly available data on individual auctions, including the item description and the bid history. The data is collected for online auctions ending during a single month for seven prespecified product categories. As with the simulation study described in the previous section, the seven product categories used in the heuristic generation portion of this research are only a small fraction of the possible categories available, but the categories are chosen to provide a breadth of available categories and to also correlate with previous research into these specific online-auction markets [3,21,25,34,47]. The target categories are Intel Celeron Desktop Computers, DVD Drives, Business Database Software, Fax Machines, New Age Compact Discs, U.S. Airmail Stamps, and Teeny Beanie Babies. Information on more than 10,000 auction items is gathered from the three auction sites.

In order to examine the applicability of our identified rules to online auctions, 30 specific products are selected for in-depth analysis. The average starting price, minimum sales price, average sales price, and maximum sales price are examined to determine if the general rules developed from the literature hold true for the sample data set. Table 4 compares prices for sold and unsold items for each of the 30 products examined.

Table 4  
Agent mined information sold versus unsold products

<table><tr><td rowspan="2">Category</td><td rowspan="2">Product</td><td colspan="6">Auctions resulting in a sale</td><td colspan="3">Auctions w/o sale</td></tr><tr><td>Average starting price (US$)</td><td>Minimum sales price (US$)</td><td>Average sales price (US$)</td><td>Maximum sales price (US$)</td><td># Sold</td><td>Average duration</td><td>Average starting price (US$)</td><td># Unsold</td><td>Average duration</td></tr><tr><td>US airmail</td><td>C1 (New VF)</td><td>14.55</td><td>15.50</td><td>47.66</td><td>133.50</td><td>9</td><td>8.00</td><td>49.00</td><td>9</td><td>6.88</td></tr><tr><td>US airmail</td><td>C2 (New VF)</td><td>17.54</td><td>18.00</td><td>40.09</td><td>66.00</td><td>11</td><td>9.00</td><td>53.35</td><td>10</td><td>7.38</td></tr><tr><td>US airmail</td><td>C3 (New VF)</td><td>16.48</td><td>13.01</td><td>44.81</td><td>142.50</td><td>14</td><td>8.62</td><td>57.99</td><td>9</td><td>6.86</td></tr><tr><td>US airmail</td><td>C4 (New VF)</td><td>7.09</td><td>2.25</td><td>15.68</td><td>39.95</td><td>15</td><td>8.14</td><td>8.50</td><td>3</td><td>6.33</td></tr><tr><td>US airmail</td><td>C5 (New VF)</td><td>15.77</td><td>15.00</td><td>33.12</td><td>62.00</td><td>16</td><td>7.93</td><td>63.34</td><td>18</td><td>5.91</td></tr><tr><td>US airmail</td><td>C6 (New VF)</td><td>12.79</td><td>15.30</td><td>42.21</td><td>107.50</td><td>16</td><td>8.48</td><td>67.33</td><td>16</td><td>7.85</td></tr><tr><td>New age CD</td><td>Brian Eno</td><td>4.74</td><td>6.99</td><td>11.35</td><td>22.83</td><td>5</td><td>7.60</td><td>4.50</td><td>3</td><td>7.00</td></tr><tr><td>New age CD</td><td>Enya, Day w/o rain</td><td>3.35</td><td>3.00</td><td>8.01</td><td>16.00</td><td>35</td><td>5.94</td><td>11.21</td><td>14</td><td>6.92</td></tr><tr><td>New age CD</td><td>George Winston</td><td>7.57</td><td>3.25</td><td>9.57</td><td>15.79</td><td>8</td><td>7.38</td><td>-</td><td>0</td><td></td></tr><tr><td>New age CD</td><td>Kitaro</td><td>5.00</td><td>2.25</td><td>6.99</td><td>14.99</td><td>16</td><td>6.78</td><td>8.28</td><td>7</td><td>6.43</td></tr><tr><td>New age CD</td><td>Sarah McLachlan</td><td>2.49</td><td>1.99</td><td>2.49</td><td>2.99</td><td>2</td><td>7.00</td><td>-</td><td>0</td><td></td></tr><tr><td>New age CD</td><td>Tangerine Dream</td><td>6.85</td><td>4.75</td><td>8.66</td><td>17.49</td><td>15</td><td>6.76</td><td>6.66</td><td>6</td><td>7.18</td></tr><tr><td>New age CD</td><td>Yanni</td><td>5.00</td><td>1.99</td><td>6.26</td><td>17.09</td><td>28</td><td>6.52</td><td>8.91</td><td>32</td><td>4.50</td></tr><tr><td>PC celeron</td><td>400–500 Mhz</td><td>65.31</td><td>52.00</td><td>122.58</td><td>249.99</td><td>35</td><td>5.02</td><td>219.56</td><td>7</td><td>5.67</td></tr><tr><td>PC celeron</td><td>633 Mhz</td><td>124.87</td><td>160.00</td><td>250.88</td><td>355.00</td><td>8</td><td>5.00</td><td>283.20</td><td>5</td><td>5.00</td></tr><tr><td>PC celeron</td><td>766 Mhz</td><td>122.58</td><td>152.50</td><td>213.11</td><td>359.00</td><td>12</td><td>5.99</td><td>317.75</td><td>4</td><td>7.20</td></tr><tr><td>PC celeron</td><td>1 Ghz</td><td>117.66</td><td>102.50</td><td>240.86</td><td>445.00</td><td>21</td><td>5.25</td><td>403.13</td><td>14</td><td>6.33</td></tr><tr><td>PC celeron</td><td>1.2 Ghz</td><td>450.00</td><td>480.00</td><td>480.00</td><td>480.00</td><td>1</td><td>3.00</td><td>561.40</td><td>5</td><td>4.97</td></tr><tr><td>DVD drive</td><td>12x</td><td>21.01</td><td>9.99</td><td>50.57</td><td>125.00</td><td>49</td><td>5.72</td><td>52.64</td><td>31</td><td>6.42</td></tr><tr><td>DVD drive</td><td>16x</td><td>27.56</td><td>39.00</td><td>53.21</td><td>66.50</td><td>14</td><td>5.00</td><td>65.59</td><td>9</td><td>4.67</td></tr><tr><td>Fax</td><td>Panasonic KX-FP151</td><td>12.08</td><td>21.51</td><td>57.39</td><td>87.25</td><td>13</td><td>7.00</td><td>45.00</td><td>1</td><td>5.00</td></tr><tr><td>Fax</td><td>Canon 8500</td><td>28.00</td><td>56.00</td><td>61.47</td><td>65.92</td><td>3</td><td>6.00</td><td>90.00</td><td>4</td><td>3.00</td></tr><tr><td>Fax</td><td>Canon 9000</td><td>140.00</td><td>152.50</td><td>455.83</td><td>725.00</td><td>3</td><td>7.00</td><td>380.00</td><td>5</td><td>2.20</td></tr><tr><td>Fax</td><td>Brother IntelliFAX 770</td><td>219.00</td><td>411.65</td><td>461.33</td><td>511.00</td><td>2</td><td>7.00</td><td>687.50</td><td>5</td><td>7.00</td></tr><tr><td>Teanie Beanie</td><td>Nanook</td><td>0.99</td><td>0.99</td><td>1.50</td><td>2.00</td><td>2</td><td>7.00</td><td>0.99</td><td>7</td><td>4.86</td></tr><tr><td>Teanie Beanie</td><td>Chocolate</td><td>2.00</td><td>5.50</td><td>7.00</td><td>8.50</td><td>2</td><td>7.00</td><td>13.22</td><td>14</td><td>3.31</td></tr><tr><td>Teanie Beanie</td><td>Pinky</td><td>4.50</td><td>5.00</td><td>8.56</td><td>10.72</td><td>4</td><td>7.33</td><td>35.00</td><td>10</td><td>3.00</td></tr><tr><td>Teanie Beanie</td><td>Liberty</td><td>2.00</td><td>3.24</td><td>6.37</td><td>9.50</td><td>2</td><td>7.00</td><td>-</td><td>0</td><td></td></tr><tr><td>Teanie Beanie</td><td>Lucky</td><td>1.16</td><td>0.99</td><td>1.41</td><td>1.99</td><td>3</td><td>3.33</td><td>1.86</td><td>18</td><td>3.00</td></tr></table>

The data in Table 4 indicate that some onlineauction buyers do pay substantially more than the average price found on similar auctions. On average, the maximum price paid for an item was 79% higher than the average price paid, and 368% higher than the minimum price paid. While there is some variability in prices for items like stamps, even products that are more similar had maximum prices 63% higher than the average prices. This indicates that many buyers are unaware of the appropriate price for the products they are purchasing online and would benefit from an agent that helps them determine the amount to bid based on current auction data.

The number of bidders participating in an auction also has an impact on the final sales price [41]. To evaluate this potential rule, the data for the 30 products was divided in half and the average selling price for those auctions that had more bidders was compared to the average selling price for those auctions with fewer bidders. Auctions with differing numbers of bidders occurred for 28 of the 30 products. Auctions with more bidders resulted in a higher average selling price than auctions with fewer bidders for 19 of the 28 products examined. Auctions with more bidders on average resulted in sales prices 36.28% higher than those with fewer bidders. The results of these calculations are summarized in Table 5.

Buyers also need to time their bids appropriately. The online auctions studied had fixed (or nearly fixed) closing times. Data was gathered for 10,522 auctions, of which 3814 of the auctions received one or more bids. In 38% of these auctions, the winning bid was placed in the last hour of bidding and in 26% of the auctions the winning bid was a new bid placed in the last 5 min of the auction. This is consistent with other online-auction research that has studied the problem of last-minute bidding [32,40,44]. The advantage of bidding late in online auctions is threefold. First, it is difficult for other bidders to respond to a bid that is placed in the last few minutes of an auction. In addition, bidding late in the auction cycle allows buyers to be committed to purchase an item for a shorter amount of time. They immediately know whether or not their bid was successful and can make future bidding/purchase decisions based on this knowledge. Finally, the fixed closing time is peculiar to online auctions and changes the way in which the auction marketplace works [19]. Late bidding, when followed as a common online-auction strategy, can significantly reduce the final closing price to be paid by a bidder (through the reduction of competition).

Table 5  
Agent mined information more bidders vs. fewer bidders

<table><tr><td rowspan="2">Category</td><td rowspan="2">Product</td><td colspan="2">More bids</td><td colspan="2">Fewer bids</td><td rowspan="2">More vs. few bids (%)</td></tr><tr><td>Average starting price (US$)</td><td>Average sales price (US$)</td><td>Average starting price (US$)</td><td>Average sales price (US$)</td></tr><tr><td>US airmail</td><td>C1 (New VF)</td><td>18.74</td><td>84.04</td><td>14.55</td><td>47.66</td><td>76</td></tr><tr><td>US airmail</td><td>C2 (New VF)</td><td>8.50</td><td>47.00</td><td>32.99</td><td>33.24</td><td>41</td></tr><tr><td>US airmail</td><td>C3 (New VF)</td><td>6.83</td><td>47.68</td><td>26.12</td><td>41.94</td><td>14</td></tr><tr><td>US airmail</td><td>C4 (New VF)</td><td>6.57</td><td>22.01</td><td>7.21</td><td>9.30</td><td>137</td></tr><tr><td>US airmail</td><td>C5 (New VF)</td><td>12.36</td><td>37.01</td><td>19.19</td><td>29.23</td><td>27</td></tr><tr><td>US airmail</td><td>C6 (New VF)</td><td>6.75</td><td>50.40</td><td>18.84</td><td>34.02</td><td>48</td></tr><tr><td>New age</td><td>Brian Eno</td><td>2.99</td><td>15.69</td><td>6.50</td><td>7.01</td><td>124</td></tr><tr><td>New age</td><td>Enya, A day w/o rain</td><td>1.60</td><td>7.55</td><td>7.34</td><td>8.41</td><td>-10</td></tr><tr><td>New age</td><td>George Winston</td><td>3.50</td><td>7.51</td><td>11.64</td><td>11.64</td><td>-36</td></tr><tr><td>New age</td><td>Kitaro</td><td>3.87</td><td>7.22</td><td>6.12</td><td>6.75</td><td>7</td></tr><tr><td>New age</td><td>Tangerine Dream</td><td>3.12</td><td>7.99</td><td>9.71</td><td>9.71</td><td>-18</td></tr><tr><td>New age</td><td>Yanni</td><td>3.40</td><td>5.93</td><td>7.17</td><td>7.17</td><td>-17</td></tr><tr><td>PC celeron</td><td>400–500 Mhz</td><td>16.28</td><td>113.83</td><td>115.11</td><td>131.99</td><td>-14</td></tr><tr><td>PC celeron</td><td>633 Mhz</td><td>28.00</td><td>227.88</td><td>221.75</td><td>273.88</td><td>-17</td></tr><tr><td>PC celeron</td><td>766 Mhz</td><td>110.17</td><td>242.24</td><td>135.00</td><td>183.98</td><td>32</td></tr><tr><td>PC celeron</td><td>1 Ghz</td><td>42.80</td><td>275.11</td><td>173.39</td><td>195.30</td><td>41</td></tr><tr><td>DVD drive</td><td>12x</td><td>4.65</td><td>53.18</td><td>38.26</td><td>47.77</td><td>11</td></tr><tr><td>DVD drive</td><td>16x</td><td>10.99</td><td>53.43</td><td>43.13</td><td>55.00</td><td>-3</td></tr><tr><td>Fax</td><td>Panasonic KX-FP151</td><td>7.00</td><td>69.47</td><td>18.33</td><td>50.64</td><td>37</td></tr><tr><td>Fax</td><td>Canon 8500</td><td>1.00</td><td>56.00</td><td>41.50</td><td>63.21</td><td>-13</td></tr><tr><td>Fax</td><td>Canon 9000</td><td>10.00</td><td>725.00</td><td>205.00</td><td>321.25</td><td>126</td></tr><tr><td>Fax</td><td>Brother IntelliFAX 770</td><td>219.00</td><td>511.00</td><td>219.00</td><td>411.65</td><td>24</td></tr><tr><td>Teanie Beanie</td><td>Nanook</td><td>0.99</td><td>2.00</td><td>0.99</td><td>0.99</td><td>102</td></tr><tr><td>Teanie Beanie</td><td>Chocolate</td><td>1.00</td><td>8.50</td><td>2.99</td><td>5.50</td><td>55</td></tr><tr><td>Teanie Beanie</td><td>Pinky</td><td>1.50</td><td>9.61</td><td>7.50</td><td>7.50</td><td>28</td></tr><tr><td>Teanie Beanie</td><td>Liberty</td><td>1.00</td><td>9.50</td><td>2.99</td><td>3.24</td><td>193</td></tr><tr><td>Teanie Beanie</td><td>Lucky</td><td>0.50</td><td>1.25</td><td>1.49</td><td>1.49</td><td>-16</td></tr></table>

## 5.2. Seller rule development

Auction sellers need to make decisions that will maximize the bids they receive on the items they sell at auction [16]. Sellers need to decide what auction site to list their item at, when best to list their item, how much to list their item for, and how long their auction should last. Research also indicates that sellers could benefit from knowing the number of unsuccessful bidders in recent past to help identify latent demand for a given product [23]. Additionally, many onlineauction services provide special features that enable a seller to promote or advertise their item for an additional cost and sellers must decide when onlineauction market conditions make these special features cost effective. Based on the available auction research, the following initial seller heuristics are proposed:

(1) The minimum bid price should be at or below the median minimum bid price for recent auctions that received bids: Recommended<sup>\_</sup>minimum<sup>\_</sup> price <sup>b</sup>= Median<sup>\_</sup>minimum<sup>\_</sup>price;

(2) If the median closing price is significantly higher than the median minimum price and if reserve prices are set for 10% or more of current auctions in the product category, a reserve price should be set to avoid selling significantly below market value: if (Median<sup>\_</sup>close<sup>\_</sup>price <sup>N</sup> (2 \* Median<sup>\_</sup> minimum<sup>\_</sup>price)) Recommended<sup>\_</sup> reserve<sup>\_</sup>price=discount<sup>\_</sup>factor \* Median<sup>\_</sup>close<sup>\_</sup>price;

(3) Auction durations should be kept short, since research indicates that longer onlineauction durations do not result in increased revenues for the seller [4,21]: Recommended<sup>\_</sup> duration <sup>b</sup>= Median<sup>\_</sup>duration;

Sellers are interested in maximizing their revenue for a given auction while having a high probability that the item will sell. One way to improve the auction outcome for the seller is by setting an appropriate minimum bid price. Table 4 shows the average starting bid level for both items that received bids and items that did not. Almost 84%, 25 out of the 30 products, have the average starting price for the unsold items higher than the average starting price for the items that sold. The average starting price for 19 of the unsold items is higher than the average sale price for similar items that sold during the same period. Additionally, six of the unsold products have an average starting price of the unsold items higher than the maximum selling price any similar product sold for during that month. This indicates that many sellers have unrealistic expectations when setting the prices for their auction items and could use the assistance of an auction advisor to help in setting prices. Table 4 also indicates that a higher than average starting price may be responsible for reducing the bidding activity (competition) for the product.

Reducing the initial bid price does present a risk to auction sellers. It makes it possible for their auction item to be sold at an unreasonably low price. One way a seller can reduce this risk is to set a reasonable reserve price. Many online-auction sellers set a low minimum price to stimulate interest in the auction and then set a higher reserve price to ensure that their item does not sell below a minimum acceptable price [44]. The data obtained during this phase of the research supports this practice. It indicates that more active auctions are likely to receive higher final bids (Table 5). It also indicates that failure to set an appropriate reserve price can result in substantially lower revenues for sellers. In Table 4, the average selling price is (on average) 33% higher than the minimum selling price. Setting a reserve price between the minimum and average sales prices would help minimize the risk of selling at too low of a price. However, the presence of a reserve price also serves to discourage bidders from entering the auction, which consequently reduces an auction’s activity and may result in the inability to sell the item, especially when an unreasonably high reserve is set. As indicated in the previous section, the acceptance of reserve pricing by a bidder community can be approximated by observing the prevalence of items with reserve prices in an auction category and also the percentage of items with a reserve price that are sold.

Prior research has indicated that auction duration has little impact on revenues for the auctioneer [4,21]. However, the data gathered as a part of this study does not support the established literature. It indicates that, on average, auctions receiving bids lasted 1.65 days longer than those that did not receive bids. While this study is preliminary, it indicates that the effect of auction duration on online-auction outcomes needs to be studied further before any firm conclusions can be drawn. The value of slightly longer auction durations may be attributed to the virtual nature of the onlineauction community, where many bidders will have preferred times of day or even days of the week to evaluate and engage in auction activity. This requires the proposed seller heuristic #3 (above) to be modified, instead of setting short auction durations; it is a better practice to set auction durations near the median auction duration for those auctions that received bids.

Revised Seller Heuristic #3: Auctions durations should be kept near the median duration for those auctions that received bids: Recommended<sup>\_</sup>duration= Max(7,Median<sup>\_</sup>duration<sup>\_</sup>auctions<sup>\_</sup>with<sup>\_</sup> bids);

Once the general auction rules are validated using actual auction data, the rules are encoded in an XML document for use in the Auction Advisor system.

## 5.3. Rule encoding for use by auction advisor

One key feature of the Auction Advisor system is that the buyer and seller heuristics are written in Simple Rule Markup Language (SRML), which is an XML standard for describing forward-chaining rules [46]. Encoding the buyer and seller rule sets in SRML increases modularity and flexibility by allowing the auction recommendation rules to be easily updated (either manually or automatically). It also makes it possible for users using a stand-alone version of the Auction Advisor to easily define new rule sets as demanded for different product types.

A small example of the rules used for the Auction Advisor system is provided for determining the recommended maximum purchase price for an online-auction bidder. The complete SRML markup for the <sup>b</sup>ManyBiddersBidPrice<sup>Q</sup> rule is shown in Fig. 3. The initial price is set to be the median price for similar items from recent auctions. This price is then modified as the DA agent discovers other relevant information that impacts the expected price. In the condition portion of the rule, the current value for the recommended bid price is checked to determine if it is greater than 0 (indicating this is a buyer session and the initial bid price has been set to the median price). The rule also checks to see if the current number of bidders participating in all auctions for a particular product exceeds a maximum number of expected bidders calculated based on historic auction data for the same product. If both conditions are true, then the recommended bid price is increased by a predefined amount (currently 15%). The multiplier as a constant in the SRML rule may be changed at any time as new information mined with Auction Advisor’s information agent indicates price differentials for various product categories and quantities of bidders.

The DA agent produces its recommendation through data analysis of the volumes of auction data returned from the Web by the IR agents. Specific elements to be mined or calculated from the acquired data are dependent on the antecedents of the rules in the recommendation rule base. As new rules are added, with additional data values required for the antecedents, the data analysis and analysis function of the advisor agent can be modified to incorporate these new required data values. Future research with the Auction Advisor agent will examine the efficiency and practicality of automatically parsing the SRML rule base to determine required data values and automatically building a corpus of subagents that will retrieve or calculate each of the desired data values.

## 5.4. Data analysis to support online-auction research and ongoing rule development

In addition to providing accurate and current information and recommendations based on that information, the Auction Advisor agent system was developed to support research to better understand the dynamics of online auctions. This research is investigating the impact of product type, buyer and seller characteristics, and current market conditions on online-auction prices and on the satisfaction buyers report having with the products purchased. One of the benefits of this ongoing research is that it also supports the development of new rules to add to the Auction Advisor rule base.

```xml
The recommended bidPrice is initialized to the medianPrice for a 'buying' session. DA agent determines the number of items currently for sale, and the number of bidders bidding on each item.
-->
<ruleset name="demo">
    <rule name="ManyBiddersBidPrice">
    <conditionPart>
    <simpleCondition className="AuctionAgent" objectVariable="air">
    <binaryExp operator="gt">
    <field name="bidPrice" />
    <constant type="float" value="0.0" />
    </binaryExp>
    <binaryExp operator="gt">
    <field name="numBidders" />
    <variable name="BIDDERSMAX" />
    </binaryExp>
    </simpleCondition>
    </conditionPart>
    <actionPart>
    <modify>
    <variable name="air" />
    <assignment>
    <field name="bidPrice" />
    <naryExp operator="multiply">
    <field name="bidPrice" />
    <constant type="float" value="1.15" />
    </naryExp>
    </assignment>
    </modify>
    </actionPart>
</rule>
+ <rule name="FewBidersBidPrice">± <rule name="ManyItemsBidPrice">±
    <rule name="FewItemsBidPrice">± <rule name="NoSaleBidPrice">
</ruleset>
```  
Fig. 3. Section of recommendation rule base for setting buyer’s bid price.

Prior research has shown that <sup>b</sup>Black box<sup>Q</sup> data analysis is not safe because there is no way to know the proper analysis without outside information [29]. Therefore, for this research, each proposed heuristic is derived using the available data and a reasonable initial hypothesis. Some rules that are evaluated and tested include rules that adjust the recommended bid price based on the current number of auctions available to bid on, adjust the bid recommendation based on the feedback score and number of negative feedbacks received by the seller and adjusted the recommended bid time based on the amount of proxy bidding activity an item is receiving. An example of the data analysis research conducted to support the development of new rules for the auction rule base is demonstrated by examining the online-auction research hypothesis,

OAH<sub>1</sub>: Bids placed by proxy bidders tend to be higher than those placed by nonproxy bidders.

This research question was proposed based on user feedback and expert examination of the data retrieved. It does not mean to imply that proxy bidders win more auctions, but rather that they pay more on average for the auctions they do win than their nonproxy counterparts.

The Information agent (a generic type of buyer/ seller agent) uses the IR and DA agents to gather and calculate desired information values. In this example, the desired data values are: total number of auctions for the specified item or category, percentage of proxy bids, quantity of proxy wins, average price paid by the proxy bid winners, and average price paid by nonproxy bid winners. The data used for the data analysis are recent archival information for closed auctions (so that the outcome is known) and for the reported example comes from the auctions for all of the auction sites closing during a single week. On Yahoo, a proxy bid is explicitly identified; however, on eBay and Amazon, a proxy bid was inferred based on the bid time—if the bid time on a bid was before the bid time of a bid with a lower bid price, it can be inferred that the bid was placed by a proxy agent. A part of the Information agent report that addresses this question is shown in Fig. 4.

From Fig. 4, it may be seen that at least one piece of empirical data (for the database software item) supports the research hypothesis, with the proxy bidder paying more than US\$9.00 (over 100% higher) over the average winning bid by nonproxy bidders. Although this is only one piece of empirical evidence, the agents may be executed in real time to evaluate any number of online-auction items of interest. In less than 1 min, the Information agent evaluates 15 different items. The results presented in Table 6 indicate that, at least for the 98 closed auctions for 15 different auction items, online proxy bidders on average pay 20% (average of the product of the second and last columns) more than nonproxy bidders. All results are produced by using the inclusive AND search method for the term listed in the first column. The result of this research question would indicate that proxy bidders tend to set too high of a proxy limit and should exercise more care or be better informed regarding the product’s valuation. The Information agent also provides evidence that proxy overbidding is not universal and bears further scrutiny. The two products that had proxy wins that underbid the nonproxy bidders were both under US\$10. Additional evidence is needed to validate if this counter-indicator for proxy overbidding is restricted to products that sell for smaller amounts (under US\$10) or for specific types of product categories or if another explanation is required to modify the original research hypothesis.

Research questions regarding proxy bidding or bidding by one-time bidders and potential sniping or last-minute bidding may all be addressed with the existing IR, DA, and Information agents. Additional research questions may also be addressed with only minor modification to the Information and DA agents that will enable them to mine additional information from the collection of online-auction data.

The data analysis aspect of the Information agent to support online-auction research enables the development of new recommendation rules for the Auction Advisor Recommendation Rule base. Once a hypothesis is confirmed with sufficient empirical evidence, the research hypothesis is then translated into a corresponding rule using the <sup>b</sup>rule building tool<sup>Q</sup> of the Information agent. As an example, a new proxy bidding rule from empirical evidence gathered by the

![](/api/attachments/84AW74WQ/fulltext/images/4be53553dd58f2d5f93eda28858e499aba9a7fcaae7881f177489eecbd40ef7b.jpg)  
Fig. 4. Information only agent output (partial).

Table 6  
Agent mined information regarding proxy bids versus nonproxy bids

<table><tr><td>Item</td><td>Auctions</td><td>Proxy wins</td><td>Proxy price (US$)</td><td>Nonproxy price (US$)</td><td>Difference (%)</td></tr><tr><td>C1 (New F) Stamp</td><td>14</td><td>3</td><td>213.17</td><td>212.94</td><td>+0.6</td></tr><tr><td>C5 (New VF) Stamp</td><td>3</td><td>0</td><td>N/A</td><td>14.52</td><td>-</td></tr><tr><td>C5 (New F) Stamp</td><td>4</td><td>0</td><td>N/A</td><td>12.39</td><td>-</td></tr><tr><td>C5 (Used) Stamp</td><td>3</td><td>1</td><td>5.77</td><td>5.92</td><td>-2.5</td></tr><tr><td>C14 (New F NH) Stamp</td><td>2</td><td>1</td><td>355.00</td><td>330.00</td><td>+7.6</td></tr><tr><td>C15 (New F) Stamp</td><td>1</td><td>1</td><td>265.00</td><td>N/A</td><td>-</td></tr><tr><td>Enya, ... Moon CD</td><td>2</td><td>0</td><td>N/A</td><td>10.76</td><td>-</td></tr><tr><td>Enya, ... Rain CD</td><td>6</td><td>3</td><td>8.76</td><td>8.99</td><td>-2.6</td></tr><tr><td>Harp CD</td><td>18</td><td>5</td><td>38.50</td><td>33.10</td><td>+16.3</td></tr><tr><td>Database software</td><td>3</td><td>1</td><td>17.51</td><td>8.22</td><td>+113.0</td></tr><tr><td>DVD 16x</td><td>11</td><td>1</td><td>91.00</td><td>53.90</td><td>+68.8</td></tr><tr><td>DVD 8x</td><td>4</td><td>0</td><td>N/A</td><td>166.13</td><td>-</td></tr><tr><td>DVD 32x</td><td>2</td><td>1</td><td>34.50</td><td>32.00</td><td>+7.8</td></tr><tr><td>DVD RAM Burner</td><td>3</td><td>1</td><td>310.00</td><td>247.00</td><td>+25.5</td></tr><tr><td>DVD 4x</td><td>2</td><td>0</td><td>N/A</td><td>175.24</td><td>-</td></tr><tr><td>Fax—Brother</td><td>10</td><td>2</td><td>53.25</td><td>38.08</td><td>+39.8</td></tr><tr><td>Fax—Panasonic</td><td>10</td><td>2</td><td>64.02</td><td>61.44</td><td>+3.2</td></tr></table>

Auction Advisor agent system that multiple proxy bidders competing in a single auction tend to artificially increase the final auction selling price is shown in Fig. 5.

Once a rule is written to the SRML rule base, it can be immediately utilized and evaluated in the same manner as existing rules in the recommendation rule base. Creation of new rules for the Recommendation Rule Base enables the Auction Advisor agents to adapt to changing market dynamics, thus providing auction participants with relevant and applicable recommendations for optimizing outcomes.

```xml
<rule name="ProxyRule">
    <conditionPart>
    <simpleCondition className="AuctionAgent" objectVariable="air">
    <binaryExp operator="gt">
    <field name="bidPrice" />
    <constant type="float" value="0.0" />
    </binaryExp>
    <binaryExp operator="gt">
    <field name="numProxyBidders" />
    <constant type="int" value="1" />
    </binaryExp>
    </simpleCondition>
</conditionPart>
<actionPart>
<modify>
    <variable name="air" />
<assignment>
    <field name="recommendation" />
<naryExp operator="add">
    <field name="recommendation" />
    <constant type="string" value="Do not place proxy bid now\n" />
    </naryExp>
    </assignment>
</modify>
</actionPart>
</rule>
```  
Fig. 5. Section of recommendation rule base for proxy bidding rule.

## 6. Conclusions

The Auction Advisor Agent system can be used to provide price histories and other auction information support to educate auction participants. In the dynamic world of online auctions, the real value of an item is constantly changing; hence, there is a significant need for current data so that the appropriate current price (or valuation) can be determined. One of the benefits provided by the Auction Advisor system is that it continuously retrieves the most recent data available when performing data analysis and making recommendations to auction participants and researchers. A question for future research is the time duration of the Auction Advisor’s IR agents. While the amount of data available from online-auction service providers may be a constraining factor, price volatility or lack thereof may indicate that the time frame for Auction Advisor’s IR search be shortened from 2 months to perhaps 2 weeks or possible lengthened for scarce items that do not come up for auction often. Auction Advisor also allows users to search for any item of interest, not just an item the agent is preprogrammed to search for, and to search across multiple online-auction sites.

Buyers using the Auction Advisor know what a reasonable price for a given item is and can avoid paying too much. They can use the bidding agent to select several items to bid on and to time their bids to maximize their probability of winning a given item within a specified period of time. Sellers can use the statistical information to determine appropriate minimum and reserve prices for their auctions and whether or not the current time is a good time to start a particular auction. They can use the seller agent to help them develop appropriate titles and descriptions for their items. The availability of these information tools can help to even the playing field between experienced and newer auction participants. It can also reduce the occurrence of <sup>b</sup>winner’s curse<sup>Q</sup> (paying too much). As rules and data are added to the Auction Advisor system, it will be able to automatically find an item by description or category across multiple auction sites and actively monitor bids that maximize a user’s value (e.g., including cost, shipping, and feedback ratings).

Another advantage of the current Auction Advisor system is that it can assist end-users in identifying appropriate search terms to locate auctions of interest. This should help improve the accuracy of the recommendations made by the DA agent. Future enhancements to the Auction Advisor agent system will also implement a more generic search that will be able to find near-misses (for misspelled words), be able to use synonyms for searching via the use of an online thesaurus, and incorporate some additional natural language processing capabilities. Fortunately, the multitier agent architecture of the Auction Advisor agent system facilitates the incorporation (with encapsulation) of new search methods [44] as they become available without interfering with the remainder of the Auction Advisor agent system functionality.

While the current Auction Advisor agent system requires predefinition of the structure of the onlineauction HTML data, ongoing research is being conducted to allow the agent to automatically determine the structure of new online-auction sites. This would allow users to add new auction sites at will and eventually allow the agent system to obtain advice based on any auction site available on the Web. A parallel effort that will facilitate automated online site parsing is the production of a specialized XML markup language for online auctions.

Introducing agents into online auctions will fundamentally change the way these auctions operate and the outcomes for both buyers and sellers. As onlineauction buyers and sellers increase their use of intelligent agents to automate information gathering and consequently auction decisions, the outcome for both buyers and sellers will be improved. Agents can be used to optimally match buyers and sellers for specific products. With sufficient information, an optimal price can be determined to maximize the return for all auction participants.

The concepts developed for the Auction Advisor system are applicable to other e-commerce and Web analysis domains. This research demonstrates that agents with extensive domain knowledge can provide meaningful assistance to end-users trying to process the vast amount of data on the Web. As the Web evolves, it is likely that similar agents will be developed to support intelligent tracking in other ecommerce domains.

Data analysis e-commerce Web agents significantly improve on traditional Web search methods by incorporating statistical inference and decisionmaking logic. Utilization of these Auction Advisorlike agents will keep electronic sellers and consumers better informed of current market conditions and maximize the outcomes for both.

## References

[1] R. Agarwal, V. Sambamurthy, R.M. Stair, Research report: the evolving relationship between general and specific computer self-efficacy—an empirical assessment, Information Systems Research 11 (4) (2000 (December)) 418 – 430.

[2] P. Anthony, N.R. Jennings, Evolving bidding strategies for multiple auctions, 15th European Conference on Artificial Intelligence (ECAI). Lyon, France 2002 (July).

[3] P. Bajari, A. Hortacsu. Economic Insights from Internet Auctions: A Survey, National Bureau of Economic Research Working Paper 10076, available at <sup>b</sup>http://www.nber.org/ papers/w10076<sup>N</sup> (2003).

[4] R. Bapna, P. Goes, A. Gupta, Insights and analysis of online auctions, Communications of the ACM 44 (11) (2001 (Nov)) 42–50.

[5] R. Bapna, P. Goes, A. Gupta, Alok analysis and design of business-to-consumer online auctions, Management Science 49 (1) (2003 (Jan.)) 85 – 101.

[6] M. Benyoucef, H. Alj, M. Ve´zeau, R.F. Keller, Combined negotiations in e-commerce: concepts and architecture, Electronic Commerce Research 1 (3) (2001) 277 – 299.

[7] M. Bichler, J. Kalagnanam, K. Katircioglu, A.J. King, R.D. Lawrence, H.S. Lee, G.Y. Lin, Y. Lu, Applications of flexible pricing in business-to-business electronic commerce, IBM Systems Journal 41 (2) (2002) 287 – 302.

[8] J.P. Bigus, J. Bigus, Constructing Intelligent Agents Using Java, 2nd edition, Wiley, New York, 2001.

[9] W. Brenner, R. Zarnekow, H. Wittig, Intelligent Software Agents, Springer, Berlin, 1998.

[10] T. Bui, J. Lee, An agent-based framework for building decision support systems, Decision Support Systems 25 (3) (1999 (Apr.)) 225 – 237.

[11] D.G. Conway, G.J. Koehler, Interface agents: caveat mercator in electronic commerce, Decision Support Systems 27 (4) (2000 (Jan)) 355–366.

[12] S.R. Datz, Official Stamp Collector’s Bible, Crown Publishing, New York, 2003.

[13] L. Deveaux, C. Paraschiv, M. Latourrette, Bargaining on a web agent-based market: behavioral vs. optimizing agents, Electronic Commerce Research 1 (4) (2001) 371– 401.

[14] M. Dumas, L. Aldred, G. Governatori, A. ter Hofstede, N. Russell, A probabilistic approach to automated bidding in alternative auctions, 11th International Conference on the World Wide Web (WWW), ACM Press, Honolulu Hawaii, USA, 2002 (May).

[15] O. Etzioni, Moving up the information food chain: deploying softbots on the World Wide Web, Al Magazine 18 (2) (1997 (Summer)) 11 – 18.

[16] S. Feldman, Electronic marketplaces, IEEE Internet Computing (2000 (July/Aug.)) 93 – 95.

[17] M.T. Goodrich, R. Tamassia, Data Structures and Algorithms in Java, 2nd edition, Wiley, New York, 2001.

[18] A. Greenwald, P. Stone, Autonomous bidding agents in the trading agent competition, IEEE Internet Computing 5 (2) (2001) 52 – 60.

[19] D.G. Gregg, S. Walczak, E-commerce auction agents and online-auction dynamics, Electronic Markets 13 (2) (2003 (Summer)).

[20] R. Guttman, A. Moukas, P. Maes, Agents as mediators in electronic commerce, in: M. Klusch (Ed.), Intelligent Information Agents, Springer, Berlin, 1999.

[21] J. Hahn, The dynamics of mass online marketplaces: a case study of an online-auction, Proc. of the SIGCHI Conference on Human Factors in Computing Systems 2001.

[22] T.J. Hess, L.P. Rees, T.R. Rakes, Using autonomous software agents to create next generation decision support systems, Decision Sciences 31 (2000 (Winter)) 1 – 31.

[23] B. Hogg, A. Swami, Using unsuccessful auction bids to identify latent demand, IEEE International Conf. On Systems Man and Cybernetics, Tucson, AZ, 2001 (Oct. 7–10), pp. 2911 – 2916.

[24] C. Hsinchun, C. Yi-Ming, M. Ramsey, C. Yang, An intelligent personal spider for dynamic Internet/Intranet searching, Decision Support Systems 23 (1998) 41–58.

[25] E. Kazumori, Selling online versus offline: theory evidences from Sotheby’s, Proc. of the 4th ACM conference on Electronic commerce, San Diego, CA, 2003, pp. 125– 134.

[26] P. Klemperer, What really matters in auction design, Journal of Economic Perspectives 16 (1) (2002 (Winter)) 169 – 190.

[27] V. Krishna, Auction Theory, Academic Press, San Diego, 2002.

[28] S. Lawrence, C. Giles, Context and page analysis for improved web search, IEEE Internet Computing 2 (4) (1998) 36 – 48.

[29] D.V. Lindley, M.R. Novick, The role of exchangeability in inference, Annals of Statistics 9 (1981) 45 – 58.

[30] D. Lucking-Reiley, Auctions on the internet: what’s being auctioned, and how? Journal of Industrial Economics 48 (3) (2000 (Sept.)) 227 – 252.

[31] P. Maes, Agents that reduce work and information overload, Communications of the ACM 37 (7) (1994 (July)) 31 – 40.

[32] S. Matsubara, Accelerating information revelation in ascending-bid auctions: avoiding last minute bidding, Proceedings of the 3rd ACM Conference on Electronic Commerce, Tampa, FL, 2001, pp. 29– 37.

[33] F. Menczer, Complementing search engines with online web analysis agents, Decision Support Systems 35 (2) (2003 (May)) 195– 212.

[34] K. Mehta, B. Lee, An empirical evidence of winner’s curse in electronic auctions, Proc. 20th international conference on Information Systems, Charlotte, NC, 1999 (December), pp. 465 – 471.

[35] P. Noriega, C. Sierra, Auctions and multi-agent systems, in: M. Klusch (Ed.), Intelligent Information Agents, Springer, Berlin, 1999.

[36] D.E. O’Leary, The internet, intranets, and the AI renaissance, Computer 30 (1) (1997 (Jan.)) 71 – 78.

[37] M.P. Papazoglou, Agent-oriented technology in support of ebusiness, Communications of the ACM 44 (4) (2001 (April)) 71–77.

[38] C. Priest, Economic agents for automated trading, in: A.L.G. Hayzelden, J. Bigham (Eds.), Software Agents for Future Communication Systems, Springer, Berlin, 1999.

[39] P.S.A. Reitsma, P. Stone, J.A. Csirik, M.L. Littman, Randomized strategic demand reduction: getting more by asking for less, 1st International Conference on Autonomous Agents and Multi-agent Systems, Bologna, Italy, 2002 (July), pp. 162 – 163.

[40] A.E. Roth, A. Ockenfels, Last-minute bidding and the rules for ending second-price auctions: evidence from eBay and Amazon auctions on the Internet, American Economic Review 92 (4) (2002 (September)) 1093 – 1103.

[41] R. Saidi, J. Marsden, Number of bids, number of bidders and bidding behavior in outer-continental shelf oil lease auction markets, European Journal of Operational Research 58 (3) (1992 (May)) 335–343.

[42] E. Selberg, O. Etzioni, The metacrawler architecture for resource aggregation on the Web, IEEE Expert 12 (1) (1997) 8 – 14.

[43] N.G. Shaw, A. Mian, S.B. Yadav, A comprehensive agentbased architecture for intelligent information retrieval in a distributed heterogeneous environment, Decision Support Systems 32 (4) (2002 (Mar.)) 401 – 415.

[44] J.E. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, A multiple unit auction algorithm: some theory and a web implementation, Electronic Markets 9 (3) (1999 (Jul.)) 199– 205.

[45] J.E. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, Designing electronic auctions: an WeB2Based hybrid procedure combining aspects of negotiations and auctions, Electronic Commerce Research 1 (3) (2001) 301 – 314.

[46] M. Thorpe, Simple Rule Markup Language (SRML), Cover Pages, available at <sup>b</sup>http://xml.coverpages.org/srml.html<sup>N</sup> (May 2001).

[47] Y. Vakrat, A. Seidmann, Can online auctions beat online catalogs? Proc. 20th International Conference on Information Systems, Charlotte, NC, 1999 (December), pp. 132 – 143.

[48] S. Walczak, A multiagent architecture for developing medical information retrieval agents, Journal of Medical Systems 27 (5) (2003) 479 – 498.

[49] C.C. Yang, J. Yen, H. Chen, Intelligent internet searching agent based on hybrid simulated annealing, Decision Support Systems 28 (3) (2000 (May)) 269 – 277.

[50] Y. Ye, J. Liu, A. Moukas, Agents in electronic commerce, Electronic Commerce Research 1 (1–2) (2001) 9 – 14.

![](/api/attachments/84AW74WQ/fulltext/images/3646af3013acc922b0a6c669da512fd37c10df199d7d13a5923621cddb4ac20a.jpg)

Dawn G. Gregg is an Assistant Professor at the University of Colorado, Denver. She received her PhD in Computer Information Systems from Arizona State University, her MBA from Arizona State University West, and her BS in Mechanical Engineering from the University of California at Irvine. Prior to her doctoral studies, she was employed for 9 years as a research and development engineer. Her current research focuses on how to organize and maintain

Web-based content so that it can be used to better meet business needs. Her work has been published in journals, such as Communications of the ACM, Decision Support Systems, and Information Systems Frontiers.

![](/api/attachments/84AW74WQ/fulltext/images/6c09435d33d4b81b95dad26ef7a8f3bff522b4c0606956c4df09d59b382fa4b6.jpg)

Steven Walczak is an Associate Professor in the Information Systems area of the Business School with the University of Colorado at Denver. He received his PhD in Artificial Intelligence from the University of Florida, his MS in Computer Science from the Johns Hopkins University, and his BS in Mathematics from the Pennsylvania State University. Dr. Walczak’s research interests are in knowledge management and applied artificial intelligence systems,

including neural networks, knowledge-based systems, and intelligent agents. He has over 80 publications, including articles in the Journal of Management Information Systems (JMIS), Decision Support Systems, and various IEEE Transactions.
