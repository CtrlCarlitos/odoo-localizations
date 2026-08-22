#!/usr/bin/env python3
"""HN Stage-5 gate-1 coverage generator.

Parses the source registry (hn/sources/README.md) and every requirements file
(hn/requirements/<topic>/<nn>_*.md), verifies the three script-checkable gates:

  G1  every registry row maps to >=1 LB citation OR carries an explicit
      not-applicable annotation (SOURCES dict below);
  G2  every FR cites >=1 LB of its own file (or a direct source cite);
  G3  every LB row's source tokens resolve to registry rows (and the files
      exist on disk).

Writes hn/requirements/COVERAGE.md. Exit 1 if any gate fails.

Regenerate after any wave that adds FRs/LBs/EVIDs:  python3 hn/scripts/build_coverage.py
"""
import os, re, sys, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REG = os.path.join(ROOT, "hn/sources/README.md")
REQ = os.path.join(ROOT, "hn/requirements")
TOPICS = ["taxation", "e-invoicing", "fiscal-reporting", "payroll"]
EXPECTED = {"taxation": 249, "e-invoicing": 157, "fiscal-reporting": 363, "payroll": 330}

# Explicit per-source status/notes. Sources absent here must be LB-cited (G1).
# Vocabulary mirrors SV's COVERAGE.md:
#   cited-as-LB | not-applicable-this-wave (+ reason)
SOURCES = {
    "93_Decreto_31-2019_interp_reforma_D31-2018_22A.pdf": (
        "not-applicable-this-wave",
        "Interpretive instrument on the D. 31-2018 22-A transition (FY2017 tariff/cálculo per D. 278-2013). "
        "No evidence pass yet; the three dated 22-A regimes are LB'd via `80_`/`04_` (taxation/03, R-H32). "
        "Read only if FY2017 historical reconstruction is ever required; gazette-number print oddity (34,932 vs catalog 34,934) pinned in registry."),
    "94_Acuerdo_464-1990_Regl_Art50_LeyISR.pdf": (
        "not-applicable-this-wave",
        "HISTORICAL reglamento-chain ancestor (1990 retention values: L10k gate, 5% honorarios, 20-day entero — all superseded). "
        "V-HN1b: evidenced EVID-351..352-class chain rows in `93+94+97_chain.evidence.md` (values confirmed; no printed derogation clause; "
        "every CR tagged HISTORICAL-NEVER-CURRENT). Explicitly NOT the modern Reglamento Ley ISR ('Acuerdo N°799' — W8/R-H83: identity pinned = G 19,972 13-ene-1970; TEXT still unacquired)."),
    "95_Decreto_199-2006_Ley_Adulto_Mayor.pdf": (
        "not-applicable-this-wave",
        "IN CORPUS UNREAD (V-HN1 status fix): acquired 2026-08-19 but never given an evidence pass; the S-HN1 'D. 199-2006 "
        "unacquired' premise was stale. THE activation key for the taxation/02 senior-tier L30,000@60 row (FR-067, OQ-008 — "
        "valid_from unpinned until read). Next: mini evidence pass + verify article text vs D. 59-2020 (`79_`) / D. 45-2025 (`96_`)."),
    "96_Decreto_45-2025_reforma_Adulto_Mayor.pdf": (
        "not-applicable-this-wave",
        "V-HN1b: evidenced EVID-342..344 (services-discount side: Art. 31 utilities tiers 25/30%/35/40%, Arts. 31-A/31-B Fiscalía/"
        "visible-info) — verified NOT to touch the Art. 30.14 deduction (OQ-008 resolution leg). Out of the four approved topics' scope "
        "(special-regimes/commercial-legal territory); cite there when those waves open."),
    "109_Gaceta_36460_Decreto_59-2023_Adulto_Mayor.pdf": (
        "not-applicable-this-wave",
        "IN CORPUS UNREAD (acquired 2026-08-20 via ENAG Gaceta Digital): G 36,460 (14-feb-2024) publishing D. 59-2023 — the Adulto Mayor "
        "intermediate reform (taxation/02 OQ-009's instrument). Page-1 verified; preliminary pp.3-4 scan: reformed Art. 30 prints the "
        "tercera/cuarta-edad two-class structure and RESTATES numeral 14 (the L30,000 credit survives). Evidence pass = next session "
        "(wording comparison vs 95_, vigencia pin, beneficiary-class check, the edition's other decrees)."),
    "97_Decreto_194-2002_Ley_Equilibrio_Financiero.pdf": (
        "not-applicable-this-wave",
        "Original of the law whose reformed Art. 14 (65+ ≤L350k exemption) is encoded from `79_` (D. 59-2020 prints the current "
        "text); 2002 ISV-side reforms superseded by the `02_` consolidation. Retained for chain verification; no current-law LB role."),
}

