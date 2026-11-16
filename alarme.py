import time
from datetime import datetime


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
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nAlarme encerrado.")