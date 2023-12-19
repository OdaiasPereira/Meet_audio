import os
import openai
from docx import Document

# Sua chave de API OpenAI
api_key = "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"

def rewrite_text(text_to_rewrite):
    # Output file for the rewritten content in .docx format
    #output_file = "C:/Users/odaia/PycharmProjects/Log_Generator"
    output_file = "outputs/test.docx"

    # Cria o diretório de saída se não existir
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Sua chave de API OpenAI
    api_key = "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"

    # Prompt para reescrever o texto
    initial_prompt = """Por favor transcreva utilizando essas instruções:
    1. Substitua quaisquer termos complexos ou técnicos por linguagem mais simples e amigável para leigos.
    2. Parafraseie as sentenças para melhorar a clareza, mantendo o significado original.
    3. Certifique-se de que o texto reescrito flua de maneira coesa e mantenha uma estrutura lógica.
    4. Verifique e corrija erros gramaticais ou frases desconfortáveis.
    5. Ajuste o tom para ser mais envolvente e acessível.
    6. Se aplicável, forneça exemplos do mundo real ou analogias para ilustrar conceitos.
    7. Condense frases ou parágrafos longos sem perder informações essenciais.
    8. Certifique-se de que o conteúdo reescrito esteja alinhado com o contexto e a intenção originais.
    9. Preste atenção à consistência na formatação e estilo ao longo do texto.
    10.Busque uma contagem final de palavras semelhante ao texto original.
    11.Troque gírias por palavras pertencentes a linguá portuguesa formal
    12. Em um diálogo a cada troca de pessoa criar uma nova linha
    Please follow these instructions to provide a rewritten version.
    """

    # Combine as instruções com o texto a ser reescrito
    prompt = initial_prompt + "\n" + text_to_rewrite

    # Usa ChatGPT-4 para gerar o conteúdo reescrito com um contexto de 32.000 tokens
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that rewrites books."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=4000,  # Defina para 8192 para usar o contexto completo
        api_key=api_key,
    )

    rewritten_text = response.choices[0].message["content"]

    # Cria um novo documento do Word
    doc = Document()
    doc.add_paragraph(rewritten_text)

    # Salva o documento do Word no arquivo de saída
    doc.save(output_file)
