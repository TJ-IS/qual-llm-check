# 肖帅勇两篇 ISR 源行—语法句—逻辑段主键 Manifest

## 1. 用途、源文与稳定口径

本文件是 `00J`、`00K`、`00M` 和 `00F` 共同使用的主键层。它不再解释论文内容，而是为每个逻辑段冻结源行集合、语法句 ID、公式或浮动对象插断、尾注接口和图像可视状态。后续的正文逐段 ISR 对照不得只写“参照肖老师某节”，必须引用本文件中的段落主键和语法句 ID。

| 论文代码 | 源文件 | 行数 | SHA-256 |
|---|---|---:|---|
| ACAA | `database_fulltext_all/28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md` | 548 | `22874E02E5DE71421110476BFC4B8E15FC80F86A1175D81A4FA3FCE7DF746239` |
| DSDL | `database_fulltext_all/16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md` | 525 | `1954CA69FF5750C7C8A0CD594C7772FABE9B9F69F84F253120D39DFC85259A2B` |

计数和 ID 规则如下。

1. `Lx` 是上表对应 Markdown 的 1-based 物理行号。连续行用 `Lx–Ly`，被公式或浮动表切断的集合用逗号分开。
2. 语法句 ID 由“论文—段落主键—句序”组成，例如 `ACAA-I1-S01`。`S01–S05` 包含端点。一个原文语法句中有两个证据或功能分句时，在 `00J/00K/00M` 中使用 `S03a/S03b`，但 manifest 只计一个 `S03`。
3. 显示公式本身不另算英文语法句。公式前导语、公式和 `where` 续句共同完成一句时，按一句计。表题、图题、表注、附件路径和子图字母不计入语法句。
4. ACAA 主文计数范围为 L29–L348，共 80 个逻辑段、397 个语法句。尾注 L352–L374 另有 12 个编号、17 个语法句。
5. DSDL 主文计数范围为 L27–L343，共 76 个逻辑段、396 个语法句。在该范围按 Markdown 空行切分，排除 History/Funding/Supplemental Material、Keywords、章节标题、显示公式、表题/表注/表格 HTML、图题/附件/子图字母后是 87 个 prose blocks。合并 `L77+L79`、`L132+L142`、`L160+L170+L179+L185`、`L189+L195`、`L199+L205+L211`、`L213+L219`、`L221+L227` 和 `L251+L265`，共减少 11 个断裂块，得 76 个逻辑段。L109 的 `Figure 1 outlines…` 和 L269 的 `Table 6 shows…` 是正文段，不是图表题。
6. “图像可视”一列的“否”是物理边界：两份源文头都写明 `images_downloaded: false`，图形仅留 `/api/attachments/...` 占位。因此可以索引正文赋予图的功能，不能声称检查了图中的节点、箭头、曲线、坐标或数值。
7. “对应索引单元”通常写目标文件中的现有单元 ID。一个 manifest 段跨越两个索引标题，或两个 manifest 段共用一个索引标题时，使用 `文件#锚点`；该锚点在 `00J/00K` 中以同名 HTML `id` 显式存在，机器检查不得再把“前半”“后半”一类解释性文字当成索引 ID。

## 2. ACAA 主文逻辑段 manifest（80 段，397 句）

