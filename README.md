# pairwise-gradient-dither

## 领域

游戏、图形与多媒体

## 主题

渐变抖动

## 说明

高位缓冲、时变噪声与编码前处理。

初始状态下 `render/gradient_dither.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
