---
otero_id: 19330
otero_key: "VZNTPG4E"
title: "Economic aspects of requirements analysis"
authors: "Peter Monk"
year: "1992"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/0963-8687(92)90005-h"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Economic aspects of requirements analysis

Peter Monk

Department of Management Science, University of Strathclyde, Livingstone Tower, Richmond Street, Glasgow G1 1XH, UK

Requirements capture and analysis (RCA) is viewed here as an economic process of information production. Concepts of supply and demand between RCA clients and engineers are examined, together with a range of resource constraints on the production of requirements specifications. Resource constraints imply a need for allocative decision making. Implications of resource allocation models are discussed in the context of organizations' pursuit of corporate objectives. Two conclusions are offered: that the same managerial rationale applies to both RCA and corporate demands for improved information systems; and that there is a need for an economic theory of systems development.

Keywords: requirements analysis, information systems, information technology, economics, resources, information production, management decision-making

Requirements capture and analysis (RCA) is the first stage in the development of new information systems and products. It is typically represented in systems development methodologies as the first step in turning the demands (requirements) of users or clients into technical specifications for subsequent design and development work. The quality and relevance of information technology (IT) products depend critically on successful analysis of requirements; most notably in safety-critical systems, where human lives may be at risk if systems are improperly specified, and in large, complex systems where substantial investments are at stake. The commercial significance of RCA has been widely acknowledged in the literature by, for example, Boehm $^{1}$ , CORE $^{2}$ , Finkelstein $^{3}$ , Longworth $^{4}$ and the contributors to Galliers $^{5}$ . These and others have emphasized the necessity of systems developers setting out in the right direction, if they are to succeed in producing systems that meet the needs of users. Yet little attention has so far been paid to the economic dimensions of the RCA process itself; existing development methodologies are silent on any basic theory in regard to the feasibility of RCA. The purpose here is to offer a constructive challenge to the widely held, and often implicit, assumption that the capture and analysis of users' requirements is always a feasible activity.

The root of the problem is that whenever the development of information systems (in the broad sense) includes the development of IT systems (in the narrow hardware plus software sense), RCA is necessarily linked to an engineering process. While significant progress has been made by researchers in broadening the concept, analysis and design of information systems to include informal and organizational factors $^{6-9}$ , RCA is conventionally conceived by IT systems developers in technical engineering terms $^{10-12}$ rather than as a necessary part of economic decision-making about investments in new systems. Clearly, engineering considerations are pertinent to the specification of requirements; systems development is, at one level, a technical activity. However, that activity always necessarily takes place in an economic context. Systems development is an investment activity that is predicated on resources being allocated for its execution. Development projects are the outcome of decisions to invest in the production of new or improved systems. The difficulty lies in exactly how such investment decisions in principle can be transformed into detailed demands for specific systems in practice. Irrespective of their degrees of knowledge, both clients and engineers must still necessarily face uncertainty about the properties of systems which have yet to be constructed.

This paper offers an analysis of RCA as an information production process, the output from which consists of requirements specifications. The economics of information production is closely related to the economics of R&D, innovation and technology policy $^{13-14}$ ; the treatment here of markets, supply, demand and resource allocation is derived from the general economic literature. The argument is structured as follows. A range of typical systems development activities are considered in relation to economic concepts of supply and demand. RCA is seen to be more problematic than is implicitly assumed in models in which engineers 'supply' systems to meet clients' 'demands'. Information availability constraints are then examined as part of the broader issue of how resources for RCA are limited. Resource constraints imply a need for allocative decision-making, a topic considered in relation to the allocative implications of decision models. Conclusions are offered on the application of economic concepts of RCA to IT systems development and on the potential value of an economic approach to systems development as a whole.

## Supply and demand in systems development

The development of methods for constructing IT systems, from waterfall and spiral models to prototyping and information engineering, has seen increasing prominence given to the role of the client, typically expressed as the user of a new or improved system. This change has been based on a growing realization by engineers (and their employers) that systems development can never be assumed to be an autonomous process, cut off from the economic world. Instead, there is now a prevalent but simplistic view that clients 'demand' systems innovations and engineers 'supply' them.

Table 1 shows seven types of systems development activity in which the RCA process may be expected to vary according to the differing roles played by clients, engineers and other economic agents (both inside and outside an organization) as supply-agents and demand-agents. Two (non-standard) definitions are used below:

Table 1. RCA supply and demand categories: a summary

