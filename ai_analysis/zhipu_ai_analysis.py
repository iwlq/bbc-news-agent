import json
from zai import ZhipuAiClient

def analysis_news(news_data):
    # 初始化客户端
    print('初始化客户端')
    client = ZhipuAiClient(api_key="你的api_key")    #填入api_key

    # 打开文件
    # print('读取nwes_data文件')
    # with open('D:/doucument/PythonProject/exercise/general_uv/bbc新闻MostRead自动化/bbc_news.json', 'r', encoding='utf-8') as f:
    #     news_data = json.load(f)

    # 提示词
    user_prompt = f"""
    你是一个具有深刻洞察力的高级国际新闻分析师。请阅读以下我通过爬虫获取的 BBC 新闻 JSON 数据。
    
    【数据说明】：
    数据为 JSON 格式列表，每条数据包含三个字段：
    - title: 新闻英文标题
    - contact: 新闻英文正文
    - url: 新闻来源链接
    
    【原始数据】：
    {news_data}
    
    【你的任务】：
    请严格按照以下要求，对数据进行处理并排版：
    1. 新闻速览：对每一条新闻的核心事件进行极简概括（要求：每条严格限制在一句话，50字以内，直击要害）。
    2. 完整翻译：将原新闻的 `title` 和 `contact` 准确、通顺地翻译成中文，要求符合中文新闻阅读习惯。
    3. 深度解读：基于以上所有新闻内容，跳出单篇报道的局限，进行宏观维度的跨界分析。提炼出 2-3 个全球宏观趋势或深层洞察（如地缘政治博弈、科技对商业的影响、宏观经济预警等）。
    4. 一一对应：速览部分的序号必须与完整翻译部分的序号完全一致，不能遗漏任何一条有效新闻。
    
    【严格输出格式】：
    ——————新闻速览——————
    1. 【概括标题】您的速览内容...
    2. 【概括标题】您的速览内容...
    ...（以此类推）
    
    ——————完整翻译——————
    1. 标题：您的中文标题翻译
       正文：您的中文正文翻译
       (原文链接: 您的url提取)
    
    2. 标题：您的中文标题翻译
       正文：您的中文正文翻译
       (原文链接: 您的url提取)
    ...（以此类推）
    
    ——————首席分析师深度解读——————
    🔴 洞察一：【您的洞察主题名称】
    分析：结合具体的新闻事件，阐述该趋势背后的潜在原因及未来可能的深远影响...
    
    🔴 洞察二：【您的洞察主题名称】
    分析：结合具体的新闻事件，阐述该趋势背后的潜在原因及未来可能的深远影响...
    ...（以此类推，至少2个洞察）
    """

    #提前定义 final_report，防止报错时 return 找不到变量
    final_report = "⚠️ 分析失败，未能生成报告（可能是网络异常或触发了敏感词风控）。"

    try:
        # 调用大模型
        print('正在思考...')
        response = client.chat.completions.create(
            model="glm-4",
            messages=[{"role": "user", "content": user_prompt}]
        )
        print(response.choices[0].message.content)
        final_report = response.choices[0].message.content
    except Exception as e:
        print(e)

    return final_report