# github-issues-analysis

github REST API を用いて，issues からバグの発見時間などの情報を含む csv ファイルを半自動的に取得します．

## 使い方

### `.env`の設定

アクセストークンを使用して，github API の使用制限を緩和医したい場合は，`.config/`内に，`.env`を作成し，`ACCESS_TOKEN`を指定してください．

#### 例

```Dotenv
ACCESS_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### レポジトリ情報の設定

`.config/`内に，`[repository name].env`を作成し，以下の変数を定義してください．

| 変数名      | 内容                              |
| ----------- | --------------------------------- |
| `OWNER`     | レポジトリ所有者のアカウント名    |
| `REPO`      | レポジトリの名前                  |
| `BUG_LABEL` | issues のバグを表すラベル名の指定 |

#### 例（https://github.com/facebook/react の場合）

```Dotenv
OWNER=facebook
REPO=react
BUG_LABEL=Type: bug
```

### 実行

`./main.py`内の`main()`の引数にレポジトリの config のパスを文字列で指定してください（例: `'./.config/react.env'`）．

### 結果

`output/`直下に`[OWNER]_[REPO]`の命名規則でディレクトリが作成されます．中には以下のファイルが含まれます．

| ファイル名             | 説明                                                                     |
| ---------------------- | ------------------------------------------------------------------------ |
| `response.json`        | レスポンスの json ファイル                                               |
| `time_series_data.csv` | `number`, `created_at`, `updated_at`, `closed_at`の列を含む csv ファイル |

レスポンス属性などについては，[GitHub / REST API endpoints for issues](https://docs.github.com/en/rest/issues/issues)を参照してください．
