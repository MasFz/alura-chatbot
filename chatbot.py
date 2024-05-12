import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
import dotenv
import os
import faiss
from sentence_transformers import SentenceTransformer

# Carrega a API Key do arquivo .env
dotenv.load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Carrega o modelo de embeddings de frases
sentence_model = SentenceTransformer('all-mpnet-base-v2')

# Carrega o conteúdo do arquivo guia.txt
with open('data/guia.txt', 'r') as f:
    guia_content = f.read()

# Divide o conteúdo em frases
guia_sentences = guia_content.split('\n')

# Gera embeddings para cada frase
guia_embeddings = sentence_model.encode(guia_sentences)

# Cria o índice Faiss
index = faiss.IndexFlatL2(guia_embeddings.shape[1])
index.add(guia_embeddings)

# Configurações de geração e segurança do Gemini
generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}
safety_settings = {
    "HATE": "BLOCK_NONE",
    "HARASSMENT": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

# Cria o modelo Gemini
model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Define a instrução ao sistema
system_instruction = "Você é um assistente de novos estagiários dentro de uma nova empresa que explica tudo de maneira clara e objetiva."

# Loop principal do chatbot
prompt = input("Insira o seu prompt: ")
while prompt != "sair":
    # Gera o embedding da pergunta do usuário
    question_embedding = sentence_model.encode([prompt])[0]

    # Busca os vizinhos mais próximos no índice
    D, I = index.search(question_embedding.reshape(1, -1), k=3)

    # Recupera as frases relevantes do guia
    relevant_sentences = [guia_sentences[i] for i in I[0]]

    # Cria o prompt completo com o contexto do documento e a system instruction
    full_prompt = f"{system_instruction}\nContexto:\n{''.join(relevant_sentences)}\n\nPergunta:\n{prompt}"

    # Envia a mensagem e recebe a resposta
    response = model.generate_content(full_prompt)
    print("Resposta: ", response.text, "\n")

    # Obtém o próximo prompt do usuário
    prompt = input("Insira o seu prompt: ")