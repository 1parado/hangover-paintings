# Hangover's Paintings 画橱

一个部署在 GitHub Pages 上的 3D 画廊网站，用 Three.js 搭建的拟真画展：四面墙挂画、射灯轨道、彩旗与樱花粉色调，支持键盘/按钮导航、点击聚焦、BGM 开关与移动端触控。

**在线访问**：<https://1parado.github.io/hangover-paintings/>

学AI，上[L站](https://linux.do/)

## 功能

- 四面墙单行挂画，左右按钮 / 方向键循环切换，点击画作聚焦
- 上一幅 / 下一幅、转墙按钮（iOS 玻璃风 UI），移动端适配
- 背景音乐开关（BGM：Le Castle Vania - Shots Fired）
- 图片自动压缩 + jsDelivr CDN 备用源 + 渐进式加载（6 张即进场）

## 本地预览

```bash
python -m http.server 8734
```

打开 <http://localhost:8734>。

## 目录结构

```
index.html   站点（单文件，Three.js 走 CDN）
img/         画作（已压缩）
bgm.mp3      背景音乐
tools/       图片压缩 / NCM 转码脚本
```
