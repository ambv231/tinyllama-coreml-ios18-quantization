import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import coremltools as ct

# === CONFIGURATION ===
model_path = "."
prompt = "Bonjour, comment vas-tu aujourd'hui ?"
float16_model_path = "float16_model.mlpackage"

# 1. Charger modèle HF
print("🔄 Chargement du modèle Hugging Face...")
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float32)
model.eval()
tokenizer = AutoTokenizer.from_pretrained(model_path)

# 2. Exemple d’entrée pour le tracing
inputs = tokenizer(prompt, return_tensors="pt")

# 3. Wrapper pour transformer la sortie en logits
import torch.nn as nn
class WrapperModel(nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = model.eval()
    def forward(self, input_ids):
        return self.model(input_ids).logits

wrapped_model = WrapperModel(model)

# 4. Tracing
print("🧠 Tracing...")
traced_model = torch.jit.trace(wrapped_model, (inputs["input_ids"],), strict=False)

# 5. Conversion CoreML (mlprogram, iOS18)
print("🔁 Conversion en CoreML (MLProgram, iOS18)...")
mlmodel = ct.convert(
    traced_model,
    inputs=[ct.TensorType(shape=inputs["input_ids"].shape)],
    convert_to="mlprogram",
    compute_units=ct.ComputeUnit.CPU_AND_NE,
    minimum_deployment_target=ct.target.iOS18  # ⬅️ IMPORTANT !
)

# 6. Sauvegarde du modèle float16
mlmodel.save(float16_model_path)
print(f"✅ Modèle CoreML float16 exporté : {float16_model_path}")
