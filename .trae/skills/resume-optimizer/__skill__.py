"""
简历优化技能 - 直接使用LLM进行简历优化
固定读取 resume.txt 文件中的实习经历和项目经历
"""
import json
import os
from typing import Dict, Any


def get_resume_txt_path() -> str:
    """
    获取 resume.txt 文件的绝对路径
    """
    skill_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(skill_dir))
    return os.path.join(project_root, "resume.txt")


def load_resume_txt() -> str:
    """
    读取 resume.txt 文件中的经历内容
    """
    try:
        resume_txt_path = get_resume_txt_path()
        with open(resume_txt_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""


def build_complete_resume(basic_info: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    构建完整简历，将 resume.txt 的经历整合进去
    """
    if basic_info is None:
        basic_info = {
            "姓名": "",
            "联系方式": {
                "邮箱": "",
                "电话": ""
            },
            "个人介绍": "",
            "技能": []
        }
    
    resume_txt_content = load_resume_txt()
    
    # 将 resume.txt 的内容作为经历的详细描述
    complete_resume = basic_info.copy()
    complete_resume["原始经历库"] = resume_txt_content
    
    return complete_resume


def optimize_resume_with_llm(jd_text: str, basic_info: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    使用LLM优化简历，自动从 resume.txt 读取经历
    
    Args:
        jd_text: 岗位JD文字
        basic_info: 可选的基本信息（姓名、联系方式等）
        
    Returns:
        优化提示词
    """
    resume_txt_content = load_resume_txt()
    
    system_prompt = """你是一位专业的简历优化专家，擅长根据岗位JD优化简历。你的任务是：

1. 深度理解岗位JD的核心要求
2. 从用户提供的"原始经历库"中筛选与岗位JD最匹配的经历
3. 优化技能列表，突出与JD匹配的技能
4. 优化个人介绍，使其更贴合岗位要求
5. 输出一份专业、与JD高度匹配的简历

请以JSON格式输出优化后的简历，保持原有的数据结构，并在根节点添加"匹配分析"字段说明优化思路。重要：所有字段名(key)请使用中文！"""

    user_prompt = f"""请根据以下岗位JD优化简历：

【岗位JD】
{jd_text}

【原始经历库（从 resume.txt 读取）】
{resume_txt_content}

【基本信息】
{json.dumps(basic_info if basic_info else {}, ensure_ascii=False, indent=2)}

请完成以下优化：
1. 从"原始经历库"中筛选与JD最匹配的实习/工作经历（整合为3-5条）
2. 从"原始经历库"中筛选与JD最匹配的项目经历（整合为2-3个）
3. 根据经历内容，提取并优化技能列表（保留10-15个，优先展示与JD匹配的技能）
4. 优化个人介绍，突出与JD匹配的能力和经验
5. 为每条经历添加匹配度分析

请以JSON格式输出，包含以下字段："姓名"、"联系方式"、"个人介绍"、"技能"、"工作经历"、"项目经历"、"匹配分析"。重要：所有字段名(key)请使用中文！"""

    return {
        "系统提示词": system_prompt,
        "用户提示词": user_prompt,
        "状态": "准备就绪",
        "说明": "已从 resume.txt 读取经历内容"
    }


def create_sample_resume():
    """创建示例简历"""
    return {
        "姓名": "张三",
        "联系方式": {
            "邮箱": "zhangsan@example.com",
            "电话": "138-0000-0000"
        },
        "个人介绍": "热爱技术，具有3年软件开发经验，善于团队协作，具备良好的问题解决能力。",
        "技能": [
            "Python", "Java", "JavaScript", "TypeScript", "React", "Vue",
            "Node.js", "Django", "Flask", "MySQL", "PostgreSQL", "MongoDB",
            "Redis", "Docker", "Git", "Linux"
        ],
        "工作经历": [
            {
                "公司": "ABC科技有限公司",
                "职位": "高级Python开发工程师",
                "时间": "2022.01 - 至今",
                "描述": "负责后端服务架构设计与开发，使用Python、Django和Flask框架构建高性能Web应用。参与微服务架构设计，负责核心模块开发。",
                "成就": "优化系统性能，提升API响应速度50%；主导数据库优化，查询效率提升3倍；获得公司年度优秀员工称号。"
            },
            {
                "公司": "XYZ互联网公司",
                "职位": "全栈开发工程师",
                "时间": "2020.06 - 2021.12",
                "描述": "使用React和Node.js开发企业级Web应用，负责前端界面设计和后端API开发。",
                "成就": "独立完成3个核心功能模块开发；参与项目获得公司季度优秀项目奖。"
            }
        ],
        "项目经历": [
            {
                "项目名称": "电商平台后端系统",
                "项目描述": "使用Python和Django开发的电商平台后端，支持高并发访问，包含用户管理、商品管理、订单系统等模块。"
            },
            {
                "项目名称": "实时数据可视化平台",
                "项目描述": "使用React和Node.js构建的实时数据可视化平台，支持多种图表展示。"
            }
        ]
    }
