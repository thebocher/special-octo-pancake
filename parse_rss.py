from lxml import etree

import requests


def parse_item(item):
    item_fields = {
        'title': './title/text()',
        'description': './description/text()',
        'audio': './enclosure[@type="audio/mpeg"]/@url'
    }
    return {
        key: item.xpath(value) for key, value in item_fields.items()
    }

def parse_rss(rss_url):
    xml = requests.get(rss_url).content
    feed = etree.fromstring(xml)
    items = feed.xpath('./channel/item')

    return [
        parse_item(item) for item in items
    ]

if __name__ == '__main__':
    from pprint import pprint
    pprint(parse_rss(
        'https://feeds.soundcloud.com/users/soundcloud:users:164688/sounds.rss',
    ))