| 段落主键 | 对应索引单元 | 源行集合 | 语法句 ID | 公式/浮动接口 | 尾注 | 图像可视 |
|---|---|---|---|---|---|---|
| ACAA-A0 | 00J ACAA-A0 | L29 | ACAA-A0-S01–S06 | 无 | 无 | 不适用 |
| ACAA-I1 | 00J ACAA-I1 | L39 | ACAA-I1-S01–S05 | 无 | 无 | 不适用 |
| ACAA-I2 | 00J ACAA-I2 | L41 | ACAA-I2-S01–S06 | 无 | 无 | 不适用 |
| ACAA-I3 | 00J ACAA-I3 | L43 | ACAA-I3-S01–S04 | 无 | N1 | 不适用 |
| ACAA-I4 | 00J ACAA-I4 | L45 | ACAA-I4-S01–S06 | 无 | 无 | 不适用 |
| ACAA-I5 | 00J ACAA-I5 | L47 | ACAA-I5-S01–S09 | 无 | 无 | 不适用 |
| ACAA-I6 | 00J ACAA-I6 | L49 | ACAA-I6-S01–S04 | 无 | 无 | 不适用 |
| ACAA-I7 | 00J ACAA-I7 | L51 | ACAA-I7-S01–S06 | 无 | 无 | 不适用 |
| ACAA-I8 | 00J ACAA-I8 | L53 | ACAA-I8-S01–S04 | 无 | N2、N3 | 不适用 |
| ACAA-I9 | 00J ACAA-I9 | L55 | ACAA-I9-S01–S06 | 无 | N4 | 不适用 |
| ACAA-L1 | 00J ACAA-L1 | L61 | ACAA-L1-S01–S05 | 无 | 无 | 不适用 |
| ACAA-L2 | 00J ACAA-L2 | L63 | ACAA-L2-S01–S04 | 无 | 无 | 不适用 |
| ACAA-L3 | 00J ACAA-L3 | L65 | ACAA-L3-S01–S05 | 无 | 无 | 不适用 |
| ACAA-L4 | 00J ACAA-L4 | L67 | ACAA-L4-S01–S06 | 无 | 无 | 不适用 |
| ACAA-L5 | 00J ACAA-L5 | L71 | ACAA-L5-S01–S06 | 无 | 无 | 不适用 |
| ACAA-L6 | 00J ACAA-L6 | L73 | ACAA-L6-S01–S05 | 无 | 无 | 不适用 |
| ACAA-L7 | 00J ACAA-L7 | L75 | ACAA-L7-S01–S04 | 无 | 无 | 不适用 |
| ACAA-L8 | 00J ACAA-L8 | L79 | ACAA-L8-S01–S09 | 无 | 无 | 不适用 |
| ACAA-L9 | 00J ACAA-L9 | L81 | ACAA-L9-S01–S04 | 无 | 无 | 不适用 |
| ACAA-L10 | 00J ACAA-L10 | L85 | ACAA-L10-S01–S05 | 无 | 无 | 不适用 |
| ACAA-L11 | 00J ACAA-L11 | L87 | ACAA-L11-S01–S08 | 附录 A/Table A2 出口 | N5 | 不适用 |
| ACAA-T1 | 00J ACAA-T1 | L91 | ACAA-T1-S01–S04 | 无 | 无 | 不适用 |
| ACAA-T2 | 00J ACAA-T2 | L93 | ACAA-T2-S01–S03 | 关联 F1 | 无 | 否（F1） |
| ACAA-T3 | 00J ACAA-T3 | L95 | ACAA-T3-S01–S07 | 关联 F1 | 无 | 否（F1） |
| ACAA-T4 | 00J ACAA-T4 | L100 | ACAA-T4-S01–S06 | 无 | 无 | 不适用 |
| ACAA-T5a | `00J#acaa-t5ab` | L102 | ACAA-T5a-S01–S04 | 无 | 无 | 不适用 |
| ACAA-T5b | `00J#acaa-t5ab` | L104 | ACAA-T5b-S01–S06 | 无 | 无 | 不适用 |
| ACAA-T6a | `00J#acaa-t6ab` | L106 | ACAA-T6a-S01–S05 | 无 | 无 | 不适用 |
| ACAA-T6b | `00J#acaa-t6ab` | L108 | ACAA-T6b-S01–S04 | 附录 A/Table A2 出口 | N6 | 不适用 |
| ACAA-T7a | `00J#acaa-t7ab` | L110 | ACAA-T7a-S01–S03 | 无 | 无 | 不适用 |
| ACAA-T7b | `00J#acaa-t7ab` | L112 | ACAA-T7b-S01–S03 | 无 | 无 | 不适用 |
| ACAA-T8a | `00J#acaa-t8ab` | L114 | ACAA-T8a-S01–S07 | 无 | 无 | 不适用 |
| ACAA-T8b | `00J#acaa-t8ab` | L116 | ACAA-T8b-S01–S04 | 无 | 无 | 不适用 |
| ACAA-T9 | 00J ACAA-T9 | L118 | ACAA-T9-S01–S03 | Table 1（L120–L122） | 无 | 不适用 |
| ACAA-M0 | 00J ACAA-M0 | L126 | ACAA-M0-S01–S02 | Table 1 回指 | 无 | 不适用 |
| ACAA-M1 | 00J ACAA-M1 | L130 | ACAA-M1-S01–S05 | F2（L136–L137） | N7 | 否（F2） |
| ACAA-M2 | 00J ACAA-M2 | L134 | ACAA-M2-S01–S08 | 无 | N8（源标记损坏） | 不适用 |
| ACAA-M3 | 00J ACAA-M3 | L139 | ACAA-M3-S01–S04 | 附录 B 例图出口 | 无 | 不适用 |
| ACAA-M4 | 00J ACAA-M4 | L141 | ACAA-M4-S01–S04 | 无 | 无 | 不适用 |
| ACAA-M5 | 00J ACAA-M5 | L143、L145–L159 | ACAA-M5-S01–S08 | 公式 1–3 | N9（抽取为上标） | 不适用 |
| ACAA-M6 | 00J ACAA-M6 | L161 | ACAA-M6-S01–S04 | 无 | N10 | 不适用 |
| ACAA-M7a | `00J#acaa-m7` | L163、L165 | ACAA-M7a-S01–S04 | 跨排版断行 | N11（源标为 1，语义对应 11，待 PDF） | 不适用 |
| ACAA-M7b | `00J#acaa-m7` | L167 | ACAA-M7b-S01–S02 | 无 | 无 | 不适用 |
| ACAA-M8 | 00J ACAA-M8 | L171 | ACAA-M8-S01–S06 | 无 | 无 | 不适用 |
| ACAA-M9 | 00J ACAA-M9 | L173 | ACAA-M9-S01–S04 | 关联 F3 | 无 | 否（F3） |
| ACAA-M10a | 00J ACAA-M10a | L175 | ACAA-M10a-S01–S03 | 无 | 无 | 不适用 |
| ACAA-M10b | 00J ACAA-M10b | L177–L187 | ACAA-M10b-S01–S07 | 公式 4–5；L184 分母异常 | 无 | 不适用 |
| ACAA-M11 | 00J ACAA-M11 | L189、L194–L198 | ACAA-M11-S01–S07 | 公式 6；被 F3 L191–L192 插断 | 无 | 否（F3） |
| ACAA-M12 | 00J ACAA-M12 | L200–L208 | ACAA-M12-S01–S08 | 公式 7 | N2 机制边界 | 不适用 |
| ACAA-M13 | 00J ACAA-M13 | L210 | ACAA-M13-S01–S02 | `hat/tilde alpha` 异常 | 无 | 不适用 |
| ACAA-M14 | 00J ACAA-M14 | L212–L218 | ACAA-M14-S01–S05 | 公式 8 | 无 | 不适用 |
| ACAA-M15 | 00J ACAA-M15 | L220 | ACAA-M15-S01–S03 | 无 | N6 情境回指 | 不适用 |
| ACAA-M16 | 00J ACAA-M16 | L224 | ACAA-M16-S01–S07 | 附录 C/Figure C1 出口 | 无 | 否（附录图缺失） |
| ACAA-P5.1-1 | 00M P5.1-1 | L228 | ACAA-P5.1-1-S01–S05 | 附录 D 出口 | 无 | 不适用 |
| ACAA-P5.2-1 | 00M P5.2-1 | L232 | ACAA-P5.2-1-S01–S06 | 无 | 无 | 不适用 |
| ACAA-P5.2-2 | 00M P5.2-2 | L234 | ACAA-P5.2-2-S01–S07 | 无 | 无 | 不适用 |
| ACAA-P5.2-3 | 00M P5.2-3 | L236 | ACAA-P5.2-3-S01–S03 | 无 | 无 | 不适用 |
| ACAA-P5.2-4 | 00M P5.2-4 | L238 | ACAA-P5.2-4-S01–S05 | 无 | N12 | 不适用 |
| ACAA-P5.2-5 | 00M P5.2-5 | L240 | ACAA-P5.2-5-S01–S04 | 无 | 无 | 不适用 |
| ACAA-P5.2-6 | 00M P5.2-6 | L242 | ACAA-P5.2-6-S01 | 无 | 无 | 不适用 |
| ACAA-P5.2-7 | 00M P5.2-7 | L244 | ACAA-P5.2-7-S01–S04 | 附录 E–F 出口 | 无 | 不适用 |
| ACAA-P5.3.1-1 | 00M P5.3.1-1 | L248 | ACAA-P5.3.1-1-S01–S03 | Table 2（L250–L254）；附录 G | 无 | 不适用 |
| ACAA-P5.3.1-2 | 00M P5.3.1-2 | L256 | ACAA-P5.3.1-2-S01–S02 | Table 2 解释 | 无 | 不适用 |
| ACAA-P5.3.1-3 | 00M P5.3.1-3 | L258 | ACAA-P5.3.1-3-S01–S07 | Table 2 机制解释 | 无 | 不适用 |
| ACAA-P5.3.2-1 | 00M P5.3.2-1 | L260 | ACAA-P5.3.2-1-S01–S02 | Table 3（L264–L268） | 无 | 不适用 |
| ACAA-P5.3.2-2 | 00M P5.3.2-2 | L262 | ACAA-P5.3.2-2-S01–S06 | Table 3；附录 G | 无 | 不适用 |
| ACAA-P5.3.2-3 | 00M P5.3.2-3 | L270 | ACAA-P5.3.2-3-S01–S03 | Table 3 解释 | 无 | 不适用 |
| ACAA-P5.3.3-1 | 00M P5.3.3-1 | L272 | ACAA-P5.3.3-1-S01–S06 | Table 4（L276–L280） | 无 | 不适用 |
| ACAA-P5.3.4-1 | 00M P5.3.4-1 | L274 | ACAA-P5.3.4-1-S01–S04 | Table 5（L282–L286） | 无 | 不适用 |
| ACAA-P5.4-1 | 00M P5.4-1 | L290 | ACAA-P5.4-1-S01–S03 | Figures 4–7 总路由 | 无 | 否（F4–F7） |
| ACAA-P5.4-2 | 00M P5.4-2 | L292 | ACAA-P5.4-2-S01–S04 | Figures 4–7 权重提取方法 | 无 | 否（F4–F7） |
| ACAA-P5.4.1 | 00M P5.4.1-1 | L294 | ACAA-P5.4.1-S01–S05 | F4（L298–L306） | 无 | 否（F4） |
| ACAA-P5.4.2 | 00M P5.4.2-1 | L296 | ACAA-P5.4.2-S01–S07 | F5（L320–L326，浮动到后文） | 无 | 否（F5） |
| ACAA-P5.4.3 | 00M P5.4.3-1 | L308 | ACAA-P5.4.3-S01–S03 | F6（L328–L333，浮动到后文） | 无 | 否（F6） |
| ACAA-P5.4.4 | 00M P5.4.4-1 | L310 | ACAA-P5.4.4-S01–S06 | F7（L337–L342，浮动到后文） | 无 | 否（F7） |
| ACAA-P5.5 | 00M P5.5-1 | L314 | ACAA-P5.5-S01–S04 | 附录 I 消融出口 | 无 | 不适用 |
| ACAA-P6-1 | 00M P6-1 | L318 | ACAA-P6-1-S01–S09 | 被 F5/F6 L320–L333 浮动插断 | 无 | 否（F5–F6） |
| ACAA-P6-2 | 00M P6-2 | L335 | ACAA-P6-2-S01–S07 | 被 F7 L337–L342 浮动插断 | 无 | 否（F7） |
| ACAA-P7-1 | 00M P7-1 | L346 | ACAA-P7-1-S01–S04 | 无 | 无 | 不适用 |
| ACAA-P7-2 | 00M P7-2 | L348 | ACAA-P7-2-S01–S08 | 无 | 无 | 不适用 |

