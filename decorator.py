def greet(fx):
    print("Good Morning", end=" ")
    fx()
    print("Thanks for visiting us.")

@greet
def hw():
    print("World!")
@greet
def me():
    print("Rume")

def withargs(fx):
    def mfx(*args, **kwargs):
        print("Hello boyzz..")
        fx(*args, **kwargs)
        print("Plz visit us later again.")
    return mfx


@withargs
def fullName(x: str, y: str):
    print(x,y)

fullName("Hasan","Rume")