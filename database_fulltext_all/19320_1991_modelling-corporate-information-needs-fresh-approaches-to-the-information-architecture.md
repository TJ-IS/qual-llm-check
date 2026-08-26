---
otero_id: 19320
otero_key: "HUNW48HU"
title: "Modelling corporate information needs: fresh approaches to the information architecture"
authors: "Tony Bidgood; Bob Jelley"
year: "1991"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/0963-8687(91)90006-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modelling corporate information needs: fresh approaches to the information architecture

Tony Bidgood and Bob Jelley\*

DCE Information Management Consultancy Ltd., Chester House, Chertsey Road, Woking, Surrey GU21 5BJ, UK

Based on work carried out at Clerical Medical Investment Group (CMIG) during 1990, this article proposes a radical new approach to structuring an information architecture and to defining its inputs (activities and entities), in order to produce an effective business tool.

The article highlights a number of problem areas common to past attempts to produce information architectures, and indicates how the CMIG experience has helped to overcome these, while increasing the value of the architecture to the organization.

The fundamental innovation at CMIG was to separate operational entities and activities from their management counterparts, producing an architecture which:

\- is simpler to construct and to understand;

\- is more flexible and adaptable to new business contexts;

\- can model effectively the management of the business and its potential system requirements.

## Conventional information architecture

An information architecture is a vehicle for determining organizational information needs. It shows how the activities undertaken by the business (or part of it), and the data that these activities require, can be grouped and sequenced, allowing the organization to plan the development of information systems on a rational basis.

A conventional information architecture maps business activities onto their use of data entities. Normally a matrix — often called a 'CRUD' matrix — is used to identify activities which create, read, update or delete each entity. Activities and entities are then clustered such that discrete groups of entities are updated by coherent sets of activities. These clusters may be referred to as 'application areas'.

Ideally, each activity only creates, updates or deletes entities within its own area, and each entity is only created, updated or deleted by activities within its area. This is difficult to achieve in practice.

Unfortunately, information architectures have suffered from a number of quality problems:

● they have been too large;

● they have taken too much effort to produce;

\- they have not been tied effectively to business objectives.

A combination of these factors has, all too often, reduced the long term usefulness of information architectures. The CMIG work has, the authors believe, resolved these issues.

## Clerical Medical Investment Group

CMIG, assisted by DCE Information Management Consultancy, recently completed a Strategic Information Systems Planning (SISP) exercise, to ensure that its information systems would meet the Group's needs in the 1990s.

Historically, systems have been developed according to the discrete functional needs of the individual business areas within the organization; there was considerable duplication of effort between systems, and the existing corporate data model did not allow data planning to be related easily to business processes, particularly at a Group level.

As part of the SISP process, the authors produced an information architecture. This was used, together with other project deliverables, for various purposes:

\- to define the existing system and business contexts for the study;

\- to identify the application areas needed to support business needs;

● to assess the adequacy of existing systems coverage;

● to prioritise and sequence future development work;

● to develop an effective migration plan.

## Overcoming classic problems

An information architecture should assist an organization at various levels: at the strategic level for planning purposes, and at the individual application system level as a starting point for analysis and, in particular, the definition of system scope and interfaces.

The problems commonly encountered with information architectures can be largely overcome by developing a concise and properly segmented strategic architecture and then, later, exploding individual application areas to greater levels of detail.

## Appropriate activities and entities

When producing an information architecture, analysts should avoid too much detail: entities and activities identified should be relevant at the enterprise level, not merely the department level. Each identified activity and entity must be briefly defined, so that business representatives can validate the model, and so that it can be later used by project teams. The more detailed the analysis, the more definitions are required, the more complex and unwieldy the subsequent matrix will become, and the less likely an architecture is to give a clear picture of information needs.

Activity analysis, whether using activity decomposition or data flow diagramming, is more an art than a science. Different analysts will produce very different models, none of them necessarily 'wrong' but each drawn from a particular perspective. The important point is to define a set of activities that the business feels is representative; the words used to describe these can say a lot about an organization's view of itself. For instance, the same set of activities, relating to provision of a quotation, can be viewed from a customer or product perspective, leading to quite different assumptions about their objectives, and about appropriate activities at a lower level.

Activities should be identified at a strategic level, and broken down only to the point where they first become meaningful to the business. Splitting and combining activities will suggest new perspectives, and will demand appropriate renaming. If the decomposition itself is inappropriate, this process will indicate a fresh start: the CMIG decomposition required several fundamental rethinks.

