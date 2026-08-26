---
otero_id: 12210
otero_key: "ZRQNTDCD"
title: "A permissioned blockchain-based implementation of LMSR prediction markets"
authors: "Arthur Carvalho"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113228"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

A Permissioned Blockchain-Based Implementation of LMSR Prediction Markets

Decision Support Systems

Arthur Carvalho

![](/api/attachments/ZRQNTDCD/fulltext/images/362e0ca002f35dc13b9fdbb4b0ed18faa2bf6c75debaf17325e2e0361660a167.jpg)

PII: S0167-9236(19)30257-X

DOI: https://doi.org/10.1016/j.dss.2019.113228

Reference: DECSUP 113228

To appear in: Decision Support Systems

Received date: 7 July 2019

Revised date: 17 October 2019

Accepted date: 27 November 2019

Please cite this article as: A. Carvalho, A Permissioned Blockchain-Based Implementation of LMSR Prediction Markets, Decision Support Systems (2019), https://doi.org/10.1016/ j.dss.2019.113228

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# A Permissioned Blockchain-Based Implementation of LMSR Prediction Markets

Arthur Carvalho Department of Information Systems and Analytics Farmer School of Business Miami University arthur.carvalho@miamioh.edu

Since the seminal work by Hanson (2003), the Logarithmic Market Scoring Rule (LMSR) has become the de facto market-maker mechanism for prediction markets. We suggest in this paper three potential issues with centralized implementations of LMSR, which we refer to as the availability, security, and privacy problems. We also explain how a permissioned blockchain-based implementation of LMSR efectively solves all the above problems. Following the design science research framework (Pefers et al. 2007), our main contribution is a fully functional permissioned blockchain-based implementation of LMSR that is ready to be deployed. We believe our results are of great value not only to prediction market researchers and practitioners looking for LMSR implementations, but also to blockchain professionals looking for fully developed solutions as well as applications of suitable research frameworks to guide blockchain research and development.

Key words : Blockchain; Design Science; Logarithmic Market Scoring Rule; Prediction Markets.

## 1. Introduction

Since its release by the elusive Satoshi Nakamoto (2008), Bitcoin has experienced a meteoric rise in popularity due to its appealing privacy, security, and decentralized aspects. This in turn has sparked a flurry of research on, for example, understanding what drives Bitcoin price and trading volume (Jerdack et al. 2018) and on technical issues surrounding the amount of electricity required to maintain the underlying network infrastructure (Foteinis 2018). Following in Bitcoin’s footsteps, thousands of other cryptocurrencies are now currently available for trading. At their core, the vast majority of the current cryptocurrencies rely on distributed, append-only ledgers that strongly use cryptographic and computer-networking techniques to ensure the safety and consensuality of the stored data. This ledger is now referred to as blockchain, a technology that promises to disrupt several business domains, from supply-chain (Wang et al. 2019) and finance (Fanning and Centers 2016) to healthcare (Yue et al. 2016) and accounting (Dai and Vasarhelyi 2017). One of the reasons for this excitement is that blockchain allows one to establish the provenance of an asset by simply looking through a list of previous transactions. The immutability property of blockchain ensures that transactions that are deemed as valid by network members can no longer be modified or deleted, which in turn enhances trust in the business process.

The original Bitcoin’s blockchain was designed to serve as a decentralized, public, append-only database. In particular, every network member has the right to read, verify, and potentially transact with others. As a public network, Bitcoin as well as several other cryptocurrencies are open to anyone. This means that transactions are not private, but users are anonymous in that they are identified by pseudorandom addresses. As the popularity of cryptocurrencies grew, so did the interest in applying blockchain to other business domains. However, the openness and anonymity of most cryptocurrencies’ blockchains are highly undesirable in many business applications. For example, the full accessibility, now referred to as the permissionless aspect of the network, might cause problems when companies want to, for example, treat customers distinctly by pricing the same product diferently. Moreover, the anonymity aspect is illegal in many domains where antimoney laundering and know-your-customer regulations must be obeyed.

Unlike permissionless blockchains, permissioned blockchains focus on business networks of known, vetted participants operating under a well-defined governance model. A primary goal of permissioned blockchains is to secure the transactions among a group of members who might not blindly trust each other. Knowing the identities of the participants allows permissioned blockchains to be more eficient, e.g., Bitcoin’s onerous proof-of-work consensus mechanism, which is often criticized due to being energy intensive (Foteinis 2018), can be replaced by more traditional Byzantine fault tolerance schemes. Another crucial aspect of permissioned blockchains is that participants do not necessarily have permission to retrieve information about all the transactions in the network. The above points imply that anonymity is efectively replaced by privacy in permissioned blockchains.

The development and deployment of permissioned blockchains have been boosted by open-source frameworks and tools. One of such tools, called Hyperledger Composer, enables organizations to quickly model and test blockchains in terms of assets, participants, transactions, and permission rules. At the time of writing, Hyperledger Composer is about two years old, meaning that many full-fledged projects are still under development. In this paper, we help to fill this gap by showing how to design a fully functional blockchain-based prediction market using Hyperledger Composer. In particular, we focus on the Logarithmic Market Scoring Rule (LMSR), the de facto market-maker mechanism for prediction markets (Hanson 2007). We argue later that centralized implementations of LMSR might sufer from three major issues, which we label as the availability, security, and privacy problems. We also carefully elaborate on why a permissioned blockchain-based implementation of LMSR can solve all the above-mentioned problems.

Although some authors have taken a more measured view of the potential and value of blockchain (Iansiti and Lakhani 2017), there is still a noticeable hype surrounding that technology. As such, we argue that a solid methodology that demonstrates the need and value of a blockchain solution is crucial to any research and/or development project. That said, design science is the methodology we use to guide our eforts. Specifically, we rely on the design science research methodology proposed by Pefers et al. (2007), which comprises six steps in a nominal sequence: 1) problem identification and motivation; 2) definition of the objectives for a solution; 3) design and development; 4) demonstration; 5) evaluation; and 6) communication. Throughout this paper, we exemplify how the first five phases of this framework can be adapted and used in a blockchain research project, whereas the last phase (communication) is represented by the paper itself. To reflect that, besides this introductory section, the rest of this paper is organized in line with the steps in the design science research methodology. The artifact resulting from our endeavors is a prediction-market model that is ready to be instantiated and deployed.

The above said, our objectives in this paper are threefold: 1) describe and motive the implementation of a fully-functional prediction-market model using permissioned blockchains; 2) further illustrate how to apply design science to develop blockchain models; and 3) illustrate how to use modern tools to model and evaluate permissioned blockchains. We believe our contributions are of great value to practitioners and researchers interested in understanding permissioned blockchains and/or looking for an efective way of developing LMSR prediction markets. Specifically, the popularity of public blockchains, such as Bitcoin and Ethereum, might have led some to believe that the data stored in a blockchain must be public and available to all. Our work illustrates that such a perspective is not true for permissioned blockchains. For example, we discuss how diferent traders (blockchain users) have diferent views of the data. This is crucial in applications such as supply chain where blockchain members, who are sharing some data, might also be competitors. Hence, there is a need to constrain the type and amount of data that is being shared. Regarding professionals interested in using prediction markets, we ofer in this paper a fully functional solution that has strong privacy and security guarantees and that is ready to be deployed, thus potentially cutting costs concerning development and/or consulting fees.

## 2. Problem Identification and Motivation

The first step in the design science research framework is to both define the specific research problem and justify the value of a solution (Pefers et al. 2007). Before doing so in Subsection 2.2, we first elaborate on important concepts related to prediction markets.

## 2.1. Logarithmic Market Scoring Rule

Prediction markets are mechanisms designed to elicit and aggregate the subjective beliefs of many traders regarding the outcome of a future event. By leveraging the wisdom of crowds, prediction markets have been successfully used to forecast film awards (Pennock et al. 2001), the result of presidential elections (Berg et al. 2008), sales numbers (Chen and Plott 2002), among many other applications. Recent years have seen a renewed interest in prediction markets by the information systems research community (Qiu et al. 2013, 2014, 2017) driven in large part by the impressive predictive accuracy of these markets as forecasting tools (Chen and Plott 2002, Berg et al. 2008).

In traditional prediction-market models, traders trade contracts (assets) whose payofs are tied to outcomes of a future event. We focus on Arrow-Debreu contracts that pay of \$1 if a certain outcome occurs and \$0 otherwise. Traders trade Arrow-Debreu contracts based on their personal beliefs. When the market closes, the market prices have predictive power in that they represent a collective estimate of how likely it is that future outcomes will occur. These market prices can be used in decision-making situations, thus making prediction markets a decision support system.

There are two traditional ways of organizing a prediction market. In a continuous double auction (CDA), the market maintains a list of both ofers to buy (bids) and ofers to sell (ask) some specific number of shares of a contract at given prices. Traders place their orders asynchronously, and a trade takes place when there is a match between buy and sell ofers. CDA markets often sufer from thin-market problems, i.e., the spread between the highest bid price and the lowest ask price, the so called bid-ask spread, can be wide. In practical terms, this means that significant trading activity might be restricted to a small set of popular events.

Market makers, the second traditional prediction-market mechanism, are (algorithmic) traders who are always ready to trade. In particular, any trader can trade with a market maker at any time as long as the former accepts the prices and costs posted by the latter. Consequently, market makers have a zero bid-ask spread. Since there are no outstanding ofers in this setting and no need to distinguish between asks and bids for the sake of matching ofers, we henceforth periodically use the generic term “transactions” when referring to either buy or sell operations.

It is fair to note that, although market markers have the potential to increase the number of trades since there is always a trader ready to trade, active participation is still an issue in diferen prediction markets. For example, it has been reported that by the 3rd quarter of 2017, Google had only 1,625 out of 23,000 employees placing a trade on its prediction market (Thompson 2012, page 90). Similarly, Best Buy’s prediction market had only 2,100 active traders out of 115,000 employees (Thompson 2012, page 105). These organizations incentivize participation by giving traders gift certificates, T-shirts, mugs, etc. Although active participation is crucial for the success of prediction markets, strategies to boost participation are beyond the scope of our work.

Hanson (2003) proposed market scoring rules, a family of algorithmic market makers based on proper scoring rules (Carvalho 2016). It has been shown that the most prominent market scoring rule, called the logarithmic market scoring rule (LMSR) (Hanson 2007), has very strong convergence properties (Carvalho 2017). Berg and Proebsting (2009) derived the necessary equations to implement an LMSR prediction market in terms of buying and selling Arrow-Debreu contracts. For example, the total cost of buying $x \ge 0$ contracts, whose current market price is $p \in [ 0 , 1 ]$ , is:

