#!/usr/bin/env python3
import argparse
import json
import os
from typing import Dict, Any


SYSTEM_PROMPT = """你是一位专业的简历优化专家，擅长根据岗位JD优化简历。你的任务是：

1. 深度理解岗位JD的核心要求
2. 从用户提供的"原始经历库"中筛选与岗位JD最匹配的经历
3. 优化技能列表，突出与JD匹配的技能
4. 优化个人介绍，使其更贴合岗位要求
5. 输出一份专业、与JD高度匹配的简历

请以JSON格式输出优化后的简历，保持原有的数据结构。重要：所有字段名(key)请使用中文！"""


class ResumeOptimizer:
    def __init__(self):
        pass
        
    def get_resume_txt_path(self) -> str:
        """获取 resume.txt 文件路径"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(script_dir))
        return os.path.join(project_root, "resume.txt")
    
    def load_resume_txt(self) -> str:
        """读取 resume.txt 文件"""
        try:
            resume_txt_path = self.get_resume_txt_path()
            with open(resume_txt_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print("⚠️  警告: resume.txt 文件未找到")
            return ""

    def build_optimization_prompt(self, resume_data: Dict, jd_text: str, resume_txt_content: str) -> str:
        """构建LLM优化提示词"""
        prompt = f"""请根据以下岗位JD优化简历：

【岗位JD】
{jd_text}

【原始经历库（从 resume.txt 读取）】
{resume_txt_content}

【基本信息】
{json.dumps(resume_data, ensure_ascii=False, indent=2)}

请完成以下优化：
1. 从"原始经历库"中筛选与JD最匹配的实习/工作经历（整合为3-5条）
2. 从"原始经历库"中筛选与JD最匹配的项目经历（整合为2-3个）
3. 根据经历内容，提取并优化技能列表（保留10-15个，优先展示与JD匹配的技能）
4. 优化个人介绍，突出与JD匹配的能力和经验
5. 为每条经历添加匹配度分析

请以JSON格式输出，包含以下字段："姓名"、"联系方式"、"个人介绍"、"技能"、"工作经历"、"项目经历"、"匹配分析"。重要：所有字段名(key)请使用中文！"""
        return prompt

    def optimize_resume(self, resume_data: Dict, jd_text: str) -> Dict:
        """使用LLM优化简历"""
        resume_txt_content = self.load_resume_txt()
        
        print("=" * 60)
        print("📋 简历优化任务")
        print("=" * 60)
        print(f"\n岗位JD长度: {len(jd_text)} 字符")
        print(f"✓ 已从 resume.txt 读取经历库，长度: {len(resume_txt_content)} 字符")
        print(f"基本信息包含 {len(resume_data.get('技能', []))} 项技能")
        print("\n" + "=" * 60)
        print("🤖 请使用以下提示词调用LLM进行优化：")
        print("=" * 60)
        
        prompt = self.build_optimization_prompt(resume_data, jd_text, resume_txt_content)
        print(f"\n{SYSTEM_PROMPT}\n\n{prompt}")
        
        print("\n" + "=" * 60)
        print("💡 使用说明：")
        print("=" * 60)
        print("1. 将上述提示词复制到你的LLM对话中")
        print("2. LLM会返回优化后的JSON简历")
        print("3. 将返回的JSON保存为 optimized_resume.json")
        print("=" * 60)
        
        return {
            "状态": "待处理",
            "消息": "请使用上述提示词调用LLM进行优化",
            "系统提示词": SYSTEM_PROMPT,
            "用户提示词": prompt,
            "说明": "已从 resume.txt 读取经历内容"
        }


def load_resume(file_path: str) -> Dict:
    """加载简历数据"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_resume(resume: Dict, file_path: str):
    """保存简历数据"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(resume, f, ensure_ascii=False, indent=2)


def create_sample_resume():
    """创建示例简历"""
    sample = {
        "姓名": "张三",
        "联系方式": {
            "邮箱": "zhangsan@example.com",
            "电话": "138-0000-0000"
        },
        "个人介绍": "热爱技术，具有3年软件开发经验，善于团队协作。",
        "技能": ["Python", "Java", "JavaScript", "MySQL", "Git", "Linux"],
        "工作经历": [
            {
                "公司": "ABC科技有限公司",
                "职位": "高级开发工程师",
                "时间": "2022.01 - 至今",
                "描述": "负责后端服务开发，使用Python和Django框架。",
                "成就": "优化系统性能，提升响应速度50%"
            },
            {
                "公司": "XYZ互联网公司",
                "职位": "前端开发工程师",
                "时间": "2020.06 - 2021.12",
                "描述": "使用React开发Web应用，负责用户界面设计。",
                "成就": "参与项目获得公司优秀项目奖"
            }
        ],
        "项目经历": [
            {
                "项目名称": "电商平台",
                "项目描述": "使用React和Node.js开发的全栈电商项目"
            }
        ]
    }
    
    save_resume(sample, "sample_resume.json")
    print("✅ 示例简历已创建: sample_resume.json")
    return sample


def main():
    parser = argparse.ArgumentParser(description='简历优化工具（基于LLM，自动读取 resume.txt）')
    parser.add_argument('--jd', type=str, help='岗位JD文字内容')
    parser.add_argument('--jd-file', type=str, help='岗位JD文件路径')
    parser.add_argument('--basic', type=str, default='basic_info.json', help='基本信息文件（默认: basic_info.json）')
    parser.add_argument('--init', action='store_true', help='创建示例基本信息文件')
    
    args = parser.parse_args()
    
    optimizer = ResumeOptimizer()
    
    if args.init:
        create_sample_resume()
        # 重命名为 basic_info.json
        if os.path.exists("sample_resume.json"):
            os.rename("sample_resume.json", "basic_info.json")
            print("✅ 示例基本信息已创建: basic_info.json")
        return
    
    jd_text = ""
    if args.jd:
        jd_text = args.jd
    elif args.jd_file:
        with open(args.jd_file, 'r', encoding='utf-8') as f:
            jd_text = f.read()
    else:
        print("❌ 请提供岗位JD内容 (--jd 或 --jd-file)")
        return
    
    # 检查 resume.txt 是否存在
    resume_txt_path = optimizer.get_resume_txt_path()
    if not os.path.exists(resume_txt_path):
        print(f"❌ 简历经历文件不存在: {resume_txt_path}")
        return
    
    # 加载基本信息
    resume_data = {}
    if os.path.exists(args.basic):
        resume_data = load_resume(args.basic)
    else:
        print("⚠️  未找到基本信息文件，使用空模板")
        resume_data = {
            "姓名": "",
            "联系方式": {
                "邮箱": "",
                "电话": ""
            },
            "个人介绍": "",
            "技能": []
        }
    
    result = optimizer.optimize_resume(resume_data, jd_text)
    
    save_resume(result, "optimization_prompt.json")
    print("\n✅ 优化提示词已保存至: optimization_prompt.json")


if __name__ == '__main__':
    main()
