
def test(volume):
    # volume = 57
    if volume < 20:
        print("It's kinda quiet.")
    elif 20 <= volume < 40:
        print("It's nice for background music")
    elif 40 <= volume < 60:
        print("Perfect, I can hear all the details")
    elif 60 <= volume < 80:
        print("Nice for parties")
    elif 80 <= volume < 100:
        print("A bit loud!")
    else:
        print("My ears are hurting! :(")

# Change the volume if it's too loud or too quiet
test(57)
print(' ')

def hi(name):
    print(f'Hello {name[0].upper()}{name[1:]}, how are you?')

hi('simon')
print(' ')


def sayHiToEveryone():
    girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
    for name in girls:
        hi(name)

sayHiToEveryone()
print(' ')

def printFrom1UpTo(endNum):
    for i in range(1, endNum):
        print(i)

printFrom1UpTo(10)
print(' ')