$$
C (b, p, x) = b \ln (p (e ^ {x / b} - 1) + 1)\tag{1}
$$

One can obtain the gains from selling contracts to the market maker by using negative values of x in Equation (1). The parameter b determines the liquidity of the market. In particular, the market prices move quickly (respectively, slowly) after every trade for small (respectively, high) values of b. For the sake of illustration, consider a company trying to predict whether a certain product will sell more than 50,000 units (outcome $\theta _ { 1 } )$ or not (outcome $\theta _ { 2 } )$ in the next month, meaning that $n = 2$ The initial market prices are $( p _ { 1 } , p _ { 2 } ) = ( 0 . 5 , 0 . 5 )$ . Assume the liquidity parameter $b = 2$ . Under these circumstances, the cost of purchasing one contract associated with $\theta _ { 1 }$ is $C ( 2 , 0 . 5 , 1 ) \approx 0 . 5 6$ . After buying one contract, the trader will receive \$1 (respectively, \$0) if $\theta _ { 1 }$ (respectively, $\theta _ { 2 } )$ occurs in the future. Nothing prevents traders from buying fractions (shares) of a contract. For example, the cost of buying 0.3 shares when the market price is 0.5 is equal to $C ( 2 , 0 . 5 , 0 . 3 ) \approx 0 . 1 6$ . This asset will pay out \$0.3 if the underlying outcome occurs. Naturally, market prices go up (respectively, down) whenever a trader buys (respectively, sells) shares. To update prices, the market maker keeps track of the number of sold contracts. Let $s _ { i }$ be the number of sold contracts associated with outcome $\theta _ { i }$ . The market price $p _ { i }$ associated with outcome $\theta _ { i }$ is then:

$$
p _ {i} = \frac {e ^ {\frac {s _ {i}}{b}}}{\sum_ {x = 1} ^ {n} e ^ {\frac {s _ {x}}{b}}}\tag{2}
$$

For the above sales-forecasting example, the new market prices after the purchase of one contract associated with outcome $\theta _ { 1 }$ is $( p _ { 1 } , p _ { 2 } ) \approx ( 0 . 6 2 , 0 . 3 8 )$ . If, thereafter, the trader sells 0.5 shares back to the market maker, then $s _ { 1 } = 1 - 0 . 5 = 0 . 5$ , and the market prices become $( p _ { 1 } , p _ { 2 } ) \approx ( 0 . 5 6 , 0 . 4 4 )$

## 2.2. Issues Faced by Centralized Implementations of LMSR

Conceptually, LMSR is centralized in nature since all the trades occur between traders and the market maker. However, we identify problems with a centralized LMSR implementation/deployment. Centralization in this context means that information about transactions and participants are stored and manipulated by a single computational device. First, if this device stops working, be it due to a malicious attack (such as a denial of service) or some hardware/software failure, then the prediction market will no longer be able to pay or receive money from traders since information about who owns what becomes unavailable. We refer to this issue as the availability problem.

The second issue with a centralized LMSR implementation is what we refer to as the security problem. Equation (2) shows that LMSR market prices are determined based on previous transactions. If one is able to modify the history of transactions, then s/he will be able to manipulate the market prices in order to get favorable trades and/or drive the market prices towards a desirable value. No matter the motivation for the attack, the market prices will no longer be of too much value since they do not represent the beliefs of the population of traders.

The next potential implementation issue we identify is called the privacy problem. In particular, traders in corporate settings might not be comfortable trading truthfully when their identities are accessible. Several high-profile prediction markets have faced similar issues. For example, a “... concern among Best Buy investors [prediction market traders] was that their managers might discover the identity of those who predicted a negative outcome. This concern diminished over time because participants were allowed to trade using pseudonyms ...” (Thompson 2012, page 102). Similarly, when Misys released its prediction market, “one reason traders stayed in is that they were allowed to use screen names.” (Thompson 2012, page 115).

The lack of privacy when trading might create undesirable consequences, such as traders overpaying for contracts whose outcomes are favorable to their companies. Relying only on pseudonyms might not entirely solve the above issue since traders could still be identified if the history of transactions is publicly available. For example, it has been shown that machine learning techniques are able to rather successfully classify diferent types of transactions coming from certain Bitcoin users (Yin et al. 2019). We argue that a similar approach could be used to discover the identities of anonymous traders in corporate prediction markets, where the number of participants are usually small and their real identities are often known to each other. As we discuss later, privacy when transacting is the key to solve the above problem, as opposed to anonymity.

An efective solution to the availability, security, and privacy problems might boost the trust a decision maker places on the market prices since they now better reflect the beliefs of the traders. We discuss in the following section the objectives and shape of an LMSR implementation that efectively deals with the availability, security, and privacy problems.

## 3. Definition of the Objectives for a Solution

The second step in the design science research framework is to “infer the objectives of a solution from the problem definition and knowledge of what is possible and feasible” (Pefers et al. 2007, page 55). To do so, we take a qualitative approach by describing how a new LMSR implementation tackles the problems we previously described. We start by noting that the redundancy created by distributed storage technologies can efectively solve the availability problem. For example, a redundant storage device can always replace a primary storage device in case of failures. However, those technologies do not immediately solve the security problem since the infrastructure ownership might still be centralized. A solution to both the availability and security problems is to use public, permissionless blockchains and store blocks of data on diferent nodes in a tamper-proof fashion. However, given the openness aspect of public blockchains, the privacy problem is still unsolved.

Permissioned blockchains, in turn, efectively solve the availability, security, and privacy problems. Having a prediction market on top of a blockchain means that all the data about transactions are stored in a decentralized fashion on an immutable data structure. Moreover, a permissioned blockchain allows for traders to have privacy, in a sense that other traders do not necessarily have access to the transactions involving a specific participant. We further motivate the use of a permissioned blockchain by following the decision model in Figure 1.

Figure 1 Decision model regarding blockchain adoption. Adapted from the work by W¨ust and Gervais (2018).  
![](/api/attachments/ZRQNTDCD/fulltext/images/0eca4a8aa43a9cfa15287bc17c3492e56b03608c7dba98bdf9d0b64ded85f588.jpg)

First and foremost, blockchain is all about storing data. If no data need to be stored, then no database is required, i.e., a blockchain is of no use. LMSR naturally must store transaction data to pay the traders when the market closes and to update market prices. Second, if only one writer/user exists, then a centralized database system, as opposed to a blockchain, provides better performance in terms of throughput and latency. In our specific problem, several traders should be able to propose transactions that will eventually be stored in the blockchain. Third, if a central, third party is trusted, then there is no need to use a blockchain. As we previously discussed, it might be too risky to run a centralized implementation of LMSR in that the central authority has the power to edit existing transactions, report inconsistent transactions, etc. By relying on a blockchain implementation, more than one entity will have access to a copy of the underlying data, including the history of transactions, thus decentralizing power and boosting trust. Finally, if the users all mutually trust each other, i.e., if they assume that no participant is malicious, then a database with shared write access is likely the most efective solution. Permissioned blockchains are more appropriate when participants are known, but do not fully trust each other. This is precisely the case with corporate prediction markets, which is our focus in this paper.

It is worth mentioning that some blockchain-based prediction markets have been recently proposed, e.g., Gnosis (2017), Augur (Peterson et al. 2018), and Stox (2018). An important aspect of these solutions is that they are implemented using a public blockchain, meaning that anyone can at any time join the blockchain. This implies that all the transactions and markets are public. This openness aspect can cause organizations to face legal issues with security regulators until the legal status of the markets is resolved. Our model, on the other hand, defines several permissions so that the market is accessible to only certain traders (e.g., employees). We argue that our model is more suitable for corporate prediction markets since organizations might not be willing to disclose which markets are currently open and/or the predictions being made regarding local afairs, e.g., whether a certain product will be released on time. Furthermore, the above-mentioned solutions are all built on top of the Ethereum blockchain platform. This means that all the trades are based on cryptocurrencies or tokens, such as Ether and Reputation. This naturally raises adoption concerns in that, in order to trade, traders have to learn about Ethereum-related concepts, such as wallets and gas fees. Relying on cryptocurrencies can also raise several legal issues since the underlying prediction markets might then be considered gambling mechanisms, which makes them illegal in many jurisdictions (Bell 2009). Our model, on the other hand, is agnostic regarding currencies. In particular, traders are assigned some currency units when they are added to system, which is in line with current practice. Google, for example, avoids possible violation of federal gambling laws by using a virtual currency called Goobles (Thompson 2012, page 89), and each trader receives a certain amount of Goobles periodically to invest. Finally, by relying on Ethereum, traders have to pay fees to get their transactions validated and executed by miners, i.e., the computational devices that maintain the blockchain infrastructure. We argue that forcing traders to pay fees might make the use of public blockchains unsuitable when it comes to the deployment of prediction markets tailored to the corporate world. The above said, to the best of our knowledge, our work suggests the first implementation of LMSR using permissioned blockchains.

## 4. Design and Development

The third step in the design science research framework is to design and create the underlying artifact (Pefers et al. 2007). We do so by using Hyperledger Composer, where the resulting artifact is called a business network archive (BNA). In what follows, we introduce Hyperledger Composer and explain the following: 1) how to model blockchain resources, such as assets, transactions, and participants of the blockchain network using Hyperledger Composer’s modeling language; 2) how to implement the logic of transactions using a JavaScript-like programming language; and 3) how to define permissions using Hyperledger Composer’s access control language. Our focus in this section and throughout the paper is on the design and development of blockchain as a back-end technology. Hence, there is no attempt to design front-end applications and/or graphical user interfaces.

## 4.1. Hyperledger Composer

Hyperledger Composer allows one to quickly prototype a blockchain model in terms of a business network where participants can transact with each. The resulting model is represented by a BNA file, which can be seen as the artifact produced by the design science research endeavor. The BNA file includes a metadata file, a network model file, a script file containing the logic of possible transactions, and an access control file defining user permissions. In this paper, we ignore the metadata file since its purpose is to simply describe what the composition and goals of the blockchain network are. As for the three files we focus on in this paper, first the network model file defines the assets of interest as well as the transactions and participants that can interact with those assets. The script file defines the logic of the transactions. The access control file contains the rules (permissions) that define the rights of the diferent participants and transactions in the business network. In what follows, we carefully describe the composition of each file.

