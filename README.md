# tinyllama-coreml-ios18-quantization

**By GreenBull31 (Morgan CAMILLERI)**

---

## 🚀 Quantizing TinyLlama to CoreML int4/int8 for iOS 18+

This repository provides a simple, up-to-date pipeline to convert [TinyLlama-1.1B-Chat](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v0.3) from Hugging Face PyTorch format to CoreML `.mlpackage`, and then quantize it to **int8** and **int4** weights (the latter being supported from iOS 18+).

* **int8**: Compatible with iOS 17+
* **int4**: Super lightweight, compatible with iOS 18+
* **Tested May 2025, works on Apple Silicon (M1/M2/M3), Python 3.11+**

---

## 🟢 Workflow Overview

1. **Download TinyLlama-1.1B-Chat (PyTorch) from Hugging Face**
2. **Convert to CoreML float16 (.mlpackage) with iOS 18 minimum deployment target**
3. **Quantize to int8 and int4**
4. **Integrate into your iOS 18+ app**

---

## 📦 Files in this repo

* `convert_tinyllama_to_coreml.py` — Convert PyTorch → CoreML float16 (iOS 18+)
* `quantize_coreml.py` — Quantize the .mlpackage (float16) into int8 and int4 variants

---

## 🛠️ Prerequisites

* **Python 3.10+** (tested with 3.11)
* **Apple Silicon Mac (M1/M2/M3)** recommended
* **coremltools >= 8.3**
* **torch >= 2.2**
* **transformers**

```bash
pip install --upgrade coremltools torch transformers
```

---

## ⚡ Quick Start

### 1️⃣ Download model from Hugging Face

* Go to [https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v0.3](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v0.3)
* Download:

  * `config.json`
  * `pytorch_model.bin`
  * `tokenizer.model`
  * Place in the same folder as the scripts

### 2️⃣ Convert to CoreML float16

```bash
python3 convert_tinyllama_to_coreml.py
```

* Output: `float16_model.mlpackage`

### 3️⃣ Quantize to int8 and int4

```bash
python3 quantize_coreml.py
```

* Output: `quant8_model.mlpackage`, `quant4_model.mlpackage`

### 4️⃣ Integrate and test in your iOS 18+ app

* For int4, set your deployment target to **iOS 18+**.
* Works on iPhone 12 Pro and newer!

---

## 🟣 Notes

* **int4 quantization** is only supported if the model is converted with `minimum_deployment_target=ct.target.iOS18`.
* For smaller models or testing, you can adapt the script to other Llama-like architectures (Phi-2, Gemma, etc).
* If you hit a dtype error (fp32/fp16) during conversion, set `torch_dtype=torch.float32` in your script.

---

## 🦾 Credits & Contact

**Author:** GreenBull31 (Morgan CAMILLERI)

* [Hugging Face Profile](https://huggingface.co/GreenBull31)
* [GitHub Profile](https://github.com/GreenBull31)

Feel free to open an issue or a PR!

---

### License

MIT
