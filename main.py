# main.py
from facades import FacadeCliente, FacadeAdmin
from menu import modoCliente, modoAdmin, menu

def main():
    clienteFacade = FacadeCliente()
    adminFacade = FacadeAdmin()
    menu(True)

if __name__ == "__main__":
    main()
