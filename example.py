from prompt_template_engine import Engine

engine = Engine()
result = engine.render("Hello {{name}}, welcome to {{city}}!", name="Alice", city="Tokyo")
print(result)
