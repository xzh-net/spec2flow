# ai-project-workflow

> 业务图（draw.io）的规格化生产与维护：业务设计说明书 + 图源（gen 脚本）+ 产物 + 画图 skill

**本文件是使用者入口**；开发者/维护者的治理文件是 [AGENTS.md](AGENTS.md)（由其维护、AI 会话自动加载，**使用者不需要读**）。

---

## 1. 使用者：怎么用

### 三步

1. **业务先定**：读 `docs/business/<图名>业务设计说明书.md`——业务对错以它为准；要新建就复制 [business-flow-template.md](.opencode/skills/business-flow-draw/templates/business-flow-template.md) 逐节填写。
2. **改图/画图**：对 AI 说一句 **"按 <说明书路径> 改图 / 画业务流程图"**，skill `business-flow-draw` 自动走"读业务 → 改图源 → 生成 → 校验 → 回写变更记录"六步；手工改则**只改 `docs/diagrams/gen-<标识>.py`**，禁止手改 `.drawio`（下次生成会覆盖）。
3. **验收**：三硬门槛全过才算交付——生成日志 `nodes>0 且 edges>0`、几何校验全 0、文字自检 OK；判据与排错见 [diagram-checklist.md](.opencode/skills/business-flow-draw/references/diagram-checklist.md)。

### 命令速查（可复制命令的唯一落点）

> **工作目录**：以下命令均为相对路径，**必须在 `ai-project-workflow\` 目录下执行**（在仓库根目录执行会报 `No such file`）：
>
> ```powershell
> Set-Location D:\xuzhihao\ai-engineering-demo\ai-project-workflow
> ```

`<标识>` 换成实际图名；当前实例为 `iam-flow`：

```powershell
# 生成
python3 docs\diagrams\gen-<标识>.py docs\diagrams\<标识>.drawio
# 验证① 看生成日志：nodes>0 且 edges>0
# 验证② 几何校验（下方 C:\ 路径为本机 drawio-skill 安装位置，换机按实际安装位置替换）
python3 C:\Users\admin\.config\opencode\skills\drawio-skill\scripts\validate.py docs\diagrams\<标识>.drawio --score
# 验证③ 文字与重叠自检
python3 .opencode\skills\business-flow-draw\scripts\check-diagram.py docs\diagrams\<标识>.drawio
```

现成三连（`iam-flow`，可直接复制运行）：

```powershell
python3 docs\diagrams\gen-iam-flow.py docs\diagrams\iam-flow.drawio
python3 C:\Users\admin\.config\opencode\skills\drawio-skill\scripts\validate.py docs\diagrams\iam-flow.drawio --score
python3 .opencode\skills\business-flow-draw\scripts\check-diagram.py docs\diagrams\iam-flow.drawio
```

### 当前图与说明书

| 说明书 | 图源 / 产物 | 状态 |
|---|---|---|
| [统一认证中心业务设计说明书](docs/business/统一认证中心业务设计说明书.md) — 三端共用一个认证中心，身份认证/授权/账号准入三环节分离 | [gen-iam-flow.py](docs/diagrams/gen-iam-flow.py) / [iam-flow.drawio](docs/diagrams/iam-flow.drawio) | 已生成，三硬校验通过（0 错误 / 0 警告 / 0 交叉 / 0 重叠） |
| [统一消息中心订阅推送业务设计说明书](docs/business/统一消息中心订阅推送业务设计说明书.md) — 订阅授权与触达准入两关卡，含配额延迟重试与换账号不串订阅 | `gen-message-push.py`（**尚未创建**） | 模拟演练稿，图尚未生成 |

---

## 2. 开发者：怎么改

治理文件 [AGENTS.md](AGENTS.md)：读者声明、目录权威分配、改图约定、验收判据、文档维护自查。**分层改哪里**：

| 要改什么 | 改哪里 | 留痕 |
|---|---|---|
| 业务内容 | 说明书正文 | 该说明书 §7 变更记录 |
| 图的坐标 / 文案 / 连线 | 只改 `gen-*.py`（唯一权威） | 无需回填清单 |
| 通用画图规范 / 验收判据 / 说明书模板 | skill `references/`、`templates/` | 改动靠 git；踩坑教训记 [维护/经验教训.md](维护/经验教训.md) |
| 项目约定 / 硬门槛判据 | `AGENTS.md` | 改动靠 git；教训与旧结论推翻记 [维护/经验教训.md](维护/经验教训.md) |

**改文档后自查**（AGENTS《文档维护自查》）：markdown 链接 0 断链；正文出现的 `*.md/*.py/*.drawio` 文件名与 `git ls-files` 实体逐个一致（不看自称）。

### 文件清单

| 文件 | 角色 |
|---|---|
| [AGENTS.md](AGENTS.md) | 项目治理（开发者维护；权威分配、改图约定、验收判据） |
| [SKILL.md](.opencode/skills/business-flow-draw/SKILL.md) | 改图工作流、硬性禁止与依赖说明 |
| [flowchart-guidelines.md](.opencode/skills/business-flow-draw/references/flowchart-guidelines.md) | 线型语义、配色、走线硬规则 |
| [diagram-checklist.md](.opencode/skills/business-flow-draw/references/diagram-checklist.md) | 三道硬门槛 + 软检查判据 + 排错表 |
| [check-diagram.py](.opencode/skills/business-flow-draw/scripts/check-diagram.py) | 硬门槛③：文字溢出 / 重叠自检 |
| [business-flow-template.md](.opencode/skills/business-flow-draw/templates/business-flow-template.md) | 业务设计说明书撰写模板 |
| [经验教训.md](维护/经验教训.md) | 现象 / 根因 / 修复分层 / 复发信号（维护侧留痕，使用者不读） |
