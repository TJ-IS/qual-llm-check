---
otero_id: 21483
otero_key: "WFBK4BX8"
title: "A response to dynamic change in the market place"
authors: "Bill Fulkerson"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00029-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A response to dynamic change in the market place

Bill Fulkerson \*

Deere and Company, Technology Integration, John Deere Road, Moline, IL 61265-8098, USA

## Abstract

Companies can no longer capture market share and gain higher profits by producing large volumes of a standard product for a mass market. Success requires adopting methods in the customer acquisition and order fulfilment processes to manage anticipated change with precision while providing a fast and flexible respond to unanticipated change. This paper describes how technology such as genetic algorithms and autonomous agents can be used to enable a mass customization strategy to respond to this challenge. © 1997 Elsevier Science B.V.

Keywords: Mass customization; Assembly line sequencing; Genetic algorithms; Autonomous agents

## 1. Introduction

Mass customization, the next stage of development in providing products and services, is the production and distribution of goods and services that are tailored to specific customer needs and made available on a timely basis at an acceptable cost. Mass customization thrives in arena comprised of global markets, informed customers, and intelligent systems. This last category is especially important. When machines can be configured as multiple modules or a sales system can track individual customer preference, mass customization becomes a cyclic process of continually improving quality.

Production methods have changed radically in recent years. From prehistory until the industrial age, craft production made high cost, narrowly available products by uncontrolled and highly variable processes. With the coming of the industrial age, mass production made low cost products widely available by adopting controlled standardized processes. By 1975 to 1985, lean production added high quality to low cost by practices such as Total Quality Management (TQM) and employee empowerment to improve manufacturing processes and manage the Supply Chain. By the early 1990's, mass customization began to make low cost, high quality, and tailored products available to individual customers through extensive use of information technology, product design flexibility, and the value chain.

Mass customization exploits capabilities in modular design, efficient production, and marketplace intelligence to translate customer needs into cost-efficient, individually tailored products. It leverages the worker knowledge and teamwork to fully capitalize on the principles and practice of modular design. Modular design has focused upon making the design process more efficient by reducing cost and shortening the product development cycle time. Combining modular products that allow manufacturing flexibility with the adaptability and teamwork of an empowered workforce sets the stage for mass customization. Lean production provides a base for mass customization. The logical progression of learning leads from mass production to lean production to mass customization. $^{1}$ Successful implementation requires an integrated set of adaptive business processes, which are motivated by a strong customer focus. Challenges to success include knowledge of customer needs, supply chain management, organizational culture, production management, effective application of information technology, and control of finished goods cost.

This paper is organized as follows. Section 2 introduces the dynamics of change in the marketplace from a historical perspective and Section 3 relates the impact of that change upon firms. Section 4 presents examples of control systems that apply in most mass customization strategies. Section 5 describes the use of a parallel simulation system to model a firm as a complex adaptive system. Section 6 contains observations and a review. Appendix A covers the technologies assumed in Sections 4 and 5 and Appendix B covers the use and limitations of the biological metaphor.

## 2. Dynamics

Companies can no longer capture market share and gain higher profits by producing large volumes of a standard product for a mass market. Firms that can understand, anticipate, or originate customer preferences and then quickly respond with appropriate products have a business advantage over competitors that are less flexible and lack customer focus. The key to success involves managing the marketing and manufacturing processes that can be anticipated and then implementing fast and flexible processes to respond to unanticipated events.

To remain competitive, firms build to satisfy orders rather than building inventory to satisfy forecasts. This approach requires the manufacturer to understand customer needs, identify products that fulfil those needs, and produce customized products for them. Firms that manage customer orders rather than production schedules can reduce the time lag caused by inventory buffers and distribution delays. A positive feedback loop emerges as wants and needs of the market place are met and then changed over successive cycles. In this environment, aggregate customer orders reflect the marketplace reality more accurately than demand forecasts made by economists, statisticians, or accountants three to six months ago.

## 3. Customization

Customers learn by experience in the marketplace. The customer has always been right—but now, the customer has become king. “Customers do not value merchants who recite monolithic mantras on customer service; they value—and buy—goods and services that meet their specific needs. Business must design and build a peerless set of customization capabilities that meet the singular needs of individual customers [1].”

Technology creates opportunities for change but firms must exploit these opportunities for them to occur. For example, retailers can monitor and respond to all retail transactions in real time at less cost now than it cost to sample a few hundred customer transactions 20 years ago. With ready access to information, selling to a single customer over a lifetime relationship becomes possible [2].

The systems view of the enterprise arises from the network structure of the supply chain. Multiple channels of supply and of distribution create the potential for bi-directional feedback. Redundant supply and demand nodes provides quick, adaptive response to change but defy conventional methods of central control. Much of this paper addresses the issues of decentralized control which apply to the enterprise in general and the supply chain network in particular.

