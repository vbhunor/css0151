import pytest
from bs4 import BeautifulSoup


def load_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def test_html_structure():
    html_content = load_file("index.html")
    soup = BeautifulSoup(html_content, "html.parser")

    score = 0

    # 1. Ellenőrizzük a nyelvi beállítást
    if soup.html and soup.html.get("lang") == "hu":
        score += 1
    else:
        print("HIBA: A <html> elem nyelve nem 'hu'.")

    # 2. Ellenőrizzük, hogy van-e legalább 5 "box" osztályú div
    boxes = soup.find_all("div", class_="box")
    if len(boxes) >= 5:
        score += 1
    else:
        print(
            f"HIBA: Csak {len(boxes)} darab 'box' osztályú div található, pedig legalább 5 kellene."
        )

    print(f"HTML teszt pontszám: {score}/2")
    assert score == 2, "A HTML struktúra nem megfelelő."


def test_css_properties():
    css_content = load_file("style.css")

    score = 0

    properties = {
        "background-color": "red",
        "width": "125px",
        "border": "5px solid greenyellow",
        "padding": "50px",
        "margin": "10px",
        "margin-left": "100px",
        "display": "flex",
    }

    for prop, value in properties.items():
        if f"{prop}: {value};" in css_content:
            score += 1
        else:
            print(
                f"HIBA: A '{prop}' tulajdonság nincs megfelelően beállítva (elvárt: {value})."
            )

    print(f"CSS teszt pontszám: {score}/7")
    assert score == 7, "A CSS tulajdonságok nem megfelelőek."


def test_total_score():
    test_html_structure()
    test_css_properties()
    total_score = 2 + 7  # HTML + CSS teszt összpontszám
    print(f"Összesített pontszám: {total_score}/9")
    assert total_score == 9, "Az összpontszám nem éri el a 9-et."


if __name__ == "__main__":
    pytest.main(["-v", "--capture=no"])
