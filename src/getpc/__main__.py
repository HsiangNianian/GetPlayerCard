import argparse
import json
from . import CharacterCard, export_to_excel, load_template

def interactive_create():
    """Feature #3: Interactive character creation"""
    name = input("Enter character name: ")
    card = CharacterCard(name)
    
    print("\nSetting attributes:")
    while True:
        attr = input("Attribute name (leave empty to finish): ")
        if not attr:
            break
        value = int(input(f"{attr} value: "))
        card.set_attribute(attr, value)
    
    print("\nSetting skills:")
    while True:
        skill = input("Skill name (leave empty to finish): ")
        if not skill:
            break
        level = int(input(f"{skill} level: "))
        card.set_skill(skill, level)
    
    return card

def main():
    parser = argparse.ArgumentParser(description='TRPG Character Card Tool')
    subparsers = parser.add_subparsers(dest='command')
    
    # Create command
    create_parser = subparsers.add_parser('create')
    create_parser.add_argument('--name', required=True)
    create_parser.add_argument('--template')
    create_parser.add_argument('--output', required=True)
    
    # Interactive command
    subparsers.add_parser('interactive')
    
    args = parser.parse_args()
    
    if args.command == 'create':
        card = CharacterCard(args.name)
        if args.template:
            template = load_template(args.template)
            card.apply_template(template)
        # Here you would add more creation logic
        export_to_excel(card, args.output)
        print(f"Character card saved to {args.output}")
    
    elif args.command == 'interactive':
        card = interactive_create()
        output = input("Output filename: ")
        export_to_excel(card, output)
        print(f"Character card saved to {output}")

if __name__ == '__main__':
    main()