---
otero_id: 17787
otero_key: "VA9XEPP2"
title: "A forecast of the future of computation"
authors: "Carl Hammer"
year: "1977"
journal: "Information & Management"
doi: "10.1016/0378-7206(77)90003-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Forecast of the Future of Computation

Carl Hammer

Sperry Univac, Washington DC, USA

Recent hardware advances reduce to one common denominator: The "Miracle" of the Chip. Large-scale integration continues its astounding progress and commercially available densities of only two years ago are already obsolete; the 100 K chip is said to be on several drawing boards. Future system architectures will exhibit increasing parallelism and modularity. An avalanche of new "hard-wired" components will include hierarchical and associative memories, pipeline and array processors; data security will be provided through cryptographic hardware. Finally, computer networks will eclipse the meteoric rise of their time-sharing ancestors as microprocessors take over the burdens of protocols and network operating systems.

Keywords: Architecture, array processors, communications, computer architecture, computer systems, cryptography, data base management, distributed systems, electronic computers, graphics, language translation, memory, monolithic chips, semi-conductors, software, voice recognition.

## 1. Introduction

The pervasive nature of electronic computers must surely be apparent to all. Entire industries are toppling under their impact while new ones are springing up everywhere. Who would have thought ten years ago, that makers of mechanical watches would be in a world-wide crisis-mode? Or that engi-

![](/api/attachments/VA9XEPP2/fulltext/images/1f6461e249a127c74a55f7f5c2c3accf60f1c0fc8ac03155789187987a84d980.jpg)

Born in Chicago, Illinois. Carl Hammer graduated in 1936 from the University of Munich, with a diploma in mathematical statistics and a Ph.D. in 1938 in the same field. Following his return to the United States, Dr. Hammer taught at Columbia University and Hunter College, both in New York City. In 1951, he joined the Computer Department of the Franklin Institute in Philadelphia as a Senior Staff Engineer. In 1955, he

was appointed Director of the Univac European Computer Center, Frankfurt am Main, Germany. Later he worked for the Radio Corporation of America, where he took charge of the initial design of the Minute Man Communications System. In January of 1963, Dr. Hammer rejoined Sperry Univac in Washington DC. Dr. Hammr has served as a Director of the American Federation of Information Processing Societies. Under the aegis of AFIPS, he was named Science and Technology Program Chairman for the first National Computer Conference June 1973. Three years later he assumed total responsibility for the 1976 National Computer Conference as its Conference Chairman.

Dr. Hammer is an Adjunct Professor at the American University and a Visiting Professor at the Industrial College of the Armed Forces, both in Washington. He is a Past Chairman of the Washington Chapter of the Association for Computing Machinery and more recently he was elected to represent its entire Capital Region. Professional organizations, to which he belongs, include the New York Academy of Sciences, the Association for the Advancement of Science, the American Mathematical Society, and the American Statistical Association. He is a Past President of the American Society for Cybernetics, an elected member of the Research Society of America, and a Senior Member of the IEEE. He is an elected Fellow of the American Association for the Advancement of Science, the Association of Computer Programmers and Analysts, and the New York Academy of Sciences. By appointment, he is also a member of the National Defense Executive Reserve. In June of 1973 he was given the Computer Sciences Man-of-the-Year Award by the Data Processing Management Association.

neering students would crave anything but a twenty-inch slide rule? These are but two of the challenges wrought upon us during the senventies. However, that was only the beginning!

Recent hardware advances reduce to one common denominator: The “Miracle” of the Chip. As large-scale integration continues its astounding progress, commercially available densities of only two years ago are already obsolete; the 100 K chip is said to be on several drawing boards. It takes little imagination to predict what will happen as micros become minis and midis turn into maxis — or is that the other way around? Future system architectures will exhibit increasing parallelism and modularity. An avalanche of new “hard-wired” components will include hierarchical and associative memories, as well as array processors, and other devices.

Another hardware feature is just entering the panic stage: Data Security through Cryptographic Methods. We will probably see “chipped” plugs shortly at every systems cabling point with programmable ROMs built into all cabled connectors to effect cryptographic security at each interconnection. Plug-to-plug compatible manufacturers, watch out! Computer networking will soon eclipse the meteoric rise of their time-sharing ancestry as micro-processors take over the burdens of protocols and network operating systems.

