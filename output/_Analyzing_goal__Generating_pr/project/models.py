import groq

groq_config = {
    'model': 'llama3-7b-4096',
    'timeout': 10
}

groq_client = groq.GroqClient(config=groq_config)