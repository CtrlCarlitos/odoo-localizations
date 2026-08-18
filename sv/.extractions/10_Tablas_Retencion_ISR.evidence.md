# Evidence — 10_Tablas_Retencion_ISR.pdf

Sources: `sv/sources/10_Tablas_Retencion_ISR.pdf` (TABLAS DE RETENCION DEL IMPUESTO SOBRE LA RENTA, DECRETO Nº 75, 21-XII-1991, D.O. Nº 1, Tomo 314, 6-I-1992; literales a)–c) sustituidos por D.E. Nº 25 del 18-II-1992, D.O. Nº 34, Tomo 314, 20-II-1992, vigentes desde el 1-III-1992 — las tablas transcritas son las del D.E. Nº 25).
Read: 2026-08-17 (W6). Full document (3pp).
Citation form: Table + page (PDF txt page markers).

## EVID-148 Tablas Retención ISR — tabla a) remuneraciones mensuales

- **Loc:** Table a) "Remuneraciones pagaderas mensualmente (1)" (p.1).
- **Verbatim:** columnas "Si la remuneración mensual es: DESDE / HASTA" → "El impuest o a retener será de:". Todas las filas, ambas monedas (¢ colones / $ dólares, paridad implícita 8.75):

```
DESDE ¢0.01 ($0.00)      HASTA ¢2,770.82 ($316.67)   SIN RETENCION
DESDE ¢2,770.83 ($316.67) HASTA ¢4,104.16 ($469.05)   ¢41.70 ($4.77) más el 10% sobre exceso de ¢2,770.83 ($316.67)
DESDE ¢4,104.17 ($469.05) HASTA ¢6,666.67 ($761.91)   ¢41.70 ($4.77) más el 10% sobre exceso de ¢2,000.00 ($228.57)
DESDE ¢6,666.68 ($761.91) HASTA ¢16,666.00 ($1,904.69) ¢525.00 ($60.00) más el 20% sobre exceso de ¢6,666.67 ($761.91)
DESDE ¢16,666.01 ($1,904.69)  En adelante              ¢2,000.00 ($228.57) más el 30% sobre exceso de ¢16,666.00 ($1,904.69 [sic: paréntesis de cierre omitido en el impreso])
```

- **Gloss:** English gloss: monthly withholding table for permanent-service remunerations (salaries/wages, cash or in kind) of resident natural persons. Structure = cuota fija (fixed quota) + marginal % over excess of a stated threshold ("sobre exceso de"). Rates 0% (exempt band to ¢2,770.82), 10%, 20%, 30%. Base is the monthly remuneración; the decree does NOT state gross-vs-net (no mention of ISSS/afp deductions). Footnote (1): these literals a)–c) are the substituted (D.E. Nº 25) versions effective 1-III-1992.
- **Candidate CRs:** Odoo payroll ISR withholding brackets (SV, old Ley ISR era) as dated legal data; amounts stored in both ¢ and $ (fixed 8.75 conversion); bracket engine = fixed amount + marginal rate over lower-bound excess.
- **Topics:** payroll, taxation.
- **Doubts/xref:** fila 3 offset "exceso de ¢2,000.00" ≠ límite inferior ¢4,104.17 (discontinuidad; patrón se repite en b) y c), ver OQ-1); cuota fija ¢41.70 ya en el inicio del bracket 2 salta desde "SIN RETENCION" (discontinuidad); xref Ley ISR D.L. 134 Arts. 37/38 (03_); rango 0.01–16,666.01+ en ¢; moneda impresa en par ¢/$ pese a fecha 1992 (ver OQ-5).

## EVID-149 Tablas Retención ISR — tabla b) remuneraciones quincenales

- **Loc:** Table b) "Remuneraciones pagaderas quincenalmente (1)" (p.2).
- **Verbatim:** "Si la remuneración Quincenal es: DESDE / HASTA" → retención:

