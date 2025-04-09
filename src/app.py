usuarios = []

def soma(a,b):
    
    return a+b

def is_par(a):
    if a%2 == 0:
        return True
    else:
        return False

def cadastro_usuario(nome, email):
    for usuario in usuarios:
        if usuario["email"] == email:
            return "email ja existe"
        
    novo_usuario ={
        "nome":nome,
        "email":email
    }

    usuarios.append(novo_usuario)
    return "sucesso"

#controller
def cadastro(nome , cpf):
    new_user = {
        "nome":nome,
        "cpf":cpf
    }
    return save(new_user)

#service
def save(new_user):
    if new_user["nome"] and new_user["cpf"]:
        return True #salvo no DB
    return False #erro ao salvar no DB

def wellcome(email):
    if email:
        resposta = send_mail(email)
        if resposta:
            return "emial de boas vindas enviado"
        return "erro de provedor de emil"

def send_mail(emil):
    return True