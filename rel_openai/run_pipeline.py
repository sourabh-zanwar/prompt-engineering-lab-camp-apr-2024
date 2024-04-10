import os
from pathlib import Path
from typing import Optional
from spacy_llm.util import assemble

def run_pipeline(
    text: str,
    config_path: Path,
    examples_path: Optional[Path]
):
    if not os.getenv("OPENAI_API_KEY", None):
        print(
            "OPENAI_API_KEY env variable was not found.\n"+ 
            "Set it by running 'export OPENAI_API_KEY=...' and try again."
        )

    nlp = assemble(
        config_path,
        overrides={}
        if examples_path is None
        else {"paths.examples": str(examples_path)},
    )

    doc = nlp(text)

    print(f"Text: {doc.text}")
    print(f"Entities: {[(ent.text, ent.label_) for ent in doc.ents]}")
    print("Relations:")
    for r in doc._.rel:
        print(f"  - {doc.ents[r.dep]} [{r.relation}] {doc.ents[r.dest]}")