<table><tr><td>n</td><td>Type of system development activity</td><td>RCA supply and demand characteristics</td></tr><tr><td>1</td><td>Maintenance, routine &amp; simple changes to existing systems</td><td>Client as demand-agent: demand-led process</td></tr><tr><td>2</td><td>Rewrites, major changes to existing systems e.g. network integration</td><td>Client as limited demand-agent: demand-led process qualified by technical advice</td></tr><tr><td>3</td><td>New systems. Paradigm RCA problems</td><td>Client as demand-agent only in principle: must negotiate demand with supply-agent</td></tr><tr><td>4</td><td>Generic systems, tools, techniques, packages</td><td>Engineer as supply-agent searches for client(s) to act as demand-agents</td></tr><tr><td>5</td><td>Product innovation, new goods or services via existing systems</td><td>Supply-led internal process: client=?</td></tr><tr><td>6</td><td>Process innovation, e.g. IT system links with external suppliers</td><td>Supply-led process? Qualified demand-led process?</td></tr><tr><td>7</td><td>Experimental systems, basic R&amp;D. invention</td><td>Specific supply and demand undefinable; origin of generic requirements?</td></tr></table>

\- Demand-agent: any individual or group able to obtain goods or services from other agents, by means of exchange or command. In markets and quasi-markets, demand-agents obtain goods or services by exchanging them for commodities (including money) and resources respectively.

● Supply-agent: any individual or group able to produce goods or services, for the purpose of supply to other agents. Production decisions may (but need not) involve reaction to the decisions of demand-agents; supply-agents may act autonomously in producing new goods or services.

The central question in each case is: who can be expected to know what and under which circumstances? Inherent differences in the characteristics of 'required' IT innovations lead to differences in the information available to clients and engineers; they also lead to doubts in some cases as to whether 'clients' can exist in any meaningful sense.

## Maintenance

Client: may be assumed to act as a demand-agent for functional changes to existing systems. RCA for such changes would be a demand-led process. However, the need for technical maintenance work may derive from changes in the systems environment of which clients may be unaware (e.g. new versions of operating systems). In this case, the client might be assumed to have a generic demand for necessary technical maintenance, to be interpreted as appropriate by the engineer acting as the client's agent.

Engineer: would act as supply-agent for demand-led changes to systems. The engineer might also act as the client's agent with regard to technical maintenance of previously demanded and constructed systems.

## Rewrites

This category also includes major modifications to existing systems.

Client: would act as demand-agent subject to the technical advice of engineers. RCA would be a qualified demand-led process.

Engineer: would act both as supply-agent and as the client's agent, for the reasons given above in regard to technical maintenance. In practice, the client might often obtain advice and supply services from different agents, for example in-house systems developers, external consultants or system suppliers. Such action would result in a more complex supply-demand relationship between clients and engineers.

## New systems

Following the systems literature, the construction of complete new systems is taken to be the paradigm case for RCA.

Client: can act as a demand-agent only in principle. Some ex post observable properties of any new system must remain unknown and hence unspecifiable before it is constructed; the client's specification of demand must therefore be incomplete ex ante.

Engineer: acts as a supply-agent who must negotiate the specification of demand with the client (i.e. demandagent), due to the incomplete knowledge of each party. RCA of this type, therefore, cannot be subject to 'supply and demand' in a conventional market sense.

## Generic systems

This category covers all systems which are not specific to one application but which are produced by engineers for in-house use by clients; for example, software packages, implemented programming languages, automated software tools.

Client: may be assumed to exist within a large organization, even if specific individuals or groups have yet to be identified. These clients could only become demand-agents in response to a supply-led development process, due to assumed limitations of clients' knowledge of currently feasible technical innovation.

Engineer: would act as an autonomous supply-agent (i.e. creator of a new supply opportunity). Engineers would need to search for internal clients to act as demand-agents; potential demand-agents would form a sub-set of the organization's possible internal clients.

## Product innovation

RCA is pertinent to the development of systems as products for external as well as internal clients. The 'product innovation' category covers the creation of new goods or services, by means of existing systems or processes, for sale to external clients. Examples from the telecommunications industry would include customer premises equipment (e.g. telephones, key systems, PABX), value-added network services (VANS) and bespoke systems engineering work $^{15}$ .

Client: cannot be assumed to be identifiable or even to exist. In the case of innovations offering previously unknown facilities, clients would not be definable as demand-agents, due to their necessary ignorance of such innovations prior to development as products.

Engineer: acts as a supply-agent. Some form of RCA might take place between engineers and proxy-clients (e.g. marketing and product development specialists) but this could not result in conventional market supply because conventional market demand would not be definable ex ante.

## Process innovation

Some external clients may require specific processing or communication systems that are related to an organization's operations. For example, in the case of inter-organizational computer networks, external suppliers may require on-line links to internal agents $^{16}$ . RCA for such systems would be undertaken as a result of the outcome of negotiations between internal and external agents. Depending on the relative strengths of interest of the two parties, together with the technical characteristics of the innovation in question, RCA may be either a supply-led process or a demand-led process, qualified by technical advice.

