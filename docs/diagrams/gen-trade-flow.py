# -*- coding: utf-8 -*-
"""关卡主视图：三端 -> 订单交易与履约中心(关卡A支付处理/关卡B履约准入) -> 通过/拒绝回环"""
import sys
from xml.sax.saxutils import escape

def esc(s):
    return escape(str(s)).replace("&amp;#xa;", "&#xa;")

cells, edges = [], []
_n = [1]

def nid():
    _n[0] += 1
    return "c%d" % _n[0]

def node(x, y, w, h, label, style, parent="1"):
    i = nid()
    cells.append('<mxCell id="%s" value="%s" style="%s" vertex="1" parent="%s">'
                 '<mxGeometry x="%d" y="%d" width="%d" height="%d" as="geometry"/></mxCell>'
                 % (i, esc(label), style, parent, x, y, w, h))
    return i

def edge(src, dst, label="", style=None, pts=None, pins=""):
    e = ('<mxCell id="%s" value="%s" style="%s" edge="1" parent="1" source="%s" target="%s">'
         '<mxGeometry relative="1" as="geometry">' % (nid(), esc(label), (style or NORM) + pins, src, dst))
    if pts:
        e += '<Array as="points">' + "".join('<mxPoint x="%d" y="%d"/>' % p for p in pts) + '</Array>'
    edges.append(e + '</mxGeometry></mxCell>')

# ---------- 样式 ----------
NORM = ("edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;"
        "endArrow=block;endSize=8;strokeColor=#333333;fontColor=#333333;labelBackgroundColor=#ffffff;")
DENY = ("edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;"
        "endArrow=block;endSize=8;dashed=1;strokeColor=#b85450;fontColor=#b85450;labelBackgroundColor=#ffffff;")
OK   = ("edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;"
        "endArrow=block;endSize=8;strokeColor=#82b366;fontColor=#3f7a2a;labelBackgroundColor=#ffffff;")
WARN = ("edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;"
        "endArrow=block;endSize=8;dashed=1;strokeColor=#d79b00;fontColor=#7c4a00;labelBackgroundColor=#ffffff;")
DATA = ("edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;"
        "endArrow=open;endSize=10;dashed=1;strokeColor=#666666;fontColor=#666666;labelBackgroundColor=#ffffff;")

BLUE  = "rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontColor=#1f3b63;"
GREEN = "rounded=0;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontColor=#2f5520;"
YELB  = "rounded=0;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontColor=#7a5c00;"
DIAY  = "rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontColor=#7a5c00;"
DIAR  = "rhombus;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontColor=#7a1f1b;"
RED   = "rounded=0;whiteSpace=wrap;html=1;fillColor=#f8cecc;strokeColor=#b85450;fontColor=#7a1f1b;"
ORNG  = "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;fontColor=#7c4a00;"
WHITEP= "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#9673a6;fontColor=#4a2a6b;"
GREY  = "rounded=0;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#999999;fontColor=#555555;"
NOTE  = ("shape=note;whiteSpace=wrap;html=1;size=14;fillColor=#fff2cc;strokeColor=#d6b656;"
         "align=left;spacingLeft=6;fontSize=11;fontColor=#5a4500;")
CYL   = ("shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=14;"
         "fillColor=#ffffff;strokeColor=#666666;fontColor=#333333;fontSize=11;")
EXT   = ("rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#666666;dashed=1;"
         "fontColor=#333333;")
TRADE_C = ("swimlane;html=1;startSize=34;collapsible=0;resizeParent=0;fillColor=#e1d5e7;"
           "swimlaneFillColor=#fbf9fd;strokeColor=#7b4bb5;strokeWidth=3;fontStyle=1;fontColor=#4a2a6b;"
           "fontSize=16;align=center;")
CONT_A = ("swimlane;html=1;startSize=30;collapsible=0;resizeParent=0;fillColor=#e1d5e7;"
          "swimlaneFillColor=#ffffff;strokeColor=#7b4bb5;strokeWidth=2;fontStyle=1;fontColor=#5c2d91;"
          "fontSize=13;align=left;spacingLeft=8;")
CONT_B = ("swimlane;html=1;startSize=30;collapsible=0;resizeParent=0;fillColor=#ffe6cc;"
          "swimlaneFillColor=#fffaf3;strokeColor=#d79b00;strokeWidth=3;fontStyle=1;fontColor=#7c4a00;"
          "fontSize=13;align=left;spacingLeft=8;")
