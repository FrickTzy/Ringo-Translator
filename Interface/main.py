from Main_Files import Backend, Elements, Window, PronunciationSleepManager


class Main(Window):
    __HEIGHT = 600
    __WIDTH = 1000

    def __init__(self):
        super().__init__("Ringo Translator", self.__WIDTH, self.__HEIGHT)
        self.__pronunciation_sleep_manager = PronunciationSleepManager()
        self.__backend = Backend(self.window, self.__pronunciation_sleep_manager)
        self.__elements = Elements(self.window, self.__backend, self.__pronunciation_sleep_manager)

    def __background_executions(self):
        self.__elements.element_change.shortcuts()

    def run(self):
        self.__elements.place_elements()
        self.__background_executions()
        self.window.mainloop()


main = Main()

if __name__ == "__main__":
    main.run()