Mass production requires both a stable market place and many internal resources to control standardized processes. A firm has three options to respond to variations in the marketplace: (1) stimulate demand; (2) cut fixed costs; and (3) produce inventory. Mass Customization accommodates continual change through current knowledge of the customer and flexible production.

Product development now includes issues such as time-to-market, quality, reliability, and ease of manufacture. However, customer information remains uncollected. $^{2}$ Firms must initiate a dialogue with individual customers to help them articulate their needs even though the customers often cannot articulate their needs and are confused by too many options.

![](/api/attachments/WFBK4BX8/fulltext/images/4982a5927bd3c4f511ba7aff62ceefb35ef8e529cca664af6ea7ccaca9264a80.jpg)  
Fig. 1. Product design for mass customization.

Knowledge of customer preferences and ability to engage in agile manufacturing will not guarantee success in mass customization. Designers must identify customer preferences for features that change (non-enduring) and features that do not change (enduring). This approach enables a modular product architecture that allows designers to map enduring needs onto a static product platform and non-enduring needs upon interchangeable functional modules that are mated with the platform via a standard interface. See Fig. 1.

Mass customization varies within industry, product, and customer. However, promotion of customization as a universal answer to standardization merely replaces one extreme with another [3]. Since the early 1900s the advocates of mass production have argued that its full potential could only be realized if design, sales, and delivery were standardized as well. This extreme position was modified by the acceptance of market segmentation in the 1950s. The recent trend toward a hybrid solution of ‘customized standardization’ makes mute the argument that product feature aggregation and individualization are necessarily distinct and mutually exclusive practices.

A schematic of a continuum of customization strategies is shown in Fig. 2. Four processes—design, fabrication, assembly, and distribution—are depicted in each strategy. These labels refer, respectively, to the extent which the firm conceives the product initially with regard to a single customer's needs, constructs and then assembles the product respecting those needs, and distributes it individually to a single customer.

Pure standardization is shown on the left and pure customization is shown on the right. The logic that standardization reduces cost by minimizing the number configurations is well known. The ability to control cost while increasing the number of configurations by customization must be learned.

![](/api/attachments/WFBK4BX8/fulltext/images/db8ed54a75349399db9b0b60dd20a930a87b4d22dd087268ebfd1f15ce873125.jpg)  
Fig. 2. A continuum of mass customization strategies.

Standardization begins upstream, near design, and spreads downstream. Customization begins downstream, near the marketplace and spreads upstream. Computer-aided design and manufacturing technologies have enabled firms to move toward the middle ground of customized standardization. The last three strategies (customized standardization, tailored customization, and pure customization) require purposeful product design strategies to enable efficient and economical customization. Another explanation of mass customization amplifies the possibility of customization outside of the factory $[1]$ .

Economic control in production has shifted from the producer to the customer. To achieve the rapid and flexible response required to please the customer, firms have expanded their span of control of the enterprise to include the supply chain. However, the producer has several conflicting goals to be profitable and satisfy the customer. What should be the appropriate level of finished goods inventory on the dealer display floor? The sales department wants a full line of dealer inventory available to motivate sales. Accounting is compelled to limit the dealer inventory to frequently sold models to maintain a sound balance sheet. Manufacturing chooses to produce more of the highly profitable models to achieve financial performance goals.

In addition to conflicting enterprise goals, the size and structure of the supply network can also create problems. In discreet manufacturing industries, a single product line can encompass several hundred suppliers. Flow production capitalizes upon a customer pull strategy to link the network of customers and suppliers directly into the supply chain. In the past, conflicts within the supply chain were accommodated with excess inventory, excess production capacity or intervention by expediters.

As the need to meet competition and produce a consistent flow of products has become increasingly important, information technology has become pervasive in supply chain management. A customer can post a schedule electronically and suppliers instantly become responsible to deliver the requirement when needed under conditions of a negotiated agreement. These agreements usually specify flexible ‘fences’ that express the requirements as an expected amount within high–low limits. See Fig. 3.

In essence, the customer purchases a specified amount of the supplier's production capacity rather than purchasing a specific quantity of parts or components. A large variation in raw material leadtime adversely affects the capability of a firm to produce regardless of whether it is producing for orders or for inventory. Contracting in advance for the specified frequency and volume of raw material deliveries can reduce delivery leadtime and control purchase cost. The producer purchases a prescribed prepaid volume to be delivered periodically at a fixed cost. If smaller volumes are required, the cost remains fixed at the contractual level. If larger volumes are required, the buyer incurs additional costs. Transportation costs are factored in as well. Parameters such as demand levels and frequency of delivery must be chosen for scenarios of inventory policy and demand variation [4].

