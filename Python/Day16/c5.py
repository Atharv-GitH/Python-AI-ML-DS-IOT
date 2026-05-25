

def subscriptionApp(subAppRef):

    def quizAttempt():

        print("Attempting quiz for subscription")

        subAppRef()

        print("win competition and get Netflix subscription")

    return quizAttempt

@subscriptionApp

def subscription():

    print("Netflix")

subscription()