The future of the software industry will perhaps make the debacle of mechanical watches look like a Sunday School picnic. A multitude of firmware applications will include not only compilers but also the management of hierarchica' and relational data bases, as well as many common elements of current software, including computer operating systems. As users continue their clamor about the high cost – and unreliability – of software, the trend will be toward more “chipped” software whose logical performance can be certified.

## 2. The miracle of the chip

Computer technology is now thirty years old (or young). Since its beginning, it has been characterized by a fiercely competitive race to develop faster processors, larger memories, and more reliable components. The most spectacular break-throughs in hardware technology have taken place with the introduction of integrated circuitry in the early 1960's. Since then the cost of maximum-complexity chips obtained with medium and large-scale integration has remained essentially constant. However, the number of components on the ICs has increased by several orders of magnitude.

Monolithic chip characteristics are compared in Table 1 for memories and logic arrays. There is no indication that we are approaching their limits to growth; the techniques of electron lithography are well enough understood to permit considerable increases in component densities. Another way of looking at this picture is to measure the width of strata and components currently deposited in terms of atomic diameters. We are still very much in the macroscopic domain with line widths of hundreds of thousands of atoms. Even projections for 1990 would indicate that anticipated gains are well within the scope of macro-technology. Thus it is readily conceivable that in less than twenty years the “true computer on a chip” will have been born.

Table 1. Monolithic chip characteristics.

<table><tr><td rowspan="2">Year</td><td colspan="2">Memories</td><td colspan="2">Logic arrays</td></tr><tr><td>Bits/Chip</td><td>Width-Atoms</td><td>Bits/Chip</td><td>Width-Atoms</td></tr><tr><td>1970</td><td>300</td><td>200 K</td><td>100</td><td>300 K</td></tr><tr><td>1975</td><td>15 K</td><td>20 K</td><td>2 K</td><td>60 K</td></tr><tr><td>1980 *</td><td>500 K</td><td>3 K</td><td>25 K</td><td>20 K</td></tr><tr><td>1985 *</td><td>20 M</td><td>500</td><td>400 K</td><td>4 K</td></tr><tr><td>1990 *</td><td>800 M</td><td>100</td><td>6 M</td><td>1 K</td></tr></table>

\* Projected estimates.

Electronic computer architectures require ever greater volumes of random access and intermediate storage memories. A number of interesting semiconductor and other technologies are being investigated to design larger and faster memories; hopefully they will also have reduced power consumption and greater reliability. Leaving aside pure research with Josephson Junction Diodes and other esoteric techniques, at least four methodologies look very promising:

BEAMOS, for Beam Addressed Metal Oxide Semiconductor, is a new technology for auxiliary memories which employs an electron beam to read and write data on a single unstructured MOS chip. Storage capacity per module runs as high as 32 megabits. Although basically non-volatile, the data have to be re-written after six to then reads, dependent upon beam currents and data recording rates. Access times range from 1 to 30 microseconds depending on such operational characteristics as switching from read to write, and settling time of the deflection amplifier.

Holographic read/write memories with up to a billion bits addressable capacity have access times measured in microseconds. They have not yet emerged as viable systems components because of limitations imposed by currently used recording media. The prospects for read-only memories appear to be much better with multi-microsecond access times and a billion bit capacities available in prototype devices. Unfortunately, the read-only property limits their usefulness to special applications where only archival storage is required.

Magnetic bubble domain memory systems are non-volatile and require minimal operational power in the order of 10 Watts for each ten megabit unit. Current densities available exceed one million bits per square inch with access times below one millisecond. Thus this type of memory fills the gap between the fastest electro-mechanical devices (8 milliseconds on head-per-track disc memories) and core memories (less than one microsecond).

Charge-coupled electric domain devices require significant peripheral and interface circuits in practical applications all of which are currently implemented by N-channel MOS technology. Present designs are limited to registers with shift data speeds below 10 MHz. Of particular concern is the limitation imposed by the power dissipated in the drivers to the CCD registers. The CCD storage element is dynamic and must be periodically refreshed similarly to a dynamic MOS RAM. Access frequencies are now in the MegaHertz range with experimental four-level memory sizes up to 64 million bits available.

