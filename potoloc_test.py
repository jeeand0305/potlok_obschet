
alfavit="A E I O U Y B C D F G H J K L M N P Q R S T V W X Z"
number0_9 = "0 1 2 3 4 5 6 7 8 9"

price={"PK":2100, "baget":150, "polotnoMDS_320":210,"cena_ugol":60, "vstavka":90, \
       "lamp":350, "trub_p":350,"KN_P":850, "KZ_P":1000,"BR_P":350,  "NO_P":500, \
       "BL_P":1000, "Vi_P":1500, "KS_P":800, "VR":400 }

shirina = float(input("Введи ширину комноты если нет пиши 0 : "))
dlina = float(input("Введи длину комноты если нет пиши 0: "))
s_potolok = float(input("Введи площадь комноты если нет пиши 0:"))
num_lite = int(input("Введи количество светильников если нет пиши 0:"))
ugol = int(input("Введи количество углов в комноте если нет пиши 0:"))
trubi = int(input("Введи количество труб диаметром до 50мм \
 котрые будут проходит через потолок если нет пиши 0:"))

# print("Краткие обозночение элементов потолка")
# print("ПРИМЕР цифра слитно количество", "PK2, NO5")
# print("          Карниз ниша - KN")
# print(" Карниз закрытая ниша - KZ")
# print("      Брус алюменивый - BR")
# print("              Вытяжка - Vi")
# print("Канализационный стояк - KS")
# print("Вентяляционая решотка - VR")
#
# zaprose_dop_rabot=input("Дополнительные элементы потолка ели нет пиши 0:")



def poluchil_tuple_shirnu_dlinu_perim_ploshad():
    dlina_f = dlina
    shirina_f = shirina
    s_potolok_f = s_potolok
    ugol_f = 4
    num_lite_f=0
    shi_dli_per_plo = {}
    if shirina > 0 and dlina > 0:
        s_potolok_f = dlina_f*shirina_f
        perimetr_f = (dlina_f+shirina_f)*2
        # замена ширины и длины между собой
        if dlina_f <= shirina_f:
            dlina_f, shirina_f = shirina_f, dlina_f
    elif shirina > 0 and s_potolok:#>0 or dlina > 0:
        dlina_f = s_potolok_f / shirina_f
        perimetr_f = (dlina_f+shirina_f)*2
        if dlina_f < shirina_f:
            dlina_f, shirina_f = shirina_f, dlina_f
    elif dlina_f > 0 and s_potolok:#>0 or :
        shirina_f = s_potolok_f / dlina_f
        perimetr_f = (dlina_f+shirina_f)*2
        if dlina_f < shirina_f:
            dlina_f, shirina_f = shirina_f, dlina_f
    elif shirina > 0 and dlina > 0 or s_potolok>0:
        dlina_f = 4
        shirina_f = s_potolok_f / dlina_f
        perimetr_f = (dlina_f + shirina_f) * 2
        if dlina_f < shirina_f:
            dlina_f, shirina_f = shirina_f, dlina_f
    if ugol != 0:
        ugol_f = ugol

    shi_dli_per_plo['shirina_f'] = shirina_f
    shi_dli_per_plo['dlina_f'] = dlina_f
    shi_dli_per_plo['perimetr_f'] = perimetr_f
    shi_dli_per_plo['s_potolok_f'] = s_potolok_f
    shi_dli_per_plo['ugol_f'] = ugol_f
    shi_dli_per_plo['num_lite_f'] = num_lite
    shi_dli_per_plo['trubi_f'] = trubi
    print(shi_dli_per_plo)
    return shi_dli_per_plo

razmeri_s_d_pe_pl=poluchil_tuple_shirnu_dlinu_perim_ploshad()

def dop_element(zaprose_dop_rabot):
    otbor_name_element = ""
    otbor_number_elementa = ""
    for name in zaprose_dop_rabot:
        if name in alfavit:
            otbor_name_element += name
        elif name in number0_9:
            otbor_number_elementa += name
        print(otbor_number_elementa, otbor_name_element)
#
# dop_element(zaprose_dop_rabot):


def stoi_pot(razmeri_s_d_pe_pl):#, dopi ):
    numb_baget25= 0 #КРАТНЫ ПАЛКАМ 2,5М
    total = 0
    total += razmeri_s_d_pe_pl["s_potolok_f"] * price["polotnoMDS_320"]
    numb_baget25 = razmeri_s_d_pe_pl["perimetr_f"]//2.5
    total += razmeri_s_d_pe_pl["perimetr_f"] * price["vstavka"]
    total += razmeri_s_d_pe_pl["ugol_f"] * price["cena_ugol"]
    total += razmeri_s_d_pe_pl["num_lite_f"] * price["lamp"]
    total += razmeri_s_d_pe_pl["trubi_f"] * price["trub_p"]


    # сдвинуть обсчет ниже если есть парящий потолок или \
    # теневой с вычетом длины из периметра и пересчет
    if numb_baget25 == razmeri_s_d_pe_pl["perimetr_f"]/2.5:
        numb_baget25 = (numb_baget25*2.5)* price["baget"]
    elif numb_baget25 != razmeri_s_d_pe_pl["perimetr_f"]/2.5:
        numb_baget25 = ((numb_baget25+1)*2.5) * price["baget"]
    total+= numb_baget25
    print("стоимость потолка", total, "руб.")
    print(
        "полотно",
        razmeri_s_d_pe_pl["s_potolok_f"] * price["polotnoMDS_320"],
        "багет",
        numb_baget25 ,
        "углы",
        razmeri_s_d_pe_pl["ugol_f"] * price["cena_ugol"],
        "вставка",
        razmeri_s_d_pe_pl["perimetr_f"] * price["vstavka"],
        "светильники",
        razmeri_s_d_pe_pl["num_lite_f"] * price["lamp"],
        "трубы",
        razmeri_s_d_pe_pl["trubi_f"] * price["trub_p"]
    )
    print("стоимость потолка со скидкой", total*0.8, "руб.")
stoi_pot(razmeri_s_d_pe_pl)

