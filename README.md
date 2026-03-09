# Som na Nuvem - Assistente de Suporte Inteligente

O projeto Som na Nuvem é um chatbot feito para atendimento a assinantes de plataformas de streaming de música. Utilizando o framework Rasa, o sistema automatiza a triagem de problemas técnicos, dúvidas sobre planos e o encaminhamento para suporte humano.

## Objetivo
O chatbot foi projetado para solucionar três demandas principais:
1. Identificação de Problemas: Extração de entidades para entender falhas de acesso, dúvidas de faturamento ou erros no aplicativo.
2. Fornecimento de Soluções: Respostas automáticas baseadas em uma lógica de busca em Python (Custom Actions).
3. Transbordo Humano: Fluxo de contingência para casos não mapeados ou complexos.

## Tecnologias e Versões
- Rasa Framework: 3.x
- Python: 3.10
- Gerenciador de Ambientes: Conda e CMD
- Versionamento: Git

## Arquitetura do Projeto
O sistema opera através da integração de três componentes:
- NLU (Natural Language Understanding): Responsável por processar o texto do usuário e identificar a intenção e a entidade 'problema'.
- Core (Dialogue Management): Gerencia o estado da conversa através de regras (Rules) e histórias (Stories).
- Action Server: Microserviço que executa a lógica de suporte definida em Python.

## Estrutura de Arquivos Principal
- data/nlu.yml: Exemplos de treinamento para reconhecimento de linguagem.
- data/rules.yml: Regras para comportamentos fixos (ex: saudações e despedidas).
- domain.yml: Registro global de intenções, entidades, slots e respostas.
- actions/actions.py: Código fonte da lógica de busca de soluções.
- config.yml: Configurações do pipeline de IA (Tokenizers, Classificadores e Políticas).

## Instruções de Execução

1. Ativação do Ambiente:
   conda activate botSN

2. Inicialização do Servidor de Ações (Terminal 1):
   rasa run actions

3. Treinamento e Execução do Chat (Terminal 2):
   rasa train
   rasa shell

## Entidades e Fluxo de Dados
O bot utiliza o slot 'problema' para persistir a informação extraída durante o diálogo. Essa informação é enviada para a classe 'ActionFornecerSuporte', que valida o conteúdo contra a base de dados interna e retorna a instrução adequada ao usuário.

## Autor
Projeto desenvolvido como estudo base de Chatbot
