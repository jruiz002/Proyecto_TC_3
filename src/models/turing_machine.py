"""
Clase TuringMachine para representar una Máquina de Turing completa
"""

from typing import List, Dict, Optional
from .state import State
from .transition import Transition
from .tape import Tape
from ..utils.exceptions import InvalidStateError, InvalidTransitionError


class TuringMachine:
    """
    Representa una Máquina de Turing completa
    """
    
    def __init__(self, states: List[str], input_alphabet: List[str], 
                 tape_alphabet: List[str], initial_state: str, 
                 accept_states: List[str], transitions: List[Dict],
                 blank_symbol: str = "B"):
        """
        Inicializa una Máquina de Turing
        
        Args:
            states: Lista de nombres de estados
            input_alphabet: Alfabeto de entrada
            tape_alphabet: Alfabeto de la cinta
            initial_state: Estado inicial
            accept_states: Lista de estados de aceptación
            transitions: Lista de transiciones en formato dict
            blank_symbol: Símbolo en blanco
        """
        self.states = {name: State(name, name in accept_states) for name in states}
        self.input_alphabet = set(input_alphabet)
        self.tape_alphabet = set(tape_alphabet)
        self.initial_state = initial_state
        self.accept_states = set(accept_states)
        self.blank_symbol = blank_symbol
        
        # Validar que el estado inicial exista
        if initial_state not in self.states:
            raise InvalidStateError(f"Estado inicial '{initial_state}' no está en la lista de estados")
        
        # Validar que todos los estados de aceptación existan
        for accept_state in accept_states:
            if accept_state not in self.states:
                raise InvalidStateError(f"Estado de aceptación '{accept_state}' no está en la lista de estados")
        
        # Crear transiciones
        self.transitions = []
        for trans_dict in transitions:
            transition = Transition(
                from_state=trans_dict['state'],
                read_symbols=trans_dict['read'],
                write_symbols=trans_dict['write'],
                move=trans_dict['move'],
                to_state=trans_dict['next']
            )
            self.transitions.append(transition)
        
        # Crear índice de transiciones para búsqueda rápida
        self._build_transition_index()
    
    def _build_transition_index(self) -> None:
        """Construye un índice para búsqueda rápida de transiciones"""
        self.transition_index = {}
        for transition in self.transitions:
            key = (transition.from_state, tuple(transition.read_symbols))
            if key in self.transition_index:
                raise InvalidTransitionError(f"Transición duplicada encontrada: {key}")
            self.transition_index[key] = transition
    
    def get_transition(self, current_state: str, tape_symbols: List[str]) -> Optional[Transition]:
        """
        Busca una transición aplicable dado el estado actual y símbolos de la cinta
        
        Args:
            current_state: Estado actual
            tape_symbols: Símbolos actuales en la cinta
            
        Returns:
            Transición aplicable o None si no existe
        """
        key = (current_state, tuple(tape_symbols))
        return self.transition_index.get(key)
    
    def is_accept_state(self, state: str) -> bool:
        """
        Verifica si un estado es de aceptación
        
        Args:
            state: Nombre del estado
            
        Returns:
            True si es estado de aceptación
        """
        return state in self.accept_states
    
    def validate_input(self, input_string: str) -> bool:
        """
        Valida que una cadena de entrada use solo símbolos del alfabeto de entrada
        
        Args:
            input_string: Cadena a validar
            
        Returns:
            True si la cadena es válida
        """
        return all(symbol in self.input_alphabet for symbol in input_string)
    
    def create_tape(self, input_string: str) -> Tape:
        """
        Crea una cinta inicializada con la cadena de entrada
        
        Args:
            input_string: Cadena inicial
            
        Returns:
            Cinta inicializada
        """
        return Tape(input_string, self.blank_symbol)
    
    def __str__(self) -> str:
        return (f"TuringMachine(\n"
                f"  States: {list(self.states.keys())}\n"
                f"  Input Alphabet: {sorted(self.input_alphabet)}\n"
                f"  Tape Alphabet: {sorted(self.tape_alphabet)}\n"
                f"  Initial State: {self.initial_state}\n"
                f"  Accept States: {sorted(self.accept_states)}\n"
                f"  Transitions: {len(self.transitions)}\n"
                f")")
    
    def get_transition_summary(self) -> str:
        """
        Obtiene un resumen de todas las transiciones
        
        Returns:
            String con el resumen de transiciones
        """
        summary = "Transiciones:\n"
        for i, transition in enumerate(self.transitions, 1):
            summary += f"  {i}. {transition}\n"
        return summary