# Special annotation appended to the cited-in summary of particular rows.
SPECIAL = {
    "49_Ayuda_revaluacion_154.pdf": "V-HN1: LB co-cite added to fiscal-reporting/08 LB-007 (was evidence-anchor-only EV29:EVID-108).",
    "89_Decreto_117-2021_interp_Art113_CT.pdf": "V-HN1: evidence pass EVID-334..336 (10th gloss incident — Art. 2 aguinaldo interp); "
        "LB rows added to payroll/02 (LB-012 + FR-087, OQ-007 conflict vs ISR 10.h) and fiscal-reporting/10 (LB-013, OQ-004 resolved).",
    "105_Decreto_112_Ley_Septimo_Dia_13er_Mes_Aguinaldo.pdf": "W5: evidence pass EVID-362..372 (R-H74 — the 13th-month statutory home); "
        "payroll/02 P2 UNBLOCKED (OQ-001 resolved; FR-052..054 rewritten + FR-088..093); séptimo día layer → payroll/06 (LB-014..016, FR-248/249).",
    "106_Gaceta_29320_D43-97_bono_educativo_Ac154-2000_reglamento_bono.pdf": "W5: evidence pass EVID-373..379 — TWO extracts: D. 43-97 from "
        "G 28,271 (29-may-1997, masthead-confirmed — the '29320' title = the reglamento's 6-nov-2000 gazette, number illegible ≈29,32x); "
        "bono reglamento OQ-004 RESOLVED (payroll/02 FR-094..096); SMM Arts. 20/35 gazette originals co-cited in payroll/01 LB-007.",
    "107_Gaceta_31753_Decreto_150-2008.pdf": "W5: evidence pass EVID-380..382 — CT Art. 120/120-A + the annual-pact Art. 2 as instrument "
        "original (≡ 86_ fn.19, no drift); R-H58 anchors upgraded in payroll/08 LB-007/008 + FR-305; new lineage lead D. 247-89.",
    "108_Acuerdo_345_Regl_Comisiones_Salario_Minimo.pdf": "W5: evidence pass EVID-383..384 — commissions procedure + the fijación "
        "+15-day vigencia default (payroll/01 LB-022 + FR-041); Acuerdo 345's own vigencia unpinned (G 25,680 date not printed).",
}

reg_re = re.compile(r"^\|\s*`([^`]+)`\s*\|")
lb_re = re.compile(r"^\|\s*(LB-\d+)\s*\|")
fr_re = re.compile(r"^\s*-\s+\*\*HN-(TAX|EINV|FREP|PAYR)-FR-(\d+)\s*:\*\*")
ac_re = re.compile(r"^\s*-\s+\*\*AC-\d+\s*:\*\*", re.M)
oq_re = re.compile(r"^\|\s*OQ-\d+\s*\|", re.M)
tok_re = re.compile(r"`(?:hn/sources/)?([0-9]{2,3}_[A-Za-z0-9_.\-]+?\.(?:pdf|xlsx|xls|docx))`")
lbcit_re = re.compile(r"\bLB-(\d+)\b")


