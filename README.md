# CS3308 MACHINE LEARNING COURSE PROJECT

#### Abstract
We presents the findings and contributions of our CS3308 Machine Learning Course Project, which focuses on three main tasks. In Task 1, we develop 3 models for template-based single-step retrosynthesis prediction. In task 2 we tries two methods to predict the cost of a single molecule and multiple molecules. Finally, in Task 3, we employs 2 novel search algorithms to identify reactions that can synthesize target molecules from starting molecules.
- **Retrosynthesis Prediction:** In task 1, we implement two different models to accomplish the single-step retrosynthesis prediction task, including one **neural seq2seq model** and another **transformer-based pre-trained model: Chemformer**. Plenty of  experiments were conducted to test top-N accuracies. For the former method, the classification accuracy of different class types and the influence of different similarity metrics on accuracy are further explored in detail. We also compare the experimental results of the two models and deeply analyze the reason of the accuracy obtained by the second method.
- **Synthetic Cost Prediction:** In task 2, we implement two deep neural networks **Molecule Interaction MLP** and **Retrieve Based Chemprop** to predict the synthetic cost of the given molecule. We conduct experiments to compare the performance of these two methods. Besides, we try to answer the question raised in the project requirement. Our experiments shows that designing a suitable function to predict the cost of multiple molecules is better.
- **Search Algorithm Design:** In task 3, we employ two different search algorithms,**Retro*** and **EG-MCTS**, to identify reactions capable of synthesizing target molecules. To evaluate the performance of these algorithms, we conduct experiments and compare them against a baseline method, Greedy Breadth-First Search. Subsequently, we analyze the experimental results in detail to gain insights into the strengths and weaknesses of each algorithm.


#### Requirements
See the specific readme file.

#### Run
See the specific readme file.




#### Acknowledgments
Our code is inspired by

- [retrosim](https://github.com/connorcoley/retrosim)
- [MolBART - aka Chemformer](https://github.com/MolecularAI/Chemformer)
- [Chemprop](https://github.com/chemprop/chemprop)
- [Retrosynthetic Planning with EG-MCTS](https://github.com/jjljkjljk/EG-MCTS)
- [Retrosynthetic Planning with Retro*](https://github.com/binghong-ml/retro_star)