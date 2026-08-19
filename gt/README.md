# Guatemala (GT)

Odoo localization requirements for Guatemala, including electronic invoicing
(facturación electrónica, régimen FEL).

- **Tax authority:** Superintendencia de Administración Tributaria (SAT) — https://www.sat.gob.gt
- **Takumi proof of concept:** not started.

## Requirements status

| Topic | Directory | Status |
|-------|-----------|--------|
| Electronic invoicing | [requirements/e-invoicing/](requirements/e-invoicing/) | Not started |
| Taxation | [requirements/taxation/](requirements/taxation/) | Not started |
| Chart of accounts | [requirements/chart-of-accounts/](requirements/chart-of-accounts/) | Not started |
| Payroll | [requirements/payroll/](requirements/payroll/) | Not started |
| Fiscal reporting | [requirements/fiscal-reporting/](requirements/fiscal-reporting/) | Not started |

Status values: Not started, In progress, In review, Complete.

## Sources

**66 registered source files + 2 schema/catalog directories** (numbering
01–73; gaps 27 dropped, 37/41/58 reserved-pending browser acquisition) — see
[sources/README.md](sources/README.md) for the full registry with provenance
and re-verify flags. Coverage: FEL e-invoicing stack (acuerdos de directorio,
incorporation resolutions SAT-DSI, Reglas y validaciones v1.7.10, Doc.
Técnico Servicios, XSD schemas + JSON catalogs from two official channels,
manuals, test cases), taxation core laws (IVA 27-92 [pre-FEL vintage — OQ10],
Reglamento IVA AG 5-2013, Código Tributario 6-91, LAT 10-2012 + AG 213-2013),
payroll (Código de Trabajo, IGSS, IRTRA D-15-1928, INTECAP D-17-72, aguinaldo
D-42-92, salario mínimo instruments), fiscal reporting (form inventory
snapshot, retenciones Web IVA/ISR pages + manuals, LET manuals, agentes
roster, criterios), chart-of-accounts anchor (Código de Comercio D-2-70), and
special regimes (zonas francas D-65-89 set, maquila D-29-89 set). Research
record: [SOURCE_RESEARCH.md](SOURCE_RESEARCH.md); pending browser items:
[DOWNLOAD_QUEUE.md](DOWNLOAD_QUEUE.md) (rev 5).
