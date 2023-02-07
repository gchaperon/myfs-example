# myfs-example
Repo to show an example of myfs + loading dvc tracked pytorch checkpoints.

This repo has two sister projects:
1. [myfs](https://github.com/gchaperon/myfs): the fsspec implementation
   (strongly based of off dvc's implementation).
2. [myfs-data](https://github.com/gchaperon/myfs-data): a repo that implements
   a simple pytorch(-lightning) model and stores a checkpoint in a ssh remote
   using dvc.

Part of the showcase is to install the necessary dependencies (both sister
projects), so please do check `requirements.txt` out.

## Disclaimer
This projects (and both sisters) requires python >= 3.8, since dvc support for
fsspec came only on version `2.27.0`, which is only available starting from
python 3.8

## User guide
The hard part is to set up a sister repo which uses dvc to track a model. In my
case, this job is done by [myfs-data](https://github.com/gchaperon/myfs-data).
If you want to run this example, you'll need to fork that repo, configure your
own remote, store a `myfs-data:models.CIFAR10Classifier` checkpoint using dvc
and finally modify the dependency in `requirements.txt` to point to that repo.

Now, that is a lot, so if you know me, you may send me youir public key so that I
can add it to the remote I have configured.


After that, the steps to run the example are super easy. First, install the
requirements:
```console
pip install -r requirements.txt
```
Make sure to use virtual environments, since this will install a lot of
(possibly quite heavy) dependencies.

Now run the example
```console
python main.py
```

That's it!