ACAA 分节句数复算：摘要 6，引言 50，文献综述 61，理论/设计理由 59，方法 93，经验评价至结论 128，合计 `6+50+61+59+93+128=397`。

## 3. DSDL 主文逻辑段 manifest（76 段，396 句）

| 段落主键 | 对应索引单元 | 源行集合 | 语法句 ID | 公式/浮动接口 | 尾注 | 图像可视 |
|---|---|---|---|---|---|---|
| DSDL-A0 | 00K A0 | L27 | DSDL-A0-S01–S07 | 无 | 无 | 不适用 |
| DSDL-I1 | 00K I1 | L35 | DSDL-I1-S01–S05 | 无 | 无 | 不适用 |
| DSDL-I2 | 00K I2 | L37 | DSDL-I2-S01–S07 | 无 | 无 | 不适用 |
| DSDL-I3 | 00K I3 | L39 | DSDL-I3-S01–S05 | 无 | 无 | 不适用 |
| DSDL-I4 | 00K I4 | L41 | DSDL-I4-S01–S08 | 无 | 无 | 不适用 |
| DSDL-I5 | 00K I5 | L43 | DSDL-I5-S01–S04 | 无 | 无 | 不适用 |
| DSDL-I6 | 00K I6 | L45 | DSDL-I6-S01–S05 | 无 | 无 | 不适用 |
| DSDL-I7 | 00K I7 | L47 | DSDL-I7-S01–S08 | 无 | 无 | 不适用 |
| DSDL-I8 | 00K I8 | L49 | DSDL-I8-S01–S11 | 无 | N1 | 不适用 |
| DSDL-I9 | 00K I9 | L51 | DSDL-I9-S01–S07 | 无 | 无 | 不适用 |
| DSDL-I10 | 00K I10 | L53 | DSDL-I10-S01–S04 | 无 | 无 | 不适用 |
| DSDL-L1 | 00K L1 | L57 | DSDL-L1-S01–S08 | 无 | 无 | 不适用 |
| DSDL-L2 | 00K L2 | L59 | DSDL-L2-S01–S08 | 无 | 无 | 不适用 |
| DSDL-L3 | 00K L3 | L63 | DSDL-L3-S01–S07 | 无 | 无 | 不适用 |
| DSDL-L4 | 00K L4 | L67 | DSDL-L4-S01–S04 | 无 | 无 | 不适用 |
| DSDL-L5 | 00K L5 | L69 | DSDL-L5-S01–S07 | 无 | 无 | 不适用 |
| DSDL-L6 | 00K L6 | L71 | DSDL-L6-S01–S03 | 无 | 无 | 不适用 |
| DSDL-L7 | 00K L7 | L75 | DSDL-L7-S01–S03 | 无 | 无 | 不适用 |
| DSDL-L8 | 00K L8 | L77、L79 | DSDL-L8-S01–S05 | 分页断句，两行合一段 | 无 | 不适用 |
| DSDL-T1 | 00K T1 | L83 | DSDL-T1-S01–S08 | 无 | 无 | 不适用 |
| DSDL-T2 | 00K T2 | L85 | DSDL-T2-S01–S07 | 无 | 无 | 不适用 |
| DSDL-T3 | 00K T3 | L87 | DSDL-T3-S01–S05 | 无 | 无 | 不适用 |
| DSDL-T4 | 00K T4 | L89 | DSDL-T4-S01–S04 | 无 | 无 | 不适用 |
| DSDL-T5 | 00K T5 | L91 | DSDL-T5-S01–S06 | 无 | 无 | 不适用 |
| DSDL-T6 | 00K T6 | L93 | DSDL-T6-S01–S07 | 无 | 无 | 不适用 |
| DSDL-T7 | 00K T7 | L95 | DSDL-T7-S01–S05 | Table 1 导入 | 无 | 不适用 |
| DSDL-M0 | 00K M0 | L99 | DSDL-M0-S01–S03 | Table 1（L101–L103） | 无 | 不适用 |
| DSDL-M1 | 00K M1 | L105 | DSDL-M1-S01–S03 | 无 | 无 | 不适用 |
| DSDL-M2 | 00K M2 | L109 | DSDL-M2-S01–S08 | F1（L115–L116） | 无 | 否（F1） |
| DSDL-M4 | 00K M4 | L113 | DSDL-M4-S01–S06 | 无 | N2 | 不适用 |
| DSDL-M5 | 00K M5 | L118 | DSDL-M5-S01–S07 | 无 | N3 | 不适用 |
| DSDL-M6 | 00K M6 | L120 | DSDL-M6-S01–S03 | 无 | 无 | 不适用 |
| DSDL-M7 | 00K M7 | L124 | DSDL-M7-S01–S05 | L124 实例集符号异常 | N4、N5 | 不适用 |
| DSDL-M8 | 00K M8 | L126 | DSDL-M8-S01–S04 | 无 | N6 | 不适用 |
| DSDL-M9 | 00K M9 | L130 | DSDL-M9-S01–S07 | 无 | 无 | 不适用 |
| DSDL-M10 | 00K M10 | L132、L142 | DSDL-M10-S01–S12 | 公式 1–2；L132 集合关系异常 | 无 | 不适用 |
| DSDL-M11 | 00K M11 | L144 | DSDL-M11-S01–S03 | 无 | 无 | 不适用 |
| DSDL-M12 | 00K M12 | L148 | DSDL-M12-S01–S06 | “最后单元/全序列”异常 | 无 | 不适用 |
| DSDL-M13 | 00K M13 | L150 | DSDL-M13-S01–S06 | S03a/S03b 是同一 `whereas` 语法句 | 无 | 不适用 |
| DSDL-M14 | 00K M14 | L152 | DSDL-M14-S01–S08 | 无 | 无 | 不适用 |
| DSDL-M15 | 00K M15 | L156 | DSDL-M15-S01–S06 | F2 回指；`a×i/a×L` 异常 | 无 | 否（F2） |
| DSDL-M16 | 00K M16 | L158 | DSDL-M16-S01–S03 | 无 | 无 | 不适用 |
| DSDL-M17_18 | `00K#dsdl-m17-18` | L160、L170、L179、L185 | DSDL-M17_18-S01–S04 | 公式 3–6；被 F2 L172–L173 插断 | 无 | 否（F2） |
| DSDL-M19 | 00K M19 | L187 | DSDL-M19-S01–S02 | 无 | 无 | 不适用 |
| DSDL-M20 | 00K M20 | L189、L195 | DSDL-M20-S01–S10 | 公式 7；L195 范数/λ 抽取异常 | 无 | 不适用 |
| DSDL-M21 | 00K M21 | L199、L205、L211 | DSDL-M21-S01–S05 | 公式 8–9 | 无 | 不适用 |
| DSDL-M22 | 00K M22 | L213、L219 | DSDL-M22-S01–S03 | 公式 10 | 无 | 不适用 |
| DSDL-M23 | 00K M23 | L221、L227 | DSDL-M23-S01–S03 | 公式 11；S02a/S02b 同句；附录 A | 无 | 不适用 |
| DSDL-E1 | 00K E1 | L231 | DSDL-E1-S01–S10 | 附录 B；S06/S07 分开 | N7 | 不适用 |
| DSDL-E2 | 00K E2 | L233 | DSDL-E2-S01–S03 | 无 | 无 | 不适用 |
| DSDL-E3 | 00K E3 | L237 | DSDL-E3-S01–S07 | S07a/S07b 同句 | 无 | 不适用 |
| DSDL-E4 | 00K E4 | L239 | DSDL-E4-S01–S06 | 附录 C–E、G–I | 无 | 不适用 |
| DSDL-E5 | 00K E5 | L243 | DSDL-E5-S01–S03 | Tables 2–3 路由 | 无 | 不适用 |
| DSDL-E7 | 00K E7 | L245 | DSDL-E7-S01–S07 | Tables 2–3 解释 | 无 | 不适用 |
| DSDL-E8 | 00K E8 | L247 | DSDL-E8-S01–S02 | 无 | 无 | 不适用 |
| DSDL-E9 | 00K E9 | L249 | DSDL-E9-S01–S04 | Tables 4–5 路由 | 无 | 不适用 |
| DSDL-E10 | 00K E10 | L251、L265 | DSDL-E10-S01–S03 | Tables 2–3 L253–L263 将 S01 插断 | 无 | 不适用 |
| DSDL-E11 | 00K E11 | L267 | DSDL-E11-S01–S02 | Table 6 路由 | 无 | 不适用 |
| DSDL-E12a | `00K#dsdl-e12` | L269 | DSDL-E12a-S01–S03 | Table 6（L289–L293，浮动） | 无 | 不适用 |
| DSDL-E12b | `00K#dsdl-e12` | L271 | DSDL-E12b-S01–S05 | Table 6 解释 | 无 | 不适用 |
| DSDL-E13 | 00K E13 | L285 | DSDL-E13-S01–S03 | Table 7/消融路由 | 无 | 不适用 |
| DSDL-E14a | `00K#dsdl-e14` | L287 | DSDL-E14a-S01–S03 | Table 7 导入 | 无 | 不适用 |
| DSDL-E14b | `00K#dsdl-e14` | L295 | DSDL-E14b-S01–S04 | Table 7（L305–L309，浮动） | 无 | 不适用 |
| DSDL-X1 | 00K X1 | L299 | DSDL-X1-S01–S02 | 附录 F.1 | 无 | 不适用 |
| DSDL-X2 | 00K X2 | L301 | DSDL-X2-S01–S05 | F3 导入 | 无 | 否（F3） |
| DSDL-X3 | 00K X3 | L303 | DSDL-X3-S01–S09 | F3 L319–L327 浮动；S07a/S07b 同句 | 无 | 否（F3） |
| DSDL-X4 | 00K X4 | L311 | DSDL-X4-S01–S06 | 附录 F.2 | 无 | 不适用 |
| DSDL-C1 | 00K C1 | L315 | DSDL-C1-S01–S04 | S01/S02 分开 | 无 | 不适用 |
| DSDL-C2 | 00K C2 | L317 | DSDL-C2-S01 | 无 | 无 | 不适用 |
| DSDL-C3 | 00K C3 | L329 | DSDL-C3-S01–S04 | 被 F3 浮动位置分隔 | 无 | 否（F3） |
| DSDL-C4 | 00K C4 | L331 | DSDL-C4-S01–S03 | 无 | 无 | 不适用 |
| DSDL-C5 | 00K C5 | L333 | DSDL-C5-S01–S03 | 无 | 无 | 不适用 |
| DSDL-C6 | 00K C6 | L335 | DSDL-C6-S01–S03 | 无 | 无 | 不适用 |
| DSDL-Z1 | 00K Z1 | L339 | DSDL-Z1-S01–S02 | 无 | 无 | 不适用 |
| DSDL-Z2 | 00K Z2 | L341 | DSDL-Z2-S01–S03 | 无 | 无 | 不适用 |
| DSDL-Z3_6 | `00K#dsdl-z3-6` | L343 | DSDL-Z3_6-S01–S11 | 同一出版自然段在 00K 按四项局限拆解 | 无 | 不适用 |

