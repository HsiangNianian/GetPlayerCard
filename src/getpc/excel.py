import pandas as pd
from ._core import CharacterCard

def export_to_excel(character: CharacterCard, filename: str):
    """
    Exports the attributes, skills, and metadata of a CharacterCard object to an Excel file.
    Args:
        character (CharacterCard): The character card object containing attributes, skills, and metadata.
        filename (str): The path and name of the Excel file to be created.
    Raises:
        ValueError: If the character object does not have the required attributes or skills.
        IOError: If there is an issue writing to the specified file.
    """
    
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