# 概要
新しいプロジェクトを作るとき、テンプレート
Python用のパッケージ管理ツールの一つである「[Poetry](https://github.com/python-poetry/poetry)」を利用

以下のコマンドを実行して環境を構築する
* poetry config virtualenvs.in-project true
* poetry install

構成
* poetry (パッケージ管理ツール)
* flake8 (リンター)
* black (フォーマッター)
* pytest (テスト)
* taskipy (タスク定義)
* pyinstaller (実行ファイル化)
* .vscode/settings.jsonでファイル保存時自動フォーマット

## ディレクトリ構成
ディレクトリ構成は以下の通り。

```shell
┣ .vscode/           # vscode用の設定記述
┣ src/               # ソースコードはここに置く
┃   ┗ main.py        # エントリーポイント
┣ tests/             # テストコードはここに置く
┃   ┗ test_main.py
┣ .flake8            # flake8の設定
┣ .gitignore
┣ README.md
┣ poetry.lock
┗ pyproject.toml
```

## 機能
`poetry shell`で仮想環境に入ったあと、以下のコマンドが使える。
* `task run`: src/main.py を実行
* `task lint`: flake8 で lint
* `task build`: pyinstaller で exe化
* `task build-one`: pyinstaller で exe化 (＋ 1つのファイルにまとめる) 
* `task test`: pytest 実行

vscodeでファイル保存時、自動フォーマット。