DSDL 分节句数复算：摘要 7，引言 64，文献综述 45，理论/挑战 42，方法 117，实证评价 65，解释分析 22，贡献/启示 18，结论/局限 16，合计 `7+64+45+42+117+65+22+18+16=396`。

## 4. 公式、表、图、尾注与附录对象 manifest

### 4.1 ACAA 非段落对象

| 对象主键 | 源行 | 接口段 | 状态/必须保留的边界 |
|---|---|---|---|
| ACAA-TBL1 | L120–L122 | ACAA-T9/M0 | 可读 HTML；Semantic diversity 的 granularity 单元格空白，待 PDF |
| ACAA-TBL2 | L250–L254 | P5.3.1-1–3 | 可读 HTML；9 个实验条件列，不是 27 |
| ACAA-TBL3 | L264–L268 | P5.3.2-1–3 | 可读 HTML |
| ACAA-TBL4 | L276–L280 | P5.3.3-1 | 可读 HTML |
| ACAA-TBL5 | L282–L286 | P5.3.4-1 | 可读 HTML |
| ACAA-FML1–3 | L145–L159 | ACAA-M5 | 可读 Markdown 公式；由前导语/where 完成句界 |
| ACAA-FML4–5 | L179–L185 | ACAA-M10b | 可读 Markdown 公式；FML5 分母 `u/j` 异常待 PDF/代码 |
| ACAA-FML6 | L194–L196 | ACAA-M11 | 可读 Markdown 公式 |
| ACAA-FML7 | L202–L204 | ACAA-M12 | 可读 Markdown 公式 |
| ACAA-FML8 | L214–L216 | ACAA-M14 | 可读 Markdown 公式 |
| ACAA-F1 | L97–L98 | T2/T3 | `images_downloaded: false`；图论证接口已索引，视觉未核对 |
| ACAA-F2 | L136–L137 | M1 | 同上 |
| ACAA-F3 | L191–L192 | M9–M12 | 同上；DTV 结构图单独主键 |
| ACAA-F4 | L298–L306 | P5.4.1 | 三子图附件占位；视觉未核对 |
| ACAA-F5 | L320–L326 | P5.4.2/P6-1 | 浮动到贡献段之后；三子图未核对 |
| ACAA-F6 | L328–L333 | P5.4.3/P6-1 | 浮动到贡献段之后；三子图未核对 |
| ACAA-F7 | L337–L342 | P5.4.4/P6-2 | 浮动到实践启示段之后；三子图未核对 |
| ACAA-N1 | L352 | I3 | 1 句；customer attention 定义；McGuire/Petty–Cacioppo/Li–Hitt |
| ACAA-N2 | L354 | I8/M12 | 1 句；timeliness×votes 交互边界 |
| ACAA-N3 | L356 | I8 | 1 句；multimodal reviews 定义；Ngiam et al. |
| ACAA-N4 | L358 | I9 | 2 句；sales 通常口径→酒店 occupancy 任务口径 |
| ACAA-N5 | L360 | L11 | 1 句；affinity compatibility 定义 |
| ACAA-N6 | L362 | T6b/M15 | 2 句；query 检索语义与 review-point 起点 |
| ACAA-N7 | L364 | M1 | 2 句；GRU 基模型与 Fu et al. 效率责任 |
| ACAA-N8 | L366 | M2 | 1 句；hotel-specific weights/适用性声明 |
| ACAA-N9 | L368 | M5 | 1 句；trainable Q/K/V 与 fixed features 区分 |
| ACAA-N10 | L370 | M6 | 2 句；hotel-month instance 与 padding 对齐 |
| ACAA-N11 | L372 | M7a/P5.2-4 | 2 句；embedding/representation 输入输出区分 |
| ACAA-N12 | L374 | P5.2-4 | 1 句；ex-ante/ex-post 作者测试报告，无本地数字复现 |
| ACAA-APP-A–I | 主文分散引用 | 多段 | 本地均缺失；只记录方法比较、例图、训练、统计、MAE、实现、显著性、探索、消融等出口，不声称阅读 |