![](/api/attachments/WFBK4BX8/fulltext/images/5546825755ea2e796cbb864b8fe06d143093b3dcd9ab04d316198e80864d2dd1.jpg)  
Fig. 3. Demand fences.

Viewing the firm as a web of processes that are executed by autonomous agents provides a useful representation of supply, demand, production, and distribution. These agents execute processes to fulfil a rich mosaic of legal, financial, social, and psychological contacts. The different levels of communication and context of a firm represent other dimensions as well. See Fig. 4. Agent technology is explained in Appendix A.

Supply chain management encompass the full range of business processes of the entire enterprise—the immediate firm, suppliers, and customers. The communication infrastructure of the supply chain must enable the entire enterprise to integrate both information and processes. See Fig. 5.

![](/api/attachments/WFBK4BX8/fulltext/images/d4d95e11b3a40c9926d0e1b05e946c51938147606cee158b39ebe8ba51a1ce79.jpg)  
Fig. 4. A view of the enterprise.

![](/api/attachments/WFBK4BX8/fulltext/images/62f626a246f23f10797bfbe81cbcc20762da081705e1cca20e767093c8377eb4.jpg)  
Fig. 5. Schematic of typical supply chain.

On the surface, supply chains appear to be orderly. In Fig. 5, suppliers (-S-) feed raw materials and components for fabrication (-F-) into products that are moved by distributors (-D-) to retailers (-R-). Since most companies qualify their suppliers and their method of transportation, they know the communication and distribution routes of the supply chain. But, the supply chain of the future could become more dynamic if the rate of supplier turn over continues to increase [5] or the trend to mass customization continues unabated. In fact, each node of the supply chain in Fig. 5 could represent another supply chain as depicted in the zoom of S5.

However, orders are not filled continuously. Economic order quantities, container sizes, and transportation schedules all disrupt continuous flow in the supply chain. Since suppliers of raw material and primary parts may serve multiple customers in the same industry, the possibility of uncontrollable disruption is real. As firms continue to revamp and redefine processes, they minimize the number of links and processes needed to satisfy corporate requirements, which in effect short-circuit the supply chain. In the future, supply chain management must adopt self-correcting methods of control to obtain optimal business processes within the constraints of capacity, cost, culture, and contractual obligations. These issues are addressed in more detail in the discussion of planning and simulation.

## 4. Response

One element required for successful flexible production is effective management of the process flow. Poor product flow management causes long manufacturing lead times, uncontrolled work-in-process inventories, and loss of the benefits of flexibility. Synchronized flow remedies these problems by implementing quick changeover, eliminating machine utilization and labor reports, and locating component production adjacent to the point of use.

In short, the customer pulls production from the enterprise with the submission of an order. Pull production enables better control of work-in-process inventories than what is afforded by push production. Successful mass customization requires economies of scope to enable economical production in small lots of a composite family of products rather than large lots of a single product.

## 4.1. Sequencing example

In 1992, John Deere Harvester Works introduced a new line of row crop planter products together with

![](/api/attachments/WFBK4BX8/fulltext/images/b450a67e423a9ae792492c3183b7eebf86acc680cbda4926aa6b7b7f21cbeb0a.jpg)  
Fig. 6. Schematic of a factory.

new production methods. Previously, local dealers assembled frames, components, and options shipped to them from factory inventory. The new line of planters are assembled at the factory and shipped directly to the dealer without entering inventory. The improvement in factory production volume, finished product inventory cost, and delivery time has justified the cost of changing production methods. However, producing all models of planters on a single assembly line presents an extremely complex scheduling problem. Since the daily model mix changes continually, creation of an efficient assembly sequence requires the scheduler to balance conflicting goals of manufacturing and marketing simultaneously.

![](/api/attachments/WFBK4BX8/fulltext/images/0b83455edefbd2e84aa304cb5a25478c7213bfbb155ba519755d2dd47f5c6124.jpg)  
Fig. 7. Production flow.

The Harvester Works created a production facility capable of producing previously configured customer orders. They incorporated a schedule centric mode of operation supported by Just-In-Time production of components in adjacent cells and point-of-use delivery of purchased components. The product flow is shown in Fig. 6. The synchronous final assembly process flows horizontally; the asynchronous cellular manufacturing flow vertically.

Several models of planters are built in a production facility similar to that shown in Fig. 7.

Efficient sequencing of orders can mean the difference between meeting or missing an order delivery date. An efficient assembly sequence balances production performance (worker productivity, operational efficiency, product quality and order cycle time) while controlling cost (among contributing production modules and suppliers). It must accommodate two forms of constraints: strong (illegal and prohibited from occurring) and weak (legal but penalized in proportion to cost). Non-manufacturing constraints such as customer service policies, market-planning goals, order fill priorities, and product distribution strategies must also be included.

