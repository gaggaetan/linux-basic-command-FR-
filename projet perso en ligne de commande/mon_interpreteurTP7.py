import cmd
from colorama import Fore, Style, init
from programation_par_contrat import Fraction


## ajouter des lamba et map pour simplifier le code

#reset/initialiser colerma
init(autoreset=True)

#lambda pour se faciler la tache
L_bright = lambda value: f"{Style.BRIGHT}{value}{Style.NORMAL}"
L_cyan = lambda value: f"{Fore.CYAN}{value}{Style.RESET_ALL}"
L_red = lambda value: f"{Fore.RED}{value}{Style.RESET_ALL}"



class mon_interpreteurTP7(cmd.Cmd) :
    intro = L_cyan(f"Bonjour,\n"
             f"Vous voici dans l'interpreteur interactif du TP7 avec la classe Fraction.\n\n"
             f"Veuillez exécuter \"{L_bright('new_fraction1 arg1 arg2')}\" pour créer votre 1er fraction pricipale avec\n"
             f"     'arg1' => le numérateur\n"
             f"     'arg2' => le dénominateur")
    prompt = ">>"

    # ------------- initalisation de l'interpreteur -------------
    def __init__(self):
        super().__init__()
        self._fraction1 = None
        self._fraction2 = None
        pass

    def emptyline(self):
        print("Veuillez introduire quelque chose :")

    # ------------- les décorateur -------------
    def check_fraction_created(nbrFractions):
        def décorateur(func):
            def wrapper(self,*args):
                if nbrFractions == 1 and self._fraction1 is not None :
                    return func(self, *args)
                elif nbrFractions == 1 :
                    print(L_red(f"Veuillez d'abbord créer la fraction pricipale avec la commande \"") + L_cyan(L_bright('new_fraction1 arg1 arg2'))+ L_red("\""))
                elif nbrFractions == 2 and self._fraction1 is not None and self._fraction2 is not None :
                    return func(self, *args)
                else :
                    print(L_red(f"Veuillez d'abbord créer les 2 fractions avec les commandes \"") + L_cyan(L_bright('new_fraction1 arg1 arg2')) + L_red("\" et \"")+L_cyan(L_bright('new_fraction2 arg1 arg2')) + L_red("\""))
            return wrapper
        return décorateur



    # ------------- création des fractions -------------
    def makeFraction(self, num, den):
        if den != 0:
            frac = Fraction(num, den)
            return frac
        else:
            raise ZeroDivisionError("Le dénominateur ne peut pas être égal à zéro.")

    def fractionsManagement(self, args):
        try :
            num, den = map(float, args.split())
            frac = self.makeFraction(num, den)
            return frac

        except ValueError:
            raise ValueError(f"Erreur : Veuillez fournir des entiers pour le numérateur et le dénominateur.")



    def do_new_fraction1(self, args):
        self._fraction1 = self.fractionsManagement(args)
        print(L_cyan(f"Vottre fraction pricipale à bien été enregistré : " + self._fraction1.__str__() + "\n" +
                  f"Maintenant Veuillez exécuter \"{L_bright('new_fraction2 arg1 arg2')}\" pour créer votre 2er fraction secondaire avec\n"
                  f"     'arg1' => le numérateur\n"
                  f"     'arg2' => le dénominateur "))
        pass

    def do_new_fraction2(self, args):
        self._fraction2 = self.fractionsManagement(args)
        methodes = ["__str__", "as_mixed_number", "__add__", "__sub__", "__sub__", "__mul__", "__truediv__",
                    "__pow__", "__eq__", "__float__", "is_greater", "is_smaller", "__rest__", "__reverse__",
                    "__neg__", "__abs__", "is_zero", "is_integer", "is_proper", "is_unit", "is_adjacent_to"]
        methodesAddStyle = list(map(lambda string: Style.BRIGHT + string + Style.NORMAL + ", ", methodes))
        methodesText = ""
        for i in methodesAddStyle:
            methodesText += i

        print(f"{methodesText}" + L_cyan(f"Vottre fraction secondaire à bien été enregistré : " + self._fraction2.__str__() + "\n" +
                     f"Vous voila avec vos 2 fractions, vous pouvez les chager à tout moment avec: new_fraction1 et new_fraction2\n"
                     f"Aussi non, voila toutes les commandes que vous pouvez faire pour manipuler vos 2 fraction :\n{methodesText}"))
        pass


    # ------------- utilisation des fonctions de la classe fraction -------------
    @check_fraction_created(1)
    def do___str__(self, args):
        print(f" => {L_cyan(self._fraction1.__str__())}")
        pass

    @check_fraction_created(1)
    def do_as_mixed_number(self, args):
        print(f" => {L_cyan(self._fraction1.as_mixed_number())}")
        pass

    @check_fraction_created(2)
    def do___add__(self, args):
        print(f" => {L_cyan(self._fraction1.__add__(self._fraction2).__str__())}")
        pass

    @check_fraction_created(2)
    def do___sub__(self, args):
        print(f" => {L_cyan(self._fraction1.__sub__(self._fraction2).__str__())}")
        pass

    @check_fraction_created(2)
    def do___mul__(self, args):
        print(f" => {L_cyan(self._fraction1.__mul__(self._fraction2).__str__())}")
        pass

    @check_fraction_created(2)
    def do___truediv__(self, args):
        print(f" => {L_cyan(self._fraction1.__truediv__(self._fraction2).__str__())}")
        pass

    @check_fraction_created(2)
    def do___pow__(self, args):
        print(f" => {L_cyan(self._fraction1.__pow__(self._fraction2))}")
        pass

    @check_fraction_created(2)
    def do___eq__(self, args):
        print(f" => {L_cyan(self._fraction1.__eq__(self._fraction2))}")
        pass

    @check_fraction_created(1)
    def do___float__(self, args):
        print(f" => {L_cyan(self._fraction1.__float__())}")
        pass

    @check_fraction_created(2)
    def do_is_greater(self, args):
        print(f" => {L_cyan(self._fraction1.is_greater(self._fraction2))}")
        pass

    @check_fraction_created(2)
    def do_is_smaller(self, args):
        print(f" => {L_cyan(self._fraction1.is_smaller(self._fraction2))}")
        pass

    @check_fraction_created(2)
    def do___rest__(self, args):
        print(f" => {L_cyan(self._fraction1.__rest__(self._fraction2))}")
        pass

    @check_fraction_created(1)
    def do___reverse__(self, args):
        print(f" => {L_cyan(self._fraction1.__reverse__().__str__())}")
        pass

    @check_fraction_created(1)
    def do___neg__(self, args):
        print(f" => {L_cyan(self._fraction1.__neg__().__str__())}")
        pass

    @check_fraction_created(1)
    def do___abs__(self, args):
        print(f" => {L_cyan(self._fraction1.__abs__().__str__())}")
        pass

    @check_fraction_created(1)
    def do_is_zero(self, args):
        print(f" => {L_cyan(self._fraction1.is_zero())}")
        pass

    @check_fraction_created(1)
    def do_is_integer(self, args):
        print(f" => {L_cyan(self._fraction1.is_integer())}")
        pass

    @check_fraction_created(1)
    def do_is_proper(self, args):
        print(f" => {L_cyan(self._fraction1.is_proper())}")
        pass

    @check_fraction_created(1)
    def do_is_unit(self, args):
        print(f" => {L_cyan(self._fraction1.is_unit())}")
        pass

    @check_fraction_created(2)
    def do_is_adjacent_to(self, args):
        print(f" => {L_cyan(self._fraction1.is_adjacent_to(self._fraction2))}")
        pass

    #fonction suplémentaire qui utilise le lambda et filter
    def do_find_integer_fractions(self, args):
        #verifier que le nombre de parametres sont pair
        if (len(args.split()) % 2) == 1 or len(args.split()) == 0:
            raise ValueError(L_red("vous devez mettre un nombre de parametres pair ou supérieur à 0 pour pouvoir définir les fractions correctement"))

        #remplis le tableau tab_fractions_objects avec des objects fraction
        tab_fractions_objects = []
        for i in range(0, len(args.split()), 2):
            num = float(args.split()[i])
            den = float(args.split()[i + 1])
            print(f"num : {num}, den : {den}")

            tab_fractions_objects.append(Fraction(num, den))

        is_integer = list(filter(lambda x: x.is_integer() ,tab_fractions_objects))
        is_integerText = ""
        for i in range(is_integer.__len__()):
            print(L_cyan(is_integer[i].__str__()))
            is_integerText += str(is_integer[i].__str__()) + "\n"

        return is_integerText[:-1]

if __name__ == '__main__':
    interpreteur = mon_interpreteurTP7()
    interpreteur.cmdloop()