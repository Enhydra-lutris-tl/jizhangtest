## 文件夹说明
### common 公用的方法
#### style_sheet.py
添加样式表
```python
# 使用此方法为组件或页面添加样式添加样式
StyleSheet.JIZHANG_VIEW.apply(self)
```

### components 组件存放

### config 配置文件存放

### resource 资源文件存放

### view 页面视图存放

### 其他
#### 记账报表json格式
```text
{
    "nowDate": nowDateime,
    "trade": comboxText,
    "iae": combox2Text,
    "payMethod": combox3Text,
    "moneyValue": DoubleSpinBoxText
}
```
#### todo
-[x] 1.qss不生效是文件路径问题
-[ ] 2.开始将通用方法解耦


