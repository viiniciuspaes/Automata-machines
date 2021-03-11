class Automata:
    def __init__(self, alphabet, transistion, initial, final):
        """
        A automata able to recognize languages given a alphabet and a transistion table.
        :param alphabet: Receives the alphabet in the format [n1, n2, ..., nn] 
        :param transistion: Receives the transistion table as a dictionary in the format
        {'q1': {'0': 'q1', '1': 'q2'}, 'q2': {'0': 'q1', '1': 'q3'}, 'q3': {'0': 'q3', '1': 'q3'}}
        :param initial: The initial state must be present inside the transistion dictionary
        :param final: The final state must be present inside the transistion dictionary
        """
        self.transistion_fuction = transistion
        self.alphabet = alphabet
        self.current_state = None
        self.initial_state = initial
        self.final_state = final

    def validate_language(self, language):
        """
        Function responsible for validate a given language
        :param language: The languagem in string format that must be validated
        :return: True if language is valid, False if not
        """
        self.current_state = self.initial_state
        for element in language:
            if element not in self.alphabet:
                self.current_state = None
                return False #Language contains characters not included in this automato alphabet
            try:
                self.current_state = self.transistion_fuction[str(self.current_state)][element]
                print("Actual state {}".format(self.current_state))
            except KeyError:
                self.current_state = None
                return False #language is not valid
        if self.current_state == self.final_state:
            self.current_state = None
            return True #Language is valid
        self.current_state = None
        return False #language didn't reach final state, it is not valid

    def upgrade_machine(self, alphabet, transistion, intial, final):
        """
        Upgrades the automato values transforming him into a new automato
        :param alphabet: the new recognized alphabet 
        :param transistion: the new recognized transistion table
        :param initial: the new initial state
        :param final: the new final state
        """
        self.alphabet = alphabet
        self.transistion_fuction = transistion
        self.initial_state = intial
        self.final_state = final
