# 🔥Awesome Augmented Language Model [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
Large Language models (LLMs) have become a new foundational platform. However, LLMs still struggle to implement many complex tasks that require human-level understanding. This repo collect research papers about leveraging the capabilities of language models, which can be a good reference for building upper-layer applications.


## Contents
- [Model](#model)
    - [Foundation Model](#foundation-model)
    - [Instruction Model](#instruction-model)
    - [Alignment and RLHF](#alignment-and-rlhf)
    - [Dialogue Model](#dialogue-model)
- [Prompt](#prompt)
    - [Hard](#hard)
    - [Soft](#soft)
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

- Scheurer, Jérémy and Campos, Jon Ander and Chan, Jun Shern and Chen, Angelica and Cho, Kyunghyun and Perez, Ethan, **Training Language Models with Language Feedback**, 2022 [[Paper]](https://arxiv.org/abs/2204.14146v4)


### Alignment and RLHF
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
### Hard 
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

- Deng, Mingkai and Wang, Jianyu and Hsieh, Cheng-Ping and Wang, Yihan and Guo, Han and Shu, Tianmin and Song, Meng and Xing, Eric P. and Hu, Zhiting, **RLPrompt: Optimizing Discrete Text Prompts With Reinforcement Learning**, 2022 [[Paper]](http://arxiv.org/abs/2205.12548)

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

- Perez, Ethan and Kiela, Douwe and Cho, Kyunghyun, **True Few-Shot Learning with Language Models**, 2021 [[Paper]](http://arxiv.org/abs/2105.11447)

- Gao, Tianyu and Fisch, Adam and Chen, Danqi, **Making Pre-trained Language Models Better Few-shot Learners**, 2021 [[Paper]](http://arxiv.org/abs/2012.15723)

- Han, Xu and Zhao, Weilin and Ding, Ning and Liu, Zhiyuan and Sun, Maosong, **PTR: Prompt Tuning with Rules for Text Classification**, 2021 [[Paper]](http://arxiv.org/abs/2105.11259)

- Taylor Shin, Yasaman Razeghi, Robert L. Logan, Eric Wallace, Sameer Singh, **AutoPrompt: Eliciting Knowledge from Language Models with Automatically Generated Prompts**, 2020 [[Paper]](https://arxiv.org/abs/2010.15980)

- Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Chi, Quoc Le, Denny Zhou, **Chain of Thought Prompting Elicits Reasoning in Large Language Models**, 2020 [[Paper]](https://arxiv.org/abs/2201.11903)


### Soft
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

- 