## 4.2. Blockchain Network Model

Hyperledger Composer allows blockchain developers to model business networks using a high-level, domain-specific language called Composer Modeling Language. This language enables one to define the (blockchain) network resources, which include assets, transactions, and participants. All network model files must have a namespace that uniquely identifies the resources of a business network. In our work, that namespace is called LMSR. Figure 2 illustrates all the resources we define in our model. Each resource of type participant or asset must be identified by an attribute, which in turn are either primitive types, such as “o String traderId” and “o Double budget”, or references to other resources, such as “−− > Trader owner ”.

Figure 2 Business network model.  
![](/api/attachments/ZRQNTDCD/fulltext/images/c6efdbb8a5598e4d7787cc9932531fff6c0ff83dc6f47fb579101a03c296f52f.jpg)

Our model has two types (categories) of participants: Trader (Figure 2a) and MarketMaker (Figure 2b). Each instance of Trader is defined by two mandatory attributes: 1) a unique identifier; and 2) a budget. Clearly, this can be tailored to diferent domains in a sense that other attributes can be used to define traders, e.g., name, address, job, bank account, etc. Each instance of MarketMaker, in turn, is represented by: 1) a unique identifier; 2) a Boolean value determining whether the market is open, whose initial value is true; 3) a liquidity value, i.e., the parameter b in Equation (1) and (2); 4) a budget; 5) the current market prices, i.e., the probability vector $\left( p _ { 1 } , p _ { 2 } , \ldots , p _ { n } \right)$ in Equation (2); and 6) the current number of sold shares, i.e., the value $s _ { i }$ in Equation (2).

The only asset in the model is called Contract (Figure 2c), which is represented by: 1) a unique identifier; 2) the outcome predicted to occur; 3) the number of purchased shares (numberShares); and 4) a reference to the owner of the contract, which is of type Trader. As we further elaborate in the next subsection, each trader holds at most one contract per predicted outcome. Nonetheless, this does not prevent the trader from buying or selling multiple shares associated with an outcome. Specifically, a contract is created when a trader purchases shares related to an outcome for the first time. Thereafter, the attribute numberShares inside the created contract is updated whenever future purchases/sales of shares related to the underlying outcome occur.

Finally, the model allows for three diferent transactions. The first two (Figure 2d and 2e) enable a trader to buy/sell a given number of shares related to a forecasted outcome from/to a market maker. Finally, the market maker can close a market via the CloseMarket transaction (Figure 2f). When doing so, the market maker must specify the observed outcome. This is used when issuing payments to the traders. We note that the behavior of the transactions listed in Figure 2 must be specified, which is the topic of the following subsection.

## 4.3. Transactions

In the context of Hyperledger Composer, transactions are often referred to as smart contracts. Instead of an analogy to legal contracts with automated enforcement, a more modern perspective of a smart contract takes the idea of putting data in a secure ledger and extends it to computation. In other words, it is a consensus mechanism for the correct execution of a given algorithm. In our setting, this means that, for example, when a trader invokes the BuyShares transaction, then the underlying computations are executed by many members of the blockchain network. This efectively alleviates the previously discussed security problem in that even if a member of the network behaves maliciously and does not process the requested transaction as intended, the other network members might still behave honestly and produce the expected output.

Before explaining the logic of the transactions defined in Figure 2, it is important to first discuss the concept of registries. Each registry in Hyperledger Composer manages a set of resources stored in the blockchain, and each network resource has its own registry. For example, when adding a new participant of type Trader to the blockchain network, the information about that trader is stored in the blockchain via the Trader registry. Thereafter, one can retrieve information stored in the blockchain about a certain trader via the respective registry. Registries might allow users to create, retrieve, update, and delete data. As we shall see in the following subsection, one can set permissions on who can perform which of those operations. In this paper, we are interested in registries related to participants and assets. Specifically, as we discuss below, the proposed transactions need access to the Trader, MarketMaker, and Contract registries.

We are now in a position to discussion the behavior of the transactions we previously defined. For the sake of readability, we defer all the underlying JavaScript code to the appendix. First, the BuyShares transaction (Appendix A) defines the operation when a trader requests a certain number of shares from the market maker. The argument of the transaction, called tx, encapsulates the necessary information about the trader calling the transaction, the underlying market maker, the forecasted outcome, and the number of requested shares (see Figure 2d). The transaction logic starts by verifying whether the current market is open (line 2). If not, an error is issued (line 47). Otherwise, as in Equation (1), the transaction calculates the cost of buying the requested number of shares (lines 3 to 6). Thereafter, it is verified whether the trader’s budget is greater than the cost of buying the shares (line 8). If not, an error is issued (line 45). Otherwise, the trader’s budget is updated (line 9) and, to reflect this change on the blockchain, the Trader registry is also updated (lines 10 and 11). Next, the marker maker’s budget (line 13) and number of sold shares related to the forecasted outcome (line 14) are also updated. The next lines verify whether the trader purchased shares regarding the same outcome before. Specifically, we represent a contract’s identifier by the concatenation of the owner’s identifier and the forecasted outcome (line 17). For example, if Alice purchases shares related to the outcome represented by the (index) value 1, then the underlying contract’s identifier is “Alice 1”. Having a contract’s identifier, the transaction searches the Contract registry for that specific contract (line 18). If it does not exist (lines 20 to 27), then a new contract is created (line 22), and the respective attributes are defined, namely the number of shares (line 23), the contract’s owner (line 24), and the predicted outcome (line 25). Finally, the contract is added to the Contract registry (line 26). Alternatively, when a contract already exists (lines 28 to 32), the respective contract is retrieved from the Contract registry (line 29), and only the number of purchased shares is updated in that contract (line 30). Next, in lines 34 to 40, the market prices are updated as in Equation (2). Lastly, in lines 42 and 43, the MarketMaker registry is updated so that the blockchain reflects the changes previously made.

The SellShares transaction (Appendix B) defines the operation when a trader tries to sell shares to the market maker. The argument of the SellShares transaction, called tx, encapsulates informa tion about the trader calling the transaction, the underlying market maker, the forecasted outcome, and the number of ofered shares (see Figure 2e). The transaction starts by verifying whether the current market is open (line 2) and, if it is, it verifies whether a contract associated with the trader and predicted outcome exists, i.e., whether the trader purchased shares associated with the same outcome before (lines 3 to 7). If not, an error is issued (line 39). Otherwise, the transaction checks whether the number of previously purchased shares is greater than or equal to the number of shares the trader is trying to sell (line 10). If not, an error is issued (line 37). This means that no short-selling operations are allowed by our current model, but this can be easily changed by simply modifying a few lines of code. The following steps are quite similar to what we previously discussed regarding the BuyShares transaction. Specifically: 1) the cost (to the market maker) is calculated (lines 11 to 14); 2) the trader’s budget is updated (lines 16 to 18); 3) the underlying contract is updated so as to reflect the number of holding shares (lines 20 to 21); 4) the market maker’s budget and number of sold shares are updated (lines 23 and 24); 5) the new market prices are calculated (lines 26 to 32); and 6) the MarketMaker registry is updated (lines 34 to 35).

Finally, the CloseMarket transaction (Appendix C) is called by the market maker to close the market, meaning that no further BuyShares and SellShares transactions is thereafter allowed. The argument of the CloseMarket transaction, called tx, encapsulates only two attributes, namely the observed outcome and the underlying market maker (see Figure 2f). The transaction initially verifies whether the observed outcome is valid (line 2). It does so by checking whether there is a valid market price associated with that outcome. Thereafter, the transaction requests access to the relevant registries (lines 3 and 4) and retrieves all the existing contracts (line 5). For each one of those, the transaction verifies whether the predicted outcome in the contract is equal to the observed outcome (line 8). If it is, then the maker maker pays the contract owner the equivalent to the number of holding shares. The trader’s and market maker’s budgets as well as the Trader registry are updated in lines 11, 12, and 13. After iterating over all the contracts, the market maker is set as closed (line 16), and the MarketMaker registry is updated (lines 17 and 18).

The above transactions provide the basic functionality for creating an LMSR prediction market. As we previously mentioned, the logic of the transactions can be easily tailored to incorporate diferent market features, such as trading rounds, as well as more error checks to further capture unexpected and unwanted behavior. Naturally, the transactions also implicitly assume that certain permissions are in place. For example, only the market maker should be able to call the CloseMarket transaction, whereas only the owner of certain shares should be able to sell these shares via a SellShares transaction. We explain next all the permissions required by our blockchain model.

## 4.4. Access Control Policies

As we suggested above, diferent transactions and, broadly speaking, data access require setting up permissions. In permissioned blockchains, a solution developer can determine whether and when participants can read, write, update, and delete information about other participants, assets, and transactions. Hyperledger Composer allows one to determine a permission policy through a declarative language called Access Control Language (ACL). The rules in ACL are declared via key-value pairs. Currently, there are seven diferent types of keys that can be used in a rule:

• Description - states the description of the rule in plain language;

• Participant - type of participant afected by the rule. Syntax: namespace.ResourceName;

• Operation - type of operation allowed or denied by the rule (READ, CREATE, UPDATE, DELETE, or ALL);

• Resource - type of resource afected by the rule. Syntax: namespace.ResourceName;

• Transaction - whether or not the rule only applies to a specific transaction;

• Condition - defines the condition that triggers the rule. Syntax: JavaScript code;

• Action - describes the permission type (ALLOW or DENY).

In our specific domain, we define 18 diferent rules, which can be roughly categorized as rules related to traders, market maker, and the overall system. We next explain the rules by category.

4.4.1. Trader Rules. Starting with trader-related rules (Figure 3), the first two rules, referred to as TradersBuyShares and TradersSellShares, give traders the permission to create new BuyShares and SellShares transactions. Technically, these rules mean that only traders, but no market maker, can initiate (“CREATE”) those two transactions.

## Figure 3 Permission rules concerning traders.

