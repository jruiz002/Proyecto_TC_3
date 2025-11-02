# Simulador de Máquinas de Turing

Un simulador completo de Máquinas de Turing desarrollado en Python con arquitectura modular, capaz de simular tanto máquinas reconocedoras como alteradoras.

## 📋 Descripción

Este proyecto implementa un simulador de Máquinas de Turing que puede:

1. **Cargar definiciones de MT desde archivos YAML**
2. **Simular la ejecución paso a paso**
3. **Generar descripciones instantáneas (IDs) completas**
4. **Determinar si las cadenas son aceptadas o rechazadas**
5. **Visualizar el estado de la cinta en cada paso**

## 🏗️ Arquitectura del Proyecto

```
Proyecto_TC_3/
├── src/                          # Código fuente principal
│   ├── models/                   # Modelos de datos
│   │   ├── turing_machine.py     # Clase principal TuringMachine
│   │   ├── tape.py               # Representación de la cinta
│   │   ├── transition.py         # Transiciones de la MT
│   │   └── state.py              # Estados de la MT
│   ├── parser/                   # Parser YAML
│   │   └── yaml_parser.py        # Carga y validación de archivos
│   ├── simulator/                # Motor de simulación
│   │   ├── mt_simulator.py       # Simulador principal
│   │   └── instantaneous_description.py  # Descripciones instantáneas
│   └── utils/                    # Utilidades
│       ├── exceptions.py         # Excepciones personalizadas
│       └── validators.py         # Validadores de estructura
├── examples/                     # Ejemplos de MT
│   ├── mt_reconocedora_anbn.yaml # MT reconocedora a^n b^n
│   └── mt_alteradora_duplicar.yaml # MT alteradora (duplicar)
├── main.py                       # Interfaz de línea de comandos
├── requirements.txt              # Dependencias
└── README.md                     # Este archivo
```

## 🚀 Instalación y Configuración

### Requisitos

- Python 3.8 o superior
- PyYAML (se instala automáticamente)

### Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd Proyecto_TC_3
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verificar instalación:**
   ```bash
   python main.py --ayuda
   ```

## 📖 Uso

### Comandos Básicos

```bash
# Simular una MT desde archivo YAML
python main.py archivo_mt.yaml

# Ejecutar ejemplo reconocedor
python main.py --ejemplo reconocedora

# Ejecutar ejemplo alterador
python main.py --ejemplo alteradora

# Crear archivo de ejemplo simple
python main.py --ejemplo simple

# Simulación detallada (con todas las IDs)
python main.py archivo.yaml --verbose

# Simulación interactiva paso a paso
python main.py archivo.yaml --interactive

# Solo mostrar resultados finales
python main.py archivo.yaml --quiet
```

### Formato de Archivo YAML

```yaml
mt:
  states: [q0, q1, q2, qf]           # Lista de estados
  input_alphabet: [a, b]             # Alfabeto de entrada
  tape_alphabet: [a, b, B, X, Y]     # Alfabeto de la cinta
  initial_state: q0                  # Estado inicial
  accept_states: [qf]                # Estados de aceptación
  transitions:                       # Lista de transiciones
    - state: q0                      # Estado origen
      read: [a]                      # Símbolo(s) a leer
      write: [X]                     # Símbolo(s) a escribir
      move: R                        # Movimiento (L/R/S)
      next: q1                       # Estado destino
  inputs:                            # Cadenas de prueba
    - "aabb"
    - "ab"
    - "aaabbb"
```

## 🎯 Ejemplos Incluidos

### 1. Máquina Reconocedora: {aⁿbⁿ | n ≥ 1}

**Archivo:** `examples/mt_reconocedora_anbn.yaml`

**Descripción:** Reconoce cadenas que tienen el mismo número de 'a's seguidas del mismo número de 'b's.

**Algoritmo:**
1. Marca la primera 'a' con 'X'
2. Busca la primera 'b' y la marca con 'Y'
3. Regresa al inicio y repite hasta procesar toda la cadena
4. Acepta si todas las 'a's y 'b's fueron emparejadas

**Cadenas de prueba:**
- ✅ `"ab"`, `"aabb"`, `"aaabbb"`, `"aaaabbbb"`, `"aaaaabbbbb"`
- ❌ `"aab"`, `"abb"`, `"abab"`, `"baba"`, `"aaabbbaa"`

### 2. Máquina Alteradora: Duplicar Cadena

**Archivo:** `examples/mt_alteradora_duplicar.yaml`

**Descripción:** Toma una cadena w y la convierte en ww (duplicada).

**Algoritmo:**
1. Marca el primer símbolo de la cadena original
2. Va al final y agrega una copia del símbolo
3. Regresa al inicio y repite para cada símbolo
4. Limpia los marcadores y finaliza

**Cadenas de prueba:**
- `"ab"` → `"abab"`
- `"aab"` → `"aabaab"`
- `"bba"` → `"bbabba"`

