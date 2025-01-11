import streamlit as st
import pandas as pd

# Título do aplicativo
st.title("Painel da Oficina Mecânica")

# Dados fictícios
data = {
    'Serviço': ['Troca de Óleo', 'Alinhamento', 'Balanceamento', 'Revisão Completa'],
    'Quantidade': [150, 80, 120, 50],
    'Preço Unitário (R$)': [100, 80, 60, 300]
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Exibição da tabela de dados
st.subheader("Serviços Realizados")
st.dataframe(df)

# Cálculo do faturamento
df['Faturamento (R$)'] = df['Quantidade'] * df['Preço Unitário (R$)']
faturamento_total = df['Faturamento (R$)'].sum()

# Exibição do faturamento total
st.subheader("Faturamento Total")
st.metric(label="Faturamento Total (R$)", value=f"{faturamento_total:.2f}")

# Gráfico de barras dos serviços
st.subheader("Quantidade de Serviços Realizados")
st.bar_chart(df.set_index('Serviço')['Quantidade'])

# Gráfico de barras do faturamento por serviço
st.subheader("Faturamento por Serviço")
st.bar_chart(df.set_index('Serviço')['Faturamento (R$)'])

# Input para adicionar novo serviço
st.subheader("Adicionar Novo Serviço")
novo_servico = st.text_input("Nome do Serviço")
quantidade_servico = st.number_input("Quantidade", min_value=0, step=1)
preco_servico = st.number_input("Preço Unitário (R$)", min_value=0.0, step=1.0)

if st.button("Adicionar Serviço"):
    if novo_servico and quantidade_servico > 0 and preco_servico > 0:
        # Adiciona o novo serviço ao DataFrame
        novo_dado = {
            'Serviço': novo_servico,
            'Quantidade': quantidade_servico,
            'Preço Unitário (R$)': preco_servico,
            'Faturamento (R$)': quantidade_servico * preco_servico
        }
        df = df.append(novo_dado, ignore_index=True)
        st.success("Serviço adicionado com sucesso!")
    else:
        st.error("Preencha todos os campos corretamente.")

# Exibição da tabela atualizada
st.subheader("Tabela Atualizada de Serviços")
st.dataframe(df)
