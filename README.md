# 🎓 Extractor de Enlaces de Vimeo - IDEBIO

**Herramienta de extracción automatizada de enlaces de sesiones grabadas del Diplomado en Biodesprogramación**

---

## 📋 Descripción

Este repositorio contiene scripts automatizados para extraer y organizar enlaces de videos de Vimeo desde archivos JSON complejos del **Diplomado en Biodesprogramación** de IDEBIO. La herramienta procesa datos de sesiones educativas y genera archivos estructurados listos para su uso y distribución.

### 🎯 Propósito

Facilitar el acceso y la gestión de las grabaciones de las sesiones del diplomado mediante:
- **Extracción automatizada** de enlaces de Vimeo desde estructuras JSON complejas
- **Organización sistemática** de sesiones por módulos temáticos
- **Generación de formatos múltiples** (TXT y CSV) para diferentes casos de uso
- **Preservación de metadatos** como títulos, fechas, tutores y módulos

---

## ✨ Características

- ✅ **Extracción recursiva** de enlaces de Vimeo desde JSON anidados
- ✅ **Soporte multilenguaje**: Scripts en Python y JavaScript
- ✅ **Múltiples formatos de salida**: TXT legible y CSV para análisis
- ✅ **Organización por módulos**: Estructura clara del contenido educativo
- ✅ **Preservación de caracteres especiales**: Acentos, ñ y símbolos
- ✅ **Metadatos completos**: Títulos, fechas, tutores e IDs de Vimeo

---

## 📁 Estructura de Archivos

### 📥 Archivos de Entrada

| Archivo | Descripción |
|---------|-------------|
| `Tutorias_G42.json` | Archivo JSON fuente con datos de todas las sesiones (449 KB) |

### 🔧 Scripts de Procesamiento

| Archivo | Lenguaje | Descripción |
|---------|----------|-------------|
| `extract_vimeo_links.py` | Python 3 | Script de extracción en Python con soporte completo UTF-8 |
| `extract_vimeo_links.js` | JavaScript (Node.js) | Script de extracción en JavaScript para entornos Node.js |

### 📤 Archivos de Salida

| Archivo | Formato | Tamaño | Descripción |
|---------|---------|--------|-------------|
| `Sesiones_Vimeo_G42.txt` | Texto plano | 10 KB | Lista organizada por módulos, ideal para lectura rápida |
| `Sesiones_Vimeo_G42.csv` | CSV | 6.8 KB | Datos estructurados para análisis en Excel/Sheets |

---

## 🚀 Uso

### Requisitos Previos

**Para Python:**
```bash
Python 3.6 o superior
```

**Para JavaScript:**
```bash
Node.js 12 o superior
```

### Ejecución

**Opción 1: Python**
```bash
python extract_vimeo_links.py
```

**Opción 2: JavaScript**
```bash
node extract_vimeo_links.js
```

### Salida Esperada

Ambos scripts generarán:
1. `Sesiones_Vimeo_G42.txt` - Archivo de texto organizado
2. `Sesiones_Vimeo_G42.csv` - Archivo CSV estructurado

---

## 📊 Contenido Extraído

### Estadísticas del Diplomado - Generación 42

- **Total de sesiones**: 82 sesiones grabadas
- **Módulos principales**: 14 módulos temáticos
- **Sesiones especiales**: 24+ sesiones extraordinarias
- **Tutores**: 12 profesionales especializados

### Módulos del Diplomado

