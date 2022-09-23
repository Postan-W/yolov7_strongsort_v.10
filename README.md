**Author：wmingzhu**

## 1.算法

在划定区域里对目标进行计时，超过阈值则标记为滞留。一个目标离开划定区域后，再次回到区域内，滞留时间从0开始计算。

当然，划定区域可以是整个画面。

**注意：**目标在画面中消失，再次检测到时id会改变，即认为是新目标

**滞留时间的计算方式:**

从目标进入划定区域开始计时。

- 如果是连续帧，则每检测到目标，则目标停留时间增加一帧(根据fps得到)，出现断检即某一帧没有检测到的话，再次检测到该目标的时候时间从0开始计(但实际上连续n帧没检测到才视为目标离开了区域，再次检测到的话时间从0计)
- 如果是跳帧处理，则结合跳帧情况计时

**具体地**，为每个视频设定一个dict用来记录每个id的停留时间，id即作为dict的key。逻辑是：每一帧检测到的id都判断是否已经在dict中存在，若存在则在原有时间上增加一次，若不存在则dict以该id为key，值为0，并将该id放到临时的集合A中。在一帧检测到的所有id判断完后，dict的key组成的集合B与集合A作差集B-A，差集中的key全部删除，因为在该帧中没检测到，以后再检测到的话时间就以上面的逻辑从0开始计。

待处理的问题是，一个人某一帧或几帧被遮挡了，对应id的时间就被置为0了。应该容许几帧的漏检而不将其时间置为0。不过连续漏检的帧数不应该太多，不然的话本跟踪系统将其id重置了。

## 2.Python库

| absl-py                 | 1.2.0           |      |
| ----------------------- | --------------- | ---- |
| beautifulsoup4          | 4.11.1          |      |
| ca-certificates         | 2022.07.19      |      |
| cachetools              | 5.2.0           |      |
| certifi                 | 2022.6.15       |      |
| charset-normalizer      | 2.1.1           |      |
| colorama                | 0.4.5           |      |
| cycler                  | 0.11.0          |      |
| cython                  | 0.29.32         |      |
| easydict                | 1.9             |      |
| filelock                | 3.8.0           |      |
| flake8                  | 5.0.4           |      |
| fonttools               | 4.37.1          |      |
| future                  | 0.18.2          |      |
| gdown                   | 4.5.1           |      |
| google-auth             | 2.11.0          |      |
| google-auth-oauthlib    | 0.4.6           |      |
| grpcio                  | 1.48.1          |      |
| h5py                    | 3.7.0           |      |
| idna                    | 3.4             |      |
| imageio                 | 2.21.3          |      |
| importlib-metadata      | 4.12.0          |      |
| isort                   | 4.3.21          |      |
| kiwisolver              | 1.4.4           |      |
| markdown                | 3.4.1           |      |
| markupsafe              | 2.1.1           |      |
| matplotlib              | 3.5.3           |      |
| mccabe                  | 0.7.0           |      |
| numpy                   | 1.23.3          |      |
| oauthlib                | 3.2.1           |      |
| opencv-python           | 4.6.0.66        |      |
| openssl                 | 1.1.1q          |      |
| packaging               | 21.3            |      |
| pandas                  | 1.4.4           |      |
| pillow                  | 9.2.0           |      |
| pip                     | 22.1.2          |      |
| plotting                | 0.0.7           |      |
| protobuf                | 3.19.5          |      |
| pyasn1                  | 0.4.8           |      |
| pyasn1-modules          | 0.2.8           |      |
| pycodestyle             | 2.9.1           |      |
| pyflakes                | 2.5.0           |      |
| pyparsing               | 3.0.9           |      |
| pysocks                 | 1.7.1           |      |
| python                  | 3.8.13          |      |
| python-dateutil         | 2.8.2           |      |
| pytz                    | 2022.2.1        |      |
| pyyaml                  | 6.0             |      |
| requests                | 2.28.1          |      |
| requests-oauthlib       | 1.3.1           |      |
| rsa                     | 4.9             |      |
| scipy                   | 1.9.1           |      |
| seaborn                 | 0.12.0          |      |
| setuptools              | 63.4.1          |      |
| six                     | 1.16.0          |      |
| soupsieve               | 2.3.2.post1     |      |
| sqlite                  | 3.39.2          |      |
| tb-nightly              | 2.11.0a20220913 |      |
| tensorboard-data-server | 0.6.1           |      |
| tensorboard-plugin-wit  | 1.8.1           |      |
| torch                   | 1.12.1+cu116    |      |
| torchaudio              | 0.12.1+cu116    |      |
| torchreid               | 0.1.1           |      |
| torchvision             | 0.13.1+cu116    |      |
| tqdm                    | 4.64.1          |      |
| typing-extensions       | 4.3.0           |      |
| urllib3                 | 1.26.12         |      |
| vc                      | 14.2            |      |
| vs2015_runtime          | 14.27.29016     |      |
| werkzeug                | 2.2.2           |      |
| wheel                   | 0.37.1          |      |
| wincertstore            | 0.2             |      |
| yacs                    | 0.1.8           |      |
| yapf                    | 0.32.0          |      |
| zipp                    | 3.8.1           |      |