In summary, semiconductor technology is being pushed to extend into the auxiliary memory area which is now dominated by magnetic recording on mechanical devices in the form of discs and drums. Shift registers utilizing charge-coupled devices as well as dynamic RAMs with almost equal densities are being pursued for such applications. Magnetic bubbles provide a competing technology. Both have the advantage of being non-mechanical and both provide faster access. Alternative formats of CCD shift registers are being studied and serpentine, serial-parallel-serial, even a line-addressable approach, are under consideration. Clock rates up to 10 MHz and densities of 1 bit per square mill are realistic. Bubble memories have the advantage of smooth substrates for their metallurgy but CCDs have the advantage of higher shift rates by at least one order of magnitude. Again, bubbles have the advantage of nonvolatility while both bubbles and CCDs promise greater reliability than floppy discs.

Parallel developments (very much in the R&D stage) now are likely to come to fruition just as we run out of macro-technological steam. It has not gone unobserved that chip technology is coupled to electron microscopy, gradually approaching its own capability limits. But current research in the field of structured molecules is quite promising and should come into its own by the end of this century. Our scientists have already “engineered” DNA molecules and even changes of genetic codes; undoubtedly they will eventually reach also their most ambitious goal: Crystal Lattice Computers. For a starter, molecular rectifiers have already been built from molecules whose respective ends have different binding energies, thus acting as anode and cathode. Achievement of the precise spacing in such crystal structures seems still to be a problem, but scientists at New York University and other research laboratories are confident of ultimate success.

## 3. Computer system architecture

We should perhaps introduce first the notion of real and virtual architectures. Throughout the 1960s no differentiation was made between the machine architecture as seen by the software programmer and the hardware design engineer. Systems programming, in particular, is still much concerned with the real hardware while applications programming has found some relief in efficient high-level language compilers and the virtual systems concept.

During the 1970s, systems architectural research centered on hierarchical memories, virtual machines, and other conventional concepts, showing little imagination. For the time being, we may safely assume that the indicated trends will continue, but radically new architectures will not emerge. Therefore, we have to live for at least a decade with the conventional architectures shown in Table 2. Fundamentally, all architectures known to date can be characterized by their (i) physical organization, (ii) control and flow of data, and (iii) data representation and transformation.

It appears worthwhile to indicate briefly some raison d'être for each architectural class. The first, and perhaps most obvious, is the scientific number cruncher (modular unit processor). Its current capability of ten million operations per second is expected to grow to 300 billion operations by 1990 as demands of the scientific community for raw computing power will remain strong. Where data and instruction streams of large scientific problems become more manageable, the pipeline processor will remain about an order of magnitude faster than the fastest modular unit processors. It is perhaps worth noting that the projected processing speed for pipeline machines in 1990 (3 trillion operations per second) is still nowhere near the limits imposed by component spacing on chips with densities indicated in Table 2. While there have been some studies on "natural limits" achievable, it is felt that they did not take into account the degree to which very large-scale integration will allow real parallelism while giving the illusion of virtual pipelines.

Table 2. Computer architectures characteristics.

<table><tr><td>Processor description</td><td>1975 MIPS</td><td>1980 BIPS</td><td>1985 BIPS</td><td>1990 TIPS</td></tr><tr><td>Functionally parallel units</td><td>10</td><td>0.3</td><td>10</td><td>0.3</td></tr><tr><td>Pipeline organization</td><td>100</td><td>3</td><td>100</td><td>3</td></tr><tr><td>Parallel array</td><td>100</td><td>3</td><td>100</td><td>3</td></tr><tr><td>Associative array</td><td>50</td><td>1.5</td><td>50</td><td>1.5</td></tr></table>

Notes: MIPS = Million (10 $^{6}$ ) instructions per second, BIPS = Billion (10 $^{9}$ ) instructions per second, TIPS = Trillion (10 $^{12}$ ) instructions per second.

Of greater interest to the commercial world of data processing should be current trends with minis, micros, and their parallel computer cousins. Most applications today are done serially while the problem structure is parallel. Payroll, inventory control, personnel records management, to mention only a few, are typical examples. Fortran DO loops and Cobol PERFORMs are representative of problems structured in parallel but processed serially. Thus the significant trend of multiminis, now often in networks, will definitely lead us into truly parallel processing where the number of submachines operating in parallel will rise meteorically in the not too distant future.

The last entry in Table 2 is reserved for a "sleeper": Associative or content-addressable processors. Few such devices are now in existence but they are very likely to emerge with great vigor once current hardware problems are overcome. They will contribute significantly to new forms of data base management systems which are flexible and truly relational in nature, rather than hierarchically and rigidly structured.

## 4. Distributed systems

