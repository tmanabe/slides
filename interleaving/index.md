---
# https://marp.app/
marp: true
---

```mermaid
%%{init: {
  "flowchart": {
    "rankSpacing": 40,
    "nodeSpacing": 1,
    "padding": 1
  }
}}%%
flowchart LR
    0[(ドキュメント<br/>コレクション)]
    1A[
      <table border="1" cellspacing="0" bgcolor="#fdc">
        <tr><th>順位</th><th>ドキュメント</th></tr>
        <tr><td>1</td><td>40型液晶</td></tr>
        <tr><td>2</td><td>55型液晶</td></tr>
        <tr><td>3</td><td>32型壁掛け</td></tr>
      </table>
    ]
    1B[
      <table border="1" cellspacing="0" bgcolor="#fec">
        <tr><th>順位</th><th>ドキュメント</th></tr>
        <tr><td>1</td><td>40型4K</td></tr>
        <tr><td>2</td><td>55型4K</td></tr>
        <tr><td>3</td><td>65型4K</td></tr>
      </table>
    ]
    1C[
      <table border="1" cellspacing="0" bgcolor="#dec">
        <tr><th>順位</th><th>ドキュメント</th></tr>
        <tr><td>1</td><td>リモコン</td></tr>
        <tr><td>2</td><td>24型液晶</td></tr>
        <tr><td>3</td><td>32型液晶</td></tr>
      </table>
    ]
    2A@{icon: "mdi:user", label: "ユーザA", h: "100"}
    2B@{icon: "mdi:user", label: "ユーザB", h: "100"}
    2C@{icon: "mdi:user", label: "ユーザC", h: "100"}
    3A[
      <table border="1" cellspacing="0" bgcolor="#fdc">
        <tr><th>順位</th><th>フィードバック</th></tr>
        <tr><td>1</td><td>クリック</td></tr>
        <tr><td>2</td><td>-</td></tr>
        <tr><td>3</td><td>-</td></tr>
      </table>
    ]
    3B[
      <table border="1" cellspacing="0" bgcolor="#fec">
        <tr><th>順位</th><th>フィードバック</th></tr>
        <tr><td>1</td><td>購買</td></tr>
        <tr><td>2</td><td>クリック</td></tr>
        <tr><td>3</td><td>-</td></tr>
      </table>
    ]
    3C[
      <table border="1" cellspacing="0" bgcolor="#dec">
        <tr><th>順位</th><th>フィードバック</th></tr>
        <tr><td>1</td><td>-</td></tr>
        <tr><td>2</td><td>-</td></tr>
        <tr><td>3</td><td>-</td></tr>
      </table>
    ]
    4A[CTR: 1/3<br/>CVR: 0]
    4B[<strong>CTR: 2/3<br/>CVR: 1/3</strong>]
    4C[CTR: 0<br/>CVR: 0]
    0 -- 既存のランキング --> 1A --- 2A --> 3A --> 4A
    0 -- 新製品重視 --> 1B --- 2B --> 3B --> 4B
    0 -- 価格重視 --> 1C --- 2C --> 3C --> 4C
```


```mermaid
%%{init: {
  "flowchart": {
    "rankSpacing": 40,
    "nodeSpacing": 1,
    "padding": 1
  }
}}%%
flowchart LR
    0[(ドキュメント<br/>コレクション)]
    1A[
      <table border="1" cellspacing="0" bgcolor="#fdc">
        <tr><th>順位</th><th>ドキュメント</th></tr>
        <tr><td>1</td><td>40型液晶</td></tr>
        <tr><td>2</td><td>55型液晶</td></tr>
        <tr><td>3</td><td>32型壁掛け</td></tr>
      </table>
    ]
    1B[
      <table border="1" cellspacing="0" bgcolor="#fec">
        <tr><th>順位</th><th>ドキュメント</th></tr>
        <tr><td>1</td><td>40型4K</td></tr>
        <tr><td>2</td><td>55型4K</td></tr>
        <tr><td>3</td><td>65型4K</td></tr>
      </table>
    ]
    1C[
      <table border="1" cellspacing="0" bgcolor="#dec">
        <tr><th>順位</th><th>ドキュメント</th></tr>
        <tr><td>1</td><td>リモコン</td></tr>
        <tr><td>2</td><td>24型液晶</td></tr>
        <tr><td>3</td><td>32型液晶</td></tr>
      </table>
    ]
    2@{icon: "mdi:blender", label: "Multileaving", h: "100"}
    3A[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#fdc"><td>1</td><td>既存</td><td>40型液晶</td></tr>
        <tr bgcolor="#fec"><td>2</td><td>新製品</td><td>55型4K</td></tr>
        <tr bgcolor="#dec"><td>3</td><td>価格</td><td>32型液晶</td></tr>
      </table>
    ]
    3B[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#fec"><td>1</td><td>新製品</td><td>40型4K</td></tr>
        <tr bgcolor="#dec"><td>2</td><td>価格</td><td>24型液晶</td></tr>
        <tr bgcolor="#fdc"><td>3</td><td>既存</td><td>32型壁掛け</td></tr>
      </table>
    ]
    3C[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#dec"><td>1</td><td>価格</td><td>リモコン</td></tr>
        <tr bgcolor="#fdc"><td>2</td><td>既存</td><td>55型液晶</td></tr>
        <tr bgcolor="#fec"><td>3</td><td>新製品</td><td>65型4K</td></tr>
      </table>
    ]
    0 -- 既存のランキング --> 1A --- 2 --> 3A
    0 -- 新製品重視 --> 1B --- 2 --> 3B
    0 -- 価格重視 --> 1C --- 2 --> 3C
```