Client would be an external agent with supply-demand role undefined ex ante.

Engineer: would be an internal agent with supply-demand role undefined ex ante, although likely in practice to be the main source of technical advice to demand-agent.

## Experimental systems

This category covers all experimental development work on systems produced as a result of invention or for the purposes of basic R&D. At some period or another, all systems technology passes through the category. Here, specific supply and demand are undefinable in conventional market economic terms, although generic requirements and supply possibilities may originate here.

Client: would be undefinable except by assumption (e.g. that the client is whoever authorizes development of the system in question).

Engineer: would be undefinable except as innovator or by assumption (e.g. that the engineer is whoever takes responsibility for supplying the client as above).

## Resource constraints on RCA

The purpose of this section is to make explicit the types of resources required for any RCA process and the ways in which limitations on those resources affect the production of requirements specifications. Common usage of the terms 'resource' and 'resource constraint' can lead to misunderstanding between people preoccupied with financial and technical concerns. For this reason, more rigorous definitions are required here.

Resources are not just available quantities of money. A resource is any physical or abstract entity which has actual or potential value in use in production $^{14}$ . Note that financial considerations are essentially secondary; financial quantities are only indirect expressions of resource quantities since they depend also on prices or unit costs. The primary issue here is the direct expression of actual quantities of those resources which are necessary inputs to RCA as a production process. The value of those resources derives from their use as inputs to production; it does not derive from external market transactions, or from any form of in-house quasi-market transactions between cost or profit centres.

Resource constraints are not just budget limits in this context. A resource constraint is any form of limitation on the quantities of a given resource that are available for use in production. It must be emphasized that constraints on resources may be of any type, some of which cannot be overcome by the provision of a larger budget for production. Indeed, some such constraints are incurable. The central question here is to determine which types of resources, as inputs to production, are constrained in which ways. Table 2 summarizes four main types of resources that are necessary for any form of RCA. Each is described briefly below.

Table 2. Resource inputs to RCA: a summary

<table><tr><td>Resource type</td><td>Example inputs to RCA</td></tr><tr><td>Skilled labour</td><td>Client: set of one or more individualsEngineer: set of one or more individuals(Each set may include a variety of persons with specific skills and knowledge)</td></tr><tr><td>Capital</td><td>Office facilities, equipment and materialsExisting systems</td></tr><tr><td>Time</td><td>Total period of RCA for given innovatione.g. time for client/engineer interactiontime for analysis by engineertime for revisions by client</td></tr><tr><td>Information</td><td>RCA method: formal or informal (ad hoc)Primary: RCA data from client and engineerIntermediate: hypotheses and draft outputsContextual: external data on constraints</td></tr></table>

Note: This table excludes non-specific resources, such as general overhead capital and labour employed by organizations undertaking RCA (e.g. head office personnel, catering facilities, car parks, research establishments)

## Skilled labour

All participants in the RCA process may be assumed to be also participants in labour markets (i.e. RCA is an activity of employed persons, not a vocation). The availability of suitably skilled or knowledgeable clients and engineers therefore depends on conditions in specific labour markets. The more specialized the set of skills demanded, the greater will be the probability of labour supply constraints. To the extent that relevantly skilled people are available in labour markets, labour resource constraints on RCA may be overcome by greater financial allocation. However, if quantitative limits on available supply are encountered, financial allocation alone cannot help; changes in client and engineer training, in RCA methods, or in the set of required innovations (e.g. new systems) would be needed to overcome labour resource constraints.

## Capital

Two forms of capital resources are necessary inputs to RCA. The first, direct capital inputs, consists of the plant and equipment required for information production. This form of capital is generic to information production and so few supply limitations need be expected. Direct capital inputs to RCA may be thus assumed to be constrained only by financial allocation. The second, indirect capital inputs, consists of existing systems which are to be modified or superseded, and the technical environment in which required new tems are to operate. While this form of capital is a resource - and it is constrained in the sense that empirically each such resource exhibits only a particular set of properties - indirect capital inputs are perhaps best treated as given conditions against which RCA is to be undertaken. Indirect capital resources set the technical context of RCA; the constrained properties of existing systems are the reason for RCA itself rather than a variable constituent of that process.

## Time

