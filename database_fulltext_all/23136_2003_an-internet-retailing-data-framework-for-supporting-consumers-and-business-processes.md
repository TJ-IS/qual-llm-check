---
otero_id: 23136
otero_key: "UY4Q62F2"
title: "An internet retailing data framework for supporting consumers and business processes"
authors: "Adam P. Vrechopoulos; Katherine C. Pramataris; Georgios Doukidis; George Lekakos"
year: "2003"
journal: "Information Systems Journal"
doi: "10.1046/j.1365-2575.2003.00153.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An internet retailing data framework for supporting consumers and business

processes

Adam P. Vrechopoulos\*, Katherine C. Pramataris<sup>†</sup>, Georgios Doukidis<sup>‡</sup> & George Lekakos<sup>§</sup>

The E-Business Center (ELTRUN), Department of Management Science and Technology, Athens University of Economics and Business, 47A Evelpidon Street, 11362, Athens, Greece, email: \*avrehop@aueb.gr, <sup>†</sup>K.Pramatari@aueb.gr, <sup>‡</sup> gjd@aueb.gr, and <sup>§</sup> glekakos@aueb.gr

Abstract. This paper describes an action research case study dealing with the development of an internet retail store with advanced capabilities. The research focuses on the exploitation of information generated through consumer–system interaction by the virtual retailer (i.e. sales, navigation and personal consumer data). The results effectively support the business processes, consumers and product suppliers. To that end, an internet retailing data framework was developed during the user requirements capturing phase of the ACTIVE (Advertising and Commerce Through the Internet in the context of the Virtual Enterprise) project, as a means of structuring the system’s information requirements and data processing mechanisms The purpose of this framework is to describe in detail what con: sumer information the system needs to collect and to advise the virtual retailer (i.e. ACTIVE’s administrator) how to use the available software components to exploit this information in order to effectively support consumers and business processes. Despite the fact that the proposed framework is tailored to the ACTIVE characteristics and needs, it can also be utilized by other virtual retailers to effectively support their key stakeholders (i.e. customers and suppliers).

Keywords: internet retailing, consumer behaviour, business processes, e-shop

## 1. RETAILING TRENDS OVER INTERNET

The fields of application of the internet for companies are numerous and invade virtually every area of business life. So far, the commercial part of the internet has been used mainly for presenting companies and products. It is now increasingly developing more into an actual marketplace where all the stages of a commercial transaction can be handled in the virtual arena. Traditional interactions in the marketplace are becoming transactions in the marketspace, which are different in terms of content, context and the infrastructure of the transaction (Rayport & Sviokla, 1994).

A growing number of retailers have successfully implemented electronic commerce solutions and the experience of these early adopters provides valuable insights into how new value chains are constructed (Aldridge & Borehamwood, 1998). Online markets are significantly different in a number of aspects from the structure of ‘classical’ or physical markets. Their typology, client potential, price competition and client–producer interactions are considerably different from the same phenomena encountered in classical markets. In these markets the physical presence of products, parties involved, distribution and transportation, advertisements and clearance of transactions play a role that online markets do not yet have and to an extent can never achieve.

However, the emerging virtual retail environment, facilitated by the technological capabilities of the internet, offers advantages other channels cannot easily replicate. To name but a few, it facilitates the instantaneous exchange of up-to-date information about products, services and market transactions. It efficiently collects information about customer communities’ specific needs, interests and demographics (Kannan et al., 1998). Furthermore, it enables direct contact with suppliers and customers, provision of advanced customer service, application of oneto-one marketing techniques, etc.

In such an environment, it is important to understand the potential that the collection of integrated data can offer and the benefits that can accrue from the utilization of the new information that is available online (Vrechopoulos et al., 2001). A comparative study of the features of a dozen virtual retail stores, currently present on the Web, shows that there is still ample room for development and improvement in order to exploit the full potential of the capabilities offerec in that information context (Pramataris et al., 2000b). More specifically, they state that it is important to understand what the data are, how and when they should be collected and, most importantly, how these data can support customers/web site visitors, web site owners, and business processes. To that end, they strongly encourage future research in this area towards providing the appropriate data collection frameworks and information processing mechanisms to be adopted by virtual retailers.

In this paper, we first examine the characteristics of an integrated virtual retail store based on the description included in the Technical Annex of the ACTIVE (Advertising and Commerce Through the Internet in the context of the Virtual Enterprise) project. We then describe the methodology followed within the ‘user requirements capturing’ phase of the project towards developing an internet retailing data framework for supporting consumers and business processes. The objectives for developing this framework were to define in detail which customer data should be collected through the consumer–system interaction and how these data should be processed and utilized towards supporting the actors involved in this environment, namely the customers, the virtual retailer and the product suppliers. It should be clarified, however, that this data framework was tailored to the ACTIVE virtual retail store specific needs and characteristics. In the fourth section of the paper, we apply the defined data framework to the ACTIVE environment and associate it with the various virtual store components. Section five concludes by presenting the

ACTIVE system current status and by identifying potential areas of further development and research.

## 2. AN OVERVIEW OF THE ACTIVE VIRTUAL RETAIL STORE

The ACTIVE project (EP 27046) was funded by the ESPRIT Programme (Framework IV) of the Commission of the European Union. Its aim was to introduce a global electronic commerce platform that will support integrated retail services and provide an intelligent interface upon which the involved players could establish a trusted relationship. It should be noted that business-tobusiness relationships are based on the project consortium agreement, which sets a series of rules that every participant (i.e. retailers and suppliers) should follow [e.g. the retailer must provide online POS (Point Of Sale) data to its suppliers]. On the other hand, business-to-consumer relationships are based on the techniques and methods dictated by permission marketing, that should be followed by the retailer and its suppliers (thoroughly discussed in section 3).

Based on the description included in the Technical Annex of the ACTIVE project, the following objectives should be met.

## Support to the end-users

A virtual retail store offering integrated services to the customers/consumers, the virtual retailer and to the product suppliers was implemented within the ACTIVE project. More specifically, ACTIVE aims to satisfy the following business objectives:

Provide efficient, customized and supportive shopping channels between consumers and retailers (and consequently suppliers) that will maximize benefits for all parties involved.

• Provide efficient marketing and advertising models that will support the application of sophisticated promotion techniques.