The symbiosis of computers and communications has been in the making for at least twenty years. It began with remote job entry, time sharing, and real-time applications, attaining considerable maturity by the middle 1970s. While the cost of computing declined steadily the same could not be said for the cost of communicating. Thus the recent emphasis is on better utilization of our limited communications bandwidth through packet switching and the wholesale creation of national and international value-added carriers and networks. Problems to be solved include standard interfaces and protocols, and only time will tell whether the user community will be dictated to by the powerful interests of common carriers and large computer manufacturers. However, the services offered now certainly cover a wide spectrum of applications with new ones being added almost weekly.

Recent legislation by governments concerned with the privacy issue and the integrity protection of personal data can be expected to extend also to the private sector. In addition to increasing the physical security to protect computer and terminal installations, the topic of data security is receiving growing attention. Most recently, proposals have been made to incorporate cryptographic transformations, perhaps through hardware, into all data streams which travel between devices and systems. The pertinent solicitation of the U.S. National Bureau of Standards produced a veritable avalanche of studies in the public domain – and probably even more which are proprietary in nature. Needless to say that with the advent of ROMs and PROMs and further successes in microminiaturization the time is not too distant where single chips can be (and probably will be) imbedded in cable shoes and plugs that connect devices and systems to one another, whether it is within the computer center or to remote stations. On the surface, this appears only as an innocuous, minor change to the interfaces of existing machine architectures. However, such an event could have far-reaching implications on the plug-to-plug compatible industry, on portability of programs and data, and on future data transmission standards.

## 5. Software

Software engineering has emerged in response to criticisms that programming has been, at best, an art or a craft - but not a science. Software engineers suggest the need for project management with all its forcing functions to increase both the productivity of programmers and the quality of their product. Modular and structured design techniques are being advocated; the design team concept stresses the need for egoless performance of individuals and its apostles would like to put the software primadonnas of the past out to pasture. Software system architects have learned the hard way – and at great cost to the user community – that only firm initial specifications can lead to reliability and efficiency. Unresolved questions in the later stages of the design impose severe penalties of complexity and running time on the software. Moreover, retrofitting more often than not proves impossible with the consequences of permanently flawed systems or the need to “go back to the drawing board”.

We see hardware technology advancing so fast that current concerns such as hardware costs and CPU efficiency will soon become meaningless. But we see no comparable reduction in the cost of software. Very High Level Languages will undoubtedly emerge to take the place of today's procedure oriented languages. In the VHLL a single word will perhaps suggest a whole set of high-level statements. The language will be used to provide a quasi-formal description of the programming problem itself. Consequently, even the software systems for future generations of machines will perhaps be written in the form of VHLL statements and the virtual machine architecture will be made to anticipate multi-functional inputs. They could be performed in a parallel, look-ahead fashion by generation of an expanded set of instructions which the real architecture then executes.

For example, the specification type statement "Membership A, T, D" might be used to generate a full-blown system to store and retrieve people's Addresses, Telephone numbers, and Dues' Terms. The implication of such a development is that functions currently performed at the software level could be built into intelligent hardware/software input devices. Thus a single keyword on input could cause a branch to hardware stored routines which would emit or interpret the necessary set of machine instructions, representing an expanded version of the keyword suitable for CPU processing. At this point the user will no longer care where the VHLL is transmuted into a form that the real hardware recognizes internally.

A temporary solution to existing software problems will undoubtedly come from interactive computer graphics which is expected to reach some degree of maturity during this decade. Current applications of computer graphics range from basics requiring hundreds of vectors and characters, to enhanced applications of greater scope requiring color and movement, to complex applications with thousands of details and extensive support in terms of hardware and software, with working sets running into millions of characters! However, the major limitation today is that intelligent graphics terminals are simply not portable.

Much like the breakthrough in pocket calculators we can expect intelligent graphics (and other) terminals to attain the status of the telephone (with circa 140 million receivers installed in the US) as soon as the CTR technology is replaced by digital (flat) screens with high resolution – and low cost. Flat screen technology is currently in the laboratory stage; it is expected to mature concurrently with the conversion of the telephone into a purely digital network. The impact of such a development which is cautiously predicted for the middle 1980s will certainly contribute to a proliferation of these devices with consequences which we can only dimly assess. Not only will the software industry be called upon to deliver ever more in services, rather than packages, but whole sectors of education, health services, law enforcement, banking, general office work, even entertainment and retail merchandising, will be totally transformed from established norms. It has been speculated that this chain of events may be speeded up by the current energy crisis, as nearly hundred million Americans travel daily by car to and from work or shopping. “Communicate – don’t commute” will perhaps become a reality toward the end of this century much to the relief of those concerned with air pollution and traffic congestion.

