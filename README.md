## Video Summarization Techniques for effective summarization

## What's this?
Simple! I will break this into 5 steps:
1) We use Video summarization techniques to extract the short summary that is descriptive of the video.
2) We then extract the keyframes using histogram analysis
3) We then generate the image captions for each keyframe.
4) We then remove the stop words, to get the final keywords that are descriptive of the video that can be used for indexing purposes!
   
## How does it work?
1) Video summarization using **DSNet** - *Zhu, Wencheng, et al. "Dsnet: A flexible detect-to-summarize network for video summarization." IEEE Transactions on Image Processing 30 (2020): 948-962.*
2) Image captioning using **ExpansionNetV2** - *Hu, Jia Cheng, Roberto Cavicchioli, and Alessandro Capotondi. "ExpansionNet v2: Block Static Expansion in fast end to end training for Image Captioning." arXiv preprint arXiv:2208.06551 (2022).* ( Can also be swapped for **ClipClap** - *Mokady, Ron, Amir Hertz, and Amit H. Bermano. "Clipcap: Clip prefix for image captioning." arXiv preprint arXiv:2111.09734 (2021).*)
 
## Repo Structure
`\nodeserver` consists of the all the backend

`\nodeserver\pythonscripts\DSNet` consists of the DSNet model

`\nodeserver\pythonscripts\ExpansionNet` consists of ExpansionNetV2 model

`\nodeserver\pythonscripts\imagecaption` consists of CLIPCLAP model.

**In order to switch between ExpansionNet or CLIPCLAP for Image captioning, [modify this line.](https://github.com/Intro-To-Deep-Learning-Systems/Using-Video-summarization-techniques-for-effective-search-indexing/blob/master/nodeserver/pythonscripts/server.py#L108)**

## Usage
1) Download `rf_model.pth` from [here](https://drive.google.com/drive/folders/1h9UY2VadIJYEA3lCyyd1C2j9u7qJWfgg?usp=share_link) and place it in `nodeserver\pythonscripts\ExpansionNet`
2) Download `model_weights.pt` from [here](https://drive.google.com/drive/folders/1h9UY2VadIJYEA3lCyyd1C2j9u7qJWfgg?usp=share_link) and place it in `nodeserver\pythonscripts\imagecaption\model`
3) `npm install ` to install required modules
4) `pip install -r requirements.txt` to install python modules
5) `npm start` to start the electron app!

## Experiments and Evaluations

For detailed evaluations, please refer to [comparisons.ipynb](comparisons.ipynb). Evaluations include:
1) Performance in seconds
2) Bleu score
3) ROUGE-1 Precision 
4) ROUGE-1 Recall
5) ROUGE-L Precision
6) ROUGE-L Recall
7) Search engine Recall score
