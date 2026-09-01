"""Defensa de Memoria — Pronóstico Jerárquico de Demanda Intermitente.
Construye el PPTX final + previews para revisión visual."""
import os
from engine import (Deck, para, W, H, MX, CW, CT, CB, EYE_Y, TIT_Y, RULE_Y,
                    ROJO, AMAR, AMAR_D, AZUL, AZUL_D, INK, TXT, GRAY, MUT,
                    LIGHT, LIGHT2, LINE, WHITE)

A = "/home/user/work/assets"
F = "/home/user/work/fig"
C = "/home/user/work/charts"
FM = "/home/user/work/formulas"

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


def b(t, size=14.2, space_after=7, color=TXT, **kw):
    return para(t, size=size, bullet=True, color=color, space_after=space_after, line=1.18, **kw)


def tabla_bt(sl, x, y, w, cols, rows, rowh=0.86, fsize=12.6):
    """Tabla estilo booktabs: solo reglas horizontales, sin fondos ni bordes verticales."""
    sl.hline(x, y, w, color=INK, lw=1.7)
    cx = x
    for cw, tit, al in cols:
        sl.text(cx, y + 0.14, cw - 0.35, 0.42,
                [para(tit, size=11.3, bold=True, color=GRAY, align=al, space_after=0, spc=1.5)])
        cx += cw
    yy = y + 0.66
    sl.hline(x, yy, w, color=INK, lw=0.9)
    for r, fila in enumerate(rows):
        cx = x
        for (cw, _, al), val in zip(cols, fila):
            first = cx == x
            sl.text(cx, yy, cw - 0.35, rowh,
                    [para(val, size=(fsize + 1.3 if first else fsize),
                          bold=first, color=(INK if first else TXT), align=al,
                          space_after=0, line=1.2)], valign="m")
            cx += cw
        yy += rowh
        if r < len(rows) - 1:
            sl.hline(x, yy, w, color="EAEDF0", lw=0.6)
    sl.hline(x, yy, w, color=INK, lw=1.7)
    return yy


def metrica(sl, x, w, abbr, nombre, img, simbolos, lectura, col):
    sl.text(x, CT, w, 0.5, [para(abbr, size=20, bold=True, color=col, space_after=2)])
    sl.text(x, CT + 0.48, w, 0.4, [para(nombre, size=13, color=GRAY, space_after=0)])
    sl.rect(x, CT + 0.90, w, 1.55, fill=WHITE, line=LINE, radius=0.05)
    sl.image(f"{FM}/{img}.png", x + 0.35, CT + 1.02, w - 0.7, 1.31)
    sl.text(x, CT + 2.58, w, 0.35, [para("QUÉ SIGNIFICA CADA SÍMBOLO", size=11, bold=True, color=GRAY,
                                         space_after=0, spc=1.6)])
    yy = CT + 2.92
    sl.hline(x, yy, w, color=INK, lw=1.1)
    for k, (sym, txt) in enumerate(simbolos):
        yy2 = yy + 0.06 + k * 0.50
        sl.text(x + 0.05, yy2, 1.2, 0.44,
                [para(sym, size=14.5, bold=True, color=INK, align="c", space_after=0)], valign="m")
        sl.text(x + 1.4, yy2, w - 1.5, 0.44,
                [para(txt, size=12.8, color=TXT, space_after=0, line=1.18)], valign="m")
        if k < len(simbolos) - 1:
            sl.hline(x, yy2 + 0.44, w, color="EAEDF0", lw=0.6)
    yfin = yy + 0.06 + len(simbolos) * 0.50
    sl.hline(x, yfin, w, color=INK, lw=1.1)
    sl.card(x, yfin + 0.26, w, 10.02 - (yfin + 0.26), "Cómo se lee",
            [para(lectura, size=12.7, color=TXT, space_after=0, line=1.2)], accent=col, tsize=15.5, pad=0.32)


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
s.caption(9.65, 9.55, 9.3, "Participación de cada estación en la demanda anual (waffle, anexo A11).")

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
s.banner(MX, CT + 7.0, CW, 0.72,
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

# ═══════════════════════════ 11 · FASE 0 · ANTI-LEAKAGE ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Fase 0 · La frontera de información",
      "La etapa que consumió más tiempo del proyecto: garantizar que ninguna variable conozca el futuro.")
s.rect(MX, 3.25, 12.9, 0.6, fill=AZUL, radius=0.05)
s.text(MX, 3.25, 12.9, 0.6, [para("INFORMACIÓN DISPONIBLE  ·  HASTA t−1", size=13.5, bold=True,
                                  color=WHITE, align="c", space_after=0, spc=2)], valign="m")
s.rect(MX + 13.3, 3.25, 4.6, 0.6, fill=ROJO, radius=0.05)
s.text(MX + 13.3, 3.25, 4.6, 0.6, [para("MES t  ·  POR PRONOSTICAR", size=13.5, bold=True, color=WHITE,
                                        align="c", space_after=0, spc=2)], valign="m")
s.vline(MX + 13.1, 3.15, 2.6, color=ROJO, lw=2)
pasado = ["Demanda rezagada\nt−1 y t−12", "Medias móviles\nde 3 y 12 meses",
          "IPC de vestuario\ny macro en t−1", "Meses desde\nla última venta"]
for i, t in enumerate(pasado):
    x = MX + i * 3.27
    s.rect(x, 4.05, 3.05, 1.5, fill=LIGHT, line=LINE, radius=0.05)
    s.text(x + 0.2, 4.05, 2.65, 1.5, [para(t, size=13.5, color=TXT, align="c", space_after=0, line=1.22)],
           valign="m")
s.rect(MX + 13.3, 4.05, 4.6, 1.5, fill="FDECEF", line=ROJO, radius=0.05)
s.text(MX + 13.5, 4.05, 4.2, 1.5,
       [para("Plan comercial ex-ante", size=14, bold=True, color=ROJO, align="c", space_after=4),
        para("precio y descuento del mes t: única señal del presente, porque la decide la empresa",
             size=12.5, color=TXT, align="c", space_after=0, line=1.2)], valign="m")