```swift
(a) Rule TradersBuyShares
rule TradersBuyShares {
    description:"Traders can buy shares"
    participant:"LMSR.Trader"
    operation:CREATE
    resource:"LMSR.BuyShares"
    action:ALLOW
}

(b) Rule TradersSellShares
rule TradersSellShares {
    description:"Traders can sell shares"
    participant:"LMSR.Trader"
    operation:CREATE
    resource:"LMSR.SellShares"
    action:ALLOW
}

(c) Rule TradersContractBuy
rule TradersContractBuy {
    description:"Traders can create/update contracts via buy BuyShares"
    participant(p):"LMSR.Trader"
    operation:UPDATE, CREATE
    resource(r):"LMSR.Contract"
    transaction:"LMSR.BuyShares"
    condition:(p.traderId==r.owner.traderId)
    action:ALLOW
}

(d) Rule TradersContractSell
rule TradersContractSell {
    description:"Traders can update contracts via SellShares"
    participant(p):"LMSR.Trader"
    operation:UPDATE
    resource(r):"LMSR.Contract"
    transaction:"LMSR.SellShares"
    condition:(p.traderId==
    r.owner.traderId)
    action:ALLOW
}

(e) Rule TradersInfoBuy
rule TradersInfoBuy {
    description:"Traders can update personal info via BuyShares"
    participant(p):"LMSR.Trader"
    operation:UPDATE
    resource(r):"LMSR.Trader"
    transaction:"LMSR.BuyShares"
    condition:(p.traderId==
    r.traderId)
    action:ALLOW
}

(f) Rule TradersInfoSell
rule TradersInfoSell {
    description:"Traders can update personal info via SellShares"
    participant(p):"LMSR.Trader"
    operation:UPDATE
    resource(r):"LMSR.Trader"
    transaction:"LMSR.SellShares"
    condition:(p.traderId==
    r.traderId)
    action:ALLOW
}

(g) Rule TradersMMBuyShares
rule TradersMMBuyShares {
    description:"Traders can update market maker's info via BuyShares"
    participant:"LMSR.Trader"
    operation:UPDATE
    resource:"LMSR.MarketMaker"
    transaction:"LMSR.BuyShares"
    action:ALLOW
}

(h) Rule TradersMMSellShares
rule TradersMMSellShares {
    description:"Traders can update market maker's info via SellShares"
    participant:"LMSR.Trader"
    operation:UPDATE
    resource:"LMSR.MarketMaker"
    transaction:"LMSR.SellShares"
    action:ALLOW
}

(i) Rule TradersCanReadOwnContracts
rule TradersCanReadOwnContracts {
    description:"Traders can read their assets"
    participant(p):"LMSR.Trader"
    operation:READ
    resource(r):"LMSR.Contract"
    condition:(r.owner.traderId==p.traderId)
    action:ALLOW
}

(j) Rule TradersCanReadPersonalInfo
rule TradersCanReadPersonalInfo {
    description:"Traders can read personal info"
    participant(p):"LMSR.Trader"
    operation:READ
    resource(r):"LMSR.Trader"
    condition:(r.traderId==p.traderId)
    action:ALLOW
```

The third and fourth rules, namely TradersContractBuy and TradersContractSell, allow traders to update and/or create contracts only through a successful execution of BuyShares or SellShares transactions. The condition key in both rules requires that a trader must be the owner of the underlying contract, i.e., the trader can neither create a contract on behalf of another nor update contracts that belong to others. Looking at the transactions’ code, one can indeed see that BuyShares can either add to or update the Contract registry (Appendix A, lines 26 and 31), and that the SellShares transaction may update the Contract registry (Appendix B, line 35).

The next two rules, TradersInfoBuy and TradersInfoSell, allow traders to update information about themselves only via a successful execution of BuyShares or SellShares transactions. The condition key in both rules determines that a trader can only update his/her own information, as opposed to any information concerning another trader. The reason for these two rules is that a trader’s budget might be updated when that trader calls either the BuyShares or the SellShares transaction (see, respectively, line 9 in Appendix A and line 16 in Appendix B).

The seventh and eighth trader-related rules, named TradersMMBuyShares and TradersMMSell-Shares, allow traders to update information about the market maker via BuyShares and SellShares transactions. The rationale behind these two rules is that a market maker’s budget, number of sold shares, and market prices might be updated when a trader calls either the BuyShares (see lines 13, 14, and 39 in Appendix A) or the SellShares transaction (see lines 23, 24, and 31 in Appendix B).

Finally, the last two rules, TradersCanReadOwnContracts and TradersCanReadPersonalInfo, allow a trader (denoted by p) to retrieve information about his/her owned assets and personal information (denoted by r ). These two rules efectively use the condition key to verify that an asset (respectively, participant) r belongs to (respectively, equates to) a participant p. It is important to highlight that those rules do not grant traders the privilege to delete, update, or create assets or participants. This is desirable since some of these operations could be used to manipulate the prediction market by, for example, artificially increasing the number of owned contracts and/or a trader’s budget. Furthermore, the TradersCanReadOwnContracts and TradersCanReadPersonal-Info rules ensure privacy in that traders are not able to retrieve information about each other, thus solving the previously discussed privacy problem. We believe these two rules boost the perception that a trader can freely express his/her opinions when trading.

4.4.2. Marker Maker Rules. The next set of rules we show in Figure 4 are all related to the market maker. The first rule, MMCloseMarket, allows the market maker, and only the market

## Figure 4 Permission rules concerning the market maker.

```swift
(a) Rule MMCloseMarket
rule MMCloseMarket {
description:"Market maker can close market"
participant:"LMSR.MarketMaker"
operation:CREATE
resource:"LMSR.CloseMarket"
action:ALLOW
}

(b) Rule MMTCloseMarket
rule MMTCloseMarket {
description:"Market maker can read/update trader info via CloseMarket transaction"
participant:"LMSR.MarketMaker"
operation:READ, UPDATE
resource:"LMSR.Trader"
transaction:"LMSR.CloseMarket"
action:ALLOW
}

(c) Rule MMItselfCloseMarket
rule MMItselfCloseMarket {
description:"Market maker can update itself via CloseMarket transaction"
participant(p):"LMSR.MarketMaker"
operation:UPDATE
resource(r):"LMSR.MarketMaker"
transaction:"LMSR.CloseMarket"
condition:(p.marketMakerId==r.marketMakerId)
action:ALLOW
}

(d) Rule MMAccessToContracts
rule MMAccessToContracts {
description:"Allow market maker to read contracts via CloseMarket transaction"
participant:"LMSR.MarketMaker"
operation:READ
resource:"LMSR.Contract"
transaction:"LMSR.CloseMarket"
action:ALLOW
}

(e) Rule AllCanReadMMInfo
rule AllCanReadMMInfo {
description:"Allow all participants to read info about the market maker"
participant:"LMSR.*"
operation:READ
resource:"LMSR.MarketMaker"
action:ALLOW
}
```

maker, to call the transaction CloseMarket. The next rule, called MMTCloseMarket, allows the market maker to read and update information about traders via the CloseMarket transaction. This is required since the market maker might have to retrieve information about a trader and update the budget of that trader when the market closes (line 10 and 12 in Appendix C).

The third rule, named MMItselfCloseMarket, allows the market maker to update information about itself via a successful execution of the CloseMarket transaction. The condition key requires that the identifier of both the participant calling the transaction and the resource to be updated must be the same. This rule is required when the market closes since the market maker might update its own budget (see line 12 in Appendix C) and status (see line 16 in Appendix C).

The fourth rule, MMAccessToContracts, allows the market maker to read contracts, but not to create, delete, or update them via the CloseMarket transaction. This is required when the market closes and the market maker has to read contracts in order to issue payments (see line 5 in Appendix C). This rule also prevents the market maker from potentially deleting contracts in order to avoid issuing payments when the market closes. Finally, the rule AllCanReadMMInfo allows all participants to retrieve information about the market maker at any time, and not only

Figure 5 Permission rules concerning system administration.

(a) Rule SystemACL

(b) Rule NetworkAdminUser

rule NetworkAdminUser { description:"Grant business network administrators full access to user resources" participant:"org.hyperledger.composer.system.NetworkAdmin" operation:ALL resource:"\*\*" action:ALLOW }

(c) Rule NetworkAdminSystem

```groovy
rule NetworkAdminSystem {
    description:"Grant business network administrators full access to system resources"
    participant:"org.hyperledger.composer.system.NetworkAdmin"
    operation:ALL
    resource:"org.hyperledger.composer.system.*"
    action:ALLOW
}
```

through predefined transactions. This is clearly desirable since traders must have access to market prices in order to have a fully operational prediction market.

4.4.3. System Rules. Figure 5 defines the next set of rules, which are system and administrative rules. The first rule, called SystemACL, allows any participant of the blockchain network to access any resource under the org.hyperledger.composer.system namespace. This is required since any deployed BNA will be under that namespace and, hence, this rule allows participants to interact with the business network. The next two rules are about system administration. As we illustrate in the following section, a Hyperledger Composer blockchain system must always have an administrator. The second rule in Figure 5, named NetworkAdminUser, states that administrators (i.e., members of the org.hyperledger.composer.system.NetworkAdmin group) have full privileges in a recursive fashion to all the resources defined by any other user. If this is not always desirable, one can then set a condition key to limit the privileges of administrators, e.g., one can specify that administrators will no longer have such privileges after the first transaction is performed by any other user. Finally, similar to SystemACL, the third rule, called NetworkAdminSystem, states that administrators have access to all the blockchain system’s resources.

The 18 rules we previously discussed illustrate how permissioned blockchains drastically depart from public blockchains in that users might not have universal access to all the resources. For instance, anyone can see all the transactions by Bitcoin users at any time, even without being a Bitcoin user. Moreover, the rules also show that participants might have diferent privileges. As we argued in previous sections, these features are crucial to the proper functioning of blockchain in several business domains, including corporate prediction markets.

## 5. Demonstration & Evaluation

The fourth and fifth steps in the design science research framework are to demonstrate and evaluate the proposed artifact by observing how well it supports a solution to the defined problems (Peterson et al. 2018). The demonstration task might involve showing the use of the artifact in experiments, simulations, case studies, etc. In our particular case, we demonstrate the use of the permissioned blockchain-based implementation of LMSR via a simulation of a prediction market in a setting involving two outcomes. Such a simulation is performed using the blockchain development tool called Hyperledger Composer Playground, henceforth referred to only as Playground. In particular, Playground provides a web-based user interface that allows one to define (see Figure 6a) and test (see Figure 6b) a blockchain network.

The define component of Playground has four tabs (see the left panel in Figure 6a) where one can: 1) describe the blockchain network; 2) model the network resources as we did in Subsection 4.2; 3) define the logic of the transactions similar to our code in Subsection 4.3; and 4) define blockchain permissions as we suggested in Subsection 4.4. That said, one can replicate our simulations by simply adding the code we discussed in the previous section to the respective tabs in Playground.

