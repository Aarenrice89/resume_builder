import logging
import shutil
import subprocess as sp
from functools import partial
from pathlib import Path

import yaml

from builder.document import Document
from builder.sections import Education, Experience, Header, Projects, Skills
from builder.utils.const import STYLING_CLASS_PATH

logger = logging.getLogger(__file__)


def load_document_from_yaml(input: Path) -> Document:
    with open(input, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    document = partial(
        Document,
    )
    for cls, args in data.items():
        try:
            if cls == "Document":
                args["local_output_tex_file_path"] = Path(args["local_output_tex_file_path"])
                document.keywords.update(args)
            else:
                document.keywords[cls.lower()] = eval(cls).from_config(**args)
        except NameError:
            logger.error(f"No class for '{cls}' found, skipping creation...")
    return document()


def create_pdf_from_document(document: Document):
    output = document.local_output_tex_file_path
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(output, "w") as f:
            f.write(document.to_tex())
    except Exception as e:
        logger.error(e)
        raise e
    dest = output.parent.joinpath(STYLING_CLASS_PATH.name)
    shutil.copy(STYLING_CLASS_PATH, dest)
    sp.check_call(["xelatex", str(output)], cwd=output.parent)


def main(input: str | Path) -> str:
    input = input if isinstance(input, Path) else Path(input)
    if not input.exists():
        raise FileNotFoundError(f"No input yaml found at: {input}")

    document = load_document_from_yaml(input)
    create_pdf_from_document(document)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compile your resume from YAML")
    parser.add_argument("--input", type=str, required=True)

    args = parser.parse_args()
    main(args.input)
