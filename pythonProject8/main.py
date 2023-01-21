from Domain.localitateValidator import LocalitateValidator
from Domain.rutaValidator import RutaValidator
from Repository.json_repository import JsonRepository
from Service.localitateService import LocalitateService
from Service.rutaService import RutaService
from Tests.teste import runAllTests
from UserInterface.console import Console


def main():
    runAllTests()
    localitateRepository = JsonRepository("localitati.json")
    localitateValidator = LocalitateValidator()
    rutaRepository = JsonRepository("rute.json")
    rutaValidator = RutaValidator()

    localitateService = LocalitateService(localitateRepository, localitateValidator)
    rutaService = RutaService(rutaRepository, localitateRepository ,rutaValidator)

    console = Console(localitateService, rutaService)
    console.runMenu()

if __name__ == '__main__':
    main()