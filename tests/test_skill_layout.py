"""Validate the four-skill installation contract and metadata."""

import re
import shutil
import tempfile
import unittest

from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
SKILL_NAMES = (
    "coding-standards",
    "writing-standards",
    "apply-coding-standards",
    "apply-writing-standards",
)


def read_frontmatter(skill_path: Path) -> dict[str, str]:
    content = (skill_path / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if match is None:
        raise AssertionError(f"Missing frontmatter: {skill_path}")

    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip()
    return values


class SkillLayoutTests(unittest.TestCase):
    def test_coding_and_writing_notation_agree(self) -> None:
        shared = (
            SKILLS_ROOT / "writing-standards" / "references" / "shared-standards.md"
        ).read_text(encoding="utf-8")
        numerical = (
            SKILLS_ROOT / "coding-standards" / "references" / "numerical-python.md"
        ).read_text(encoding="utf-8")

        for source_name, source in (("shared", shared), ("numerical", numerical)):
            with self.subTest(source=source_name):
                self.assertIn("lowercase", source)
                self.assertIn("vectors", source)
                self.assertIn("uppercase", source)
                self.assertIn("rank two or greater", source)
                self.assertIn("descriptive", source)
                self.assertIn("hidden_states", source)

    def test_notation_fixture_coverage(self) -> None:
        fixture = (
            REPOSITORY_ROOT / "tests" / "fixtures" / "notation.md"
        ).read_text(encoding="utf-8")

        for expected in ("number of samples", "feature vector", "matrix", "rank-three tensor"):
            with self.subTest(expected=expected):
                self.assertIn(expected, fixture)

        self.assertIn("Mean pooling", fixture)
        self.assertIn("**Figure 1.**", fixture)
        self.assertIn("hidden_states", fixture)
        self.assertIn("shape", fixture)

    def test_complete_suite_metadata(self) -> None:
        for skill_name in SKILL_NAMES:
            with self.subTest(skill=skill_name):
                skill_path = SKILLS_ROOT / skill_name
                frontmatter = read_frontmatter(skill_path)
                agent_metadata = (skill_path / "agents" / "openai.yaml").read_text(
                    encoding="utf-8"
                )

                self.assertEqual(frontmatter["name"], skill_name)
                self.assertTrue(frontmatter["description"])
                self.assertIn("default_prompt:", agent_metadata)
                self.assertIn("allow_implicit_invocation: true", agent_metadata)

    def test_complete_install_preserves_sibling_references(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            installed_root = Path(temp_directory) / "skills"
            shutil.copytree(SKILLS_ROOT, installed_root)

            for skill_name in SKILL_NAMES:
                skill_text = (installed_root / skill_name / "SKILL.md").read_text(
                    encoding="utf-8"
                )
                self.assertIn("complete four-skill suite", skill_text)

            self.assertTrue(
                (
                    installed_root
                    / "writing-standards"
                    / "references"
                    / "shared-standards.md"
                ).is_file()
            )
            self.assertTrue(
                (
                    installed_root
                    / "writing-standards"
                    / "scripts"
                    / "audit_language.py"
                ).is_file()
            )

    def test_missing_sibling_is_detectable_and_explained(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            for skill_name in SKILL_NAMES:
                other_skills = set(SKILL_NAMES) - {skill_name}
                for sibling_name in other_skills:
                    with self.subTest(skill=skill_name, missing=sibling_name):
                        installed_root = (
                            Path(temp_directory) / f"{skill_name}-{sibling_name}"
                        )
                        shutil.copytree(SKILLS_ROOT, installed_root)
                        shutil.rmtree(installed_root / sibling_name)
                        skill_text = (
                            installed_root / skill_name / "SKILL.md"
                        ).read_text(encoding="utf-8")

                        sibling_path = installed_root / sibling_name / "SKILL.md"
                        self.assertFalse(sibling_path.exists())
                        self.assertIn(f"../{sibling_name}/SKILL.md", skill_text)
                        self.assertIn("If any sibling is missing, stop", skill_text)
                        self.assertIn(
                            "install the complete four-skill suite",
                            skill_text,
                        )


if __name__ == "__main__":
    unittest.main()
