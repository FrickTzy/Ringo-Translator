from Main_Files import Backend, Elements, Window


class Main(Window):
    __HEIGHT = 600
    __WIDTH = 1000

    def __init__(self):
        super().__init__("Ringo Translator", self.__WIDTH, self.__HEIGHT)
        self.__backend = Backend(self.window)
        self.__elements = Elements(self.window, self.__backend)

    def __background_executions(self):
        self.__elements.element_change.shortcuts()

    def run(self):
        self.__elements.place_elements()
        self.__background_executions()
        self.window.mainloop()


main = Main()

if __name__ == "__main__":
    main.run()
