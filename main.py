# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

price={"RK":2100, "baget":150, "polotnoMDS_320":210,"cena_ugol":60, "vstavka":90, \
       "lamp":350, "trub_p":350,"KN_P":850, "KZ_P":1000,"BR_P":350,  "NO_P":500, \
       "BL_P":1000, "Vi_P":1500, "KS_P":800, "VR":400, "PL":10 }

alfavit="AEIOUYBCDFGHJKLMNPQRSTVWXZ"
# alfavit = "A E I O U Y B C D F G H J K L M N P Q R S T V W X Z"

# number0_9 = "0 1 2 3 4 5 6 7 8 9"
number0_9 = "0123456789"

# получаем картеж доп услуг из ввода данных
def dop_element(zaprose_dop_rabot):
    total=0
    otbor_name_element = ""
    otbor_number_elementa = ""
    count = 0
    dict_zapros_dop={}
    if zaprose_dop_rabot[len(zaprose_dop_rabot)-1] != ",":
         zaprose_dop_rabot = zaprose_dop_rabot + ","
    print(zaprose_dop_rabot)
    for name in zaprose_dop_rabot:
        if name in alfavit:
            otbor_name_element += name
        elif name in number0_9:
            otbor_number_elementa += name
        otbor_number_elementa
        if ','== name:
            print(len(otbor_name_element))
            dict_zapros_dop[otbor_name_element]= int(otbor_number_elementa)
            otbor_name_element = ""
            otbor_number_elementa = ""
        # else:
        elif len(otbor_name_element) == 2:
            otbor_number_elementa = otbor_number_elementa.strip()
            dict_zapros_dop[otbor_name_element]= otbor_number_elementa
    for usluga in price:
        if usluga in dict_zapros_dop:
            print("usluga", usluga)
    total += price["PL"] * dict_zapros_dop["PL"]# int(otbor_number_elementa[1])
    print(otbor_number_elementa, otbor_name_element)
    print(total, dict_zapros_dop)

dop_element("KL8, PL6, RT28, RK92,")

# for i in price:
#     print(i)
