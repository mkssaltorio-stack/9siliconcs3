class Pencil:
    def __init__(self, color, brand, length, isSharpened):
        self.color = color
        self.brand = brand
        self.length = length
        self.__isSharpened = isSharpened

    def sharpen(self):
        if not self.__isSharpened:
            self.__isSharpened = True
            print("The pencil has been sharpened.")
        else:
            print("The pencil is already sharp.")

    def write(self, text):
        if self.__isSharpened:
            print("Pencil wrote:", text)
        else:
            print("The pencil needs to be sharpened first.")

    def erase(self):
        print("The pencil erased something.")

    def get_sharpened_status(self):
        return self.__isSharpened


# Create two independent Pencil objects
pencil1 = Pencil("Yellow", "Mongol", 15, False)
pencil2 = Pencil("Blue", "Faber-Castell", 18, True)


# Initial states
print("--- BEFORE ---")
print("Pencil 1:")
print("Color:", pencil1.color)
print("Brand:", pencil1.brand)
print("Length:", pencil1.length)
print("Sharpened:", pencil1.get_sharpened_status())

print("\nPencil 2:")
print("Color:", pencil2.color)
print("Brand:", pencil2.brand)
print("Length:", pencil2.length)
print("Sharpened:", pencil2.get_sharpened_status())


# Perform action only on Pencil 1
print("\nSharpening Pencil 1...")
pencil1.sharpen()


# Updated states
print("\n--- AFTER ---")
print("Pencil 1:")
print("Color:", pencil1.color)
print("Brand:", pencil1.brand)
print("Length:", pencil1.length)
print("Sharpened:", pencil1.get_sharpened_status())

print("\nPencil 2:")
print("Color:", pencil2.color)
print("Brand:", pencil2.brand)
print("Length:", pencil2.length)
print("Sharpened:", pencil2.get_sharpened_status())