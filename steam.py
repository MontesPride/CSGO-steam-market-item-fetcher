from __future__ import generators
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

def kmp(text, pattern):
	shift = computeShifts(pattern)
	startPos = 0
	matchLen = 0
	for c in text:
		while matchLen >= 0 and pattern[matchLen] != c:
			startPos += shift[matchLen]
			matchLen -= shift[matchLen]
		matchLen += 1
		if matchLen == len(pattern):
			yield startPos
			startPos += shift[matchLen]
			matchLen -= shift[matchLen]

def computeShifts(pattern):
	shifts = [None] * (len(pattern) + 1)
	shift = 1
	for pos in range(len(pattern) + 1):
		while shift < pos and pattern[pos-1] != pattern[pos-shift-1]:
			shift += shifts[pos-shift-1]
		shifts[pos] = shift
	return shifts


root = ET.parse('items.xml').getroot()
"""
for child in root.findall('Heavy'):
        print(child.tag)
        for child2 in child:
                print(child2.tag)
                """
skin_wear = ["Factory New", "Minimal Wear", "Field-Tested", "Well-Worn", "Battle-Scarred", ""]

q = 1
weapon_kind = list()
"Wybierz rodzaj broni: "
for child in root:
        print(q, '-', child.tag)
        weapon_kind.append(child.tag)
        q = q + 1
i1 = int(input("Wybierz rodzaj broni: "))

q = 1
weapon_list = list()
weapon_list_name = list()
for child in root.findall(weapon_kind[i1-1]):
        print(child.tag)
        for child2 in child:
                print(q, '-', child2.get('name'))
                weapon_list.append(child2.tag)
                weapon_list_name.append(child2.get('name'))
                q = q + 1
i2 = int(input("Wybierz bron: "))

q = 1
weapon_skins = list()
weapon_specials = list()
for child in root.findall(weapon_kind[i1-1]):
        for child2 in child.findall(weapon_list[i2-1]):
                print(child2.get('name'))
                for child3 in child2.findall('skin'):
                        print(q, '-', child3.text)
                        weapon_skins.append(child3.get('search'))
                        weapon_specials.append(child3.get('special'))
                        q = q + 1
i3 = int(input("Wybierz skin: "))

if(weapon_skins[i3-1] != ""):
        for i in range (0,5):
                print(i+1, '-', skin_wear[i])
        i4 = int(input("Wybierz jakosc: "))
else:
        i4 = 6

s = str()
if(weapon_specials[i3-1] == "StatTrak"):
        s = input("StatTrak (1/0): ")
if(weapon_specials[i3-1] == "Souvenir"):
        s = input("Souvenir (1/0): ")
if(weapon_specials[i3-1] == "None"):
        s = '0'
        



urls = "http://steamcommunity.com/market/listings/730/"
stattrak_knife = "%E2%98%85%20StatTrak%E2%84%A2"
just_knife = "%E2%98%85"
stattrak_weapon = "StatTrak%E2%84%A2"
souvenir = "Souvenir%20"


url_renders = "/render/?query=&start="
url_rendere = "&count=100&country=PL&language=polish&currency=3"

search_start = ',"listinginfo'
search_end = "}]}}}"


weapon_name = weapon_list_name[i2-1]
skin_name = weapon_skins[i3-1]
skin_wear = skin_wear[i4-1]
weapon_name = weapon_name.replace(" ", "%20")
skin_name = skin_name.replace(" ", "%20")
skin_wear = skin_wear.replace(" ", "%20")
page_num = 0
url_render = url_renders + str(page_num) + "0" + url_rendere
url_end_uni = "%20%7C%20" + skin_name + "%20%28" + skin_wear + "%29" + url_render

if(s != '0' and i1 != 5):
        if(weapon_specials[i3-1] == "StatTrak"):
                url = urls + stattrak_weapon + "%20" + weapon_name + url_end_uni
        if(weapon_specials[i3-1] == "Souvenir"):
                url = urls + souvenir + weapon_name + url_end_uni
