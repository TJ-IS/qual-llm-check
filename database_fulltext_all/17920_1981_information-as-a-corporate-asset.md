---
otero_id: 17920
otero_key: "J54YUHNU"
title: "Information as a corporate asset"
authors: "R.C.Spinosa Cattela"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90023-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information as a Corporate Asset

R.C. Spinosa Cattela

Philips' Gloeilampenfabrieken, Eindhoven, the Netherlands

The author explains the need for and necessity of information for running a complex multinational company like Philips. He gives a short overview of the organization and structure of Philips, employing almost 400,000 people, and its world-wide activities. He deals with specific aspects and problems regarding the production, storage and distribution of a large range of Philips products, i.e., how this huge task was tackled in the early EDP days, and what difficulties and troubles had to be overcome. Gradually a new generation of managers has developed who are able to handle the possibilities of computers and automated information systems.

However, the multinational Philips covers thousands of separate units which cannot operate on their own. For business-information exchange they have to communicate in a well-defined language based on standardized data elements. Data-bases, in the future interconnected by a world-wide communications network, contain data that represent valuable and indispensable information for the Philips company: a real corporate asset.

With some reserve the writer dares to make predictions about the future of automation, yet mentions some clear trends and draws interesting conclusions.

Keywords: Information as Corporate Asset, Organization of Philips Company, Information systems & logistics control, Realtime Order Processing Systems (RETOPS), Problems in early EDP days, System implementation & psychological preparation, "Hard" data & "soft" data, Decision rules & human experience, Automated systems & users appreciation, Data communication in a multinational company, Standardization of Data Elements, Office for Data Element Standards (ODES), Future EDP trends, Database Manager, Security & privacy aspects.

## 1. Introduction

The philosopher Francis Bacon once wrote: "Preserve the right of thy place, but stir not questions of jurisdiction; and rather assume thy right in silence and de facto than voice it with claims and challenges". This is more or less how I approach this paper. Not to voice my right - if I have any at all -- with claims and challenges. Do not expect any spectacular new statements; I intend to explain, in a pragmatic way, how we look upon "Information as a Corporate Asset" in such a huge and complex company as Philips.

But before discussing the matter in more detail, I should like to make clear my definition of information and the relation between information and data. In the past, these words were often interchanged and

![](/api/attachments/J54YUHNU/fulltext/images/3615997b568e26fc268d2c59f0fcf980c103bee76526a8cbd7610300d854d1ab.jpg)

Mr. R.C. Spinosa Cattela was born in Eindhoven in 1923. He studied Economics at the Universities of Buenos Aires, Cape Town and Melbourne. He graduated in 1947 with the degree of Bachelor of Commerce. In 1956 he joined the Argentine Philips organization as an internal auditor, where he became in 1964 Financial and Administrative manager and member of the Management Committee. In 1971 he assumed this post in the Spanish

Philips organization. In 1974, Mr. Spinosa Cattela became manager of the Concern Accounting department of N.V. Philips' Gloeilampenfabrieken, Eindhoven, the Netherlands, and in 1976 member of the Board of Management (responsible for Accounting and Data Automation).

Other activities of Mr. Spinosa Cattela comprise: Member of the Board, later President of the Argentine-Netherlands Chamber of Commerce (1956–1970). From 1970 until 1974: Member of the Board of the Spanish – Netherlands Chamber of Commerce, and President of the Dutch School in Madrid. Since 1976 he has been member of the Tripartite Deliberation Committee on Accounting Standards. Mr. Spinosa Cattela has lectured in the Netherlands, the United Kingdom, Japan, Australia and South America, mainly on matters of accounting and budgetary control.

there was no need to make a distinction. But when information systems were automated, one came up against problems and gradually we had to define the word data as: facts, definitions or instructions, presented in such a way that they are suitable for communication, interpretation, or processing by men and by means of automated tools.

And, on the other hand we define information as: the meaning which people attribute to data by means of conventions, agreements, experience, or knowledge.

For instance, a distance given in kilometres is for most of us on the continent of Europe at least clear information. We know places about the same distance apart and we can compare them. However, for Europeans, the same distance given in miles says less: it is data which have to be transformed, namely divided by 1.609, to make it information. It is in this sense that the title of my speech should be understood. In a company billions of characters of data can be stored, but they are useless if they are not procured in good time, in the right place and in the correct shape to serve as information for those people in the organization that need them for doing their jobs.

