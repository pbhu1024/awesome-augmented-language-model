# 🔥Awesome Augmented Language Model [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
This repo collect research papers about leveraging the capabilities of language models, which can be a good reference for building upper-layer applications.



## Contents
- [Model](#model)
    - [Foundation Model](#foundation-model)
    - [Instruction Model](#instruction-model)
    - [Alignment and RLHF](#alignment-and-rlhf)
    - [Dialogue Model](#dialogue-model)
- [Prompt](#prompt)
    - [Hard Prompt](#hard-prompt)
    - [Soft Prompt](#soft-prompt)
    - [Dialogue Prompt](#dialogue-prompt) 
- [Information Seeking](#information-seeking)
    - [Extra Knowledge](#extra-knowledge)
    - [Extra Modality](#extra-modality)
    - [Web Search](#web-search)
- [Action and Plan](#action-and-plan)
- [Reasoning](#reasoning)
- [Long-text Generation](#long-text-generation)
- [Analysis and Boundary](#analysis-and-boundary)
- [Motivation](#motivation)
    - [Persona](#persona)
    - [Emotion](#emotion)
- [Application](#application)
- [Safety](#safety)
- [Related Project](#related-project)
## Model
❗  Here, only generative language models are included. 
### Foundation Model
- Amatriain, Xavier, **Transformer models: an introduction and catalog**, 2023 [[Paper]](http://arxiv.org/abs/2302.07730)

- Zhou, Ce and Li, Qian and Li, Chen and Yu, Jun et al., **A Comprehensive Survey on Pretrained Foundation Models: A History from BERT to ChatGPT**, 2023 [[Paper]](http://arxiv.org/abs/2302.09419)

- Radford, Alec and Narasimhan, Karthik and Salimans, Tim and Sutskever, Ilya, **Improving Language Understanding by Generative Pre-Training**, 2023 [[Paper]]()

- Radford, Alec and Wu, Jeffrey and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya, **Language Models are Unsupervised Multitask Learners**, 2023 [[Paper]]()

- Smith, Shaden and Patwary, Mostofa and Norick, Brandon et al., **Using DeepSpeed and Megatron to Train Megatron-Turing NLG 530B, A Large-Scale Generative Language Model**, 2022 [[Paper]](http://arxiv.org/abs/2201.11990)

- Du, Nan and Huang, Yanping and Dai, Andrew M. and Tong, Simon et al., **GLaM: 
Efficient Scaling of Language Models with Mixture-of-Experts**, 2022 [[Paper]](http://arxiv.org/abs/2112.06905)

- Borgeaud, Sebastian and Mensch, Arthur and Hoffmann, Jordan et al., **Improving language models by retrieving from trillions of tokens**, 2022 [[Paper]](http://arxiv.org/abs/2112.04426)

- Hoffmann, Jordan and Borgeaud, Sebastian and Mensch, Arthur et al., **Training Compute-Optimal Large Language 
Models**, 2022 [[Paper]](http://arxiv.org/abs/2203.15556)

- Workshop, BigScience and Scao, Teven Le, et al., **BLOOM: A 176B-Parameter Open-Access Multilingual Language Model**, 2022 [[Paper]](http://arxiv.org/abs/2211.05100)

- Zhang, Susan and Roller, Stephen and Goyal, Naman et al., **OPT: Open Pre-trained Transformer Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2205.01068)
 
- Chowdhery, Aakanksha and Narang, Sharan and Devlin, Jacob et al., **PaLM: Scaling Language Modeling with Pathways**, 2022 [[Paper]](http://arxiv.org/abs/2204.02311)

- Bai, Yuntao and Kadavath, Saurav and Kundu, Sandipan et al., **Constitutional AI: Harmlessness from AI Feedback**, 2022 [[Paper]]()

- Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming et al., **Evaluating Large Language Models Trained on Code**, 2021 [[Paper]](http://arxiv.org/abs/2107.03374)

- Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J., **Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer**, 2020 [[Paper]](http://arxiv.org/abs/1910.10683)

- Brown, Tom B. and Mann, Benjamin and Ryder, Nick and Subbiah, Melanie et al., **Language Models are Few-Shot Learners**, 2020 [[Paper]](http://arxiv.org/abs/2005.14165)

- Lieber, Opher and Sharir, Or and Lentz, Barak and Shoham, Yoav, **Jurassic-1: Technical Details and Evaluation**, 2020 [[Paper]](https://uploads-ssl.webflow.com/60fd4503684b466578c0d307/61138924626a6981ee09caf6_jurassic_tech_paper.pdf)

- Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Ves and Zettlemoyer, Luke, **BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension**, 2019 [[Paper]](http://arxiv.org/abs/1910.13461)

### Instruction Model
- Touvron, Hugo and Lavril, Thibaut and Izacard, Gautier et al., **LLaMA: Open and Efficient Foundation Language Models**, 2023 [[Paper]](https://research.facebook.com/file/1574548786327032/LLaMA--Open-and-Efficient-Foundation-Language-Models.pdf)

- Longpre, Shayne and Hou, Le and Vu, Tu and Webson, Albert and Chung, Hyung Won and Tay, Yi and Zhou, Denny and Le, Quoc V. and Zoph, Barret and Wei, Jason and Roberts, Adam, **The Flan Collection: Designing Data and Methods for Effective Instruction Tuning**, 2023 [[Paper]](http://arxiv.org/abs/2301.13688)

- Iyer, Srinivasan and Lin, Xi Victoria and Pasunuru, Ramakanth et al., **OPT-IML: Scaling Language Model Instruction Meta Learning through the Lens of Generalization**, 2023 [[Paper]](http://arxiv.org/abs/2212.12017)

- Bai, Yuntao and Jones, Andy and Ndousse, Kamal et al., **Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback**, 2022 [[Paper]](https://arxiv.org/abs/2204.05862v1)

- Ouyang, Long and Wu, Jeff and Jiang, Xu and Almeida, Diogo et al., **Training language models to follow instructions with human feedback**, 2022 [[Paper]](http://arxiv.org/abs/2203.02155)

- Hoffmann, Jordan and Borgeaud, Sebastian and Mensch, Arthur et al., **Training Compute-Optimal Large Language 
Models**, 2022 [[Paper]](http://arxiv.org/abs/2203.15556)


- Chung, Hyung Won and Hou, Le and Longpre, Shayne and Zoph, Barret  et al., **Scaling Instruction-Finetuned Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2210.11416)

- Scheurer, Jérémy and Campos, Jon Ander and Chan, Jun Shern and Chen, Angelica and Cho, Kyunghyun and Perez, Ethan, **Training Language Models with Language Feedback**, 2022 [[Paper]](https://arxiv.org/abs/2204.14146v4)


### Alignment and RLHF
- Kwon, Minae and Xie, Sang Michael and Bullard, Kalesha and Sadigh, Dorsa, **Reward Design with Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2303.00001)

- Go, Dongyoung and Korbak, Tomasz and Kruszewski, Germán and Rozen, Jos and Ryu, Nahyeon and Dymetman, Marc, **Aligning Language Models with Preferences through f-divergence Minimization**, 2023 [[Paper]](http://arxiv.org/abs/2302.08215)

- Myers, Vivek and Bıyık, Erdem and Sadigh, Dorsa, **Active Reward Learning from Online Preferences**, 2023 [[Paper]](http://arxiv.org/abs/2302.13507)

- Hartmann, Jochen and Schwenzow, Jasper and Witte, Maximilian, **The political ideology of conversational AI: Converging evidence on ChatGPT's pro-environmental, left-libertarian orientation**, 2023 [[Paper]](http://arxiv.org/abs/2301.01768)

- Liu, Ruibo and Jia, Chenyan and Zhang, Ge and Zhuang, Ziyu and Liu, Tony X. and Vosoughi, Soroush, **Second Thoughts are Best: Learning to Re-Align With Human Values from Text Edits**, 2023 [[Paper]](http://arxiv.org/abs/2301.00355)        

- Mechergui, Malek and Sreedharan, Sarath, **Goal Alignment: A Human-Aware Account of Value Alignment Problem**, 2023 [[Paper]](http://arxiv.org/abs/2302.00813)

- Ganguli, Deep and Lovitt, Liane and Kernion, Jackson et al., **Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned**, 2023 [[Paper]]()

- Liu, Hao and Sferrazza, Carmelo and Abbeel, Pieter, **Languages are Rewards: Hindsight Finetuning using Human Feedback**, 2023 [[Paper]](http://arxiv.org/abs/2302.02676)

- Prabhumoye, Shrimai and Patwary, Mostofa and Shoeybi, Mohammad and Catanzaro, Bryan, **Adding Instructions during Pretraining: Effective Way of Controlling Toxicity in Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.07388)      

- Ganguli, Deep and Askell, Amanda and Schiefer, Nicholas et al., **The Capacity for Moral Self-Correction in Large Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.07459)

- Korbak, Tomasz and Shi, Kejian and Chen, Angelica and Bhalerao, Rasika and Buckley, Christopher L. and Phang, Jason and Bowman, Samuel R. and Perez, Ethan, **Pretraining Language Models with Human Preferences**, 2023 [[Paper]](http://arxiv.org/abs/2302.08582)

- Lee, Kimin and Liu, Hao and Ryu, Moonkyung and Watkins, Olivia and Du, Yuqing and Boutilier, Craig and Abbeel, Pieter and Ghavamzadeh, Mohammad and Gu, Shixiang Shane, **Aligning Text-to-Image Models using Human Feedback**, 2023 [[Paper]](http://arxiv.org/abs/2302.12192)

- Bakker, Michiel A. and Chadwick, Martin J. and Sheahan, Hannah R. and Tessler, Michael Henry and Campbell-Gillingham, Lucy and Balaguer, Jan and McAleese, Nat and Glaese, Amelia and Aslanides, John and Botvinick, Matthew M. and Summerfield, Christopher, **Fine-tuning language models to find agreement among humans with diverse preferences**, 2022 [[Paper]](http://arxiv.org/abs/2211.15006)

- Glaese, Amelia and McAleese, Nat and Trębacz, Maja et al., **Improving alignment of dialogue agents via targeted human judgements**, 2022 [[Paper]](http://arxiv.org/abs/2209.14375)

- Stiennon, Nisan and Ouyang, Long and Wu, Jeff and Ziegler, Daniel M. and Lowe, Ryan and Voss, Chelsea and Radford, Alec and Amodei, Dario and Christiano, Paul, **Learning to summarize from human feedback**, 2022 [[Paper]](http://arxiv.org/abs/2009.01325)

- Bai, Yuntao and Jones, Andy and Ndousse, Kamal et al., **Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback**, 2022 [[Paper]](http://arxiv.org/abs/2204.05862)

- Bai, Yuntao and Kadavath, Saurav and Kundu, Sandipan et al., **Constitutional AI: Harmlessness from AI Feedback**, 2022 [[Paper]](http://arxiv.org/abs/2212.08073)

- Zhao, Lingjun and Nguyen, Khanh and Daumé III, Hal, **A Cognitive Evaluation of Instruction Generation Agents tl;dr They Need Better Theory-of-Mind Capabilities**, 2022 [[Paper]](http://arxiv.org/abs/2301.05149)

- Askell, Amanda and Bai, Yuntao and Chen, Anna et al., **A General Language Assistant as a Laboratory for Alignment**, 2021 [[Paper]](http://arxiv.org/abs/2112.00861)

### Dialogue Model
- Thoppilan, Romal and De Freitas, Daniel and Hall, Jamie et al., **LaMDA: Language Models for Dialog Applications**, 2022 [[Paper]](http://arxiv.org/abs/2201.08239)

- Shuster, Kurt and Xu, Jing and Komeili, Mojtaba and Ju, Da et al., **BlenderBot 3: a deployed conversational agent that continually learns to responsibly engage**, 2022 [[Paper]](http://arxiv.org/abs/2208.03188)

- Glaese, Amelia and McAleese, Nat and Trębacz, Maja et al., **Improving alignment of dialogue agents via targeted human judgements**, 2022 [[Paper]](http://arxiv.org/abs/2209.14375)

- Zhang, Yizhe and Sun, Siqi and Galley, Michel and Chen, Yen-Chun and Brockett, Chris and Gao, Xiang and Gao, Jianfeng and Liu, Jingjing and Dolan, Bill, **DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation**, 2020 [[Paper]](http://arxiv.org/abs/1911.00536)

- Zhang, Yizhe and Sun, Siqi and Galley, Michel and Chen, Yen-Chun and Brockett, Chris and Gao, Xiang and Gao, Jianfeng and Liu, Jingjing and Dolan, Bill, **DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation**, 2020 [[Paper]](http://arxiv.org/abs/1911.00536)
 
## Prompt
### Hard Prompt
- Kim, Seungone and Joo, Se June and Jang, Yul and Chae, Hyungjoo and Yeo, Jinyoung, **CoTEVer: Chain of Thought Prompting Annotation Toolkit for Explanation Verification**, 2023 [[Paper]](http://arxiv.org/abs/2303.03628)

- Wei, Jerry and Wei, Jason and Tay, Yi and Tran, Dustin and Webson, Albert and Lu, Yifeng and Chen, Xinyun and Liu, Hanxiao and Huang, Da and Zhou, Denny and Ma, Tengyu, **Larger language models do in-context learning differently**, 2023 [[Paper]](http://arxiv.org/abs/2303.03846)

- Singh, Chandan and Morris, John X. and Aneja, Jyoti and Rush, Alexander M. and Gao, Jianfeng, **Explaining Patterns in Data with Language Models via Interpretable Autoprompting**, 2023 [[Paper]](http://arxiv.org/abs/2210.01848)

- Zhang, Renrui and Hu, Xiangfei and Li, Bohao and Huang, Siyuan and Deng, Hanqiu and Li, Hongsheng and Qiao, Yu and Gao, Peng, **Prompt, Generate, then Cache: Cascade of Foundation Models makes Strong Few-shot Learners**, 2023 [[Paper]](http://arxiv.org/abs/2303.02151)

- Wu, Zhiyong and Wang, Yaoxiang and Ye, Jiacheng and Kong, Lingpeng, **Self-adaptive In-context Learning**, 2022 [[Paper]](http://arxiv.org/abs/2212.10375)

- Lu, Yao and Bartolo, Max and Moore, Alastair and Riedel, Sebastian and Stenetorp, Pontus, **Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity**, 2022 [[Paper]](http://arxiv.org/abs/2104.08786)

- Wu, Zhenyu and Wang, YaoXiang and Ye, Jiacheng and Feng, Jiangtao and Xu, Jingjing and Qiao, Yu and Wu, Zhiyong, **OpenICL: An Open-Source Framework for In-context Learning**, 2023 [[Paper]](http://arxiv.org/abs/2303.02913)

- Ye, Seonghyeon and Hwang, Hyeonbin and Yang, Sohee and Yun, Hyeongu and Kim, Yireun and Seo, Minjoon, **In-Context Instruction Learning**, 2023 [[Paper]](http://arxiv.org/abs/2302.14691)

- Liu, Hao and Sferrazza, Carmelo and Abbeel, Pieter, **Chain of Hindsight Aligns Language Models with Feedback**, 2023 [[Paper]](http://arxiv.org/abs/2302.02676)

- Shum, KaShun and Diao, Shizhe and Zhang, Tong, **Automatic Prompt Augmentation and Selection with Chain-of-Thought from Labeled Data**, 2023 [[Paper]](http://arxiv.org/abs/2302.12822)

- Diao, Shizhe and Wang, Pengcheng and Lin, Yong and Zhang, Tong, **Active Prompting with Chain-of-Thought for Large Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.12246)

- Li, Xiaonan and Qiu, Xipeng, **Finding Supporting Examples for In-Context Learning**, 2023 [[Paper]](http://arxiv.org/abs/2302.13539)

- Wang, Yunlong and Shen, Shuyuan and Lim, Brian Y., **RePrompt: Automatic Prompt Editing to Refine AI-Generative Art Towards Precise Expressions**, 2023 [[Paper]](http://arxiv.org/abs/2302.09466)

- Wei, Xiang and Cui, Xingyu and Cheng, Ning and Wang, Xiaobin and Zhang, Xin and Huang, Shen and Xie, Pengjun and Xu, Jinan and Chen, Yufeng and Zhang, Meishan and Jiang, Yong and Han, Wenjuan, **Zero-Shot Information Extraction via Chatting with ChatGPT**, 2023 [[Paper]](http://arxiv.org/abs/2302.10205)

- Li, Zekun and Peng, Baolin and He, Pengcheng and Galley, Michel and Gao, Jianfeng and Yan, Xifeng, **Guiding Large Language Models via Directional Stimulus Prompting**, 2023 [[Paper]](http://arxiv.org/abs/2302.11520)

- Diao, Shizhe and Wang, Pengcheng and Lin, Yong and Zhang, Tong, **Active Prompting with Chain-of-Thought for Large Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.12246)

- Zhang, Zhuosheng and Zhang, Aston and Li, Mu and Zhao, Hai and Karypis, George and Smola, Alex, **Multimodal Chain-of-Thought Reasoning in Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.00923)

- Wen, Yuxin and Jain, Neel and Kirchenbauer, John and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom, **Hard Prompts Made Easy: Gradient-Based Discrete Optimization for Prompt Tuning and Discovery**, 2023 [[Paper]](http://arxiv.org/abs/2302.03668)

- Goswami, Koustava and Lange, Lukas and Araki, Jun and Adel, Heike, **SwitchPrompt: Learning Domain-Specific Gated Soft Prompts for Classification in Low-Resource Domains**, 2023 [[Paper]](http://arxiv.org/abs/2302.06868)

- Cheng, Zhoujun and Kasai, Jungo and Yu, Tao, **Batch Prompting: Efficient Inference with Large Language Model APIs**, 2023 [[Paper]](http://arxiv.org/abs/2301.08721)

- Lyu, Qing and Havaldar, Shreya and Stein, Adam and Zhang, Li and Rao, Delip and Wong, Eric and Apidianaki, Marianna and Callison-Burch, Chris, **Faithful Chain-of-Thought Reasoning**, 2023 [[Paper]](http://arxiv.org/abs/2301.13379)

- Shao, Zhihong and Gong, Yeyun and Shen, Yelong and Huang, Minlie and Duan, Nan and Chen, Weizhu, **Synthetic Prompting: Generating Chain-of-Thought Demonstrations for Large Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.00618) 

- Wang, Yizhong and Kordi, Yeganeh and Mishra, Swaroop and Liu, Alisa and Smith, Noah A. and Khashabi, Daniel and Hajishirzi, Hannaneh, **Self-Instruct: Aligning Language Model with Self Generated Instructions**, 2022 [[Paper]](http://arxiv.org/abs/2212.10560)

- Deng, Mingkai and Wang, Jianyu and Hsieh, Cheng-Ping and Wang, Yihan and Guo, Han and Shu, Tianmin and Song, Meng and Xing, Eric P. and Hu, Zhiting, **RLPrompt: Optimizing Discrete Text Prompts With Reinforcement Learning**, 2022 [[Paper]](http://arxiv.org/abs/2205.12548)

- Khot, Tushar and Trivedi, Harsh and Finlayson, Matthew and Fu, Yao and Richardson, Kyle and Clark, Peter and Sabharwal, Ashish, **Decomposed Prompting: A Modular Approach for Solving Complex Tasks**, 2022 [[Paper]](http://arxiv.org/abs/2210.02406)

- Khot, Tushar and Richardson, Kyle and Khashabi, Daniel and Sabharwal, Ashish, **Hey AI, Can You Solve Complex Tasks by Talking to Agents?**, 2022 [[Paper]](http://arxiv.org/abs/2110.08542)

- Honovich, Or and Shaham, Uri and Bowman, Samuel R. and Levy, Omer, **Instruction Induction: From Few Examples to Natural Language Task Descriptions**, 2022 [[Paper]](http://arxiv.org/abs/2205.10782)

- Yuan, Weizhe and Liu, Pengfei, **reStructured Pre-training**, 2022 [[Paper]](http://arxiv.org/abs/2206.11147)

- Zhong, Wanjun and Gao, Yifan and Ding, Ning and Qin, Yujia and Liu, Zhiyuan and Zhou, Ming and Wang, Jiahai and Yin, Jian and Duan, Nan, **ProQA: Structural Prompt-based Pre-training for Unified Question Answering**, 2022 [[Paper]](http://arxiv.org/abs/2205.04040)

- Zhang, Zhuosheng and Zhang, Aston and Li, Mu and Smola, Alex, **Automatic Chain of Thought Prompting in Large Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2210.03493)

- Kojima, Takeshi and Gu, Shixiang Shane and Reid, Machel and Matsuo, Yutaka and Iwasawa, Yusuke, **Large Language Models are Zero-Shot Reasoners**, 2022 [[Paper]](http://arxiv.org/abs/2205.11916)

- Weng, Jinta and Hu, Yue and Tian, Zhihong and Huang, Heyan, **ConsPrompt: Easily Exploiting Contrastive Samples for Few-shot Prompt Learning**, 2022 [[Paper]](http://arxiv.org/abs/2211.04118)

- Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny, **Self-Consistency Improves Chain of Thought Reasoning in Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2203.11171)

- Beurer-Kellner, Luca and Fischer, Marc and Vechev, Martin, **Prompting Is Programming: A Query Language For Large Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2212.06094)

- Zhou, Yongchao and Muresanu, Andrei Ioan and Han, Ziwen and Paster, Keiran and Pitis, Silviu and Chan, Harris and Ba, Jimmy, **Large Language Models Are Human-Level Prompt Engineers**, 2022 [[Paper]](http://arxiv.org/abs/2211.01910)        

- Anna-Maria Meck, Lisa Precht, **How to Design the Perfect Prompt: A Linguistic Approach to Prompt Design in Automotive Voice Assistants – An Exploratory Study \textbar 13th International Conference on Automotive User Interfaces and Interactive Vehicular Applications**, 2022 [[Paper]](https://dl.acm.org/doi/10.1145/3409118.3475144)

- Arora, Simran and Narayan, Avanika and Chen, Mayee F. and Orr, Laurel and Guha, Neel and Bhatia, Kush and Chami, Ines and Sala, Frederic and Ré, Christopher, **Ask Me Anything: A simple strategy for prompting language models**, 2022 [[Paper]](http://arxiv.org/abs/2210.02441)

- Rubin, Ohad and Herzig, Jonathan and Berant, Jonathan, **Learning To Retrieve Prompts for In-Context Learning**, 2022 [[Paper]](http://arxiv.org/abs/2112.08633)

- Liu, Pengfei and Yuan, Weizhe and Fu, Jinlan and Jiang, Zhengbao and Hayashi, Hiroaki and Neubig, Graham, **Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing**, 2021 [[Paper]](http://arxiv.org/abs/2107.13586)
 
- Reynolds, Laria and McDonell, Kyle, **Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm**, 2021 [[Paper]](http://arxiv.org/abs/2102.07350)

- Liu, Jiachang and Shen, Dinghan and Zhang, Yizhe and Dolan, Bill and Carin, Lawrence and Chen, Weizhu, **What Makes Good In-Context Examples for GPT-3?**, 2021 [[Paper]](http://arxiv.org/abs/2101.06804)

- Perez, Ethan and Kiela, Douwe and Cho, Kyunghyun, **True Few-Shot Learning with Language Models**, 2021 [[Paper]](http://arxiv.org/abs/2105.11447)

- Gao, Tianyu and Fisch, Adam and Chen, Danqi, **Making Pre-trained Language Models Better Few-shot Learners**, 2021 [[Paper]](http://arxiv.org/abs/2012.15723)

- Han, Xu and Zhao, Weilin and Ding, Ning and Liu, Zhiyuan and Sun, Maosong, **PTR: Prompt Tuning with Rules for Text Classification**, 2021 [[Paper]](http://arxiv.org/abs/2105.11259)

- Taylor Shin, Yasaman Razeghi, Robert L. Logan, Eric Wallace, Sameer Singh, **AutoPrompt: Eliciting Knowledge from Language Models with Automatically Generated Prompts**, 2020 [[Paper]](https://arxiv.org/abs/2010.15980)

- Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Chi, Quoc Le, Denny Zhou, **Chain of Thought Prompting Elicits Reasoning in Large Language Models**, 2020 [[Paper]](https://arxiv.org/abs/2201.11903)


### Soft Prompt
- Chen, Derek and Lee, Celine and Lu, Yunan and Rosati, Domenic and Yu, Zhou, **Mixture of Soft Prompts for Controllable Data Generation**, 2023 [[Paper]](http://arxiv.org/abs/2303.01580)

- Yang, Xianjun and Cheng, Wei and Zhao, Xujiang and Petzold, Linda and Chen, Haifeng, **Dynamic Prompting: A Unified Framework for Prompt Tuning**, 2023 [[Paper]](http://arxiv.org/abs/2303.02909)

- Xiao, Guangxuan and Lin, Ji and Han, Song, **Offsite-Tuning: Transfer Learning without Full Model**, 2023 [[Paper]](http://arxiv.org/abs/2302.04870)


- Razdaibiedina, Anastasia and Mao, Yuning and Hou, Rui and Khabsa, Madian and Lewis, Mike and Almahairi, Amjad, **Progressive Prompts: Continual Learning for Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2301.12314)

- Chen, Chen and Zhang, Wei Emma and Shakeri, Alireza Seyed, **Incorporating Knowledge into Document Summarization: an Application of Prefix-Tuning on GPT-2**, 2023 [[Paper]](http://arxiv.org/abs/2301.11719)

- Bowman, Benjamin and Achille, Alessandro and Zancato, Luca and Trager, Matthew and Perera, Pramuditha and Paolini, Giovanni and Soatto, Stefano, **\textbackslash`A-la-carte Prompt Tuning (APT): Combining Distinct Data Via Composable Prompting**, 2023 [[Paper]](http://arxiv.org/abs/2302.07994)

- Sun, Simeng and Liu, Yang and Iter, Dan and Zhu, Chenguang and Iyyer, Mohit, **How Does In-Context Learning Help Prompt Tuning?**, 2023 [[Paper]](http://arxiv.org/abs/2302.11521)
 
- Wang, Zifeng and Zhang, Zizhao and Ebrahimi, Sayna and Sun, Ruoxi and Zhang, Han and Lee, Chen-Yu and Ren, Xiaoqi and Su, Guolong and Perot, Vincent and Dy, Jennifer and Pfister, Tomas, **DualPrompt: Complementary Prompting for Rehearsal-free Continual Learning**, 2022 [[Paper]](http://arxiv.org/abs/2204.04799)

- Nie, Xing and Ni, Bolin and Chang, Jianlong and Meng, Gaomeng and Huo, Chunlei and Zhang, Zhaoxiang and Xiang, Shiming and Tian, Qi and Pan, Chunhong, **Pro-tuning: Unified Prompt Tuning for Vision Tasks**, 2022 [[Paper]](http://arxiv.org/abs/2207.14381)

- Wang, Shijie and Chang, Jianlong and Wang, Zhihui and Li, Haojie and Ouyang, Wanli and Tian, Qi, **Fine-grained Retrieval Prompt Tuning**, 2022 [[Paper]](http://arxiv.org/abs/2207.14465)

- Santos, Cicero Nogueira dos and Dong, Zhe and Cer, Daniel and Nham, John and Shakeri, Siamak and Ni, Jianmo and Sung, Yun-hsuan, **Knowledge Prompts: Injecting World Knowledge into Language Models through Soft Prompts**, 2022 [[Paper]](http://arxiv.org/abs/2210.04726)

- Ma, Fang and Zhang, Chen and Ren, Lei and Wang, Jingang and Wang, Qifan and Wu, Wei and Quan, Xiaojun and Song, Dawei, **XPrompt: Exploring the Extreme of Prompt Tuning**, 2022 [[Paper]](http://arxiv.org/abs/2210.04457)

- Liu, Xiao and Ji, Kaixuan and Fu, Yicheng and Tam, Weng Lam and Du, Zhengxiao and Yang, Zhilin and Tang, Jie, **P-Tuning v2: Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks**, 2022 [[Paper]](http://arxiv.org/abs/2110.07602)

- Cui, Ganqu and Hu, Shengding and Ding, Ning and Huang, Longtao and Liu, Zhiyuan, **Prototypical Verbalizer for Prompt-based Few-shot Tuning**, 2022 [[Paper]](http://arxiv.org/abs/2203.09770)

- He, Yun and Zheng, Huaixiu Steven and Tay, Yi and Gupta, Jai and Du, Yu and Aribandi, Vamsi and Zhao, Zhe and Li, YaGuang and Chen, Zhao and Metzler, Donald and Cheng, Heng-Tze and Chi, Ed H., **HyperPrompt: Prompt-based Task-Conditioning of Transformers**, 2022 [[Paper]](http://arxiv.org/abs/2203.00759)

- Gu, Yuxian and Han, Xu and Liu, Zhiyuan and Huang, Minlie, **PPT: Pre-trained Prompt Tuning for Few-shot Learning**, 2021 [[Paper]](http://arxiv.org/abs/2109.04332)

- Li, Xiang Lisa and Liang, Percy, **Prefix-Tuning: Optimizing Continuous Prompts for Generation**, 2021 [[Paper]](http://arxiv.org/abs/2101.00190)

- Logan IV, Robert L. and Balažević, Ivana and Wallace, Eric and Petroni, Fabio and Singh, Sameer and Riedel, Sebastian, **Cutting Down on Prompts and Parameters: Simple Few-Shot Learning with Language Models**, 2021 [[Paper]](http://arxiv.org/abs/2106.13353)

- Peters, Matthew E. and Ruder, Sebastian and Smith, Noah A., **To Tune or Not to Tune? Adapting Pretrained Representations to Diverse Tasks**, 2019 [[Paper]](http://arxiv.org/abs/1903.05987)


### Dialogue Prompt
- Madaan, Aman and Tandon, Niket and Clark, Peter and Yang, Yiming, **Memory-assisted prompt editing to improve GPT-3 after deployment**, 2023 [[Paper]](http://arxiv.org/abs/2201.06009)

- Chen, Maximillian and Papangelis, Alexandros and Tao, Chenyang and Kim, Seokhwan and Rosenbaum, Andy and Liu, Yang and Yu, Zhou and Hakkani-Tur, Dilek, **PLACES: Prompting Language Models for Social Conversation Synthesis**, 2023 [[Paper]](http://arxiv.org/abs/2302.03269)

- White, Jules and Fu, Quchen and Hays, Sam and Sandborn, Michael and Olea, Carlos and Gilbert, Henry and Elnashar, Ashraf and Spencer-Smith, Jesse and Schmidt, Douglas C., **A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT**, 2023 [[Paper]](http://arxiv.org/abs/2302.11382)

- Ross, Steven I. and Muller, Michael and Martinez, Fernando and Houde, Stephanie and Weisz, Justin D., **A Case Study in Engineering a Conversational Programming Assistant's Persona**, 2023 [[Paper]](http://arxiv.org/abs/2301.10016)


- Lee, Young-Jun and Lim, Chae-Gyun and Choi, Ho-Jin, **Does GPT-3 Generate Empathetic Dialogues? A Novel In-Context Example Selection Method and Automatic Evaluation Metric for Empathetic Dialogue Generation**, 2022 [[Paper]](https://aclanthology.org/2022.coling-1.56)

- Liu, Zihan and Patwary, Mostofa and Prenger, Ryan and Prabhumoye, Shrimai and Ping, Wei and Shoeybi, Mohammad and Catanzaro, Bryan, **Multi-Stage Prompting for Knowledgeable Dialogue Generation**, 2022 [[Paper]](http://arxiv.org/abs/2203.08745)

- Mehri, Shikib and Altun, Yasemin and Eskenazi, Maxine, **LAD: Language Models as Data for Zero-Shot Dialog**, 2022 [[Paper]](http://arxiv.org/abs/2207.14393)

- Gupta, Prakhar and Jiao, Cathy and Yeh, Yi-Ting and Mehri, Shikib and Eskenazi, Maxine and Bigham, Jeffrey P., **InstructDial: Improving Zero and Few-shot Generalization in Dialogue through Instruction Tuning**, 2022 [[Paper]](http://arxiv.org/abs/2205.12673)

- Li, Zekun and Chen, Wenhu and Li, Shiyang and Wang, Hong and Qian, Jing and Yan, Xifeng, **Dialogic: Controllable Dialogue Simulation with In-Context Learning**, 2022 [[Paper]](https://arxiv.org/abs/2210.04185)

- Han, Seungju and Kim, Beomsu and Yoo, Jin Yong and Seo, Seokjun and Kim, Sangbum and Erdenee, Enkhbayar and Chang, Buru, **Meet Your Favorite Character: Open-domain Chatbot Mimicking Fictional Characters with only a Few Utterances**, 2022 [[Paper]](http://arxiv.org/abs/2204.10825)

- Hu, Yushi and Lee, Chia-Hsuan and Xie, Tianbao and Yu, Tao and Smith, Noah A. and Ostendorf, Mari, **In-Context Learning for Few-Shot Dialogue State Tracking**, 2022 [[Paper]](http://arxiv.org/abs/2203.08568)

- Saha, Debjoy and Santra, Bishal and Goyal, Pawan, **A Study on Prompt-based Few-Shot Learning Methods for Belief State Tracking in Task-oriented Dialog Systems**, 2022 [[Paper]](https://www.semanticscholar.org/reader/21e46f11898748778a31b5b2fe2f60128eb66ba1)


- Kumar, Harsh and Musabirov, Ilya and Shi, Jiakai and Lauzon, Adele and Choy, Kwan Kiu and Gross, Ofek and Kulzhabayeva, Dana and Williams, Joseph Jay, **Exploring The Design of Prompts For Applying GPT-3 based Chatbots: A Mental Wellbeing Case Study on Mechanical Turk**, 2022 [[Paper]](http://arxiv.org/abs/2209.11344)

- Mitsuda, Koh and Higashinaka, Ryuichiro and Saito, Kuniko, **Combining Argumentation Structure and Language Model for Generating Natural Argumentative Dialogue**, 2022 [[Paper]](https://aclanthology.org/2022.aacl-short.9)

- Valvoda, Josef and Fang, Yimai and Vandyke, David, **Prompting for a conversation: How to control a dialog model?**, 2022 [[Paper]](http://arxiv.org/abs/2209.11068)

- He, Keqing and Wang, Jingang and Sun, Chaobo and Wu, Wei, **Unified Knowledge Prompt Pre-training for Customer Service Dialogues**, 2022 [[Paper]](https://dl.acm.org/doi/10.1145/3511808.3557718)

- Reed, Lena and Li, Cecilia and Ramirez, Angela and Wu, Liren and Walker, Marilyn, **Jurassic is (almost) All You Need: Few-Shot Meaning-to-Text Generation for Open-Domain Dialogue**, 2021 [[Paper]](http://arxiv.org/abs/2110.08094)

- Liu, Jiachang and Shen, Dinghan and Zhang, Yizhe and Dolan, Bill and Carin, Lawrence and Chen, Weizhu, **What Makes Good In-Context Examples for GPT-3**, 2021 [[Paper]](http://arxiv.org/abs/2101.06804)

- Madotto, Andrea and Lin, Zhaojiang and Winata, Genta Indra and Fung, Pascale, **Few-Shot Bot: Prompt-Based Learning for Dialogue Systems**, 2021 [[Paper]](http://arxiv.org/abs/2110.08118)
 
- Prodan, George P and Pelican, Elena, **Prompt scoring system for dialogue summarization using GPT-3**, 2021 [[Paper]](https://www.techrxiv.org/ndownloader/files/30833896/1)

## Information Seeking
### Extra Knowledge

- Peng, Baolin and Galley, Michel and He, Pengcheng and Cheng, Hao and Xie, Yujia and Hu, Yu and Huang, Qiuyuan and Liden, Lars and Yu, Zhou and Chen, Weizhu and Gao, Jianfeng, **Check Your Facts and Try Again: Improving Large Language Models with External Knowledge and Automated Feedback**, 2023 [[Paper]](http://arxiv.org/abs/2302.12813)

- Khattab, Omar and Santhanam, Keshav and Li, Xiang Lisa and Hall, David and Liang, Percy and Potts, Christopher and Zaharia, Matei, **Demonstrate-Search-Predict: Composing retrieval and language models for knowledge-intensive NLP**, 2023 [[Paper]](http://arxiv.org/abs/2212.14024)


- Zhou, Shuyan and Alon, Uri and Xu, Frank F. and Wang, Zhiruo and Jiang, Zhengbao and Neubig, Graham, **DocPrompting: Generating Code by Retrieving the Docs**, 2023 [[Paper]](https://arxiv.org/abs/2207.05987)

- Sun, Zhiqing and Wang, Xuezhi and Tay, Yi and Yang, Yiming and Zhou, Denny, **Recitation-Augmented Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2210.01296)

- Yu, Wenhao and Iter, Dan and Wang, Shuohang and Xu, Yichong and Ju, Mingxuan and Sanyal, Soumya and Zhu, Chenguang and Zeng, Michael and Jiang, Meng, **Generate rather than Retrieve: Large Language Models are Strong Context Generators**, 2023 [[Paper]](http://arxiv.org/abs/2209.10063)

- Cohen, Roi and Geva, Mor and Berant, Jonathan and Globerson, Amir, **Crawling the Internal Knowledge-Base of Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2301.12810)

- Zamani, Hamed and Trippas, Johanne R. and Dalton, Jeff and Radlinski, Filip, **Conversational Information Seeking**, 2023 [[Paper]](http://arxiv.org/abs/2201.08808)

- Guo, Zhixin and Yan, Minyxuan and Qi, Jiexing and Zhou, Jianping and He, Ziwei and Lin, Zhouhan and Zheng, Guanjie and Wang, Xinbing, **Few-Shot Table-to-Text Generation with Prompt Planning and Knowledge Memorization**, 2023 [[Paper]](http://arxiv.org/abs/2302.04415)


- BehnamGhader, Parishad and Miret, Santiago and Reddy, Siva, **Can Retriever-Augmented Language Models Reason? The Blame Game Between the Retriever and the Language Model**, 2022 [[Paper]](http://arxiv.org/abs/2212.09146)

- Borgeaud, Sebastian and Mensch, Arthur and Hoffmann, Jordan et al., **Improving language models by retrieving from trillions of tokens**, 2022 [[Paper]](http://arxiv.org/abs/2112.04426)

- Shaier, Sagi and Hunter, Lawrence and Kann, Katharina, **Mind the Knowledge Gap: A Survey of Knowledge-enhanced Dialogue Systems**, 2022 [[Paper]](http://arxiv.org/abs/2212.09252)

- Majumder, Bodhisattwa Prasad and Jhamtani, Harsh and Berg-Kirkpatrick, Taylor and McAuley, Julian, **Achieving Conversational Goals with Unsupervised Post-hoc Knowledge Injection**, 2022 [[Paper]](http://arxiv.org/abs/2203.11399)

- Pereira, Jayr and Fidalgo, Robson and Lotufo, Roberto and Nogueira, Rodrigo, **Visconde: Multi-document QA with GPT-3 and Neural Reranking**, 2022 [[Paper]](https://arxiv.org/abs/2212.09656)

- Izacard, Gautier and Lewis, Patrick and Lomeli, Maria and Hosseini, Lucas et al., **Atlas: Few-shot Learning with Retrieval Augmented Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2208.03299)

- Trivedi, Harsh and Balasubramanian, Niranjan and Khot, Tushar and Sabharwal, Ashish, **Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions**, 2022 [[Paper]](http://arxiv.org/abs/2212.10509)


- Izacard, Gautier and Lewis, Patrick and Lomeli, Maria and Hosseini, Lucas and Petroni, Fabio and Schick, Timo and Dwivedi-Yu, Jane and Joulin, Armand and Riedel, Sebastian and Grave, Edouard, **DocPrompting: Generating Code by Retrieving the Docs**, 2022 [[Paper]](http://arxiv.org/abs/2207.05987)

- AlKhamissi, Badr and Li, Millicent and Celikyilmaz, Asli and Diab, Mona and Ghazvininejad, Marjan, **A Review on Language Models as Knowledge Bases**, 2022 [[Paper]](http://arxiv.org/abs/2204.06031)

- Dong, Qingxiu and Dai, Damai and Song, Yifan and Xu, Jingjing and Sui, Zhifang and Li, Lei, **Calibrating Factual Knowledge in Pretrained Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2210.03329)

- Santos, Cicero Nogueira dos and Dong, Zhe and Cer, Daniel and Nham, John and Shakeri, Siamak and Ni, Jianmo and Sung, Yun-hsuan, **Knowledge Prompts: Injecting World Knowledge into Language Models through Soft Prompts**, 2022 [[Paper]](http://arxiv.org/abs/2210.04726)

- He, Hangfeng and Zhang, Hongming and Roth, Dan, **Rethinking with Retrieval: Faithful Large Language Model Inference**, 2022 [[Paper]](http://arxiv.org/abs/2301.00303)

- Shuster, Kurt and Komeili, Mojtaba and Adolphs, Leonard and Roller, Stephen and Szlam, Arthur and Weston, Jason, **Language Models that Seek for Knowledge: Modular Search \& Generation for Dialogue and Prompt Completion**, 2022 [[Paper]](http://arxiv.org/abs/2203.13224)

- Xue, Qiang and Takiguchi, Tetsuya and Ariki, Yasuo, **Building a Knowledge-Based Dialogue System with Text Infilling**, 2022 [[Paper]](https://aclanthology.org/2022.sigdial-1.25)

- Lewis, Patrick and Perez, Ethan and Piktus, Aleksandra and Petroni, Fabio and Karpukhin, Vladimir and Goyal, Naman and Küttler, Heinrich and Lewis, Mike and Yih, Wen-tau and Rocktäschel, Tim and Riedel, Sebastian and Kiela, Douwe, **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**, 2021 [[Paper]](http://arxiv.org/abs/2005.11401)

- Adolphs, Leonard and Shuster, Kurt and Urbanek, Jack and Szlam, Arthur and Weston, Jason, **Reason first, then respond: Modular Generation for Knowledge-infused Dialogue**, 2021 [[Paper]](http://arxiv.org/abs/2111.05204)

- Shuster, Kurt and Poff, Spencer and Chen, Moya and Kiela, Douwe and Weston, Jason, **Retrieval Augmentation Reduces Hallucination in Conversation**, 2021 [[Paper]](https://aclanthology.org/2021.findings-emnlp.320)

- Xueliang Zhao, Wei Wu, Can Xu, Chongyang Tao, Dongyan Zhao, Rui Yan, **Knowledge-Grounded Dialogue Generation with Pre-trained Language Models.**, 2020 [[Paper]](https://arxiv.org/abs/2010.08824)


### Extra Modality
- Wu, Chenfei and Yin, Shengming and Qi, Weizhen and Wang, Xiaodong and Tang, Zecheng and Duan, Nan, **Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models**, 2023 [[Paper]](https://arxiv.org/abs/2303.04671)

- Camposampiero, Giacomo and Houmard, Loic and Estermann, Benjamin and Mathys, Joël and Wattenhofer, Roger, **Visual Abstraction and Reasoning through Language**, 2023 [[Paper]](http://arxiv.org/abs/2303.04091)

- Shao, Zhenwei and Yu, Zhou and Wang, Meng and Yu, Jun, **Prompting Large Language Models with Answer Heuristics for Knowledge-based Visual Question Answering**, 2023 [[Paper]](http://arxiv.org/abs/2303.01903)

- West, Colin G., **AI and the FCI: Can ChatGPT Project an Understanding of Introductory Physics?**, 2023 [[Paper]](http://arxiv.org/abs/2303.01067)

- Huang, Shaohan and Dong, Li and Wang, Wenhui and Hao, Yaru and Singhal, Saksham and Ma, Shuming and Lv, Tengchao and Cui, Lei and Mohammed, Owais Khan and Liu, Qiang and Aggarwal, Kriti and Chi, Zewen and Bjorck, Johan and Chaudhary, Vishrav and Som, Subhojit and Song, Xia and Wei, Furu, **Language Is Not All You Need: Aligning Perception with Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.14045)

- Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven, **BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2301.12597)
 
- Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline et al., **Flamingo: a Visual Language Model for Few-Shot Learning**, 2022 [[Paper]](http://arxiv.org/abs/2204.14198)

- Su, Yixuan and Lan, Tian and Liu, Yahui and Liu, Fangyu and Yogatama, Dani and Wang, Yan and Kong, Lingpeng and Collier, Nigel, **Language Models Can See: Plugging Visual Controls in Text Generation**, 2022 [[Paper]](http://arxiv.org/abs/2205.02655)

- Yang, Zhengyuan and Gan, Zhe and Wang, Jianfeng and Hu, Xiaowei and Lu, Yumao and Liu, Zicheng and Wang, Lijuan, **An Empirical Study of GPT-3 for Few-Shot Knowledge-Based VQA**, 2022 [[Paper]](http://arxiv.org/abs/2109.05014)

- Tsimpoukelli, Maria and Menick, Jacob and Cabi, Serkan and Eslami, S. M. Ali and Vinyals, Oriol and Hill, Felix, **Multimodal Few-Shot Learning with Frozen Language Models**, 2021 [[Paper]](http://arxiv.org/abs/2106.13884)

### Web Search
- Ram, Ori and Levine, Yoav and Dalmedigos, Itay and Muhlgay, Dor and Shashua, Amnon and Leyton-Brown, Kevin and Shoham, Yoav, **In-Context Retrieval-Augmented Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.00083)

- Khattab, Omar and Santhanam, Keshav and Li, Xiang Lisa and Hall, David and Liang, Percy and Potts, Christopher and Zaharia, Matei, **Demonstrate-Search-Predict: Composing retrieval and language models for knowledge-intensive NLP**, 2023 [[Paper]](http://arxiv.org/abs/2212.14024)

- Shi, Weijia and Min, Sewon and Yasunaga, Michihiro and Seo, Minjoon and James, Rich and Lewis, Mike and Zettlemoyer, Luke and Yih, Wen-tau, **REPLUG: Retrieval-Augmented Black-Box Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2301.12652)

- Lazaridou, Angeliki and Gribovskaya, Elena and Stokowiec, Wojciech and Grigorev, Nikolai, **Internet-augmented language models through few-shot prompting for open-domain question answering**, 2022 [[Paper]](http://arxiv.org/abs/2203.05115) 

- Piktus, Aleksandra and Petroni, Fabio and Karpukhin, Vladimir et al., **The Web Is Your Oyster - Knowledge-Intensive NLP against a Very Large Web Corpus**, 2022 [[Paper]](http://arxiv.org/abs/2112.09924)

- Nakano, Reiichiro and Hilton, Jacob and Balaji, Suchir et al., **WebGPT: Browser-assisted question-answering with human feedback**, 2021 [[Paper]](https://arxiv.org/abs/2112.09332)

- Komeili, Mojtaba and Shuster, Kurt and Weston, Jason, **Internet-Augmented Dialogue Generation**, 2021 [[Paper]](http://arxiv.org/abs/2107.07566)


## Action and Plan
- Luo, Zhezheng and Mao, Jiayuan and Wu, Jiajun and Lozano-Pérez, Tomás and Tenenbaum, Joshua B. and Kaelbling, Leslie Pack, **Learning Rational Subgoals from Demonstrations and Instructions**, 2023 [[Paper]](http://arxiv.org/abs/2303.05487)

- Zhang, Shun and Chen, Zhenfang and Shen, Yikang and Ding, Mingyu and Tenenbaum, Joshua B. and Gan, Chuang, **Planning with Large Language Models for Code Generation**, 2023 [[Paper]](http://arxiv.org/abs/2303.05510)

- Dorbala, Vishnu Sashank and Mullen Jr., James F. and Manocha, Dinesh, **Can an Embodied Agent Find Your "Cat-shaped Mug"? LLM-Based Zero-Shot Object Navigation**, 2023 [[Paper]](http://arxiv.org/abs/2303.03480)

- Haldar, Siddhant and Pari, Jyothish and Rai, Anant and Pinto, Lerrel, **Teach a Robot to FISH: Versatile Imitation from One Minute of Demonstrations**, 2023 [[Paper]](http://arxiv.org/abs/2303.01497)

- Huang, Wenlong and Xia, Fei and Shah, Dhruv and Driess, Danny and Zeng, Andy and Lu, Yao and Florence, Pete and Mordatch, Igor and Levine, Sergey and Hausman, Karol and Ichter, Brian, **Grounded Decoding: Guiding Text Generation with Grounded Models for Robot Control**, 2023 [[Paper]](http://arxiv.org/abs/2303.00855)

- Capitanelli, Alessio and Mastrogiovanni, Fulvio, **A Framework to Generate Neurosymbolic PDDL-compliant Planners**, 2023 [[Paper]](http://arxiv.org/abs/2303.00438)


- Karamcheti, Siddharth and Nair, Suraj and Chen, Annie S. and Kollar, Thomas and Finn, Chelsea and Sadigh, Dorsa and Liang, Percy, **Language-Driven Representation Learning for Robotics**, 2023 [[Paper]](http://arxiv.org/abs/2302.12766) 

- Vemprala, Sai and Bonatti, Rogerio and Bucker, Arthur and Kapoor, Ashish, **ChatGPT for Robotics: Design Principles and Model Abilities**, 2023 [[Paper]](https://www.microsoft.com/en-us/research/uploads/prod/2023/02/ChatGPT___Robotics.pdf)

- Carta, Thomas and Romac, Clément and Wolf, Thomas and Lamprier, Sylvain and Sigaud, Olivier and Oudeyer, Pierre-Yves, **Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning**, 2023 [[Paper]](http://arxiv.org/abs/2302.02662)

- Dasgupta, Ishita and Kaeser-Chen, Christine and Marino, Kenneth and Ahuja, Arun and Babayan, Sheila and Hill, Felix and Fergus, Rob, **Collaborating with language models for embodied reasoning**, 2023 [[Paper]](http://arxiv.org/abs/2302.00763)

- Mialon, Grégoire and Dessì, Roberto and Lomeli, Maria and Nalmpantis, Christoforos and Pasunuru, Ram and Raileanu, Roberta and Rozière, Baptiste and Schick, Timo and Dwivedi-Yu, Jane and Celikyilmaz, Asli and Grave, Edouard and LeCun, Yann 
and Scialom, Thomas, **Augmented Language Models: a Survey**, 2023 [[Paper]](http://arxiv.org/abs/2302.07842)

- Schick, Timo and Dwivedi-Yu, Jane and Dessì, Roberto and Raileanu, Roberta and Lomeli, Maria and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas, **Toolformer: Language Models Can Teach Themselves to Use Tools**, 2023 [[Paper]](http://arxiv.org/abs/2302.04761)

- Xie, Yaqi and Yu, Chen and Zhu, Tongyao and Bai, Jinbin and Gong, Ze and Soh, Harold, **Translating Natural Language to Planning Goals with Large-Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.05128)

- Du, Yuqing and Watkins, Olivia and Wang, Zihan and Colas, Cédric and Darrell, Trevor and Abbeel, Pieter and Gupta, Abhishek and Andreas, Jacob, **Guiding Pretraining in Reinforcement Learning with Large Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.06692)

- Wang, Zihao and Cai, Shaofei and Liu, Anji and Ma, Xiaojian and Liang, Yitao, **Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents**, 2023 [[Paper]](http://arxiv.org/abs/2302.01560)

- Li, Belinda Z. and Chen, William and Sharma, Pratyusha and Andreas, Jacob, **LaMPP: Language Models as Probabilistic Priors for Perception and Action**, 2023 [[Paper]](http://arxiv.org/abs/2302.02801)

- Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan, **ReAct: Synergizing Reasoning and Acting in Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2210.03629)
 
- Li, Shuang and Puig, Xavier and Paxton, Chris and Du, Yilun and Wang, Clinton and Fan, Linxi and Chen, Tao and Huang, De-An and Akyürek, Ekin and Anandkumar, Anima and Andreas, Jacob and Mordatch, Igor and Torralba, Antonio and Zhu, Yuke, **Pre-Trained Language Models for Interactive Decision-Making**, 2022 [[Paper]](http://arxiv.org/abs/2202.01771)

- Valmeekam, Karthik and Sreedharan, Sarath and Marquez, Matthew and Olmo, Alberto and Kambhampati, Subbarao, **On the Planning Abilities of Large Language Models (A Critical Investigation with a Proposed Benchmark)**, 2023 [[Paper]](http://arxiv.org/abs/2302.06706)

- Sharma, Pratyusha and Torralba, Antonio and Andreas, Jacob, **Skill Induction and Planning with Latent Language**, 2022 [[Paper]](http://arxiv.org/abs/2110.01517)

- Xu, Jing and Ung, Megan and Komeili, Mojtaba and Arora, Kushal and Boureau, Y.-Lan and Weston, Jason, **Learning New Skills after Deployment: Improving open-domain internet-driven dialogue with human feedback**, 2022 [[Paper]](http://arxiv.org/abs/2208.03270)

- Press, Ofir and Zhang, Muru and Min, Sewon and Schmidt, Ludwig and Smith, Noah A. and Lewis, Mike, **Measuring and Narrowing the Compositionality Gap in Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2210.03350)

- Liu, Ruibo and Wei, Jason and Gu, Shixiang Shane and Wu, Te-Yen and Vosoughi, Soroush and Cui, Claire and Zhou, Denny and Dai, Andrew M., **Mind's Eye: Grounded Language Model Reasoning through Simulation**, 2022 [[Paper]](http://arxiv.org/abs/2210.05359)

- Brohan, Anthony and Brown, Noah and Carbajal, et al., **RT-1: Robotics Transformer for Real-World Control at Scale**, 2022 [[Paper]](http://arxiv.org/abs/2212.06817)

- Huang, Wenlong and Xia, Fei and Xiao, Ted and Chan, Harris and Liang, Jacky and Florence, Pete and Zeng, Andy and Tompson, Jonathan and Mordatch, Igor and Chebotar, Yevgen and Sermanet, Pierre and Brown, Noah and Jackson, Tomas and Luu, Linda and Levine, Sergey and Hausman, Karol and Ichter, Brian, **Inner Monologue: Embodied Reasoning through Planning with Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2207.05608)

- Ahn, Michael and Brohan, Anthony and Brown, et al., **Do As I Can, Not As I Say: Grounding Language in Robotic Affordances**, 2022 [[Paper]](http://arxiv.org/abs/2204.01691)

- Shashank Kalakonda, Sai and Maheshwari, Shubh and Kiran Sarvadevabhatla, Ravi, **Action-GPT: Leveraging Large-scale Language Models for Improved and Generalized Zero Shot Action Generation**, 2022 [[Paper]](https://ui.adsabs.harvard.edu/abs/2022arXiv221115603S)

- Liang, Jacky and Huang, Wenlong and Xia, Fei and Xu, Peng and Hausman, Karol and Ichter, Brian and Florence, Pete and Zeng, Andy, **Code as Policies: Language Model Programs for Embodied Control**, 2022 [[Paper]](http://arxiv.org/abs/2209.07753)

- Zelikman, Eric and Wu, Yuhuai and Mu, Jesse and Goodman, Noah D., **STaR: Bootstrapping Reasoning With Reasoning**, 2022 [[Paper]](http://arxiv.org/abs/2203.14465)

- Nakamura, Taiki and Kawano, Seiya and Yuguchi, Akishige and Kawanishi, Yasutomo and Yoshino, Koichiro, **What Should the System Do Next?: Operative Action Captioning for Estimating System Actions**, 2022 [[Paper]](http://arxiv.org/abs/2210.02735)

- Colas, Cédric and Karch, Tristan and Moulin-Frier, Clément and Oudeyer, Pierre-Yves, **Language and Culture Internalisation for Human-Like Autotelic AI**, 2022 [[Paper]](http://arxiv.org/abs/2206.01134)

- Valmeekam, Karthik and Olmo, Alberto and Sreedharan, Sarath and Kambhampati, Subbarao, **Large Language Models Still Can't Plan (A Benchmark for LLMs on Planning and Reasoning about Change)**, 2022 [[Paper]](http://arxiv.org/abs/2206.10498)
- Song, Chan Hee and Wu, Jiaman and Washington, Clayton and Sadler, Brian M. and Chao, Wei-Lun and Su, Yu, **LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2212.04088)

- Singh, Ishika and Blukis, Valts and Mousavian, Arsalan and Goyal, Ankit and Xu, Danfei and Tremblay, Jonathan and Fox, Dieter and Thomason, Jesse and Garg, Animesh, **ProgPrompt: Generating Situated Robot Task Plans using Large Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2209.11302)

- Huang, Wenlong and Abbeel, Pieter and Pathak, Deepak and Mordatch, Igor, **Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents**, 2022 [[Paper]](http://arxiv.org/abs/2201.07207)

## Reasoning
- Yang, Sherry and Nachum, Ofir and Du, Yilun and Wei, Jason and Abbeel, Pieter and Schuurmans, Dale, **Foundation Models for Decision Making: Problems, Methods, and Opportunities**, 2023 [[Paper]](http://arxiv.org/abs/2303.04129)

- Yu, Hangyeol and Jeong, Myeongho and Shin, Jamin and Moon, Hyeongdon and Park, Juneyoung and Choi, Seungtaek, **Towards Zero-Shot Functional Compositionality of Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2303.03103)

- Reppert, Justin and Rachbach, Ben and George, Charlie and Stebbing, Luke and Byun, Jungwon and Appleton, Maggie and Stuhlmüller, Andreas, **Iterated Decomposition: Improving Science Q\&A by Supervising Reasoning Processes**, 2023 [[Paper]](http://arxiv.org/abs/2301.01751)

- Blair-Stanek, Andrew and Holzenberger, Nils and Van Durme, Benjamin, **Can GPT-3 Perform Statutory Reasoning?**, 2023 [[Paper]](http://arxiv.org/abs/2302.06100)

- Huang, Jiaxin and Gu, Shixiang Shane and Hou, Le and Wu, Yuexin and Wang, Xuezhi and Yu, Hongkun and Han, Jiawei, **Large Language Models Can Self-improve**, 2023 [[Paper]](https://openreview.net/forum?id=NiEtU7blzN)

- Gurrapu, Sai and Kulkarni, Ajay and Huang, Lifu and Lourentzou, Ismini and Freeman, Laura and Batarseh, Feras A., **Rationalization for Explainable NLP: A Survey**, 2023 [[Paper]](http://arxiv.org/abs/2301.08912)

- Gao, Luyu and Madaan, Aman and Zhou, Shuyan and Alon, Uri and Liu, Pengfei and Yang, Yiming and Callan, Jamie and Neubig, Graham, **PAL: Program-aided Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2211.10435)

- Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu, **On the Advance of Making Language Models Better Reasoners**, 2022 [[Paper]](http://arxiv.org/abs/2206.02336)

- Kazemi, Seyed Mehran and Kim, Najoung and Bhatia, Deepti and Xu, Xin and Ramachandran, Deepak, **LAMBADA: Backward Chaining for Automated Reasoning in Natural Language**, 2022 [[Paper]](http://arxiv.org/abs/2212.13894)
 
- Marasović, Ana and Beltagy, Iz and Downey, Doug and Peters, Matthew E., **Few-Shot Self-Rationalization with Natural Language Prompts**, 2022 [[Paper]](http://arxiv.org/abs/2111.08284)

- Chen, Yanda and Zhong, Ruiqi and Zha, Sheng and Karypis, George and He, He, **Meta-learning via Language Model In-context Tuning**, 2022 [[Paper]](https://aclanthology.org/2022.acl-long.53)

- Lampinen, Andrew K. and Dasgupta, Ishita and Chan, Stephanie C. Y. and Matthewson, Kory and Tessler, Michael Henry and Creswell, Antonia and McClelland, James L. and Wang, Jane X. and Hill, Felix, **Can language models learn from explanations in context?**, 2022 [[Paper]](http://arxiv.org/abs/2204.02329)

- Wei, Jason and Wang, Xuezhi and Schuurmans, Dale and Bosma, Maarten and Ichter, Brian and Xia, Fei and Chi, Ed and Le, Quoc and Zhou, Denny, **Chain of Thought Prompting Elicits Reasoning in Large Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2201.11903)

- Ye, Xi and Durrett, Greg, **The Unreliability of Explanations in Few-shot Prompting for Textual Reasoning**, 2022 [[Paper]](http://arxiv.org/abs/2205.03401)

- Jackson, Ilya and Saenz, Maria Jesus, **From Natural Language to Simulations: Applying GPT-3 Codex to Automate Simulation Modeling of Logistics Systems**, 2022 [[Paper]](http://arxiv.org/abs/2202.12107)

- Lu, Pan and Qiu, Liang and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Rajpurohit, Tanmay and Clark, Peter and Kalyan, Ashwin, **Dynamic Prompt Learning via Policy Gradient for Semi-structured Mathematical Reasoning**, 2022 [[Paper]](http://arxiv.org/abs/2209.14610)

- Wu, Tongshuang and Jiang, Ellen and Donsbach, Aaron and Gray, Jeff and Molina, Alejandra and Terry, Michael and Cai, Carrie J., **PromptChainer: Chaining Large Language Model Prompts through Visual Programming**, 2022 [[Paper]](http://arxiv.org/abs/2203.06566)

- Creswell, Antonia and Shanahan, Murray, **Faithful Reasoning Using Large Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2208.14271)

- Taylor, Ross and Kardas, Marcin and Cucurull, Guillem and Scialom, Thomas and Hartshorn, Anthony and Saravia, Elvis and Poulton, Andrew and Kerkez, Viktor and Stojnic, Robert, **Galactica: A Large Language Model for Science**, 2022 [[Paper]](http://arxiv.org/abs/2211.09085)

- Wu, Tongshuang and Terry, Michael and Cai, Carrie J., **AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts**, 2022 [[Paper]](http://arxiv.org/abs/2110.01691)

- Wang, Boshi and Deng, Xiang and Sun, Huan, **Iteratively Prompt Pre-trained Language Models for Chain of Thought**, 2022 [[Paper]](http://arxiv.org/abs/2203.08383)

- Khot, Tushar and Trivedi, Harsh and Finlayson, Matthew and Fu, Yao and Richardson, Kyle and Clark, Peter and Sabharwal, Ashish, **Decomposed Prompting: A Modular Approach for Solving Complex Tasks**, 2022 [[Paper]](http://arxiv.org/abs/2210.02406)

- Dua, Dheeru and Gupta, Shivanshu and Singh, Sameer and Gardner, Matt, **Successive Prompting for Decomposing Complex Questions**, 2022 [[Paper]](http://arxiv.org/abs/2212.04092)

- Zelikman, Eric and Wu, Yuhuai and Mu, Jesse and Goodman, Noah D., **STaR: Bootstrapping Reasoning With Reasoning**, 2022 [[Paper]](http://arxiv.org/abs/2203.14465)

- Yang, Jingfeng and Jiang, Haoming and Yin, Qingyu and Zhang, Danqing and Yin, Bing and Yang, Diyi, **SeqZero: Few-shot Compositional Semantic Parsing with Sequential Prompts and Zero-shot Models**, 2022 [[Paper]](https://arxiv.org/abs/2205.07381v1)

- Qiao, Shuofei and Ou, Yixin and Zhang, Ningyu and Chen, Xiang and Yao, Yunzhi and Deng, Shumin and Tan, Chuanqi and Huang, Fei and Chen, Huajun, **Reasoning with Language Model Prompting: A Survey**, 2022 [[Paper]](https://arxiv.org/abs/2212.09597v1)

- Huang, Jie and Chang, Kevin Chen-Chuan, **Towards Reasoning in Large Language Models: A Survey**, 2022 [[Paper]](https://arxiv.org/abs/2212.10403v1)

- Press, Ofir and Zhang, Muru and Min, Sewon and Schmidt, Ludwig and Smith, Noah A. and Lewis, Mike, **Measuring and Narrowing the Compositionality Gap in Language Models**, 2022 [[Paper]](https://arxiv.org/abs/2210.03350v1)

- Creswell, Antonia and Shanahan, Murray and Higgins, Irina, **Selection-Inference: Exploiting Large Language Models for Interpretable Logical Reasoning**, 2022 [[Paper]](https://arxiv.org/abs/2205.09712v1)

- Karpas, Ehud and Abend, Omri and Belinkov, Yonatan and Lenz, Barak et al., **MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning**, 2022 [[Paper]](http://arxiv.org/abs/2205.00445)

- Nye, Maxwell and Andreassen, Anders Johan and Gur-Ari, Guy and Michalewski, Henryk et al., **Show 
Your Work: Scratchpads for Intermediate Computation with Language Models**, 2021 [[Paper]](http://arxiv.org/abs/2112.00114)


## Long-text Generation
- Faltings, Felix and Galley, Michel and Peng, Baolin and Brantley, Kianté and Cai, Weixin and Zhang, Yizhe and Gao, Jianfeng and Dolan, Bill, **Interactive Text Generation**, 2023 [[Paper]](http://arxiv.org/abs/2303.00908)

- Xie, Zhuohan and Cohn, Trevor and Lau, Jey Han, **Can Very Large Pretrained Language Models Learn Storytelling With A Few Examples?**, 2023 [[Paper]](http://arxiv.org/abs/2301.09790)

- Peng, Xiangyu and Cui, Christopher and Zhou, Wei and Jia, Renee and Riedl, Mark, **Story Shaping: Teaching Agents Human-like Behavior with Stories**, 2023 [[Paper]](http://arxiv.org/abs/2301.10107)

- Toplyn, Joe, **Witscript: A System for Generating Improvised Jokes in a Conversation**, 2023 [[Paper]](http://arxiv.org/abs/2302.02008)

- Dan Klein, Nanyun Peng, Yuandong Tian Kevin Yang, **Re3: Generating Longer Stories With Recursive Reprompting and Revision**, 2022 [[Paper]](https://arxiv.org/abs/2210.06774)
 
- Li, Junyi and Tang, Tianyi and Zhao, Wayne Xin and Nie, Jian-Yun and Wen, Ji-Rong, **Pretrained Language Models for Text Generation: A Survey**, 2022 [[Paper]](http://arxiv.org/abs/2201.05273)

- Yang, Kevin and Klein, Dan and Peng, Nanyun and Tian, Yuandong, **DOC: Improving Long Story Coherence With Detailed Outline Control**, 2022 [[Paper]](http://arxiv.org/abs/2212.10077)

- Taylor, Ross and Kardas, Marcin and Cucurull, Guillem and Scialom, Thomas and Hartshorn, Anthony and Saravia, Elvis and Poulton, Andrew and Kerkez, Viktor and Stojnic, Robert, **Galactica: A Large Language Model for Science**, 2022 [[Paper]](http://arxiv.org/abs/2211.09085)

- Chang, Haw-Shiuan and Yuan, Jiaming and Iyyer, Mohit and McCallum, Andrew, **Changing the Mind of Transformers for Topically-Controllable Language Generation**, 2021 [[Paper]](http://arxiv.org/abs/2103.15335)

- Li, Junyi and Tang, Tianyi and Zhao, Wayne Xin and Wen, Ji-Rong, **Pretrained Language Models for Text Generation: A Survey**, 2021 [[Paper]](http://arxiv.org/abs/2105.10311)

- Garbacea, Cristina and Mei, Qiaozhu, **Neural Language Generation: Formulation, Methods, and Evaluation**, 2020 [[Paper]](http://arxiv.org/abs/2007.15780)

- Dathathri, Sumanth and Madotto, Andrea and Lan, Janice and Hung, Jane and Frank, Eric and Molino, Piero and Yosinski, Jason and Liu, Rosanne, **Plug and Play Language Models: A Simple Approach to Controlled Text Generation**, 2020 [[Paper]](http://arxiv.org/abs/1912.02164)



## Analysis and Boundary 
- Wang, Jiaan and Liang, Yunlong and Meng, Fandong and Shi, Haoxiang and Li, Zhixu and Xu, Jinan and Qu, Jianfeng and Zhou, Jie, **Is ChatGPT a Good NLG Evaluator? A Preliminary Study**, 2023 [[Paper]](http://arxiv.org/abs/2303.04048)

- Amin, Mostafa M. and Cambria, Erik and Schuller, Björn W., **Will Affective Computing Emerge from Foundation Models and General AI? A First Evaluation on ChatGPT**, 2023 [[Paper]](http://arxiv.org/abs/2303.03186)

- Zhong, Ruiqi and Zhang, Peter and Li, Steve and Ahn, Jinwoo and Klein, Dan and Steinhardt, Jacob, **Goal Driven Discovery of Distributional Differences via Language Descriptions**, 2023 [[Paper]](http://arxiv.org/abs/2302.14233)

- Wang, Yizhong and Mishra, Swaroop and Alipoormolabashi, Pegah and Kordi, Yeganeh et al., **Super-NaturalInstructions: Generalization via Declarative Instructions on 1600+ NLP Tasks**, 2022 [[Paper]](http://arxiv.org/abs/2204.07705)

- Chen, Xuanting and Ye, Junjie and Peng, Minlong and Zhou, Jie and Gui, Tao and Zhang, Qi and Huang, Xuanjing, **How Robust is GPT-3.5 to Predecessors? A Comprehensive Study on Language Understanding Tasks**, 2023 [[Paper]](https://arxiv.org/abs/2303.00293)

- Leiter, Christoph and Zhang, Ran and Chen, Yanran and Belouadi, Jonas and Larionov, Daniil and Fresen, Vivian and Eger, Steffen, **ChatGPT: A Meta-Analysis after 2.5 Months**, 2023 [[Paper]](http://arxiv.org/abs/2302.13795)

- Bommarito, Jillian and Bommarito, Michael and Katz, Daniel Martin and Katz, Jessica, **GPT as Knowledge Worker: A Zero-Shot Evaluation of (AI)CPA Capabilities**, 2023 [[Paper]](http://arxiv.org/abs/2301.04408)

- Shahriar, Sakib and Hayawi, Kadhim, **Let's have a chat! A Conversation with ChatGPT: Technology, Applications, and Limitations**, 2023 [[Paper]](http://arxiv.org/abs/2302.13817)

- Bommarito, Jillian and Bommarito, Michael and Katz, Daniel Martin and Katz, Jessica, **GPT as Knowledge Worker: A Zero-Shot Evaluation of (AI)CPA Capabilities**, 2023 [[Paper]](http://arxiv.org/abs/2301.04408)

- Michelmann, Sebastian and Kumar, Manoj and Norman, Kenneth A. and Toneva, Mariya, **Large language models can segment narrative events similarly to humans**, 2023 [[Paper]](http://arxiv.org/abs/2301.10297)

- Shi, Freda and Chen, Xinyun and Misra, Kanishka and Scales, Nathan and Dohan, David and Chi, Ed and Schärli, Nathanael and Zhou, Denny, **Large Language Models Can Be Easily Distracted by Irrelevant Context**, 2023 [[Paper]](http://arxiv.org/abs/2302.00093)

- Carta, Thomas and Romac, Clément and Wolf, Thomas and Lamprier, Sylvain and Sigaud, Olivier and Oudeyer, Pierre-Yves, **Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning**, 2023 [[Paper]](http://arxiv.org/abs/2302.02662)

- Fu, Jinlan and Ng, See-Kiong and Jiang, Zhengbao and Liu, Pengfei, **GPTScore: Evaluate as You Desire**, 2023 [[Paper]](http://arxiv.org/abs/2302.04166)

- Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy, **Data Selection for Language Models via Importance Resampling**, 2023 [[Paper]](http://arxiv.org/abs/2302.03169)

- Jang, Joel and Kim, Seungone and Ye, Seonghyeon and Kim, Doyoung and Logeswaran, Lajanugen and Lee, Moontae and Lee, Kyungjae and Seo, Minjoon, **Exploring the Benefits of Training Expert Language Models over Instruction Tuning**, 2023 [[Paper]](http://arxiv.org/abs/2302.03202)

- Borji, Ali, **A Categorical Archive of ChatGPT Failures**, 2023 [[Paper]](http://arxiv.org/abs/2302.03494)

- Zhang, Tianjun and Liu, Fangchen and Wong, Justin and Abbeel, Pieter and Gonzalez, Joseph E., **The Wisdom of Hindsight Makes Language Models Better Instruction Followers**, 2023 [[Paper]](http://arxiv.org/abs/2302.05206)

- Ullman, Tomer, **Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks**, 2023 [[Paper]](http://arxiv.org/abs/2302.08399)

- Mökander, Jakob and Schuett, Jonas and Kirk, Hannah Rose and Floridi, Luciano, **Auditing large language models: a three-layered approach**, 2023 [[Paper]](http://arxiv.org/abs/2302.08500)

- Huang, Fan and Kwak, Haewoon and An, Jisun, **Is ChatGPT better than Human Annotators? Potential and Limitations of ChatGPT in Explaining Implicit Hate Speech**, 2023 [[Paper]](http://arxiv.org/abs/2302.07736)

- Kocoń, Jan and Cichecki, Igor and Kaszyca, et al., **ChatGPT: Jack of all trades, master of none**, 2023 [[Paper]](http://arxiv.org/abs/2302.10724)

- Wang, Jindong and Hu, Xixu and Hou, Wenxin and Chen, Hao and Zheng, Runkai and Wang, Yidong and Yang, Linyi and Huang, Haojun and Ye, Wei and Geng, Xiubo and Jiao, Binxin and Zhang, Yue and Xie, Xing, **On the Robustness of ChatGPT: An Adversarial and Out-of-distribution Perspective**, 2023 [[Paper]](http://arxiv.org/abs/2302.12095)

- Akyürek, Ekin and Schuurmans, Dale and Andreas, Jacob and Ma, Tengyu and Zhou, Denny, **What learning algorithm is in-context learning? Investigations with linear models**, 2022 [[Paper]](http://arxiv.org/abs/2211.15661)

- Dai, Damai and Sun, Yutao and Dong, Li and Hao, Yaru and Sui, Zhifang and Wei, Furu, **Why Can GPT Learn In-Context? Language Models Secretly Perform Gradient Descent as Meta-Optimizers**, 2022 [[Paper]](http://arxiv.org/abs/2212.10559)

- Yang, Sen and Zhang, Yunchen and Cui, Leyang and Zhang, Yue, **Do Prompts Solve NLP Tasks Using Natural Language?**, 2022 [[Paper]](http://arxiv.org/abs/2203.00902)

- Ross, Alexis and Peters, Matthew E. and Marasović, Ana, **Does Self-Rationalization Improve Robustness to Spurious Correlations?**, 2022 [[Paper]](http://arxiv.org/abs/2210.13575)

- Wei, Jason and Tay, Yi and Bommasani, et al., **Emergent Abilities of Large Language Models**, 2022 [[Paper]](http://arxiv.org/abs/2206.07682)

- Li, Jiaoda and Cotterell, Ryan and Sachan, Mrinmaya, **Probing via Prompting**, 2022 [[Paper]](http://arxiv.org/abs/2207.01736)

- Zhang, Renrui and Zeng, Ziyao and Guo, Ziyu, **Can Language Understand Depth?**, 2022 [[Paper]](http://arxiv.org/abs/2207.01077)

- Kann, Katharina and Ebrahimi, Abteen and Koh, Joewie and Dudy, Shiran and Roncone, Alessandro, **Open-domain Dialogue Generation: What We Can Do, Cannot Do, And Should Do Next**, 2022 [[Paper]](https://aclanthology.org/2022.nlp4convai-1.13)

- Kadavath, Saurav and Conerly, Tom and Askell, et al., **Language Models (Mostly) Know What They Know**, 2022 [[Paper]](http://arxiv.org/abs/2207.05221)

- Wei, Xiaokai and Wang, Shen and Zhang, Dejiao and Bhatia, Parminder and Arnold, Andrew, **Knowledge Enhanced Pretrained Language Models: A Compreshensive Survey**, 2021 [[Paper]](http://arxiv.org/abs/2110.08455)
 
- Liu, Pengfei and Yuan, Weizhe and Fu, Jinlan and Jiang, Zhengbao and Hayashi, Hiroaki and Neubig, Graham, **Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing**, 2021 [[Paper]](http://arxiv.org/abs/2107.13586)
 
- Webson, Albert and Pavlick, Ellie, **Do Prompt-Based Models Really Understand the Meaning of their Prompts?**, 2021 [[Paper]](http://arxiv.org/abs/2109.01247)
 
- Elazar, Yanai and Kassner, Nora and Ravfogel, Shauli and Ravichander, Abhilasha and Hovy, Eduard and Schütze, Hinrich and Goldberg, Yoav, **Measuring and Improving Consistency in Pretrained Language Models**, 2021 [[Paper]](http://arxiv.org/abs/2102.01017)
 
- Hase, Peter and Diab, Mona and Celikyilmaz, Asli and Li, Xian and Kozareva, Zornitsa and Stoyanov, Veselin and Bansal, Mohit and Iyer, Srinivasan, **Do Language Models Have Beliefs? Methods for Detecting, Updating, and Visualizing Model Beliefs**, 2021 [[Paper]](http://arxiv.org/abs/2111.13654)
 
- Da, Jeff and Bras, Ronan Le and Lu, Ximing and Choi, Yejin and Bosselut, Antoine, **Analyzing Commonsense Emergence in Few-shot Knowledge Models**, 2021 [[Paper]](http://arxiv.org/abs/2101.00297)

- Jiang, Zhengbao and Araki, Jun and Ding, Haibo and Neubig, Graham, **How Can We Know When Language Models Know? On the Calibration of Language Models for Question Answering**, 2021 [[Paper]](http://arxiv.org/abs/2012.00955)

- Le Scao, Teven and Rush, Alexander, **How many data points is a prompt worth?**, 2021 [[Paper]](https://aclanthology.org/2021.naacl-main.208)

- Jiang, Zhengbao and Xu, Frank F. and Araki, Jun and Neubig, Graham, **How Can We Know What Language Models Know?**, 2020 [[Paper]](http://arxiv.org/abs/1911.12543)
 
## Motivation
### Emotion
- Liu, Yiren and Kilicoglu, Halil, **Commonsense-Aware Prompting for Controllable Empathetic Dialogue Generation**, 2023 [[Paper]](http://arxiv.org/abs/2302.01441)

- Gao, Pan and Han, Donghong and Zhou, Rui and Zhang, Xuejiao and Wang, Zikun, **CAB: Empathetic Dialogue Generation with Cognition, Affection and Behavior**, 2023 [[Paper]](http://arxiv.org/abs/2302.01935)

- Qian, Yushan and Wang, Bo and Ma, Shangzhao and Bin, Wu and Zhang, Shuo and Zhao, Dongming and Huang, Kun and Hou, Yuexian, **Think Twice: A Human-like Two-stage Conversational Agent for Emotional Response Generation**, 2023 [[Paper]](http://arxiv.org/abs/2301.04907)

- Kasahara, Tomohito and Kawahara, Daisuke and Tung, Nguyen and Li, Shengzhe and Shinzato, Kenta and Sato, Toshinori, **Building a Personalized Dialogue System with Prompt-Tuning**, 2022 [[Paper]](http://arxiv.org/abs/2206.05399)

- Jiang, Chenglin and Zhang, Chunhong and Ji, Yang and Hu, Zheng and Zhan, Zhiqiang and Yang, Guanghua, **An affective chatbot with controlled specific emotion expression**, 2022 [[Paper]](https://link.springer.com/10.1007/s11432-020-3356-4)

- Cheng, Jiale and Sabour, Sahand and Sun, Hao and Chen, Zhuang and Huang, Minlie, **PAL: Persona-Augmented Emotional Support Conversation Generation**, 2022 [[Paper]](http://arxiv.org/abs/2212.09235)

- Li, Qintong and Li, Piji and Ren, Zhaochun and Ren, Pengjie and Chen, Zhumin, **Knowledge Bridging for Empathetic Dialogue Generation**, 2021 [[Paper]](http://arxiv.org/abs/2009.09708)

### Persona
- Rao, Haocong and Leung, Cyril and Miao, Chunyan, **Can ChatGPT Assess Human Personalities? A General Evaluation Framework**, 2023 [[Paper]](http://arxiv.org/abs/2303.01248)

- Ramirez, Angela and Alsalihy, Mamon and Aggarwal, Kartik and Li, Cecilia and Wu, Liren and Walker, Marilyn, **Controlling Personality Style in Dialogue with Zero-Shot Prompt-Based Learning**, 2023 [[Paper]](http://arxiv.org/abs/2302.03848)

- Lim, Jungwoo and Kang, Myunghoon and Hur, Yuna and Jung, Seungwon and Kim, Jinsung and Jang, Yoonna and Lee, Dongyub and Ji, Hyesung and Shin, Donghoon and Kim, Seungryong and Lim, Heuiseok, **You Truly Understand What I Need: Intellectual and Friendly Dialogue Agents grounding Knowledge and Persona**, 2023 [[Paper]](http://arxiv.org/abs/2301.02401)

- Chen, Ruijun and Wang, Jin and Yu, Liang-Chih and Zhang, Xuejie, **Learning to Memorize Entailment and Discourse Relations for Persona-Consistent Dialogues**, 2023 [[Paper]](http://arxiv.org/abs/2301.04871)

- Ross, Steven I. and Muller, Michael and Martinez, Fernando and Houde, Stephanie and Weisz, Justin D., **A Case Study in Engineering a Conversational Programming Assistant's Persona**, 2023 [[Paper]](http://arxiv.org/abs/2301.10016)    

- Kasahara, Tomohito and Kawahara, Daisuke and Tung, Nguyen and Li, Shengzhe and Shinzato, Kenta and Sato, Toshinori, **Building a Personalized Dialogue System with Prompt-Tuning**, 2022 [[Paper]](http://arxiv.org/abs/2206.05399)
    

- Matveev, Yuri and Makhnytkina, Olesia and Posokhov, Pavel and Matveev, Anton and Skrylnikov, Stepan, **Personalizing Hybrid-Based Dialogue Agents**, 2022 [[Paper]](https://www.mdpi.com/2227-7390/10/24/4657)

- Xu, Xinchao and Gou, Zhibin and Wu, Wenquan and Niu, Zheng-Yu and Wu, Hua and Wang, Haifeng and Wang, Shihang, **Long Time No See! Open-Domain Conversation with Long-Term Persona Memory**, 2022 [[Paper]](https://www.semanticscholar.org/reader/081edae651e709e448bdd8a1f1b5760c7c7e1f53)


- Liu, Yifan and Wei, Wei and Liu, Jiayi and Mao, Xianling and Fang, Rui and Chen, Dangyang, **Improving Personality Consistency in Conversation by Persona Extending**, 2022 [[Paper]](http://arxiv.org/abs/2208.10816)


- Natarajan, Bharatram and Nargund, Abhijit, **MRE : Multi Relationship Extractor for Persona based Empathetic Conversational Model**, 2021 [[Paper]](https://aclanthology.org/2021.icon-main.21)


- Peixiang Zhong, Chen Zhang, Hao Wang, Yong Liu, Chunyan Miao, **Towards Persona-Based Empathetic Conversational Models**, 2020 [[Paper]](https://arxiv.org/abs/2004.12316)

- Qian Liu, Yihong Chen, Bei Chen, Jian-Guang Lou, Zixuan Chen, Bin Zhou, Dongmei Zhang, **You Impress Me: Dialogue Generation via Mutual Persona Perception**, 2020 [[Paper]](https://arxiv.org/abs/2004.05388)

- Haoyu Song, Yan Wang, Wei-Nan Zhang, Xiaojiang Liu, Ting Liu, **Generate, Delete and Rewrite: A Three-Stage Framework for Improving Persona Consistency of Dialogue Generation**, 2020 [[Paper]]()



## Application
- Kargaran, Amir Hossein and Nikeghbal, Nafiseh and Heydarnoori, Abbas and Schütze, Hinrich, **MenuCraft: Interactive Menu System Design with Large Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2303.04496)

- Polak, Maciej P. and Morgan, Dane, **Extracting Accurate Materials Data from Research Papers with Conversational Language Models and Prompt Engineering -- Example of ChatGPT**, 2023 [[Paper]](http://arxiv.org/abs/2303.05352)

- Zhang, Dell and Schilder, Frank and Conrad, Jack G. and Makrehchi, Masoud and von Rickenbach, David and Moulinier, Isabelle, **Making a Computational Attorney**, 2023 [[Paper]](http://arxiv.org/abs/2303.05383)

- Imani, Shima and Du, Liang and Shrivastava, Harsh, **MathPrompter: Mathematical Reasoning using Large Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2303.05398)

- Dai, Haixing and Liu, Zhengliang and Liao, Wenxiong and Huang, Xiaoke and Wu, Zihao and Zhao, Lin and Liu, Wei and Liu, Ninghao and Li, Sheng and Zhu, Dajiang and Cai, Hongmin and Li, Quanzheng and Shen, Dinggang and Liu, Tianming and Li, Xiang, **ChatAug: Leveraging ChatGPT for Text Data Augmentation**, 2023 [[Paper]](http://arxiv.org/abs/2302.13007)

- Qin, Chengwei and Zhang, Aston and Zhang, Zhuosheng and Chen, Jiaao and Yasunaga, Michihiro and Yang, Diyi, **Is ChatGPT a General-Purpose Natural Language Processing Task Solver?**, 2023 [[Paper]](http://arxiv.org/abs/2302.06476)    

- Dai, Haixing and Liu, Zhengliang and Liao, Wenxiong and Huang, Xiaoke and Wu, Zihao and Zhao, Lin and Liu, Wei and Liu, Ninghao and Li, Sheng and Zhu, Dajiang and Cai, Hongmin and Li, Quanzheng and Shen, Dinggang and Liu, Tianming and Li, Xiang, **ChatAug: Leveraging ChatGPT for Text Data Augmentation**, 2023 [[Paper]](http://arxiv.org/abs/2302.13007)

- Brocki, Lennart and Dyer, George C. and Gładka, Anna and Chung, Neo Christopher, **Deep Learning Mental Health Dialogue System**, 2023 [[Paper]](https://arxiv.org/abs/2301.09412)

- Ott, Simon and Hebenstreit, Konstantin and Liévin, Valentin and Hother, Christoffer Egeberg and Moradi, Milad and Mayrhauser, Maximilian and Praas, Robert and Winther, Ole and Samwald, Matthias, **ThoughtSource: A central hub for large language model reasoning data**, 2023 [[Paper]](http://arxiv.org/abs/2301.11596)

- Nguyen, Ha-Thanh, **A Brief Report on LawGPT 1.0: A Virtual Legal Assistant Based on GPT-3**, 2023 [[Paper]](http://arxiv.org/abs/2302.05729)

- Argyle, Lisa P. and Busby, Ethan and Gubler, Joshua and Bail, Chris and Howe, Thomas and Rytting, Christopher and Wingate, David, **AI Chat Assistants can Improve Conversations about Divisive Topics**, 2023 [[Paper]](http://arxiv.org/abs/2302.07268)

- Kocaballi, A. Baki, **Conversational AI-Powered Design: ChatGPT as Designer, User, and Product**, 2023 [[Paper]](http://arxiv.org/abs/2302.07406)

- Shanahan, Murray, **Talking About Large Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2212.03551)

- Shibata, Hisaichi and Miki, Soichiro and Nakamura, Yuta, **Playing the Werewolf game with artificial intelligence for language understanding**, 2023 [[Paper]](http://arxiv.org/abs/2302.10646)

- Megahed, Fadel M. and Chen, Ying-Ju and Ferris, Joshua A. and Knoth, Sven and Jones-Farmer, L. Allison, **How Generative AI models such as ChatGPT can be (Mis)Used in SPC Practice, Education, and Research? An Exploratory Study**, 2023 [[Paper]](http://arxiv.org/abs/2302.10916)

- Lehman, Eric and Hernandez, Evan and Mahajan, Diwakar and Wulff, Jonas and Smith, Micah J. and Ziegler, Zachary and Nadler, Daniel and Szolovits, Peter and Johnson, Alistair and Alsentzer, Emily, **Do We Still Need Clinical Language Models?**, 2023 [[Paper]](http://arxiv.org/abs/2302.08091)

- Zeng, Donghuo and Wu, Jianming and Wang, Yanan and Matsumoto, Kazunori and Hattori, Gen and Ikeda, Kazushi, **Topic-switch adapted Japanese Dialogue System based on PLATO-2**, 2023 [[Paper]](http://arxiv.org/abs/2302.11280)

- Feng, Yutao and Qiang, Jipeng and Li, Yun and Yuan, Yunhao and Zhu, Yi, **Sentence Simplification via Large Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.11957)


- Noever, David and McKee, Forrest, **Chatbots as Problem Solvers: Playing Twenty Questions with Role Reversals**, 2022 [[Paper]](http://arxiv.org/abs/2301.01743)

- Haolan Zhan, Yufei Wang, Tao Feng, Yuncheng Hua, Suraj Sharma, Zhuang Li, Lizhen Qu, Gholamreza Haffari, **Let's Negotiate! A Survey of Negotiation Dialogue Systems**, 2022 [[Paper]](https://arxiv.org/abs/2212.09072)



## Safety
- Greshake, Kai and Abdelnabi, Sahar and Mishra, Shailesh and Endres, Christoph and Holz, Thorsten and Fritz, Mario, **More than you've asked for: A Comprehensive Analysis of Novel Prompt Injection Threats to Application-Integrated Large Language Models**, 2023 [[Paper]](http://arxiv.org/abs/2302.12173)
 
- Kang, Daniel and Li, Xuechen and Stoica, Ion and Guestrin, Carlos and Zaharia, Matei and Hashimoto, Tatsunori, **Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks**, 2023 [[Paper]](http://arxiv.org/abs/2302.05733)

## Related Project
- **Prompt API** 
    - https://github.com/hwchase17/langchain
    - https://promptlayer.com/
    - https://github.com/promptslab/Promptify


- **Prompt Reference**
    - https://learnprompting.org/
    - https://gpt3demo.com/
    - https://sharegpt.com/
    - https://github.com/dair-ai/Prompt-Engineering-Guide
    - https://promptbase.com/
