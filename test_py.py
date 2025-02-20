import pytest
from bs4 import BeautifulSoup

def test_html_language():
    with open("index.html", encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content, "html.parser")
    
    assert "lang" in soup.html.attrs, "Hiányzik a lang attribútum a <html> elemből."
    assert soup.html["lang"] == "hu", "A lang attribútum értéke nem 'hu'."

def test_html_boxes():
    with open("index.html", encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content, "html.parser")
    
    boxes = soup.find_all("div", class_="box")
    assert len(boxes) >= 5, f"Csak {len(boxes)} darab .box elem található, de legalább 5 kell."

def test_html_css_link():
    with open("index.html", encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content, "html.parser")
    
    linked_styles = soup.find("link", {"rel": "stylesheet", "href": "style.css"})
    assert linked_styles, "A CSS fájl nincs linkelve, vagy rossz az elérési út."

def test_css_box_class_exists():
    with open("style.css", encoding="utf-8") as f:
        content = f.read()
    
    assert ".box {" in content, "Hiányzik a .box osztály a CSS fájlból."

def test_css_background_color():
    with open("style.css", encoding="utf-8") as f:
        content = f.read()
    
    assert "background-color: red;" in content, "A háttérszín nem piros (background-color: red;)."

def test_css_width():
    with open("style.css", encoding="utf-8") as f:
        content = f.read()
    
    assert "width: 125px;" in content, "A szélesség nem 125px (width: 125px;)."

def test_css_border():
    with open("style.css", encoding="utf-8") as f:
        content = f.read()
    
    assert "border: 5px solid greenyellow;" in content, "A keret nem 5px széles és zöldessárga (border: 5px solid greenyellow;)."

def test_css_padding():
    with open("style.css", encoding="utf-8") as f:
        content = f.read()
    
    assert "padding: 50px;" in content, "A belső térköz nem 50px (padding: 50px;)."

def test_css_margin():
    with open("style.css", encoding="utf-8") as f:
        content = f.read()
    
    assert "margin: 10px;" in content, "A külső térköz nem 10px (margin: 10px;)."

def test_css_margin_left():
    with open("style.css", encoding="utf-8") as f:
        content = f.read()
    
    assert "margin-left: 100px;" in content, "A bal oldali külső térköz nem 100px (margin-left: 100px;)."

def test_css_display_flex():
    with open("style.css", encoding="utf-8") as f:
        content = f.read()
    
    assert "display: flex;" in content, "A megjelenítés nem flex (display: flex;)."
