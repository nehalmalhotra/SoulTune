import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def generate_dna_profile(genre, dsp_metrics):
    """
    Injects raw audio math into a zero-shot prompt to generate a poetic DNA profile.
    """
    print("Initiating Gemini LLM translation...")

    # Using the fast model since we just need a quick text generation
    model = genai.GenerativeModel('gemini-2.5-flash')

    # The Zero-Shot Prompt Injection
    prompt = f"""
        You are SonicDNA, an AI Music Geneticist.
        
        Your job is to analyze the mathematical fingerprint of a song and produce a structured DNA report.
        
        INPUT DATA:
        
        Genre: {genre}
        Tempo (BPM): {dsp_metrics['bpm']}
        Energy (RMSE): {dsp_metrics['energy_rmse']}
        Brightness (Spectral Centroid): {dsp_metrics['brightness_centroid']} Hz
        
        INTERPRETATION RULES:
        
        Tempo:
        - High tempo = kinetic, restless, accelerating, soaring
        - Medium tempo = balanced, flowing, dynamic
        - Low tempo = grounded, deliberate, reflective
        
        Energy:
        - High energy = powerful, explosive, intense
        - Medium energy = steady, confident
        - Low energy = delicate, fragile, atmospheric
        
        Brightness:
        - High brightness = crystalline, neon, sharp, radiant
        - Medium brightness = clear, vivid, balanced
        - Low brightness = warm, shadowed, earthy
        
        TASK:
        
        Generate a SonicDNA report using EXACTLY this format:
        
        DNA Category: <create a unique 2-word name>
        
        Core Traits:
        - <trait 1>
        - <trait 2>
        - <trait 3>
        
        Genetic Summary:
        <exactly 3 sentences>
        
        RULES:
        
        1. Do NOT mention BPM values, numbers, Hz values, RMSE values, or technical terms.
        2. The DNA Category should feel like a species or archetype name.
        3. The Core Traits must be concise personality descriptors.
        4. The Genetic Summary must sound intelligent and artistic, not random fantasy poetry.
        5. Make the output clearly influenced by the supplied genre.
        6. Output ONLY the report. No markdown. No explanations.
        """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"LLM Error: {e}")
        return "The genetic sequence was too complex to translate at this time."
