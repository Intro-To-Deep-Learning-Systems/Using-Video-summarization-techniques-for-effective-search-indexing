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
 

## Usage
1) `npm install ` to install required modules
2) `npm start` to start the electron app!

## Coming soon!
We are taking performance logs and evaluating the ML system, so check back in a few days for more on it!