f0 = [("Auditoría variable por variable", ROJO,
       "Se revisó una a una la disponibilidad temporal de cada variable y de cada transformación: medias "
       "móviles, agregaciones y escalados pueden arrastrar señal del mes t sin que se note."),
      ("Decenas de iteraciones", AMAR,
       "Cada corrección de rezago cambiaba el comportamiento del ensamble. La arquitectura final es el "
       "resultado de ese ciclo de revisión, reajuste y nueva medición."),
      ("Pruebas automatizadas de integridad", AZUL,
       "Una batería de tests verifica los rezagos en cada corrida. Las variables identificadas como fuente "
       "de fuga se eliminaron o se rezagaron antes de volver a entrenar.")]
for i, (t, col, txt) in enumerate(f0):
    s.card(MX + i * 6.08, 5.95, 5.73, 2.6, t, [para(txt, size=13.8, color=TXT, space_after=0, line=1.24)],
           accent=col, tsize=17)
s.banner(MX, 8.75, CW, 1.25,
         "Sin esta fase, cualquier resultado sería un artefacto: un modelo que ve el futuro siempre gana en "
         "el papel y falla en producción. El 16,10 % vale porque se obtuvo bajo esta restricción.",
         fill=AZUL, size=16)

# ═══════════════════════════ 12 · BATERÍA DE MODELOS ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Diez arquitecturas, un mismo protocolo",
      "Desde la heurística estacional de 1970 hasta los modelos fundacionales pre-entrenados de 2024.")
s.rect(3.35, 3.05, 13.3, 6.15, fill=WHITE, line=LINE, radius=0.06)
s.image(EVOL, 3.75, 3.35, 12.5, 5.55)
s.banner(MX, 9.35, CW, 0.67,
         "Todas las referencias se evalúan sobre la misma ventana, la misma jerarquía y la misma métrica: "
         "la comparación es una decisión de diseño, no un accidente.", fill=LIGHT2, color=TXT, size=14.5,
         bold=False)

# ═══════════════════════════ 13 · ARQUITECTURA ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Arquitectura ES-GBM: dos tracks en paralelo, un ensamble ponderado")
s.pill((W - 13.0) / 2, 2.38, 13.0, 0.55,
       "Fase 0  ·  Panel Familia × Fecha con variables auditadas y rezagadas", fill=INK, size=13.5)
tracks = [(MX, 6.9, "CAPA 1  ·  SIN SUAVIZAMIENTO", ROJO, "Modelos sobre la serie directa",
           ["XGBoost · LightGBM · CatBoost", "Escala arcsinh con decay de 24 meses",
            "Reactiva: sigue los giros bruscos", "3 predicciones"]),
          (MX + 7.2, 6.9, "CAPA 2  ·  CON SUAVIZAMIENTO", AMAR_D, "Modelos sobre la serie relativa al nivel",
           ["LightGBM · CatBoost", "Escala log(1 + unidades / nivel)",
            "Nivel base extraído por Holt amortiguado", "2 predicciones"]),
          (MX + 14.4, 3.5, "EN PARALELO", AZUL, "TabPFN",
           ["Modelo fundacional tabular", "Inferencia zero-shot", "1 predicción"])]
ty, th = 3.12, 2.62
for x, wd, cap, col, tit, bs in tracks:
    s.rect(x, ty, wd, th, fill=LIGHT, radius=0.055)
    s.rect(x, ty, wd, 0.5, fill=col, radius=0.055)
    s.rect(x, ty + 0.28, wd, 0.22, fill=col)
    s.text(x, ty, wd, 0.5, [para(cap, size=11.5, bold=True, color=WHITE, align="c", space_after=0, spc=1.6)],
           valign="m")
    s.text(x + 0.34, ty + 0.62, wd - 0.68, 0.42,
           [para(tit, size=15, bold=True, color=INK, space_after=0, line=1.1)])
    s.text(x + 0.34, ty + 1.12, wd - 0.68, th - 1.25,
           [b(t, size=12.6, space_after=5, indent=0.24) for t in bs])
for x in (MX + 3.45, MX + 10.65, MX + 16.15):
    s.vline(x, ty + th + 0.04, 0.16, color=MUT, lw=1.5)
s.hline(MX + 3.45, ty + th + 0.20, 12.70, color=MUT, lw=1.5)
s.arrow(10.0, ty + th + 0.20, 10.0, 6.06, color=MUT, lw=1.6)
s.pill((W - 8.4) / 2, 6.10, 8.4, 0.55, "6 predicciones candidatas por familia", fill=LIGHT2, color=INK, size=14.5)
s.arrow(10.0, 6.68, 10.0, 6.88, color=MUT, lw=1.6)
s.banner(MX, 6.95, CW, 0.82,
         "VALIDACIÓN  ·  Ponderación NNLS y búsqueda en grilla: se fija el peso de cada modelo y el umbral "
         "de ruteo minimizando el WAPE", fill=AZUL, size=14.5)
s.arrow(10.0, 7.85, 10.0, 8.05, color=MUT, lw=1.6)
s.pill((W - 10.5) / 2, 8.10, 10.5, 0.55, "Demanda proyectada por familia  ·  WAPE 12,89 %",
       fill="E8EEF3", color=AZUL_D, size=14.5)
s.arrow(10.0, 8.72, 10.0, 8.92, color=MUT, lw=1.6)
s.rect(MX, 8.97, CW, 0.62, fill=LIGHT, line=LINE, radius=0.05)
s.text(MX + 0.4, 8.97, CW - 0.8, 0.62,
       [para("CAPA 3  ·  los mismos modelos estiman la cuota de cada SKU dentro de su familia → "
             "desagregación top-down", size=14, bold=True, color=INK, align="c", space_after=0)], valign="m")
s.arrow(10.0, 9.64, 10.0, 9.82, color=MUT, lw=1.6)
s.text(MX, 9.85, CW, 0.4, [para("Pronóstico por SKU  ·  Top 100  ·  WAPE 16,10 %", size=15, bold=True,
                                color=AZUL, align="c", space_after=0)])

