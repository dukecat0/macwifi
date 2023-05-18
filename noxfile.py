import nox
from pathlib import Path

LINT_DEPENDENCIES = ["black==23.3.0", "mypy==0.930", "ruff==0.0.254"]


@nox.session
def lint(session):
    session.install(*LINT_DEPENDENCIES)
    p = Path(".").resolve()
    file = str(Path(p / "macwifi" / "macwifi.py"))
    session.run(
        "ruff",
        "--format=github",
        "--ignore=F403,F405",
        "--line-length=109",
        "--target-version=py37",
        file,
    )
    session.run("black", file)
    session.run("mypy", "--no-warn-no-return", file)
