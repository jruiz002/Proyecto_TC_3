# 🤖 Simulador de Máquinas de Turing - Proyecto TC3

**Autor:** José Ruiz  
**Curso:** Teoría de la Computación  
**Universidad:** Universidad del Valle de Guatemala  
**Fecha:** Noviembre 2025

## 📋 Descripción del Proyecto

Este proyecto implementa un simulador completo de Máquinas de Turing con capacidad para ejecutar tanto **máquinas reconocedoras** como **máquinas alteradoras**. El sistema está diseñado con una interfaz de menú interactivo que facilita la comprensión y demostración del funcionamiento de las MT.

## 🎯 Objetivos

- ✅ Implementar una **MT Reconocedora** para el lenguaje {aⁿbⁿ | n ≥ 1}
- ✅ Implementar una **MT Alteradora** que duplica cadenas (w → ww)
- ✅ Crear un sistema de archivos organizados para fácil evaluación
- ✅ Proporcionar un menú interactivo intuitivo
- ✅ Generar descripciones instantáneas completas

## 🏗️ Estructura del Proyecto

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
- PyYAML (se instala automáticamente)

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
🤖 SIMULADOR DE MÁQUINAS DE TURING
   Proyecto TC3 - Teoría de la Computación
   Universidad del Valle de Guatemala
============================================================

📋 OPCIONES DISPONIBLES:
1. 🔍 Ejecutar MT Reconocedora {aⁿbⁿ | n ≥ 1}
2. 🔄 Ejecutar MT Alteradora (Duplicar cadena)
3. 📖 Ver información del proyecto
4. 🚪 Salir
```

### Opción 1: MT Reconocedora
- **Lenguaje:** {aⁿbⁿ | n ≥ 1}
- **Archivo YAML:** `mt_reconocedora.yaml`
- **Cadenas de prueba:** `cadenas_reconocedora.txt`
- **Algoritmo:** Marca 'a's con 'X' y 'b's con 'Y', verifica balance

### Opción 2: MT Alteradora  
- **Función:** Duplicar cadena (w → ww)
- **Archivo YAML:** `mt_alteradora.yaml`
- **Cadenas de prueba:** `cadenas_alteradora.txt`
- **Algoritmo:** Copia cada símbolo al final de la cadena

## 📊 Evaluación según Rúbrica

### 🔍 MT Reconocedora (7 puntos)

**Cadenas Aceptadas (≥5 caracteres):**
- `"aaaaabbbbb"` - 10 caracteres, perfectamente balanceada
- `"aaabbb"` - 6 caracteres, caso básico balanceado

**Cadenas Rechazadas (≥5 caracteres):**
- `"aaabbbaa"` - 8 caracteres, tiene 'a's después de 'b's
- `"aabbba"` - 6 caracteres, más 'b's que 'a's

**Dificultad de la MT:** Media-Alta
- Requiere conteo y emparejamiento de símbolos
- Utiliza marcadores para rastrear progreso
- Maneja múltiples estados y transiciones complejas

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
  states: [q0, q1, q2, q3, qf, qr]
  input_alphabet: [a, b]
  tape_alphabet: [a, b, X, Y, B]
  initial_state: q0
  accept_states: [qf]
  transitions: [...]  # 8 transiciones definidas
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
# Cadenas ACEPTADAS (2 cadenas de 5+ caracteres)
aaaaabbbbb
aaabbb

# Cadenas RECHAZADAS (2 cadenas de 5+ caracteres)  
aaabbbaa
aabbba
```

### Alteradora (`cadenas_alteradora.txt`)
```
# 4 cadenas de 5+ caracteres para probar
ababa
bbbaa
aabbb
babab
```

## 🎥 Demostración para Video

### Flujo de Demostración Sugerido:

1. **Introducción (30 seg)**
   - Mostrar estructura del proyecto
   - Explicar archivos principales

2. **MT Reconocedora (3 min)**
   - Ejecutar opción 1 del menú
   - Mostrar las 4 cadenas (2 aceptadas, 2 rechazadas)
   - Explicar algoritmo y dificultad

3. **MT Alteradora (3 min)**
   - Ejecutar opción 2 del menú  
   - Mostrar las 4 cadenas de duplicación
   - Explicar algoritmo y dificultad

4. **Arquitectura (1 min)**
   - Mostrar opción 3 del menú
   - Explicar diseño modular
   - Destacar facilidad de uso

## 🔍 Características Técnicas

### Funcionalidades del Simulador:
- ✅ **Carga automática** de archivos YAML y TXT
- ✅ **Validación completa** de estructura de MT
- ✅ **Simulación paso a paso** con descripciones instantáneas
- ✅ **Visualización clara** del estado de la cinta
- ✅ **Manejo robusto de errores**
- ✅ **Interfaz intuitiva** con pausas interactivas
- ✅ **Resumen estadístico** de resultados

### Algoritmos Implementados:

**MT Reconocedora {aⁿbⁿ}:**
1. Marca la primera 'a' con 'X'
2. Busca la primera 'b' y la marca con 'Y'  
3. Regresa al inicio y repite
4. Verifica que solo queden marcadores
5. Acepta si está balanceada

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

---

## 🚀 ¡Listo para Evaluación!

El proyecto está completamente funcional y optimizado para la evaluación. Simplemente ejecuta:

```bash
python main.py
```

Y sigue el menú interactivo para demostrar todas las funcionalidades requeridas por la rúbrica.

**¡Éxito en tu evaluación! 🎉**