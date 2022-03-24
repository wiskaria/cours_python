def show_multiple_str(my_str, times):
    try:
        times = int(times)
    except:
        print("Le second paramètre doit être un entier !")
    if times < 0:
        raise ValueError("")
    print(my_str * times)


show_multiple_str("ha", 0)