## 6. Conclusion

What about the long range for computing and contributions by the information processing industry? My shopping bag floweth over!

With the advent of the superchip we will surely be able to tackle the last frontier in man-machine communications. Of the three channels available to man - tactile, audio, video -- we are using only two which happen to come at the extreme ends of the communications spectrum. The lowest available speed, ranging from an average of six bauds to bursts of less than one hundred bauds, is used by us to communicate with the machine through a tactile keyboard. On the other extreme we can perceive data and information through the video channel at rates approximating 4 KB and higher for occasional bursts. Yet little has been accomplished to round out our ability and to communicate through the audio channel.

The information processing industry has often taken the lead in developing new systems and concepts, as with interactive graphics, for example. Here are then our challenges for the next several decades.

Selective speech recognition is already being accomplished by specialized systems. It operates on small vocabularies and requires great care in the voice calibration process. But linguistic complexities of syntax, grammar, parsing, content analysis, and associative relevance are still far beyond the capabilities of even our largest machines. Yet with the projected increases in chip densities and interna machine parallelism, selective speech systems for recognition and response will perhaps be the first to appear on the technological scene. With their help interactive systems will certainly receive a great boost and become much more powerful. They could also greatly improve the "image" of computers, removing the well-known syndrome of today, which proclaims at the slightest provocation that "you can't talk back to a computer". By 1985 we will very likely be able to do just that!

General voice recognition is at least one order of magnitude more difficult and is unlikely to occur before 1995. It is perhaps desirable to define it in alternate terms by referring to it as Voice-to-Print transformations. Its perfection will also cause some major upheavals in general office work, beginning with the need to retrain a million typists and clerks for more meaningful activities, and ending with the decentralization and dispersal of office functions as we know them today. A good deal of the work we now do gregariously at our working locations can be transferred to our homes or to specially equipped community offices. With that event, commuting could be reduced to less than one per cent of its current level and travel may again become a pleasure rather than a dangerous chore.

Language translation or print-to-print transformations are probably of the same complexity as general voice recognition. Linguists and the computer sciences have wrestled with this problem for almost thirty years and successes have been generally limited to small vocabularies and the technical literature. However, with the immense storage capacities of future machines and their incredible internal speeds, we should achieve print-to-print capability also during the middle 1990s. From an aesthetic viewpoint, there seems to be absolutely no need to be concerned with literature, poetry, and drama; their beauty will almost always be constrained to the authors' source languages. However, the commercial community will greatly benefit from this print-to-print capability as it could greatly ease international tensions through improved communications.

Coupling the two above capabilities with the generation of digitized voice -- already in existence -- will get us to the implementation of real-time systems for voice translation. Again, we would be less concerned with rendering Sir Laurence Olivier in Russian, than with the world of commerce, law, and politics. Anyone who has ever observed the strain on human interpreters can appreciate the impact which such systems applied universally will have upon the international mass media, news services, and humanity itself. Where will it all lead to? In a nutshell, the answer is that we are approaching the "final" transition to the realtime world of an international information society. It forebodes a way to make better decisions by individuals and societal units. It will give mankind a chance to better manage its limited resources. "Computer Power to the People" is not entirely an idle slogan: it could well symbolize a major structural change in an adolescent global society. Or, as Norbert Wiener put it so forcefully, it may signal an era where we will begin to make human use of human beings.

## References

[1] Clark Adams, Over the Horizon, Computer, February 1976, pp. 8–11.

[2] Roger Allan, Semiconductor Memories, Spectrum, August 1975, pp. 40--45.

[3] Gilver F. Amelio, Charge-coupled Devices for Memory Applications, Proceedings, National Computer Conference, 1975, Anaheim, California, pp. 515–522.

[4] W. Anacker, Superconducting Memories Employing Josephson Devices, Proceedings, National Computer Conference, 1975, Anaheim, California, pp. 529–534.

[5] Auerbach Editorial Staff, What is Network Architecture?, Computer Decisions, June 1976, pp. 24–26, 33.