Data modelling suffers, generally, from a pre-occupation with normalization. Although important for database design purposes, at the strategic level it is irrelevant. Strategic data entities are at a high level of abstraction (e.g. customer, product or market) and relationships between such entities, though identifiable, are often very complex and cannot be identified precisely in a strategic exercise. Also attributes, key or otherwise, are not relevant.

One vital aspect of strategic data modelling, however, is the extensive use of partitioning (subtyping), which allows both generalization and specialization to be clearly expressed. Figure 1 illustrates the usefulness of this technique in reducing the number of entities which need to be represented on the matrix.

## Distinguishing operational and management information

Activity and data models, particularly the latter, commonly make no distinction between management and operational areas of information. This complicates the models, and confuses the resulting architecture.

CMIG experience suggests that the activity decomposition should distinguish at the highest level between managing the business (planning, controlling, etc.), managing its resources (enabling, developing, etc.) and performing operational activities (marketing, developing products, selling, etc.). Such a breakdown of activities makes sense in most organizations.

It is, however, difficult to make this split in a data model: management entities such as Plan would have relationships with almost all operational entities. The CMIG solution was to produce a separate data model for purely management entities — Plan, Resource, Objective, etc. — and this separation simplified the task, producing a more powerful and usable model.

The resulting matrix shows explicitly the interactions between management and operational activities and data.

## Identifying common entities

Some data entities are created or updated by many activities. In part, this may be resolved by splitting managing from doing: Plan is updated by various planning activities, not by marketing, selling, etc.

The CMIG study identified that Organization and Person were ‘common entities’, neither management nor operational. It was recognized that these entities would contain any basic data, such as name and address, which could potentially be shared across the Group. More detailed information related to the specific relationships which those people and organizations have with the Group; entities defining such relationships (see Figure 1) are identified and included in the architecture separately where required.

The identification of common entities improved both the clarity and compactness of the matrix, while indicating to the business the fundamentally shared nature of its personal and organizational information.

## Keeping the matrix small

A major problem with information architectures is their sheer size. Cross relating (say) 200 entities with 130 activities — not uncommon — produces a matrix of 26 000 cells. Each must be examined to determine whether the activity creates, reads, updates or deletes the entity. Not only is considerable effort required, but the level of detail is inappropriate for a strategic study — not least because it tends to focus attention on current practice to the exclusion of future requirements.

Components were modelled at a high level of generalization, and only split where this was required to achieve a coherent clustering. Activities or (more rarely) entities were combined where their 'CRUD' behaviour was identical, and where they were closely related in business terms. Components of limited importance for the business were examined for their relevance, and excluded wherever possible.

The authors were able to manage the CMIG matrix firstly by deliberately keeping it at a high level, and secondly by segmenting it using the business management/resource management/operational split outlined above. Although the resulting matrix exceeded the intended maximum of 1000 cells, it was still manageable because of this segmentation.

![](/api/attachments/HUNW48HU/fulltext/images/c7944fc1e6230dbdcb1f70521e0520bceaa1849dda66ed3d83f286cebd90be11.jpg)  
Figure 1. Partitioning the data model: a partial view showing some possible relationships. Entities divided into sub-entities are shown in boxes. Only those entities with direct relationships of interest to the business are represented on the information architecture (shown in capitals).

## Avoiding over-elaboration

Usually, information architectures indicate creates, reads, updates and deletes, often recording all four for a single cell. Besides producing a cluttered-looking matrix, this level of detail is redundant at the strategic level, and at CMIG the decision was made to simplify the architecture to maximize communication, even at the expense of a degree of precision. The following simplifications were adopted:

\- operational information was held indefinitely — although archived after a period — so deletes were ignored;

● activities which created data were assumed also to update and read it;

● activities which updated data were assumed also to read it.

Thus the matrix showed C, U, R or nothing for each cell. For presentation and discussion purposes, a version without reads was used: the elegance of the resulting architecture produced a powerful aid to decision making.

## Pre-sorting the matrix

With a matrix of any size, clustering the cells is a complex, iterative task. The analyst must move rows and columns (and split and combine them) to derive application areas which are discrete, yet meaningful in business terms. A matrix manipulation tool would have been extremely useful, but nothing more than a spreadsheet was available to the authors.

