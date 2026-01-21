from __future__ import annotations
import random
from typing import Any, Annotated, get_args, get_origin, get_type_hints
from src.main.api.generators.creation_rule import FloatRange, IntRange, StrLen

class RandomModelGenerator:

    @staticmethod
    def generate(cls: type) -> Any:
        type_hints = get_type_hints(cls, include_extras=True)
        init_data: dict[str, Any] = {}
        for field_name, annotated_type in type_hints.items():
            rule = None
            actual_type = annotated_type
            if get_origin(annotated_type) is Annotated:
                actual_type, *annotations = get_args(annotated_type)
                for a in annotations:
                    if isinstance(a, (IntRange, FloatRange, StrLen)):
                        rule = a
            init_data[field_name] = RandomModelGenerator._generate_value(actual_type, rule)
        if cls.__name__ == 'CreateUserRequest':
            init_data['username'] = RandomModelGenerator._valid_username()
            init_data['password'] = RandomModelGenerator._valid_password()
            init_data['role'] = 'ROLE_USER'
        return cls(**init_data)

    @staticmethod
    def _generate_value(tp: Any, rule: Any) -> Any:
        if rule is not None:
            if isinstance(rule, IntRange):
                return random.randint(rule.min, rule.max)
            if isinstance(rule, FloatRange):
                return random.uniform(rule.min, rule.max)
            if isinstance(rule, StrLen):
                length = random.randint(rule.min, rule.max)
                return ''.join((random.choice(rule.alphabet) for _ in range(length)))
        if tp is int:
            return random.randint(0, 1000)
        if tp is float:
            return random.uniform(0.0, 1000.0)
        if tp is bool:
            return random.choice([True, False])
        if tp is str:
            length = random.randint(5, 12)
            alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            return ''.join((random.choice(alphabet) for _ in range(length)))
        origin = get_origin(tp)
        if origin is list:
            inner, = get_args(tp)
            return [RandomModelGenerator._generate_value(inner, None)]
        return None

    @staticmethod
    def _valid_username() -> str:
        return f'Max{random.randint(1000, 9999)}'

    @staticmethod
    def _valid_password() -> str:
        lower = random.choice('abcdefghijklmnopqrstuvwxyz')
        upper = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        digit = random.choice('0123456789')
        special = random.choice('!@#$%^&*()_+-=')
        rest = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5)))
        pwd = list(lower + upper + digit + special + rest)
        random.shuffle(pwd)
        return ''.join(pwd)
