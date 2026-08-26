import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const runDir = path.resolve("runs/ais_basket_objective_outcome_screening_77");
const outputDir = path.join(runDir, "output_v1");
const rows = JSON.parse(await fs.readFile(path.join(outputDir, "decisions_flat.json"), "utf8"));

const workbook = Workbook.create();
const summary = workbook.worksheets.add("Summary");
const allSheet = workbook.worksheets.add("All Decisions");
const retainedSheet = workbook.worksheets.add("Retained 66");
const excludedSheet = workbook.worksheets.add("Excluded 11");

const headers = [
  "Record ID", "Title", "Year", "Journal", "DOI", "Authors",
  "Objective outcome match", "Objective design target", "Objectively measured outcome",
  "Outcome count", "Objective outcome names", "Outcome roles", "Measurement methods",
  "Objectivity bases", "Subjective focal outcomes", "Artifact–outcome link",
  "Decision reason", "Confidence", "Limitations", "Evidence", "Source file",
];

function rowValues(row) {
  return [
    row.record_id, row.title, row.year, row.journal, row.doi, row.authors,
    row.objective_outcome_match ? "Yes" : "No",
    row.objective_design_target ? "Yes" : "No",
    row.objectively_measured_outcome ? "Yes" : "No",
    row.outcome_count, row.outcome_names, row.outcome_roles, row.measurement_methods_cn,
    row.objectivity_bases_cn, row.subjective_focal_outcomes_cn, row.artifact_outcome_link_cn,
    row.decision_reason_cn, row.confidence, row.limitations_cn, row.evidence, row.source_file,
  ];
}

function populateDecisionSheet(sheet, sourceRows, tableName) {
  const values = [headers, ...sourceRows.map(rowValues)];
  const endRow = values.length;
  const range = sheet.getRange(`A1:U${endRow}`);
  range.values = values;
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(1);
  sheet.freezePanes.freezeColumns(2);
  const header = sheet.getRange("A1:U1");
  header.format = {
    fill: "#17365D",
    font: { bold: true, color: "#FFFFFF" },
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "outside", style: "thin", color: "#17365D" },
  };
  header.format.rowHeight = 34;
  if (endRow > 1) {
    const body = sheet.getRange(`A2:U${endRow}`);
    body.format = {
      verticalAlignment: "top",
      wrapText: true,
      borders: { insideHorizontal: { style: "thin", color: "#E5E7EB" } },
    };
    body.format.rowHeight = 60;
    sheet.getRange(`C2:C${endRow}`).format.numberFormat = "0";
    sheet.getRange(`G2:J${endRow}`).format.horizontalAlignment = "center";
    sheet.getRange(`J2:J${endRow}`).format.numberFormat = "0";
    sheet.getRange(`R2:R${endRow}`).format.numberFormat = "0.00";
    sheet.getRange(`G2:G${endRow}`).conditionalFormats.add("containsText", {
      text: "Yes", format: { fill: "#DCFCE7", font: { color: "#166534", bold: true } },
    });
    sheet.getRange(`G2:G${endRow}`).conditionalFormats.add("containsText", {
      text: "No", format: { fill: "#FEE2E2", font: { color: "#991B1B", bold: true } },
    });
  }
  const widths = [12, 42, 9, 22, 24, 34, 16, 16, 18, 12, 36, 20, 48, 44, 38, 46, 50, 12, 38, 52, 34];
  widths.forEach((width, index) => {
    sheet.getRangeByIndexes(0, index, endRow, 1).format.columnWidth = width;
  });
  sheet.tables.add(`A1:U${endRow}`, true, tableName);
}

populateDecisionSheet(allSheet, rows, "AllDecisionsTable");
populateDecisionSheet(retainedSheet, rows.filter((row) => row.objective_outcome_match), "RetainedTable");
populateDecisionSheet(excludedSheet, rows.filter((row) => !row.objective_outcome_match), "ExcludedTable");

summary.showGridLines = false;
summary.getRange("A1:H1").merge();
summary.getRange("A1").values = [["AIS Basket software-design candidates: objective-outcome screen"]];
summary.getRange("A1:H1").format = {
  fill: "#17365D",
  font: { bold: true, color: "#FFFFFF", size: 16 },
  verticalAlignment: "center",
};
summary.getRange("A1:H1").format.rowHeight = 32;
summary.getRange("A3:A9").values = [["Candidates screened"], ["Retained"], ["Excluded"], ["Objective design target"], ["Objectively measured outcome"], ["Both routes"], ["Retention rate"]];
summary.getRange("B3").formulas = [["=COUNTA('All Decisions'!$A$2:$A$78)"]];
summary.getRange("B4").formulas = [["=COUNTIF('All Decisions'!$G$2:$G$78,\"Yes\")"]];
summary.getRange("B5").formulas = [["=COUNTIF('All Decisions'!$G$2:$G$78,\"No\")"]];
summary.getRange("B6").formulas = [["=COUNTIF('All Decisions'!$H$2:$H$78,\"Yes\")"]];
summary.getRange("B7").formulas = [["=COUNTIF('All Decisions'!$I$2:$I$78,\"Yes\")"]];
summary.getRange("B8").formulas = [["=COUNTIFS('All Decisions'!$H$2:$H$78,\"Yes\",'All Decisions'!$I$2:$I$78,\"Yes\")"]];
summary.getRange("B9").formulas = [["=B4/B3"]];
summary.getRange("A3:B9").format = { borders: { preset: "outside", style: "thin", color: "#CBD5E1" } };
summary.getRange("A3:A9").format = { fill: "#E2E8F0", font: { bold: true, color: "#1E293B" } };
summary.getRange("B3:B8").format.numberFormat = "0";
summary.getRange("B9").format.numberFormat = "0.0%";

