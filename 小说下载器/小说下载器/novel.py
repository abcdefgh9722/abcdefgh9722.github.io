import requests
import parsel


def get_response(link):
    """
    发送请求
    :param link: 请求网址
    :return: 响应对象response
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    }
    response = requests.get(url=link, headers=headers)
    response.encoding = response.apparent_encoding
    return response


def get_result(key_word):
    """
    搜索内容
    :param key_word: 剑来
    :return:
    """
    search_url = f'https://www.xbiquwx.la/modules/article/search.php?searchkey={key_word}'
    response = get_response(link=search_url)
    response.encoding = 'utf-8'
    search_data = response.text
    selector = parsel.Selector(search_data)
    name_list = selector.css('.grid .odd a::text').getall()
    href = selector.css('.grid .even a::attr(href)').getall()
    href = [i.split('/')[1] for i in href]
    return name_list, href


def get_novel_url(num_id):
    novel_url = f'https://www.xbiquwx.la/{num_id}/'
    html_data = get_response(novel_url).text
    selector = parsel.Selector(html_data)
    name = selector.css('#info h1::text').get()
    chapter_url_list = selector.css('#list dd a::attr(href)').getall()
    chapter_url_list = [f'https://www.xbiquwx.la/{num_id}/{j}' for j in chapter_url_list]
    return name, chapter_url_list


def get_novel_content(chapter_url):
    response = get_response(chapter_url)
    selector = parsel.Selector(response.text)
    chapter_title = selector.css('.bookname h1::text').get()
    content = '\n'.join(selector.css('#content::text').getall())
    return chapter_title, content


def save(name, title, content):
    with open(name + '.txt', mode='a', encoding='utf-8') as f:
        f.write(title)
        f.write('\n')
        f.write(content)
        f.write('\n')


def main(novel_id):
    name, chapter_url_list = get_novel_url(novel_id)
    for chapter_url in chapter_url_list:
        chapter_title, content = get_novel_content(chapter_url)
        save(name, chapter_title, content)


if __name__ == '__main__':
    url = 'https://www.xbiquwx.la/1_1245/603352.html'
    get_novel_content(url)
