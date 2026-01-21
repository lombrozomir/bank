from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class IntRange:
    min: int
    max: int

@dataclass(frozen=True)
class FloatRange:
    min: float
    max: float

@dataclass(frozen=True)
class StrLen:
    min: int = 1
    max: int = 20
    alphabet: str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