It is clear that any form of RCA must be a time consuming process. It is equally clear that, in a commercial context at least, the time available for RCA will be limited. In this sense, time may be treated as a resource that has value in use for clients and engineers. It seems a plausible hypothesis that the quality of requirements specifications (i.e. RCA output) will vary directly with the amount of time allocated to RCA production. Beyond a certain point, however, increased time allocation may result in less than proportional increases in output quality, due to the persistence of other determinants of quality. The existence of such diminishing returns, or conversely, increasing returns, would depend on the specific circumstances of particular projects. There are at present no theoretical economic grounds for making a priori claims about the degree of returns to be expected from changes in time allocated to information production processes. Empirical investigation of the quality increases obtainable from increased time allocation could yield useful insights for RCA resource allocation.

In principle, time resource constraints may often be overcome by managerial decisions to allocate more time to RCA for a given project. However, two potential problems must be noted here. The first problem is that time may not always be directly substituted by other resources. While some resource substitution may be feasible in some circumstances, all RCA projects must be subject to minimum necessary time constraints; all IT systems have a positive gestation period, none can be created instantaneously. The second problem derives from the commercial innovation environment: it is that there is a potential conflict between the development of ever more complex technical systems and the increasing rate of innovation in the IT and telecommunications industries $^{15}$ . In order for systems to become more complex, increased time will be necessary for their specification and development. As the commercially viable life-cycle of IT systems (notably those as or within products) continues to decrease, sooner or later the minimum time necessary for RCA for a given project will exceed that project's commercially viable life-span. Whether or not this practical impasse is ever reached, it is identifiable as a probable outcome of current trends in IT innovation. The lesson for RCA methods researchers is that time, as an allocatable resource, must be analysed both in micro (project-level) and macro (industrial innovation) terms. Failure to account for relevant industrial issues may result in technically feasible RCA methods being commercially unviable.

## Information

Four examples of information resource inputs to RCA are set out in Table 2. First, 'RCA method' represents the technology of the RCA process itself. Some such technology is a necessary condition for any form of RCA as an information production process; the use of formalized methods rather than informal ad hoc methods merely represents an economic choice of technique. Second, any RCA process must involve inputs of unprocessed information (RCA data) from clients and engineers. If either one of these agents fails to generate relevant input resources, the other's input would be of little value; in effect, either party would produce an unguided monologue that could not be critically evaluated. Third, assuming that the adopted RCA technique allows clients and engineers each to seek clarification of data provided by the other, the RCA production process must involve 'intermediate' inputs of information. Hypotheses (and other ex ante forecasts) and draft specifications would be input resources of this type. Fourth, any RCA process takes place in context, even if that technical, economic (social etc.) environment is apparently rather restricted. 'Contextual' information inputs to RCA are considered here to encompass any necessary or significant information derived from sources external to the client and engineer. Information on resource constraints, or on the commercial viability of a constructed requirements specification, would be included here.

Information resource inputs to RCA are constrained in two ways. First, information is costly to acquire and to evaluate; the acquisition of information is itself a resource consuming process $^{17}$ . Second, there are logical and temporal limitations on the types of information that may be acquired at any given stage of the RCA process. In particular, there is a significant difference between ex post empirical information which, in principle, can be acquired by clients or engineers, and ex ante predictive information which, in principle, cannot be acquired in the same sense. For example, ex ante empirical information about the properties of systems yet to be constructed is simply unobtainable; indeed, it is a contradiction in terms.

In addition, it is possible to consider communication and computation as limited resources within the RCA production process. For example, necessary exchanges of information between clients and engineers depend on the use of the participants' limited capacity for communication (over any given time period). Some uses of that communication capacity resource are likely to be more valuable or productive than others. Similarly, clients and engineers have only limited capacities for computation (in the broadest sense) which constrain the extent of analysis of requirements. Again, some uses of this computation capacity resource are likely to be more valuable or productive than others. Choices between alternative uses of resources imply the need for allocative decisions.

## Allocation of resources to RCA

It must be stated immediately that no ready-made economic models are adequate to the task of aiding the efficient allocation of resources to RCA. Neither is it likely that any such applicable model will be developed within the immediate future, given the state of current research in the field. However, progress can be made in two areas: first, in analysis of factors which are relevant to resource allocation and second, in making RCA practitioners and resource managers aware of the economic dimensions of RCA as a resource consuming process.

Given that RCA is an information production process related to R&D, the work in economics most directly applicable here concerns the economics of R&D, invention, innovation and technology policy. Despite its origins in Arrow's $^{18}$ analysis of 'Economic welfare and the allocation of resources for invention' and the subsequent burgeoning literature, the problem of how to allocate resources efficiently to R&D activities remains unresolved. In particular, the relative efficiency of market and quasi-market allocative mechanisms versus centralized (monopolistic) decision-making structures remains open to debate. This question is related to the broader issue of the efficient organization of large firms $^{19,20}$ ; for example, how might any large IT user allocate resources internally between activities and between development projects.

