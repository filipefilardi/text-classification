# text-classification

This respository was created with the intention to provide easy-to-go data to researchers that want to try different machine learning techniques, such as text classification and text clustering, without having to worry about how the corpus is structured and initial preprocessing.

We know this is just the beginning to normalize your text documents, but we didn't want to apply more cleaning to the point you can't try different approaches. If you don't want to use the original dataset and get the pre-processed one structured in one dataframe, follow this [repository](https://www.kaggle.com/filipefilardi/20-newsgroup-preprocessed) or run [preprocessing.ipynb](notebooks/preprocesing.ipynb) in notebooks folder.

Also, in [this notebook](notebooks/models_evaluation.ipynb) we show a simple approach of how you can try a few models, test and evaluate it. 

## Dataset 

We are using the 20Newsgroup dataset, collected by Ken Lang and available [here](http://qwone.com/~jason/20Newsgroups/), containing 20 different classes and 18.828 documents.

### 20 newsgroups topics

Below you can see each newsgroup. Some of them are related (e.g. rec.sport.baseball and rec.sport.hockey), while others are unrelated (e.g alt.atheism and misc.forsale).

- alt.atheism
- comp.graphics
- comp.os.ms-windows.misc
- comp.sys.ibm.pc.hardware
- comp.sys.mac.hardware
- comp.windows.x
- misc.forsale
- rec.autos
- rec.motorcycles
- rec.sport.baseball
- rec.sport.hockey
- sci.crypt
- sci.electronics
- sci.med
- sci.space
- soc.religion.christian
- talk.politics.guns
- talk.politics.mideast
- talk.politics.misc
- talk.religion.misc

## License

This repository is licensed under [MIT License](LICENSE.md)
