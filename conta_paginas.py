class ContaPagina:

    def conta_pagina(slef, n):
        i = 1
        while (i <= n):
            if i+5 < n:
                print("{:02d}-{:02d}".format(i,i+4))
                i = i+5
            else:
                print("{:02d}-{:02d}".format(i,n))
                i = n+1    

def main():
        
    prog = ContaPagina()

    prog.conta_pagina(51)

if __name__ == "__main__":
    main()
