def loenimed(failinimi):
    sisend=open(failinimi)
    lines=sisned.readlines()
    sisend.close()
    return lines

katse=loenimed()

sisend=open("palgad.csv")
lines=sisend.readlines()
print(lines)
reanr=0
palgasumma=0
meestepalgasumma=0
naistepalgasumma=0
meestearv=0
naistearv=0
# nyyd tuleb tsykkel yle koigi inimeste
while reanr<len(lines):
    rida=lines[reanr]
    print(rida)
    tykid=rida.split(",")
    print(tykid)
    if tykid[1]=="m":
      # meeste case
      print("mees")
      meesterarv=meestearv+1
      meestepalgasumma=meestepalgasumma+int(tykid[2])
    else:
      # naiste case
      print("naine")
      naistearv=naistearv+1
    palgasumma=palgasumma+int(tykid[2])
    naistepalgasumma=naistepalgasumma+int(tykid[2])
    reanr=reanr+1

print("keskmine palk",palgasumma/len(lines))