Figure 6a (top right) also shows the logged in user, which in this case is the administrator of the network (admin). After defining the network resources, the logic of the transactions, and the appropriate permissions, one can simulate the deployment of the blockchain network by simply clicking on the “Deploy changes” button (see the lower left region of Figure 6a). After deployment, one is now able to test the blockchain network (see Figure 6b). In particular, the test component of Playground allows one to read, write, update, and delete data from the registries as diferent users based on the underlying permissions. In our specific case, Playground displays three registries since our model has two participant categories (MarketMaker and Trader ) and one asset type (Contract). From the test interface (Figure 6b), one can see that, for example, the MarketMaker registry is empty, which is expected since the blockchain network has just been deployed.

Figure 6 Hyperledger Composer Playground.  
(a) The Define tab  
(b) The Test tab  
![](/api/attachments/ZRQNTDCD/fulltext/images/abfbb6521258e57fdd4a3a8ed66f5dd8e3a42b3fbfc10bd0e7e2962a46304cde.jpg)

In order to highlight some features of our solution, we contrast our blockchain model with Augur<sup>1</sup> (Peterson et al. 2018), which is arguably the most popular blockchain-based prediction market implementation at the time of writing. As we discussed in Section 3, Augur is built on top of Ethereum, a public blockchain. This means that anyone can at any time create markets, visualize market prices, place transactions, and observe the identifiers of traders who placed transactions. In other words, unlike our solution, Augur is permissionless. To create a market on Augur, an Ethereum user has to specify several attributes, such as the gas fees, which in turn is the amount of money paid to Ethereum nodes responsible for maintaining the blockchain infrastructure. Moreover, the market creator has to define a “market creator fee”, i.e., a percentage over the winnings s/he will receive. This efectively implies that traders have to share a portion of their winnings with the market creator. Finally, the market creator has to pay using the cryptocurrency Ether to create a prediction market, which in turn requires a cryptocurrency wallet. We strongly argue that the openness aspect of Augur in conjunction with the requirement that traders and market creators must know about the inner workings of Ethereum might strongly hinder corporate adoption.

## Figure 7 Definition of the participants using the JSON format.

```json
(a) Participant MM
{
    "$class": "LMSR.MarketMaker",
    "marketMakerId": "MM",
    "openMarket": true,
    "liquidity": 100,
    "budget": 100,
    "marketPrices": [0.5, 0.5],
    "numberSoldShares": [0, 0]
}
(b) Participant Alice
{
    "$class": "LMSR.Trader",
    "traderId": "Alice",
    "budget": 100
}
(c) Participant Bob
{
    "$class": "LMSR.Trader",
    "traderId": "Bob",
    "budget": 100
}
```

We contrast the above with our model, where creating a prediction market simply resorts to creating a participant of type MarketMaker. All the resources in Hyperledger Composer are created using the JSON format (see Figure 7). The first key-value pair in each resource definition determines the category (class) of the resource. The following key-value pairs define the attributes of the resource respecting the model we outlined in Subsection 4.2. Using Playground as the network administrator, who has the permission to create participants (see the rule NetworkAdminUser in Figure 5), we create the first participant called MM (Figure 7a), which efectively defines the prediction market. That participant is of type MarketMaker. It is currently open for trades, has a liquidity parameter b = 100, an initial budget of \$100, initial market prices equal to 0.5, and 0 as the number of sold shares associated with each outcome. Note that when creating the market maker under our model, there is no need for any cryptocurrency or to deal with blockchain peculiarities.

In what follows, we visually describe a few tests concerning the accuracy of the transactions and permissions in our model. These few tests represent a small subset of the 108 behavior-driven development tests we performed for three diferent markets using the Cucumber testing framework. Other than the market maker, these tests have two other participants interacting with the prediction market/blockchain. These participants belong to the Trader category and have an initial budget of \$100 each. Their unique identifiers are, respectively, Alice (Figure 7b) and Bob (Figure 7c). The reason behind having two traders is to test the permissions regarding what these traders can see from each other. Otherwise, having a single trader would be enough to test the market operations since LMSR’s path-independence property means that a sequence of several trades by any number of traders can be represented as a single trade from a single trader (Carvalho 2017).

## Figure 8 Illustrative transaction calls coded using JSON.

```jsonl
(a) Alice buys 50 shares regarding outcome 0
{ "$class": "LMSR.BuyShares", "trader": "resource:LMSR.Trader#Alice", "marketMaker": "resource:LMSR.MarketMaker#MM", "forecastedOutcome": 0, "numberRequestedShares": 50}
(c) Bob buys 10 shares regarding outcome 1
{ "$class": "LMSR.BuyShares", "trader": "resource:LMSR.Trader#Bob", "marketMaker": "resource:LMSR.MarketMaker#MM", "forecastedOutcome": 1, "numberRequestedShares": 10}
(d) The market maker closes the market
{ "$class": "LMSR.CloseMarket", "observedOutcome": 0, "marketMaker": "resource:LMSR.MarketMaker#MM" }
```

## 5.1. Testing Transactions

We first exemplify the efectiveness and accuracy of the proposed blockchain model through four transactions: 1) Alice buys 50 shares regarding the outcome represented by the value “0”; 2) Alice then sells 30 shares regarding the same outcome; 3) Bob buys 10 shares regarding the outcome represented by the value “1”; and 4) the market maker closes the market. In practice, to perform the transactions, each trader must simply connect to the network by using a certificate provided by the admin user. This authentication process is often handled behind the scenes by the front-end application. Unlike Augur, there is no need for traders to have cryptocurrency wallets or to deal with specific aspects of the blockchain network, such as determining Ethereum’s gas fees.

Similar to how instances of network resources are defined, all the transaction calls must also be coded using the JSON format. In particular, the first key-value pair in each transaction call defines the type of the transaction (i.e., BuyShares, SellShares, or CloseMarket). The remaining key-value pairs define the arguments of the transaction as we outlined in Subsection 4.2. Figure 8 displays the JSON code used to call each one of the four illustrative transactions.

Focusing on the first transaction (Figure 8a), the transaction logic in Appendix A is executed in tandem by blockchain nodes after Alice calls the BuyShares transaction, which efectively changes

## Figure 9 Relevant JSON data after Alice buys 50 shares concerning outcome 0.

```txt
(a) Alice record
{ "$class":"LMSR.Trader", "traderId":"Alice", "budget":71.90701963798 }
```

the Trader, Contract, and MarketMaker registries. Figure 9 shows the relevant JSON data from those registries after the transaction is over. In particular, the budgets of Alice and the market maker are updated after the transaction calculates the cost of buying 50 shares according to Equation (1), i.e., C(100, 0.5, 50) ≈ 28.09. The market maker further updates: 1) its current number of sold shares to reflect the sale of the 50 shares; and 2) the market prices according to Equation (2), i.e., $\left( \frac { e ^ { \frac { 5 0 } { 1 0 0 } } } { e ^ { \frac { 5 0 } { 1 0 0 } } + e ^ { \frac { 0 } { 1 0 0 } } } , \frac { e ^ { \frac { 0 } { 1 0 0 } } } { e ^ { \frac { 5 0 } { 1 0 0 } } + e ^ { \frac { 0 } { 1 0 0 } } } \right) \approx ( 0 . 6 2 2 , 0 . 3 7 8 )$ . Finally, a new contract identified by Alice 0 is created to record the number of shares trader Alice currently holds.

In the second transaction (Figure 8b), trader Alice calls the SellShares transaction to sell 30 of the previously purchased shares. In practice, this might happen when, for example, a trader receives further information that leads to a revision of his/her personal belief regarding the occurrence of a future event. Similar to the previous transaction, this second transaction efectively changes the Trader, Contract, and MarketMaker registries. Figure 10 shows the relevant JSON data from those registries after the second transaction is over. The budgets of Alice and the market maker are updated after the transaction calculates the cost (to the market maker) of selling 30 shares, i.e., C(100, 0.622, −30) ≈ −17.59. The negative value encodes the money received by Alice. The market maker further updates: 1) its current number of sold shares to reflect the purchase of 30 shares; and 2) the market prices according to Equation (2), i.e., $\left( \frac { e ^ { \frac { 2 0 } { 1 0 0 } } } { e ^ { \frac { 2 0 } { 1 0 0 } } + e ^ { \frac { 0 } { 1 0 0 } } } , \frac { e ^ { \frac { 0 } { 1 0 0 } } } { e ^ { \frac { 2 0 } { 1 0 0 } } + e ^ { \frac { 0 } { 1 0 0 } } } \right) \approx ( 0 . 5 5 , 0 . 4 5 )$ . Finally, the contract identified by Alice 0 is updated to reflect the number of shares Alice currently holds. In the third transaction (Figure 8c), trader Bob calls the BuyShares transaction to buy 10 shares related to outcome 1. This transaction is rather similar to the first transaction by Alice in that it

## Figure 10 Relevant JSON data after trader Alice sells 30 shares concerning outcome 0.

```json
(a) Alice record
{ "$class":"LMSR.Trader", "traderId":"Alice", "budget":89.50083111784 }    { "$class":"LMSR.Contract", "contractId":"Alice_0", "forecastedOutcome":0, "numberShares":20, "owner":"resource:LMSR.Trader#Alice" }    { "$class":"LMSR.MarketMaker", "marketMakerId":"MM", "openMarket":true, "liquidity":100, "budget":110.49916888216465, "marketPrices": [ 0.549833997312478, 0.45016600268752216 ], "numberSoldShares":[20,0] }
```

Figure 11 Relevant JSON data after trader Bob buys 10 shares concerning outcome 1.  
```json
(a) Bob record
{
    "$class": "LMSR.Trader",
    "traderId": "Bob",
    "budget": 95.3742209308
}
(b) Bob_1 record
{
    "$class": "LMSR.Contract",
    "contractId": "Bob_1",
    "forecastedOutcome": 1,
    "numberShares": 10,
    "owner": "resource:LMSR.Trader#Bob"
}
(c) MM record
{
    "$class": "LMSR.MarketMaker",
    "marketMakerId": "MM",
    "openMarket": true,
    "liquidity": 100,
    "budget": 115.12494795136256,
    "marketPrices": [
    0.52497918747894,
    0.4750208125210601
],
    "numberSoldShares": [20, 10]
}
```

