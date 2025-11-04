"""
Clase Tape para representar la cinta de una Máquina de Turing
"""

from typing import Optional


class Tape:
    """
    Representa la cinta de una Máquina de Turing
    """
    
    def __init__(self, input_string: str = "", blank_symbol: str = "B"):
        """
        Inicializa la cinta con una cadena de entrada
        
        Args:
            input_string: Cadena inicial en la cinta
            blank_symbol: Símbolo en blanco
        """
        self.blank_symbol = blank_symbol
        self.tape = list(input_string) if input_string else [blank_symbol]
        self.head_position = 0
        
        # Asegurar que la cinta tenga al menos un símbolo
        if not self.tape:
            self.tape = [blank_symbol]
    
    def read(self) -> str:
        """
        Lee el símbolo en la posición actual del cabezal
        
        Returns:
            Símbolo en la posición actual
        """
        self._ensure_position_exists()
        return self.tape[self.head_position]
    
    def write(self, symbol: str) -> None:
        """
        Escribe un símbolo en la posición actual del cabezal
        
        Args:
            symbol: Símbolo a escribir
        """
        self._ensure_position_exists()
        self.tape[self.head_position] = symbol
    
    def move_left(self) -> None:
        """Mueve el cabezal una posición a la izquierda"""
        self.head_position -= 1
        if self.head_position < 0:
            # Expandir la cinta hacia la izquierda
            self.tape.insert(0, self.blank_symbol)
            self.head_position = 0
    
    def move_right(self) -> None:
        """Mueve el cabezal una posición a la derecha"""
        self.head_position += 1
        self._ensure_position_exists()
    
    def move(self, direction: str) -> None:
        """
        Mueve el cabezal en la dirección especificada
        
        Args:
            direction: 'L' para izquierda, 'R' para derecha, 'S' para quedarse
        """
        if direction == 'L':
            self.move_left()
        elif direction == 'R':
            self.move_right()
        elif direction == 'S':
            pass  # No se mueve
        else:
            raise ValueError(f"Dirección inválida: {direction}")
    
    def _ensure_position_exists(self) -> None:
        """Asegura que la posición del cabezal exista en la cinta"""
        while len(self.tape) <= self.head_position:
            self.tape.append(self.blank_symbol)
    
    def get_tape_content(self, start: Optional[int] = None, end: Optional[int] = None) -> str:
        """
        Obtiene el contenido de la cinta como string
        
        Args:
            start: Posición inicial (opcional)
            end: Posición final (opcional)
            
        Returns:
            Contenido de la cinta como string
        """
        if start is None:
            start = 0
        if end is None:
            end = len(self.tape)
        
        # Encontrar el primer y último símbolo no en blanco para mostrar contenido relevante
        first_non_blank = 0
        last_non_blank = len(self.tape) - 1
        
        for i, symbol in enumerate(self.tape):
            if symbol != self.blank_symbol:
                first_non_blank = i
                break
        
        for i in range(len(self.tape) - 1, -1, -1):
            if self.tape[i] != self.blank_symbol:
                last_non_blank = i
                break
        
        # Incluir al menos la posición del cabezal
        start = min(start, first_non_blank, self.head_position)
        end = max(end, last_non_blank + 1, self.head_position + 1)
        
        return ''.join(self.tape[start:end])
    
    def get_visual_representation(self, context: int = 5) -> str:
        """
        Obtiene una representación visual de la cinta con el cabezal marcado
        
        Args:
            context: Número de posiciones a mostrar alrededor del cabezal
            
        Returns:
            Representación visual de la cinta
        """
        # Determinar rango a mostrar
        start = max(0, self.head_position - context)
        end = min(len(self.tape), self.head_position + context + 1)
        
        # Asegurar que el rango incluya contenido relevante
        first_non_blank = next((i for i, s in enumerate(self.tape) if s != self.blank_symbol), 0)
        last_non_blank = next((i for i in range(len(self.tape) - 1, -1, -1) if self.tape[i] != self.blank_symbol), len(self.tape) - 1)
        
        start = min(start, first_non_blank)
        end = max(end, last_non_blank + 1)
        
        # Crear representación
        tape_section = self.tape[start:end]
        head_pos_in_section = self.head_position - start
        
        # Línea superior con posiciones
        positions = [str(i).center(3) for i in range(start, end)]
        pos_line = '|'.join(positions)
        
        # Línea con símbolos
        symbols = [symbol.center(3) for symbol in tape_section]
        symbol_line = '|'.join(symbols)
        
        # Línea con indicador del cabezal
        head_indicators = [' ^ ' if i == head_pos_in_section else '   ' for i in range(len(tape_section))]
        head_line = '|'.join(head_indicators)
        
        return f"{pos_line}\n{symbol_line}\n{head_line}"
    
    def __str__(self) -> str:
        return self.get_tape_content()
    
    def __repr__(self) -> str:
        return f"Tape(content='{self.get_tape_content()}', head_position={self.head_position})"