Following recent work by Dasgupta and Stone-man $^{21}$ , Dosi et al $^{22}$ , Hagedoorn $^{23}$ , Gerrard $^{24}$ and others, three factors have been identified here as directly pertinent to the allocation of resources to RCA:

\- Concepts of markets;

● Risk and uncertainty; and

● Characteristics of information.

Each is discussed briefly below.

## Concepts of markets

A consistent theme in the management of IT literature is the assumption that RCA is part of a process by which the requirements of clients or customers can be satisfied, typically through the production of technically new systems. Closely allied to this theme is the idea that such requirements are formulated and satisfied through market processes. RCA resource allocation is therefore set in a market-related context. The problem here is that at least three radically different concepts of 'markets' are available. These three concepts are liable to be confused, even by economists, with the consequence that unsupportable conclusions are drawn about efficient methods of resource allocation.

Firstly, there is a concept of abstractly 'perfect' markets, from which economists have derived theoretical conclusions, that such markets offer the best possible method of allocating resources between competing agents and activities. This is the concept used by Arrow $^{18}$ in suggesting that competitive markets are more efficient in allocating resources to invention than monopolistic markets. Demsetz $^{25}$ accuses Arrow of adopting a 'nirvana' approach, by ignoring a number of unavoidable sources of market imperfections in the real world.

Secondly, then, there is a theoretical concept of 'imperfect' markets based on possible institutional arrangements rather than an unattainable ideal. While this concept is more realistic than the first, it is still very far from representing the kinds of institutional arrangements to be found through empirical investigation of market processes. Moreover, once the first concept is abandoned, economic theory can no longer justify one institutional arrangement over another in terms of allocative efficiency. (This important though frequently overlooked result is due to Lipsey and Lancaster $^{26}$ .) That is, there are no a priori grounds for claiming that the competitive market is a more efficient means of allocating resources than any other arrangement (e.g. monopoly, centralized decision-making). This means, for example, that there is no theoretical economic justification for a large firm to allocate resources to RCA through the operation of an internal quasi-market.

Thirdly, there is a pragmatic, empirical concept of markets that derives from marketing as a management function, rather than from economic theory (see, for example, Reference 27). This commercial concept of markets is typically used in the development of strategies for profitable corporate activities, not for making micro-decisions about the allocation of resources to particular activities such as RCA. The mistake to be avoided by RCA participants, and RCA methods developers, is believing that the theoretical efficiency results derivable from the first ('nirvana') concept of markets are also derivable from the second or third concepts. They are not. However, this does still allow the possibility that concepts of efficiency and profitability from marketing, as a long-term, strategic planning discipline, might prove useful in the allocation of resources to RCA for large or complex projects.

## Risk and uncertainty

RCA is an uncertain process, like any other form of information production. The allocation of resources to RCA therefore involves, at best, risk and (more likely) uncertainty in the sense of ignorance of quantifiable risk. Specifically, the problem is that the value (success) of the output produced (requirements specifications) will be less than the maximum that could be expected. Available economic theory suggests that the quantities of resources allocated to any activity with an uncertain outcome will depend in part on the degree of risk aversion of relevant decision-makers, such as resource managers (see, for example, References 28 and 29). While quantitative evaluation of risk and uncertainty is technically difficult, conceptually plausible hypotheses about resource allocation and risk aversion can be formed. Two such hypotheses are offered here in relation to RCA.

Firstly, decision-makers who are more risk-averse will tend to allocate fewer resources to high risk projects and more resources to low risk projects. Precisely how risks are to be evaluated, and how quantities of resources are determined, will depend on whether decision-makers are sensitive only to the chance of success of a given proposed project, or whether they take account of absolute levels of expected gains from projects. In this sense, higher risk aversion is likely to result in a lower chance of a given project (and hence its necessary RCA component) being allocated any resources at all.

Secondly, however, the more risk-averse decision-maker is likely to attempt to improve the chances of success of any project which passes an initial selection test. In this situation, RCA offers a mechanism for increasing the amount and quality of information on which a project is to be pursued; improved RCA would be intended to raise the probability of successful system development through a reduction in uncertainty about clients' requirements. Leaving aside the problematic nature of requirements definition, the more risk-averse decision-maker will perceive an incentive to allocate more resources to RCA for any selected project. That is, informally, the truly cautious but effective resource manager will decide: 'If we undertake this project, let's do it properly' rather than 'Let's have a go at any project that looks even remotely possible'. The latter decision rule would be more effective, in economic terms, for the allocation of resources to innovative ('blue-sky') research or the search for inventions.

## Characteristics of information

