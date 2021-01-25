# Model Training

We will leverage a Docker container to train our model.

```shell
cd model

./train.sh
```

This will build our Docker image, mount our current directory, in /tmp, train our model, and output the model artifact.

Once the process complete you will see the `iris_model.pkl` in the directory. You can now return to the project root.

```shell
cd ..
```