### 4.2 DSDL 非段落对象

| 对象主键 | 源行 | 接口段 | 状态/必须保留的边界 |
|---|---|---|---|
| DSDL-TBL1 | L101–L103 | T7/M0 | 可读 HTML |
| DSDL-TBL2 | L253–L257 | E5/E7/E10 | 可读 HTML；浮动插断 L251/L265 |
| DSDL-TBL3 | L259–L263 | E5/E7/E10 | 可读 HTML；浮动插断 L251/L265 |
| DSDL-TBL4 | L273–L277 | E9/E10 | 可读 HTML |
| DSDL-TBL5 | L279–L283 | E9/E10 | 可读 HTML |
| DSDL-TBL6 | L289–L293 | E11/E12 | 可读 HTML；浮动 |
| DSDL-TBL7 | L305–L309 | E13/E14 | 可读 HTML；浮动 |
| DSDL-FML1 | L134–L136 | M10 | 可读 Markdown 公式 |
| DSDL-FML2 | L138–L140 | M10 | 可读 Markdown 公式 |
| DSDL-FML3 | L162–L164 | M17 | 可读 Markdown 公式 |
| DSDL-FML4 | L166–L168 | M17 | 可读 Markdown 公式 |
| DSDL-FML5 | L175–L177 | M18 | 可读 Markdown 公式 |
| DSDL-FML6 | L181–L183 | M18 | 可读 Markdown 公式 |
| DSDL-FML7 | L191–L193 | M20 | 可读 Markdown 公式；L195 解释异常 |
| DSDL-FML8 | L201–L203 | M21 | 可读 Markdown 公式 |
| DSDL-FML9 | L207–L209 | M21 | 可读 Markdown 公式 |
| DSDL-FML10 | L215–L217 | M22 | 可读 Markdown 公式 |
| DSDL-FML11 | L223–L225 | M23 | `argmin` 下交叉熵疑似缺负号，待 PDF/代码 |
| DSDL-F1 | L115–L116 | M2/M3 | `images_downloaded: false`；视觉未核对 |
| DSDL-F2 | L172–L173 | M15/M17–M18 | 浮动插入公式逻辑段；视觉未核对 |
| DSDL-F3 | L319–L327 | X2/X3/C3 | 三子图浮动到贡献节；视觉未核对 |
| DSDL-N1 | L351 | I8 | 1 句；multiview 定义；Xue et al. |
| DSDL-N2 | L353 | M4 | 1 句；注册表示初始意向的入组逻辑 |
| DSDL-N3 | L355 | M5 | 1 句；pyannote-audio 工具地址，无版本冻结 |
| DSDL-N4 | L357 | M7 | 1 句；商业语音转文本 API，无版本/参数 |
| DSDL-N5 | L359 | M7/M13 | 1 句；先整体序列后角色分开的顺序 |
| DSDL-N6 | L361 | M8 | 2 句；FFT 解释与 MFCC 维度来源 |
| DSDL-N7 | L363 | E1 | 1 句；用户服务协议合规声明，不替代完整伦理报告 |
| DSDL-APP-A–I | 主文分散引用 | 多段 | 本地均缺失；不声称已阅读训练算法、统计、参数、敏感性、补充指标、显著性或实例分析 |