The economic literature on R&D resource allocation is much preoccupied by the appropriability of benefits to be derived from the sale or use of information. Product design information, for example, is difficult to appropriate; this is one reason for patents, commercial confidentiality agreements and the like. The 'public goods' characteristic of information, whereby its use by one agent need not preclude its use by others, presents resource allocation theorists with severe difficulties. One common result is that non-appropriability leads to systematic under-investment in information production $^{18,21}$ . However, in the case of information about requirements, it is not clear that the question of appropriability is pertinent to RCA resource allocation. Information is inherently heterogeneous and, in the case of RCA, specific to the system development project in hand. While in principle such information might be a public good, and thus be subject to adverse investment incentives, in practice it might only be useful in one specific circumstance. If the use value of a set of requirements information is specific to a given project, the allocation of resources to its acquisition (or construction) will present a different economic problem to that for the production of generic information.

Efficient allocation of resources to RCA will depend, therefore, on the type of project (i.e. type of innovation activity) for which RCA is undertaken. The seven categories of systems development activity, discussed above, serve to illustrate the point. In each case, different forms of supply and demand would imply different possibilities and responsibilities for resource allocation by engineers and their clients.

## Allocative implications of decision models

One reason why economic theory currently fails to provide adequately applicable models for analysis of RCA resource allocation, is that all available approaches to resource allocation are predicated on some form of rational, explicit decisions. It is implicitly or explicitly assumed in the theories on which allocative models are based that, first, complete decision-making structures may be identified (typically, on the basis of incentives to the various agents involved) and, second, rational decisions are actually made. Most notably, results obtained from theoretical treatments of markets, including firms' internal quasi-markets, depend critically on appropriate agents making appropriate decisions. The development of any practical model of RCA resource allocation must confront the question of whether such assumptions are justified, or even credible, in practice. Decisionmaking structures and processes in industry are properly matters for empirical investigation; they cannot be deduced directly from the assumed behaviour of firms or individual agents, or from the quantity or quality of innovations (e.g. new systems) produced. The allocative implications of decision models depend fundamentally on whether allocative decisions are made in practice by appropriate agents. Accordingly, this section is presented in two parts.

## If decisions are made

Analysis of allocative decision models, commonly used in the economics of R&D, suggests four possible implications of decision-makers adopting consistent methods of allocating resources to RCA:

1. optimal allocation;

2. random misallocation;

3. systematic over-investment; and

4. systematic under-investment.

Cases 1 and 2 are of little interest. Optimal allocation must be ruled out in practice, due to the degrees of uncertainty and indivisibility involved in RCA as an information production process. Random misallocation of resources refers to intermittent or consistent failure of a chosen resource allocation decision method. In principle, the extent of these deviations from optimal or satisfactory outcomes could vary from occasional failures (for example, due to projects being 'special cases') to completely random allocation for any project. However, the characteristics of information suggest that every instance of RCA is a special case, due to the heterogeneity of RCA output as information. For this reason, random misallocation would imply that the adopted decision method failed to provide consistently better results than those obtainable from any random process. In effect, no economically significant decisions would be enacted, even though an economically costly decision process had been undertaken; clearly a very inefficient result.

Systematic variations from optimal resource allocation would, however, have implications both for the outcome of RCA for a given project and for the set of development projects undertaken over a period of time. Case 3, systematic over-investment in RCA, would most probably lead to inefficiency and/or over-engineering within a given systems development project. Over-investment in RCA information production as a whole would have less predictable consequences. It might lead to the production of too many new systems – some of which would be less 'required' than others – and hence to an inefficient use of corporate resources. Yet a recent theme in the management literature (e.g. Reference 30) has been to suggest that firms need greater knowledge of their own operations and their relations with suppliers, customers and rivals in order to survive in competitive markets. RCA enquiries would represent a direct route to such corporate self-knowledge and thus to its potential benefits. Further research including empirical studies would be needed to reveal actual corporate perceptions of over-investment in this area.

By contrast, case 4, systematic under-investment in

RCA, would most probably lead to ineffectiveness in the specification of a given system and/or project failures during development or subsequent operation. Under-investment over time could lead to either too few projects being undertaken or inadequate resources being allocated to projects pursued (or both). In terms of corporate knowledge, these possibilities would respectively imply resource saving in exchange for corporate ignorance, or lack of credibility for the information produced as output from systems known to have being inadequately specified (or both).

The rational decision-maker's choice between cases 3 and 4 would depend on the perceived costs and benefits of these probable outcomes. For non-critical cost-constrained systems, inefficiency may undermine the commercial viability of development projects to the extent that it would be no longer worthwhile proceeding with them. In these cases, over-investment in RCA could negate the rationale for undertaking RCA at all. However, for any form of 'critical' system, inefficiency may prove to be a mere commercial inconvenience in comparison to the consequences of system failures due to ineffective specification. For safety-critical systems, ineffective specifications might well lead to catastrophic results. Here, under-investment in RCA would undermine the critical properties of required systems, again to the extent that further development would be no longer worthwhile. In this way, rational decisions about the allocation of resources to RCA would necessarily have to take account of the required general characteristics, such as cost-effectiveness or safety-criticality, of the system in question. The result of this is a chicken-and-egg problem: resources can only be allocated rationally to RCA once RCA itself has commenced.

