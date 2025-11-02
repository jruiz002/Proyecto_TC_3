"""
Excepciones personalizadas para el simulador de Máquinas de Turing
"""


class MTException(Exception):
    """Excepción base para errores del simulador de MT"""
    pass


class TuringMachineError(MTException):
    """Excepción general para errores de la Máquina de Turing"""
    pass


class InvalidTransitionError(MTException):
    """Error cuando se intenta aplicar una transición inválida"""
    pass


class InvalidStateError(MTException):
    """Error cuando se encuentra un estado inválido"""
    pass


class InvalidTapeSymbolError(MTException):
    """Error cuando se encuentra un símbolo inválido en la cinta"""
    pass


class YAMLParsingError(MTException):
    """Error al parsear el archivo YAML"""
    pass


class SimulationError(MTException):
    """Error durante la simulación de la MT"""
    pass