• Provide efficient physical inventory, virtual sales management methods and tools that will exploit information to optimize stock and establish a continuous replenishment environment.

Establish trusted relationships among all parties involved where information and products flow efficiently along the virtual and physical value chain, respectively.

The ACTIVE e-shop follows the ‘Transaction to Information’ evolutionary path of a web site introduced by Quelch & Klein (1996). Here transactions between customers and the e-shop are implemented up-front and supported by online and after-sales customer services. Product information is initially kept to a minimum but is extended gradually as the e-shop evolves as well as implementation of information collection and market research tools (Figure 1). The opposite path is followed by traditional web sites. The initial function supported by the site is that of information collection and the one implemented last is that of online transactions with visitors and prospective customers.

ACTIVE’s implementation follows the agent-based approach for electronic commerce. This permits the creation of a virtual marketplace in which a number of autonomous or semiautonomous agents trade goods and support users. Agents, semi-intelligent computer programs, can assist in handling repetitive and time-consuming tasks. In an electronic commerce environment, agents can ‘go shopping’ for a user, taking specs and returning with recommendations of purchases which meet those specifications; they can act as ‘sales-people’ on behalf of product suppliers by providing product or service sales advice; they can help troubleshoot customer problems, etc. (Terpsidis et al., 1998).

![](/api/attachments/UY4Q62F2/fulltext/images/7ce1a2fbe81d04292e30bcfdc69aede7860b0642bffa2541286450d32e447e10.jpg)

The components comprising the ACTIVE system include:

1 Home Shopping Tool/Service The purpose of the Home Shopping Tool (HST) is to provide consumers with a personalized environment. It is based on a set of services and facilities that transform the shopping process to an entertainment experience while acting on behalf of the consumer. The services offered to consumers include:

Catalogue information The system provides a complete view of all the products stored in the database, a view that is constructed dynamically and based on the preferences and needs of the consumer. Products are grouped in categories and subcategories that are arranged in hierarchies.

Product uploading The retailer or suppliers can upload product description details and images on the database through a graphical user interface. They can also replace and update existing information, product descriptions, etc.

Shopping facilities These refer to the facilities offered to the consumer in order to enhance or support the shopping experience. They include the traditional shopping basket, shopping lists and the quick shopping facility.

• Searching Searching is based on multiple search criteria specified by the user and on the consumer information given. Search options are limited to those that are relevant to the already selected data, thus preventing consumers from choosing invalid or empty selections.

• Payment services The HST provides an open payment architecture that can incorporate most of the payment systems currently available.

2 Consumer Behaviour Tool (CBT) The CBT aims to capture customer-related information while he/she navigates through the ACTIVE system. The type of information to be obtained might relate to consumer preferences, navigational data, etc. while the consumer interacts with the system. The collected information is then processed by an analysis module and the provided results are stored in the Consumer Information Model. These results are further used to create or update consumer profiles based on well-defined consumer characteristics. The CBT has three main functionalities:

acquisition of consumer related information: this takes place by tracking the customer’s behaviour throughout their visit to the ACTIVE e-shop, as well as through questionnaires, complaint forms, after-sales forms, suggestions, etc.;

• structuring of the related navigational data; and

• analysis of the extracted data and visualization through the generation of reports on customer behaviour.

3 Advertising Tool The main aim of the advertising tool is to offer the virtual retailer and supplier the ability to advertise their products in the ACTIVE virtual shop. Advertisement takes place in the form of banners that are displayed on specific pages and space on the screen. Another form of advertisement can be the order and format used to present the products to the user, as well as the appearance of a product at the ‘special offers’ page. The supplier or retailer should be able to address the advertisement campaign to a well-defined target consumer group. The advertising tool allows them to define the consumer group they want to target as well as the form and duration of the advertisement. It then schedules the advertisement campaign based on the constraints set by the user and measures the advertisement effectiveness, allowing for online corrective action or future reference.

4 POS Analyser The POS analyser allows both retailer and suppliers to access past sales data and analyse the effectiveness of specific brands, product segments, product categories, etc. in terms of sales, turnover or profit generated. In addition, the POS analyser combines sales data with consumer information in order to analyse performance by target group, show the product preferences of specific consumer profiles and facilitate the definition of the target consumer groups for each product or product category.

5 Shopping Recommender This agent assists the user during the shopping process while at the same time promotes the products on behalf of the retailer and the suppliers. The assistance offered to consumers is in the form of recommendations about new products, product discounts, coupons, special offers, contests, lotteries, etc. All recommendations are tailored to the consumer’s individual profile and needs. The retailer or supplier that wishes to make a targeted recommendation specifies the target group by defining a set of rules/constraints.

6 Online Sales Negotiator Consumers are able to make automated online negotiations with the sellers for the purchase of various goods and commodities. They can easily create an agent through a user-friendly procedure that does not require special programming skills. They instruct the agent to find and negotiate the purchase of a product according to their preferred product attributes (e.g. product name, quantity, price, time). This agent will get involved in a negotiation process with the agents that represent the sellers and will try to reach a mutual agreement according to the mandate from its creator.

![](/api/attachments/UY4Q62F2/fulltext/images/98e38f8c04e754f9ccf11bc9667adaff85fe68ffb770defb4c77910622b607a5.jpg)  
Figure 2. The ACTIVE (Advertising and Commerce Through the Internet in the context of the Virtual Enterprise) system architecture.

The overall ACTIVE architecture, presenting the various agents and other system components, as well as the interaction among them, is graphically depicted in Figure 2.

## 3. THE DEVELOPMENT PROCESS OF THE INTERNET RETAILING DATA FRAMEWORK

The agents and other components presented above aim to support all the actors involved in the ACTIVE system, such as the customers, the virtual retailer (i.e. the intermediary who is the ‘owner’ of the virtual store) and the various product suppliers. The key element, in doing so, is the appropriate utilization of the information that is obtained by monitoring customers’ interaction with the system. During the ‘user requirements capturing’ phase of the project, it was clear that there was a need to develop a data framework that would be able to advise ACTIVE’s administrators (i.e. retailer or a new type of intermediary between retailer and suppliers) which type of consumer information they should collect from the system. It also advised how this information could be exploited by the corresponding online store’s software components towards effectively supporting ACTIVE players (i.e. consumers, retailers and suppliers). To that end, a data framework was developed as an outcome of the process of developing the ACTIVE virtual retail store. It should be clarified that this specific framework is based only on those data generated by consumers visiting the ACTIVE online store. Therefore, this particular framework was developed in order to:

