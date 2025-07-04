# 🧬 BioExplorer

#**BioExplorer** es una web app prototipo de exploración bioinformática, que permite buscar genes, proteínas o variantes usando APIs públicas como NCBI, UniProt, KEGG, Reactome y PDB. Incluye alineamientos, visualizaciones estructurales, rutas metabólicas, variantes, y más.

---

## 🚀 Funcionalidades

- 🔍 Buscar genes, proteínas o variantes por nombre o ID
- 📡 Consultar APIs externas (NCBI, UniProt, KEGG, etc.)
- 📊 Visualizar estructuras 3D, alineamientos y plots (como Ramachandran)
- 🧬 Mostrar características de secuencia: dominios, regiones, features
- 🧠 Mostrar rutas metabólicas asociadas
- ⚙️ API REST lista para escalar

---

```
## Estructura de la aplicación Web:
BioExplorer/
├── backend/
│   ├── app.py                  # FastAPI o Flask backend principal
│   └── bioHerramientas/
│       ├── __init__.py
│       ├── ncbiAPI.py             # Funciones para consumir NCBI APIs
│       ├── uniprotAPI.py          # Funciones para consumir UniProt APIs
│       ├── alineamiento.py       # Alineamiento básico
│       ├── bioGraficos.py            # Ramachandran, otros plots (PNG)
│       └── bioEstructuras.py       # py3Dmol u otros análisis 3D
│──── frontend/                 # Archivos estáticos (CSS, JS)
│       ├── static/  
│       │       ├── css/
│       │       │   └── style.css
│       │       └── js/
│       │           └── main.js
│       └── templates/              # HTML templates
│           └── index.html
├── data/                       # Archivos de prueba, PDBs, FASTA, etc.
│   └── test_data.fasta
├── requirements.txt            # Dependencias Python
├── README.md                   # Instrucciones del proyecto
└── .gitignore                  # Ignorar venvs, cachés, etc.
```