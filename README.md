# Extração de Dados - Formulários MCT (Minha Criança Trans)

Este projeto tem como objetivo automatizar a coleta de informações de formulários digitalizados relacionados à pesquisa com pessoas trans/travestis vinculadas à ONG **Minha Criança Trans (MCT)**, em parceria com o **Ministério dos Direitos Humanos e da Cidadania**.

## Etapas do Processo

### 1. Reconhecimento Óptico de Caracteres (OCR)
- A primeira etapa consistiu na aplicação de OCR utilizando a biblioteca **Tesseract OCR**, em conjunto com **OpenCV** e **Pillow**, para converter imagens digitalizadas dos formulários em texto bruto.
- Foram utilizados modelos de OCR com configuração customizada (`--oem 3 --psm 6`) para melhor interpretação de formulários semi-estruturados.

### 2. Pré-processamento das Imagens
- As imagens foram convertidas para escala de cinza e binarizadas para melhorar a taxa de acerto do OCR.
- Utilizou-se a função `cv2.threshold()` para separar o conteúdo do fundo e isolar os textos relevantes.

### 3. Extração de Campos
- Após o OCR, utilizamos expressões regulares (`re`) para capturar informações específicas como:
  - Nome da entrevistada
  - Data da entrevista
  - Nome do entrevistador
  - Local e tipo de moradia
  - Identidade de gênero, histórico de transição
  - Escolaridade, histórico de violência, forma de renda, entre outros

### 4. Armazenamento dos Dados
- Os dados extraídos foram organizados em um `DataFrame` do **pandas**.
- Em seguida, exportamos para arquivos `.xlsx` e `.csv` para posterior análise estatística.

## Possibilidades Analíticas

- Análise descritiva por categoria (frequência de respostas, idade média de transição, níveis de escolaridade etc.).
- Geração de dashboards para identificação de padrões (ex: acolhimento x escolaridade, migração x renda).
- Avaliação da consistência dos dados e possíveis viéses de resposta.

## Considerações Éticas

- Todos os dados são **sensíveis** e relacionados a identidade de gênero, história de vida e saúde. A manipulação dos dados exige **consentimento ético** e anonimização.
- Cuidados foram tomados para garantir sigilo e respeito às informações coletadas.

## Bibliotecas Utilizadas

- `pytesseract`
- `opencv-python`
- `Pillow`
- `re`
- `pandas`

## 📁 Estrutura do Projeto