The product sequence is generated daily by commercial software, OptiFlex. $^{3}$ It incorporates a proprietary genetic algorithm for sequence generation and an intelligent GUI to enable manual sequencing and sequence repair. An efficient constraint computation engine enables OptiFlex to compute a production sequence without illegal constraint violations while it minimizes the sum of legal constraint penalty scores. The system operates on a PC under Microsoft Windows $^{4}$ with a relational database that stores constraints, dealer orders, product sequences, and operational data. Genetic Algorithms are explained in Appendix A.

## 4.2. Product differentiation example

Mass customization requires coordination of product design and production processes to fill custom orders. For example, a truck production facility must operate to minimize the constraints in assembly, paint, and shipping processes. This example incorporates a concurrent blackboard system to produce a ‘cosmetic’ mass customized truck.

Truck bodies [6] enter the paint shop in random color sequence at a rate of 1/min. They are immediately dispatched to a paint module to be painted a base coat color, sealed with a clear coat, and inspected. The painting process takes slightly less than 3 min. Agents control the choice of paint booth by negotiation via messages. The arrival of a truck triggers the 'dispatcher' to post the color to be painted and prompts the functional paint 'modules' to bid for the job. The 'dispatcher' acknowledges receipt of the bids and assigns the job to the winning 'module'. The winning 'module' accepts the job and the truck moves to that module. Bidding follows these simple rules: (1) bid the same color (to avoid set-up cost); (2) bid a new color (least set-up cost); and (3) bid any color (to keep busy). The amount bid reflects the relative cost of travel time, paint lost cleaning system to change color, and queue length. Agent technology and blackboard systems are explained in Appendix A.

This controller essentially eliminates paint color as an assembly constraint by enabling trucks to be painted in any order. Although the solution it provided was not optimal, savings over the conventional scheduling method were significant. Anecdotal reports estimate the annual savings in paint alone to exceed US\$1M per year.

## 4.3. Scheduling example

The technology of the future holds the promise of incorporating human and software agents to enable decentralized control techniques. Agent technology is explained in Appendix A.

Consider this conventional approach to scheduling:

Step 1: Prepare a plan

Step 2: Order material to plan

Step 3: Schedule to order

Step 3a: Execute the schedule until schedule is complete. STOP! Operating context makes this schedule unfeasible.

Step 3b: Obtain information on current status and repair the schedule.

Step 3c: Return to Step 3a.

Since unfeasible schedules are more numerous than feasible schedules, Step 3 can be a perpetual loop.

The conventional view of factory coordination and control is based upon linear theory when the problem is known to be nonlinear. The constraints and objective functions of all stakeholders are often not known and if known are rarely made explicit. Constraints are often contradictory. Optimal solutions are often intractable. Communication is asynchronous and multiple interactions are required which involve communication with human decision-makers and with computers. Worse, each agent (either human or computer) must divide its resources between many tasks. For example, commercial aircraft may carry passengers and cargo with conflicting time constraints and milestones none of which are optimal for all parties $[7]$ . Rather than assume a centralized decision model that gathers local information and makes an optimal decision, assume that local preferences and local constraints elicited from individual agents can establish a decentralized control using agent auction and bidding.

One such system developed for the Autonomous Agents at Rock Island Arsenal (AARIA) project $[8]$ operates under decentralized control. Local information available to pairs of agents (supplier/producer) form the basis of this self-repairing scheduler. Under decentralized control, the schedule there is no need to compute a new global schedule as in Step 3 above because the schedule is essentially self-repairing.

The purpose of the AARIA project is to demonstrate the feasibility of obtaining the functionality of current manufacturing systems from a population of agents endowed with the abstract properties of various manufacturing entities, resources, and strategies. AARIA customer agents buy products through a direct dialogue with the manufacturing agents that make and deliver orders. These agents negotiate among themselves to make and meet commitments to the customer, trade off customer orders and available resources, and control the lead-time and order cost.

AARIA manufacturing execution system functionality includes simulation, finite capacity scheduling, and intelligent shop floor interfaces. Its enterprise resource planning functionality includes planning, order entry, and purchasing capability as well as bill-of-materials, inventory, resource, and personnel management accompanied by integrated financial reports. Agents self-configure themselves to provide a full enterprise resource planning and manufacturing execution system functionality without need for centralized control. See Fig. 8.

![](/api/attachments/WFBK4BX8/fulltext/images/0f0df047b7d1dfc64ef71375f1b677db4c4e9997e9850f134882bb190a48b96a.jpg)  
Fig. 8. ARRIA system architecture.