```mermaid
%%{init: {
  "flowchart": {
    "rankSpacing": 40,
    "nodeSpacing": 1,
    "padding": 1
  }
}}%%
flowchart LR
    0A[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#fdc"><td>1</td><td>既存</td><td>40型液晶</td></tr>
        <tr bgcolor="#fec"><td>2</td><td>新製品</td><td>55型4K</td></tr>
        <tr bgcolor="#dec"><td>3</td><td>価格</td><td>32型液晶</td></tr>
      </table>
    ]
    0B[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#fec"><td>1</td><td>新製品</td><td>40型4K</td></tr>
        <tr bgcolor="#dec"><td>2</td><td>価格</td><td>24型液晶</td></tr>
        <tr bgcolor="#fdc"><td>3</td><td>既存</td><td>32型壁掛け</td></tr>
      </table>
    ]
    0C[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#dec"><td>1</td><td>価格</td><td>リモコン</td></tr>
        <tr bgcolor="#fdc"><td>2</td><td>既存</td><td>55型液晶</td></tr>
        <tr bgcolor="#fec"><td>3</td><td>新製品</td><td>65型4K</td></tr>
      </table>
    ]
    1A@{icon: "mdi:user", label: "ユーザA", h: "100"}
    1B@{icon: "mdi:user", label: "ユーザB", h: "100"}
    1C@{icon: "mdi:user", label: "ユーザC", h: "100"}
    2A[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>フィードバック</th></tr>
        <tr bgcolor="#fdc"><td>1</td><td>既存</td><td>クリック</td></tr>
        <tr bgcolor="#fec"><td>2</td><td>新製品</td><td>-</td></tr>
        <tr bgcolor="#dec"><td>3</td><td>価格</td><td>-</td></tr>
      </table>
    ]
    2B[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>フィードバック</th></tr>
        <tr bgcolor="#fec"><td>1</td><td>新製品</td><td>購買</td></tr>
        <tr bgcolor="#dec"><td>2</td><td>価格</td><td>-</td></tr>
        <tr bgcolor="#fdc"><td>3</td><td>既存</td><td>-</td></tr>
      </table>
    ]
    2C[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>フィードバック</th></tr>
        <tr bgcolor="#dec"><td>1</td><td>価格</td><td>-</td></tr>
        <tr bgcolor="#fdc"><td>2</td><td>既存</td><td>-</td></tr>
        <tr bgcolor="#fec"><td>3</td><td>新製品</td><td>クリック</td></tr>
      </table>
    ]
    3[
      <table border="1" cellspacing="0">
        <tr><th>手法</th><th>CTR</th><th>CVR</th></tr>
        <tr bgcolor="#fdc"><td>既存</td><td>1/3</td><td>0</td></tr>
        <tr bgcolor="#fec"><td>新製品</td><td><strong>2/3</strong></td><td><strong>1/3</strong></td></tr>
        <tr bgcolor="#dec"><td>価格</td><td>0</td><td>0</td></tr>
      </table>
    ]
    0A --- 1A --> 2A --> 3
    0B --- 1B --> 2B --> 3
    0C --- 1C --> 2C --> 3
```


