import json
import argparse
import os
from clip_image_score import calculate_clip_image_scores_folder
from clip_text_score import calculate_clip_text_scores_folder

if __name__ == '__main__':
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process some JSON data.')
    parser.add_argument('--json_path', type=str, help='Path to the JSON file')
    parser.add_argument('--input_dir', type=str, default='.', help='Root directory of the hw2_data')
    parser.add_argument('--output_dir', type=str, default='.', help='Directory of saved output')
    
    # Parse the arguments
    args = parser.parse_args()
    json_path = args.json_path
    input_dir = args.input_dir
    output_dir = args.output_dir
    
    # Assuming the JSON is saved in a file named 'data.json'
    with open(json_path, 'r') as f:
        data = json.load(f)

    total_image_score = 0
    total_text_score = 0
    count = 0

    # Iterate through the data and print the prompt_4_clip_eval
    for key, value in data.items():
        input_folder_path = os.path.join(input_dir, key)
        output_folder_path = os.path.join(output_dir, key)

        src = value['src_image']

        for idx, clip_eval in enumerate(value['prompt_4_clip_eval']):
            prompt_output_folder_path = os.path.join(output_folder_path, str(idx))
            print(f"Image source \"{src}\", text prompt: {clip_eval}")
            score = calculate_clip_image_scores_folder(prompt_output_folder_path, input_folder_path)
            print(f"CLIP Image Score: {score}")
            total_image_score += score
            score = calculate_clip_text_scores_folder(prompt_output_folder_path, clip_eval)
            print(f"CLIP Text Score: {score}")
            total_text_score += score
            count += 1

    print(f"Average Image Score: {total_image_score / count}")
    print(f"Average Text Score: {total_text_score / count}")

    print("Baseline of CLIP Image/Text score: 60/30")

    