## 🔧 Características Técnicas

### Componentes Principales

1. **TuringMachine**: Clase principal que representa la MT completa
2. **Tape**: Maneja la cinta infinita con expansión automática
3. **Transition**: Representa transiciones individuales
4. **MTSimulator**: Motor de simulación con control de pasos
5. **InstantaneousDescription**: Captura el estado completo en cada paso

### Funcionalidades Avanzadas

- **Validación completa** de archivos YAML
- **Visualización de cinta** con posición del cabezal
- **Simulación paso a paso** interactiva
- **Detección de bucles infinitos** con límite configurable
- **Manejo robusto de errores** con mensajes descriptivos
- **Soporte para múltiples cadenas** de entrada

## 📊 Salida del Simulador

### Información de la Máquina
```
📋 INFORMACIÓN DE LA MÁQUINA DE TURING
----------------------------------------
TuringMachine(
  States: ['q0', 'q1', 'q2', 'qf']
  Input Alphabet: ['a', 'b']
  Tape Alphabet: ['B', 'X', 'Y', 'a', 'b']
  Initial State: q0
  Accept States: ['qf']
  Transitions: 8
)
```

### Descripciones Instantáneas
```
🎯 SIMULACIÓN PARA: 'aabb'
--------------------------------------------------
📝 DESCRIPCIONES INSTANTÁNEAS:
  Inicial: (q0aabb)
  Paso 1: (Xq1abb)
    └─ Transición: δ(q0, [a]) = (q1, [X], R)
  Paso 2: (Xaq1bb)
    └─ Transición: δ(q1, [a]) = (q1, [a], R)
  ...
✅ RESULTADO: Cadena ACEPTADA en 12 pasos
```

### Resumen de Resultados
```
📊 RESUMEN DE RESULTADOS
============================================================
Total de cadenas probadas: 10
Cadenas aceptadas: 5
Cadenas rechazadas: 5
Tasa de aceptación: 50.0%

Detalle por cadena:
  'ab' → ✅ ACEPTADA (8 pasos)
  'aabb' → ✅ ACEPTADA (12 pasos)
  'aab' → ❌ RECHAZADA (6 pasos)
```

## 🧪 Casos de Prueba

### Para MT Reconocedora (aⁿbⁿ)

**Cadenas Aceptadas (≥5 caracteres):**
- `"aaaaabbbbb"` - Perfectamente balanceada
- `"aaabbb"` - Caso básico balanceado

**Cadenas Rechazadas (≥5 caracteres):**
- `"aaabbbaa"` - Tiene 'a's después de 'b's
- `"aabbba"` - Más 'b's que 'a's

### Para MT Alteradora (Duplicar)

**Cadenas de Prueba (≥5 caracteres):**
- `"ababa"` → `"ababaababa"`
- `"bbbaa"` → `"bbbaabbaa"`
- `"aabbb"` → `"aabbbaabbb"`
- `"babab"` → `"bababbabab"`

## 🎥 Video Demostrativo

Para la evaluación del proyecto, se debe crear un video mostrando:

1. **MT Reconocedora (7 puntos):**
   - Ejecución con 2 cadenas aceptadas (≥5 caracteres)
   - Ejecución con 2 cadenas rechazadas (≥5 caracteres)
   - Explicación de la dificultad de la MT

2. **MT Alteradora (7 puntos):**
   - Ejecución con 4 cadenas (≥5 caracteres)
   - Explicación de la dificultad de la MT

3. **Arquitectura del Programa (1 punto):**
   - Explicación del diseño modular
   - Demostración de las clases principales

## 🛠️ Desarrollo y Extensión

### Agregar Nueva MT

1. Crear archivo YAML con la definición
2. Validar estructura con el parser
3. Probar con el simulador
4. Documentar el algoritmo

### Modificar Comportamiento

- **Límite de pasos:** Modificar `max_steps` en `MTSimulator`
- **Símbolos de cinta:** Agregar al `tape_alphabet` en YAML
- **Visualización:** Personalizar métodos en `InstantaneousDescription`

## 📝 Notas Técnicas

- **Cinta infinita:** Se expande automáticamente según necesidad
- **Símbolo en blanco:** Por defecto 'B', configurable
- **Movimientos:** L (izquierda), R (derecha), S (quedarse)
- **Estados:** Nombres arbitrarios, distingue inicial y finales
- **Transiciones:** Determinísticas, una por combinación estado-símbolo

## 🤝 Contribución

Este proyecto fue desarrollado como parte del curso de Teoría de la Computación. Para contribuir:

1. Fork del repositorio
2. Crear rama para nueva funcionalidad
3. Implementar cambios con pruebas
4. Crear pull request con descripción detallada

---
**Curso:** Teoría de la Computación  
**Universidad:** Universidad del Valle de Guatemala  
**Fecha:** Noviembre 2025