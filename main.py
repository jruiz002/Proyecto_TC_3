#!/usr/bin/env python3
"""
Simulador de Máquinas de Turing - Proyecto TC3
Autor: José Ruiz
Universidad del Valle de Guatemala
Teoría de la Computación - Noviembre 2025
"""

import os
import sys
from src.parser.yaml_parser import YAMLParser
from src.simulator.mt_simulator import MTSimulator
from src.utils.exceptions import TuringMachineError

class TuringMachineMenu:
    """Menú interactivo para el simulador de Máquinas de Turing"""
    
    def __init__(self):
        pass
        
    def mostrar_menu_principal(self):
        """Muestra el menú principal del simulador"""
        print("\n" + "="*60)
        print("🤖 SIMULADOR DE MÁQUINAS DE TURING")
        print("   Proyecto TC3 - Teoría de la Computación")
        print("   Universidad del Valle de Guatemala")
        print("="*60)
        print("\n📋 OPCIONES DISPONIBLES:")
        print("1. 🔍 Ejecutar MT Reconocedora {aⁿbⁿ | n ≥ 1}")
        print("2. 🔄 Ejecutar MT Alteradora (Duplicar cadena)")
        print("3. 📖 Ver información del proyecto")
        print("4. 🚪 Salir")
        print("-"*60)
        
    def leer_cadenas_desde_archivo(self, archivo_txt):
        """Lee las cadenas de prueba desde un archivo TXT"""
        try:
            with open(archivo_txt, 'r', encoding='utf-8') as f:
                cadenas = []
                for linea in f:
                    linea = linea.strip()
                    # Ignorar líneas vacías y comentarios
                    if linea and not linea.startswith('#'):
                        cadenas.append(linea)
                return cadenas
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo {archivo_txt}")
            return []
        except Exception as e:
            print(f"❌ Error al leer {archivo_txt}: {e}")
            return []
    
    def ejecutar_mt_reconocedora(self):
        """Ejecuta la MT reconocedora con las cadenas del archivo"""
        print("\n" + "🔍 MÁQUINA DE TURING RECONOCEDORA".center(60, "="))
        print("Lenguaje: {aⁿbⁿ | n ≥ 1}")
        print("Descripción: Reconoce cadenas con igual número de 'a's seguidas de 'b's")
        print("-"*60)
        
        # Cargar la MT desde el archivo YAML
        try:
            data = YAMLParser.load_from_file("mt_reconocedora.yaml")
            mt = YAMLParser.parse_turing_machine(data)
            print("✅ MT reconocedora cargada exitosamente")
        except Exception as e:
            print(f"❌ Error al cargar MT reconocedora: {e}")
            return
        
        # Leer cadenas de prueba
        cadenas = self.leer_cadenas_desde_archivo("cadenas_reconocedora.txt")
        if not cadenas:
            print("❌ No se pudieron cargar las cadenas de prueba")
            return
        
        print(f"\n📝 Cadenas a probar: {cadenas}")
        input("\n⏸️  Presiona ENTER para comenzar la simulación...")
        
        # Ejecutar simulación para cada cadena
        resultados = []
        simulator = MTSimulator(mt)  # Crear simulador con la MT cargada
        
        for i, cadena in enumerate(cadenas, 1):
            print(f"\n{'='*20} CADENA {i}: '{cadena}' {'='*20}")
            try:
                accepted, ids, final_result = simulator.simulate(cadena)
                resultados.append((cadena, accepted, len(ids)))
                
                if accepted:
                    print(f"✅ RESULTADO: Cadena '{cadena}' ACEPTADA en {len(ids)} pasos")
                else:
                    print(f"❌ RESULTADO: Cadena '{cadena}' RECHAZADA en {len(ids)} pasos")
                    
            except Exception as e:
                print(f"❌ Error simulando '{cadena}': {e}")
                resultados.append((cadena, False, 0))
            
            if i < len(cadenas):
                input("\n⏸️  Presiona ENTER para continuar con la siguiente cadena...")
        
        # Mostrar resumen
        self.mostrar_resumen_resultados(resultados, "Reconocedora")
    
    def ejecutar_mt_alteradora(self):
        """Ejecuta la MT alteradora con las cadenas del archivo"""
        print("\n" + "🔄 MÁQUINA DE TURING ALTERADORA".center(60, "="))
        print("Función: Duplicar cadena (w → ww)")
        print("Descripción: Toma una cadena y la duplica al final")
        print("-"*60)
        
        # Cargar la MT desde el archivo YAML
        try:
            data = YAMLParser.load_from_file("mt_alteradora.yaml")
            mt = YAMLParser.parse_turing_machine(data)
            print("✅ MT alteradora cargada exitosamente")
        except Exception as e:
            print(f"❌ Error al cargar MT alteradora: {e}")
            return
        
        # Leer cadenas de prueba
        cadenas = self.leer_cadenas_desde_archivo("cadenas_alteradora.txt")
        if not cadenas:
            print("❌ No se pudieron cargar las cadenas de prueba")
            return
        
        print(f"\n📝 Cadenas a probar: {cadenas}")
        input("\n⏸️  Presiona ENTER para comenzar la simulación...")
        
        # Ejecutar simulación para cada cadena
        resultados = []
        simulator = MTSimulator(mt)  # Crear simulador con la MT cargada
        
        for i, cadena in enumerate(cadenas, 1):
            print(f"\n{'='*20} CADENA {i}: '{cadena}' {'='*20}")
            try:
                accepted, ids, final_result = simulator.simulate(cadena)
                resultados.append((cadena, accepted, len(ids)))
                
                if accepted:
                    print(f"✅ RESULTADO: Cadena '{cadena}' procesada exitosamente en {len(ids)} pasos")
                    print(f"🔄 Resultado final: '{final_result}'")
                else:
                    print(f"❌ RESULTADO: Error procesando '{cadena}' en {len(ids)} pasos")
                    
            except Exception as e:
                print(f"❌ Error simulando '{cadena}': {e}")
                resultados.append((cadena, False, 0))
            
            if i < len(cadenas):
                input("\n⏸️  Presiona ENTER para continuar con la siguiente cadena...")
        
        # Mostrar resumen
        self.mostrar_resumen_resultados(resultados, "Alteradora")
    
    def mostrar_resumen_resultados(self, resultados, tipo_mt):
        """Muestra un resumen de los resultados de la simulación"""
        print(f"\n{'📊 RESUMEN DE RESULTADOS - MT ' + tipo_mt.upper():=^60}")
        
        exitosas = sum(1 for _, aceptada, _ in resultados if aceptada)
        total = len(resultados)
        
        print(f"Total de cadenas probadas: {total}")
        print(f"Cadenas procesadas exitosamente: {exitosas}")
        print(f"Cadenas con error: {total - exitosas}")
        print(f"Tasa de éxito: {(exitosas/total)*100:.1f}%")
        
        print(f"\n📋 Detalle por cadena:")
        for cadena, aceptada, pasos in resultados:
            estado = "✅ ÉXITO" if aceptada else "❌ ERROR"
            print(f"  '{cadena}' → {estado} ({pasos} pasos)")
        
        print("="*60)
    
    def mostrar_informacion_proyecto(self):
        """Muestra información sobre el proyecto"""
        print("\n" + "📖 INFORMACIÓN DEL PROYECTO".center(60, "="))
        print("""
🎯 OBJETIVO:
   Implementar un simulador de Máquinas de Turing que pueda ejecutar
   tanto máquinas reconocedoras como alteradoras.

🏗️ ESTRUCTURA DEL PROYECTO:
   • mt_reconocedora.yaml    - Definición de MT reconocedora
   • mt_alteradora.yaml      - Definición de MT alteradora  
   • cadenas_reconocedora.txt - Cadenas de prueba para reconocedora
   • cadenas_alteradora.txt   - Cadenas de prueba para alteradora
   • src/                     - Código fuente del simulador
   • main.py                  - Este menú interactivo

🔍 MT RECONOCEDORA:
   • Lenguaje: {aⁿbⁿ | n ≥ 1}
   • Algoritmo: Marca 'a's con 'X' y 'b's con 'Y', verifica balance
   • Dificultad: Media (requiere conteo y verificación)

🔄 MT ALTERADORA:
   • Función: Duplicar cadena (w → ww)
   • Algoritmo: Copia cada símbolo al final de la cadena
   • Dificultad: Media (requiere manipulación de cinta)

👨‍💻 AUTOR: José Ruiz
📚 CURSO: Teoría de la Computación
🏫 UNIVERSIDAD: Universidad del Valle de Guatemala
📅 FECHA: Noviembre 2025
        """)
        print("="*60)
    
    def ejecutar(self):
        """Ejecuta el menú principal del simulador"""
        while True:
            try:
                self.mostrar_menu_principal()
                opcion = input("🔢 Selecciona una opción (1-4): ").strip()
                
                if opcion == "1":
                    self.ejecutar_mt_reconocedora()
                elif opcion == "2":
                    self.ejecutar_mt_alteradora()
                elif opcion == "3":
                    self.mostrar_informacion_proyecto()
                elif opcion == "4":
                    print("\n👋 ¡Gracias por usar el simulador de Máquinas de Turing!")
                    print("🎓 Proyecto TC3 - Universidad del Valle de Guatemala")
                    break
                else:
                    print("❌ Opción inválida. Por favor selecciona 1, 2, 3 o 4.")
                
                if opcion in ["1", "2", "3"]:
                    input("\n⏸️  Presiona ENTER para volver al menú principal...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Simulación interrumpida por el usuario. ¡Hasta luego!")
                break
            except Exception as e:
                print(f"\n❌ Error inesperado: {e}")
                input("⏸️  Presiona ENTER para continuar...")

def main():
    """Función principal del programa"""
    # Verificar que estamos en el directorio correcto
    archivos_requeridos = [
        "mt_reconocedora.yaml",
        "mt_alteradora.yaml", 
        "cadenas_reconocedora.txt",
        "cadenas_alteradora.txt"
    ]
    
    for archivo in archivos_requeridos:
        if not os.path.exists(archivo):
            print(f"❌ Error: No se encontró el archivo requerido '{archivo}'")
            print("🔧 Asegúrate de ejecutar el programa desde el directorio del proyecto")
            sys.exit(1)
    
    # Iniciar el menú
    menu = TuringMachineMenu()
    menu.ejecutar()

if __name__ == "__main__":
    main()