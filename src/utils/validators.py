"""
Validadores para la estructura de archivos YAML y configuraciones de MT
"""

from typing import Dict, List, Any
from .exceptions import YAMLParsingError


def validate_yaml_structure(data: Dict[str, Any]) -> None:
    """
    Valida que la estructura del YAML sea correcta para una MT
    
    Args:
        data: Diccionario con los datos del YAML
        
    Raises:
        YAMLParsingError: Si la estructura no es válida
    """
    required_fields = ['mt']
    mt_required_fields = [
        'states', 'input_alphabet', 'tape_alphabet', 
        'initial_state', 'accept_states', 'transitions'
    ]
    
    # Verificar campos principales
    for field in required_fields:
        if field not in data:
            raise YAMLParsingError(f"Campo requerido '{field}' no encontrado")
    
    mt_data = data['mt']
    
    # Verificar campos de la MT
    for field in mt_required_fields:
        if field not in mt_data:
            raise YAMLParsingError(f"Campo requerido 'mt.{field}' no encontrado")
    
    # Validar tipos de datos
    if not isinstance(mt_data['states'], list):
        raise YAMLParsingError("'states' debe ser una lista")
    
    if not isinstance(mt_data['input_alphabet'], list):
        raise YAMLParsingError("'input_alphabet' debe ser una lista")
    
    if not isinstance(mt_data['tape_alphabet'], list):
        raise YAMLParsingError("'tape_alphabet' debe ser una lista")
    
    if not isinstance(mt_data['accept_states'], list):
        raise YAMLParsingError("'accept_states' debe ser una lista")
    
    if not isinstance(mt_data['transitions'], list):
        raise YAMLParsingError("'transitions' debe ser una lista")
    
    # Validar que el estado inicial esté en la lista de estados
    if mt_data['initial_state'] not in mt_data['states']:
        raise YAMLParsingError("El estado inicial debe estar en la lista de estados")
    
    # Validar que los estados de aceptación estén en la lista de estados
    for accept_state in mt_data['accept_states']:
        if accept_state not in mt_data['states']:
            raise YAMLParsingError(f"Estado de aceptación '{accept_state}' no está en la lista de estados")
    
    # Validar que el alfabeto de entrada esté contenido en el alfabeto de la cinta
    for symbol in mt_data['input_alphabet']:
        if symbol not in mt_data['tape_alphabet']:
            raise YAMLParsingError(f"Símbolo '{symbol}' del alfabeto de entrada no está en el alfabeto de la cinta")
    
    # Validar estructura de transiciones
    for i, transition in enumerate(mt_data['transitions']):
        validate_transition_structure(transition, i, mt_data)


def validate_transition_structure(transition: Dict[str, Any], index: int, mt_data: Dict[str, Any]) -> None:
    """
    Valida la estructura de una transición individual
    
    Args:
        transition: Diccionario con los datos de la transición
        index: Índice de la transición para mensajes de error
        mt_data: Datos completos de la MT para validaciones cruzadas
    """
    required_fields = ['state', 'read', 'write', 'move', 'next']
    
    for field in required_fields:
        if field not in transition:
            raise YAMLParsingError(f"Campo '{field}' faltante en transición {index}")
    
    # Validar que el estado esté en la lista de estados
    if transition['state'] not in mt_data['states']:
        raise YAMLParsingError(f"Estado '{transition['state']}' en transición {index} no está en la lista de estados")
    
    # Validar que el siguiente estado esté en la lista de estados
    if transition['next'] not in mt_data['states']:
        raise YAMLParsingError(f"Estado siguiente '{transition['next']}' en transición {index} no está en la lista de estados")
    
    # Validar que read y write sean listas
    if not isinstance(transition['read'], list):
        raise YAMLParsingError(f"'read' en transición {index} debe ser una lista")
    
    if not isinstance(transition['write'], list):
        raise YAMLParsingError(f"'write' en transición {index} debe ser una lista")
    
    # Validar que read y write tengan la misma longitud
    if len(transition['read']) != len(transition['write']):
        raise YAMLParsingError(f"'read' y 'write' en transición {index} deben tener la misma longitud")
    
    # Validar símbolos de lectura y escritura
    for symbol in transition['read'] + transition['write']:
        if symbol not in mt_data['tape_alphabet']:
            raise YAMLParsingError(f"Símbolo '{symbol}' en transición {index} no está en el alfabeto de la cinta")
    
    # Validar movimiento
    if transition['move'] not in ['L', 'R', 'S']:
        raise YAMLParsingError(f"Movimiento '{transition['move']}' en transición {index} debe ser 'L', 'R' o 'S'")