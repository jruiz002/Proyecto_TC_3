"""
Clase InstantaneousDescription para representar descripciones instantáneas de una MT
"""

from typing import Optional
from ..models.tape import Tape


class InstantaneousDescription:
    """
    Representa una descripción instantánea (ID) de una Máquina de Turing
    Una ID captura el estado completo de la MT en un momento dado
    """
    
    def __init__(self, state: str, tape: Tape, step: int = 0, 
                 transition_applied: Optional[str] = None):
        """
        Inicializa una descripción instantánea
        
        Args:
            state: Estado actual de la MT
            tape: Estado actual de la cinta
            step: Número de paso en la simulación
            transition_applied: Descripción de la transición aplicada (opcional)
        """
        self.state = state
        self.tape_content = tape.get_tape_content()
        self.head_position = tape.head_position
        self.step = step
        self.transition_applied = transition_applied
        
        # Crear una copia del estado de la cinta para preservar el historial
        self.tape_visual = tape.get_visual_representation()
    
    def __str__(self) -> str:
        """
        Representación string de la descripción instantánea
        Formato: (estado, contenido_cinta_con_cabezal)
        """
        # Crear representación con el estado marcado en la posición del cabezal
        tape_chars = list(self.tape_content)
        
        # Asegurar que la cinta tenga suficientes caracteres
        while len(tape_chars) <= self.head_position:
            tape_chars.append('B')
        
        # Insertar el estado en la posición del cabezal
        if self.head_position < len(tape_chars):
            left_part = ''.join(tape_chars[:self.head_position])
            right_part = ''.join(tape_chars[self.head_position:])
            return f"({left_part}{self.state}{right_part})"
        else:
            return f"({''.join(tape_chars)}{self.state})"
    
    def get_detailed_representation(self) -> str:
        """
        Obtiene una representación detallada de la descripción instantánea
        
        Returns:
            String con representación detallada
        """
        result = f"Paso {self.step}:\n"
        result += f"  Estado: {self.state}\n"
        result += f"  Posición del cabezal: {self.head_position}\n"
        result += f"  Contenido de la cinta: {self.tape_content}\n"
        
        if self.transition_applied:
            result += f"  Transición aplicada: {self.transition_applied}\n"
        
        result += f"  ID: {self}\n"
        result += f"  Visualización de la cinta:\n"
        
        # Indentar la visualización de la cinta
        visual_lines = self.tape_visual.split('\n')
        for line in visual_lines:
            result += f"    {line}\n"
        
        return result
    
    def get_compact_representation(self) -> str:
        """
        Obtiene una representación compacta para listados
        
        Returns:
            String con representación compacta
        """
        transition_info = f" [{self.transition_applied}]" if self.transition_applied else ""
        return f"Paso {self.step}: {self}{transition_info}"
    
    def __repr__(self) -> str:
        return f"InstantaneousDescription(state='{self.state}', head_pos={self.head_position}, step={self.step})"