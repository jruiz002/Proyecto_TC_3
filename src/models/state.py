"""
Clase State para representar estados de una Máquina de Turing
"""

from typing import Set


class State:
    """
    Representa un estado en una Máquina de Turing
    """
    
    def __init__(self, name: str, is_accept: bool = False):
        """
        Inicializa un estado
        
        Args:
            name: Nombre del estado
            is_accept: Si es un estado de aceptación
        """
        self.name = name
        self.is_accept = is_accept
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"State('{self.name}', is_accept={self.is_accept})"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, State):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        return False
    
    def __hash__(self) -> int:
        return hash(self.name)