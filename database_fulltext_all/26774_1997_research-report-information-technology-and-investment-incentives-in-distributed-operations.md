---
otero_id: 26774
otero_key: "XSFR7PTE"
title: "Research Report: Information Technology and Investment Incentives in Distributed Operations"
authors: "Barrie R. Nault"
year: "1997"
journal: "Information Systems Research"
doi: "10.1287/isre.8.2.196"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## HSR Agriation Systems Research

# Information Systems Research

![](/api/attachments/XSFR7PTE/fulltext/images/648d2e87d5fd38d4fbe0f69ea4d9d590899c3f81bd65bef950cbd5c186245f2d.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Report: Information Technology and Investment Incentives in Distributed Operations

Barrie R. Nault,

To cite this article:

Barrie R. Nault, (1997) Research Report: Information Technology and Investment Incentives in Distributed Operations. Information Systems Research 8(2):196-202. http://dx.doi.org/10.1287/isre.8.2.196

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1997 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/XSFR7PTE/fulltext/images/cfce7abaf6f96bb9ab8a7806c27a06ff4cff01d410567c43fd98658aba3e7dd2.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Report: Information Technology and Investment Incentives in Distributed Operations

Barrie R. Nault

Graduate School of Management, University of California, Irvine, California, 92697 brnault@uci.edu

In distributed operations with positive externalities between branches, local underinvestment occurs because one branch does not account for the impact of its actions on other branches. Previous work found that an IT-enabled incentive mechanism called “ownership of customers” (OoC) reduced the problem of local underinvestment by accounting for inter-branch transactions. This report examines the impact of including investment by a central office on the set of previously developed results for local investment by branches. It shows that ownership of customers can reduce the problem of both central and local underinvestment. It also demonstrates how central investment can yield second-best levels of profitability—optimal profits given contracting problems in local investment with branches. It highlights how charging branches a unit fee to fund the needed level of central investment is consistent with that second-best solution.

(Positive Network Externalities; Centralization; Decentralization; Channels; Ownership of Customers; Underinvestment; Branch Operations; Franchising)

## 1. Introduction

The most important impact of information technology (IT) is how IT can change organizational form. Historically, organizational form is thought to result from two competing tensions: coordination and motivation (Milgrom and Roberts 1992). This tension is at the root of choices between centralization and decentralization, and more generally between markets and hierarchies (Gurbaxani and Whang 1991, Malone et al., 1987). Unrecognized until recently is that IT can improve motivation by enabling incentives that reward investments when there are positive externalities between organizational units. Although IT has historically been used for monitoring, one of the main points in our prior work and in the current report is that IT has an important role in enabling incentives that should not be overlooked when designing new organization forms.

We have shown that in certain franchise environments, when there are positive externalities such as customers that purchase from several different franchises, IT-based transfers between franchises can improve the performance of each franchise and the franchisor (Nault and Dexter 1994, Nault 1997). That research is characterized by local investments by franchises and the coupling of exclusive rights to customers and locations: franchises have exclusive rights to customers that reside in their territories and for all purchases that are made in their territories. The role of IT is to match customers to franchises, to perfectly monitor cross-franchise transactions, and to make transfers based on that matching and inter-franchise transactions. We call that IT-enabled mechanism “ownership of customers”, and employ the abbreviation OoC from Nault (1997). OoC mitigates franchise underinvestment that occurs because franchises ignore the effects of their own investment on other franchises (Katz 1989). As a result, franchisor profits and franchise investments may be increased over levels that are obtained in traditional franchise arrangements.

An example of our model is Pacific Pride Commercial Fueling Systems. Details of Pacific Pride's system are available elsewhere (HBS Case Services 1988, Nault and Dexter 1994, 1995, Nault 1997), but the essential aspects are as follows. Pacific Pride is a network of independent commercial fueling franchises. The network covers several regions of the United States, providing gasoline and diesel fuel for customers in vehicle fleet and trucking operations over those regions. Each franchise is assigned a territory and has exclusive rights to recruit customers residing in that territory to adopt the network—that is, to purchase gasoline and diesel fuel from franchises in the network. Because vehicle fleet and trucking operations make energy purchases that span different regions, Pacific Pride has implemented IT that captures the purchase transactions anywhere in the network, matches customers to the owning and serving franchise, and divides profits from the transaction between the owning and serving franchise. Each franchise bills customers residing in its territory for purchases across the network. Customers value the network because it allows them greater control over costs (Nault and Dexter 1995).

Although Pacific Pride is a franchise structure, we have argued that our models apply to organizational forms that are not strictly franchise structures (Nault 1997). However, they do not apply to all franchise structures. Our models apply to any organizational form where there is a single central office and many branches, the central office provides a margin to the branches, transfers between branches are possible, ownership of each individual customer can be uniquely established, and the owner and server of the customer can be verifiably identified.

The present report extends our results based on the OoC mechanism to include central investment by the central office, where central investment affects branch profits differently than does local investment. We begin with our assumptions, which are both parsimonious and representative of many environments that are encountered in practice. We then show how a straightforward formulation of central investment, similar to a unit investment fee, yields “second-best” levels of central and local investment—that is, investment levels that are optimal given the different information and incentives of the central office and branches. We then directly extend our prior results to show how even the IT-enabled form yields underinvestment in central and local investment relative to first-best investments—that is, investments that would result in a fully informed and integrated firm. Finally, we show how the application of the OoC through IT can make the firm more profitable with centralized investment.

## 2. Essentials of the Setting

Our model has one central office and many branches. Areas covered by branches are territories and a single branch controls the local decisions in each territory. Each branch may have multiple outlets in its territory, but local decision-making authority resides at the branch. Each branch has exclusive rights to recruit customers that reside in its territory to do business with the organization, meaning that no other branch may recruit customers from another branch's territory. Not all territories have the same demand potential. Branches differ in some dimension that we relate to demand potential in Assumption 1 below. We refer to that dimension as "size" and represent it with the variable $x \in [x, \bar{x}]$ . $x$ could represent, for example, the population of the local market. A Pacific Pride territory, for example, may contain more than one station, and is usually defined by zip codes.

We model two types of investment: central and local. Central investment is represented by the variable $a$ , where $a$ is restricted to the interval $[a, \bar{a}]$ . As with local investment defined below, we assume the interval is compact and convex to ensure the existence of the investment equilibria. Central investment is organization-wide investment, for example, improvements in infrastructure or national advertising. Local investment made by branch $x$ , $e_x$ , ranges over the interval $[e_x, \overline{e_x}]$ . The vector of local investment over all of the branches is $\mathbf{e} = (e_x, e_{\backslash x})$ , where $e_{\backslash x}$ is the vector of local investments made by branches other than $x$ . Local investment is branch-specific, for example, effort in new customer recruitment.

The separation of investments into central and local is common. Marketing investment, for example, is often separated into two types—promotion and direct selling. Promotion such as advertising through different media and couponing are usually decided nationally. Direct selling activities such as customer visits and sales calls are often specified locally. Using our example, Pacific Pride's central office makes media promotion decisions, such as advertising in trade magazines. Local franchise operators decide which prospective and existing customers to visit, how often, and when.

We use the term own customers to refer to those customers based in the branch's territory and foreign customers to refer to customers based outside of the territory. Each branch faces three mutually exclusive demands.

\- $d_{D}(x, y, a, \mathbf{e}) =$ domestic demand: demand from own customers at own branch,

\- $d_E(x, y, a, \mathbf{e}) =$ exported demand: demand from own customers at foreign branch,

\- $d_{I}(x, y, a, \mathbf{e}) =$ imported demand: demand from foreign customers at own branch.

The aggregate of the branches that participate in the incentive mechanism we call the system, and the variable y represents system size and will be formally defined later. We assume the demands are twice continuously differentiable where needed. We require four basic sets of assumptions for the mechanics of our model. Three are restrictions on demands, and the fourth accounts for incomplete contracts.

ASSUMPTION 1 (SIZE). Demands from own customers are increasing in branch size, and demands from foreign customers are unaffected by branch size; all demands are increasing in system size:

$$
\begin{array}{c} \frac {\partial d _ {D} (x , y , a , \mathbf {e})}{\partial x}, \quad \frac {\partial d _ {E} (x , y , a , \mathbf {e})}{\partial x} > 0, \\ \frac {\partial d _ {I} (x , y , a , \mathbf {e})}{\partial x} = 0, \quad \frac {\partial d _ {i} (x , y , a , \mathbf {e})}{\partial y} > 0, \quad i \in \{D, E, I \}. \end{array}
$$

The reasoning to support the conditions in Assumption 1 that pertain to x follow logically from our interpretation of the variable x as branch size, so that larger branches have greater domestic and exported demands. The size of a branch does not affect its imported demand. The condition in Assumption 1 that all the demands increase in system size follows from interpreting the number of branches as a positive externality whereby a system with a greater number of branches is more attractive to the customer. A Pacific Pride franchise with a larger customer base has larger domestic and exported demands from those customers, and the size of its customer base does not affect the magnitude of imported demand. A larger network provides more locations outside the territory for the fueling customer to use, making the network more attractive.

ASSUMPTION 2 (INVESTMENT). (a) All demands are increasing and concave in central investment:

$$
\frac {\partial d _ {i} (x , y , a , \mathbf {e})}{\partial a} > 0, \quad \frac {\partial^ {2} d _ {i} (x , y , a , \mathbf {e})}{\partial a ^ {2}} <   0:
$$

(b) Domestic and exported demands are increasing and concave in own local investment, and are unaffected by other branches' own local investment, and imported demand is unaffected by own local investment and is increasing in other branches' own local investment:

$$
\begin{array}{c} \frac {\partial d _ {j} (x , y , a , \mathbf {e})}{\partial e _ {x}} > 0, \quad \frac {\partial^ {2} d _ {j} (x , y , a , \mathbf {e})}{\partial e _ {x} ^ {2}} <   0, \\ \frac {\partial d _ {j} (x , y , a , \mathbf {e})}{\partial e _ {\backslash x}} = 0, \quad j \in \{D, E \}, \\ \frac {\partial d _ {I} (x , y , a , \mathbf {e})}{\partial e _ {x}} = 0, \quad \frac {\partial d _ {I} (x , y , a , \mathbf {e})}{\partial e _ {\backslash x}} > 0. \end{array}
$$

(c) Central and local investment are complementary at the margin: $\partial^2 d_j(x, y, a, \mathbf{e}) / \partial a \partial e_x > 0$ .

Parts (a) and (b) of Assumption 2 reflect standard conditions of increasing returns with diminishing marginal returns to both central and local investment, with the returns to local investment restricted to own customers. That latter characterization follows from the fact that local investment applies to customers residing locally only. Assumption 2(c) indicates that the two types of investment are mutually reinforcing rather than substitutes.

The equalities in Assumption 2(b) can best be understood when local investment is interpreted as direct selling. Visits or telephone calls are made directly to customers residing in a branch's territory, and are targeted to having that customer adopt the network and recorded as being "owned" by the branch. A franchisee on Pacific Pride's network, for example, makes personal visits to trucking firms in its territory with the purpose of having those firms sign up with that franchise as part of the network.

ASSUMPTION 3 (MODELING). (a) Marginal returns from local investment are increasing in branch size: $\partial^2 d_j(x, y, a, e) / \partial e_x \partial x > 0$ .

(b) For the smallest branch on the system, imported demand is greater than exported demand.

Assumption 3 is needed for several of our results, and we believe that neither condition is unreasonable. Assumption 3 (a) follows from the logic that the next dollar of investment yields higher returns in a larger market. Assumption 3 (b) is satisfied by any reasonable distribution of foreign demand as the smallest branch receives imported demand from all of the remaining branches, each of which has more own customers.

ASSUMPTION 4 (CONTRACTIBILITY). Local investment is not contractible.

The final assumption allocates local investment decisions to the branches rather than to the central office. We argue that incomplete contracts, whereby all the necessary terms and conditions cannot be specified in a contract by the central office, is the reason why decisions are often decentralized. There are a variety of reasons why contracts can often not be complete, including bounded rationality and asymmetric information. When local investment is direct selling, specific knowledge of customers is private information of the branch. As long as that information is changing, the central office cannot construct a contract that reveals and mandates the optimum use of that private information. In a sense, the central office cannot determine with sufficient precision what it is that it does not know. At Pacific Pride, for example, a franchisee knows which customers to visit, how often, and when, because of constant contact with local firms. Pacific Pride's central office may know the relationship between local investment and demand but cannot determine how to carry out local investment as effectively as the franchisee.

In some cases it may be possible for the central office to determine how a branch should optimally invest a portion of its local investment and verify that that portion of local investment was made in the optimal way.

If the latter is true, then local investment is partially contractible, and should be partially contracted. Then the contractible portion of local investment should be mandated through a contract, penalizing the branch if those investments were not made as contracted. The remaining noncontractible portion of local investment would follow as in our analysis. In practice, penalties take the form of fixed payments or discrete actions like personnel replacements or shutting down the branch. Pacific Pride, for example, mandates safety and display standards at each franchise's stations, with the option of terminating the franchise's relationship with the network if it does not comply.

## 3. Model

Ownership of customers (OoC) consists of the following mechanism. When the customer makes a purchase, the purchase is recorded along with the customer's identity. The customer is matched with the branch that owns the customer. If the customer made the purchase at its owning branch (domestic demand), then that branch receives a unit margin on the purchase. If the customer made the purchase at another branch (foreign demand), then the owning branch receives a unit margin on the purchase and transfers part of that margin to the serving branch. In that way, both the owning and serving branches are rewarded for foreign purchases. The role of IT is critical in being able to employ that mechanism. An application of IT is necessary to determine which branch owns the customer being served so that on foreign demand the owning branch can be rewarded for its local investment through the transfer.

We model the problem of central and local investment in two steps. In chronological order, the central office sets central investment, the margin, and the transfer. Then, branches react to the setting of those three variables in their local investments. In setting central investment, the margin, and the transfer, the central office accounts for branches' local investment. We solve the branch's investment problem first, and then incorporate the resulting local investments in the central office's problem.

## 3.1. Branch Profits

Each branch makes a single decision: its local investment. The branch's profit function is

$$
\begin{array}{r l} \pi (x, y, a, \mathbf {e}) & = m d _ {D} (x, y, a, \mathbf {e}) + [ m - t ] d _ {E} (x, y, a, \mathbf {e}) \\ & + t d _ {I} (x, y, a, \mathbf {e}) - e _ {x}. \end{array}
$$

m is the margin, which is the price less a royalty, p - r, and is collected on domestic demand. The owning branch receives m - t on exported demands. $^{1}$ t is the transfer paid on exported demand and received on imported demand. $^{2}$

We consider transfers that are less than the margin, t < m. Branches maximize profits by choosing their own local investment, $e_{x}$ . Their first-order condition is

$$
\begin{array}{r l} \frac {\partial \pi (x , y , a , \mathbf {e})}{\partial e _ {x}} & = m \frac {\partial d _ {D} (x , y , a , \mathbf {e})}{\partial e _ {x}} \\ & + [ m - t ] \frac {\partial d _ {E} (x , y , a , \mathbf {e})}{\partial e _ {x}} - 1 = 0. \end{array}\tag{1}
$$

The second-order condition is satisfied from Assumption 2(b). The set of first-order conditions (1), one for each branch, defines the equilibrium local investment across branches as a function of the margin, the transfer, and central investment, $e_{x}(m, t, a)$ . Using the implicit function rule and employing Assumptions 2(b) and (c) along with Assumption 3(a), it is straightforward to show that local investments are increasing in branch size, the margin, and central investment, and are decreasing in the transfer.

We define the smallest branch that participates in the system as a function of the margin, the transfer, central investment, and the vector of equilibrium local investments, in the following manner:

$$
\tilde {x} (m, t, a, \mathbf {e} (m, t, a)) = \min \{x \mid \pi (x, y, a, \mathbf {e} (m, t, a)) = 0 \}.
$$

Using that condition, the implicit function rule can again be used together with Assumptions 1, 2, and 3 to show that the smallest branch that participates in the system is smaller if any of the margin, the transfer, central investment, and other branches' local investment are higher. To save on space, we refer to $\tilde{x}(m, t, a, \mathbf{e}(m, t, a))$ as $\tilde{x}(\cdot)$ . Because each branch is already choosing its own local investment optimally, there is no impact from a change in own investment.

We are now able to define the system size, y, as a function of that smallest branch: $y(\tilde{x}(\cdot)) = \int_{\tilde{x}(.)}^{\tilde{x}} f(x) \, dx$ . It is straightforward to show that system size is increasing in the margin and in central investment. The effect of the transfer on system size is inconclusive because the positive effect on the indifferent branch's size is offset by the negative effect of local investment.

We define the total system volume as the aggregate of domestic and exported demand:

$$
\begin{array}{l} q (\tilde {x} (\cdot), a, \mathbf {e} (m, t, a)) \\ = \int_ {\tilde {x} (\cdot)} ^ {\bar {x}} [ d _ {D} (x, y (\tilde {x} (\cdot)), a, \mathbf {e} (m, t, a)) \\ \qquad + d _ {E} (x, y (\tilde {x} (\cdot)), a, \mathbf {e} (m, t, a)) ] f (x) d x. \end{array}
$$

To conserve space, we represent $q(\tilde{x}(\cdot), a, \mathbf{e}(m, t, a))$ by $q(\cdot)$ . With that definition, it is simple to show that system volume is increasing in the margin and in central investment. The impact of the transfer on system volume cannot be determined for the same reason that its impact on system size is inconclusive: the positive effect on the system's smallest branch is offset by a reduced incentive for local investment.

## 3.2. The Central Office: System Profits

At the system level the central office sets the margin, transfer, and central investment. The central office maximizes the system's profit function,

$$
\max _ {m, t, a} \psi (m, t, a) = \max _ {m, t, a} [ [ p - m ] q (\cdot) - a ].
$$

The first-order conditions necessary for an interior solution are

$$
\begin{array}{r l} - q (\cdot) + [ p - m ] \frac {d q (\cdot)}{d m} & = 0, \quad [ p - m ] \frac {d q (\cdot)}{d t} = 0, \\ \text { and } \quad \frac {d q (\cdot)}{d a} - 1 & = 0. \end{array}\tag{2}
$$

The optimization yields central and local investments that are "second-best", in the sense that having non-contractible local investment and having restricted the margin and transfer to being non-discriminatory (linear), profits could not be increased by a different implementation of central investment.

Straightforward manipulation of the objective function gives $\psi(m, t, a) = [p - m - w] q(\cdot)$ where $w = a / q(\cdot)$ is defined as a unit fee for central investment. That provides the central office with two distinct ways to present the funding of central investment. In the first way the central office declares that it will provide the lump-sum central investment out of its profits. In the second way the central office charges a unit fee for central investment to the branches, with the ability to commit to this use of the proceeds of the fee. The latter approach is commonly seen in franchise contracts whereby the franchise provides the franchisor with a royalty and a unit advertising fee that the franchisor commits to using for national advertising. What is important to recognize is that those two treatments of central investment are isomorphic. Thus, rather than being restrictive, a unit fee for central investment set in this way is “second-best”. Pacific Pride, for example, builds a unit advertising fee into its royalty and commits to using the funds generated by that fee for system-wide advertising.

## 3.3. Comparison to First-Best

In the first-best solution, the solution that would be obtained in a fully integrated and informed firm, the central office chooses the levels of $a$ and $\mathbf{e}$ directly and simultaneously. In that case, the central office expands the organization so all of the units are included. There is no loss of generality as some of the local investments could be set to zero. With universal adoption, $y = 1$ so that the demand elements are $d_{t}(x, 1, a, \mathbf{e})$ , giving $q(\mathbf{x}, a, \mathbf{e})$ . In addition, there is no margin, transfer or central investment fee. The profit function to be maximized is

$$
\phi (a, \mathbf {e}) = p q (\mathbf {x}, a, \mathbf {e}) - a - \mathbf {e}.
$$

The necessary first-order conditions are

$$
p \frac {d q (\mathbf {x} , a , \mathbf {e})}{d a} - 1 = 0 \quad \text { and } \quad p \frac {d q (\mathbf {x} , a , \mathbf {e})}{d e _ {x}} - 1 = 0,\tag{3}
$$

where for the second equation in (3) there is a first-order condition for each $e_{x}$ . We can compare local investment using the second equation in (3) and (1). From Assumption 1 and the definition of total system volume, at each branch the first-order condition (3) is satisfied at a higher level of local investment, given the same central investment, than (1). Again using Assumption 1, comparing the first term in (3) with the last term in (2), the first-order condition is satisfied at a higher level of central investment, given the same local investments. From the investment complementarities in Assumption 2(c), all levels of investment are higher under first-best. Therefore, the underinvestment problem extends to central investment.

## 3.4. Comparison to the Traditional Mechanism

Given the same number of branches, our model always yields higher profits than the traditional approach without IT-enabled transfers between branches. Profits in a traditional organization are

$$
\tau (x, y, a, \mathbf {e}) = m [ d _ {D} (x, y, a, \mathbf {e}) + d _ {I} (x, y, a, \mathbf {e}) ] - e _ {x}.
$$

Branch local investments result from the first-order conditions

$$
\frac {\partial \tau (x , y , a , \mathbf {e})}{\partial e _ {x}} = m \frac {\partial d _ {D} (x , y , a , \mathbf {e})}{\partial e _ {x}} - 1 = 0,\tag{4}
$$

one for each branch. The concavity condition is satisfied by Assumption 2(b). Comparing the first-order condition (4) to (1), if the margins are equal in both cases, then the traditional model yields lower levels of local investment, lower central investment because of investment complementarities, and, thus, lower levels of profitability because of the underinvestment problem. Although we cannot show that investment increases because the margins are not necessarily the same in the two cases, the central office with the IT-enabled mechanism could always set the margin equal to that which maximizes profits in the traditional case and be more profitable. Therefore, the IT-enabled mechanism is always more profitable, whether or not there is central investment.

In our two mechanisms (OoC and traditional) there are conditions under which it is optimal to have no central investment. Those correspond to corner solutions of the optimization problems faced by the central office. It is not possible to determine that in general one mechanism is more likely to maximize profits with zero central investment than another. That occurs for the same reason that it is not possible to rank the magnitude of investments obtained from each mechanism. A specific parameterization of the problem is needed to determine interpretable conditions for that ranking. As is often the case with economic analyses, idiosyncratic characteristics of the problem determine whether it is better to take additional profits on price (i.e., the royalty), on increased volume (i.e., system volume), or on both.

## 3.5. Summary of Results

The following bullets summarize the novel results contained in this report:

\- The IT-enabled OoC mechanism can increase central and local investment through the use of incentives. OoC reduces the dual problems of central and local underinvestment that occur when there are positive externalities, problems that are compounded when there are complementarities between the two types of investment.

\- For investment from the central office, a lump-sum investment from system profits is the same as investment generated from a unit fee added to the royalty. The central office can credibly commit to the use of that administratively simple unit fee for central investment, and the fee can be integrated into the OoC mechanism. This explains why unit fees are seen so often in practice.

\- Compared to the traditional approach, OoC makes organizations with the same number of branches more profitable, extending our previous results by adding central investment to the formulation. OoC can increase both central and local investment, although that may not be necessary for the organization to increase profit.

## 4. Conclusions

One of the fundamental problems in situations where there are positive externalities between contributors is that these contributors underinvest relative to first-best because they do not receive the full rewards from their investment. In this report, we extended our previously developed incentive mechanism, OoC, to include central investment by a central office. We showed that OoC reduces the problem of central, as well as local, underinvestment. Our underlying theme is that IT enables incentives that were not feasible before—incentives that take advantage of transfers between contributors when there are positive externalities. Our models demonstrate that new incentive mechanisms enabled by IT have important implications for generating additional profits within and between organizational units. We believe they open up new areas of organizational design based on different forms of alliances and networks. They are representative of a new era where IT is used to separate and reward individual contributions to group benefits, mitigating individual underinvestment and raising the levels of individual and group performance.

We used the commercial fueling industry as a real-world example from which our model was abstracted, and of where our model is applied. The abstraction from, and application to, the same example validates the modelling process. Little was lost in abstracting from reality to the model—a goal that is desired but not always achieved. Other industries with similar structure as commercial fueling include certain car dealerships such as Saturn for repairs when breakdowns occur away from home, consulting with professional service firms to multinationals, and distributors of bulk fuel. $^{3}$

$^{3}$ Helpful comments have been provided by the participants in the workshop “Information Technology and the Changing Boundaries of the Firm” at Wharton’s SEI Center for Advanced Studies in Management and by the participants in the MIS Seminar series at the Center for Research on Information Technology and Organizations (CRITO) at the University of California, Irvine.

## References

Gurbaxani, V., and S. Whang, "The Impact of Information Systems on Organizations and Markets," Comm. ACM, 34, 1 (January 1991), 59–73.

HBS Case Services, "Pacific Pride Commercial Fueling Systems (C)," 9-188-084, Harvard Business School, Boston, MA, 1988.

Katz, M. L., "Vertical Contractual Relations," in R. Schmalensee and R. D. Willig (Eds.), Handbook of Industrial Organization, Volume 1, Chapter 11, Elsevier Science Publishers B. V., Amsterdam, 1989, 655–721.

Malone, T. W., J. Yates, and R. I. Benjamin, "Electronic Markets and Electronic Hierarchis," Comm. ACM, 30, 6 (June 1987), 484–497.

Milgrom, P. and J. Roberts, Economics, Organization and Management, Prentice Hall, Englewood Cliffs, NJ, 1992.

Nault, B. R., "Mitigating Underinvestment through an IT-Enabled Organization Form," Organization Sci., 8, 3 (1997), 223–234.

— and A. S. Dexter, "Adoption, Transfers and Incentives in a Franchise Network with Positive Externalities," Marketing Sci., 13, 4 (Fall 1994), 412–423.

— and —, "Added Value and Pricing with Information Technology," Management Information Systems Quarterly, 19, 4 (December 1995), 449–463.
