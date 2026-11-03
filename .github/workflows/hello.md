name: Hello World!

# Push時起動
on: push

# 行うこと
jobs:
  hello:
    runs-on: ubuntu-latest
    steps: 
      - run: echo "Hello World!" # stepsのrun順に処理
      - run: echo "run2 Hey"
