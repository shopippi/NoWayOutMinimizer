# NoWayOutMinimizer
4つの数字と、四則演算、()の組み合わせで出力できない解の最小値を答える。

## 以下の条件をみたす式で、1、2、3…… という整数をそれぞれ作りたい。

- 3、4、5、6 の 4 つの数字をそれぞれただ一度だけ用いる。

- 演算子には、+、-、*、/ のいずれかを用いる (重複も可)。

- 演算順序を変更する括弧は自由に用いてよい。

## How to Solve Itになぞらえて今回の問題に取り組もうと思う。

### 第一原則：問題を理解する

- 未知のものは何か、与えられているものは何か。条件は何か。
	- 未知なもの→組み合わせの最大数は？{}を加えると何通りあるのだろ？

	- 与えられてるもの、条件
		- 3、4、5、6 の 4 つの数字をそれぞれただ一度だけ用いる。

		- 演算子には、+、-、*、/ のいずれかを用いる (重複も可)。

		- 演算順序を変更する括弧は自由に用いてよい。

- 条件を満足させうるか。条件は未知のものを定めるのに十分であるか。または、不十分であるか。又は、余剰であるか、または矛盾しているか。
	- 与えられた条件を用いて組み合わせの総数および、（）込みの組み合わせの総数も分かりそう。

- 図をかけ、適当な記号を導入せよ
	
	- A ? B ? C ? D
	- { A ? B } ? C ? D
	- A ? B ? {C ? D}
	- A ? {B ? C} ? D
	- {A ? B} ? {C ? D}
	- {A ? B ? C} ? D
	-A ? {B ? C ? D}
	-？は["+","-","*","/"]

- 条件の各部を分離せよ。
	- まず、+,- のみで表現できる数値の組み合わせを検証する事とした。
	- 1-100に表現できない数値が存在しているか検証してみた。

## プログラムの説明
1-100までの間で、numbers 今回は[3, 4, 5, 6]を一回ずつ用いた計算において、生み出す事の出来ない解の最小値をアウトプットするプログラムを作成した。

opには、計算記号を格納する。今回は、["+","-","*","/"]を使用した。
現段階では、opに^2のような四則演算以外の複雑な計算には対応していない。

## 実行例

python3 calc.pyと実行すると、

最小の数字は43となっています。
次に小さい値は46となっています。
と出力される。

```
if(result==○○): #解答の手法を示す。
    print(sol)
```
ここをresult == ○○にすると、解が○○となる数式を表示することが出来る。
例えば、
```
if(result==41): #解答の手法を示す。
    print(sol)
```
とすると、
```
(3+4)*5+6
(3+6)*4+5
(3+6)*5-4
(4+3)*5+6
5+4*(3+6)
5+4*(6+3)
(5+6)*4-3
(6+3)*4+5
(6+3)*5-4
6+5*(3+4)
6+5*(4+3)
(6+5)*4-3
```
と表示されます。
