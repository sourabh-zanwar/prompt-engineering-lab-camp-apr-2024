import os
from pathlib import Path
from typing import Optional


from spacy_llm.util import assemble
from contextextract import ContextExtractTask

def run_pipeline_custom(config_path: Path, text: str):
    if not os.getenv("OPENAI_API_KEY", None):
        print(
            "OPENAI_API_KEY env variable was not found.\n"+ 
            "Set it by running 'export OPENAI_API_KEY=...' and try again."
        )
    else:
        nlp = assemble(
            config_path
        )
        doc = nlp(text)
        print(f": {doc.text}")
        print(f"Context: {doc._.context}")


def run_pipeline():
    if not os.getenv("OPENAI_API_KEY", None):
        print(
            "OPENAI_API_KEY env variable was not found.\n"+ 
            "Set it by running 'export OPENAI_API_KEY=...' and try again."
        )
    else:
        return 0