CONT_N = ("swimlane;html=1;startSize=30;collapsible=0;resizeParent=0;fillColor=#fde7e7;"
          "swimlaneFillColor=#ffffff;strokeColor=#b85450;strokeWidth=2;dashed=1;fontStyle=1;"
          "fontColor=#7a1f1b;fontSize=13;align=left;spacingLeft=8;")
CONT_O = ("swimlane;html=1;startSize=30;collapsible=0;resizeParent=0;fillColor=#fff7ec;"
          "swimlaneFillColor=#ffffff;strokeColor=#d79b00;strokeWidth=2;dashed=1;fontStyle=1;"
          "fontColor=#7c4a00;fontSize=13;align=left;spacingLeft=8;")
CONT_G = ("swimlane;html=1;startSize=30;collapsible=0;resizeParent=0;fillColor=#d5e8d4;"
          "swimlaneFillColor=#ffffff;strokeColor=#82b366;strokeWidth=2;fontStyle=1;fontColor=#2f5520;"
          "fontSize=13;align=left;spacingLeft=8;")
CONT_K = ("swimlane;html=1;startSize=30;collapsible=0;resizeParent=0;fillColor=#f5f5f5;"
          "swimlaneFillColor=#ffffff;strokeColor=#999999;strokeWidth=1;dashed=1;fontStyle=1;"
          "fontColor=#555555;fontSize=12;align=left;spacingLeft=8;")

TOP_IN=";entryX=0.5;entryY=0;entryDx=0;entryDy=0;"
BOT_IN=";entryX=0.5;entryY=1;entryDx=0;entryDy=0;"
LEFT_IN=";entryX=0;entryY=0.5;entryDx=0;entryDy=0;"
RIGHT_IN=";entryX=1;entryY=0.5;entryDx=0;entryDy=0;"
LEFT_IN7=";entryX=0;entryY=0.7;entryDx=0;entryDy=0;"
LEFT_IN3=";entryX=0;entryY=0.3;entryDx=0;entryDy=0;"
TOP_OUT=";exitX=0.5;exitY=0;exitDx=0;exitDy=0;"
BOT_OUT=";exitX=0.5;exitY=1;exitDx=0;exitDy=0;"
RIGHT_OUT=";exitX=1;exitY=0.5;exitDx=0;exitDy=0;"
LEFT_OUT=";exitX=0;exitY=0.5;exitDx=0;exitDy=0;"

# ---------- 标题 ----------
cells.append('<mxCell id="title" value="订单交易与履约中心 —— 三端下单与履约业务流程图（关卡 A 支付处理 → 关卡 B 履约准入 → 发货交付）" '
             'style="text;html=1;align=left;verticalAlign=middle;fontSize=24;fontStyle=1;fontColor=#262626;" '
             'vertex="1" parent="1"><mxGeometry x="80" y="36" width="2000" height="44" as="geometry"/></mxCell>')

# ---------- 图例 ----------
rows = [("#333333", "s", "正常业务流（黑实线）"),
        ("#b85450", "d", "支付失败 · 履约拒绝 · 退款换规格（红虚线）"),
        ("#82b366", "s", "准入通过 · 完成履约（绿线）"),
        ("#d79b00", "d", "风控命中 · 人工审核分支（橙虚线）"),
        ("#666666", "d", "查询规则库 / Redis / 支付网关（灰虚线）"),
        ("#e1d5e7", "b", "订单交易与履约中心 · 关卡 A 支付处理"),
        ("#ffe6cc", "b", "关卡 B · 履约准入"),
        ("#dae8fc", "b", "买家端"),
        ("#d5e8d4", "b", "商家 · 履约交付结果"),
        ("#fff2cc", "b", "运营后台 · 人工审核"),
        ("#f8cecc", "b", "拒绝提示 · 自动原路退款区")]
lh = 30 + 24 * len(rows)
legs = ['<mxCell id="legend" value="图例" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;'
        'strokeColor=#666666;verticalAlign=top;fontSize=14;fontStyle=1;align=left;spacingLeft=8;" '
        'vertex="1" parent="1"><mxGeometry x="2380" y="140" width="440" height="%d" as="geometry"/></mxCell>' % lh]
