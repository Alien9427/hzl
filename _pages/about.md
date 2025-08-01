---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hi! I am currently an associate professor at the <a href='https://nwpu-brainlab.gitee.io/index_en.html'> BRAIN LAB </a> of Northwestern Polytechnical University, Xi'an, China. In 2015, I obtained a Bachelor's degree from Beijing Normal University and a Ph.D. from the Chinese Academy of Sciences in 2020. I was a visiting Ph.D. student at the German Aerospace Center (DLR) from 2018 to 2019, under the supervision of Prof. Mihai Datcu. Since November 2020, I have been a faculty member at NPU and a postdoctoral researcher in collaboration with Prof. Junwei Han.

My research interests include Synthetic Aperture Radar (SAR) image interpretation, eXplainable Artificial Intelligence (XAI), and knowledge-guided data science. Particularly, we focus on cutting-edge artificial intelligence technologies combined with domain knowledge and physical models of SAR, targeting a wide range of applications including but not limit to SAR target detection and recognition, image classification and segmentation, content generation, etc. I have published more than 20 papers at the top journals and conferences with total <a href='https://scholar.google.com/citations?user=oqkhjW0AAAAJ&hl=zh-CN'><img src="https://img.shields.io/endpoint?logo=Google%20Scholar&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FAlien9427%2Fhzl%40google-scholar-stats%2Fgs_data_shieldsio.json&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

<!-- https://cdn.jsdelivr.net/gh/Alien9427/hzl@google-scholar-stats/gs_data_shieldsio.json -->

# 🔥 News
- *2025.08*: &nbsp; 📒 We organized a community contribution session in IGARSS-2025 with Prof. Mihai Datcu. "Physics Aware AI Models for SAR Data Generation and Understanding"
- *2025.07*: &nbsp; 🥳 One paper has been accepted by TCSVT. Congratuations to Long Liu!
- *2025.06*: &nbsp; 🥳 One paper has been accepted by ICCV2025 <a href='https://arxiv.org/abs/2503.02242'> $\mathbf{\Phi}$-GAN: Physics-Inspired GAN for Generating SAR Images Under Limited Data </a>! Congratuations to Xidan Zhang and Yihan Zhuang (Equal Contribution)! It is also our first paper accepted by Computer Vision Top Conferences!
- *2025.03*: &nbsp; 🧑🏻‍🎓 Congratulations to Haodong Yang on graduating with a Master's Degree and continuing his Ph.D journal at NPU. He is also my first Master student. Happy for him!
- *2024.09*: &nbsp; 🥳 One paper has been accepted by GRSM!
- *2024.07*: &nbsp; 📒 We organized a community contribution session in IGARSS-2024, “Explainable, Physics-aware, and Trustworthy AI for SAR: Towards Digital Twin Earth”.
- *2024.03*: &nbsp; 🧑🏻‍🎓 Congratulations to Zishi Wang and Chong Wu on graduating with a Master's degree. (Co-supervised with Prof. Junwei Han)
- *2023.07*: &nbsp; 📒 We organized a community contribution session in IGARSS-2023, “Physics Informed Artificial Intelligence for Synthetic Aperture Radar Applications”.
- *2023.03*: &nbsp; 👩🏻‍🎓 Congratulations to Ying Liu on graduating with a Master's degree. (Co-supervised with Prof. Junwei Han)
- *2022.07*: &nbsp; 📒 We organized an invited special session in IGARSS-2022, “Physics Aware Machine Learning for Synthetic Aperture Radar Applications”.
- *2021.07*: &nbsp; 📒 We organized an invited special session in IGARSS-2021, “DEEP Insight SAR”.
<!-- - *2021.06*: &nbsp; I . -->

# 📝 Selected Publications 

<!-- ## 🟣 Reviews -->

<!-- 论文：GRSM-XAI -->

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">GRSM-2023</div><img src='images/2023GRSM-XAI.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1"> -->


