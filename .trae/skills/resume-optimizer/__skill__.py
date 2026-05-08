"""
简历优化技能 - 直接使用LLM进行简历优化
"""
import json
from typing import Dict, Any


def optimize_resume_with_llm(resume_data: Dict[str, Any], jd_text: str) -> Dict[str, Any]:
    """
    使用LLM优化简历
    
    Args:
        resume_data: 原始简历数据（JSON格式）
        jd_text: 岗位JD文字
        
    Returns:
        优化后的简历
    """
    system_prompt = """你是一位专业的简历优化专家，擅长根据岗位JD优化简历。你的任务是：

1. 深度理解岗位JD的核心要求
2. 从用户提供的简历中筛选与岗位JD最匹配的经历
3. 优化技能列表，突出与JD匹配的技能
4. 优化个人介绍，使其更贴合岗位要求
5. 输出一份专业、与JD高度匹配的简历

请以JSON格式输出优化后的简历，保持原有的数据结构，并在根节点添加match_analysis字段说明优化思路。"""

    user_prompt = f"""请根据以下岗位JD优化简历：

【岗位JD】
{jd_text}

【原始简历】
{json.dumps(resume_data, ensure_ascii=False, indent=2)}

请完成以下优化：
1. 筛选与JD最匹配的3-5条工作/实习经历
2. 筛选与JD最匹配的2-3个项目经历
3. 优化技能列表，优先展示与JD匹配的技能（保留10-15个）
4. 优化个人介绍，突出与JD匹配的能力和经验
5. 为每条经历添加匹配度分析

请以JSON格式输出，保持与原始简历相同的结构，并在根节点添加match_analysis字段说明优化思路。"""

    return {
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "status": "ready_for_llm"
    }


def create_sample_resume():
    """创建示例简历"""
    return {
        "name": "张三",
        "contact": {
            "email": "zhangsan@example.com",
            "phone": "138-0000-0000"
        },
        "introduction": "热爱技术，具有3年软件开发经验，善于团队协作，具备良好的问题解决能力。",
        "skills": [
            "Python", "Java", "JavaScript", "TypeScript", "React", "Vue",
            "Node.js", "Django", "Flask", "MySQL", "PostgreSQL", "MongoDB",
            "Redis", "Docker", "Git", "Linux"
        ],
        "experiences": [
            {
                "company": "ABC科技有限公司",
                "position": "高级Python开发工程师",
                "period": "2022.01 - 至今",
                "description": "负责后端服务架构设计与开发，使用Python、Django和Flask框架构建高性能Web应用。参与微服务架构设计，负责核心模块开发。",
                "achievements": "优化系统性能，提升API响应速度50%；主导数据库优化，查询效率提升3倍；获得公司年度优秀员工称号。"
            },
            {
                "company": "XYZ互联网公司",
                "position": "全栈开发工程师",
                "period": "2020.06 - 2021.12",
                "description": "使用React和Node.js开发企业级Web应用，负责前端界面设计和后端API开发。",
                "achievements": "独立完成3个核心功能模块开发；参与项目获得公司季度优秀项目奖。"
            }
        ],
        "projects": [
            {
                "name": "电商平台后端系统",
                "description": "使用Python和Django开发的电商平台后端，支持高并发访问，包含用户管理、商品管理、订单系统等模块。"
            },
            {
                "name": "实时数据可视化平台",
                "description": "使用React和Node.js构建的实时数据可视化平台，支持多种图表展示。"
            }
        ]
    }
