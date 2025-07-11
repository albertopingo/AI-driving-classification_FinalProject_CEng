# AI Driving Classification

## Project Overview
This project investigates the use of Artificial Intelligence (AI) and Deep Learning (DL) techniques to analyze and classify different driving behaviors using sensor data collected from mobile devices. The study focuses on Recurrent Neural Networks (RNN), particularly Long Short-Term Memory (LSTM) architectures, to develop a system capable of classifying driving behaviors such as acceleration, braking, cornering, and navigating roundabouts.

### Motivation
The motivation for this project is to enhance road safety by analyzing driving behaviors in real-time using the sensors available in smartphones. The goal is to create an accessible and effective solution for detecting and classifying various driving styles, thereby contributing to accident prevention and promoting responsible driving.

### Authors
- Alberto Pingo ([@albertopingo](https://github.com/albertopingo))
- João Castro ([@jcastroo](https://github.com/jcastroo))


# Methodology
The project is approached from two perspectives:

First Approach: Analyzes data from a complete trip by segmenting sensor data (accelerometer, gyroscope) to classify driving patterns over an entire journey. Architectures such as Stacked LSTM, Bidirectional LSTM, and Convolutional LSTM were applied.

Second Approach: Focuses on specific driving scenarios like acceleration, braking, and cornering, with pre-classified driving styles as "Slow," "Normal," and "Aggressive." This approach allows the development of models that can classify diverse behavior patterns in different driving situations.

### Key Technologies
Python: The primary programming language used for model development.

TensorFlow & Keras: Libraries used for building and training the neural network models.

Pandas, NumPy, Matplotlib, Seaborn: For data manipulation, analysis, and visualization.

### Key Directories
- datasets/: Contains the datasets used for training and testing the models.
- code/: Contains Jupyter notebooks and models for both approaches.
  - first-approach/: Code for analyzing a complete trip using various LSTM architectures.
  - second-approach/: Code for specific driving scenarios classified into "Slow," "Normal," and "Aggressive."
- extras/, others/, publications/: Additional resources, references, and publications related to the project.

## Acknowledgments
We would like to express our gratitude to the following individuals and groups:
- Professors Sílvio Priem Mendes, Anabela Moreira Bernardino, and Paulo Jorge Gonçalves Loureiro for their guidance, support, and availability throughout the development of this project.
- Students who developed the Vehicle Tracking Application, which was instrumental in obtaining the datasets for this project. Your work provided the necessary tools for our data collection and analysis efforts.
- All the professors who accompanied us throughout our course, whose knowledge was fundamental to the completion of this project as well as our academic and personal growth.

## License
The source code and datasets located in the `code/`, `extras/`, `others/`, `FINAL_SUBMISSION/`, and datasets in `datasets/` directories are licensed under the [MIT License](LICENSE.md).  
All documentation, academic content, and presentation materials — including reports, papers, and slides — found in the `publications/`, `extras/` and `others/` and `FINAL_SUBMISSION/` directories are licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](LICENSE-CC-BY-4.0.md). [![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)