- ``ISPRS JPRS 2024`` [Physics Inspired Hybrid Attention for SAR Target Recognition](https://www.sciencedirect.com/science/article/abs/pii/S0924271623003374), **Zhongling Huang**, Chong Wu, Xiwen Yao*, Zhicheng Zhao, Xiankai Huang, Junwei Han. [Code&Data](https://github.com/XAI4SAR/PIHA)

-  ``Remote Sensing 2023`` [SAR-HUB: Pre-training, Fine-tuning, and Explaining](https://www.mdpi.com/2072-4292/15/23/5534), Haodong Yang, Xinyue Kang, Long Liu, Yujiang Liu, **Zhongling Huang***. [Code](https://github.com/XAI4SAR/SAR-HUB)

- ``IEEE TGRS 2023`` [Uncertainty Exploration: Toward Explainable SAR Target Detection](https://ieeexplore.ieee.org/document/10050159), **Zhongling Huang**, Ying Liu, Xiwen Yao*, Jun Ren, Junwei Han. [Code](https://github.com/XAI4SAR/XDet)

- ``REVIEW`` ``IEEE GRSM 2023`` [Explainable, Physics-aware, Trustworthy Artificial Intelligence: A Paradigm Shift for Synthetic Aperture Radar](https://ieeexplore.ieee.org/abstract/document/10035918/), Mihai Datcu, **Zhongling Huang***, Andrei Anghel, Juanping Zhao, Remus Cacoveanu

- ``ISPRS JPRS 2022`` [Physically explainable CNN for SAR image classification](https://www.sciencedirect.com/science/article/pii/S0924271622001472), **Zhongling Huang**, Xiwen Yao*, Ying Liu, Corneliu Octavian Dumitru, Mihai Datcu, Junwei Han. [Code/Data](https://github.com/Alien9427/XAI4SAR-PGIL)

- ``REVIEW`` ``JR 2022`` [Progress and perspective on physically explainable deep learning for synthetic aperture radar image interpretation](https://www.researchgate.net/publication/359424199_Progress_and_Perspective_on_Physically_Explainable_Deep_Learning_for_Synthetic_Aperture_Radar_Image_Interpretation), [中文版](https://radars.ac.cn/article/doi/10.12000/JR21165?viewType=HTML), **Zhongling Huang***, Xiwen Yao, Junwei Han

- ``IEEE TGRS 2020`` [HDEC-TFA: An unsupervised learning approach for discovering physical scattering properties of single-polarized SAR image](https://ieeexplore.ieee.org/abstract/document/9169671/), **Zhongling Huang***, Mihai Datcu*, Zongxu Pan, Xiaolan Qiu, Bin Lei

- ``ISPRS JPRS 2020`` [Deep SAR-Net: Learning objects from signals](https://www.sciencedirect.com/science/article/pii/S0924271620300162), **Zhongling Huang***,  Mihai Datcu*, Zongxu Pan, Bin Lei. [Code](https://github.com/Alien9427/DSN)

- ``IEEE TGRS 2020`` [What, where, and how to transfer in SAR target recognition based on deep CNNs](https://ieeexplore.ieee.org/abstract/document/8907833/), **Zhongling Huang**, Zongxu Pan*, Bin Lei

- ``IEEE GRSL 2020`` [Classification of large-scale high-resolution SAR images with deep transfer learning](https://ieeexplore.ieee.org/abstract/document/8966281/), **Zhongling Huang**, Corneliu Octavian Dumitru, Zongxu Pan, Bin Lei, Mihai Datcu

- ``Remote Sensing 2017`` [Transfer learning with deep convolutional neural network for SAR target classification with limited labeled data](https://ieeexplore.ieee.org/abstract/document/8966281/), **Zhongling Huang**, Zongxu Pan, Bin Lei*

<!-- [**Project**](https://scholar.google.de/citations?view_op=view_citation&hl=zh-CN&user=oqkhjW0AAAAJ&citation_for_view=oqkhjW0AAAAJ:8k81kl-MbHgC) <strong><span class='show_paper_citations' data='oqkhjW0AAAAJ:8k81kl-MbHgC'></span></strong>
- . 
</div>
</div> -->
<!-- 
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">GRSM-2023</div><img src='images/2023GRSM-XAI.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Explainable, Physics-aware, Trustworthy Artificial Intelligence: A Paradigm Shift for Synthetic Aperture Radar](https://www.sciencedirect.com/science/article/abs/pii/S0924271623003374)

**Zhongling Huang***, Xiwen Yao, Junwei Han

[**Project**](https://scholar.google.de/citations?view_op=view_citation&hl=zh-CN&user=oqkhjW0AAAAJ&citation_for_view=oqkhjW0AAAAJ:8k81kl-MbHgC) <strong><span class='show_paper_citations' data='oqkhjW0AAAAJ:8k81kl-MbHgC'></span></strong>
- . 
</div>
</div> -->

<!-- ## 🟣 Physically Explainable AI for SAR -->

<!-- 论文：PIHA -->

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISPRS-JPRS-2024</div><img src='images/2024ISPRS-PIHA.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Physics Inspired Hybrid Attention for SAR Target Recognition](https://www.sciencedirect.com/science/article/abs/pii/S0924271623003374)

**Zhongling Huang**, Chong Wu, Xiwen Yao, Zhicheng Zhao, Xiankai Huang, Junwei Han

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=DhtAFkwAAAAJ&citation_for_view=DhtAFkwAAAAJ:ALROH1vI_8AC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
</div>
</div> -->

<!-- 论文：BDD -->

<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">TGRS-2023</div><img src='images/2023TGRS-BDD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Uncertainty Exploration: Toward Explainable SAR Target Detection](https://ieeexplore.ieee.org/document/10050159)

**Zhongling Huang**, Ying Liu, Xiwen Yao, Jun Ren, Junwei Han

[**Code**](https://github.com/XAI4SAR/PIHA/) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
</div>
</div>

- [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->

<!-- # 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

# 📖 Educations
- *2018.10 - 2019.09*, Visiting Ph.D Student, German Aerospace Center. 
- *2015.09 - 2020.09*, Ph.D Student, University of Chinese Academy of Sciences. 
- *2011.09 - 2015.06*, Bechelor, Beijing Normal University.

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

<!-- # 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China. -->