summary.getRange("D3:F3").values = [["Year", "Candidates", "Retained"]];
const years = [2021, 2022, 2023, 2024, 2025];
summary.getRange("D4:D8").values = years.map((year) => [year]);
summary.getRange("E4").formulas = [["=COUNTIF('All Decisions'!$C$2:$C$78,D4)"]];
summary.getRange("E4:E8").fillDown();
summary.getRange("F4").formulas = [["=COUNTIFS('All Decisions'!$C$2:$C$78,D4,'All Decisions'!$G$2:$G$78,\"Yes\")"]];
summary.getRange("F4:F8").fillDown();
summary.getRange("D3:F8").format = { borders: { preset: "outside", style: "thin", color: "#CBD5E1" } };
summary.getRange("D3:F3").format = { fill: "#E2E8F0", font: { bold: true, color: "#1E293B" } };
summary.getRange("D4:F8").format.numberFormat = "0";

summary.getRange("A12:H12").merge();
summary.getRange("A12").values = [["Decision rule"]];
summary.getRange("A12:H12").format = { fill: "#DCE6F1", font: { bold: true, color: "#17365D" } };
summary.getRange("A13:B16").values = [
  ["Retain", "At least one route below is true."],
  ["Route 1", "The artifact/design explicitly targets improvement in a substantive objective state, behavior, performance, or result."],
  ["Route 2", "At least one central substantive outcome is objectively measured using task performance, logs, time, errors, actual behavior/choice, transactions, sensors, or verifiable scoring."],
  ["Do not count", "Self-report-only constructs, manipulation/attention checks, controls, demographics, treatment exposure, or numerical scales without objective measurement."],
];
summary.getRange("A13:A16").format = { fill: "#F1F5F9", font: { bold: true } };
summary.getRange("A13:B16").format.wrapText = true;
summary.getRange("A13:B16").format.verticalAlignment = "top";
summary.getRange("A13:B16").format.borders = { insideHorizontal: { style: "thin", color: "#E5E7EB" } };
summary.getRange("A18:H18").merge();
summary.getRange("A18").values = [["Scope note: this is a second-stage outcome screen of the 77 raw software-design candidates. It does not independently correct any artifact-eligibility false positives inherited from the prior screen."]];
summary.getRange("A18:H18").format = { fill: "#FFF7ED", font: { color: "#9A3412", italic: true }, wrapText: true };
summary.getRange("A18:H18").format.rowHeight = 42;
summary.getRange("A20:H20").merge();
summary.getRange("A20").values = [["Model: deepseek-v4-flash | Unit: one full-text article per independent request | Completed: 77/77 | Failures: 0"]];
summary.getRange("A20:H20").format = { font: { color: "#475569", italic: true }, wrapText: true };
summary.getRange("A:A").format.columnWidth = 28;
summary.getRange("B:B").format.columnWidth = 74;
summary.getRange("C:C").format.columnWidth = 4;
summary.getRange("D:F").format.columnWidth = 16;
summary.getRange("G:H").format.columnWidth = 12;

const summaryCheck = await workbook.inspect({ kind: "table", sheetId: "Summary", range: "A1:F20", include: "values,formulas", tableMaxRows: 20, tableMaxCols: 6, maxChars: 8000 });
console.log(summaryCheck.ndjson);
const retainedCheck = await workbook.inspect({ kind: "table", sheetId: "Retained 66", range: "A1:K5", include: "values", tableMaxRows: 5, tableMaxCols: 11, tableMaxCellChars: 100, maxChars: 5000 });
console.log(retainedCheck.ndjson);
const excludedCheck = await workbook.inspect({ kind: "table", sheetId: "Excluded 11", range: "A1:K12", include: "values", tableMaxRows: 12, tableMaxCols: 11, tableMaxCellChars: 100, maxChars: 8000 });
console.log(excludedCheck.ndjson);
const errors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "formula error scan" });
console.log(errors.ndjson);
const preview = await workbook.render({ sheetName: "Summary", range: "A1:H20", scale: 1.5, format: "png" });
await fs.writeFile(path.join(outputDir, "objective_outcome_screening_preview.png"), new Uint8Array(await preview.arrayBuffer()));
for (const sheetName of ["All Decisions", "Retained 66", "Excluded 11"]) {
  const sheetPreview = await workbook.render({ sheetName, range: "A1:K7", scale: 1, format: "png" });
  const safeName = sheetName.toLowerCase().replaceAll(" ", "_");
  await fs.writeFile(path.join(outputDir, `${safeName}_preview.png`), new Uint8Array(await sheetPreview.arrayBuffer()));
}
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(path.join(outputDir, "objective_outcome_screening_77.xlsx"));
