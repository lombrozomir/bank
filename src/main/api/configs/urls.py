from pathlib import Path

def get_base_url() -> str:
    props = Path('resources') / 'urls.properties'
    if not props.exists():
        return 'http://localhost:4111'
    for line in props.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('base_url='):
            return line.split('=', 1)[1].strip().rstrip('/')
    return 'http://localhost:4111'
