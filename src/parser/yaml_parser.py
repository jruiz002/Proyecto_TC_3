"""
Parser YAML para configuraciones de Máquinas de Turing
"""

import yaml
from typing import Dict, Any, List
from pathlib import Path
from ..models.turing_machine import TuringMachine
from ..utils.exceptions import YAMLParsingError
from ..utils.validators import validate_yaml_structure


class YAMLParser:
    """
    Parser para archivos YAML que contienen definiciones de Máquinas de Turing
    """
    
    @staticmethod
    def load_from_file(file_path: str) -> Dict[str, Any]:
        """
        Carga un archivo YAML y retorna su contenido
        
        Args:
            file_path: Ruta al archivo YAML
            
        Returns:
            Diccionario con el contenido del archivo
            
        Raises:
            YAMLParsingError: Si hay errores al leer o parsear el archivo
        """
        try:
            path = Path(file_path)
            if not path.exists():
                raise YAMLParsingError(f"Archivo no encontrado: {file_path}")
            
            with open(path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                
            if data is None:
                raise YAMLParsingError("El archivo YAML está vacío")
                
            return data
            
        except yaml.YAMLError as e:
            raise YAMLParsingError(f"Error al parsear YAML: {e}")
        except Exception as e:
            raise YAMLParsingError(f"Error al leer archivo: {e}")
    
    @staticmethod
    def load_from_string(yaml_content: str) -> Dict[str, Any]:
        """
        Carga contenido YAML desde un string
        
        Args:
            yaml_content: Contenido YAML como string
            
        Returns:
            Diccionario con el contenido parseado
            
        Raises:
            YAMLParsingError: Si hay errores al parsear el contenido
        """
        try:
            data = yaml.safe_load(yaml_content)
            if data is None:
                raise YAMLParsingError("El contenido YAML está vacío")
            return data
        except yaml.YAMLError as e:
            raise YAMLParsingError(f"Error al parsear YAML: {e}")
    
    @staticmethod
    def parse_turing_machine(data: Dict[str, Any]) -> TuringMachine:
        """
        Parsea los datos YAML y crea una instancia de TuringMachine
        
        Args:
            data: Diccionario con los datos del YAML
            
        Returns:
            Instancia de TuringMachine configurada
            
        Raises:
            YAMLParsingError: Si la estructura no es válida
        """
        # Validar estructura
        validate_yaml_structure(data)
        
        mt_data = data['mt']
        
        try:
            # Crear la máquina de Turing
            turing_machine = TuringMachine(
                states=mt_data['states'],
                input_alphabet=mt_data['input_alphabet'],
                tape_alphabet=mt_data['tape_alphabet'],
                initial_state=mt_data['initial_state'],
                accept_states=mt_data['accept_states'],
                transitions=mt_data['transitions'],
                blank_symbol=YAMLParser._get_blank_symbol(mt_data['tape_alphabet'])
            )
            
            return turing_machine
            
        except Exception as e:
            raise YAMLParsingError(f"Error al crear la Máquina de Turing: {e}")
    
    @staticmethod
    def get_test_inputs(data: Dict[str, Any]) -> List[str]:
        """
        Extrae las cadenas de entrada para pruebas
        DEPRECATED: Las cadenas de prueba ahora se cargan desde archivos TXT separados
        
        Args:
            data: Diccionario con los datos del YAML
            
        Returns:
            Lista vacía (método deprecado)
        """
        validate_yaml_structure(data)
        return []  # Retorna lista vacía ya que las cadenas están en archivos TXT
    
    @staticmethod
    def _get_blank_symbol(tape_alphabet: List[str]) -> str:
        """
        Determina el símbolo en blanco del alfabeto de la cinta
        
        Args:
            tape_alphabet: Alfabeto de la cinta
            
        Returns:
            Símbolo en blanco (por defecto 'B')
        """
        # Buscar símbolos comunes para blancos
        blank_candidates = ['B', '_', ' ', 'blank', 'BLANK']
        
        for candidate in blank_candidates:
            if candidate in tape_alphabet:
                return candidate
        
        # Si no se encuentra un candidato obvio, usar 'B' por defecto
        return 'B'
    
    @staticmethod
    def create_sample_yaml() -> str:
        """
        Crea un ejemplo de archivo YAML para una MT
        
        Returns:
            String con contenido YAML de ejemplo
        """
        sample = """mt:
  states: [q0, q1, q2, qf]
  input_alphabet: [a, b]
  tape_alphabet: [a, b, B, X, Y]
  initial_state: q0
  accept_states: [qf]
  transitions:
    - state: q0
      read: [a]
      write: [X]
      move: R
      next: q1
    - state: q1
      read: [a]
      write: [a]
      move: R
      next: q1
    - state: q1
      read: [Y]
      write: [Y]
      move: R
      next: q1
    - state: q1
      read: [b]
      write: [Y]
      move: L
      next: q2
    - state: q2
      read: [Y]
      write: [Y]
      move: L
      next: q2
    - state: q2
      read: [a]
      write: [a]
      move: L
      next: q2
    - state: q2
      read: [X]
      write: [X]
      move: R
      next: q0
    - state: q0
      read: [Y]
      write: [Y]
      move: R
      next: q0
    - state: q0
      read: [B]
      write: [B]
      move: R
      next: qf
  inputs:
    - "aabb"
    - "ab"
    - "aaabbb"
    - "aab"
    - "abab"
"""
        return sample