---
otero_id: 26374
otero_key: "BCNVNPWZ"
title: "Innovation and Control in Standards Architectures: The Rise and Fall of Japan's PC-98"
authors: "Joel West; Jason Dedrick"
year: "2000"
journal: "Information Systems Research"
doi: "10.1287/isre.11.2.197.11778"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Innovation and Control in Standards Architectures: The Rise and Fall of Japan’s PC-98

Joel West • Jason Dedrick

Center for Research on Information Technology and Organizations (CRITO), University of California, Irvine, 3200 Berkeley Place, Irvine, California 92697–4650 joelwest@ieee.org • jdedrick@uci.edu

F <sup>or</sup> <sup>more</sup> <sup>than</sup> <sup>a</sup> <sup>decade</sup> <sup>NEC</sup> <sup>dominated</sup> <sup>the</sup> <sup>Japanese</sup> <sup>PC</sup> <sup>market</sup> <sup>with</sup> <sup>its</sup> <sup>PC-98</sup> <sup>architecture,</sup> which was incompatible both with its major Japanese rivals and the global PC standard. However, NEC was powerless to prevent the introduction of Japanese versions of Windows 3.1 and 95 that ran on its competitors’ architectures as well as on the PC-98, unifying the Japanese PC market and creating a common set of application programming interfaces for all Intel-based Japanese PCs. The introduction of Windows rendered obsolete the large DOSbased software library that had provided strong positive externalities for the NEC architecture. Absent those advantages, the market share of the PC-98 standard fell from 60% to 33% in five years, and NEC finally abandoned the PC-98 in favor of the global standard. An examination of the unusual rise and fall of the PC-98 shows how victory in a standards competition can be negated by the introduction of a new architectural layer that spans two or more previously incompatible architectures.

(Standards Competition; Computer Architecture; Application Programming Interface; Network Externalities; Personal Computers; Japan)

Theoretical research on standards competition has focused on the lasting economic advantages accruing to the standard that first earns a dominant market share (Katz and Shapiro 1985, Farrell and Saloner 1985, Besen and Farrell 1994). By virtue of a larger market share, these standards attract a larger supply of complementary assets such as third-party software, which fuels a further market share advantage. When coupled with the costs of switching between standards and the high up front R&D costs associated with such technologies, the net result is “increasing returns to scale” that assure that the standards leader retains that lead for an extended period of time (Arthur 1996).

Such principles of standards competition have been deduced from a succession of well-known standards battles—such as in VCRs, minicomputers, PCs, workstations, and web browsers. The presumption of enduring advantage held by a leading standard has heavily influenced industry and government standards policies (Gomes 1998).

The pattern of standards competition in the Japanese PC industry during the 1980s was consistent with these principles. NEC developed its own PC-98 standard which, although divergent from the global standard, generally paralleled the IBM PC development in the United States. The PC-98 attracted the largest supply of complementary assets, including distributors and software developers, which assured it a majority of the Japanese PC market for more than a decade (Fransman 1995, West and Dedrick 1996, Methe´ et al. 1997).

However, the PC-98 standard was supplanted in less than five years by a series of shifts in PC computer architectures that dramatically grew Japan’s PC market and led it to convergence with the global Wintel PC standard. In 1997, the once dominant PC-98 standard was all but abandoned as NEC struggled to keep up with challenges by both domestic and foreign rivals.

Does the rapid decline of the PC-98 mean, as some have argued, that positive network externalities explain little beyond the other advantages available to a market leader (Liebowitz and Margolis 1994)? Or did NEC fail to execute a network externalities strategy that would assure the permanence of its lead?

We believe the explanation lies in an often overlooked aspect of standards, that is, the frequent use of architectures of related standards to construct I.T. products (Morris and Ferguson 1993). As in the case of the PC industry, a stable competitive environment may exist for a period of time when different firms control different layers of the architecture—applications, the operating system, BIOS, and processor (Grove 1996). However, extant theories ignore the incentive that such differential control provides for architectural innovations to disrupt this stable arrangement. Such architectural innovation can do more to topple incumbents than radical innovation because its impact is not immediately recognized by entrenched incumbents (Henderson and Clark 1990).

In this case, NEC was powerless to prevent a change in its architecture that eliminated the software library advantage it held over its Japanese competitors. The introduction of Windows meant that existing DOSbased programs had to be rewritten to take advantage of the graphical features of the Windows interface; the rules for writing these new applications were determined by the Windows application programming interfaces (APIs) defined by Microsoft. When Microsoft designed a common set of Windows APIs for the Japanese market, it meant that (unlike the DOS era) NEC had to share its software library with its Intel-based rivals. Without an advantage in its software library, NEC soon faced a challenge from arch-rival Fujitsu, which was able to match or beat NEC on the other key attributes of price, performance, marketing, and distribution.

To enable analysis of the PC-98’s decline, the paper first contrasts the leading PC architectures established by IBM and NEC. Building upon IBM’s PC standard, NEC successfully executed an increasing returns strategy within its isolated national market, creating network externalities for the PC-98, amortizing its R&D costs over a larger user base than its domestic competitors, and sustaining its market dominance through the effects of customer lock-in.

However, the PC-98 standard was vulnerable for several reasons. First, its leadership stemmed in part from the fragmentation of its rivals into various mutually incompatible architectures. Second, its proprietary hardware architecture lacked the economies of scale to match the production costs of global standard PC hardware. Finally, low market penetration in Japan’s PC market meant that there were large numbers of non-users without a commitment to any existing standard.

We show how a series of architectural changes in the 1990s—i.e., the introduction of DOS/V and Windows 3.1—united NEC’s competition on the global PC hardware standard, spurred a price war that attracted millions of new buyers into the market, and eventually led to the demise of the PC-98 standard. We conclude by offering general implications of the role of architectural control, based both on the PC-98 case and the recent U.S. “browser wars.”

## Background

Standards battles do not take place in a vacuum. Rather, they are fought in complex national and international environments that include companies, markets, industry structures, and technological developments. To understand the evolution of Japanese PC standards, it must be analyzed within a broader context that includes the history and structure of Japan’s computer market, and the development of the global PC industry.

## Japan’s Computer Market

The origins of Japan’s computer industry were established with the introduction of the first IBM computers in the 1950s. IBM used its combination of technical and marketing prowess to establish its position as the leading seller of mainframe computers in Japan in the 1960s. However, IBM was successfully challenged by

Japanese government policy that both limited IBM’s sales and helped develop viable domestic competitors (Flamm 1987, Anchordoguy 1989, Mason 1992).

The growth of Japanese computer makers fueled and built upon domestic demand until, by the late 1970s, Japanese computer production was second only to that of the United States (Flamm 1988). Since the late 1970s, three large, vertically integrated computer and telecommunications firms—Fujitsu, Hitachi and NEC—have consistently accounted for 60% of the Japanese mainframe market. Including second-place IBM Japan, the top four firms account for 85%.

Despite the broad diffusion of computers, Japanese users have been generally conservative and slow to adopt new technologies. While PCs and packaged software were quickly embraced in the United States and many other markets, Japanese corporations preferred to stay with large-scale systems and custom software for three reasons (Baba et al. 1996). First, companies faced both difficulties in handling the Japanese language on computer keyboards, and a shortage of keyboard skills among Japanese workers. Second, the centralized corporate culture of large Japanese firms slowed the move from centralized computing to the decentralized world of PCs and client-server computing. Finally, the belief that custom software applications were a source of competitive advantage—reinforced by the mainframe computer vendors who wanted their customers to remained locked-in to their proprietary platform—meant that firms did not shift to open systems and packaged software solutions until very recently (Dedrick and Kraemer 1998). Together, these factors helped mute and delay the impact of the PC revolution in Japan.

## Birth and Growth of the Global PC Industry

In Japan as in the United States, postwar digital computers began as large, centralized resources owned and shared within the largest firms. Even with the introduction of minicomputers, computers remained large-budget items. This centralized vision of computing was eventually disrupted by the invention of the microprocessor, a single low-cost chip that could serve as a computer’s central processing unit. Intel introduced the first microprocessor, its 4004, in November 1971, followed by the more powerful 8008 (1972) and the 8080 (1974) models, as well as rival products from firms such as Motorola and National Semiconductor.

It was the 8080, however, that launched the PC industry in the United States, leading to a burst of entrepreneurial company formation, both by builders of personal computers and those that offered complementary hardware and software products. Preassembled computers and prewritten application software packages expanded the market beyond hobbyists, and the market focus shifted from hobbyists to businesses in the early 1980s (Venkatesh and Vitalari 1986).