Customer and supplier agents negotiate to allocate resources as new jobs enter the system, to optimize schedules across resources, to recover from faults in the factory, to dispatch work against the schedule, and to report results. AARIA design principles include these elements: enterprise resource planning functionality from aggregate agent behavior; treats internal and external suppliers and customers in the same manner; human stakeholders control the system rather than being controlled by it; reconfigures itself dynamically in response to internal and external conditions; Demand develops to meet system commitments to customers—No planning for the planning's sake; operations are scheduled in advance, dispatched, or pulled depending upon status of the factory; and entity information is recorded at each stage of its life cycle (e.g. order, part, production history).

## 5. Planning

Scheduling sequences all material and plant resources, at an operation level, over the near term time horizon. Planning balances material and plant resources to best meet customer demand while achieving business goals. A crucial distinction between planning and scheduling is the tradeoff of time horizon versus level of detail.

\- Schedule-centric systems assume that unless each material requirement, order movement and work center load is scheduled, it is not possible to accurately determine due dates, perform realistic available to promise, or maximize throughput. Schedule-centric systems emphasize available to promise and production scheduling.

\- The planning-centric systems assume that it is much more important to get the plan right. Without a valid plan optimized sequencing does not help, since the planner will be working with the wrong product mix or set of orders. Planning-centric systems emphasize available to promise and enterprise planning.

Unfortunately, both approaches ‘exhort the operator’ rather than take advantage of operator intelligence. Neither approach regards the current context—the space and time window of opportunity—to be a sufficient basis for appropriate action. Both approaches assume the command-and-control orientation of centralized control so schedules are unduly constrained by the plan.

## 5.1. Planning systems

Enterprise Resource Planning systems were designed to control monolithic vertically integrated hierarchical organizations. They develop a detailed schedule of tasks and resources in a chain of linked processes. Each process make increasingly detailed calculations based on aggregated data passed down from the previous process in the planning hierarchy. Should the resulting shop schedule prove to be unfeasible, the reason for this infeasibility is unavailable and there is little or no time in which to recover [9].

The changes required to make the transition from build-and-sell (planning centric) to sense-and-re-spond (schedule centric) firms require a new frame of mind. Unfortunately, firms often use a build-to-plan combined with schedule-to-order and call it build-to-order. This approach limits the firm's ability to respond to customer needs with its ability to plan and forecast rather than by its ability to manufacture.

In general, interpreting planning and scheduling from a build-and-sell perspective negates the benefits of sense-and-respond. Scheduling centric systems retain essential customer information along with the order that makes them ideal for supply chain management. They enable product to be pulled at a metered rate through the complete value chain rather than enforce a precise schedule of material requirements, movement of work-in-process inventory, and work center utilization. Planning remains necessary but subordinate to scheduling. Schedule centric systems can only be effective when operating in a business environment anticipated by effective planning. Simulation supports the planning function.

## 5.2. Planning simulation

A planning simulation in the form of a multi-agent information system includes software agents, tasks, organizations, and information structures. The business entities are represented by physical agents (suppliers, inventory buffers, assemblers) while logical agents control the flow of information and material throughout the enterprise (order entry system, capacity planner, material planner, production scheduler, shop floor controller).

Three levels of organization displayed in Fig. 9 provide a useful model of the firm. In this model, material and tactical information flow horizontally within each level while communication related to governance and strategy flow between the levels. The implicit hierarchical structure of Swarm (depicted in Fig. 10) enables an explicit simulation of all three levels. A one-to-one mapping between supply chains and Swarm capabilities makes model building intuitive [10].

![](/api/attachments/WFBK4BX8/fulltext/images/8c428fa1ffbcdae2bd4831c7f23243300fb8492a5c86295bc9dae871eb284265.jpg)  
Fig. 9. Granularity of agents.

![](/api/attachments/WFBK4BX8/fulltext/images/d6653f5824ba93dd6c911b6aaebe2088f740e6dae169e70d51b6f065cdcb4fc9.jpg)  
Fig. 10. Swarm implementation of supply chain.

Agent technology and Swarm intelligence are explained in Appendix A. The uses and limitations of biological metaphor is explained in Appendix B.

When viewed in the abstract, a supply chain is a sequence of processes beginning with raw material supplier(s) and ending with a consumer that successively transform an input into an output. Contrast the Swarm model in Fig. 10 with the supply chain schematic in Fig. 5.

The following conclusions were obtained from a series of simulated experiments performed with the Swarm simulation platform. These results pertain to specific scenarios of high volume discrete manufacturing and related policies $[11]$ : cycle time can be shortened at the cost of higher raw and work-on-process inventories; combinations of make-to-order (downstream) and make-to-stock or make-to-order policies (upstream) are effective; and variation in demand patterns does not change the relative performance of policy combinations.

