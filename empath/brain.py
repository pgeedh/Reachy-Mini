import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

class EmpathBrain:
    def __init__(self, model_name="google/gemma-2b-it"):
        print(f"🧠 Loading Brain ({model_name})... this might take a while.")
        try:
            # We use pipeline for simplicity. Device map auto will use GPU if available
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name, 
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                device_map="auto"
            )
            self.history = [
                {"role": "user", "content": "You are Reachy, a small compassionate robot. Your goal is to be a helpful, empathetic companion. You speak briefly and kindly."},
                {"role": "model", "content": "Hello! I am Reachy. I am here to help you smile and feel better. How are you feeling today?"}
            ]
            self.offline = False
            print("🧠 Brain is ONLINE.")
        except Exception as e:
            print(f"⚠️ Brain failed to load: {e}. Switching to Lobotomy Mode (Simple responses).")
            self.offline = True

    def process_query(self, user_text, current_emotion="neutral"):
        """
        Generates a response based on text and user's current emotion.
        """
        if self.offline:
            return self._fallback_response(user_text, current_emotion)

        # Inject emotion context
        context_prompt = f"[User is currently feeling: {current_emotion}]. {user_text}"
        
        # Add to history
        self.history.append({"role": "user", "content": context_prompt})
        
        # Generate
        input_ids = self.tokenizer.apply_chat_template(self.history, return_tensors="pt").to(self.model.device)
        
        outputs = self.model.generate(
            input_ids, 
            max_new_tokens=100, 
            do_sample=True, 
            temperature=0.7
        )
        
        response = self.tokenizer.decode(outputs[0][input_ids.shape[1]:], skip_special_tokens=True)
        
        # Append response
        self.history.append({"role": "model", "content": response})
        
        # Keep history short
        if len(self.history) > 10:
            self.history = self.history[:1] + self.history[-9:]
            
        return response

    def _fallback_response(self, text, emotion):
        if emotion in ["sad", "angry", "fear"]:
            return "I notice you seem upset. I am here for you. Want to see a dance?"
        elif emotion in ["happy", "surprise"]:
            return "You look radiant today! Keeping that energy up!"
        else:
            return "I am listening. Tell me more."