def main():
    registry, reg_section = [], None
    for line in open(REG, encoding="utf-8"):
        m = reg_re.match(line)
        if m and not m.group(1).endswith("/"):
            registry.append(m.group(1))
    regset = set(registry)

    diskset = {f for f in os.listdir(os.path.join(ROOT, "hn/sources"))
               if not f.startswith(".") and f != "README.md"}
    errors = []
    if regset != diskset:
        errors.append(f"registry/disk mismatch: {sorted(regset ^ diskset)}")

    cit, frs_no_lb, lb_bad = {}, [], []
    fr_count = lb_count = ac_count = oq_count = 0
    topic_frs = {t: 0 for t in TOPICS}
    reqfiles = []
    for t in TOPICS:
        for p in sorted(glob.glob(os.path.join(REQ, t, "[0-9][0-9]_*.md"))):
            reqfiles.append(p)

    for rf in reqfiles:
        rel = os.path.relpath(rf, REQ)
        text = open(rf, encoding="utf-8").read()
        defined = set()
        for line in text.splitlines():
            m = lb_re.match(line)
            if m:
                lb_id = m.group(1)
                defined.add(lb_id)
                lb_count += 1
                toks = tok_re.findall(line)
                if not toks:
                    lb_bad.append(f"{rel} {lb_id}: no source token")
                for tk in toks:
                    if tk not in regset:
                        lb_bad.append(f"{rel} {lb_id}: token not in registry: {tk}")
                    if not os.path.exists(os.path.join(ROOT, "hn/sources", tk)):
                        lb_bad.append(f"{rel} {lb_id}: file missing on disk: {tk}")
                    cit.setdefault(tk, {}).setdefault(rel, []).append(lb_id)
        blocks = re.split(r"(?m)^(?=\s*-\s+\*\*HN-(?:TAX|EINV|FREP|PAYR)-FR-)", text)
        for b in blocks:
            m = fr_re.match(b)
            if not m:
                continue
            frid = f"HN-{m.group(1)}-FR-{int(m.group(2)):03d}"
            fr_count += 1
            topic_frs[m.group(1).lower().replace("tax", "taxation").replace("einv", "e-invoicing")
                      .replace("frep", "fiscal-reporting").replace("payr", "payroll")] += 1
            if not lbcit_re.findall(b) and not tok_re.findall(b):
                frs_no_lb.append(f"{rel} {frid}")
            for r in set(lbcit_re.findall(b)):
                if f"LB-{int(r):03d}" not in defined:
                    lb_bad.append(f"{rel} {frid}: unresolved LB-{int(r):03d}")
        ac_count += len(ac_re.findall(text))
        oq_count += len(oq_re.findall(text))

    for t, exp in EXPECTED.items():
        if topic_frs[t] != exp:
            errors.append(f"FR count {topic_frs[t]} != expected {exp} for {t}")
    if frs_no_lb:
        errors.append(f"FRs without LB/source cite: {frs_no_lb}")
    if lb_bad:
        errors.append(f"LB issues: {lb_bad[:20]}")
    uncited = [f for f in registry if f not in cit and f not in SOURCES]
    if uncited:
        errors.append(f"uncited sources without N/A annotation: {uncited}")

    if errors:
        print("GATE FAILURES:", *errors, sep="\n  ")
        sys.exit(1)

    # ---- emit COVERAGE.md ----
    n_cited = sum(1 for f in registry if f in cit)
    n_na = len([f for f in registry if f not in cit])
    out = []
    out.append("# HN — Source coverage matrix\n")
    out.append("| Field   | Value |")
    out.append("|---------|-------|")
    out.append("| Country | hn |")
    out.append("| Topic   | all (cross-topic) |")
    out.append("| Status  | validated (V-HN1 gate 1 — S-HN1/S-HN2/S-HN3/S-HN4 waves; W5 acquisition-reads refresh) |")
    out.append("| Authors | script `hn/scripts/build_coverage.py` (regenerate after every wave) |")
    out.append("| Updated | 2026-08-20 |")
    out.append("")
    out.append(f"Every row of [../sources/README.md](../sources/README.md) ({len(registry)} registered files, gap 103 reserved-unused)"
               f" mapped against the four synthesis waves + the W5 acquisition-reads wave (taxation 7 files / e-invoicing 4 / fiscal-reporting 11 /"
               f" payroll 10 = 32 requirement files; {fr_count} FRs, {lb_count} LB rows, {ac_count} ACs, {oq_count} OQ rows)."
               " Script-checked gates (exit 1 on failure): every FR cites ≥1 LB of its own file;"
               " every LB token resolves to a registry row that exists on disk; every registry row is LB-cited or"
               " carries an explicit not-applicable annotation; per-topic FR totals match the wave records"
               f" ({', '.join(f'{t} {v}' for t, v in EXPECTED.items())}).")
    out.append("")
    out.append("Status vocabulary (mirrors SV): **cited-as-LB** — appears in a Legal Basis row of a requirements file"
               " (citing file(s) + LB ids listed); **not-applicable-this-wave** — explicit annotation with reason"
               " (superseded/historical, in-corpus-unread pending evidence pass, or out of scope for the four topics).")
    out.append("")
    out.append(f"## Matrix ({len(registry)} source files)")
    out.append("")
    out.append("| Source | Status | Cited in / note |")
    out.append("|--------|--------|-----------------|")
    for f in registry:
        if f in cit:
            s = "; ".join(f"`{k}` ({'+'.join(v)})" for k, v in sorted(cit[f].items()))
            if f in SPECIAL:
                s += f" — {SPECIAL[f]}"
            out.append(f"| {f} | cited-as-LB | {s} |")
        else:
            status, note = SOURCES[f]
            out.append(f"| {f} | {status} | {note} |")
    out.append("")
    out.append("## Rollup")
    out.append("")
    out.append("| Status | Rows |")
    out.append("|--------|------|")
    out.append(f"| cited-as-LB | {n_cited} |")
    out.append(f"| not-applicable-this-wave | {n_na} |")
    out.append(f"| **Total** | **{len(registry)}** |")
    out.append("")
    out.append("""## V-HN1 gate-1 findings (2026-08-20, fixed in this wave)

1. **`89_` D. 117-2021 had NO evidence pass** despite being in corpus since
   2026-08-18 — the registry gloss sold it as the CT-Art.-113.1 interp only.
   Full read (EVID-334..336) surfaced **Art. 2 = authentic interpretation of
   D. 112-82 Art. 3** (séptimo día + 13th month = salario ONLY for labor
   prestaciones; aguinaldo exempt from ALL taxes/cotizaciones/deductions
   except alimony). Encoded: payroll/02 LB-012 + **HN-PAYR-FR-087**
   (reserved-range addition) + OQ-007 (CONFLICT vs ISR Art. 10.h 10-SMM caps —
   ISR rows stand, immunity row conflict-flagged); IHSS-base statutory lean
   recorded in payroll/03 (flag stays); RAP-base lean in payroll/05 OQ-001;
   TP-scope narrowing in fiscal-reporting/10 LB-013 + FR-326(c) with
   **OQ-004 RESOLVED** (the Ayuda's "Decreto No 117-2021" = `89_`, the
   carrier of CT 113.1's quoted clause). 10th title-vs-content incident
   (registry gloss understated content).
2. **`95_`/`96_` (D. 199-2006 + D. 45-2025, Adulto Mayor) were in corpus
   BEFORE S-HN1** yet taxation/02 claimed the statute "unacquired" —
   corrected to IN-CORP-UNREAD (no evidence pass); FR-067 senior-tier row
   stays activation-blocked pending that read (OQ-008). HANDOVER acquisition
   queue line amended accordingly.
3. **`49_` (Ayuda revaluación 154) was evidence-anchor-cited but LB-uncited**
   — EV29:EVID-108 carried it while LB-007 named only `04_`; co-cite added.
4. `93_`/`94_`/`97_` annotated not-applicable-this-wave (interpretive FY2017
   transition / historical 1990 ancestor / superseded-as-cited original) —
   no FR rests on them; read-on-demand discipline documented above.

Gate 2 (NotebookLM): no notebook exists for HN — optional gate skipped per
procedure ("where a notebook exists"). Gate 3 (adversarial review): dispatched
per topic at this wave; findings adjudicated in EXTRACTION_PLAN wave log.

## W5 refresh (2026-08-20, acquisition-reads wave)

The four V-HN1b acquisitions (105_-108_) given full evidence passes
(EVID-362..384) and flipped from not-applicable to cited-as-LB: **105_ D.
112-1982 = the 13th-month statutory home (R-H74) — payroll/02 P2 UNBLOCKED**
(OQ-001 resolved; the "D. 135-94 Ley del Aguinaldo + Acuerdo 201-96" framing
was a conflation, R-H75); the D. 112 séptimo-día chapter → payroll/06
(FR-248/249 statutory valuation/deemed-inclusion/forfeiture); **106_ = TWO
gazette extracts** (D. 43-97 G 28,271 29-may-1997 + Reglamento STSS-154-2000,
gazette 6-nov-2000) — bono reglamento OQ-004 RESOLVED (FR-094..096); 107_
D. 150-2008 original ≡ 86_ fn.19 (R-H58 anchors upgraded; D. 247-89 lineage
lead); 108_ Acuerdo 345 commissions procedure + fijación +15-day default
(payroll/01 FR-041). Payroll FR total 314 → 326 (+9 payroll/02, +2 payroll/06,
+1 payroll/01).

## W7 refresh (2026-08-21, residual-chain decode wave)

119_ (congreso "Inventarios de Leyes" — official thematic law inventory,
text-native) registered + cited as LB (payroll/02 LB-025). R-H81: the 102_
OQ-2 "conflict" decodes as TWO 1995 decrees — D. 74-95 = the Art.-34 interp
(G 27,655 18-may-1995; the W4 footnote read "54-95" was an OCR misread,
dual-dpi-fixed in EVID-238/LB-002) and D. 54-95 = the jubilados/pensionados
extension (G 27,639 28-abr-1995; the book's "28,639" = digit-swap,
monotonicity-arbitrated) → payroll/02 FR-057 re-attributed + FR-097 dated
beneficiary row + OQ-002 RESOLVED. R-H82: D. 36-90 = G 26,131 11-MAY-1990
(the inventory's "11-abril" = its own slip — payroll/06 LB-014/FR-248 rows)
and D. 247-89 = G 26,028 6-ene-1990 (payroll/08 LB-007 lineage; text remains
the live residual). Payroll FR total 326 → 327 (+FR-097); LBs +1; ACs +1.""")
    with open(os.path.join(REQ, "COVERAGE.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print(f"OK: COVERAGE.md written — {len(registry)} rows ({n_cited} cited-as-LB, {n_na} N/A); "
          f"{fr_count} FRs / {lb_count} LBs / {ac_count} ACs / {oq_count} OQs; gates pass.")


if __name__ == "__main__":
    main()
