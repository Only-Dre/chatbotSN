from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionFornecerSuporte(Action):
    # Função para fornecer suporte
    def name(self) -> Text:
        return "action_fornecer_suporte"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Recupera o problema salvo no slot
        problema = tracker.get_slot("problema")
        
        # Simulação da Base de Dados
        base_dados = {
            "acesso": "Para problemas de acesso, tente redefinir sua senha no link: somnanuvem.com/recuperar",
            "plano": "Nossos planos atuais são: Free, Premium (R$19,90) e Família (R$34,90).",
            "aplicativo": "Tente limpar o cache do app ou verificar se há atualizações na sua loja de aplicativos."
        }

        if not problema:
            dispatcher.utter_message(text="Não identifiquei o problema. Vou te passar para um atendente humano agora.")
            return []

        # Lógica de busca simples (pode ser aprimorada com busca por palavras-chave)
        resposta = None
        for chave in base_dados:
            if chave in problema.lower():
                resposta = base_dados[chave]
                break

        if resposta:
            dispatcher.utter_message(text=f"Encontrei uma solução: {resposta}")
        else:
            dispatcher.utter_message(text="Este problema parece complexo. Estou te transferindo para um especialista humano. Aguarde um instante.")

        return []