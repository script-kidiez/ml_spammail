import requests, time

def banner():
    print("""
    +===============================================+
    | ███╗   ███╗██╗     |                          |
    | ████╗ ████║██║     | Tiktok  : @script_kiddiez|
    | ██╔████╔██║██║     | Github  : @script_kidiez |
    | ██║╚██╔╝██║██║     | Author  : DPN            |
    | ██║ ╚═╝ ██║███████╗|                          |
    | ╚═╝     ╚═╝╚══════╝|                          |
    | SPAM MAIL          |                          |
    +===============================================+
    """)

def spam(uid, jumlah):
    url = f"https://api.mobilelegends.com/mlweb/sendMail?roleId={uid}&language=en"
    print()
    print("MULAI SPAM")
    for i in range(jumlah):
        res = requests.get(url).json()
        if res['status'] == 'success':
            print(f"{i+1}. SPAM TO {uid} => BERHASIL (wait 60s)")
        else:
            print(f"{i+1}. SPAM TO {uid} => GAGAL (wait 60s)")
        if i+1 != jumlah:
            time.sleep(60)
    print("SPAM SELESAI!")

def main():
    banner()
    print()
    run = True
    while run == True:
        uid = input("Masukan ID akun : ")
        jumlah = int(input("Masukan jumlah : "))
        spam(uid, jumlah)
        pesan = input("Ingin lagi(y/t) : ")
        if pesan.lower() == "t" or pesan.lower() == "tidak":
            run = False

main()