```
DESDE ¢0.01 ($0.00)       HASTA ¢1,385.41 ($158.33)   SIN RETENCION
DESDE ¢1,385.42 ($158.33) HASTA ¢2,052.08 ($234.52)   ¢20.85 ($2.38) más el 10% sobre exceso de ¢1,385.42 ($158.33)
DESDE ¢2,052.09 ($234.52) HASTA ¢3,333.33 ($380.95)   ¢20.85 ($2.38) más el 10% sobre exceso de ¢1,000.00 ($114.29)
DESDE ¢3,333.34 ($380.95) HASTA ¢8,333.33 ($952.34)   ¢262.50 ($30.00) más el 20% sobre exceso de ¢3,333.34 ($380.95)
DESDE ¢8,333.01 ($952.34)      En adelante             ¢1,000.00 ($114.29) más el 30% sobre exceso de ¢8,333.01 ($952.34)
```

- **Gloss:** English gloss: quincenal (fortnightly, half-month) variant; every bound/quota is exactly the monthly value ÷ 2 (e.g. 41.70/2 = 20.85; 525.00/2 = 262.50; 2,000.00/2 = 1,000.00). Same mechanics: fixed quota + marginal % over stated excess threshold; exempt to ¢1,385.41; rates 10/20/30%.
- **Candidate CRs:** Odoo SV payroll must support quincenal contract frequency with its own legal table (not a naive half of monthly tax); amounts as dated legal data in ¢/$.
- **Topics:** payroll, taxation.
- **Doubts/xref:** solapamiento impreso HASTA ¢8,333.33 vs DESDE ¢8,333.01 (ver OQ-2); $952.34 corresponde a ¢8,333.00 (= 16,666.00/2), no a 8,333.33 (8,333.33/8.75 = 952.38); mismo offset anómalo "¢1,000.00" en fila 3 (OQ-1).

## EVID-150 Tablas Retención ISR — tabla c) remuneraciones semanales

- **Loc:** Table c) "Remuneraciones pagaderas semanalmente (1)" (p.2).
- **Verbatim:** "Si la remuneración semanal es: DESDE / HASTA" → retención:

```
DESDE ¢0.01 ($0.00)       HASTA ¢692.70 ($79.17)      SIN RETENCION
DESDE ¢692.71 ($79.17)    HASTA ¢1,026.04 ($117.26)   ¢10.43 ($1.19) más el 10% sobre exceso de ¢692.71 ($79.17)
DESDE ¢1,026.05 ($117.26) HASTA ¢1,666.66 ($190.48)   ¢10.43 ($1.19) más el 10% sobre exceso de ¢500.00 ($57.14)
DESDE ¢1,666.67 ($190.48) HASTA ¢4,166.00 ($476.11)   ¢131.25 ($15.00) más el 20% sobre exceso de ¢1,666.66 ($190.48)
DESDE ¢4,1666.01 [sic; leer ¢4,166.01] ($476.12)  En adelante   ¢500.00 ($57.14) más el 30% sobre exceso de ¢4,166.00 ($476.11)
```

- **Gloss:** English gloss: weekly variant; bounds/quotas = monthly ÷ 4 (41.70/4 = 10.425 → 10.43; 525.00/4 = 131.25; 2,000.00/4 = 500.00). Same fixed-quota + marginal-% mechanics; exempt to ¢692.70; rates 10/20/30%. The "DESDE" of the last row prints an extra digit (4,1666.01) — the $476.12 (= 4,166.01/8.75) confirms it should read 4,166.01.
- **Candidate CRs:** Odoo SV payroll weekly frequency table as dated legal data; digit-level validation of source PDF needed before encoding (OQ-3).
- **Topics:** payroll, taxation.
- **Doubts/xref:** "¢4,1666.01" typo flag [?] (OQ-3); límite superior ¢4,166.00 = 16,666.00/4 exacto (consistente con a)/b)); mismo offset anómalo "¢500.00" en fila 3 (OQ-1).

## EVID-151 Tablas Retención ISR — períodos especiales (d) y caso multi-empleador (e)

- **Loc:** Literals d) "Remuneraciones pagaderas por día o períodos especiales" and e) "Caso especial" (p.2).
- **Verbatim:**

