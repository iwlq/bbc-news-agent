from ai_analysis.zhipu_ai_analysis import analysis_news
from crawler.bbc_crawler import get_bbc_news
from notifier.email_sender import send_email

def main():
    print('start！')
    news_list= get_bbc_news()
    report_text =analysis_news(news_list)
    send_email(report_text)

if __name__ == '__main__':
    main()