Similar technical and market changes emerged in Japan. In 1974, Sord Computer Company introduced Japan’s first PC based on the Intel 8080 (Levering et al. 1984). Meanwhile, NEC sold microcomputer kits like the TK-50 to boost demand for its microprocessors. In 1979, it released its first assembled PC, the PC-8001, which became the top selling 8-bit PC in Japan, gaining 44% of the market from 1980–1982 (Kobayashi 1986, Fransman 1995, p. 274; Horiguchi 1983, pp. 30–31). Meanwhile, PC production for domestic use soared from 9,143 units in 1978 to 683,051 units in 1982 (IBM Japan 1988 pp. 231).

IBM Defines Global Standard for PC Architecture. A technological discontinuity such as the microprocessor leads to a period of technological experimentation and variation, eventually ending with the establishment of a dominant design that “incorporates a range of basic choices about the design that are not revisited in every subsequent design” (Henderson and Clark 1990 p. 14). After this, technological evolution focuses on incremental improvements to this benchmark (Anderson and Tushman 1990). The dominant design for PC product attributes was set with the introduction of the IBM PC in August 1981, the first popular PC based on a 16-bit microprocessor, which helped it to nullify the head start of various (mutually incompatible) 8-bit PCs.

The IBM PC set the benchmark for subsequent PCs, and also established its architecture as the standard for most of the global personal computer industry. The success of the IBM PC architecture enabled a wide range of complementary products—components, expansion boards, peripherals, software—that fueled the growth of the global personal computer industry, particularly in the United States and East Asia (Langlois 1992, Dedrick and Kraemer 1998).

To encourage this ready supply of complementary hardware and software products, IBM had deliberately adopted an “open architecture” like that of the Apple II. However, unlike Apple, IBM controlled only the middle layer of the PC architecture, the BIOS. In its rush to market, IBM had purchased the other key layers from outside suppliers—the processor from Intel and the operating system from Microsoft—who eagerly sold these technologies to IBM’s competitors. IBM had hoped to preserve control of the entire PC architecture through intellectual property protection of its BIOS. However, while direct copies of IBM’s lowlevel BIOS were prohibited, court rulings allowed various indirect reverse engineering methods, leading to direct substitutes for IBM’s PC series, the “100% compatible” or “clones.” The ready supply of such clones assured the success of the IBM PC architecture but nullified a major source of competitive advantage for IBM (Chposky and Leonsis 1988, Langlois 1992).

Complementary Assets and Network Externalities: the Role of Software. The same open architecture that made cloning easier was spawned by IBM’s desire to quickly obtain necessary complementary assets such as software (Chposky and Leonsis 1988). The success of I.T. product standards can be crucially dependent on the availability of complementary assets. Unlike prepackaged appliances, these systems gain much of their value from user-selected combinations of modular components (Langlois and Robertson 1995).

Some complementary assets may be shared by rival standards within the same product category, such as small hard disk drives or the PC distribution system in the United States. For these assets, as the industry grows and thrives, the benefits (e.g. reduced cost, increased availability) are shared by all products. Other assets—which Teece (1986) calls “cospecialized assets”—are not available for use with products of a competing standard. The most common example for personal computers is software, where, for example, a spreadsheet application will run under Microsoft’s Windows but not Apple’s Mac OS.

Such specialized assets make it difficult for a later entrant to overtake a successfully established dominant standard such as the IBM PC for two reasons (Katz and Shapiro 1994, Arthur 1996). First, a user investment in standard-specific assets makes it expensive to abandon that standard in favor of another, so such asymmetric switching costs mean that the customer is more likely to buy successive products that adhere to the same standard. Second, positive network externalities mean that the more people who join a network of users, the more each user benefits. Such benefits are both direct and indirect. The direct benefit is the ability to share data, files, or other content (e.g., videotapes, CDs) with other users of the same standard. The indirect benefit is that the larger the network, the more attractive it is to providers of complementary assets such as software, which in turn increases the availability of software.

As its market share quickly grew, the IBM PC attracted a wide range of software, expansion boards, and peripherals that cemented its global dominance. However, by definition such an “open” standard enables intrastandard competition, which for IBM came in the form of the 100% PC-compatible clones. These clone makers (such as Compaq) were able to leverage the complementary assets—hardware, software, and distribution—supporting the IBM PC. On the supply side, they built upon the extensive global supplier base that was developed by IBM at considerable cost, and could buy excess capacity from those suppliers as their production costs declined. On the demand side, the 100% compatibles exploited sales opportunities as second sources for genuine IBM products, and also grabbed market share by offering different features or lower prices than IBM. The effect of this competition is that IBM’s global PC market share declined from 25% in 1985 to just 8% in 1995. Meanwhile, Intel and Microsoft used their control over the microprocessor and operating system standards to sustain market shares of over 80% for those markets (Dedrick and Kraemer 1998).

APIs as the Mediator of Software Compatibility. For one key type of complementary asset—application software—compatibility with a given architectural standard is determined by the set of rules known as application programming interfaces (APIs).<sup>1</sup> These rules define how a software application interacts with the underlying standardized information system, which is often called a “platform.” The APIs themselves are implemented in hardware, firmware, system software, or some combination thereof. They provide both explicit and tacit information to the application programmer; the former is disclosed through formal documentation, while the latter can only be discerned through trial and error tests of an actual system implementation.

These APIs form part of an implicit contract between the owner of a standard and developers of potential complementary assets cospecialized for that standard. The standard owner offers a promise (often explicit) that the APIs will continue with future versions of its information systems, assuring the software developer that it has an adequate period of time to recoup its R&D investment in a series of applications that utilize these APIs. Such a commitment by the standard owner reduces the inefficiency and uncertainty in the development of complementary assets, and thus maximizes the available supply.

APIs determine which information systems can benefit from a given library of third-party complementary assets. For example, since Microsoft defines the APIs for Windows, PC makers must license Windows from Microsoft in order to benefit from the supply of Windows-compatible applications. The ability to define APIs can also be used to establish proprietary standards in a nominally open market, as with the many variants of Unix.

The ability to define and change APIs thus acts as a barrier to competition in the operating system market. As Cusumano and Yoffie (1998 p. 132) argue,

Microsoft has become one of the most profitable companies in the world because it owns the underlying technology that drives PCs. Through its ownership of the operating system, it controls the critical device drivers (software that connects the hardware and the software) as well as the critical APIs or application programming interfaces (software that connects applications to the operating system). No one can copy Windows APIs or device drivers, and Microsoft can change them, eliminate them, or upgrade them, whenever it sees fit.<sup>2</sup>

## The Rise of the PC-98 Architecture in Japan

The establishment of a layered IBM PC architecture as the global standard fueled the growth of both supply and demand in personal computers in most countries. In its annual study of the global computer industry, McKinsey (1996 pp. 2–22) referred to personal computer systems as “the most fragmented hardware segment,” as evidenced by the fact that the top 10 PC makers worldwide held only 53% of the worldwide market in 1995. By contrast, in Japan, NEC alone held a market share of over 50% throughout the 1980s and early 1990s.

The Japan PC market was also the exception to the dominance of the IBM PC architecture among developed countries: It was fragmented among several PC architectures that were based on Intel processors and Microsoft’s DOS operating system, but mutually incompatible with each other and the global IBM PC standard (Cottrell 1996). These incompatible PC standards were developed and maintained by a few vertically integrated firms who consequently failed to leverage the horizontally segmented supply chain that was developing all around it in Asia.

The most successful PCs during this period were those made by NEC, which was able to establish and maintain its PC-98 series as the dominant PC architecture in Japan. NEC took a unique approach among the four major mainframe makers of the time. The other three—Fujitsu, IBM Japan, and Hitachi—viewed the PC as a supplement to their booming mainframe business, marketing it primarily as an access terminal for large computers while trying to avoid cannibalization of mainframe sales; some even called their PCs damutan, for “dumb terminal” (Beirne 1996). Even at outside dealers, sales staff tried to redirect customers from low-priced PCs to high-priced, high-margin office automation minicomputers (Sekiguchi 1997).

However, as the smallest of the top mainframe vendors, NEC was less concerned about cannibalization and recognized the importance of the standalone PC earlier, focusing on small retailers and other markets unserved by existing computer products. It also followed a textbook strategy for establishing a dominant standard based on complementary assets.

## Triumph of the PC-98 Architecture