```
d) Remuneraciones pagaderas por día o períodos especiales
"Se aplicará la tabla mensual, para lo cual buscará el salario equivalente mensual, lo mismo que la porción
del impuesto que corresponda, y por el mismo método el impuesto que corresponda al período."

e) Caso especial
"Cuando una persona natural domiciliada preste servicios de carácter permanente, para dos o más personas o
empresas y la sumatoria de todas las remuneraciones mensuales o su equivalente fuere igual o mayor de
¢2,770.83 ($316.67), cada remuneración menor a ¢2,770.83 ($316.67) estará sujeta a una retención del 2%;
la remuneración que fuere igual o mayor de ¢2,770.83 ($316.67) estará sujeta a retención conforme a las
Tablas anteriores según el caso. Para estos efectos el contribuyente como sujeto pasivo de la retención,
queda obligado a informar a cada Agente de retención para quienes trabaja y cual es el monto de la
remuneración respectiva en cada caso."
```

- **Gloss:** English gloss: (d) for daily or special pay periods, use the MONTHLY table: find the equivalent monthly salary, compute the corresponding monthly tax, and derive the period's tax by the same method (prorate via equivalent-monthly lookup, not a flat 1/30). (e) Multiple employers: if the sum of all monthly (or equivalent) remunerations ≥ ¢2,770.83 ($316.67), each individual remuneration BELOW that figure is withheld at a flat 2%; the one at or above it uses the applicable table. Employee must disclose to each withholding agent who they work for and each remuneration amount.
- **Candidate CRs:** Odoo SV payroll proration rule (compute ISR on equivalent-monthly base for daily/special periods); flat 2% withholding branch for secondary employments below threshold; employee multi-employer declaration/information requirement.
- **Topics:** payroll, taxation.
- **Doubts/xref:** umbral del 2% usa el mismo ¢2,770.83 ($316.67) del límite exento mensual; base de la equivalencia mensual no definida (¿30 días? ¿4,33 semanas?) — OQ-4; xref 03_ (Ley ISR retenciones).

## EVID-152 Tablas Retención ISR — sujetos, base, vigencia y contexto (Arts. 1–4, considerandos, reforma)

- **Loc:** Considerandos I–IV, Arts. 1–4, firma y nota REFORMAS (pp.1–3).
- **Verbatim:**

```
Considerando II: "la nueva Ley de Impuesto sobre la Renta, según Decreto Legislativo número 134 de fecha
dieciocho de diciembre de mil novecientos noventa y uno; publicado en el Diario Oficial número 242 Tomo
313 del día 21 del mismo mes y año, en el Art. 92 Inciso 2°) numeral 1°) establece como obligados a
declarar, a todas las personas naturales domiciliadas que obtengan rentas superiores a ¢ 22,000.00
($2,514.29), dentro de un ejercicio de imposición"

Considerando III: "el Art. 38 del mismo cuerpo legal, prescribe que las personas naturales domiciliadas,
cuyos ingresos provengan exclusivamente de remuneraciones de carácter permanente; Salarios, Sueldos y
otros, y sus ingresos anuales no excedan de ¢ 50,000.00 ($5,714.29) no están obligados a presentar
liquidación de impuestos; en consecuencia su impuesto será igual a la suma de las retenciones efectuadas
de acuerdo a la tabla respectiva"

Art. 1: "Se consideran sujetos pasivos de la retención, las personas naturales domiciliadas en el país que
perciban rentas gravadas en concepto de remuneraciones por la prestación de servicios de carácter
permanente; ya sea en efectivo o en especie, las que serán afectas a una retención de acuerdo a las
siguientes Tablas"

Art. 2: "...se consideran objetos de retención de Impuesto sobre la Renta, las remuneraciones por la
prestación de servicios de carácter permanente, a partir del día primero de enero de mil novecientos
noventa y dos."

Art. 3: "Derogase en todas sus partes el Decreto Ejecutivo Nº 36 del 20 de diciembre de 1989, publicado en
el Diario Oficial Nº 236, Tomo 305 del mismo día, mes y año."

Art. 4: "El presente Decreto entrará en vigencia a partir del día de su publicación en el Diario Oficial y
será aplicable a partir del 1° de enero de 1992."

Firma: "DADO EN CASA PRESIDENCIAL: San Salvador, a los veintiún días del mes de diciembre de mil novecientos
noventa y uno."
Publicación: "D. O. Nº 1, Tomo 314, del 6 de enero de 1992."
REFORMAS: "(1) D. E. Nº 25, del 18 de febrero de 1992, publicado en el D. O. Nº 34, Tomo 314, del 20 de
febrero de 1992, que sustituye los literales a), b) y c), con vigencia a partir del 1° de marzo de 1992."
```

