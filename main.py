""" module permettant de verifier si une chaine de caractere est un palindrome
un palimdrome se lit dans les deux sens 
en ignorant les accentes et les caractere speciaux 
"""
import string
def ispalindrome(p):
    """ Vérifie si une chaîne de caractères donnée est un palindrome.
    Arguments :
    p (str) : La chaîne de caractères à vérifier.   
    Retour :
    bool : True si la chaîne est un palindrome, False sinon.
    """
    # Déclare une chaîne contenant les lettres avec accents.
    accents = "àâäéèêëîïôöùûüç"
    # Déclare une chaîne équivalente avec les lettres sans accents.
    sans_accents = "aaaeeeeiioouuuc"
    # Déclare une chaîne contenant les caractères spéciaux (ponctuations et espaces).
    c_spec = string.punctuation + " "
    # Crée une table de traduction pour remplacer les caractères accentués par non-accentués
    # et pour supprimer les caractères spéciaux.
    transtab = str.maketrans(accents, sans_accents, c_spec)
    # Transforme la chaîne en minuscules, remplace les accents, et enlève les caractères spéciaux.
    p = p.lower().translate(transtab)
    # Inverse la chaîne transformée.
    p2 = p[::-1]
    # Compare la chaîne transformée avec son inverse et renvoie True si elles sont identiques.
    return p2 == p
def main():
    """ Fonction principale qui teste la fonction `ispalindrome` sur plusieurs chaînes.
    Liste de chaînes à tester pour vérifier si elles sont des palindromes.
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        # Affiche le résultat pour chaque chaîne en indiquant si elle est un palindrome.
        print(s, ispalindrome(s))
# Point d'entrée du programme.
if __name__ == "__main__":
    # Appelle la fonction principale.
    main()