## 5. 引文密度、句长、段长与标点习惯的可复现文本代理

用户要求不仅学习段落功能，还要核对引文密度、句长、段长与标点习惯。下表提供一个可重复的 Markdown 文本代理，而不冒充出版 PDF 的版面统计。语法句数和逻辑段数来自上述人工全量句界，是精确口径；英文词元、引文标记和标点是对当前 Markdown 抽取的可复现代理。

| 指标 | ACAA | DSDL | 口径 |
|---|---:|---:|---|
| 主文语法句 | 397 | 396 | 人工全量句界；排除图表题/纯公式 |
| 逻辑段 | 80 | 76 | 上述 manifest 主键 |
| 每段语法句，均值/中位数/范围 | 4.96 / 5 / 1–9 | 5.21 / 5 / 1–12 | 基于精确句数和段落主键 |
| 清理后英文词元 | 11,145 | 11,017 | 见下方 token regex；数学块/行内数学与 HTML tag 移除 |
| 词元/语法句 | 28.07 | 27.82 | 聚合代理；不声称为逐句中位长度 |
| 词元/逻辑段 | 139.31 | 144.96 | 聚合代理；受 MinerU 断词/数学抽取影响 |
| author–year-like 引文标记 | 147 | 127 | 重复引用重复计；过滤月份+年份假阳性 |
| 每 100 语法句引文标记 | 37.03 | 32.07 | 上一行/精确语法句数 |
| 逗号 `,` | 764 | 735 | 清理后 Markdown 字符计数 |
| 句点 `.` | 633 | 611 | 同上；包含缩写/引文中句点，不等于句数 |
| 分号 `;` | 8 | 7 | 同上 |
| 冒号 `:` | 12 | 17 | 同上 |
| 问号 `?` | 2 | 0 | 同上；RQ 多以陈述句+独立问句展示 |
| 左括号 `(` | 315 | 238 | 同上；同时包含引文、术语、符号和举例 |
| en dash `–` | 17 | 72 | 同上；记录抽取字符，不直接模仿为中文破折号 |
| em dash `—` | 3 | 14 | 同上；可能包含 OCR/排版转写 |