# ═══════════════════════════ 14 · CAPAS 1 Y 2 ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Capas 1 y 2 · Por qué entrenar dos veces lo mismo")
s.rect(MX, CT, 9.4, 5.0, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{C}/tracks.png", MX + 0.3, CT + 0.25, 8.8, 4.5)
s.caption(MX, CT + 5.15, 9.4, "Comportamiento esperado de cada track frente a la demanda real.")
s.card(MX + 10.0, CT, 7.9, 2.4, "Capa 1 · sin suavizamiento",
       [b("Los modelos ven la serie tal cual, en escala arcsinh.", size=13.6),
        b("Reacciona rápido a shocks comerciales, pero hereda el ruido: mayor varianza.",
          size=13.6, space_after=0)], accent=ROJO, tsize=17)
s.card(MX + 10.0, CT + 2.7, 7.9, 2.45, "Capa 2 · con suavizamiento",
       [b("Holt amortiguado extrae el nivel base y los modelos trabajan en escala relativa a ese nivel.",
          size=13.6),
        b("Filtra ruido y conserva estacionalidad: menor varianza, pero reacciona más tarde.",
          size=13.6, space_after=0)], accent=AMAR, tsize=17)
s.banner(MX, CT + 5.7, CW, 1.85,
         "La clave es la diversificación de errores: cuando el mercado gira, la Capa 1 llega antes; cuando "
         "hay ruido, la Capa 2 no se deja arrastrar. Sus errores no están correlacionados, y por eso la "
         "combinación pondera mejor que cualquiera de los dos por separado.", fill=AZUL, size=16)

# ═══════════════════════════ 15 · PESOS ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Cómo se combinan: pesos calibrados en validación")
s.card(MX, CT, 5.73, 3.5, "Ponderación NNLS",
       [b("Mínimos cuadrados no negativos: pesos mayores o iguales a cero que suman exactamente 1.",
          size=13.6),
        b("Ningún modelo puede entrar con signo invertido ni dominar por construcción.",
          size=13.6, space_after=0)], accent=ROJO, tsize=17.5)
s.card(MX + 6.08, CT, 5.73, 3.5, "Búsqueda en grilla",
       [b("Se evalúa una grilla de umbrales de momentum entre 1,05 y 1,50.", size=13.6),
        b("Para cada valor se reoptimizan los pesos de ruteo y se elige la combinación que minimiza el "
          "WAPE en validación.", size=13.6, space_after=0)], accent=AMAR, tsize=17.5)
s.card(MX + 12.17, CT, 5.73, 3.5, "Ruteo por régimen",
       [b("Indicador de momentum: media móvil de 3 meses sobre media móvil de 12.", size=13.6),
        b("Si la familia acelera, pesa más el componente de nivel dinámico; si está madura, la señal "
          "conservadora.", size=13.6, space_after=0)], accent=AZUL, tsize=17.5)
s.text(MX, CT + 3.85, CW, 0.4, [para("GRILLA DE UMBRALES EVALUADA EN VALIDACIÓN", size=12.5, bold=True,
                                     color=GRAY, space_after=0, spc=2)])
taus = ["1,05", "1,15", "1,25", "1,35", "1,50"]
gw = 2.6
for i, t in enumerate(taus):
    x = MX + i * (gw + 0.35)
    sel = i == 2
    s.rect(x, CT + 4.35, gw, 1.0, fill=(AZUL if sel else LIGHT), line=(None if sel else LINE), radius=0.05)
    s.text(x, CT + 4.35, gw, 1.0, [para(t, size=17, bold=True, color=(WHITE if sel else GRAY),
                                        align="c", space_after=0)], valign="m")
s.text(MX + 2 * (gw + 0.35), CT + 5.45, gw, 0.35,
       [para("τ* seleccionado", size=12, bold=True, color=AZUL, align="c", space_after=0)])
s.text(MX + 15.0, CT + 4.35, 2.9, 1.0,
       [para("...para cada umbral se reoptimizan los pesos", size=12.5, color=MUT, space_after=0, line=1.2)],
       valign="m")
s.banner(MX, CT + 6.0, CW, 1.55,
         "Esto es lo que da sostenibilidad en el tiempo: los pesos no son una constante del modelo, son un "
         "parámetro recalibrable. Si cambia la estructura del mercado, la recalibración reasigna peso hacia "
         "los modelos que mejor capturan el nuevo régimen, sin rediseñar la arquitectura.",
         fill=AZUL, size=16)

# ═══════════════════════════ 16 · CAPA 3 ═══════════════════════════
s = S("04", "METODOLOGÍA Y ARQUITECTURA", "Capa 3 · De la familia al SKU: desagregación top-down")
s.rect(MX, CT, 8.6, 2.55, fill=LIGHT, radius=0.06)
s.rect(MX + 0.45, CT + 0.78, 2.5, 0.9, fill=AZUL, radius=0.06)
s.text(MX + 0.45, CT + 0.78, 2.5, 0.9,
       [para("Familia", size=14.5, bold=True, color=WHITE, align="c", space_after=2),
        para("demanda proyectada", size=10.5, color="CBDCE7", align="c", space_after=0)], valign="m")
for i, (k, pc) in enumerate([("SKU A", "41 %"), ("SKU B", "27 %"), ("SKU C", "19 %"), ("SKU D", "13 %")]):
    y = CT + 0.26 + i * 0.52
    s.rect(MX + 4.6, y, 3.5, 0.46, fill=WHITE, line=LINE, radius=0.04)
    s.text(MX + 4.85, y, 1.6, 0.46, [para(k, size=12.5, bold=True, color=INK, space_after=0)], valign="m")
    s.text(MX + 6.3, y, 1.6, 0.46, [para(pc, size=12.5, bold=True, color=AZUL, align="r", space_after=0)],
           valign="m")
    s.arrow(MX + 3.05, CT + 1.23, MX + 4.5, y + 0.23, color=MUT, lw=1.2)
s.text(MX + 0.45, CT + 2.02, 3.6, 0.4, [para("Las cuotas suman 100 %", size=11.5, color=MUT,
                                             space_after=0)])
s.card(MX + 9.3, CT, 8.6, 2.55, "Qué predice esta capa",
       [b("No la demanda del SKU, sino su participación dentro de la familia; la demanda familiar se "
          "multiplica por esa cuota.", size=13.4),
        b("Restringido al catálogo estratégico: las cuotas se normalizan sobre el Top 100 de cada familia.",
          size=13.4, space_after=0)], accent=AZUL, tsize=17)
vias = [("Vía A · proporciones históricas", AMAR,
         [("La cuota se calcula con las ventas del período de entrenamiento y se mantiene fija durante el "
           "test.", False),
          ("Es el esquema que usan todos los modelos comparados: garantiza una comparación justa.", False),
          ("Resultado principal: WAPE 16,10 %.", True)]),
        ("Vía B · cuotas supervisadas", INK,
         [("LightGBM, XGBoost y CatBoost predicen la cuota mes a mes con la historia que va surgiendo.",
           False),
          ("Variables: cuota rezagada en t−1 y t−12, medias móviles de 3 y 12 meses, meses desde la última "
           "venta y precio relativo del SKU.", False),
          ("Evaluada en la misma ventana: WAPE 24,35 %.", True)]),
        ("Regla de selección en validación", AZUL,
         [("El pipeline compara el WAPE de ambos esquemas sobre la ventana de validación.", False),
          ("Adopta el de menor error para la prueba ciega, sin intervención manual.", False),
          ("En esta ventana seleccionó el reparto estático; si el catálogo cambia, la misma regla puede "
           "adoptar las cuotas aprendidas.", False)])]
for i, (tit, col, bs) in enumerate(vias):
    s.card(MX + i * 6.08, CT + 2.85, 5.73, 3.85, tit,
           [b(t, size=13.4, bold=bo, color=(INK if bo else TXT), space_after=10) for t, bo in bs],
           accent=col, tsize=17)
s.banner(MX, CT + 6.95, CW, 0.72,
         "En catálogos con alta intermitencia, la estabilidad de las proporciones históricas le ganó a la "
         "sofisticación de las cuotas aprendidas.", fill=LIGHT2, color=TXT, size=14.5, bold=False)

# ═══════════════════════════ 17 · BENCHMARK ═══════════════════════════
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
          "WAPE fuera de muestra sobre 7 meses de prueba ciega. Detalle completo de métricas en el anexo A3.")