Exchange of information and data are as old, or even older, than mankind. Communication, i.e., exchange of information, occurs not only among men, but also among higher species of animals — it is a characteristic feature of people and animals, living in groups, with a mutual social dependence. In the course of time many, more or less complicated, languages have been developed — firstly only in relation to concrete objects and actions, but later-on also offering the possibility of giving expression to abstract matters.

Formerly, data were only stored in human brains, and this is still largely the case today. Consequently data are linked to persons. Of course people can communicate data to others, thus enlarging the circle of people informed, but still the group remains very limited. Therefore, throughout the centuries, man has searched for means of bringing important data and information to the notice of large groups of people. One of these means is script. Many thousands of years ago, mankind started to store data in writing, in order to separate it from person and time. In the beginning, the great achievements of rulers were recorded for posterity, religious rituals were noted, and also commercial transactions (such as purchase and sales of land and cattle). In the course of time, the writing of data was extended to all areas of society and the invention of the art of printing has made it possible to distribute data to millions of people.

Then the computer with its numerous possibilities arrived on the scene. Designed for making complex calculations at high speed, it soon appeared that the computer could also be put to excellent use, not only for storing great quantities of data, but also for quick retrieval of the data needed for subsequent transformation and printing in the form required. Since, in most cases, the user was unable to indicate in advance exactly what he needed, everything that he could possibly need was provided in accordance with the telephone-directory method. The user was therefore regularly snowed under with files of computer print-outs, in which he had to find his information. As an illustration, I may mention that our Corporate Computer Centre the biggest but not the only Philips computer centre in the Eindhoven area, has printed for many years an average of 8 million lines per day and often more copies per page.

In fact, modern man is flooded with data, hardly knowing what to do with them and unable to use them as valuable information. But gradually technical means became available, offering the user possibilities to call up data at the moment in which they were needed and in the necessary form.

Before going further into the systems which, over the years, were developed in and by Philips for transforming data into information, I should describe something of the organization and structure of the Philips Company.

## 2. The Philips Environment

I assume that the Philips Company is known to the reader. The Company generally calls itself "a global enterprise", and it can be described as a Company manufacturing diversified electrical and electronic products.

The core of the Philips organization consists of two types of organizational units: Product Divisions and National Organizations (See fig. 1). Their area of competence covers the entire process which extends from research and product development, through manufacturing and sales, to providing service to our customers, but each plays a different role.

![](/api/attachments/J54YUHNU/fulltext/images/aa80c4a80499c30fee973417270a0def27e4d996e8fce72ce941a135c079f514.jpg)  
Fig. 1. Organization of the Philips Company.

Philips has six Product Sectors which are composed of 14 Product Divisions. These are primarily responsible for world-wide product policy. This includes development, production and marketing. The policy of the Product Divisions should be such as to enable the National Philips Organizations to make optimal use of the opportunities on the local market.

Philips has National Organizations in 64 different countries. So-called "direct sales" are carried out to a similar number of countries, but this is done through representatives and no "own" organization exists in these countries. The National Organizations are responsible for all the Philips' activities in their respective countries. It is their job to integrate these activities as fully as possible into the social conditions of their country and to ensure that they are embedded in the national situation.

There is a close parallel between the tasks of the Product Divisions and the National Organizations and they form part of an indivisible process.

In the past, Philips made products in a great many countries, nearly always exclusively for the local market. A radical change took place in the past twenty years due to the emergence of the European Common Market. The new situation made it necessary to establish International Product Centres, which also make products for markets outside national frontiers. The Concern Centre is located in Eindhoven, The Netherlands. At the hub of the activities of the Product Divisions, National Organizations, research laboratories, and central supporting staff departments is the Board of Management, this highest executive body in the Company. The Board of Management is responsible for long-term strategy, for decisions about large investments and for top-management appointments both in the Netherlands and abroad.

Turnover of Philips amounted to Df. 33 billion in 1979 or about \$ 16.5 billion. The world-wide work force counts almost 400,000 employees. Sixty-four percent of sales in 1979 were achieved in Europe (including the EEC), 17% in the U.S.A. and Canada, 7% in Latin America, 2% in Africa, 7% in Asia and 3% in Australia and New Zealand. From these figures, one can see that the emphasis of Philips' activities as a whole still remains in Europe.