[6] Aviation Week and Space Technology, Computer Proves Architecture Concept (PEPE), 11 October 1976, pp. 35–36.

[7] Dan M. Bowers, Systems-on-a-Chip, Mini-Micro Systems, July 1976, pp. 42–48.

[8] Margaret K. Butler, Prospective Capabilities in Hardware, Proceedings, National Computer Conference, 1976, New York, New York, pp. 323–336.

[9] Eric D. Carlson, Graphics Terminal Requirements for the 1970's, Computer, August 1976, pp. 37–45.

[10] Yaohan Chu, Evolution of Computer Memory Structure. Proceedings, National Computer Conference, 1976, New York, New York, pp. 733–748.

[11] D.L. Critchlow, High Speed MOSFET Circuits Using Advanced Lithography, Computer, February 1976, pp. 31–37.

[12] Samuel Derman, Progress in Gigabit Logic Reported for Superfast Switching Uses, Electronic Design, July 19, 1976, pp. 34–38.

[13] Howard Falk, Computers: Poised for Progress, Spectrum, January 1976, pp. 44–49.

[14] George C. Feth, Workshop Report: Impact of Emerging Technology, Computer, January 1975, pp. 51–54.

[15] George C. Feth, Memories: Smaller, Faster, and Cheaper, Spectrum, June 1976, pp. 37–43.

[16] A.K. Gillis, G.F., Hoffman and R.H. Nelson, Holographic Memories – Fantasy or Reality? Proceedings, National Computer Conference, 1975, Anaheim, California, pp. 535–539.

[17] Eugene Hnatek, Chipping Away at Core. Digital Design, July 1976, pp. 31–42.

[18] W.C. Hughes, C.Q. Lemmond, H.G. Parks, G.W. Ellis, G.E. Fossin, and R.H. Wilson, BEAMOS - A New Electronic Digital Memory, Proceedings, National Computer Conference, 1975, Anaheim, California, pp. 541-548.

[19] John Kelly, The Development of an Experimental Electron-Beam-Addressed Memory Module, Computer, February 1975, pp. 32–42.

[20] R.M. Lea, Information Processing with an Associative Parallel Processor, Computer, November 1975, pp. 25–32.

[21] Jim McDermott, Semiconductor Memories, Electronic Design, June 7, 1976, pp. 78–82.

[22] Ware Myers, Key Developments in Computer Technology: A Survey, Computer, November 1976, pp. 48–75.

[23] G. Panigrahi, Charge-Coupled Memories For Computer Systems, Computer, April 1976, pp. 33–41.

[24] R.A. Pedersen, Integrated Injection Logic: A Bipolar LSI Technique, Computer, February 1976, pp. 24–29.

[25] S.L. Rege, Cost Performance, and Size Tradeoffs For Different Levels in a Memory Hierarchy, Computer, April 1976, pp. 43–50.

[26] S.S. Reddi and E.A. Feustel, A Conceptual Framework for Computer Architecture, ACM Computing Surveys, June 1976, pp. 277–299.

[27] John M. Salzer, Bubble Memories - Where Do We Stand?, Computer, March 1976, pp. 36-41.

[28] David J. Sykes, Protecting Data by Encryption, Datamation, August 1976, pp. 81, 84–85.

[29] Time, Mini-Mini Components, 6 May 1974, p. 97.

[30] Edward A. Tornero, At the International Solid State Circuits Conference, Electronic Design, March 29, 1976, pp. 26–30.

[31] Edward A. Torrero, Bubbles Rise from the Lab, Spectrum, September 1976, pp. 29–31.

[32] Edward A. Torrero, High-frequency Components Play Catch-Up, Spectrum, November 1976, pp. 31–35.

[33] Richard L. Turmail, EIA Crystal Ball shows Trends in

Electronics to the Year 201.2, Electronic Design, 22 June 1972, pp. 34–36.

[34] Rein Turn, Computers in the 1980's, Columbia University Press, 1974.

[35] R. Turn and A.E. Nimitz, Computers and Strategic Advantage: 1. Computer Technology in the United States and the Soviet Union, Rand Corporation Report R-1642-PR, Santa Monica, California, May 1975.

[36] Frederick G. Withington, Beyond 1984: A Technology Forecast, Datamation, January 1975, pp. 54–73.

[37] John E. Ypma, Bubble Domain Memory Systems, Proceedings, National Computer Conference, 1975, Anaheim, California, pp. 523–528.
