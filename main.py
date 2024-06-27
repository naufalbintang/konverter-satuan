panjang_map = {
    # km ke
    "km":{
        "hm": lambda x: x * 10, 
        "dam": lambda x: x * 100,
        "m": lambda x: x * 1000,
        "dm": lambda x: x * 10000,
        "cm": lambda x: x * 100000,
        "mm": lambda x: x * 1000000,
    },
    
    # hm ke  
    "hm":{
        "km": lambda x: x / 10,
        "dam": lambda x: x * 10,
        "m": lambda x: x * 100,
        "dm": lambda x: x * 1000,
        "cm": lambda x: x * 10000,
        "mm": lambda x: x * 100000,
    },
    # dam ke
    "dam":{
        "km": lambda x: x / 100,
        "hm": lambda x: x / 10,
        "m": lambda x: x * 10,
        "dm": lambda x: x * 100,
        "cm": lambda x: x * 1000,
        "mm": lambda x: x * 10000,
    },
    # m ke
    "m":{
        "km": lambda x: x / 1000,
        "hm": lambda x: x / 100,
        "dam": lambda x: x * 10,
        "dm": lambda x: x * 10,
        "cm": lambda x: x * 100,
        "mm": lambda x: x * 1000,
    },
    # dm ke
    "dm":{
        "km": lambda x: x / 10000,
        "hm": lambda x: x / 1000,
        "dam": lambda x: x / 100,
        "m": lambda x: x / 10,
        "cm": lambda x: x * 10,
        "mm": lambda x: x * 100,
    },
    # cm ke
    "cm":{
        "km": lambda x: x / 100000,
        "hm": lambda x: x / 10000,
        "dam": lambda x: x / 1000,
        "m": lambda x: x / 100,
        "dm": lambda x: x / 10,
        "mm": lambda x: x * 10,
    },
    # mm ke
    "mm":{
        "km": lambda x: x / 1000000,
        "hm": lambda x: x / 100000,
        "dam": lambda x: x / 10000,
        "m": lambda x: x / 1000,
        "dm": lambda x: x / 100,
        "cm": lambda x: x / 10,
    },
}
berat_map = {
    # kg ke
    "kg":{
        "hg": lambda x: x * 10, 
        "dag": lambda x: x * 100,
        "g": lambda x: x * 1000,
        "dg": lambda x: x * 10000,
        "cg": lambda x: x * 100000,
        "mg": lambda x: x * 1000000,
    },
    
    # hg ke  
    "hg":{
        "kg": lambda x: x / 10,
        "dag": lambda x: x * 10,
        "g": lambda x: x * 100,
        "dg": lambda x: x * 1000,
        "cg": lambda x: x * 10000,
        "mg": lambda x: x * 100000,
    },
    # dag ke
    "dag":{
        "kg": lambda x: x / 100,
        "hg": lambda x: x / 10,
        "g": lambda x: x * 10,
        "dg": lambda x: x * 100,
        "cg": lambda x: x * 1000,
        "mg": lambda x: x * 10000,
    },
    # g ke
    "g":{
        "kg": lambda x: x / 1000,
        "hg": lambda x: x / 100,
        "dag": lambda x: x * 10,
        "dg": lambda x: x * 10,
        "cg": lambda x: x * 100,
        "mg": lambda x: x * 1000,
    },
    # dg ke
    "dg":{
        "kg": lambda x: x / 10000,
        "hg": lambda x: x / 1000,
        "dag": lambda x: x / 100,
        "g": lambda x: x / 10,
        "cg": lambda x: x * 10,
        "mg": lambda x: x * 100,
    },
    # cg ke
    "cg":{
        "kg": lambda x: x / 100000,
        "hg": lambda x: x / 10000,
        "dag": lambda x: x / 1000,
        "g": lambda x: x / 100,
        "dg": lambda x: x / 10,
        "mg": lambda x: x * 10,
    },
    # mg ke
    "mg":{
        "kg": lambda x: x / 1000000,
        "hg": lambda x: x / 100000,
        "dag": lambda x: x / 10000,
        "g": lambda x: x / 1000,
        "dg": lambda x: x / 100,
        "cg": lambda x: x / 10,
    },
}

while True:
    angka = float(input("Masukkan angka\t\t: "))
    satuan_input = input("Masukkan satuan awal\t: ")
    satuan_output = input("Masukkan satuan akhir\t: ")
    if satuan_input.lower() in panjang_map and satuan_output.lower() in panjang_map:
        print(f"{angka:,.2f} {satuan_input} = {panjang_map[satuan_input][satuan_output](angka):,.2f} {satuan_output}")  
    elif satuan_input.lower() in berat_map and satuan_output.lower() in berat_map:
        print(f"{angka:,.2f} {satuan_input} = {berat_map[satuan_input][satuan_output](angka):,.2f} {satuan_output}")  
    else:
        print("satuan tidak sah")
        continue
    # break
    is_keluar = input("Apakah ingin keluar (y/n)? ")
    if is_keluar == "y":
        break
    else:
        continue