复算规则如下。

1. 取 ACAA L29–L348 或 DSDL L27–L343。遇到单独 `$$` 时切换 display-math 状态并排除该块。
2. 排除空行、`^#{1,6}\s`、`^(History:|Funding:|Supplemental Material:|Keywords:)`、`^<table`、`^!\[\]`、`^(Figure|Table)\s+\d+\.`、`^Note\.`、纯子图字母行和 ACAA 纯时间窗标签行。特别保留以 `Figure 1 outlines` 或 `Table 6 shows` 开头但不匹配图表题格式的正文。
3. 先删除 HTML tags，再删除行内 `\$[^$]*\$` 数学内容和残留 LaTeX command。词元 regex 为 `[A-Za-z]+(?:[-’'][A-Za-z]+)*|\d+(?:[.,]\d+)*`。
4. 引文代理 regex 为 `(?:[A-Z][A-Za-z’'\-]+(?:\s+(?:and|&)\s+[A-Z][A-Za-z’'\-]+|\s+et\s+al\.)?)[,\s\(]+(?:19|20)\d{2}[a-z]?`，然后排除以 January–December 月份开头的匹配。该指标是 citation-marker proxy，不是去重参考文献数，也不替代逐条引用核验。
5. 由于公式跨行、`i.e.`/`et al.` 缩写与 OCR 断词会使自动分句失真，本文件不报任何自动分句得到的“逐句中位词数”伪精确值。若需该分布，必须将上文每个人工语法句 ID 与其完整字符跨行对齐后另行复核。

