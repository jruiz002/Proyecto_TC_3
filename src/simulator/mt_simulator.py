"""
Simulador principal de Máquinas de Turing
"""

from typing import List, Tuple, Optional
from ..models.turing_machine import TuringMachine
from ..models.tape import Tape
from ..models.transition import Transition
from .instantaneous_description import InstantaneousDescription
from ..utils.exceptions import SimulationError


class MTSimulator:
    """
    Simulador de Máquinas de Turing que genera descripciones instantáneas
    """
    
    def __init__(self, turing_machine: TuringMachine, max_steps: int = 10000):
        """
        Inicializa el simulador
        
        Args:
            turing_machine: La Máquina de Turing a simular
            max_steps: Número máximo de pasos para evitar bucles infinitos
        """
        self.turing_machine = turing_machine
        self.max_steps = max_steps
    
    def simulate(self, input_string: str) -> Tuple[bool, List[InstantaneousDescription], str]:
        """
        Simula la ejecución de la MT con una cadena de entrada
        
        Args:
            input_string: Cadena de entrada a procesar
            
        Returns:
            Tupla con (aceptada, lista_de_IDs, resultado_final)
            - aceptada: True si la cadena fue aceptada
            - lista_de_IDs: Lista de descripciones instantáneas
            - resultado_final: Descripción del resultado
        """
        # Validar entrada
        if not self.turing_machine.validate_input(input_string):
            invalid_symbols = [s for s in input_string if s not in self.turing_machine.input_alphabet]
            return False, [], f"Cadena rechazada: contiene símbolos inválidos {invalid_symbols}"
        
        # Inicializar simulación
        current_state = self.turing_machine.initial_state
        tape = self.turing_machine.create_tape(input_string)
        step = 0
        
        # Lista para almacenar las descripciones instantáneas
        ids = []
        
        # Crear ID inicial
        initial_id = InstantaneousDescription(current_state, tape, step)
        ids.append(initial_id)
        
        # Simulación principal
        while step < self.max_steps:
            # Verificar si estamos en un estado de aceptación
            if self.turing_machine.is_accept_state(current_state):
                result = f"Cadena ACEPTADA en {step} pasos"
                return True, ids, result
            
            # Leer símbolo actual de la cinta
            current_symbol = tape.read()
            
            # Buscar transición aplicable
            transition = self.turing_machine.get_transition(current_state, [current_symbol])
            
            if transition is None:
                # No hay transición aplicable
                result = f"Cadena RECHAZADA: No hay transición desde estado '{current_state}' leyendo '{current_symbol}' en paso {step}"
                return False, ids, result
            
            # Aplicar transición
            try:
                new_state, write_symbols, move_direction = transition.apply()
                
                # Escribir en la cinta
                tape.write(write_symbols[0])  # Para MT de una cinta
                
                # Mover cabezal
                tape.move(move_direction)
                
                # Actualizar estado
                current_state = new_state
                step += 1
                
                # Crear nueva ID
                transition_desc = str(transition)
                new_id = InstantaneousDescription(current_state, tape, step, transition_desc)
                ids.append(new_id)
                
            except Exception as e:
                result = f"Error durante la simulación en paso {step}: {e}"
                return False, ids, result
        
        # Se alcanzó el límite máximo de pasos
        result = f"Simulación detenida: se alcanzó el límite máximo de {self.max_steps} pasos"
        return False, ids, result
    
    def simulate_step_by_step(self, input_string: str) -> 'StepByStepSimulation':
        """
        Crea un simulador paso a paso para ejecución interactiva
        
        Args:
            input_string: Cadena de entrada
            
        Returns:
            Instancia de StepByStepSimulation
        """
        return StepByStepSimulation(self.turing_machine, input_string, self.max_steps)
    
    def simulate_multiple(self, input_strings: List[str]) -> List[Tuple[str, bool, List[InstantaneousDescription], str]]:
        """
        Simula múltiples cadenas de entrada
        
        Args:
            input_strings: Lista de cadenas a simular
            
        Returns:
            Lista de tuplas con (cadena, aceptada, IDs, resultado)
        """
        results = []
        
        for input_string in input_strings:
            accepted, ids, result = self.simulate(input_string)
            results.append((input_string, accepted, ids, result))
        
        return results


class StepByStepSimulation:
    """
    Simulador paso a paso para ejecución interactiva
    """
    
    def __init__(self, turing_machine: TuringMachine, input_string: str, max_steps: int = 10000):
        """
        Inicializa la simulación paso a paso
        
        Args:
            turing_machine: La Máquina de Turing a simular
            input_string: Cadena de entrada
            max_steps: Número máximo de pasos
        """
        self.turing_machine = turing_machine
        self.input_string = input_string
        self.max_steps = max_steps
        
        # Estado de la simulación
        self.current_state = turing_machine.initial_state
        self.tape = turing_machine.create_tape(input_string)
        self.step = 0
        self.finished = False
        self.accepted = False
        self.result_message = ""
        
        # Historial de IDs
        self.ids = []
        initial_id = InstantaneousDescription(self.current_state, self.tape, self.step)
        self.ids.append(initial_id)
    
    def next_step(self) -> Optional[InstantaneousDescription]:
        """
        Ejecuta el siguiente paso de la simulación
        
        Returns:
            Nueva ID o None si la simulación ha terminado
        """
        if self.finished:
            return None
        
        # Verificar estado de aceptación
        if self.turing_machine.is_accept_state(self.current_state):
            self.finished = True
            self.accepted = True
            self.result_message = f"Cadena ACEPTADA en {self.step} pasos"
            return None
        
        # Verificar límite de pasos
        if self.step >= self.max_steps:
            self.finished = True
            self.accepted = False
            self.result_message = f"Simulación detenida: límite de {self.max_steps} pasos alcanzado"
            return None
        
        # Leer símbolo actual
        current_symbol = self.tape.read()
        
        # Buscar transición
        transition = self.turing_machine.get_transition(self.current_state, [current_symbol])
        
        if transition is None:
            self.finished = True
            self.accepted = False
            self.result_message = f"Cadena RECHAZADA: No hay transición desde '{self.current_state}' leyendo '{current_symbol}'"
            return None
        
        # Aplicar transición
        try:
            new_state, write_symbols, move_direction = transition.apply()
            
            # Actualizar cinta y estado
            self.tape.write(write_symbols[0])
            self.tape.move(move_direction)
            self.current_state = new_state
            self.step += 1
            
            # Crear nueva ID
            transition_desc = str(transition)
            new_id = InstantaneousDescription(self.current_state, self.tape, self.step, transition_desc)
            self.ids.append(new_id)
            
            return new_id
            
        except Exception as e:
            self.finished = True
            self.accepted = False
            self.result_message = f"Error en paso {self.step}: {e}"
            return None
    
    def run_to_completion(self) -> Tuple[bool, List[InstantaneousDescription], str]:
        """
        Ejecuta la simulación hasta completarse
        
        Returns:
            Tupla con (aceptada, IDs, resultado)
        """
        while not self.finished:
            self.next_step()
        
        return self.accepted, self.ids, self.result_message
    
    def get_current_id(self) -> InstantaneousDescription:
        """
        Obtiene la ID actual
        
        Returns:
            Descripción instantánea actual
        """
        return self.ids[-1] if self.ids else None