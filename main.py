#!/usr/bin/env python3
"""
Gra Ortograficzna - Polish Spelling Game
A command-line application for learning Polish spelling.
"""

from itertools import count
import random
import os

LIMIT = 50
THE_LIST = (
    {"problem": "ó czy u", "cases": (
        {"case": "u", "rules": (
            {"rule": '"uje" "ujesz" "uję" się nie kreskuje', "examples": (
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
            {"rule": 'Wyjątek: "u" a nie "ó". Zapamiętaj!', "examples": (
                'zasuwka',
                'skuwka',
                'wsuwka',
                'posuwać',       
            )},
        )},
        {"case": "ó", "rules": (
            {"rule": '"ó" wymawia się na "o", "e", "a"', "examples": (
                'mróz',
                'pióro',
                'lód',
                'sól',
                'kółko',
                'miód',
                'piórek',
                'dróżka',
                'ziółko',
                'szósty',
                'wrócić',
            )},
            {"rule": 'Wyraz zakończony na "ów" piszemy z kreską', "examples": (
                'królów',
                'mistrzów',
                'panów',
                'władców',
                'Kraków',
                'chłopców',
            )},
            {"rule": 'Wyraz zakończony na "ówka" piszemy z kreską', "examples": (
                'klasówka',
                'siatkówka',
        
            )},
            {"rule": 'Wyraz zakończony na "ówna" w stopniu wyższym piszemy z kreską', "examples": (
                'cesarzówna',
                'Nowakówna',

            )},
            {"rule": 'Wyraz bez reguły na "ó". Zapamiętaj!', "examples": (
                'królik',
                'róża',
                'półka',
                'góra',
                'który',
                'żółty',
                'różowy',
                'próba',
                'różnica',
                'źródło',
                'również',
                'skóra',
                'sójka',
                'ogórek',
                'ołówek',
                'wkrótce',
                'włóczka',
                'późno',
                'kłótnia',
                'jaskółka',
                'wiewiórka',
                'wróbel',
                'żółw',
                'córka',
                'król',
                'tchórz',
            )},
        )},
    )},

    {"problem": "rz czy ż", "cases": (
        {"case": "rz", "rules": (
            {"rule": 'Piszemy "rz" gdy wymienia się na "r"', "examples": (
                'orzeł',
                'rycerz',
                'harcerz',
            )},
            {"rule": 'Po spółgłoskach piszemy "rz"', "examples": (
                'brzoza',
                'chrzan',
                'chrzest',
                'dojrzały',
                'drzewo',
                'drzwi',
                'grzmot',
                'grzyb',
                'igrzyska',
                'krzak',
                'krzesło',
                'krzyż',
                'olbrzym',
                'potrzebny',
                'przejście',
                'przygoda',
                'przyjaciel',
                'skrzydło',
                'spojrzeć',
                'strzała',
                'trzaskać',
                'trzcina',
                'wrzask',
                'wrzesień',
                'wrzos',
                'zajrzeć',
            )},
            {"rule": 'Nazwy zawodów i niektóre wyrazy zakończone na "arz"', "examples": (
                'malarz',
                'piekarz',
                'lekarz',
            )},
            {"rule": 'Wyrazy bez reguły na "rz". Zapamiętaj!', "examples": (
                'rzeka',
                'zwierzęta',
                'jarzębina',
                'burza',
                'rząd',
                'kurz',
                'wierzba',
                'rzecz',
                'tchórz',
                'zmierzch',
                'rzęsy',
                'orzech',
                'porządek',
                'rzadki',
                'korzeń',
                'marzenie',
                'rzeźba',
                'jarzyny',
                'porzeczka',
                'rzodkiewka',
                'warzywa',
                'wydarzenie',
            )},
        )},
        {"case": "ż", "rules": (
            # {"rule": 'Piszemy "ż", gdy wymienia się na "g", "dz", "h", "z", "ź", "s"', "examples": (
            
            # )},


            
            #'krzyż',
            {"rule": 'Wyjątek! Wyrazy zakończony na "aż"', "examples": (
                'bandaż',
                'pejzaż',
                'papież',
                'młodzież',
                'straż',
            )},
        )},
    )},

    {"problem": "ch czy h", "cases": (
        {"case": "ch", "rules": (
            {"rule": 'Piszemy "ch" gdy wymienia się na "sz"', "examples": (
                'cicho',
                'duch',
                'mucha', 
                'zapach',
            )},
            {"rule": 'Piszemy "ch" po literze "s"', "examples": (
                'schody',
                'schronisko',
                'wschód',
            )},
            {"rule": 'Piszemy "ch" na końcu wyrazów', "examples": (
                'brzuch',
                'książkach',
                'ładnych',
                'palcach',
                'słuch',
                'strach',
                'uśmiech',
                'zapach',
            )},
            {"rule": 'Wyrazy bez reguły "ch". Zapamiętaj!', "examples": (
                'architekt',
                'charakter',
                'chcieć',
                'chemia',
                'chirurg',
                'chleb',
                'chmura',
                'chociaż',
                'chodzić',
                'choroba',
                'chory',
                'chrupki',
                'chrzest',
                'chudy',
                'chusteczka',
                'chwała',
                'chwalić',
                'chytry',
                'echo',
                'ochota',
                'ochrona',
                'psycholog',
                'szlachetny',
                'technika',
                'zachód',
                'zachwyt',
            )},
        )},
        {"case": "h", "rules": (
            {"rule": 'Piszemy "h" gdy wymienia się na "g", "ż" lub "z"', "examples": (
                'wahać się',
                'druh',
                'błahy',
            )},
            {"rule": 'Piszemy "H" na początku imion', "examples": (
                'Halina',
                'Hania',
                'Helena',
                'Henryk',
                'Hubert',
            )},
            {"rule": 'Wyjątek "h" na końcu wyrazu. Zapamiętaj!', "examples": (
                'druh',
            )},
            {"rule": 'Wyrazy bez reguły "h". Zapamiętaj!', "examples": (
                'bohater',
                'filharmonia'
                'haft',
                'hak',
                'hałas',
                'hamak',
                'hamulec',
                'harcerz',
                'harmonia',
                'hasło',
                'helikopter',
                'herb',
                'herbata',
                'higiena',
                'hipopotam',
                'historia',
                'hobby',
                'honor',
                'hotel',
                'huk',
                'hulajnoga',
                'humor',
                'huragan',
                'huśtawka',
                'hymn',
            )},
        )},
    )},
)


def get_random_word_from_list(done):
    try:
        choice  = random.choice(THE_LIST)
        problem = choice['problem']
        case    = random.choice(choice['cases'])
        rule    = random.choice(case['rules'])

        available = [x for x in rule['examples'] if x not in done]

        if not available:
            return get_random_word_from_list(done)
        
        example = random.choice(available)
            
        return {
            "problem": problem,
            "case":    case['case'],
            "rule":    rule['rule'],
            "example": example,
        }
    except:
        return False


def the_loop():
    os.system('clear')
    print("Gra Ortograficzna - Polish Spelling Game")
    print(f"Dostaniesz {LIMIT} przykładów do rozwiązania. Powodzenia!")
    input("Naciśnij Enter, aby zacząć.")

    success = 0
    fail = 0
    done = []
    for i in range(LIMIT):
        entry = get_random_word_from_list(done)
        if not entry:
            print("Brak dostępnych słów do nauki. Koniec gry.")
            break

        done.append(entry['example'])
        mask = entry['example'].lower().replace(entry['case'], '_')

        iteration = i + 1  
        while True:
            os.system('clear')
            ort = input(f"Wyraz nr {iteration}/{LIMIT}: {mask}\n{entry['problem']}?': ").lower().strip()
            if ort == entry['case']:
                success += 1
                input(f"Dobrze! {entry['rule']}. Naciśnij Enter, aby kontynuować...")
                break
            else:
                fail += 1
                input(f"Źle!    {entry['rule']}. Naciśnij Enter, aby spróbować ponownie...")

    print(f"Twoje wyniki: {success} poprawnych, {fail} błędnych.")
    print("Koniec gry!")


def main():
    """Main entry point for the application."""
    the_loop()
    

if __name__ == "__main__":
    main()