changes the Trader, Contract, and MarketMaker registries. Figure 11 shows the relevant JSON data from the above registries after that transaction is over. The budgets of Bob and the market maker are updated after the transaction calculates the cost of buying 10 shares, i.e., $C ( 1 0 0 , 0 . 4 5 , 1 0 ) \approx$ 4.63. The market maker then updates: 1) its current number of sold shares to reflect the sale of 10 shares; and 2) the market prices according to Equation (2), i.e., $\begin{array} { r l r } { \left( \frac { e ^ { \frac { 2 0 } { 1 0 0 } } } { e ^ { \frac { 2 0 } { 1 0 0 } } + e ^ { \frac { 1 0 } { 1 0 0 } } } , \frac { e ^ { \frac { 1 0 } { 1 0 0 } } } { e ^ { \frac { 2 0 } { 1 0 0 } } + e ^ { \frac { 1 0 } { 1 0 0 } } } \right) \approx } \end{array}$ (0.525, 0.475). Finally, the contract Bob 1 is created to reflect the shares trader Bob holds.

Finally, the market market closes the market by calling the CloseMarket transaction (Figure 8d). In our particular example, outcome 0 is the observed outcome and, hence, traders are paid based on whether they hold shares related to outcome 0. For example, Bob holds no share related to outcome 0 and, hence, that trader’s budget immediately before and after the market closes are the same. Alice, on the other hand, holds 20 shares related to outcome 0, which means that the market maker must pay her \$20 when the market closes. Figure 12 shows the final JSON data from relevant registries after the execution of the CloseMarket transaction.

Figure 12 Relevant JSON data after the market maker closes the market.  
```json
(a) Alice record
{
    "$class": "LMSR.Trader",
    "traderId": "Alice",
    "budget": 109.5008311179
}
(b) Bob record
{
    "$class": "LMSR.Trader",
    "traderId": "Bob",
    "budget": 95.3742209308
}
(c) MM record
{
    "$class": "LMSR.MarketMaker",
    "marketMakerId": "MM",
    "openMarket": false,
    "liquidity": 100,
    "budget": 95.12494795136256,
    "marketPrices": [
    0.52497918747894,
    0.4750208125210601
    ],
    "numberSoldShares": [20, 10]
}
```

## 5.2. Testing Permissions

The previous subsection illustrated the operation of the proposed blockchain-based implementation of LMSR. In this subsection, we illustrate the permissioned nature of our blockchain model. Specif ically, we focus on how diferent participants have diferent views of the final registries. We start by noting that in order to solve the previously discussed privacy problem, traders are not allowed ReadOwnContracts in Figure 3i). Figure 13a reflects this permission by showing a trader’s view of the Contract registry. In particular, trader Alice is only able to retrieve information about her own contract, namely Alice 0. Furthermore, due to the TradersCanReadPersonalInfo rule (see Figure 3j), Alice is only able to read information about herself (Figure 13b). This means that no trader is able to, for example, read information about another trader’s budget. In contrast, Augur allows anyone to visualize information about all the trades and traders since that information is open to all inside Ethereum, which in turn is a public blockchain.

Moving to the market maker’s view of the registries, we show in Figure 14 how the market maker neither has read access to contracts (Figure 14a) nor to traders’ personal information (Figure 14b). Recall that the access rules MMTCloseMarket and MMAccessToContracts in Figure 4 only give the market maker permission to access the above registries when executing the CloseMarket transaction. In real-life applications, we expect our model to be tailored to diferent domains and, consequently, to store more information about traders beyond their budgets. This subsection illustrates how such information is protected by being unavailable to others.

Figure 13 Trader Alice’s view of some registries.  
(a) Contract registry  
![](/api/attachments/ZRQNTDCD/fulltext/images/18c7c5eceb8b319b809fa4f48b914370eef30b86a43b09ce9a45d731bd4ad509.jpg)

(b) Trader registry  
![](/api/attachments/ZRQNTDCD/fulltext/images/54980e04c7585ce3b1213a952531d0e984a529c834b35ba0861bffacb418ddd1.jpg)  
Figure 14 The market maker’s view of some registries.

(a) Contract registry  
![](/api/attachments/ZRQNTDCD/fulltext/images/69773cae8d6212cf9e54b2b7243ab3f4c475444f37a9089be767b10370ed6944.jpg)

(b) Trader registry  
![](/api/attachments/ZRQNTDCD/fulltext/images/9f547269f51ec04bed31c6b7cad1e0c8b5884244764be4512dcc2c1bdc268494.jpg)

## 6. Conclusion

In this paper, we identified three issues with centralized implementations of LMSR prediction markets (Subsection 2.2). First, the availability problem states that the market might come to an end if it relies upon a single node, and that node becomes unavailable. We argued that a blockchainbased implementation of LMSR solves the availability problem by having all the data concerning transactions, participants, and assets stored in a distributed fashion. Hence, even if a single node fails, access to the prediction market can still be provided by other functioning nodes.

The second issue with a centralized LMSR implementation is what we referred to as the security problem. In particular, the node running the market maker can, for example, manipulate market prices by simply altering the history of transactions. Our blockchain solution makes similar manipulations less feasible since price updating, or any other transaction, are executed as smart contracts, i.e., the transactions are independently executed in tandem by network nodes. Any price manipulation would require some sort of collusion among such nodes, similar to the well-known 51% attacks in blockchain models that rely on proof-of-work consensus algorithms.

Finally, the third issue with centralized implementations of LMSR is the privacy problem. For instance, we mentioned that traders in corporate settings might not be comfortable trading truthfully and potentially betting against company-wide desirable outcomes when their identities are known. Our blockchain-based implementation deals with the privacy problem by defining appropriate permissions so that traders are not allowed to read personal information and/or information about current holdings of other traders. Moreover, the market maker is only allowed to read those information when explicitly calling a predefined transaction to close the market. Our blockchain model thus allow the prediction market to function without any unnecessary disclosure of private information. One can even make adjustments to the proposed transactions so as to issue real payments based on traders’ budgets without any human intervention.

Our blockchain model is an artifact produced by following the design science research methodology (Pefers et al. 2007). This methodology fits our purpose since, given the current hype surrounding the blockchain technology, we argue that the design and demonstration of the usefulness of a model should be a central component in experimental blockchain research. Hence, we believe that besides the proposed artifact, another contribution of our work is to show how to successfully apply a suitable research framework to guide blockchain research and development.

It is worth discussing some deployment aspects concerning our blockchain model. In general terms, a blockchain is an immutable transaction ledger maintained by a network of computational devices referred to as nodes. Each node stores blocks of transactions that have been validated by following a predefined consensus protocol. A blockchain model developed using Hyperledger Composer abstracts lower-level details and, instead, it emphasizes a business-centric vocabulary that allows for quick prototype creation and easy validation with key stakeholders. A BNA file created using Hyperledger Composer is usually deployed to a Hyperledger Fabric network, which in turn defines all the lower-level network, computational, and cryptographic details. That said, an important deployment-related question is: which entities should be the blockchain network nodes? We argue that traders should not necessarily be network nodes, otherwise each one would need a computational device available throughout the whole duration of the market. This might not be feasible for a market trying to predict events far of in the future. We suggest instead that the organization(s) implementing the blockchain LMSR model should use dedicated internal or even external (e.g., cloud-based) devices as nodes of the network. For example, each department or branch of an organization could have its own node, which in turn would instantiate the same BNA file and provide the appropriate interface through application programming interfaces (APIs) for the end users (traders) to interact with the blockchain. In this case, the end users, such as Alice and Bob in Section 5, would simply require a suitable graphical interface that could be accessed from devices such as smartphones or personal computers.

As future work, it is worth investigating whether blockchain-based implementations of prediction markets lead to more accurate predictions. For our particular implementation, we argue that the market prices are less prone to manipulations due to our solution explicitly dealing with the availability and security problems. Moreover, by solving the anonymity problem, we ensure that traders have the freedom to trade without being concerned about potential retaliations. These points lead us to conjecture that our blockchain-based implementation results in more accurate forecasts, although it is clear that experimental work must be performed to (in)validate this claim.

## References

Bell, T. W. (2009). Private Prediction Markets and the Law. The Journal of Prediction Markets, 3(1):89–110. Berg, H. and Proebsting, T. A. (2009). Hanson’s Automated Market Maker. The Journal of Prediction Markets, 3(1):45–59.

Berg, J., Forsythe, R., Nelson, F., and Rietz, T. (2008). Results from a Dozen Years of Election Futures Markets Research. In Plott, C. A. and Smith, V. L., editors, Handbook of Experimental Economic Results, volume 1, pages 742–751. North Holland.

Carvalho, A. (2016). An Overview of Applications of Proper Scoring Rules. Decision Analysis, 13(4):223–242.

Carvalho, A. (2017). On A Participation Structure that Ensures Representative Prices in Prediction Markets. Decision Support Systems, 104:13–25.

Chen, K.-Y. and Plott, C. R. (2002). Information Aggregation Mechanisms: Concept, Design and Implementation for a Sales Forecasting Problem. Technical Report 1131, California Institute of Technology, Division of the Humanities and Social Sciences.

Dai, J. and Vasarhelyi, M. A. (2017). Toward Blockchain-Based Accounting and Assurance. Journal of Information Systems, 31(3):5–21.

Fanning, K. and Centers, D. P. (2016). Blockchain and its Coming Impact on Financial Services. Journal of Corporate Accounting & Finance, 27(5):53–57.

Foteinis, S. (2018). Bitcoins Alarming Carbon Footprint. Nature, 7691(554):169–169.

Gnosis (2017). Gnosis Whitepaper. Retrieved from: https://gnosis.pm/assets/pdf/gnosis-whitepaper. pdf. Last accessed: December 2, 2019.

Hanson, R. (2003). Combinatorial Information Market Design. Information Systems Frontiers, 5(1):107–119.

Hanson, R. (2007). Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation. The Journal of Prediction Markets, 1(1):3–15.

Iansiti, M. and Lakhani, K. R. (2017). The Truth About Blockchain. Harvard Business Review, 95(1):118– 127.

Jerdack, N., Dauletbek, A., Divine, M., Hult, M., and Carvalho, A. (2018). Understanding What Drives Bitcoin Trading Activities. In Proceedings of the 2018 Annual Meeting of the Decision Sciences Institute, pages 1864–1872.

Nakamoto, S. (2008). Bitcoin: A Peer-to-Peer Electronic Cash System. Retrieved from: https://bitcoin. org/bitcoin.pdf. Last accessed: December 2, 2019.

Pefers, K., Tuunanen, T., Rothenberger, M. A., and Chatterjee, S. (2007). A Design Science Research Methodology for Information Systems Research. Journal of Management Information Systems, 24(3):45–77.

