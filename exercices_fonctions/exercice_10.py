def celsius_to_fahrenheit():
    try:
        celsius = float(input("Entrez votre température en Celsius :\n"))
        fahrenheit = (celsius * 1.8) + 32
        print(f"Votre température de {celsius}°C donne {fahrenheit}°F")
    except ValueError:
        print("Votre température doit être un nombre !")


celsius_to_fahrenheit()
