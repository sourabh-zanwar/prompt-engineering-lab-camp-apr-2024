from pathlib import Path
from spacy_llm.registry import registry
import jinja2
from typing import Iterable
from spacy.tokens import Doc

TEMPLATE_DIR = Path("templates")

@registry.llm_tasks("labcamp.ContextExtractTask.v1")
def make__extraction() -> "ContextExtractTask":
    return ContextExtractTask()

def read_template(name: str) -> str:
    """Read a template"""

    path = TEMPLATE_DIR / f"{name}.jinja"
    #print(path)

    if not path.exists():
        raise ValueError(f"{name} is not a valid template.")

    return path.read_text()


class ContextExtractTask:
  def __init__(self, template: str = "contextextract.v1", field: str = "context"):
    self._template = read_template(template)
    self._field = field

  def _check_doc_extension(self):
     """Add extension if need be."""
     if not Doc.has_extension(self._field):
         Doc.set_extension(self._field, default=None)

  def generate_prompts(self, docs: Iterable[Doc]) -> Iterable[str]:
    environment = jinja2.Environment()
    _template = environment.from_string(self._template)
    for doc in docs:
        prompt = _template.render(
            text=doc.text,
        )
        yield prompt  

  def parse_responses(
      self, docs: Iterable[Doc], responses: Iterable[str]
  ) -> Iterable[Doc]:
    self._check_doc_extension()
    for doc, prompt_responses in zip(docs, responses):
      if len(prompt_responses)>1:
        prompt_response = ', '.join(prompt_responses)
      else:
        prompt_response = prompt_responses[0]
      try:
        setattr(
            doc._,
            self._field,
            prompt_response.replace("Context:", "").strip(),
        ),
      except ValueError:
        setattr(doc._, self._field, None)
    yield doc