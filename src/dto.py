from typing import List
from dataclasses import dataclass


@dataclass
class Solution:
    x: List[float]
    min_value: float
    tails: List[float]