Additional results are reported on the value of various information exchange strategies among the business entities in the supply chain. One salient result is that order fulfilment process improvement is more directly influenced by the accuracy of demand information from the customer than by the availability of material information from suppliers. This result reinforces the need for improved market research information on the customer rather than improved supplier information.

## 6. Observations

A successful firm must closely couple vendor, firm, and customer. They must:

• effect shorter order fulfilment cycle times

• produce low volumes of identical items economically

• produce a variety of products

\- adapt (to change in the marketplace with appropriate products) quickly

\- incorporate flexible and adaptable production processes and facilities

Product variety generates complexity in the manufacturing processes including the supply chain. However, product variety benefits the firm if the advantages gained in the marketplace balance the added cost of manufacture. As long as the profit generated by variety exceeds its cost, variety is free. Adoption of a standardized approach to customization is suggested.

Management must provide an appropriate and unambiguous strategic context; identifying key accountabilities and their inter-dependencies; negotiating, rather than assigning, accountability; measuring employee performance of their commitments; and allocating resources to accountabilities that link themselves dynamically.

“The difficulty with all revolutions is this: the leaders think that they can substitute new ideas for old before they have changed the action tendencies, habit systems, of people. As this cannot be done, revolution after revolution fails. The first thing a normal class of revolutionists should be taught is that behavior must be changed through experience, that it cannot be changed through the impact of ideas $[12]$ .” Multi-agent frameworks to organize, model, and evaluate the processes and the supporting information systems involved can provide a useful substitute for experience.

## Appendix A. Technologies

This Appendix contains a technical commentary on two technologies applied in this paper. Genetic algorithms and agents are described within the context of their use in this paper.

## A.1. Genetic algorithms

Genetic algorithms mimic the mechanisms of population biology. The process begins by generating a genetically diverse population composed of a fixed number of candidate solutions, expressed as strings, called chromosomes. A chromosome is composed of genes, each of which can take on a number of values called alleles. In each generation, candidate solutions are selected (by their relative fitness) to generate offspring. New chromosomes are created with two operators—crossover and mutation. At each generation, the population is refreshed with the fittest individuals. A simple flow chart of the steps in a genetic algorithm are outlined below:

1. Determine a stopping time.

2. Initialize a diverse population (fixed size) of chromosomes.

3. Evaluate fitness of each chromosome in the population.

4. Create new chromosomes by mating current chromosomes.

5. Evaluate fitness of new chromosomes.

6. Select most fit chromosome(s) and insert it (them) into the population.

7. If time has expired, STOP and return best chromosome in the population.

8. Otherwise go to Step 4.

While the generic form of the genetic algorithm can be simply explained $[13]$ , its successful application requires intelligent choice of chromosome structures and the operators to match the problem. The chromosome can either be encoded directly with the schedule or indirectly with a schedule builder. Since the search space in the direct method will contain the optimum solution but most of the search space will be unfeasible. The search space of the indirect method will be limited to feasible solutions by the schedule builder. Thus, the indirect method dramatically reduces the size of the search space and saves memory as well. Although genetic algorithms search a state space blindly, the choice of specially designed operators for scheduling problems can limit any inefficiency. Since, no general theory is available practitioners often must rediscover unpublished methods.

## A.2. Agent technology

The definition of an agent varies depending upon the area of application. Areas such as complex adaptive systems, artificial life and evolutionary computation often conceive of agents as relatively simple, but adaptive reactive entities. Classical artificial intelligence emphasizes an engineered construction of intelligent software agents that incorporate the machinery of planning and machine learning.

Agents function as decision-making units that apply internal rules to govern their response. They may act upon messages from other agents, the agent's internal state, or the state of the external environment. When multiple agents interact with each other and their environment, the long-term result behavior is unpredictable. This type of outcome is in direct contrast to Newtonian ‘clockwork’ systems.

More precisely, agents are software objects that consist of $[14]$ : (1) a data structure containing internal state variables local to the agent. This data structure enables an individual-based modelling approach in which past experience affects the next action through the internal state variables, e.g., a bill-of-materials or operational procedures for a process step; (2) a step function to specify action for an active agent prior to receiving a message. e.g. time-of-day warm-up or backup procedures; (3) multiple step functions to specify action when triggered by messages from other agents or system control objects. e.g. orders, tool breakage, unavailable materials.

Intelligent agents perform specific assignments on the behalf of a user such as search the worldwide web for documents, filter e-mail messages, or sound alarms when malfunctions are sensed. These personal assistants improve performance by (1) observing the user perform tasks, (2) accepting positive and negative, feedback from the user (3) accepting instructions from the user or (4) interrogating other agents for information. Autonomous agents learn by interacting with their environment and by exchanging messages with other agents. Their more general, active role enables them to perform general tasks and they may over time assume a persona.

