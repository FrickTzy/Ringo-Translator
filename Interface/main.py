from Main_Files import Backend, Elements, Window


class Main(Window):
    height = 600
    width = 1000

    def __init__(self):
        super().__init__("Ringo Translator", self.width, self.height)
        self.backend = Backend()
        self.elements = Elements(self.window, self.backend)

    def background_executions(self):
        self.elements.element_change.shortcuts()

    def run(self):
        self.elements.place_elements()
        self.background_executions()
        self.window.mainloop()


main = Main()

if __name__ == "__main__":
    main.run()
