import gchapero.models as models

checkpoint_name = "models/cifar10-classifier/checkpoints/epoch=4-step=3910.ckpt"
classifier = models.CIFAR10Classifier.load_from_checkpoint(
    f"gchapero://{checkpoint_name}"
)
print("Classifier loaded!")
print(classifier)
