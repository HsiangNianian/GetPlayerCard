import pandas as pd
from ._core import CharacterCard

def export_to_excel(character: CharacterCard, filename: str):
    with pd.ExcelWriter(filename) as writer:
        # Attributes Sheet
        pd.DataFrame({
            'Attribute': list(character.attributes.keys()),
            'Value': list(character.attributes.values())
        }).to_excel(writer, sheet_name='Attributes', index=False)
        
        # Skills Sheet
        pd.DataFrame({
            'Skill': list(character.skills.keys()),
            'Level': list(character.skills.values())
        }).to_excel(writer, sheet_name='Skills', index=False)
        
        # Metadata
        pd.DataFrame({
            'Property': ['Name', 'Template'],
            'Value': [character.name, character.template or 'Default']
        }).to_excel(writer, sheet_name='Metadata', index=False)