from typing import Optional, Dict, List

class CharacterCard:
    """
    A class to represent a character card with attributes and skills.
    
    ## Attributes:
    
    name : str
        The name of the character.
    attributes : Dict[str, int]
        A dictionary of character attributes and their values.
    skills : Dict[str, int]
        A dictionary of character skills and their values.
    template : Optional[str]
        An optional template for the character card.
    
    ## Methods:
    
    __init__(name: str) -> None
        Initializes the character card with a name.
    set_attribute(name: str, value: int) -> None
        Sets the value of a specific attribute.
    set_skill(name: str, value: int) -> None
        Sets the value of a specific skill.
    apply_template(template: Dict[str, List[str]]) -> None
        Applies a template to the character card.
    to_json() -> str
        Converts the character card to a JSON string.
    """
    name: str
    attributes: Dict[str, int]
    skills: Dict[str, int]
    template: Optional[str]

    def __init__(self, name: str) -> None: ...
    def set_attribute(self, name: str, value: int) -> None: ...
    def set_skill(self, name: str, value: int) -> None: ...
    def apply_template(self, template: Dict[str, List[str]]) -> None: ...
    def to_json(self) -> str: ...

def load_template(path: str) -> Dict[str, List[str]]: ...