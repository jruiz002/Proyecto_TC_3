#!/usr/bin/env python3
"""
Simulador de Máquinas de Turing
Interfaz de línea de comandos principal

Uso:
    python main.py <archivo_yaml>
    python main.py --ejemplo <tipo>
    python main.py --ayuda
"""

import sys
import argparse
from pathlib import Path
from typing import List, Tuple

# Agregar el directorio src al path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from src.parser.yaml_parser import YAMLParser
from src.simulator.mt_simulator import MTSimulator
from src.utils.exceptions import MTException, YAMLParsingError


def print_banner():
    """Imprime el banner del programa"""
    print("=" * 60)
    print("    SIMULADOR DE MÁQUINAS DE TURING")
    print("    Proyecto de Teoría de la Computación")
    print("=" * 60)
    print()


def print_machine_info(turing_machine):
    """Imprime información de la máquina de Turing"""
    print("📋 INFORMACIÓN DE LA MÁQUINA DE TURING")
    print("-" * 40)
    print(turing_machine)
    print()
    print("🔄 TRANSICIONES:")
    print(turing_machine.get_transition_summary())


def print_simulation_results(input_string: str, accepted: bool, ids: List, result: str, verbose: bool = True):
    """Imprime los resultados de una simulación"""
    print(f"🎯 SIMULACIÓN PARA: '{input_string}'")
    print("-" * 50)
    
    if verbose:
        print("📝 DESCRIPCIONES INSTANTÁNEAS:")
        for i, id_desc in enumerate(ids):
            if i == 0:
                print(f"  Inicial: {id_desc}")
            else:
                print(f"  Paso {i}: {id_desc}")
                if hasattr(id_desc, 'transition_applied') and id_desc.transition_applied:
                    print(f"    └─ Transición: {id_desc.transition_applied}")
        print()
    
    # Resultado final
    status_icon = "✅" if accepted else "❌"
    print(f"{status_icon} RESULTADO: {result}")
    print()


def simulate_file(file_path: str, verbose: bool = True, interactive: bool = False):
    """Simula una MT desde un archivo YAML"""
    try:
        # Cargar y parsear el archivo
        print(f"📂 Cargando archivo: {file_path}")
        data = YAMLParser.load_from_file(file_path)
        turing_machine = YAMLParser.parse_turing_machine(data)
        test_inputs = YAMLParser.get_test_inputs(data)
        
        print_machine_info(turing_machine)
        
        # Crear simulador
        simulator = MTSimulator(turing_machine)
        
        # Simular cada entrada
        print("🚀 INICIANDO SIMULACIONES")
        print("=" * 60)
        
        results = []
        for i, input_string in enumerate(test_inputs, 1):
            print(f"\n[{i}/{len(test_inputs)}] ", end="")
            
            if interactive:
                input(f"Presiona Enter para simular '{input_string}'...")
            
            accepted, ids, result = simulator.simulate(input_string)
            results.append((input_string, accepted, len(ids) - 1, result))
            
            print_simulation_results(input_string, accepted, ids, result, verbose)
        
        # Resumen final
        print_summary(results)
        
    except YAMLParsingError as e:
        print(f"❌ Error al parsear YAML: {e}")
        sys.exit(1)
    except MTException as e:
        print(f"❌ Error en la Máquina de Turing: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ Archivo no encontrado: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        sys.exit(1)


def print_summary(results: List[Tuple[str, bool, int, str]]):
    """Imprime un resumen de los resultados"""
    print("📊 RESUMEN DE RESULTADOS")
    print("=" * 60)
    
    accepted_count = sum(1 for _, accepted, _, _ in results)
    total_count = len(results)
    
    print(f"Total de cadenas probadas: {total_count}")
    print(f"Cadenas aceptadas: {accepted_count}")
    print(f"Cadenas rechazadas: {total_count - accepted_count}")
    print(f"Tasa de aceptación: {accepted_count/total_count*100:.1f}%")
    print()
    
    print("Detalle por cadena:")
    for input_str, accepted, steps, result in results:
        status = "✅ ACEPTADA" if accepted else "❌ RECHAZADA"
        print(f"  '{input_str}' → {status} ({steps} pasos)")


def create_example_file(example_type: str):
    """Crea un archivo de ejemplo"""
    examples = {
        'reconocedora': 'examples/mt_reconocedora_anbn.yaml',
        'alteradora': 'examples/mt_alteradora_duplicar.yaml',
        'simple': YAMLParser.create_sample_yaml()
    }
    
    if example_type not in examples:
        print(f"❌ Tipo de ejemplo no válido: {example_type}")
        print(f"Tipos disponibles: {', '.join(examples.keys())}")
        return
    
    if example_type == 'simple':
        # Crear archivo simple
        with open('ejemplo_simple.yaml', 'w', encoding='utf-8') as f:
            f.write(examples[example_type])
        print("✅ Archivo 'ejemplo_simple.yaml' creado exitosamente")
    else:
        example_path = examples[example_type]
        if Path(example_path).exists():
            print(f"✅ Ejemplo disponible en: {example_path}")
            simulate_file(example_path)
        else:
            print(f"❌ Archivo de ejemplo no encontrado: {example_path}")


def main():
    """Función principal"""
    parser = argparse.ArgumentParser(
        description="Simulador de Máquinas de Turing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python main.py mt_config.yaml              # Simular MT desde archivo
  python main.py --ejemplo reconocedora      # Ejecutar ejemplo reconocedor
  python main.py --ejemplo alteradora        # Ejecutar ejemplo alterador
  python main.py --ejemplo simple            # Crear ejemplo simple
  python main.py archivo.yaml --verbose      # Simulación detallada
  python main.py archivo.yaml --interactive  # Simulación paso a paso
        """
    )
    
    parser.add_argument('archivo', nargs='?', help='Archivo YAML con la definición de la MT')
    parser.add_argument('--ejemplo', choices=['reconocedora', 'alteradora', 'simple'],
                       help='Crear o ejecutar un ejemplo predefinido')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Mostrar descripciones instantáneas detalladas')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Simulación interactiva paso a paso')
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Mostrar solo resultados finales')
    
    args = parser.parse_args()
    
    # Mostrar banner
    if not args.quiet:
        print_banner()
    
    # Procesar argumentos
    if args.ejemplo:
        create_example_file(args.ejemplo)
    elif args.archivo:
        verbose = args.verbose and not args.quiet
        simulate_file(args.archivo, verbose=verbose, interactive=args.interactive)
    else:
        parser.print_help()
        print("\n💡 Sugerencia: Comienza con 'python main.py --ejemplo simple' para crear un ejemplo básico")


if __name__ == "__main__":
    main()