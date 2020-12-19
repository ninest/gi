import pytest
from gi_cli.functions import get_language_to_add


@pytest.mark.parametrize(
    "input_names_list, expexted_languages_list",
    [
        (
            ["python", "noDe"],
            ["Python", "Node"],
        ),
        (
            ["pyThOn", "metaprogrammingsystem"],
            ["Python", "MetaProgrammingSystem"],
        ),
        (
            ["vvvv", "visualstudio"],
            ["VVVV", "VisualStudio"],
        ),
    ],
)
def test_get_language_to_add(input_names_list, expexted_languages_list):
    assert get_language_to_add(input_names_list) == expexted_languages_list