As in the United States, Japanese companies introduced new PCs based on Intel’s 16-bit microprocessor standard. A few introduced 16-bit products prior to the IBM PC, but NEC was the first Japanese firm to respond to the leading U.S. 16-bit PC architecture. Having previously licensed Basic interpreters from Microsoft for its 8-bit PCs, an NEC executive asked cofounder Bill Gates to develop a Japanese-language version of MS-DOS, “but he was too busy with the U.S. market” (Boyd 1997 p. 30). Instead, NEC acquired the source code to the operating system and made its own modifications. It also emulated IBM’s BIOS-based architecture, but modified the hardware design to include support for Japanese character display, including built-in kanji fonts and a higher resolution (640x400) screen than IBM’s CGA (320x200) standard (See Figure 1).

Fourteen months after the IBM PC was introduced, in October 1982, NEC announced the PC-9801, a full year ahead of major competitors, enabling it to grab a reported 80% of the 16-bit market in the first year. In addition to this head start, NEC leveraged the complementary assets it had established for the 8-bit PC-8001, including distribution channels tailored to personal computers (Fransman 1995 p. 274, Methe´ et al. 1997).

In another carryover from the PC-8001, NEC moved aggressively to promote development of the essential complementary asset, application software. First, NEC designed the PC-98 to be backwards compatible with existing PC-8001 software (Fransman 1995 p. 276). Then NEC distributed detailed specifications and free computers to third-party developers prior to the PC-9801’s release. By 1987 the PC-98 had 3,589 software titles from outside developers—nearly 10 times as many as its leading rival, Fujitsu’s FMR (Umeyama 1996). This included the best-selling word processor (Ichitaroˆ ) and spreadsheet (Lotus 1–2-3). By 1990, NEC had 1,800 vendors selling 11,500 packages of PC-98 compatible software (Fransman 1995 p. 276).

Rival Japanese PC Architectures. NEC’s major computer rivals—Fujitsu, IBM Japan, Hitachi, and Toshiba—developed their own computers based on Intel’s 16-bit processor standard, as did various weaker firms. However, many based their first 16-bit PCs on the CP/M-86 operating system, which was quickly eclipsed in the United States by MS-DOS. Japanese makers that began with CP/M-86 were forced to introduce yet another product line based on MS-DOS and the IBM PC architecture, as Fujitsu did in 1987 with its FMR series.

Figure 1 Comparison of Dominant PC Architectures in the United States and Japan  
![](/api/attachments/BCNVNPWZ/fulltext/images/d7f36a0828c0522bdb441f4c7b7ab9ee5f29145727b24665ab73f36bde0fdca5.jpg)  
A Implementation of the most commonly-used APIs

Although they based their products on the IBM PC standard, each firm (including IBM Japan) made its own kanji-specific modifications to the operating system, BIOS, and hardware. To the extent that these modifications defined new APIs beyond English-language MS-DOS, applications developed using these APIs were mutually incompatible with each other, with the PC-98, and with the global IBM PC standard. Since none of NEC’s competitors gained more than 15% of the market during this era, they were unable to attract the range of application software found on the PC-98 (Cottrell 1996). Several joint attempts were made by rival firms to dislodge NEC from its PC position, the most serious being the “AX” version of the PC/AT standard proposed in 1987 by 19 Japanese companies. However, AX failed to gain market share, in part because its backers did not include any major PC makers.

One firm, Seiko Epson, decided not to compete with PC-98 but to emulate it, announcing the first NECcompatible laptop in 1987, as well as a family of desktop “clones.” NEC sued for copyright infringement, but the two firms settled out of court. Without a line of mainframe computers, Seiko aggressively promoted its PC-98 compatible PCs. By producing clones at a slight discount, Seiko helped solidify the PC-98 standard (Fukunaga 1988).<sup>3</sup>

Unlike IBM in the United States, NEC retained control of proprietary extensions to the Microsoft/Intelbased architecture, specifically the APIs necessary for kanji support. This meant that it controlled access to what became the largest library of application software, a barrier to entry that allowed it to charge premium prices for the PC-98.

Industry Analysis, 1991. By 1991, the PC-98 standard had nearly 60% of the market, most of that held by NEC. The other PC-98 maker, Seiko Epson, was second, closely followed by three other firms: Fujitsu, IBM Japan, and Toshiba. The remaining 18% was split between a variety of firms, including the various members of the AX coalition (see Table 2).

Annual PC sales remained virtually flat from 1990 to 1993, ranging between 2.1 and 2.5 million units. By comparison, U.S. sales increased from 9 million to 14.5 million during this period. As a result, Japan’s PC penetration remained comparatively low for a major industrialized country, at only 8.7 PCs per 100 people in 1994, compared to 28.4 for the United States (World Telecommunication Development Report 1995). There were several major reasons. One is the price of a PC was high, roughly twice that in the United States. Two, the DOS-based interfaces of PCs were hard to use, exacerbated by limited white collar keyboard skills. Last, sales during the 1990–1993 period suffered from an ongoing recession following the speculative “bubble economy” of the late 1980s.

Table 1 Event History in U.S. and Japanese PC Markets

<table><tr><td>Year</td><td>Japan</td><td>U.S.</td></tr><tr><td>1981</td><td></td><td>IBM PC</td></tr><tr><td>1982</td><td>NEC PC-9801</td><td></td></tr><tr><td>1983</td><td>IBM 5550</td><td>Compaq PortableIBM XTLotus 1–2-3</td></tr><tr><td>1984</td><td>Fujitsu FM-16</td><td>Apple MacintoshIBM PC-AT (Intel 80286)</td></tr><tr><td>1985</td><td>Ichitarō for PC-98</td><td>Windows 1.0</td></tr><tr><td>1986</td><td>Apple KanjiTalk 1.0Lotus 1–2-3J</td><td></td></tr><tr><td>1987</td><td>Seiko Epson PC-98 cloneToshiba AT-compatible laptopFujitsu FMRAX Consortium formed</td><td>386-based PCsToshiba AT-compatible laptop</td></tr><tr><td>1988</td><td></td><td></td></tr><tr><td>1989</td><td>Fujitsu FM TownsToshiba Dynabook notebook</td><td></td></tr><tr><td>1990</td><td>IBM Japan announces DOS/V</td><td>486-based PCsWindows 3.0</td></tr><tr><td>1991</td><td>Windows 3.0 (J)OADG formedDOS/V-based PCs</td><td>Macintosh System 7.0</td></tr><tr><td>1992</td><td>KanjiTalk 7.1“Compaq shock” price cuts</td><td>Windows 3.1</td></tr><tr><td>1993</td><td>Windows 3.1 (J)Fujitsu backs DOS/V</td><td></td></tr><tr><td>1994</td><td>Seiko Epson backs DOS/V</td><td>Windows NTPentium-based PCs</td></tr><tr><td>1995</td><td>“Fujitsu shock” price cutsWindows 95</td><td>Packard Bell sells control to NECWindows 95</td></tr><tr><td>1996</td><td>NEC-Packard Bell backs DOS/V</td><td>NEC increases stake in Packard BellFujitsu, Hitachi enter market</td></tr><tr><td>1997</td><td>NEC announces PC98-NX DOS/V systems</td><td></td></tr></table>

Table 2 Leading PC Makers, Market Share and Standard in Japan Market, 1991

<table><tr><td>Rank</td><td>Firm</td><td>Share</td><td>Standard</td></tr><tr><td>1</td><td>NEC</td><td>51.0%</td><td>PC-98</td></tr><tr><td>2</td><td>Seiko Epson</td><td>8.5%</td><td>PC-98</td></tr><tr><td>3</td><td>Fujitsu</td><td>8.2%</td><td>(own)</td></tr><tr><td>4</td><td>IBM Japan</td><td>7.6%</td><td>(own)</td></tr><tr><td>5</td><td>Toshiba</td><td>6.8%</td><td>(own)</td></tr><tr><td>6</td><td>Apple</td><td>5.8%</td><td>(own)</td></tr><tr><td></td><td>Other</td><td>12.2%</td><td>various</td></tr></table>

Source: Nomura Research Institute

## Durability of the PC-98 Architecture During the 1980s

The PC-98 architecture held a comfortable lead during the 1980s, maintaining its market position through an overwhelming array of complementary assets, including application software, distribution channels, support, and maintenance organizations. In this sense, the dominance of the PC-98 regime was consistent with well-understood principles of technological competition, including first mover advantages and the importance of complementary assets.

While the establishment of the PC-98 in Japan paralleled that of the IBM PC in the United States, NEC differed from IBM in achieving a significant and durable advantage. NEC obtained such durable advantage through intellectual property protection (under a different legal regime) for its more substantial customization of the MS-DOS APIs. That durability meant that NEC, unlike IBM, was able to retain competitive advantages that provided both higher market share and higher profits than its rivals. According to one estimate, personal computers accounted for 18% of NEC’s total 1991 sales but 40% of its profits (Tanzer 1992).

