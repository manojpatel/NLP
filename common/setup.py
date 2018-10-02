import os

def download_github_code(path):
  filename = path.rsplit("/")[-1]
  os.system("wget https://raw.githubusercontent.com/manojpatel/NLP/master/{} -O {}".format(path, filename))
