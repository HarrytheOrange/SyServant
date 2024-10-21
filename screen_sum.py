from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info
import torch
from PIL import Image
import base64
import io
import json
import os
from tqdm import tqdm


model = Qwen2VLForConditionalGeneration.from_pretrained(
        "/mnt/cache/huangzhiyuan/models/Qwen/Qwen2-VL-7B-Instruct",
        torch_dtype=torch.bfloat16,
        attn_implementation="flash_attention_2",
        device_map="auto",
    )
processor = AutoProcessor.from_pretrained("/mnt/cache/huangzhiyuan/models/Qwen/Qwen2-VL-7B-Instruct")


image_dir = "/mnt/cache/huangzhiyuan/WebServant/screenshots"
for image_path in tqdm(os.listdir(image_dir)):

    image_path = image_dir + f'/{image_path}'

    prompt = '''### Instructions:
    1. Please describe this screenshot in detail.
    2. Then infer what help or assist the user may need in this situation.
    3. Please give a general tag about what the user is doing.
    ### Output format:
    {"screen_description": "xxx", "prospective assist": "xxx", "screen_time_tag": "xxx"}
    '''
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image_path},
                {"type": "text", "text": prompt},
            ],
        }
    ]

    # Preparation for inference
    text = processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True, add_vision_id=True
    )
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )
    inputs = inputs.to("cuda")

    # Inference: Generation of the output
    generated_ids = model.generate(**inputs, max_new_tokens=128)
    generated_ids_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    print(output_text)

    output_data_line = {
        "image_path": image_path,
        "answer": output_text[0]
    }

    output_file = "./screen_infer_output.jsonl"
    with open(output_file, 'a') as jsonl_file:
        jsonl_file.write(json.dumps(output_data_line) + '\n')