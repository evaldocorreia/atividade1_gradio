import gradio as gr 
import pandas as pd 
import os 
from datetime import datetime 
 
ARQUIVO_CSV = "gr_pacientes.csv" 


COLUNAS = ["timestamp", "nome", "endereco", "email", "idade", "genero", "contato_emergencia", 
           "convenio", "prioridade", "motivo", "historico_medico", "alergia", "estilo_vida",
           "historico_familiar", "hospitalizacao"] 

def cadastrar_paciente(nome, endereco, email, idade, genero, contato_emergencia, convenio, 
                       prioridade, motivo, historico_medico, alergia, estilo_vida, historico_familiar, hospitalizacao ):     
    linha = { 
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
    "nome": nome, "endereco": endereco, "email": email, "idade": idade,"genero": genero, 
    "contato_emergencia": contato_emergencia,
    "convenio": convenio, "prioridade": prioridade, 
    "motivo": motivo, "historico_medico": historico_medico, "alergia": alergia, 
    "estilo_vida": estilo_vida, "historico_familiar": historico_familiar, "hospitalizacao": hospitalizacao,
    }
    
    novo = pd.DataFrame([linha])
    if os.path.exists(ARQUIVO_CSV): 
        novo.to_csv(ARQUIVO_CSV, mode="a", header=False, index=False)     
    else:
        novo.to_csv(ARQUIVO_CSV, mode="w", header=True, index=False) 
    return "Paciente cadastrado com sucesso!", pd.read_csv(ARQUIVO_CSV).tail(5) 

with gr.Blocks() as cadastro: 
    gr.Markdown("## Cadastro de Pacientes")     
    nome = gr.Textbox(label="Nome do paciente")
    endereco = gr.Textbox(label="Endereço do paciente")
    email = gr.Textbox(label="Endereço de e-mail")
    idade = gr.Number(label="Idade") 
    genero = gr.Dropdown( 
            ["Não declarado", "Masculino", "Feminino" ],
            label="Gênero", 
        )     
    contato_emergencia = gr.Textbox(label="Contato de emergência") 
    convenio = gr.Dropdown( 
        ["Particular", "Unimed", "Bradesco Saúde", "SulAmérica", "Outro"],
        label="Convênio", 
    ) 
    prioridade = gr.Slider(1, 5, step=1, label="Prioridade do atendimento")     
    motivo = gr.Textbox(label="Motivo da consulta / observações", lines=3)
    historico_medico = gr.Dropdown( 
                ["Não Possui", "Cardíaco", "Hipertenso","Diabético", "Câncer", "Hepatite", "outro"],
                label="histórico médico", 
            )
    alergia = gr.Dropdown( 
                    ["Não Possui", "Medicamentos", "Alimentos", "Ambiental", "Não sabe"],
                    label="Alergias e Reações Adversas", 
                )
    estilo_vida = gr.Dropdown( 
                        ["Não declarado", "Tabagismo", "Consumo de álcool", "Sedentário", "Atividade Física"],
                        label="Fatores de estilo de vida", 
                    )
    historico_familiar = gr.Dropdown( 
                            ["Não declarado", "Sim", "Não", "Não Sabe"],
                            label="Histórico médico familiar", 
                        )
    hospitalizacao = gr.Dropdown( 
                                ["Não declarado", "grandes cirurgias", "hospitalizações", "condições crônicas"],
                                label="Hospitalizações ou tratamentos anteriores", 
                            )       
    botao = gr.Button("Cadastrar") 
    saida_msg = gr.Textbox(label="Status", interactive=False)     
    tabela = gr.Dataframe(label="Últimos pacientes cadastrados")     
    botao.click( 
        cadastrar_paciente, 
        [nome, endereco, email, idade, genero, contato_emergencia, 
         convenio, prioridade, motivo, historico_medico, alergia, estilo_vida, 
         historico_familiar, hospitalizacao], 
        [saida_msg, tabela], 
    )  
cadastro.launch()
