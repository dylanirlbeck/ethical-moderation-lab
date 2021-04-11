# Ethical Moderation Lab

### HackIllinois 2021

## About

The Ethical Moderation Lab is a lab that is included within the Ethical Moderation HackIllinois project. The lab guides students through a scenario where they are in charge of creating a simple Content Moderation machine learning algorithm for a sports platform, Sport-It. The students will train their model using a given dataset and helper methods, and along the way, they will be challenged to think about many different ethical issues that arise when moderation content.
They will be questioned on topics such as:

- How would an inaccurate algorithm affect the company, and the users using their platform?
- What are the major downsides of using a Bag-Of-Words algorithm?
- Think about some examples that may be flagged in a BoW algo, when in actuality, they should be allowed on the platform.
- Who decides what constitutes an off-topic conversation?
- When should consider using human content moderators, and are the use of human reviewers ethical?

## Setup

Install required packages:

```
pip install -r ./requirements.txt
```

Build the notebook:

```
python3 ./build.py
```

## Data

We pull data from multiple different resources, which we have listed below:

### Training Data

<https://www.kaggle.com/socialmedianews/how-news-appears-on-social-media>

ESPN: (Taken 4/11/2021) http://www.espn.com/espn/latestnews

### Testing Data

ESPN: https://web.archive.org/web/20210213225238/http://www.espn.com/espn/latestnews
