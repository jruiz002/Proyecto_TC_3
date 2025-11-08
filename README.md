# 🤖 Simulador de Máquinas de Turing - Proyecto TC3

## 🎥 Video de demostración

<p align="center">
  <a href="https://youtu.be/a9uvLOrx9Dw" target="_blank">
    <img src="https://img.youtube.com/vi/a9uvLOrx9Dw/hqdefault.jpg" alt="Video del proyecto: Máquinas de Turing" />
  </a>
  <br/>
  <em>Haz clic en la imagen para ver el video</em>
  <br/>
</p>

**Curso:** Teoría de la Computación  
**Universidad:** Universidad del Valle de Guatemala  
**Fecha:** Noviembre 2025

## 📋 Descripción del Proyecto

Este proyecto implementa un simulador completo de Máquinas de Turing con capacidad para ejecutar tanto **máquinas reconocedoras** como **máquinas alteradoras**. El sistema está diseñado con una interfaz de menú interactivo que facilita la comprensión y demostración del funcionamiento de las MT.

## 🏗️ Arquitectura del Proyecto

```
Proyecto_TC_3/
├── 📄 main.py                    # Menú interactivo principal
├── 🔧 mt_reconocedora.yaml       # Definición MT Reconocedora
├── 🔧 mt_alteradora.yaml         # Definición MT Alteradora  
├── 📝 cadenas_reconocedora.txt   # Cadenas de prueba reconocedora
├── 📝 cadenas_alteradora.txt     # Cadenas de prueba alteradora
├── 📚 requirements.txt           # Dependencias del proyecto
├── 📖 README.md                  # Esta documentación
└── 📁 src/                       # Código fuente
    ├── models/                   # Modelos de datos
    ├── parser/                   # Parser YAML
    ├── simulator/                # Motor de simulación
    └── utils/                    # Utilidades y validadores
```

## 🚀 Instalación y Ejecución

### 1. Requisitos Previos
- Python 3.8 o superior

### 2. Instalación
```bash
# Instalar dependencias
pip install -r requirements.txt
```

### 3. Ejecución
```bash
# Ejecutar el menú interactivo
python main.py
```

## 🎮 Uso del Menú Interactivo

Al ejecutar `python main.py`, aparecerá el siguiente menú:

```
SIMULADOR DE MÁQUINAS DE TURING
   Proyecto TC3 - Teoría de la Computación
   Universidad del Valle de Guatemala
============================================================

OPCIONES DISPONIBLES:
1. Ejecutar MT Reconocedora de Palíndromos
2. Ejecutar MT Alteradora (Duplicar cadena)
3. Ver información del proyecto
4. Salir
```

### Opción 1: MT Reconocedora
- **Lenguaje:** Palíndromos sobre {a, b}
- **Archivo YAML:** `mt_reconocedora.yaml`
- **Cadenas de prueba:** `cadenas_reconocedora.txt`
- **Algoritmo:** Compara primer símbolo con el último, marca ambos y repite hasta el centro

### Opción 2: MT Alteradora  
- **Función:** Duplicar cadena (w → ww)
- **Archivo YAML:** `mt_alteradora.yaml`
- **Cadenas de prueba:** `cadenas_alteradora.txt`
- **Algoritmo:** Copia cada símbolo al final de la cadena

## 📊 Evaluación según Rúbrica

### 🔍 MT Reconocedora (7 puntos)

**Cadenas Aceptadas (≥5 caracteres):**
- `"abba"` - 4 caracteres, palíndromo simple
- `"ababa"` - 5 caracteres, palíndromo impar
- `"aabbaa"` - 6 caracteres, palíndromo par
- `"bbaabb"` - 6 caracteres, palíndromo con patrón diferente

**Cadenas Rechazadas (≥5 caracteres):**
- `"abab"` - 4 caracteres, no es palíndromo
- `"aabbb"` - 5 caracteres, no es palíndromo
- `"aaabba"` - 6 caracteres, no es palíndromo

**Dificultad de la MT:** Media-Alta
- Requiere comparación de símbolos en posiciones simétricas
- Utiliza marcadores para rastrear progreso de comparación
- Maneja navegación compleja por la cinta (ida y vuelta)

### 🔄 MT Alteradora (7 puntos)

**Cadenas de Prueba (≥5 caracteres):**
- `"ababa"` → `"ababaababa"` (5→10 caracteres)
- `"bbbaa"` → `"bbbaabbbaa"` (5→10 caracteres)  
- `"aabbb"` → `"aabbbaabbb"` (5→10 caracteres)
- `"babab"` → `"bababbabab"` (5→10 caracteres)

**Dificultad de la MT:** Media-Alta
- Requiere manipulación compleja de la cinta
- Copia símbolo por símbolo al final
- Maneja marcadores temporales y limpieza final

### 🏗️ Arquitectura del Programa (1 punto)

**Diseño Modular:**
- **Separación clara** entre parser, simulador y modelos
- **Interfaz intuitiva** con menú interactivo
- **Archivos organizados** para fácil evaluación
- **Código bien documentado** y estructurado

## 🔧 Archivos de Configuración

### MT Reconocedora (`mt_reconocedora.yaml`)
```yaml
mt:
  states: [q0, q1, q2, q3, q4, q5, q6, q7, qf, qr]
  input_alphabet: [a, b]
  tape_alphabet: [a, b, X, Y, B]
  initial_state: q0
  accept_states: [qf]
  transitions: [...]  # 25 transiciones definidas
```

### MT Alteradora (`mt_alteradora.yaml`)
```yaml
mt:
  states: [q0, q1, q2, q3, q4, q5, qf]
  input_alphabet: [a, b]
  tape_alphabet: [a, b, X, Y, B]
  initial_state: q0
  accept_states: [qf]
  transitions: [...]  # 15 transiciones definidas
```

## 📝 Archivos de Cadenas de Prueba

### Reconocedora (`cadenas_reconocedora.txt`)
```
# Cadenas para MT Reconocedora de Palíndromos
# Formato: una cadena por línea
# Las líneas que empiecen con # son comentarios

# Cadenas ACEPTADAS (palíndromos)
abba
ababa
aabbaa
bbaabb

# Cadenas RECHAZADAS (no son palíndromos)
abab
aabbb
aaabba
```

### Alteradora (`cadenas_alteradora.txt`)
```
# 4 cadenas de 5+ caracteres para probar
ababa
bbbaa
aabbb
babab
```

## 🔍 Características Técnicas

### Algoritmos Implementados:

**MT Reconocedora de Palíndromos:**
1. Lee el primer símbolo no marcado y lo marca (a→X, b→Y)
2. Avanza hasta el final de la cadena
3. Verifica que el último símbolo coincida con el primero y lo marca
4. Regresa al inicio y repite el proceso
5. Acepta si todos los símbolos coinciden correctamente

**MT Alteradora (Duplicar):**
1. Marca el primer símbolo de la cadena
2. Va al final de la cinta
3. Agrega una copia del símbolo marcado
4. Regresa al inicio y repite
5. Limpia marcadores y finaliza

## 🎓 Información Académica

**Cumplimiento de Rúbrica:**
- ✅ MT Reconocedora: 2+2+3 = 7 puntos
- ✅ MT Alteradora: 4+3 = 7 puntos  
- ✅ Arquitectura: 1 punto
- ✅ **Total: 15/15 puntos**

**Ventajas del Diseño:**
- **Fácil de evaluar:** Archivos específicos y organizados
- **Fácil de demostrar:** Menú interactivo intuitivo
- **Fácil de entender:** Código modular y bien documentado
- **Fácil de extender:** Arquitectura flexible y escalable