The Advantages and Disadvantages of Being First. Being first to establish a market position usually offers pioneers several advantages, including the ability to preempt strategic assets and also—when switching costs are high—to lock customers into the pioneer’s product line (Lieberman and Montgomery 1988, Kerin et al. 1992). NEC built upon these advantages to develop complementary assets to protect its position, and did better than IBM had in the United States in preventing competitors from leveraging these assets. NEC maintained a closed architecture and thus earned most of the hardware sales for that architecture. And, by having its own exclusive dealers, NEC did not have to share its channel with followers as IBM had with Compaq and others in the United States.

NEC did suffer from one problem endemic to successful pioneers, that of incumbent inertia. A pioneer’s tendency towards complacency is exacerbated when substantial visible barriers to entry protect a dominant position for an extended period. The best defense is for a firm to attack its own products before rivals do so, innovating to keep ahead of the competition (Foster 1986). However, owners of the leading standard are particularly reticent to cannibalize that standard, fearing they will undermine the barriers that shielded that standard (and high profits) in the first place (Morris and Ferguson 1993). So, rather than open its standard to even a few competitors, or cut prices to expand the market for its standard, NEC retained a high-price, high-margin strategy that both limited the size of the market for the PC-98 and created an opportunity for rivals to undercut its prices.

Barriers to Entry in the Japanese PC Market. NEC was able to sustain its high prices (and thus profits) because of high entry barriers. First and foremost, NEC reaped the benefits of any dominant computer standard—the lead in network externalities provided by a superior software library. In addition, both NEC and its established rivals were protected by two other barriers—Japan’s industry structure and the technical requirements of supporting the Japanese language.

As many firms have found, the large Japanese market is expensive to enter. NEC, its major rivals, and even many of the smaller PC makers were large, established firms in computers (Fujitsu, IBM Japan), consumer electronics (Sharp, Sony, Matsushita), or both (Hitachi, Toshiba). The Japanese firms were either part of horizontally diversified corporate groups or vertically integrated production systems (keiretsu) (West et al. 1997). Nearly all had established distribution channels, either through subsidiaries or networks of dedicated dealers.

In addition to overcoming the distribution and capitalization obstacles, a new entrant also had to adapt its PC to support the Japanese language. Compared to European languages, displaying Japanese characters requires data for 30 times as many characters (6,000 vs. 200), each drawn at four times the resolution. Thus, Japanese PCs require far more computational horsepower than those using European languages. It was not until the introduction of PCs based on the Intel 386 (1987) and Intel 486 (1990) that PC performance for ordinary word processing become acceptably fast, which meant that office automation minicomputers and standalone word processors remained popular in Japan longer than elsewhere.

Japanese characters are input using front-end processor (FEP) software, which applies complex dictionaries to allow phonetic input of the kanji characters. Such display and input requirements prevented foreign PCs from being sold to all but the small minority of Japanese willing to work in English. In addition, similar issues required major changes to printers and application software, limiting the availability of imports. This language complexity also had prevented the widespread use of typewriters, so few Japanese had the chance to learn typing until wordpro electronic typewriters and Japanese-compatible PCs were developed in the 1980s.

Protected both by the inherent advantages of a dominant standard and by specific barriers to entry in the Japanese market, NEC profited greatly from the PC-98 standard. However, the high prices and low market penetration suggested that NEC might be vulnerable— if these advantages could be overcome by competitors.

## Architectural Innovation and the Fall of the PC-98

As recently as 1991, the PC-98 architecture remained dominant, accounting for a majority of PC sales in Japan, and rivals remained fragmented between multiple architectures. Yet five years later, the PC-98 had been displaced by a new standard and NEC’s market share was falling steadily. What had happened? A series of architectural innovations consolidated NEC’s competition around a single standard, made NEC’s complementary assets obsolete, and opened the market to new competitors. An ensuing series of price wars led to explosive growth in the PC market, bringing in millions of new users who were not committed to the NEC standard. The net result was an end to the dominance of the PC-98.

## Architectural Innovation Challenges the PC-98

Two successive architectural changes in the Japanese PC industry led to the decline of the PC-98 architecture: a new architectural standard for Japanese PCs (DOS/V), and the addition of a new layer on top of all the DOS-based PC architectures (Windows).

Both were architectural innovations (as defined by Henderson and Clark 1990) in that they changed the relationship between the other layers within the product architecture. In particular, both changed the competitive advantage provided by the PC-98 software library. While less dramatic than so-called “radical” innovations, the threat they posed was no less severe:

[A]rchitectural innovations destroy the usefulness of the architectural knowledge of established firms, and . . . this destruction is difficult for firms to recognize and hard to correct. Architectural innovation therefore presents established organizations with subtle challenges that may have significant competitive implications. (Henderson and Clark 1990 p. 9)

In this case, NEC was slow to recognize the degree to which its architectural knowledge was being destroyed, and even when the challenge became clear, there was no obvious response to try to correct the situation.

DOS/V. DOS/V provided a software-only implementation of Japanese language support, replacing the combination of hardware and software used by the

PC-98 and most of its earlier rivals. Compared to earlier PC standards, its main advantages were: (1) it was shared by multiple firms, and (2) it ran on the same global-standard IBM PC-compatibles sold by IBM, Toshiba, and Compaq in the rest of the world, thus allowing these makers to apply global economies of scale to reduce their Japanese-market costs.<sup>4</sup> As a side benefit, it also ran U.S. or European software without modifications (albeit with English menus), and allowed those applications to be localized easily for the Japanese market.

DOS/V was developed initially by IBM Japan as an enhancement of the Japanese-language MS-DOS: Its initial goal was to reduce its development costs by using the same PCs worldwide rather than to provide a market advantage.<sup>5</sup> In effect, DOS/V liberated companies from a flaw caused by premature establishment of the dominant design for PCs in Japan: The PC-98 was designed around hardware modifications to support the Japanese language, and all subsequent Japanese makers of Intel-based PCs (including IBM Japan) had followed suit.

DOS/V was preannounced by IBM Japan in October 1990, and IBM Japan and several other firms shipped the first DOS/V-based PCs the following year. To institutionalize support for DOS/V, IBM Japan formed a new consortium (the Open Application Development Group, or OADG) in March 1991. IBM transferred to OADG the necessary marketing and technical expertise to support DOS/V, risking the invitation of strong competition within the DOS/V standard. DOS/V caught on quickly, winning the support of 23 hardware and software makers by the end of 1991. Toshiba, Sanyo, and Canon joined and shipped DOS/V machines that year, followed by various other non-OADG firms (including Compaq, Dell, and Packard Bell).

Of NEC’s major rivals, IBM Japan unequivocally backed DOS/V from the beginning, as did all Intelbased foreign makers and the minor Japanese players. The second major PC maker to join was Toshiba, which saw the same benefit as IBM Japan—leveraging its much larger overseas sales to reduce production costs for the Japanese market.

The other major PC maker, Fujitsu, publicly fought DOS/V in support of its existing (mutually incompatible) Intel-based architectures, the corporate FMR and consumer/education-oriented FM Towns. Privately, however, it began development of a new DOS/V-compatible series, the FMV, which it unveiled in October 1993. In late 1994, even Seiko Epson announced its shift from PC-98 clones to DOS/V.

The support of major PC makers and explicit attempts to court software developers enabled DOS/V to overcome its early lack of software. By 1994, DOS/ V was compatible with more than 5,000 software packages—quite an increase in four years, though still only one-third the number available on the PC-98. The consolidation of NEC’s competition on a single standard created the first viable challenge to the PC-98, but the deciding blow to NEC came with the introduction of Microsoft Windows 3.1 to Japan.

Windows 3.1 Makes Complementary Assets Obsolete. In Japan as in the United States, it was not until version 3.0 that Windows had a significant impact; even so, 3.0 was purchased on only about 10% of the Intel-based PCs sold in 1991 and 1992. Windows 3.1, introduced in May 1993, was much more popular for two reasons. First, (like its U.S. counterpart) it corrected most of the serious problems in the previous 3.0 version. More significantly, Microsoft made a strategic decision to introduce a single Windows architecture that ran on all MS-DOS systems: PC-98, DOS/V, and other DOS-based systems like Fujitsu’s FMR (See Figure 2). This approach continued with Windows 95, which eliminated the MS-DOS layer and was introduced in Japan in November 1995.

