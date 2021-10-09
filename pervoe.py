class Soda:
    """gasirovka"""
    
    def show_my_drink(self,sirop):
        if len(sirop) == 0:
            print("Обычная газировка")
        else:
            print("Газировка и ", sirop)
def main():
    g = Soda()
    sirop = str(input("какую добаку вы хотите "))
    g.show_my_drink(sirop)
main()
