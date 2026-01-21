from pathlib import Path

class Config:

    @staticmethod
    def fetch(key: str) -> str:
        props = Path('resources') / 'urls.properties'
        if not props.exists():
            raise FileNotFoundError('resources/urls.properties not found')
        for line in props.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' not in line:
                continue
            k, v = line.split('=', 1)
            if k.strip() == key:
                return v.strip().rstrip('/')
        raise KeyError(f"Key '{key}' not found in resources/urls.properties")
