___
## Introduction
Side-channel attacks (SCAs) pose a significant threat to the security of cryptographic systems, as they exploit unintended information leakage through side channels such as power consumption, timing variations, or electromagnetic radiation. These attacks aim to extract sensitive information, like secret keys, by analyzing the physical implementations (as mentioned above) of a cryptographic device rather than directly breaking the algorithm.<br>
In recent years, deep learning (DL) techniques have gained considerable attention and success in various fields, and domains. When we speak about Deep Learning algorithms, we have Recurrent Neural Networks (RNNs), Long Short Term Memory (LSTM), Generative Adversarial Networks (GANs), Reinforcement Learning (RL), Deep neural networks (DNNs), Convolutional neural networks (CNNs) etc. Each algorithm has its own strengths and applications. The choice of algorithm depends on the nature of the problem or issue and the characteristics of the data. But most of the cases have been captured by Deep neural networks (DNNs) and
Convolutional Neural Networks (CNNs). Both algorithms have shown remarkable capabilities in capturing complex patterns and extracting meaningful features from high-dimensional data. When we went through related researches or publications Convolutional Neural Networks has played a major role.<br>
Deep Learning based SCA attacks leverage the power of neural networks to learn the complex relationship between the observed side-channel leakage and the underlying secret key even without knowing the algorithm. By training DL models on large amount of datasets of side-channel measurements or traces, these attacks can enhance the efficiency and accuracy of information extraction, even in the presence of countermeasures.To train DL models, it requires substantial amounts of labeled training data, which may be costly or time-consuming to obtain.But, currently its not a big issue since some research in this field have already addressed these issues.<br>
This field, Deep Learning based SCA attacks is rapidly evolving, and numerous research papers have been published.These papers explore various aspects, including the design and architecture of DL models, the impact of different network configurations on attack performance, and the effectiveness of DL-based attacks against different cryptographic devices and countermeasures.<br>
We expect to test RFTC against ASCAD, AISY and SCAAML frmework, improve MLP andd CNN models to attack RFTC and also attack other block cipher circuit (PRESENT, Simon, Speck etc ...) using the developed CNN or MLP models.
___

## Side Channel Attacks
A side-channel attack is a type of security vulnerability or attack that targets a computer system or cryptographic algorithm by exploiting unintended information leakage from various channels, such as power consumption, electromagnetic radiation, timing, or even sound. These attacks do not typically target the core algorithm or the encryption keys directly but instead focus on the observable side-effects of a system's operation. By analyzing these side-channel information leaks, attackers can potentially deduce sensitive information like encryption keys or data. Side-channel attacks can be a significant threat to the security of systems and are a critical consideration in the design and evaluation of secure hardware and software implementations.<br>
Eg;<br>
+ Power Analysis Attacks
+ Differential Power Analysis (DPA)
+ Simple Power Analysis (SPA)
+ Timing Attacks
+ Electromagnetic Radiation Analysis (e.g., Van Eck phreaking)
+ Acoustic Cryptanalysis

<p align="center">
  <img src="./docs/images/SCA.png" alt="Diagram showing SCA" width="500" height="250">
</p>

<hr>

## Power Analysis Attacks
A power analysis attack is a type of side-channel attack that targets cryptographic systems and devices by analyzing variations in power consumption during their operation. These attacks exploit the fact that the power consumption of a device, such as a smart card or a hardware security module, can reveal information about the internal operations and data being processed. By carefully monitoring and analyzing these power fluctuations, attackers can infer sensitive information, such as encryption keys or cryptographic algorithms used in a secure device. Power analysis attacks can be particularly concerning for systems that rely on cryptographic protection and have led to the development of countermeasures to mitigate their effectiveness, such as masking, shuffling, or other cryptographic techniques to obscure power signatures.
<p align="center">
  <img src="./docs/images/Power Analysis Attacks.png" alt="Diagram showing SCA">
</p>

<hr>

## Countermeasures
Countermeasures against power analysis attacks are security techniques and practices designed to protect cryptographic systems and devices from being vulnerable to power analysis. These countermeasures aim to make it more challenging for attackers to extract sensitive information by analyzing power consumption variations during the operation of the device. Here are some common countermeasures:
1. Randomization Techniques
    + These involve introducing randomness into the power consumption profile to make it harder for attackers to discern patterns. This can include adding random delays, randomizing the order of operations, or introducing noise into power traces.
2. Masking
    + Masking techniques involve splitting sensitive data or operations into multiple shares, and each share is processed separately. This helps obscure the power signature associated with the secret data. The final result is then derived by combining the shares.
3. Shuffling
    + Shuffling techniques reorder the execution of cryptographic operations to hide power consumption patterns. By varying the order of operations, attackers find it more difficult to correlate power fluctuations with specific actions.
4. Differential Power Analysis (DPA) Resistance
    + DPA-resistant designs are created with the goal of minimizing the correlation between power consumption and sensitive data. This may involve using algorithms and hardware implementations that are less susceptible to DPA attacks.
5. Constant-Time Implementations
    + In constant-time implementations, the execution time of cryptographic operations remains constant regardless of the input data. This makes it more difficult for attackers to deduce information from the timing of power consumption.
6. Secure Hardware
    + Using secure hardware components that are specifically designed to resist power analysis attacks, such as tamper-resistant modules and secure elements, can provide an additional layer of protection.

<hr>

## Runtime Frequency Tuning Countermeasure
Runtime Frequency Tuning Countermeasure (RFTC) is a random execution time countermeasure based on frequency randomization. In RFTC, the clock frequencies are chosen randomly from 3,702 distinct clock frequencies (arranged in 1024 X 3 groups) which are chosen carefully and fixed during design time. These selections are dobe at runtime to mitigate the vulnerabilities of power analysis attacks in FPGAs. to mitigate power analysis attack vulnerabilities of FPGAs. RFTC uses dynamic reconfiguration of clock managers of FPGAs (such as Xilinx Mixed-Mode Clock Manager - MMCM) to generate the desired clock frequencies within FPGA to run cryptographic circuits. No other countermeasure has been proved secure against Dynamic Time  Warping   based  CPA  attacks (DTW-CPA), Principal Component  Analysis   based  CPA  attacks (PCA-CPA) and Fast   Fourier   Transform based  CPA  attacks (FFT-CPA) except for RFTC. But, RFTC was not tested against deep learning based SCAs.


