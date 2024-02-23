from django.shortcuts import render


def lista_promocoes(request):
    lista_promocoes = [
        {'id': 1, 'titulo': 'Yakuza 0', 'preco': 40.99, 'descricao': '...', 'imagem_url': 'https://upload.wikimedia.org/wikipedia/pt/f/fa/Yakuza_0_Ryu_Ga_Gotoku_Studio_Sega_capa_digital.png', 'url': 'VER DETALHES'},
        {'id': 2, 'titulo': 'Yakuza: Like a Dragon', 'preco': 199.99, 'descricao': '...', 'imagem_url': 'https://upload.wikimedia.org/wikipedia/pt/5/56/Yakuza_Like_a_Dragon_Sega_Ryu_Ga_Gotoku_capa_digital.png', 'url': 'VER DETALHES'},
    ]
    return render(request, 'promotions/lista_promocoes.html', {'promocoes': lista_promocoes})

def detalhes_promocao(request, promocao_id):
    lista_promocoes = [
        {'id': 1, 'titulo': 'Yakuza 0', 'preco': 40.99, 'descricao': 'Jogo Yakuza 0 Steam Chave Global, Sinopse: Kazuma Kiryu é um membro de baixo escalão da Família Dojima e logo após descobrir que uma cobrança de dívida se tornou um assassinato, Kiryu corre contra o tempo para provar sua inocência, Goro Majima dirige o Cabaret Grand, um dos maiores clubes de Sotenbori, como punição por um assassinato fracassado, mas recebe uma proposta para ser reintegrado à sua família e descobrirá que existe uma conspiração por trás de um golpe de assassinato.', 'imagem_url': 'https://upload.wikimedia.org/wikipedia/pt/f/fa/Yakuza_0_Ryu_Ga_Gotoku_Studio_Sega_capa_digital.png'},
        {'id': 2, 'titulo': 'Yakuza: Like a Dragon', 'preco': 199.99, 'descricao': 'Jogo Yakuza: Like a Dragon Steam Chave Global, Sinopse: Ichiban Kasuga, um membro de baixo nível da família Yakuza em Tóquio, é condenado a 18 anos de prisão após assumir a culpa por um crime que não cometeu. Mantendo seu otimismo, ele cumpre a pena com lealdade e ao retornar à sociedade, descobre que ninguém o esperava do lado de fora e que seu clã foi destruído pelo homem que ele mais respeitava.', 'imagem_url': 'https://upload.wikimedia.org/wikipedia/pt/5/56/Yakuza_Like_a_Dragon_Sega_Ryu_Ga_Gotoku_capa_digital.png'},
    ]
    promocao = next((p for p in lista_promocoes if p['id'] == promocao_id), None)
    return render(request, 'promotions/detalhes_promocao.html', {'promocao': promocao})