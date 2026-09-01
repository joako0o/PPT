"""Defensa de Memoria — Pronóstico Jerárquico de Demanda Intermitente.
Construye el PPTX final + previews para revisión visual."""
import os
from engine import (Deck, para, W, H, MX, CW, CT, CB, EYE_Y, TIT_Y, RULE_Y,
                    ROJO, AMAR, AMAR_D, AZUL, AZUL_D, INK, TXT, GRAY, MUT,
                    LIGHT, LIGHT2, LINE, WHITE)

A = "/home/user/work/assets"
F = "/home/user/work/fig"
C = "/home/user/work/charts"

LOGO      = f"{A}/image1.png"
FORMULA   = f"{A}/image5.png"
SKU97     = f"{A}/image3.png"
EVOL      = f"{A}/image4.png"
DEMANDA   = f"{A}/image2.png"
SIMBOLOS  = f"{A}/image6.png"
TABLA51   = f"{A}/image7.png"
HEATMAP   = f"{A}/image8.png"

d = Deck()
n = [0]


def S(eyebrow_num, eyebrow, title, subtitle=None, foot=True):
    n[0] += 1
    s = d.new(number=n[0])
    s.header(eyebrow_num, eyebrow, title, subtitle)
    if foot:
        s.footer()
    return s


def b(t, size=14.2, space_after=7, **kw):
    return para(t, size=size, bullet=True, color=TXT, space_after=space_after, line=1.18, **kw)


# ═══════════════════════════ 1 · PORTADA ═══════════════════════════
n[0] += 1
s = d.new()
s.image(LOGO, (W - 4.6) / 2, 0.95, 4.6, 2.15)
s.text(MX, 3.60, CW, 0.55, [para("Memoria para optar al título de Ingeniero Comercial",
                                 size=25, bold=True, color=INK, align="c", space_after=0)])
s.text(2.0, 4.32, W - 4.0, 1.75,
       [para("“Pronóstico Jerárquico de Demanda Intermitente\nen el Retail de Moda Femenina”",
             size=40, bold=True, color=INK, align="c", space_after=0, line=1.16)])
s.text(2.0, 6.16, W - 4.0, 0.6,
       [para("Un Ensamble Híbrido de Machine Learning con Desacoplamiento Jerárquico",
             size=23, color=GRAY, align="c", space_after=0)])
for i, c in enumerate((ROJO, AMAR, AZUL)):
    s.rect(2.15 + i * 5.15, 7.05, 5.15, 0.10, fill=c)
for i, (rol, nom) in enumerate([("Profesor Guía", "Marcelo Julián Villena Chamorro"),
                                ("Autor", "Joaquín Ignacio Mondaca Parada"),
                                ("Profesora Correferente", "Jocelyn Andrea Tapia Stefanoni")]):
    x = 2.15 + i * 5.15
    s.text(x, 7.62, 5.0, 0.85, [para(rol, size=15, bold=True, color=INK, space_after=4),
                                para(nom, size=15.5, color=GRAY, space_after=0)])
s.text(MX, 9.55, CW, 0.4,
       [para("Universidad Técnica Federico Santa María  ·  Departamento de Ingeniería Comercial  ·  "
             "Campus Vitacura  ·  Santiago de Chile, 2026",
             size=13, color=MUT, align="c", space_after=0)])

# ═══════════════════════════ 2 · AGENDA ═══════════════════════════
s = S("", "", "Hoja de ruta", "Seis bloques: del problema comercial a la evidencia y su impacto financiero.")
items = [("01", "Contexto y problema", "Moda femenina, ciclos ultracortos e intermitencia estructural"),
         ("02", "Pregunta, hipótesis y objetivo", "Qué se pone a prueba y con qué métrica se decide"),
         ("03", "Datos, variables y supuestos", "Núcleo comercial: Top 100 SKUs y 58 familias, 2020–2025"),
         ("04", "Metodología y arquitectura", "Protocolo anti-leakage y las tres capas del ES-GBM"),
         ("05", "Resultados y evidencia", "Benchmark de diez arquitecturas y estudio de ablación"),
         ("06", "Impacto y conclusiones", "Capital de trabajo liberado, límites y trabajo futuro")]
