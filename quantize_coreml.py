import coremltools as ct
from coremltools.optimize.coreml import OpLinearQuantizerConfig, OptimizationConfig, linear_quantize_weights
import os

# --- Parameters ---
base_dir = "Models/TinyLlama/coreml/text-generation"
float16_model_path = "float16_model.mlpackage"
quant8_model_path  = os.path.join(base_dir, "quant8_model.mlpackage")
quant4_model_path  = os.path.join(base_dir, "quant4_model.mlpackage")

# --- Load float16 CoreML model ---
print(f"🔄 Loading float16 model: {float16_model_path}")
model = ct.models.MLModel(float16_model_path)

# --- Quantize to 8 bits (int8) ---
print("⚡ Quantizing to 8 bits (int8)...")
op_config = OpLinearQuantizerConfig(mode="linear_symmetric")
config = OptimizationConfig(global_config=op_config)
try:
    quant8_model = linear_quantize_weights(model, config=config)
    quant8_model.save(quant8_model_path)
    print(f"✅ Quantized int8 model saved: {quant8_model_path}")
except Exception as e:
    print(f"❌ Quantization to int8 failed: {e}")

# --- Quantize to 4 bits (int4) ---
print("⚡ Quantizing to 4 bits (int4)...")
try:
    op_config_4bit = OpLinearQuantizerConfig(
        mode="linear_symmetric",
        dtype="int4",
        granularity="per_block",
        block_size=32,
    )
    config_4bit = OptimizationConfig(global_config=op_config_4bit)
    quant4_model = linear_quantize_weights(model, config=config_4bit)
    quant4_model.save(quant4_model_path)
    print(f"✅ Quantized int4 model saved: {quant4_model_path}")
except Exception as e:
    print(f"❌ Quantization to int4 failed: {e}")

print("🎉 Script finished. Check the size of generated files and test them in Xcode or on your device!")