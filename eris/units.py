from pint import UnitRegistry

UNIT_REGISTRY = UnitRegistry()
ACCELERATION = UNIT_REGISTRY.meter / (UNIT_REGISTRY.second ** 2)
MASS = UNIT_REGISTRY.g