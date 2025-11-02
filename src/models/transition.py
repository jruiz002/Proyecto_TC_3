"""
Clase Transition para representar transiciones de una Máquina de Turing
"""

from typing import List, Tuple
from .state import State


class Transition:
    """
    Representa una transición en una Máquina de Turing
    """
    
    def __init__(self, from_state: str, read_symbols: List[str], 
                 write_symbols: List[str], move: str, to_state: str):
        """
        Inicializa una transición
        
        Args:
            from_state: Estado origen
            read_symbols: Símbolos a leer de la cinta
            write_symbols: Símbolos a escribir en la cinta
            move: Dirección de movimiento ('L', 'R', 'S')
            to_state: Estado destino
        """
        self.from_state = from_state
        self.read_symbols = read_symbols
        self.write_symbols = write_symbols
        self.move = move
        self.to_state = to_state
        
        # Validar que read y write tengan la misma longitud
        if len(read_symbols) != len(write_symbols):
            raise ValueError("read_symbols y write_symbols deben tener la misma longitud")
    
    def matches(self, current_state: str, tape_symbols: List[str]) -> bool:
        """
        Verifica si esta transición puede aplicarse dado el estado actual y símbolos de la cinta
        
        Args:
            current_state: Estado actual de la MT
            tape_symbols: Símbolos actuales en las posiciones relevantes de la cinta
            
        Returns:
            True si la transición puede aplicarse
        """
        return (self.from_state == current_state and 
                len(tape_symbols) == len(self.read_symbols) and
                all(tape_sym == read_sym for tape_sym, read_sym in zip(tape_symbols, self.read_symbols)))
    
    def apply(self) -> Tuple[str, List[str], str]:
        """
        Aplica la transición y retorna el nuevo estado, símbolos a escribir y movimiento
        
        Returns:
            Tupla con (nuevo_estado, símbolos_a_escribir, movimiento)
        """
        return self.to_state, self.write_symbols, self.move
    
    def __str__(self) -> str:
        read_str = ','.join(self.read_symbols)
        write_str = ','.join(self.write_symbols)
        return f"δ({self.from_state}, [{read_str}]) = ({self.to_state}, [{write_str}], {self.move})"
    
    def __repr__(self) -> str:
        return (f"Transition(from_state='{self.from_state}', "
                f"read_symbols={self.read_symbols}, "
                f"write_symbols={self.write_symbols}, "
                f"move='{self.move}', to_state='{self.to_state}')")