• describe which customer information should be collected through the system; and

• describe the process of converting information to knowledge through the exploitation of the available software components towards effectively supporting ACTIVE’s stakeholders’ (retailer, customers and suppliers) key processes.

## 3.1. The research methodology

The present study employs an action research approach. According to Galliers (1992), action research constitutes an alternative information systems research method. Galliers (1992, p. 152) reports that action research is an ‘applied research where there is an attempt to obtain results of practical value to groups with whom the researcher is allied, while at the same time adding to theoretical knowledge.’ In the case of the present study, we were involved as funded partners in the ACTIVE project and our role was to capture user (i.e. retailers, suppliers and consumers) requirements in order to design an effective application (we were the leaders of the corresponding work package labelled ‘user requirements capturing’). This implies that the ‘groups with whom the researcher is allied’ in the case of the present study are, on the one hand, the participating retailers and suppliers (project-funded partners) and, on the other hand, the consumers that participated in the corresponding surveys. More specifically, we designed and conducted the surveys (i.e. questionnaires and in-depth interviews), collected and analysed the data and prepared the requirements documents. Then, we designed the framework which has ‘practical value’ for the involved groups while at the same time adds to the internet retailing ‘theoretical knowledge’. Finally, we associated the framework with the ACTIVE’s software components as dictated by the technical annex of the project.

The first step in the development of the framework was to understand what the user (i.e. retailers, suppliers and consumers) requirements were based both on current practices and on future expectations. As discussed, this took place during the ‘user requirements capturing phase of the project which considered the information requirements of the following users:

1 a Greek traditional retailer (NIKI SA, Marinopoulos & Co, Continent Group) wishing to move into the online business but having no experience in this environment whatsoever;

2 a German mail-order company (Otto Versand GmbH & Go KG) wishing to extend its current catalogue-based presence on the internet with advanced features;

3 three product suppliers/manufacturers (Procter & Gamble S.A., Johnson & Johnson S.A., and ELGEKA S.A.) who were interested in exploring the potential of the new market channel; and

4 potential customers in the two markets (i.e. Germany and Greece) that were sought among consumers who were both distant shoppers and PC users.

The first three types of users above were analysed separately as a unique case. This involved:

a process analysis describing the current way of conducting business including the identi fication of key processes and potential areas of improvement;

• an analysis and prioritization of the users’ information requirements in the virtual retail envi ronment; and

• market research analysing the market’s competitive status, customer base, trends among leading companies and competitors, etc.

These analyses were based mainly on personal interviews and took place within crossfunctional teams in each company.

On the other hand, as reported by Turban et al. (2002), a key task for electronic commerce is to find out who the actual and potential customers are. To that end, the information requirements of actual and potential customers in the virtual retail environment were defined via two different consumer surveys, based on questionnaires, that took place in the two target markets (i.e. Germany and Greece). The selection of the sample participants was conducted based on random sampling procedures from nine different areas both in Greece and in Germany. The basic criteria for the participation in the survey were age range (i.e. 18–45) and use or ownership of a PC. The samples were particularly well-balanced in terms of some basic demographic characteristics of the respondents (i.e. gender, age, etc.) and more skewed (toward the higher levels) in terms of family income and education. This last observation is explainable by the ‘PC use/ownership’ criterion for participation in the survey.

It should be clarified, however, that it is out of scope of the present paper to discuss in detail the methodology followed during the aforementioned research efforts (i.e. case studies and consumer surveys) along with their corresponding analytical results. On the contrary, the objective of this paper is to present the outcome of these research initiatives which is the internet retailing data framework and its exploitation by the ACTIVE system. Vrechopoulos et al. (2001) and Pramataris et al. (2000a) have already thoroughly discussed these research efforts.

Furthermore, a parallel internet survey was conducted focusing on specific virtual retail stores over the Web (Pramataris et al., 2000b). This survey served as a supplementary research effort towards deciding which kind of information the ACTIVE system should collect and how this information should be utilized towards supporting ACTIVE’s stakeholders (i.e. virtual retailer, suppliers and customers). This was achieved by investigating what type of information the researched virtual retail stores collect through interaction with their customers and how they use this information to support key business processes and customers’ behaviour.

Finally, the proposed data framework was tested within the trials of the ACTIVE system. Retailers, suppliers and consumers evaluated the system and provided valuable feedback towards its improvement. The following discussion, therefore, includes the feedback provided through the trials of the ACTIVE system. It refers to the type of data the system should collect along with the process of utilizing these data towards supporting retailers, suppliers and consumers.

## 3.2. The data framework

Customer information allows any marketer to communicate in a direct and meaningful fashion with precisely targeted customers (Roberts, 1997). The internet and more specifically the virtual retail environment revolutionizes this capability by offering online access and processing to consumer behaviour information. This feature, combined with the rest of the properties of the new sales channel, has led many researchers to talk about a new marketing paradigm for electronic commerce (Hoffman & Novak, 1997). This paradigm shift is seen across all four Ps represented by the term marketing (i.e. product, price, promotion and place/distribution). ‘Information processing’ constitutes the fifth ‘P’ of the marketing mix in an electronic commerce environment. Thus, the new marketing paradigm for electronic commerce captures not only the business-to-consumer interface but also the business-to-business relationships and the function of the value chain in total.

Applying the aforementioned paradigm shift within the context of the ACTIVE system, it was first necessary to define in detail what type of information was available in the new market environment. The following step was to define how this information could be exploited and processed by the system capabilities in order to support consumers and business processes. To that end, the following information categories were derived through the research efforts con: ducted within the ‘user requirements capturing’ phase of the ACTIVE project, as discussed above. These categories constitute the information that should be collected by the ACTIVE’s software components during the consumer–system interaction:

1 Consumer information This category comprises all the data that characterize each consumer separately (i.e. demographics and preferences). These data enable marketing analysts to build consumer profiles, divide the market into segments, target the most attractive consumer groups and position existing or new products effectively. The whole process is based on the personal characteristics and preferences that each consumer has, which compose the enabling factor for applying personalized marketing/sales strategies over the internet (Bush et al., 1998). Consumer data are divided into the following categories:

Identification This includes the consumer name, identification number, login-name, password, credit card information, etc. It is used for personalized dialogue on the one hand and for security/credibility reasons on the other. Part of this information is provided up-front when the user enters the virtual store and part of it when he/she completes the purchasing cycle. • Demography This category refers to the demographic characteristics of the user, such as age, sex, income, home address, occupation, education, etc. This is the typical information used for targeting products and services in the traditional business environment. In the virtual environment it can be used in conjunction with other data categories for the same purpose. This information is provided when the user registers either upon entering the store or at check out. As some consumers may be reluctant to provide this information, despite the promise of getting a better service, alternative ways of targeting can also be applied in the online environment as explained below.

• Consumption habits and preferences Apart from demographic information, it is important to keep track of what the consumers have previously purchased, what categories and products they usually buy and with what frequency, when they have preferred one product over another, when and why they have changed purchasing habits, etc. This information can be used as an alternative means of targeting and, in combination with the rest of the consumer data, can provide powerful conclusions regarding product preferences, promotion effectiveness, etc. For example, a supplier may decide to target a new product to consumers who have previously purchased products of the same or relative category. In addition, a manufacturer may make decisions on specific product attributes (e.g. colour, fragrance, etc.) based on perceived consumer preferences on other products. The problem, and at the same time the challenge, is how to manage and process online this immense amount of data for dynamic decision-making and action.

• Segment affiliation Based on the demographic and consumption habits/preferences information, a consumer may belong to one or more segments depending on how these have been defined. For example, a segment may be defined on the basis of purely demographic information, such as ‘women 20–35 years old’, on the basis of consumption habits, such as ‘consumers buying baby products’ or both ‘consumers buying cigarettes and age 20–25’. This assignment of consumers to specific segments is necessary for applying targeted marketing techniques, such as direct email or targeted banner advertising and is usually maintained in the database for efficiency reasons.

• Pre-sales communication This category refers to any kind of information that has been generated by the consumer before the time of purchase. This can be, e.g. requests for specific products or services, responses to questionnaires and other forms, etc.

2 Sales data Sales data refer to the data created by consumers while performing sales transactions by interacting with the system. These data relate sales of a specific product or product category to dimensions, such as time, consumer characteristics, etc., rendering the valuable information of ‘which consumer buys which products and when’. Sales data are divided into the following categories:

Purchasing behaviour This type of data includes a reference to all the products a consumer has bought, the time of the purchase, the quantity bought, the price paid, whether or not the product was sold under promotion, etc. In other words, these correspond to the typical POS data as generated by scanning equipment in the traditional retail environment, with the additional feature of them being related to a specific consumer.

Post-purchase behaviour This category records all consumer responses after the actual purchase, such as product returns, requests for service, requests for product usage instructions, complaints, etc.

Payment and delivery preferences Another type of information that is necessary for the proper management of payment and delivery facilities. It corresponds to the preferred payment and delivery method of each consumer, the frequency at which each facility is used, problems encountered, etc.

• Credit worthiness In a distant shopping environment, where the consumer makes a purchase after an order has been executed, either on delivery, pick-up or via credit card, it is important to keep track of a consumer’s past credit worthiness. This information is usually combined with other mechanisms and practices checking the validity of an order, such as performing a telephone call before delivery.

3 Navigation data These refer to the consumer’s behaviour through the store, the consumer navigation habits, ‘click-throughs’, etc. While the cost of collecting these data in a traditional store is very high, in a virtual store environment this cost is minimized because of the capabilities offered by technology. More specifically, a traditional store has to use techniques, such as video recording, in order to monitor in-store consumer behaviour. Whereas a virtual store can monitor this in many different ways which are more effective, accurate, quick and low in cost. Using these data, we can monitor, analyse, predict and finally guide consumers through their shopping activity. Navigation data are divided into the following categories:

Visits This field records the number of times a consumer has visited the store. This information is easy to record for consumers that register upon entering the e-shop or for those that allow the usage of ‘cookies’ on their PCs (Schønberger, 1999). For the rest of consumers, whose identity is unknown while they navigate through the e-shop, this information may be recorded only if they complete their visit with a purchase and thus unveil their identity. This applies to all the data categories mentioned below.

First and last visit This is the date and time a consumer visited the e-shop for the first and last time. In combination with the number of visits, it allows us to determine the frequency of visits to the store.

• Entrance and exit This is the date and time a consumer entered and exited the e-shop at each visit. This information allows us to determine the average time of a visit, to see whether there are variations among different consumer groups or among the different visits of the same consumer, etc.

Response in promotions This category records a consumer’s response in promotional areas such as clicking through a banner-ad (Briggs & Hollis, 1997), purchasing a ‘specialoffers’ item, whether checks the ‘special-offers’ section each time one enters the e-shop, taking part in a product contest or lottery online, etc. This information is valuable in evaluating a promotion’s effectiveness especially when matched with purchase behaviour information and consumer profiles.

• Searching Criteria and parameters are also part of navigation data. They are used for searching specific products, the way and degree to which the search facility is used, the response to search results, etc.

• In-front of shelf behaviour Valuable conclusions regarding consumer behaviour may be derived from monitoring a consumer’s response in front of the virtual shelf. For example, by observing whether the customer selects one of the top products on the list, ‘scrolls down’ for a specific brand, looks for more detailed product information, ‘sorts’ the shelf based on specific criteria (e.g. price, brand name), etc.

• Category sequence Last but not least, in the virtual environment we have the possibility to record the sequence at which a consumer moves from one category to another. Given the fact that there are no space limitations, the user may jump from one category to another based on impulse, complementary category usage, etc. The outlining of relationship patterns among different categories may be a valuable tool for designing or dynamically restructuring a virtual store’s layout.

The above list is not meant to be exhaustive or definitive. While covering all the major data fields used in the current practice, it may well expand as innovative features are realized to take full advantage of the Web. The first two data categories are also available in the traditional shopping environment, although to a limited extent, through POS scanning facilities and the mechanism of consumer loyalty cards. The third type of data (i.e. navigation) is only relevant to the internet environment. Although, each data category can find great use on its own, in supporting consumers and business processes, the great power rests in the combination of the different types of data.