for k, (color, kind, label) in enumerate(rows):
    yy = 34 + 24 * k
    if kind in ("s", "d"):
        dash = ";dashed=1" if kind == "d" else ""
        legs.append('<mxCell id="lg%d" value="" style="endArrow=block;endSize=6;strokeColor=%s%s;html=1;strokeWidth=2;" '
                    'edge="1" parent="legend"><mxGeometry relative="1" as="geometry">'
                    '<mxPoint as="sourcePoint" x="12" y="%d"/><mxPoint as="targetPoint" x="66" y="%d"/>'
                    '</mxGeometry></mxCell>' % (k, color, dash, yy + 8, yy + 8))
    else:
        legs.append('<mxCell id="lgb%d" value="" style="rounded=0;html=1;fillColor=%s;strokeColor=#999999;" '
                    'vertex="1" parent="legend"><mxGeometry x="14" y="%d" width="52" height="16" as="geometry"/>'
                    '</mxCell>' % (k, color, yy))
    legs.append('<mxCell id="lgt%d" value="%s" style="text;html=1;align=left;verticalAlign=middle;fontSize=12;" '
                'vertex="1" parent="legend"><mxGeometry x="80" y="%d" width="350" height="20" as="geometry"/>'
                '</mxCell>' % (k, esc(label), yy - 2))

# ---------- 结构容器 ----------
trade   = node(620, 140, 1360, 880, "订单交易与履约中心（三端共用：统一收银台 · 支付处理 · 履约准入 · 状态编排）", TRADE_C)
gateA   = node(40, 70, 620, 760, "关卡 A · 支付处理（下单受理 → 收单 → 支付回调）", CONT_A, parent=trade)
gateB   = node(700, 70, 620, 760, "关卡 B · 履约准入（支付成功 ≠ 一定能履约发货）", CONT_B, parent=trade)
zone    = node(140, 1120, 580, 430, "已支付被拒 → 提示 → 自动原路退款 → 换规格重下（不离开订单页）", CONT_N)
ops     = node(2060, 640, 460, 360, "运营后台 · 风控人工审核", CONT_O)
res     = node(1440, 1150, 560, 280, "回到最初想购买的订单（换规格重下后完成原目标履约）", CONT_G)
strip   = node(140, 1640, 2380, 300, "先用后付（独立流程 · 同一交易履约中心与同一套准入规则）", CONT_A)
other   = node(2060, 1060, 460, 240, "其他接入渠道（次要）", CONT_K)

# ---------- 两侧节点 ----------
buyer    = node(140, 200, 340, 90, "买家端用户&#xa;发起下单 · 完成支付 · 查看订单", BLUE)
merchant = node(140, 360, 340, 90, "商家后台&#xa;商品与库存维护 · 处理发货", GREEN)
db       = node(2060, 140, 300, 120, "订单与准入规则数据库&#xa;订单 · SKU 库存 · 商品归属&#xa;履约渠道准入规则 · 风控名单", CYL)
redis    = node(2060, 300, 300, 110, "Redis&#xa;下单快照 · 支付幂等 · 履约临时状态", CYL)
paygw    = node(2060, 460, 300, 110, "支付网关（微信 / 支付宝 / 银行卡）&#xa;收单 · 原路退款", EXT)

# ---------- 说明便签 ----------
node(800, 1150, 580, 170,
     "反向场景：跨境商品走普通渠道 → 被普通渠道准入规则拒绝 →&#xa;换用跨境收货方式重新提交 → 准入通过 →&#xa;返回最初提交的订单完成发货。", NOTE)
node(800, 1360, 580, 150,
     "铁律：支付成功 ≠ 一定能履约发货。关卡 A（支付处理）与&#xa;关卡 B（履约准入）是两个独立判断，顺序不可颠倒。", NOTE)

# ---------- 关卡 A · 支付处理 ----------
o_in    = node(30, 50, 560, 70, "买家选定商品发起下单&#xa;交易中心生成订单并占用库存预占", WHITEP, parent=gateA)
checkout= node(30, 160, 560, 70, "统一收银台（三端共用同一张）· 买家选择支付方式", WHITEP, parent=gateA)
charge  = node(30, 270, 560, 70, "向支付网关发起收单（微信 / 支付宝 / 银行卡）", WHITEP, parent=gateA)
pay_ok  = node(110, 380, 400, 130, "支付成功？", DIAY, parent=gateA)
pay_fail= node(30, 570, 260, 80, "支付未完成（扣款失败 / 超时）", RED, parent=gateA)
risk_rev= node(330, 570, 260, 80, "大额支付二次验证&#xa;支付风控复核", ORNG, parent=gateA)

