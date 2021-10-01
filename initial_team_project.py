
from gilles import gilles_greeting
import thompson
import proksch
import rodriguez


def main():
    print("Welcome to our collaborative program.")

    print()
    s_name = thompson.scotts_greeting()
    print()
    proksch.alexs_greeting()
    print()
    gilles_greeting("Gilles", "Mambou")
    print()
    rodriguez.rodriguez_greeting()




main()


