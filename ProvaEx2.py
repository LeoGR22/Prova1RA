idade = int(input("Digite sua idade"))
tempotrabalho = int(input("Digite por quantos anos voce trabalha"))
idadepermitida = 65
tempotrabpermitido = 30
tempoeidade = 85


if idade >= idadepermitida:
    print("Voce pode se aposentar por conta de sua idade")
if idade < idadepermitida:
    print("Vc nao pode se aposentar por conta de sua idade")

if tempotrabalho >= tempotrabpermitido:
    print("Vc pode se aposentar por conta de seu tempo de trabalho")
elif tempotrabalho < tempotrabpermitido:
    print("Vc nao pode se aposentar por conta de seu tempo de trabalho")

if idade + tempotrabalho >= tempoeidade:
    print("Vc pode se aposentar por seu tempo de trabalho somado com sua idade")


