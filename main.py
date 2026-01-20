#!/usr/bin/env python3
"""
Gra Ortograficzna - Polish Spelling Game
A command-line application for learning Polish spelling.
"""

from itertools import count
import random
import os

THE_LIST = (
    {"problem": "ó czy u", "cases": (
        {"case": "u", "rules": (
            {"rule": '"uje" się nie kreskuje', "examples": (
                'pracuję',
                'rysuję',
                'maluję',
                'gotujesz',
                'planujesz',
                'obserwuje',
                'pilnuje',
                'sprawujesz',
                'czuje',
            )},
            {"rule": '"u" na początku wyrazu piszemy bez kreski', "examples": (
                'uśmiech',
                'ulica',
                'ucho',
                'upał',
                'ulotka',
                'uprawa',
                'uwaga',
                'umieć',
                'urodziny',
                'ul',
            )},
            {"rule": '"u" na końcu wyrazu piszemy bez kreski', "examples": (
                'Tomku',
                'domu',
                'duchu',
                'dachu',
                'zeszytu',
                'Aniu',
                'mleku',
            )},
            {"rule": 'Wyraz zakończony na "un" piszemy bez kreski', "examples": (
                'opiekun',
                'zdun',
            )},
            {"rule": 'Wyraz zakończony na "unek" piszemy bez kreski', "examples": (
                'pakunek',
                'rysunek',
                'malunek',
                'posterunek',
            )},
            {"rule": 'Wyraz zakończony na "uch" piszemy bez kreski', "examples": (
                'zuch',
                'maluch',
            )},
            {"rule": 'Wyraz zakończony na "uś" piszemy bez kreski', "examples": (
                'tatuś',
                'Piotruś',
            )},
            {"rule": 'Wyraz bez reguły na "u". Zapamiętaj!', "examples": (
                'już',
                'jutro',
                'tłusty',
                'rzut',
                'wujek',
                'okulary',
                'żubr',
                'żuraw',
                'kukułka',
                'kura',
                'kurtka',
                'sukienka',
                'duży',
                'bluzka',
                'popołudnie',
                'guma',
                'trudny',
                'słuchawka',
            )},
        )},
        # {"case": "ó", "rules": ()},
    )},

    # {"problem": "rz czy ż", "cases": (
    #     {"case": "rz", "rules": ()},
    #     {"case": "ż", "rules": ()},
    # )},

    # {"problem": "ch czy h", "cases": (
    #     {"case": "ch", "rules": ()},
    #     {"case": "h", "rules": ()},
    # )},
)


def get_random_word_from_list():
    """Returns a random word from the list."""
    choice  = random.choice(THE_LIST)
    problem = choice['problem']
    case    = random.choice(choice['cases'])
    rule    = random.choice(case['rules'])
    example = random.choice(rule['examples'])

    return {
        "problem": problem,
        "case":    case['case'],
        "rule":    rule['rule'],
        "example": example,
    }

def the_loop():
    for _ in range(101):
        entry = get_random_word_from_list()
        mask = entry['example'].replace(entry['case'], '_')
            
        while True:
            os.system('clear')
            ort = input(f"Wyraz: {mask}\n{entry['problem']}?': ").lower().strip()
            if ort == entry['case']:
                input(f"Dobrze! {entry['rule']}. Naciśnij Enter, aby kontynuować...")
                break
            else:
                input(f"Źle!    {entry['rule']}. Naciśnij Enter, aby spróbować ponownie...")
        


def main():
    """Main entry point for the application."""
    print("Gra Ortograficzna - Polish Spelling Game")
    the_loop()
    print("Koniec gry!")

if __name__ == "__main__":
    main()
