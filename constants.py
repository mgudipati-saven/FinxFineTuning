from pathlib import Path
from decouple import config
from openai import OpenAI

CLIENT=OpenAI(api_key=str(config('OPENAI_API_KEY')))
DATA_DIRECTORY=Path(__file__).parent / 'data'