It was decided, therefore, to 'pre-sort' at a high level before the full matrix was drawn. Activities and entities were grouped into half a dozen categories — such as Product Development — and a small 'CRUD' matrix drawn for each. These were then manipulated to achieve an approximate clustering of activities and entities: creates were placed, where possible, above updates and reads. The categories themselves were then sequenced approximately by drawing a higher level matrix, before assembling them into the full matrix. When collated, this already exhibited a significant degree of clustering, and reasonable sequencing.

## Manipulating the full matrix

Manipulating the full matrix, still a time consuming iterative process, was simplified as far as possible:

\- initial sorting used creates only, then updates were added, and finally reads;

\- names of activities and entities were replaced, while manipulating, by code letters and numbers in order to avoid preconceptions (e.g. 'Surely product development should come before marketing?').

Where the sorted matrix did not clearly show discrete clustering, where a small number of creates and updates lay outside the clusters, or where data was updated before it was created, each offending cell had to be re-examined.

Business staff found it difficult to separate an activity into its constituent parts. At the first pass it might appear that an activity created or updated an entity, but a second activity, triggered by the first, might have been responsible. Each such activity was examined to see whether it should be combined with another existing one. Similarly, entities which appeared to be updated before they were created were examined: were there really two distinct entities? In this way, the models and matrix were finalized simultaneously.

## New opportunities

## Mapping current systems onto the architecture

The high level of the architecture, and in particular its segmentation, allowed existing systems to be mapped onto it more effectively than would otherwise be possible. Using the architecture it was possible to answer such questions as 'What potential management information requirements cannot be supported by our existing systems?' and 'Which operational areas have no management control systems in place?'

## Identifying different types of system requirement

The segmented matrix, with operational application areas distinguished from management areas, produced a powerful illustration of the different types of information system required to run the organization.

As can be seen from Figure 2, apart from the ‘common entities’ — Organization and Person — all of the creates and updates occurred within three segments of the matrix:

\- business management — activities and data required to control all aspects of organizational activity;

\- resource management — activities and data required to support the operational running of the organization;

![](/api/attachments/HUNW48HU/fulltext/images/63426d6883a1ed7c2e318de7c3e01123792189aeaf475a0087c30c707c284340.jpg)  
Figure 2. Segmentation of the information architecture. All creates and updates appear within the shaded applications areas.

\- business operations — activities and data concerned with the normal supply chain of the organization.

Reads were concentrated within the clusters in the business operations segments. However, they were virtually ubiquitous in most other segments. Much of this could be attributed to traditional MIS requirements: most of the management activities needed information from all parts of the business. Additionally all activities needed, in principle, access to information created by the business management activities. This reflected the need to plan, monitor and control the business, and indicated a potential need for systems support in this area.

The interaction of the three types of application area formed a coherent control loop (plan/inform and control/do/monitor) for the organization, as illustrated in Figure 3.

## Priority areas for further analysis

As part of the SISP process, the primary role of the information architecture was strategic. To be of practical use on specific application projects a lower level of detail is needed, and there are distinct advantages in developing this after a strategic architecture has been produced:

\- once the information needs of the business at a high level are established, the organization can target more effectively the significant effort required to define lower levels of detail;

\- individual development projects will understand the system interfaces, and will be provided with a head start to their analysis process;

\- information management staff can coordinate system development with their development and maintenance of corporate models.

Expanding an individual application area involves the process — relatively straightforward — of further decomposing relevant activities, and a more detailed analysis of specific areas of the data model. Effort can be concentrated within a manageable area, and focused where the greatest benefit is anticipated.

![](/api/attachments/HUNW48HU/fulltext/images/8af5a44d5495bcb5d9e68fa0d236a443c09f8ec4161fa91d09678e64a5af44a6.jpg)  
Figure 3. Management control loop: Plan - Inform and Control - Do - Monitor.

## A final lesson learned

Apart from the issues and opportunities discussed above, another issue has subsequently emerged. Before the architecture can be expanded for system development purposes, each application area must be checked in detail against the business view of that area. The architecture was created and validated at an enterprise level, but it must also prove its relevance to individual business units.

For project use, the architecture must be fully documented. Each create, update and read must be defined (why? what? when? how?) but it is equally important to identify why the blank cells are empty (why not?).

This reinforces the wisdom of keeping the matrix compact. 1000 definitions, even brief ones, is a fair undertaking, but it is a lot more attractive than 10 000 or 100 000.
