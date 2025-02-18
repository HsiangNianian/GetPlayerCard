import pytest
from getpc import CharacterCard, export_to_excel

def test_character_card():
    card = CharacterCard("Alice")
    card.set_attribute("STR", 15)
    card.set_skill("Swordsmanship", 75)

    export_to_excel(card, "alice.xlsx")

    # Add assertions here to verify the results
    # For example, you can check if the file was created
    assert os.path.exists("alice.xlsx")