cw, ch, gx, gy = 8.7, 1.92, 0.5, 0.44
for i, (num, tit, des) in enumerate(items):
    x = MX + (i % 2) * (cw + gx)
    y = 3.15 + (i // 2) * (ch + gy)
    s.rect(x, y, cw, ch, fill=LIGHT, radius=0.06)
    s.rect(x, y, 0.075, ch, fill=(ROJO, AMAR, AZUL)[i // 2])
    s.text(x + 0.45, y, 1.3, ch, [para(num, size=34, bold=True, color=(ROJO, AMAR_D, AZUL)[i // 2],
                                       space_after=0, line=1.0)], valign="m")
    s.text(x + 1.85, y, cw - 2.3, ch, [para(tit, size=18.5, bold=True, color=INK, space_after=5),
                                       para(des, size=13.5, color=GRAY, space_after=0, line=1.2)], valign="m")

# ═══════════════════════════ 3 · CONTEXTO ═══════════════════════════
s = S("01", "CONTEXTO Y PROBLEMA", "La moda femenina decide hoy lo que venderá en seis meses")
cards = [("Ciclos de vida ultracortos",
          "Colecciones de 2 a 3 meses: la serie histórica de un SKU casi nunca alcanza a madurar antes de que el producto salga del catálogo."),
         ("La demanda la dirige el plan comercial",
          "Precio, descuento y campañas mueven el volumen mensual con más fuerza que la inercia histórica de la serie."),
         ("Compromisos con 3 a 6 meses de anticipación",
          "Las órdenes a fábrica se cierran antes de observar la demanda: equivocarse tarde se paga en inventario o en venta perdida.")]
for i, (t, txt) in enumerate(cards):
    y = CT + i * 2.55
    s.card(MX, y, 8.25, 2.3, t, [para(txt, size=14, color=TXT, space_after=0, line=1.24)],
           accent=(ROJO, AMAR, AZUL)[i], tsize=17.5)
s.rect(9.65, CT, 9.3, 5.35, fill=WHITE, line=LINE, radius=0.06)
s.image(DEMANDA, 10.0, CT + 0.32, 8.6, 4.7)
s.caption(9.65, CT + 5.45, 9.3, "Demanda agregada mensual del núcleo comercial (Top 100 SKUs), 2020–2025.")
for i, (lab, val) in enumerate([("Primavera", "31 %"), ("Verano", "25 %"), ("Invierno", "23 %"), ("Otoño", "21 %")]):
    x = 9.65 + i * 2.36
    s.rect(x, 8.42, 2.2, 1.05, fill=WHITE, line=LINE, radius=0.05)
    s.text(x, 8.42, 2.2, 1.05, [para(val, size=20, bold=True, color=AZUL, align="c", space_after=1),
                                para(lab, size=12, color=GRAY, align="c", space_after=0)], valign="m")
s.caption(9.65, 9.55, 9.3, "Participación de cada estación en la demanda anual (waffle, anexo A6).")

# ═══════════════════════════ 4 · EL PROBLEMA ═══════════════════════════
s = S("01", "CONTEXTO Y PROBLEMA", "Series que prenden y se apagan: demanda intermitente")
s.stat(MX, CT, 7.5, 2.15, "30,3 %", "de los pares SKU–mes no registran ninguna venta",
       color=ROJO, note="Ceros estructurales, no ruido aleatorio")
s.card(MX, CT + 2.42, 7.5, 2.35, "Por qué rompe a los modelos clásicos",
       [para("Croston y SBA asumen intermitencia sin estacionalidad; SARIMA asume continuidad. "
             "En moda conviven las tres cosas: ceros, estacionalidad fuerte y shocks promocionales.",
             size=14, color=TXT, space_after=0, line=1.24)], accent=AZUL, tsize=17)
s.card(MX, CT + 5.05, 7.5, 2.5, "El dilema que hay detrás",
       [b("Sobre-stock: inmoviliza capital de trabajo y fuerza liquidaciones que erosionan el margen."),
        b("Quiebre: destruye ingreso directo y deteriora la fidelidad del cliente.", space_after=0)],
       accent=ROJO, tsize=17)
s.rect(8.85, CT, 10.1, 6.55, fill=WHITE, line=LINE, radius=0.06)
s.image(HEATMAP, 9.2, CT + 0.3, 9.4, 5.95)
s.caption(8.85, CT + 6.65, 10.1,
          "Matriz de demanda: 100 SKUs × 66 meses. Las zonas claras son meses sin venta.")
s.banner(8.85, 9.15, 10.1, 0.87,
         "Cada punto de error se paga dos veces: en capital inmovilizado y en venta perdida.",
         fill=AZUL, size=15.5)

# ═══════════════════════════ 5 · PREGUNTA E HIPÓTESIS ═══════════════════════════
s = S("02", "PREGUNTA, HIPÓTESIS Y OBJETIVO", "Qué se pone a prueba")
s.card(MX, CT, CW, 1.95, "Pregunta de investigación",
       [para("¿Cuál enfoque de modelado —clásicos univariados, causales, redes recurrentes, modelos "
             "fundacionales pre-entrenados o arquitecturas híbridas de ensamble jerárquico— alcanza la mayor "
             "capacidad predictiva y robustez metodológica para pronosticar la demanda de retail de moda en "
             "Chile, evaluado mediante WAPE en un horizonte mensual h = 1?",
             size=14.5, color=TXT, space_after=0, line=1.26)], accent=ROJO)
s.card(MX, CT + 2.2, 8.7, 2.15, "H₀  ·  hipótesis nula",
       [para("El WAPE esperado de la arquitectura ES-GBM no es inferior al de los benchmarks primarios "
             "(SARIMA, SARIMAX y LSTM).", size=14.5, color=TXT, space_after=0, line=1.26)],
       accent=MUT, fill=LIGHT2)
s.card(MX + 9.2, CT + 2.2, 8.7, 2.15, "H₁  ·  hipótesis de trabajo",
       [para("El WAPE esperado de la arquitectura ES-GBM es inferior al de los benchmarks primarios de "
             "referencia.", size=14.5, color=TXT, space_after=0, line=1.26)], accent=AZUL)
s.card(MX, CT + 4.6, CW, 1.95, "Objetivo general",
       [para("Desarrollar y evaluar una arquitectura de pronóstico jerárquica de ensamble (ES-GBM con "
             "desacoplamiento jerárquico a nivel SKU) para el retail de moda femenina en Chile, que minimice "
             "el error de predicción integrando variables comerciales ex-ante y suavizamiento exponencial, "
             "con el fin de optimizar la eficiencia del capital de trabajo.",
             size=14.5, color=TXT, space_after=0, line=1.26)], accent=AMAR)
s.banner(MX, CT + 6.85, CW, 0.85,
         "Benchmarks primarios: SARIMA · SARIMAX · LSTM      |      Referencias de frontera: "
         "Croston · SBA · Seasonal Naïve · Chronos-Bolt", fill=LIGHT2, color=TXT, size=14.5, bold=False)

# ═══════════════════════════ 6 · DATOS Y ALCANCE ═══════════════════════════
s = S("03", "DATOS, VARIABLES Y SUPUESTOS", "El núcleo comercial: dónde se juega el margen")
chips = [("Top 100", "SKUs modelados a nivel producto", AZUL),
         ("58", "familias comerciales activas", AZUL),
         ("72 %", "del volumen físico de la cadena", ROJO),
         ("78 %", "del margen de contribución", ROJO)]
for i, (v, l, col) in enumerate(chips):
    s.stat(MX + i * 4.53, CT, 4.28, 1.95, v, l, color=col, vsize=40, lsize=13)
s.card(MX, CT + 2.25, 7.4, 5.3, "Jerarquía de agregación", None, accent=AZUL)
levels = [("Departamento", "3 superfamilias"), ("Familia", "58 series agregadas"),
          ("Sub-familia", "agrupación intermedia"), ("SKU", "Top 100 productos")]
for i, (lv, det) in enumerate(levels):
    y = CT + 3.05 + i * 1.12
    s.rect(MX + 0.5, y, 6.4, 0.82, fill=WHITE, line=LINE, radius=0.08)
    s.text(MX + 0.85, y, 3.0, 0.82, [para(lv, size=15, bold=True, color=INK, space_after=0)], valign="m")
    s.text(MX + 3.6, y, 3.0, 0.82, [para(det, size=12.5, color=GRAY, align="r", space_after=0)], valign="m")
    if i < 3:
        s.arrow(MX + 3.7, y + 0.84, MX + 3.7, y + 1.08, color=MUT, lw=1.4)
s.card(MX + 7.9, CT + 2.25, 10.0, 5.3, "Origen y ventana de los datos",
       [b("Registros POS reales de una cadena líder de moda femenina en Chile (“Empresa X”), "
          "segmento premium-mass market."),
        b("66 meses de historia mensual, 2020–2025; catálogo activo de 1.457 SKUs en 3 superfamilias "
          "y 58 familias."),
        b("El Top 100 se define únicamente con datos previos al corte de calibración: la selección "
          "no mira el período de prueba."),
        b("Regla ex-ante para familias descontinuadas y regularización de la grilla temporal "
          "(zero-filling) antes de agregar."),
        b("Granularidad mensual: la unidad de decisión de compra y reposición de la cadena."),
        b("Variable objetivo: unidades vendidas; el monto neto se usa para ponderar el impacto "
          "financiero de cada familia.", space_after=0)])

# ═══════════════════════════ 7 · VARIABLES ═══════════════════════════
s = S("03", "DATOS, VARIABLES Y SUPUESTOS", "Variables del modelo")
vcards = [("Target e identificación", ROJO,
           ["Venta cantidad — variable objetivo",
            "Venta monto neto — ponderación financiera",
            "Jerarquía: departamento, familia, sub-familia y SKU",
            "Mes calendario"]),
          ("Plan comercial ex-ante", AMAR,
           ["Precio promedio proyectado del mes t",
            "Descuento comercial promedio planificado",
            "Son decisiones de la empresa: se conocen antes de que ocurra la demanda",
            "Constituyen la señal predictiva más potente del ensamble"]),
          ("Temporales y de rezago", AZUL,
           ["Demanda rezagada y estadísticas móviles de 12 meses",
            "Estacionalidad armónica (seno y coseno del mes)",
            "Días de venta efectiva del período",
            "Variación porcentual de la demanda en t−1"])]
for i, (t, col, bs) in enumerate(vcards):
    s.card(MX + i * 6.08, CT, 5.73, 4.3, t, [b(x, size=14.8, space_after=13) for x in bs],
           accent=col, tsize=17.5)
s.banner(MX, CT + 4.65, CW, 2.2,
         "Regla de oro anti-leakage: toda variable usa información disponible en t−1, salvo el plan comercial "
         "que la propia empresa fija ex-ante. Pruebas automatizadas sobre rezagos verifican que ninguna "
         "variable filtre información del futuro.", fill=AZUL, size=17)

# ═══════════════════════════ 8 · SUPUESTOS ═══════════════════════════
s = S("03", "DATOS, VARIABLES Y SUPUESTOS", "Supuestos y consideraciones relevantes")
s.card(MX, CT, 8.75, 3.2, "Supuestos base",
       [b("Venta cero con inventario disponible se interpreta como demanda cero."),
        b("Precio y descuento son conocidos ex-ante por la planificación comercial."),
        b("El target son ventas observadas en POS, no demanda latente no censurada.", space_after=0)],
       accent=ROJO)
s.card(MX + 9.15, CT, 8.75, 3.2, "Foco estratégico",
       [b("Se modela el núcleo comercial: Top 100 SKUs y 58 familias activas."),
        b("Concentra 72 % del volumen y 78 % del margen: máximo impacto financiero por unidad de esfuerzo."),
        b("La cola larga (1.357 SKUs de baja rotación) se plantea como trabajo futuro.", space_after=0)],
       accent=AZUL)
s.card(MX, CT + 3.5, 8.75, 3.35, "Qué implica al leer los resultados",
       [b("Ante quiebres de stock la venta observada se trunca: se pronostica demanda orgánica bajo las "
          "condiciones de disponibilidad históricas."),
        b("No se capturan liquidaciones reactivas intramensuales (mark-downs de emergencia de última "
          "semana).", space_after=0)], accent=AMAR)
s.card(MX + 9.15, CT + 3.5, 8.75, 3.35, "Asimetría metodológica declarada",
       [b("Las líneas base econométricas usan una parametrización global parsimoniosa estándar "
          "(1,1,1)×(1,1,1) con período estacional 12, sin selección de órdenes por SKU."),
        b("La arquitectura propuesta sí contó con ingeniería de variables y calibración por fases: "
          "esto debe considerarse al interpretar la magnitud del diferencial.", space_after=0)],
       accent=INK)
s.banner(MX, CT + 7.15, CW, 0.85,
         "Declarar los supuestos por adelantado es lo que permite interpretar correctamente la magnitud "
         "de los resultados.", fill=LIGHT2, color=TXT, size=15, bold=False)

# ═══════════════════════════ 9 · MÉTRICA ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "WAPE: la métrica que resiste la demanda cero")
s.rect(MX, CT, 8.6, 3.4, fill=WHITE, line=LINE, radius=0.06)
s.image(FORMULA, MX + 0.9, CT + 0.4, 6.8, 2.6)
s.card(MX, CT + 3.7, 8.6, 3.85, "Por qué WAPE y no MAPE",
       [b("El MAPE divide por la demanda de cada mes: con ceros o valores unitarios pequeños se "
          "indetermina o explota."),
        b("El WAPE agrega errores y volumen antes de dividir: pondera por unidades físicas y refleja "
          "el impacto operacional real."),
        b("Ejemplo del propio benchmark: SARIMA obtiene sMAPE 309,88 % frente a un WAPE de 76,74 %; "
          "SARIMAX, 170,87 % frente a 73,24 %.", space_after=0)], accent=AZUL)
s.rect(MX + 9.15, CT, 8.75, 5.6, fill=WHITE, line=LINE, radius=0.06)
s.image(SIMBOLOS, MX + 9.5, CT + 0.28, 8.05, 5.04)
s.card(MX + 9.15, CT + 5.9, 8.75, 1.65, "Métricas complementarias",
       [para("RMSE, MAE, sesgo y R² acompañan la evaluación; el WRMSSE (0,2017) da comparabilidad con el "
             "marco de la competencia M5.", size=13.8, color=TXT, space_after=0, line=1.22)],
       accent=AMAR, tsize=16, pad=0.34)

# ═══════════════════════════ 10 · PROTOCOLO ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Protocolo de validación: 80 / 10 / 10 cronológico")
segs = [("Entrenamiento", "80 %", 0.80, "D8DEE4", INK),
        ("Validación", "10 %", 0.10, AMAR, INK),
        ("Prueba ciega", "10 %", 0.10, AZUL, WHITE)]
x = MX
for name, pct, frac, col, tcol in segs:
    w = CW * frac
    s.rect(x, 3.35, w - 0.06, 1.15, fill=col, radius=0.05)
    s.text(x, 3.35, w - 0.06, 1.15, [para(pct, size=19, bold=True, color=tcol, align="c", space_after=0)],
           valign="m")
    s.text(x, 2.95, w - 0.06, 0.35, [para(name, size=14.5, bold=True, color=INK, align="c", space_after=0)])
    x += w
s.text(MX, 4.62, CW * 0.8, 0.35, [para("Enero 2020  →  corte de calibración: enero 2025", size=13,
                                       color=GRAY, space_after=0)])
s.text(MX + CW - 6.0, 4.62, 6.0, 0.35, [para("Febrero – agosto 2025  ·  7 meses fuera de muestra",
                                             size=13, color=AZUL, bold=True, align="r", space_after=0)])
tcards = [("Entrenamiento", "Aprende los patrones históricos de nivel, estacionalidad y respuesta comercial.", ROJO),
          ("Validación", "Calibra pesos NNLS del ensamble y el umbral de ruteo τ* sin observar el futuro.", AMAR),
          ("Prueba ciega", "Siete meses evaluados con pesos congelados: simula un despliegue real.", AZUL)]
for i, (t, txt, col) in enumerate(tcards):
    s.card(MX + i * 6.08, 5.5, 5.73, 2.35, t, [para(txt, size=14, color=TXT, space_after=0, line=1.24)],
           accent=col, tsize=17)
s.banner(MX, 8.15, CW, 1.6,
         "En series de tiempo el orden temporal es innegociable: partición estrictamente cronológica, rezagos "
         "seguros en t−1 y pesos congelados desde el corte. Cualquier aleatorización filtraría el futuro hacia "
         "el pasado.", fill=AZUL, size=15.5)

# ═══════════════════════════ 11 · BATERÍA DE MODELOS ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Diez arquitecturas, un mismo protocolo",
      "Desde la heurística estacional de 1970 hasta los modelos fundacionales pre-entrenados de 2024.")
s.rect(3.35, 3.05, 13.3, 6.15, fill=WHITE, line=LINE, radius=0.06)
s.image(EVOL, 3.75, 3.35, 12.5, 5.55)
s.banner(MX, 9.35, CW, 0.67,
         "Todas las referencias se evalúan sobre la misma ventana, la misma jerarquía y la misma métrica: "
         "la comparación es una decisión de diseño, no un accidente.", fill=LIGHT2, color=TXT, size=14.5,
         bold=False)

# ═══════════════════════════ 12 · ARQUITECTURA ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Arquitectura ES-GBM: tres capas, tres problemas distintos")
s.pill((W - 10.5) / 2, CT, 10.5, 0.72, "Demanda mensual agregada  ·  58 familias comerciales (2020–2025)",
       fill=INK, size=15)
layers = [("CAPA 1", "Desacoplamiento estructural", ROJO,
           ["Holt amortiguado sobre la serie de familia",
            "Extrae nivel, tendencia e inercia estacional",
            "La señal continua y predecible de la categoría"]),
          ("CAPA 2", "Residuos comerciales", AMAR_D,
           ["Ensamble GBDT: XGBoost · LightGBM · CatBoost",
            "Modelo fundacional tabular TabPFN",
            "Escala arcsinh y ponderación con decay de 24 meses",
            "Aquí entran precio y descuento ex-ante"]),
          ("CAPA 3", "Integración y desagregación", AZUL,
           ["Ponderación NNLS + ruteo por momentum: umbral τ* entre 1,05 y 1,50",
            "Desagregación top-down con proporciones históricas",
            "Coherencia jerárquica exacta: las cuotas suman 1"])]
cw2, gap = 5.6, 0.55
for i, (num, tit, col, bs) in enumerate(layers):
    x = MX + i * (cw2 + gap)
    y, hh = 3.62, 4.5
    s.rect(x, y, cw2, hh, fill=LIGHT, radius=0.06)
    s.rect(x, y, cw2, 0.62, fill=col, radius=0.06)
    s.rect(x, y + 0.35, cw2, 0.27, fill=col)
    s.text(x, y, cw2, 0.62, [para(num, size=14, bold=True, color=WHITE, align="c", space_after=0, spc=2)],
           valign="m")
    s.text(x + 0.42, y + 0.85, cw2 - 0.84, 0.6,
           [para(tit, size=17.5, bold=True, color=INK, space_after=0, line=1.1)])
    s.text(x + 0.42, y + 1.62, cw2 - 0.84, hh - 2.0, [b(t, size=13.6, space_after=8) for t in bs])
    if i < 2:
        s.arrow(x + cw2 + 0.08, y + hh / 2, x + cw2 + gap - 0.08, y + hh / 2, color=MUT, lw=2)
s.text(MX + cw2 + 0.02, 8.25, gap + 0.1, 0.3, [para("residuos", size=11, color=MUT, align="c", space_after=0)])
s.text(MX + 2 * cw2 + gap + 0.02, 8.25, gap + 0.1, 0.3,
       [para("blend", size=11, color=MUT, align="c", space_after=0)])
s.pill((W - 12.0) / 2, 8.62, 12.0, 0.74,
       "Pronóstico mensual por SKU  ·  Top 100 productos  ·  WAPE 16,10 %", fill=AZUL, size=15.5)
s.text(MX, 9.55, CW, 0.4,
       [para("Cada capa resuelve un problema distinto: inercia → comercialidad → intermitencia.",
             size=14, color=GRAY, align="c", space_after=0, italic=True)])

# ═══════════════════════════ 13 · CAPA 1 ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Capa 1  ·  Desacoplamiento estructural")
c1 = [("Objetivo", ROJO, "Capturar la inercia, el nivel base y la estacionalidad estructural de cada una "
                         "de las 58 familias comerciales, donde la serie es continua y tiene señal."),
      ("Método", AMAR, "Suavizamiento exponencial Holt amortiguado. El amortiguamiento frena la "
                       "extrapolación de la tendencia y evita proyecciones explosivas en horizontes largos."),
      ("Qué delega", AZUL, "Todo evento disruptivo —promociones, liquidaciones, campañas— queda deliberadamente "
                           "en el residuo, para que lo explique la Capa 2 con información comercial.")]
for i, (t, col, txt) in enumerate(c1):
    s.card(MX + i * 6.08, CT, 5.73, 2.95, t, [para(txt, size=14.5, color=TXT, space_after=0, line=1.26)],
           accent=col, tsize=18)
s.card(MX, CT + 3.25, CW, 2.15, "Por qué empezar por aquí",
       [para("Pedirle a un árbol de decisión que aprenda el nivel de una serie es gastar capacidad de modelo "
             "en algo que una ecuación de suavizamiento hace mejor y con menos varianza. Al retirar el nivel, "
             "el problema que queda —el residuo— es justamente donde la información comercial es decisiva.",
             size=15, color=TXT, space_after=0, line=1.28)], accent=INK)
s.banner(MX, CT + 5.75, CW, 1.15,
         "Resultado de la capa: una señal base estable sobre la que el aprendizaje automático solo tiene que "
         "explicar desviaciones.", fill=LIGHT2, color=TXT, size=15, bold=False)

# ═══════════════════════════ 14 · CAPA 2 ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Capa 2  ·  Proyección de residuos comerciales")
s.card(MX, CT, 8.6, 2.5, "El objetivo",
       [para("Modelar el residuo de la Capa 1: la parte de la demanda que la inercia no explica. Ahí es "
             "donde vive el efecto de las palancas comerciales sobre la venta.",
             size=14.5, color=TXT, space_after=0, line=1.26)], accent=ROJO)
s.card(MX + 9.3, CT, 8.6, 2.5, "Las palancas que entran al modelo",
       [b("Precio promedio proyectado ex-ante del mes t"),
        b("Descuento comercial planificado"),
        b("Rezagos, ventanas móviles y estacionalidad armónica", space_after=0)], accent=AMAR)
s.text(MX, CT + 2.85, CW, 0.42, [para("BANCO DE MODELOS DEL ENSAMBLE", size=13, bold=True, color=GRAY,
                                      space_after=0, spc=2.2)])
models = [("XGBoost", "boosting por gradiente"), ("LightGBM", "boosting histogramado"),
          ("CatBoost", "boosting ordenado"), ("TabPFN", "modelo fundacional tabular")]
for i, (m, det) in enumerate(models):
    x = MX + i * 4.53
    s.rect(x, CT + 3.35, 4.28, 1.6, fill=LIGHT, line=LINE, radius=0.06)
    s.text(x, CT + 3.35, 4.28, 1.6, [para(m, size=18, bold=True, color=AZUL, align="c", space_after=3),
                                     para(det, size=12.5, color=GRAY, align="c", space_after=0)], valign="m")
s.card(MX, CT + 5.25, CW, 2.3, "Tratamiento numérico",
       [para("Los residuos se modelan en escala arcsinh —que absorbe magnitudes extremas sin descartar el "
             "signo— con ponderación temporal decreciente (decay de 24 meses) para privilegiar el "
             "comportamiento comercial reciente. Modelos distintos fallan distinto: el ensamble promedia "
             "errores no correlacionados.", size=14.2, color=TXT, space_after=0, line=1.24)], accent=AZUL)

# ═══════════════════════════ 15 · CAPA 3 ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Capa 3  ·  Integración y desagregación jerárquica")
c3 = [("Ruteo dinámico por momentum", ROJO,
       "Los pesos del ensamble se optimizan por NNLS en validación. Si el momentum trimestral de la familia "
       "supera el umbral τ* (calibrado entre 1,05 y 1,50), el sistema conmuta hacia el componente de aprendizaje automático; "
       "si la categoría está estable, pesa más la señal inercial."),
      ("Desagregación top-down", AMAR,
       "La predicción de familia se reparte a cada SKU con proporciones históricas del período de "
       "entrenamiento, garantizando coherencia jerárquica exacta: las partes suman el total."),
      ("Por qué resuelve la intermitencia", AZUL,
       "Arriba, la serie agregada es continua y tiene estacionalidad clara; abajo, el reparto proporcional "
       "distribuye ese pronóstico limpio. El 30,3 % de ceros deja de ser un problema de modelado.")]
for i, (t, col, txt) in enumerate(c3):
    s.card(MX + i * 6.08, CT, 5.73, 3.45, t, [para(txt, size=14.3, color=TXT, space_after=0, line=1.26)],
           accent=col, tsize=17.5)
s.card(MX, CT + 3.75, CW, 2.0, "Decisión experimental documentada",
       [para("Se probó también una desagregación supervisada con cuotas dinámicas aprendidas (learned "
             "shares): obtuvo 24,35 % de WAPE frente al 16,10 % del reparto estático. En catálogos muy "
             "intermitentes, la estabilidad de las proporciones históricas vence a la sofisticación.",
             size=14.5, color=TXT, space_after=0, line=1.26)], accent=INK)
s.banner(MX, CT + 6.05, CW, 1.0,
         "Pronosticar bien la familia y repartir bien el SKU venció a todos los modelos que pronostican "
         "el SKU directamente.", fill=AZUL, size=15.5)

# ═══════════════════════════ 16 · BENCHMARK ═══════════════════════════
s = S("05", "RESULTADOS Y EVIDENCIA", "Benchmark fuera de muestra: febrero – agosto 2025")
s.rect(MX, CT, 11.4, 7.05, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{C}/benchmark_sku.png", MX + 0.25, CT + 0.25, 10.9, 6.55)
s.card(MX + 11.8, CT, 6.1, 3.05, "Lectura de resultados",
       [b("El ES-GBM reduce el error a menos de un cuarto de la mejor referencia clásica.", size=13.8),
        b("Supera también a la red LSTM y al modelo fundacional Chronos-Bolt.", size=13.8),
        b("Croston y SBA fallan por diseño: ignoran la estacionalidad.", size=13.8, space_after=0)],
       accent=AZUL, tsize=17)
s.rect(MX + 11.8, CT + 3.35, 6.1, 3.7, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{C}/benchmark_familia.png", MX + 12.0, CT + 3.5, 5.7, 3.4)
s.caption(MX, CT + 7.2, CW,
          "WAPE fuera de muestra sobre 7 meses de prueba ciega. Detalle completo de métricas en el anexo A1.")

# ═══════════════════════════ 17 · CALIDAD DEL AJUSTE ═══════════════════════════
s = S("05", "RESULTADOS Y EVIDENCIA", "Calidad del ajuste: el pronóstico sigue a la demanda real")
s.rect(MX, CT, 11.4, 6.2, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{F}/fig5_3.png", MX + 0.3, CT + 0.3, 10.8, 5.6)
s.caption(MX, CT + 6.35, 11.4, "Suma mensual del Top 100 SKUs: demanda observada vs. pronóstico ES-GBM.")
stats = [("16,10 %", "WAPE a nivel SKU", AZUL), ("12,89 %", "WAPE a nivel familia", AZUL),
         ("0,95 / 0,96", "R² SKU y familia", ROJO), ("−4,8 %", "sesgo medio del pronóstico", ROJO)]
for i, (v, l, col) in enumerate(stats):
    x = MX + 11.8 + (i % 2) * 3.15
    y = CT + (i // 2) * 1.85
    s.stat(x, y, 2.95, 1.65, v, l, color=col, vsize=27, lsize=12.5, align="c")
s.card(MX + 11.8, CT + 3.85, 6.1, 3.4, "Qué dice esto",
       [b("R² de 0,95 a nivel SKU: la arquitectura explica casi toda la varianza de la demanda.", size=13.8),
        b("Sesgo levemente negativo (−4,8 %): el modelo sub-predice de forma sistemática y corregible.", size=13.8),
        b("WRMSSE de 0,2017, comparable con el marco de la competencia M5.", size=13.8, space_after=0)],
       accent=AZUL, tsize=17)

# ═══════════════════════════ 18 · ABLACIÓN ═══════════════════════════
s = S("05", "RESULTADOS Y EVIDENCIA", "Ablación: la demanda no es estocástica, la dirige el plan comercial")
s.rect(MX, CT, 8.6, 6.1, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{C}/ablation.png", MX + 0.3, CT + 0.3, 8.0, 5.5)
s.caption(MX, CT + 6.25, 8.6, "WAPE a nivel SKU según la información de precios disponible.")
s.rect(MX + 9.3, CT, 8.6, 4.2, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{F}/fig5_4.png", MX + 9.55, CT + 0.25, 8.1, 3.7)
s.caption(MX + 9.3, CT + 4.35, 8.6, "Importancia por ganancia total del módulo GBDT.")
s.card(MX + 9.3, CT + 4.85, 8.6, 2.7, "Dos lecturas, una advertencia",
       [b("El precio ex-ante concentra el 67,0 % de la ganancia total del submodelo GBDT.", size=13.8),
        b("Aun sin precios (38,25 %), la arquitectura supera a SARIMA (76,74 %) y SBA (83,42 %): la base "
          "estructural aporta por sí sola.", size=13.8),
        b("La importancia por ganancia no es una estimación causal de la elasticidad precio.",
          size=13.8, space_after=0)], accent=AMAR, tsize=17)

# ═══════════════════════════ 19 · IMPACTO FINANCIERO ═══════════════════════════
s = S("06", "IMPACTO Y CONCLUSIONES", "Del error de pronóstico al capital de trabajo")
fin = [("$105,6M", "CLP de capital de trabajo liberado", "efecto nivel, en balance", AZUL),
       ("$23,2M", "CLP de ahorro anual recurrente", "holding costs, i = 22 % anual", AZUL),
       ("7.041", "unidades de stock de seguridad liberadas", "CSL 95 %, lead time de 1 mes", ROJO)]
for i, (v, l, note, col) in enumerate(fin):
    s.stat(MX + i * 6.08, CT, 5.73, 2.15, v, l, color=col, vsize=38, lsize=13.5, note=note)
s.rect(MX, CT + 2.45, 8.6, 5.1, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{C}/inventario.png", MX + 0.3, CT + 2.7, 8.0, 4.6)
s.card(MX + 9.3, CT + 2.45, 8.6, 2.35, "Sensibilidad del escenario",
       [b("Rango conservador–exigente: $84,5M a $126,8M CLP de capital liberado.", size=13.8),
        b("Ahorro anual entre $15,2M y $33,0M CLP según costo de reposición y tasa de mantención.",
          size=13.8, space_after=0)], accent=AMAR, tsize=17)
s.card(MX + 9.3, CT + 4.95, 8.6, 2.6, "Escala y honestidad metodológica",
       [b("Con aprovisionamiento marítimo (L = 4 meses) el buffer liberado escala a 14.082 unidades.", size=13.8),
        b("Ejercicio ilustrativo de orden de magnitud: usa el MAE como proxy de dispersión (sigma aprox. 1,25 × MAE).",
          size=13.8, space_after=0)], accent=INK, tsize=17)

# ═══════════════════════════ 20 · CONCLUSIONES ═══════════════════════════
s = S("06", "IMPACTO Y CONCLUSIONES", "Conclusiones")
concl = [("01", "La evidencia respalda H₁", ROJO,
          "16,10 % de WAPE a nivel SKU y 12,89 % a nivel familia (R² 0,95 y 0,96), frente a errores "
          "superiores al 69 % en todas las referencias clásicas y al 45 % en las redes recurrentes."),
         ("02", "La demanda del fast fashion es dirigida", AMAR_D,
          "El plan comercial ex-ante reduce el error 22,2 puntos porcentuales. Sin señales de precio el "
          "error casi se duplica: 38,25 % frente a 16,10 %."),
         ("03", "El desacoplamiento jerárquico vence a la intermitencia", AZUL,
          "Pronosticar donde la señal es continua y repartir hacia abajo resultó superior a modelar el SKU "
          "directamente, incluso con cuotas aprendidas."),
         ("04", "El ensamble híbrido supera a los enfoques puros", INK,
          "Estadística para el nivel, aprendizaje automático para el residuo comercial y ruteo adaptativo "
          "según el estado de la categoría: cada componente hace lo que mejor sabe.")]
for i, (num, tit, col, txt) in enumerate(concl):
    x = MX + (i % 2) * 9.15
    y = CT + (i // 2) * 2.75
    s.rect(x, y, 8.75, 2.5, fill=LIGHT, radius=0.06)
    s.rect(x, y, 0.075, 2.5, fill=col)
    s.text(x + 0.45, y + 0.36, 1.1, 0.6, [para(num, size=25, bold=True, color=col, space_after=0, line=1.0)])
    s.text(x + 1.75, y + 0.34, 6.6, 1.9, [para(tit, size=17, bold=True, color=INK, space_after=7, line=1.1),
                                          para(txt, size=13.6, color=TXT, space_after=0, line=1.22)])
s.banner(MX, CT + 5.75, CW, 1.8,
         "La contribución no es un algoritmo nuevo, sino una arquitectura que asigna cada problema —inercia, "
         "comercialidad e intermitencia— al método que mejor lo resuelve, bajo un protocolo que impide que el "
         "resultado se explique por fuga de información.", fill=AZUL, size=16)

# ═══════════════════════════ 21 · LIMITACIONES Y FUTURO ═══════════════════════════
s = S("06", "IMPACTO Y CONCLUSIONES", "Limitaciones y trabajo futuro")
s.card(MX, CT, 8.75, 5.5, "Limitaciones reconocidas",
       [b("Horizonte h = 1 mensual: la industria con abastecimiento marítimo requiere extender la evaluación a 3 y 6 meses."),
        b("Validez externa: un solo retailer del segmento premium-mass market en Chile."),
        b("La ventana de prueba incluye el peak de mayo, pero excluye noviembre–diciembre, el período de "
          "mayor presión promocional."),
        b("El target son ventas observadas: los quiebres truncan la demanda latente."),
        b("Pesos y umbrales congelados desde el corte: la frecuencia óptima de reentrenamiento queda abierta."),
        b("El ejercicio financiero es ilustrativo, con MAE como proxy de dispersión.", space_after=0)],
       accent=ROJO)
s.card(MX + 9.15, CT, 8.75, 5.5, "Líneas de trabajo futuro",
       [b("Fine-tuning de modelos fundacionales (Chronos, TimesFM) incorporando exógenas comerciales; el "
          "zero-shot ya alcanzó 36,35 % a nivel familia."),
        b("Arquitecturas híbridas de deep learning y modelos tabulares en la etapa de desagregación de cuotas."),
        b("Desempeño diferencial por perfil de SKU: asignar el método según rotación, intermitencia y "
          "sensibilidad al precio, en lugar de una arquitectura única."),
        b("Extensión a la cola larga del catálogo (1.357 SKUs de baja rotación)."),
        b("Integración del pronóstico al proceso de S&OP y a la política de compra internacional.",
          space_after=0)], accent=AZUL)
s.banner(MX, CT + 5.85, CW, 1.7,
         "Declarar los límites con precisión es parte del resultado: define hasta dónde puede extrapolarse "
         "la evidencia y qué preguntas quedan abiertas para la siguiente iteración.", fill=AZUL, size=16.5)

# ═══════════════════════════ 22 · CIERRE ═══════════════════════════
n[0] += 1
s = d.new()
s.image(LOGO, (W - 3.4) / 2, 1.5, 3.4, 1.57)
s.text(MX, 3.75, CW, 1.4, [para("Gracias", size=62, bold=True, color=INK, align="c", space_after=0)])
for i, c in enumerate((ROJO, AMAR, AZUL)):
    s.rect(6.6 + i * 2.28, 5.45, 2.28, 0.10, fill=c)
s.text(MX, 5.95, CW, 0.6, [para("Preguntas y comentarios", size=24, color=GRAY, align="c", space_after=0)])
s.text(MX, 7.15, CW, 1.4,
       [para("Joaquín Ignacio Mondaca Parada", size=19, bold=True, color=INK, align="c", space_after=6),
        para("Memoria para optar al título de Ingeniero Comercial  ·  Universidad Técnica Federico Santa María",
             size=14.5, color=GRAY, align="c", space_after=4),
        para("Profesor guía: Marcelo Julián Villena Chamorro  ·  Profesora correferente: Jocelyn Andrea Tapia Stefanoni",
             size=14.5, color=GRAY, align="c", space_after=0)])
s.text(MX, 9.35, CW, 0.4, [para("Los anexos que siguen respaldan las preguntas del jurado.",
                                size=13, color=MUT, align="c", space_after=0, italic=True)])

# ═══════════════════════════ ANEXOS ═══════════════════════════
def ANEXO(code, title, subtitle=None):
    n[0] += 1
    sl = d.new(number=n[0])
    sl.header(f"ANEXO {code}", "", title, subtitle)
    sl.footer("Material de respaldo  ·  Defensa de memoria")
    return sl


s = ANEXO("A1", "Comparativa consolidada de desempeño (Tabla 5.1)")
s.rect(MX, CT, CW, 6.7, fill=WHITE, line=LINE, radius=0.06)
s.image(TABLA51, MX + 0.4, CT + 0.3, 17.1, 6.1)
s.caption(MX, CT + 6.85, CW, "Métricas completas fuera de muestra (feb–ago 2025) para los diez modelos "
                             "evaluados, en los niveles SKU y familia.")

s = ANEXO("A2", "Pronóstico vs. demanda real por modelo")
s.rect(MX, CT, CW, 6.9, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{F}/fig5_1.png", MX + 0.4, CT + 0.3, 17.1, 6.3)
s.caption(MX, CT + 7.05, CW, "Seis arquitecturas representativas contra la demanda observada del Top 100 "
                             "SKUs en la ventana de prueba.")

s = ANEXO("A3", "Diagnóstico de residuos del modelo propuesto")
s.rect(MX, CT, CW, 4.6, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{F}/fig5_5.png", MX + 0.4, CT + 0.3, 17.1, 4.0)
s.card(MX, CT + 4.9, 8.75, 2.6, "Qué muestra el diagnóstico",
       [b("Residuos aproximadamente simétricos y centrados en cero."),
        b("Ljung–Box (lag 12): Q = 8,42 con p = 0,751; no se rechaza la ausencia de autocorrelación.",
          space_after=0)], accent=AZUL, tsize=17)
s.card(MX + 9.15, CT + 4.9, 8.75, 2.6, "Alcance de la conclusión",
       [b("Shapiro–Wilk p = 0,184: compatible con normalidad, sin constituir prueba definitiva."),
        b("No se afirma homocedasticidad estricta; la evidencia es consistente con un comportamiento "
          "residual adecuado.", space_after=0)], accent=MUT, tsize=17)

s = ANEXO("A4", "Intermitencia: del catálogo completo a un SKU")
s.rect(MX, CT, 10.4, 7.05, fill=WHITE, line=LINE, radius=0.06)
s.image(HEATMAP, MX + 0.3, CT + 0.3, 9.8, 6.15)
s.caption(MX + 0.3, CT + 6.55, 9.8, "Matriz de demanda: 100 SKUs × 66 meses.")
s.rect(MX + 10.8, CT, 7.1, 3.4, fill=WHITE, line=LINE, radius=0.06)
s.image(SKU97, MX + 11.0, CT + 0.35, 6.7, 2.7)
s.caption(MX + 11.0, CT + 3.5, 6.7, "Ejemplo individual: 62 % de meses en cero.")
s.card(MX + 10.8, CT + 4.0, 7.1, 3.05, "Lectura",
       [b("La intermitencia no es homogénea: convive con familias de rotación continua.", size=13.8),
        b("Modelar el SKU aislado obliga a predecir la ocurrencia y la magnitud a la vez.", size=13.8),
        b("La agregación a familia recupera una señal continua y estacional.", size=13.8, space_after=0)],
       accent=AZUL, tsize=17)

s = ANEXO("A5", "Matriz de sensibilidad del impacto financiero (Tabla 6.1)")
rows = [("Conservador", "$12.000", "18 %", "$84,5M CLP", "$15,2M CLP/año", False),
        ("Caso base", "$15.000", "22 %", "$105,6M CLP", "$23,2M CLP/año", True),
        ("Exigente (alta merma)", "$18.000", "26 %", "$126,8M CLP", "$33,0M CLP/año", False)]
colx = [MX, MX + 5.2, MX + 8.0, MX + 11.0, MX + 14.4]
colw = [5.2, 2.8, 3.0, 3.4, 3.5]
heads = ["Escenario de costo y tasa", "Costo reposición (c)", "Tasa holding (i)", "Capital liberado", "Ahorro anual"]
s.text(MX, CT, CW, 0.4, [para("PANEL A  ·  GESTIÓN DESCENTRALIZADA POR SKU (K = 100 · 7.041 UNIDADES LIBERADAS)",
                              size=12.5, bold=True, color=GRAY, space_after=0, spc=1.6)])
yh = CT + 0.5
s.rect(MX, yh, CW, 0.62, fill=INK, radius=0.0)
for x, w, t in zip(colx, colw, heads):
    s.text(x + 0.28, yh, w - 0.4, 0.62, [para(t, size=13, bold=True, color=WHITE, space_after=0)], valign="m")
for i, (esc, c_, i_, cap, aho, hero) in enumerate(rows):
    y = yh + 0.62 + i * 0.78
    s.rect(MX, y, CW, 0.78, fill=(LIGHT if hero else WHITE), line=LINE)
    vals = [esc, c_, i_, cap, aho]
    for j, (x, w, v) in enumerate(zip(colx, colw, vals)):
        s.text(x + 0.28, y, w - 0.4, 0.78,
               [para(v, size=14, bold=hero, color=(AZUL if hero and j >= 3 else INK if hero else TXT),
                     space_after=0)], valign="m")
s.text(MX, yh + 3.3, CW, 0.4, [para("PANEL B  ·  AGRUPACIÓN CENTRALIZADA CON RISK POOLING (K = 10 · 704 UNIDADES)",
                                    size=12.5, bold=True, color=GRAY, space_after=0, spc=1.6)])
s.card(MX, yh + 3.8, 8.75, 1.75, None,
       [para("Bajo pooling independiente el capital liberado se reduce a un rango de $8,5M a $12,7M CLP, con "
             "ahorros anuales de $1,5M a $3,3M CLP.", size=14, color=TXT, space_after=0, line=1.24)],
       accent=MUT)
s.card(MX + 9.15, yh + 3.8, 8.75, 1.75, None,
       [para("Con aprovisionamiento marítimo internacional (L = 4 meses) el buffer liberado escala por √4: "
             "14.082 unidades, equivalentes a $211,2M CLP.", size=14, color=TXT, space_after=0, line=1.24)],
       accent=AZUL)
s.caption(MX, yh + 5.75, CW, "Supuestos: Z = 1,645 (CSL 95 %); SS = Z × MAE × K × raíz(L). Ejercicio ilustrativo "
                             "de orden de magnitud.")

s = ANEXO("A6", "Entorno macro y estacionalidad de la demanda")
s.rect(MX, CT, 10.6, 5.2, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{F}/fig2_2.png", MX + 0.35, CT + 0.3, 9.9, 4.6)
s.caption(MX, CT + 5.35, 10.6, "IPC de vestuario y calzado, serie mensual auditada INE (base 2023 = 100).")
s.rect(MX + 11.0, CT, 6.9, 6.7, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{F}/fig2_1.png", MX + 11.3, CT + 0.3, 6.3, 6.1)
s.card(MX, CT + 5.9, 10.6, 1.65, None,
       [para("Los precios del vestuario caen de forma sostenida en el período: el margen se defiende con "
             "volumen bien planificado, no con precio. La estacionalidad se reparte entre las cuatro "
             "estaciones, sin un peak único dominante.", size=13.5, color=TXT, space_after=0, line=1.2)],
       accent=AMAR)

s = ANEXO("A7", "Trazabilidad, verificación y uso de herramientas de IA")
s.card(MX, CT, 8.75, 5.4, "Mecanismos de verificación",
       [b("Separación cronológica estricta entre entrenamiento, validación y prueba."),
        b("Pruebas automatizadas sobre rezagos y disponibilidad temporal de cada variable."),
        b("Revisión manual de transformaciones y agregaciones jerárquicas."),
        b("Recálculo directo de las métricas a partir de las predicciones almacenadas."),
        b("Fijación de semillas, versiones de librerías y parámetros de ejecución."),
        b("Verificación de consistencia entre las formulaciones matemáticas y el código.", space_after=0)],
       accent=AZUL)
s.card(MX + 9.15, CT, 8.75, 5.4, "Uso de herramientas de IA generativa",
       [b("Apoyo instrumental en programación, depuración, refactorización y revisión de redacción."),
        b("No sustituyó la formulación del problema, la selección de datos, las decisiones metodológicas ni "
          "la interpretación de resultados."),
        b("Distintos modelos fundacionales se usaron como panel de contraste técnico para debatir "
          "decisiones de diseño."),
        b("Ningún fragmento de código se incorporó sin inspección, adaptación y validación previa."),
        b("Por confidencialidad del retailer, los registros transaccionales no son distribuibles; se "
          "conservan scripts, entornos y resultados intermedios para auditoría.", space_after=0)],
       accent=ROJO)
s.banner(MX, CT + 5.75, CW, 1.7,
         "El autor definió la arquitectura experimental, las reglas de disponibilidad temporal de las "
         "variables, los criterios de comparación, las métricas y los supuestos del impacto financiero. "
         "La responsabilidad por la exactitud de resultados y conclusiones recae en el autor.",
         fill=LIGHT2, color=TXT, size=15.5, bold=False)


# ═══════════════════════════ NOTAS DEL ORADOR ═══════════════════════════
NOTAS = {
1: "45 s. Saludo: buenos días, mi nombre es Joaquín Mondaca y presento la memoria "
   "«Pronóstico Jerárquico de Demanda Intermitente en el Retail de Moda Femenina», guiada por el profesor "
   "Villena y con la profesora Tapia como correferente. En 18 minutos voy a mostrar el problema, la "
   "arquitectura que propongo, la evidencia y el impacto financiero.",
2: "30 s. Recorrido en seis bloques. No leer la lámina: anunciar que el bloque 5, resultados, es el centro "
   "de la presentación y que hay anexos de respaldo al final para las preguntas.",
3: "1 min 15 s. Tres hechos de la industria que definen el problema: ciclos de 2 a 3 meses, demanda "
   "dirigida por el plan comercial y compromisos de compra con 3 a 6 meses de anticipación. El gráfico "
   "muestra la demanda agregada del núcleo comercial: alta volatilidad y caída estructural post-2021. "
   "Transición: sobre esta serie agregada la señal existe; el problema aparece al bajar al SKU.",
4: "1 min 30 s. Dato clave: 30,3 % de los pares SKU-mes no registran venta. El mapa de calor muestra 100 "
   "SKUs por 66 meses; las zonas claras son ceros. No es ruido, es estructura. Croston y SBA fueron "
   "diseñados para intermitencia sin estacionalidad; SARIMA supone continuidad. Cerrar con el dilema: "
   "sobre-stock inmoviliza capital, quiebre destruye ingreso y fidelidad.",
5: "1 min. Leer la pregunta de investigación en voz alta y luego H0/H1. Enfatizar que la hipótesis se "
   "operacionaliza con WAPE y que los benchmarks primarios son SARIMA, SARIMAX y LSTM; Croston, SBA, "
   "Seasonal Naïve y Chronos-Bolt entran como referencias de frontera.",
6: "1 min. Justificar el foco: Top 100 SKUs y 58 familias concentran 72 % del volumen y 78 % del margen. "
   "Punto crítico anti-leakage: el Top 100 se selecciona solo con datos previos al corte, no con el "
   "período de prueba. Mostrar la jerarquía de agregación de departamento a SKU.",
7: "50 s. Tres grupos de variables. La distinción importante: el plan comercial (precio y descuento) es "
   "ex-ante porque lo decide la empresa antes del mes; el resto de la información va rezagada en t-1. "
   "Si el jurado pregunta por leakage, esta es la lámina para volver.",
8: "1 min. Declarar supuestos antes de mostrar resultados: venta cero con inventario = demanda cero; "
   "target son ventas observadas, no demanda latente. Y declarar la asimetría metodológica: las líneas "
   "base usan parametrización parsimoniosa estándar, sin auto-ARIMA por SKU. Esto anticipa una pregunta "
   "probable del jurado.",
9: "50 s. Por qué WAPE: el MAPE se indetermina con ceros. Ejemplo concreto del propio benchmark: SARIMA "
   "tiene sMAPE de 309,88 % y WAPE de 76,74 %. El WAPE pondera por volumen físico, que es la unidad de "
   "decisión de inventario.",
10: "1 min. Partición 80/10/10 estrictamente cronológica; calibración congelada en enero de 2025 y siete "
    "meses de prueba ciega (febrero a agosto de 2025). Recalcar: pesos congelados, sin reajustar durante "
    "el test. Esto es lo que hace creíble el resultado.",
11: "40 s. La batería de referencia cubre desde Seasonal Naïve y SARIMA hasta LSTM y modelos "
    "fundacionales de 2024. Todos evaluados con la misma ventana, jerarquía y métrica.",
12: "2 min. Lámina central. Recorrer el flujo: la serie agregada de familia entra a la Capa 1 (Holt "
    "amortiguado, inercia); lo que queda son residuos que la Capa 2 explica con el ensamble GBDT más "
    "TabPFN y las señales de precio; la Capa 3 integra ambas con ruteo por momentum y desagrega top-down "
    "a SKU. Frase de cierre: cada capa resuelve un problema distinto.",
13: "50 s. Capa 1. La idea de fondo: no gastar capacidad del modelo de árboles en aprender el nivel, que "
    "una ecuación de suavizamiento estima mejor y con menos varianza.",
14: "1 min. Capa 2. El ensamble modela el residuo. Cuatro modelos porque fallan de forma distinta y el "
    "promedio ponderado por NNLS reduce el error. Escala arcsinh y decay de 24 meses para privilegiar el "
    "comportamiento comercial reciente.",
15: "1 min 15 s. Capa 3. Ruteo por momentum: si la categoría acelera, pesa más el aprendizaje automático. "
    "Desagregación con proporciones históricas. Mencionar la honestidad experimental: las cuotas "
    "aprendidas dieron 24,35 %, peor que el reparto estático de 16,10 %.",
16: "2 min. Resultado principal. Leer de abajo hacia arriba: Croston 84,87 %, SARIMA 76,74 %, Seasonal "
    "Naïve 69,89 %, LSTM 45,75 %, Chronos-Bolt 48,44 % y ES-GBM 16,10 %. A nivel familia, 12,89 %. "
    "Pausa después del número: es el corazón de la defensa.",
17: "1 min. El pronóstico sigue la trayectoria real en los siete meses. R² de 0,95 a nivel SKU y 0,96 a "
    "nivel familia; sesgo de −4,8 %, es decir, sub-predicción leve y sistemática, que es corregible y "
    "operacionalmente preferible a sobre-predecir.",
18: "1 min 30 s. Ablación: sin precios el error sube a 38,25 %; con precio rezagado, 26,42 %; con plan "
    "ex-ante, 16,10 %. Conclusión conceptual: la demanda del fast fashion no es estocástica, la dirige el "
    "plan comercial. Matiz honesto: la importancia por ganancia del 67 % no es una estimación causal de "
    "elasticidad precio.",
19: "1 min 30 s. Traducción a negocio: pasar de MAE 54,2 a 11,4 unidades por SKU reduce el stock de "
    "seguridad de 8.916 a 1.875 unidades. Eso son 7.041 unidades, 105,6 millones de pesos de capital "
    "liberado y 23,2 millones anuales de ahorro en holding. Declarar de inmediato que es un ejercicio "
    "ilustrativo de orden de magnitud con MAE como proxy.",
20: "1 min 15 s. Cuatro conclusiones. La contribución no es un algoritmo nuevo: es una arquitectura que "
    "asigna cada problema al método que mejor lo resuelve, bajo un protocolo que impide explicar el "
    "resultado por fuga de información.",
21: "1 min. Limitaciones primero, con seguridad: horizonte de un mes, un solo retailer, ventana de prueba "
    "sin el peak de noviembre-diciembre, ejercicio financiero ilustrativo. Luego trabajo futuro: "
    "fine-tuning de modelos fundacionales, desagregación con deep learning y cola larga del catálogo.",
22: "Cierre. Agradecer al profesor guía, a la profesora correferente y a la empresa por los datos. "
    "Quedar en silencio y esperar preguntas. Los anexos A1 a A7 están listos para respaldar respuestas.",
23: "Anexo A1. Tabla 5.1 completa: WAPE, sMAPE, RMSE, MAE, sesgo, R² y ranking en ambos niveles.",
24: "Anexo A2. Comparativa visual de seis arquitecturas contra la demanda real.",
25: "Anexo A3. Residuos: Ljung-Box con p = 0,751 y Shapiro-Wilk con p = 0,184. Usar si preguntan por "
    "supuestos estadísticos.",
26: "Anexo A4. Evidencia de intermitencia: matriz completa y un SKU con 62 % de meses en cero.",
27: "Anexo A5. Matriz de sensibilidad financiera: rango de 84,5 a 126,8 millones bajo gestión "
    "descentralizada y de 8,5 a 12,7 millones con risk pooling. Usar si cuestionan el supuesto de "
    "agregación.",
28: "Anexo A6. Contexto macro: el IPC de vestuario cae de forma sostenida. Estacionalidad repartida entre "
    "las cuatro estaciones.",
29: "Anexo A7. Protocolo de verificación y uso declarado de herramientas de IA. Tenerlo presente: es una "
    "pregunta cada vez más frecuente en defensas.",
}
for i, sl in enumerate(d.slides, 1):
    if i in NOTAS:
        sl.notes = NOTAS[i]

# ═══════════════════════════ salida ═══════════════════════════
if __name__ == "__main__":
    import sys
    issues = d.qa()
    print(f"Láminas: {len(d.slides)}")
    if issues:
        print(f"\n⚠ {len(issues)} incidencias de control de calidad:")
        for i in issues:
            print("  -", i)
    else:
        print("✓ Control de calidad sin incidencias")
    out = "/home/user/PPT/Defensa_Tesis_Estructurada.pptx"
    d.save_pptx(out)
    print("PPTX:", out, os.path.getsize(out) // 1024, "KB")
    only = None
    if len(sys.argv) > 1 and sys.argv[1] != "all":
        only = {int(x) for x in sys.argv[1].split(",")}
    d.render_previews("/home/user/work/preview", only=only)
    print("previews listos")
    if not only:
        pdf = "/home/user/PPT/Defensa_Tesis_Estructurada_respaldo.pdf"
        d.save_pdf(pdf)
        print("PDF respaldo:", pdf, os.path.getsize(pdf) // 1024, "KB")
