# Generador del deck de defensa

Reconstruye `Defensa_Tesis_Estructurada.pptx` (32 láminas) de forma reproducible.

- `engine.py` — motor de maquetación: un mismo spec genera el PPTX (python-pptx) y un
  preview PNG (Pillow) para revisión visual, más control de calidad automático
  (desbordes de texto, márgenes y glifos ausentes en la tipografía).
- `charts.py` — gráficos propios con la paleta institucional UTFSM
  (rojo `#D10120`, amarillo `#F7B006`, azul `#005F91`).
- `build_deck.py` — contenido de las 32 láminas + notas del orador.

```bash
pip install python-pptx pillow numpy matplotlib pymupdf fonttools
python charts.py        # gráficos
python build_deck.py all  # PPTX + previews + PDF de respaldo
```

Tipografía del PPTX: **Open Sans** (misma de la portada original).
Si el equipo donde se presenta no la tiene instalada, PowerPoint la sustituirá:
se puede instalar gratis desde Google Fonts.