As an international company it is essential for Philips to be in a position to participate in world markets, particularly the technology areas: Europe, Japan and the U.S.A. As we are basically a European company our position is firmly established here – our activities in the U.S.A. have been steadily growing, but Japan poses many problems.

Two other characteristics of our company are important. The first is that less than 10% of total turnover is achieved in our home country. The second is that more than 20% of the total work force is employed in the Netherlands (82,400) and a few tens of thousands are employed in each of the other large European countries.

To conclude this part, I will make a few remarks about our Company as a user of computers. Worldwide, the Philips company has a few thousand office and minicomputers in use – nearly all of our own brand – and at least 100 medium-sized and larger computer configurations. A large number of the latter belong to the Philips P1000 computer family, the production of which we were forced to stop some time ago. Although these P1000 computer systems run extremely well even today and give fewer problems than we ever had with other well-known brands, we nevertheless feel the need to replace our home-made computers by more modern equipment from other suppliers.

## 3. Some Information Systems and Logistics Control Aspects

It will be clear that, especially with the set-up of International Product Centres, perfect control of the flow of goods is of vital importance for the Company. This is often a problem in a factory that makes its own component parts for the production of finished articles. Therefore, one can imagine how much bigger this problem is for a multinational company like ours.

Each National Organization sells products originating from a range of different factories and assembled from parts made by several other factories, composed in turn of articles produced in other plants, etc. Moreover, these factories are located in different countries, and can be situated on different continents, with their own rules and regulations.

For years we have been busy working on the development of information systems for the control of logistics. In the beginning this was only done in a factory or even in one production department. But gradually the systems are being extended, covering a number of steps in the production chain.

It appears that, if production planning is made per factory and based on orders from other factories needing component parts, greater delays are caused in plants at the end of the chain due to unavoidable delivery delays. The managements of the factories concerned still hardly know what is happening on the sales front. We have found situations where factories have even increased their production of parts at a time when the finished articles in which they were used had been taken out of production. The same phenomenon occurs in a military column in which each driver reacts only to the behaviour of the truck in front. In practice, this means that the last vehicle either almost stands still or has to run at top speed, even if the first truck goes at a fairly constant speed.

Formerly the National Organizations usually ordered resale products directly from the factories that were situated in the same country. But since the time that products were concentrated in International Product Centres, this direct process has no longer been possible. Today, ordering is done by Central Planning Departments, one in each Product Division. These CPD' collect the orders from the National Organizations and order the total from the particular plant.

In the consumer product sector, many articles can be supplied from stock, and systems have been developed by which the CPD's are able to issue instructions that the goods ordered move from the factory store within 24 hours of receipt of the order. For big customers, the goods are shipped directly to their address, and I can cite cases, where, thanks to realtime systems, deliveries from the factory store in the Netherlands can be made quicker than delivery from the local commercial stores of the National Organization in the country of the customer. The reader may understand that these new possibilities and procedures have changed our stock-policy. It is no longer necessary to keep commercial stocks of all articles in all countries. They are supplied directly from Euro-stores or directly from plants. This policy has led to important savings and, moreover, the discipline of delivery has been considerably improved.

Realtime Order Processing Systems have also been implemented in the National Organizations, making it possible to inform a customer straight away if the articles needed can be delivered, and if not, when they will be available. Also, substitutes for products-out-of-stock can be suggested and, depending on the size of the country, the goods shipped can reach the customer's store within 1 to 3 days after ordering. Such fast deliveries were greatly appreciated, but today several big customers prefer a fully loaded truck at lower freight costs, even if that means a somewhat longer delivery time. The system records the volume of the goods ordered and signals when a truck can be completely filled. Besides a greater reliability of delivery and substantial cost savings, our systems also provide plenty of statistical data on request. Sales departments can now follow market trends closely, and react, wherever and whenever necessary, with directed actions resulting in a much greater effectiveness of salesmen visiting customers. The necessary information systems have not grown up overnight: they have cost 'blood, sweat and tears', not to speak of time and money, both at the users' end and in the EDP-departments. I shall briefly explain the main reasons why the early systems were unsuccessful.

## 4. Why Were the Early Systems Unsuccessful?

In the beginning EDP was very new and different to what managers (and in particular senior managers)

