# Model Training

We will leverage a Docker container to train our model.

```shell
cd model

./train.sh
```

This will build our Docker image, mount our current directory, in /tmp, train our model, and output the model artifact.


