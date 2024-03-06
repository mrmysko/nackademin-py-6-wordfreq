# Skriv endast din funktionsdefinition här på denna indenteringsnivå! Det är
# viktigt att du ger funktionen exakt det namn som står i beskrivningen.
def wordfreq(words: str) -> dict:
    """Returns a dict with wordfrequency"""
    list_words = words.split()
    dict_words = {}

    for i in list_words:
        if i not in dict_words:
            dict_words[i] = 1
        else:
            dict_words[i] += 1

    # dict_words = {[(key, value) for key, in list_words]}

    return dict_words


if __name__ == "__main__":
    # Här kan du skriva testkod för din funktion. Denna körs endast när du kör
    # filen direkt, och inte när du importerar den som modul i en annan fil.
    # Koden importeras som en modul av autograding-funktionen för att utföra ett
    # "smoke test" av din funktion, så det är viktigt att din kod inte kör något
    # utanför denna if-sats.
    #
    # Exempel:
    #
    # print(funktionsnamn("hejsan", 99))
    # print(funktionsnamn([19, 22, 31, 29, 1])
    print(wordfreq("python programmering python"))
    print(wordfreq("test test test"))
    print(wordfreq("hej hej på dig"))
    print(wordfreq(""))