were accustomed to. It was, to a certain extent, frightening black magic, and many managers, already fully occupied by their normal activities, left the provision of data and information to the care of the EDP experts. These were young people as a rule, very intelligent, strongly attuned to logical and analytical thinking, and often without any experience with, or respect for, the social structures that exist in every organization. Their idea was to re-organise the world and its establishment with the aid of the new tools. Full of confidence, they started their task on what they saw as their mission. They built information systems, magnificent for that time, but unfortunately not in line with the requirements of the organization and reality. In fact, these early systems were the Towers of Babel in automation, creating numerous data which could not be recognized as valuable information for the users.

Learning from this kind of troubles and drawbacks, a generation of managers gradually developed with great interest in the new trend towards automation, knowing their organizations well, able to define their wishes and requirements, and taking into account the current possibilities of automation. Those managers were selected for new system developments, and then the snowball effect began: the successful manager promoted a system, invited colleagues to look at it, and demonstrated well-known applications, which also made the colleagues enthusiastic. The next system, using parts of the existing one, could be built and implemented in a much shorter time, and with less effort. One of the advantages of the Philips organization is clear: identical functions are frequently repeated in numerous plants and departments. Consequently, system experience can be passed on for further implementation in many places.

Nowadays EDP-systems run in all parts of the Company. Very much money has been invested in this software and it stands to reason that a system, once implemented, is seldom replaced by an entirely new system. Of course modifications, adaptations, and extensions regularly occur but this is done within the framework of keeping the systems up-to-date.

Furthermore, in the early days, poor psychological preparation of the system users contributed to the problems. Sometimes projects were wrongly directed or far too ambitious. This has left us with the good pragmatic rule, that an automation project should not last longer than one year from the first discussion with the user, up to and including complete implementation. Should the proposed project occupy more time than one year, a masterplan is made cutting the project up into functional pieces, each of which should be realized within one year.

Then, there was another problem. The computer was made for computing, and when we started to implement more administrative systems, we still wanted to make use of the computing feature as much as possible. The Central Computer unit could cope with large calculations in the time necessary to get data from the disc. In the Production Office, for instance, certain rules were used for calculating the quantity of products or components to be ordered from suppliers. Also, there was the theory of economic order series, calculated on the basis of Camp's formula, which was not easy to apply in practice. But the computer offered the possibility of calculating the quantity to be ordered as each order is processed. What happened? Stock-outs occurred totally unexpectedly for some products, and sudden delays occurred. What was the matter? Only "hard data", such as agreed planning figures, can be put into the computer. And the economic series were calculated in accordance with this. But the people in the Ordering Department were using "soft data" also: e.g., knowledge about sales reality as opposed to the planning figures, rumours about modification of products in the development laboratory, and delivery problems at the suppliers. Accordingly, people adapted the quantities to be ordered higher or lower than those indicated in the tables. In addition, people no longer felt the same responsibility as before, since everything was calculated automatically.

This kind of problems has given us much insight into what really happens in an organization. Things which we thought to be automatic, appeared in reality as subtle decision-procedures. Of course, one should not take away the possibility for a person to use knowledge and experience: thus, decision rules leading to automatic results are seldom built into our information systems. Suggestions for decisions are printed out, then the man who knows what rules are used in the computer program decides if the suggestions are valid for the case concerned. The person judges whether conditions are normal or not. If so, he signs his initials and puts in the approved data. If not, he indicates the alternative.

It is important that the calculation rules incorporated in the system are so simple that everybody who has to work with them understands them well, without confusion. Systems built this way are used with pleasure, since the user appreciates them as supporting the job: the system has been adapted to the working method, not the person to the system.

A further problem lies in the organization field. In order to keep such a big and complex organization as the Philips Company manageable, a separation of functions in the commercial, industrial, and financial/administrative areas was introduced long ago. Emphasis has shifted gradually from a strong national orientation towards international logistics management.

EDP-systems have been built for each of the functions and operational units, but as a consequence, parallel systems have come into being; these handle the same transaction in different ways. This has led to confusion, because the results are very often difficult to compare or are not comparable as all. Of course, this situation hampers internal and external communication in the Company. The matter is being given full attention, but solving the problem is by no means easy or simple.

Basically, the problems can be summarized as follows:

\- Data are often ill-defined and inconsistent, and therefore only meaningful to a specific function or group of people;