Concurrent blackboard systems can be interpreted as group of cooperating intelligent agents, working to solve a common problem $[15]$ . Each intelligent agent, known as a knowledge source, independently monitors the global background data structure and determines when it can advance the current solution of the problem. The paint shop control system described earlier is a blackboard system. The paint booth allocation is solved asynchronously by multiple agents operating in parallel without contention for memory or information.

The following definition due to Wooldridge and Jennings contains several descriptors usually associated with autonomous agents [16]. “... a hardware or (more usually) software-based computer system that enjoys the following properties. (a) Autonomy:

agents operate without the direct intervention of humans or others, and to some degree controls their actions and internal state. (b) Social ability: agents interact with other agents (and possibly humans) via some kind of agent-communication. (c) Language. (d) Reactivity: agents perceive their environment, (which may be the physical world, a user via a graphical user interface, a collection of other agents, the INTERNET, or perhaps all of these combined), and respond in a timely fashion to changes as they occur. (e) Pro-activity: agents do not only act in response to their environment, they exhibit goal-directed behavior and take the initiative."

The Swarm simulation system ${}^{5}$ is a general-purpose framework developed by the Santa Fe Institute, Artificial Life Group, to simulate various concurrent, distributed artificial worlds across a wide variety of disciplines ranging from physics to biology and to economics. Its generality pertains to the structure of objects or agents belonging to a simulated world as well as to the actions that they can perform.

The recursive management of time supports a full spectrum of temporal and system synchrony management alternatives. These alternatives can vary from a strict, lock-step synchrony of the total system to a loose asynchrony of multiple elements. A single global schedule object may control all agents or a hierarchy of sub-swarms may each be controlled by a local schedule object and coordinated with the global schedule object. This abstract representation of time made possible by the generality of the Swarm schedulers enables efficient simulation on either serial or parallel computer systems and provides the capability for multiple concurrent simulations of a common scenario to reflective evaluation of competing alternatives.

Specifically, a Swarm program differs from other computing formalisms in the following three important ways:

Swarm differs from other computing formalisms in three important ways. (1) Radical concurrency: the elements of program execution can represent events that can happen to many parts of a complex system simultaneously. (2) History: events create a history that can produce enduring change in the system behavior. (3) Indeterminism: the occurrence of events may be stochastic and their relative ordering may not be fully constrained by program specifications.

## Appendix B. Biological metaphor

Biological metaphor is being increasingly used to explain business. “... the economy is not a mechanism, businesses are not machines. They are co-evolving, unpredictable organisms within a constantly shifting business ecosystem that no on controls... Managers of companies both great and small must learn how to co-evolve in this changing environment—to compete with what the competition is becoming not with what it is now [17].” Co-evolution in nature takes the form of predator and prey competition and cooperation. In business co-evolution, two entities iterate through cycles of reciprocal change. The experience of competition and cooperation provides opportunities for learning which force them in the direction of predetermined goals.

Explicit insertion of human cognition remains necessary regardless of the capability of agent representations or the power of computational systems. Human agents are necessary to provide the insight needed for complex systems to achieve useful results in a timely manner. The ability to think in unconventional ways and to invoke models from exogenous contexts is crucial to establishing purpose a priori, rather than as an unpredictable emergent system-level behavior.

## B.1. Swarm intelligence

The building blocks of bottom-up systems, are fine-grained entities present in large numbers called swarms. “Emergent behavior of swarms of agents is often more robust, flexible, and fault tolerant than programmed, top-down organized complexity. This is the case because none of the components is really in charge of producing this complexity. None of the components is more critical than another one. When one of them breaks down, the system demonstrates a graceful degradation of performance. Because all of the components interact in parallel, the system is also able to adapt more quickly to environmental changes. Often the system explores multiple solutions in parallel, so that as soon as certain variables change, the system is capable of changing to an alternative way of doing things” [18].

Traditional education assumes a rational world model that readily lends itself to an analytical solution. However, the simplicity of the rational model masks the nonlinear or irrational nature of the real world which is a complex adaptive system comprised of many agents which that are simultaneously competing, cooperating, collaborating, or just coping. Although the predictive horizon for complex adaptive systems models is short, this limitation does not negate the value of models. The sheer number of predictive variables and the possibility for their interaction must be acknowledged as well. These limitations support the argument against use of deterministic models (as F = MA of Newtonian physics) to predict the behavior of individuals. However, the “... intrinsic unpredictability of individuals has no implication for the unpredictability of aggregates. In the physical sciences, statistical models of phenomena such as magnets and glasses have precisely this property [19].”

In addition to model accuracy, complex adaptive systems models seek to explain behavior and to determine the effect of various interventions. Thus, predictive accuracy of a model with respect to a change in policy is as desirable as predictive accuracy alone. Useful complex adaptive systems models can simultaneously exhibit low predictive accuracy for a scenario but exhibit high predictive accuracy for the effect of change in particular variables.