## If decisions are not made

Explicit allocative decisions are a necessary condition for any form of rational allocation of resources. If such decisions are not made, resource allocation cannot be held to be rational, controlled or efficient, even by default. By implication, the quantity and quality of output from any production process, for which the resources in question are required as inputs, could not be held to be rationally or efficiently determined. Therefore, if no explicit decisions are made to allocate sets of resources to RCA (for any given project) there could be no basis for making or evaluating claims about the efficiency or effectiveness of any RCA undertaken. Under these circumstances, it would be impossible to define economically rational, or even plausible, expectations about the quantity and quality of requirements specifications (i.e. RCA output) that might be produced.

For example, if RCA is undertaken using just residual resources, left over from other activities subsumed under 'systems analysis', the requirements specification produced is highly unlikely to be the product of an appropriately resourced process. More importantly, irrespective of the actual resources used in practice, the lack of adherence to any demonstrable allocative decision process would prevent any systematic ex post economic evaluation of the output produced. In short, if allocative decisions are not made, there can be no basis for attempts to measure or improve the quantity and quality of RCA outputs. Nor, indeed, could there be an economically rational basis for evaluating productivity or quality in software or systems development as a whole.

## Conclusions

The specification of users' requirements for innovations in IT systems is an activity with strategic significance for organizations in both the public and private sectors. It is a critical step in the process by which investments in new or improved systems are realized in practice. As such, the quality of outputs from RCA directly affects the functionality and reliability of information systems intended to aid achievement of an organization's objectives. If IT systems are to be effective in this regard, they have to be constructed on the basis of requirements specifications which have been derived from known and viable processes. Effective management of RCA as a production process must take account of the costs and feasibility of relevant production activities, i.e. just like other forms of production management. Ignoring these costs and limits is a recipe for failure, both technical and commercial, in IT systems development.

Resource constraints apply both to RCA for any given project as a whole and to specific activities within the RCA process. Limited resources (labour, capital, time, information, and communication and computation capacities) are available for each part of the capture or construction of requirements. Some resource limits may be overcome, while some are inherent properties of the resources in question. Practical benefits may be gained by clients and engineers from explicit recognition of the variously limited resources available for RCA for any given type of IT innovation project.

The efficiency and effectiveness of specifications of requirements depend directly on whether resources are allocated to RCA by design or by default. As a practical step to the improvement of resource allocation, three questions might be addressed by RCA managers and practitioners:

1. Who makes decisions about the types and amounts of resources to be devoted to RCA, for any given project?

2. On what basis are these decisions made?

3. Are these decisions evaluated? If so, how? If not, why not?

These questions doubtless sound familiar. Directly in tune with contemporary management practice, they might be heard in any board meeting. The rationale for asking such questions is simple; it is the same as that most frequently put forward to support proposals for the development of information systems themselves. Corporate activities, undertaken in pursuit of corporate objectives, are constrained by limited resources, including time and information available to respond to the activities of corporate rivals. In order to improve the efficiency and effectiveness of chosen activities and the organization's ability to formulate strategy, improved information systems are required. Such system innovations are costly in terms of scarce resources, costs which sharpen an organization's incentives to construct appropriate and reliable systems within an appropriate time period. That is, an organization has an incentive, derived from its pursuit of corporate objectives, to specify and satisfy its information system requirements within the boundaries of resource feasibility. RCA has no privileged status as an information production activity, somehow removed from the economic environment in which all other corporate activities take place. The rationale for managing RCA as an economic activity is thus precisely the same as that for using RCA-based information systems to aid operational and strategic management activities.

The intention of this paper has been to offer constructive criticism of the notion that RCA is primarily a technical activity rather than part of an important process of economic decision-making. A similar approach might usefully be taken towards the systems development process as a whole, as well as its other constituent parts. It is abundantly clear from experience that the development, maintenance and improvement of IT systems are processes that take place over time and require the allocation of scarce resources for their successful completion. It is equally clear that very many development projects are successfully completed and beneficially used, despite the potential costs and hazards of mis-specification. These characteristics represent sufficient conditions for systems development to be seen in economic terms; conditions which are reinforced by the strategic significance of IT systems as the outcome of investment decisions. This observation suggests a need for an economic theory of systems development that would account for the possibilities and constraints imposed by the scarcity and other characteristics of economic resources. Such a perspective might temper the optimism of both technical and business enthusiasts and help to produce more realistic and effective methods for systems development.

