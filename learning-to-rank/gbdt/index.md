---
# https://marp.app/
marp: true
---

# GBDT (Gradient Boosting Decision Trees)

---

## GBDT (Gradient Boosting Decision Trees)

- Decision Trees: 決定木
- Boosting: 複数のシンプルだが精度の低いモデルを協調させる
    - GBDTでは、ここでいう「シンプルだが精度の低いモデル」が決定木
    - 複数の小さいモデルを協調させて大きいモデルとして動かす
- Gradient: 目的関数の*勾配*
    - 本スライドの範囲では意識しない

---

## GBDTの全体像

それぞれの決定木は数値を出力。その総和をスコアとするモデル

<img src="image8.png" height="25%">
<img src="../../_common/plus-orange.drawio.png">
<img src="image9.png" height="25%">
<img src="../../_common/plus-orange.drawio.png">
<img src="image10.png" height="25%">
<img src="../../_common/plus-orange.drawio.png">
<img src="image11.png" height="25%">

---

## GBDTの特長

ランキング学習に限らず、いろいろなタスクで**スタンダードな**モデル
- 重要そうな特徴量を自然に選択してくれる
- できたモデルが人間にも理解しやすい

---

## 決定木

GBDTの部品。見ての通り、人間にも理解しやすい
- クエリに対して、ドキュメントごとに数値が出る（回帰）
- よく使われる特徴量、そうでない特徴量がある（特徴選択）

![](image8.png)

---

## 決定木の訓練

- 最初は、すべてのドキュメントに同じ数値を振る ![](image15.png)

<br />

- ひとつずつ分岐を作る。目的関数を最大化するように選ぶ
    - どこで・どの特徴量で・どの値で分岐し、数値はいくつにするか
![](image15.png)

---

## 決定木の訓練

- 最初は、すべてのドキュメントに同じ数値を振る ![](image15.png)

<br />

- ひとつずつ分岐を作る。目的関数を最大化するように選ぶ
    - どこで・どの特徴量で・どの値で分岐し、数値はいくつにするか
![](image14.png)

---

## 決定木の訓練

- 最初は、すべてのドキュメントに同じ数値を振る ![](image15.png)

<br />

- ひとつずつ分岐を作る。目的関数を最大化するように選ぶ
    - どこで・どの特徴量で・どの値で分岐し、数値はいくつにするか
![](image13.png)

---

## 決定木の訓練

- 最初は、すべてのドキュメントに同じ数値を振る ![](image15.png)

<br />

- ひとつずつ分岐を作る。目的関数を最大化するように選ぶ
    - どこで・どの特徴量で・どの値で分岐し、数値はいくつにするか
![](image12.png)

---

## ブースティング

決定木そのものも、ひとつずつ作る
- 過去の決定木を推論しても残った誤差を最小化するように作る

<img src="image8.png" height="25%">

---

## ブースティング

決定木そのものも、ひとつずつ作る
- 過去の決定木を推論しても残った誤差を最小化するように作る

<img src="image8.png" height="25%">
<img src="../../_common/plus-orange.drawio.png">
<img src="image9.png" height="25%">

---

## ブースティング

決定木そのものも、ひとつずつ作る
- 過去の決定木を推論しても残った誤差を最小化するように作る

<img src="image8.png" height="25%">
<img src="../../_common/plus-orange.drawio.png">
<img src="image9.png" height="25%">
<img src="../../_common/plus-orange.drawio.png">
<img src="image10.png" height="25%">

---

## ブースティング

決定木そのものも、ひとつずつ作る
- 過去の決定木を推論しても残った誤差を最小化するように作る

<img src="image8.png" height="25%">
<img src="../../_common/plus-orange.drawio.png">
<img src="image9.png" height="25%">
<img src="../../_common/plus-orange.drawio.png">
<img src="image10.png" height="25%">
<img src="../../_common/plus-orange.drawio.png">
<img src="image11.png" height="25%">
