import time
from datetime import datetime

from progresso import registrar_confirmacao
from recompensas import PONTOS_POR_DOSE


def _pedir_confirmacao(agora, nome, remedios, remedio, hhmm):
    resposta = input("   Você tomou? (s/n): ").strip().lower()
    if resposta == "s":
        registrar_confirmacao(nome, remedios, remedio["nome"], hhmm, agora.date())
        print(f"   ✅ Confirmado! +{PONTOS_POR_DOSE} pontos")
    else:
        print("   Dose não registrada.")


def iniciar_alarmes(dados):
    print("Alarme ativo! Pressione Ctrl+C para voltar ao menu.")
    avisados = set()  # evita repetir o aviso no mesmo minuto
    try:
        while True:
            agora = datetime.now()
            hhmm = agora.strftime("%H:%M")
            for nome, remedios in dados.items():
                for r in remedios:
                    chave = (agora.date(), nome, r["nome"], hhmm)
                    if hhmm in r["horarios"] and chave not in avisados:
                        avisados.add(chave)
                        print(f"\a\a\a⏰ {hhmm} - {nome}: tomar {r['nome']} ({r['dosagem'] or 'sem dosagem'})")
                        _pedir_confirmacao(agora, nome, remedios, r, hhmm)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nAlarme encerrado.")

        #a mudança foi feita aqui para que ele pudesse perguntar se o usuário tomou o remédio ou não.