elif(i1 == 5):
        if(s != '0'):
                url = urls + stattrak_knife + "%20" + weapon_name + url_end_uni
        else:
                url = urls + just_knife + "%20" + weapon_name + url_end_uni
elif(s == '0' and i1 != 5):
        url = urls + weapon_name + url_end_uni
if(i1 == 5 and skin_name == ""):
        url = urls + just_knife + "%20" + weapon_name + url_render
print(url)
"""
if(stat_trak == 'y'):
        url = urls + stattrak_weapon + "%20" + weapon_name + "%20%7C%20" + skin_name + "%20%28" + skin_wear + "%29" + url_renders + str(page_num) + url_rendere
else:
        url = urls + weapon_name + "%20%7C%20" + skin_name + "%20%28" + skin_wear + "%29" + url_renders + str(page_num) + url_rendere
print(url)
"""

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = str(urlopen(req).read(), "utf-8")
if(len(list(kmp(webpage, search_start))) > 0 and len(list(kmp(webpage, search_end))) > 0):
        x = list(kmp(webpage, search_start))[0]
        y = list(kmp(webpage, search_end))[0]
        list_info = webpage[x:y]
        c_s_f = 'converted_steam_fee":'   #21
        c_p_f = ',"converted_publisher_fee":'   #27
        c_p_p_u = ',"converted_price_per_unit":'   #28
        c_f_p_u = ',"converted_fee_per_unit":'   #26
        listing_id = '"listingid":"'   #13
        pr_ice = '","price"'
        asset_id = '"id":"'   #ich jest 2 razy wiecej   #6
        ammount_asset = '","amount"'   #ich jest 2 razy wiecej
        D_parame = '%A%assetid%'   #11
        D_parame_end = '","name":'   #ich jest 3 razy wiecej
        c_steam_fee = list(kmp(list_info, c_s_f))
        c_pub_fee = list(kmp(list_info, c_p_f))
        c_pri_p_unit = list(kmp(list_info, c_p_p_u))
        c_fee_p_unit = list(kmp(list_info, c_f_p_u))
        listing_id_list = list(kmp(list_info, listing_id))
        pr_ice_list = list(kmp(list_info, pr_ice))
        asset_id_list = list(kmp(list_info, asset_id))
        ammount_asset_list = list(kmp(list_info, ammount_asset))
        D_parame_list = list(kmp(list_info, D_parame))
        D_parame_end_list = list(kmp(list_info, D_parame_end))
        num_items = len(c_steam_fee)
        c_steam_fees = list()
        c_pub_fees = list()
        c_pri_p_units = list()
        M_list = list()
        A_list = list()
        D_list = list()
        codes = list()
        prices = list()
        file = open('items.js','w') 
         

        for i in range (0, num_items):
                c_steam_fees.append(int(list_info[c_steam_fee[i]+21:c_pub_fee[i]]))
                c_pub_fees.append(int(list_info[c_pub_fee[i]+27:c_pri_p_unit[i]]))
                c_pri_p_units.append(int(list_info[c_pri_p_unit[i]+28:c_fee_p_unit[i]]))
                M_list.append(list_info[listing_id_list[i]+13:pr_ice_list[i]])
                A_list.append(list_info[asset_id_list[i]+6:ammount_asset_list[i]])
                D_list.append(list_info[D_parame_list[i]+12:D_parame_end_list[i]])
                temp_price = (c_steam_fees[i] + c_pub_fees[i] + c_pri_p_units[i])/100
                link_param_temp = "M" + M_list[i] + "A" + A_list[i] + "D" + D_list[i]
                print(link_param_temp, str(temp_price))
                codes.append(link_param_temp)
                prices.append(str(temp_price) + "€")
                file.write('CSGOCli.itemDataRequest("0", "' + A_list[i] + '", "' + D_list[i] + '", "' + M_list[i] + '");\n')
        print("Liczba przedmiotow:", num_items)
        #print("var codes =", codes)
        #print("var prices =", prices)
        file.close()
                
else:
        print("Aktualnie brak takiego przedmiotu na rynku")