## B.2. Limitations

There are some problems with the direct transfer of the biological model to business. Nature serves as a useful model for computational schemes. However, Nature's solutions are typically feasible not necessarily optimal. Nature produces a long chain of feasible solutions punctuated by radical improvement or extinction. In organizations, leadership influences change toward improvement or breaks gridlock. Leadership is not control.

New structures or patterns may be overlooked because of human inability to express or perceive their existence. Nature's agents are heterogeneous while social science agents are purposeful or intentional. The self-organization (an emergent behavior) in human social systems is due to purposeful interaction. Since no mathematics exists for computing inverse solutions or determining stopping rules, it may be possible to observe simulation results that cannot be repeated in either simulation or in reality. The benefit of simulation stems from its capability to reveal alternate realities rather than revealing a single reality or solution.

## References

[1] J. Gilmore, J. Pine, The four faces of mass customization, Harvard Business Review, January–February 1997.

[2] D. Pepper, Building Relationships One Customer at a Time. Doubleday, NY, 1993.

[3] J. Lampel, H. Mintzberg, Customizing customization, Sloan Management Review, Fall 1996, pp. 21–30.

[4] M. Henig, Y. Gerchak, R. Ernst, D. Pyke, An inventory model embedded in designing a supply contract, Manage. Sci. 43 (2) (1997).

[5] E. Keller, Turning supply chains into value networks, White Paper, Manufacturing Directions, special Advertising Supplement to Manufacturing Systems, September 1996.

[6] Worried about PLC Programming Productivity? Try Another Flavor. Advanced Manufacturing Research Control Strategy Report, Advanced Manufacturing Research, Boston, MA, June 1992.

[7] P. Harker, L. Ungar. A market-based approach to workflow automation.

[8] H. Parunak, A. Baker, Clark, The AARIA agent architecture: an example of requirements-driven agent-based system design, Proceedings of the International Conference on Autonomous Agents.

[9] J. Bermudez, J. Serface, The advanced planning and scheduling system market, The AMR Report on Manufacturing, Advanced Manufacturing Research, Boston, MA. December 1996 and January 1997.

[10] F-R. Lin, G. Tan, M. Shaw, Multi-agent Enterprise Modelling, Department of Business Administration, University of Illinois, Urbana-Champaign, October 1996.

[11] F-R. Lin, Reengineering the Order Fulfillment Process in Supply Chain Networks: A Multi-agent Information System Approach. Department of Business Administration, University of Illinois, Urbana-Champaign, July 1996.

[12] M. Fowlett. Creative Experience, 1924.

[13] L. Davis (Ed.), Handbook of Genetic Algorithms, Van Nostrand-Reinhold, New York, 1991.

[14] F-R. Lin, Reengineering the Order Fulfillment Process in Supply Chain Networks: A Multi-Agent Information Systems Approach, University of Illinois, Urbana-Champaign, January 1996.

[15] J. McManus, W. Bynum, Design and analysis techniques for concurrent blackboard systems, IEEE Trans. Syst. Man and Cybernetics 26 (6) (1966).

[16] S. Franklin, A. Graesser, Is it an agent, or just a program? A taxonomy for autonomous agents, Proceedings of the Third International Workshop on Agent Theories, Architectures, and Languages, Springer-Verlag, 1996.

[17] J. Moore, The Death of Competition: Leadership and Strategy in the Age of Business Ecosystems, Harper Collins, 1996.

[18] P. Maes, Modeling adaptive autonomous agents, Artificial Life, Vol. 1, No. 1/2.

[19] S. Durlauf, Limits to Science or Limits to Epistemology? Complexity, Wiley, Vol. 2, No. 3.

![](/api/attachments/WFBK4BX8/fulltext/images/304bb46bb2aaad84bd6c1c0be8bc7f923bd5d6c76b0e5cfa99a0553622bf7e3c.jpg)

Bill (William F.) Fulkerson is Staff Analyst, Technology Integration, Computer Information Systems for Deere and Company. He specializes in information technology to enable the order fulfillment and customer acquisition processes of the corporation. He holds degrees in mathematics from Central Missouri State College (BS-64 and MS-65). Prior to joining Technology Integration, Bill had a variety of assignments at Deere and Company in other departments includ ing the Technical Center, Production Engineering, Materials, and Parts Distribution. He has also served as a military operations research analyst for the Gen. Thomas J. Rodman Laboratory at Rock Island, IL, as well as Computer Sciences and Booz-Allen Applied Research, Ft. Leavenworth, KS. Bill also was Instructor of Mathematics, Central Missouri State University.
