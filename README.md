# 🚗 Geeso Locadora

Aplicação web simples, feita com [Streamlit](https://streamlit.io/), para calcular o valor total do aluguel de um carro com base no modelo escolhido, na quantidade de dias e nos quilômetros rodados.

## 📋 Funcionalidades

- Seleção do modelo do carro na barra lateral
- Exibição da imagem do carro escolhido
- Entrada da quantidade de dias de aluguel
- Entrada da quilometragem rodada
- Cálculo automático do valor total a pagar

## 🚘 Modelos e valores

| Modelo        | Diária (R$) |
|---------------|-------------|
| BMW X5        | 750,00      |
| Audi R8       | 900,00      |
| Ford Mustang  | 800,00      |
| VW Polo       | 650,00      |
| Fiat Toro     | 700,00      |

**Taxa por quilômetro rodado:** R$ 0,15

## 🧮 Como o valor é calculado

```
total_dias    = dias × diária
total_km      = km × 0,15
aluguel_total = total_dias + total_km
```

**Exemplo:** Fiat Toro por 3 dias, rodando 200 km:

- 3 × 700 = R$ 2.100,00
- 200 × 0,15 = R$ 30,00
- **Total: R$ 2.130,00**

## ⚙️ Pré-requisitos

- Python 3.8 ou superior
- Streamlit

## 📦 Instalação

1. Clone ou baixe este repositório.
2. (Opcional) Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. Instale a dependência:

```bash
pip install streamlit
```

## 🗂️ Estrutura de arquivos

As imagens precisam estar **na mesma pasta** do arquivo Python, com os nomes exatamente iguais aos modelos:

```
geeso-locadora/
├── app.py
├── logo.png
├── BMW X5.png
├── Audi R8.png
├── Ford Mustang.png
├── VW Polo.png
├── Fiat Toro.png
└── README.md
```

> O nome do arquivo Python (`app.py`) pode ser alterado; basta usar o mesmo nome ao executar.

## ▶️ Como executar

```bash
streamlit run app.py
```

O navegador abrirá automaticamente em `http://localhost:8501`.

## 🖱️ Como usar

1. Escolha o carro na barra lateral.
2. Informe por quantos dias ele foi alugado.
3. Informe quantos km foram rodados.
4. Clique em **Calcular** para ver o valor total.

## ⚠️ Observações

- Os campos de dias e km devem ser preenchidos com números. Dias deve ser um número inteiro (ex.: `3`) e km pode ter casas decimais usando ponto (ex.: `150.5`).
- Se os campos estiverem vazios ou com texto, o aplicativo exibirá um erro ao clicar em **Calcular**. Uma melhoria futura é validar essas entradas.
- Se alguma imagem não for encontrada, o Streamlit exibirá um erro de arquivo.

## 💡 Ideias de melhorias

- Validar as entradas com `try/except` ou usar `st.number_input`
- Armazenar as diárias em um dicionário no lugar do `if/elif`
- Permitir cadastro de novos modelos
- Gerar um recibo do aluguel em PDF

## 📄 Licença

Projeto de uso livre para fins de estudo.