# ═══════════════════════════ 18 · CALIDAD DEL AJUSTE ═══════════════════════════
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

# ═══════════════════════════ 19 · ABLACIÓN ═══════════════════════════
s = S("05", "RESULTADOS Y EVIDENCIA", "Ablación del vector de precios: tres configuraciones, un mismo ensamble")
s.rect(MX, CT, 8.6, 5.0, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{C}/ablation.png", MX + 0.3, CT + 0.25, 8.0, 4.5)
s.caption(MX, CT + 5.15, 8.6, "WAPE a nivel SKU según la información de precios disponible al pronosticar.")
s.card(MX, CT + 5.55, 8.6, 2.15, "Cómo se corrió el experimento",
       [b("Se reentrena el ensamble completo excluyendo o rezagando el vector de precios; el resto del "
          "protocolo se mantiene idéntico.", size=13.6),
        b("Ejecuciones separadas del pipeline: 8 semillas × 3 modelos GBDT × NNLS × ruteo.",
          size=13.6, space_after=0)], accent=INK, tsize=17)
s.text(MX + 9.3, CT - 0.06, 8.6, 0.4, [para("ESTUDIO DE ABLACIÓN · NIVEL SKU (TABLA 5.5)", size=12.5,
                                            bold=True, color=GRAY, space_after=0, spc=1.8)])
tx = MX + 9.3
cols = [(0.0, 3.5, "Configuración de precios", "l"), (3.5, 1.4, "WAPE", "r"), (4.9, 1.3, "MAPE", "r"),
        (6.2, 1.2, "RMSE", "r"), (7.4, 1.2, "R²", "r")]
yh = CT + 0.42
s.rect(tx, yh, 8.6, 0.55, fill=INK)
for dx, wd, t, al in cols:
    s.text(tx + dx + 0.18, yh, wd - 0.36, 0.55,
           [para(t, size=12.5, bold=True, color=WHITE, align=al, space_after=0)], valign="m")
filas = [("1 · Sin información de precios", "38,25 %", "44,10 %", "58,3", "0,69", False),
         ("2 · Con precio rezagado t−1", "26,42 %", "31,50 %", "41,2", "0,78", False),
         ("3 · Con plan comercial ex-ante t", "16,10 %", "20,47 %", "26,7", "0,95", True)]
for i, (cfg, wa, ma, rm, r2, hero) in enumerate(filas):
    y = yh + 0.55 + i * 0.72
    s.rect(tx, y, 8.6, 0.72, fill=("E8EEF3" if hero else WHITE), line=LINE)
    if hero:
        s.rect(tx, y, 0.06, 0.72, fill=AZUL)
    for (dx, wd, _, al), v in zip(cols, (cfg, wa, ma, rm, r2)):
        s.text(tx + dx + 0.18, y, wd - 0.36, 0.72,
               [para(v, size=13.5, bold=hero, color=(AZUL_D if hero else TXT), align=al, space_after=0)],
               valign="m")
s.caption(tx, yh + 2.78, 8.6,
          "La configuración 3 es el modelo propuesto; las otras dos son reentrenamientos controlados.")
s.rect(tx, CT + 3.75, 8.6, 3.8, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{F}/fig5_4.png", tx + 0.25, CT + 3.95, 8.1, 3.4)
s.caption(tx, CT + 7.42, 8.6,
          "Importancia por ganancia total del módulo GBDT: el precio ex-ante concentra el 67,0 %.")

# ═══════════════════════════ 20 · IMPACTO FINANCIERO ═══════════════════════════
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

# ═══════════════════════════ 21 · CONCLUSIONES ═══════════════════════════
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

# ═══════════════════════════ 22 · LIMITACIONES Y FUTURO ═══════════════════════════
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

# ═══════════════════════════ 23 · CIERRE ═══════════════════════════
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


s = ANEXO("A1", "Los modelos de referencia, en simple")
cols = [(3.0, "Modelo", "l"), (4.9, "Qué hace", "l"), (4.4, "Punto fuerte", "l"),
        (4.3, "Punto débil", "l"), (1.3, "WAPE", "r")]
rows = [
 ("Seasonal Naïve", "Repite lo que se vendió el mismo mes del año anterior.",
  "Referencia honesta y sin costo: captura la estacionalidad pura.",
  "Ciega a precios, campañas y cambios de tendencia.", "69,89 %"),
 ("SARIMA", "Proyecta la serie usando su propia historia y su ciclo anual.",
  "Estándar de la literatura: interpretable y reproducible.",
  "Es lineal y no admite información externa; los ceros la desestabilizan.", "76,74 %"),
 ("SARIMAX", "SARIMA más variables externas: precio y descuento.",
  "Incorpora la palanca comercial dentro de un marco econométrico.",
  "La relación precio-demanda no es lineal: la estructura se le queda corta.", "73,24 %"),
 ("Croston", "Separa dos preguntas: cada cuánto se vende y cuánto se vende.",
  "Diseñado específicamente para demanda con muchos ceros.",
  "No modela estacionalidad ni precio, que es justo lo que manda en moda.", "84,87 %"),
 ("SBA", "Croston con una corrección de sesgo (Syntetos-Boylan).",
  "Corrige la sobreestimación sistemática del Croston clásico.",
  "Hereda la misma ceguera estacional y comercial.", "83,42 %"),
 ("LSTM", "Red neuronal con memoria que aprende patrones de secuencias.",
  "Captura relaciones no lineales y dependencias temporales largas.",
  "Exige mucha historia; con series cortas e intermitentes se vuelve inestable.", "45,75 %"),
 ("Chronos-Bolt", "Modelo fundacional pre-entrenado sobre miles de millones de series.",
  "Predice sin entrenamiento previo; muy sólido en agregado (36,35 % en familia).",
  "No admite las variables comerciales propias de la empresa.", "48,44 %"),
]
yfin = tabla_bt(s, MX, CT, CW, cols, rows, rowh=0.82)
s.banner(MX, yfin + 0.42, CW, 0.75,
         "Ninguna referencia clásica combina las tres cosas que exige la moda: ceros, estacionalidad fuerte "
         "y sensibilidad al plan comercial.", fill=LIGHT2, color=TXT, size=14, bold=False)

s = ANEXO("A2", "Los componentes de la arquitectura propuesta")
cols2 = [(2.7, "Componente", "l"), (1.9, "Dónde actúa", "l"), (4.9, "Qué hace", "l"),
         (4.2, "Punto fuerte", "l"), (4.2, "Punto débil", "l")]
rows2 = [
 ("Holt amortiguado", "Capa 2", "Suaviza la serie y estima su nivel y tendencia, frenando la extrapolación.",
  "Muy estable y con pocos parámetros: entrega una base limpia.",
  "Por sí solo ignora precios y cualquier relación no lineal."),
 ("XGBoost", "Capas 1 y 2", "Árboles que corrigen, uno tras otro, el error del anterior.",
  "Captura interacciones como precio por temporada; muy preciso en datos tabulares.",
  "No extrapola tendencias fuera del rango que vio en entrenamiento."),
 ("LightGBM", "Capas 1 y 2", "Mismo principio que XGBoost, pero por histogramas: mucho más rápido.",
  "Escala bien y maneja con soltura las variables categóricas.",
  "Puede sobreajustar en series cortas si no se regula."),
 ("CatBoost", "Capas 1 y 2", "Boosting ordenado, pensado para variables categóricas.",
  "Robusto con familias y canales; menos propenso al sobreajuste.",
  "Es el más lento de entrenar de los tres."),
 ("TabPFN", "En paralelo", "Modelo fundacional para tablas: infiere sin entrenar.",
  "Buen desempeño inmediato y aporta diversidad al ensamble.",
  "Pensado para conjuntos pequeños; no es un modelo de series nativo."),
 ("NNLS y ruteo", "Validación", "Decide cuánto pesa cada predicción y en qué régimen aplicarla.",
  "Adapta el ensamble al momento comercial de cada familia.",
  "Los pesos deben recalibrarse cuando cambia la estructura del mercado."),
]
yfin2 = tabla_bt(s, MX, CT, CW, cols2, rows2, rowh=0.92)
s.banner(MX, yfin2 + 0.42, CW, 0.85,
         "La arquitectura no elige un ganador: pone a cada método a hacer aquello en lo que es bueno y deja "
         "que la validación decida el peso.", fill=AZUL, size=15)

s = ANEXO("A3", "Comparativa consolidada de desempeño (Tabla 5.1)")
t51 = [(6.4, "Modelo / arquitectura", "l"), (1.7, "WAPE", "r"), (1.9, "sMAPE", "r"), (1.6, "RMSE", "r"),
       (1.5, "MAE", "r"), (1.7, "Bias", "r"), (1.4, "R²", "r"), (1.7, "Ranking", "r")]
panelA = [("ES-GBM (Static Top-Down)", "16,10 %", "20,47 %", "26,7", "11,4", "−4,8 %", "0,95", "1°", True),
          ("ES-GBM (Learned Dynamic Share)", "24,35 %", "28,90 %", "41,2", "17,2", "−5,2 %", "0,79", "2°", False),
          ("LSTM Recurrente (con precio ex-ante)", "45,75 %", "52,10 %", "64,1", "32,3", "+8,4 %", "0,55", "3°", False),
          ("Chronos-Bolt Desagregado (Static Share)", "48,44 %", "70,69 %", "65,1", "34,2", "+5,6 %", "0,72", "4°", False),
          ("LSTM Recurrente (sin precio ex-ante)", "53,76 %", "61,40 %", "68,1", "38,1", "+11,2 %", "0,38", "5°", False),
          ("Seasonal Naïve (benchmark del año anterior)", "69,89 %", "88,17 %", "107,2", "49,4", "+6,3 %", "0,23", "6°", False),
          ("SARIMAX (con precio y descuento)", "73,24 %", "170,87 %", "122,9", "51,7", "+11,6 %", "−0,01", "7°", False),
          ("SARIMA Univariado (línea base)", "76,74 %", "309,88 %", "139,6", "54,2", "+14,3 %", "−0,31", "8°", False),
          ("SBA (Syntetos-Boylan Approximation)", "83,42 %", "95,19 %", "108,1", "58,9", "−4,2 %", "0,22", "9°", False),
          ("Croston Clásico", "84,87 %", "95,35 %", "108,6", "59,9", "+0,9 %", "0,21", "10°", False)]
panelB = [("ES-GBM Ensamble Agregado", "12,89 %", "14,67 %", "35,9", "15,7", "−4,8 %", "0,96", "1°", True),
          ("Chronos-Bolt Agregado (Zero-Shot)", "36,35 %", "61,38 %", "81,9", "44,3", "+5,6 %", "0,79", "2°", False),
          ("LSTM Recurrente Agregado", "40,51 %", "69,36 %", "88,1", "49,3", "+7,9 %", "0,76", "3°", False),
          ("SARIMAX Agregado", "59,64 %", "268,31 %", "165,3", "72,6", "+11,6 %", "0,16", "4°", False),
          ("Seasonal Naïve Agregado", "59,78 %", "84,80 %", "148,9", "72,8", "+6,3 %", "0,32", "5°", False),
          ("SARIMA Agregado", "64,84 %", "450,19 %", "183,3", "79,0", "+14,3 %", "−0,03", "6°", False)]
yy = CT
s.hline(MX, yy, CW, color=INK, lw=1.7)
cx = MX
for cw, tit, al in t51:
    s.text(cx + (0 if al == "l" else 0), yy + 0.10, cw - 0.30, 0.36,
           [para(tit, size=11, bold=True, color=GRAY, align=al, space_after=0, spc=1.2)])
    cx += cw
yy += 0.52
s.hline(MX, yy, CW, color=INK, lw=0.9)
for panel, titulo in ((panelA, "PANEL A · MODELOS DESAGREGADOS A NIVEL SKU (TOP 100 PRODUCTOS)"),
                      (panelB, "PANEL B · MODELOS AGREGADOS A NIVEL FAMILIA (58 FAMILIAS)")):
    s.text(MX, yy + 0.06, CW, 0.32, [para(titulo, size=10.5, bold=True, color=ROJO, space_after=0, spc=1.2)])
    yy += 0.40
    for fila in panel:
        hero = fila[-1]
        if hero:
            s.rect(MX, yy, CW, 0.37, fill="EEF3F7")
        cx = MX
        for (cw, _, al), v in zip(t51, fila[:-1]):
            s.text(cx, yy, cw - 0.30, 0.37,
                   [para(v, size=11.6, bold=hero, color=(AZUL_D if hero else TXT), align=al, space_after=0)],
                   valign="m")
            cx += cw
        yy += 0.37
        s.hline(MX, yy, CW, color="EDF0F2", lw=0.5)
s.hline(MX, yy, CW, color=INK, lw=1.7)
s.caption(MX, yy + 0.16, CW, "Evaluación fuera de muestra, febrero a agosto de 2025. Las fórmulas de cada "
                             "métrica están en los anexos A4 a A6.")

s = ANEXO("A4", "Métricas de error relativo")
metrica(s, MX, 8.6, "WAPE", "Weighted Absolute Percentage Error  ·  métrica rectora del estudio", "wape",
        [("y", "demanda real observada en el mes t, en unidades vendidas"),
         ("ŷ", "pronóstico del modelo para ese mismo mes"),
         ("Σ", "suma sobre los n meses del horizonte de evaluación"),
         ("n", "número de meses evaluados: 7 en la prueba ciega"),
         ("100 %", "expresa el resultado como porcentaje del volumen vendido")],
        "Suma todos los errores y los divide por el volumen total vendido: es inmune a la división por "
        "cero. Un WAPE de 16,10 % significa que el error acumulado equivale al 16,10 % de las unidades "
        "vendidas.", AZUL)
s.vline(MX + 8.95, CT, 7.4, color=LINE, lw=0.75)
metrica(s, MX + 9.3, 8.6, "MAPE", "Mean Absolute Percentage Error  ·  reportado en su variante simétrica",
        "mape",
        [("y", "demanda real observada en el mes t"),
         ("ŷ", "pronóstico del modelo para ese mismo mes"),
         ("T +", "conjunto de meses con demanda estrictamente positiva"),
         ("|T +|", "cantidad de esos meses: el promedio se calcula solo sobre ellos")],
        "Promedia el error relativo mes a mes. Con demanda cero se indetermina y con demanda baja se "
        "dispara: SARIMA llega a un sMAPE de 309,88 % pese a un WAPE de 76,74 %.", ROJO)

s = ANEXO("A5", "Métricas de escala absoluta")
metrica(s, MX, 8.6, "MAE", "Mean Absolute Error  ·  error promedio en unidades físicas", "mae",
        [("y", "demanda real observada en el mes t"),
         ("ŷ", "pronóstico del modelo para ese mismo mes"),
         ("| |", "valor absoluto: ignora si el modelo sobrestimó o subestimó"),
         ("n", "número total de observaciones evaluadas")],
        "Error promedio expresado en prendas. Alimenta el cálculo del stock de seguridad: 11,4 unidades "
        "por SKU frente a 54,2 de SARIMA, y esa diferencia es la que libera capital.", AZUL)
s.vline(MX + 8.95, CT, 7.4, color=LINE, lw=0.75)
metrica(s, MX + 9.3, 8.6, "RMSE", "Root Mean Squared Error  ·  penaliza los errores grandes", "rmse",
        [("y", "demanda real observada en el mes t"),
         ("ŷ", "pronóstico del modelo para ese mismo mes"),
         ("( )²", "eleva al cuadrado: castiga con más fuerza las desviaciones grandes"),
         ("raíz", "devuelve el resultado a las unidades originales")],
        "Al castigar los errores grandes, delata a los modelos que aciertan casi siempre pero fallan feo en "
        "los peaks de campaña. El ES-GBM obtiene 26,7 unidades frente a 139,6 de SARIMA.", ROJO)

s = ANEXO("A6", "Métricas de calibración y bondad de ajuste")
metrica(s, MX, 8.6, "Bias", "Sesgo porcentual  ·  hacia qué lado se equivoca el modelo", "bias",
        [("ŷ − y", "diferencia con signo entre pronóstico y demanda real"),
         ("+", "sobreestimación sistemática: riesgo de sobre-stock"),
         ("−", "subestimación sistemática: riesgo de quiebre"),
         ("Σ y", "volumen total vendido, para expresarlo como porcentaje")],
        "Un buen modelo combina WAPE bajo con sesgo cercano a cero. El ES-GBM tiene −4,8 %: subestima "
        "levemente, que en gestión de inventario es el error más barato de los dos.", AMAR_D)
s.vline(MX + 8.95, CT, 7.4, color=LINE, lw=0.75)
metrica(s, MX + 9.3, 8.6, "R²", "Coeficiente de determinación  ·  cuánta varianza explica el modelo", "r2",
        [("y", "demanda real observada en el mes t"),
         ("ŷ", "pronóstico del modelo para ese mismo mes"),
         ("media", "demanda promedio del período: la y con barra en la fórmula"),
         ("1 −", "resta la varianza no explicada sobre la varianza total")],
        "Proporción de la variabilidad de la demanda que el modelo explica. El ES-GBM alcanza 0,95 a nivel "
        "SKU y 0,96 a nivel familia; SARIMA queda en terreno negativo, es decir, predice peor que usar el "
        "promedio.", AZUL)

s = ANEXO("A7", "Pronóstico vs. demanda real por modelo")
s.rect(MX, CT, CW, 6.9, fill=WHITE, line=LINE, radius=0.06)
s.image(f"{F}/fig5_1.png", MX + 0.4, CT + 0.3, 17.1, 6.3)
s.caption(MX, CT + 7.05, CW, "Seis arquitecturas representativas contra la demanda observada del Top 100 "
                             "SKUs en la ventana de prueba.")

s = ANEXO("A8", "Diagnóstico de residuos del modelo propuesto")
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

s = ANEXO("A9", "Intermitencia: del catálogo completo a un SKU")
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

s = ANEXO("A10", "Matriz de sensibilidad del impacto financiero (Tabla 6.1)")
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

s = ANEXO("A11", "Entorno macro y estacionalidad de la demanda")
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

s = ANEXO("A12", "Trazabilidad, verificación y uso de herramientas de IA")
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
1: "45 s. Saludo: mi nombre es Joaquín Mondaca y presento la memoria «Pronóstico Jerárquico de Demanda "
   "Intermitente en el Retail de Moda Femenina», guiada por el profesor Villena y con la profesora Tapia "
   "como correferente. En 18 minutos: problema, arquitectura, evidencia e impacto financiero.",
2: "30 s. Recorrido en seis bloques. Anunciar que el bloque 5, resultados, es el centro, y que hay siete "
   "anexos de respaldo para las preguntas.",
3: "1 min 15 s. Tres hechos de la industria: ciclos de 2 a 3 meses, demanda dirigida por el plan comercial "
   "y compromisos de compra con 3 a 6 meses de anticipación. El gráfico muestra la demanda agregada del "
   "núcleo comercial. Transición: en la serie agregada la señal existe; el problema aparece al bajar al SKU.",
4: "1 min 30 s. 30,3 % de los pares SKU-mes no registran venta. El mapa de calor son 100 SKUs por 66 meses; "
   "las zonas claras son ceros. No es ruido, es estructura. Croston y SBA suponen intermitencia sin "
   "estacionalidad, SARIMA supone continuidad. Cerrar con el dilema: sobre-stock inmoviliza capital, "
   "quiebre destruye ingreso.",
5: "1 min. Leer la pregunta y luego H0/H1. La hipótesis se operacionaliza con WAPE. Benchmarks primarios: "
   "SARIMA, SARIMAX y LSTM; Croston, SBA, Seasonal Naïve y Chronos-Bolt como referencias de frontera.",
6: "1 min. Top 100 SKUs y 58 familias concentran 72 % del volumen y 78 % del margen. Punto crítico: el Top "
   "100 se selecciona solo con datos previos al corte, no con el período de prueba.",
7: "50 s. Tres grupos de variables. La distinción clave: el plan comercial es ex-ante porque lo decide la "
   "empresa; todo lo demás va rezagado en t-1. Enlaza directo con la Fase 0.",
8: "1 min. Declarar supuestos antes de los resultados: venta cero con inventario es demanda cero; el target "
   "son ventas observadas. Y declarar la asimetría metodológica de las líneas base. Esto anticipa una "
   "pregunta probable del jurado.",
9: "50 s. Por qué WAPE: el MAPE se indetermina con ceros. Ejemplo del propio benchmark: SARIMA tiene sMAPE "
   "de 309,88 % y WAPE de 76,74 %. El WAPE pondera por volumen físico, la unidad de decisión de inventario.",
10: "1 min. Partición 80/10/10 cronológica, calibración congelada en enero de 2025 y siete meses de prueba "
    "ciega. Recalcar: pesos congelados, sin reajustar durante el test.",
11: "1 min 30 s. LÁMINA IMPORTANTE: contar que esta fue la etapa donde más tiempo se invirtió. La demanda y "
    "las variables macro solo se conocen en t-1; la única señal del presente es el plan comercial, porque "
    "lo fija la empresa. Explicar que fueron decenas de iteraciones: al transformar variables (medias "
    "móviles, agregaciones) a veces se colaba señal del mes t sin darse cuenta, y cada corrección de rezago "
    "cambiaba el comportamiento del modelo. Cerrar con la frase del banner: un modelo que ve el futuro "
    "siempre gana en el papel.",
12: "40 s. La batería de referencia cubre desde Seasonal Naïve y SARIMA hasta LSTM y modelos fundacionales "
    "de 2024. Todos con la misma ventana, jerarquía y métrica.",
13: "2 min 30 s. LÁMINA CENTRAL. Recorrer el flujo de arriba hacia abajo: del panel auditado en Fase 0 salen "
    "dos tracks paralelos. La Capa 1 entrena XGBoost, LightGBM y CatBoost sobre la serie directa en escala "
    "arcsinh: reactiva, más volátil. La Capa 2 entrena LightGBM y CatBoost sobre la serie relativa al nivel "
    "que extrae el Holt amortiguado: más estable. Sumando TabPFN son seis predicciones candidatas por "
    "familia. Esas seis entran a validación, donde se fija el peso de cada una. Con esos pesos se obtiene "
    "la demanda de familia y recién ahí entra la Capa 3, que desagrega a SKU.",
14: "1 min 15 s. Explicar por qué se entrena dos veces: no es redundancia, es diversificación de errores. "
    "El track sin suavizar llega antes cuando el mercado gira; el suavizado no se deja arrastrar por el "
    "ruido. Como sus errores no están correlacionados, la combinación pondera mejor que cualquiera solo. "
    "Aclarar que el gráfico es un esquema ilustrativo del comportamiento, no datos del modelo.",
15: "1 min 30 s. Aquí está el argumento de sostenibilidad. Los pesos salen de NNLS (no negativos y suman 1) "
    "y la calibración se hace con una búsqueda en grilla sobre validación: se recorre la grilla de umbrales "
    "de momentum entre 1,05 y 1,50 y para cada valor se reoptimizan los pesos, quedándose con la "
    "combinación que minimiza el WAPE. La consecuencia práctica: si la industria cambia de comportamiento, "
    "la recalibración reasigna peso a los modelos que capturan mejor el nuevo régimen, sin rediseñar nada.",
16: "1 min 45 s. La Capa 3 no predice demanda: predice la cuota de cada SKU dentro de su familia. Vía A: "
    "proporciones históricas, que es el esquema que usan todos los benchmarks y por eso garantiza una "
    "comparación justa; entrega el 16,10 %. Vía B: el motor supervisado que estima la cuota mes a mes con "
    "cuota rezagada, medias móviles, meses sin venta y precio relativo; dio 24,35 %. Y lo importante: el "
    "pipeline no elige a mano. Compara el WAPE de ambos esquemas en la ventana de validación y adopta el "
    "de menor error para la prueba ciega; en esta ventana seleccionó el reparto estático. Si el catálogo "
    "cambiara de comportamiento, la misma regla podría adoptar las cuotas aprendidas sin rediseñar nada.",
17: "2 min. Resultado principal. Leer de abajo hacia arriba: Croston 84,87 %, SARIMA 76,74 %, Seasonal Naïve "
    "69,89 %, Chronos-Bolt 48,44 %, LSTM 45,75 % y ES-GBM 16,10 %. A nivel familia, 12,89 %. Pausa después "
    "del número.",
18: "1 min. El pronóstico sigue la trayectoria real en los siete meses. R2 de 0,95 a nivel SKU y 0,96 a "
    "nivel familia; sesgo de -4,8 %, sub-predicción leve, sistemática y corregible.",
19: "2 min. LÁMINA DE EVIDENCIA. Explicar que se probaron tres configuraciones reentrenando el ensamble "
    "completo: sin ninguna información de precios, con el precio rezagado del mes anterior, y con el plan "
    "comercial ex-ante del propio mes. Resultados: 38,25 %, 26,42 % y 16,10 % de WAPE, con R2 de 0,69, "
    "0,78 y 0,95. Dos lecturas: el plan comercial aporta 22,2 puntos de reducción, o sea la demanda del "
    "fast fashion no es estocástica sino dirigida; y aun sin precios el modelo queda en 38,25 %, muy por "
    "debajo de SARIMA (76,74 %) y SBA (83,42 %), lo que muestra que no depende de forma frágil de esa "
    "señal. Matiz honesto: el 67 % de importancia por ganancia no es una estimación causal de elasticidad.",
20: "1 min 30 s. Traducción a negocio: pasar de MAE 54,2 a 11,4 unidades por SKU baja el stock de seguridad "
    "de 8.916 a 1.875 unidades. Son 7.041 unidades, 105,6 millones de capital liberado y 23,2 millones "
    "anuales de ahorro. Declarar de inmediato que es un ejercicio ilustrativo de orden de magnitud.",
21: "1 min 15 s. Cuatro conclusiones. La contribución no es un algoritmo nuevo: es una arquitectura que "
    "asigna cada problema al método que mejor lo resuelve, bajo un protocolo que impide explicar el "
    "resultado por fuga de información.",
22: "1 min. Limitaciones primero y con seguridad: horizonte de un mes, un solo retailer, ventana sin el peak "
    "de noviembre-diciembre, ejercicio financiero ilustrativo. Luego trabajo futuro.",
23: "Cierre. Agradecer al profesor guía, a la profesora correferente y a la empresa por los datos. Silencio "
    "y esperar preguntas. Los anexos A1 a A7 respaldan las respuestas.",
24: "Anexo A1. Glosario de los modelos de referencia en lenguaje simple. Es la lámina para responder "
    "cualquier pregunta del tipo por qué no usó tal método o qué diferencia hay entre Croston y SARIMA.",
25: "Anexo A2. Los componentes de la arquitectura propia y por qué cada uno está donde está. Útil si "
    "preguntan por qué tres GBDT distintos o para qué sirve TabPFN.",
26: "Anexo A3. Tabla 5.1 completa: WAPE, sMAPE, RMSE, MAE, sesgo, R2 y ranking en los dos niveles de "
    "agregación. Es la lámina de respaldo para cualquier cifra que pregunten.",
27: "Anexo A4. Fórmulas de WAPE y MAPE con el significado de cada símbolo. Usar si piden justificar por "
    "qué el WAPE es la métrica rectora: el MAPE se indetermina con demanda cero.",
28: "Anexo A5. Fórmulas de MAE y RMSE. El MAE es el que conecta con el cálculo de stock de seguridad; el "
    "RMSE castiga los errores grandes de los peaks.",
29: "Anexo A6. Fórmulas de Bias y R2. El sesgo dice hacia qué lado se equivoca el modelo: −4,8 % es "
    "subestimación leve, que en inventario es el error más barato.",
30: "Anexo A7. Comparativa visual de seis arquitecturas contra la demanda real.",
31: "Anexo A8. Residuos: Ljung-Box p = 0,751 y Shapiro-Wilk p = 0,184. Usar si preguntan por supuestos.",
32: "Anexo A9. Evidencia de intermitencia: matriz completa y un SKU con 62 % de meses en cero.",
33: "Anexo A10. Sensibilidad financiera: 84,5 a 126,8 millones bajo gestión descentralizada y 8,5 a 12,7 "
    "millones con risk pooling. Usar si cuestionan el supuesto de agregación.",
34: "Anexo A11. Contexto macro: el IPC de vestuario cae de forma sostenida. Estacionalidad repartida.",
35: "Anexo A12. Protocolo de verificación y uso declarado de herramientas de IA.",
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
