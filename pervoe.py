class Soda:
    """gasirovka"""
    
    def gas(self, sirop,):
        print("Газировка и ", sirop)
    
    def fake(self):
        print("Обычная газировка")


def main():
    g = Soda()
    sirop = str(input("какую добаку вы хотите "))
    if len(sirop) == 0:
        g.fake()
    else:
        g.gas(sirop)
main()
