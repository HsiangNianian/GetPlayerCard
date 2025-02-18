from getpc.character import generate_character, export_to_excel, Race, Class

pc1 = generate_character(name="艾利克斯")
pc2 = generate_character(race=Race.ELF, char_class=Class.WIZARD)

export_to_excel([pc1, pc2], "characters.xlsx")