# ---------- 关卡 B · 履约准入 ----------
g_in     = node(30, 50, 560, 70, "获取当前订单身份 + 买家实际选择的履约渠道 / 收货地址", WHITEP, parent=gateB)
g_query  = node(30, 160, 560, 90, "查询商品归属及履约渠道准入规则&#xa;库存是否充足 · 该 SKU 是否允许此渠道发货&#xa;买家是否在风控名单", WHITEP, parent=gateB)
admit    = node(110, 300, 400, 150, "当前订单是否满足目标&#xa;履约渠道的准入条件？", DIAR, parent=gateB)
fulfill  = node(30, 500, 560, 70, "履约编排与发货：生成待发货订单并通知商家", GREEN, parent=gateB)

# ---------- 拒绝 → 提示 → 自动退款 → 换规格重下（左下红虚线区） ----------
p_deny   = node(30, 40, 520, 110, "当前订单无法按所选方式履约，已为你原路退款，&#xa;请更换规格或收货方式重新下单", RED, parent=zone)
p_refund = node(30, 180, 520, 70, "触发自动原路退款（已支付订单 · 免重复扣款）", ORNG, parent=zone)
p_respec = node(30, 290, 520, 90, "在订单确认页更换可用规格 / 收货方式重新提交&#xa;（不离开订单页 · 不退回商品首页）", ORNG, parent=zone)

# ---------- 运营后台 · 风控人工审核（右侧橙虚线分支） ----------
o_hit    = node(30, 40, 400, 70, "命中风控：黑名单 / 异常 → 订单挂起", ORNG, parent=ops)
o_review = node(30, 140, 400, 70, "运营人工审核（放行 / 驳回）", YELB, parent=ops)
o_pass   = node(30, 250, 190, 70, "审核放行&#xa;→ 准入通过履约", GREEN, parent=ops)
o_rej    = node(240, 250, 190, 70, "审核驳回&#xa;→ 退款关单", RED, parent=ops)

# ---------- 结果区：回到原订单 ----------
r_recv   = node(30, 45, 500, 80, "重新受理 → 重新准入通过&#xa;回到最初提交的订单", GREEN, parent=res)
r_done   = node(30, 155, 500, 80, "完成最初想购买的那笔订单（发货履约）", GREEN, parent=res)

# ---------- 先用后付（底部独立横条 · 7 步） ----------
steps = [("① 买家选择先用后付发起下单", BLUE),
         ("② 交易中心做信用预授权（不即时扣款）", WHITEP),
         ("③ 展示先用后付确认页", WHITEP),
         ("④ 买家确认先用后付协议", BLUE),
         ("⑤ 检查商品 / 买家是否允许先用后付（准入）", ORNG),
         ("⑥ 准入通过 → 先发货、后扣款", WHITEP),
         ("⑦ 收货确认 → 向支付网关发起延迟扣款", WHITEP)]
pay_steps = [node(30 + i * 330, 90, 300, 110, t, st, parent=strip)
             for i, (t, st) in enumerate(steps)]

# ---------- 其他接入渠道（次要 · 灰底） ----------
k1 = node(30, 45, 400, 70, "开放 API 渠道（三方接入 · 准入对所有用户开放）", GREY, parent=other)
k2 = node(30, 145, 400, 70, "小程序渠道（三方接入 · 准入对所有用户开放）", GREY, parent=other)

# ---------- 主链：三端汇入 → 关卡 A ----------
edge(buyer, o_in, "发起下单", NORM, pins=RIGHT_OUT + LEFT_IN)
edge(merchant, trade, "商品 · 库存维护", NORM, pins=RIGHT_OUT + LEFT_IN7)
edge(o_in, checkout, "尚未支付", NORM, pins=BOT_OUT + TOP_IN)
edge(checkout, charge, "选择支付方式", NORM, pins=BOT_OUT + TOP_IN)
edge(charge, pay_ok, "发起收单", NORM, pins=BOT_OUT + TOP_IN)