## Acknowledgements

This paper draws in part on results of research undertaken by Martin Bell, Joanna Hodge and the author in 1989-90, at the Department of Philosophy, University of York. The project 'Towards Requirements Construction' was wholly funded by, and undertaken in collaboration with, British Telecom Research Laboratories. I would like to acknowledge the contributions of Brett van Toen, Betsy Cordingley and David Freestone of BTRL, those of my philosophical colleagues and, more recently, comments by Professors Norman Lawrie and Howard Williams of the Department of Management Science, University of Strathclyde. Each, however, remains innocent of any errors or omissions in this work.

## References

1 Boehm, B Software Engineering Economics Prentice-Hall, Englewood Cliff, NJ (1981)

2 CORE CORE - The Method Systems Designers, London (1987)

3 Finkelstein, C An Introduction to Information Engineering Addison-Wesley, Sydney (1989)

4 Longworth, G Realistic User Requirements NCC Publications, Manchester (1987)

5 Galliers, R (ed) Information Analysis Addison-Wesley. Sydney (1987)

6 Land, F and Kennedy-McGregor, M Information and information systems: concepts and perspectives. In Galliers, R (ed) Information Analysis Addison-Wesley, Sydney (1987)

7 Floyd, C and Keil R Adapting software development for systems design with the user. In Galliers, R (ed) Information Analysis Addison-Wesley, Sydney (1987)

8 Valusek, J R and Fryback, D G Information requirements determination: obstacles within, among and between participants. In Galliers, R (ed) Information Analysis Addison-Wesley, Sydney (1987)

9 Boaden, R and Lockett G Information technology, information systems and information management: definiton and development European J. of Inf. Syst. Vol 1 No 1 (1991) pp 23-32

10 Roman, G-C A taxonomy of current issues in requirements engineering IEEE Computer Vol 18 No 4 (April 1985) pp 14-23

11 Greenspan, S J, Borgida, A and Mylopoulos, J A requirements modelling language and its logic Inf. Syst. Vol 11 No 1 (1986) pp 9-23

12 Redmill, F J Difficulties of specifying users' requirements for computer systems and methods of mitigating them British Telecom. Eng. Vol 6 (April 1987) pp 60-67

13 Hepworth, M Geography of the Information Economy Pinter Publishers, London (1989)

14 Monk, P Technological Change in the Information Economy Pinter Publishers, London (1989)

15 Charles, D, Monk, P J and Sciberras, E Technology and Competition in the International Telecommunications Industry Pinter Publishers, London (1989)

16 Capello, R and Williams, H Computer network trajectories and organisational dynamics: a cross national review. In Antonelli, C (ed) The Economics of Information Networks North Holland, Amsterdam (1991)

17 Stigler, G J The economics of information J. of Political Economy Vol 69 No 3 (1961) pp 213-235

18 Arrow, K J Economic welfare and the allocation of resources for invention. In Nelson, R R (ed) The Rate and Direction of Inventive Activity: Economic and Social Factors Princeton University Press, Princeton NJ (1962)

19 Williamson, O E Markets and Hierarchies: Analysis and Antitrust Implications Free Press, New York (1975)

20 Radner, R The internal economy of large firms Supplement to the Economic J. Vol. 96 Conf. Papers 1-22 (1986)

21 Dasgupta, P and Stoneman, P (eds) Economic Policy and Technological Performance Cambridge University Press, Cambridge (1987)

22 Dosi, G et al. (eds) Technical Change and Economic Theory Pinter Publishers, London (1988)

23 Hagedoorn, J The Dynamic Analysis of Innovation and Diffusion Pinter Publishers, London (1989)

24 Gerrard, W Theory of the Capitalist Economy Basil Blackwell, Oxford (1989)

25 Demsetz, H Information and efficiency: another viewpoint J. of Law and Economics Vol XI (1969) pp 1-22

26 Lipsey, R G and Lancaster, K The General Theory of Second Best Rev. of Economic Stud. Vol 24 (1956) pp 11-32

27 Chisnall, P M Strategic Industrial Marketing 2nd edn Prentice Hall International, Hemel Hempstead (1989)

28 Stoneman, P The Economic Analysis of Technology Policy Clarendon Press, Oxford (1987)

29 Dasgupta, P The economic theory of technology policy. In Dasgupta, P and Stoneman, P (eds) Economic Policy and Technological Performance Cambridge University Press, Cambridge (1987)

30 Earl, M (ed) Information Management: The Strategic Dimension Clarendon Press, Oxford (1988)
