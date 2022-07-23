class human():
    def __init__(self, age = 0, sex = "?"):
        self.age = age
        self.sex = sex
    def speak(self):
        print("Hello ya ", self.age, "and ", self.sex)


man = human(12, "male")
woman = human(25, "female")
human.speak(man)
human.speak(woman)