from spellchecker import SpellChecker

corrector = SpellChecker()

word = input("Enter a Word : ")
if word in corrector:
    print("Corrector")
else:
    corrector_word = corrector.correction(word)
    print("Correct Spelling is ", corrector_word)