Pennock, D. M., Lawrence, S., Giles, C. L., and Nielsen, F. A. (2001). The Real Power of Artificial Markets. Science, 291(5506):987–988.

Peterson, J., Krug, J., Zoltu, M., Williams, A. K., and Alexander, S. (2018). Augur: a Decentralized Oracle and Prediction Market Platform. Retrieved from: https://github.com/AugurProject/whitepaper/ blob/master/english/whitepaper.pdf. Last accessed: December 2, 2019.

Qiu, L., Cheng, H. K., and Pu, J. (2017). Hidden Profiles in Corporate Prediction Markets: The Impact of Public Information Precision and Social Interactions. MIS Quarterly, 41(4):1249–1273.

Qiu, L., Rui, H., and Whinston, A. (2013). Social Network-Embedded Prediction Markets: The Efects of Information Acquisition and Communication on Predictions. Decision Support Systems, 55(4):978–987.

Qiu, L., Rui, H., and Whinston, A. B. (2014). Efects of Social Networks on Prediction Markets: Examination in a Controlled Experiment. Journal of Management Information Systems, 30(4):235–268.

Stox (2018). Stox Platform for Prediction Markets. Retrieved from: https://resources.stox.com/ stox-whitepaper.pdf. Last accessed: December 2, 2019.

Thompson, D. N. (2012). Oracles: How Prediction Markets Turn Employees into Visionaries. Harvard Business Press.

Wang, Y., Han, J. H., and Beynon-Davies, P. (2019). Understanding Blockchain Technology for Future Supply Chains: A Systematic Literature Review and Research Agenda. Supply Chain Management: An International Journal, 24(1):62–84.

W¨ust, K. and Gervais, A. (2018). Do You Need a Blockchain? In 2018 Crypto Valley Conference on Blockchain Technology, pages 45–54.

Yin, H. H. S., Langenheldt, K., Harlev, M., Mukkamala, R. R., and Vatrapu, R. (2019). Regulating Cryptocurrencies: A Supervised Machine Learning Approach to De-Anonymising the Bitcoin Blockchain. Journal of Management Information Systems, 36(1):37–73.

Yue, X., Wang, H., Jin, D., Li, M., and Jiang, W. (2016). Healthcare Data Gateways: Found Healthcare Intelligence on Blockchain with Novel Privacy Risk Control. Journal of Medical Systems, 40(218).

## Appendix. JavaScript Code for the Transactions

## A. BuyShares Transaction

```javascript
async function BuyShares(tx) {
    if(tx.marketMaker.openMarket == true) {
    const b = tx.marketMaker.liquidity;
    const p = tx.marketMaker.marketPrices[tx.forecastedOutcome];
    const x = tx.numberRequestedShares;
    const cost = b * Math.log(p * (Math.exp(x/b) - 1) + 1);

    if(tx.trader.budget >= cost) {
    tx.trader.budget -= cost;
    const traderRegistry = await getParticipantRegistry("LMSR.Trader");
    await traderRegistry.update(tx.trader);

    tx.marketMaker.budget += cost;
    tx.marketMaker.numberSoldShares[tx.forecastedOutcome] += tx.numberRequestedShares;

    const contractRegistry = await getAssetRegistry("LMSR.Contract");
    const contractId = tx.trader.traderId + "_" + tx.forecastedOutcome;
    const contractExists = await contractRegistry.exists(contractId);

    if(!contractExists) {
    const factory = getFactory();
    var newContract = factory.newResource("LMSR", "Contract", contractId);
    newContract.numberShares = tx.numberRequestedShares;
    newContract.owner = tx.trader;
    newContract.forecastedOutcome = tx.forecastedOutcome;
    await contractRegistry.add(newContract);
    }
    else {
    var contract = await contractRegistry.get(contractId);
    contract.numberShare += tx.numberRequestedShares;
    await contractRegistry.update(contract);
    }

    var denominator = 0;
    for (i = 0; i < tx.marketMaker.numberSoldShares.length; i++) {
    denominator += Math.exp(tx.marketMaker.numberSoldShares[i]/b);
    }
    for (i = 0; i < tx.marketMaker.numberSoldShares.length; i++) {
    tx.marketMaker.marketPrices[i] = Math.exp(tx.marketMaker.numberSoldShares[i]/b)/denominator;
    }

    const marketMakerRegistry = await getParticipantRegistry("LMSR.MarketMaker");
    await marketMakerRegistry.update(tx.marketMaker);
    }
    else { throw new Error("Not enough funds to cover the transaction"); }
    } else { throw new Error("The market is closed"); }
```

## B. SellShares Transaction

```javascript
async function SellShares(tx) {
    if(tx.marketMaker.openMarket == true) {
    const contractRegistry = await getAssetRegistry("LMSR.Contract");
    const contractId = tx.trader.traderId + "_" + tx.forecastedOutcome;
    const contractExists = await contractRegistry.exists(contractId);

    if(contractExists) {
    var contract = await contractRegistry.get(contractId);

    if(contract.numberShares >= tx.numberRequestedShares) {
    const b = tx.marketMaker.liquidity;
    const p = tx.marketMaker.marketPrices[tx.forecastedOutcome];
    const x = -1 * tx.numberRequestedShares;
    const cost = b * Math.log(p * (Math.exp(x/b) - 1) + 1);

    tx.trader.budget -= cost;
    const traderRegistry = await getParticipantRegistry("LMSR.Trader");
    await traderRegistry.update(tx.trader);

    contract.numberShares -= tx.numberRequestedShares;
    await contractRegistry.update(contract);

    tx.marketMaker.budget += cost;
    tx.marketMaker.numberSoldShares[tx.forecastedOutcome] -= tx.numberRequestedShares;

    var denominator = 0;
    for (i = 0; i < tx.marketMaker.numberSoldShares.length; i++) {
    denominator += Math.exp(tx.marketMaker.numberSoldShares[i]/b);
    }
    for (i = 0; i < tx.marketMaker.numberSoldShares.length; i++) {
    tx.marketMaker.marketPrices[i] = Math.exp(tx.marketMaker.numberSoldShares[i]/b)/denominator;
    }

    const marketMakerRegistry = await getParticipantRegistry("LMSR.MarketMaker");
    await marketMakerRegistry.update(tx.marketMaker);
    }
    else { throw new Error("Not enough shares to sell"); }
    } else { throw new Error("No shares were purchased before"); }
    } else { throw new Error("The market is closed"); }
}

C. CloseMarket Transaction

async function CloseMarket(tx) {
    if(tx.marketMaker.marketPrices[tx.observedOutcome] != undefined) {
    const traderRegistry = await getParticipantRegistry("LMSR.Trader");
    const contractRegistry = await getAssetRegistry("LMSR.Contract");
    const allContracts = await contractRegistry.getAll();

    for (const contract of allContracts) {
    if(tx.observedOutcome == contract.forecastedOutcome) {
    const ownerId = contract.owner.getIdentifier();
    const owner = await traderRegistry.get(ownerId);
    owner.budget += contract.numberShares;
    tx.marketMaker.budget -= contract.numberShares;
    await traderRegistry.update(owner);
    }
    }
    tx.marketMaker.openMarket = false;
    const marketMakerRegistry = await getParticipantRegistry("LMSR.MarketMaker");
    await marketMakerRegistry.update(tx.marketMaker);
    }
    else { throw new Error("Invalid outcome"); }
}
```

## 4. Highlights

• Three issues with centralized implementations of LMSR are identified

• A permissioned blockchain-based implementation of LMSR can solve the above issues

• We propose a ready-to-deploy permissioned blockchain-based implementation of LMSR

![](/api/attachments/ZRQNTDCD/fulltext/images/b482f63914565c7571c0524c730d61937b0eedaa4889d1a6dcc6aff5e72951bc.jpg)  
Figure 1

```swift
(a) Participant Trader
    participant Trader
    identified by traderId {
    o String traderId
    o Double budget
    }

(d) Transaction BuyShares
transaction BuyShares {
    --> Trader trader
    --> MarketMaker marketMaker
    o Integer forecastedOutcome
    o Double numberRequestedShares
}

(b) Participant MarketMaker
participant MarketMaker
identified by marketMakerId {
    o String marketMakerId
    o Boolean openMarket default = true
    o Double liquidity
    o Double budget
    o Double[] marketPrices
    o Double[] numberSoldShares
}

(e) Transaction SellShares
transaction SellShares {
    --> Trader trader
    --> MarketMaker marketMaker
    o Integer forecastedOutcome
    o Double numberRequestedShares
}

(c) Asset Contract
asset Contract
identified by contractId {
    o String contractId
    o Integer forecastedOutcome
    o Double numberShares
    --> Trader owner
}

(f) Transaction CloseMarket
transaction CloseMarket {
    o Integer observedOutcome
    --> MarketMaker marketMaker
}
```

```swift
(a) Rule TradersBuyShares (b) Rule TradersSellShares (c) Rule TradersContractBuy
rule TradersBuyShares {    rule TradersSellShares {    rule TradersContractBuy {    rule TradersContractSell {    rule TradersInfoBuy {    rule TradersInfoSell {    rule TradersMMBuyShares
    rule TradersMMBuyShares {    rule TradersMMSellShares
    rule TradersCanReadOwnContracts {    rule TradersCanReadPersonalInfo {    rule TradersCanReadPersonalInfo
    rule TradersCanReadOwnContracts {    rule TradersCanReadPersonalInfo {    rule TradersCanReadPersonalInfo
    rule TradersCanReadOwnContracts {    rule TradersCanReadPersonalInfo {    rule TradersCanReadPersonalInfo
    rule TradersCanReadOwnContracts {    rule TradersCanReadPersonalInfo {    rule TradersCanReadPersonalInfo
    rule TradersCanReadPersonalInfo {    rule TradersCanReadPersonalInfo
    rule TradersCanReadPersonalInfo {    rule TradersCanReadPersonalInfo
    rule TradersCanReadPersonalInfo {    rule TradersCanReadPersonalInfo
    rule TradersCanReadPersonalInfo {    rule TradersCanReadPersonalInfo
    rule TradersCanReadPersonalInfo {    rule TradersCanReadPersonalInfo
    rule TradersCanReadPersonalInfo {  }
}
```