For Windows 3.1 and the subsequent Windows 95/ 98, application software written to support Japanese Windows could run on all Windows-based PCs. Rivals successfully argued that the PC-98 had no functionality advantages under Windows. Meanwhile, the shift in the market to Windows applications obsoleted

Figure 2 Evolution of Architectural Layers in Japanese Personal Computers  
![](/api/attachments/BCNVNPWZ/fulltext/images/956660421070ddbfe46c3f1e6cd36e9f99a337ec08ffb109e7a1263555c7820e.jpg)  
//Implementation of the most commonly-used APIs

NEC’s existing DOS-based software library. With its strategic decision to implement cross-platform Windows compatibility, Microsoft took control of the APIs. These new APIs nullified the huge positive externalities of NEC’s software library, that had protected NEC from serious challenge for more than a decade. NEC was still aided by its vast distribution channels, close ties to corporate users, and strong brand recognition, but even those strengths would not be enough when NEC was challenged by a competitor with comparable assets—Fujitsu.

## Increasing Market Competition

New Entrants Spark Price Competition. Many smaller Japanese PC makers joined the OADG in 1992, including most of the former members of the AX group. More importantly, DOS/V enabled market entry by new firms—foreign makers of Intel-compatible PCs, including five major U.S. firms—Compaq, Dell, DEC, Gateway 2000, and Packard Bell—as well as Acer (Taiwan) and Olivetti (Italy).

To gain market share, Compaq chose to compete on price, leading to the 1992 “Compaq shock.”<sup>6</sup> Shaking up an oligopolistic price system in which other firms generally matched NEC’s high prices, Compaq introduced new PCs at half the price of rival machines.

Japanese makers were forced to cut prices, particularly since consumers had become much more cost conscious during Japan’s extended economic slump. In reality, Compaq was not a serious threat to the established leaders, having minimal name recognition and distribution channels. Its initial successes were limited to foreign-owned multinationals, and its share of Japan’s PC market has never reached 5%. Nevertheless, although it had little direct impact, Compaq introduced the first serious price competition to the Japanese PC market.

Fujitsu Shock. The price cutting begun by Compaq helped Japan’s market grow 50% from 1992 to 1994. Still, it was not until a second round of pricecutting—the “Fujitsu shock” of 1995—that the market exploded, with sales increasing 60% in 1995 alone (IDC

Japan 1996). Sales were helped by growing consumer interest prompted by the “multimedia” fad in 1994 and Internet fever in 1995 (West et al. 1997). PC makers capitalized on this interest by designing machines for the untapped home market, featuring CD-ROM drives and stereo speakers, and adding modems to support the growing number of Internet users. Windows 3.1/ 95 also expanded the home market by offering a graphical user interface to replace the cryptic English commands of MS-DOS.

However, the biggest boost came from the “Fujitsu shock,” when Fujitsu cut prices below even the lowpriced imports. Competitors charged that by losing \$200–\$500 on every PC sold, Fujitsu was buying market share; Fujitsu attributed its losses to long-term investments in distribution that could not be amortized over short-term sales (Beirne 1996).

Why did Fujitsu suddenly shift from a sleepy alsoran to the fastest-growing Japanese PC maker? The urgency came from its dependence on the declining mainframe market, which accounted for about 40% of the company’s computer revenues in 1992—much higher than for NEC, Hitachi, or Toshiba (Poe 1993, Juliussen and Juliussen 1993). So, when Japanese mainframe production fell 40% in two years from its 1991 peak, Fujitsu fell from a ¥12 billion profit in 1991 to its first-ever losses, totaling ¥33 billion in 1992 and ¥38 billion in 1993.

In 1990, Fujitsu installed a new president, Tadashi Sekizawa, a veteran telecommunications manager who replaced a former mainframe executive. To get around the PC myopia of its large systems division, Fujitsu set up a new division to plan, design, and develop the FMV computers using parts sourced on the open market (Beirne 1996). After introduction, it moved aggressively to cut prices, mobilizing its large distributor network and ramping up production in an all-out bid for market share.

The “Fujitsu shock” dwarfed the earlier “Compaq shock.” While Compaq’s price cuts had only a minor impact on its market share, Fujitsu nearly quadrupled its sales in one year, selling almost 1 million PCs in 1995, and its market share more than doubled to 17.5%, second only to NEC. Fujitsu also grew the overall PC market at the same time (Figure 3). In 1996, Fujitsu raised its share to 22%, while NEC’s fell another 7% to 33% (IDC Japan 1997).

Absent the DOS/V and Windows architectural changes, Fujitsu would have been unable to challenge NEC’s dominance in the market. Its earlier FMR series was at a severe disadvantage to the PC-98 because of its smaller software library. However, the new Windows APIs were shared between NEC and its rivals, thus leveling the software playing field, eliminating NEC’s differentiation, and shifting the basis of competition between PCs to price.

NEC’s Response. The introduction of Windows left NEC with few strategic options, none of them very appealing. First, it could try to protect its lead by aggressively cutting prices on the PC-98, a strategy that might have worked if the only competition were Compaq or IBM. However, NEC could not hope to prevail in a price war with Fujitsu, which could match NEC’s Japanese distribution channels and presence in corporate markets. Given the higher production costs of the largely proprietary PC-98, NEC would have faced huge losses trying to undercut Fujitsu’s prices. NEC did in fact cut prices significantly, but could not stem the decline of the PC-98 market share.

A second option was to try to fight a standards battle with Microsoft by developing or adopting an alternative graphical user interface (GUI), much as Microsoft has done in its browser war with Netscape. This was unrealistic for several reasons, however. First, NEC is a hardware company, and had relied heavily on its close relationship with Microsoft to develop and upgrade the PC-98 version of DOS. Second, by fighting the Windows tide, NEC would risk being left out as users and application developers all shifted to Windows. Last, NEC would be trying to sustain its national standards island at a time when large Japanese corporations were moving to standardize on a single PC standard worldwide.

Figure 3 Sales of PCs in Japan, 1990–1996  
![](/api/attachments/BCNVNPWZ/fulltext/images/94e7d57a02ef90420b7e83407d1e06d70cfab80dd50d548e7599457c77c99ccb.jpg)  
Source: Nomura Research Institute, IDC Japan

Given this, the only viable option was to abandon the PC-98 architecture and shift to the global standard represented by DOS/V. While NEC ultimately did this, it was loathe to make such a decision, which meant giving up control of most design and engineering decisions and losing a captive market for its affiliated electronic components business. Once the shift was made, NEC’s share of the value added in its PCs shrunk considerably, as it was forced to outsource production and buy components externally in order to be competitive on price.

In the end, to respond to cost and market share pressure, NEC shifted procurement of many PC parts from Japan to Southeast Asia, particularly in 1995 when the value of the dollar dropped to a record low of ¥80. It also increased the share of imported components from 20% in 1992 to more than 60% for desktop PCs shipped in 1996, and even announced plans to move PC design to its Hong Kong subsidiary (Takezaki 1997, Fulford 1996).

At the same time, NEC took advantage of the financial troubles of a low-cost U.S. producer of PCs, Packard Bell, by buying effective control of the firm in 1995 in a complex three-way transaction involving Machines Bull of France (Gomes 1996). It used Packard Bell to gain design and production capabilities for global-standard $\mathrm { P C } \mathbf { s } ,$ and in March 1997 announced that it would sell DOS/V machines in Japan under the NEC brand name. In October 1997, it unveiled its PC98-NX product line, at long last abandoning the PC-98 architecture that had provided it with the largest share of the Japanese PC market for nearly 15 years.

However, the acquisition of Packard Bell and a shift to the global standard failed to improve NEC’s global competitiveness. Both NEC’s and Packard Bell’s market shares rapidly declined in their respective home markets, and Packard Bell’s reputation for poor quality began to tarnish the NEC brand in the U.S. market.

Winners and Losers. Two firms enjoyed the full benefits of the architectural revolution. The biggest winner was Microsoft, which gained sales not only because increased PC sales sold more operating systems, but also because the use of the IBM PC standard made it easier to adapt its U.S. applications to the Japanese market. Its sales doubled in 1995, to more than the next four largest PC software makers in the Japanese market combined (Nikkei Pasokon 1996).

Additionally, Fujitsu quickly exploited the DOS/V market opportunity to grab market share from NEC, increased its sales five-fold in two years, and gained capabilities for the global PC market. But by the end of 1996, Fujitsu called a cease fire in the price wars, and average PC prices drifted upward again in Japan (Umeyama 1996). Higher prices, combined with lower production costs resulting from economies of scale, boosted Fujitsu’s profit margins in the Japanese market, much as the company had hoped when it launched its market share strategy.

