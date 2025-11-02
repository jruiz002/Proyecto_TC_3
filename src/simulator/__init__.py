"""
Simulador de Máquinas de Turing

Este módulo contiene la lógica principal para simular
la ejecución de Máquinas de Turing y generar descripciones instantáneas.
"""

from .mt_simulator import MTSimulator
from .instantaneous_description import InstantaneousDescription

__all__ = ['MTSimulator', 'InstantaneousDescription']