\- The variety of procedures in use for information exchange leads to errors, delays, and inefficiency;

\- On top of that, information exchange with external bodies becomes more and more complex and demanding, and is often different from internal communication.

If one wants to make full use of computer systems and data communication, this is a major organizational problem, which one has to solve before one is able to transform data into useful management information at all levels of the Company. Only then data and the information derived from it become, in my opinion, a Corporate Asset.

Before going into our approach I must tell about another problem, one which we have not yet solved. Formerly, it took weeks before reliable information about the business results was available and consequently certain decisions were taken late by management, sometimes too late. We had the firm conviction that if we could provide managers with the correct and reliable figures quickly, their decisions would also be taken in time. Unfortunately, this supposition was and is not always true.

Reliable data about market trends, sales, and stocks in different countries are readily available today, almost realtime, but if situations change, managers often hesitate to follow trends immediately. They are slow, in particular, for unpleasant measures such as decreasing production, firing staff, and/or closing down plants. Then, procedures appear to take too much time. For obvious reasons, pleasant decisions on positive measures, such as increasing production, hiring new personnel, or opening new plants, hardly ever cause problems, and managers are inclined to run ahead of the improving situation. In this respect, automated information systems have not offered much relief, and the question remains: how can reliable data, which do represent clear information, activate people to take proper action in the organization in good time?

## 5. Standardization of Data Elements

We now return to the problem of ill-defined and inconsistent information. This cannot be solved without a certain degree of standardization. When we consider that in the Philips Company thousands of separate units can be distinguished, each of which can, in principle, communicate with all the others (often via computers), it is clear that - without standardization - we will soon be facing a new computerized Tower of Babel.

Examples of communication problems range from apparently trivial difficulties, such as different interpretations of "Delivery Date", to the wider problems of satisfactorily defining a very wide variety of management control parameters, such as stock levels, efficiency, and yield parameters, prices, costs, etc. These difficulties are compounded by the variety of languages and jargon that are in use in our multinational Company.

In order to improve this situation, an Office for Data Element Standards has been established. This has as its prime task to define precisely information elements and their coded representations: so-called data elements. These may be seen as elements of a formal language, to be used for business information exchange at Company level, being consistent with external standards and suitable for automation purposes, if necessary.

The universal implementation of company-wide Standard Data Elements is a very difficult job, because in numerous offices and plants people must be retrained to work with the new definitions. Moreover, procedures must be adapted in some cases. The conclusion is that this is a very laborious, time-consuming and consequently expensive operation, but one that is absolutely necessary if we want to make full use of the data available within the Company.

## 6. Future Trends

Having described some of the things that we at Philips have achieved in the past years, and also about a number of problems. I should like to give also a glimpse of the future as we see it. But I must better temper the reader's high expectations of my views, because it is almost impossible to give a clear picture of precisely how a world-wide Company information network will appear, in say, five years.

As already stated, development and implementation of a formalized Company language will be tedious. We do not yet know the legal consequences of information exchange between countries. And what are the security aspects of such data networks?

On the other hand, we know that many things are technically possible already, but it will be necessary to adapt the organization to achieve meaningful applications. And this is a slow process, needing time, because people, especially older people, must learn to do new things, and to do the old familiar things which they have been doing for many years in a different way. Sometimes it is better to wait for the next generation before introducing change.

The reader will understand that such considerations make it even more difficult for me to give reliable predictions. However, some trends are clear:

1. Prices of computer hardware will go on decreasing. Computer suppliers have been able to halve the hardware prices of bigger systems every 4 to 5 years, offering (as a rule) a better performance.

2. It is only a few years since the appearance of the first micro-processor on a chip. Since then, technical science and production methods have continuously made progress, making it possible to put more transistor equivalents on one chip, raising the data processing speed at the same time. It is expected that these microprocessors will be used for a steadily increasing number of applications, and that ever greater production volumes will keep costs of microprocessors falling. Small mainframes of the early days are now available as mini- and microcomputers allowing the use of computer power on an ever wider scale.

3. As regards storage of data, price reductions will be even greater. Physical science and engineering are discovering new ways and means to realize ever growing storage densities of data, both in rotating magnetic memories and in semi-conductor devices. A reduction in cost by a factor of 10 for storage per bit has been realized every 5 years in the past decade.