As any economist would have predicted, users (in both households and firms) also benefited from increased competition and lower prices, which now matched international levels. Many new users moved to adopt PCs, develop networks, and connect to the Internet.

Not surprisingly, the losers were the two firms wedded to the PC-98. NEC lost market share, market dominance and its profit sanctuary, although total sales increased. Seiko Epson dropped from being a major producer to being completely irrelevant when its position as the low-priced solution was obsoleted by many DOS/V machines (Table 3).

The results for the other three major PC producers are less clear. IBM Japan successfully reduced its costs and tripled its sales from 1994 to 1996, but it failed to appreciably increase market share. Toshiba lost market share in Japan, but, like IBM, it gained from producing one PC design worldwide and its global position improved. Apple saw its sales increase 650% (and its market share increase five-fold) from 1990 to 1994, but was unable to sustain that growth as a result of executive blunders in the United States and the concomitant concern by users about its future.

Table 3 Comparison of Japanese and World Market Shares, 1991– 1995

<table><tr><td rowspan="2">Firm</td><td colspan="2">1991 Share</td><td colspan="2">1995 Share</td></tr><tr><td>Japan†</td><td>World††</td><td>Japan†</td><td>World††</td></tr><tr><td>NEC</td><td>51.0%</td><td>10.1</td><td>41.2%</td><td>7.9</td></tr><tr><td>Seiko Epson</td><td>8.5</td><td>n/a</td><td>2.5</td><td>n/a</td></tr><tr><td>Fujitsu</td><td>8.2</td><td>4.1</td><td>17.5</td><td>2.2</td></tr><tr><td>Toshiba</td><td>6.8</td><td>4.2</td><td>3.7</td><td>4.0</td></tr><tr><td>IBM</td><td>7.6</td><td>18.2</td><td>8.8</td><td>8.9</td></tr><tr><td>Compaq</td><td>0.0</td><td>5.2</td><td>3.3</td><td>11.1</td></tr><tr><td>Apple</td><td>5.8</td><td>10.1</td><td>12.6</td><td>9.7</td></tr><tr><td>Other</td><td>12.2</td><td>49.8</td><td>10.3</td><td>56.2</td></tr></table>

†Unit sales; source: Nomura Research Institute  
††Revenues; source: McKinsey & Co.

The new challengers had more symbolic than actual effect on the Japanese market. The share of U.S. makers peaked at 30% in 1994, then declined in the face of Fujitsu’s price war. After entering in October 1992, Compaq managed to increase its share to nearly 4% in 1994, but fell again when it failed to match price-cutting and promotional spending by NEC and Fujitsu. Compaq also briefly held the top spot in the lucrative PC server market in 1995, but slipped behind both NEC and Fujitsu the following year (IDC Japan 1996, 1997). One analyst noted Compaq’s local performance was constrained by broader corporate objectives: “If you want to have a profit every quarter, Compaq’s strategy was not so bad” (Arai 1997). The subsequent softening of the Japanese PC market (as the country recorded negative GDP growth in 1997 and 1998) suggested that Compaq’s caution was well grounded.

Unintended Consequences: New Entrants in the U.S. Market. Other foreign makers new to the Japanese market—Dell, Acer, and DEC—were unable to match even Compaq’s limited success. Meanwhile, the foreign DOS/V challengers unintentionally widened the geographic scope of PC competition.

Finally, the adoption of the global PC standard by Japanese makers allowed them to enter (or reenter) the United States and other foreign markets in 1996, using hardware designs developed for DOS/V. Vendors such as Fujitsu, Hitachi, and Toshiba failed to capture sizable U.S. market shares, but increased the pricing pressures for U.S. makers in their home market. DOS/ V also enabled entry by non-PC makers, most notably Sony, which had its first successful computer product ever with the introduction of its lightweight Vaio notebooks in Japan and the United States. While IBM and Compaq saw Japan’s PC-98 standard as vulnerable to an outside challenge, only a few foresaw that increased domestic competition would ultimately improve the efficiency of Japanese makers and their PC exports. However, one analyst noted in 1992:

Longer term, IBM’s and Apple’s success in Japan could make Japan a stronger competitor in PCs. The Japanese computer industry will never admit it, but the tradition of closed architectures and high hardware and software prices has been a disaster for Japan. Proportional to population, Japan’s installed base of personal computers is much less than half that of the U.S., and Japan has lagged years behind the U.S. in every PC industry trend—from networking and downsizing to the growth of sophisticated packaged software. By shutting itself off from the world, Japan was never able to build much of a personal computer export industry. (Tanzer 1992)

United States firms may take comfort from past exaggerated predictions of Japanese success which assumed Japanese electronics firms would triumph in PCs as they had in consumer electronics. One such prediction came from Intel’s Andrew Grove, who in 1990 forecast that Japanese companies would capture over 40% of the worldwide PC market by 1992, with U.S. companies’ share falling to 38% (New York Times, May 2, 1990); the actual share for Japanese and U.S. firms in 1995 were instead around 20% and 50% (McKinsey 1996).

At the same time, Japanese PC makers have already improved their technical and marketing proficiency based on lessons learned in Japan from the DOS/V challenge. Their new offerings in the U.S. market are bound to cost existing firms both market share and profits, particularly in the notebook market. However, the ultimate test for both U.S. and Japanese makers will not be decided in their respective home markets, but in the overall global market.

## Analysis

Architectural Control in Dynamic Industries The rise and fall of the PC-98 highlights two different normative models of standards competition.

In one model, standards competition is a one-time battle between rival standards that ends when one side accrues the overwhelming majority of the market (Cusumano et al. 1992). Various consumer products have followed this pattern: videocassette recorders and analog, and digital audio tape formats. Meanwhile, the video game industry has seen a series of such one-time battles, with each generation of technology bringing new competing systems and little carryover of advantage between generations.

In contrast to such a static view, others propose that competition between standards (or architectures of related standards) is an ongoing process in which control of a standard is used to drive its evolution and maintain competitive advantage (Morris and Ferguson 1993, Garud and Kumaraswamy 1993). This was the approach taken in engineering workstations.

Which model is correct—or when might we expect each model to apply? The normative implications are quite different for the firms that develop and promote a new standard: Should they gird for an all-out initial battle, or prepare for sustained competition? The question is also important to those firms (e.g., PDA makers) that must pick “sides” in a standards battle, producers of cospecialized assets (such as software), as well as buyers planning long-term investments in I.T. infrastructure.

If we were to look only at the United States, we might conclude that personal computers standards were resolved by a one-time competition. From its 1981 debut with the IBM PC, Microsoft’s DOS has withstood various challengers which offered superior performance on at least one key dimension, such as ease of use (MacOS) or reliability (OS/2). MS-DOS survived through a series of incremental improvements (i.e., Windows) that maintained compatibility with the existing software library that assured its advantage in network externalities.

The processor standard similarly was resolved in 1981, with IBM’s choice of Intel’s first 16-bit processors. These comparatively static OS and processors standards (along with more radical changes in peripheral standards) have had little effect on the relative popularity of various PC vendors, except for those vendors who tied their fates to failed challenges like the Macintosh.

However, the Japanese market suggests a different picture for PC standards competition. NEC, like IBM, won the crucial early battle for its standard but, unlike IBM, was prepared to reap the lion’s share of the rewards through intellectual property it protected against rival PC makers, specifically its custom APIs. Yet its majority standard was toppled in less than five years by a standards coalition that succeeded where others had failed.

What distinguishes NEC’s PC-98 standard from the IBM PC, VHS VCR, and other durable standards victories? While there are many possible explanations, we believe the most important issue was NEC’s inability to prevent Microsoft from introducing a common Windows interface for all Japanese PCs—adding a new architectural layer that erased previous incompatibilities between these PCs. This made the large library of PC-98 applications obsolete, negating NEC’s advantage in complementary assets. It also eliminated any differentiation between the PC-98 and other architectures based on application software compatibility, as all software developers were now writing programs to a common set of Windows APIs. Now NEC had to compete solely on price, distribution, marketing, and services, leaving it vulnerable to intense competition from DOS/V rivals selling low cost hardware built on the global PC standard.

The PC-98 example of shared architectural control— and divergent incentives among standards owners— provides clear evidence about which aspect of architectural control provides a competitive advantage for the standards owner. If, as in personal computers, the key positive network externalities are provided by software, then the most important layer for such network industries is that containing application programming interfaces, which determine which software packages are compatible with a standard.<sup>7</sup> Because NEC could not prevent a new set of APIs, it could not protect the complementary assets that provided its competitive advantage.