| Módulo | Tema | Sesiones | Tutor/a Principal |
|--------|------|----------|-------------------|
| M1 | Introducción a la Biodesprogramación: Leyes Universales | 3 | Ofelia Puente |
| M2 | La Nueva Medicina Germánica | 4 | Ivette Ferrer / Osmary Acebal |
| M3 | La Nueva Medicina Germánica 2 | 4 | Osmary Acebal |
| M4 | Anatomía | 5 | Dra. Dulce Herrera |
| M5 | Psicobiología | 4 | Laura García |
| M6 | Órganos y Emociones - Conflictos por Capas Embrionarias | 4 | María de la O |
| M7 | Órganos y Emociones II | 4 | María de la O Córdova |
| M8 | Conflictos de Comportamiento I | 4 | Fabiola Guzmán |
| M9 | Conflictos de Comportamiento II | 4 | Fabiola Guzmán |
| M10 | Tipos de Cuerpo y Alimentos | 4 | Alejandra Benchoam |
| M11 | Proyecto Sentido | 4 | Osmary Acebal |
| M12 | Árbol Transgeneracional | 4 | Angélica Marín |
| M13 | Acompañamiento al Inconsciente | 6 | Denisse Jiménez / Fernando Sánchez |
| M14 | Principios de PNL | 4 | Patricia Pascual |

---

## 📖 Formatos de Salida

### Archivo TXT (`Sesiones_Vimeo_G42.txt`)

**Características:**
- ✅ Organizado por módulos temáticos
- ✅ Formato legible para humanos
- ✅ Incluye títulos completos, URLs e IDs
- ✅ Ideal para consulta rápida y referencia

**Ejemplo:**
```
MÓDULO 1: INTRODUCCIÓN A LA BIODESPROGRAMACIÓN: LEYES UNIVERSALES
Tutora: Ofelia Puente

1. G42 M1 INTRODUCCIÓN A LA BIODESPROGRAMACIÓN: LEYES UNIVERSALES Tutora Ofelia Puente 29OCT
   Vimeo URL: https://vimeo.com/1025238330
```

### Archivo CSV (`Sesiones_Vimeo_G42.csv`)

**Características:**
- ✅ Importable a Excel, Google Sheets, etc.
- ✅ Permite filtrado y ordenamiento
- ✅ Ideal para análisis de datos

**Columnas:**
- `title` - Título completo de la sesión
- `vimeo_id` - ID numérico del video en Vimeo
- `vimeo_url` - URL completa del video

---

## 🔧 Detalles Técnicos

### Proceso de Extracción

1. **Lectura del JSON**: Carga del archivo `Tutorias_G42.json`
2. **Búsqueda recursiva**: Navegación por la estructura JSON anidada
3. **Extracción de IDs**: Uso de expresiones regulares para identificar IDs de Vimeo
   - Patrón: `player\.vimeo\.com/video/(\d+)`
4. **Generación de URLs**: Construcción de enlaces completos
   - Formato: `https://vimeo.com/[ID]`
5. **Exportación**: Creación de archivos TXT y CSV con codificación UTF-8

### Tecnologías Utilizadas

- **Python**: Módulos `json`, `re`, `csv`
- **JavaScript**: Módulos nativos `fs` de Node.js
- **Expresiones Regulares**: Para extracción de IDs de Vimeo
- **UTF-8**: Codificación para preservar caracteres especiales

---

## 👥 Tutores del Diplomado

- Ofelia Puente
- Ivette Ferrer
- Osmary Acebal
- Dra. Dulce Herrera
- Laura García
- María de la O / María de la O Córdova
- Fabiola Guzmán
- Alejandra Benchoam
- Angélica Marín
- Denisse Jiménez
- Fernando Sánchez
- Patricia Pascual

---

## 📝 Notas

- Los enlaces de Vimeo se extraen del campo `tab_content` en el JSON
- Se preservan todos los caracteres especiales (acentos, ñ, etc.)
- Los archivos de salida usan codificación UTF-8
- El script es reutilizable para otras generaciones del diplomado

---

## 📄 Licencia

Este proyecto es de uso interno para IDEBIO.

---

## 📧 Contacto

Para más información sobre el Diplomado en Biodesprogramación, visita [IDEBIO](https://idebio.com).

---

**Generado para**: Diplomado en Biodesprogramación - Generación 42  
**Última actualización**: Diciembre 2025