4. In the field of data communication, technology is moving forward by leaps and bounds. Beside many existing private networks, public networks are coming into use in different countries. This trend is highly interesting for a great many users who need data communication for a limited quantity of messages at regular times.

5. Wages continue to increase, and it will become more advantageous to have employees work more efficiently with the aid of equipment that is priced lower and lower. Such tools will penetrate all departments of a company, including those hardly touched by automation to date, as for instance, the office.

What conclusions can be drawn from these trends? In former days EDP-equipment was very costly, rather unreliable, and operated only by specialists. For that reason it was logical for EDP-equipment to be concentrated in big computer centres. The computers themselves had to be used as much as possible, in two or better still, three shifts, in order to obtain a reasonable cost for data processing. But this meant that, besides the application software, much and difficult system software was required for controlling the entire computer configuration. Such system software, however, required a substantial part of the computer capacity itself. The set-up often became so complicated and so difficult to handle that mistakes, disturbances, and breakdowns could hardly be avoided. It is to be expected therefore that one will have to reconsider the philosophy of concentrating data processing on large mainframe computers.

Given the decreasing prices of mini and micro-computers and the better possibilities of data-communication networks, it may be expected that storage of data, as well as data processing, will be taken back to places where the work proper is being done. This will be the era of "distributed data bases" and "distributed processing". Much is being said about it at present, and many EDP-people are working to find good and reliable solutions. No doubt, positive results can be expected in the years to come.

The greatest modification, however, will not be technical, but of an organizational nature. This will be done by storing data in data bases with realtime access via display terminals, that will allow general users - without help from EDP personnel - to satisfy ad hoc requests for information and to "browse" through either internal data bases or data bases outside the Company. Such data bases will be interconnected by world-wide data communication networks. It will be an absolute necessity for all company data bases to be organized in the same way, so that the users can approach them consistently to obtain and combine the data required.

## 7. Security and Privacy

All this can be realized technically, and even at a reasonable cost, but there are a number of organizational problems. In every company more and more data are now being stored, both about their own activities as well as about the outside world. To start with, these data and information must be understandable, and to this end we need to implement unambiguous definitions.

However, further questions are then raised, e.g.: Who is allowed to input data? Who may change data? Who is authorized to obtain data? Typically, not everybody is entitled to have access to all data. For instance, in a personnel file, a distinction should be made between neutral data (such as name, address, marital status, etc.) and sensitive data (such as appraisal, salary, medical details, etc.).

A Database Manager will have to be appointed for most databases. He will be responsible for the proper use of the database by the various users. It is obvious that all data stored should be, and should remain, correct and up-to-date. Several organizational measures must be taken.

The application software making use of the data files will have to meet certain conditions with respect to internal control, to be defined by the Company's controllers. In general, it is advisable to maintain regular contact with the auditors at the system design stage, so that afterwards they can accept the results of the system in operation.

Security and privacy are to be taken very seriously, measures must be taken to prevent non-authorized people from retrieving confidential data, (e.g., by means of password control). Moreover, in case such data are transmitted by telephone lines, the system should be safeguarded against tapping, (e.g., with the aid of method like encrypting).

The general conclusion is clear: Data and the Information that can be derived from it will become a Corporate Asset for every company. And the companies which succeed in correctly organizing the development of this asset, will have a special edge on their rivals.

But, it will not be plain sailing. Either management will establish organizational control over these new technologies of database systems, data communications, small business computers, microcomputers, distributed processing, etc. Or, because of management's failure to grapple with the organizational challenge, these powerful tools - evermore readily available for less and less - will penetrate from different directions, and ultimately render improvements in data processing invalid.

## 8. Conclusion

In the literature a one-man business is sometimes pictured as ideal: the owner looking around in his shop can see at a glance how much raw material is in stock, how much work is in progress, and how many finished products are stacked on the shelves of his store. From this, the owner can decide immediately how much of what materials has to be ordered, what the next job will be, and for which articles to start a special sales campaign.

We, in Philips, are trying to achieve that situation in our large, complex organization so that the people

responsible at different levels of management obtain all necessary information when they need it. Of course, this is no longer possible by simply looking around, but it can be done by means of visual displays and simple query-languages for calling data onto the screen. That is the information they need for doing their jobs, and that is the kind of information that I consider a real Corporate Asset for our Company.