Some might argue that the fall of the PC-98 was yet another victory for “open systems,” and thus the Japanese PC market provides additional evidence for the inevitable triumph of “open” over “closed” architectures. There are at least two problems with such an argument.

First, the normal reason “open” multivendor standards (e.g., VHS, the IBM PC) are believed to be more successful is they attract a greater supply of hardware. This supply of hardware leads to greater standard share and a larger supply of software, fueling a positive feedback loop that assures the standard’s inevitable dominance. Since the PC-98 had both the majority of the PC market and the largest supply of software for more than a decade, this dynamic does not explain why the PC-98 share plummeted from 50% in 1994 to negligible levels in 1998.

The second problem with such an “open systems” thesis is that NEC’s problem was not too little openness, but too much. NEC built its architecture upon third-party processor and OS standards available to its rivals. It had little recourse when Microsoft introduced new APIs that eliminated NEC’s differentiation versus its competitors.

The crucial role APIs play in architectural control is consistent with substantive concerns about their role in computer standards. Dissimilar APIs were central in the ongoing failure of rival UNIX variants to merge into a single standard. Microsoft’s control of Windows APIs is the basis of its “Windows everywhere” strategy that has migrated Windows to non-Intel processors. Meanwhile, those seeking antitrust regulation of the firm have claimed that the timing of API disclosure has been a key mediator of Microsoft’s market power (Software Publishers’ Association 1998, Gomes 1998).

## Rival Explanations

There are two rival explanations which we believe complement (but do not supplant) the role of architectural control in the decline of the PC-98.

National Standards Islands. Some could argue that the PC-98 was merely an anachronism, a national standards island that would inevitably disappear in an increasingly globalized world of technology and technical standards. They point to the strong incentive that multinational corporations have to reduce development, manufacturing, and inventory costs by standardizing their goods worldwide, and how this can be used to achieve a pricing advantage over competitors (Methe´ et al. 1998). Such an incentive certainly exists, and explains IBM’s DOS/V initiative, Microsoft’s single Windows API, and the enthusiastic support by global PC makers like Toshiba, Compaq, and Dell. It also explains NEC’s successful efforts to reduce PC-98 manufacturing costs by adopting global standard components.

However, we believe globalization is a necessary but not sufficient condition for the decline of the PC-98. For more than a decade NEC produced computers for export that adhered to the global standard, but never offered those computers to its domestic market until Fall 1997. If Microsoft had not introduced a single version of Windows for the Japanese market, NEC might never have adopted global standard PCs in Japan, because they obliterated the differentiation it had built over a decade between the PC-98 and its competitors. Because globalization pressures have been present for many years, they also do not explain the speed of the PC-98’s collapse in market share.

Low Market Penetration. While NEC held a commanding lead among the PC installed base in the late 1980s and early 1990s, the actual penetration rate of PCs was low compared to the United States and even Europe. This was true not only for home users, but also among managers and ordinary company employees, where as late as 1994 the United States held a greater than 3:1 advantage (West et al 1997). Such low market penetration leaves a large number of buyers who have not made a commitment to any standard. If the market should grow rapidly, it is the new rather than prior buyers that are important in determining the overall standards share (Liebowitz and Margolis 1990).

While low market penetration minimized the impact of switching costs, it did nothing to undercut the significant advantages NEC held in distribution and brand image. If NEC had been able to leverage its large software library to its advantage, it would doubtlessly have won the largest share of the new adopters. But because it did not control the APIs, it faced a new generation of Windows-only users who saw no difference in software library size between NEC and its Intelbased competitors.

## Applicability to Other Settings

The PC-98 story may appear to be an isolated case, but the underlying principles can be applied to any standards architecture where a new layer could render existing complementary assets obsolete.

The addition of a GUI to the IBM PC standard in the United States could potentially have led to a change in API control. In a highly publicized split in 1991, IBM and Microsoft ended their joint development of PC operating systems, with IBM gaining custody of OS/2 and Microsoft keeping Windows. For a variety of marketing and timing reasons, Windows proved more popular. Thus, while the MS-DOS APIs became obsolete—and thus with them the corresponding supply of complementary assets—the replacement APIs were also controlled by Microsoft instead of its challenger, IBM.

The value of the Windows “platform” was, in turn, threatened by the emergence of the Internet as an alternative application platform. The Internet created the first serious threat to Microsoft’s hegemony by providing a set of open protocols that were independent of the underlying hardware device and operating system, which potentially could render irrelevant Microsoft’s control of the APIs for more than 90% of the world’s personal computers.

When Netscape developed its Navigator browser, it pursued a strategy of cross-platform compatibility, similar to Microsoft’s decision to develop one version of Windows for all Japanese Intel-based hardware platforms. This threatened Microsoft, because software programmers began to develop web applications based on Netscape’s APIs, potentially shifting the relevant API definition from the PC operating system layer to the Internet browser layer.

In his May 1995 memo (cited in the 1998 U.S. v. Microsoft anti-trust trial), Microsoft CEO Bill Gates wrote:

If the Netscape API layer were to be firmly established, it could render the Windows advantage in complementary assets obsolete—just as Microsoft had eliminated NEC’s advantage in DOS-based software for its PC-98. To combat this, Microsoft developed a rival browser and bundled it with its Windows 95 and Windows 98 operating systems. This eventually reduced Netscape’s market share and thus its ability to unilaterally define a rival API.

However, as the PC-98 case illustrates, few standards leaders have the resources available to Microsoft to overcome the threat presented by the introduction of a unifying architectural layer. When the competition shifts to a new arena, incumbent leaders are more likely to be slow to recognize the challenge and hesitant to react for fear of jeopardizing their existing position.

## Implications for Theory

Research on the economics of standards (e.g., Katz and Shapiro 1985, Teece 1986, Besen and Farrell 1994) explain the importance of promulgating a successful standard and gaining a supply of complementary assets to raise the relative popularity of that standard. However, these studies generally focus on a one-time competition of two standards that are not evolving over time.

Subsequent papers focus on the role of product architectures in competitive success. Henderson and Clark (1990) introduce the importance of architectural change, but, by focusing on semiconductor manufacturing, do not link this to the role of standards and complementary assets. Both Garud and Kumaraswamy (1993) and Morris and Ferguson (1993) examine the evolution of IT architectural standards for competitive advantage, but do not examine the possibility of architectural change that renders previous complementary assets obsolete.

Based on the dynamics of the PC-98 case, we offer two additions to prior theory. First, a very specific aspect of an IT standards architecture, application programming interfaces, mediates the compatibility of complementary assets. Where such APIs exist, and where the variety of the complementary assets is a major factor in buyer adoption decisions, then, we argue, the APIs are the single most important determinant of the right to profit from architectural evolution.

Second, most modern IT systems are intentionally designed around a modular architecture of standards (Langlois and Robertson 1995) to allow for decentralized product development and standards evolution. While such modular design (intentionally) allows for the complete substitution of products within a given layer, it can also enable (as in Windows 3.1J or Netscape) the addition of an entire new architectural layer with new APIs. If it provides compelling performance benefits, this new layer can make obsolete both the prior supply of complementary assets and the control of (and thus right to profit from) the interfaces for such assets—as happened with the PC-98 and might have happened with Internet browsers.

## Conclusions

While the rise of the PC-98 provides yet another example of the well-known importance of complementary assets, its fall highlights a lesser-known, but equally crucial point: Ceding control of even a small part of a standards architecture enables an architectural innovation that could render those assets obsolete. The PC-98 also serves as a reminder that an advantage based on switching costs will be of little importance in cases of low market penetration, if opponents can find a way to expand the market and attract the large number of uncommitted buyers.

In short, establishing a strong supply of complementary assets may be a necessary condition for success in standards wars, but it is not sufficient. A standards leader can find itself vulnerable to changes in technology and market conditions that nullify its advantages and open it to increased competition, especially if the firm does not control the particular technology that provides access to its positive network externalities.

Acknowledgments. The authors gratefully acknowledge helpful feedback from the associate editor and the anonymous reviewers, as well as Bryan MacQuarrie, Nigel Melville, and seminar participants at New York University Stern School of Business and Kobe University Research Institute for Economics and Business Administration. This research was supported in part by grants from the Computation and Social Systems Program in the Computer, Intelligent Systems, and Engineering Division and the International Program of the Social and Behavioral Sciences Division of the U.S. National Science Foundation. The authors also thank Professor Kenneth L. Kraemer for providing research support and sharing findings from his research in Japan.

## References

Anchordoguy, Marie. 1989. Computers Inc., Harvard University Press, Cambridge, MA.