# 关卡 A → 关卡 B（支付成功 · 一次短横跳）
edge(pay_ok, g_in, "支付成功", NORM, pts=[(1300, 655), (1300, 295)],
     pins=RIGHT_OUT + LEFT_IN)

# 关卡 B：查询 → 判断 → 通过履约
edge(g_in, g_query, "取订单与所选渠道", NORM, pins=BOT_OUT + TOP_IN)
edge(g_query, admit, "查询结果", NORM, pins=BOT_OUT + TOP_IN)
edge(admit, fulfill, "满足", OK, pins=BOT_OUT + TOP_IN)

# ---------- 异常路径：支付失败红虚线小回环（左侧） ----------
edge(pay_ok, pay_fail, "失败 / 超时", DENY, pts=[(860, 745), (860, 790)],
     pins=BOT_OUT + TOP_IN)
edge(pay_fail, checkout, "重新发起支付", DENY, pts=[(645, 790), (645, 405)],
     pins=LEFT_OUT + LEFT_IN3)

# ---------- 履约拒绝 → 提示 → 自动退款 → 换规格重下（红虚线入左下红区） ----------
edge(admit, p_deny, "不满足（如库存不足）", DENY, pts=[(1335, 585), (1335, 1090), (430, 1090)],
     pins=LEFT_OUT + TOP_IN)
edge(p_deny, p_refund, "已提示", DENY, pins=BOT_OUT + TOP_IN)
edge(p_refund, p_respec, "退款完成", DENY, pins=BOT_OUT + TOP_IN)

# ---------- 换规格重下 → 绿线回原订单（不退回商品首页） ----------
edge(p_respec, r_recv, "重新提交", OK, pts=[(750, 1455), (750, 1580), (1400, 1580), (1400, 1240)],
     pins=RIGHT_OUT + LEFT_IN7)

# ---------- 风控命中 → 右侧橙虚线进运营审核 ----------
edge(admit, o_hit, "命中风控名单", WARN, pts=[(1950, 585), (1950, 690)],
     pins=";exitX=1;exitY=0.7;exitDx=0;exitDy=0;" + LEFT_IN)

# ---------- 数据侧（灰虚线，非业务流） ----------
edge(g_query, db, "查询渠道准入规则 · 风控名单", DATA, pts=[(1990, 415), (1990, 200)],
     pins=RIGHT_OUT + LEFT_IN)
edge(fulfill, redis, "写履约临时状态", DATA, pts=[(2040, 745), (2040, 355)],
     pins=RIGHT_OUT + LEFT_IN)
edge(pay_steps[6], paygw, "延迟扣款", DATA, pts=[(2300, 1560), (2550, 1560), (2550, 515)],
     pins=TOP_OUT + RIGHT_IN)

# ---------- 运营审核内链 + 放行回履约 ----------
edge(o_hit, o_review, "挂起转人工", NORM, pins=BOT_OUT + TOP_IN)
edge(o_review, o_pass, "放行", NORM,
     pins=";exitX=0.2375;exitY=1;exitDx=0;exitDy=0;" + TOP_IN)
edge(o_review, o_rej, "驳回", NORM,
     pins=";exitX=0.7625;exitY=1;exitDx=0;exitDy=0;" + TOP_IN)
edge(o_pass, fulfill, "审核放行 · 准入通过履约", OK, pts=[(2000, 925), (2000, 830), (1630, 830)],
     pins=LEFT_OUT + BOT_IN)
edge(r_recv, r_done, "完成原目标", OK, pins=BOT_OUT + TOP_IN)

# ---------- 装配 ----------
W, H = 2860, 2100
xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<mxfile host="drawio" version="26.0.0">\n'
       '<diagram name="订单交易与履约中心业务流程图">\n'
       '<mxGraphModel dx="1600" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" '
       'arrows="1" fold="1" page="1" pageScale="1" pageWidth="%d" pageHeight="%d">\n'
       '<root><mxCell id="0"/><mxCell id="1" parent="0"/>\n' % (W, H))
xml += "".join(cells) + "\n" + "".join(edges) + "\n" + "".join(legs) + "\n"
xml += '</root></mxGraphModel></diagram></mxfile>\n'
open(sys.argv[1], "w", encoding="utf-8").write(xml)
print("wrote", sys.argv[1], len(xml), "bytes;", len(cells), "nodes,", len(edges), "edges")
