---
name: "resume-optimizer"
description: "根据岗位JD优化简历，筛选相关经历、优化技能和个人介绍，生成匹配度高的简历。Invoke when user needs to optimize resume based on job description."
---

# 简历优化器

## 功能说明

本技能利用LLM帮助用户根据岗位JD自动优化简历，主要功能包括：

1. 使用LLM深度理解岗位JD要求
2. 智能筛选预存简历中与岗位JD最匹配的实习、工作、项目经历
3. 根据岗位JD专属优化技能、个人介绍等内容
4. 生成一份能够大概率通过筛选进入面试阶段的完美简历

## 使用方法

1. 准备好你的预存简历信息
2. 提供岗位JD（文字或描述）
3. 运行简历优化工具

## 文件结构

- `resume_data.json` - 预存的简历信息
- `optimize_resume.py` - 简历优化主程序（使用LLM）
- `requirements.txt` - 依赖包列表

## 快速开始

1. 准备你的简历数据
2. 调用技能进行优化：系统会自动使用LLM分析JD并优化简历

