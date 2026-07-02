"""Tests for prompt_template_engine."""
import pytest
from prompt_template_engine import Engine


def test_render_basic():
    engine = Engine()
    result = engine.render("Hello {{name}}", name="World")
    assert result == "Hello World"


def test_render_multiple_vars():
    engine = Engine()
    result = engine.render("{{greeting}} {{name}} from {{city}}", greeting="Hi", name="Alice", city="Tokyo")
    assert result == "Hi Alice from Tokyo"


def test_render_missing_var_raises():
    engine = Engine()
    with pytest.raises(ValueError, match="not found"):
        engine.render("{{missing}}", name="Alice")


def test_render_batch():
    engine = Engine()
    templates = ["Hello {{name}}", "Bye {{name}}"]
    results = engine.render_batch(templates, name="Bob")
    assert results == ["Hello Bob", "Bye Bob"]


def test_render_no_vars():
    engine = Engine()
    result = engine.render("No variables here")
    assert result == "No variables here"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