- **Gloss:** English gloss: retention subjects = resident natural persons earning taxable remuneration for permanent services, in cash or in kind. Context: persons whose income is exclusively permanent remunerations and ≤ ¢50,000/year ($5,714.29) need not file an annual return — their tax equals the sum of withholdings (Art. 38 Ley); filing duty threshold ¢22,000/year ($2,514.29) (Art. 92 Ley). Decree effective on publication (D.O. 6-I-1992), applicable from 1-I-1992; tables a)–c) as printed are the D.E. Nº 25 substitution effective 1-III-1992; repeals D.E. Nº 36 (1989). Old-law instrument under D.L. 134 (Ley ISR 1991).
- **Candidate CRs:** validity dating for bracket data in Odoo (from 1992-03-01 for tables a)–c); "withholding = final tax" rule for low-income employees; decree supersedes-chain metadata (D.E. 36 → D.E. 75 → D.E. 25).
- **Topics:** payroll, taxation, legal-basis.
- **Doubts/xref:** el documento no define base neta vs bruta ni deducciones (OQ-4); tablas son fijadas por decreto (no regeneración anual) — confirmar si existieron reformas posteriores hasta la derogación por la Ley ISR 2000 (OQ-5); xref 03_ Ley ISR Arts. 37, 38, 92.

---

## Open questions (10_Tablas_Retencion_ISR)

- OQ-1: Fila 3 de las tres tablas: el offset marginal impreso ("10% sobre exceso de ¢2,000.00" mensual; ¢1,000.00 quincenal; ¢500.00 semanal) NO coincide con el límite inferior del bracket (¢4,104.17 / ¢2,052.09 / ¢1,026.05) y produce discontinuidad frente a la fila 2 (además la cuota fija ¢41.70 ya aplica en el primer centavo del bracket 2, saltando desde "SIN RETENCION"). El patrón es consistente en las tres tablas, pero ¿es exactamente lo que imprime el D.O. Nº 34 (D.E. Nº 25) original, o error de transcripción del PDF fuente? Verificar contra el D.O. antes de codificar.
- OQ-2: Tabla quincenal, límite bracket 4/5: HASTA ¢8,333.33 vs DESDE ¢8,333.01 se solapan (8,333.01 < 8,333.33) y el $ impreso (952.34) corresponde a ¢8,333.00 (= 16,666.00/2), no a 8,333.33. ¿El HASTA correcto es ¢8,333.00? Verificar D.O. original.
- OQ-3: Tabla semanal, bracket 5 DESDE impreso "¢4,1666.01" [sic] — el equivalente $476.12 indica lectura correcta ¢4,166.01. ¿Confirmar dígito en D.O. original?
- OQ-4: Base de cálculo: el decreto aplica las tablas sobre la "remuneración" sin especificar bruto vs neto ni tratamiento de deducciones (ISSS/AFP no mencionadas). ¿La base es la remuneración bruta? Cruzar con Ley ISR D.L. 134 Arts. 37/38 (fuente 03_) y definir para Odoo. Tampoco define el método de "salario equivalente mensual" del literal d) (¿factor 30 días, 4,33 semanas?).
- OQ-5: Validez y moneda: documento de la Ley ISR de 1991 (D.L. 134) que imprime valores duales ¢/$ a paridad fija 8.75 (¿inserción posterior a la dolarización 2001?). ¿Estas tablas quedaron derogadas/sustituidas por la Ley ISR 2000 y sus tablas posteriores, o siguen vigentes para algún período? Determina si se codifican en Odoo solo como dato histórico datado (vigente 1992-03-01 hasta derogación) — cruzar con 03_/05_ y confirmar cadena de reformas del D.E. Nº 75.
