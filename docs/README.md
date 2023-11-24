---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: https://github.com/cepdnaclk/e17-4yp-Deep-Learning-for-Side-Channel-Attacks
title: Investigating Machine Learning-based Attacks on Random Frequency Tuning-based Countermeasures
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Investigating Machine Learning-based Attacks on Random Frequency Tuning-based Countermeasures

#### Team

- E17038, Chandrasekara C.M.A, [e17038@eng.pdn.ac.lk](mailto:e17038@eng.pdn.ac.lk)
- E17101, Gunathilaka S.P.A.U, [e17101@eng.pdn.ac.lk](mailto:e17101@eng.pdn.ac.lk)
- E17292, Rilwan M M M , [e17292@eng.pdn.ac.lk](mailto:e17292@eng.pdn.ac.lk)

#### Supervisors

- Name, [email](mailto:name@eng.pdn.ac.lk)
- Name, [email](mailto:name@eng.pdn.ac.lk)

#### Table of content

1. [Abstract](#abstract)
2. [Related works](#related-works)
3. [Methodology](#methodology)
4. [Experiment Setup and Implementation](#experiment-setup-and-implementation)
5. [Results and Analysis](#results-and-analysis)
6. [Conclusion](#conclusion)
7. [Publications](#publications)
8. [Links](#links)

---

<!-- 
DELETE THIS SAMPLE before publishing to GitHub Pages !!!
This is a sample image, to show how to add images to your page. To learn more options, please refer [this](https://projects.ce.pdn.ac.lk/docs/faq/how-to-add-an-image/)

![Sample Image](./images/sample.png) 
-->


## Abstract
Side-channel attacks (SCAs) pose a significant threat to the security of cryptographic systems. These attacks exploit unintended information leakage through side channels such as power consumption, timing variations, or electromagnetic radiation. Rather than directly breaking the algorithm, SCAs aim to extract sensitive information like secret keys by analyzing the physical implementations of cryptographic devices.

In recent years, deep learning (DL) techniques, including Recurrent Neural Networks (RNNs), Long Short-Term Memory (LSTM), Generative Adversarial Networks (GANs), Reinforcement Learning (RL), Deep Neural Networks (DNNs), and Convolutional Neural Networks (CNNs), have gained considerable attention and success across various fields. Each algorithm has its strengths and applications, with DNNs and CNNs often capturing most cases due to their capabilities in handling complex patterns and extracting meaningful features from high-dimensional data. Convolutional Neural Networks, in particular, have played a significant role in related research and publications.

![SCA](./images/SCA.png) 

Deep Learning-based SCA attacks leverage neural networks to learn complex relationships between observed side-channel leakage and underlying secret keys, even without knowledge of the algorithm used. By training DL models on large datasets of side-channel measurements or traces, these attacks enhance the efficiency and accuracy of information extraction, even in the presence of countermeasures. Although training DL models requires substantial labeled data, recent research has addressed issues related to data availability and cost.

The field of Deep Learning-based SCA attacks is rapidly evolving, with numerous research papers exploring various aspects. These include the design and architecture of DL models, the impact of different network configurations on attack performance, and the effectiveness of DL-based attacks against different cryptographic devices and countermeasures.

We are mainly targetting counter measure Runtime Frequency Tuning Countermeasure (RFTC). It is a random execution time countermeasure based on frequency randomization. In RFTC, the clock frequencies are chosen randomly from 3,702 distinct clock frequencies (arranged in 1024 X 3 groups) which are chosen carefully and fixed during design time. These selections are dobe at runtime to mitigate the vulnerabilities of power analysis attacks in FPGAs. to mitigate power analysis attack vulnerabilities of FPGAs. RFTC uses dynamic reconfiguration of clock managers of FPGAs (such as Xilinx Mixed-Mode Clock Manager - MMCM) to generate the desired clock frequencies within FPGA to run cryptographic circuits. No other countermeasure has been proved secure against Dynamic Time Warping based CPA attacks (DTW-CPA), Principal Component Analysis based CPA attacks (PCA-CPA) and Fast Fourier Transform based CPA attacks (FFT-CPA) except for RFTC. But, RFTC was not tested against deep learning based SCAs.


## Related works
#### Template Attack
Template attacks involve a pre-computation phase where the attacker gathers side-channel traces, known plaintexts, and secret keys. This phase includes statistical analysis on these traces. However, as the number of side-channel features increases, the data space's dimensionality grows, leading to sparse data in high-dimensional spaces. This sparsity makes accurate statistical modeling and pattern capture challenging. Analyzing data becomes computationally expensive and time-consuming due to the exponential increase in dimensions. Two prominent approaches in recent years are template attacks and machine learning-based attacks. Template attacks excel when few Points of Interest (POI) in leakage traces carry most information. Conversely, machine learning-based attacks become more favorable as useless samples in leakage traces increase.

#### Machine Learning Based Attack
As mentioned in the template attack, the dimensionality issue is discussed as a ”curse of dimensionality” in publications. Dimension reduction techniques like PCA (Principal Component Analysis) and LDA (Linear Discriminant Analysis) can be used to overcome this problems. Research primarily revolves around machine learning attacks on PRESENT and AES in channel analysis. Classical machine learning techniques like Random Forest, Support Vector Machines, Naive Bayes, and multilayer perceptrons have been extensively explored and valued for their effectiveness across domains. For instance, Random Forest uses decision tree ensembles for predictions, while Naive Bayes, based on Bayes' theorem, is commonly used for text classification and spam filtering. The emerging field of deep learning sees a focus on Deep Neural Networks (DNNs) and Convolutional Neural Networks (CNNs) in most papers.

#### Random Frequency Tuning-based Countermeasures - RFTC
RFTC utilizes the flexibility of clock managers in Field-Programmable Gate Arrays (FPGAs) like the Xilinx Mixed-Mode Clock Manager (MMCM). By dynamically adjusting the operating frequency, RFTC implements the Advanced Encryption Standard (AES) block cipher algorithm using randomly chosen clock frequencies from a vast set. This method aims to reduce vulnerabilities to power analysis attacks.

![RFTC](./images/rftc.png)

The effectiveness of this clock randomization approach is evaluated through Correlation Power Analysis (CPA) attacks conducted on collected power traces. Various preprocessing techniques such as Dynamic Time Warping (DTW), Principal Component Analysis (PCA), and Fast Fourier Transform (FFT) are employed on the power traces to assess the removal of patterns resulting from random execution


## Methodology

## Experiment Setup and Implementation

## Results and Analysis

## Conclusion

## Publications
[//]: # "Note: Uncomment each once you uploaded the files to the repository"

<!-- 1. [Semester 7 report](./) -->
<!-- 2. [Semester 7 slides](./) -->
<!-- 3. [Semester 8 report](./) -->
<!-- 4. [Semester 8 slides](./) -->
<!-- 5. Author 1, Author 2 and Author 3 "Research paper title" (2021). [PDF](./). -->


## Links

[//]: # ( NOTE: EDIT THIS LINKS WITH YOUR REPO DETAILS )

- [Project Repository](https://github.com/cepdnaclk/e17-4yp-Deep-Learning-for-Side-Channel-Attacks)
- [Project Page](https://cepdnaclk.github.io/repository-name)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

[//]: # "Please refer this to learn more about Markdown syntax"
[//]: # "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"
