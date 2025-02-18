from getpc import CharacterCard, export_to_excel

card = CharacterCard("Alice")
card.set_attribute("STR", 15)
card.set_skill("Swordsmanship", 75)

export_to_excel(card, "alice.xlsx")