```swift
(a) Rule MMCloseMarket
rule MMCloseMarket {
description:"Market maker can close market"
participant:"LMSR.MarketMaker"
operation:CREATE
resource:"LMSR.CloseMarket"
action:ALLOW
}

(b) Rule MMTCloseMarket
rule MMTCloseMarket {
description:"Market maker can read/update trader info via CloseMarket transaction"
participant:"LMSR.MarketMaker"
operation:READ, UPDATE
resource:"LMSR.Trader"
transaction:"LMSR.CloseMarket"
action:ALLOW
}

(c) Rule MMI itselfCloseMarket
rule MMI itselfCloseMarket {
description:"Market maker can update itself via CloseMarket transaction"
participant(p):"LMSR.MarketMaker"
operation:UPDATE
resource(r):"LMSR.MarketMaker"
transaction:"LMSR.CloseMarket"
condition:(p.marketMakerId==
    r.marketMakerId)
action:ALLOW
}

(d) Rule MMAccessToContracts
rule MMAccessToContracts {
description:"Allow market maker to read contracts via CloseMarket transaction"
participant:"LMSR.MarketMaker"
operation:READ
resource:"LMSR.Contract"
transaction:"LMSR.CloseMarket"
action:ALLOW
}

(e) Rule AllCanReadMMInfo
rule AllCanReadMMInfo {
description:"Allow all participants to read info about the market maker"
participant:"LMSR.*"
operation:READ
resource:"LMSR.MarketMaker"
action:ALLOW
}
```

```txt
(a) Rule SystemACL (b) Rule NetworkAdminUser   
rule SystemACL { rule NetworkAdminUser { description:"Grant business network administrators participant:"org.hyperledger.composer.system.Participant" full access to user resources participant:"org.hyperledger.composer.system.NetworkAdmin" operation:ALL resource:"**" action:ALLOW }   
}   
(c) Rule NetworkAdminSystem   
rule NetworkAdminSystem { description:"Grant business network administrators full access to system resources participant:"org.hyperledger.composer.system.NetworkAdmin" operation:ALL resource:"org.hyperledger.composer.system."action:ALLOW }
```

## (a) The Define tab

## (b) The Test tab

![](/api/attachments/ZRQNTDCD/fulltext/images/33fffb678937f269eeee964d71c05f07bea16ae213f52a9c1f1d02b48e085356.jpg)

<table><tr><td>Web prediction-markets</td><td>Define</td><td>Test</td><td>admin</td></tr><tr><td>PARTICIPANTS</td><td colspan="2">Participant registry for LMSR.MarketMaker</td><td>+ Create New Participant</td></tr><tr><td>Marketemaker</td><td colspan="2"></td><td></td></tr><tr><td>Trader</td><td>ID</td><td>Data</td><td></td></tr><tr><td>ASSETS</td><td colspan="2"></td><td></td></tr><tr><td>Contract</td><td colspan="2"></td><td></td></tr><tr><td>TRANSACTIONS</td><td colspan="2"></td><td></td></tr><tr><td>All Transactions</td><td colspan="3">This registry is empty!To create resources in this registry click createnew at the top of this page</td></tr><tr><td>Submit Transaction</td><td colspan="3"></td></tr></table>

Figure 6

```json
(a) Participant MM
{
    "$class": "LMSR.MarketMaker",
    "marketMakerId": "MM",
    "openMarket": true,
    "liquidity": 100,
    "budget": 100,
    "marketPrices": [0.5, 0.5],
    "numberSoldShares": [0, 0]
}
(b) Participant Alice
{
    "$class": "LMSR.Trader",
    "traderId": "Alice",
    "budget": 100
}
(c) Participant Bob
{
    "$class": "LMSR.Trader",
    "traderId": "Bob",
    "budget": 100
}
```

```json
(a) Alice buys 50 shares regarding outcome 0
{ "$class": "LMSR.BuyShares",
    "trader": "resource:LMSR.Trader#Alice",
    "marketMaker": "resource:LMSR.MarketMaker#MM",
    "forecastedOutcome": 0,
    "numberRequestedShares": 50
}
```

```txt
(c) Bob buys 10 shares regarding outcome 1
(d) The market maker closes the market
{
    "$class": "LMSR.BuyShares",
    "trader": "resource:LMSR.Trader#Bob",
    "marketMaker": "resource:LMSR.MarketMaker#MM",
    "forecastedOutcome": 1,
    "numberRequestedShares": 10
}
```

```jsonl
(a) Alice record
{$class":"LMSR.Trader", "traderId":"Alice", "budget":71.90701963798}
(b) Alice_0 record
{$class":"LMSR.Contract", "contractId":"Alice_0", "forecastedOutcome":0, "numberShares":50, "owner":"resource:LMSR.Trader#Alice"}
(c) MM record
{$class":"LMSR.MarketMaker", "marketMakerId":"MM", "openMarket":true, "liquidity":100, "budget":128.09298036201614, "marketPrices": [0.6224593312018546, 0.3775406687981454], "numberSoldShares":[50,0]}
{
```

```jsonl
(a) Alice record
{$class":"LMSR.Trader", "traderId":"Alice", "budget":89.50083111784}
(b) Alice_0 record
{$class":"LMSR.Contract", "contractId":"Alice_0", "forecastedOutcome":0, "numberShares":20, "owner":"resource:LMSR.Trader#Alice"}
(c) MM record
{$class":"LMSR.MarketMaker", "marketMakerId":"MM", "openMarket":true, "liquidity":100, "budget":110.49916888216465, "marketPrices": [0.549833997312478, 0.45016600268752216], "numberSoldShares":[20,0]}
}
```

```jsonl
(a) Bob record
{$class":"LMSR.Trader", "traderId":"Bob", "budget":95.3742209308}
(b) Bob_1 record
{$class":"LMSR.Contract", "contractId":"Bob_1", "forecastedOutcome":1, "numberShares":10, "owner":"resource:LMSR.Trader#Bob"
(c) MM record
{$class":"LMSR.MarketMaker", "marketMakerId":"MM", "openMarket":true, "liquidity":100, "budget":115.12494795136256, "marketPrices": [0.52497918747894, 0.4750208125210601], "numberSoldShares":[20,10]
}
```

```json
(a) Alice record
{
    "$class": "LMSR.Trader",
    "traderId": "Alice",
    "budget": 109.5008311179
}
(b) Bob record
{
    "$class": "LMSR.Trader",
    "traderId": "Bob",
    "budget": 95.3742209308
}
(c) MM record
{
    "$class": "LMSR.MarketMaker",
    "marketMakerId": "MM",
    "openMarket": false,
    "liquidity": 100,
    "budget": 95.12494795136256,
    "marketPrices": [
    0.52497918747894,
    0.4750208125210601
],
    "numberSoldShares": [20, 10]
}
```

## (a) Contract registry

<table><tr><td>Web prediction-markets</td><td>Define</td><td>Test</td><td>Alice</td></tr><tr><td>PARTICIPANTS</td><td colspan="3">Asset registry for LMSR.Contract</td></tr><tr><td>MarketMaker</td><td colspan="3"></td></tr><tr><td>Trader</td><td>ID</td><td colspan="2">Data</td></tr><tr><td>ASSETS</td><td rowspan="2">Alice_0</td><td rowspan="2" colspan="2">{&quot;$class&quot;: &quot;LMSR.Contract&quot;,&quot;contractId&quot;: &quot;Alice_0&quot;,&quot;forecastedOutcome&quot;: 0,&quot;numberShares&quot;: 20,&quot;Owner&quot;: &quot;resource:LMSR.Trader#Alice&quot;}</td></tr><tr><td>Contract</td></tr><tr><td>TRANSACTIONS</td><td colspan="2"></td><td>Collapse</td></tr><tr><td>All Transactions</td><td colspan="3"></td></tr></table>

## (b) Trader registry

<table><tr><td>Web prediction-markets</td><td>Define</td><td>Test</td><td>Alice</td></tr><tr><td>PARTICIPANTS</td><td colspan="2">Participant registry for</td><td>+ Create New Participant</td></tr><tr><td>MarketMaker</td><td colspan="2">LMSR.Trader</td><td></td></tr><tr><td>Trader</td><td>ID</td><td>Data</td><td></td></tr><tr><td>ASSETS</td><td rowspan="2">Alice</td><td>{</td><td rowspan="2"></td></tr><tr><td>Contract</td><td>&quot;class&quot;: &quot;LMSR.Trader&quot;, &quot;traderId&quot;: &quot;Alice&quot;, &quot;budget&quot;: 109.50083111783535}</td></tr><tr><td>TRANSACTIONS</td><td></td><td></td><td></td></tr><tr><td>All Transactions</td><td></td><td></td><td></td></tr></table>

Figure 13

## (a) Contract registry

<table><tr><td>Web prediction-markets</td><td>Define</td><td>Test</td><td>MM</td></tr><tr><td>PARTICIPANTS</td><td colspan="2">Asset registry for LMSR.Contract</td><td>+ Create New Asset</td></tr><tr><td>MarketMaker</td><td colspan="3"></td></tr><tr><td>Trader</td><td>ID</td><td colspan="2">Data</td></tr><tr><td>ASSETS</td><td colspan="3"></td></tr><tr><td>Contract</td><td colspan="2"></td><td><img src="/api/attachments/ZRQNTDCD/fulltext/images/9acecde0f54e8217a116c49ced5230b04802b3920c1d641c6f881bda7a74cd09.jpg"/></td></tr><tr><td>TRANSACTIONS</td><td colspan="3"></td></tr><tr><td rowspan="2">All Transactions</td><td colspan="3">This registry is empty!</td></tr><tr><td colspan="3">To create resources in this registry clickcreate new at the top of this page</td></tr></table>

## (b) Trader registry

<table><tr><td>Web prediction-markets</td><td>Define</td><td>Test</td><td>MM</td></tr><tr><td>PARTICIPANTS</td><td colspan="2">Participant registry for LMSR.Trader</td><td>+ Create New Participant</td></tr><tr><td>MarketMaker</td><td colspan="3"></td></tr><tr><td>Trader</td><td>ID</td><td colspan="2">Data</td></tr><tr><td>ASSETS</td><td colspan="3"></td></tr><tr><td>Contract</td><td colspan="2"></td><td><img src="/api/attachments/ZRQNTDCD/fulltext/images/9e1cc5e1f27419d4c21c8126f4f64af62c55dd4013a4ebcf355612153263df9b.jpg"/></td></tr><tr><td>TRANSACTIONS</td><td colspan="3"></td></tr><tr><td>All Transactions</td><td colspan="3">This registry is empty!To create resources in this registry clickcreate new at the top of this page</td></tr></table>