Anderson, Philip, Michael Tushman. 1990. Technological discontinuities and dominant designs: A cyclical model of technological change. Admin. Sci. Quart. 35(4) 604–633.

Arai, Yasuhiko. 1997. Interview (March 21). Industrial research and management consulting department, Nomura Research Institute. Yokohama, Japan.

Arthur, W. Brian. 1996. Increasing returns and the new world of business. Harvard Bus. Rev. 74(4) 100–109.

Baba, Yasunori, Shinji Takai, Yuji Mizuta. 1996. The user-driven evolution of the Japanese software industry: The case of customized software for mainframes. David C. Mowery, ed. The International Computer Software Industry: A Comparative Study of Industry Evolution and Structure. Oxford University Press, New York.

Beirne, Michael. 1996. Interview (Dec. 17). Fujitsu K. K., Tokyo.

Besen, Stanley M., Joseph Farrell. 1994. Choosing how to compete: Strategies and tactics in standardization. J. Econom. Perspectives 8(2) 117–131.

Boyd, John. 1997. From chaos to competition: Japan’s PC industry in transformation. Comput. Japan 4(4) 29–32.

Chposky, James, Ted Leonsis. 1988. Blue Magic: The People, Power and Politics Behind the IBM Personal Computer. Facts on File, New York.

Cottrell, Tom. 1996. Standards and the arrested development of Japan’s microcomputer software industry. David C. Mowery, ed. The International Computer Software Industry: A Comparative Study of Industry Evolution and Structure. Oxford University Press, New York.

Cusumano, Michael, Yiorgos Mylonadis, Richard Rosenbloom. 1992. Strategic maneuvering and mass-market dynamics: the triumph of VHS over Beta. Bus. History Rev. 66(1) 51–94.

Cusumano, Michael A., David B. Yoffie. 1998. Competing on Internet Time: Lessons from Netscape and Its Battle with Microsoft. Free Press, New York.

Dedrick, Jason, Kenneth L. Kraemer. 1998. Asia’s Computer Challenge: Threat or Opportunity for the United States and the World? Oxford University Press, New York.

Farrell, Joseph, Garth Saloner. 1985. Standardization, compatibility, and innovation. Rand J. Econom. 16(1) 70–83.

Flamm, Kenneth. 1987. Targeting the Computer: Government Support and International Competition. Brookings, Washington, D.C.

——. 1988. Creating the Computer: Government, Industry and High Tech nology. Brookings, Washington, D.C.

Foster, Richard N. 1986. Innovation: The Attacker’s Advantage. Summit, New York.

Fransman, Martin. 1995. Japan’s Computer and Communications Industry. Oxford University Press, Oxford, U.K.

Fukunaga, Hiroshi. 1988. Personal computer competition heats up. Tokyo Bus. Today 58 (September) 32–35.

Fulford, Benjamin. 1996. Price war forces PC industry restructuring; manufacturers turn to imports as margins on profits plummet. Nikkei Weekly February 26.

Garud, Raghu, Arun Kumaraswamy. 1993. Changing competitive dynamics in network industries: An exploration of Sun Microsystems’ open systems strategy. Strategic Management J. 14(5) 351–369.

Gomes, Lee. 1996. Packard Bell’s debt to Intel is trimmed to \$113 million. The Wall Street Journal June 10.

——. 1998. QWERTY spells a saga of market economics. Wall Street Journal, Feb. 25.

Grove, Andrew S. 1996. Only the Paranoid Survive: How to Exploit the Crisis Points That Challenge Every Company and Career. Doubleday, New York.

Henderson, Rebecca M., Kim B. Clark. 1990. Architectural innovation: The reconfiguration of existing product technologies and the failure of established firms. Admin. Sci. Quart. 35(1) 9–30.

Horiguchi, Tetsuo. 1983. Personal Computers in Japan. NTIS PB84- 176510, PB Co., Ltd., Tokyo, Japan.

IBM Japan. 1988. Joˆhoˆ Shori Sangyoˆ Nenpyoˆ (Information Processing Industry Chronology). Nihon IBM K.K., Tokyo, Japan.

IDC Japan. 1996. IDC Japan forecasts Japanese market to surpass 10 million units by 1997. Press release, February 6.

IDC Japan. 1997. IDC Asia/Pacific and IDC Japan announces PC shipment results for 1996. Press release, February 13.

Juliussen, Karen, Egil Juliussen. 1993. Computer Industry Almanac. Computer Industry Almanac, Inc. Lake Tahoe, NV.

Katz, Michael L., Carl Shapiro. 1985. Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3) 424–440.

——, ——. 1994. Systems competition and network effects. J. Econom. Perspectives 8(2) 93–115.

Kerin, Roger A., P. Rajan Varadarajan, Robert A. Peterson. 1992. First-Mover advantage: A synthesis, conceptual framework, and research propositions. J. Marketing 56(4) 33–52.

Kobayashi, Koji. 1986. Computers and Communications. MIT Press, Cambridge, MA.

Kraemer, Kenneth L., Jason Dedrick. 1998. Competing in Computers. Oxford University Press, New York. Forthcoming.

Langlois, Richard. 1992. External economies and economic progress: The case of the microcomputer industry. Bus. History Rev. 66(1) 1–50.

——, Paul Robertson. 1995. Firms, Markets and Economic Change. Routledge, London.

Levering, Robert, Michael Katz, Milton Moskowitz. 1984. The Computer Entrepreneurs: Who’s Making It Big and How in America’s Upstart Industry. New American Library, New York.

Lieberman, Marvin B., David B. Montgomery. 1988. First-mover advantages. Strategic Management J. 9 41–58.

Liebowitz, S. J., Stephen E. Margolis. 1990. The fable of the keys. J. Law and Econom. 33(1) 1–26.

Liebowitz, S. J., Stephen E. Margolis. 1994. Network externality—an uncommon tragedy. J. Econom. Perspectives 8(2) 133–150.

Mason, Mark. 1992. American Multinationals and Japan. Harvard University Press, Cambridge, MA.

McKinsey & Co. 1996. The 1996 Report on The Computer Industry. McKinsey & Company, Inc., New York.

Methe´, David T., Ryoko Toyama, Junichiro Miyabe. 1997. Product development strategy and organizational learning: A tale of two PC makers. J. Product Innovation Management 14(5) 323–336.

, ——. 1998. Overcoming a standard bearer: Challenges to NEC’s personal computer in Japan. Acad. Management Proc. ’98, Tech. and Innovation Management Division. San Diego, CA.

Morris, Charles R., Charles H. Ferguson. 1993. How architecture wins technology wars. Harvard Bus. Rev. 71(2) 86–96.

Nikkei Pasokon. 1996. 95nendo Sofutohausu Uriagedaka Rankingu (FY95 Software House Sales Ranking). Aug. 26, 230.

Poe, Robert. 1993. Can Fujitsu reinvent itself? Electr. Bus. Asia 4(1) 34–41.

Sekiguchi, Masuteru. 1997. Interview (March 24). Fujitsu K. K., Tokyo.

Software Publisher’s Association. 1998. Competition in the network market: The Microsoft challenge. June 19.

Takezaki, Noriko. 1997. Balancing price with quality: Japanese PC makers have second thoughts about foreign procurement. Comput. Japan. 4(3) 18–20.

Tanzer, Andrew. 1992. A message from Akihabara. Forbes June 8.

Teece, David. 1986. Profiting from technological innovation: Implications for integration, collaboration, licensing and public policy. Res. Policy 15(6) 285–305.

Umeyama, Takahiko. 1996. Interview (Dec. 18). Systems & Personal Group, IDC Japan, Tokyo.

Venkatesh, Alladi, Nicholas P. Vitalari. 1986. Computing technology for the home: Product strategies for the next generation. J. Product Innovation Management 3(3) 171–186.

West, Joel, Jason Dedrick. 1996. Competing through standards: DOS/V and Japan’s PC market. Strategic Management Society 16th International Conference. Phoenix, AZ.

, ——, Kenneth L. Kraemer. 1997. Back to the future: Japan’s NII plans. Brian Kahin and Ernest Wilson, eds. National Information Initiatives: Vision and Policy Design. MIT Press, Cambridge, MA.

Wilson, David L. 1999. Microsoft executive says Netscape didn’t pose a threat. San Jose Mercury News February 23.

World Telecommunication Development Report. 1995. International Telecommunications Union. Geneva, Switzerland.

Jiro Kokuryo, Associate Editor. This paper was received on May 27, 1997, and was with the authors 4 months for 2 revisions.
