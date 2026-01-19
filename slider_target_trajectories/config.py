from dataclasses import dataclass

@dataclass
class TargetTrajectoriesCfg:
    # Amplitudes (meters)
    A: float = 0.50
    B: float = 0.50
    
    # Frequencies
    a: int = 1 
    b: int = 1 
    
    delta: float = 1.0  # Phase
    omega: float = 0.05 # Angular frequency

    target_x: float = 0.7
    target_y: float = 0.0
    
    publish_frequency: float = 100 # hz
    frame: str = 'world'
