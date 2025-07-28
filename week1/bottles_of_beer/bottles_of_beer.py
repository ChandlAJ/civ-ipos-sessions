from time import sleep

STARTING_BOTTLES = 3

def bottle_display_text(bottles):
    if bottles == 0:
        return "no more bottles"
    elif bottles == 1:
        return f"{bottles} bottle"
    else:
        return f"{bottles} bottles"

def main():

    for bottles in range(STARTING_BOTTLES, 0, -1):
        for c in (f"{bottle_display_text(bottles)} of beer on the wall, {bottle_display_text(bottles)} of beer."):
            print(c, end='', flush=True)
            sleep(0.07)
        sleep(0.5)
        bottles -= 1
        print()
        for c in f"Take one down and pass it round, {bottle_display_text(bottles)} of beer on the wall.":
            print(c, end='', flush=True)
            sleep(0.07)
        print()
    else:
        for c in (f"{bottle_display_text(bottles)} of beer on the wall, {bottle_display_text(bottles)} of beer"):
            print(c, end='', flush=True)
            sleep(0.07)
        print()
        for c in (f"Go to the store and buy some more, {STARTING_BOTTLES} bottles of beer on the wall."):
            print(c, end='', flush=True)
            sleep(0.07)

if __name__ == "__main__":
    main()

