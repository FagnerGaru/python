import random

pontuacao = {
    "GRIFINÓRIA": 0,
    "LUFA-LUFA": 0,
    "CORVINAL": 0,
    "SONSERINA": 0
}

mensagens_casas = {
    "GRIFINÓRIA": "Coragem, ousadia e determinação! Sabia que Godric Gryffindor empunhava a espada que só aparece para os verdadeiros bravos? Você está entre Harry Potter, Hermione e Rony!",
    "LUFA-LUFA": "Lealdade, paciência e trabalho duro! Helga Hufflepuff aceitava todos que quisessem aprender. Newt Scamander, o famoso magizoologista, também foi da Lufa-Lufa!",
    "CORVINAL": "Sabedoria, criatividade e inteligência! Ravenclaw valoriza mentes brilhantes. Sabia que a corvina Luna Lovegood é uma das suas integrantes mais excêntricas e brilhantes?",
    "SONSERINA": "Astúcia, ambição e liderança! Salazar Slytherin queria formar grandes líderes. Merlin, o maior feiticeiro de todos os tempos, também foi Sonserino!"
}

def saudacao():
    print("Olá, jovem! Aí está você! Vamos, vamos! Apresse-se, ainda há muitos alunos para fazer o teste! Suba aqui e deixe que o Chapéu Seletor nos diga a qual casa você pertence. Ele irá ler seus pensamentos e sentimentos mais profundos para decidir para onde você irá. Vamos começar?\n")
    resposta = input("Você está pronto para começar o teste? (s/n): ").strip().lower()
    if resposta == 's': 
        pergunta1()
    else:
        print("Tudo bem, volte quando estiver preparado!\n")

def tratamento(resposta):
    return resposta.strip().upper()

def pergunta1():
    print("\nVocê vê um filhote de Acromântula andando pelos corredores da escola. O que você faz?\n\n"
          "A. Chama o monitor da sua casa para decidir o que fazer com a criatura.\n"
          "B. Alimenta ele e leva para seu dormitório, afinal é uma criatura adorável.\n"
          "C. Sai gritando por ajuda, afinal alguém tem que se livrar desse monstro nojento.\n"
          "D. Atrairia a criatura para a casa do Hagrid sem contar para ninguém.\n")
    resposta = input("Escolha A, B, C ou D: ")
    if resposta:
        opcao = tratamento(resposta)
        if opcao == "A":
            pontuacao["LUFA-LUFA"] += 1
        elif opcao == "B":
            pontuacao["SONSERINA"] += 1
        elif opcao == "C":
            pontuacao["CORVINAL"] += 1
        elif opcao == "D":
            pontuacao["GRIFINÓRIA"] += 1
        else:
            print("Opção inválida! Vamos tentar novamente.")
            pergunta1()
            return
        pergunta2()
    else:
        print("Você precisa responder algo!")
        pergunta1()

def pergunta2():
    print("\nSe você pudesse escolher uma matéria preferida em Hogwarts, qual seria?\n\n"
          "A. Defesa Contra as Artes das Trevas\n"
          "B. Herbologia\n"
          "C. Feitiços\n"
          "D. Poções\n")
    resposta = input("Escolha A, B, C ou D: ")
    if resposta:
        opcao = tratamento(resposta)
        if opcao == "A":
            pontuacao["GRIFINÓRIA"] += 1
        elif opcao == "B":
            pontuacao["LUFA-LUFA"] += 1
        elif opcao == "C":
            pontuacao["CORVINAL"] += 1
        elif opcao == "D":
            pontuacao["SONSERINA"] += 1
        else:
            print("Opção inválida! Vamos tentar novamente.")
            pergunta2()
            return
        pergunta3()
    else:
        print("Você precisa responder algo!")
        pergunta2()

def pergunta3():
    print("\nO que você mais valoriza?\n\n"
          "A. Coragem\n"
          "B. Lealdade\n"
          "C. Inteligência\n"
          "D. Ambição\n")
    resposta = input("Escolha A, B, C ou D: ")
    if resposta:
        opcao = tratamento(resposta)
        if opcao == "A":
            pontuacao["GRIFINÓRIA"] += 1
        elif opcao == "B":
            pontuacao["LUFA-LUFA"] += 1
        elif opcao == "C":
            pontuacao["CORVINAL"] += 1
        elif opcao == "D":
            pontuacao["SONSERINA"] += 1
        else:
            print("Opção inválida! Vamos tentar novamente.")
            pergunta3()
            return
        pergunta4()
    else:
        print("Você precisa responder algo!")
        pergunta3()

def pergunta4():
    print("\nSe você tivesse acesso ao Mapa do Maroto, o que faria?\n\n"
          "A. Usaria apenas para proteger Hogwarts de ameaças.\n"
          "B. Compartilharia o segredo com seus amigos mais leais.\n"
          "C. Estudaria cada canto do castelo só por curiosidade.\n"
          "D. Usaria para escapar das regras e planejar aventuras secretas.\n")
    resposta = input("Escolha A, B, C ou D: ")
    if resposta:
        opcao = tratamento(resposta)
        if opcao == "A":
            pontuacao["GRIFINÓRIA"] += 1
        elif opcao == "B":
            pontuacao["LUFA-LUFA"] += 1
        elif opcao == "C":
            pontuacao["CORVINAL"] += 1
        elif opcao == "D":
            pontuacao["SONSERINA"] += 1
        else:
            print("Opção inválida! Vamos tentar novamente.")
            pergunta4()
            return
        pergunta5()
    else:
        print("Você precisa responder algo!")
        pergunta4()

def pergunta5():
    print("\nVocê descobre um segredo sobre um professor perigoso. O que faz?\n\n"
          "A. Vai direto até Dumbledore, sem hesitar.\n"
          "B. Conta para seus amigos, buscando apoio.\n"
          "C. Investiga tudo sozinho para ter certeza.\n"
          "D. Guarda o segredo até achar a melhor hora para usá-lo a seu favor.\n")
    resposta = input("Escolha A, B, C ou D: ")
    if resposta:
        opcao = tratamento(resposta)
        if opcao == "A":
            pontuacao["GRIFINÓRIA"] += 1
        elif opcao == "B":
            pontuacao["LUFA-LUFA"] += 1
        elif opcao == "C":
            pontuacao["CORVINAL"] += 1
        elif opcao == "D":
            pontuacao["SONSERINA"] += 1
        else:
            print("Opção inválida! Vamos tentar novamente.")
            pergunta5()
            return
        resultado()
    else:
        print("Você precisa responder algo!")
        pergunta5()

def resultado():
    max_pontos = max(pontuacao.values())
    casas_empate = [casa for casa, pontos in pontuacao.items() if pontos == max_pontos]

    print("\nHmmmm… difícil… muito difícil… Vejo qualidades em você que o fariam brilhar em qualquer casa…\n")

    if len(casas_empate) == 1:
        casa_escolhida = casas_empate[0]
    else:
        print(f"Empate entre: {', '.join(casas_empate)}. Vou precisar pensar mais...")
        casa_escolhida = random.choice(casas_empate)
        print("Pronto! Decidi!\n")

    print(f"MAS DECIDI! Você vai para… {casa_escolhida}!!!\n")
    print(mensagens_casas[casa_escolhida])
    print("\nPontuação final:")
    for c, pontos in pontuacao.items():
        print(f"{c}: {pontos}")

saudacao()
