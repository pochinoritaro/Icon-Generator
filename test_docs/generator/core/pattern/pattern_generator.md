# UT仕様
## 正常系テスト項目（期待通りの動作確認）
- 指定した16進数文字列から正しいサイズのパターンが生成されること
- 生成されたパターンが左右対称であること
- apply_color メソッドで指定したRGB色が正しくパターンに適用されること
- apply_color が返す配列の形状が (PATTERN_WIDTH, PATTERN_HEIGHT, 3) になっていること
- apply_color がパターンの白部分に白（255,255,255）を適用していること
- 90度回転した最終パターンが期待通りのものになっていること

## 異常系テスト項目（入力値や環境の誤りに対する挙動）
- 16進数文字列の長さが正しくない場合に ValueError が発生すること
- 16進数以外の文字（例：GやZなど）が含まれている場合に ValueError が発生すること
- apply_color に渡す RGB リストの長さが3でない場合に ValueError が発生すること
- apply_color に渡す RGB の各要素が 0〜255 の整数範囲外の場合に ValueError が発生すること
- apply_color に渡す RGB の要素が整数でない場合に ValueError が発生すること

## 準異常系テスト項目（入力は正しいが境界値や特殊ケース）
- 16進数文字列がすべて偶数（またはすべて奇数）で偏ったパターンになる場合の処理確認
- RGB色が白（255,255,255）の場合の動作確認（すべて白になるか）
- RGB色が黒（0,0,0）の場合の動作確認
- apply_color に空のリストや None が渡された場合の挙動（明示的にエラーになるかなど）
- 16進数文字列の大文字・小文字混在時に正しく処理できることの確認
- 連続した同じ値が並ぶ16進数パターンで、ミラーリング処理が崩れないこと