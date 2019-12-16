# Pincelate

By [Allison Parrish](https://www.decontextualize.com/)

Pincelate is a machine learning model for spelling English words and sounding
them out, plus a Python module that makes it super simple to do fun and useful
things with the model.

A quick example:

    >>> from pincelate import Pincelate
    >>> pin = Pincelate()
    >>> pin.soundout("pincelate")
    ['P', 'IH1', 'N', 'S', 'AH0', 'L', 'EY1', 'T']
    >>> pin.spell(["HH", "EH", "L", "OW"])
    'hello'

Please see [the documentation](https://pincelate.readthedocs.io/en/latest/) for
more information!


## My Notes

### Install

create conda env
```
conda create -n pincelate python=3.7
conda activate pincelate
```

training is faster with tensorflow_gpu (50 seconds vs 77 seconds per epoch). change tensorflow to tensorflow_gpu in requirements.txt

install required packages
```
pip install -r requirements.txt
pip install -e .
pip install jupyterlab numpy scipy
conda install -c conda-forge ipywidgets
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

modify pincelate/seq2seq.py to save topology and weights

```
python train.py --model-prefix pincelate/models/orth-phon-enc256-dec256 --src orth --target phon
python train.py --model-prefix pincelate/models/phon-orth-enc256-dec256 --src phon --target orth
```