上表不是手工抄写的近似数。2026-08-15 的最终复验实际执行了下列 PowerShell；它把 ACAA 的 `(1) Quarter`、`(2) Half-year`、`(3) Year` 等纯图内标签全部排除。早先只用 `\w+` 匹配标签会漏掉带连字符的 `Half-year`，因此不能复现本表。

```powershell
function Measure-XiaoMarkdown {
  param([string]$Path,[int]$Start,[int]$End,[string]$Paper,[int]$Grammar,[int]$Paragraphs)
  $source = Get-Content -LiteralPath $Path -Encoding utf8
  $kept = [System.Collections.Generic.List[string]]::new()
  $inDisplay = $false
  foreach ($lineNo in $Start..$End) {
    $line = $source[$lineNo - 1]
    if ($line.Trim() -eq '$$') { $inDisplay = -not $inDisplay; continue }
    if ($inDisplay) { continue }
    $t = $line.Trim()
    if (!$t -or $t -match '^#{1,6}\s' -or
        $t -match '^(History:|Funding:|Supplemental Material:|Keywords:)' -or
        $t -match '^<table' -or $t -match '^!\[\]' -or
        $t -match '^(Figure|Table)\s+\d+\.' -or $t -match '^Note\.' -or
        $t -match '^\([a-z]\)$' -or
        ($Paper -eq 'ACAA' -and $t -match '^\(\d+\)\s+(Quarter|Half-year|Year)$')) { continue }
    $clean = $t -replace '<[^>]+>',' '
    $clean = $clean -replace '\$[^$]*\$',' '
    $clean = $clean -replace '\\[A-Za-z]+',' '
    $kept.Add(($clean -replace '\s+',' ').Trim())
  }
  $text = $kept -join "`n"
  $wordRx = "[A-Za-z]+(?:[-’'][A-Za-z]+)*|\d+(?:[.,]\d+)*"
  $citeRx = "(?:[A-Z][A-Za-z’'\-]+(?:\s+(?:and|&)\s+[A-Z][A-Za-z’'\-]+|\s+et\s+al\.)?)[,\s\(]+(?:19|20)\d{2}[a-z]?"
  $monthRx = '^(January|February|March|April|May|June|July|August|September|October|November|December)'
  $words = [regex]::Matches($text,$wordRx).Count
  $cites = @([regex]::Matches($text,$citeRx) | Where-Object { $_.Value -notmatch $monthRx }).Count
  [pscustomobject]@{
    Paper=$Paper; KeptLines=$kept.Count; Words=$words
    WordsPerSentence=[math]::Round($words/$Grammar,2)
    WordsPerParagraph=[math]::Round($words/$Paragraphs,2)
    CitationMarkers=$cites; CitationsPer100=[math]::Round(100*$cites/$Grammar,2)
    Comma=[regex]::Matches($text,',').Count; Period=[regex]::Matches($text,'\.').Count
    Semicolon=[regex]::Matches($text,';').Count; Colon=[regex]::Matches($text,':').Count
    Question=[regex]::Matches($text,'\?').Count; LeftParen=[regex]::Matches($text,'\(').Count
    EnDash=[regex]::Matches($text,'–').Count; EmDash=[regex]::Matches($text,'—').Count
  }
}

Measure-XiaoMarkdown `
  'database_fulltext_all/28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md' `
  29 348 ACAA 397 80
Measure-XiaoMarkdown `
  'database_fulltext_all/16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md' `
  27 343 DSDL 396 76
```

这些统计的写作约束是：学习的重点仍然是每句的必要性、承接关系和引文覆盖，不是让中文段落机械达到 28 个英文词/句或复制英文括号与破折号。对每个新段落，`00F` 要求在对照记录中保留其句数、字符或词元长度、引文标记与非常用标点，并与功能最近的上述主键比较。
