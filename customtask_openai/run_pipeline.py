import os
from pathlib import Path
from typing import Optional
 

from spacy_llm.util import assemble
from contextextract import ContextExtractTask

def run_pipeline(
    text: str,
    config_path: Path,
    examples_path: Optional[Path] = None
):
    if not os.getenv("AZURE_OPENAI_KEY", None):
        print(
            "AZURE_OPENAI_API_KEY env variable was not found.\n"+ 
            "Set it by running 'export AZURE_OPENAI_KEY=...' and try again."
        )
        return 0
    else:
        nlp = assemble(
            config_path
        )
        doc = nlp(text)
        print(f"Text: {doc.text}")
        print(f"Context: {doc._.context}")
        return doc
