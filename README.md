# DLCV-Fall-2023-HW2
Please click [this link](https://docs.google.com/presentation/d/1nWH_CmF6iba0kQmi0TV_yI2Emu1EvjrX/edit?usp=sharing&ouid=107585355306558125830&rtpof=true&sd=true) to view the slides of HW2

## Usage
To start working on this assignment, you should clone this repository into your local machine by using the following command.

    git clone https://github.com/DLCV-Fall-2023/hw2-<username>.git
Note that you should replace `<username>` with your own GitHub username.

## Grading
We provide the code for evaluation
    
    python evaluation/grade_hw2_3.py --json_path hw2_data/concepts/input.json --output_dir output --input_dir hw2_data/concepts/

Note that the directory structure of output dir should looks like
```
output folder/
├── 0/
│   ├── 0/
│   │   ├── source0_prompt0_0.png
│   │   ├── source0_prompt0_1.png
│   │   ├── ...
│   │   └── source0_prompt0_100.png
│   ├── 1/
│   │   ├── source0_prompt1_0.png
│   │   └── ...
│   └── 2/
│       ├── source0_prompt2_0.png
│       └── ...
├── 1/
│   ├── 0/
│   │   └── source1_prompt0_0.png
│   └── ...
└── 2/
    ├── ...
    └── 2/
        └── source2_prompt2_0.png
```
the first level is the index of concept, and the second level is the index of prompts. In private test, we will replace the *prompt* and *prompt_4_clip_eval* in input.json
## Submission Rules
### Deadline
2023/11/7 (Tue.) 23:59 (GMT+8)

### Packages
This homework should be done using python 3.8.5. For a list of packages you are allowed to import in this assignment, please refer to the stable-diffusion/environment.yaml for more details.

You can run the following command to install all the packages listed in the requirements.txt:

    conda env create -f stable-diffusion/environment.yaml
    conda activate ldm

Note that using packages with different versions will very likely lead to compatibility issues, so make sure that you install the correct version if one is specified above. E-mail or ask the TAs first if you want to import other packages.

> :warning: You can't use diffuser for easy implementation!

# Q&A
If you have any problems related to HW2, you may
- Use TA hours: Thu. 14:20~15.10 in MK514.
- Contact TAs by e-mail ([ntudlcv@gmail.com](mailto:ntudlcv@gmail.com)) with title [DLCV hw2] Problems about ...
- Post your question under hw2 discuss section in NTU COOL