## 3.3. Privacy and trust issues

The ACTIVE system follows the consumer privacy laws as dictated by the European Commission. Furthermore, the system collects and exploits customer information following the rules of permission marketing towards guarding consumer privacy. According to Straus & Frost (2001, p. 463), ‘permission marketing allows advertisers to present marketing communication messages (e.g. banners, emails) to consumers who agree to receive them.’ More specifically, for its commercial exploitation the ACTIVE system will meet the following requirements essential to the ethical use of consumer information and protection of privacy (Strauss & Frost, 2001): (1) notice: users will be aware of the site’s information policy before data are collected; (2) consent: users will be allowed to choose participation or exclusion from the data collection procedure and will be given choice over how their personal information is used and shared: (3) access: users will have the ability to access their data and correct it if erroneous; (4) security: the ACTIVE system will ensure that consumer data (e.g. credit card information, shopping habits, demographics, etc.) will only be used for the purpose they have been collected (users will be aware of that purpose before allowing the system to collect their information); and (5) enforcement: users will have the capability to select what kind of information they would like to offer to the system, opt-out from mailing lists, request removal of their information from the database, etc. At the same time, the ACTIVE system will publish all the necessary information right on the web site to gain the TRUSTe seal (http://www.truste.org).

As far as the B2B trust dimension is concerned (i.e. trusted relationships between suppliers and the retailer adopting the ACTIVE system), this will be based on the win–win relationship concept which constitutes the core idea of the ACTIVE system. In other words, suppliers and retailers should work together towards meeting the needs of the end-customer (Hofstetter & Corsten, 2002). To that end, Hofstetter & Corsten (2002, p. 95) state that ‘loyalty is crucial to both retailers and manufacturers. It delivers a double win.’ They also suggest that ‘both retailers and manufacturers might profit from aligning their marketing strategies’ (p. 96). Similarly, Seifert (2002) supports that above any consortium/business agreement, the most important prerequisite for participating in business environments similar to the ACTIVE system is the adoption of collaborative commerce business practices. These are based on the trusted relationships between the partners and the continuous and free information flow along the retail value chain. Otherwise, the advanced capabilities of such systems cannot be exploited.

## 3.4. Support offered to consumers, retailers and suppliers

Below we examine in more detail how the above data categories offer support to the various system actors, such as the consumer, the virtual retailer and the product suppliers.

## 3.4.1. Consumer

With reference to the support offered to consumers, we examine this service under the perspective of the classical consumer buying process as many other researchers have done in the past (e.g. O’Keefe & McEachern, 1998; Falkou et al., 1999). According to this perspective, consumers progress through the rational stages of problem/need recognition, information search, evaluation of alternatives, purchase decision and post-purchase behaviour (Bettman, 1979; Howard, 1989; Engel et al., 1990). In other words, the consumer in the physical environment passes through five stages during the buying process as described in Figure 3.

Hawkins et al. (1998) argue that the convenience, depth and variety of information available on the internet may well change the nature of consumer information search behaviour and evaluation of alternatives process in the future. It can generally transform the traditional model of the buying process. Indeed, one could see the five stage model of the consumer buying process being transformed as following within a virtual shopping environment (Vrechopoulos et al., 1999):

By combining advertising features (e.g. banners, personalized recommendations) with shopping facilities, virtual retailing may create consumer enthusiasm and lead to an immediate product purchase. This would allow the consumer to jump from stage 1 to stage 4 of the buying process. Consumers may purchase the products they want directly from shopping lists or purchase a product that is being recommended to them based on their profiles.

On the other hand, information search and evaluation of alternatives (second and third stage of the buying process) can take place at the same time by using multi-criteria search engines. These can automatically find and present the various alternatives while performing a comparative analysis of their characteristics. For example, a user may ask to see all the products in a category ranked or categorized by a certain attribute. Based on this attribute, the results of the search will then immediately allow for the evaluation of various alternatives.

Post-purchase behaviour (fifth stage) can be supported and effectively controlled by the after-sales support services offered by the virtual store while utilizing the technology capabilities (i.e. answer to consumer’s questions directly by email).

![](/api/attachments/UY4Q62F2/fulltext/images/f317e47934b101d9253475030494d06c98ae9218939d7487a99f2ead0239ffb8.jpg)  
Figure 3. The internet retailing data framework for supporting consumers and business processes.

Based on the aforementioned classification scheme, the resulting information categories collected through the consumer–system interaction are mapped to each stage of the consumer buying process (Figure 3). In the next section (section 4), we will map this process to the components of the ACTIVE system.

## 3.4.2. Retailer

The business process classification scheme included in the ECR Europe Report (1999) was adopted for the virtual retailer as an analytical tool within the ‘user requirements capturing phase. This classification scheme supported the current research towards, on the one hand, defining the key processes that need to be supported by the collected data and, on the other hand, describing the process of exploiting and utilizing the collected data towards effectively supporting each of the corresponding business processes. The key business processes for the virtual retailer are the following:

• Define store assortment This process incorporates all the decisions regarding which products to carry ‘on-shelf’, how these are hierarchically structured in product categories and subcategories, who is the target consumer, which are the key product categories, etc. These decisions are based on market and competitive environment analyses, product performance in terms of sales and profit, profile of consumers entering the store, etc. For example, a retailer may choose to offer those products that sell best in the market and render him the highest profit. Alternatively, he may make his selection of products among those mostly bought by his target consumers. The virtual structure of the categories in store also depends on conclusions that are derived from the analysis of navigation data. It can be easily understood from the above description that this continuous process dynamically reshapes the assortment of products and structure of the categories in-store.

• Define pricing and promotions Having decided on the product assortment, the next step is to define the pricing and promotion scheme for these products. This depends on the character that the retailer wants to communicate to the customers. For example, the retailer with the ‘lowest prices’, the ‘best offers’, the ‘greatest product assortment and reasonable prices’, etc. Instore product promotions may be initiated by the retailer or be in co-operation with the product suppliers. In any case, this process is based on the analysis of past consumer purchase behaviour (i.e. what products have been bought, at what prices and whether on promotion) and the matching of consumer profiles to past buys in order to perform the right targeting, as well as the analysis of navigation data regarding response to promotions, search criteria, etc.

Shelf management This process refers to the way the products are placed and presented on-shelf, the space allocated to each product category and to individual brands and the levels of stock maintained on shelf and at the warehouse in order to allow for efficient shelf fulfilment. This is done both during regular and promotional periods, etc. In the virtual shop environment, this process takes on different dimension as space limitations are virtual (e.g. screen space on first view) and not physical. Thus, the data required to support this process in the e-shop include sales data in combination with consumer data (e.g. in order to offer personalized service by presenting the most relevant products to each consumer) as well as navigation data (e.g. in order to decide the depth of information available to consumers at each level).

• Product replenishment The final critical process for the retailer is the process of product replenishment. This incorporates the stages of the supply chain from product ordering to product delivery at the central warehouse, distribution to local warehouses or stores, and up to shelf replenishment. In the virtual environment, the stage of shelf replenishment is replaced by the ‘home-replenishment’, which is either performed by the retailer or outsourced to a third party. Included in the data required to support this process are sales data. These data are used to predict future product off-take and corresponding inventory levels at the warehouse, as well as schedule home deliveries.

## 3.4.3. Supplier

A similar categorization of processes, as the one used for the virtual retailer, is also used for the supplier of products in the virtual environment, again based on the ECR Europe Report (1999). The examined processes that depend on the support offered by the aforementioned data framework include:

Introduce products Consumer information in combination with sales and navigation data is a very good source for identifying consumer preferences, unmet consumer needs, desirable product characteristics, etc. This type of information has proved valuable for the development of new products or new product variables that meet these needs. In addition, the virtual environment gives the possibility to virtually introduce a product to only a specific consumer segment. This is accomplished by identifying consumers based on profile information and thus, testing consumer response before introducing the product to the whole market.

Merchandize products Decisions regarding the variety of products offered per category to specific consumer groups, the prices and sizes at which these products are offered, the market channels used, etc. all fall within this key process of a product supplier. Obviously, consumer and sales data are necessary in order to support decisions in this area by offering insight on past consumer response and product performance.

Promote products For a supplier it is critical to decide whether and when he will promote a product, a whole product range or a specific hero item, what type of promotion to apply, what group of consumers to target, etc. Both the decision-making and the implementation of the final decision rely on the usage of the data framework described above. On the one hand, consumer data in combination with sales data and navigation (response to promotions) data allow the evaluation of past promotion performance; on the other hand, consumer data allow the right targeting of promotions.

Replenish products Last but not least, the process of product replenishment is the key to ensuring that the right products arrive at the virtual retailer warehouse on time, in order to respond effectively to the consumer home-replenishment requirements. The information on product sales should be passed-on from the e-shop to the product suppliers, so they can follow consumer demand and better plan the replenishment process. In the case of the Continuous Replenishment Process (CRP Report, 1994), this practice has exhibited significant efficiencies and cost savings for both the retailer and the supplier.

The relation as described above, between the defined data framework and the support offered to consumers and business processes, is graphically summarized in Figure 3. In the following section this data framework is associated with the ACTIVE system components in order to meet the objectives of this particular study.

## 4. ASSOCIATION OF THE DATA FRAMEWORK IN THE ACTIVE CONTEXT

We have provided the information that should be collected by the ACTIVE system and described the process of exploiting this information towards supporting the ACTIVE stakeholders’ key business processes. We will now examine how this information and exploitation process is related to the components of the ACTIVE system as presented in section 2. This effort offered a basis for examining the degree to which the ACTIVE system may support consumer and business processes. This is achieved through its software components and the nonexploited potential that still exists in this area. Table 1 summarizes this relation. It should be noted that Table 1 was developed after the trials of the ACTIVE system. More specifically, retailers, suppliers and consumers who participated in these trials provided valuable feedback (through focus groups) regarding the way that the ACTIVE components can effectively support their key business processes or behavioural steps, respectively.

The CBT captures consumer data, from the time a consumer enters the virtual store to the time of exit. In case the consumer does not register oneself upon entering, the tool follows the user session and records the information once the consumer identity becomes available. For example, when the consumer completes a purchase or fills-in a form. In addition, the CBT captures the consumer behaviour through the store (i.e. the navigation data) and associates these to consumer data. This functionality makes the CBT a valuable tool for supporting the provision of targeted services to consumers in the need recognition, information search and purchase decision phases. The value of consumer and navigation data for the support of retailer and business processes has also been explained in the previous paragraphs.

The HST uses the data generated by the CBT (i.e. consumer and navigation data) in order to facilitate the consumer shopping process and guide the user to a purchase decision. For example, customer data are used for adapting the product catalogue and structure to the specific consumer profile. Navigation data are used for optimizing the usage of the search facility. The HST then records which products were bought and by which consumer. This information is further used for consumer targeting based on past product and category purchases.

Table 1. ACTIVE support to consumers, retailer, and suppliers

<table><tr><td rowspan="2">ACTIVE component</td><td rowspan="2">Data used</td><td colspan="3">Process support</td></tr><tr><td>Consumer</td><td>Retailer</td><td>Supplier</td></tr><tr><td rowspan="3">Consumer Behaviour tool</td><td>Consumer data</td><td>Need recognition</td><td>Define assortment</td><td>Introduce products</td></tr><tr><td>Navigation data</td><td>Information search</td><td>Define prices/promotion</td><td>Merchandise products</td></tr><tr><td></td><td>Purchase decision</td><td>Shelf management</td><td>Promote products</td></tr><tr><td rowspan="3">Home Shopping Tool</td><td>Consumer data</td><td>Information search</td><td></td><td></td></tr><tr><td>Sales data</td><td>Evaluation of alternatives</td><td></td><td></td></tr><tr><td>Navigation data</td><td>Purchase decision</td><td></td><td></td></tr><tr><td rowspan="3">Advertising Tool</td><td>Consumer data</td><td>Need recognition</td><td>Define prices/promotion</td><td>Promote products</td></tr><tr><td>Sales data</td><td>Purchase decision</td><td></td><td></td></tr><tr><td>Navigation data</td><td></td><td></td><td></td></tr><tr><td rowspan="4">POS (Point Of Sale) Analyser</td><td>Consumer data</td><td></td><td>Define assortment</td><td>Introduce products</td></tr><tr><td>Sales data</td><td></td><td>Define prices/promotion</td><td>Merchandise products</td></tr><tr><td></td><td></td><td>Shelf management</td><td>Promote products</td></tr><tr><td></td><td></td><td>Product replenishment</td><td>Replenish products</td></tr><tr><td rowspan="2">Online Sales Negotiator</td><td>Consumer data</td><td>Information search</td><td></td><td></td></tr><tr><td>Sales data</td><td>Evaluation of alternatives</td><td></td><td></td></tr><tr><td rowspan="3">Shopping Recommender</td><td>Consumer data</td><td>Need recognition</td><td>Define prices/promotion</td><td>Promote products</td></tr><tr><td>Sales data</td><td>Purchase decision</td><td></td><td></td></tr><tr><td>Navigation data</td><td></td><td></td><td></td></tr></table>

The Advertising Tool also uses consumer, sales and navigation data in order to send the right targeting of advertising messages to the consumers. In this way, it facilitates the steps of need recognition and purchase decision of the consumer buying process. In addition, the same tool allows both retailer and product suppliers to schedule their advertisement, measure the effectiveness of their promotions (in terms of impressions and effect on product sales) and develop their promotion plan for the future.

The POS Analyser is a tool facilitating the analysis of past sales data in combination with consumer information. This data analysis supports retailer and supplier decisions regarding all the described processes. For example, knowing which products are mostly preferred by what group of consumers, and what profit benefits are associated with them, can greatly help a retailer define the ideal product assortment for that specific consumer group. In the same way, both a retailer and a supplier can see the position of each product in the market, identify inefficiencies in the marketing strategy, effectively plan the replenishment process, etc.

The Online Sales Negotiator is clearly a tool at the service of the consumer. It allows the customer to make fast purchases by negotiating with several product suppliers on specific product attributes at the same time. In other words, this agent automates the information search and evaluation of alternatives steps of the consumer buying process. The data required for this service is the consumer profile information. It performs a matching between products, profile and past sales data in order to analyse consumer response to past purchases.

Finally, the Shopping Recommender can be regarded as a personalized advertising tool which makes customized recommendations to consumers. It facilitates them in their buying process and at the same time serves as a promotion tool for the retailer and suppliers. Again, the combination of consumer, sales and navigation data is necessary in order to implement the targeted shopping recommendations and evaluate their effectiveness afterwards.

It should be clarified that the internet retailing data framework does not intend to be a detailed one, covering all the possible aspects. The objective here is to show how a virtual retail store needs to take into account the needs and demands of all partners involved (i.e. consumers, retailer and suppliers) and how these can be satisfied via the effective exploitation of the correct information.

## 5. CONCLUSIONS, MANAGERIAL IMPLICATIONS AND FUTURE RESEARCH PERSPECTIVES

As digital technology and consumer behaviour evolve, marketers need to continuously enhance the value of their digital marketing offering. In an interactive two-way addressable world, it is the consumer and not the marketer who decides with whom to interact, what to interact about and how if at all to interact. This requires marketers to acquire a good knowledge of consumer behaviour within such an environment and understand their habits and preferences. This should be done in order to market products and services that meet their needs. To this end, they have the technology capabilities on their side. The virtual retail environment provides them with an enormous amount of information they can use to enhance their understanding of the consumer (Turban et al., 1999).

The framework presented in this paper sets the initial basis for understanding this great potential. It clarifies the various types of information that exist in the virtual shopping environment and the way these can support consumer services and business processes. The ACTIVE project gives us a great opportunity to explore these possibilities in a real case context. However, the basic limitation of this study is that the proposed data framework was developed according to the needs and characteristics of the ACTIVE system. This implies that it may not be applicable in other business sectors (e.g. online banking, etc.). However, the robust methodological steps followed ensure that this framework can be effectively applied in online retailing. There it can be continuously revised and improved based on the empirical data provided through its application into real business conditions. Therefore, the contribution of the present study is summarized, on the one hand, on the internet retailing theory built through the development of the internet retailing data framework and, on the other hand, on the provision of direct managerial implications to virtual retailers.

The ACTIVE system and the corresponding internet retailing data framework introduced by the present study will be tested against real customers within the ‘ACTIVE SME’ Ten Telecom project of the European Commission, in 2003. The core objective of this project is to provide a reliable business plan for the initial market deployment of the ACTIVE platform. A large number of small and medium enterprises from the retail sector along with experienced internet shoppers will participate in this pilot project. The objective is to provide sound results towards launching the deployment phase of the ACTIVE system (i.e. market exploitation). It should be noted, however, that the internet retailing data framework discussed herein has already been tested against real customers during the ACTIVE project trials. The feedback provided (through focus groups) by customers, retailers and suppliers towards its improvement has already been included in the aforementioned discussion (sections 3 and 4).

In conclusion, it should be mentioned that there is still ample room for research in this area. The proposed framework is only a first step towards this direction. One of the research topics we will look at next is the investigation of characteristics that influence decisions on product promotion and advertising in the context of virtual retailing. Given the limited resources of a porta site, the topic includes the development of mechanisms required to resolve conflicts among the many suppliers. In that context, the application of auctioning mechanisms is also investigated.

## ACKNOWLEDGEMENTS

This study was partly funded by the ACTIVE project (EP 27046), ESPRIT Programme – Framework IV, Commission of the European Union.

## REFERENCES

Aldridge, D. (1998) Purchasing on the net – the new opportunities for Electronic Commerce. International Journa of Electronic Markets, 8, 1.

Bettman, J. (1979) An Information Processing Theory of the Consumer Choice. Addison-Wesley, Reading, MA.

Briggs, R. & Hollis, N. (1997) Advertising on the Web: is there response before click-through? Journal of Advertising Research, 37 (2), 33–45.

Bush, A.J., Bush, V. & Harris, S. (1998) Advertising perceptions of the Internet as a marketing communications tool. Journal of Advertising Research, 38 (2), 17–27.

CRP Report (1994) Continuous Replenishment: An ECR Best Practices Report. Joint Industry Project on Efficient Consumer Response.

ECR Europe Report (1999) How to Create Consumer Enthusiasm – Roadmap to Growth.

Engel, J.F., Blackwell, R.D. & Miniard, P.W. (1990) Consumer Behaviour. Dryden, Chicago, IL.

Falkou, X., Lytras, G., Pramataris, K.C. & Vrechopoulos, A.P. (1999) Putting the consumer on ‘TOP’: traditional online products store. In: Proceedings of the 7th European Conference on Information Systems Pries-Heie J., Ciborra, C., Kautz, K., Valor, J., Christiaanse, E., Avison, D. & Heje, C. (eds), pp. 142–155. Copenhagen Business School, Copenhagen, Denmark, 23–25 June.

Galliers, R. (1992) Choosing information systems research approaches. In: Information Systems Research: Issues, Methods and Practical Guidelines, Galliers, R. (ed.), pp. 144–162. Blackwell Scientific Publications, Oxford.

Hawkins, D.I., Best, R.J. & Coney, K.A. (1998) Consumer Behaviour-Building Marketing Strategy, 7th edn. McGraw-Hill. Boston. MA.

Hoffman, D.L. & Novak, T.P. (1997) A new marketing paradigm for Electronic Commerce. Information Society, 13, 43–54.

Hofstetter, J.S. & Corsten, D. (2002) Rethinking strategies for new value creation. International Commerce Review – ECR Journal, 2, 94–99.

Howard, J.A. (1989) Consumer Behaviour in Marketing Strategy. Prentice Hall, Englewood Cliffs, NJ.

Kannan, P.K., Chang, A.M. & Whinston, A.B. (1998) Marketing information on the I-way: data junkyard or information gold mine? Communications of the ACM, 41, 35–43.

O’Keefe, R.M. & McEachern, T. (1998) Web-based customer decision support systems. Communications of the ACM, 41, 71–78.

Pramataris, K.C., Vrechopoulos, A.P. & Doukidis, G.I. (2000b) The transformation of the promotion mix in the virtual retail environment: an initial framework and comparative study. International Journal of New Product Development and Innovation Management, 2, 163–178.

Pramataris, K.C., Vrechopoulos, A.P., Mylonopoulos, N., Papamichail, G. & Poylymenakou, A. (2000a) Personalised services and promotions in internet retailing. In: E-Business: Key Issues, Applications, Technologies, Stanford-Smith, B. & Kidd, P.T. (eds), pp. 796–802. IOS Press, Amsterdam.

Quelch, J.A. & Klein, L.R. (1996) The Internet and international marketing. Sloan Management Review, 37, 60– 75.

Rayport, J.F. & Sviokla, J.J. (1994) Managing in the mar ketspace Harvard Business Review 72 141-150

Roberts, M.L. (1997) Expanding the role of the direct marketing database. Journal of Direct Marketing, 11, 26–35.

Schønberger, V.M. (1999) The Cookie Concept, http:// www.cookiecentral.com/c\_concept.htm

Seifert, D. (2002) Collaborative Planning, Forecasting and Replenishment: How to Create a Supply Chain Advantage, SAP preprint edition. Galileo Press GmbH, Bonn.

Strauss, J. & Frost, R. (2001) E-Marketing, 2nd edn. Prentice Hall, Upper Saddle River, NJ.

Terpsidis, I.S., Moukas, A., Pergioudakis, B.Z. & Doukidis, G.I. (1998) The potential of electronic commerce in re-engineering consumer-retailer relationships through intelligent agents. Proceedings of the European Multimedia, Microprocessor Systems and Electronic Commerce Conference and Exposition (EMMSEC), pp. 35–47.

Turban, E., King, D., Lee, J., Warkentin, M. & Chung, H.M. (2002) Electronic Commerce: A Managerial Perspective. Prentice Hall – Pearson Education International, Upper Saddle River, NJ.

Turban, E., McLean, E. & Wetherbe, J. (1999) Information Technology for Management – Making Connections for Strategic Advantage, 2nd edn. John Wiley & Sons, Inc, New York, NY.

Vrechopoulos, A.P., Pramataris, K.C. & Doukidis, G.I. (1999) Utilizing information processing for enhancing value: towards a model for supporting business and con: sumers within an Internet retailing environment. Proceedings of 12th International Bled Electronic Commerce Conference, Bled, Slovenia, 7–9 June, pp. 424–438.

Vrechopoulos, A.P., Siomkos, G.J. & Doukidis, G.I. (2001) Internet shopping adoption by Greek consumers.

European Journal of Innovation Management, 4, 142– 152.

## Biography

Dr Adam P. Vrechopoulos is a Lecturer at the Athens Uni versity of Economics and Business (AUEB), Department of Management Science and Technology and Scientific Coordinator of the Digital Marketing and e-Customer Relationship Management (eCRM) research area at ELTRUN E-Business Research Center. His research and teaching areas are management of information systems, digital marketing, eCRM and electronic commerce. He holds a PhD in Electronic Commerce from Brunel University, UK, an MBA from ALBA, and a BSc in Information Systems from the Athens University of Economics and Business. He has published more than 20 papers in peer reviewed journals and international conferences and has acted as a reviewer for six international journals. He is the 2002 ‘Gold Award’ winner of the ECR Europe Academic Partnership Award. Before starting his academic career he worked in the industry in marketing and sales positions.

Katherine C. Pramataris is a PhD student at the Athens University of Economics and Business (AUEB), Department of Management Science and Technology. Her research is in the area of marketing information systems in the virtual business environment, focusing on the exploitation of data for supporting business decisions. Prior to that, she was employed by Procter and Gamble in the Management Systems Department, at their European Headquarters and in their Marketing Department in Greece.

Dr Georgios I. Doukidis is a Professor of Information Systems at the Athens University of Economics and Business (AUEB). Department of Management Science anc Technology and Visiting Professor at Brunel University. His research and teaching areas are information systems management, electronic commerce, decision-support sys tems and simulation He has published a total of 12 books and 90 research papers and has acted as guest editor for the Journal of the Operational Research Society, the Euro: pean Journal of Information Systems, the Journal of Information Technology and the International Journal of Electronic Commerce. He is the Director of ELTRUN E-Business Center

George D. Lekakos is a PhD candidate at the Athens University of Economics and Business (AUEB), Department of Management Science and Technology and Senior Research Officer at ELTRUN E-Business Center. His research is in the area of electronic commerce, focusing on the use of data mining techniques for the provision of per sonalized advertisements in the context of Interactive TV.