```mermaid
%%{init: {
  "flowchart": {
    "rankSpacing": 40,
    "nodeSpacing": 1,
    "padding": 1
  }
}}%%
flowchart LR
    0[(ドキュメント<br/>コレクション)]
    1A[
      <table border="1" cellspacing="0" bgcolor="#fdc">
        <tr><th>順位</th><th>ドキュメント</th></tr>
        <tr><td>1</td><td>40型液晶</td></tr>
        <tr><td>2</td><td>55型液晶</td></tr>
        <tr><td>3</td><td>32型壁掛け</td></tr>
      </table>
    ]
    1B[
      <table border="1" cellspacing="0" bgcolor="#fec">
        <tr><th>順位</th><th>ドキュメント</th></tr>
        <tr><td>1</td><td>40型4K</td></tr>
        <tr><td>2</td><td>55型4K</td></tr>
        <tr><td>3</td><td>65型4K</td></tr>
      </table>
    ]
    1C[
      <table border="1" cellspacing="0" bgcolor="#dec">
        <tr><th>順位</th><th>ドキュメント</th></tr>
        <tr><td>1</td><td>リモコン</td></tr>
        <tr><td>2</td><td>24型液晶</td></tr>
        <tr><td>3</td><td>32型液晶</td></tr>
      </table>
    ]
    2@{icon: "mdi:blender", label: "Multileaving", h: "100"}
    3A[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#fdc"><td>1</td><td>既存</td><td>40型液晶</td></tr>
        <tr bgcolor="#fec"><td>2</td><td>新製品</td><td>55型4K</td></tr>
        <tr bgcolor="#dec"><td>3</td><td>価格</td><td>32型液晶</td></tr>
      </table>
    ]
    3B[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#fec"><td>1</td><td>新製品</td><td>40型4K</td></tr>
        <tr bgcolor="#dec"><td>2</td><td>価格</td><td>24型液晶</td></tr>
        <tr bgcolor="#fdc"><td>3</td><td>既存</td><td>32型壁掛け</td></tr>
      </table>
    ]
    3C[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#dec"><td>1</td><td>価格</td><td>リモコン</td></tr>
        <tr bgcolor="#fdc"><td>2</td><td>既存</td><td>55型液晶</td></tr>
        <tr bgcolor="#fec"><td>3</td><td>新製品</td><td>65型4K</td></tr>
      </table>
    ]
    4[(ランキング<br/>コレクション)]
    0 -- 既存のランキング --> 1A --- 2
    0 -- 新製品重視 --> 1B --- 2
    0 -- 価格重視 --> 1C --- 2
    2 --> 3A & 3B & 3C --> 4
```

```mermaid
%%{init: {
  "flowchart": {
    "rankSpacing": 40,
    "nodeSpacing": 1,
    "padding": 1
  }
}}%%
flowchart LR
    -1[(ランキング<br/>コレクション)]
    0A[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#fdc"><td>1</td><td>既存</td><td>40型液晶</td></tr>
        <tr bgcolor="#fec"><td>2</td><td>新製品</td><td>55型4K</td></tr>
        <tr bgcolor="#dec"><td>3</td><td>価格</td><td>32型液晶</td></tr>
      </table>
    ]
    0B[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#fec"><td>1</td><td>新製品</td><td>40型4K</td></tr>
        <tr bgcolor="#dec"><td>2</td><td>価格</td><td>24型液晶</td></tr>
        <tr bgcolor="#fdc"><td>3</td><td>既存</td><td>32型壁掛け</td></tr>
      </table>
    ]
    0C[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>ドキュメント</th></tr>
        <tr bgcolor="#dec"><td>1</td><td>価格</td><td>リモコン</td></tr>
        <tr bgcolor="#fdc"><td>2</td><td>既存</td><td>55型液晶</td></tr>
        <tr bgcolor="#fec"><td>3</td><td>新製品</td><td>65型4K</td></tr>
      </table>
    ]
    1A@{icon: "mdi:user", label: "ユーザA", h: "100"}
    1B@{icon: "mdi:user", label: "ユーザB", h: "100"}
    1C@{icon: "mdi:user", label: "ユーザC", h: "100"}
    2A[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>フィードバック</th></tr>
        <tr bgcolor="#fdc"><td>1</td><td>既存</td><td>クリック</td></tr>
        <tr bgcolor="#fec"><td>2</td><td>新製品</td><td>-</td></tr>
        <tr bgcolor="#dec"><td>3</td><td>価格</td><td>-</td></tr>
      </table>
    ]
    2B[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>フィードバック</th></tr>
        <tr bgcolor="#fec"><td>1</td><td>新製品</td><td>購買</td></tr>
        <tr bgcolor="#dec"><td>2</td><td>価格</td><td>-</td></tr>
        <tr bgcolor="#fdc"><td>3</td><td>既存</td><td>-</td></tr>
      </table>
    ]
    2C[
      <table border="1" cellspacing="0">
        <tr><th>順位</th><th>手法</th><th>フィードバック</th></tr>
        <tr bgcolor="#dec"><td>1</td><td>価格</td><td>-</td></tr>
        <tr bgcolor="#fdc"><td>2</td><td>既存</td><td>-</td></tr>
        <tr bgcolor="#fec"><td>3</td><td>新製品</td><td>クリック</td></tr>
      </table>
    ]
    3[
      <table border="1" cellspacing="0">
        <tr><th>手法</th><th>CTR</th><th>CVR</th></tr>
        <tr bgcolor="#fdc"><td>既存</td><td>1/3</td><td>0</td></tr>
        <tr bgcolor="#fec"><td>新製品</td><td><strong>2/3</strong></td><td><strong>1/3</strong></td></tr>
        <tr bgcolor="#dec"><td>価格</td><td>0</td><td>0</td></tr>
      </table>
    ]
    -1 --> 0A --- 1A --> 2A --> 3
    -1 --> 0B --- 1B --> 2B --> 3
    -1 --> 0C --- 1C --> 2C --> 3
```
